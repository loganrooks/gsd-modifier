"""Command-line entry point for manual model benchmark ingest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from tooling.codex.model_benchmark import costs, reports, schema
from tooling.codex.model_benchmark.io import read_json_object, read_jsonl_objects, write_jsonl_objects
from tooling.codex.model_benchmark.profiles import validate_profile_registry


def _load_registry(path: str | None) -> dict[str, dict[str, Any]]:
    return validate_profile_registry(read_json_object(path) if path else None)


def _validate_runs(path: str, profiles_path: str | None = None) -> list[dict[str, Any]]:
    registry = _load_registry(profiles_path)
    return [schema.validate_run_record(row, profile_registry=registry) for row in read_jsonl_objects(path)]


def _write_json(path: str | Path, value: dict[str, Any], overwrite: bool = False) -> None:
    path_obj = Path(path)
    if path_obj.exists() and not overwrite:
        raise FileExistsError(f"{path_obj} already exists; pass --overwrite to replace it")
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    with path_obj.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _cmd_validate_runs(args: argparse.Namespace) -> int:
    rows = _validate_runs(args.runs, args.profiles)
    print(f"validated {len(rows)} run record(s)")
    return 0


def _cmd_estimate_costs(args: argparse.Namespace) -> int:
    rows = _validate_runs(args.runs, args.profiles)
    rate_table = read_json_object(args.rates)
    estimated = [costs.attach_cost_estimate(row, rate_table) for row in rows]
    write_jsonl_objects(args.output, estimated, overwrite=args.overwrite)
    print(f"wrote {len(estimated)} estimated run record(s) to {args.output}")
    return 0


def _cmd_summarize_runs(args: argparse.Namespace) -> int:
    rows = _validate_runs(args.runs, args.profiles)
    summary = reports.summarize_runs(rows)
    _write_json(args.output, summary, overwrite=args.overwrite)
    print(f"wrote summary for {len(summary['groups'])} group(s) to {args.output}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="model-benchmark")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-runs", help="validate benchmark run JSONL")
    validate.add_argument("--runs", required=True)
    validate.add_argument("--profiles")
    validate.set_defaults(func=_cmd_validate_runs)

    estimate = subparsers.add_parser("estimate-costs", help="attach API-equivalent cost estimates to run JSONL")
    estimate.add_argument("--runs", required=True)
    estimate.add_argument("--rates", required=True)
    estimate.add_argument("--output", required=True)
    estimate.add_argument("--profiles")
    estimate.add_argument("--overwrite", action="store_true")
    estimate.set_defaults(func=_cmd_estimate_costs)

    summarize = subparsers.add_parser("summarize-runs", help="summarize benchmark run JSONL")
    summarize.add_argument("--runs", required=True)
    summarize.add_argument("--output", required=True)
    summarize.add_argument("--profiles")
    summarize.add_argument("--overwrite", action="store_true")
    summarize.set_defaults(func=_cmd_summarize_runs)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
