import json
import pathlib
import tempfile
import unittest

from harness_modifier.closure import host_exercise_packet
from harness_modifier.closure import host_exercise_packet_writer


class ClosureHostExercisePacketWriterTests(unittest.TestCase):
    def _payload(self) -> dict:
        return {
            "packet_id": "packet-001",
            "target_host_class": "codex-disjoint-gsd-installed-no-reflect",
            "host_reference": "demo-host",
            "host_repo_path": "/tmp/demo-host",
            "runtime_class": "codex-only",
            "host_shape": "disjoint-codex-only",
            "host_has_regular_gsd": True,
            "host_has_reflect_artifacts": False,
            "host_has_reflect_artifacts_rationale": "No Reflect-specific commands, KB, or hooks found.",
            "host_age_posture": "lightly-aged",
            "declaration_capture": {
                "basis_commit": "7f10904",
                "dirty_worktree": False,
            },
            "output_targets": {
                "observation_record_path": "audit/observations/packet-001.json",
                "runtime_visibility_snapshot_path": "audit/runtime/packet-001.json",
                "verify_materialized_summary": "audit/runtime/packet-001-summary.md",
            },
        }

    def test_policy_loads_expected_shape(self) -> None:
        policy = host_exercise_packet.load_host_exercise_packet()
        self.assertEqual(policy["bundle_family"], "responsible-closure")
        self.assertEqual(policy["exercise_mode"], "observe-only")
        self.assertIn("codex-disjoint-gsd-installed-no-reflect", policy["target_host_class_vocab"])
        self.assertIn("level-1", policy["automation_skip_reasons"])
        self.assertIn("reflect_artifact_presence", policy["abort_condition_codes"])

    def test_write_host_exercise_packet_applies_defaults(self) -> None:
        payload = self._payload()
        with tempfile.TemporaryDirectory() as tmpdir:
            target = pathlib.Path(tmpdir) / "packet.json"
            written = host_exercise_packet_writer.write_host_exercise_packet(target, payload)

            self.assertEqual(written["packet_version"], 1)
            self.assertEqual(written["bundle_family"], "responsible-closure")
            self.assertEqual(written["exercise_mode"], "observe-only")
            self.assertEqual(
                written["declaration_capture"]["declaration_posture"],
                "observed_basis_only",
            )
            self.assertEqual(
                written["declaration_capture"]["observed_basis_runtime"],
                ".codex",
            )
            self.assertEqual(
                written["declaration_capture"]["compatibility_window_state"],
                "unknown",
            )
            self.assertIn("runtime_visibility", written["preflight_reads"])
            self.assertIn("reflect_artifact_presence", written["abort_conditions"])

            on_disk = json.loads(target.read_text(encoding="utf-8"))
            self.assertEqual(on_disk["packet_id"], "packet-001")

    def test_validate_rejects_unknown_target_host_class(self) -> None:
        payload = self._payload()
        payload["target_host_class"] = "unknown-host"
        with self.assertRaisesRegex(ValueError, "target_host_class"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_reflect_artifact_host_for_first_slice(self) -> None:
        payload = self._payload()
        payload["host_has_reflect_artifacts"] = True
        with self.assertRaisesRegex(ValueError, "Reflect artifacts"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_missing_required_preflight_read(self) -> None:
        payload = self._payload()
        payload["preflight_reads"] = [
            "compatibility_declaration",
            "overlay_install_contract",
        ]
        with self.assertRaisesRegex(ValueError, "missing required preflight reads"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_incomplete_abort_conditions(self) -> None:
        payload = self._payload()
        payload["abort_conditions"] = [
            "outside_compatibility_window",
            "dirty_worktree",
        ]
        with self.assertRaisesRegex(ValueError, "abort_conditions must match"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_same_repo_host_path(self) -> None:
        payload = self._payload()
        payload["host_repo_path"] = str(pathlib.Path(__file__).resolve().parents[3])
        with self.assertRaisesRegex(ValueError, "disjoint from prix-guesser"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_dirty_worktree_capture(self) -> None:
        payload = self._payload()
        payload["declaration_capture"]["dirty_worktree"] = True
        with self.assertRaisesRegex(ValueError, "clean worktree"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_unknown_basis_commit_marker(self) -> None:
        payload = self._payload()
        payload["declaration_capture"]["basis_commit"] = "unknown"
        with self.assertRaisesRegex(ValueError, "known basis commit"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_duplicate_preflight_read(self) -> None:
        payload = self._payload()
        payload["preflight_reads"] = [
            "compatibility_declaration",
            "overlay_install_contract",
            "runtime_visibility",
            "runtime_visibility",
        ]
        with self.assertRaisesRegex(ValueError, "preflight_reads entries must be unique"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)

    def test_validate_rejects_duplicate_abort_condition(self) -> None:
        payload = self._payload()
        payload["abort_conditions"] = [
            "outside_compatibility_window",
            "dirty_worktree",
            "unknown_basis_commit",
            "requires_write_side_install_mutation",
            "single_writer_host_governance_touch",
            "reflect_artifact_presence",
            "reflect_artifact_presence",
        ]
        with self.assertRaisesRegex(ValueError, "abort_conditions entries must be unique"):
            host_exercise_packet_writer.validate_host_exercise_packet(payload)


if __name__ == "__main__":
    unittest.main()
