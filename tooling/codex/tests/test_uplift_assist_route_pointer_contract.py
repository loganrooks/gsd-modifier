import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_source_path

ROOT = Path(__file__).resolve().parents[3]


class UpliftAssistRoutePointerContractTests(unittest.TestCase):
    def test_workflow_keeps_pointer_operator_initiated(self) -> None:
        workflow = overlay_source_path("get-shit-done/workflows/uplift-project.md").read_text(encoding="utf-8")

        self.assertIn("host uplift assist-family reference", workflow)
        self.assertIn("host docs-governance classification packet entry", workflow)
        self.assertIn("host carrier-gap identification packet entry", workflow)
        self.assertIn("entry-uplift-audit/outputs/", workflow)
        self.assertIn("entry-uplift-audit/dispositions/", workflow)
        self.assertIn("operator wants one bounded assist-family packet", workflow)
        self.assertIn("do not auto-spawn", workflow)
        self.assertIn("do not widen the helper or CLI", workflow)
        self.assertNotIn("--assist", workflow)

    def test_skill_inherits_pointer_without_mirroring_template_details(self) -> None:
        skill = overlay_source_path("skills/gsd-uplift-project/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("follow the workflow's route block", skill)
        self.assertNotIn("06-uplift-docs-governance-classification-packet-template.md", skill)
        self.assertNotIn("08-uplift-carrier-gap-identification-packet-template.md", skill)


if __name__ == "__main__":
    unittest.main()
