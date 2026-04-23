import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_entry_mode


ROOT = Path(__file__).resolve().parents[3]


class ExploreSeedFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_explore_seed_surfaces(self) -> None:
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/explore.md"), "overwrite")
        self.assertEqual(overlay_entry_mode("skills/gsd-explore/SKILL.md"), "overwrite")

    def test_explore_workflow_routes_seed_outputs_through_current_seed_contract(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/explore.md"
        ).read_text()
        self.assertIn("$gsd-plant-seed", text)
        self.assertIn("SEED-NNN-slug", text)
        self.assertIn("trigger_when", text)
        self.assertIn("Strengthening Carry", text)
        self.assertNotIn("trigger_condition", text)
        self.assertNotIn("planted_date", text)
        self.assertNotIn(".planning/seeds/{slug}.md", text)

    def test_explore_skill_keeps_current_seed_route_explicit(self) -> None:
        text = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-explore/SKILL.md"
        ).read_text()
        self.assertIn("$gsd-plant-seed", text)
        self.assertIn("legacy seed shape", text)
