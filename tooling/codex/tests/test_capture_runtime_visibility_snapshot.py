import pathlib
import sys
import subprocess
import tempfile
import unittest
from unittest import mock

from harness_modifier.capture import capture_runtime_visibility_snapshot as crvs


class CaptureRuntimeVisibilitySnapshotTests(unittest.TestCase):
    def test_build_snapshot_captures_git_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            subprocess.run(["git", "init"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_root, check=True, capture_output=True)
            (repo_root / "README.md").write_text("test\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_root, check=True, capture_output=True)

            with mock.patch.object(
                crvs.runtime_visibility,
                "build_report",
                return_value={"runtime_scope": "both", "summary": {"total_entries": 1}},
            ):
                snapshot = crvs.build_snapshot(repo_root, "baseline", "snapshot note", runtime_scope="both")

            self.assertEqual(snapshot["label"], "baseline")
            self.assertEqual(snapshot["notes"], "snapshot note")
            self.assertEqual(snapshot["runtime_scope"], "both")
            self.assertEqual(snapshot["dirty_worktree"], False)
            self.assertRegex(snapshot["basis_commit"], r"^[0-9a-f]{40}$")
            self.assertIn("runtime_visibility_report", snapshot)
            self.assertEqual(snapshot["runtime_visibility_report"]["summary"]["total_entries"], 1)

    def test_script_invocation_by_path_writes_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            subprocess.run(["git", "init"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_root, check=True, capture_output=True)
            (repo_root / "README.md").write_text("test\n", encoding="utf-8")
            overlay_root = repo_root / "tooling" / "portable-gsd" / "overlay"
            live_root = repo_root / ".codex"
            overlay_root.mkdir(parents=True)
            live_root.mkdir(parents=True)
            (overlay_root / "config.toml").write_text("model = \"overlay\"\n", encoding="utf-8")
            (overlay_root / "OVERLAY-MANIFEST.json").write_text(
                "{\"schema_version\": 2, \"entries\": {\"config.toml\": \"add\"}}\n",
                encoding="utf-8",
            )
            (live_root / "config.toml").write_text("model = \"overlay\"\n", encoding="utf-8")
            (live_root / "gsd-file-manifest.json").write_text("{\"files\": [\"config.toml\"]}\n", encoding="utf-8")
            (live_root / "gsd-local-patches").mkdir(parents=True)
            (live_root / "gsd-local-patches" / "backup-meta.json").write_text("{\"files\": []}\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "add", "tooling", ".codex"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_root, check=True, capture_output=True)

            output_path = repo_root / "snapshot.json"
            script_path = pathlib.Path(crvs.__file__).resolve()
            subprocess.run(
                [
                    sys.executable,
                    str(script_path),
                    str(repo_root),
                    "--runtime",
                    "codex",
                    "--label",
                    "direct-script",
                    "--output",
                    str(output_path),
                ],
                cwd=repo_root,
                check=True,
                capture_output=True,
                text=True,
            )

            payload = output_path.read_text(encoding="utf-8")
            self.assertIn('"label": "direct-script"', payload)
            self.assertIn('"runtime_scope": "codex"', payload)
            self.assertIn('"runtime_visibility_report"', payload)


if __name__ == "__main__":
    unittest.main()
