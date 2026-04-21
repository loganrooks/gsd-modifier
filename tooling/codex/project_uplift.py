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
import tomllib
from datetime import datetime, timezone


STATE_HEADING = "## Project Uplift"
REPORT_REL_PATH = ".planning/UPLIFT-REPORT.md"
MANIFEST_REL_PATH = ".planning/UPLIFT-MANIFEST.json"
HELD_LATER_REL_PATH = "tooling/codex/UPLIFT-HELD-LATER.md"
RUNTIME_MANIFEST_REL_PATH = ".codex/gsd-file-manifest.json"
RUNTIME_VERSION_REL_PATH = ".codex/get-shit-done/VERSION"
OVERLAY_MANIFEST_REL_PATH = "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"
UPLIFT_MANIFEST_SCHEMA_VERSION = 4
COMPATIBILITY_POSTURE = "observed_basis_only"
COMPATIBILITY_HELD_LATER = [
    "version-window claims beyond the observed runtime basis",
    "cross-runtime compatibility matrix",
    "upstream-template drift compatibility",
]
PROGRESS_NOTE_RENDER_FIELDS = (
    ("last_uplift_class", "Last uplift class"),
    ("last_uplift_secondary_signals", "Secondary signals"),
    ("recommendation", "Recommendation"),
    ("report_path", "Report"),
    ("manifest_path", "Manifest"),
)
PROGRESS_NOTE_REASON_LABEL = "Reason"

RUNTIME_DIRS = [
    ".codex",
    ".claude",
    ".gemini",
    ".config/opencode",
    ".opencode",
    ".config/kilo",
    ".kilo",
]

RERUN_BOUNDARY_PATTERNS = [
    re.compile(r"pre-rerun", re.I),
    re.compile(r"fresh discuss \+ plan required", re.I),
    re.compile(r"rerun-boundary", re.I),
    re.compile(r"input to the next discuss pass", re.I),
]


@dataclasses.dataclass(frozen=True)
class FileCarrierSpec:
    key: str
    group: str
    rel_path: str
    label: str
    fingerprint_shape: str = "content_sha256"


@dataclasses.dataclass(frozen=True)
class MarkerCarrierSpec:
    key: str
    group: str
    rel_path: str
    label: str
    marker: str
    fingerprint_shape: str = "marker_block_hash"


