"""Command-line entry point for manual model benchmark ingest."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import quote

from tooling.codex.model_benchmark import costs, manifest, migrate, query, rebuild, reports, schema, store
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


def _print_json(value: dict[str, Any]) -> None:
    print(json.dumps(value, indent=2, sort_keys=True))


def _prepare_new_db(path: str | Path, *, overwrite: bool) -> Path:
    path_obj = Path(path)
    if path_obj.exists():
        if not overwrite:
            raise FileExistsError(f"{path_obj} already exists; pass --overwrite to replace it")
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    return path_obj


def _require_existing_db(path: str | Path) -> Path:
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"{path_obj} does not exist")
    return path_obj


def _counts_from_result(result: dict[str, Any], keys: tuple[str, ...]) -> dict[str, int]:
    return {key: int(result.get(key, 0)) for key in keys}


def _temporary_db_path(final_path: Path) -> Path:
    final_path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        dir=final_path.parent,
        prefix=f".{final_path.name}.",
        suffix=".tmp",
        delete=False,
    )
    handle.close()
    return Path(handle.name)


def _replace_db(temp_path: Path, final_path: Path) -> None:
    temp_path.replace(final_path)


def _cleanup_temp(path: Path) -> None:
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def _connect_read_only_db(path: str | Path) -> sqlite3.Connection:
    path_obj = _require_existing_db(path).resolve()
    uri = f"file:{quote(str(path_obj), safe='/')}?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    return conn


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


def _cmd_import_v0_runs(args: argparse.Namespace) -> int:
    db_path = _prepare_new_db(args.db, overwrite=args.overwrite)
    temp_db_path = _temporary_db_path(db_path)
    try:
        conn = store.connect(temp_db_path)
        try:
            result = migrate.import_v0_run_jsonl(conn, args.runs)
        finally:
            conn.close()
        payload = {
            "command": "import-v0-runs",
            "db": str(db_path),
            "source_uri": result["source_uri"],
            "source_hash": result["source_hash"],
            "counts": _counts_from_result(
                result,
                (
                    "runs",
                    "observations",
                    "rubric_observations",
                    "legacy_score_observations",
                    "cost_estimates",
                    "skipped_records",
                ),
            ),
            "diagnostic_count": int(result["diagnostic_count"]),
            "diagnostics": result["diagnostics"],
        }
        if payload["counts"]["runs"] == 0 and payload["diagnostic_count"]:
            raise ValueError(
                f"import-v0-runs imported no valid run records; diagnostic_count={payload['diagnostic_count']}"
            )
        _replace_db(temp_db_path, db_path)
    except Exception:
        _cleanup_temp(temp_db_path)
        raise
    _print_json(payload)
    return 0


def _cmd_migration_report(args: argparse.Namespace) -> int:
    conn = _connect_read_only_db(args.db)
    try:
        report = reports.telemetry_migration_report(conn, strict=True)
    finally:
        conn.close()
    _write_json(args.output, report, overwrite=args.overwrite)
    _print_json(report)
    return 0


def _cmd_rebuild_fixtures(args: argparse.Namespace) -> int:
    db_path = _prepare_new_db(args.db, overwrite=args.overwrite)
    registry = manifest.load_manifest(args.manifest)
    temp_db_path = _temporary_db_path(db_path)
    try:
        conn = store.connect(temp_db_path)
        try:
            result = rebuild.rebuild_fixture_sources(conn, registry, args.source)
        finally:
            conn.close()
        payload = {
            "command": "rebuild-fixtures",
            "db": str(db_path),
            "rebuild_id": int(result["rebuild_id"]),
            "schema_version": result["schema_version"],
            "registry_version": result["registry_version"],
            "registry_hash": result["registry_hash"],
            "source_set_hash": result["source_set_hash"],
            "counts": {
                "sources": len(args.source),
                "diagnostics": len(result["diagnostics"]),
            },
            "diagnostic_count": len(result["diagnostics"]),
            "diagnostics": result["diagnostics"],
        }
        _replace_db(temp_db_path, db_path)
    except Exception:
        _cleanup_temp(temp_db_path)
        raise
    _print_json(payload)
    return 0


def _cmd_query_rebuild(args: argparse.Namespace) -> int:
    conn = _connect_read_only_db(args.db)
    try:
        summary = query.query_rebuild_summary(conn, registry_hash=args.registry_hash, strict=True)
        report = reports.telemetry_rebuild_report(
            summary,
            registry_hash=args.registry_hash,
            strict=True,
        )
    finally:
        conn.close()
    _write_json(args.output, report, overwrite=args.overwrite)
    _print_json(report)
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

    import_v0 = subparsers.add_parser(
        "import-v0-runs",
        help="import explicit local v0 run JSONL into a new local SQLite telemetry cache",
    )
    import_v0.add_argument("--runs", required=True, help="local model-benchmark-run/v1 JSONL path")
    import_v0.add_argument("--db", required=True, help="local SQLite output path")
    import_v0.add_argument("--overwrite", action="store_true")
    import_v0.set_defaults(func=_cmd_import_v0_runs)

    migration = subparsers.add_parser(
        "migration-report",
        help="write a local JSON report for an imported v0 telemetry SQLite cache",
    )
    migration.add_argument("--db", required=True, help="local SQLite input path")
    migration.add_argument("--output", required=True, help="local JSON report output path")
    migration.add_argument("--overwrite", action="store_true")
    migration.set_defaults(func=_cmd_migration_report)

    fixture_rebuild = subparsers.add_parser(
        "rebuild-fixtures",
        help="rebuild a new local SQLite cache from a YAML or JSON telemetry plugin manifest and explicit sources",
    )
    fixture_rebuild.add_argument("--manifest", required=True, help="local YAML or JSON telemetry plugin manifest")
    fixture_rebuild.add_argument("--db", required=True, help="local SQLite output path")
    fixture_rebuild.add_argument("--source", required=True, action="append", help="local fixture source path")
    fixture_rebuild.add_argument("--overwrite", action="store_true")
    fixture_rebuild.set_defaults(func=_cmd_rebuild_fixtures)

    query_rebuild = subparsers.add_parser(
        "query-rebuild",
        help="query latest rebuild metadata from a local SQLite cache and write a JSON report",
    )
    query_rebuild.add_argument("--db", required=True, help="local SQLite input path")
    query_rebuild.add_argument("--output", required=True, help="local JSON report output path")
    query_rebuild.add_argument("--registry-hash")
    query_rebuild.add_argument("--overwrite", action="store_true")
    query_rebuild.set_defaults(func=_cmd_query_rebuild)
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
