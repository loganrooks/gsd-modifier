import json
import pathlib
import tempfile
import unittest
from unittest import mock

from harness_modifier.compatibility import declaration as compatibility_declaration
from harness_modifier.contract import harness_canary as hc
from harness_modifier.contract import portable_gsd_contract as pgc


class HarnessCanaryTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _repo_fixture(self, root: pathlib.Path) -> None:
        declaration = compatibility_declaration.load_declaration()
        self._write(
            root,
            "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
            json.dumps(
                {
                    "schema_version": 1,
                    "entries": {
                        "config.toml": "add",
                        "agents/gsd-executor.toml": "add",
                        "agents/gsd-planner.toml": "add",
                    },
                }
            )
            + "\n",
        )
        self._write(root, ".codex/gsd-local-patches/backup-meta.json", json.dumps({"files": []}) + "\n")
        self._write(root, "tooling/portable-gsd/overlay/config.toml", 'model = "gpt-5.4"\n')
        self._write(root, "tooling/portable-gsd/overlay/agents/gsd-planner.toml", 'description = "planner"\n')
        self._write(root, "tooling/portable-gsd/overlay/agents/gsd-executor.toml", 'description = "executor"\n')
        self._write(root, ".codex/config.toml", 'model = "gpt-5.4"\nmodel_reasoning_effort = "xhigh"\n')
        self._write(
            root,
            ".codex/agents/gsd-planner.toml",
            'description = "planner"\nmodel_reasoning_effort = "xhigh"\n',
        )
        self._write(
            root,
            ".codex/agents/gsd-executor.toml",
            'description = "executor"\nmodel_reasoning_effort = "high"\n',
        )
        self._write(root, ".codex/get-shit-done/VERSION", "1.38.3\n")
        self._write(root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")
        self._write(
            root,
            ".planning/UPLIFT-MANIFEST.json",
            json.dumps(
                {
                    "compatibility_basis": {
                        "compatibility_posture": declaration["compatibility_posture"],
                        "compatibility_declaration_path": compatibility_declaration.DECLARATION_REL_PATH,
                        "compatibility_declaration_schema_version": declaration["schema_version"],
                        "runtime_basis": declaration["runtime_basis"],
                        "runtime_held_annotations": declaration["runtime_held_annotations"],
                        "observed_runtime_version": "1.38.3",
                        "observed_runtime_manifest_version": "1.38.3",
                        "observed_runtime_version_source": ".codex/get-shit-done/VERSION",
                        "observed_runtime_manifest_source": ".codex/gsd-file-manifest.json",
                        "observed_runtime_version_aligned": True,
                        "declared_overlay_schema_version": declaration["overlay_schema_version"],
                        "overlay_manifest_schema_version": 1,
                        "overlay_manifest_schema_version_matches_declaration": True,
                        "upstream_compatibility_window": declaration["upstream_compatibility_window"],
                        "parity_scan_baseline": {
                            "target_runtime": declaration["parity_scan_baseline"]["target_runtime"],
                            "rule_count": len(declaration["parity_scan_baseline"]["rules"]),
                        },
                    }
                }
            )
            + "\n",
        )

    def test_build_report_is_clean_for_bounded_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._repo_fixture(repo_root)

            with mock.patch.dict(pgc.QUALITY_REASONING, {"gsd-planner": "xhigh", "gsd-executor": "high"}, clear=True):
                report = hc.build_report(repo_root)

            self.assertEqual(report["summary"]["status"], "ok")
            self.assertEqual(report["summary"]["issue_count"], 0)
            self.assertEqual(report["summary"]["not_applicable_count"], 0)

    def test_build_report_surfaces_reasoning_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._repo_fixture(repo_root)
            self._write(
                repo_root,
                ".codex/agents/gsd-executor.toml",
                'description = "executor"\nmodel_reasoning_effort = "xhigh"\n',
            )

            with mock.patch.dict(pgc.QUALITY_REASONING, {"gsd-planner": "xhigh", "gsd-executor": "high"}, clear=True):
                report = hc.build_report(repo_root)

            self.assertEqual(report["summary"]["status"], "issue")
            failing = {check["name"]: check for check in report["checks"] if check["status"] == "issue"}
            self.assertIn("agent_reasoning:gsd-executor", failing)

    def test_build_report_surfaces_uplift_compatibility_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._repo_fixture(repo_root)
            self._write(root=repo_root, rel_path=".codex/get-shit-done/VERSION", text="1.39.0\n")
            self._write(root=repo_root, rel_path=".codex/gsd-file-manifest.json", text=json.dumps({"version": "1.39.0"}) + "\n")

            with mock.patch.dict(pgc.QUALITY_REASONING, {"gsd-planner": "xhigh", "gsd-executor": "high"}, clear=True):
                report = hc.build_report(repo_root)

            failing = {check["name"]: check for check in report["checks"] if check["status"] == "issue"}
            self.assertIn("uplift_compatibility_anchor", failing)


if __name__ == "__main__":
    unittest.main()
