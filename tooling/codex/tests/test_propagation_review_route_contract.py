import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_entry_mode, overlay_source_path

ROOT = Path(__file__).resolve().parents[3]


class PropagationReviewRouteContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_propagation_review_surfaces(self) -> None:
        self.assertEqual(
            overlay_entry_mode("get-shit-done/workflows/propagation-review.md"), "add"
        )
        self.assertEqual(overlay_entry_mode("skills/gsd-propagation-review/SKILL.md"), "add")

    def test_workflow_reads_baseline_delta_and_names_runtime_gate_tools(self) -> None:
        text = overlay_source_path("get-shit-done/workflows/propagation-review.md").read_text(encoding="utf-8")
        self.assertIn("host repo's current propagation baseline pair", text)
        self.assertIn("manifest_install_coherence.py", text)
        self.assertIn("harness_canary.py report . --strict", text)
        self.assertIn("harness_modifier/overlay/helpers/audit_refmap.py", text)
        self.assertIn("harness_modifier/overlay/helpers/project_uplift.py", text)
        self.assertIn("Do not let a clean tool result replace contextual reread.", text)
        self.assertIn("Updated In This Slice", text)
        self.assertIn("Held With Explicit Boundary", text)
        self.assertIn("outputs/` when you are preserving", text)
        self.assertIn("local claim-type grammar", text)

    def test_skill_keeps_route_read_only_and_specialist_handoffs_explicit(self) -> None:
        text = overlay_source_path("skills/gsd-propagation-review/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("$gsd-propagation-review", text)
        self.assertIn("Default posture is read-only.", text)
        self.assertIn("--write-note PATH", text)
        self.assertIn("existing lane home", text)
        self.assertIn("$gsd-uplift-project --write", text)
        self.assertIn("$gsd-seed-migration-inventory", text)


if __name__ == "__main__":
    unittest.main()
