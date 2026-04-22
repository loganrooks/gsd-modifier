import pathlib
import tempfile
import unittest

from tooling.codex import seed_migration_inventory as smi


class SeedMigrationInventoryTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _write_seed(
        self,
        root: pathlib.Path,
        rel_path: str,
        *,
        seed_id: str,
        title: str,
        version: str | None,
        include_current_shape: bool,
    ) -> None:
        version_line = f"seed_contract_version: {version}\n" if version is not None else ""
        body = [
            "---",
            f"id: {seed_id}",
            version_line.rstrip(),
            "status: dormant",
        ]
        if include_current_shape:
            body.extend(
                [
                    "planted: 2026-04-22",
                    "planted_during: milestone",
                    "trigger_when: later",
                    "scope: Medium",
                ]
            )
        else:
            body.append("trigger_when: later")
        body.extend(
            [
                "---",
                "",
                f"# {seed_id}: {title}",
                "",
                "## Why This Matters",
                "",
                "- Keep the route visible.",
                "",
                "## When to Surface",
                "",
                "- later",
            ]
        )
        if include_current_shape:
            body.extend(
                [
                    "",
                    "## Scope Estimate",
                    "",
                    "- Medium",
                    "",
                    "## Strengthening Carry",
                    "",
                    "- Intensify the route.",
                    "",
                    "## Breadcrumbs",
                    "",
                    "- notes",
                    "",
                    "## Notes",
                    "",
                    "- context",
                ]
            )
        self._write(root, rel_path, "\n".join(body) + "\n")

    def test_detect_surfaces_legacy_noncurrent_and_shape_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._write_seed(
                root,
                ".planning/seeds/SEED-001-legacy.md",
                seed_id="SEED-001",
                title="Legacy",
                version=None,
                include_current_shape=False,
            )
            self._write_seed(
                root,
                ".planning/seeds/SEED-002-current-gap.md",
                seed_id="SEED-002",
                title="Current Gap",
                version=smi.pu.CURRENT_SEED_CONTRACT_VERSION,
                include_current_shape=False,
            )
            self._write_seed(
                root,
                ".planning/seeds/SEED-003-old-version.md",
                seed_id="SEED-003",
                title="Old Version",
                version="1",
                include_current_shape=True,
            )

            analysis = smi.analyze_repo(root)

            self.assertEqual(analysis["route_state"], "surfaced")
            self.assertEqual(analysis["seed_count"], 3)
            self.assertEqual(analysis["migration_candidate_count"], 3)
            self.assertIn("legacy-unversioned seeds still present: 1", analysis["reasons"])
            self.assertIn("noncurrent seed contract versions still present: v1=1", analysis["reasons"])
            self.assertIn("seed contract-shape gaps still visible: 2", analysis["reasons"])
            entries = {entry["seed_id"]: entry for entry in analysis["entries"]}
            self.assertEqual(entries["SEED-001"]["contract_vintage"], "legacy_unversioned")
            self.assertIn("seed_contract_version", entries["SEED-001"]["missing_frontmatter_keys"])
            self.assertIn("stamp `seed_contract_version: 2`", entries["SEED-001"]["migration_moves"])
            self.assertEqual(entries["SEED-002"]["contract_vintage"], "current_contract")
            self.assertIn("scope", entries["SEED-002"]["missing_frontmatter_keys"])
            self.assertIn("Strengthening Carry", entries["SEED-002"]["missing_section_headings"])
            self.assertEqual(entries["SEED-003"]["contract_vintage"], "noncurrent:1")
            self.assertIn("move `seed_contract_version` from `1` to `2`", entries["SEED-003"]["migration_moves"])

    def test_detect_stays_quiet_for_current_contract_only_corpus(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._write_seed(
                root,
                ".planning/seeds/SEED-004-current.md",
                seed_id="SEED-004",
                title="Current",
                version=smi.pu.CURRENT_SEED_CONTRACT_VERSION,
                include_current_shape=True,
            )

            analysis = smi.analyze_repo(root)

            self.assertEqual(analysis["route_state"], "dormant")
            self.assertEqual(analysis["migration_candidate_count"], 0)
            self.assertEqual(analysis["reasons"], [])
            self.assertEqual(analysis["entries"][0]["route_state"], "current_contract_visible")

    def test_write_outputs_records_report_and_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            self._write_seed(
                root,
                ".planning/seeds/SEED-005-legacy.md",
                seed_id="SEED-005",
                title="Legacy",
                version=None,
                include_current_shape=False,
            )

            analysis = smi.analyze_repo(root)
            written = smi.write_outputs(root, analysis)

            self.assertEqual(written["report_path"], smi.REPORT_REL_PATH)
            self.assertEqual(written["manifest_path"], smi.MANIFEST_REL_PATH)
            report_text = (root / smi.REPORT_REL_PATH).read_text(encoding="utf-8")
            self.assertIn("# Seed Migration Report", report_text)
            self.assertIn("Route state: surfaced", report_text)
            self.assertIn("SEED-005: Legacy", report_text)
            self.assertTrue((root / smi.MANIFEST_REL_PATH).exists())


if __name__ == "__main__":
    unittest.main()
