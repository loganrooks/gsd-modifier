import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

from tooling.codex import portable_gsd_contract as pgc


class PortableGsdContractTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_validate_manifest_accepts_add_and_overwrite_split(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, "tooling/portable-gsd/overlay/config.toml", 'model = "gpt-5.4"\n')
            self._write(repo_root, "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md", "overlay\n")
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 1,
                        "entries": {
                            "config.toml": "add",
                            "get-shit-done/workflows/plan-phase.md": "overwrite",
                        },
                    }
                )
                + "\n",
            )
            self._write(
                repo_root,
                ".codex/gsd-local-patches/backup-meta.json",
                json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}) + "\n",
            )

            report = pgc.build_manifest_validation_report(repo_root)

            self.assertEqual(report["summary"]["overwrite_count"], 1)
            self.assertEqual(report["summary"]["add_count"], 1)
            self.assertEqual(report["hard_failures"], [])

    def test_validate_manifest_flags_add_paths_in_backup_meta(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, "tooling/portable-gsd/overlay/config.toml", 'model = "gpt-5.4"\n')
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps({"schema_version": 1, "entries": {"config.toml": "add"}}) + "\n",
            )
            self._write(repo_root, ".codex/gsd-local-patches/backup-meta.json", json.dumps({"files": ["config.toml"]}) + "\n")

            report = pgc.build_manifest_validation_report(repo_root)

            self.assertIn("config.toml", report["add_present_in_backup"])
            self.assertTrue(report["hard_failures"])

    def test_materialization_report_accepts_reasoning_default_mutations(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, "tooling/portable-gsd/overlay/config.toml", 'model = "gpt-5.4"\n')
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/agents/gsd-planner.toml",
                'description = "planner"\n',
            )
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                "Plan phase\n",
            )
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 1,
                        "entries": {
                            "agents/gsd-planner.toml": "add",
                            "config.toml": "add",
                            "get-shit-done/workflows/plan-phase.md": "overwrite",
                        },
                    }
                )
                + "\n",
            )
            self._write(
                repo_root,
                ".codex/gsd-local-patches/backup-meta.json",
                json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}) + "\n",
            )
            self._write(repo_root, ".codex/gsd-local-patches/get-shit-done/workflows/plan-phase.md", "upstream\n")
            self._write(repo_root, ".codex/config.toml", 'model = "gpt-5.4"\nmodel_reasoning_effort = "xhigh"\n')
            self._write(
                repo_root,
                ".codex/agents/gsd-planner.toml",
                'description = "planner"\nmodel_reasoning_effort = "xhigh"\n',
            )
            self._write(repo_root, ".codex/get-shit-done/workflows/plan-phase.md", "Plan phase\n")

            report = pgc.build_materialization_report(repo_root, pgc.DEFAULT_COMPACT_PROMPT_FILE)

            self.assertEqual(report["content_mismatch"], [])
            self.assertEqual(report["backup_copy_missing"], [])
            self.assertEqual(report["hard_failures"], [])

    def test_script_invocation_by_path_verifies_materialized_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md", "Plan phase\n")
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 1,
                        "entries": {"get-shit-done/workflows/plan-phase.md": "overwrite"},
                    }
                )
                + "\n",
            )
            self._write(
                repo_root,
                ".codex/gsd-local-patches/backup-meta.json",
                json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}) + "\n",
            )
            self._write(repo_root, ".codex/gsd-local-patches/get-shit-done/workflows/plan-phase.md", "upstream\n")
            self._write(repo_root, ".codex/get-shit-done/workflows/plan-phase.md", "Plan phase\n")

            output_path = repo_root / "report.json"
            script_path = pathlib.Path(pgc.__file__).resolve()
            subprocess.run(
                [
                    sys.executable,
                    str(script_path),
                    "verify-materialized",
                    str(repo_root),
                    "--output",
                    str(output_path),
                    "--strict",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            payload = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["summary"]["content_mismatch_count"], 0)
            self.assertEqual(payload["hard_failures"], [])


if __name__ == "__main__":
    unittest.main()
