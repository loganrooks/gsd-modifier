import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import migrate, store


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "model_benchmark" / "v0_run_jsonl_compatibility"


class ModelBenchmarkMigrateTests(unittest.TestCase):
    def _connect(self) -> sqlite3.Connection:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        conn = store.connect(Path(tmpdir.name) / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _write_jsonl(self, row: dict) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "runs.jsonl"
        path.write_text(json.dumps(row, sort_keys=True) + "\n", encoding="utf-8")
        return path

    def _run_record(self, **overrides) -> dict:
        record = {
            "run_id": "v0-run-raw-fields",
            "task_id": "TASK-RAW",
            "candidate_profile": "55-medium",
            "model": "gpt-5.5",
            "reasoning_effort": "medium",
            "runtime_provider": "codex_cli",
            "status": "completed",
            "usage": {
                "input_tokens": 10,
                "cached_input_tokens": "not_available",
                "output_tokens": 5,
                "reasoning_tokens": "not_available",
                "initialization_tokens": "not_available",
                "tool_result_tokens": "not_available",
                "usage_metric_status": "measured",
            },
        }
        record.update(overrides)
        return record

    def _persisted_store_text(self, conn: sqlite3.Connection) -> str:
        chunks = []
        for table, columns in (
            ("source_artifacts", ("provenance_json",)),
            ("runs", ("run_json", "provenance_json")),
            ("observations", ("value_json", "provenance_json")),
            ("rubric_observations", ("value_json", "provenance_json")),
            ("cost_estimates", ("cost_json", "provenance_json")),
        ):
            for row in conn.execute(f"SELECT {', '.join(columns)} FROM {table}").fetchall():
                chunks.extend(str(value) for value in row)
        return "\n".join(chunks)

    def test_import_v0_run_jsonl_populates_store_without_collapsing_compatibility(self):
        conn = self._connect()

        result = migrate.import_v0_run_jsonl(conn, FIXTURE_DIR / "runs.jsonl")

        self.assertEqual(result["runs"], 2)
        self.assertEqual(result["rubric_observations"], 1)
        self.assertEqual(result["legacy_score_observations"], 1)
        self.assertEqual(result["cost_estimates"], 1)
        self.assertEqual(result["skipped_records"], 0)
        self.assertEqual(result["diagnostics"], [])
        self.assertGreaterEqual(result["observations"], 13)

        run_count = conn.execute("SELECT COUNT(*) AS count FROM runs").fetchone()["count"]
        observation_count = conn.execute("SELECT COUNT(*) AS count FROM observations").fetchone()["count"]
        self.assertEqual(run_count, 2)
        self.assertEqual(observation_count, result["observations"])

        legacy = conn.execute(
            "SELECT metric_id, status, reliability_mode, comparability, value_json, provenance_json "
            "FROM observations WHERE metric_id = ?",
            ("legacy.score.overall",),
        ).fetchone()
        self.assertIsNotNone(legacy)
        self.assertEqual(legacy["status"], "measured")
        self.assertEqual(legacy["reliability_mode"], "manual_label")
        self.assertEqual(legacy["comparability"], "not_comparable")
        self.assertEqual(json.loads(legacy["value_json"])["value"], 3.25)
        self.assertEqual(json.loads(legacy["provenance_json"])["compatibility"], "compatibility_only")

        rubric = conn.execute(
            "SELECT rubric_id, dimension_id, value_json, provenance_json FROM rubric_observations"
        ).fetchone()
        self.assertEqual(rubric["rubric_id"], "quality.task_boundary")
        self.assertEqual(rubric["dimension_id"], "follows_task_boundary")
        rubric_provenance = json.loads(rubric["provenance_json"])
        self.assertEqual(rubric_provenance["evaluator_id"], "fixture.manual-reviewer")
        self.assertEqual(rubric_provenance["rubric_version"], "2026.04.24")

        missing_usage = conn.execute(
            "SELECT status, value_json FROM observations "
            "WHERE entity_id = ? AND metric_id = ?",
            ("v0-run-001", "usage.reasoning_tokens"),
        ).fetchone()
        self.assertEqual(missing_usage["status"], "not_available")
        self.assertEqual(json.loads(missing_usage["value_json"])["value"], "not_available")

        measured_usage = conn.execute(
            "SELECT status, value_json FROM observations "
            "WHERE entity_id = ? AND metric_id = ?",
            ("v0-run-001", "usage.input_tokens"),
        ).fetchone()
        self.assertEqual(measured_usage["status"], "measured")
        self.assertEqual(json.loads(measured_usage["value_json"])["value"], 1200)
        self.assertEqual(json.loads(measured_usage["value_json"])["availability_status"], "measured")

        cost = conn.execute("SELECT cost_evidence_mode, comparability, cost_json FROM cost_estimates").fetchone()
        self.assertEqual(cost["cost_evidence_mode"], "api_equivalent_estimate")
        self.assertEqual(cost["comparability"], "comparable_with_caveat")
        self.assertIn("API-equivalent estimate", json.loads(cost["cost_json"])["caveat"])

        artifact = conn.execute(
            "SELECT source_uri, source_hash, content_contract, provenance_json FROM source_artifacts"
        ).fetchone()
        self.assertTrue(artifact["source_uri"].endswith("runs.jsonl"))
        self.assertRegex(artifact["source_hash"], r"^sha256:[0-9a-f]{64}$")
        self.assertEqual(artifact["content_contract"], "metadata_only")
        artifact_provenance = json.loads(artifact["provenance_json"])
        self.assertEqual(artifact_provenance["content_contract"], "metadata_only")
        self.assertNotIn("raw_content", artifact_provenance)

    def test_malformed_v0_records_emit_metadata_only_diagnostics(self):
        conn = self._connect()

        result = migrate.import_v0_run_jsonl(conn, FIXTURE_DIR / "malformed.jsonl")

        self.assertEqual(result["runs"], 1)
        self.assertEqual(result["skipped_records"], 1)
        self.assertEqual(result["diagnostic_count"], 1)
        self.assertGreaterEqual(result["observations"], 7)
        diagnostic = result["diagnostics"][0]
        self.assertEqual(diagnostic["line_number"], 2)
        self.assertEqual(diagnostic["status"], "malformed_source")
        self.assertEqual(diagnostic["content_contract"], "metadata_only")
        self.assertNotIn("raw_content", diagnostic)
        self.assertNotIn("broken", json.dumps(diagnostic, sort_keys=True))

        persisted = "\n".join(
            row[0]
            for table, column in (
                ("source_artifacts", "provenance_json"),
                ("observations", "value_json"),
                ("observations", "provenance_json"),
            )
            for row in conn.execute(f"SELECT {column} FROM {table}").fetchall()
        )
        self.assertNotIn("TASK-BAD", persisted)
        self.assertNotIn("broken", persisted)

        persisted_diagnostic = conn.execute(
            "SELECT status, metric_id, value_json, provenance_json FROM observations "
            "WHERE status = ? AND metric_id = ?",
            ("malformed_source", "source.parse_status"),
        ).fetchone()
        self.assertIsNotNone(persisted_diagnostic)
        self.assertEqual(json.loads(persisted_diagnostic["value_json"])["line_number"], 2)
        self.assertNotIn("raw_content", persisted_diagnostic["value_json"])
        self.assertNotIn("TASK-BAD", persisted_diagnostic["value_json"])
        self.assertNotIn("broken", persisted_diagnostic["provenance_json"])

    def test_import_sanitizes_raw_looking_fields_from_valid_v0_records(self):
        conn = self._connect()
        raw_record = self._run_record(
            telemetry_features={
                "trace_id": "trace-raw",
                "agent_role": "executor",
                "intervention_id": "intervention-raw",
                "metric_granularity": "run",
                "provenance": "fixture",
                "derived_feature_version": "v1",
                "prompt": "PRIVATE PROMPT SHOULD NOT PERSIST",
                "nested": {"assistant_text": "PRIVATE ASSISTANT SHOULD NOT PERSIST"},
            },
            rubric_observations=[
                {
                    "rubric_id": "quality.task_boundary",
                    "dimension_id": "follows_task_boundary",
                    "evaluator_id": "fixture.manual-reviewer",
                    "rubric_version": "2026.04.24",
                    "value": 1,
                    "status": "measured",
                    "evidence_class": "manual_evidence",
                    "reliability_mode": "manual_label",
                    "content_contract": "derived_features_only",
                    "comparability": "partial",
                    "provenance": {
                        "source": "synthetic_fixture",
                        "prompt_excerpt": "PRIVATE RUBRIC PROMPT SHOULD NOT PERSIST",
                        "tool_result": {"text": "PRIVATE TOOL RESULT SHOULD NOT PERSIST"},
                    },
                }
            ],
            cost_estimate={
                "estimate_status": "estimated",
                "model": "gpt-5.5",
                "currency": "USD",
                "source_url": "https://example.test/pricing",
                "retrieved_at": "2026-04-24T00:00:00Z",
                "effective_date": "2026-04-24",
                "total_estimated_cost": "0.000060",
                "line_items": [
                    {
                        "token_field": "input_tokens",
                        "tokens": 10,
                        "rate_per_million": "1.00",
                        "estimated_cost": "0.000010",
                        "assistant_text": "PRIVATE COST FIELD SHOULD NOT PERSIST",
                    }
                ],
                "raw_response": {"content": "PRIVATE COST RAW RESPONSE SHOULD NOT PERSIST"},
                "caveat": "API-equivalent estimate only; not direct ChatGPT or Codex plan quota burn.",
            },
        )

        migrate.import_v0_run_jsonl(conn, self._write_jsonl(raw_record))

        persisted = self._persisted_store_text(conn)
        self.assertNotIn("PRIVATE PROMPT SHOULD NOT PERSIST", persisted)
        self.assertNotIn("PRIVATE ASSISTANT SHOULD NOT PERSIST", persisted)
        self.assertNotIn("PRIVATE RUBRIC PROMPT SHOULD NOT PERSIST", persisted)
        self.assertNotIn("PRIVATE TOOL RESULT SHOULD NOT PERSIST", persisted)
        self.assertNotIn("PRIVATE COST FIELD SHOULD NOT PERSIST", persisted)
        self.assertNotIn("PRIVATE COST RAW RESPONSE SHOULD NOT PERSIST", persisted)
        self.assertIn("trace-raw", persisted)
        self.assertIn("fixture.manual-reviewer", persisted)
        self.assertIn("0.000060", persisted)

    def test_estimated_integer_usage_observation_payload_does_not_claim_measured_missingness(self):
        conn = self._connect()
        path = self._write_jsonl(
            self._run_record(
                usage={
                    "input_tokens": 10,
                    "cached_input_tokens": "not_available",
                    "output_tokens": 5,
                    "reasoning_tokens": "not_available",
                    "initialization_tokens": "not_available",
                    "tool_result_tokens": "not_available",
                    "usage_metric_status": "estimated",
                }
            )
        )

        migrate.import_v0_run_jsonl(conn, path)

        row = conn.execute(
            "SELECT status, value_json FROM observations "
            "WHERE entity_id = ? AND metric_id = ?",
            ("v0-run-raw-fields", "usage.input_tokens"),
        ).fetchone()
        payload = json.loads(row["value_json"])
        self.assertEqual(row["status"], "estimated")
        self.assertEqual(payload["availability_status"], "estimated")
        self.assertNotEqual(payload.get("missingness"), "measured")


if __name__ == "__main__":
    unittest.main()
