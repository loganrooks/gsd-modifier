#!/usr/bin/env python3
"""Detect and record repo-local project uplift posture."""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timezone


STATE_HEADING = "## Project Uplift"
REPORT_REL_PATH = ".planning/UPLIFT-REPORT.md"
MANIFEST_REL_PATH = ".planning/UPLIFT-MANIFEST.json"

RUNTIME_DIRS = [
    ".codex",
    ".claude",
    ".gemini",
    ".config/opencode",
    ".opencode",
    ".config/kilo",
    ".kilo",
]

HELD_LATER_FAMILIES = [
    "required-reading installation practice",
    "cross-runtime uplift composition",
    "upstream-template drift machinery",
    "aged-bespoke deep merge",
    "audit-subtree aging carry",
]


@dataclasses.dataclass(frozen=True)
class FileCarrierSpec:
    key: str
    group: str
    rel_path: str
    label: str


@dataclasses.dataclass(frozen=True)
class MarkerCarrierSpec:
    key: str
    group: str
    rel_path: str
    label: str
    marker: str


FILE_CARRIERS = [
    FileCarrierSpec("root_agents", "doctrine_sensitive", "AGENTS.md", "Root AGENTS"),
    FileCarrierSpec("planning_agents", "doctrine_sensitive", ".planning/AGENTS.md", "Planning AGENTS"),
    FileCarrierSpec("root_claude", "doctrine_sensitive", "CLAUDE.md", "Root CLAUDE"),
    FileCarrierSpec("planning_claude", "doctrine_sensitive", ".planning/CLAUDE.md", "Planning CLAUDE"),
    FileCarrierSpec("claim_types", "additive_install", ".planning/CLAIM-TYPES.md", "Claim Types"),
    FileCarrierSpec("long_arc", "additive_install", ".planning/LONG-ARC.md", "Long Arc"),
    FileCarrierSpec("tooling_inventory", "additive_install", "tooling/codex/README.md", "Tooling Inventory"),
    FileCarrierSpec("runtime_config", "runtime_registry", ".codex/config.toml", "Runtime Config"),
    FileCarrierSpec("planner_agent", "runtime_registry", ".codex/agents/gsd-planner.toml", "Planner Agent Contract"),
    FileCarrierSpec("plan_checker_agent", "runtime_registry", ".codex/agents/gsd-plan-checker.toml", "Plan Checker Agent Contract"),
]

MARKER_CARRIERS = [
    MarkerCarrierSpec(
        "strengthening_discuss",
        "doctrine_sensitive",
        ".codex/get-shit-done/workflows/discuss-phase.md",
        "Discuss Strengthening Route",
        "Strengthening Opportunities",
    ),
    MarkerCarrierSpec(
        "strengthening_context",
        "doctrine_sensitive",
        ".codex/get-shit-done/templates/context.md",
        "Context Strengthening Route",
        "Strengthening Opportunities",
    ),
    MarkerCarrierSpec(
        "strengthening_plan",
        "doctrine_sensitive",
        ".codex/get-shit-done/workflows/plan-phase.md",
        "Plan Strengthening Route",
        "Strengthening Opportunities",
    ),
    MarkerCarrierSpec(
        "strengthening_research",
        "doctrine_sensitive",
        ".codex/skills/gsd-rigorous-research/references/output-template.md",
        "Research Strengthening Route",
        "Strengthening Opportunities",
    ),
]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path: pathlib.Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect repo-local project uplift posture.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    detect = subparsers.add_parser("detect", help="Analyze current uplift posture.")
    detect.add_argument("repo_root", nargs="?", default=".")
    detect.add_argument("--write", action="store_true", help="Write report, manifest, and STATE uplift section.")
    detect.add_argument("--json", action="store_true", help="Emit JSON to stdout.")

    progress_note = subparsers.add_parser("progress-note", help="Build a read-only progress recommendation from uplift memory.")
    progress_note.add_argument("repo_root", nargs="?", default=".")
    progress_note.add_argument("--json", action="store_true", help="Emit JSON to stdout.")

    return parser.parse_args()


