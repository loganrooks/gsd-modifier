import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class HealthAndMigrationFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_health_and_migration_surfaces(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(entries["get-shit-done/workflows/health.md"], "overwrite")
        self.assertEqual(entries["skills/gsd-health/SKILL.md"], "overwrite")
        self.assertEqual(entries["skills/gsd-from-gsd2/SKILL.md"], "overwrite")

    def test_health_workflow_uses_layered_packet_and_separate_uplift_route(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/health.md"
        ).read_text()
        self.assertIn(
            "@/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/mandatory-initial-read.md".replace("@/home/rookslog/workspace/projects/prix-guesser/", "@__PROJECT_ROOT__/"),
            text,
        )
        self.assertIn("<supporting_reading>", text)
        self.assertIn("<deeper_reading>", text)
        self.assertIn("$gsd-uplift-project --write", text)
        self.assertIn("$gsd-new-project", text)
        self.assertIn("$gsd-ingest-docs", text)

    def test_skill_wrappers_keep_health_and_uplift_follow_through_explicit(self) -> None:
        health_skill = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-health/SKILL.md"
        ).read_text()
        migration_skill = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md"
        ).read_text()

        self.assertIn("$gsd-uplift-project --write", health_skill)
        self.assertIn("structural planning health", health_skill)

        self.assertIn("gsd-sdk query validate.health", migration_skill)
        self.assertIn("$gsd-uplift-project --write", migration_skill)
        self.assertIn("format migration", migration_skill)
