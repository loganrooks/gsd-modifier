import json
import shutil
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

from tooling.codex.tests.overlay_paths import overlay_entry_mode


ROOT = Path(__file__).resolve().parents[3]
AUDIT_HELPER = ROOT / "tooling/portable-gsd/overlay/get-shit-done/bin/lib/audit.cjs"
LIB_RUNTIME_DIR = ROOT / ".codex/get-shit-done/bin/lib"
OVERLAY_MANIFEST = ROOT / "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"
MILESTONE_CLOSE_WORKFLOW = ROOT / "tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md"


class SeedAuditGateFollowThroughContractTests(unittest.TestCase):
    def _write(self, root: Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _run_audit_helper(self, repo_root: Path) -> dict:
        with tempfile.TemporaryDirectory() as moduledir:
            module_root = Path(moduledir)
            lib_dir = module_root / "lib"
            lib_dir.mkdir(parents=True, exist_ok=True)
            for dep in LIB_RUNTIME_DIR.glob("*.cjs"):
                if dep.name == "audit.cjs":
                    continue
                shutil.copy2(dep, lib_dir / dep.name)
            shutil.copy2(AUDIT_HELPER, lib_dir / "audit.cjs")

            script = textwrap.dedent(
                f"""
                const audit = require({json.dumps(str(lib_dir / "audit.cjs"))});
                const result = audit.auditOpenArtifacts({json.dumps(str(repo_root))});
                const report = audit.formatAuditReport(result);
                process.stdout.write(JSON.stringify({{ result, report }}));
                """
            )
            completed = subprocess.run(
                ["node", "-e", script],
                cwd=ROOT,
                check=True,
                text=True,
                capture_output=True,
            )
            return json.loads(completed.stdout)

    def test_seed_audit_surfaces_vintage_why_and_strengthening_carry(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            self._write(
                repo_root,
                ".planning/seeds/SEED-001-current-route.md",
                "---\n"
                "id: SEED-001\n"
                "seed_contract_version: 2\n"
                "status: dormant\n"
                "trigger_when: later\n"
                "---\n\n"
                "# SEED-001: Current Route\n\n"
                "## Why This Matters\n\n"
                "- Preserve the richer route for later milestone-open decisions.\n\n"
                "## Strengthening Carry\n\n"
                "- Intensify the current route instead of re-discovering it.\n",
            )
            self._write(
                repo_root,
                ".planning/seeds/SEED-002-legacy-route.md",
                "---\n"
                "id: SEED-002\n"
                "status: active\n"
                "trigger_when: later\n"
                "---\n\n"
                "# SEED-002: Legacy Route\n\n"
                "## Why This Matters\n\n"
                "- Keep the older route visible until it is migrated.\n",
            )

            payload = self._run_audit_helper(repo_root)
            result = payload["result"]
            seeds = {
                item["seed_id"]: item
                for item in result["items"]["seeds"]
                if not item.get("scan_error")
            }

            self.assertEqual(result["counts"]["seeds"], 2)
            self.assertEqual(seeds["SEED-001"]["contract_vintage"], "2")
            self.assertEqual(seeds["SEED-001"]["strengthening_carry_status"], "present")
            self.assertIn("Preserve the richer route", seeds["SEED-001"]["why_this_matters_excerpt"])
            self.assertIn("Intensify the current route", seeds["SEED-001"]["strengthening_carry_excerpt"])
            self.assertEqual(seeds["SEED-002"]["contract_vintage"], "legacy_unversioned")
            self.assertEqual(seeds["SEED-002"]["strengthening_carry_status"], "none")
            self.assertEqual(seeds["SEED-002"]["strengthening_carry_excerpt"], "")
            self.assertIn("[vintage: 2] [strengthening: present]", payload["report"])
            self.assertIn("[vintage: legacy_unversioned] [strengthening: none]", payload["report"])
            self.assertIn("why: Preserve the richer route", payload["report"])
            self.assertIn("carry: Intensify the current route", payload["report"])

    def test_overlay_manifest_and_milestone_close_keep_seed_audit_contract_visible(self) -> None:
        self.assertEqual(
            overlay_entry_mode("get-shit-done/bin/lib/audit.cjs"),
            "overwrite",
        )

        text = MILESTONE_CLOSE_WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("contract vintage", text)
        self.assertIn("strengthening carry", text)
        self.assertIn("flattening them back to bare seed IDs", text)


if __name__ == "__main__":
    unittest.main()
