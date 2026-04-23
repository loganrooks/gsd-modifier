#!/usr/bin/env python3
"""Detect and record repo-local project uplift posture."""

from __future__ import annotations

import argparse
import dataclasses
import functools
import hashlib
import json
import pathlib
import re
import sys
import tomllib
from datetime import datetime, timezone

REPO_ROOT_FOR_IMPORTS = pathlib.Path(__file__).resolve().parents[2]
if str(REPO_ROOT_FOR_IMPORTS) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT_FOR_IMPORTS))

from harness_modifier.compatibility import declaration as compatibility_declaration
from harness_modifier.compatibility import observation as compatibility_observation
from harness_modifier.compatibility import seed_contract as compatibility_seed_contract
from harness_modifier.uplift import carrier_catalog as uplift_carrier_catalog
from harness_modifier.uplift import output_policy as uplift_output_policy
from harness_modifier.uplift import phase_layout as uplift_phase_layout
from harness_modifier.uplift import state_writer as uplift_state_writer
from harness_modifier.uplift import vocabulary as uplift_vocabulary


OVERLAY_MANIFEST_REL_PATH = "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json"
PROGRESS_NOTE_RENDER_FIELDS = (
    ("last_uplift_class", "Last uplift class"),
    ("last_uplift_secondary_signals", "Secondary signals"),
    ("held_runtime_annotation", "Held runtime annotation"),
    ("seed_corpus_posture", "Seed corpus posture"),
    ("recommendation", "Recommendation"),
    ("report_path", "Report"),
    ("manifest_path", "Manifest"),
)
PROGRESS_NOTE_REASON_LABEL = "Reason"
SEED_POSTURE_REASON_LABEL = "Seed posture reason"
SEED_MIGRATION_CANDIDATE_LABEL = "Seed migration candidates"
SEED_MIGRATION_BREAKDOWN_LABEL = "Seed migration breakdown"
SEED_MIGRATION_INSPECT_POINTER_LABEL = "Seed migration inventory"
SEED_MIGRATION_WRITE_POINTER_LABEL = "Seed migration write packet"


def compatibility_policy() -> dict:
    return compatibility_declaration.load_declaration()


def compatibility_declaration_rel_path() -> str:
    return compatibility_declaration.DECLARATION_REL_PATH


def observation_policy() -> dict:
    return compatibility_observation.load_observation()


def seed_contract_policy() -> dict:
    return compatibility_seed_contract.load_seed_contract()


def uplift_output_policy_data() -> dict:
    return uplift_output_policy.load_output_policy()


def phase_layout_policy() -> dict:
    return uplift_phase_layout.load_phase_layout()


def carrier_catalog_policy() -> dict:
    return uplift_carrier_catalog.load_carrier_catalog()


def vocabulary_policy() -> dict:
    return uplift_vocabulary.load_vocabulary()


def command_text(key: str) -> str:
    return str(vocabulary_policy()["commands"][key])


def recommendation_text(key: str) -> str:
    return str(vocabulary_policy()["recommendations"][key])


def phase_boundary_note(key: str) -> str:
    return str(vocabulary_policy()["phase_boundary_notes"][key])


def carrier_catalog_ordering_rule() -> str:
    return str(carrier_catalog_policy()["ordering_rule"])


@functools.lru_cache(maxsize=1)
def _compiled_rerun_boundary_patterns() -> tuple[re.Pattern[str], ...]:
    return tuple(
        re.compile(pattern, re.I)
        for pattern in vocabulary_policy()["rerun_boundary_patterns"]
    )


SEED_MIGRATION_SKILL_COMMAND = command_text("seed_migration_inventory")
SEED_MIGRATION_WRITE_COMMAND = command_text("seed_migration_write")


def state_heading() -> str:
    return str(uplift_output_policy_data()["state_heading"])


def report_rel_path() -> str:
    return str(uplift_output_policy_data()["report_rel_path"])


def manifest_rel_path() -> str:
    return str(uplift_output_policy_data()["manifest_rel_path"])


def held_later_rel_path() -> str:
    return str(uplift_output_policy_data()["held_later_rel_path"])


def overlay_manifest_rel_path() -> str:
    return OVERLAY_MANIFEST_REL_PATH


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


@dataclasses.dataclass(frozen=True)
class RuntimeAgentRegistrySpec:
    key_prefix: str
    group: str
    rel_path_glob: str
    label_prefix: str
    fingerprint_shape: str = "normalized_toml_hash"


def _canonicalize_catalog_rows(rows: list[dict]) -> list[dict]:
    ordering_rule = carrier_catalog_ordering_rule()
    if ordering_rule == "stable_by_key_within_section":
        return sorted(rows, key=lambda row: str(row["key"]))
    return list(rows)


def file_carrier_specs() -> list[FileCarrierSpec]:
    rows = _canonicalize_catalog_rows(list(carrier_catalog_policy()["file_carriers"]))
    return [
        FileCarrierSpec(
            key=str(row["key"]),
            group=str(row["group"]),
            rel_path=str(row["rel_path"]),
            label=str(row["label"]),
            fingerprint_shape=str(row.get("fingerprint_shape", "content_sha256")),
        )
        for row in rows
    ]


