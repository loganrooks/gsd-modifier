import pathlib
import tempfile
import unittest

from tooling.codex import audit_refmap


class AuditRefmapTests(unittest.TestCase):
    def test_normalize_local_path_strips_line_suffix_from_absolute_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "notes.md"
            source.write_text("# Notes\n", encoding="utf-8")
            target = root / "nested" / "artifact.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# Artifact\n", encoding="utf-8")

            resolved, line_suffix = audit_refmap.normalize_local_path(f"{target}:12", source)

            self.assertEqual(resolved, target.resolve())
            self.assertEqual(line_suffix, ":12")


if __name__ == "__main__":
    unittest.main()
