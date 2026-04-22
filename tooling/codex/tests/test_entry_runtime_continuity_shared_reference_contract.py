import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class EntryRuntimeContinuitySharedReferenceContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_shared_reference_as_add(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(
            entries.get("get-shit-done/references/entry-runtime-uplift-continuity.md"),
            "add",
        )

    def test_shared_reference_carries_bounded_read_only_structure(self) -> None:
        reference = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/references/entry-runtime-uplift-continuity.md"
        ).read_text()

        self.assertIn("## Primary Compact Read", reference)
        self.assertIn("## Supporting Narrative Read", reference)
        self.assertIn("## Deeper Typed Read", reference)
        self.assertIn("## Interpretation Frame", reference)
        self.assertIn("## When To Surface", reference)
        self.assertIn("Compatibility posture: observed_basis_only", reference)
        self.assertIn("Do not run `$gsd-uplift-project --write`", reference)
        self.assertIn("### `new-project.md` Greenfield", reference)
        self.assertIn("### `new-project.md` Brownfield", reference)
        self.assertIn("### `ingest-docs.md` New Mode", reference)
        self.assertIn("### `ingest-docs.md` Merge Mode", reference)

    def test_mandatory_initial_read_stays_grammar_only(self) -> None:
        text = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md"
        ).read_text()
        self.assertNotIn("entry-runtime-uplift-continuity.md", text)

    def test_new_project_points_at_shared_reference_and_keeps_route_read_only(self) -> None:
        workflow = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md"
        ).read_text()

        self.assertIn(
            "@__PROJECT_ROOT__/.codex/get-shit-done/references/entry-runtime-uplift-continuity.md",
            workflow,
        )
        self.assertIn("## 1.5. Review Entry Runtime Continuity", workflow)
        self.assertIn("Do not run `$gsd-uplift-project --write` from `new-project.md`", workflow)

    def test_ingest_docs_points_at_shared_reference_and_keeps_route_read_only(self) -> None:
        workflow = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md"
        ).read_text()

        self.assertIn(
            "@__PROJECT_ROOT__/.codex/get-shit-done/references/entry-runtime-uplift-continuity.md",
            workflow,
        )
        self.assertIn('<step name="review_entry_runtime_continuity">', workflow)
        self.assertIn("Do not run `$gsd-uplift-project --write` inside ingest", workflow)


if __name__ == "__main__":
    unittest.main()
