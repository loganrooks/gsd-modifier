#!/usr/bin/env python3

"""Run a Claude headless probe and print a compact diagnostic summary.

Operational note:
If the prompt tells Claude to read a repo-local spec or wrapper file, prefer
that file to live in the repo (not `/tmp`) and usually pass
`--dangerously-skip-permissions`. Without that, headless probes can fail in a
misleading way: startup/auth complete, `/v1/messages` is sent, then the run dies
before any assistant/result event is emitted.
"""

from __future__ import annotations

import argparse
import collections
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a Claude headless probe with stream-json diagnostics."
    )
    parser.add_argument("--label", required=True, help="Short label for temp artifact names.")
    parser.add_argument("--model", required=True, help="Claude model string, e.g. sonnet or opus[1m].")
    parser.add_argument("--effort", default="medium", help="Reasoning effort.")
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Inline prompt text.")
    prompt_group.add_argument(
        "--prompt-file",
        help=(
            "Path to a prompt file. If the prompt instructs Claude to read other "
            "repo files, prefer a repo-local path and usually pair this with "
            "--dangerously-skip-permissions."
        ),
    )
    parser.add_argument(
        "--output-dir",
        default="/tmp",
        help="Directory for stream/stderr/debug artifacts. Default: /tmp",
    )
    parser.add_argument(
        "--dangerously-skip-permissions",
        action="store_true",
        help=(
            "Pass --dangerously-skip-permissions to Claude for the probe. "
            "Recommended when the prompt asks Claude to read repo-local spec or "
            "wrapper files."
        ),
    )
    return parser.parse_args()


def load_prompt(args: argparse.Namespace) -> str:
    if args.prompt is not None:
        return args.prompt
    return Path(args.prompt_file).read_text()


def extract_blocks(obj: dict) -> list[str]:
    blocks: list[str] = []
    if obj.get("type") == "assistant":
        message = obj.get("message") or {}
        for item in message.get("content", []) or []:
            if isinstance(item, dict) and item.get("type") == "text" and item.get("text"):
                blocks.append(item["text"])
    if obj.get("type") == "result":
        result = obj.get("result")
        if isinstance(result, str) and result:
            blocks.append(result)
    return blocks


def summarize_stream(path: Path) -> dict:
    event_counts: collections.Counter[str] = collections.Counter()
    system_subtypes: collections.Counter[str] = collections.Counter()
    extracted: list[str] = []
    last_error_like: str | None = None

    if not path.exists():
        return {
            "event_counts": {},
            "system_subtypes": {},
            "text_chunks": 0,
            "last_text": None,
            "last_error_like": None,
        }

    with path.open() as handle:
        for raw_line in handle:
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            try:
                obj = json.loads(raw_line)
            except json.JSONDecodeError:
                continue
            event_type = obj.get("type")
            if event_type:
                event_counts[event_type] += 1
            if event_type == "system" and obj.get("subtype"):
                system_subtypes[obj["subtype"]] += 1
            extracted.extend(extract_blocks(obj))
            if "error" in raw_line.lower() or "failed" in raw_line.lower():
                last_error_like = raw_line

    return {
        "event_counts": dict(event_counts),
        "system_subtypes": dict(system_subtypes),
        "text_chunks": len(extracted),
        "last_text": extracted[-1] if extracted else None,
        "last_error_like": last_error_like,
    }


def tail_text(path: Path, lines: int = 20) -> str:
    if not path.exists():
        return ""
    data = path.read_text(errors="replace").splitlines()
    return "\n".join(data[-lines:])


def main() -> int:
    args = parse_args()
    prompt = load_prompt(args)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    stamp = time.strftime("%Y%m%d-%H%M%S")
    prefix = f"{args.label}-{stamp}"
    stream_file = Path(tempfile.mktemp(prefix=prefix + ".", suffix=".stream.jsonl", dir=output_dir))
    stderr_file = Path(tempfile.mktemp(prefix=prefix + ".", suffix=".stderr.log", dir=output_dir))
    debug_file = Path(tempfile.mktemp(prefix=prefix + ".", suffix=".debug.log", dir=output_dir))

    cmd = [
        "claude",
        "-p",
        "--model",
        args.model,
        "--effort",
        args.effort,
        "--output-format",
        "stream-json",
        "--include-partial-messages",
        "--verbose",
        "--debug-file",
        str(debug_file),
        prompt,
    ]

    if args.dangerously_skip_permissions:
        cmd.insert(2, "--dangerously-skip-permissions")

    start = time.time()
    with stream_file.open("w") as stream_handle, stderr_file.open("w") as stderr_handle:
        completed = subprocess.run(
            cmd,
            stdin=subprocess.DEVNULL,
            stdout=stream_handle,
            stderr=stderr_handle,
            text=True,
            check=False,
        )
    elapsed = time.time() - start

    summary = summarize_stream(stream_file)
    stderr_tail = tail_text(stderr_file, lines=10)
    debug_tail = tail_text(debug_file, lines=10)

    print(f"label={args.label}")
    print(f"exit_code={completed.returncode}")
    print(f"elapsed_seconds={elapsed:.3f}")
    print(f"stream={stream_file}")
    print(f"stderr={stderr_file}")
    print(f"debug={debug_file}")
    print(f"stream_bytes={stream_file.stat().st_size if stream_file.exists() else 0}")
    print(f"stderr_bytes={stderr_file.stat().st_size if stderr_file.exists() else 0}")
    print(f"debug_bytes={debug_file.stat().st_size if debug_file.exists() else 0}")
    print(f"event_counts={json.dumps(summary['event_counts'], sort_keys=True)}")
    print(f"system_subtypes={json.dumps(summary['system_subtypes'], sort_keys=True)}")
    print(f"text_chunks={summary['text_chunks']}")
    if summary["last_text"]:
        print("last_text_begin")
        print(summary["last_text"].rstrip())
        print("last_text_end")
    if summary["last_error_like"]:
        print("last_error_like_begin")
        print(summary["last_error_like"])
        print("last_error_like_end")
    if stderr_tail:
        print("stderr_tail_begin")
        print(stderr_tail)
        print("stderr_tail_end")
    if debug_tail:
        print("debug_tail_begin")
        print(debug_tail)
        print("debug_tail_end")

    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
