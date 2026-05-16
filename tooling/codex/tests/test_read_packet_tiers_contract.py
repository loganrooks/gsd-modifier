import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import (
    overlay_entry_mode,
    overlay_inject_source_paths,
    overlay_source_path,
)


ROOT = Path(__file__).resolve().parents[3]


class ReadPacketTiersContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_mandatory_initial_read_reference(self) -> None:
        self.assertEqual(
            overlay_entry_mode("get-shit-done/references/mandatory-initial-read.md"),
            "inject",
        )

    def test_mandatory_initial_read_reference_defines_packet_tiers(self) -> None:
        (source_path,) = overlay_inject_source_paths(
            "get-shit-done/references/mandatory-initial-read.md"
        )
        content = source_path.read_text()
        for needle in (
            "<required_reading>",
            "<supporting_reading>",
            "<deeper_reading>",
            "When a workflow or prompt provides structured helpers, summaries, manifests, or snapshots",
            "do not rewrite or omit it merely to keep the packet narrow",
        ):
            self.assertIn(needle, content)

    def test_entry_surfaces_carry_layered_reading_control(self) -> None:
        surfaces = [
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md",
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md",
            overlay_source_path("get-shit-done/workflows/uplift-project.md"),
        ]
        for path in surfaces:
            content = path.read_text()
            self.assertIn("@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md", content)
            self.assertIn("<supporting_reading>", content)
            self.assertIn("<deeper_reading>", content)


if __name__ == "__main__":
    unittest.main()
