import unittest

from tooling.codex.model_benchmark import fixtures
from tooling.codex.model_benchmark import io as bench_io


class ModelBenchmarkFixtureTests(unittest.TestCase):
    def test_fixture_manifest_lists_required_provider_neutrality_corpus(self):
        manifest = fixtures.load_fixture_manifest()

        self.assertEqual(
            set(manifest["fixtures"]),
            {
                "codex_sqlite_minimal_thread",
                "codex_rollout_redacted_stream",
                "manual_run_with_rubric_dimensions",
                "claude_local_jsonl_minimal_structure",
                "provider_denominator_mismatch",
                "malformed_jsonl_fixture",
                "rebuild_parity_fixture_set",
            },
        )
        for fixture_id, entry in manifest["fixtures"].items():
            with self.subTest(fixture_id=fixture_id):
                self.assertTrue(entry["source_kind"])
                self.assertIn(entry["expected_privacy_contract"], fixtures.DEFAULT_SAFE_CONTENT_CONTRACTS)
                self.assertTrue(entry["expected_outputs"])
                self.assertTrue(fixtures.fixture_path(fixture_id).exists())

    def test_default_fixtures_do_not_expose_raw_transcript_fields(self):
        diagnostics = fixtures.lint_default_fixture_privacy()

        self.assertEqual(diagnostics, [])

    def test_claude_shaped_fixture_uses_structural_fields_without_codex_names(self):
        rows = fixtures.read_fixture_jsonl("claude_local_jsonl_minimal_structure", "session.jsonl")
        row_types = {row["record_type"] for row in rows}

        self.assertIn("session", row_types)
        self.assertIn("message", row_types)
        self.assertIn("tool", row_types)
        self.assertIn("sidechain_agent", row_types)
        self.assertIn("parse_diagnostic", row_types)
        self.assertNotIn("response_item", fixtures.flatten_keys(rows))
        self.assertNotIn("turn_context", fixtures.flatten_keys(rows))
        self.assertEqual({row["redaction_state"] for row in rows}, {"synthetic", "redacted"})
        diagnostic = [row for row in rows if row["record_type"] == "parse_diagnostic"][0]
        self.assertEqual(diagnostic["status"], "malformed_source")
        self.assertEqual(diagnostic["line_number"], 4)

    def test_provider_denominator_fixture_preserves_distinct_usage_semantics(self):
        fixture = fixtures.read_fixture_json("provider_denominator_mismatch", "expected_normalized.json")
        observations = fixture["observations"]

        self.assertEqual(observations["openai"]["reasoning_tokens"]["status"], "measured")
        self.assertEqual(observations["anthropic"]["reasoning_tokens"]["status"], "not_exposed")
        self.assertEqual(observations["openai"]["cost"]["cost_evidence_mode"], "provider_reported_per_request")
        self.assertEqual(observations["anthropic"]["cost"]["cost_evidence_mode"], "pricing_table_estimate")
        self.assertEqual(observations["anthropic"]["cache_read_tokens"]["denominator"], "cache_read_input_tokens")
        self.assertEqual(observations["openai"]["cache_read_tokens"]["denominator"], "cached_input_tokens")
        self.assertEqual(observations["anthropic"]["quota"]["status"], "not_collected")

    def test_manual_rubric_fixture_has_dimensions_without_canonical_overall_score(self):
        fixture = fixtures.read_fixture_json("manual_run_with_rubric_dimensions", "manual_run.json")

        self.assertNotIn("score", fixture)
        self.assertEqual(fixture["runtime_provider"], "manual")
        self.assertGreaterEqual(len(fixture["rubric_observations"]), 2)
        for observation in fixture["rubric_observations"]:
            with self.subTest(dimension=observation["dimension_id"]):
                self.assertNotEqual(observation["dimension_id"], "overall")
                self.assertEqual(observation["reliability_mode"], "manual_label")
                self.assertEqual(observation["content_contract"], "derived_features_only")

    def test_malformed_jsonl_fixture_reports_line_number_without_private_content(self):
        path = fixtures.fixture_path("malformed_jsonl_fixture") / "malformed.jsonl"

        with self.assertRaisesRegex(ValueError, r"malformed\.jsonl line 2"):
            bench_io.read_jsonl_objects(path)
        expected = fixtures.read_fixture_json("malformed_jsonl_fixture", "expected_diagnostics.json")
        self.assertEqual(expected["diagnostics"][0]["status"], "malformed_source")
        self.assertEqual(expected["diagnostics"][0]["line_number"], 2)
        self.assertEqual(expected["diagnostics"][0]["content_contract"], "metadata_only")

    def test_rebuild_parity_fixture_set_carries_matching_registry_and_source_hashes(self):
        fixture = fixtures.read_fixture_json("rebuild_parity_fixture_set", "expected_parity.json")
        expected_registry_hash = fixture["registry"]["registry_hash"]
        expected_source_set_hash = fixture["rebuild_run"]["source_set_hash"]

        self.assertEqual(fixture["query_output"]["registry_hash"], expected_registry_hash)
        self.assertEqual(fixture["report_output"]["registry_hash"], expected_registry_hash)
        self.assertEqual(fixture["query_output"]["source_set_hash"], expected_source_set_hash)
        self.assertEqual(fixture["report_output"]["source_set_hash"], expected_source_set_hash)


if __name__ == "__main__":
    unittest.main()
