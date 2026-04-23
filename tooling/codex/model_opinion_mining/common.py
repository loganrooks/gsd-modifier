"""Shared helpers for opinion-mining collection scripts."""

from __future__ import annotations

import json
import pathlib
import re
from datetime import datetime, timezone
from typing import Any


REQUIRED_SEED_FIELDS = ("source_id", "platform", "url", "query", "claim_tags", "collection_caveat")
SAFE_HEADER_KEYS = ("content-type", "etag", "last-modified", "cache-control")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_jsonl(path: pathlib.Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSONL row: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_number}: row must be an object")
        rows.append(row)
    return rows


def write_jsonl(path: pathlib.Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def read_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: pathlib.Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_seed_rows(path: pathlib.Path) -> list[dict[str, Any]]:
    rows = read_jsonl(path) if path.suffix == ".jsonl" else read_json(path)
    if isinstance(rows, dict):
        rows = rows.get("sources")
    if not isinstance(rows, list):
        raise ValueError("seed file must be JSONL or a JSON list/object with sources[]")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"seed row {index} must be an object")
        missing = [field for field in REQUIRED_SEED_FIELDS if field not in row]
        if missing:
            raise ValueError(f"seed row {index} missing required fields: {', '.join(missing)}")
        source_id = str(row["source_id"]).strip()
        if not source_id:
            raise ValueError(f"seed row {index} has empty source_id")
        if source_id in seen:
            raise ValueError(f"duplicate source_id: {source_id}")
        seen.add(source_id)
        claim_tags = row["claim_tags"]
        if not isinstance(claim_tags, list) or not all(isinstance(tag, str) for tag in claim_tags):
            raise ValueError(f"seed row {index} claim_tags must be a list of strings")
        normalized.append(
            {
                **row,
                "source_id": source_id,
                "platform": str(row["platform"]).strip(),
                "url": str(row["url"]).strip(),
                "query": str(row["query"]).strip(),
                "claim_tags": claim_tags,
                "collection_caveat": str(row["collection_caveat"]).strip(),
            }
        )
    return normalized


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "-", value.strip())
    return slug.strip("-") or "source"


def safe_headers(headers: dict[str, str]) -> dict[str, str]:
    lowered = {key.lower(): value for key, value in headers.items()}
    return {key: lowered[key] for key in SAFE_HEADER_KEYS if key in lowered}


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    compact: list[str] = []
    blank = False
    for line in lines:
        if not line:
            if not blank and compact:
                compact.append("")
            blank = True
            continue
        compact.append(line)
        blank = False
    return "\n".join(compact).strip() + ("\n" if compact else "")


def short_excerpt(text: str, limit: int = 220) -> str:
    single_line = re.sub(r"\s+", " ", text).strip()
    if not single_line:
        return ""
    sentence = re.split(r"(?<=[.!?])\s+", single_line, maxsplit=1)[0]
    excerpt = sentence if len(sentence) <= limit else single_line[:limit]
    return excerpt.rstrip()

