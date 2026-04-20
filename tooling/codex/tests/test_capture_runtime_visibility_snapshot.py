import pathlib
import subprocess
import tempfile
import unittest
from unittest import mock

from tooling.codex import capture_runtime_visibility_snapshot as crvs


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

            with mock.patch.object(crvs.runtime_visibility, "build_report", return_value={"summary": {"total_entries": 1}}):
                snapshot = crvs.build_snapshot(repo_root, "baseline", "snapshot note")

            self.assertEqual(snapshot["label"], "baseline")
            self.assertEqual(snapshot["notes"], "snapshot note")
            self.assertEqual(snapshot["dirty_worktree"], False)
            self.assertRegex(snapshot["basis_commit"], r"^[0-9a-f]{40}$")
            self.assertIn("runtime_visibility_report", snapshot)
            self.assertEqual(snapshot["runtime_visibility_report"]["summary"]["total_entries"], 1)


if __name__ == "__main__":
    unittest.main()
