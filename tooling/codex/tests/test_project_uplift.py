import json
import pathlib
import tempfile
import unittest

from tooling.codex import project_uplift as pu


STATE_TEMPLATE = """---
gsd_state_version: 1.0
status: {status}
last_updated: "2026-04-21T12:00:00+00:00"
---

# Project State

## Current Position

Status: {status}

## Session Continuity

Last session: 2026-04-21T12:00:00+00:00
Stopped at: test
Resume file: None
"""


class ProjectUpliftTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _minimal_project(self, root: pathlib.Path, status: str = "completed") -> None:
        self._write(root, ".planning/PROJECT.md", "# Project\n")
        self._write(root, ".planning/ROADMAP.md", "# Roadmap\n")
        self._write(root, ".planning/STATE.md", STATE_TEMPLATE.format(status=status))
        self._write(root, "AGENTS.md", "# Agents\n")
        self._write(root, ".planning/AGENTS.md", "# Planning Agents\n")
        self._write(root, ".codex/config.toml", 'model = "gpt-5.4"\n')
        self._write(root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.1"}) + "\n")
        self._write(root, ".codex/get-shit-done/VERSION", "1.38.1\n")
        self._write(root, ".codex/agents/gsd-planner.toml", 'description = "planner"\n')
        self._write(root, ".codex/agents/gsd-plan-checker.toml", 'description = "checker"\n')
        self._write(
            root,
            "tooling/codex/UPLIFT-HELD-LATER.md",
            "- required-reading installation practice — held\n"
            "- cross-runtime uplift composition — held\n"
            "- legacy seed corpus migration — partially landed: harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md | intervention-proposals/92-seed-migration-pointer-bridge-harden-follow-through-implementation.md | propagation-audit/38-seed-migration-pointer-bridge-harden-change-triggered-refresh.md\n"
            "- routed-entry hooks beyond `progress` — partially landed: propagation-audit/04-resume-project-second-consumer-implementation.md\n",
        )

    def _write_strengthening_carriers(self, root: pathlib.Path) -> None:
        self._write(
            root,
            ".codex/get-shit-done/workflows/discuss-phase.md",
            "# Discuss\n\nIntro.\n\n### Strengthening Opportunities\n- Keep this route.\n\n## Later\nLater text.\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/templates/context.md",
            "# Context\n\n### Strengthening Opportunities\n- Carry route.\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/workflows/plan-phase.md",
            "# Plan\n\n### Strengthening Opportunities\n- Preserve route.\n",
        )
        self._write(
            root,
            ".codex/skills/gsd-rigorous-research/references/output-template.md",
            "# Output Template\n\n### Strengthening Opportunities\n- Intensify route.\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/workflows/verify-phase.md",
            "# Verify\n\n## Future-Preservation Carry Review\n- Protected seams stay carried.\n",
        )
        self._write(
            root,
            ".codex/get-shit-done/templates/verification-report.md",
            "# Verification Report\n\n## Future-Preservation Carry\n- carried\n",
        )

    def _write_seed(
        self,
        root: pathlib.Path,
        seed_id: str,
        slug: str,
        version: str | None,
        *,
        include_current_shape: bool = True,
    ) -> None:
        version_line = f"seed_contract_version: {version}\n" if version is not None else ""
        frontmatter_tail = (
            "planted: 2026-04-22\n"
            "planted_during: milestone\n"
            "trigger_when: later\n"
            "scope: Medium\n"
            if include_current_shape
            else "trigger_when: later\n"
        )
        sections = (
            "## Why This Matters\n\n- Keep the route visible.\n\n"
            "## When to Surface\n\n- later\n\n"
            "## Scope Estimate\n\n- Medium\n\n"
            "## Strengthening Carry\n\n- Intensify the route.\n\n"
            "## Breadcrumbs\n\n- notes\n\n"
            "## Notes\n\n- context\n"
            if include_current_shape
            else "## Why This Matters\n\n- Keep the route visible.\n\n## When to Surface\n\n- later\n"
        )
        self._write(
            root,
            f".planning/seeds/SEED-{seed_id}-{slug}.md",
            "---\n"
            f"id: SEED-{seed_id}\n"
            f"{version_line}"
            "status: dormant\n"
            f"{frontmatter_tail}"
            "---\n\n"
            f"# SEED-{seed_id}: {slug}\n\n"
            f"{sections}",
        )

    def _write_doctrine_stack(self, root: pathlib.Path) -> None:
        self._write(root, "CLAUDE.md", "# Claude\n")
        self._write(root, ".planning/CLAUDE.md", "# Planning Claude\n")
        self._write(root, ".planning/CLAIM-TYPES.md", "# Claim Types\n")
        self._write(root, "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json", json.dumps({"schema_version": 2, "entries": {}}) + "\n")
        self._write(
            root,
            ".planning/LONG-ARC.md",
            "---\ndocument: LONG-ARC\nstatus: canonical\n---\n\n# Long Arc\n",
        )
        self._write(root, "tooling/codex/README.md", "# Codex Tooling Notes\n\n## Utilities\n- `audit_refmap.py`\n- `project_uplift.py`\n")
        self._write_strengthening_carriers(root)

    def _write_claude_runtime(self, root: pathlib.Path, version: str) -> None:
        self._write(root, ".claude/get-shit-done/VERSION", f"{version}\n")

    def test_detect_classifies_vanilla_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "vanilla uplift")
            self.assertTrue(analysis["recommend_detect_only"])
            self.assertIn("Claim Types", analysis["absent_additive_carriers"])
            self.assertTrue(
                any(
                    proposal["label"] == "Root CLAUDE" and proposal["proposal_state"] == "absent"
                    for proposal in analysis["pending_doctrine_sensitive_proposals"]
                )
            )

    def test_detect_classifies_lightly_aged_project(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "lightly aged uplift")
            self.assertTrue(analysis["recommend_detect_only"])
            self.assertEqual(analysis["absent_additive_carriers"], [])
            self.assertTrue(
                all(proposal["proposal_state"] != "absent" for proposal in analysis["pending_doctrine_sensitive_proposals"])
            )

    def test_detect_surfaces_legacy_seed_corpus_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_seed(repo_root, "001", "legacy-route", None)
            self._write_seed(repo_root, "002", "current-route", pu.CURRENT_SEED_CONTRACT_VERSION)

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "lightly aged uplift")
            self.assertIn("legacy_seed_corpus", analysis["secondary_signals"])
            self.assertEqual(analysis["seed_corpus_posture"]["posture"], "mixed_current_and_legacy_unversioned")
            self.assertEqual(analysis["seed_corpus_posture"]["seed_file_count"], 2)
            self.assertEqual(analysis["seed_corpus_posture"]["current_contract_count"], 1)
            self.assertEqual(analysis["seed_corpus_posture"]["legacy_unversioned_count"], 1)
            self.assertEqual(analysis["seed_corpus_posture"]["current_contract_shape_gap_count"], 0)
            self.assertTrue(
                any("legacy-unversioned seeds still present: 1" == reason for reason in analysis["recommendation_reasons"])
            )

    def test_detect_surfaces_current_contract_shape_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_seed(
                repo_root,
                "005",
                "current-gap",
                pu.CURRENT_SEED_CONTRACT_VERSION,
                include_current_shape=False,
            )

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "lightly aged uplift")
            self.assertIn("legacy_seed_corpus", analysis["secondary_signals"])
            self.assertEqual(analysis["seed_corpus_posture"]["posture"], "current_contract_only")
            self.assertEqual(analysis["seed_corpus_posture"]["current_contract_shape_gap_count"], 1)
            self.assertTrue(
                any(
                    "current-contract seed shape gaps still present: 1" == reason
                    for reason in analysis["recommendation_reasons"]
                )
            )

    def test_write_outputs_and_progress_note_detect_doctrine_change(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)
            written = pu.write_outputs(repo_root, analysis)
            self.assertEqual(written["report_path"], ".planning/UPLIFT-REPORT.md")
            self.assertTrue((repo_root / ".planning/UPLIFT-MANIFEST.json").exists())
            self.assertIn("## Project Uplift", (repo_root / ".planning/STATE.md").read_text(encoding="utf-8"))

            note = pu.build_progress_note(repo_root)
            self.assertTrue(note["show"])
            self.assertFalse(note["recommend_detect_only"])
            self.assertFalse(note["recommend_write"])
            self.assertFalse(note["show_seed_corpus_posture"])
            self.assertIsNone(note["seed_corpus_posture"])
            self.assertEqual(note["seed_corpus_reasons"], [])
            self.assertFalse(note["show_seed_migration_pointer"])
            self.assertEqual(note["seed_migration_candidate_count"], 0)
            self.assertIsNone(note["seed_migration_candidate_breakdown"])
            self.assertIsNone(note["seed_migration_inspect_pointer"])
            self.assertIsNone(note["seed_migration_write_pointer"])

            self._write(repo_root, "AGENTS.md", "# Agents changed\n")
            changed_note = pu.build_progress_note(repo_root)
            self.assertTrue(changed_note["recommend_detect_only"])
            self.assertFalse(changed_note["recommend_write"])
            self.assertTrue(changed_note["doctrine_reference_changed"])
            self.assertTrue(
                any(
                    proposal["label"] == "Root AGENTS" and proposal["proposal_state"] == "drifted"
                    for proposal in changed_note["pending_doctrine_sensitive_proposals"]
                )
            )

    def test_progress_note_render_contract_matches_overlay_consumers(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            note = pu.build_progress_note(repo_root)
            for key, _label in pu.PROGRESS_NOTE_RENDER_FIELDS:
                self.assertIn(key, note)

            progress_workflow = pathlib.Path(
                "tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md"
            ).read_text(encoding="utf-8")
            resume_workflow = pathlib.Path(
                "tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md"
            ).read_text(encoding="utf-8")

            for _key, label in pu.PROGRESS_NOTE_RENDER_FIELDS:
                self.assertIn(f"{label}:", progress_workflow)
                self.assertIn(f"{label}:", resume_workflow)
            self.assertIn(f"{pu.PROGRESS_NOTE_REASON_LABEL}:", progress_workflow)
            self.assertIn(f"{pu.PROGRESS_NOTE_REASON_LABEL}:", resume_workflow)
            self.assertIn(f"{pu.SEED_POSTURE_REASON_LABEL}:", progress_workflow)
            self.assertIn(f"{pu.SEED_POSTURE_REASON_LABEL}:", resume_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_CANDIDATE_LABEL}:", progress_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_CANDIDATE_LABEL}:", resume_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_BREAKDOWN_LABEL}:", progress_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_BREAKDOWN_LABEL}:", resume_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_INSPECT_POINTER_LABEL}:", progress_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_INSPECT_POINTER_LABEL}:", resume_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_WRITE_POINTER_LABEL}:", progress_workflow)
            self.assertIn(f"{pu.SEED_MIGRATION_WRITE_POINTER_LABEL}:", resume_workflow)

    def test_progress_note_surfaces_seed_corpus_without_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_seed(repo_root, "003", "current-route", pu.CURRENT_SEED_CONTRACT_VERSION)

            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["show"])
            self.assertFalse(note["manifest_present"])
            self.assertTrue(note["recommend_detect_only"])
            self.assertTrue(note["show_seed_corpus_posture"])
            self.assertIn("current_contract_only", note["seed_corpus_posture"])
            self.assertEqual(note["seed_corpus_reasons"], [])
            self.assertTrue(
                any("no uplift manifest recorded yet" == reason for reason in note["reasons"])
            )

    def test_progress_note_keeps_seed_attention_visible_without_basis_movement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_seed(repo_root, "004", "legacy-route", None)
            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["show"])
            self.assertTrue(note["manifest_present"])
            self.assertFalse(note["recommend_write"])
            self.assertTrue(note["show_seed_corpus_posture"])
            self.assertIn("legacy_unversioned_only", note["seed_corpus_posture"])
            self.assertTrue(note["show_seed_migration_pointer"])
            self.assertEqual(note["seed_migration_candidate_count"], 1)
            self.assertEqual(
                note["seed_migration_candidate_breakdown"],
                "legacy 1 / noncurrent 0 / shape-gap 0",
            )
            self.assertEqual(note["seed_migration_inspect_pointer"], pu.SEED_MIGRATION_SKILL_COMMAND)
            self.assertEqual(note["seed_migration_write_pointer"], pu.SEED_MIGRATION_WRITE_COMMAND)
            self.assertTrue(
                any(
                    "legacy-unversioned seeds still present: 1" == reason
                    for reason in note["seed_corpus_reasons"]
                )
            )

    def test_write_outputs_preserves_typed_held_later_statuses(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)
            pu.write_outputs(repo_root, analysis)

            manifest = json.loads((repo_root / ".planning/UPLIFT-MANIFEST.json").read_text(encoding="utf-8"))
            held_later = manifest["held_later_families"]
            self.assertEqual(manifest["schema_version"], 6)
            self.assertTrue(any(item["status"] == "held" for item in held_later))
            self.assertTrue(
                any(
                    item["family"] == "legacy seed corpus migration"
                    and item["status"] == "partially landed"
                    and item["pointer"]
                    == [
                        "harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md",
                        "intervention-proposals/92-seed-migration-pointer-bridge-harden-follow-through-implementation.md",
                        "propagation-audit/38-seed-migration-pointer-bridge-harden-change-triggered-refresh.md",
                    ]
                    for item in held_later
                )
            )
            self.assertTrue(
                any(
                    item["family"] == "routed-entry hooks beyond `progress`"
                    and item["status"] == "partially landed"
                    and item["pointer"] == "propagation-audit/04-resume-project-second-consumer-implementation.md"
                    for item in held_later
                )
            )
            self.assertEqual(manifest["compatibility_basis"]["compatibility_posture"], "observed_basis_only")
            self.assertEqual(manifest["compatibility_basis"]["observed_runtime_version"], "1.38.1")
            self.assertTrue(manifest["compatibility_basis"]["observed_runtime_version_aligned"])
            self.assertEqual(manifest["seed_corpus_posture"]["posture"], "no_seed_corpus")
            self.assertEqual(manifest["seed_corpus_posture"]["migration_candidate_count"], 0)
            self.assertEqual(
                manifest["seed_corpus_posture"]["migration_candidate_breakdown"],
                {
                    "legacy_unversioned": 0,
                    "noncurrent_version": 0,
                    "current_contract_shape_gap": 0,
                },
            )

    def test_compatibility_basis_anchors_to_observed_runtime_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)

            compatibility = analysis["compatibility_basis"]
            self.assertEqual(compatibility["compatibility_posture"], "observed_basis_only")
            self.assertEqual(
                compatibility["compatibility_declaration_path"],
                "harness_modifier/compatibility/declaration.json",
            )
            self.assertEqual(compatibility["observed_runtime_version"], "1.38.1")
            self.assertEqual(compatibility["observed_runtime_manifest_version"], "1.38.1")
            self.assertTrue(compatibility["observed_runtime_version_aligned"])
            self.assertEqual(compatibility["runtime_basis"]["runtime"], ".codex")
            self.assertEqual(compatibility["declared_overlay_schema_version"], 2)
            self.assertEqual(compatibility["overlay_manifest_schema_version"], 2)
            self.assertTrue(compatibility["overlay_manifest_schema_version_matches_declaration"])
            self.assertEqual(compatibility["uplift_manifest_schema_version"], 6)
            self.assertEqual(compatibility["upstream_compatibility_window"]["state"], "unknown")
            self.assertEqual(compatibility["parity_scan_baseline"]["rule_count"], 3)
            self.assertIn("version-window claims beyond the observed runtime basis", compatibility["held_later"])

    def test_compatibility_basis_carries_held_claude_annotation_without_relabeling_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_claude_runtime(repo_root, "1.34.2")

            compatibility = pu.analyze_repo(repo_root)["compatibility_basis"]

            self.assertEqual(compatibility["compatibility_posture"], "observed_basis_only")
            self.assertEqual(compatibility["observed_runtime_version"], "1.38.1")
            self.assertEqual(compatibility["held_runtime_annotation"]["runtime"], ".claude")
            self.assertEqual(compatibility["held_runtime_annotation"]["version"], "1.34.2")
            self.assertEqual(compatibility["held_runtime_annotation"]["version_source"], ".claude/get-shit-done/VERSION")
            self.assertEqual(compatibility["held_runtime_annotation"]["annotation_posture"], "held_annotation")
            self.assertEqual(compatibility["held_runtime_annotation_summary"], ".claude 1.34.2 (held_annotation)")

    def test_progress_note_recommends_write_after_runtime_basis_movement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            self._write(repo_root, ".codex/get-shit-done/VERSION", "1.38.3\n")
            self._write(repo_root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")

            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["recommend_write"])
            self.assertFalse(note["recommend_detect_only"])
            self.assertTrue(note["compatibility_basis_changed"])
            self.assertIn("--write", note["recommendation"])
            self.assertTrue(
                any("observed runtime version moved from 1.38.1 to 1.38.3" in reason for reason in note["reasons"])
            )

    def test_progress_note_recommends_write_after_held_runtime_annotation_movement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_claude_runtime(repo_root, "1.34.2")
            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            self._write_claude_runtime(repo_root, "1.34.3")

            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["recommend_write"])
            self.assertFalse(note["recommend_detect_only"])
            self.assertTrue(note["compatibility_basis_changed"])
            self.assertEqual(note["held_runtime_annotation"], ".claude 1.34.2 (held_annotation)")
            self.assertTrue(
                any(
                    "held runtime annotation moved from .claude 1.34.2 (held_annotation) to .claude 1.34.3 (held_annotation)"
                    in reason
                    for reason in note["reasons"]
                )
            )

    def test_compatibility_basis_ignores_noncanonical_runtime_version_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            (repo_root / ".codex/get-shit-done/VERSION").unlink()
            self._write(repo_root, ".codex/VERSION", "9.99.9\n")

            compatibility = pu.analyze_repo(repo_root)["compatibility_basis"]

            self.assertIsNone(compatibility["observed_runtime_version"])
            self.assertIsNone(compatibility["observed_runtime_version_source"])
            self.assertEqual(compatibility["observed_runtime_manifest_version"], "1.38.1")
            self.assertFalse(compatibility["observed_runtime_version_aligned"])

    def test_progress_note_recommends_write_after_seed_corpus_movement(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            self._write_seed(repo_root, "003", "legacy-drift", None)

            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["recommend_write"])
            self.assertFalse(note["recommend_detect_only"])
            self.assertTrue(note["seed_corpus_basis_changed"])
            self.assertTrue(note["show_seed_corpus_posture"])
            self.assertIn("legacy_unversioned_only", note["seed_corpus_posture"])
            self.assertTrue(note["show_seed_migration_pointer"])
            self.assertEqual(note["seed_migration_candidate_count"], 1)
            self.assertEqual(
                note["seed_migration_candidate_breakdown"],
                "legacy 1 / noncurrent 0 / shape-gap 0",
            )
            self.assertEqual(note["seed_migration_inspect_pointer"], pu.SEED_MIGRATION_SKILL_COMMAND)
            self.assertEqual(note["seed_migration_write_pointer"], pu.SEED_MIGRATION_WRITE_COMMAND)
            self.assertTrue(
                any(
                    "legacy-unversioned seeds still present: 1" == reason
                    for reason in note["seed_corpus_reasons"]
                )
            )
            self.assertIn("--write", note["recommendation"])
            self.assertTrue(
                any("seed file count moved from 0 to 1" in reason for reason in note["reasons"])
            )

    def test_progress_note_surfaces_pointer_for_current_contract_shape_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_seed(
                repo_root,
                "005",
                "shape-gap",
                pu.CURRENT_SEED_CONTRACT_VERSION,
                include_current_shape=False,
            )

            note = pu.build_progress_note(repo_root)

            self.assertTrue(note["show"])
            self.assertTrue(note["recommend_detect_only"])
            self.assertTrue(note["show_seed_corpus_posture"])
            self.assertIn("current_contract_only", note["seed_corpus_posture"])
            self.assertTrue(note["show_seed_migration_pointer"])
            self.assertEqual(note["seed_migration_candidate_count"], 1)
            self.assertEqual(
                note["seed_migration_candidate_breakdown"],
                "legacy 0 / noncurrent 0 / shape-gap 1",
            )
            self.assertEqual(note["seed_migration_inspect_pointer"], pu.SEED_MIGRATION_SKILL_COMMAND)
            self.assertEqual(note["seed_migration_write_pointer"], pu.SEED_MIGRATION_WRITE_COMMAND)
            self.assertTrue(
                any(
                    "current-contract seed shape gaps still present: 1" == reason
                    for reason in note["seed_corpus_reasons"]
                )
            )

    def test_write_outputs_and_progress_note_surface_held_runtime_annotation(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_claude_runtime(repo_root, "1.34.2")

            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))

            manifest = json.loads((repo_root / ".planning/UPLIFT-MANIFEST.json").read_text(encoding="utf-8"))
            report_text = (repo_root / ".planning/UPLIFT-REPORT.md").read_text(encoding="utf-8")
            state_text = (repo_root / ".planning/STATE.md").read_text(encoding="utf-8")
            note = pu.build_progress_note(repo_root)

            self.assertEqual(manifest["schema_version"], 6)
            self.assertEqual(
                manifest["compatibility_basis"]["compatibility_declaration_path"],
                "harness_modifier/compatibility/declaration.json",
            )
            self.assertEqual(manifest["compatibility_basis"]["held_runtime_annotation_summary"], ".claude 1.34.2 (held_annotation)")
            self.assertIn("- Compatibility declaration: harness_modifier/compatibility/declaration.json", report_text)
            self.assertIn("### Held Runtime Annotation", report_text)
            self.assertLess(report_text.index("### Compatibility Check Protocol"), report_text.index("### Held Runtime Annotation"))
            self.assertIn("Compatibility declaration: harness_modifier/compatibility/declaration.json", state_text)
            self.assertIn("Held runtime annotation: .claude 1.34.2 (held_annotation)", state_text)
            self.assertEqual(note["held_runtime_annotation"], ".claude 1.34.2 (held_annotation)")

    def test_cross_runtime_primary_class_preserves_mid_phase_secondary_signal(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="planning")
            self._write_doctrine_stack(repo_root)
            self._write(
                repo_root,
                ".planning/phases/01-test-phase/01-CONTEXT.md",
                "# Context\n\n**Status:** Pre-rerun steering snapshot; fresh discuss + plan required before execution\n",
            )
            (repo_root / ".claude").mkdir(parents=True, exist_ok=True)

            analysis = pu.analyze_repo(repo_root)

            self.assertEqual(analysis["project_class"], "cross-runtime uplift")
            self.assertIn("mid_phase", analysis["secondary_signals"])
            self.assertEqual(
                analysis["phase_boundary_signal"]["note"],
                "phase CONTEXT carries explicit rerun-boundary posture",
            )

    def test_marker_block_fingerprint_ignores_unrelated_whitespace(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            first = pu.analyze_repo(repo_root)
            first_fingerprint = next(
                carrier["fingerprint"]
                for carrier in first["carriers"]
                if carrier["key"] == "strengthening_discuss"
            )

            self._write(
                repo_root,
                ".codex/get-shit-done/workflows/discuss-phase.md",
                "# Discuss\n\nIntro with extra whitespace.   \n\n### Strengthening Opportunities\n- Keep this route.\n\n## Later\nLater text with spacing.\n\n",
            )
            second = pu.analyze_repo(repo_root)
            second_fingerprint = next(
                carrier["fingerprint"]
                for carrier in second["carriers"]
                if carrier["key"] == "strengthening_discuss"
            )

            self.assertEqual(first_fingerprint, second_fingerprint)

    def test_runtime_agent_inventory_uses_globbed_contracts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write(repo_root, ".codex/agents/gsd-extra.toml", 'description = "extra"\n')

            analysis = pu.analyze_repo(repo_root)

            self.assertTrue(
                any(carrier["key"] == "runtime_agent_gsd-extra" for carrier in analysis["carriers"])
            )


if __name__ == "__main__":
    unittest.main()
