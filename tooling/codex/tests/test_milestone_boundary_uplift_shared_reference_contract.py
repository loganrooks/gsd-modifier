import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class MilestoneBoundaryUpliftSharedReferenceContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_shared_reference_as_add(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(
            entries.get("get-shit-done/references/milestone-boundary-uplift-continuity.md"),
            "add",
        )

    def test_shared_reference_carries_bounded_read_only_structure(self) -> None:
        reference = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/references/milestone-boundary-uplift-continuity.md"
        ).read_text()

        self.assertIn("## Primary Compact Read", reference)
        self.assertIn("## Supporting Narrative Read", reference)
        self.assertIn("## Deeper Typed Read", reference)
        self.assertIn("## Interpretation Frame", reference)
        self.assertIn("## When To Surface", reference)
        self.assertIn("Compatibility posture: observed_basis_only", reference)
        self.assertIn("Do not run `$gsd-uplift-project --write`", reference)

    def test_new_milestone_reads_shared_reference_and_keeps_open_route_read_only(self) -> None:
        workflow = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md"
        ).read_text()

        self.assertIn(
            "@__PROJECT_ROOT__/.codex/get-shit-done/references/milestone-boundary-uplift-continuity.md",
            workflow,
        )
        self.assertIn("## 1.5. Review Project Uplift Milestone-Open Continuity", workflow)
        self.assertIn("Do not run `$gsd-uplift-project --write` from milestone open", workflow)

    def test_complete_milestone_reads_shared_reference_and_keeps_close_route_read_only(self) -> None:
        workflow = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md"
        ).read_text()

        self.assertIn(
            "@__PROJECT_ROOT__/.codex/get-shit-done/references/milestone-boundary-uplift-continuity.md",
            workflow,
        )
        self.assertIn('<step name="review_project_uplift_milestone_close_continuity">', workflow)
        self.assertIn("Do not run `$gsd-uplift-project --write` from milestone close", workflow)


if __name__ == "__main__":
    unittest.main()
