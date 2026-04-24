#!/usr/bin/env python3
"""Build compact snippet packets for model-based source synthesis."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from typing import Any

if __package__ in {None, ""}:
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from tooling.codex.model_opinion_mining import common


DEFAULT_KEYWORDS = (
    "usage",
    "limit",
    "quota",
    "pricing",
    "credit",
    "fast mode",
    "context",
    "window",
    "gpt-5.5",
    "gpt 5.5",
    "gpt-5.4",
    "gpt 5.4",
    "codex",
    "model",
    "access",
    "error",
    "rollout",
    "frontend",
    "review",
    "planning",
    "benchmark",
    "latency",
    "token",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build capped evidence packets from source inventories.")
    parser.add_argument("--inventory", required=True, help="Source inventory JSONL.")
    parser.add_argument("--metadata", required=True, help="Fetch/extract metadata JSON.")
    parser.add_argument("--output", required=True, help="Output packet JSONL.")
    parser.add_argument("--max-snippets", type=int, default=5, help="Maximum snippets per source.")
    parser.add_argument("--snippet-chars", type=int, default=300, help="Maximum characters per snippet.")
    return parser.parse_args()


def load_text(metadata: dict[str, Any]) -> str:
    text_path = metadata.get("text_path")
    if not isinstance(text_path, str) or text_path == "not_available":
        return ""
    path = pathlib.Path(text_path)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def sentence_windows(text: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    parts = re.split(r"(?<=[.!?])\s+", normalized)
    return [part.strip() for part in parts if part.strip()]


def snippet_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def keyword_snippets(
    text: str,
    keywords: tuple[str, ...] = DEFAULT_KEYWORDS,
    *,
    max_snippets: int = 5,
    snippet_chars: int = 300,
) -> list[dict[str, Any]]:
    snippets: list[dict[str, Any]] = []
    seen_hashes: set[str] = set()
    lower_keywords = tuple(keyword.lower() for keyword in keywords)
    for sentence in sentence_windows(text):
        lower_sentence = sentence.lower()
        matched = [keyword for keyword in lower_keywords if keyword in lower_sentence]
        if not matched:
            continue
        snippet = sentence[:snippet_chars].rstrip()
        digest = snippet_hash(snippet)
        if digest in seen_hashes:
            continue
        seen_hashes.add(digest)
        snippets.append(
            {
                "snippet_hash": digest,
                "matched_keywords": matched[:6],
                "text": snippet,
            }
        )
        if len(snippets) >= max_snippets:
            break
    return snippets


def fallback_snippet(text: str, snippet_chars: int) -> list[dict[str, Any]]:
    excerpt = common.short_excerpt(text, limit=snippet_chars)
    if not excerpt:
        return []
    return [{"snippet_hash": snippet_hash(excerpt), "matched_keywords": [], "text": excerpt}]


def packet_row(
    inventory: dict[str, Any],
    metadata: dict[str, Any],
    *,
    max_snippets: int,
    snippet_chars: int,
) -> dict[str, Any]:
    text = load_text(metadata)
    snippets = keyword_snippets(text, max_snippets=max_snippets, snippet_chars=snippet_chars)
    if not snippets:
        snippets = fallback_snippet(text, snippet_chars)
    return {
        "source_id": inventory["source_id"],
        "platform": inventory["platform"],
        "url": inventory["url"],
        "claim_tags": inventory["claim_tags"],
        "source_type": inventory.get("source_type", "not_available"),
        "collection_caveat": inventory["collection_caveat"],
        "fetch_status": inventory["fetch_status"],
        "extract_status": inventory["extract_status"],
        "text_char_count": inventory.get("text_char_count", 0),
        "summary": inventory["summary"],
        "snippet_count": len(snippets),
        "snippets": snippets,
    }


def build_packets(
    inventory_path: pathlib.Path,
    metadata_path: pathlib.Path,
    output_path: pathlib.Path,
    *,
    max_snippets: int = 5,
    snippet_chars: int = 300,
) -> list[dict[str, Any]]:
    inventory_rows = common.read_jsonl(inventory_path)
    metadata_rows = common.read_json(metadata_path)
    if not isinstance(metadata_rows, list):
        raise ValueError("metadata file must contain a list")
    metadata_by_id = {row.get("source_id"): row for row in metadata_rows if isinstance(row, dict)}
    packets = [
        packet_row(
            inventory,
            metadata_by_id.get(inventory["source_id"], {}),
            max_snippets=max_snippets,
            snippet_chars=snippet_chars,
        )
        for inventory in inventory_rows
    ]
    common.write_jsonl(output_path, packets)
    return packets


def main() -> None:
    args = parse_args()
    build_packets(
        pathlib.Path(args.inventory),
        pathlib.Path(args.metadata),
        pathlib.Path(args.output),
        max_snippets=args.max_snippets,
        snippet_chars=args.snippet_chars,
    )


if __name__ == "__main__":
    main()
