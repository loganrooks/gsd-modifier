import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

from harness_modifier.contract import manifest_install_coherence as mic
from harness_modifier.contract import runtime_visibility as rv


class ManifestInstallCoherenceTests(unittest.TestCase):
    def _init_repo(self, repo_root: pathlib.Path) -> None:
        subprocess.run(["git", "init"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.name", "Test User"], cwd=repo_root, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo_root, check=True, capture_output=True)

    def _snapshot_payload(self) -> dict:
        return {
            "label": "baseline",
            "runtime_scope": "codex",
            "basis_commit": "deadbeef" * 5,
            "dirty_worktree": False,
            "runtime_visibility_report": {
                "runtime_scope": "codex",
                "parity_state": "single-runtime",
                "parity_details": {
                    "parity_state": "single-runtime",
                    "present_runtimes": ["codex"],
                    "missing_runtimes": [],
                    "read_side_runtimes": [],
                    "conflicting_runtimes": [],
                    "version_alignment": {"aligned": True, "values": {"codex": "1.38.3"}},
                    "manifest_alignment": {"aligned": True, "values": {"codex": "1.38.3"}},
                    "notes": [],
                },
                "summary": {
                    "total_entries": 3,
                    "intentional_materialized_carry": 1,
                    "repo_local_config_carry": 0,
                    "selective_overlay_boundary": 2,
                    "obsolete_live_residue": 0,
                    "unknown_live_drift": 0,
                    "requested_runtime_count": 1,
                    "present_runtime_count": 1,
                    "present_runtimes": ["codex"],
                    "missing_runtimes": [],
                    "read_side_runtime_count": 0,
                    "dual_runtime_version_aligned": True,
                    "dual_runtime_manifest_aligned": True,
                },
                "subclassification_summary": {
                    rv.SUB_TEMPLATE_MATERIALIZATION: 1,
                    rv.SUB_SELECTIVE_INSTALL: 1,
                    rv.SUB_SELECTIVE_UNTRACKED: 1,
                },
                "runtimes": {
                    "codex": {
                        "runtime": "codex",
                        "present": True,
                        "has_modifier_materialization_marker": True,
                        "summary": {
                            "total_entries": 3,
                            "intentional_materialized_carry": 1,
                            "repo_local_config_carry": 0,
                            "selective_overlay_boundary": 2,
                            "obsolete_live_residue": 0,
                            "unknown_live_drift": 0,
                        },
                        "subclassification_summary": {
                            rv.SUB_TEMPLATE_MATERIALIZATION: 1,
                            rv.SUB_SELECTIVE_INSTALL: 1,
                            rv.SUB_SELECTIVE_UNTRACKED: 1,
                        },
                        "entries": [
                            {
                                "family": "workflow",
                                "rel_path": "get-shit-done/workflows/plan-phase.md",
                                "overlay_exists": True,
                                "live_exists": True,
                                "in_manifest": True,
                                "in_backup_meta": True,
                                "is_install_mutation_target": False,
                                "classification": rv.INTENTIONAL,
                                "subclassification": rv.SUB_TEMPLATE_MATERIALIZATION,
                            },
                            {
                                "family": "agent_toml",
                                "rel_path": "agents/gsd-planner.toml",
                                "overlay_exists": False,
                                "live_exists": True,
                                "in_manifest": False,
                                "in_backup_meta": False,
                                "is_install_mutation_target": True,
                                "classification": rv.SELECTIVE,
                                "subclassification": rv.SUB_SELECTIVE_INSTALL,
                            },
                            {
                                "family": "agent_toml",
                                "rel_path": "agents/gsd-pattern-mapper.toml",
                                "overlay_exists": False,
                                "live_exists": True,
                                "in_manifest": False,
                                "in_backup_meta": False,
                                "is_install_mutation_target": False,
                                "classification": rv.SELECTIVE,
                                "subclassification": rv.SUB_SELECTIVE_UNTRACKED,
                            },
                        ],
                    }
                },
            },
        }

    def test_build_report_summarizes_three_surface_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = pathlib.Path(tmpdir)
            repo_root = tmp_path / "repo"
            repo_root.mkdir()
            self._init_repo(repo_root)
            live_root = repo_root / ".codex"
            (live_root / "gsd-local-patches").mkdir(parents=True)
            (repo_root / "scripts").mkdir(parents=True)

            (repo_root / "scripts" / "setup-portable-gsd.sh").write_text(
                'quality_reasoning = {"gsd-planner": "xhigh"}\n',
                encoding="utf-8",
            )
            (live_root / "gsd-file-manifest.json").write_text(
                json.dumps({"files": ["get-shit-done/workflows/plan-phase.md", "get-shit-done/references/planner-reviews.md"]}),
                encoding="utf-8",
            )
            (live_root / "gsd-local-patches" / "backup-meta.json").write_text(
                json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}),
                encoding="utf-8",
            )
            (repo_root / "README.md").write_text("test\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_root, check=True, capture_output=True)

            snapshot_path = tmp_path / "snapshot.json"
            snapshot_path.write_text(json.dumps(self._snapshot_payload()), encoding="utf-8")

            report = mic.build_report(repo_root, snapshot_path, runtime_scope="codex")

            self.assertEqual(report["requested_runtime_scope"], "codex")
            self.assertEqual(report["overlap_summary"]["manifest_total_files"], 2)
            self.assertEqual(report["overlap_summary"]["backup_total_files"], 1)
            self.assertEqual(report["overlap_summary"]["selected_scope_entries_in_manifest"], 1)
            self.assertEqual(report["overlap_summary"]["selected_scope_entries_in_backup_meta"], 1)
            self.assertEqual(report["overlap_summary"]["selected_scope_entries_install_mutation_targets"], 1)
            self.assertEqual(report["candidate_future_overlay_carry"], ["agents/gsd-pattern-mapper.toml"])
            self.assertEqual(report["install_mutation_outside_overlay_subset"], ["agents/gsd-planner.toml"])
            self.assertFalse(report["hard_failures"])

    def test_evaluate_gates_fails_dirty_or_unknown_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._init_repo(repo_root)
            (repo_root / "README.md").write_text("test\n", encoding="utf-8")
            subprocess.run(["git", "add", "README.md"], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_root, check=True, capture_output=True)

            snapshot_payload = {
                "basis_commit": "deadbeef",
                "dirty_worktree": True,
            }
            runtime_report = {
                "summary": {
                    "unknown_live_drift": 1,
                    "obsolete_live_residue": 0,
                },
                "parity_state": "single-runtime",
            }

            gates = mic.evaluate_gates(
                snapshot_payload,
                runtime_report,
                repo_root,
                captured_runtimes={"codex"},
                requested_runtimes={"codex"},
            )
            failed = {gate["name"] for gate in gates if not gate["passed"]}

            self.assertIn("snapshot_clean_boundary", failed)
            self.assertIn("selected_scope_unknown_drift_zero", failed)

    def test_script_invocation_by_path_writes_report(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = pathlib.Path(tmpdir)
            repo_root = tmp_path / "repo"
            repo_root.mkdir()
            self._init_repo(repo_root)
            live_root = repo_root / ".codex"
            (live_root / "gsd-local-patches").mkdir(parents=True)
            (repo_root / "scripts").mkdir(parents=True)

            (repo_root / "scripts" / "setup-portable-gsd.sh").write_text(
                'quality_reasoning = {"gsd-planner": "xhigh"}\n',
                encoding="utf-8",
            )
            (live_root / "gsd-file-manifest.json").write_text(
                json.dumps({"files": ["get-shit-done/workflows/plan-phase.md"]}),
                encoding="utf-8",
            )
            (live_root / "gsd-local-patches" / "backup-meta.json").write_text(
                json.dumps({"files": []}),
                encoding="utf-8",
            )
            (repo_root / "README.md").write_text("test\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=repo_root, check=True, capture_output=True)
            subprocess.run(["git", "commit", "-m", "init"], cwd=repo_root, check=True, capture_output=True)

            snapshot_path = tmp_path / "snapshot.json"
            snapshot_path.write_text(json.dumps(self._snapshot_payload()), encoding="utf-8")
            output_path = tmp_path / "report.json"
            script_path = pathlib.Path(mic.__file__).resolve()

            subprocess.run(
                [
                    sys.executable,
                    str(script_path),
                    str(repo_root),
                    "--snapshot",
                    str(snapshot_path),
                    "--runtime",
                    "codex",
                    "--output",
                    str(output_path),
                    "--strict",
                ],
                cwd=repo_root,
                check=True,
                capture_output=True,
                text=True,
            )

            payload = output_path.read_text(encoding="utf-8")
            self.assertIn('"hard_failures": []', payload)
            self.assertIn('"requested_runtime_scope": "codex"', payload)


if __name__ == "__main__":
    unittest.main()
