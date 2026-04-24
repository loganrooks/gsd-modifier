import sqlite3
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import manifest, query, rebuild, reports, store


class ModelBenchmarkReportParityTests(unittest.TestCase):
    def _connect(self) -> sqlite3.Connection:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        conn = store.connect(Path(tmpdir.name) / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _manifest(self) -> dict:
        return manifest.validate_manifest(
            {
                "schema_version": manifest.SCHEMA_VERSION,
                "registry_id": "fixture.telemetry",
                "registry_version": "2026.04.24-test",
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

    def _source(self, text: str) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "source.jsonl"
        path.write_text(text, encoding="utf-8")
        return path

    def test_report_output_includes_registry_hash_and_source_set_hash(self):
        conn = self._connect()
        registry = self._manifest()
        rebuild_result = rebuild.rebuild_fixture_sources(
            conn,
            registry,
            [self._source('{"record_type":"ok","content_contract":"metadata_only"}\n')],
        )
        query_output = query.query_rebuild_summary(conn, registry_hash=registry["registry_hash"], strict=True)

        report = reports.telemetry_rebuild_report(query_output, registry_hash=registry["registry_hash"], strict=True)

        self.assertEqual(report["registry_hash"], registry["registry_hash"])
        self.assertEqual(report["source_set_hash"], rebuild_result["source_set_hash"])

    def test_strict_report_fails_registry_hash_mismatch(self):
        conn = self._connect()
        registry = self._manifest()
        rebuild.rebuild_fixture_sources(conn, registry, [self._source('{"record_type":"ok"}\n')])
        query_output = query.query_rebuild_summary(conn, registry_hash=registry["registry_hash"], strict=True)

        with self.assertRaisesRegex(ValueError, "registry_hash mismatch"):
            reports.telemetry_rebuild_report(query_output, registry_hash="sha256:not-the-registry", strict=True)

    def test_strict_report_input_validation_rejects_undeclared_enums(self):
        cases = (
            ("status", "locally_true"),
            ("evidence_class", "codex_log"),
            ("reliability_mode", "sqlite_private_column"),
            ("content_contract", "raw_private_transcript"),
            ("cost_evidence_mode", "billing_guess"),
            ("comparability", "same_enough"),
        )

        for field, bad_value in cases:
            with self.subTest(field=field):
                query_output = {
                    "registry_hash": "sha256:registry",
                    "source_set_hash": "sha256:sources",
                    "diagnostics": [
                        {
                            "status": "malformed_source",
                            "evidence_class": "synthetic_fixture",
                            "reliability_mode": "direct_field",
                            "content_contract": "metadata_only",
                            "cost_evidence_mode": "not_applicable",
                            "comparability": "not_comparable",
                        }
                    ],
                }
                query_output["diagnostics"][0][field] = bad_value

                with self.assertRaisesRegex(ValueError, field):
                    reports.telemetry_rebuild_report(query_output, registry_hash="sha256:registry", strict=True)


if __name__ == "__main__":
    unittest.main()
