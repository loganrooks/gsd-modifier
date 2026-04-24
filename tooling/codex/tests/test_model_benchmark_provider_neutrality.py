import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import fixtures, manifest, query, rebuild, store


class ModelBenchmarkProviderNeutralityTests(unittest.TestCase):
    def _connect(self) -> sqlite3.Connection:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        conn = store.connect(Path(tmpdir.name) / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _registry(self) -> dict:
        source_kinds = [
            "benchmark.manual_run",
            "runtime.claude_code.local_jsonl",
            "provider.usage_fixture",
            "runtime.codex_cli.rollout_stream",
        ]
        metrics = [
            ("source.parse_status", "malformed_source", "synthetic_fixture", "direct_field", "metadata_only", "not_applicable", "not_comparable"),
            ("runtime.redaction_state", "measured", "synthetic_fixture", "local_structural_field", "structural_only", "not_applicable", "surface_semantics_differ"),
            ("tokens.input", "measured", "synthetic_fixture", "provider_emitted", "metadata_only", "not_applicable", "provider_semantics_differ"),
            ("tokens.cache_read", "measured", "synthetic_fixture", "provider_emitted", "metadata_only", "not_applicable", "provider_semantics_differ"),
            ("tokens.reasoning", "measured", "synthetic_fixture", "provider_emitted", "metadata_only", "not_exposed", "provider_semantics_differ"),
            ("cost.total", "measured", "synthetic_fixture", "provider_emitted", "metadata_only", "provider_reported_per_request", "provider_semantics_differ"),
            ("quota.status", "not_collected", "synthetic_fixture", "provider_emitted", "metadata_only", "not_applicable", "provider_semantics_differ"),
        ]
        return manifest.validate_manifest(
            {
                "schema_version": manifest.SCHEMA_VERSION,
                "registry_id": "fixture.provider_neutrality",
                "registry_version": "2026.04.24-task06",
                "source_kinds": [{"id": source_kind} for source_kind in source_kinds],
                "namespaces": [
                    {"id": "benchmark.manual"},
                    {"id": "runtime.claude_code"},
                    {"id": "provider.openai"},
                    {"id": "provider.anthropic"},
                    {"id": "runtime.codex_cli"},
                ],
                "predicates": [
                    {"id": "run.has_rubric_observation"},
                    {"id": "source.has_diagnostic"},
                    {"id": "source.has_redaction_state"},
                    {"id": "provider.has_usage_evidence"},
                ],
                "metrics": [
                    {
                        "id": metric_id,
                        "status": status,
                        "evidence_class": evidence_class,
                        "reliability_mode": reliability_mode,
                        "content_contract": content_contract,
                        "cost_evidence_mode": cost_mode,
                        "comparability": comparability,
                    }
                    for (
                        metric_id,
                        status,
                        evidence_class,
                        reliability_mode,
                        content_contract,
                        cost_mode,
                        comparability,
                    ) in metrics
                ],
                "rubrics": [
                    {"id": "quality.task_boundary", "dimensions": [{"id": "follows_task_boundary"}]},
                    {"id": "quality.auditability", "dimensions": [{"id": "records_verification"}]},
                ],
                "emits": [
                    {
                        "source_kind": source_kind,
                        "namespace": "benchmark.manual",
                        "predicate": "run.has_rubric_observation",
                        "rubric_id": "quality.task_boundary",
                        "status": "measured",
                        "reliability_mode": "manual_label",
                        "content_contract": "derived_features_only",
                    }
                    for source_kind in source_kinds
                ],
            }
        )

    def _gate_sources(self) -> list[Path]:
        return [
            fixtures.fixture_path("manual_run_with_rubric_dimensions") / "manual_run.json",
            fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl",
            fixtures.fixture_path("provider_denominator_mismatch") / "expected_normalized.json",
        ]

    def _named_gate_sources(
        self,
        root: Path,
        *,
        manual_payload: dict,
        claude_jsonl: str,
        provider_payload: dict,
    ) -> list[Path]:
        manual_dir = root / "manual_run_with_rubric_dimensions"
        claude_dir = root / "claude_local_jsonl_minimal_structure"
        provider_dir = root / "provider_denominator_mismatch"
        manual_dir.mkdir()
        claude_dir.mkdir()
        provider_dir.mkdir()

        manual_path = manual_dir / "manual_run.json"
        claude_path = claude_dir / "session.jsonl"
        provider_path = provider_dir / "expected_normalized.json"
        manual_path.write_text(json.dumps(manual_payload), encoding="utf-8")
        claude_path.write_text(claude_jsonl, encoding="utf-8")
        provider_path.write_text(json.dumps(provider_payload), encoding="utf-8")
        return [manual_path, claude_path, provider_path]

    def test_provider_neutrality_gate_requires_strict_rebuild_and_query_validation(self):
        conn = self._connect()
        registry = self._registry()

        rebuild_result = rebuild.rebuild_provider_neutrality_gate(
            conn,
            registry,
            self._gate_sources(),
            strict=True,
        )
        gate = query.query_provider_neutrality_gate(
            conn,
            registry_hash=registry["registry_hash"],
            strict=True,
        )

        self.assertEqual(rebuild_result["registry_hash"], registry["registry_hash"])
        self.assertEqual(gate["registry_hash"], registry["registry_hash"])
        self.assertEqual(gate["source_set_hash"], rebuild_result["source_set_hash"])
        self.assertEqual(gate["provider_neutrality_gate"]["status"], "passed")
        self.assertNotIn("provider_neutrality_claim", gate)
        self.assertNotIn("score.overall", json.dumps(gate, sort_keys=True))

    def test_correctly_named_empty_gate_sources_do_not_pass_without_required_evidence(self):
        conn = self._connect()
        registry = self._registry()
        with tempfile.TemporaryDirectory() as tmpdir:
            sources = self._named_gate_sources(
                Path(tmpdir),
                manual_payload={"run_id": "empty-manual", "rubric_observations": []},
                claude_jsonl="",
                provider_payload={"observations": {}},
            )

            rebuild_result = rebuild.rebuild_provider_neutrality_gate(conn, registry, sources, strict=True)
            gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        self.assertEqual(rebuild_result["provider_neutrality_gate"]["status"], "not_passed")
        self.assertEqual(gate["provider_neutrality_gate"]["status"], "not_passed")
        required_evidence = gate["provider_neutrality_gate"]["required_evidence"]
        self.assertEqual(required_evidence["manual_run_with_rubric_dimensions"]["status"], "missing_evidence")
        self.assertEqual(required_evidence["claude_local_jsonl_minimal_structure"]["status"], "missing_evidence")
        self.assertEqual(required_evidence["provider_denominator_mismatch"]["status"], "missing_evidence")

    def test_correctly_named_minimal_sources_do_not_pass_when_any_required_evidence_is_absent(self):
        registry = self._registry()
        cases = [
            (
                "manual_without_rubrics",
                {"run_id": "empty-manual", "rubric_observations": []},
                (fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl").read_text(encoding="utf-8"),
                json.loads((fixtures.fixture_path("provider_denominator_mismatch") / "expected_normalized.json").read_text(encoding="utf-8")),
                "manual_run_with_rubric_dimensions",
            ),
            (
                "claude_without_items_or_diagnostics",
                json.loads((fixtures.fixture_path("manual_run_with_rubric_dimensions") / "manual_run.json").read_text(encoding="utf-8")),
                "",
                json.loads((fixtures.fixture_path("provider_denominator_mismatch") / "expected_normalized.json").read_text(encoding="utf-8")),
                "claude_local_jsonl_minimal_structure",
            ),
            (
                "provider_without_usage_observations",
                json.loads((fixtures.fixture_path("manual_run_with_rubric_dimensions") / "manual_run.json").read_text(encoding="utf-8")),
                (fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl").read_text(encoding="utf-8"),
                {"observations": {}},
                "provider_denominator_mismatch",
            ),
        ]
        for name, manual_payload, claude_jsonl, provider_payload, missing_fixture in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmpdir:
                conn = self._connect()
                sources = self._named_gate_sources(
                    Path(tmpdir),
                    manual_payload=manual_payload,
                    claude_jsonl=claude_jsonl,
                    provider_payload=provider_payload,
                )

                rebuild.rebuild_provider_neutrality_gate(conn, registry, sources, strict=True)
                gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

                self.assertEqual(gate["provider_neutrality_gate"]["status"], "not_passed")
                self.assertEqual(
                    gate["provider_neutrality_gate"]["required_evidence"][missing_fixture]["status"],
                    "missing_evidence",
                )

    def test_latest_forged_gate_without_source_artifact_mapping_cannot_reuse_stale_evidence(self):
        conn = self._connect()
        registry = self._registry()

        rebuild_result = rebuild.rebuild_provider_neutrality_gate(
            conn,
            registry,
            self._gate_sources(),
            strict=True,
        )
        self.assertEqual(rebuild_result["provider_neutrality_gate"]["status"], "passed")

        store.insert_rebuild_run(
            conn,
            {
                "schema_version": store.SCHEMA_VERSION,
                "registry_version": registry["registry_version"],
                "registry_hash": registry["registry_hash"],
                "source_set_hash": rebuild_result["source_set_hash"],
                "status": "completed",
                "completed_at": "1970-01-01T00:00:00Z",
                "provenance_json": {
                    "provider_neutrality_gate": True,
                    "gate_status": "passed",
                    "fixture_ids": sorted(rebuild.PROVIDER_NEUTRALITY_REQUIRED_FIXTURES),
                },
            },
        )

        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        self.assertEqual(gate["provider_neutrality_gate"]["status"], "not_passed")
        self.assertEqual(gate["provider_neutrality_gate"]["source_artifact_ids_by_fixture"], {})
        self.assertEqual(gate["rubric_observations"], [])
        self.assertEqual(gate["runtime_response_items"], [])
        self.assertEqual(gate["provider_usage_evidence"], {})
        for evidence in gate["provider_neutrality_gate"]["required_evidence"].values():
            self.assertEqual(evidence["status"], "missing_evidence")

    def test_latest_forged_gate_with_wrong_source_artifact_mapping_cannot_reuse_stale_evidence(self):
        conn = self._connect()
        registry = self._registry()

        rebuild_result = rebuild.rebuild_provider_neutrality_gate(
            conn,
            registry,
            self._gate_sources(),
            strict=True,
        )
        source_artifacts = rebuild_result["source_artifact_ids_by_fixture"]
        wrong_mapping = {
            "manual_run_with_rubric_dimensions": source_artifacts["provider_denominator_mismatch"],
            "claude_local_jsonl_minimal_structure": source_artifacts["manual_run_with_rubric_dimensions"],
            "provider_denominator_mismatch": source_artifacts["claude_local_jsonl_minimal_structure"],
        }
        store.insert_rebuild_run(
            conn,
            {
                "schema_version": store.SCHEMA_VERSION,
                "registry_version": registry["registry_version"],
                "registry_hash": registry["registry_hash"],
                "source_set_hash": rebuild_result["source_set_hash"],
                "status": "completed",
                "completed_at": "1970-01-01T00:00:00Z",
                "provenance_json": {
                    "provider_neutrality_gate": True,
                    "gate_status": "passed",
                    "fixture_ids": sorted(rebuild.PROVIDER_NEUTRALITY_REQUIRED_FIXTURES),
                    "source_artifact_ids_by_fixture": wrong_mapping,
                },
            },
        )

        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        self.assertEqual(gate["provider_neutrality_gate"]["status"], "not_passed")
        self.assertEqual(gate["provider_neutrality_gate"]["source_artifact_ids_by_fixture"], wrong_mapping)
        for evidence in gate["provider_neutrality_gate"]["required_evidence"].values():
            self.assertEqual(evidence["status"], "missing_evidence")

    def test_manual_rubric_fixture_round_trips_without_canonical_overall_score(self):
        conn = self._connect()
        registry = self._registry()
        rebuild.rebuild_provider_neutrality_gate(conn, registry, self._gate_sources(), strict=True)

        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        rubric_dimensions = {(row["rubric_id"], row["dimension_id"]) for row in gate["rubric_observations"]}
        self.assertIn(("quality.task_boundary", "follows_task_boundary"), rubric_dimensions)
        self.assertIn(("quality.auditability", "records_verification"), rubric_dimensions)
        self.assertFalse(any(row["dimension_id"] == "overall" for row in gate["rubric_observations"]))

    def test_claude_fixture_parses_without_codex_fields_and_preserves_redaction_diagnostics(self):
        conn = self._connect()
        registry = self._registry()
        rebuild.rebuild_provider_neutrality_gate(conn, registry, self._gate_sources(), strict=True)

        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)
        encoded_items = json.dumps(gate["runtime_response_items"], sort_keys=True)

        self.assertNotIn("response_item", encoded_items)
        self.assertNotIn("turn_context", encoded_items)
        self.assertEqual({item["runtime_namespace"] for item in gate["runtime_response_items"]}, {"runtime.claude_code"})
        self.assertEqual({item["redaction_state"] for item in gate["runtime_response_items"]}, {"synthetic", "redacted"})
        self.assertEqual(gate["diagnostics"][0]["status"], "malformed_source")
        self.assertEqual(gate["diagnostics"][0]["line_number"], 4)
        self.assertEqual(gate["diagnostics"][0]["content_contract"], "metadata_only")

    def test_provider_denominator_mismatch_keeps_usage_cost_and_quota_axes_separate(self):
        conn = self._connect()
        registry = self._registry()
        rebuild.rebuild_provider_neutrality_gate(conn, registry, self._gate_sources(), strict=True)

        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)
        usage = gate["provider_usage_evidence"]

        self.assertEqual(usage["openai"]["cache_read_tokens"]["denominator"], "cached_input_tokens")
        self.assertEqual(usage["anthropic"]["cache_read_tokens"]["denominator"], "cache_read_input_tokens")
        self.assertEqual(usage["openai"]["reasoning_tokens"]["status"], "measured")
        self.assertEqual(usage["anthropic"]["reasoning_tokens"]["status"], "not_exposed")
        self.assertEqual(usage["openai"]["cost"]["cost_evidence_mode"], "provider_reported_per_request")
        self.assertEqual(usage["anthropic"]["cost"]["cost_evidence_mode"], "pricing_table_estimate")
        self.assertEqual(usage["openai"]["quota"]["status"], "not_exposed")
        self.assertEqual(usage["anthropic"]["quota"]["status"], "not_collected")

    def test_codex_only_fixture_cannot_set_provider_neutrality_flag_or_claim(self):
        conn = self._connect()
        registry = self._registry()
        rebuild.rebuild_provider_neutrality_gate(
            conn,
            registry,
            [fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"],
            strict=True,
        )

        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        self.assertEqual(gate["provider_neutrality_gate"]["status"], "not_passed")
        self.assertNotIn("provider_neutrality_claim", gate)
        self.assertNotIn("provider_neutral", gate)

    def test_gate_fails_if_strict_manifest_rebuild_or_query_hash_validation_is_bypassed(self):
        registry = self._registry()
        invalid_registry = json.loads(json.dumps(registry))
        invalid_registry["source_kinds"] = [
            entry for entry in invalid_registry["source_kinds"] if entry["id"] != "provider.usage_fixture"
        ]
        invalid_registry.pop("registry_hash", None)
        with self.assertRaisesRegex(ValueError, "undeclared source_kind"):
            rebuild.rebuild_provider_neutrality_gate(
                self._connect(),
                invalid_registry,
                self._gate_sources(),
                strict=True,
            )

        conn = self._connect()
        rebuild.rebuild_provider_neutrality_gate(conn, registry, self._gate_sources(), strict=True)
        conn.execute("UPDATE rebuild_runs SET source_set_hash = ''")
        conn.commit()
        with self.assertRaisesRegex(ValueError, "source_set_hash"):
            query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        with self.assertRaisesRegex(ValueError, "registry_hash mismatch"):
            query.query_provider_neutrality_gate(conn, registry_hash="sha256:not-the-registry", strict=True)


if __name__ == "__main__":
    unittest.main()
