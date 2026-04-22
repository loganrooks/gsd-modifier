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
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LOCAL_PATH_RE = re.compile(
    r"(?P<path>"
    r"/home/rookslog/workspace/projects/prix-guesser/[^\s`\"'()<>]+"
    r"|(?:\.planning|tooling|scripts)/[^\s`\"'()<>]+"
    r")"
)
LINE_SUFFIX_RE = re.compile(r"^(.*?)(:\d+)?$")
URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


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

    snapshot_parser = subparsers.add_parser(
        "snapshot",
        help="Emit a machine-readable JSON snapshot of the local markdown reference graph.",
    )
    snapshot_parser.add_argument("root", help="Directory to scan.")
    snapshot_parser.add_argument("--output", help="Write the JSON snapshot here.")

    verify_parser = subparsers.add_parser(
        "verify",
        help="Scan local markdown links and fail if any local targets are missing.",
    )
    verify_parser.add_argument("root", help="Directory to scan.")
    verify_parser.add_argument("--output", help="Write the markdown report here.")

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
    if stripped.startswith("#") or URL_SCHEME_RE.match(stripped):
        return None, ""

    path_part = stripped
    line_suffix = ""
    head, sep, tail = stripped.rpartition(":")
    if sep and tail.isdigit():
        path_part = head
        line_suffix = f":{tail}"

    if path_part.startswith("/"):
        candidate = Path(path_part).resolve()
        return candidate, line_suffix

    relative_candidate = (source_file.parent / path_part).resolve()
    if relative_candidate.exists():
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
                try:
                    resolved_rel = repo_relative(resolved_path)
                except ValueError:
                    resolved_rel = resolved_path.as_posix()
                if resolved_path.exists():
                    status = "local-existing"
                else:
                    status = "local-missing"
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


def render_map_report(root: Path, links: list[LinkOccurrence]) -> str:
    local_links = [link for link in links if link.status.startswith("local-")]
    local_existing = [link for link in local_links if link.status == "local-existing"]
    local_missing = [link for link in local_links if link.status == "local-missing"]
    inbound_counter: Counter[str] = Counter()
    outbound_counter: Counter[str] = Counter()
    source_to_missing: dict[str, list[LinkOccurrence]] = defaultdict(list)

    for link in local_existing:
        assert link.resolved is not None
        inbound_counter[link.resolved] += 1
        outbound_counter[link.source] += 1
    for link in local_missing:
        source_to_missing[link.source].append(link)

    lines = [
        "# Audit Reference Map",
        "",
        f"- Root: `{repo_relative(root)}`",
        f"- Markdown files scanned: `{len(iter_markdown_files(root))}`",
        f"- Markdown links scanned: `{len(links)}`",
        f"- Local existing links: `{len(local_existing)}`",
        f"- Local missing links: `{len(local_missing)}`",
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

    lines.extend(["", "## Missing Local Targets", ""])
    if not source_to_missing:
        lines.append("- none")
    else:
        for source, missing_links in sorted(source_to_missing.items()):
            lines.append(f"- `{source}`")
            for link in missing_links:
                lines.append(
                    f"  - line `{link.line}` -> `{link.target_text}`"
                )
    return "\n".join(lines) + "\n"


def missing_local_links(links: list[LinkOccurrence]) -> list[LinkOccurrence]:
    return [link for link in links if link.status == "local-missing"]


def build_snapshot(root: Path, links: list[LinkOccurrence]) -> dict[str, object]:
    markdown_files = iter_markdown_files(root)
    inbound_counter: Counter[str] = Counter()
    outbound_counter: Counter[str] = Counter()
    local_edges: list[dict[str, object]] = []
    external_links: list[dict[str, object]] = []
    missing_links: list[dict[str, object]] = []

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
            missing_links.append(
                {
                    "source": link.source,
                    "line": link.line,
                    "raw_target": link.target_text,
                    "resolved": link.resolved,
                }
            )
        else:
            external_links.append(
                {
                    "source": link.source,
                    "line": link.line,
                    "raw_target": link.target_text,
                }
            )

    return {
        "root": repo_relative(root),
        "markdown_files": [repo_relative(path) for path in markdown_files],
        "stats": {
            "markdown_files": len(markdown_files),
            "links_scanned": len(links),
            "local_existing_links": len(local_edges),
            "local_missing_links": len(missing_links),
            "external_links": len(external_links),
        },
        "inbound_counts": dict(sorted(inbound_counter.items())),
        "outbound_counts": dict(sorted(outbound_counter.items())),
        "local_edges": local_edges,
        "external_links": external_links,
        "missing_links": missing_links,
    }


def load_moves(path: Path) -> list[Move]:
    moves: list[Move] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        old_raw, new_raw = stripped.split("\t", 1)
        old_abs = (REPO_ROOT / old_raw).resolve()
        new_abs = (REPO_ROOT / new_raw).resolve()
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


def rewrite_links(
    text: str,
    source_file: Path,
    move_by_old_abs: dict[str, Move],
    move_by_old_rel: dict[str, Move],
    move_by_old_name: dict[str, Move],
) -> tuple[str, int]:
    replacements = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal replacements
        label, raw_target = match.group(1), match.group(2)
        stripped = raw_target.strip()
        had_brackets = stripped.startswith("<") and stripped.endswith(">")
        core = stripped[1:-1] if had_brackets else stripped
        line_match = LINE_SUFFIX_RE.match(core)
        assert line_match is not None
        target_core = line_match.group(1)
        resolved_path, line_suffix = normalize_local_path(raw_target, source_file)
        move: Move | None = None
        if resolved_path is not None:
            move = move_by_old_abs.get(resolved_path.as_posix())
        if move is None:
            move = move_by_old_rel.get(target_core)
        if move is None and "/" not in target_core:
            move = move_by_old_name.get(target_core)
        if move is None:
            return match.group(0)
        replacements += 1
        rewritten = format_target(raw_target, source_file, Path(move.new_abs), line_suffix)
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
        replace_if_present(move.old_rel, move.new_rel)

        rendered_rel = os.path.relpath(Path(move.new_abs), start=source_file.parent).replace(os.sep, "/")
        replace_if_present(f"`{move.old_name}`", f"`{rendered_rel}`")

    return updated, replacements


def rewrite_workspace(root: Path, moves: list[Move], apply: bool) -> str:
    move_by_old_abs = {move.old_abs: move for move in moves}
    move_by_old_rel = {move.old_rel: move for move in moves}
    basename_counter = Counter(move.old_name for move in moves)
    move_by_old_name = {
        move.old_name: move for move in moves if basename_counter[move.old_name] == 1
    }
    changed_files: list[tuple[str, int]] = []

    for source_file in iter_markdown_files(root):
        original = source_file.read_text(encoding="utf-8")
        updated, link_replacements = rewrite_links(
            original,
            source_file,
            move_by_old_abs,
            move_by_old_rel,
            move_by_old_name,
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
        report = render_map_report(root, collect_links(root))
        write_output(report, args.output)
        return 0

    if args.command == "snapshot":
        snapshot = build_snapshot(root, collect_links(root))
        write_output(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", args.output)
        return 0

    if args.command == "verify":
        links = collect_links(root)
        report = render_map_report(root, links)
        write_output(report, args.output)
        return 1 if missing_local_links(links) else 0

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
