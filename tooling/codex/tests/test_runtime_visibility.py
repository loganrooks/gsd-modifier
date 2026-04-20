import json
import pathlib
import tempfile
import unittest

from tooling.codex import runtime_visibility as rv


class RuntimeVisibilityTests(unittest.TestCase):
    def test_normalize_overlay_text_replaces_tokens(self) -> None:
        repo_root = pathlib.Path("/tmp/example-repo")
        text = "__PROJECT_ROOT__ :: __COMPACT_PROMPT_FILE__"
        normalized = rv.normalize_overlay_text(text, repo_root, "tooling/compact-prompts/project.md")
        self.assertEqual(
            normalized,
            "/tmp/example-repo :: tooling/compact-prompts/project.md",
        )

    def test_classify_marks_obsolete_live_residue(self) -> None:
        classification, note = rv.classify(
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
        self.assertIn("outside overlay, manifest", note)

    def test_classify_keeps_manifest_tracked_live_only_as_selective(self) -> None:
        classification, note = rv.classify(
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
        self.assertIn("upstream-shipped surface", note)

    def test_build_report_records_scope_and_obsolete_count(self) -> None:
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

            self.assertEqual(report["normalized_overlay_sha_scope"], "checkout-local")
            self.assertEqual(report["summary"]["intentional_materialized_carry"], 1)
            self.assertEqual(report["summary"]["obsolete_live_residue"], 1)
            self.assertEqual(report["summary"]["unknown_live_drift"], 0)


if __name__ == "__main__":
    unittest.main()
