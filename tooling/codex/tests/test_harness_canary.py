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
        self._write(root, ".claude/get-shit-done/VERSION", "1.38.3\n")
        self._write(root, ".claude/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")
        self._write(
            root,
            ".planning/UPLIFT-MANIFEST.json",
            json.dumps(
                {
                    "compatibility_basis": {
                        "compatibility_posture": declaration["compatibility_posture"],
                        "compatibility_declaration_path": compatibility_declaration.DECLARATION_REL_PATH,
                    }
                }
            )
            + "\n",
        )

    def _clean_runtime_visibility_report(self) -> dict:
        return {
            "parity_state": "dual-runtime-aligned",
            "summary": {"present_runtime_count": 2},
            "parity_details": {
                "parity_state": "dual-runtime-aligned",
                "present_runtimes": ["codex", "claude"],
                "missing_runtimes": [],
                "read_side_runtimes": [],
                "conflicting_runtimes": [],
                "version_alignment": {"aligned": True, "values": {"codex": "1.38.3", "claude": "1.38.3"}},
                "manifest_alignment": {"aligned": True, "values": {"codex": "1.38.3", "claude": "1.38.3"}},
                "notes": [],
            },
        }

    def _clean_contract_report(self) -> dict:
        return {"summary": {}, "hard_failures": []}

    def test_build_report_is_clean_for_bounded_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._repo_fixture(repo_root)

            with (
                mock.patch.dict(pgc.QUALITY_REASONING, {"gsd-planner": "xhigh", "gsd-executor": "high"}, clear=True),
                mock.patch.object(hc.pgc, "build_manifest_validation_report", return_value=self._clean_contract_report()),
                mock.patch.object(hc.pgc, "build_materialization_report", return_value=self._clean_contract_report()),
                mock.patch.object(hc.rv, "build_report", return_value=self._clean_runtime_visibility_report()),
                mock.patch.object(hc.pu, "build_progress_note", return_value={"compatibility_basis_changed": False, "reasons": []}),
            ):
                report = hc.build_report(repo_root)

            self.assertEqual(report["summary"]["status"], "ok")
            self.assertEqual(report["summary"]["issue_count"], 0)
            self.assertEqual(report["summary"]["not_applicable_count"], 3)
            self.assertEqual(report["parity_state"], "dual-runtime-aligned")

    def test_build_report_surfaces_reasoning_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._repo_fixture(repo_root)
            self._write(
                repo_root,
                ".codex/agents/gsd-executor.toml",
                'description = "executor"\nmodel_reasoning_effort = "xhigh"\n',
            )

            with (
                mock.patch.dict(pgc.QUALITY_REASONING, {"gsd-planner": "xhigh", "gsd-executor": "high"}, clear=True),
                mock.patch.object(hc.pgc, "build_manifest_validation_report", return_value=self._clean_contract_report()),
                mock.patch.object(hc.pgc, "build_materialization_report", return_value=self._clean_contract_report()),
                mock.patch.object(hc.rv, "build_report", return_value=self._clean_runtime_visibility_report()),
                mock.patch.object(hc.pu, "build_progress_note", return_value={"compatibility_basis_changed": False, "reasons": []}),
            ):
                report = hc.build_report(repo_root)

            self.assertEqual(report["summary"]["status"], "issue")
            failing = {
                check["name"]: check
                for check in report["runtimes"]["codex"]["checks"]
                if check["status"] == "issue"
            }
            self.assertIn("codex:agent_reasoning:gsd-executor", failing)

    def test_build_report_surfaces_uplift_compatibility_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._repo_fixture(repo_root)

            with (
                mock.patch.dict(pgc.QUALITY_REASONING, {"gsd-planner": "xhigh", "gsd-executor": "high"}, clear=True),
                mock.patch.object(hc.pgc, "build_manifest_validation_report", return_value=self._clean_contract_report()),
                mock.patch.object(hc.pgc, "build_materialization_report", return_value=self._clean_contract_report()),
                mock.patch.object(hc.rv, "build_report", return_value=self._clean_runtime_visibility_report()),
                mock.patch.object(
                    hc.pu,
                    "build_progress_note",
                    return_value={"compatibility_basis_changed": True, "reasons": ["runtime moved"]},
                ),
            ):
                report = hc.build_report(repo_root)

            failing = {check["name"]: check for check in report["checks"] if check["status"] == "issue"}
            self.assertIn("uplift_compatibility_anchor", failing)


if __name__ == "__main__":
    unittest.main()