STATIC_FILE_CARRIERS = [
    FileCarrierSpec("root_agents", "doctrine_sensitive", "AGENTS.md", "Root AGENTS"),
    FileCarrierSpec("planning_agents", "doctrine_sensitive", ".planning/AGENTS.md", "Planning AGENTS"),
    FileCarrierSpec("root_claude", "doctrine_sensitive", "CLAUDE.md", "Root CLAUDE"),
    FileCarrierSpec("planning_claude", "doctrine_sensitive", ".planning/CLAUDE.md", "Planning CLAUDE"),
    FileCarrierSpec("claim_types", "additive_install", ".planning/CLAIM-TYPES.md", "Claim Types"),
    FileCarrierSpec(
        "long_arc",
        "additive_install",
        ".planning/LONG-ARC.md",
        "Long Arc",
        fingerprint_shape="frontmatter_hash",
    ),
    FileCarrierSpec(
        "tooling_inventory",
        "additive_install",
        "tooling/codex/README.md",
        "Tooling Inventory",
        fingerprint_shape="inventory_item_hash",
    ),
    FileCarrierSpec(
        "runtime_config",
        "runtime_registry",
        ".codex/config.toml",
        "Runtime Config",
        fingerprint_shape="normalized_toml_hash",
    ),
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


def read_json(path: pathlib.Path) -> dict | None:
    text = read_text(path)
    if text is None:
        return None
    return json.loads(text)


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


def rel_path(repo_root: pathlib.Path, path: pathlib.Path) -> str:
    return str(path.relative_to(repo_root))


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
    for rel_path_str in RUNTIME_DIRS:
        if (repo_root / rel_path_str).exists():
            present.append(rel_path_str)
    return present


def load_manifest(repo_root: pathlib.Path) -> dict | None:
    return read_json(repo_root / MANIFEST_REL_PATH)


def load_runtime_manifest(repo_root: pathlib.Path) -> dict | None:
    return read_json(repo_root / RUNTIME_MANIFEST_REL_PATH)


def load_overlay_manifest(repo_root: pathlib.Path) -> dict | None:
    return read_json(repo_root / OVERLAY_MANIFEST_REL_PATH)


def runtime_version_source(repo_root: pathlib.Path) -> tuple[str | None, str | None]:
    text = read_text(repo_root / RUNTIME_VERSION_REL_PATH)
    if text is None:
        return None, None
    return text.strip(), RUNTIME_VERSION_REL_PATH


def build_compatibility_basis(repo_root: pathlib.Path) -> dict:
    runtime_manifest = load_runtime_manifest(repo_root) or {}
    overlay_manifest = load_overlay_manifest(repo_root) or {}
    runtime_version, runtime_version_source_path = runtime_version_source(repo_root)
    runtime_manifest_version = runtime_manifest.get("version")
    aligned = (
        runtime_version is not None
        and runtime_manifest_version is not None
        and runtime_version == runtime_manifest_version
    )
    observed_versions = [
        version
        for version in [runtime_version, runtime_manifest_version]
        if isinstance(version, str) and version
    ]
    return {
        "compatibility_posture": COMPATIBILITY_POSTURE,
        "observed_runtime_version": runtime_version,
        "observed_runtime_version_source": runtime_version_source_path,
        "observed_runtime_manifest_version": runtime_manifest_version,
        "observed_runtime_manifest_source": RUNTIME_MANIFEST_REL_PATH if runtime_manifest_version else None,
        "observed_runtime_version_aligned": aligned,
        "observed_runtime_version_set": sorted(set(observed_versions)),
        "overlay_manifest_schema_version": overlay_manifest.get("schema_version"),
        "uplift_manifest_schema_version": UPLIFT_MANIFEST_SCHEMA_VERSION,
        "check_protocol": [
            "compare candidate runtime version to observed_runtime_version",
            "compare candidate runtime manifest version to observed_runtime_manifest_version when present",
            "rerun ./scripts/setup-portable-gsd.sh before refreshing durable uplift memory after runtime movement",
            "rerun $gsd-uplift-project --write after runtime movement so compatibility anchors and uplift posture stay in tune",
        ],
        "held_later": COMPATIBILITY_HELD_LATER,
    }


def compatibility_drift_reasons(previous: dict, current: dict) -> list[str]:
    reasons: list[str] = []
    fields = (
        ("observed_runtime_version", "observed runtime version"),
        ("observed_runtime_manifest_version", "observed runtime manifest version"),
        ("observed_runtime_version_source", "observed runtime version source"),
        ("observed_runtime_manifest_source", "observed runtime manifest source"),
        ("observed_runtime_version_aligned", "runtime version alignment state"),
    )
    for key, label in fields:
        before = previous.get(key)
        after = current.get(key)
        if before == after:
            continue
        before_text = "unrecorded" if before in (None, "") else str(before)
        after_text = "unrecorded" if after in (None, "") else str(after)
        reasons.append(f"{label} moved from {before_text} to {after_text}")
    return reasons


def parse_held_later_family_line(line: str) -> dict:
    body = line[2:].strip()
    if " — " not in body:
        return {
            "family": body,
            "status": "held",
            "pointer": None,
        }
    family, remainder = body.split(" — ", 1)
    if ": " in remainder:
        status, pointer = remainder.split(": ", 1)
        pointer = pointer.strip() or None
    else:
        status = remainder
        pointer = None
    return {
        "family": family.strip(),
        "status": status.strip(),
        "pointer": pointer,
    }


def format_held_later_family(entry: dict) -> str:
    text = f"{entry['family']} — {entry['status']}"
    if entry.get("pointer"):
        text += f": {entry['pointer']}"
    return text


def load_held_later_families(repo_root: pathlib.Path) -> list[dict]:
    text = read_text(repo_root / HELD_LATER_REL_PATH)
    if text is None:
        return [
            {
                "family": f"held-later reference missing: {HELD_LATER_REL_PATH}",
                "status": "missing",
                "pointer": None,
            }
        ]
    items = [
        parse_held_later_family_line(line)
        for line in text.splitlines()
        if line.startswith("- ")
    ]
    return items


def phase_sort_key(path: pathlib.Path) -> tuple:
    prefix = path.parent.name.split("-", 1)[0]
    parts: list[tuple[int, int | str]] = []
    for piece in prefix.split("."):
        if piece.isdigit():
            parts.append((0, int(piece)))
        else:
            parts.append((1, piece))
    return tuple(parts)


def latest_phase_context_path(repo_root: pathlib.Path) -> pathlib.Path | None:
    phase_root = repo_root / ".planning" / "phases"
    if not phase_root.exists():
        return None
    context_paths = list(phase_root.glob("*/*-CONTEXT.md"))
    if not context_paths:
        return None
    return sorted(context_paths, key=phase_sort_key)[-1]


def has_rerun_boundary_marker(text: str) -> bool:
    return any(pattern.search(text) for pattern in RERUN_BOUNDARY_PATTERNS)


def phase_boundary_signal(repo_root: pathlib.Path, active_phase: bool, doctrine_changed: bool) -> dict:
    if not active_phase:
        return {
            "context_path": None,
            "context_present": False,
            "rerun_boundary_marker_present": False,
            "mid_phase_signal": False,
            "note": "no active phase boundary signal",
        }

    context_path = latest_phase_context_path(repo_root)
    if context_path is None:
        return {
            "context_path": None,
            "context_present": False,
            "rerun_boundary_marker_present": False,
            "mid_phase_signal": False,
            "note": "active phase detected but no phase CONTEXT carrier found",
        }

    text = read_text(context_path) or ""
    marker_present = has_rerun_boundary_marker(text)
    mid_phase_signal = marker_present or doctrine_changed
    if marker_present:
        note = "phase CONTEXT carries explicit rerun-boundary posture"
    elif doctrine_changed:
        note = "phase CONTEXT lacks explicit rerun-boundary posture while doctrine moved"
    else:
        note = "phase CONTEXT present without explicit rerun-boundary posture"
    return {
        "context_path": rel_path(repo_root, context_path),
        "context_present": True,
        "rerun_boundary_marker_present": marker_present,
        "mid_phase_signal": mid_phase_signal,
        "note": note,
    }


def build_runtime_agent_specs(repo_root: pathlib.Path) -> list[FileCarrierSpec]:
    agent_root = repo_root / ".codex" / "agents"
    if not agent_root.exists():
        return []
    specs: list[FileCarrierSpec] = []
    for path in sorted(agent_root.glob("*.toml")):
        stem = path.stem
        specs.append(
            FileCarrierSpec(
                key=f"runtime_agent_{stem}",
                group="runtime_registry",
                rel_path=rel_path(repo_root, path),
                label=f"Runtime Agent Contract: {stem}",
                fingerprint_shape="normalized_toml_hash",
            )
        )
    return specs


def frontmatter_text(text: str) -> str | None:
    match = re.match(r"^---\n([\s\S]+?)\n---", text)
    if not match:
        return None
    return match.group(1).strip()


def inventory_items(text: str) -> list[str]:
    items = [
        match.group(1)
        for match in re.finditer(r"^- `([^`]+)`", text, re.M)
    ]
    return items


def normalized_toml_fingerprint(text: str) -> str:
    data = tomllib.loads(text)
    return sha256_text(json.dumps(data, sort_keys=True, separators=(",", ":")))


def heading_level(line: str) -> int | None:
    match = re.match(r"^(#+)\s+", line)
    if not match:
        return None
    return len(match.group(1))


def marker_block_text(text: str, marker: str) -> str | None:
    lines = text.splitlines()
    heading_indexes = [
        idx
        for idx, line in enumerate(lines)
        if marker in line and heading_level(line) is not None
    ]
    if heading_indexes:
        start = heading_indexes[0]
    else:
        raw_indexes = [idx for idx, line in enumerate(lines) if marker in line]
        if not raw_indexes:
            return None
        start = raw_indexes[0]

    level = heading_level(lines[start])
    if level is None:
        return lines[start]

    end = len(lines)
    for idx in range(start + 1, len(lines)):
        candidate_level = heading_level(lines[idx])
        if candidate_level is not None and candidate_level <= level:
            end = idx
            break
    return "\n".join(lines[start:end]).strip()


def compute_fingerprint(text: str, fingerprint_shape: str, marker: str | None = None) -> str:
    if fingerprint_shape == "frontmatter_hash":
        payload = frontmatter_text(text) or text
        return sha256_text(payload)
    if fingerprint_shape == "inventory_item_hash":
        items = inventory_items(text)
        payload = "\n".join(items) if items else text
        return sha256_text(payload)
    if fingerprint_shape == "normalized_toml_hash":
        try:
            return normalized_toml_fingerprint(text)
        except tomllib.TOMLDecodeError:
            return sha256_text(text)
    if fingerprint_shape == "marker_block_hash" and marker is not None:
        payload = marker_block_text(text, marker) or text
        return sha256_text(payload)
    return sha256_text(text)


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
        "fingerprint_shape": spec.fingerprint_shape,
        "fingerprint": compute_fingerprint(text, spec.fingerprint_shape) if text is not None else None,
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
        "fingerprint_shape": spec.fingerprint_shape,
        "fingerprint": compute_fingerprint(text, spec.fingerprint_shape, marker=spec.marker) if marker_present and text is not None else None,
        "note": note,
    }


