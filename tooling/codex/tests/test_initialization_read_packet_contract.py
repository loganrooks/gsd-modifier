import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class InitializationReadPacketContractTests(unittest.TestCase):
    def test_overlay_manifest_owns_initialization_workflows(self) -> None:
        manifest = json.loads(
            (ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json").read_text()
        )
        entries = manifest["entries"]
        self.assertEqual(entries.get("get-shit-done/workflows/new-project.md"), "overwrite")
        self.assertEqual(entries.get("get-shit-done/workflows/new-milestone.md"), "overwrite")
        self.assertEqual(entries.get("get-shit-done/workflows/ingest-docs.md"), "overwrite")

    def test_initialization_workflows_use_layered_read_packets(self) -> None:
        surfaces = [
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md",
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md",
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md",
        ]
        for path in surfaces:
            content = path.read_text()
            self.assertIn(
                "@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md",
                content,
            )
            self.assertIn("<supporting_reading>", content)
            self.assertIn("<deeper_reading>", content)

    def test_new_project_and_ingest_keep_uplift_route_explicit(self) -> None:
        new_project = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md"
        ).read_text()
        ingest_docs = (
            ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md"
        ).read_text()
        self.assertIn("$gsd-uplift-project --write", new_project)
        self.assertIn("$gsd-uplift-project --write", ingest_docs)


if __name__ == "__main__":
    unittest.main()