def marker_carrier_specs() -> list[MarkerCarrierSpec]:
    rows = _canonicalize_catalog_rows(list(carrier_catalog_policy()["marker_carriers"]))
    return [
        MarkerCarrierSpec(
            key=str(row["key"]),
            group=str(row["group"]),
            rel_path=str(row["rel_path"]),
            label=str(row["label"]),
            marker=str(row["marker"]),
            fingerprint_shape=str(row.get("fingerprint_shape", "marker_block_hash")),
        )
        for row in rows
    ]


def runtime_agent_registry_spec() -> RuntimeAgentRegistrySpec:
    row = dict(carrier_catalog_policy()["runtime_agent_registry"])
    return RuntimeAgentRegistrySpec(
        key_prefix=str(row["key_prefix"]),
        group=str(row["group"]),
        rel_path_glob=str(row["rel_path_glob"]),
        label_prefix=str(row["label_prefix"]),
        fingerprint_shape=str(row.get("fingerprint_shape", "normalized_toml_hash")),
    )


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


def read_runtime_version_at(repo_root: pathlib.Path, rel_path_str: str) -> tuple[str | None, str | None]:
    text = read_text(repo_root / rel_path_str)
    if text is None:
        return None, None
    return text.strip(), rel_path_str


def state_status(repo_root: pathlib.Path) -> str:
    state_path = repo_root / uplift_state_writer.state_rel_path()
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


def phase_root_path(repo_root: pathlib.Path) -> pathlib.Path:
    return repo_root / str(phase_layout_policy()["phase_root_rel_path"])


def phase_document_glob(kind: str) -> str:
    return str(phase_layout_policy()["document_globs"][kind])


def count_phase_files(repo_root: pathlib.Path, kind: str) -> int:
    phase_root = phase_root_path(repo_root)
    if not phase_root.exists():
        return 0
    return sum(1 for _ in phase_root.glob(phase_document_glob(kind)))


def runtime_dirs_present(repo_root: pathlib.Path) -> list[str]:
    policy = observation_policy()
    rel_paths = list(policy["observed_runtime_directories"]) + list(
        policy["candidate_observed_runtime_directories"]
    )
    present: list[str] = []
    seen: set[str] = set()
    for rel_path_str in rel_paths:
        if rel_path_str in seen:
            continue
        seen.add(rel_path_str)
        if (repo_root / rel_path_str).exists():
            present.append(rel_path_str)
    return present


def load_manifest(repo_root: pathlib.Path) -> dict | None:
    return read_json(repo_root / manifest_rel_path())


def load_runtime_manifest(repo_root: pathlib.Path, declaration: dict) -> dict | None:
    return read_json(repo_root / declaration["runtime_basis"]["manifest_version_source"])


def load_overlay_manifest(repo_root: pathlib.Path) -> dict | None:
    return read_json(repo_root / overlay_manifest_rel_path())


def runtime_version_source(repo_root: pathlib.Path, declaration: dict) -> tuple[str | None, str | None]:
    return read_runtime_version_at(repo_root, declaration["runtime_basis"]["version_source"])


def held_runtime_annotation(repo_root: pathlib.Path, declaration: dict) -> dict | None:
    for declared_annotation in declaration["runtime_held_annotations"]:
        version_source = declared_annotation["version_source"]
        version, version_source_path = read_runtime_version_at(repo_root, version_source)
        if version is None:
            continue
        return {
            "runtime": declared_annotation["runtime"],
            "version": version,
            "version_source": version_source_path,
            "annotation_posture": declared_annotation["annotation_posture"],
            "note": declared_annotation["note"],
        }
    return None


def held_runtime_annotation_summary(annotation: dict | None) -> str | None:
    if not isinstance(annotation, dict):
        return None
    runtime = annotation.get("runtime") or "unnamed"
    version = annotation.get("version") or "unrecorded"
    posture = annotation.get("annotation_posture") or "held"
    return f"{runtime} {version} ({posture})"


