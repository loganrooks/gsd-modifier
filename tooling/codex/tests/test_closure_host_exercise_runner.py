import json
import pathlib
import subprocess
import tempfile
import unittest

from harness_modifier.closure import host_exercise_runner


class ClosureHostExerciseRunnerTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _init_git_repo(self, root: pathlib.Path) -> None:
        subprocess.run(["git", "init"], cwd=root, check=True, capture_output=True, text=True)
        subprocess.run(
            ["git", "add", "."],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(
            [
                "git",
                "-c",
                "user.name=Codex Test",
                "-c",
                "user.email=codex@example.com",
                "commit",
                "-m",
                "fixture baseline",
            ],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_detect_reflect_artifacts_finds_paths_and_tokens(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            host_root = pathlib.Path(tmpdir)
            self._write(host_root, ".planning/knowledge-base/index.json", "{}\n")
            self._write(host_root, ".codex/config.toml", "hook = session_meta_postlude\n")

            findings = host_exercise_runner.detect_reflect_artifacts(
                host_root,
                {
                    "reflect_artifact_abort_list": [
                        ".planning/knowledge-base/",
                        "session_meta_postlude",
                    ]
                },
            )

            self.assertEqual(len(findings), 2)
            self.assertEqual(findings[0]["kind"], "path")
            self.assertEqual(findings[1]["kind"], "token")

    def test_run_host_exercise_writes_packet_observation_and_runtime_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            modifier_root = root / "modifier"
            host_root = root / "host"
            output_dir = root / "audit-out"

            self._write(modifier_root, "tooling/portable-gsd/overlay/config.toml", 'model = "gpt-5.4"\n')
            self._write(
                modifier_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps({"schema_version": 2, "entries": {"config.toml": "add"}}) + "\n",
            )
            self._write(modifier_root, ".codex/get-shit-done/VERSION", "1.38.3\n")
            self._write(
                modifier_root,
                ".codex/gsd-file-manifest.json",
                json.dumps({"version": "1.38.3"}) + "\n",
            )
            self._write(host_root, ".codex/get-shit-done/workflows/plan-phase.md", "Plan phase\n")
            self._write(host_root, ".codex/get-shit-done/VERSION", "1.38.3\n")
            self._write(
                host_root,
                ".codex/gsd-file-manifest.json",
                json.dumps({"version": "1.38.3"}) + "\n",
            )
            self._write(host_root, "README.md", "# Host Fixture\n")
            self._init_git_repo(host_root)

            outputs = host_exercise_runner.run_host_exercise(
                modifier_repo_root=modifier_root,
                host_repo_root=host_root,
                output_dir=output_dir,
                exercise_id="exercise-001",
                host_reference="fixture-host",
                host_age_posture="pristine",
                narrative_summary="Fixture host remains regular-GSD-only, so the run stayed read-side.",
            )

            packet = json.loads(outputs["packet_path"].read_text(encoding="utf-8"))
            observation = json.loads(outputs["observation_path"].read_text(encoding="utf-8"))
            snapshot = json.loads(outputs["runtime_visibility_snapshot_path"].read_text(encoding="utf-8"))
            verify_summary = outputs["verify_materialized_summary_path"].read_text(encoding="utf-8")

            self.assertEqual(packet["packet_id"], "exercise-001")
            self.assertEqual(packet["host_reference"], "fixture-host")
            self.assertEqual(packet["declaration_capture"]["compatibility_window_state"], "inside-window")
            self.assertNotIn("manifest_install_coherence_if_materialized", packet["preflight_reads"])
            self.assertEqual(observation["exercise_id"], "exercise-001")
            self.assertEqual(observation["disposition"], "shift-mode")
            self.assertEqual(observation["narrative_summary"], "Fixture host remains regular-GSD-only, so the run stayed read-side.")
            compatibility_rows = [
                row for row in observation["expectation_vs_observation"] if row["check"] == "compatibility_window"
            ]
            verify_rows = [
                row for row in observation["expectation_vs_observation"] if row["check"] == "verify_materialized"
            ]
            self.assertEqual(compatibility_rows[0]["check_outcome"], "accept")
            self.assertEqual(verify_rows[0]["skip_reason"], "context_deferred")
            self.assertEqual(
                observation["semantic_deviation"][0]["signal_subtype"],
                "contract-mismatch",
            )
            self.assertEqual(snapshot["modifier_repo_root"], str(modifier_root))
            self.assertEqual(snapshot["host_repo_root"], str(host_root))
            self.assertIn("status: `skipped`", verify_summary)
            self.assertIn("packet_path", observation["measurement_provenance"]["about_work"])


if __name__ == "__main__":
    unittest.main()
