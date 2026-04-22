import re
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
            self.assertIn("Seed migration breakdown:", text)
            self.assertIn("Seed migration inventory:", text)
            self.assertIn("Seed migration write packet:", text)
            self.assertIn("project_uplift.py\" progress-note", text)
            self.assertRegex(
                text,
                re.compile(
                    r"Only show these lines when `UPLIFT_NOTE\.show_seed_migration_pointer` is `true`:"
                    r"[\s\S]*?- Seed migration candidates: \{seed_migration_candidate_count\}"
                    r"[\s\S]*?- Seed migration breakdown: \{seed_migration_candidate_breakdown\}"
                    r"[\s\S]*?- Seed migration inventory: \{seed_migration_inspect_pointer\}"
                    r"[\s\S]*?- Seed migration write packet: \{seed_migration_write_pointer\}",
                    re.MULTILINE,
                ),
            )


if __name__ == "__main__":
    unittest.main()
