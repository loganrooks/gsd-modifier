import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class SeedConsumerFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_seed_producer_and_wrapper(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(entries["get-shit-done/workflows/plant-seed.md"], "overwrite")
        self.assertEqual(entries["skills/gsd-plant-seed/SKILL.md"], "overwrite")

    def test_plant_seed_workflow_keeps_strengthening_carry_explicit(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md"
        ).read_text()
        self.assertIn("header: \"Strengthening\"", text)
        self.assertIn("## Strengthening Carry", text)
        self.assertIn("$STRENGTHENING_CARRY", text)

    def test_new_milestone_consumes_seed_meaning_and_strengthening_carry(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md"
        ).read_text()
        self.assertIn("Why This Matters", text)
        self.assertIn("Strengthening Carry", text)
        self.assertIn("Selected seeds become additional context", text)

    def test_plant_seed_wrapper_mentions_strengthening_carry(self) -> None:
        text = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-plant-seed/SKILL.md"
        ).read_text()
        self.assertIn("strengthening carry", text)
        self.assertIn("$gsd-new-milestone", text)

