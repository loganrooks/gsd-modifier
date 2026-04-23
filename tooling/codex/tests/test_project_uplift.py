import json
import pathlib
import tempfile
import unittest
from unittest import mock

from harness_modifier.compatibility import observation as compatibility_observation
from harness_modifier.compatibility import seed_contract as compatibility_seed_contract
from harness_modifier.uplift import carrier_catalog as uplift_carrier_catalog
from harness_modifier.uplift import output_policy as uplift_output_policy
from harness_modifier.uplift import phase_layout as uplift_phase_layout
from harness_modifier.uplift import state_section as uplift_state_section
from harness_modifier.uplift import state_writer as uplift_state_writer
from harness_modifier.uplift import vocabulary as uplift_vocabulary
from tooling.codex import project_uplift as pu


OBSERVATION_POLICY = compatibility_observation.load_observation()
SEED_CONTRACT = compatibility_seed_contract.load_seed_contract()
CARRIER_CATALOG = uplift_carrier_catalog.load_carrier_catalog()
OUTPUT_POLICY = uplift_output_policy.load_output_policy()
PHASE_LAYOUT = uplift_phase_layout.load_phase_layout()
STATE_SECTION = uplift_state_section.load_state_section()
VOCABULARY = uplift_vocabulary.load_vocabulary()


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

    def _reordered_carrier_catalog(self) -> dict:
        catalog = json.loads(json.dumps(CARRIER_CATALOG))
        catalog["file_carriers"] = list(reversed(catalog["file_carriers"]))
        catalog["marker_carriers"] = list(reversed(catalog["marker_carriers"]))
        return catalog

    def _recommendation_line(self, report_text: str) -> str:
        return next(
            line
            for line in report_text.splitlines()
            if line.startswith("- Recommendation: ")
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

    def test_neutralization_carriers_load_expected_shapes(self) -> None:
        self.assertEqual(OBSERVATION_POLICY["observed_runtime_directories"], [".codex", ".claude"])
        self.assertIn(".gemini", OBSERVATION_POLICY["candidate_observed_runtime_directories"])
        self.assertEqual(SEED_CONTRACT["seed_dir_rel_path"], ".planning/seeds")
        self.assertEqual(SEED_CONTRACT["current_seed_contract_version"], "2")
        self.assertIn("seed_contract_version", SEED_CONTRACT["required_seed_frontmatter_keys"])
        self.assertIn("Strengthening Carry", SEED_CONTRACT["required_seed_section_headings"])
        self.assertEqual(OUTPUT_POLICY["report_rel_path"], ".planning/UPLIFT-REPORT.md")
        self.assertEqual(OUTPUT_POLICY["manifest_rel_path"], ".planning/UPLIFT-MANIFEST.json")
        self.assertEqual(OUTPUT_POLICY["state_heading"], "## Project Uplift")
        self.assertEqual(CARRIER_CATALOG["ordering_rule"], "stable_by_key_within_section")
        self.assertEqual(CARRIER_CATALOG["runtime_agent_registry"]["rel_path_glob"], ".codex/agents/*.toml")
        self.assertEqual(CARRIER_CATALOG["runtime_agent_registry"]["key_prefix"], "runtime_agent_")
        self.assertEqual(
            [spec.key for spec in pu.file_carrier_specs()],
            sorted(spec.key for spec in pu.file_carrier_specs()),
        )
        self.assertEqual(
            [spec.key for spec in pu.marker_carrier_specs()],
            sorted(spec.key for spec in pu.marker_carrier_specs()),
        )
        self.assertEqual(pu.SEED_MIGRATION_SKILL_COMMAND, VOCABULARY["commands"]["seed_migration_inventory"])
        self.assertEqual(pu.SEED_MIGRATION_WRITE_COMMAND, VOCABULARY["commands"]["seed_migration_write"])
        self.assertIn("rerun-boundary", VOCABULARY["rerun_boundary_patterns"])
        self.assertEqual(
            VOCABULARY["recommendations"]["progress_continue"],
            "Continue with current routing.",
        )
        self.assertEqual(PHASE_LAYOUT["phase_root_rel_path"], ".planning/phases")
        self.assertEqual(PHASE_LAYOUT["document_globs"]["context"], "*/*-CONTEXT.md")
        self.assertEqual(PHASE_LAYOUT["phase_name_delimiter"], "-")
        self.assertEqual(PHASE_LAYOUT["phase_segment_delimiter"], ".")
        self.assertEqual(STATE_SECTION["state_rel_path"], ".planning/STATE.md")
        self.assertEqual(
            STATE_SECTION["sibling_markers"],
            ["## Deferred Items", "## Session Continuity"],
        )
        self.assertEqual(
            STATE_SECTION["ordered_selector_keys"][:3],
            ["last_uplift_pass", "last_uplift_class", "last_uplift_secondary_signals"],
        )
        self.assertEqual(
            STATE_SECTION["selector_labels"]["current_uplift_manifest"],
            "Current uplift manifest",
        )
        self.assertEqual(
            STATE_SECTION["selector_labels"]["observed_runtime_basis"],
            "Observed runtime profiles",
        )
        self.assertEqual(
            STATE_SECTION["selector_labels"]["mixed_runtime_policy"],
            "Mixed-runtime policy",
        )
        self.assertEqual(
            STATE_SECTION["selector_labels"]["held_runtime_annotation"],
            "Secondary runtime observation",
        )

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

    def test_catalog_reordering_keeps_absent_additive_routes_stable(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")

            baseline = pu.analyze_repo(repo_root)
            with mock.patch(
                "tooling.codex.project_uplift.carrier_catalog_policy",
                return_value=self._reordered_carrier_catalog(),
            ):
                reordered = pu.analyze_repo(repo_root)

            self.assertEqual(
                baseline["absent_additive_carriers"],
                reordered["absent_additive_carriers"],
            )
            self.assertEqual(
                baseline["doctrine_reference_hash"],
                reordered["doctrine_reference_hash"],
            )

    def test_catalog_reordering_keeps_fingerprints_and_recommendations_equivalent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            pu.write_outputs(repo_root, pu.analyze_repo(repo_root))
            self._write(repo_root, "AGENTS.md", "# Agents changed\n")

            baseline_analysis = pu.analyze_repo(repo_root)
            baseline_note = pu.build_progress_note(repo_root)
            baseline_carriers = {
                carrier["key"]: (
                    carrier["status"],
                    carrier["fingerprint_shape"],
                    carrier["fingerprint"],
                )
                for carrier in baseline_analysis["carriers"]
            }

            with mock.patch(
                "tooling.codex.project_uplift.carrier_catalog_policy",
                return_value=self._reordered_carrier_catalog(),
            ):
                reordered_analysis = pu.analyze_repo(repo_root)
                reordered_note = pu.build_progress_note(repo_root)

            reordered_carriers = {
                carrier["key"]: (
                    carrier["status"],
                    carrier["fingerprint_shape"],
                    carrier["fingerprint"],
                )
                for carrier in reordered_analysis["carriers"]
            }

            self.assertEqual(baseline_carriers, reordered_carriers)
            self.assertEqual(
                baseline_analysis["pending_doctrine_sensitive_proposals"],
                reordered_analysis["pending_doctrine_sensitive_proposals"],
            )
            self.assertEqual(baseline_note["reasons"], reordered_note["reasons"])
            self.assertEqual(
                baseline_note["recommendation"],
                reordered_note["recommendation"],
            )
            self.assertEqual(
                self._recommendation_line(pu.render_report(baseline_analysis)),
                self._recommendation_line(pu.render_report(reordered_analysis)),
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

    def test_runtime_dirs_present_matches_observation_policy_union(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            for rel_path in [".claude", ".gemini", ".config/opencode", ".opencode", ".config/kilo", ".kilo"]:
                (repo_root / rel_path).mkdir(parents=True, exist_ok=True)

            runtime_dirs = pu.runtime_dirs_present(repo_root)

            self.assertEqual(
                runtime_dirs,
                [
                    ".codex",
                    ".claude",
                    ".gemini",
                    ".config/opencode",
                    ".opencode",
                    ".config/kilo",
                    ".kilo",
                ],
            )

    def test_detect_surfaces_legacy_seed_corpus_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_seed(repo_root, "001", "legacy-route", None)
            self._write_seed(repo_root, "002", "current-route", SEED_CONTRACT["current_seed_contract_version"])

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
                SEED_CONTRACT["current_seed_contract_version"],
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

    def test_state_writer_inserts_before_deferred_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write(
                repo_root,
                ".planning/STATE.md",
                "---\nstatus: completed\n---\n\n# Project State\n\n## Deferred Items\n- later\n",
            )

            analysis = pu.analyze_repo(repo_root)
            pu.update_state_section(repo_root, analysis)

            state_text = (repo_root / ".planning/STATE.md").read_text(encoding="utf-8")
            self.assertLess(state_text.index("## Project Uplift"), state_text.index("## Deferred Items"))
            self.assertIn("Current uplift manifest: .planning/UPLIFT-MANIFEST.json", state_text)

    def test_state_writer_replaces_existing_section_in_place(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)
            initial_values = pu.build_state_section_values(analysis)
            existing_text = "\n".join(
                [
                    "---",
                    "status: completed",
                    "---",
                    "",
                    "# Project State",
                    "",
                    uplift_state_writer.render_state_section(initial_values).rstrip(),
                    "",
                    "## Session Continuity",
                    "Resume file: None",
                    "",
                ]
            )
            self._write(repo_root, ".planning/STATE.md", existing_text)

            analysis["project_class"] = "cross-runtime uplift"
            pu.update_state_section(repo_root, analysis)

            state_text = (repo_root / ".planning/STATE.md").read_text(encoding="utf-8")
            self.assertEqual(state_text.count("## Project Uplift"), 1)
            self.assertIn("Last uplift class: cross-runtime uplift", state_text)

    def test_state_writer_appends_when_no_sibling_marker_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write(
                repo_root,
                ".planning/STATE.md",
                "---\nstatus: completed\n---\n\n# Project State\n\nNo markers here.\n",
            )

            analysis = pu.analyze_repo(repo_root)
            pu.update_state_section(repo_root, analysis)

            state_text = (repo_root / ".planning/STATE.md").read_text(encoding="utf-8")
            self.assertTrue(state_text.rstrip().endswith("Current uplift manifest: .planning/UPLIFT-MANIFEST.json"))

    def test_phase_layout_drives_count_and_latest_context_selection(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="planning")
            self._write_doctrine_stack(repo_root)
            self._write(repo_root, ".planning/phases/2.9-earlier/2.9-CONTEXT.md", "# Context\n")
            self._write(repo_root, ".planning/phases/2.10-later/2.10-CONTEXT.md", "# Context\n")
            self._write(repo_root, ".planning/phases/2.9-earlier/2.9-PLAN.md", "# Plan\n")
            self._write(repo_root, ".planning/phases/2.10-later/2.10-PLAN.md", "# Plan\n")
            self._write(repo_root, ".planning/phases/2.9-earlier/2.9-SUMMARY.md", "# Summary\n")

            self.assertEqual(pu.count_phase_files(repo_root, "plan"), 2)
            self.assertEqual(pu.count_phase_files(repo_root, "summary"), 1)
            self.assertEqual(
                pu.latest_phase_context_path(repo_root),
                repo_root / ".planning/phases/2.10-later/2.10-CONTEXT.md",
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
            self._write_seed(repo_root, "003", "current-route", SEED_CONTRACT["current_seed_contract_version"])

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
            self.assertEqual(manifest["compatibility_basis"]["compatibility_posture"], "core_runtime_parity")
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
            self.assertEqual(compatibility["compatibility_posture"], "core_runtime_parity")
            self.assertEqual(
                compatibility["compatibility_declaration_path"],
                "harness_modifier/compatibility/declaration.json",
            )
            self.assertEqual(compatibility["observed_runtime_version"], "1.38.1")
            self.assertEqual(compatibility["observed_runtime_manifest_version"], "1.38.1")
            self.assertTrue(compatibility["observed_runtime_version_aligned"])
            self.assertEqual(compatibility["runtime_basis"]["runtime"], ".codex")
            self.assertEqual(compatibility["declared_overlay_schema_version"], 3)
            self.assertEqual(compatibility["overlay_manifest_schema_version"], 2)
            self.assertTrue(compatibility["overlay_manifest_schema_version_matches_declaration"])
            self.assertEqual(compatibility["uplift_manifest_schema_version"], 6)
            self.assertEqual(compatibility["upstream_compatibility_window"]["state"], "active")
            self.assertEqual(compatibility["parity_scan_baseline"]["rule_count"], 3)
            self.assertEqual(compatibility["support_claims"]["active_core_profiles"], ["codex", "claude"])
            self.assertNotIn("dual-runtime-core release claims before the parity matrix is green", compatibility["held_later"])

    def test_compatibility_basis_carries_held_claude_annotation_without_relabeling_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)
            self._write_claude_runtime(repo_root, "1.34.2")

            compatibility = pu.analyze_repo(repo_root)["compatibility_basis"]

            self.assertEqual(compatibility["compatibility_posture"], "core_runtime_parity")
            self.assertEqual(compatibility["observed_runtime_version"], "1.38.1")
            self.assertEqual(compatibility["held_runtime_annotation"]["runtime"], ".claude")
            self.assertEqual(compatibility["held_runtime_annotation"]["version"], "1.34.2")
            self.assertEqual(compatibility["held_runtime_annotation"]["version_source"], ".claude/get-shit-done/VERSION")
            self.assertEqual(compatibility["held_runtime_annotation"]["annotation_posture"], "active_core_profile")
            self.assertEqual(compatibility["held_runtime_annotation_summary"], ".claude 1.34.2 (active_core_profile)")

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
            self.assertEqual(note["held_runtime_annotation"], ".claude 1.34.2 (active_core_profile)")
            self.assertTrue(
                any(
                    "held runtime annotation moved from .claude 1.34.2 (active_core_profile) to .claude 1.34.3 (active_core_profile)"
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
                SEED_CONTRACT["current_seed_contract_version"],
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
            self.assertEqual(manifest["compatibility_basis"]["held_runtime_annotation_summary"], ".claude 1.34.2 (active_core_profile)")
            self.assertIn("- Compatibility declaration: harness_modifier/compatibility/declaration.json", report_text)
            self.assertIn("### Secondary Core Runtime Observation", report_text)
            self.assertLess(report_text.index("### Compatibility Check Protocol"), report_text.index("### Secondary Core Runtime Observation"))
            self.assertIn("Compatibility declaration: harness_modifier/compatibility/declaration.json", state_text)
            self.assertIn("Mixed-runtime policy: dual-runtime-core (active)", state_text)
            self.assertIn("Secondary runtime observation: .claude 1.34.2 (active_core_profile)", state_text)
            self.assertEqual(note["held_runtime_annotation"], ".claude 1.34.2 (active_core_profile)")

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
