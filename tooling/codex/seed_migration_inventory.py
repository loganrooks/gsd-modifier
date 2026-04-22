#!/usr/bin/env python3
"""Detect-only inventory for legacy or drifted seed corpora."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

try:
    from tooling.codex import project_uplift as pu
except ModuleNotFoundError:
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    from tooling.codex import project_uplift as pu


REPORT_REL_PATH = ".planning/SEED-MIGRATION-REPORT.md"
MANIFEST_REL_PATH = ".planning/SEED-MIGRATION-MANIFEST.json"
SEED_MIGRATION_MANIFEST_SCHEMA_VERSION = 1
REQUIRED_FRONTMATTER_KEYS = (
    "id",
    "seed_contract_version",
    "status",
    "planted",
    "planted_during",
    "trigger_when",
    "scope",
)
REQUIRED_SECTION_HEADINGS = (
    "Why This Matters",
    "When to Surface",
    "Scope Estimate",
    "Strengthening Carry",
    "Breadcrumbs",
    "Notes",
)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inventory seed-corpus migration posture.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    detect = subparsers.add_parser("detect", help="Analyze current seed-corpus migration posture.")
    detect.add_argument("repo_root", nargs="?", default=".")
    detect.add_argument("--write", action="store_true", help="Write report and manifest outputs.")
    detect.add_argument("--json", action="store_true", help="Emit JSON to stdout.")
    return parser.parse_args()


def parse_frontmatter_map(text: str | None) -> dict[str, str]:
    if not text:
        return {}
    rows: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line.strip())
        if not match:
            continue
        rows[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return rows


def extract_h2_headings(text: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"^##\s+(.+?)\s*$", text, re.M)]


def extract_seed_title(text: str) -> str:
    match = re.search(r"^#\s*(?:SEED-[^:]+:\s*)?(.+)$", text, re.M)
    return match.group(1).strip() if match else ""


def summarize_gap_list(items: list[str]) -> str:
    return ", ".join(items) if items else "none"


def build_seed_entry(repo_root: pathlib.Path, path: pathlib.Path) -> dict:
    text = pu.read_text(path) or ""
    frontmatter = parse_frontmatter_map(pu.frontmatter_text(text))
    sections = extract_h2_headings(text)
    version = pu.parse_seed_contract_version(pu.frontmatter_text(text))

    if version is None:
        vintage = "legacy_unversioned"
    elif version == pu.CURRENT_SEED_CONTRACT_VERSION:
        vintage = "current_contract"
    else:
        vintage = f"noncurrent:{version}"

    missing_frontmatter = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in frontmatter]
    missing_sections = [heading for heading in REQUIRED_SECTION_HEADINGS if heading not in sections]
    migration_moves: list[str] = []

    if version is None:
        migration_moves.append(
            f"stamp `seed_contract_version: {pu.CURRENT_SEED_CONTRACT_VERSION}`"
        )
    elif version != pu.CURRENT_SEED_CONTRACT_VERSION:
        migration_moves.append(
            f"move `seed_contract_version` from `{version}` to `{pu.CURRENT_SEED_CONTRACT_VERSION}`"
        )

    nonversion_frontmatter_gaps = [
        key for key in missing_frontmatter if key != "seed_contract_version"
    ]
    if nonversion_frontmatter_gaps:
        migration_moves.append(
            "add frontmatter keys: " + ", ".join(f"`{key}`" for key in nonversion_frontmatter_gaps)
        )
    if missing_sections:
        migration_moves.append(
            "add sections: " + ", ".join(f"`{heading}`" for heading in missing_sections)
        )

    return {
        "seed_id": frontmatter.get("id") or path.stem.split("-", 2)[0] + "-" + path.stem.split("-", 2)[1],
        "title": extract_seed_title(text) or path.stem,
        "rel_path": pu.rel_path(repo_root, path),
        "contract_vintage": vintage,
        "current_contract_version": pu.CURRENT_SEED_CONTRACT_VERSION,
        "missing_frontmatter_keys": missing_frontmatter,
        "missing_section_headings": missing_sections,
        "migration_moves": migration_moves,
        "route_state": "migration_candidate" if migration_moves else "current_contract_visible",
    }


def migration_reasons(seed_corpus_posture: dict, entries: list[dict]) -> list[str]:
    reasons = pu.seed_corpus_reasons(seed_corpus_posture)
    shape_gap_count = sum(
        1 for entry in entries if entry["missing_frontmatter_keys"] or entry["missing_section_headings"]
    )
    if shape_gap_count > 0:
        reasons.append(f"seed contract-shape gaps still visible: {shape_gap_count}")
    return reasons


def analyze_repo(repo_root: pathlib.Path) -> dict:
    repo_root = repo_root.resolve()
    seed_root = repo_root / pu.SEED_DIR_REL_PATH
    seed_paths = sorted(seed_root.glob("SEED-*.md")) if seed_root.exists() else []
    entries = [build_seed_entry(repo_root, path) for path in seed_paths]
    seed_corpus_posture = pu.build_seed_corpus_posture(repo_root)
    migration_candidates = [
        entry for entry in entries if entry["route_state"] == "migration_candidate"
    ]
    reasons = migration_reasons(seed_corpus_posture, entries)
    route_state = "surfaced" if migration_candidates else "dormant"

    return {
        "schema_version": SEED_MIGRATION_MANIFEST_SCHEMA_VERSION,
        "generated_at": now_iso(),
        "mode": "detect-only",
        "repo_root": str(repo_root),
        "seed_corpus_posture": seed_corpus_posture,
        "route_state": route_state,
        "recommend_write": bool(migration_candidates),
        "recommendation": (
            "Write the seed-migration inventory when you want durable migration planning memory."
            if migration_candidates
            else "Continue with current seed routing."
        ),
        "reasons": reasons,
        "seed_count": len(entries),
        "migration_candidate_count": len(migration_candidates),
        "entries": entries,
        "inventory_fingerprint": pu.sha256_text(
            "\n".join(
                f"{entry['rel_path']}:{entry['contract_vintage']}:{','.join(entry['missing_frontmatter_keys'])}:{','.join(entry['missing_section_headings'])}"
                for entry in entries
            )
        )
        if entries
        else None,
    }


def render_report(analysis: dict) -> str:
    seed_posture = analysis["seed_corpus_posture"]
    lines = [
        "# Seed Migration Report",
        "",
        f"- Generated: {analysis['generated_at']}",
        f"- Mode: {analysis['mode']}",
        f"- Route state: {analysis['route_state']}",
        f"- Corpus posture: {pu.seed_corpus_summary(seed_posture)}",
        f"- Migration candidate count: {analysis['migration_candidate_count']}",
        f"- Recommendation: {analysis['recommendation']}",
        "",
        "## Reasons",
        "",
    ]

    if analysis["reasons"]:
        lines.extend(f"- {reason}" for reason in analysis["reasons"])
    else:
        lines.append("- The visible seed corpus already stays on the current contract route.")

    lines.extend(
        [
            "",
            "## Seed Inventory",
            "",
        ]
    )

    if not analysis["entries"]:
        lines.append("- No `SEED-*.md` files are present.")
        return "\n".join(lines) + "\n"

    for entry in analysis["entries"]:
        lines.extend(
            [
                f"### {entry['seed_id']}: {entry['title']}",
                "",
                f"- Path: {entry['rel_path']}",
                f"- Contract vintage: {entry['contract_vintage']}",
                f"- Missing frontmatter keys: {summarize_gap_list(entry['missing_frontmatter_keys'])}",
                f"- Missing sections: {summarize_gap_list(entry['missing_section_headings'])}",
                f"- Route state: {entry['route_state']}",
            ]
        )
        if entry["migration_moves"]:
            lines.append("- Migration moves:")
            lines.extend(f"  - {move}" for move in entry["migration_moves"])
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_outputs(repo_root: pathlib.Path, analysis: dict) -> dict:
    report_path = repo_root / REPORT_REL_PATH
    manifest_path = repo_root / MANIFEST_REL_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_report(analysis), encoding="utf-8")
    manifest_path.write_text(json.dumps(analysis, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "report_path": REPORT_REL_PATH,
        "manifest_path": MANIFEST_REL_PATH,
    }


def main() -> int:
    args = parse_args()
    if args.command != "detect":
        raise AssertionError(f"unsupported command: {args.command}")
    repo_root = pathlib.Path(args.repo_root)
    analysis = analyze_repo(repo_root)
    if args.write:
        analysis["written_outputs"] = write_outputs(repo_root, analysis)
    if args.json:
        json.dump(analysis, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_report(analysis))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
