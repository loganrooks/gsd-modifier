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
            "- legacy seed corpus migration — held\n"
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

    def _write_seed(self, root: pathlib.Path, seed_id: str, slug: str, version: str | None) -> None:
        version_line = f"seed_contract_version: {version}\n" if version is not None else ""
        self._write(
            root,
            f".planning/seeds/SEED-{seed_id}-{slug}.md",
            "---\n"
            f"id: SEED-{seed_id}\n"
            f"{version_line}"
            "status: dormant\n"
            "trigger_when: later\n"
            "---\n\n"
            f"# SEED-{seed_id}: {slug}\n",
        )

    def _write_doctrine_stack(self, root: pathlib.Path) -> None:
        self._write(root, "CLAUDE.md", "# Claude\n")
        self._write(root, ".planning/CLAUDE.md", "# Planning Claude\n")
        self._write(root, ".planning/CLAIM-TYPES.md", "# Claim Types\n")
        self._write(root, "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json", json.dumps({"schema_version": 1, "entries": {}}) + "\n")
        self._write(
            root,
            ".planning/LONG-ARC.md",
            "---\ndocument: LONG-ARC\nstatus: canonical\n---\n\n# Long Arc\n",
        )
        self._write(root, "tooling/codex/README.md", "# Codex Tooling Notes\n\n## Utilities\n- `audit_refmap.py`\n- `project_uplift.py`\n")
        self._write_strengthening_carriers(root)

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
            self.assertTrue(
                any("legacy-unversioned seeds still present: 1" == reason for reason in analysis["recommendation_reasons"])
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

    def test_write_outputs_preserves_typed_held_later_statuses(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)
            pu.write_outputs(repo_root, analysis)

            manifest = json.loads((repo_root / ".planning/UPLIFT-MANIFEST.json").read_text(encoding="utf-8"))
            held_later = manifest["held_later_families"]
            self.assertEqual(manifest["schema_version"], 5)
            self.assertTrue(any(item["status"] == "held" for item in held_later))
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

    def test_compatibility_basis_anchors_to_observed_runtime_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = pathlib.Path(tmpdir)
            self._minimal_project(repo_root, status="completed")
            self._write_doctrine_stack(repo_root)

            analysis = pu.analyze_repo(repo_root)

            compatibility = analysis["compatibility_basis"]
            self.assertEqual(compatibility["compatibility_posture"], "observed_basis_only")
            self.assertEqual(compatibility["observed_runtime_version"], "1.38.1")
            self.assertEqual(compatibility["observed_runtime_manifest_version"], "1.38.1")
            self.assertTrue(compatibility["observed_runtime_version_aligned"])
            self.assertEqual(compatibility["overlay_manifest_schema_version"], 1)
            self.assertEqual(compatibility["uplift_manifest_schema_version"], 5)
            self.assertIn("version-window claims beyond the observed runtime basis", compatibility["held_later"])

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
            self.assertIn("--write", note["recommendation"])
            self.assertTrue(
                any("seed file count moved from 0 to 1" in reason for reason in note["reasons"])
            )

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