def build_compatibility_basis(repo_root: pathlib.Path, declaration: dict) -> dict:
    runtime_manifest = load_runtime_manifest(repo_root, declaration) or {}
    overlay_manifest = load_overlay_manifest(repo_root) or {}
    runtime_version, runtime_version_source_path = runtime_version_source(repo_root, declaration)
    annotation = held_runtime_annotation(repo_root, declaration)
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
        "compatibility_posture": str(declaration["compatibility_posture"]),
        "compatibility_declaration_path": compatibility_declaration_rel_path(),
        "compatibility_declaration_schema_version": declaration["schema_version"],
        "runtime_basis": json.loads(json.dumps(declaration["runtime_basis"])),
        "runtime_held_annotations": json.loads(json.dumps(declaration["runtime_held_annotations"])),
        "observed_runtime_version": runtime_version,
        "observed_runtime_version_source": runtime_version_source_path,
        "observed_runtime_manifest_version": runtime_manifest_version,
        "observed_runtime_manifest_source": (
            declaration["runtime_basis"]["manifest_version_source"] if runtime_manifest_version else None
        ),
        "observed_runtime_version_aligned": aligned,
        "observed_runtime_version_set": sorted(set(observed_versions)),
        "held_runtime_annotation": annotation,
        "held_runtime_annotation_summary": held_runtime_annotation_summary(annotation),
        "declared_overlay_schema_version": declaration["overlay_schema_version"],
        "overlay_manifest_schema_version": overlay_manifest.get("schema_version"),
        "overlay_manifest_schema_version_matches_declaration": (
            overlay_manifest.get("schema_version") == declaration["overlay_schema_version"]
        ),
        "uplift_manifest_schema_version": int(declaration["uplift_manifest_schema_version"]),
        "upstream_compatibility_window": json.loads(json.dumps(declaration["upstream_compatibility_window"])),
        "parity_scan_baseline": {
            "target_runtime": declaration["parity_scan_baseline"]["target_runtime"],
            "rule_count": len(declaration["parity_scan_baseline"]["rules"]),
        },
        "check_protocol": list(declaration["check_protocol"]),
        "held_later": list(declaration["held_later"]),
    }


def compatibility_drift_reasons(previous: dict, current: dict) -> list[str]:
    reasons: list[str] = []
    fields = (
        ("compatibility_declaration_schema_version", "compatibility declaration schema version"),
        ("observed_runtime_version", "observed runtime version"),
        ("observed_runtime_manifest_version", "observed runtime manifest version"),
        ("observed_runtime_version_source", "observed runtime version source"),
        ("observed_runtime_manifest_source", "observed runtime manifest source"),
        ("observed_runtime_version_aligned", "runtime version alignment state"),
        ("declared_overlay_schema_version", "declared overlay schema version"),
        ("overlay_manifest_schema_version_matches_declaration", "overlay schema declaration alignment"),
    )
    for key, label in fields:
        before = previous.get(key)
        after = current.get(key)
        if before == after:
            continue
        before_text = "unrecorded" if before in (None, "") else str(before)
        after_text = "unrecorded" if after in (None, "") else str(after)
        reasons.append(f"{label} moved from {before_text} to {after_text}")
    before_annotation = previous.get("held_runtime_annotation")
    after_annotation = current.get("held_runtime_annotation")
    if before_annotation != after_annotation:
        before_text = held_runtime_annotation_summary(before_annotation) or "unrecorded"
        after_text = held_runtime_annotation_summary(after_annotation) or "unrecorded"
        reasons.append(f"held runtime annotation moved from {before_text} to {after_text}")
    object_fields = (
        ("runtime_basis", "declared runtime basis"),
        ("runtime_held_annotations", "declared runtime held annotations"),
        ("upstream_compatibility_window", "upstream compatibility window"),
        ("parity_scan_baseline", "parity scan baseline"),
    )
    for key, label in object_fields:
        if previous.get(key) != current.get(key):
            reasons.append(f"{label} changed")
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
        if pointer and " | " in pointer:
            pointer = [item.strip() for item in pointer.split(" | ") if item.strip()]
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
    pointer = entry.get("pointer")
    if isinstance(pointer, list):
        pointer_text = " | ".join(pointer)
    else:
        pointer_text = pointer
    if pointer_text:
        text += f": {pointer_text}"
    return text


