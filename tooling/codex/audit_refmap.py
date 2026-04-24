#!/usr/bin/env python3

"""Map and rewrite local markdown references for audit-workspace migrations."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_POLICY_PATH = REPO_ROOT / ".planning" / "refmap" / "audit-refmap-policy.json"
POLICY_SCHEMA_VERSION = 1
ALLOWED_POLICY_CLASSIFICATIONS = frozenset(
    {
        "historical_external_origin",
        "intentionally_unimported_origin_artifact",
        "materialized_runtime_reference",
        "deferred_archive_gap",
    }
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
REPO_ROOT_ESCAPED = re.escape(str(REPO_ROOT))
LOCAL_PATH_RE = re.compile(
    r"(?P<path>"
    + REPO_ROOT_ESCAPED
    + r"/[^\s`\"'()<>]+"
    r"|(?:\.planning|tooling|scripts)/[^\s`\"'()<>]+"
    r")"
)
LINE_SUFFIX_RE = re.compile(r"^(.*?)(:\d+(?:-\d+)?)?$")
URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
DYNAMIC_TEMPLATE_RE = re.compile(r"\$\{[^}]+\}|\{[^}/]+\}")


@dataclass(frozen=True)
class Move:
    old_abs: str
    new_abs: str
    old_rel: str
    new_rel: str
    old_name: str


@dataclass(frozen=True)
class LinkOccurrence:
    source: str
    target_text: str
    line: int
    resolved: str | None
    status: str


@dataclass(frozen=True)
class PolicyEntry:
    source: str
    line: int
    raw_target: str
    resolved: str | None
    classification: str
    rationale: str
    reviewed_by: str


@dataclass(frozen=True)
class MoveIndex:
    by_old_abs: dict[str, Move]
    by_old_rel: dict[str, Move]
    by_old_name: dict[str, Move]
    by_new_abs: dict[str, Move]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Map local markdown references in an audit workspace and optionally "
            "rewrite them after a bounded move."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    map_parser = subparsers.add_parser("map", help="Summarize local markdown links.")
    map_parser.add_argument("root", help="Directory to scan.")
    map_parser.add_argument("--output", help="Write the markdown report here.")
    map_parser.add_argument("--policy", help="Policy JSON for classified missing links.")

    snapshot_parser = subparsers.add_parser(
        "snapshot",
        help="Emit a machine-readable JSON snapshot of the local markdown reference graph.",
    )
    snapshot_parser.add_argument("root", help="Directory to scan.")
    snapshot_parser.add_argument("--output", help="Write the JSON snapshot here.")
    snapshot_parser.add_argument("--policy", help="Policy JSON for classified missing links.")

    verify_parser = subparsers.add_parser(
        "verify",
        help="Scan local markdown links and fail if any local targets are missing.",
    )
    verify_parser.add_argument("root", help="Directory to scan.")
    verify_parser.add_argument("--output", help="Write the markdown report here.")
    verify_parser.add_argument("--policy", help="Policy JSON for classified missing links.")

    rewrite_parser = subparsers.add_parser(
        "rewrite",
        help="Rewrite references according to a TSV move manifest.",
    )
    rewrite_parser.add_argument("root", help="Directory whose markdown files should be rewritten.")
    rewrite_parser.add_argument(
        "--moves",
        required=True,
        help="TSV file with OLD_PATH<TAB>NEW_PATH rows.",
    )
    rewrite_parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes back to disk. Without this flag, only print a report.",
    )
    rewrite_parser.add_argument("--output", help="Write the markdown report here.")

    move_parser = subparsers.add_parser(
        "move",
        help=(
            "Apply a move manifest with git mv, rewrite local markdown references, "
            "and verify the workspace afterwards."
        ),
    )
    move_parser.add_argument("root", help="Directory whose markdown files should be rewritten.")
    move_parser.add_argument(
        "--moves",
        required=True,
        help="TSV file with OLD_PATH<TAB>NEW_PATH rows.",
    )
    move_parser.add_argument(
        "--skip-git-mv",
        action="store_true",
        help="Skip the git mv step and only rewrite/verify.",
    )
    move_parser.add_argument("--output", help="Write the markdown report here.")

    retire_parser = subparsers.add_parser(
        "retire",
        help=(
            "Retire one markdown artifact by optionally rewriting local references to "
            "a replacement and writing a tombstone in place."
        ),
    )
    retire_parser.add_argument("root", help="Directory whose markdown files should be rewritten.")
    retire_parser.add_argument(
        "--target",
        required=True,
        help="Repo-relative markdown file to retire.",
    )
    retire_parser.add_argument(
        "--replacement",
        help="Repo-relative replacement markdown file, if references should be redirected.",
    )
    retire_parser.add_argument(
        "--reason",
        help="Optional short reason recorded in the tombstone.",
    )
    retire_parser.add_argument("--output", help="Write the markdown report here.")

    return parser.parse_args()


def repo_relative(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def is_inside_repo(path: Path) -> bool:
    resolved = path.resolve()
    try:
        resolved.relative_to(REPO_ROOT)
        return True
    except ValueError:
        return False


def resolve_input_path(raw: str) -> Path:
    candidate = Path(raw)
    if candidate.is_absolute():
        return candidate.resolve()
    return (REPO_ROOT / raw).resolve()


def normalize_local_path(raw: str, source_file: Path) -> tuple[Path | None, str]:
    stripped = raw.strip()
    if not stripped:
        return None, ""
    if stripped.startswith("<") and stripped.endswith(">"):
        stripped = stripped[1:-1]

    path_part = stripped
    line_suffix = ""
    head, sep, tail = stripped.rpartition(":")
    if sep and re.fullmatch(r"\d+(?:-\d+)?", tail):
        path_part = head
        line_suffix = f":{tail}"

    if path_part.startswith("#") or URL_SCHEME_RE.match(path_part):
        return None, ""
    if DYNAMIC_TEMPLATE_RE.search(path_part):
        return None, ""

    if path_part.startswith("/"):
        candidate = Path(path_part).resolve()
        return candidate, line_suffix
    if path_part.startswith(".planning/") or path_part.startswith("tooling/") or path_part.startswith("scripts/"):
        return (REPO_ROOT / path_part).resolve(), line_suffix

    relative_candidate = (source_file.parent / path_part).resolve()
    if relative_candidate.exists():
        return relative_candidate, line_suffix
    if path_part.startswith("."):
        return relative_candidate, line_suffix

    repo_candidate = (REPO_ROOT / path_part).resolve()
    return repo_candidate, line_suffix


def format_target(raw_target: str, source_file: Path, destination: Path, line_suffix: str) -> str:
    stripped = raw_target.strip()
    had_brackets = stripped.startswith("<") and stripped.endswith(">")
    core = stripped[1:-1] if had_brackets else stripped

    if core.startswith("/"):
        rendered = destination.as_posix()
    elif core.startswith(".planning/") or core.startswith("tooling/") or core.startswith("scripts/"):
        rendered = repo_relative(destination)
    else:
        rendered = os.path.relpath(destination, start=source_file.parent).replace(os.sep, "/")
    rendered += line_suffix
    if had_brackets:
        return f"<{rendered}>"
    return rendered


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def collect_links(root: Path) -> list[LinkOccurrence]:
    links: list[LinkOccurrence] = []
    for source_file in iter_markdown_files(root):
        text = source_file.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target_text = match.group(2)
            line = text.count("\n", 0, match.start()) + 1
            resolved_path, _ = normalize_local_path(target_text, source_file)
            status = "external"
            resolved_rel: str | None = None
            if resolved_path is not None:
                if is_inside_repo(resolved_path):
                    resolved_rel = repo_relative(resolved_path)
                    if resolved_path.exists():
                        status = "local-existing"
                    else:
                        status = "local-missing"
                else:
                    resolved_rel = resolved_path.as_posix()
                    status = "external-absolute"
            links.append(
                LinkOccurrence(
                    source=repo_relative(source_file),
                    target_text=target_text,
                    line=line,
                    resolved=resolved_rel,
                    status=status,
                )
            )
    return links


def policy_key(link: LinkOccurrence) -> tuple[str, int, str, str | None]:
    return (link.source, link.line, link.target_text, link.resolved)


def entry_key(entry: PolicyEntry) -> tuple[str, int, str, str | None]:
    return (entry.source, entry.line, entry.raw_target, entry.resolved)


def load_policy(path: Path) -> dict[tuple[str, int, str, str | None], PolicyEntry]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("refmap policy must be a JSON object")
    if payload.get("schema_version") != POLICY_SCHEMA_VERSION:
        raise ValueError(f"refmap policy schema_version must be {POLICY_SCHEMA_VERSION}")
    raw_entries = payload.get("entries")
    if not isinstance(raw_entries, list):
        raise ValueError("refmap policy entries must be an array")
    raw_counts = payload.get("classification_counts", {})
    if raw_counts is not None and not isinstance(raw_counts, dict):
        raise ValueError("refmap policy classification_counts must be an object when present")

    entries: dict[tuple[str, int, str, str | None], PolicyEntry] = {}
    classification_counts: Counter[str] = Counter()
    for index, raw_entry in enumerate(raw_entries):
        if not isinstance(raw_entry, dict):
            raise ValueError(f"refmap policy entry {index} must be an object")
        entry = PolicyEntry(
            source=str(raw_entry["source"]),
            line=int(raw_entry["line"]),
            raw_target=str(raw_entry["raw_target"]),
            resolved=None if raw_entry.get("resolved") is None else str(raw_entry["resolved"]),
            classification=str(raw_entry["classification"]),
            rationale=str(raw_entry["rationale"]),
            reviewed_by=str(raw_entry["reviewed_by"]),
        )
        if entry.classification not in ALLOWED_POLICY_CLASSIFICATIONS:
            raise ValueError(
                f"refmap policy entry {index} has unsupported classification: {entry.classification}"
            )
        key = entry_key(entry)
        if key in entries:
            raise ValueError(f"duplicate refmap policy entry for {entry.source}:{entry.line}")
        entries[key] = entry
        classification_counts[entry.classification] += 1
    if raw_counts:
        declared_counts = {str(key): int(value) for key, value in raw_counts.items()}
        actual_counts = dict(sorted(classification_counts.items()))
        if declared_counts != actual_counts:
            raise ValueError(
                "refmap policy classification_counts do not match entries: "
                f"declared={declared_counts} actual={actual_counts}"
            )
    return entries


def default_policy_for(root: Path) -> dict[tuple[str, int, str, str | None], PolicyEntry] | None:
    if root.resolve() == REPO_ROOT and DEFAULT_POLICY_PATH.exists():
        return load_policy(DEFAULT_POLICY_PATH)
    return None


def load_cli_policy(root: Path, raw_policy: str | None) -> dict[tuple[str, int, str, str | None], PolicyEntry] | None:
    if raw_policy:
        return load_policy(resolve_input_path(raw_policy))
    return default_policy_for(root)


def split_missing_links(
    links: list[LinkOccurrence],
    policy: dict[tuple[str, int, str, str | None], PolicyEntry] | None = None,
) -> tuple[list[LinkOccurrence], list[tuple[LinkOccurrence, PolicyEntry]]]:
    policy = policy or {}
    unclassified: list[LinkOccurrence] = []
    classified: list[tuple[LinkOccurrence, PolicyEntry]] = []
    for link in links:
        if link.status != "local-missing":
            continue
        entry = policy.get(policy_key(link))
        if entry is None:
            unclassified.append(link)
        else:
            classified.append((link, entry))
    return unclassified, classified


def render_map_report(
    root: Path,
    links: list[LinkOccurrence],
    policy: dict[tuple[str, int, str, str | None], PolicyEntry] | None = None,
) -> str:
    local_links = [link for link in links if link.status.startswith("local-")]
    local_existing = [link for link in local_links if link.status == "local-existing"]
    local_missing = [link for link in local_links if link.status == "local-missing"]
    unclassified_missing, classified_missing = split_missing_links(links, policy)
    inbound_counter: Counter[str] = Counter()
    outbound_counter: Counter[str] = Counter()
    source_to_missing: dict[str, list[LinkOccurrence]] = defaultdict(list)
    source_to_classified: dict[str, list[tuple[LinkOccurrence, PolicyEntry]]] = defaultdict(list)
    classified_counter: Counter[str] = Counter()

    for link in local_existing:
        assert link.resolved is not None
        inbound_counter[link.resolved] += 1
        outbound_counter[link.source] += 1
    for link in unclassified_missing:
        source_to_missing[link.source].append(link)
    for link, entry in classified_missing:
        source_to_classified[link.source].append((link, entry))
        classified_counter[entry.classification] += 1

    lines = [
        "# Audit Reference Map",
        "",
        f"- Root: `{repo_relative(root)}`",
        f"- Markdown files scanned: `{len(iter_markdown_files(root))}`",
        f"- Markdown links scanned: `{len(links)}`",
        f"- Local existing links: `{len(local_existing)}`",
        f"- Local missing links: `{len(local_missing)}`",
        f"- Classified missing links: `{len(classified_missing)}`",
        f"- Unclassified missing links: `{len(unclassified_missing)}`",
        "",
        "## Top Inbound Targets",
        "",
    ]
    for path, count in inbound_counter.most_common(15):
        lines.append(f"- `{path}` <- `{count}` inbound links")
    if not inbound_counter:
        lines.append("- none")

    lines.extend(["", "## Top Outbound Sources", ""])
    for path, count in outbound_counter.most_common(15):
        lines.append(f"- `{path}` -> `{count}` local links")
    if not outbound_counter:
        lines.append("- none")

    lines.extend(["", "## Unclassified Missing Local Targets", ""])
    if not source_to_missing:
        lines.append("- none")
    else:
        for source, missing_links in sorted(source_to_missing.items()):
            lines.append(f"- `{source}`")
            for link in missing_links:
                lines.append(
                    f"  - line `{link.line}` -> `{link.target_text}`"
                )
    lines.extend(["", "## Classified Missing Local Targets", ""])
    if not source_to_classified:
        lines.append("- none")
    else:
        for classification, count in sorted(classified_counter.items()):
            lines.append(f"- `{classification}`: `{count}`")
        lines.append("")
        for source, classified_links in sorted(source_to_classified.items()):
            lines.append(f"- `{source}`")
            for link, entry in classified_links:
                lines.append(
                    f"  - line `{link.line}` -> `{link.target_text}` "
                    f"(`{entry.classification}`)"
                )
    return "\n".join(lines) + "\n"


def missing_local_links(
    links: list[LinkOccurrence],
    policy: dict[tuple[str, int, str, str | None], PolicyEntry] | None = None,
) -> list[LinkOccurrence]:
    return split_missing_links(links, policy)[0]


def build_snapshot(
    root: Path,
    links: list[LinkOccurrence],
    policy: dict[tuple[str, int, str, str | None], PolicyEntry] | None = None,
) -> dict[str, object]:
    markdown_files = iter_markdown_files(root)
    inbound_counter: Counter[str] = Counter()
    outbound_counter: Counter[str] = Counter()
    local_edges: list[dict[str, object]] = []
    external_links: list[dict[str, object]] = []
    missing_links: list[dict[str, object]] = []
    classified_missing_links: list[dict[str, object]] = []
    unclassified_missing_links: list[dict[str, object]] = []
    policy = policy or {}

    for link in links:
        if link.status == "local-existing":
            assert link.resolved is not None
            inbound_counter[link.resolved] += 1
            outbound_counter[link.source] += 1
            local_edges.append(
                {
                    "source": link.source,
                    "target": link.resolved,
                    "line": link.line,
                    "raw_target": link.target_text,
                }
            )
        elif link.status == "local-missing":
            row = {
                "source": link.source,
                "line": link.line,
                "raw_target": link.target_text,
                "resolved": link.resolved,
            }
            entry = policy.get(policy_key(link))
            if entry is None:
                unclassified_missing_links.append(row)
            else:
                classified_row = dict(row)
                classified_row["classification"] = entry.classification
                classified_row["rationale"] = entry.rationale
                classified_row["reviewed_by"] = entry.reviewed_by
                classified_missing_links.append(classified_row)
            missing_links.append(row)
        else:
            row = {
                "source": link.source,
                "line": link.line,
                "raw_target": link.target_text,
                "status": link.status,
            }
            if link.resolved is not None:
                row["resolved"] = link.resolved
            external_links.append(row)

    return {
        "root": repo_relative(root),
        "markdown_files": [repo_relative(path) for path in markdown_files],
        "stats": {
            "markdown_files": len(markdown_files),
            "links_scanned": len(links),
            "local_existing_links": len(local_edges),
            "local_missing_links": len(missing_links),
            "classified_missing_links": len(classified_missing_links),
            "unclassified_missing_links": len(unclassified_missing_links),
            "external_links": len(external_links),
        },
        "inbound_counts": dict(sorted(inbound_counter.items())),
        "outbound_counts": dict(sorted(outbound_counter.items())),
        "local_edges": local_edges,
        "external_links": external_links,
        "missing_links": missing_links,
        "classified_missing_links": classified_missing_links,
        "unclassified_missing_links": unclassified_missing_links,
    }


def load_moves(path: Path) -> list[Move]:
    moves: list[Move] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        old_raw, new_raw = stripped.split("\t", 1)
        old_path = Path(old_raw)
        new_path = Path(new_raw)
        old_abs = old_path.resolve() if old_path.is_absolute() else (REPO_ROOT / old_path).resolve()
        new_abs = new_path.resolve() if new_path.is_absolute() else (REPO_ROOT / new_path).resolve()
        moves.append(
            Move(
                old_abs=old_abs.as_posix(),
                new_abs=new_abs.as_posix(),
                old_rel=old_raw,
                new_rel=new_raw,
                old_name=Path(old_raw).name,
            )
        )
    return moves


def build_move_index(moves: list[Move]) -> MoveIndex:
    by_old_abs: dict[str, Move] = {}
    by_old_rel: dict[str, Move] = {}
    by_new_abs: dict[str, Move] = {}
    moves_by_old_name: dict[str, list[Move]] = defaultdict(list)

    for move in moves:
        by_old_abs[move.old_abs] = move
        by_old_rel[move.old_rel] = move
        by_new_abs[move.new_abs] = move
        try:
            by_old_rel[repo_relative(Path(move.old_abs))] = move
        except RuntimeError:
            pass
        moves_by_old_name[move.old_name].append(move)

    by_old_name: dict[str, Move] = {}
    for old_name, named_moves in moves_by_old_name.items():
        new_targets = {move.new_abs for move in named_moves}
        if len(new_targets) == 1:
            by_old_name[old_name] = named_moves[0]

    return MoveIndex(
        by_old_abs=by_old_abs,
        by_old_rel=by_old_rel,
        by_old_name=by_old_name,
        by_new_abs=by_new_abs,
    )


def find_target_move(
    raw_target: str,
    source_file: Path,
    move_index: MoveIndex,
) -> tuple[Move | None, str]:
    stripped = raw_target.strip()
    had_brackets = stripped.startswith("<") and stripped.endswith(">")
    core = stripped[1:-1] if had_brackets else stripped
    line_match = LINE_SUFFIX_RE.match(core)
    assert line_match is not None
    target_core = line_match.group(1)
    resolved_path, line_suffix = normalize_local_path(raw_target, source_file)
    move: Move | None = None
    if resolved_path is not None:
        move = move_index.by_old_abs.get(resolved_path.as_posix())
        if move is None:
            move = move_index.by_old_rel.get(repo_relative(resolved_path))
    if move is None:
        move = move_index.by_old_rel.get(target_core)
    if move is None and "/" not in target_core:
        move = move_index.by_old_name.get(target_core)
    return move, line_suffix


def rewrite_links(
    text: str,
    source_file: Path,
    move_index: MoveIndex,
) -> tuple[str, int]:
    replacements = 0
    source_move = move_index.by_new_abs.get(source_file.resolve().as_posix())

    def repl(match: re.Match[str]) -> str:
        nonlocal replacements
        label, raw_target = match.group(1), match.group(2)
        move, line_suffix = find_target_move(raw_target, source_file, move_index)
        destination: Path | None = Path(move.new_abs) if move is not None else None

        if destination is None and source_move is not None:
            old_source = Path(source_move.old_abs)
            old_resolved_path, line_suffix = normalize_local_path(raw_target, old_source)
            if old_resolved_path is not None:
                old_target_move = move_index.by_old_abs.get(old_resolved_path.as_posix())
                if old_target_move is None:
                    old_target_move = move_index.by_old_rel.get(repo_relative(old_resolved_path))
                if old_target_move is not None:
                    destination = Path(old_target_move.new_abs)
                elif old_resolved_path.exists():
                    destination = old_resolved_path

        if destination is None:
            return match.group(0)
        replacements += 1
        rewritten = format_target(raw_target, source_file, destination, line_suffix)
        return f"[{label}]({rewritten})"

    return MARKDOWN_LINK_RE.sub(repl, text), replacements


def rewrite_literal_paths(text: str, source_file: Path, moves: list[Move]) -> tuple[str, int]:
    updated = text
    replacements = 0

    def replace_if_present(old: str, new: str) -> None:
        nonlocal updated, replacements
        count = updated.count(old)
        if count:
            updated = updated.replace(old, new)
            replacements += count

    for move in sorted(moves, key=lambda item: len(item.old_abs), reverse=True):
        replace_if_present(move.old_abs, move.new_abs)
        if "/" in move.old_rel or move.old_rel.startswith("."):
            replace_if_present(move.old_rel, move.new_rel)

        rendered_rel = os.path.relpath(Path(move.new_abs), start=source_file.parent).replace(os.sep, "/")
        replace_if_present(f"`{move.old_name}`", f"`{rendered_rel}`")

    return updated, replacements


def rewrite_workspace(root: Path, moves: list[Move], apply: bool) -> str:
    move_index = build_move_index(moves)
    changed_files: list[tuple[str, int]] = []

    for source_file in iter_markdown_files(root):
        original = source_file.read_text(encoding="utf-8")
        updated, link_replacements = rewrite_links(
            original,
            source_file,
            move_index,
        )
        updated, literal_replacements = rewrite_literal_paths(updated, source_file, moves)
        replacement_count = link_replacements + literal_replacements
        if updated == original:
            continue
        changed_files.append((repo_relative(source_file), replacement_count))
        if apply:
            source_file.write_text(updated, encoding="utf-8")

    lines = [
        "# Audit Reference Rewrite Report",
        "",
        f"- Root: `{repo_relative(root)}`",
        f"- Move entries: `{len(moves)}`",
        f"- Mode: `{'apply' if apply else 'dry-run'}`",
        f"- Changed markdown files: `{len(changed_files)}`",
        "",
        "## Changed Files",
        "",
    ]
    if not changed_files:
        lines.append("- none")
    else:
        for path, count in changed_files:
            lines.append(f"- `{path}` -> `{count}` textual rewrites")
    return "\n".join(lines) + "\n"


def apply_git_moves(moves: list[Move]) -> tuple[int, int]:
    moved = 0
    skipped = 0
    for move in moves:
        old_path = Path(move.old_abs)
        new_path = Path(move.new_abs)
        if not old_path.exists():
            skipped += 1
            continue
        new_path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "mv", move.old_rel, move.new_rel],
            cwd=REPO_ROOT,
            check=True,
        )
        moved += 1
    return moved, skipped


def execute_move(root: Path, moves: list[Move], skip_git_mv: bool) -> str:
    moved = 0
    skipped = 0
    if not skip_git_mv:
        moved, skipped = apply_git_moves(moves)

    rewrite_report = rewrite_workspace(root, moves, apply=True)
    links = collect_links(root)
    missing = missing_local_links(links)

    lines = [
        "# Audit Move Report",
        "",
        f"- Root: `{repo_relative(root)}`",
        f"- Move entries: `{len(moves)}`",
        f"- Git mv mode: `{'skipped' if skip_git_mv else 'applied'}`",
        f"- Files moved by git: `{moved}`",
        f"- Move rows skipped because the old path was absent: `{skipped}`",
        f"- Post-move missing local links: `{len(missing)}`",
        "",
        "## Rewrite Pass",
        "",
        rewrite_report.strip(),
        "",
        "## Verify Pass",
        "",
    ]
    if not missing:
        lines.append("- no missing local links")
    else:
        for link in missing:
            lines.append(f"- `{link.source}` line `{link.line}` -> `{link.target_text}`")
    return "\n".join(lines) + "\n"


def build_tombstone(target: Path, replacement: Path | None, reason: str | None) -> str:
    lines = [
        f"# Retired: {target.name}",
        "",
        "Status: retired artifact",
        f"Date: {date.today().isoformat()}",
        "",
        "## Disposition",
        "",
    ]
    if replacement is not None:
        relative = os.path.relpath(replacement, start=target.parent).replace(os.sep, "/")
        lines.append(
            f"- This artifact has been retired and replaced by [{replacement.name}]({relative})."
        )
    else:
        lines.append("- This artifact has been retired without a direct replacement.")
    if reason:
        lines.append(f"- Reason: {reason}")
    lines.extend(
        [
            "",
            "## Note",
            "",
            "- Historical references should treat this file as a tombstone rather than an active source of truth.",
            "",
        ]
    )
    return "\n".join(lines)


def execute_retire(
    root: Path,
    target_rel: str,
    replacement_rel: str | None,
    reason: str | None,
) -> str:
    target = resolve_input_path(target_rel)
    if not target.exists():
        raise SystemExit(f"Retire target not found: {target_rel}")
    if target.suffix.lower() != ".md":
        raise SystemExit("Retire currently supports markdown targets only.")

    replacement_path: Path | None = None
    rewrite_report = ""
    if replacement_rel:
        replacement_path = resolve_input_path(replacement_rel)
        if not replacement_path.exists():
            raise SystemExit(f"Replacement not found: {replacement_rel}")
        synthetic_move = Move(
            old_abs=target.as_posix(),
            new_abs=replacement_path.as_posix(),
            old_rel=target_rel,
            new_rel=replacement_rel,
            old_name=target.name,
        )
        rewrite_report = rewrite_workspace(root, [synthetic_move], apply=True).strip()

    target.write_text(
        build_tombstone(target, replacement_path, reason),
        encoding="utf-8",
    )

    links = collect_links(root)
    missing = missing_local_links(links)
    lines = [
        "# Audit Retire Report",
        "",
        f"- Root: `{repo_relative(root)}`",
        f"- Target: `{target_rel}`",
        f"- Replacement: `{replacement_rel or '-'}`",
        f"- Post-retire missing local links: `{len(missing)}`",
        "",
    ]
    if rewrite_report:
        lines.extend(["## Rewrite Pass", "", rewrite_report, ""])
    lines.extend(["## Verify Pass", ""])
    if not missing:
        lines.append("- no missing local links")
    else:
        for link in missing:
            lines.append(f"- `{link.source}` line `{link.line}` -> `{link.target_text}`")
    return "\n".join(lines) + "\n"


def write_output(text: str, output: str | None) -> None:
    if output:
        Path(output).write_text(text, encoding="utf-8")
        return
    sys.stdout.write(text)


def main() -> int:
    args = parse_args()
    root = (REPO_ROOT / args.root).resolve() if not Path(args.root).is_absolute() else Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Root not found: {root}")

    if args.command == "map":
        policy = load_cli_policy(root, args.policy)
        report = render_map_report(root, collect_links(root), policy)
        write_output(report, args.output)
        return 0

    if args.command == "snapshot":
        policy = load_cli_policy(root, args.policy)
        snapshot = build_snapshot(root, collect_links(root), policy)
        write_output(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", args.output)
        return 0

    if args.command == "verify":
        policy = load_cli_policy(root, args.policy)
        links = collect_links(root)
        report = render_map_report(root, links, policy)
        write_output(report, args.output)
        return 1 if missing_local_links(links, policy) else 0

    if args.command == "retire":
        report = execute_retire(root, args.target, args.replacement, args.reason)
        write_output(report, args.output)
        return 0

    moves = load_moves(Path(args.moves))
    if args.command == "rewrite":
        report = rewrite_workspace(root, moves, args.apply)
        write_output(report, args.output)
        return 0

    report = execute_move(root, moves, args.skip_git_mv)
    write_output(report, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
