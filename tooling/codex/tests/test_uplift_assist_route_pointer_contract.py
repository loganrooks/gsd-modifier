import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class UpliftAssistRoutePointerContractTests(unittest.TestCase):
    def test_workflow_keeps_pointer_operator_initiated(self) -> None:
        workflow = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/uplift-project.md"
        ).read_text(encoding="utf-8")

        self.assertIn("103-uplift-agent-assist-patterns.md", workflow)
        self.assertIn("06-uplift-docs-governance-classification-packet-template.md", workflow)
        self.assertIn("08-uplift-carrier-gap-identification-packet-template.md", workflow)
        self.assertIn("entry-uplift-audit/outputs/", workflow)
        self.assertIn("entry-uplift-audit/dispositions/", workflow)
        self.assertIn("operator wants one bounded assist-family packet", workflow)
        self.assertIn("do not auto-spawn", workflow)
        self.assertIn("do not widen the helper or CLI", workflow)
        self.assertNotIn("--assist", workflow)

    def test_skill_inherits_pointer_without_mirroring_template_details(self) -> None:
        skill = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-uplift-project/SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("follow the workflow's route block", skill)
        self.assertNotIn("06-uplift-docs-governance-classification-packet-template.md", skill)
        self.assertNotIn("08-uplift-carrier-gap-identification-packet-template.md", skill)


if __name__ == "__main__":
    unittest.main()
