#!/usr/bin/env python3

"""Capture requested-versus-effective Codex launch truth from state_5.sqlite."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


DEFAULT_DB_PATH = Path.home() / ".codex" / "state_5.sqlite"
KNOWN_SANDBOX_TYPES = {
    "danger-full-access",
    "read-only",
    "workspace-write",
}


@dataclass
class RequestedSettings:
    model: str | None
    reasoning_effort: str | None
    approval_mode: str | None
    sandbox_policy: str | None
    agent: str | None
    agent_path: str | None

    def as_rows(self) -> list[tuple[str, str]]:
        rows = [
            ("model", self.model),
            ("reasoning_effort", self.reasoning_effort),
            ("approval_mode", self.approval_mode),
            ("sandbox_policy", self.sandbox_policy),
            ("requested_agent", self.agent),
            ("requested_agent_path", self.agent_path),
        ]
        return [(label, value) for label, value in rows if value]

    def has_comparison_inputs(self) -> bool:
        return bool(self.as_rows())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Capture requested-versus-effective worker launch settings from "
            "~/.codex/state_5.sqlite into a reviewable markdown artifact."
        )
    )
    boundary_group = parser.add_mutually_exclusive_group(required=True)
    boundary_group.add_argument(
        "--since",
        help=(
            "Capture worker threads created at or after this boundary. Accepts "
            "unix seconds or an ISO-8601 timestamp."
        ),
    )
    boundary_group.add_argument(
        "--latest",
        type=int,
        help=(
            "Capture the latest N worker threads. Use only when you did not "
            "record a stronger pre-spawn boundary."
        ),
    )
    parser.add_argument(
        "--label",
        required=True,
        help="Short human label for the launch being captured.",
    )
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB_PATH),
        help="Path to the Codex sqlite state database.",
    )
    parser.add_argument("--requested-model")
    parser.add_argument("--requested-reasoning")
    parser.add_argument("--requested-approval")
    parser.add_argument(
        "--requested-sandbox",
        help=(
            "Requested sandbox policy. Shorthand values such as "
            "'danger-full-access' are accepted."
        ),
    )
    parser.add_argument(
        "--requested-agent",
        help="Named agent or role that the operator intended to launch.",
    )
    parser.add_argument(
        "--requested-agent-path",
        help="Requested agent config path, if the launch depended on a specific file.",
    )
    parser.add_argument(
        "--include-non-worker",
        action="store_true",
        help="Do not filter the capture to threads whose agent_role is 'worker'.",
    )
    parser.add_argument(
        "--output",
        help="Write markdown output to this path instead of stdout.",
    )
    args = parser.parse_args()
    if args.latest is not None and args.latest < 1:
        parser.error("--latest must be at least 1")
    return args


def parse_boundary(value: str) -> int:
    stripped = value.strip()
    if stripped.isdigit():
        return int(stripped)

    try:
        if stripped.endswith("Z"):
            stripped = stripped[:-1] + "+00:00"
        parsed = datetime.fromisoformat(stripped)
    except ValueError as exc:
        raise SystemExit(
            "--since must be unix seconds or an ISO-8601 timestamp"
        ) from exc

    if parsed.tzinfo is None:
        parsed = parsed.astimezone()

    return int(parsed.timestamp())


def normalize_sandbox(raw_value: str | None) -> tuple[str | None, str | None]:
    if raw_value is None:
        return None, None

    value = raw_value.strip()
    if not value:
        return None, None

    if value in KNOWN_SANDBOX_TYPES:
        return value, json.dumps({"type": value}, sort_keys=True)

    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return value, value

    if isinstance(parsed, dict) and set(parsed.keys()) == {"type"}:
        sandbox_type = parsed.get("type")
        if isinstance(sandbox_type, str):
            return sandbox_type, json.dumps(parsed, sort_keys=True)

    return json.dumps(parsed, sort_keys=True), json.dumps(parsed, sort_keys=True)


def fetch_threads(
    db_path: Path,
    since: int | None,
    latest: int | None,
    include_non_worker: bool,
) -> list[sqlite3.Row]:
    filters: list[str] = []
    parameters: list[object] = []

    if not include_non_worker:
        filters.append("agent_role = 'worker'")
    if since is not None:
        filters.append("created_at >= ?")
        parameters.append(since)

    where_clause = ""
    if filters:
        where_clause = "WHERE " + " AND ".join(filters)

    query = (
        "SELECT id, created_at, updated_at, model, reasoning_effort, "
        "sandbox_policy, approval_mode, agent_role, agent_path "
        "FROM threads "
        f"{where_clause} "
        "ORDER BY created_at DESC, id DESC"
    )

    if latest is not None:
        query += " LIMIT ?"
        parameters.append(latest)

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        return connection.execute(query, parameters).fetchall()
    finally:
        connection.close()


def format_local_timestamp(epoch_seconds: int | None) -> str:
    if epoch_seconds is None:
        return "-"
    return datetime.fromtimestamp(epoch_seconds).astimezone().isoformat(timespec="seconds")


def summarize_field(
    field_name: str,
    requested_display: str | None,
    requested_key: str | None,
    effective_values: Iterable[str | None],
) -> str:
    if requested_display is None or requested_key is None:
        return f"- `{field_name}`: not captured as a requested setting."

    normalized_effective = [value for value in effective_values if value]
    if not normalized_effective:
        return (
            f"- `{field_name}`: unresolved. Requested `{requested_display}`, but no "
            "effective value was present in the captured thread rows."
        )

    matches = sum(1 for value in normalized_effective if value == requested_key)
    total = len(normalized_effective)

    if matches == total:
        return (
            f"- `{field_name}`: matched requested `{requested_display}` across "
            f"{matches}/{total} captured rows."
        )

    return (
        f"- `{field_name}`: mixed or mismatched. Requested `{requested_display}`; "
        f"{matches}/{total} captured rows matched."
    )


def render_markdown(
    label: str,
    db_path: Path,
    boundary_description: str,
    requested: RequestedSettings,
    rows: list[sqlite3.Row],
) -> str:
    captured_at = datetime.now().astimezone().isoformat(timespec="seconds")

    requested_sandbox_display, requested_sandbox_key = normalize_sandbox(
        requested.sandbox_policy
    )

    model_summary = summarize_field(
        "model",
        requested.model,
        requested.model,
        [row["model"] for row in rows],
    )
    reasoning_summary = summarize_field(
        "reasoning_effort",
        requested.reasoning_effort,
        requested.reasoning_effort,
        [row["reasoning_effort"] for row in rows],
    )
    approval_summary = summarize_field(
        "approval_mode",
        requested.approval_mode,
        requested.approval_mode,
        [row["approval_mode"] for row in rows],
    )
    sandbox_summary = summarize_field(
        "sandbox_policy",
        requested_sandbox_display,
        requested_sandbox_key,
        [normalize_sandbox(row["sandbox_policy"])[1] for row in rows],
    )

    lines = [
        "# Codex Launch Truth Capture",
        "",
        f"- `label`: {label}",
        f"- `captured_at`: {captured_at}",
        f"- `db_path`: {db_path}",
        f"- `selection`: {boundary_description}",
        "",
        "## Requested Settings",
    ]

    requested_rows = requested.as_rows()
    if requested_rows:
        for setting, value in requested_rows:
            lines.append(f"- `{setting}`: {value}")
    else:
        lines.append("- No requested settings were supplied.")

    lines.extend(
        [
            "",
            "## Effective Thread Rows",
            "",
            "| thread_id | created_at | model | reasoning_effort | approval_mode | sandbox_policy | agent_role | agent_path |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )

    for row in reversed(rows):
        sandbox_display, _ = normalize_sandbox(row["sandbox_policy"])
        lines.append(
            "| {thread_id} | {created_at} | {model} | {reasoning_effort} | "
            "{approval_mode} | {sandbox_policy} | {agent_role} | {agent_path} |".format(
                thread_id=row["id"],
                created_at=format_local_timestamp(row["created_at"]),
                model=row["model"] or "-",
                reasoning_effort=row["reasoning_effort"] or "-",
                approval_mode=row["approval_mode"] or "-",
                sandbox_policy=sandbox_display or "-",
                agent_role=row["agent_role"] or "-",
                agent_path=row["agent_path"] or "-",
            )
        )

    lines.extend(
        [
            "",
            "## Assessment",
            model_summary,
            reasoning_summary,
            approval_summary,
            sandbox_summary,
        ]
    )

    if requested.agent:
        lines.append(
            "- `requested_agent`: preserved as operator-declared intent only. "
            "The current sqlite thread rows do not prove the named agent."
        )

    if requested.agent_path:
        populated_agent_paths = [row["agent_path"] for row in rows if row["agent_path"]]
        if not populated_agent_paths:
            lines.append(
                "- `requested_agent_path`: unresolved. The current sqlite thread rows "
                "did not populate `agent_path`, so this capture cannot prove that "
                "specific config file reached the worker."
            )
        else:
            matches = sum(
                1 for path in populated_agent_paths if Path(path) == Path(requested.agent_path)
            )
            total = len(populated_agent_paths)
            if matches == total:
                lines.append(
                    "- `requested_agent_path`: matched across all captured rows that "
                    "reported `agent_path`."
                )
            else:
                lines.append(
                    "- `requested_agent_path`: mixed or mismatched across captured rows "
                    "that reported `agent_path`."
                )

    if "latest" in boundary_description:
        lines.append(
            "- Selection caveat: `--latest` is weaker evidence than a pre-recorded "
            "`--since` boundary because unrelated recent worker launches can fall into "
            "the same capture."
        )

    lines.append(
        "- This artifact records operator-declared requested settings beside effective "
        "thread rows. It does not replace reviewer judgment, and missing runtime fields "
        "must stay unresolved rather than being inferred."
    )

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()

    requested = RequestedSettings(
        model=args.requested_model,
        reasoning_effort=args.requested_reasoning,
        approval_mode=args.requested_approval,
        sandbox_policy=args.requested_sandbox,
        agent=args.requested_agent,
        agent_path=args.requested_agent_path,
    )

    if not requested.has_comparison_inputs():
        raise SystemExit(
            "Provide at least one --requested-* setting so the capture can record "
            "requested-versus-effective truth."
        )

    db_path = Path(args.db).expanduser()
    if not db_path.exists():
        raise SystemExit(f"sqlite database not found: {db_path}")

    since = parse_boundary(args.since) if args.since else None
    rows = fetch_threads(
        db_path=db_path,
        since=since,
        latest=args.latest,
        include_non_worker=args.include_non_worker,
    )

    if not rows:
        raise SystemExit("No matching thread rows were found for the requested capture.")

    boundary_description = (
        f"worker threads created at or after {format_local_timestamp(since)}"
        if since is not None
        else f"latest {args.latest} worker thread(s)"
    )

    markdown = render_markdown(
        label=args.label,
        db_path=db_path,
        boundary_description=boundary_description,
        requested=requested,
        rows=rows,
    )

    if args.output:
        output_path = Path(args.output).expanduser()
        output_path.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
