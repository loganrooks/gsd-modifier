#!/usr/bin/env python3
"""Detect-only inventory for legacy or drifted seed corpora."""

from __future__ import annotations

import argparse
import copy
import json
import pathlib
import re
import sys
from datetime import datetime, timezone

from harness_modifier.compatibility import seed_contract as compatibility_seed_contract

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
SEED_CONTRACT = compatibility_seed_contract.load_seed_contract()
CURRENT_SEED_CONTRACT_VERSION = str(SEED_CONTRACT["current_seed_contract_version"])
REQUIRED_SEED_FRONTMATTER_KEYS = tuple(SEED_CONTRACT["required_seed_frontmatter_keys"])
REQUIRED_SEED_SECTION_HEADINGS = tuple(SEED_CONTRACT["required_seed_section_headings"])
SEED_DIR_REL_PATH = str(SEED_CONTRACT["seed_dir_rel_path"])


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


def extract_seed_title(text: str) -> str:
    match = re.search(r"^#\s*(?:SEED-[^:]+:\s*)?(.+)$", text, re.M)
    return match.group(1).strip() if match else ""


def summarize_gap_list(items: list[str]) -> str:
    return ", ".join(items) if items else "none"


def build_seed_entry(repo_root: pathlib.Path, path: pathlib.Path) -> dict:
    text = pu.read_text(path) or ""
    frontmatter = pu.parse_frontmatter_map(pu.frontmatter_text(text))
    sections = pu.extract_h2_headings(text)
    version = pu.parse_seed_contract_version(pu.frontmatter_text(text))

    if version is None:
        vintage = "legacy_unversioned"
    elif version == CURRENT_SEED_CONTRACT_VERSION:
        vintage = "current_contract"
    else:
        vintage = f"noncurrent:{version}"

    missing_frontmatter = [
        key for key in REQUIRED_SEED_FRONTMATTER_KEYS if key not in frontmatter
    ]
    missing_sections = [
        heading for heading in REQUIRED_SEED_SECTION_HEADINGS if heading not in sections
    ]
    migration_moves: list[str] = []
    migration_move_kinds: list[str] = []

    if version is None:
        migration_moves.append(
            f"stamp `seed_contract_version: {CURRENT_SEED_CONTRACT_VERSION}`"
        )
        migration_move_kinds.append("stamp_seed_contract_version")
    elif version != CURRENT_SEED_CONTRACT_VERSION:
        migration_moves.append(
            f"move `seed_contract_version` from `{version}` to `{CURRENT_SEED_CONTRACT_VERSION}`"
        )
        migration_move_kinds.append("move_seed_contract_version")

    nonversion_frontmatter_gaps = [
        key for key in missing_frontmatter if key != "seed_contract_version"
    ]
    if nonversion_frontmatter_gaps:
        migration_moves.append(
            "add frontmatter keys: " + ", ".join(f"`{key}`" for key in nonversion_frontmatter_gaps)
        )
        migration_move_kinds.append("add_frontmatter_keys")
    if missing_sections:
        migration_moves.append(
            "add sections: " + ", ".join(f"`{heading}`" for heading in missing_sections)
        )
        migration_move_kinds.append("add_sections")

    return {
        "seed_id": frontmatter.get("id") or path.stem.split("-", 2)[0] + "-" + path.stem.split("-", 2)[1],
        "title": extract_seed_title(text) or path.stem,
        "rel_path": pu.rel_path(repo_root, path),
        "contract_vintage": vintage,
        "current_contract_version": CURRENT_SEED_CONTRACT_VERSION,
        "missing_frontmatter_keys": missing_frontmatter,
        "missing_section_headings": missing_sections,
        "migration_moves": migration_moves,
        "migration_move_kinds": migration_move_kinds,
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
    seed_root = repo_root / SEED_DIR_REL_PATH
    seed_paths = sorted(seed_root.glob("SEED-*.md")) if seed_root.exists() else []
    entries = [build_seed_entry(repo_root, path) for path in seed_paths]
    seed_corpus_posture = pu.build_seed_corpus_posture(repo_root)
    migration_candidates = [
        entry for entry in entries if entry["route_state"] == "migration_candidate"
    ]
    reasons = migration_reasons(seed_corpus_posture, entries)
    if seed_corpus_posture["seed_file_count"] == 0:
        route_state = "no_corpus"
    elif migration_candidates:
        route_state = "surfaced"
    else:
        route_state = "current_only"

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
            if route_state == "surfaced"
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
        if entry["migration_move_kinds"]:
            lines.append(
                "- Migration move kinds: " + ", ".join(entry["migration_move_kinds"])
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def post_write_analysis(analysis: dict, written_outputs: dict) -> dict:
    written_analysis = copy.deepcopy(analysis)
    written_analysis["written_outputs"] = written_outputs
    written_analysis["recommend_write"] = False
    written_analysis["recommendation"] = (
        "The specialist seed-migration packet now carries the durable inventory. "
        "Rerun when seed posture moves."
    )
    return written_analysis


def write_outputs(repo_root: pathlib.Path, analysis: dict) -> dict:
    report_path = repo_root / REPORT_REL_PATH
    manifest_path = repo_root / MANIFEST_REL_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    written_outputs = {
        "report_path": REPORT_REL_PATH,
        "manifest_path": MANIFEST_REL_PATH,
    }
    written_analysis = post_write_analysis(analysis, written_outputs)
    report_path.write_text(render_report(written_analysis), encoding="utf-8")
    manifest_path.write_text(
        json.dumps(written_analysis, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return written_analysis


def main() -> int:
    args = parse_args()
    if args.command != "detect":
        raise AssertionError(f"unsupported command: {args.command}")
    repo_root = pathlib.Path(args.repo_root)
    analysis = analyze_repo(repo_root)
    if args.write:
        analysis = write_outputs(repo_root, analysis)
    if args.json:
        json.dump(analysis, sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_report(analysis))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