def doctrine_reference_hash(carriers: list[dict]) -> str:
    selected = [
        f"{carrier['key']}:{carrier['status']}:{carrier['fingerprint_shape']}:{carrier['fingerprint'] or '-'}"
        for carrier in carriers
        if carrier["group"] in {"additive_install", "doctrine_sensitive", "runtime_registry"}
    ]
    return sha256_text("\n".join(sorted(selected)))


def project_fingerprint_hash(
    carriers: list[dict],
    status: str,
    runtime_dirs: list[str],
    primary_class: str,
    secondary_signals: list[str],
    boundary_signal: dict,
) -> str:
    payload = {
        "status": status,
        "runtime_dirs": runtime_dirs,
        "primary_class": primary_class,
        "secondary_signals": secondary_signals,
        "phase_boundary_signal": boundary_signal,
        "carriers": [
            {
                "key": carrier["key"],
                "status": carrier["status"],
                "fingerprint_shape": carrier["fingerprint_shape"],
                "fingerprint": carrier["fingerprint"],
            }
            for carrier in carriers
        ],
    }
    return sha256_text(json.dumps(payload, sort_keys=True))


def summarize_proposal_route(proposal: dict) -> str:
    state = proposal["proposal_state"]
    if state == "absent":
        return f"{proposal['label']} (absent)"
    return f"{proposal['label']} (drifted)"