def state_status(repo_root: pathlib.Path) -> str:
    state_path = repo_root / ".planning" / "STATE.md"
    text = read_text(state_path)
    if not text:
        return "unknown"

    frontmatter_match = re.match(r"^---\n([\s\S]+?)\n---", text)
    if frontmatter_match:
        status_match = re.search(r"^status:\s*(.+)$", frontmatter_match.group(1), re.M)
        if status_match:
            return status_match.group(1).strip().strip('"').strip("'")

    body_match = re.search(r"^Status:\s*(.+)$", text, re.M | re.I)
    if body_match:
        return body_match.group(1).strip()
    return "unknown"


def count_phase_files(repo_root: pathlib.Path, pattern: str) -> int:
    phase_root = repo_root / ".planning" / "phases"
    if not phase_root.exists():
        return 0
    return sum(1 for _ in phase_root.glob(pattern))


def runtime_dirs_present(repo_root: pathlib.Path) -> list[str]:
    present: list[str] = []
    for rel_path in RUNTIME_DIRS:
        if (repo_root / rel_path).exists():
            present.append(rel_path)
    return present


def build_file_carrier(repo_root: pathlib.Path, spec: FileCarrierSpec) -> dict:
    path = repo_root / spec.rel_path
    text = read_text(path)
    present = text is not None
    return {
        "key": spec.key,
        "label": spec.label,
        "group": spec.group,
        "rel_path": spec.rel_path,
        "present": present,
        "status": "present" if present else "absent",
        "fingerprint": sha256_text(text) if text is not None else None,
        "note": "file carrier present" if present else "file carrier absent",
    }


def build_marker_carrier(repo_root: pathlib.Path, spec: MarkerCarrierSpec) -> dict:
    path = repo_root / spec.rel_path
    text = read_text(path)
    file_present = text is not None
    marker_present = bool(text and spec.marker in text)
    if marker_present:
        status = "marker_present"
        note = "marker present on carrier"
    elif file_present:
        status = "marker_absent"
        note = "carrier file present without marker"
    else:
        status = "absent"
        note = "carrier file absent"
    return {
        "key": spec.key,
        "label": spec.label,
        "group": spec.group,
        "rel_path": spec.rel_path,
        "present": marker_present,
        "status": status,
        "fingerprint": sha256_text(text) if marker_present and text is not None else None,
        "note": note,
    }


def doctrine_reference_hash(carriers: list[dict]) -> str:
    selected = [
        f"{carrier['key']}:{carrier['status']}:{carrier['fingerprint'] or '-'}"
        for carrier in carriers
        if carrier["group"] in {"additive_install", "doctrine_sensitive", "runtime_registry"}
    ]
    return sha256_text("\n".join(sorted(selected)))


def project_fingerprint_hash(carriers: list[dict], status: str, runtime_dirs: list[str]) -> str:
    payload = {
        "status": status,
        "runtime_dirs": runtime_dirs,
        "carriers": [
            {
                "key": carrier["key"],
                "status": carrier["status"],
                "fingerprint": carrier["fingerprint"],
            }
            for carrier in carriers
        ],
    }
    return sha256_text(json.dumps(payload, sort_keys=True))


def load_manifest(repo_root: pathlib.Path) -> dict | None:
    manifest_path = repo_root / MANIFEST_REL_PATH
    if not manifest_path.exists():
        return None
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def classify_project(
    planning_exists: bool,
    state_exists: bool,
    project_exists: bool,
    roadmap_exists: bool,
    runtime_dirs: list[str],
    active_phase: bool,
    has_manifest: bool,
    doctrine_changed: bool,
    absent_additive: list[str],
    pending_doctrine_sensitive: list[str],
) -> str:
    if not planning_exists or not state_exists or not project_exists or not roadmap_exists:
        return "pre-uplift structural initialization"
    if any(runtime_dir != ".codex" for runtime_dir in runtime_dirs):
        return "cross-runtime uplift"
    if active_phase and (not has_manifest or doctrine_changed or pending_doctrine_sensitive or absent_additive):
        return "mid-phase uplift"
    if not has_manifest and len(absent_additive) + len(pending_doctrine_sensitive) >= 5:
        return "vanilla uplift"
    if doctrine_changed or absent_additive or pending_doctrine_sensitive or not has_manifest:
        return "lightly aged uplift"
    return "current-aligned posture"


