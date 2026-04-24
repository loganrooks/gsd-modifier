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

    def test_normalize_local_path_strips_line_range_suffix_from_absolute_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "notes.md"
            source.write_text("# Notes\n", encoding="utf-8")
            target = root / "nested" / "artifact.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# Artifact\n", encoding="utf-8")

            resolved, line_suffix = audit_refmap.normalize_local_path(f"{target}:12-18", source)

            self.assertEqual(resolved, target.resolve())
            self.assertEqual(line_suffix, ":12-18")

    def test_normalize_local_path_ignores_braced_template_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "notes.md"
            source.write_text("# Notes\n", encoding="utf-8")

            resolved, line_suffix = audit_refmap.normalize_local_path("./{phase}-USER-SETUP.md", source)

            self.assertIsNone(resolved)
            self.assertEqual(line_suffix, "")

    def test_normalize_local_path_ignores_shell_style_template_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "notes.md"
            source.write_text("# Notes\n", encoding="utf-8")

            resolved, line_suffix = audit_refmap.normalize_local_path("./quick/${quick_id}-${slug}/", source)

            self.assertIsNone(resolved)
            self.assertEqual(line_suffix, "")

    def test_normalize_local_path_preserves_missing_dot_relative_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "nested" / "notes.md"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text("# Notes\n", encoding="utf-8")

            resolved, line_suffix = audit_refmap.normalize_local_path("../moved.md", source)

            self.assertEqual(resolved, (root / "moved.md").resolve())
            self.assertEqual(line_suffix, "")

    def test_normalize_local_path_treats_planning_path_as_repo_relative(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "nested" / "notes.md"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text("# Notes\n", encoding="utf-8")

            resolved, line_suffix = audit_refmap.normalize_local_path(".planning/STATE.md", source)

            self.assertEqual(resolved, (audit_refmap.REPO_ROOT / ".planning/STATE.md").resolve())
            self.assertEqual(line_suffix, "")

    def test_load_moves_accepts_absolute_old_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            old = root / "origin" / "artifact.md"
            old.parent.mkdir(parents=True, exist_ok=True)
            old.write_text("# Artifact\n", encoding="utf-8")
            moves_file = root / "moves.tsv"
            moves_file.write_text(
                f"{old}\tdocs/origin-audit/imported/artifact.md\n",
                encoding="utf-8",
            )

            moves = audit_refmap.load_moves(moves_file)

            self.assertEqual(len(moves), 1)
            self.assertEqual(moves[0].old_abs, old.resolve().as_posix())
            self.assertEqual(moves[0].old_rel, old.as_posix())
            self.assertTrue(moves[0].new_abs.endswith("/docs/origin-audit/imported/artifact.md"))

    def test_rewrite_allows_duplicate_old_names_when_target_is_same(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            source = root / "notes.md"
            source.write_text("[Artifact](artifact.md)\n", encoding="utf-8")
            moves = [
                audit_refmap.Move(
                    old_abs=(root / "origin-a" / "artifact.md").as_posix(),
                    new_abs=(root / "new" / "artifact.md").as_posix(),
                    old_rel="origin-a/artifact.md",
                    new_rel="new/artifact.md",
                    old_name="artifact.md",
                ),
                audit_refmap.Move(
                    old_abs=(root / "origin-b" / "artifact.md").as_posix(),
                    new_abs=(root / "new" / "artifact.md").as_posix(),
                    old_rel="origin-b/artifact.md",
                    new_rel="new/artifact.md",
                    old_name="artifact.md",
                ),
            ]

            audit_refmap.rewrite_workspace(root, moves, apply=True)

            self.assertEqual(source.read_text(encoding="utf-8"), "[Artifact](new/artifact.md)\n")

    def test_rewrite_recalculates_relative_link_when_source_moves(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            target = root / "artifact.md"
            target.write_text("# Artifact\n", encoding="utf-8")
            moved_source = root / "nested" / "notes.md"
            moved_source.parent.mkdir(parents=True, exist_ok=True)
            moved_source.write_text("[Artifact](artifact.md)\n", encoding="utf-8")
            moves = [
                audit_refmap.Move(
                    old_abs=(root / "notes.md").resolve().as_posix(),
                    new_abs=moved_source.resolve().as_posix(),
                    old_rel="notes.md",
                    new_rel="nested/notes.md",
                    old_name="notes.md",
                )
            ]

            audit_refmap.rewrite_workspace(root, moves, apply=True)

            self.assertEqual(moved_source.read_text(encoding="utf-8"), "[Artifact](../artifact.md)\n")

    def test_rewrite_recalculates_relative_link_when_source_and_target_move(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            moved_target = root / "assets" / "artifact.md"
            moved_target.parent.mkdir(parents=True, exist_ok=True)
            moved_target.write_text("# Artifact\n", encoding="utf-8")
            moved_source = root / "docs" / "notes.md"
            moved_source.parent.mkdir(parents=True, exist_ok=True)
            moved_source.write_text("[Artifact](artifact.md)\n", encoding="utf-8")
            moves = [
                audit_refmap.Move(
                    old_abs=(root / "notes.md").resolve().as_posix(),
                    new_abs=moved_source.resolve().as_posix(),
                    old_rel="notes.md",
                    new_rel="docs/notes.md",
                    old_name="notes.md",
                ),
                audit_refmap.Move(
                    old_abs=(root / "artifact.md").resolve().as_posix(),
                    new_abs=moved_target.resolve().as_posix(),
                    old_rel="artifact.md",
                    new_rel="assets/artifact.md",
                    old_name="artifact.md",
                ),
            ]

            audit_refmap.rewrite_workspace(root, moves, apply=True)

            self.assertEqual(moved_source.read_text(encoding="utf-8"), "[Artifact](../assets/artifact.md)\n")

    def test_rewrite_preserves_line_range_when_recalculating_moved_source_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            target = root / "artifact.md"
            target.write_text("# Artifact\n", encoding="utf-8")
            moved_source = root / "nested" / "notes.md"
            moved_source.parent.mkdir(parents=True, exist_ok=True)
            moved_source.write_text("[Artifact](artifact.md:12-18)\n", encoding="utf-8")
            moves = [
                audit_refmap.Move(
                    old_abs=(root / "notes.md").resolve().as_posix(),
                    new_abs=moved_source.resolve().as_posix(),
                    old_rel="notes.md",
                    new_rel="nested/notes.md",
                    old_name="notes.md",
                )
            ]

            audit_refmap.rewrite_workspace(root, moves, apply=True)

            self.assertEqual(moved_source.read_text(encoding="utf-8"), "[Artifact](../artifact.md:12-18)\n")


if __name__ == "__main__":
    unittest.main()
