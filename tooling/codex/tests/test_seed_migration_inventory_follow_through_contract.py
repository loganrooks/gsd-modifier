import json
import re
import unittest
from pathlib import Path

from harness_modifier.compatibility import seed_contract as compatibility_seed_contract
from tooling.codex import project_uplift as pu
from tooling.codex.tests.overlay_paths import overlay_entry_mode, overlay_source_path


ROOT = Path(__file__).resolve().parents[3]
SEED_CONTRACT = compatibility_seed_contract.load_seed_contract()


class SeedMigrationInventoryFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_seed_migration_workflow_and_wrapper(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        self.assertEqual(
            overlay_entry_mode("get-shit-done/workflows/seed-migration-inventory.md"), "add"
        )
        self.assertEqual(
            overlay_entry_mode("skills/gsd-seed-migration-inventory/SKILL.md"), "add"
        )

    def test_uplift_route_names_seed_migration_inventory(self) -> None:
        workflow = overlay_source_path("get-shit-done/workflows/uplift-project.md").read_text(encoding="utf-8")
        skill = overlay_source_path("skills/gsd-uplift-project/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("$gsd-seed-migration-inventory", workflow)
        self.assertIn("$gsd-seed-migration-inventory --write", workflow)
        self.assertIn("current-version shape gaps", workflow)
        self.assertIn("$gsd-seed-migration-inventory", skill)
        self.assertIn("$gsd-seed-migration-inventory --write", skill)

    def test_project_uplift_pointer_commands_stay_bound_to_specialist_skill(self) -> None:
        skill = overlay_source_path("skills/gsd-seed-migration-inventory/SKILL.md").read_text(encoding="utf-8")
        self.assertIn(pu.SEED_MIGRATION_SKILL_COMMAND, skill)
        self.assertIn(pu.SEED_MIGRATION_WRITE_COMMAND, skill)

    def test_seed_migration_inventory_workflow_keeps_rewrite_separate(self) -> None:
        workflow = overlay_source_path("get-shit-done/workflows/seed-migration-inventory.md").read_text(encoding="utf-8")
        skill = overlay_source_path("skills/gsd-seed-migration-inventory/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("does not rewrite seed files", workflow)
        self.assertIn("SEED-MIGRATION-REPORT.md", workflow)
        self.assertIn("SEED-MIGRATION-MANIFEST.json", workflow)
        self.assertIn("detect-only inventory", skill)

    def test_seed_migration_helper_shape_contract_tracks_plant_seed_template(self) -> None:
        workflow = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Write `.planning/seeds/SEED-{PADDED}-{slug}.md`:", workflow)
        template = workflow.split("```markdown\n", 1)[1].split("\n```", 1)[0]
        frontmatter_match = re.search(r"^---\n([\s\S]+?)\n---", template)
        self.assertIsNotNone(frontmatter_match)
        frontmatter_keys = {
            key
            for key in re.findall(r"^([A-Za-z0-9_-]+):", frontmatter_match.group(1), re.M)
        }
        section_headings = {
            heading for heading in re.findall(r"^##\s+(.+?)\s*$", template, re.M)
        }

        self.assertEqual(frontmatter_keys, set(SEED_CONTRACT["required_seed_frontmatter_keys"]))
        self.assertEqual(section_headings, set(SEED_CONTRACT["required_seed_section_headings"]))


if __name__ == "__main__":
    unittest.main()
