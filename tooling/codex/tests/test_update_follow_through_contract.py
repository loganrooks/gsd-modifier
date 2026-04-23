import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_entry_mode


ROOT = Path(__file__).resolve().parents[3]


class UpdateFollowThroughContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_update_surfaces(self) -> None:
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/update.md"), "overwrite")
        self.assertEqual(overlay_entry_mode("skills/gsd-update/SKILL.md"), "overwrite")

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
        self.assertIn(
            "@__PROJECT_ROOT__/.codex/get-shit-done/references/entry-runtime-uplift-continuity.md",
            text,
        )
        self.assertIn("PREFERRED_RUNTIME` is `codex` or `claude`", text)
        self.assertIn("Do not run `$gsd-uplift-project --write` from `update.md`", text)
        self.assertIn(
            "before the clean-install step below rewrites the runtime copy via overlay rematerialization",
            text,
        )
        self.assertIn("$gsd-health", text)
        self.assertIn("$gsd-uplift-project --write", text)

    def test_update_skill_wrapper_keeps_runtime_and_follow_through_explicit(
        self,
    ) -> None:
        text = (ROOT / "tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md").read_text()
        self.assertIn("runtime/package update", text)
        self.assertIn("only when the active runtime is `.codex` or `.claude`", text)
        self.assertIn(
            "It does not translate that continuity into broader parity, matrix, or version-window claims.",
            text,
        )
        self.assertIn("$gsd-health", text)
        self.assertIn("$gsd-uplift-project --write", text)
