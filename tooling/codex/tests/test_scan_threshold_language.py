import unittest

from tooling.codex.scan_threshold_language import is_meta_instruction_line


class ScanThresholdLanguageTests(unittest.TestCase):
    def test_explicit_forbid_line_counts_as_meta_instruction(self) -> None:
        line = (
            "- [g:r:i] The launch spec should explicitly forbid `adequate`, "
            "`good enough`, `passes`, or `ready` as the governing question."
        )
        self.assertTrue(is_meta_instruction_line(line))

    def test_plain_residue_line_does_not_count_as_meta_instruction(self) -> None:
        line = "- [d:r:i] The family is `ready` once the scanner is quiet."
        self.assertFalse(is_meta_instruction_line(line))


if __name__ == "__main__":
    unittest.main()
