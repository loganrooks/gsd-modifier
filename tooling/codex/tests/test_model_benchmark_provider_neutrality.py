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
