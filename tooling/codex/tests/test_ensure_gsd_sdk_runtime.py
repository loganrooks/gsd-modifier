import os
import pathlib
import tempfile
import unittest

from tooling.codex import ensure_gsd_sdk_runtime as egsr


class EnsureGsdSdkRuntimeTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str, mode: int = 0o644) -> pathlib.Path:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        path.chmod(mode)
        return path

    def test_build_report_marks_healthy_when_command_is_executable(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._write(
                root,
                "bin/gsd-sdk",
                "#!/bin/sh\nprintf 'gsd-sdk v0.1.0\\n'\n",
                mode=0o755,
            )
            env = {"PATH": str(root / "bin")}

            report = egsr.build_report(env=env)

            self.assertEqual(report["status"], "healthy")
            self.assertEqual(report["final_exec"]["returncode"], 0)
            self.assertIsNone(report["repair_action"])

    def test_build_report_repairs_non_executable_symlink_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            target = self._write(
                root,
                "pkg/cli.js",
                "#!/usr/bin/env node\nconsole.log('gsd-sdk v0.1.0')\n",
                mode=0o600,
            )
            bin_dir = root / "bin"
            bin_dir.mkdir(parents=True, exist_ok=True)
            (bin_dir / "gsd-sdk").symlink_to(target)
            self._write(
                root,
                "bin/node",
                "#!/bin/sh\nprintf 'gsd-sdk v0.1.0\\n'\n",
                mode=0o755,
            )
            env = {"PATH": str(bin_dir)}

            report = egsr.build_report(env=env)

            self.assertEqual(report["status"], "repaired")
            self.assertEqual(report["repair_action"]["action"], "chmod_target_executable")
            self.assertEqual(report["repair_action"]["after_mode"], "0o755")
            self.assertTrue(os.access(target, os.X_OK))
            self.assertEqual(report["final_exec"]["returncode"], 0)

    def test_build_report_stays_unresolved_without_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            env = {"PATH": tmpdir}

            report = egsr.build_report(env=env, allow_repair=False)

            self.assertEqual(report["status"], "unresolved_no_candidate")
            self.assertEqual(report["final_command_v"]["returncode"], 127)
            self.assertFalse(any(candidate["exists"] for candidate in report["candidates"]))


if __name__ == "__main__":
    unittest.main()