def doctrine_sensitive_proposals(carriers: list[dict], manifest: dict | None) -> list[dict]:
    previous_carriers = {
        carrier["key"]: carrier
        for carrier in (manifest or {}).get("carriers", [])
        if isinstance(carrier, dict) and "key" in carrier
    }
    proposals: list[dict] = []
    for carrier in carriers:
        if carrier["group"] != "doctrine_sensitive":
            continue
        previous = previous_carriers.get(carrier["key"], {})
        proposal_state: str | None = None
        note: str
        if not carrier["present"]:
            proposal_state = "absent"
            note = "carrier absent and needs first-pass install or explicit review"
        else:
            previous_fingerprint = previous.get("fingerprint")
            current_fingerprint = carrier.get("fingerprint")
            if (
                manifest is not None
                and previous_fingerprint
                and current_fingerprint
                and previous_fingerprint != current_fingerprint
            ):
                proposal_state = "drifted"
                note = "carrier present but fingerprint drifted since the last uplift pass"
            else:
                continue

        proposals.append(
            {
                "key": carrier["key"],
                "label": carrier["label"],
                "proposal_state": proposal_state,
                "group": carrier["group"],
                "rel_path": carrier["rel_path"],
                "fingerprint_shape": carrier["fingerprint_shape"],
                "current_fingerprint": carrier.get("fingerprint"),
                "previous_fingerprint": previous.get("fingerprint"),
                "note": note,
            }
        )
    return proposals


def secondary_signals(
    primary_class: str,
    runtime_dirs: list[str],
    boundary_signal: dict,
    doctrine_changed: bool,
    pending_proposals: list[dict],
) -> list[str]:
    signals: list[str] = []
    if any(runtime_dir != ".codex" for runtime_dir in runtime_dirs) and primary_class != "cross-runtime uplift":
        signals.append("cross_runtime")
    if boundary_signal.get("mid_phase_signal") and primary_class != "mid-phase uplift":
        signals.append("mid_phase")
    if doctrine_changed:
        signals.append("doctrine_changed")
    if pending_proposals:
        signals.append("has_pending_proposals")
    return signals


