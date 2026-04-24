import contextlib
import io
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tooling.codex.model_benchmark import cli


V0_FIXTURE_DIR = Path(__file__).parent / "fixtures" / "model_benchmark" / "v0_run_jsonl_compatibility"


class ModelBenchmarkCliTests(unittest.TestCase):
    def _tmpdir(self) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        return Path(tmpdir.name)

    def _run_cli(self, argv: list[str]) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            status = cli.main(argv)
        return status, stdout.getvalue(), stderr.getvalue()

    def _manifest(self) -> dict:
        return {
            "schema_version": "telemetry-plugin-manifest/v1",
            "registry_id": "fixture.telemetry",
            "registry_version": "2026.04.24-cli",
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

    def _write_jsonl(self, path: Path) -> None:
        path.write_text(
            '{"record_type":"ok","content_contract":"metadata_only"}\n'
            '{"record_type":"broken","content_contract":"metadata_only"\n',
            encoding="utf-8",
        )

    def _write_manifest(self, path: Path) -> None:
        path.write_text(json.dumps(self._manifest(), sort_keys=True), encoding="utf-8")

    def _create_marker_db(self, path: Path, marker: str = "preserve-me") -> None:
        conn = sqlite3.connect(path)
        try:
            conn.execute("CREATE TABLE marker(value TEXT NOT NULL)")
            conn.execute("INSERT INTO marker(value) VALUES (?)", (marker,))
            conn.commit()
        finally:
            conn.close()

    def _marker_value(self, path: Path) -> str:
        conn = sqlite3.connect(path)
        try:
            row = conn.execute("SELECT value FROM marker").fetchone()
            return str(row[0])
        finally:
            conn.close()

    def _set_store_metadata_marker(self, path: Path, marker: str) -> None:
        conn = sqlite3.connect(path)
        try:
            conn.execute("UPDATE store_metadata SET value = ? WHERE key = ?", (marker, "schema_version"))
            conn.commit()
        finally:
            conn.close()

    def _store_metadata_marker(self, path: Path) -> str:
        conn = sqlite3.connect(path)
        try:
            row = conn.execute("SELECT value FROM store_metadata WHERE key = ?", ("schema_version",)).fetchone()
            return str(row[0])
        finally:
            conn.close()

    def _assert_no_ambient_config_reads(self, argv: list[str]) -> tuple[int, str, str]:
        def forbidden_home() -> Path:
            raise AssertionError("CLI must not resolve home-level provider configuration")

        with mock.patch.dict(
            os.environ,
            {
                "OPENAI_API_KEY": "SHOULD_NOT_BE_READ",
                "ANTHROPIC_API_KEY": "SHOULD_NOT_BE_READ",
                "CODEX_HOME": "SHOULD_NOT_BE_READ",
                "CLAUDE_CONFIG_DIR": "SHOULD_NOT_BE_READ",
            },
            clear=False,
        ), mock.patch("pathlib.Path.home", side_effect=forbidden_home):
            status, stdout, stderr = self._run_cli(argv)
        combined = stdout + stderr
        self.assertNotIn("SHOULD_NOT_BE_READ", combined)
        return status, stdout, stderr

    def test_existing_v0_commands_still_work(self):
        tmpdir = self._tmpdir()
        runs = V0_FIXTURE_DIR / "runs.jsonl"
        rates = tmpdir / "rates.json"
        estimated = tmpdir / "estimated.jsonl"
        summary = tmpdir / "summary.json"
        rates.write_text(
            json.dumps(
                {
                    "model": "gpt-5.5",
                    "currency": "USD",
                    "source_url": "https://example.test/pricing",
                    "retrieved_at": "2026-04-24T00:00:00Z",
                    "effective_date": "2026-04-24",
                    "input_per_million": "1.00",
                    "cached_input_per_million": "0.10",
                    "output_per_million": "5.00",
                    "reasoning_per_million": "5.00",
                }
            ),
            encoding="utf-8",
        )

        status, stdout, stderr = self._run_cli(["validate-runs", "--runs", str(runs)])
        self.assertEqual(status, 0, stderr)
        self.assertIn("validated 2 run record", stdout)

        status, stdout, stderr = self._run_cli(
            ["estimate-costs", "--runs", str(runs), "--rates", str(rates), "--output", str(estimated)]
        )
        self.assertEqual(status, 0, stderr)
        self.assertTrue(estimated.exists())
        self.assertIn("wrote 2 estimated run record", stdout)

        status, stdout, stderr = self._run_cli(
            ["summarize-runs", "--runs", str(estimated), "--output", str(summary)]
        )
        self.assertEqual(status, 0, stderr)
        self.assertTrue(summary.exists())
        self.assertGreaterEqual(len(json.loads(summary.read_text(encoding="utf-8"))["groups"]), 1)

    def test_import_v0_runs_writes_local_db_and_refuses_db_overwrite(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "telemetry.sqlite"

        status, stdout, stderr = self._assert_no_ambient_config_reads(
            ["import-v0-runs", "--runs", str(V0_FIXTURE_DIR / "runs.jsonl"), "--db", str(db)]
        )

        self.assertEqual(status, 0, stderr)
        self.assertTrue(db.exists())
        payload = json.loads(stdout)
        self.assertEqual(payload["counts"]["runs"], 2)
        self.assertEqual(payload["diagnostic_count"], 0)
        self.assertRegex(payload["source_hash"], r"^sha256:[0-9a-f]{64}$")

        status, stdout, stderr = self._run_cli(
            ["import-v0-runs", "--runs", str(V0_FIXTURE_DIR / "runs.jsonl"), "--db", str(db)]
        )

        self.assertNotEqual(status, 0)
        self.assertIn("--overwrite", stderr)

    def test_migration_report_writes_json_and_refuses_output_overwrite(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "telemetry.sqlite"
        output = tmpdir / "migration-report.json"
        self.assertEqual(
            self._run_cli(
                [
                    "import-v0-runs",
                    "--runs",
                    str(V0_FIXTURE_DIR / "runs.jsonl"),
                    "--db",
                    str(db),
                ]
            )[0],
            0,
        )
        output.write_text("{}", encoding="utf-8")

        status, stdout, stderr = self._run_cli(["migration-report", "--db", str(db), "--output", str(output)])
        self.assertNotEqual(status, 0)
        self.assertIn("--overwrite", stderr)

        status, stdout, stderr = self._assert_no_ambient_config_reads(
            ["migration-report", "--db", str(db), "--output", str(output), "--overwrite"]
        )

        self.assertEqual(status, 0, stderr)
        payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(payload["v0_compatibility_status"], "compatibility_active")
        self.assertEqual(payload["counts"]["legacy_score_observations"], 1)
        self.assertEqual(payload["registry_hash"], "not_collected")
        self.assertEqual(payload["source_set_hash"], "not_collected")

    def test_rebuild_fixtures_writes_local_db_and_reports_hashes(self):
        tmpdir = self._tmpdir()
        manifest = tmpdir / "manifest.json"
        source = tmpdir / "source.jsonl"
        db = tmpdir / "fixtures.sqlite"
        self._write_manifest(manifest)
        self._write_jsonl(source)

        status, stdout, stderr = self._assert_no_ambient_config_reads(
            ["rebuild-fixtures", "--manifest", str(manifest), "--db", str(db), "--source", str(source)]
        )

        self.assertEqual(status, 0, stderr)
        payload = json.loads(stdout)
        self.assertEqual(payload["counts"]["diagnostics"], 1)
        self.assertRegex(payload["registry_hash"], r"^sha256:[0-9a-f]{64}$")
        self.assertRegex(payload["source_set_hash"], r"^sha256:[0-9a-f]{64}$")

        status, stdout, stderr = self._run_cli(
            ["rebuild-fixtures", "--manifest", str(manifest), "--db", str(db), "--source", str(source)]
        )

        self.assertNotEqual(status, 0)
        self.assertIn("--overwrite", stderr)

    def test_query_rebuild_writes_report_and_refuses_output_overwrite(self):
        tmpdir = self._tmpdir()
        manifest = tmpdir / "manifest.json"
        source = tmpdir / "source.jsonl"
        db = tmpdir / "fixtures.sqlite"
        output = tmpdir / "rebuild-report.json"
        self._write_manifest(manifest)
        self._write_jsonl(source)
        status, stdout, stderr = self._run_cli(
            ["rebuild-fixtures", "--manifest", str(manifest), "--db", str(db), "--source", str(source)]
        )
        self.assertEqual(status, 0, stderr)
        rebuild_result = json.loads(stdout)
        output.write_text("{}", encoding="utf-8")

        status, stdout, stderr = self._run_cli(["query-rebuild", "--db", str(db), "--output", str(output)])
        self.assertNotEqual(status, 0)
        self.assertIn("--overwrite", stderr)

        status, stdout, stderr = self._assert_no_ambient_config_reads(
            [
                "query-rebuild",
                "--db",
                str(db),
                "--output",
                str(output),
                "--registry-hash",
                rebuild_result["registry_hash"],
                "--overwrite",
            ]
        )

        self.assertEqual(status, 0, stderr)
        payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(payload["registry_hash"], rebuild_result["registry_hash"])
        self.assertEqual(payload["source_set_hash"], rebuild_result["source_set_hash"])
        self.assertEqual(payload["diagnostic_count"], 1)

    def test_cli_errors_are_nonzero_and_do_not_dump_raw_rows(self):
        tmpdir = self._tmpdir()
        runs = tmpdir / "private.jsonl"
        db = tmpdir / "private.sqlite"
        runs.write_text(
            '{"run_id":"PRIVATE-RUN","task_id":"PRIVATE-TASK","prompt":"PRIVATE PROMPT"}\n',
            encoding="utf-8",
        )

        status, stdout, stderr = self._run_cli(["import-v0-runs", "--runs", str(runs), "--db", str(db)])

        self.assertNotEqual(status, 0)
        self.assertNotIn("PRIVATE-RUN", stderr)
        self.assertNotIn("PRIVATE-TASK", stderr)
        self.assertNotIn("PRIVATE PROMPT", stderr)
        self.assertEqual(stdout, "")

    def test_import_v0_runs_overwrite_failure_preserves_existing_db(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "existing.sqlite"
        missing_runs = tmpdir / "missing.jsonl"
        self._create_marker_db(db)

        status, stdout, stderr = self._run_cli(
            ["import-v0-runs", "--runs", str(missing_runs), "--db", str(db), "--overwrite"]
        )

        self.assertNotEqual(status, 0)
        self.assertEqual(stdout, "")
        self.assertEqual(self._marker_value(db), "preserve-me")

    def test_rebuild_fixtures_overwrite_failure_preserves_existing_db(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "existing.sqlite"
        missing_manifest = tmpdir / "missing-manifest.json"
        source = tmpdir / "source.jsonl"
        self._write_jsonl(source)
        self._create_marker_db(db)

        status, stdout, stderr = self._run_cli(
            [
                "rebuild-fixtures",
                "--manifest",
                str(missing_manifest),
                "--db",
                str(db),
                "--source",
                str(source),
                "--overwrite",
            ]
        )

        self.assertNotEqual(status, 0)
        self.assertEqual(stdout, "")
        self.assertEqual(self._marker_value(db), "preserve-me")

    def test_rebuild_fixtures_missing_source_overwrite_failure_preserves_existing_db(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "existing.sqlite"
        manifest = tmpdir / "manifest.json"
        missing_source = tmpdir / "missing-source.jsonl"
        self._write_manifest(manifest)
        self._create_marker_db(db)

        status, stdout, stderr = self._run_cli(
            [
                "rebuild-fixtures",
                "--manifest",
                str(manifest),
                "--db",
                str(db),
                "--source",
                str(missing_source),
                "--overwrite",
            ]
        )

        self.assertNotEqual(status, 0)
        self.assertEqual(stdout, "")
        self.assertEqual(self._marker_value(db), "preserve-me")

    def test_migration_report_uses_read_only_db_on_success_and_output_overwrite_failure(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "telemetry.sqlite"
        output = tmpdir / "migration-report.json"
        status, stdout, stderr = self._run_cli(
            ["import-v0-runs", "--runs", str(V0_FIXTURE_DIR / "runs.jsonl"), "--db", str(db)]
        )
        self.assertEqual(status, 0, stderr)
        self._set_store_metadata_marker(db, "read-only-marker")
        output.write_text("{}", encoding="utf-8")

        status, stdout, stderr = self._run_cli(["migration-report", "--db", str(db), "--output", str(output)])

        self.assertNotEqual(status, 0)
        self.assertEqual(self._store_metadata_marker(db), "read-only-marker")

        status, stdout, stderr = self._run_cli(
            ["migration-report", "--db", str(db), "--output", str(output), "--overwrite"]
        )

        self.assertEqual(status, 0, stderr)
        self.assertEqual(self._store_metadata_marker(db), "read-only-marker")

    def test_query_rebuild_uses_read_only_db_on_success_and_output_overwrite_failure(self):
        tmpdir = self._tmpdir()
        manifest = tmpdir / "manifest.json"
        source = tmpdir / "source.jsonl"
        db = tmpdir / "fixtures.sqlite"
        output = tmpdir / "rebuild-report.json"
        self._write_manifest(manifest)
        self._write_jsonl(source)
        status, stdout, stderr = self._run_cli(
            ["rebuild-fixtures", "--manifest", str(manifest), "--db", str(db), "--source", str(source)]
        )
        self.assertEqual(status, 0, stderr)
        self._set_store_metadata_marker(db, "read-only-marker")
        output.write_text("{}", encoding="utf-8")

        status, stdout, stderr = self._run_cli(["query-rebuild", "--db", str(db), "--output", str(output)])

        self.assertNotEqual(status, 0)
        self.assertEqual(self._store_metadata_marker(db), "read-only-marker")

        status, stdout, stderr = self._run_cli(
            ["query-rebuild", "--db", str(db), "--output", str(output), "--overwrite"]
        )

        self.assertEqual(status, 0, stderr)
        self.assertEqual(self._store_metadata_marker(db), "read-only-marker")


if __name__ == "__main__":
    unittest.main()
