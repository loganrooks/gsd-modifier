import json
import pathlib
import tempfile
import unittest

from harness_modifier.contract import runtime_visibility as rv


class RuntimeVisibilityTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _write_inject_fixture(self, repo_root: pathlib.Path, live_content: str) -> str:
        target = "get-shit-done/references/injected.md"
        marker_key = "GSD_MODIFIER:test:runtime-visibility"
        self._write(repo_root, "scripts/setup-portable-gsd.sh", 'quality_reasoning = {"gsd-planner": "xhigh"}\n')
        self._write(
            repo_root,
            "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
            json.dumps(
                {
                    "schema_version": 4,
                    "entries": {
                        target: {
                            "capability_id": target,
                            "parity_tier": "runtime_specific",
                            "parity_intent": "outcome_aligned",
                            "materializers": {
                                "codex": {
                                    "mode": "inject",
                                    "target": target,
                                    "operations": [
                                        {
                                            "kind": "block_replace",
                                            "start_anchor": "Anchor line\n",
                                            "end_anchor": "Anchor line\n",
                                            "source": "harness_modifier/overlay/inject-sources/injected.md",
                                            "marker_key": marker_key,
                                        }
                                    ],
                                }
                            },
                        }
                    },
                }
            ),
        )
        self._write(repo_root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1", "files": [target]}) + "\n")
        self._write(repo_root, ".codex/gsd-local-patches/backup-meta.json", json.dumps({"files": []}) + "\n")
        self._write(repo_root, f".codex/{target}", live_content)
        return target

    def test_normalize_overlay_text_replaces_tokens(self) -> None:
        repo_root = pathlib.Path("/tmp/example-repo")
        text = "__PROJECT_ROOT__ :: __COMPACT_PROMPT_FILE__"
        normalized = rv.normalize_overlay_text(text, repo_root, "tooling/compact-prompts/project.md")
        self.assertEqual(
            normalized,
            "/tmp/example-repo :: tooling/compact-prompts/project.md",
        )

    def test_classify_marks_obsolete_live_residue(self) -> None:
        classification, subclassification, note = rv.classify(
            family="workflow",
            rel_path="get-shit-done/workflows/legacy.md",
            overlay_exists=False,
            live_exists=True,
            in_manifest=False,
            in_backup_meta=False,
            is_install_mutation_target=False,
            raw_equal=False,
            normalized_equal=False,
            overlay_text=None,
            live_text="legacy",
        )
        self.assertEqual(classification, rv.OBSOLETE)
        self.assertEqual(subclassification, rv.SUB_OBSOLETE_UNTRACKED)
        self.assertIn("outside overlay, manifest", note)

    def test_classify_keeps_manifest_tracked_live_only_as_selective(self) -> None:
        classification, subclassification, note = rv.classify(
            family="workflow",
            rel_path="get-shit-done/workflows/plan-phase.md",
            overlay_exists=False,
            live_exists=True,
            in_manifest=True,
            in_backup_meta=False,
            is_install_mutation_target=False,
            raw_equal=False,
            normalized_equal=False,
            overlay_text=None,
            live_text="live",
        )
        self.assertEqual(classification, rv.SELECTIVE)
        self.assertEqual(subclassification, rv.SUB_SELECTIVE_UPSTREAM)
        self.assertIn("upstream-shipped surface", note)

    def test_build_report_records_scope_and_subclassification_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            overlay_workflows = repo_root / "tooling" / "portable-gsd" / "overlay" / "get-shit-done" / "workflows"
            live_workflows = repo_root / ".codex" / "get-shit-done" / "workflows"
            codex_root = repo_root / ".codex"
            (repo_root / "scripts").mkdir(parents=True)
            (codex_root / "gsd-local-patches").mkdir(parents=True)
            overlay_workflows.mkdir(parents=True)
            live_workflows.mkdir(parents=True)

            (repo_root / "scripts" / "setup-portable-gsd.sh").write_text(
                'quality_reasoning = {"gsd-planner": "xhigh"}\n',
                encoding="utf-8",
            )
            (repo_root / "tooling" / "portable-gsd" / "overlay" / "OVERLAY-MANIFEST.json").write_text(
                json.dumps(
                    {
                        "schema_version": 2,
                        "entries": {
                            "get-shit-done/workflows/plan-phase.md": "overwrite",
                        },
                    }
                ),
                encoding="utf-8",
            )
            (codex_root / "gsd-file-manifest.json").write_text(
                json.dumps({"version": "1", "timestamp": "now", "files": {}}),
                encoding="utf-8",
            )
            (codex_root / "gsd-local-patches" / "backup-meta.json").write_text(
                json.dumps(
                    {
                        "backed_up_at": "now",
                        "from_version": "1",
                        "from_manifest_timestamp": "now",
                        "files": [],
                        "pristine_hashes": {},
                    }
                ),
                encoding="utf-8",
            )

            overlay_text = "__PROJECT_ROOT__\n"
            live_text = f"{repo_root.resolve()}\n"
            (overlay_workflows / "plan-phase.md").write_text(overlay_text, encoding="utf-8")
            (live_workflows / "plan-phase.md").write_text(live_text, encoding="utf-8")
            (live_workflows / "legacy.md").write_text("legacy\n", encoding="utf-8")

            report = rv.build_report(repo_root)
            codex_report = report["runtimes"]["codex"]
            claude_report = report["runtimes"]["claude"]

            self.assertEqual(report["runtime_scope"], "both")
            self.assertEqual(report["parity_state"], "single-runtime")
            self.assertEqual(report["normalized_overlay_sha_scope"], "checkout-local")
            self.assertEqual(codex_report["summary"]["intentional_materialized_carry"], 1)
            self.assertEqual(codex_report["summary"]["obsolete_live_residue"], 1)
            self.assertEqual(codex_report["summary"]["unknown_live_drift"], 0)
            self.assertEqual(report["subclassification_summary"][rv.SUB_TEMPLATE_MATERIALIZATION], 1)
            self.assertEqual(report["subclassification_summary"][rv.SUB_OBSOLETE_UNTRACKED], 1)
            self.assertFalse(claude_report["present"])

    def test_build_report_verifies_inject_entry_without_source_path_read(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            target = self._write_inject_fixture(
                repo_root,
                "Anchor line\n"
                "<!-- GSD_MODIFIER:start key:GSD_MODIFIER:test:runtime-visibility -->\n"
                "Injected content\n"
                "<!-- GSD_MODIFIER:end key:GSD_MODIFIER:test:runtime-visibility -->\n",
            )

            report = rv.build_report(repo_root, runtime_scope="codex")
            codex_report = report["runtimes"]["codex"]
            entry = next(entry for entry in codex_report["entries"] if entry["rel_path"] == target)

            self.assertTrue(entry["overlay_exists"])
            self.assertIsNone(entry["overlay_path"])
            self.assertEqual(entry["mode"], "inject")
            self.assertEqual(entry["classification"], rv.INTENTIONAL)
            self.assertEqual(entry["subclassification"], rv.SUB_INJECT_VERIFIED)
            self.assertTrue(entry["inject_verification"]["passed"])
            self.assertEqual(codex_report["summary"]["unknown_live_drift"], 0)
            self.assertEqual(codex_report["summary"]["intentional_materialized_carry"], 1)

    def test_build_report_marks_failed_inject_verification_as_unknown_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            target = self._write_inject_fixture(repo_root, "Anchor line\nInjected content without marker\n")

            report = rv.build_report(repo_root, runtime_scope="codex")
            codex_report = report["runtimes"]["codex"]
            entry = next(entry for entry in codex_report["entries"] if entry["rel_path"] == target)

            self.assertTrue(entry["overlay_exists"])
            self.assertIsNone(entry["overlay_path"])
            self.assertEqual(entry["classification"], rv.UNKNOWN)
            self.assertEqual(entry["subclassification"], rv.SUB_INJECT_UNVERIFIED)
            self.assertFalse(entry["inject_verification"]["passed"])
            self.assertIn("missing_marker", entry["note"])
            self.assertEqual(codex_report["summary"]["unknown_live_drift"], 1)

    def test_build_report_marks_dual_runtime_read_side_when_both_runtimes_exist_without_markers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            overlay_root = repo_root / "tooling" / "portable-gsd" / "overlay"
            overlay_root.mkdir(parents=True)
            (overlay_root / "get-shit-done" / "workflows").mkdir(parents=True)
            (overlay_root / "OVERLAY-MANIFEST.json").write_text(
                json.dumps(
                    {
                        "schema_version": 3,
                        "entries": {
                            "get-shit-done/workflows/plan-phase.md": {
                                "capability_id": "get-shit-done/workflows/plan-phase.md",
                                "parity_tier": "core_required",
                                "materializers": {
                                    "codex": {
                                        "mode": "overwrite",
                                        "target": "get-shit-done/workflows/plan-phase.md",
                                        "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                    },
                                    "claude": {
                                        "mode": "overwrite",
                                        "target": "get-shit-done/workflows/plan-phase.md",
                                        "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                    },
                                },
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                "Plan phase\n",
            )
            self._write(repo_root, "scripts/setup-portable-gsd.sh", 'quality_reasoning = {"gsd-planner": "xhigh"}\n')

            for runtime in ("codex", "claude"):
                runtime_root = repo_root / f".{runtime}"
                self._write(
                    repo_root,
                    f".{runtime}/gsd-file-manifest.json",
                    json.dumps({"version": "1", "files": ["get-shit-done/workflows/plan-phase.md"]}) + "\n",
                )
                self._write(repo_root, f".{runtime}/get-shit-done/VERSION", "1\n")
                self._write(
                    repo_root,
                    f".{runtime}/get-shit-done/workflows/plan-phase.md",
                    "Plan phase\n",
                )
                runtime_root.mkdir(parents=True, exist_ok=True)

            report = rv.build_report(repo_root)

            self.assertEqual(report["parity_state"], "dual-runtime-read-side")
            self.assertEqual(report["summary"]["present_runtime_count"], 2)
            self.assertEqual(report["summary"]["read_side_runtime_count"], 2)

    def test_build_report_for_runtime_roots_reads_modifier_and_host_separately(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            modifier_root = root / "modifier"
            host_root = root / "host"
            overlay_workflows = modifier_root / "tooling" / "portable-gsd" / "overlay" / "get-shit-done" / "workflows"
            live_workflows = host_root / ".codex" / "get-shit-done" / "workflows"
            (modifier_root / "scripts").mkdir(parents=True)
            (host_root / ".codex" / "gsd-local-patches").mkdir(parents=True)
            overlay_workflows.mkdir(parents=True)
            live_workflows.mkdir(parents=True)

            (modifier_root / "scripts" / "setup-portable-gsd.sh").write_text(
                'quality_reasoning = {"gsd-planner": "xhigh"}\n',
                encoding="utf-8",
            )
            (modifier_root / "tooling" / "portable-gsd" / "overlay" / "OVERLAY-MANIFEST.json").write_text(
                json.dumps(
                    {
                        "schema_version": 2,
                        "entries": {
                            "get-shit-done/workflows/plan-phase.md": "overwrite",
                        },
                    }
                ),
                encoding="utf-8",
            )
            (host_root / ".codex" / "gsd-file-manifest.json").write_text(
                json.dumps({"version": "1", "timestamp": "now", "files": {}}),
                encoding="utf-8",
            )
            (host_root / ".codex" / "gsd-local-patches" / "backup-meta.json").write_text(
                json.dumps({"files": []}),
                encoding="utf-8",
            )

            (overlay_workflows / "plan-phase.md").write_text("__PROJECT_ROOT__\n", encoding="utf-8")
            (live_workflows / "plan-phase.md").write_text(f"{modifier_root.resolve()}\n", encoding="utf-8")

            report = rv.build_report_for_runtime_roots(modifier_root, host_root, runtime_scope="codex")
            codex_report = report["runtimes"]["codex"]

            self.assertEqual(report["modifier_repo_root"], str(modifier_root))
            self.assertEqual(report["live_repo_root"], str(host_root))
            self.assertEqual(codex_report["summary"]["intentional_materialized_carry"], 1)
            self.assertEqual(report["parity_state"], "single-runtime")


if __name__ == "__main__":
    unittest.main()
