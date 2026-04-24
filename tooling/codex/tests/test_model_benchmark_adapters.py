import builtins
import json
import tempfile
import unittest
from unittest import mock
from pathlib import Path

from tooling.codex.model_benchmark import fixtures
from tooling.codex.model_benchmark.adapters import validate_adapter_output
from tooling.codex.model_benchmark.adapters import codex_rollout, codex_sqlite


class ModelBenchmarkAdapterTests(unittest.TestCase):
    def test_sqlite_fixture_emits_session_and_subagent_edge_without_sensitive_content(self):
        output = codex_sqlite.normalize_source_index(
            fixtures.fixture_path("codex_sqlite_minimal_thread") / "source_index.json"
        )

        validate_adapter_output(output, strict=True)
        self.assertEqual(output["sessions"][0]["session_id"], "codex-session-001")
        self.assertEqual(output["sessions"][0]["source_artifact_ref"]["artifact_id"], "codex-thread-sqlite-001")
        self.assertEqual(output["entity_edges"][0]["predicate"], "session.has_subagent")
        self.assertEqual(output["entity_edges"][0]["target_entity_type"], "subagent")
        self.assertEqual(output["turns"][0]["turn_id"], "codex-item-001")

        encoded = json.dumps(output, sort_keys=True)
        self.assertNotIn("title", encoded)
        self.assertNotIn("first_message", encoded)
        self.assertNotIn("message_content", encoded)

    def test_rollout_fixture_emits_runtime_items_distinct_from_model_calls(self):
        output = codex_rollout.normalize_rollout_jsonl(
            fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"
        )

        validate_adapter_output(output, strict=True)
        self.assertEqual(output["model_calls"], [])
        self.assertEqual(output["runtime_response_items"][0]["runtime_item_id"], "codex-rollout-item-001")
        self.assertIsNone(output["runtime_response_items"][0]["model_call_id"])
        self.assertEqual(output["runtime_response_items"][0]["correlation_status"], "unknown")
        self.assertEqual(output["turns"][0]["turn_id"], "codex-rollout-item-001")

    def test_adapters_emit_environment_model_and_reasoning_observations(self):
        output = codex_rollout.normalize_rollout_jsonl(
            fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"
        )

        metric_ids = {observation["metric_id"] for observation in output["observations"]}
        self.assertIn("runtime.sandbox", metric_ids)
        self.assertIn("runtime.approval_policy", metric_ids)
        self.assertIn("runtime.git_state", metric_ids)
        self.assertIn("runtime.model", metric_ids)
        self.assertIn("runtime.reasoning", metric_ids)

    def test_runtime_items_include_required_generic_and_provenance_fields(self):
        output = codex_rollout.normalize_rollout_jsonl(
            fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"
        )
        item = output["runtime_response_items"][0]

        for field in (
            "source_kind",
            "provider_namespace",
            "runtime_namespace",
            "item_type",
            "redaction_state",
            "content_state",
            "source_artifact_ref",
            "provenance",
            "payload",
            "correlation_status",
        ):
            self.assertIn(field, item)
        self.assertEqual(item["source_artifact_ref"]["line_number"], 2)
        self.assertRegex(item["source_artifact_ref"]["line_hash"], r"^sha256:[0-9a-f]{64}$")
        self.assertIn("codex", item["payload"])

    def test_adapter_output_validation_rejects_undeclared_enums_in_strict_mode(self):
        output = codex_rollout.normalize_rollout_jsonl(
            fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"
        )
        checks = (
            ("parse_diagnostics", "status", "made_up_status"),
            ("parse_diagnostics", "evidence_class", "made_up_evidence"),
            ("parse_diagnostics", "reliability_mode", "made_up_reliability"),
            ("parse_diagnostics", "content_contract", "made_up_contract"),
            ("token_observations", "cost_evidence_mode", "made_up_cost_mode"),
            ("token_observations", "comparability", "made_up_comparability"),
        )
        for section, field, bad_value in checks:
            with self.subTest(section=section, field=field):
                mutated = json.loads(json.dumps(output))
                mutated[section][0][field] = bad_value
                with self.assertRaisesRegex(ValueError, field):
                    validate_adapter_output(mutated, strict=True)

    def test_compaction_marker_is_structural_without_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "rollout.jsonl"
            path.write_text(
                '{"record_type":"session_meta","session_id":"codex-rollout-compact","redaction_state":"synthetic","content_contract":"structural_only"}\n'
                '{"record_type":"turn_context","marker":"compacted","lineage":"synthetic","redaction_state":"redacted","content_contract":"structural_only"}\n',
                encoding="utf-8",
            )

            output = codex_rollout.normalize_rollout_jsonl(path)

        validate_adapter_output(output, strict=True)
        item = output["runtime_response_items"][0]
        self.assertEqual(item["item_type"], "compaction_marker")
        self.assertEqual(item["content_state"], "no_content")
        self.assertNotIn("content", item["payload"])
        self.assertNotIn("lineage", item["payload"])

    def test_codex_specific_field_names_stay_inside_provider_payload_namespace(self):
        output = codex_rollout.normalize_rollout_jsonl(
            fixtures.fixture_path("codex_rollout_redacted_stream") / "stream.jsonl"
        )
        item = output["runtime_response_items"][0]

        self.assertNotIn("response_item", item)
        self.assertNotIn("turn_context", item)
        self.assertIn("codex", item["payload"])
        self.assertIn("record_type", item["payload"]["codex"])

    def test_sqlite_adapter_requires_explicit_path_and_does_not_open_home_codex(self):
        fixture_path = fixtures.fixture_path("codex_sqlite_minimal_thread") / "source_index.json"
        real_open = builtins.open
        opened_paths = []

        def tracking_open(path, *args, **kwargs):
            opened_paths.append(str(path))
            if str(path).startswith(str(Path.home() / ".codex")):
                raise AssertionError("adapter opened home Codex state")
            return real_open(path, *args, **kwargs)

        with mock.patch("builtins.open", tracking_open):
            output = codex_sqlite.normalize_source_index(fixture_path)

        self.assertEqual(output["sessions"][0]["session_id"], "codex-session-001")
        self.assertTrue(opened_paths)
        self.assertTrue(all(not path.startswith(str(Path.home() / ".codex")) for path in opened_paths))


if __name__ == "__main__":
    unittest.main()