def recommendation_reasons(
    has_manifest: bool,
    doctrine_changed: bool,
    absent_additive: list[str],
    pending_doctrine_sensitive: list[str],
    project_class: str,
) -> list[str]:
    reasons: list[str] = []
    if not has_manifest:
        reasons.append("no uplift manifest recorded yet")
    if doctrine_changed:
        reasons.append("doctrine reference fingerprint changed since the last uplift pass")
    if absent_additive:
        reasons.append(f"additive carriers still absent: {', '.join(absent_additive)}")
    if pending_doctrine_sensitive:
        reasons.append(
            "doctrine-sensitive carriers still need review: "
            + ", ".join(pending_doctrine_sensitive)
        )
    if project_class == "mid-phase uplift":
        reasons.append("phase work is active, so uplift should stay detect-only and composition-first")
    return reasons


def analyze_repo(repo_root: pathlib.Path) -> dict:
    repo_root = repo_root.resolve()
    planning_root = repo_root / ".planning"
    manifest = load_manifest(repo_root)
    planning_exists = planning_root.exists()
    project_exists = (planning_root / "PROJECT.md").exists()
    roadmap_exists = (planning_root / "ROADMAP.md").exists()
    state_exists = (planning_root / "STATE.md").exists()
    runtime_dirs = runtime_dirs_present(repo_root)
    current_status = state_status(repo_root)
    plan_count = count_phase_files(repo_root, "*/*-PLAN.md")
    summary_count = count_phase_files(repo_root, "*/*-SUMMARY.md")
    carriers = [build_file_carrier(repo_root, spec) for spec in FILE_CARRIERS]
    carriers.extend(build_marker_carrier(repo_root, spec) for spec in MARKER_CARRIERS)
    doctrine_hash = doctrine_reference_hash(carriers)
    project_hash = project_fingerprint_hash(carriers, current_status, runtime_dirs)
    absent_additive = [carrier["label"] for carrier in carriers if carrier["group"] == "additive_install" and not carrier["present"]]
    pending_doctrine_sensitive = [
        carrier["label"]
        for carrier in carriers
        if carrier["group"] == "doctrine_sensitive" and not carrier["present"]
    ]
    active_phase = current_status.lower() not in {"completed", "unknown"} or plan_count > summary_count
    doctrine_changed = bool(manifest and manifest.get("doctrine_reference_hash") != doctrine_hash)
    project_class = classify_project(
        planning_exists=planning_exists,
        state_exists=state_exists,
        project_exists=project_exists,
        roadmap_exists=roadmap_exists,
        runtime_dirs=runtime_dirs,
        active_phase=active_phase,
        has_manifest=manifest is not None,
        doctrine_changed=doctrine_changed,
        absent_additive=absent_additive,
        pending_doctrine_sensitive=pending_doctrine_sensitive,
    )
    reasons = recommendation_reasons(
        has_manifest=manifest is not None,
        doctrine_changed=doctrine_changed,
        absent_additive=absent_additive,
        pending_doctrine_sensitive=pending_doctrine_sensitive,
        project_class=project_class,
    )
    recommend_detect_only = bool(reasons) and project_class != "current-aligned posture"
    return {
        "repo_root": str(repo_root),
        "generated_at": now_iso(),
        "planning_exists": planning_exists,
        "project_exists": project_exists,
        "roadmap_exists": roadmap_exists,
        "state_exists": state_exists,
        "runtime_dirs": runtime_dirs,
        "current_status": current_status,
        "phase_activity": {
            "plan_count": plan_count,
            "summary_count": summary_count,
            "active_phase": active_phase,
        },
        "project_class": project_class,
        "doctrine_reference_hash": doctrine_hash,
        "project_fingerprint_hash": project_hash,
        "previous_manifest_present": manifest is not None,
        "doctrine_reference_changed": doctrine_changed,
        "absent_additive_carriers": absent_additive,
        "pending_doctrine_sensitive_proposals": pending_doctrine_sensitive,
        "held_later_families": HELD_LATER_FAMILIES,
        "recommend_detect_only": recommend_detect_only,
        "recommendation_reasons": reasons,
        "carriers": carriers,
    }


