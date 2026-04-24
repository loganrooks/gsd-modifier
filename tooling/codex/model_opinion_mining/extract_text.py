#!/usr/bin/env python3
"""Extract normalized text from fetched opinion-mining HTML."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
from html.parser import HTMLParser
from typing import Any

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:  # pragma: no cover - exercised only in lean runtimes
    BeautifulSoup = None

if __package__ in {None, ""}:
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from tooling.codex.model_opinion_mining import common


DROP_TAGS = ("script", "style", "noscript", "svg", "template")
REDDIT_TEXT_KEYS = {"title", "selftext", "body"}


class TextOnlyHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        _ = attrs
        if tag in DROP_TAGS:
            self.skip_stack.append(tag)
            return
        if tag in {"p", "li", "br", "div", "article", "section", "blockquote"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.skip_stack and self.skip_stack[-1] == tag:
            self.skip_stack.pop()
            return
        if tag in {"p", "li", "div", "article", "section", "blockquote"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_stack:
            self.parts.append(data)

    def text(self) -> str:
        return "".join(self.parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract normalized text from fetched HTML.")
    parser.add_argument("--raw-dir", required=True, help="Directory containing raw fetched HTML.")
    parser.add_argument("--text-dir", required=True, help="Directory for extracted text files.")
    parser.add_argument("--metadata", required=True, help="Fetch metadata JSON file to augment.")
    return parser.parse_args()


def html_to_text(html: str) -> str:
    if BeautifulSoup is None:
        parser = TextOnlyHTMLParser()
        parser.feed(html)
        return common.normalize_text(parser.text())
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(DROP_TAGS):
        tag.decompose()
    for separator_tag in soup.find_all(["p", "li", "br", "div", "article", "section", "blockquote"]):
        separator_tag.append("\n")
    text = soup.get_text("\n")
    return common.normalize_text(text)


def json_to_text(raw_json: str, platform: str) -> str:
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError:
        return ""
    if platform == "reddit":
        return reddit_json_to_text(payload)
    if platform == "Hacker News":
        return keyed_json_to_text(payload, ("title", "text", "url"))
    if platform in {"github-issue", "github_issue"}:
        return keyed_json_to_text(payload, ("title", "body", "state", "created_at", "updated_at"))
    return generic_json_to_text(payload)


def reddit_json_to_text(payload: Any) -> str:
    parts: list[str] = []
    seen: set[str] = set()

    def add(value: Any) -> None:
        if not isinstance(value, str):
            return
        clean = common.normalize_text(value)
        if not clean or clean in {"[deleted]", "[removed]"} or clean in seen:
            return
        seen.add(clean)
        parts.append(clean)

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key in REDDIT_TEXT_KEYS:
                add(value.get(key))
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(payload)
    return common.normalize_text("\n\n".join(parts))


def generic_json_to_text(payload: Any) -> str:
    parts: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, str):
            clean = common.normalize_text(value)
            if clean:
                parts.append(clean)
        elif isinstance(value, dict):
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(payload)
    return common.normalize_text("\n\n".join(parts))


def keyed_json_to_text(payload: Any, keys: tuple[str, ...]) -> str:
    if not isinstance(payload, dict):
        return generic_json_to_text(payload)
    parts = []
    for key in keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            parts.append(f"{key}: {value}")
    return common.normalize_text("\n\n".join(parts))


def record_is_json(record: dict[str, Any], raw_path: pathlib.Path) -> bool:
    headers = record.get("safe_headers")
    content_type = ""
    if isinstance(headers, dict):
        content_type = str(headers.get("content-type", "")).lower()
    return raw_path.suffix == ".json" or "json" in content_type


def extract_one(record: dict[str, Any], text_dir: pathlib.Path) -> dict[str, Any]:
    augmented = dict(record)
    augmented.setdefault("extract_status", "not_run")
    augmented.setdefault("text_path", "not_available")
    if record.get("fetch_status") != "fetched" or record.get("raw_path") == "not_available":
        augmented["extract_status"] = "skipped_fetch_failed"
        return augmented
    raw_path = pathlib.Path(str(record["raw_path"]))
    if not raw_path.exists():
        augmented["extract_status"] = "raw_missing"
        return augmented
    raw_text = raw_path.read_text(encoding="utf-8", errors="replace")
    if record_is_json(record, raw_path):
        text = json_to_text(raw_text, str(record.get("platform", "")))
    else:
        text = html_to_text(raw_text)
    source_id = common.safe_slug(str(record["source_id"]))
    text_dir.mkdir(parents=True, exist_ok=True)
    text_path = text_dir / f"{source_id}.txt"
    text_path.write_text(text, encoding="utf-8")
    augmented["extract_status"] = "extracted" if text.strip() else "empty"
    augmented["text_path"] = str(text_path)
    augmented["text_char_count"] = len(text)
    return augmented


def extract_text(raw_dir: pathlib.Path, text_dir: pathlib.Path, metadata_path: pathlib.Path) -> list[dict[str, Any]]:
    _ = raw_dir
    rows = common.read_json(metadata_path)
    if not isinstance(rows, list):
        raise ValueError("metadata file must contain a list of fetch records")
    augmented = [extract_one(row, text_dir) for row in rows]
    common.write_json(metadata_path, augmented)
    return augmented


def main() -> None:
    args = parse_args()
    extract_text(
        pathlib.Path(args.raw_dir),
        pathlib.Path(args.text_dir),
        pathlib.Path(args.metadata),
    )


if __name__ == "__main__":
    main()
