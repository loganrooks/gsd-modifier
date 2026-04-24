import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import migrate, query, reports, store
from tooling.codex.model_benchmark.enums import COST_EVIDENCE_MODES


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "model_benchmark" / "v0_run_jsonl_compatibility"


class ModelBenchmarkMigrationReportTests(unittest.TestCase):
    def _connect(self) -> sqlite3.Connection:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        conn = store.connect(Path(tmpdir.name) / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _import_fixture(self) -> sqlite3.Connection:
        conn = self._connect()
        migrate.import_v0_run_jsonl(conn, FIXTURE_DIR / "runs.jsonl")
        return conn

    def _source_artifact_id(self, conn: sqlite3.Connection) -> int:
        return store.insert_source_artifact(
            conn,
            {
                "source_kind": "model-benchmark-run/v1-jsonl",
                "source_uri": "fixture://malicious-diagnostic",
                "source_hash": "sha256:" + "0" * 64,
                "content_contract": "metadata_only",
                "provenance_json": {"test": "migration-report"},
            },
        )

    def test_migration_report_counts_v0_compatibility_state(self):
        conn = self._import_fixture()

        report = reports.telemetry_migration_report(conn, strict=True)

        self.assertEqual(report["v0_compatibility_status"], "compatibility_active")
        self.assertEqual(report["counts"]["runs"], 2)
        self.assertEqual(report["counts"]["legacy_score_observations"], 1)
        self.assertEqual(report["counts"]["rubric_observations"], 1)
        self.assertEqual(report["counts"]["source_artifacts"], 1)
        self.assertEqual(report["counts"]["diagnostics"], 0)
        self.assertEqual(report["usage_observation_status_counts"]["measured"], 3)
        self.assertEqual(report["usage_observation_status_counts"]["not_available"], 9)
        self.assertEqual(report["usage_missingness_counts"]["not_applicable"], 3)
        self.assertEqual(report["usage_missingness_counts"]["not_available"], 9)
        self.assertEqual(report["cost_evidence_mode_counts"]["api_equivalent_estimate"], 1)
        self.assertEqual(report["cost_evidence_mode_counts"]["provider_reported_per_request"], 0)
        self.assertEqual(report["cost_evidence_mode_counts"]["provider_reported_aggregate"], 0)
        self.assertEqual(report["cost_evidence_mode_counts"]["pricing_table_estimate"], 0)
        self.assertEqual(report["cost_evidence_mode_counts"]["manual_cost_entry"], 0)
        self.assertEqual(set(report["cost_evidence_mode_counts"]), COST_EVIDENCE_MODES)
        self.assertEqual(report["registry_hash"], "not_collected")
        self.assertEqual(report["source_set_hash"], "not_collected")

    def test_query_surface_exposes_source_hashes_and_diagnostics(self):
        conn = self._connect()
        import_result = migrate.import_v0_run_jsonl(conn, FIXTURE_DIR / "malformed.jsonl")

        state = query.query_migration_state(conn, strict=True)

        self.assertEqual(state["v0_compatibility_status"], "compatibility_active")
        self.assertEqual(state["counts"]["source_artifacts"], 1)
        self.assertEqual(state["counts"]["diagnostics"], import_result["diagnostic_count"])
        self.assertRegex(state["source_artifacts"][0]["source_hash"], r"^sha256:[0-9a-f]{64}$")
        self.assertEqual(state["source_artifacts"][0]["content_contract"], "metadata_only")
        self.assertEqual(state["registry_hash"], "not_collected")
        self.assertEqual(state["source_set_hash"], "not_collected")

    def test_migration_report_does_not_emit_raw_private_content(self):
        conn = self._connect()
        raw_record = {
            "run_id": "v0-run-private",
            "task_id": "TASK-PRIVATE",
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
            "telemetry_features": {
                "trace_id": "trace-private",
                "prompt": "PRIVATE PROMPT",
                "assistant": "PRIVATE ASSISTANT",
                "tool_arguments": "PRIVATE TOOL ARGUMENTS",
                "tool_result": "PRIVATE TOOL RESULT",
                "transcript": "PRIVATE TRANSCRIPT",
            },
        }
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "runs.jsonl"
        path.write_text(json.dumps(raw_record, sort_keys=True) + "\n", encoding="utf-8")
        migrate.import_v0_run_jsonl(conn, path)

        serialized_report = json.dumps(reports.telemetry_migration_report(conn, strict=True), sort_keys=True)

        self.assertNotIn("PRIVATE PROMPT", serialized_report)
        self.assertNotIn("PRIVATE ASSISTANT", serialized_report)
        self.assertNotIn("PRIVATE TOOL ARGUMENTS", serialized_report)
        self.assertNotIn("PRIVATE TOOL RESULT", serialized_report)
        self.assertNotIn("PRIVATE TRANSCRIPT", serialized_report)

    def test_migration_report_sanitizes_persisted_diagnostic_payloads(self):
        conn = self._connect()
        source_artifact_id = self._source_artifact_id(conn)
        store.insert_observation(
            conn,
            {
                "entity_type": "source_artifact",
                "entity_id": str(source_artifact_id),
                "metric_id": "source.parse_status",
                "status": "malformed_source",
                "evidence_class": "local_observed",
                "reliability_mode": "direct_field",
                "content_contract": "metadata_only",
                "comparability": "not_comparable",
                "source_artifact_id": source_artifact_id,
                "value_json": {
                    "status": "malformed_source",
                    "line_number": 7,
                    "error_type": "schema_validation_failed",
                    "content_contract": "metadata_only",
                    "prompt": "PRIVATE PROMPT FROM DIAGNOSTIC",
                    "assistant": "PRIVATE ASSISTANT FROM DIAGNOSTIC",
                    "tool_result": "PRIVATE TOOL RESULT FROM DIAGNOSTIC",
                    "transcript": "PRIVATE TRANSCRIPT FROM DIAGNOSTIC",
                },
                "provenance_json": {"test": "migration-report"},
            },
        )

        serialized_report = json.dumps(reports.telemetry_migration_report(conn, strict=True), sort_keys=True)
        serialized_query = json.dumps(query.query_migration_state(conn, strict=True), sort_keys=True)

        for serialized in (serialized_report, serialized_query):
            self.assertIn("schema_validation_failed", serialized)
            self.assertNotIn("PRIVATE PROMPT FROM DIAGNOSTIC", serialized)
            self.assertNotIn("PRIVATE ASSISTANT FROM DIAGNOSTIC", serialized)
            self.assertNotIn("PRIVATE TOOL RESULT FROM DIAGNOSTIC", serialized)
            self.assertNotIn("PRIVATE TRANSCRIPT FROM DIAGNOSTIC", serialized)

    def test_strict_query_rejects_invalid_observation_enum_values(self):
        conn = self._import_fixture()
        conn.execute(
            "UPDATE observations SET status = ? WHERE metric_id = ?",
            ("locally_true", "usage.input_tokens"),
        )
        conn.commit()

        with self.assertRaisesRegex(ValueError, "status"):
            query.query_migration_state(conn, strict=True)

    def test_strict_query_rejects_invalid_cost_evidence_mode_values(self):
        conn = self._import_fixture()
        conn.execute(
            "UPDATE cost_estimates SET cost_evidence_mode = ?",
            ("provider_invoice_maybe",),
        )
        conn.commit()

        with self.assertRaisesRegex(ValueError, "cost_evidence_mode"):
            reports.telemetry_migration_report(conn, strict=True)

    def test_strict_query_rejects_invalid_usage_payload_missingness_values(self):
        conn = self._import_fixture()
        row = conn.execute(
            "SELECT id, value_json FROM observations WHERE metric_id = ? LIMIT 1",
            ("usage.input_tokens",),
        ).fetchone()
        payload = json.loads(row["value_json"])
        payload["missingness"] = "maybe_measured"
        payload["availability_status"] = "maybe_measured"
        conn.execute(
            "UPDATE observations SET value_json = ? WHERE id = ?",
            (json.dumps(payload, sort_keys=True), row["id"]),
        )
        conn.commit()

        with self.assertRaisesRegex(ValueError, "missingness"):
            query.query_migration_state(conn, strict=True)

    def test_migration_report_does_not_attribute_unrelated_rebuild_hashes(self):
        conn = self._import_fixture()
        store.insert_rebuild_run(
            conn,
            {
                "schema_version": "model-benchmark-store/v1",
                "registry_version": "unrelated",
                "registry_hash": "sha256:" + "1" * 64,
                "source_set_hash": "sha256:" + "2" * 64,
                "status": "completed",
                "provenance_json": {"test": "unrelated-rebuild"},
            },
        )

        report = reports.telemetry_migration_report(conn, strict=True)

        self.assertEqual(report["registry_hash"], "not_collected")
        self.assertEqual(report["source_set_hash"], "not_collected")


if __name__ == "__main__":
    unittest.main()
