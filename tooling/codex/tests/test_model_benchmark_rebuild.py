import sqlite3
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import manifest, query, rebuild, store


class ModelBenchmarkRebuildTests(unittest.TestCase):
    def _connect(self) -> sqlite3.Connection:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        conn = store.connect(Path(tmpdir.name) / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _manifest(self, registry_version: str = "2026.04.24-test") -> dict:
        return manifest.validate_manifest(
            {
                "schema_version": manifest.SCHEMA_VERSION,
                "registry_id": "fixture.telemetry",
                "registry_version": registry_version,
                "source_kinds": [{"id": "diagnostic.malformed_jsonl"}],
                "namespaces": [{"id": "fixture"}],
                "predicates": [{"id": "source.has_diagnostic"}],
                "metrics": [
                    {
                        "id": "source.parse_status",
                        "status": "malformed_source",
                        "evidence_class": "synthetic_fixture",
                        "reliability_mode": "direct_field",
                        "content_contract": "metadata_only",
                        "cost_evidence_mode": "not_applicable",
                        "comparability": "not_comparable",
                    }
                ],
                "rubrics": [{"id": "quality.auditability", "dimensions": [{"id": "records_diagnostics"}]}],
                "emits": [
                    {
                        "source_kind": "diagnostic.malformed_jsonl",
                        "namespace": "fixture",
                        "predicate": "source.has_diagnostic",
                        "metric_id": "source.parse_status",
                        "status": "malformed_source",
                        "reliability_mode": "direct_field",
                        "content_contract": "metadata_only",
                    }
                ],
            }
        )

    def _write_jsonl(self, text: str) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "source.jsonl"
        path.write_text(text, encoding="utf-8")
        return path

    def test_rebuild_stores_registry_hash_source_set_hash_and_query_exposes_them(self):
        conn = self._connect()
        registry = self._manifest()
        source = self._write_jsonl('{"record_type":"ok","content_contract":"metadata_only"}\n')

        result = rebuild.rebuild_fixture_sources(conn, registry, [source])

        self.assertEqual(result["registry_hash"], registry["registry_hash"])
        self.assertRegex(result["source_set_hash"], r"^sha256:[0-9a-f]{64}$")
        row = conn.execute("SELECT registry_hash, source_set_hash FROM rebuild_runs").fetchone()
        self.assertEqual(row["registry_hash"], result["registry_hash"])
        self.assertEqual(row["source_set_hash"], result["source_set_hash"])

        output = query.query_rebuild_summary(conn, registry_hash=registry["registry_hash"], strict=True)
        self.assertEqual(output["registry_hash"], registry["registry_hash"])
        self.assertEqual(output["source_set_hash"], result["source_set_hash"])

    def test_strict_query_fails_registry_hash_mismatch(self):
        conn = self._connect()
        registry = self._manifest()
        source = self._write_jsonl('{"record_type":"ok","content_contract":"metadata_only"}\n')
        rebuild.rebuild_fixture_sources(conn, registry, [source])

        with self.assertRaisesRegex(ValueError, "registry_hash mismatch"):
            query.query_rebuild_summary(conn, registry_hash="sha256:not-the-registry", strict=True)

    def test_malformed_jsonl_records_parse_diagnostics_without_raw_content(self):
        conn = self._connect()
        registry = self._manifest()
        source = self._write_jsonl(
            '{"record_type":"ok","content_contract":"metadata_only"}\n'
            '{"record_type":"broken","content_contract":"metadata_only"\n'
        )

        result = rebuild.rebuild_fixture_sources(conn, registry, [source])

        self.assertEqual(result["diagnostics"][0]["status"], "malformed_source")
        self.assertEqual(result["diagnostics"][0]["line_number"], 2)
        self.assertEqual(result["diagnostics"][0]["content_contract"], "metadata_only")
        self.assertNotIn("raw_content", result["diagnostics"][0])
        persisted = query.query_rebuild_summary(conn, registry_hash=registry["registry_hash"], strict=True)
        self.assertEqual(persisted["diagnostic_count"], 1)
        observation = conn.execute("SELECT value_json FROM observations").fetchone()
        self.assertNotIn("broken", observation["value_json"])

    def test_rebuild_is_deterministic_for_same_fixture_source_set(self):
        source = self._write_jsonl('{"record_type":"ok","content_contract":"metadata_only"}\n')
        registry = self._manifest()
        first = rebuild.rebuild_fixture_sources(self._connect(), registry, [source])
        second = rebuild.rebuild_fixture_sources(self._connect(), registry, [source])

        self.assertEqual(first["registry_hash"], second["registry_hash"])
        self.assertEqual(first["source_set_hash"], second["source_set_hash"])
        self.assertEqual(first["diagnostics"], second["diagnostics"])


if __name__ == "__main__":
    unittest.main()
