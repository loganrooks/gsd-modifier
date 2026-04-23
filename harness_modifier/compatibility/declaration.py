"""Load the portable compatibility declaration for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


DECLARATION_REL_PATH = "harness_modifier/compatibility/declaration.json"
DECLARATION_PATH = pathlib.Path(__file__).resolve().with_name("declaration.json")

DEFAULT_RUNTIME = "codex"


@functools.lru_cache(maxsize=1)
def _load_declaration() -> dict[str, Any]:
    return json.loads(DECLARATION_PATH.read_text(encoding="utf-8"))


def load_declaration() -> dict[str, Any]:
    return copy.deepcopy(_load_declaration())


def runtime_profiles() -> dict[str, Any]:
    return load_declaration()["runtime_profiles"]


def supported_runtimes() -> list[str]:
    return list(runtime_profiles())


def core_runtimes() -> list[str]:
    declaration = load_declaration()
    return list(declaration["support_claims"]["active_core_profiles"])


def runtime_profile(runtime: str) -> dict[str, Any]:
    profiles = runtime_profiles()
    if runtime not in profiles:
        raise KeyError(f"unknown runtime profile: {runtime}")
    return copy.deepcopy(profiles[runtime])


def runtime_root(runtime: str) -> str:
    return str(runtime_profile(runtime)["runtime_root"])


def version_source(runtime: str) -> str:
    return str(runtime_profile(runtime)["version_source"])


def manifest_version_source(runtime: str) -> str:
    return str(runtime_profile(runtime)["manifest_version_source"])


def overlay_schema_version() -> int:
    return int(load_declaration()["overlay_schema_version"])


def uplift_manifest_schema_version() -> int:
    return int(load_declaration()["uplift_manifest_schema_version"])