def classify_project(
    planning_exists: bool,
    state_exists: bool,
    project_exists: bool,
    roadmap_exists: bool,
    runtime_dirs: list[str],
    boundary_signal: dict,
    has_manifest: bool,
    doctrine_changed: bool,
    absent_additive: list[str],
    pending_doctrine_sensitive: list[dict],
) -> str:
    if not planning_exists or not state_exists or not project_exists or not roadmap_exists:
        return "pre-uplift structural initialization"
    if any(runtime_dir != ".codex" for runtime_dir in runtime_dirs):
        return "cross-runtime uplift"
    if boundary_signal.get("mid_phase_signal"):
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
    pending_doctrine_sensitive: list[dict],
    primary_class: str,
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
            + ", ".join(summarize_proposal_route(proposal) for proposal in pending_doctrine_sensitive)
        )
    if primary_class == "mid-phase uplift":
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
    active_phase = current_status.lower() not in {"completed", "unknown"} or plan_count > summary_count

    file_specs = STATIC_FILE_CARRIERS + build_runtime_agent_specs(repo_root)
    carriers = [build_file_carrier(repo_root, spec) for spec in file_specs]
    carriers.extend(build_marker_carrier(repo_root, spec) for spec in MARKER_CARRIERS)

    previous_manifest_present = manifest is not None
    doctrine_hash = doctrine_reference_hash(carriers)
    doctrine_changed = bool(manifest and manifest.get("doctrine_reference_hash") != doctrine_hash)
    boundary_signal = phase_boundary_signal(repo_root, active_phase, doctrine_changed)
    absent_additive = [
        carrier["label"]
        for carrier in carriers
        if carrier["group"] == "additive_install" and not carrier["present"]
    ]
    pending_doctrine_sensitive = doctrine_sensitive_proposals(carriers, manifest)
    primary_class = classify_project(
        planning_exists=planning_exists,
        state_exists=state_exists,
        project_exists=project_exists,
        roadmap_exists=roadmap_exists,
        runtime_dirs=runtime_dirs,
        boundary_signal=boundary_signal,
        has_manifest=previous_manifest_present,
        doctrine_changed=doctrine_changed,
        absent_additive=absent_additive,
        pending_doctrine_sensitive=pending_doctrine_sensitive,
    )
    secondary = secondary_signals(
        primary_class=primary_class,
        runtime_dirs=runtime_dirs,
        boundary_signal=boundary_signal,
        doctrine_changed=doctrine_changed,
        pending_proposals=pending_doctrine_sensitive,
    )
    project_hash = project_fingerprint_hash(
        carriers=carriers,
        status=current_status,
        runtime_dirs=runtime_dirs,
        primary_class=primary_class,
        secondary_signals=secondary,
        boundary_signal=boundary_signal,
    )
    reasons = recommendation_reasons(
        has_manifest=previous_manifest_present,
        doctrine_changed=doctrine_changed,
        absent_additive=absent_additive,
        pending_doctrine_sensitive=pending_doctrine_sensitive,
        primary_class=primary_class,
    )
    recommend_detect_only = bool(reasons) and primary_class != "current-aligned posture"
    held_later = load_held_later_families(repo_root)
    compatibility_basis = build_compatibility_basis(repo_root)
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
        "phase_boundary_signal": boundary_signal,
        "project_class": primary_class,
        "primary_project_class": primary_class,
        "secondary_signals": secondary,
        "doctrine_reference_hash": doctrine_hash,
        "project_fingerprint_hash": project_hash,
        "previous_manifest_present": previous_manifest_present,
        "doctrine_reference_changed": doctrine_changed,
        "absent_additive_carriers": absent_additive,
        "pending_doctrine_sensitive_proposals": pending_doctrine_sensitive,
        "held_later_families": held_later,
        "compatibility_basis": compatibility_basis,
        "recommend_detect_only": recommend_detect_only,
        "recommendation_reasons": reasons,
        "carriers": carriers,
    }


