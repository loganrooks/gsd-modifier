import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class SeedMigrationInventoryFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_seed_migration_workflow_and_wrapper(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(
            entries["get-shit-done/workflows/seed-migration-inventory.md"], "add"
        )
        self.assertEqual(
            entries["skills/gsd-seed-migration-inventory/SKILL.md"], "add"
        )

    def test_uplift_route_names_seed_migration_inventory(self) -> None:
        workflow = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/uplift-project.md"
        ).read_text(encoding="utf-8")
        skill = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-uplift-project/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("$gsd-seed-migration-inventory --write", workflow)
        self.assertIn("legacy-unversioned or noncurrent seed posture", workflow)
        self.assertIn("$gsd-seed-migration-inventory --write", skill)

    def test_seed_migration_inventory_workflow_keeps_rewrite_separate(self) -> None:
        workflow = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/seed-migration-inventory.md"
        ).read_text(encoding="utf-8")
        skill = (
            ROOT
            / "tooling/portable-gsd/overlay/skills/gsd-seed-migration-inventory/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("does not rewrite seed files", workflow)
        self.assertIn("SEED-MIGRATION-REPORT.md", workflow)
        self.assertIn("SEED-MIGRATION-MANIFEST.json", workflow)
        self.assertIn("detect-only inventory", skill)


if __name__ == "__main__":
    unittest.main()
