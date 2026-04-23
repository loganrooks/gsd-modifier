#!/usr/bin/env python3
"""Build compact opinion-mining inventory rows from extracted text."""

from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Any

if __package__ in {None, ""}:
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from tooling.codex.model_opinion_mining import common


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build compact source inventory JSONL.")
    parser.add_argument("--seeds", required=True, help="JSONL or JSON seed source file.")
    parser.add_argument("--text-dir", required=True, help="Directory containing extracted text files.")
    parser.add_argument("--metadata", required=True, help="Fetch/extract metadata JSON file.")
    parser.add_argument("--output", required=True, help="Output inventory JSONL path.")
    return parser.parse_args()


def inventory_row(seed: dict[str, Any], metadata: dict[str, Any], text_dir: pathlib.Path) -> dict[str, Any]:
    source_id = seed["source_id"]
    text = ""
    text_path_value = metadata.get("text_path")
    if isinstance(text_path_value, str) and text_path_value != "not_available":
        text_path = pathlib.Path(text_path_value)
        if text_path.exists():
            text = text_path.read_text(encoding="utf-8", errors="replace")
    if not text:
        fallback_path = text_dir / f"{common.safe_slug(source_id)}.txt"
        if fallback_path.exists():
            text = fallback_path.read_text(encoding="utf-8", errors="replace")

    excerpt = common.short_excerpt(text)
    summary = excerpt if excerpt else "No extracted text available."
    return {
        "source_id": source_id,
        "platform": seed["platform"],
        "url": seed["url"],
        "query": seed["query"],
        "collected_at": metadata.get("fetched_at", "not_available"),
        "posted_at": seed.get("posted_at", "not_available"),
        "author_public_id": seed.get("author_public_id", "not_collected"),
        "engagement": seed.get(
            "engagement",
            {"score": "not_available", "comments": "not_available"},
        ),
        "claim_tags": seed["claim_tags"],
        "summary": summary,
        "excerpt": excerpt,
        "source_type": seed.get("source_type", "anecdote"),
        "collection_caveat": seed["collection_caveat"],
        "fetch_status": metadata.get("fetch_status", "not_available"),
        "extract_status": metadata.get("extract_status", "not_available"),
        "text_char_count": metadata.get("text_char_count", 0),
    }


def build_inventory(
    seeds_path: pathlib.Path,
    text_dir: pathlib.Path,
    metadata_path: pathlib.Path,
    output_path: pathlib.Path,
) -> list[dict[str, Any]]:
    seeds = common.read_seed_rows(seeds_path)
    metadata_rows = common.read_json(metadata_path)
    if not isinstance(metadata_rows, list):
        raise ValueError("metadata file must contain a list of records")
    metadata_by_id = {str(row.get("source_id")): row for row in metadata_rows if isinstance(row, dict)}
    rows = [inventory_row(seed, metadata_by_id.get(seed["source_id"], {}), text_dir) for seed in seeds]
    common.write_jsonl(output_path, rows)
    return rows


def main() -> None:
    args = parse_args()
    build_inventory(
        pathlib.Path(args.seeds),
        pathlib.Path(args.text_dir),
        pathlib.Path(args.metadata),
        pathlib.Path(args.output),
    )


if __name__ == "__main__":
    main()
