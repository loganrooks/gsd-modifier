import sqlite3
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import store


MINIMUM_TABLES = {
    "source_artifacts",
    "task_definitions",
    "task_instances",
    "runs",
    "sessions",
    "turns",
    "runtime_response_items",
    "model_calls",
    "tool_calls",
    "entity_edges",
    "observations",
    "rubric_observations",
    "cost_estimates",
    "registries",
    "rebuild_runs",
}


class ModelBenchmarkStoreTests(unittest.TestCase):
    def _connect(self) -> sqlite3.Connection:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        conn = store.connect(Path(tmpdir.name) / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _columns(self, conn: sqlite3.Connection, table: str) -> dict[str, sqlite3.Row]:
        rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
        return {row["name"]: row for row in rows}

    def _insert_source_artifact(self, conn: sqlite3.Connection) -> int:
        return store.insert_source_artifact(
            conn,
            {
                "source_kind": "fixture.jsonl",
                "source_uri": "fixtures/run.jsonl",
                "source_hash": "sha256:artifact",
                "content_contract": "metadata_only",
                "provenance_json": {"created_by": "unit-test"},
            },
        )

    def _runtime_item(self, source_artifact_id: int, **overrides):
        item = {
            "session_id": None,
            "turn_id": None,
            "model_call_id": None,
            "source_artifact_id": source_artifact_id,
            "source_kind": "fixture.jsonl",
            "provider_namespace": "runtime.codex_cli",
            "runtime_namespace": "codex.local",
            "item_type": "assistant_message",
            "status": "completed",
            "role": "assistant",
            "redaction_state": "metadata_only",
            "content_state": "content_hash_or_length_only",
            "correlation_status": "uncorrelated",
            "payload_json": {"runtime.codex_cli": {"item_id": "item-1"}},
            "provenance_json": {"line": 1},
        }
        item.update(overrides)
        return item

    def _observation(self, source_artifact_id: int, **overrides):
        observation = {
            "entity_type": "run",
            "entity_id": "run-001",
            "metric_id": "tokens.input",
            "status": "measured",
            "evidence_class": "synthetic_fixture",
            "reliability_mode": "direct_field",
            "content_contract": "metadata_only",
            "source_artifact_id": source_artifact_id,
            "value_json": {"value": 100},
            "provenance_json": {"line": 1},
            "comparability": "comparable",
        }
        observation.update(overrides)
        return observation

    def test_store_initializes_minimum_tables_without_required_telemetry_events(self):
        conn = self._connect()

        tables = {
            row["name"]
            for row in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
        }

        self.assertTrue(MINIMUM_TABLES.issubset(tables))
        self.assertNotIn("telemetry_events", tables)

    def test_store_records_schema_version(self):
        conn = self._connect()

        self.assertEqual(store.schema_version(conn), store.SCHEMA_VERSION)

    def test_runtime_response_items_model_call_id_is_nullable(self):
        conn = self._connect()

        columns = self._columns(conn, "runtime_response_items")

        self.assertEqual(columns["model_call_id"]["notnull"], 0)

    def test_runtime_response_items_require_core_provider_neutral_fields(self):
        conn = self._connect()
        source_artifact_id = self._insert_source_artifact(conn)

        row_id = store.insert_runtime_response_item(conn, self._runtime_item(source_artifact_id))

        self.assertIsInstance(row_id, int)
        required_fields = (
            "source_kind",
            "provider_namespace",
            "runtime_namespace",
            "item_type",
            "redaction_state",
            "content_state",
            "source_artifact_id",
            "payload_json",
            "provenance_json",
            "correlation_status",
        )
        for field in required_fields:
            with self.subTest(field=field):
                invalid = self._runtime_item(source_artifact_id)
                invalid.pop(field)
                with self.assertRaisesRegex(ValueError, field):
                    store.insert_runtime_response_item(conn, invalid)

        with self.assertRaisesRegex(ValueError, "status or role"):
            store.insert_runtime_response_item(conn, self._runtime_item(source_artifact_id, status=None, role=None))

    def test_runtime_item_correlation_status_is_strict_enum(self):
        conn = self._connect()
        source_artifact_id = self._insert_source_artifact(conn)

        for correlation_status in (
            "uncorrelated",
            "correlates_with",
            "same_as_model_call",
            "not_applicable",
            "unknown",
        ):
            with self.subTest(correlation_status=correlation_status):
                store.insert_runtime_response_item(
                    conn,
                    self._runtime_item(
                        source_artifact_id,
                        payload_json={"runtime.codex_cli": {"item_id": correlation_status}},
                        correlation_status=correlation_status,
                    ),
                )

        with self.assertRaisesRegex(ValueError, "correlation_status"):
            store.insert_runtime_response_item(
                conn, self._runtime_item(source_artifact_id, correlation_status="codex_response_item")
            )

    def test_observations_require_evidence_and_content_contract_fields(self):
        conn = self._connect()
        source_artifact_id = self._insert_source_artifact(conn)

        row_id = store.insert_observation(conn, self._observation(source_artifact_id))

        self.assertIsInstance(row_id, int)
        for field in (
            "status",
            "evidence_class",
            "reliability_mode",
            "content_contract",
            "source_artifact_id",
            "value_json",
            "provenance_json",
        ):
            with self.subTest(field=field):
                invalid = self._observation(source_artifact_id)
                invalid.pop(field)
                with self.assertRaisesRegex(ValueError, field):
                    store.insert_observation(conn, invalid)

    def test_strict_validation_rejects_undeclared_enum_values(self):
        conn = self._connect()
        source_artifact_id = self._insert_source_artifact(conn)

        cases = (
            ("status", "locally_true", lambda value: self._observation(source_artifact_id, status=value)),
            ("evidence_class", "codex_log", lambda value: self._observation(source_artifact_id, evidence_class=value)),
            (
                "reliability_mode",
                "sqlite_private_column",
                lambda value: self._observation(source_artifact_id, reliability_mode=value),
            ),
            (
                "content_contract",
                "raw_private_transcript",
                lambda value: self._observation(source_artifact_id, content_contract=value),
            ),
            (
                "cost_evidence_mode",
                "billing_guess",
                lambda value: {
                    "run_id": "run-001",
                    "source_artifact_id": source_artifact_id,
                    "cost_evidence_mode": value,
                    "cost_json": {"total_estimated_cost": "1.00"},
                    "provenance_json": {"line": 1},
                },
            ),
            ("comparability", "same_enough", lambda value: self._observation(source_artifact_id, comparability=value)),
        )
        for field, bad_value, row_factory in cases:
            with self.subTest(field=field):
                with self.assertRaisesRegex(ValueError, field):
                    if field == "cost_evidence_mode":
                        store.insert_cost_estimate(conn, row_factory(bad_value), strict=True)
                    else:
                        store.insert_observation(conn, row_factory(bad_value), strict=True)

    def test_registry_and_rebuild_tables_support_hashes(self):
        conn = self._connect()

        registry_id = store.insert_registry(
            conn,
            {
                "registry_id": "fixture.telemetry",
                "registry_version": "2026.04.24",
                "registry_hash": "sha256:registry",
                "canonical_json": {"registry_id": "fixture.telemetry"},
            },
        )
        rebuild_id = store.insert_rebuild_run(
            conn,
            {
                "schema_version": store.SCHEMA_VERSION,
                "registry_version": "2026.04.24",
                "registry_hash": "sha256:registry",
                "source_set_hash": "sha256:sources",
                "status": "completed",
                "provenance_json": {"created_by": "unit-test"},
            },
        )

        self.assertIsInstance(registry_id, int)
        self.assertIsInstance(rebuild_id, int)
        row = conn.execute("SELECT registry_hash, source_set_hash FROM rebuild_runs").fetchone()
        self.assertEqual(row["registry_hash"], "sha256:registry")
        self.assertEqual(row["source_set_hash"], "sha256:sources")

    def test_core_tables_do_not_require_provider_specific_columns(self):
        conn = self._connect()

        for table in MINIMUM_TABLES:
            with self.subTest(table=table):
                columns = self._columns(conn, table)
                self.assertNotIn("response_item", columns)
                self.assertNotIn("parentUuid", columns)


if __name__ == "__main__":
    unittest.main()
