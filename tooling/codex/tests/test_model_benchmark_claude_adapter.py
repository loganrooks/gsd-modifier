import builtins
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tooling.codex.model_benchmark import fixtures
from tooling.codex.model_benchmark.adapters import validate_adapter_output
from tooling.codex.model_benchmark.adapters import claude_local


class ModelBenchmarkClaudeAdapterTests(unittest.TestCase):
    def test_fixture_path_emits_claude_structures_without_codex_field_names(self):
        output = claude_local.normalize_local_jsonl(
            fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"
        )

        validate_adapter_output(output, strict=True)
        self.assertEqual(output["source_kind"], "runtime.claude_code.local_jsonl")
        self.assertEqual(output["sessions"][0]["session_id"], "claude-session-001")
        self.assertEqual(output["runtime_response_items"][0]["provider_namespace"], "provider.anthropic")
        self.assertEqual(output["runtime_response_items"][0]["runtime_namespace"], "runtime.claude_code")
        self.assertEqual(output["tool_calls"][0]["tool_call_id"], "claude-tool-001")
        self.assertEqual(output["entity_edges"][0]["predicate"], "session.has_sidechain_agent")

        encoded_payloads = json.dumps(
            {
                "sessions": output["sessions"],
                "turns": output["turns"],
                "items": output["runtime_response_items"],
                "tools": output["tool_calls"],
                "edges": output["entity_edges"],
            },
            sort_keys=True,
        )
        self.assertNotIn("response_item", encoded_payloads)
        self.assertNotIn("turn_context", encoded_payloads)
        self.assertNotIn('"codex"', encoded_payloads)
        self.assertIn('"anthropic"', encoded_payloads)
        self.assertIn('"claude_code"', encoded_payloads)

    def test_preserves_redaction_content_contract_diagnostics_and_source_lines(self):
        output = claude_local.normalize_local_jsonl(
            fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"
        )

        redaction_states = {item["redaction_state"] for item in output["runtime_response_items"]}
        self.assertEqual(redaction_states, {"synthetic", "redacted"})
        message = [item for item in output["runtime_response_items"] if item["item_type"] == "message"][0]
        self.assertEqual(message["content_state"], "redacted_reference")
        self.assertEqual(message["source_artifact_ref"]["line_number"], 2)
        self.assertEqual(message["source_artifact_ref"]["content_contract"], "redacted_content_reference")
        self.assertRegex(message["source_artifact_ref"]["line_hash"], r"^sha256:[0-9a-f]{64}$")

        diagnostic = output["parse_diagnostics"][0]
        self.assertEqual(diagnostic["status"], "malformed_source")
        self.assertEqual(diagnostic["source_artifact_ref"]["line_number"], 4)
        self.assertEqual(diagnostic["content_contract"], "metadata_only")

    def test_malformed_json_line_becomes_diagnostic_without_raw_line_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "session.jsonl"
            path.write_text(
                '{"record_type":"session","session_id":"claude-session-002","content_contract":"structural_only"}\n'
                '{"record_type":"message","message_id":"claude-message-raw","session_id":"claude-session-002",'
                '"redaction_state":"redacted","content":"SECRET-RAW-TRANSCRIPT"}\n'
                '{"record_type":\n',
                encoding="utf-8",
            )

            output = claude_local.normalize_local_jsonl(path)

        validate_adapter_output(output, strict=True)
        encoded = json.dumps(output, sort_keys=True)
        self.assertNotIn("SECRET-RAW-TRANSCRIPT", encoded)
        self.assertEqual(output["parse_diagnostics"][0]["status"], "malformed_source")
        self.assertEqual(output["parse_diagnostics"][0]["source_artifact_ref"]["line_number"], 3)

    def test_rejects_explicit_home_claude_path_before_open(self):
        disallowed_path = Path.home() / ".claude" / "projects" / "private-session.jsonl"

        with mock.patch("builtins.open", side_effect=AssertionError("open should not be called")):
            with self.assertRaisesRegex(ValueError, "disallowed Claude local source path"):
                claude_local.normalize_local_jsonl(disallowed_path)

    def test_rejects_explicit_provider_config_surface_before_open(self):
        disallowed_path = Path.home() / ".config" / "anthropic" / "session.jsonl"

        with mock.patch("builtins.open", side_effect=AssertionError("open should not be called")):
            with self.assertRaisesRegex(ValueError, "disallowed Claude local source path"):
                claude_local.normalize_local_jsonl(disallowed_path)

    def test_rejects_explicit_provider_surface_path_part_before_open(self):
        disallowed_path = Path("/tmp/fixture/hooks/session.jsonl")

        with mock.patch("builtins.open", side_effect=AssertionError("open should not be called")):
            with self.assertRaisesRegex(ValueError, "disallowed Claude local source path"):
                claude_local.normalize_local_jsonl(disallowed_path)

    def test_tool_payload_sanitizes_raw_args_content_and_private_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "session.jsonl"
            path.write_text(
                '{"record_type":"session","session_id":"claude-session-raw","content_contract":"structural_only"}\n'
                '{"record_type":"tool","tool_call_id":"claude-tool-raw","session_id":"claude-session-raw",'
                '"tool_name":"PrivateProjectSecretTool","redaction_state":"redacted","content_contract":"structural_only",'
                '"argument_shape":{"path":"/home/alice/private/secret.txt","content":"SECRET-TOOL-CONTENT",'
                '"prompt":"copy this private raw text","line_count":7,"mode":"SECRET-MODE"},'
                '"result_state":"SECRET-RESULT","raw_body":{"api_key":"sk-secret"}}\n',
                encoding="utf-8",
            )

            output = claude_local.normalize_local_jsonl(path)

        validate_adapter_output(output, strict=True)
        encoded = json.dumps(output, sort_keys=True)
        self.assertNotIn("/home/alice/private/secret.txt", encoded)
        self.assertNotIn("SECRET-TOOL-CONTENT", encoded)
        self.assertNotIn("copy this private raw text", encoded)
        self.assertNotIn("sk-secret", encoded)
        self.assertNotIn("PrivateProjectSecretTool", encoded)
        self.assertNotIn("SECRET-MODE", encoded)
        self.assertNotIn("SECRET-RESULT", encoded)
        self.assertIn('"path_shape"', encoded)
        self.assertIn('"line_count"', encoded)
        self.assertIn('"mode"', encoded)
        self.assertIn('"other"', encoded)

    def test_payload_sanitizes_non_tool_caller_controlled_fields(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "session.jsonl"
            path.write_text(
                '{"record_type":"session","session_id":"claude-session-raw-fields","content_contract":"structural_only",'
                '"thinking_summary_present":true,"facets":["SECRET-FACET"]}\n'
                '{"record_type":"sidechain_agent","agent_id":"claude-agent-raw","session_id":"claude-session-raw-fields",'
                '"agent_role":"SECRET-AGENT-ROLE","redaction_state":"synthetic","content_contract":"structural_only"}\n'
                '{"record_type":"message","message_id":"claude-message-raw-role","session_id":"claude-session-raw-fields",'
                '"role":"SECRET-ROLE","redaction_state":"redacted","content_contract":"structural_only"}\n',
                encoding="utf-8",
            )

            output = claude_local.normalize_local_jsonl(path)

        validate_adapter_output(output, strict=True)
        encoded = json.dumps(output, sort_keys=True)
        self.assertNotIn("SECRET-FACET", encoded)
        self.assertNotIn("SECRET-AGENT-ROLE", encoded)
        self.assertNotIn("SECRET-ROLE", encoded)
        self.assertIn('"facets_count"', encoded)
        self.assertIn('"agent_role_present"', encoded)

    def test_thinking_signals_are_substitute_structure_not_token_or_quality_truth(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "session.jsonl"
            path.write_text(
                '{"record_type":"session","session_id":"claude-session-003","content_contract":"structural_only",'
                '"thinking_summary_present":true,"facets":["planning","verification"]}\n'
                '{"record_type":"thinking_summary","summary_id":"claude-thinking-001","session_id":"claude-session-003",'
                '"redaction_state":"redacted","content_ref":"redacted://fixture/thinking","content_contract":"redacted_content_reference"}\n',
                encoding="utf-8",
            )

            output = claude_local.normalize_local_jsonl(path)

        validate_adapter_output(output, strict=True)
        metrics = {observation["metric_id"]: observation for observation in output["observations"]}
        self.assertEqual(metrics["runtime.reasoning.substitute_signal"]["status"], "derived")
        self.assertEqual(metrics["runtime.reasoning.substitute_signal"]["reliability_mode"], "substitute_signal")
        self.assertEqual(metrics["runtime.reasoning.substitute_signal"]["comparability"], "insufficient_evidence")
        self.assertEqual(output["token_observations"][0]["metric_id"], "tokens.reasoning")
        self.assertEqual(output["token_observations"][0]["status"], "not_exposed")
        self.assertNotIn("quality", json.dumps(output, sort_keys=True))

    def test_validation_rejects_undeclared_claude_enum_values_in_strict_mode(self):
        output = claude_local.normalize_local_jsonl(
            fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"
        )
        output["runtime_response_items"][0]["correlation_status"] = "provider_magic"

        with self.assertRaisesRegex(ValueError, "correlation_status"):
            validate_adapter_output(output, strict=True)

    def test_sanitizes_top_level_runtime_item_fields_before_strict_persistence(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "session.jsonl"
            path.write_text(
                '{"record_type":"session","session_id":"SECRET-RAW-SESSION","content_contract":"structural_only",'
                '"redaction_state":"SECRET-RAW-STATE","content_state":"SECRET-RAW-CONTENT"}\n'
                '{"record_type":"message","message_id":"SECRET-RAW-MESSAGE","session_id":"SECRET-RAW-SESSION",'
                '"role":"SECRET-RAW-ROLE","status":"SECRET-RAW-STATUS","redaction_state":"SECRET-RAW-STATE",'
                '"content_state":"SECRET-RAW-CONTENT","correlation_status":"SECRET-RAW-CORRELATION",'
                '"content_contract":"structural_only"}\n',
                encoding="utf-8",
            )

            output = claude_local.normalize_local_jsonl(path)

        validate_adapter_output(output, strict=True)
        encoded = json.dumps(output, sort_keys=True)
        self.assertNotIn("SECRET-RAW-SESSION", encoded)
        self.assertNotIn("SECRET-RAW-MESSAGE", encoded)
        self.assertNotIn("SECRET-RAW-ROLE", encoded)
        self.assertNotIn("SECRET-RAW-STATUS", encoded)
        self.assertNotIn("SECRET-RAW-STATE", encoded)
        self.assertNotIn("SECRET-RAW-CONTENT", encoded)
        self.assertNotIn("SECRET-RAW-CORRELATION", encoded)

    def test_strict_validation_rejects_raw_top_level_runtime_item_fields(self):
        output = claude_local.normalize_local_jsonl(
            fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"
        )
        output["runtime_response_items"][0].update(
            {
                "runtime_item_id": "SECRET-RAW-ITEM",
                "session_id": "SECRET-RAW-SESSION",
                "status": "SECRET-RAW-STATUS",
                "role": "SECRET-RAW-ROLE",
                "redaction_state": "SECRET-RAW-STATE",
                "content_state": "SECRET-RAW-CONTENT",
                "correlation_status": "SECRET-RAW-CORRELATION",
            }
        )

        with self.assertRaisesRegex(ValueError, "runtime_response_items"):
            validate_adapter_output(output, strict=True)

    def test_payload_namespace_validation_matches_provider_and_runtime_namespaces(self):
        claude_output = claude_local.normalize_local_jsonl(
            fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"
        )
        claude_output["runtime_response_items"][0]["payload"] = {"codex": {"record_type": "session"}}
        with self.assertRaisesRegex(ValueError, "payload namespace"):
            validate_adapter_output(claude_output, strict=True)

        codex_like_output = json.loads(json.dumps(claude_output))
        codex_like_output["runtime_response_items"][0].update(
            {
                "source_kind": "runtime.codex_cli.rollout_stream",
                "provider_namespace": "provider.openai",
                "runtime_namespace": "runtime.codex_cli",
                "payload": {"anthropic": {"record_type": "message"}},
            }
        )
        with self.assertRaisesRegex(ValueError, "payload namespace"):
            validate_adapter_output(codex_like_output, strict=True)

    def test_stale_provider_neutrality_rebuild_integration_boundary_marker_is_removed(self):
        self.assertFalse(hasattr(claude_local, "INTEGRATION_BOUNDARY"))

    def test_requires_explicit_path_and_does_not_open_home_claude_state(self):
        fixture_path = fixtures.fixture_path("claude_local_jsonl_minimal_structure") / "session.jsonl"
        real_open = builtins.open
        opened_paths = []

        def tracking_open(path, *args, **kwargs):
            opened_paths.append(str(path))
            blocked_fragments = (
                str(Path.home() / ".claude"),
                "hooks",
                "plugins",
                "skills",
                "credentials",
                "api",
            )
            if any(fragment in str(path) for fragment in blocked_fragments):
                raise AssertionError(f"adapter opened disallowed Claude surface: {path}")
            return real_open(path, *args, **kwargs)

        with mock.patch("builtins.open", tracking_open):
            output = claude_local.normalize_local_jsonl(fixture_path)

        self.assertEqual(output["sessions"][0]["session_id"], "claude-session-001")
        self.assertEqual(opened_paths, [str(fixture_path)])


if __name__ == "__main__":
    unittest.main()
