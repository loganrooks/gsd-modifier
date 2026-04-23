import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_entry_mode


ROOT = Path(__file__).resolve().parents[3]


class ReviewRouteContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_review_surfaces(self) -> None:
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/review.md"), "overwrite")
        self.assertEqual(overlay_entry_mode("skills/gsd-review/SKILL.md"), "overwrite")

    def test_review_workflow_uses_run_home_and_helper_layer(self) -> None:
        text = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/review.md"
        ).read_text()
        self.assertIn(
            'python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" prepare-run-home',
            text,
        )
        self.assertIn(".planning/phases/{padded_phase}/reviews/{run_id}/", text)
        self.assertIn('python3 "__PROJECT_ROOT__/tooling/codex/run_claude_probe.py"', text)
        self.assertIn('python3 "__PROJECT_ROOT__/tooling/codex/capture_launch_truth.py"', text)
        self.assertIn("`partial` or `absent`", text)
        self.assertIn("Do not delete the run-home.", text)
        self.assertNotIn("/tmp/gsd-review-", text)

    def test_review_skill_wrapper_mentions_durable_reviewer_trail(self) -> None:
        text = (ROOT / "tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md").read_text()
        self.assertIn("durable per-run reviewer trail", text)
        self.assertIn("launch truth", text)
        self.assertIn("timing calibration", text)
        self.assertIn("last-message salvage", text)