def load_held_later_families(repo_root: pathlib.Path) -> list[dict]:
    held_later_path = held_later_rel_path()
    text = read_text(repo_root / held_later_path)
    if text is None:
        return [
            {
                "family": f"held-later reference missing: {held_later_path}",
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
    layout = phase_layout_policy()
    prefix = path.parent.name.split(str(layout["phase_name_delimiter"]), 1)[0]
    parts: list[tuple[int, int | str]] = []
    for piece in prefix.split(str(layout["phase_segment_delimiter"])):
        if piece.isdigit():
            parts.append((0, int(piece)))
        else:
            parts.append((1, piece))
    return tuple(parts)


def latest_phase_context_path(repo_root: pathlib.Path) -> pathlib.Path | None:
    phase_root = phase_root_path(repo_root)
    if not phase_root.exists():
        return None
    context_paths = list(phase_root.glob(phase_document_glob("context")))
    if not context_paths:
        return None
    return sorted(context_paths, key=phase_sort_key)[-1]


def has_rerun_boundary_marker(text: str) -> bool:
    return any(pattern.search(text) for pattern in _compiled_rerun_boundary_patterns())


def phase_boundary_signal(repo_root: pathlib.Path, active_phase: bool, doctrine_changed: bool) -> dict:
    if not active_phase:
        return {
            "context_path": None,
            "context_present": False,
            "rerun_boundary_marker_present": False,
            "mid_phase_signal": False,
            "note": phase_boundary_note("no_active_phase"),
        }

    context_path = latest_phase_context_path(repo_root)
    if context_path is None:
        return {
            "context_path": None,
            "context_present": False,
            "rerun_boundary_marker_present": False,
            "mid_phase_signal": False,
            "note": phase_boundary_note("active_phase_missing_context"),
        }

    text = read_text(context_path) or ""
    marker_present = has_rerun_boundary_marker(text)
    mid_phase_signal = marker_present or doctrine_changed
    if marker_present:
        note = phase_boundary_note("marker_present")
    elif doctrine_changed:
        note = phase_boundary_note("marker_missing_doctrine_changed")
    else:
        note = phase_boundary_note("marker_missing")
    return {
        "context_path": rel_path(repo_root, context_path),
        "context_present": True,
        "rerun_boundary_marker_present": marker_present,
        "mid_phase_signal": mid_phase_signal,
        "note": note,
    }


def build_runtime_agent_specs(repo_root: pathlib.Path) -> list[FileCarrierSpec]:
    registry = runtime_agent_registry_spec()
    agent_paths = sorted(
        repo_root.glob(registry.rel_path_glob),
        key=lambda path: rel_path(repo_root, path),
    )
    if not agent_paths:
        return []
    specs: list[FileCarrierSpec] = []
    for path in agent_paths:
        stem = path.stem
        specs.append(
            FileCarrierSpec(
                key=f"{registry.key_prefix}{stem}",
                group=registry.group,
                rel_path=rel_path(repo_root, path),
                label=f"{registry.label_prefix}{stem}",
                fingerprint_shape=registry.fingerprint_shape,
            )
        )
    return specs


def frontmatter_text(text: str) -> str | None:
    match = re.match(r"^---\n([\s\S]+?)\n---", text)
    if not match:
        return None
    return match.group(1).strip()


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


def inventory_items(text: str) -> list[str]:
    items = [
        match.group(1)
        for match in re.finditer(r"^- `([^`]+)`", text, re.M)
    ]
    return items


def parse_seed_contract_version(text: str | None) -> str | None:
    if text is None:
        return None
    match = re.search(r"^seed_contract_version:\s*(.+)$", text, re.M)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


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


def build_seed_corpus_posture(repo_root: pathlib.Path) -> dict:
    contract = seed_contract_policy()
    seed_dir_rel_path = str(contract["seed_dir_rel_path"])
    current_contract_version = str(contract["current_seed_contract_version"])
    required_frontmatter_keys = tuple(contract["required_seed_frontmatter_keys"])
    required_section_headings = tuple(contract["required_seed_section_headings"])
    seed_root = repo_root / seed_dir_rel_path
    seed_paths = sorted(seed_root.glob("SEED-*.md")) if seed_root.exists() else []
    current_contract_count = 0
    legacy_unversioned_count = 0
    noncurrent_version_counts: dict[str, int] = {}
    legacy_unversioned_examples: list[str] = []
    noncurrent_version_examples: list[dict] = []
    current_contract_shape_gap_count = 0
    current_contract_shape_gap_examples: list[dict] = []
    fingerprint_rows: list[str] = []

    for path in seed_paths:
        rel = rel_path(repo_root, path)
        text = read_text(path) or ""
        frontmatter = frontmatter_text(text)
        version = parse_seed_contract_version(frontmatter)
        if version is None:
            legacy_unversioned_count += 1
            if len(legacy_unversioned_examples) < 5:
                legacy_unversioned_examples.append(rel)
            fingerprint_rows.append(f"{rel}:legacy_unversioned")
            continue
        if version == current_contract_version:
            current_contract_count += 1
            frontmatter_map = parse_frontmatter_map(frontmatter)
            headings = extract_h2_headings(text)
            missing_frontmatter_keys = [
                key for key in required_frontmatter_keys if key not in frontmatter_map
            ]
            missing_section_headings = [
                heading for heading in required_section_headings if heading not in headings
            ]
            if missing_frontmatter_keys or missing_section_headings:
                current_contract_shape_gap_count += 1
                if len(current_contract_shape_gap_examples) < 5:
                    current_contract_shape_gap_examples.append(
                        {
                            "path": rel,
                            "missing_frontmatter_keys": missing_frontmatter_keys,
                            "missing_section_headings": missing_section_headings,
                        }
                    )
                fingerprint_rows.append(
                    f"{rel}:current:{version}:shape-gap:{','.join(missing_frontmatter_keys)}:{','.join(missing_section_headings)}"
                )
            else:
                fingerprint_rows.append(f"{rel}:current:{version}")
            continue
        noncurrent_version_counts[version] = noncurrent_version_counts.get(version, 0) + 1
        if len(noncurrent_version_examples) < 5:
            noncurrent_version_examples.append({"version": version, "path": rel})
        fingerprint_rows.append(f"{rel}:noncurrent:{version}")

    seed_file_count = len(seed_paths)
    noncurrent_version_total = sum(noncurrent_version_counts.values())
    migration_candidate_count = (
        legacy_unversioned_count
        + noncurrent_version_total
        + current_contract_shape_gap_count
    )
    if seed_file_count == 0:
        posture = "no_seed_corpus"
    elif legacy_unversioned_count == 0 and noncurrent_version_total == 0:
        posture = "current_contract_only"
    elif legacy_unversioned_count > 0 and current_contract_count == 0 and noncurrent_version_total == 0:
        posture = "legacy_unversioned_only"
    elif legacy_unversioned_count > 0 and noncurrent_version_total == 0:
        posture = "mixed_current_and_legacy_unversioned"
    elif legacy_unversioned_count == 0 and current_contract_count == 0:
        posture = "noncurrent_versions_only"
    else:
        posture = "mixed_with_noncurrent_versions"

    return {
        "seed_dir_present": seed_root.exists(),
        "seed_file_count": seed_file_count,
        "seed_dir_rel_path": seed_dir_rel_path,
        "current_contract_version": current_contract_version,
        "posture": posture,
        "current_contract_count": current_contract_count,
        "legacy_unversioned_count": legacy_unversioned_count,
        "noncurrent_version_total": noncurrent_version_total,
        "noncurrent_version_counts": dict(sorted(noncurrent_version_counts.items())),
        "legacy_unversioned_examples": legacy_unversioned_examples,
        "noncurrent_version_examples": noncurrent_version_examples,
        "current_contract_shape_gap_count": current_contract_shape_gap_count,
        "current_contract_shape_gap_examples": current_contract_shape_gap_examples,
        "migration_candidate_count": migration_candidate_count,
        "migration_candidate_breakdown": {
            "legacy_unversioned": legacy_unversioned_count,
            "noncurrent_version": noncurrent_version_total,
            "current_contract_shape_gap": current_contract_shape_gap_count,
        },
        "corpus_fingerprint": sha256_text("\n".join(fingerprint_rows)) if fingerprint_rows else None,
    }


def seed_corpus_needs_attention(seed_corpus_posture: dict) -> bool:
    return seed_corpus_posture.get("migration_candidate_count", 0) > 0


def seed_corpus_summary(seed_corpus_posture: dict) -> str:
    noncurrent = seed_corpus_posture["noncurrent_version_counts"]
    noncurrent_text = (
        ", ".join(f"v{version}={count}" for version, count in noncurrent.items())
        if noncurrent
        else "none"
    )
    return (
        f"{seed_corpus_posture['posture']} "
        f"(total {seed_corpus_posture['seed_file_count']}; "
        f"current {seed_corpus_posture['current_contract_count']}; "
        f"legacy {seed_corpus_posture['legacy_unversioned_count']}; "
        f"noncurrent {noncurrent_text}; "
        f"shape gaps {seed_corpus_posture.get('current_contract_shape_gap_count', 0)})"
    )


def seed_corpus_reasons(seed_corpus_posture: dict) -> list[str]:
    reasons: list[str] = []
    if seed_corpus_posture["legacy_unversioned_count"] > 0:
        reasons.append(
            f"legacy-unversioned seeds still present: {seed_corpus_posture['legacy_unversioned_count']}"
        )
    if seed_corpus_posture["noncurrent_version_total"] > 0:
        versions = ", ".join(
            f"v{version}={count}"
            for version, count in seed_corpus_posture["noncurrent_version_counts"].items()
        )
        reasons.append(f"noncurrent seed contract versions still present: {versions}")
    if seed_corpus_posture.get("current_contract_shape_gap_count", 0) > 0:
        reasons.append(
            "current-contract seed shape gaps still present: "
            f"{seed_corpus_posture['current_contract_shape_gap_count']}"
        )
    return reasons


def seed_migration_candidate_breakdown_text(seed_corpus_posture: dict) -> str:
    breakdown = seed_corpus_posture.get("migration_candidate_breakdown") or {}
    legacy = breakdown.get("legacy_unversioned", seed_corpus_posture.get("legacy_unversioned_count", 0))
    noncurrent = breakdown.get("noncurrent_version", seed_corpus_posture.get("noncurrent_version_total", 0))
    shape_gap = breakdown.get(
        "current_contract_shape_gap",
        seed_corpus_posture.get("current_contract_shape_gap_count", 0),
    )
    return f"legacy {legacy} / noncurrent {noncurrent} / shape-gap {shape_gap}"


def seed_corpus_drift_reasons(previous: dict, current: dict) -> list[str]:
    reasons: list[str] = []
    fields = (
        ("posture", "seed corpus posture"),
        ("seed_file_count", "seed file count"),
        ("current_contract_count", "current-contract seed count"),
        ("legacy_unversioned_count", "legacy-unversioned seed count"),
        ("noncurrent_version_counts", "noncurrent seed version counts"),
        ("current_contract_shape_gap_count", "current-contract seed shape-gap count"),
        ("migration_candidate_count", "seed migration candidate count"),
        ("migration_candidate_breakdown", "seed migration candidate breakdown"),
    )
    for key, label in fields:
        before = previous.get(key)
        after = current.get(key)
        if before == after:
            continue
        before_text = "none" if before in (None, "", [], {}) else json.dumps(before, sort_keys=True) if isinstance(before, dict) else str(before)
        after_text = "none" if after in (None, "", [], {}) else json.dumps(after, sort_keys=True) if isinstance(after, dict) else str(after)
        reasons.append(f"{label} moved from {before_text} to {after_text}")
    return reasons


def progress_note_seed_fields(seed_corpus_posture: dict | None) -> dict:
    if seed_corpus_posture is None:
        return {
            "show_seed_corpus_posture": False,
            "seed_corpus_posture": None,
            "seed_corpus_reasons": [],
            "show_seed_migration_pointer": False,
            "seed_migration_candidate_count": 0,
            "seed_migration_candidate_breakdown": None,
            "seed_migration_inspect_pointer": None,
            "seed_migration_write_pointer": None,
        }
    seed_file_count = seed_corpus_posture.get("seed_file_count", 0)
    show_seed_corpus_posture = seed_file_count > 0
    migration_candidate_count = seed_corpus_posture.get("migration_candidate_count", 0)
    show_seed_migration_pointer = show_seed_corpus_posture and migration_candidate_count > 0
    return {
        "show_seed_corpus_posture": show_seed_corpus_posture,
        "seed_corpus_posture": (
            seed_corpus_summary(seed_corpus_posture) if show_seed_corpus_posture else None
        ),
        "seed_corpus_reasons": (
            seed_corpus_reasons(seed_corpus_posture) if show_seed_corpus_posture else []
        ),
        "show_seed_migration_pointer": show_seed_migration_pointer,
        "seed_migration_candidate_count": migration_candidate_count,
        "seed_migration_candidate_breakdown": (
            seed_migration_candidate_breakdown_text(seed_corpus_posture)
            if show_seed_migration_pointer
            else None
        ),
        "seed_migration_inspect_pointer": (
            SEED_MIGRATION_SKILL_COMMAND if show_seed_migration_pointer else None
        ),
        "seed_migration_write_pointer": (
            SEED_MIGRATION_WRITE_COMMAND if show_seed_migration_pointer else None
        ),
    }


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
    seed_corpus_posture: dict,
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
    if seed_corpus_needs_attention(seed_corpus_posture):
        signals.append("legacy_seed_corpus")
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
    seed_corpus_posture: dict,
) -> str:
    if not planning_exists or not state_exists or not project_exists or not roadmap_exists:
        return "pre-uplift structural initialization"
    if any(runtime_dir != ".codex" for runtime_dir in runtime_dirs):
        return "cross-runtime uplift"
    if boundary_signal.get("mid_phase_signal"):
        return "mid-phase uplift"
    if not has_manifest and len(absent_additive) + len(pending_doctrine_sensitive) >= 5:
        return "vanilla uplift"
    if (
        doctrine_changed
        or absent_additive
        or pending_doctrine_sensitive
        or not has_manifest
        or seed_corpus_needs_attention(seed_corpus_posture)
    ):
        return "lightly aged uplift"
    return "current-aligned posture"


def recommendation_reasons(
    has_manifest: bool,
    doctrine_changed: bool,
    absent_additive: list[str],
    pending_doctrine_sensitive: list[dict],
    primary_class: str,
    seed_corpus_posture: dict,
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
    reasons.extend(seed_corpus_reasons(seed_corpus_posture))
    if primary_class == "mid-phase uplift":
        reasons.append("phase work is active, so uplift should stay detect-only and composition-first")
    return reasons


def analyze_repo(repo_root: pathlib.Path) -> dict:
    repo_root = repo_root.resolve()
    declaration = compatibility_policy()
    planning_root = repo_root / ".planning"
    manifest = load_manifest(repo_root)
    planning_exists = planning_root.exists()
    project_exists = (planning_root / "PROJECT.md").exists()
    roadmap_exists = (planning_root / "ROADMAP.md").exists()
    state_exists = (planning_root / "STATE.md").exists()
    runtime_dirs = runtime_dirs_present(repo_root)
    current_status = state_status(repo_root)
    plan_count = count_phase_files(repo_root, "plan")
    summary_count = count_phase_files(repo_root, "summary")
    active_phase = current_status.lower() not in {"completed", "unknown"} or plan_count > summary_count

    file_specs = file_carrier_specs() + build_runtime_agent_specs(repo_root)
    carriers = [build_file_carrier(repo_root, spec) for spec in file_specs]
    carriers.extend(build_marker_carrier(repo_root, spec) for spec in marker_carrier_specs())

    previous_manifest_present = manifest is not None
    doctrine_hash = doctrine_reference_hash(carriers)
    doctrine_changed = bool(manifest and manifest.get("doctrine_reference_hash") != doctrine_hash)
    boundary_signal = phase_boundary_signal(repo_root, active_phase, doctrine_changed)
    seed_corpus_posture = build_seed_corpus_posture(repo_root)
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
        seed_corpus_posture=seed_corpus_posture,
    )
    secondary = secondary_signals(
        primary_class=primary_class,
        runtime_dirs=runtime_dirs,
        boundary_signal=boundary_signal,
        doctrine_changed=doctrine_changed,
        pending_proposals=pending_doctrine_sensitive,
        seed_corpus_posture=seed_corpus_posture,
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
        seed_corpus_posture=seed_corpus_posture,
    )
    recommend_detect_only = bool(reasons) and primary_class != "current-aligned posture"
    held_later = load_held_later_families(repo_root)
    compatibility_basis = build_compatibility_basis(repo_root, declaration)
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
        "seed_corpus_posture": seed_corpus_posture,
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
        f"- Recommendation: {recommendation_text('report_detect_only') if analysis['recommend_detect_only'] else recommendation_text('report_continue')}",
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
        lines.append(f"- {recommendation_text('report_no_reasons')}")

    compatibility = analysis["compatibility_basis"]
    version_alignment = "aligned" if compatibility["observed_runtime_version_aligned"] else "split-or-partial"
    lines.extend(
        [
            "",
            "## Compatibility Basis",
            "",
            f"- Compatibility posture: {compatibility['compatibility_posture']}",
            f"- Compatibility declaration: {compatibility['compatibility_declaration_path']}",
            f"- Compatibility declaration schema version: {compatibility['compatibility_declaration_schema_version']}",
            f"- Declared runtime basis: {compatibility['runtime_basis']['runtime']} ({compatibility['runtime_basis']['basis_mode']})",
            f"- Observed runtime version: {compatibility['observed_runtime_version'] or 'unrecorded'}",
            f"- Observed runtime manifest version: {compatibility['observed_runtime_manifest_version'] or 'unrecorded'}",
            f"- Runtime version alignment: {version_alignment}",
            f"- Declared overlay schema version: {compatibility['declared_overlay_schema_version']}",
            f"- Overlay manifest schema version: {compatibility['overlay_manifest_schema_version'] or 'unrecorded'}",
            (
                "- Overlay schema declaration alignment: aligned"
                if compatibility["overlay_manifest_schema_version_matches_declaration"]
                else "- Overlay schema declaration alignment: moved"
            ),
            f"- Uplift manifest schema version: {compatibility['uplift_manifest_schema_version']}",
            f"- Upstream compatibility window: {compatibility['upstream_compatibility_window']['state']} ({compatibility['upstream_compatibility_window']['mode']})",
            f"- Parity scan baseline: {compatibility['parity_scan_baseline']['target_runtime']} ({compatibility['parity_scan_baseline']['rule_count']} rules)",
            "",
            "### Compatibility Check Protocol",
            "",
        ]
    )
    lines.extend(f"- {step}" for step in compatibility["check_protocol"])
    if compatibility["held_runtime_annotation"]:
        annotation = compatibility["held_runtime_annotation"]
        lines.extend(
            [
                "",
                "### Held Runtime Annotation",
                "",
                f"- Runtime: {annotation['runtime']}",
                f"- Held runtime version: {annotation['version']}",
                f"- Held runtime version source: {annotation['version_source']}",
                f"- Annotation posture: {annotation['annotation_posture']}",
                f"- Note: {annotation['note']}",
                "",
            ]
        )
    lines.extend(
        [
            "",
            "### Wider Compatibility Claims Held",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in compatibility["held_later"])
    seed_posture = analysis["seed_corpus_posture"]
    lines.extend(
        [
            "",
            "## Seed Corpus Posture",
            "",
            f"- Summary: {seed_corpus_summary(seed_posture)}",
            f"- Current contract version: {seed_posture['current_contract_version']}",
            f"- Legacy-unversioned examples: {', '.join(seed_posture['legacy_unversioned_examples']) if seed_posture['legacy_unversioned_examples'] else 'none'}",
            f"- Noncurrent-version examples: {json.dumps(seed_posture['noncurrent_version_examples'], sort_keys=True) if seed_posture['noncurrent_version_examples'] else 'none'}",
            "",
        ]
    )
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
        seed_corpus_posture=analysis["seed_corpus_posture"],
    )
    retained_secondary = secondary_signals(
        primary_class=analysis["project_class"],
        runtime_dirs=analysis["runtime_dirs"],
        boundary_signal=analysis["phase_boundary_signal"],
        doctrine_changed=False,
        pending_proposals=retained_pending,
        seed_corpus_posture=analysis["seed_corpus_posture"],
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


def build_state_section_values(analysis: dict) -> dict[str, str]:
    output_policy = uplift_output_policy_data()
    recommendation = (
        recommendation_text("state_detect_only")
        if analysis["recommend_detect_only"]
        else recommendation_text("state_continue")
    )
    pending_count = len(analysis["pending_doctrine_sensitive_proposals"])
    secondary = ", ".join(analysis["secondary_signals"]) if analysis["secondary_signals"] else "none"
    compatibility = analysis["compatibility_basis"]
    return {
        "last_uplift_pass": str(analysis["generated_at"]),
        "last_uplift_class": str(analysis["project_class"]),
        "last_uplift_secondary_signals": secondary,
        "phase_boundary_signal": str(analysis["phase_boundary_signal"]["note"]),
        "doctrine_reference_changed": "yes" if analysis["doctrine_reference_changed"] else "no",
        "compatibility_posture": str(compatibility["compatibility_posture"]),
        "compatibility_declaration": str(compatibility["compatibility_declaration_path"]),
        "observed_runtime_basis": (
            ", ".join(compatibility["observed_runtime_version_set"])
            if compatibility["observed_runtime_version_set"]
            else "unrecorded"
        ),
        "held_runtime_annotation": compatibility["held_runtime_annotation_summary"] or "none",
        "seed_corpus_posture": seed_corpus_summary(analysis["seed_corpus_posture"]),
        "pending_doctrine_sensitive_proposals": str(pending_count),
        "current_recommendation": recommendation,
        "current_uplift_report": str(output_policy["report_rel_path"]),
        "current_uplift_manifest": str(output_policy["manifest_rel_path"]),
    }


def state_section_text(analysis: dict) -> str:
    return uplift_state_writer.render_state_section(build_state_section_values(analysis))


def update_state_section(repo_root: pathlib.Path, analysis: dict) -> None:
    uplift_state_writer.write_state_section(repo_root, build_state_section_values(analysis))


def write_outputs(repo_root: pathlib.Path, analysis: dict) -> dict:
    output_policy = uplift_output_policy_data()
    planning_root = repo_root / ".planning"
    planning_root.mkdir(parents=True, exist_ok=True)
    written_analysis = post_write_analysis(analysis)
    report_path = repo_root / output_policy["report_rel_path"]
    manifest_path = repo_root / output_policy["manifest_rel_path"]
    report_path.write_text(render_report(written_analysis), encoding="utf-8")
    manifest_payload = {
        "schema_version": written_analysis["compatibility_basis"]["uplift_manifest_schema_version"],
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
        "seed_corpus_posture": written_analysis["seed_corpus_posture"],
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
    output_policy = uplift_output_policy_data()
    manifest = load_manifest(repo_root)
    if manifest is None:
        planning_root = repo_root / ".planning"
        show = planning_root.exists()
        analysis = analyze_repo(repo_root) if show else None
        seed_fields = progress_note_seed_fields(
            analysis["seed_corpus_posture"] if analysis is not None else None
        )
        return {
            "show": show,
            "manifest_present": False,
            "recommend_detect_only": show,
            "last_uplift_class": None,
            "last_uplift_secondary_signals": [],
            "held_runtime_annotation": (
                analysis["compatibility_basis"]["held_runtime_annotation_summary"] if analysis is not None else None
            ),
            "doctrine_reference_changed": False,
            "seed_corpus_basis_changed": False,
            "pending_doctrine_sensitive_proposals": [],
            "recommendation": recommendation_text("progress_no_manifest") if show else recommendation_text("progress_no_memory"),
            "reasons": ["no uplift manifest recorded yet"] if show else [],
            "report_path": output_policy["report_rel_path"],
            "manifest_path": output_policy["manifest_rel_path"],
            **seed_fields,
        }

    analysis = analyze_repo(repo_root)
    pending = analysis["pending_doctrine_sensitive_proposals"]
    doctrine_changed = manifest.get("doctrine_reference_hash") != analysis["doctrine_reference_hash"]
    manifest_compatibility = manifest.get("compatibility_basis") or {}
    current_compatibility = analysis["compatibility_basis"]
    compatibility_reasons = compatibility_drift_reasons(manifest_compatibility, current_compatibility)
    compatibility_basis_changed = bool(compatibility_reasons)
    manifest_seed_corpus = manifest.get("seed_corpus_posture") or {}
    current_seed_corpus = analysis["seed_corpus_posture"]
    seed_corpus_rewrite_reasons = seed_corpus_drift_reasons(manifest_seed_corpus, current_seed_corpus)
    seed_corpus_basis_changed = bool(seed_corpus_rewrite_reasons)
    seed_fields = progress_note_seed_fields(current_seed_corpus)
    recommend_write = compatibility_basis_changed or seed_corpus_basis_changed
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
    reasons.extend(seed_corpus_rewrite_reasons)
    recommendation = (
        recommendation_text("progress_write_refresh")
        if recommend_write
        else (
            recommendation_text("progress_detect_refresh")
            if recommend_detect_only
            else recommendation_text("progress_continue")
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
        "held_runtime_annotation": (
            manifest_compatibility.get("held_runtime_annotation_summary")
            or held_runtime_annotation_summary(manifest_compatibility.get("held_runtime_annotation"))
        ),
        "doctrine_reference_changed": doctrine_changed,
        "compatibility_basis_changed": compatibility_basis_changed,
        "seed_corpus_basis_changed": seed_corpus_basis_changed,
        "pending_doctrine_sensitive_proposals": pending,
        "recommendation": recommendation,
        "reasons": reasons,
        "report_path": output_policy["report_rel_path"],
        "manifest_path": output_policy["manifest_rel_path"],
        **seed_fields,
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
