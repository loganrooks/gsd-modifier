import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class PropagationReviewRouteContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_propagation_review_surfaces(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(
            entries["get-shit-done/workflows/propagation-review.md"], "add"
        )
        self.assertEqual(entries["skills/gsd-propagation-review/SKILL.md"], "add")

    def test_workflow_reads_baseline_delta_and_names_runtime_gate_tools(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/propagation-review.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "95-upstream-pristine-propagation-baseline-first-slice.md",
            text,
        )
        self.assertIn(
            "96-repo-local-propagation-delta-first-slice.md",
            text,
        )
        self.assertIn("manifest_install_coherence.py", text)
        self.assertIn("harness_canary.py report . --strict", text)
        self.assertIn("Do not let a clean tool result replace contextual reread.", text)

    def test_skill_keeps_route_read_only_and_specialist_handoffs_explicit(self) -> None:
        text = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-propagation-review/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("$gsd-propagation-review", text)
        self.assertIn("Default posture is read-only.", text)
        self.assertIn("--write-note PATH", text)
        self.assertIn("$gsd-uplift-project --write", text)
        self.assertIn("$gsd-seed-migration-inventory", text)


if __name__ == "__main__":
    unittest.main()
