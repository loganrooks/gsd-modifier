import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class UpdateFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_update_surfaces(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(entries["get-shit-done/workflows/update.md"], "overwrite")
        self.assertEqual(entries["skills/gsd-update/SKILL.md"], "overwrite")

    def test_update_workflow_uses_layered_packet_and_explicit_routes(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/update.md"
        ).read_text()
        self.assertIn(
            "@/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/mandatory-initial-read.md".replace(
                "@/home/rookslog/workspace/projects/prix-guesser/",
                "@__PROJECT_ROOT__/",
            ),
            text,
        )
        self.assertIn("<supporting_reading>", text)
        self.assertIn("<deeper_reading>", text)
        self.assertIn("$gsd-health", text)
        self.assertIn("$gsd-uplift-project --write", text)

    def test_update_skill_wrapper_keeps_runtime_and_follow_through_explicit(
        self,
    ) -> None:
        text = (ROOT / "tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md").read_text()
        self.assertIn("runtime/package update", text)
        self.assertIn("$gsd-health", text)
        self.assertIn("$gsd-uplift-project --write", text)

