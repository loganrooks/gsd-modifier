"""Codex runtime adapter."""

from __future__ import annotations

import os
import pathlib
import subprocess
from typing import Any

from harness_modifier.compatibility import declaration as compatibility_declaration


class CodexRuntimeAdapter:
    name = "codex"
    profile_name = "codex-core"

    @property
    def profile(self) -> dict[str, Any]:
        return compatibility_declaration.runtime_profile(self.name)

    @property
    def runtime_root(self) -> str:
        return str(self.profile["runtime_root"])

    def detect(self, repo_root: pathlib.Path) -> dict[str, Any]:
        runtime_root = repo_root / self.runtime_root
        return {
            "runtime": self.name,
            "profile_name": self.profile_name,
            "runtime_root": self.runtime_root,
            "present": runtime_root.exists(),
            "version_source": str(self.profile["version_source"]),
            "manifest_version_source": str(self.profile["manifest_version_source"]),
        }

    def install_regular_gsd(self, repo_root: pathlib.Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["npx", "get-shit-done-cc", "--codex", "--local"],
            cwd=repo_root,
            check=False,
            capture_output=True,
            text=True,
            env={**os.environ, "GSD_ALLOW_OFF_PATH": "1"},
        )

    def capture_pristine(self, repo_root: pathlib.Path) -> dict[str, Any]:
        from harness_modifier.contract import portable_gsd_contract as pgc

        return pgc.capture_pristine_overwrites(repo_root, runtime=self.name)

    def apply_overlay(self, repo_root: pathlib.Path, compact_prompt: str) -> list[str]:
        from harness_modifier.contract import portable_gsd_contract as pgc

        return pgc.apply_overlay(repo_root, compact_prompt, runtime=self.name)

    def apply_defaults(self, repo_root: pathlib.Path) -> None:
        from harness_modifier.contract import portable_gsd_contract as pgc

        pgc.apply_reasoning_defaults(repo_root, runtime=self.name)

    def verify_materialized(self, repo_root: pathlib.Path, compact_prompt: str) -> dict[str, Any]:
        from harness_modifier.contract import portable_gsd_contract as pgc

        return pgc.build_materialization_report(repo_root, compact_prompt, runtime=self.name)

    def capture_probe_evidence(self, repo_root: pathlib.Path) -> dict[str, Any]:
        return {
            "runtime": self.name,
            "runtime_root": self.runtime_root,
            "probe_family": "runtime_visibility",
            "note": "Codex parity evidence is derived from runtime visibility and materialization checks.",
        }