def render_report(analysis: dict) -> str:
    secondary = ", ".join(analysis["secondary_signals"]) if analysis["secondary_signals"] else "none"
    boundary = analysis["phase_boundary_signal"]
    lines = [
        "# Project Uplift Report",
        "",
        f"- Generated: {analysis['generated_at']}",
        "- Mode: detect-only",
        f"- Project class: {analysis['project_class']}",
        f"- Secondary signals: {secondary}",
        f"- Recommendation: {'Run `$gsd-uplift-project --detect-only` again after doctrine movement or review queued proposals' if analysis['recommend_detect_only'] else 'Continue with current routing'}",
        "",
        "## Before-State Posture",
        "",
        f"- Planning surface present: {'yes' if analysis['planning_exists'] else 'no'}",
        f"- Current state status: {analysis['current_status']}",
        f"- Runtime directories present: {', '.join(analysis['runtime_dirs']) if analysis['runtime_dirs'] else 'none'}",
        f"- Prior uplift memory present: {'yes' if analysis['previous_manifest_present'] else 'no'}",
        f"- Doctrine reference changed since prior uplift: {'yes' if analysis['doctrine_reference_changed'] else 'no'}",
        f"- Phase boundary signal: {boundary['note']}",
        f"- Phase context carrier: {boundary['context_path'] or 'none'}",
        "",
        "## Recommendation Reasons",
        "",
    ]
    if analysis["recommendation_reasons"]:
        lines.extend(f"- {reason}" for reason in analysis["recommendation_reasons"])
    else:
        lines.append("- Current uplift memory keeps ordinary routing explicit without queuing another detect-only pass.")

    compatibility = analysis["compatibility_basis"]
    version_alignment = "aligned" if compatibility["observed_runtime_version_aligned"] else "split-or-partial"
    lines.extend(
        [
            "",
            "## Compatibility Basis",
            "",
            f"- Compatibility posture: {compatibility['compatibility_posture']}",
            f"- Observed runtime version: {compatibility['observed_runtime_version'] or 'unrecorded'}",
            f"- Observed runtime manifest version: {compatibility['observed_runtime_manifest_version'] or 'unrecorded'}",
            f"- Runtime version alignment: {version_alignment}",
            f"- Overlay manifest schema version: {compatibility['overlay_manifest_schema_version'] or 'unrecorded'}",
            f"- Uplift manifest schema version: {compatibility['uplift_manifest_schema_version']}",
            "",
            "### Compatibility Check Protocol",
            "",
        ]
    )
    lines.extend(f"- {step}" for step in compatibility["check_protocol"])
    lines.extend(
        [
            "",
            "### Wider Compatibility Claims Held",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in compatibility["held_later"])
    lines.extend(
        [
            "",
            "## Carrier Posture",
            "",
            "| Carrier | Group | State | Fingerprint Shape | Fingerprint | Note |",
            "|---------|-------|-------|-------------------|-------------|------|",
        ]
    )
    for carrier in analysis["carriers"]:
        lines.append(
            f"| {carrier['label']} | {carrier['group']} | {carrier['status']} | "
            f"{carrier['fingerprint_shape']} | {carrier['fingerprint'] or '-'} | {carrier['note']} |"
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
        for proposal in analysis["pending_doctrine_sensitive_proposals"]:
            lines.append(
                "- "
                + f"{proposal['label']} — {proposal['proposal_state']} "
                + f"({proposal['fingerprint_shape']})"
            )
    else:
        lines.append("- No doctrine-sensitive proposal route is currently queued.")

    lines.extend(
        [
            "",
            "## Held For Later Families",
            "",
        ]
    )
    lines.extend(f"- {format_held_later_family(item)}" for item in analysis["held_later_families"])
    return "\n".join(lines) + "\n"


def post_write_analysis(analysis: dict) -> dict:
    retained_pending = [
        proposal
        for proposal in analysis["pending_doctrine_sensitive_proposals"]
        if proposal["proposal_state"] != "drifted"
    ]
    retained_reasons = recommendation_reasons(
        has_manifest=True,
        doctrine_changed=False,
        absent_additive=analysis["absent_additive_carriers"],
        pending_doctrine_sensitive=retained_pending,
        primary_class=analysis["project_class"],
    )
    retained_secondary = secondary_signals(
        primary_class=analysis["project_class"],
        runtime_dirs=analysis["runtime_dirs"],
        boundary_signal=analysis["phase_boundary_signal"],
        doctrine_changed=False,
        pending_proposals=retained_pending,
    )
    return {
        **analysis,
        "previous_manifest_present": True,
        "doctrine_reference_changed": False,
        "pending_doctrine_sensitive_proposals": retained_pending,
        "secondary_signals": retained_secondary,
        "recommend_detect_only": bool(retained_reasons) and analysis["project_class"] != "current-aligned posture",
        "recommendation_reasons": retained_reasons,
    }


def state_section_text(analysis: dict) -> str:
    recommendation = (
        "Run `$gsd-uplift-project --detect-only` before treating ordinary routing as settled."
        if analysis["recommend_detect_only"]
        else "Continue with ordinary routing; uplift memory keeps this posture explicit."
    )
    pending_count = len(analysis["pending_doctrine_sensitive_proposals"])
    secondary = ", ".join(analysis["secondary_signals"]) if analysis["secondary_signals"] else "none"
    compatibility = analysis["compatibility_basis"]
    return "\n".join(
        [
            STATE_HEADING,
            "",
            f"Last uplift pass: {analysis['generated_at']}",
            f"Last uplift class: {analysis['project_class']}",
            f"Last uplift secondary signals: {secondary}",
            f"Phase boundary signal: {analysis['phase_boundary_signal']['note']}",
            f"Doctrine reference changed since prior uplift: {'yes' if analysis['doctrine_reference_changed'] else 'no'}",
            f"Compatibility posture: {compatibility['compatibility_posture']}",
            f"Observed runtime basis: {', '.join(compatibility['observed_runtime_version_set']) if compatibility['observed_runtime_version_set'] else 'unrecorded'}",
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
        "schema_version": UPLIFT_MANIFEST_SCHEMA_VERSION,
        "generated_at": written_analysis["generated_at"],
        "mode": "detect-only",
        "last_uplift_class": written_analysis["project_class"],
        "last_uplift_secondary_signals": written_analysis["secondary_signals"],
        "phase_boundary_signal": written_analysis["phase_boundary_signal"],
        "doctrine_reference_hash": written_analysis["doctrine_reference_hash"],
        "project_fingerprint_hash": written_analysis["project_fingerprint_hash"],
        "current_status": written_analysis["current_status"],
        "runtime_dirs": written_analysis["runtime_dirs"],
        "recommend_detect_only": written_analysis["recommend_detect_only"],
        "recommendation_reasons": written_analysis["recommendation_reasons"],
        "absent_additive_carriers": written_analysis["absent_additive_carriers"],
        "pending_doctrine_sensitive_proposals": written_analysis["pending_doctrine_sensitive_proposals"],
        "held_later_families": written_analysis["held_later_families"],
        "compatibility_basis": written_analysis["compatibility_basis"],
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
            "last_uplift_secondary_signals": [],
            "doctrine_reference_changed": False,
            "pending_doctrine_sensitive_proposals": [],
            "recommendation": "Run `$gsd-uplift-project --detect-only` to record uplift memory." if show else "No uplift memory available.",
            "reasons": ["no uplift manifest recorded yet"] if show else [],
            "report_path": REPORT_REL_PATH,
            "manifest_path": MANIFEST_REL_PATH,
        }

    analysis = analyze_repo(repo_root)
    pending = analysis["pending_doctrine_sensitive_proposals"]
    doctrine_changed = manifest.get("doctrine_reference_hash") != analysis["doctrine_reference_hash"]
    manifest_compatibility = manifest.get("compatibility_basis") or {}
    current_compatibility = analysis["compatibility_basis"]
    compatibility_reasons = compatibility_drift_reasons(manifest_compatibility, current_compatibility)
    compatibility_basis_changed = bool(compatibility_reasons)
    recommend_write = compatibility_basis_changed
    recommend_detect_only = bool((doctrine_changed or pending) and not recommend_write)
    reasons: list[str] = []
    if doctrine_changed:
        reasons.append("current doctrine reference fingerprint moved after the last uplift pass")
    if pending:
        reasons.append(
            "doctrine-sensitive proposals still recorded: "
            + ", ".join(summarize_proposal_route(proposal) for proposal in pending)
        )
    reasons.extend(compatibility_reasons)
    recommendation = (
        "Run `$gsd-uplift-project --write` to refresh uplift memory after runtime basis movement."
        if recommend_write
        else (
            "Run `$gsd-uplift-project --detect-only` to refresh uplift memory."
            if recommend_detect_only
            else "Continue with current routing."
        )
    )
    return {
        "show": True,
        "manifest_present": True,
        "recommend_write": recommend_write,
        "recommend_detect_only": recommend_detect_only,
        "last_uplift_class": manifest.get("last_uplift_class"),
        "last_uplift_secondary_signals": manifest.get("last_uplift_secondary_signals", []),
        "last_uplift_at": manifest.get("generated_at"),
        "doctrine_reference_changed": doctrine_changed,
        "compatibility_basis_changed": compatibility_basis_changed,
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
