#!/usr/bin/env python3
"""Verify source-candidate reachability and quality before synthesis."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time
from typing import Any
from urllib.parse import parse_qs, urlparse, urlunparse

import requests

if __package__ in {None, ""}:
    repo_root = pathlib.Path(__file__).resolve().parents[3]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

from tooling.codex.model_opinion_mining import common


USER_AGENT = "gsd-modifier-source-verifier/1.0"
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", flags=re.IGNORECASE | re.DOTALL)
GITHUB_ISSUE_RE = re.compile(r"^/([^/]+)/([^/]+)/issues/([0-9]+)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify source candidates before adding them to the synthesis corpus.")
    parser.add_argument("--seeds", required=True, help="JSONL or JSON candidate source file.")
    parser.add_argument("--output", required=True, help="Output JSONL verification report.")
    parser.add_argument("--timeout", type=float, default=12.0, help="Request timeout in seconds.")
    parser.add_argument("--sleep", type=float, default=0.0, help="Seconds to sleep between requests.")
    return parser.parse_args()


def reddit_probe_url(url: str) -> str:
    parsed = urlparse(url)
    if "reddit.com" not in parsed.netloc or "/comments/" not in parsed.path:
        return url
    if parsed.path.endswith(".json"):
        return url
    return urlunparse(parsed._replace(path=parsed.path.rstrip("/") + "/.json"))


def hacker_news_probe_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc != "news.ycombinator.com":
        return url
    item_ids = parse_qs(parsed.query).get("id", [])
    if not item_ids:
        return url
    return f"https://hacker-news.firebaseio.com/v0/item/{item_ids[0]}.json"


def github_probe_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc != "github.com":
        return url
    match = GITHUB_ISSUE_RE.match(parsed.path)
    if not match:
        return url
    owner, repo, issue_number = match.groups()
    return f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"


def probe_url(seed: dict[str, Any]) -> str:
    explicit_probe_url = seed.get("probe_url")
    if isinstance(explicit_probe_url, str) and explicit_probe_url.strip():
        return explicit_probe_url
    url = str(seed["url"])
    for transform in (reddit_probe_url, hacker_news_probe_url, github_probe_url):
        transformed = transform(url)
        if transformed != url:
            return transformed
    return url


def extract_html_title(text: str) -> str:
    match = TITLE_RE.search(text[:100_000])
    if not match:
        return ""
    return common.normalize_text(match.group(1)).replace("\n", " ").strip()[:220]


def extract_json_title(payload: Any, platform: str) -> str:
    if platform == "reddit":
        return extract_reddit_title(payload)
    if platform == "Hacker News" and isinstance(payload, dict):
        return str(payload.get("title", "")).strip()[:220]
    if isinstance(payload, dict):
        title = payload.get("title") or payload.get("name")
        if isinstance(title, str):
            return title.strip()[:220]
    return ""


def extract_reddit_title(payload: Any) -> str:
    if not isinstance(payload, list) or not payload:
        return ""
    try:
        children = payload[0]["data"]["children"]
        if not children:
            return ""
        title = children[0]["data"].get("title", "")
    except (KeyError, TypeError, IndexError):
        return ""
    return str(title).strip()[:220]


def classify_source_kind(seed: dict[str, Any], title: str) -> str:
    platform = str(seed["platform"])
    url = str(seed["url"])
    parsed = urlparse(url)
    if "reddit.com" in parsed.netloc and "/comments/" in parsed.path:
        return "discussion_thread"
    if parsed.netloc == "community.openai.com":
        if "/tag/" in parsed.path:
            return "discovery_hub"
        return "discussion_thread"
    if platform == "official" or parsed.netloc in {"openai.com", "platform.openai.com"}:
        return "official"
    if parsed.netloc == "news.ycombinator.com":
        return "discussion_thread"
    if parsed.netloc == "github.com" and "/issues/" in parsed.path:
        return "issue"
    if "techmeme.com" in parsed.netloc:
        return "aggregator"
    if platform in {"X/Twitter", "Bluesky"}:
        return "social_permalink"
    if title:
        return "article"
    return "unknown"


def classify_directness(source_kind: str) -> str:
    return {
        "official": "official",
        "discussion_thread": "user_discussion",
        "issue": "user_report",
        "aggregator": "discovery_context",
        "social_permalink": "unverified_social",
        "article": "secondary_analysis",
        "discovery_hub": "discovery_only",
    }.get(source_kind, "unknown")


def source_mentions_topic(seed: dict[str, Any], title: str) -> bool:
    haystack = " ".join(
        [
            title,
            str(seed.get("query", "")),
            " ".join(seed.get("claim_tags", [])),
            str(seed.get("collection_caveat", "")),
        ]
    ).lower()
    return any(term in haystack for term in ("gpt-5.5", "gpt55", "gpt-5.4", "gpt54", "codex", "openai"))


def disposition(seed: dict[str, Any], http_status: int | str, title: str, source_kind: str) -> tuple[str, str]:
    caveat = str(seed.get("collection_caveat", "")).lower()
    platform = str(seed["platform"])
    if source_kind == "social_permalink" and "inferred" in caveat:
        return "reject", "inferred_social_permalink"
    if source_kind == "discovery_hub":
        return "reject", "discovery_hub_not_claim_source"
    if isinstance(http_status, int) and http_status >= 400:
        if source_kind == "official":
            return "hold", f"official_fetch_blocked_{http_status}"
        return "reject", f"http_status_{http_status}"
    if http_status == "request_failed":
        return "reject", "request_failed"
    if source_kind == "aggregator" and not source_mentions_topic(seed, title):
        return "reject", "aggregator_title_off_topic"
    if source_kind == "aggregator":
        return "hold", "aggregator_discovery_context"
    if platform in {"official", "OpenAI Community", "Hacker News", "reddit", "github-issue"}:
        return "accept", "reachable_relevant_source"
    if source_mentions_topic(seed, title):
        return "hold", "reachable_secondary_or_uncertain_source"
    return "reject", "topic_not_confirmed"


def verify_one(seed: dict[str, Any], timeout: float) -> dict[str, Any]:
    url = probe_url(seed)
    row: dict[str, Any] = {
        "source_id": seed["source_id"],
        "platform": seed["platform"],
        "url": seed["url"],
        "probe_url": url,
        "query": seed["query"],
        "claim_tags": seed["claim_tags"],
        "collection_caveat": seed["collection_caveat"],
        "http_status": "request_failed",
        "final_url": "not_available",
        "content_type": "not_available",
        "title": "",
        "source_kind": "unknown",
        "directness": "unknown",
        "verification_status": "reject",
        "rejection_reason": "request_failed",
    }
    try:
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout, allow_redirects=True)
        row["http_status"] = response.status_code
        row["final_url"] = response.url
        row["content_type"] = response.headers.get("Content-Type", "not_available")
        title = ""
        if "json" in row["content_type"].lower():
            try:
                title = extract_json_title(response.json(), str(seed["platform"]))
            except json.JSONDecodeError:
                title = ""
        if not title:
            title = extract_html_title(response.text)
        source_kind = classify_source_kind(seed, title)
        verification_status, rejection_reason = disposition(seed, response.status_code, title, source_kind)
        row.update(
            {
                "title": title,
                "source_kind": source_kind,
                "directness": classify_directness(source_kind),
                "verification_status": verification_status,
                "rejection_reason": rejection_reason,
            }
        )
    except requests.RequestException as exc:
        row["rejection_reason"] = exc.__class__.__name__
    return row


def verify_sources(seeds_path: pathlib.Path, output_path: pathlib.Path, timeout: float, sleep_seconds: float = 0.0) -> list[dict[str, Any]]:
    seeds = common.read_seed_rows(seeds_path)
    rows: list[dict[str, Any]] = []
    for index, seed in enumerate(seeds):
        if index and sleep_seconds:
            time.sleep(sleep_seconds)
        rows.append(verify_one(seed, timeout))
    common.write_jsonl(output_path, rows)
    return rows


def main() -> None:
    args = parse_args()
    verify_sources(
        pathlib.Path(args.seeds),
        pathlib.Path(args.output),
        args.timeout,
        args.sleep,
    )


if __name__ == "__main__":
    main()
