import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class SeedOperatorConsumerFollowThroughContractTests(unittest.TestCase):
    def test_progress_and_resume_surface_seed_corpus_posture_from_uplift_note(self) -> None:
        surfaces = [
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md",
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md",
        ]
        for path in surfaces:
            text = path.read_text(encoding="utf-8")
            self.assertIn("UPLIFT_NOTE.show_seed_corpus_posture", text)
            self.assertIn("Seed corpus posture:", text)
            self.assertIn("Seed posture reason:", text)
            self.assertIn("UPLIFT_NOTE.show_seed_migration_pointer", text)
            self.assertIn("Seed migration candidates:", text)
            self.assertIn("Seed migration packet:", text)
            self.assertIn("project_uplift.py\" progress-note", text)


if __name__ == "__main__":
    unittest.main()
