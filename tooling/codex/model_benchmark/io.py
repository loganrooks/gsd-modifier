"""File IO helpers for model benchmark ingest artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def _path_label(path: str | Path) -> str:
    return str(path)


def read_jsonl_objects(path: str | Path) -> list[dict[str, Any]]:
    """Read newline-delimited JSON objects with line-numbered errors."""

    rows: list[dict[str, Any]] = []
    path_obj = Path(path)
    with path_obj.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{_path_label(path_obj)} line {line_number}: invalid JSON: {exc.msg}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"{_path_label(path_obj)} line {line_number}: JSONL row must be an object")
            rows.append(value)
    return rows


def write_jsonl_objects(path: str | Path, rows: Iterable[dict[str, Any]], overwrite: bool = False) -> None:
    """Write newline-delimited JSON objects, refusing accidental overwrite."""

    path_obj = Path(path)
    if path_obj.exists() and not overwrite:
        raise FileExistsError(f"{_path_label(path_obj)} already exists; pass overwrite=True to replace it")
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    with path_obj.open("w", encoding="utf-8") as handle:
        for index, row in enumerate(rows, start=1):
            if not isinstance(row, dict):
                raise ValueError(f"row {index} must be an object")
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=False))
            handle.write("\n")


def read_json_object(path: str | Path) -> dict[str, Any]:
    """Read a single JSON object file and reject arrays/scalars."""

    path_obj = Path(path)
    with path_obj.open("r", encoding="utf-8") as handle:
        try:
            value = json.load(handle)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{_path_label(path_obj)}: invalid JSON: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{_path_label(path_obj)} must contain a single JSON object")
    return value