def render_report(analysis: dict) -> str:
    lines = [
        "# Project Uplift Report",
        "",
        f"- Generated: {analysis['generated_at']}",
        "- Mode: detect-only",
        f"- Project class: {analysis['project_class']}",
        f"- Recommendation: {'Run `$gsd-uplift-project --detect-only` again after doctrine movement or review queued proposals' if analysis['recommend_detect_only'] else 'Continue with current routing'}",
        "",
        "## Before-State Posture",
        "",
        f"- Planning surface present: {'yes' if analysis['planning_exists'] else 'no'}",
        f"- Current state status: {analysis['current_status']}",
        f"- Runtime directories present: {', '.join(analysis['runtime_dirs']) if analysis['runtime_dirs'] else 'none'}",
        f"- Prior uplift memory present: {'yes' if analysis['previous_manifest_present'] else 'no'}",
        f"- Doctrine reference changed since prior uplift: {'yes' if analysis['doctrine_reference_changed'] else 'no'}",
        "",
        "## Recommendation Reasons",
        "",
    ]
    if analysis["recommendation_reasons"]:
        lines.extend(f"- {reason}" for reason in analysis["recommendation_reasons"])
    else:
        lines.append("- Current uplift memory and current carrier posture are already carrying ordinary routing cleanly.")
    lines.extend(
        [
            "",
            "## Carrier Posture",
            "",
            "| Carrier | Group | State | Fingerprint | Note |",
            "|---------|-------|-------|-------------|------|",
        ]
    )
    for carrier in analysis["carriers"]:
        lines.append(
            f"| {carrier['label']} | {carrier['group']} | {carrier['status']} | "
            f"{carrier['fingerprint'] or '-'} | {carrier['note']} |"
        )

    lines.extend(
        [
            "",
            "## Additive Install Routes",
            "",
        ]
    )
    if analysis["absent_additive_carriers"]:
        lines.extend(f"- {carrier}" for carrier in analysis["absent_additive_carriers"])
    else:
        lines.append("- No additive carrier install is currently queued.")

    lines.extend(
        [
            "",
            "## Doctrine-Sensitive Proposal Routes",
            "",
        ]
    )
    if analysis["pending_doctrine_sensitive_proposals"]:
        lines.extend(f"- {carrier}" for carrier in analysis["pending_doctrine_sensitive_proposals"])
    else:
        lines.append("- No doctrine-sensitive proposal route is currently queued.")

    lines.extend(
        [
            "",
            "## Held For Later Families",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in analysis["held_later_families"])
    return "\n".join(lines) + "\n"


def post_write_analysis(analysis: dict) -> dict:
    retained_reasons = [
        reason
        for reason in analysis["recommendation_reasons"]
        if reason != "no uplift manifest recorded yet"
    ]
    return {
        **analysis,
        "recommend_detect_only": bool(retained_reasons) and analysis["project_class"] != "current-aligned posture",
        "recommendation_reasons": retained_reasons,
    }


def state_section_text(analysis: dict) -> str:
    recommendation = (
        "Run `$gsd-uplift-project --detect-only` before treating ordinary routing as settled."
        if analysis["recommend_detect_only"]
        else "Continue with ordinary routing; uplift memory is already carrying this posture."
    )
    pending_count = len(analysis["pending_doctrine_sensitive_proposals"])
    return "\n".join(
        [
            STATE_HEADING,
            "",
            f"Last uplift pass: {analysis['generated_at']}",
            f"Last uplift class: {analysis['project_class']}",
            f"Doctrine reference changed since prior uplift: {'yes' if analysis['doctrine_reference_changed'] else 'no'}",
            f"Pending doctrine-sensitive proposals: {pending_count}",
            f"Current recommendation: {recommendation}",
            f"Current uplift report: {REPORT_REL_PATH}",
            f"Current uplift manifest: {MANIFEST_REL_PATH}",
            "",
        ]
    )


def update_state_section(repo_root: pathlib.Path, analysis: dict) -> None:
    state_path = repo_root / ".planning" / "STATE.md"
    text = read_text(state_path)
    if text is None:
        return
    section = state_section_text(analysis)
    pattern = re.compile(rf"\n{re.escape(STATE_HEADING)}\n[\s\S]*?(?=\n## |\Z)")
    if pattern.search(text):
        updated = pattern.sub("\n" + section.rstrip() + "\n", text)
    else:
        session_marker = "\n## Session Continuity"
        if session_marker in text:
            updated = text.replace(session_marker, "\n" + section.rstrip() + "\n" + session_marker, 1)
        else:
            updated = text.rstrip() + "\n\n" + section
    state_path.write_text(updated, encoding="utf-8")


def write_outputs(repo_root: pathlib.Path, analysis: dict) -> dict:
    planning_root = repo_root / ".planning"
    planning_root.mkdir(parents=True, exist_ok=True)
    written_analysis = post_write_analysis(analysis)
    report_path = repo_root / REPORT_REL_PATH
    manifest_path = repo_root / MANIFEST_REL_PATH
    report_path.write_text(render_report(written_analysis), encoding="utf-8")
    manifest_payload = {
        "schema_version": 1,
        "generated_at": written_analysis["generated_at"],
        "mode": "detect-only",
        "last_uplift_class": written_analysis["project_class"],
        "doctrine_reference_hash": written_analysis["doctrine_reference_hash"],
        "project_fingerprint_hash": written_analysis["project_fingerprint_hash"],
        "current_status": written_analysis["current_status"],
        "runtime_dirs": written_analysis["runtime_dirs"],
        "recommend_detect_only": written_analysis["recommend_detect_only"],
        "recommendation_reasons": written_analysis["recommendation_reasons"],
        "absent_additive_carriers": written_analysis["absent_additive_carriers"],
        "pending_doctrine_sensitive_proposals": written_analysis["pending_doctrine_sensitive_proposals"],
        "held_later_families": written_analysis["held_later_families"],
        "carriers": written_analysis["carriers"],
    }
    manifest_path.write_text(json.dumps(manifest_payload, indent=2) + "\n", encoding="utf-8")
    update_state_section(repo_root, written_analysis)
    return {
        "report_path": str(report_path.relative_to(repo_root)),
        "manifest_path": str(manifest_path.relative_to(repo_root)),
    }


def build_progress_note(repo_root: pathlib.Path) -> dict:
    repo_root = repo_root.resolve()
    manifest = load_manifest(repo_root)
    if manifest is None:
        planning_root = repo_root / ".planning"
        show = planning_root.exists()
        return {
            "show": show,
            "manifest_present": False,
            "recommend_detect_only": show,
            "last_uplift_class": None,
            "doctrine_reference_changed": False,
            "pending_doctrine_sensitive_proposals": [],
            "recommendation": "Run `$gsd-uplift-project --detect-only` to record uplift memory." if show else "No uplift memory available.",
            "reasons": ["no uplift manifest recorded yet"] if show else [],
            "report_path": REPORT_REL_PATH,
            "manifest_path": MANIFEST_REL_PATH,
        }

    analysis = analyze_repo(repo_root)
    pending = manifest.get("pending_doctrine_sensitive_proposals", [])
    doctrine_changed = manifest.get("doctrine_reference_hash") != analysis["doctrine_reference_hash"]
    recommend_detect_only = bool(doctrine_changed or pending)
    reasons: list[str] = []
    if doctrine_changed:
        reasons.append("current doctrine reference fingerprint moved after the last uplift pass")
    if pending:
        reasons.append("pending doctrine-sensitive proposals are still recorded in uplift memory")
    recommendation = (
        "Run `$gsd-uplift-project --detect-only` to refresh uplift memory."
        if recommend_detect_only
        else "Continue with current routing."
    )
    return {
        "show": True,
        "manifest_present": True,
        "recommend_detect_only": recommend_detect_only,
        "last_uplift_class": manifest.get("last_uplift_class"),
        "last_uplift_at": manifest.get("generated_at"),
        "doctrine_reference_changed": doctrine_changed,
        "pending_doctrine_sensitive_proposals": pending,
        "recommendation": recommendation,
        "reasons": reasons,
        "report_path": REPORT_REL_PATH,
        "manifest_path": MANIFEST_REL_PATH,
    }


def emit_json(payload: dict) -> None:
    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")


def main() -> int:
    args = parse_args()
    repo_root = pathlib.Path(args.repo_root).resolve()
    if args.command == "detect":
        analysis = analyze_repo(repo_root)
        if args.write:
            analysis = {
                **analysis,
                "written_outputs": write_outputs(repo_root, analysis),
            }
        if args.json or True:
            emit_json(analysis)
        return 0

    if args.command == "progress-note":
        note = build_progress_note(repo_root)
        if args.json or True:
            emit_json(note)
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
