import contextlib
import io
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tooling.codex.model_benchmark import cli, fixtures, manifest, query, rebuild, reports, store
from tooling.codex.model_benchmark.adapters import claude_local, validate_adapter_output


FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "model_benchmark"
V0_RUNS = FIXTURE_ROOT / "v0_run_jsonl_compatibility" / "runs.jsonl"
CLAUDE_SESSION = fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"


class ModelBenchmarkIntegrationTests(unittest.TestCase):
    def _tmpdir(self) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        return Path(tmpdir.name)

    def _connect(self) -> sqlite3.Connection:
        tmpdir = self._tmpdir()
        conn = store.connect(tmpdir / "benchmark.sqlite")
        self.addCleanup(conn.close)
        return conn

    def _run_cli(self, argv: list[str]) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            status = cli.main(argv)
        return status, stdout.getvalue(), stderr.getvalue()

    def _rebuild_manifest(self) -> dict:
        return {
            "schema_version": manifest.SCHEMA_VERSION,
            "registry_id": "fixture.integration.rebuild",
            "registry_version": "2026.04.24-integration",
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

    def _provider_registry(self) -> dict:
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
                "registry_id": "fixture.integration.provider_neutrality",
                "registry_version": "2026.04.24-integration",
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
            CLAUDE_SESSION,
            fixtures.fixture_path("provider_denominator_mismatch") / "expected_normalized.json",
        ]

    def test_v0_import_migration_report_and_cli_query_stay_metadata_only(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "telemetry.sqlite"
        report = tmpdir / "migration-report.json"

        status, stdout, stderr = self._run_cli(["import-v0-runs", "--runs", str(V0_RUNS), "--db", str(db)])
        self.assertEqual(status, 0, stderr)
        import_payload = json.loads(stdout)
        self.assertEqual(import_payload["counts"]["runs"], 2)
        self.assertEqual(import_payload["counts"]["legacy_score_observations"], 1)

        status, stdout, stderr = self._run_cli(["migration-report", "--db", str(db), "--output", str(report)])
        self.assertEqual(status, 0, stderr)
        report_payload = json.loads(report.read_text(encoding="utf-8"))
        self.assertEqual(report_payload, json.loads(stdout))
        self.assertEqual(report_payload["v0_compatibility_status"], "compatibility_active")
        self.assertEqual(report_payload["counts"]["legacy_score_observations"], 1)
        self.assertEqual(report_payload["counts"]["rubric_observations"], 1)
        self.assertEqual(report_payload["cost_evidence_mode_counts"]["api_equivalent_estimate"], 1)

        serialized = json.dumps({"stdout": stdout, "report": report_payload}, sort_keys=True)
        self.assertNotIn("prompt", serialized.lower())
        self.assertNotIn("assistant", serialized.lower())
        self.assertNotIn("tool_result", serialized.lower())
        self.assertNotIn("transcript", serialized.lower())
        self.assertNotIn("raw_content", serialized.lower())

    def test_fixture_rebuild_cli_query_and_report_propagate_registry_and_source_hashes(self):
        tmpdir = self._tmpdir()
        manifest_path = tmpdir / "manifest.json"
        source_path = tmpdir / "source.jsonl"
        db = tmpdir / "fixtures.sqlite"
        output = tmpdir / "query.json"
        manifest_path.write_text(json.dumps(self._rebuild_manifest(), sort_keys=True), encoding="utf-8")
        source_path.write_text(
            '{"record_type":"ok","content_contract":"metadata_only"}\n'
            '{"record_type":"broken","content_contract":"metadata_only"\n',
            encoding="utf-8",
        )

        status, stdout, stderr = self._run_cli(
            ["rebuild-fixtures", "--manifest", str(manifest_path), "--db", str(db), "--source", str(source_path)]
        )
        self.assertEqual(status, 0, stderr)
        rebuild_payload = json.loads(stdout)

        status, stdout, stderr = self._run_cli(
            [
                "query-rebuild",
                "--db",
                str(db),
                "--output",
                str(output),
                "--registry-hash",
                rebuild_payload["registry_hash"],
            ]
        )
        self.assertEqual(status, 0, stderr)
        query_payload = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(query_payload["registry_hash"], rebuild_payload["registry_hash"])
        self.assertEqual(query_payload["source_set_hash"], rebuild_payload["source_set_hash"])

        report_payload = reports.telemetry_rebuild_report(
            query_payload,
            registry_hash=rebuild_payload["registry_hash"],
            strict=True,
        )
        self.assertEqual(report_payload["registry_hash"], rebuild_payload["registry_hash"])
        self.assertEqual(report_payload["source_set_hash"], rebuild_payload["source_set_hash"])

    def test_provider_neutrality_gate_statuses_and_claude_adapter_payload_shape_coexist(self):
        registry = self._provider_registry()

        codex_only_conn = self._connect()
        rebuild.rebuild_provider_neutrality_gate(
            codex_only_conn,
            registry,
            [fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"],
            strict=True,
        )
        codex_only_gate = query.query_provider_neutrality_gate(
            codex_only_conn,
            registry_hash=registry["registry_hash"],
            strict=True,
        )
        self.assertEqual(codex_only_gate["provider_neutrality_gate"]["status"], "not_passed")

        claude_output = claude_local.normalize_local_jsonl(CLAUDE_SESSION)
        validate_adapter_output(claude_output, strict=True)

        mixed_conn = self._connect()
        rebuild.rebuild_provider_neutrality_gate(mixed_conn, registry, self._gate_sources(), strict=True)
        mixed_gate = query.query_provider_neutrality_gate(
            mixed_conn,
            registry_hash=registry["registry_hash"],
            strict=True,
        )

        self.assertEqual(mixed_gate["provider_neutrality_gate"]["status"], "passed")
        self.assertEqual(
            [item["item_type"] for item in mixed_gate["runtime_response_items"]],
            [item["item_type"] for item in claude_output["runtime_response_items"]],
        )
        for item in mixed_gate["runtime_response_items"]:
            self.assertEqual(item["provider_namespace"], "provider.anthropic")
            self.assertEqual(item["runtime_namespace"], "runtime.claude_code")
            self.assertIn("anthropic", item["payload"])
            self.assertNotIn("codex", item["payload"])
            self.assertNotIn("claude", item["payload"])

        usage = mixed_gate["provider_usage_evidence"]
        self.assertEqual(usage["openai"]["cache_read_tokens"]["denominator"], "cached_input_tokens")
        self.assertEqual(usage["anthropic"]["cache_read_tokens"]["denominator"], "cache_read_input_tokens")
        self.assertEqual(usage["anthropic"]["reasoning_tokens"]["status"], "not_exposed")

    def test_score_overall_is_legacy_only_and_runtime_items_are_not_model_calls(self):
        conn = self._connect()
        registry = self._provider_registry()
        rebuild.rebuild_provider_neutrality_gate(conn, registry, self._gate_sources(), strict=True)
        gate = query.query_provider_neutrality_gate(conn, registry_hash=registry["registry_hash"], strict=True)

        canonical_manifest = json.dumps(registry, sort_keys=True)
        self.assertNotIn('"score.overall"', canonical_manifest)
        self.assertNotIn("score.overall", json.dumps(gate, sort_keys=True))
        self.assertGreater(
            conn.execute("SELECT COUNT(*) AS count FROM runtime_response_items").fetchone()["count"],
            0,
        )
        self.assertEqual(
            conn.execute("SELECT COUNT(*) AS count FROM model_calls").fetchone()["count"],
            0,
        )

        tmpdir = self._tmpdir()
        db = tmpdir / "telemetry.sqlite"
        report_path = tmpdir / "migration-report.json"
        self.assertEqual(self._run_cli(["import-v0-runs", "--runs", str(V0_RUNS), "--db", str(db)])[0], 0)
        self.assertEqual(
            self._run_cli(["migration-report", "--db", str(db), "--output", str(report_path)])[0],
            0,
        )
        migration_report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(migration_report["counts"]["legacy_score_observations"], 1)

    def test_integration_paths_do_not_open_home_provider_logs_or_configs(self):
        tmpdir = self._tmpdir()
        db = tmpdir / "telemetry.sqlite"
        provider_fragments = (
            str(Path.home() / ".codex"),
            str(Path.home() / ".claude"),
            "credentials",
            "api_keys",
            "raw_api_bodies",
        )
        real_open = open
        opened_paths: list[str] = []

        def tracking_open(path, *args, **kwargs):
            opened_paths.append(str(path))
            if any(fragment in str(path) for fragment in provider_fragments):
                raise AssertionError(f"opened home-level provider surface: {path}")
            return real_open(path, *args, **kwargs)

        with mock.patch.dict(
            os.environ,
            {
                "OPENAI_API_KEY": "SHOULD_NOT_BE_READ",
                "ANTHROPIC_API_KEY": "SHOULD_NOT_BE_READ",
                "CODEX_HOME": "SHOULD_NOT_BE_READ",
                "CLAUDE_CONFIG_DIR": "SHOULD_NOT_BE_READ",
            },
            clear=False,
        ), mock.patch("builtins.open", tracking_open), mock.patch(
            "pathlib.Path.home",
            side_effect=AssertionError("integration path resolved a home-level provider surface"),
        ):
            status, stdout, stderr = self._run_cli(["import-v0-runs", "--runs", str(V0_RUNS), "--db", str(db)])
            self.assertEqual(status, 0, stderr)
            conn = self._connect()
            rebuild.rebuild_provider_neutrality_gate(conn, self._provider_registry(), self._gate_sources(), strict=True)

        self.assertNotIn("SHOULD_NOT_BE_READ", stdout + stderr)


if __name__ == "__main__":
    unittest.main()
