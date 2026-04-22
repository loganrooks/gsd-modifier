import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

from harness_modifier.contract import portable_gsd_contract as pgc


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
                        "schema_version": 2,
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
                json.dumps({"schema_version": 2, "entries": {"config.toml": "add"}}) + "\n",
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
                        "schema_version": 2,
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

    def test_capture_pristine_overwrites_synthesizes_backup_meta_from_fresh_install(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md", "overlay\n")
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 2,
                        "entries": {"get-shit-done/workflows/plan-phase.md": "overwrite"},
                    }
                )
                + "\n",
            )
            self._write(
                repo_root,
                ".codex/gsd-file-manifest.json",
                json.dumps({"version": "1.38.3", "files": {"get-shit-done/workflows/plan-phase.md": {}}}) + "\n",
            )
            self._write(repo_root, ".codex/get-shit-done/workflows/plan-phase.md", "upstream\n")

            report = pgc.capture_pristine_overwrites(repo_root)

            self.assertEqual(report["hard_failures"], [])
            self.assertEqual(report["copied"], ["get-shit-done/workflows/plan-phase.md"])
            backup_meta = json.loads(
                (repo_root / ".codex/gsd-local-patches/backup-meta.json").read_text(encoding="utf-8")
            )
            self.assertEqual(backup_meta["files"], ["get-shit-done/workflows/plan-phase.md"])
            self.assertEqual(
                (repo_root / ".codex/gsd-local-patches/get-shit-done/workflows/plan-phase.md").read_text(encoding="utf-8"),
                "upstream\n",
            )

            validation = pgc.build_manifest_validation_report(repo_root)
            self.assertEqual(validation["hard_failures"], [])

    def test_script_invocation_by_path_verifies_materialized_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(repo_root, "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md", "Plan phase\n")
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 2,
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

    def test_apply_overlay_renders_project_root_tokens_for_explicit_source_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._write(
                repo_root,
                "harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md",
                "<execution_context>\n@__PROJECT_ROOT__/.codex/get-shit-done/workflows/uplift-project.md\n</execution_context>\n",
            )
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 2,
                        "entries": {
                            "skills/gsd-uplift-project/SKILL.md": {
                                "mode": "add",
                                "source": "harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md",
                            }
                        },
                    }
                )
                + "\n",
            )

            written = pgc.apply_overlay(repo_root, pgc.DEFAULT_COMPACT_PROMPT_FILE)

            self.assertEqual(written, ["skills/gsd-uplift-project/SKILL.md"])
            live_skill = (repo_root / ".codex/skills/gsd-uplift-project/SKILL.md").read_text(encoding="utf-8")
            self.assertIn(
                f"@{repo_root}/.codex/get-shit-done/workflows/uplift-project.md",
                live_skill,
            )
            self.assertNotIn("__PROJECT_ROOT__", live_skill)

    def test_materialization_report_classifies_known_runtime_specific_reference_hits(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            update_example = "# RUNTIME_DIR is the resolved config directory (e.g. ~/.claude, ~/.config/opencode)\n"
            self._write(repo_root, "tooling/portable-gsd/overlay/get-shit-done/workflows/update.md", update_example)
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 2,
                        "entries": {
                            "get-shit-done/workflows/update.md": "overwrite",
                        },
                    }
                )
                + "\n",
            )
            self._write(
                repo_root,
                ".codex/gsd-local-patches/backup-meta.json",
                json.dumps({"files": ["get-shit-done/workflows/update.md"]}) + "\n",
            )
            self._write(repo_root, ".codex/get-shit-done/workflows/update.md", update_example)
            self._write(repo_root, ".codex/gsd-local-patches/get-shit-done/workflows/update.md", update_example)
            self._write(repo_root, ".codex/agents/gsd-debugger.toml", "configDir = ~/.claude\n")

            report = pgc.build_materialization_report(repo_root, pgc.DEFAULT_COMPACT_PROMPT_FILE)

            runtime_scan = report["runtime_specific_reference_scan"]
            compatibility = report["compatibility_declaration"]
            self.assertEqual(compatibility["path"], "harness_modifier/compatibility/declaration.json")
            self.assertEqual(compatibility["runtime_basis"]["runtime"], ".codex")
            self.assertTrue(compatibility["overlay_schema_version_matches_declaration"])
            self.assertEqual(report["summary"]["compatibility_declaration_rule_count"], 3)
            self.assertEqual(runtime_scan["summary"]["total_hits"], 3)
            self.assertEqual(runtime_scan["summary"]["expected_baseline_count"], 3)
            self.assertEqual(runtime_scan["summary"]["review_needed_count"], 0)
            self.assertFalse(runtime_scan["requires_contextual_reread"])
            self.assertEqual(runtime_scan["compatibility_declaration_path"], "harness_modifier/compatibility/declaration.json")
            self.assertEqual(runtime_scan["baseline_rule_count"], 3)
            classifications = {hit["path"]: hit["classification"] for hit in runtime_scan["hits"]}
            self.assertEqual(classifications["agents/gsd-debugger.toml"], "upstream_only_contextual_carry")
            self.assertEqual(classifications["get-shit-done/workflows/update.md"], "overlay_owned_comment_example")
            self.assertEqual(
                classifications["gsd-local-patches/get-shit-done/workflows/update.md"],
                "pristine_backup_mirror",
            )
            self.assertEqual(report["summary"]["runtime_specific_reference_hit_count"], 3)
            self.assertEqual(report["summary"]["runtime_specific_reference_review_needed_count"], 0)
            self.assertEqual(report["hard_failures"], [])

    def test_materialization_report_marks_unreviewed_runtime_specific_reference_hits_for_contextual_reread(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            update_runtime_reference = "See ~/.claude/runtime.md for more.\n"
            self._write(repo_root, "tooling/portable-gsd/overlay/get-shit-done/workflows/update.md", update_runtime_reference)
            self._write(
                repo_root,
                "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
                json.dumps(
                    {
                        "schema_version": 2,
                        "entries": {
                            "get-shit-done/workflows/update.md": "overwrite",
                        },
                    }
                )
                + "\n",
            )
            self._write(
                repo_root,
                ".codex/gsd-local-patches/backup-meta.json",
                json.dumps({"files": ["get-shit-done/workflows/update.md"]}) + "\n",
            )
            self._write(repo_root, ".codex/gsd-local-patches/get-shit-done/workflows/update.md", update_runtime_reference)
            self._write(repo_root, ".codex/get-shit-done/workflows/update.md", update_runtime_reference)

            report = pgc.build_materialization_report(repo_root, pgc.DEFAULT_COMPACT_PROMPT_FILE)

            runtime_scan = report["runtime_specific_reference_scan"]
            self.assertTrue(runtime_scan["requires_contextual_reread"])
            self.assertEqual(runtime_scan["summary"]["total_hits"], 2)
            self.assertEqual(runtime_scan["summary"]["review_needed_count"], 2)
            self.assertEqual(
                [hit["path"] for hit in runtime_scan["hits"]],
                [
                    "get-shit-done/workflows/update.md",
                    "gsd-local-patches/get-shit-done/workflows/update.md",
                ],
            )
            self.assertEqual(
                {hit["classification"] for hit in runtime_scan["hits"]},
                {"unreviewed_runtime_specific_reference_hit"},
            )
            self.assertEqual(
                {hit["family"] for hit in runtime_scan["hits"]},
                {"needs_contextual_reread"},
            )
            self.assertTrue(all(hit["requires_contextual_reread"] for hit in runtime_scan["hits"]))
            self.assertEqual(report["hard_failures"], [])


if __name__ == "__main__":
    unittest.main()
