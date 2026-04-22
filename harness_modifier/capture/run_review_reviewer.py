#!/usr/bin/env python3

"""Prepare and record durable cross-vendor review-run artifacts."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from harness_modifier.capture.run_claude_probe import summarize_stream


@dataclass
class ReviewClassification:
    reviewer: str
    shape: str
    state: str
    canonical_review_path: str | None
    stdout_path: str | None
    stderr_path: str | None
    stream_path: str | None
    launch_truth_path: str
    timing_path: str
    last_recoverable_text: str | None
    exit_code: int
    elapsed_seconds: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare a durable run-home for review routes or record one reviewer "
            "into that run-home with bounded launch-truth/timing/salvage support."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare-run-home")
    prepare.add_argument("--phase-dir", required=True)
    prepare.add_argument("--padded-phase", required=True)
    prepare.add_argument("--run-id")
    prepare.add_argument("--git-sha")

    record = subparsers.add_parser("record-reviewer")
    record.add_argument("--run-home", required=True)
    record.add_argument("--reviewer", required=True)
    record.add_argument(
        "--shape",
        required=True,
        choices=("claude", "codex", "plain"),
    )
    record.add_argument("--stdout-file")
    record.add_argument("--stderr-file")
    record.add_argument("--stream-file")
    record.add_argument("--launch-truth-markdown")
    record.add_argument("--probe-summary-file")
    record.add_argument("--estimated-duration")
    record.add_argument("--invocation")
    record.add_argument("--requested-model")
    record.add_argument("--requested-reasoning")
    record.add_argument("--requested-approval")
    record.add_argument("--requested-sandbox")
    record.add_argument("--exit-code", required=True, type=int)
    record.add_argument("--elapsed-seconds", required=True, type=float)

    return parser.parse_args()


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def git_short_sha() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except Exception:
        return "unknown"
    return completed.stdout.strip() or "unknown"


def write_json_stdout(payload: dict) -> int:
    sys.stdout.write(json.dumps(payload, indent=2, sort_keys=True))
    sys.stdout.write("\n")
    return 0


def prepare_run_home(args: argparse.Namespace) -> int:
    phase_dir = Path(args.phase_dir).resolve()
    run_id = args.run_id or f"{utc_stamp()}-{args.git_sha or git_short_sha()}"
    run_home = phase_dir / "reviews" / run_id
    launch_truth_dir = run_home / "launch-truth"

    run_home.mkdir(parents=True, exist_ok=True)
    launch_truth_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "run_id": run_id,
        "run_home": str(run_home),
        "prompt_path": str(run_home / "prompt.md"),
        "launch_truth_dir": str(launch_truth_dir),
        "timing_path": str(run_home / "timing.md"),
        "padded_phase": args.padded_phase,
    }
    return write_json_stdout(payload)


def read_text_if_present(path: Path | None) -> str | None:
    if path is None or not path.exists():
        return None
    text = path.read_text(errors="replace")
    return text if text else None


def copy_if_present(source: str | None, destination: Path) -> Path | None:
    if not source:
        return None
    src = Path(source)
    if not src.exists():
        return None
    destination.parent.mkdir(parents=True, exist_ok=True)
    if src.resolve() == destination.resolve():
        return destination
    shutil.copyfile(src, destination)
    return destination


def classify_claude(stream_path: Path | None, exit_code: int) -> tuple[str, str | None]:
    if stream_path is None or not stream_path.exists():
        return "absent", None

    summary = summarize_stream(stream_path)
    last_text = summary.get("last_text")
    result_events = summary.get("event_counts", {}).get("result", 0)

    if last_text and exit_code == 0 and result_events:
        return "complete", last_text
    if last_text:
        return "partial", last_text
    return "absent", None


def classify_text_output(stdout_path: Path | None, exit_code: int) -> tuple[str, str | None]:
    text = read_text_if_present(stdout_path)
    if text and exit_code == 0:
        return "complete", text
    if text:
        return "partial", text
    return "absent", None


def render_launch_truth(
    reviewer: str,
    shape: str,
    invocation: str | None,
    estimated_duration: str | None,
    elapsed_seconds: float,
    exit_code: int,
    stdout_path: Path | None,
    stderr_path: Path | None,
    stream_path: Path | None,
    probe_summary_path: Path | None,
    copied_launch_truth: Path | None,
    requested_model: str | None,
    requested_reasoning: str | None,
    requested_approval: str | None,
    requested_sandbox: str | None,
) -> str:
    lines = [
        "# Review Reviewer Launch Truth",
        "",
        f"- `reviewer`: {reviewer}",
        f"- `shape`: {shape}",
        f"- `exit_code`: {exit_code}",
        f"- `elapsed_seconds`: {elapsed_seconds:.3f}",
    ]

    if invocation:
        lines.append(f"- `invocation`: {invocation}")
    if estimated_duration:
        lines.append(f"- `estimated_duration`: {estimated_duration}")
    if requested_model:
        lines.append(f"- `requested_model`: {requested_model}")
    if requested_reasoning:
        lines.append(f"- `requested_reasoning`: {requested_reasoning}")
    if requested_approval:
        lines.append(f"- `requested_approval`: {requested_approval}")
    if requested_sandbox:
        lines.append(f"- `requested_sandbox`: {requested_sandbox}")
    if stdout_path:
        lines.append(f"- `stdout_path`: {stdout_path}")
        lines.append(f"- `stdout_bytes`: {stdout_path.stat().st_size if stdout_path.exists() else 0}")
    if stderr_path:
        lines.append(f"- `stderr_path`: {stderr_path}")
        lines.append(f"- `stderr_bytes`: {stderr_path.stat().st_size if stderr_path.exists() else 0}")
    if stream_path:
        lines.append(f"- `stream_path`: {stream_path}")
        lines.append(f"- `stream_bytes`: {stream_path.stat().st_size if stream_path.exists() else 0}")

    if copied_launch_truth:
        lines.extend(
            [
                "",
                "## Captured Effective Launch Truth",
                "",
                copied_launch_truth.read_text(errors="replace").rstrip(),
            ]
        )

    if probe_summary_path and probe_summary_path.exists():
        lines.extend(
            [
                "",
                "## Probe Summary",
                "",
                "```text",
                probe_summary_path.read_text(errors="replace").rstrip(),
                "```",
            ]
        )

    return "\n".join(lines) + "\n"


def append_timing_entry(
    timing_path: Path,
    reviewer: str,
    estimated_duration: str | None,
    elapsed_seconds: float,
) -> None:
    lines: list[str] = []
    if timing_path.exists():
        existing = timing_path.read_text(errors="replace").rstrip()
        if existing:
            lines.append(existing)
            lines.append("")
    else:
        lines.extend(["# Review Timing", ""])

    lines.append(f"## {reviewer}")
    if estimated_duration:
        lines.append(f"- `estimate`: {estimated_duration}")
    else:
        lines.append("- `estimate`: not recorded")
    lines.append(f"- `actual_elapsed_seconds`: {elapsed_seconds:.3f}")
    lines.append("- `calibration_note`: pending local operator calibration note")
    lines.append("")
    timing_path.write_text("\n".join(lines).rstrip() + "\n")


def write_classification_note(
    run_home: Path,
    reviewer: str,
    state: str,
    last_recoverable_text: str | None,
) -> Path:
    note_path = run_home / f"{reviewer}.status.md"
    lines = [
        f"# {reviewer} Reviewer State",
        "",
        f"- `state`: {state}",
    ]
    if last_recoverable_text:
        lines.extend(["", "## Last Recoverable Text", "", last_recoverable_text.rstrip()])
    note_path.write_text("\n".join(lines).rstrip() + "\n")
    return note_path


def record_reviewer(args: argparse.Namespace) -> int:
    run_home = Path(args.run_home).resolve()
    run_home.mkdir(parents=True, exist_ok=True)
    launch_truth_dir = run_home / "launch-truth"
    launch_truth_dir.mkdir(parents=True, exist_ok=True)

    reviewer = args.reviewer
    stdout_path = copy_if_present(args.stdout_file, run_home / f"{reviewer}.stdout.md")
    stderr_path = copy_if_present(args.stderr_file, run_home / f"{reviewer}.stderr.log")
    stream_path = copy_if_present(args.stream_file, run_home / f"{reviewer}.stream.jsonl")
    probe_summary_path = copy_if_present(
        args.probe_summary_file,
        run_home / f"{reviewer}.probe-summary.txt",
    )
    copied_launch_truth = copy_if_present(
        args.launch_truth_markdown,
        launch_truth_dir / f"{reviewer}.captured.md",
    )

    if args.shape == "claude":
        state, last_recoverable_text = classify_claude(stream_path, args.exit_code)
    else:
        state, last_recoverable_text = classify_text_output(stdout_path, args.exit_code)

    canonical_review_path: Path | None = None
    if last_recoverable_text:
        canonical_review_path = run_home / f"{reviewer}.review.md"
        canonical_review_path.write_text(last_recoverable_text.rstrip() + "\n")

    launch_truth_path = launch_truth_dir / f"{reviewer}.md"
    launch_truth_path.write_text(
        render_launch_truth(
            reviewer=reviewer,
            shape=args.shape,
            invocation=args.invocation,
            estimated_duration=args.estimated_duration,
            elapsed_seconds=args.elapsed_seconds,
            exit_code=args.exit_code,
            stdout_path=stdout_path,
            stderr_path=stderr_path,
            stream_path=stream_path,
            probe_summary_path=probe_summary_path,
            copied_launch_truth=copied_launch_truth,
            requested_model=args.requested_model,
            requested_reasoning=args.requested_reasoning,
            requested_approval=args.requested_approval,
            requested_sandbox=args.requested_sandbox,
        )
    )

    timing_path = run_home / "timing.md"
    append_timing_entry(
        timing_path=timing_path,
        reviewer=reviewer,
        estimated_duration=args.estimated_duration,
        elapsed_seconds=args.elapsed_seconds,
    )

    write_classification_note(
        run_home=run_home,
        reviewer=reviewer,
        state=state,
        last_recoverable_text=last_recoverable_text,
    )

    classification = ReviewClassification(
        reviewer=reviewer,
        shape=args.shape,
        state=state,
        canonical_review_path=str(canonical_review_path) if canonical_review_path else None,
        stdout_path=str(stdout_path) if stdout_path else None,
        stderr_path=str(stderr_path) if stderr_path else None,
        stream_path=str(stream_path) if stream_path else None,
        launch_truth_path=str(launch_truth_path),
        timing_path=str(timing_path),
        last_recoverable_text=last_recoverable_text,
        exit_code=args.exit_code,
        elapsed_seconds=args.elapsed_seconds,
    )
    return write_json_stdout(asdict(classification))


def main() -> int:
    args = parse_args()
    if args.command == "prepare-run-home":
        return prepare_run_home(args)
    if args.command == "record-reviewer":
        return record_reviewer(args)
    raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
