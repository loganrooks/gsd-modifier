"""Golden fixture helpers for the model benchmark telemetry substrate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark import io as bench_io


FIXTURE_ROOT = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "model_benchmark"
MANIFEST_PATH = FIXTURE_ROOT / "manifest.json"

DEFAULT_SAFE_CONTENT_CONTRACTS = frozenset(
    {
        "no_content_access",
        "metadata_only",
        "structural_only",
        "content_hash_or_length_only",
        "derived_features_only",
        "redacted_content_reference",
    }
)

FORBIDDEN_RAW_FIELD_NAMES = frozenset(
    {
        "prompt",
        "raw_prompt",
        "assistant",
        "assistant_message",
        "raw_assistant",
        "tool_result",
        "tool_results",
        "raw_tool_result",
        "transcript",
        "raw_transcript",
        "raw_content",
        "private_content",
    }
)


def load_fixture_manifest() -> dict[str, Any]:
    return bench_io.read_json_object(MANIFEST_PATH)


def fixture_path(fixture_id: str) -> Path:
    manifest = load_fixture_manifest()
    try:
        relative_path = manifest["fixtures"][fixture_id]["path"]
    except KeyError as exc:
        raise ValueError(f"unknown fixture_id: {fixture_id}") from exc
    return FIXTURE_ROOT / relative_path


def read_fixture_json(fixture_id: str, filename: str) -> dict[str, Any]:
    return bench_io.read_json_object(fixture_path(fixture_id) / filename)


def read_fixture_jsonl(fixture_id: str, filename: str) -> list[dict[str, Any]]:
    return bench_io.read_jsonl_objects(fixture_path(fixture_id) / filename)


def flatten_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(flatten_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(flatten_keys(child))
    return keys


def _iter_fixture_objects(path: Path) -> list[dict[str, Any]]:
    if path.suffix == ".json":
        return [bench_io.read_json_object(path)]
    if path.suffix == ".jsonl":
        objects: list[dict[str, Any]] = []
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                try:
                    value = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(value, dict):
                    objects.append(value)
        return objects
    return []


def _lint_object(value: Any, label: str) -> list[str]:
    diagnostics: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_label = f"{label}.{key}"
            if str(key).lower() in FORBIDDEN_RAW_FIELD_NAMES:
                diagnostics.append(f"{key_label}: forbidden raw transcript-like field")
            if key == "content_contract" and child not in DEFAULT_SAFE_CONTENT_CONTRACTS:
                diagnostics.append(f"{key_label}: unsafe default content contract {child}")
            diagnostics.extend(_lint_object(child, key_label))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            diagnostics.extend(_lint_object(child, f"{label}[{index}]"))
    return diagnostics


def lint_default_fixture_privacy() -> list[str]:
    diagnostics: list[str] = []
    for path in sorted(FIXTURE_ROOT.rglob("*")):
        if not path.is_file():
            continue
        for item in _iter_fixture_objects(path):
            diagnostics.extend(_lint_object(item, str(path.relative_to(FIXTURE_ROOT))))
    return diagnostics
