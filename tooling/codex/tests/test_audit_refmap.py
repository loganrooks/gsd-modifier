import json
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

    def test_collect_links_treats_absolute_outside_repo_as_external(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            external_target = root / "external-origin.md"
            external_target.write_text("# External\n", encoding="utf-8")
            source = root / "notes.md"
            source.write_text(f"[External]({external_target})\n", encoding="utf-8")

            links = audit_refmap.collect_links(root)

            self.assertEqual(len(links), 1)
            self.assertEqual(links[0].status, "external-absolute")
            self.assertEqual(links[0].resolved, external_target.resolve().as_posix())

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

    def test_policy_classified_missing_link_does_not_fail_missing_filter(self) -> None:
        link = audit_refmap.LinkOccurrence(
            source=".planning/archive/note.md",
            target_text="../../old/CLAUDE.md",
            line=12,
            resolved="CLAUDE.md",
            status="local-missing",
        )
        entry = audit_refmap.PolicyEntry(
            source=link.source,
            line=link.line,
            raw_target=link.target_text,
            resolved=link.resolved,
            classification="historical_external_origin",
            rationale="Preserved imported archive reference.",
            reviewed_by="test",
        )

        missing = audit_refmap.missing_local_links([link], {audit_refmap.entry_key(entry): entry})

        self.assertEqual(missing, [])

    def test_policy_requires_exact_source_line_target_and_resolved_match(self) -> None:
        link = audit_refmap.LinkOccurrence(
            source=".planning/archive/note.md",
            target_text="../../old/CLAUDE.md",
            line=12,
            resolved="CLAUDE.md",
            status="local-missing",
        )
        entry = audit_refmap.PolicyEntry(
            source=link.source,
            line=13,
            raw_target=link.target_text,
            resolved=link.resolved,
            classification="historical_external_origin",
            rationale="Preserved imported archive reference.",
            reviewed_by="test",
        )

        missing = audit_refmap.missing_local_links([link], {audit_refmap.entry_key(entry): entry})

        self.assertEqual(missing, [link])

    def test_snapshot_separates_classified_and_unclassified_missing_links(self) -> None:
        classified = audit_refmap.LinkOccurrence(
            source=".planning/archive/a.md",
            target_text="../../old/CLAUDE.md",
            line=4,
            resolved="CLAUDE.md",
            status="local-missing",
        )
        unclassified = audit_refmap.LinkOccurrence(
            source="docs/current.md",
            target_text="missing.md",
            line=8,
            resolved="docs/missing.md",
            status="local-missing",
        )
        entry = audit_refmap.PolicyEntry(
            source=classified.source,
            line=classified.line,
            raw_target=classified.target_text,
            resolved=classified.resolved,
            classification="historical_external_origin",
            rationale="Preserved imported archive reference.",
            reviewed_by="test",
        )

        snapshot = audit_refmap.build_snapshot(
            audit_refmap.REPO_ROOT,
            [classified, unclassified],
            {audit_refmap.entry_key(entry): entry},
        )

        self.assertEqual(snapshot["stats"]["classified_missing_links"], 1)
        self.assertEqual(snapshot["stats"]["unclassified_missing_links"], 1)
        self.assertEqual(snapshot["classified_missing_links"][0]["classification"], "historical_external_origin")
        self.assertEqual(snapshot["unclassified_missing_links"][0]["source"], "docs/current.md")

    def test_render_report_separates_classified_and_unclassified_missing_links(self) -> None:
        classified = audit_refmap.LinkOccurrence(
            source=".planning/archive/a.md",
            target_text="../../old/CLAUDE.md",
            line=4,
            resolved="CLAUDE.md",
            status="local-missing",
        )
        unclassified = audit_refmap.LinkOccurrence(
            source="docs/current.md",
            target_text="missing.md",
            line=8,
            resolved="docs/missing.md",
            status="local-missing",
        )
        entry = audit_refmap.PolicyEntry(
            source=classified.source,
            line=classified.line,
            raw_target=classified.target_text,
            resolved=classified.resolved,
            classification="historical_external_origin",
            rationale="Preserved imported archive reference.",
            reviewed_by="test",
        )

        report = audit_refmap.render_map_report(
            audit_refmap.REPO_ROOT,
            [classified, unclassified],
            {audit_refmap.entry_key(entry): entry},
        )

        self.assertIn("Classified missing links: `1`", report)
        self.assertIn("Unclassified missing links: `1`", report)
        self.assertIn("## Unclassified Missing Local Targets", report)
        self.assertIn("## Classified Missing Local Targets", report)

    def test_load_policy_rejects_unsupported_classification(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            policy_path = pathlib.Path(tmpdir) / "policy.json"
            policy_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "entries": [
                            {
                                "source": "docs/current.md",
                                "line": 1,
                                "raw_target": "missing.md",
                                "resolved": "docs/missing.md",
                                "classification": "ignored",
                                "rationale": "bad",
                                "reviewed_by": "test",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "unsupported classification"):
                audit_refmap.load_policy(policy_path)

    def test_load_policy_rejects_mismatched_classification_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            policy_path = pathlib.Path(tmpdir) / "policy.json"
            policy_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "classification_counts": {"historical_external_origin": 2},
                        "entries": [
                            {
                                "source": "docs/current.md",
                                "line": 1,
                                "raw_target": "missing.md",
                                "resolved": "docs/missing.md",
                                "classification": "historical_external_origin",
                                "rationale": "preserved",
                                "reviewed_by": "test",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "classification_counts do not match"):
                audit_refmap.load_policy(policy_path)


if __name__ == "__main__":
    unittest.main()
