import pathlib
import unittest

from tooling.codex.tests.overlay_paths import overlay_entry_mode


REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]


class SpecFutureCarryContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_spec_surfaces(self) -> None:
        self.assertEqual(overlay_entry_mode("get-shit-done/workflows/spec-phase.md"), "overwrite")
        self.assertEqual(overlay_entry_mode("get-shit-done/templates/spec.md"), "overwrite")

    def test_spec_template_exposes_future_aware_notes(self) -> None:
        template = (
            REPO_ROOT
            / "tooling"
            / "portable-gsd"
            / "overlay"
            / "get-shit-done"
            / "templates"
            / "spec.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Future-Aware Notes", template)
        self.assertIn("### Protected Seams", template)
        self.assertIn("### Explicit Non-Decisions", template)
        self.assertIn("### Current Posture", template)
        self.assertIn("### Future Shape Notes", template)
        self.assertIn("### Strengthening Opportunities", template)

    def test_spec_phase_and_discuss_phase_move_together(self) -> None:
        spec_phase = (
            REPO_ROOT
            / "tooling"
            / "portable-gsd"
            / "overlay"
            / "get-shit-done"
            / "workflows"
            / "spec-phase.md"
        ).read_text(encoding="utf-8")
        discuss_phase = (
            REPO_ROOT
            / "tooling"
            / "portable-gsd"
            / "overlay"
            / "get-shit-done"
            / "workflows"
            / "discuss-phase.md"
        ).read_text(encoding="utf-8")

        self.assertIn(".planning/LONG-ARC.md", spec_phase)
        self.assertIn("Future-Aware Notes", spec_phase)
        self.assertIn("SPEC_FILE=$(ls ${phase_dir}/*-SPEC.md", discuss_phase)
        self.assertIn("Source 0 (now):** If `SPEC_FILE` exists", discuss_phase)
        self.assertIn("If `SPEC_FILE` carries `Future-Aware Notes`", discuss_phase)


if __name__ == "__main__":
    unittest.main()
