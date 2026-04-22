#!/usr/bin/env python3

"""Extract text-bearing content from Claude/Codex stream-json logs.

Examples:
  python3 harness_modifier/capture/extract_stream_text.py run.stream.jsonl
  python3 harness_modifier/capture/extract_stream_text.py run.stream.jsonl --tail 100
  python3 harness_modifier/capture/extract_stream_text.py run.stream.jsonl --head 50
  python3 harness_modifier/capture/extract_stream_text.py run.stream.jsonl --range 120:180
  python3 harness_modifier/capture/extract_stream_text.py run.stream.jsonl --last-message
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from pathlib import Path
from typing import Iterable


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract text-bearing content from a Claude/Codex stream-json log."
    )
    parser.add_argument("path", help="Path to the stream-jsonl file.")

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--head", type=int, help="Use only the first N raw jsonl lines.")
    mode.add_argument("--tail", type=int, help="Use only the last N raw jsonl lines.")
    mode.add_argument(
        "--range",
        dest="line_range",
        help="Use only raw jsonl lines START:END (1-based, inclusive).",
    )
    mode.add_argument(
        "--last-message",
        action="store_true",
        help="Print only the last text-bearing message/result found.",
    )

    parser.add_argument(
        "--include-result",
        action="store_true",
        help="Include result text if present.",
    )
    parser.add_argument(
        "--include-thinking",
        action="store_true",
        help="Include thinking/redacted_thinking content if present.",
    )
    parser.add_argument(
        "--show-source-lines",
        action="store_true",
        help="Prefix extracted chunks with their source jsonl line numbers.",
    )
    parser.add_argument(
        "--output",
        help="Write extracted text to this file instead of stdout.",
    )
    args = parser.parse_args()

    if args.head is not None and args.head < 1:
        parser.error("--head must be at least 1")
    if args.tail is not None and args.tail < 1:
        parser.error("--tail must be at least 1")
    if args.line_range:
        parse_line_range(args.line_range)

    return args


def parse_line_range(spec: str) -> tuple[int, int]:
    if ":" not in spec:
        raise SystemExit("--range must look like START:END")
    start_raw, end_raw = spec.split(":", 1)
    try:
        start = int(start_raw)
        end = int(end_raw)
    except ValueError as exc:
        raise SystemExit("--range bounds must be integers") from exc
    if start < 1 or end < start:
        raise SystemExit("--range must use 1-based inclusive bounds with END >= START")
    return start, end


def iter_selected_lines(path: Path, args: argparse.Namespace) -> list[tuple[int, str]]:
    if args.head is not None:
        selected: list[tuple[int, str]] = []
        with path.open() as handle:
            for idx, line in enumerate(handle, start=1):
                if idx > args.head:
                    break
                selected.append((idx, line))
        return selected

    if args.tail is not None:
        bucket: deque[tuple[int, str]] = deque(maxlen=args.tail)
        with path.open() as handle:
            for idx, line in enumerate(handle, start=1):
                bucket.append((idx, line))
        return list(bucket)

    if args.line_range:
        start, end = parse_line_range(args.line_range)
        selected = []
        with path.open() as handle:
            for idx, line in enumerate(handle, start=1):
                if idx < start:
                    continue
                if idx > end:
                    break
                selected.append((idx, line))
        return selected

    with path.open() as handle:
        return [(idx, line) for idx, line in enumerate(handle, start=1)]


def extract_blocks(obj: dict, include_result: bool, include_thinking: bool) -> list[str]:
    event_type = obj.get("type")
    blocks: list[str] = []

    if event_type in {"assistant", "user"}:
        message = obj.get("message") or {}
        for item in message.get("content", []) or []:
            if not isinstance(item, dict):
                continue
            item_type = item.get("type")
            if item_type == "text" and item.get("text"):
                blocks.append(item["text"])
            elif include_thinking and item_type in {"thinking", "redacted_thinking"}:
                text = item.get("thinking") or item.get("text")
                if text:
                    blocks.append(text)

    if include_result and event_type == "result":
        result = obj.get("result")
        if isinstance(result, str) and result:
            blocks.append(result)

    return blocks


def format_chunk(source_line: int, text: str, show_source_lines: bool) -> str:
    if not show_source_lines:
        return text.rstrip()
    return f"[jsonl:{source_line}]\n{text.rstrip()}"


def main() -> int:
    args = parse_args()
    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    selected = iter_selected_lines(path, args)
    extracted: list[str] = []

    for source_line, raw_line in selected:
        stripped = raw_line.strip()
        if not stripped:
            continue
        try:
            obj = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        for block in extract_blocks(obj, args.include_result, args.include_thinking):
            if block.strip():
                extracted.append(format_chunk(source_line, block, args.show_source_lines))

    if args.last_message:
        output_text = extracted[-1] if extracted else ""
    else:
        output_text = "\n\n".join(extracted)

    if args.output:
        Path(args.output).write_text(output_text)
    else:
        sys.stdout.write(output_text)
        if output_text and not output_text.endswith("\n"):
            sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
