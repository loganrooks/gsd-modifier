#!/usr/bin/env python3
"""Fetch seeded opinion-mining pages and record safe fetch metadata."""

from __future__ import annotations

import argparse
import pathlib
import sys
from typing import Any
from urllib.parse import urlparse, urlunparse

import requests

if __package__ in {None, ""}:
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from tooling.codex.model_opinion_mining import common


USER_AGENT = "gsd-modifier-model-opinion-mining/1.0"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch seeded public pages for opinion mining.")
    parser.add_argument("--seeds", required=True, help="JSONL or JSON seed source file.")
    parser.add_argument("--raw-dir", required=True, help="Directory for raw fetched bodies.")
    parser.add_argument("--metadata", required=True, help="Output fetch metadata JSON file.")
    parser.add_argument("--timeout", type=float, default=20.0, help="Request timeout in seconds.")
    return parser.parse_args()


def fetch_url_for_seed(seed: dict[str, Any]) -> str:
    explicit_fetch_url = seed.get("fetch_url")
    if isinstance(explicit_fetch_url, str) and explicit_fetch_url.strip():
        return explicit_fetch_url
    url = str(seed["url"])
    if seed.get("platform") != "reddit" or urlparse(url).path.endswith(".json"):
        return url
    parsed = urlparse(url)
    path = parsed.path.rstrip("/") + "/.json"
    return urlunparse(parsed._replace(path=path))


def raw_extension(response: requests.Response) -> str:
    content_type = response.headers.get("Content-Type", "").lower()
    if "json" in content_type:
        return ".json"
    return ".html"


def fetch_one(seed: dict[str, Any], raw_dir: pathlib.Path, timeout: float) -> dict[str, Any]:
    source_id = common.safe_slug(seed["source_id"])
    fetched_at = common.utc_now_iso()
    fetch_url = fetch_url_for_seed(seed)
    record: dict[str, Any] = {
        "source_id": seed["source_id"],
        "platform": seed["platform"],
        "url": seed["url"],
        "fetch_url": fetch_url,
        "query": seed["query"],
        "claim_tags": seed["claim_tags"],
        "collection_caveat": seed["collection_caveat"],
        "fetched_at": fetched_at,
        "fetch_status": "failed",
        "http_status": "not_available",
        "raw_path": "not_available",
        "safe_headers": {},
        "error": "not_available",
    }
    try:
        response = requests.get(
            fetch_url,
            headers={"User-Agent": USER_AGENT},
            timeout=timeout,
        )
        record["http_status"] = response.status_code
        record["safe_headers"] = common.safe_headers(dict(response.headers))
        if response.status_code >= 400:
            record["error"] = f"http_status_{response.status_code}"
            return record
        raw_dir.mkdir(parents=True, exist_ok=True)
        raw_path = raw_dir / f"{source_id}{raw_extension(response)}"
        raw_path.write_text(response.text, encoding=response.encoding or "utf-8", errors="replace")
        record["fetch_status"] = "fetched"
        record["raw_path"] = str(raw_path)
        return record
    except requests.RequestException as exc:
        record["error"] = exc.__class__.__name__
        return record


def fetch_pages(seeds_path: pathlib.Path, raw_dir: pathlib.Path, metadata_path: pathlib.Path, timeout: float) -> list[dict[str, Any]]:
    seeds = common.read_seed_rows(seeds_path)
    rows = [fetch_one(seed, raw_dir, timeout) for seed in seeds]
    common.write_json(metadata_path, rows)
    return rows


def main() -> None:
    args = parse_args()
    fetch_pages(
        pathlib.Path(args.seeds),
        pathlib.Path(args.raw_dir),
        pathlib.Path(args.metadata),
        args.timeout,
    )


if __name__ == "__main__":
    main()
