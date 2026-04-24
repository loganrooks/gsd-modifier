# Telemetry Substrate Second Slice Implementation Plan

Plan timestamp: `20260424T075728Z`
Status: ready for review, not implementation
Target executor profile: GPT-5.5 medium
Predecessor slice: `.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/`
Research basis: `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/`

## Purpose

Implement the next smallest usable slice of the model benchmark telemetry substrate after the first fixture/store/registry foundation.

This slice connects current benchmark run JSONL compatibility into the new observation/store path, adds migration reporting, exposes local-only CLI commands for rebuild/query/report, and strengthens provider-neutrality evidence with a fixture-backed Claude local JSONL adapter. It still does not implement live provider capture.

## Current Baseline

The predecessor slice is accepted in `20260424T061025Z/VERIFICATION.md`.

Already available:

- canonical enum and manifest validation modules
- synthetic privacy-safe fixture corpus
- SQLite cache skeleton
- fixture rebuild/query/report parity
- fixture-backed Codex SQLite and rollout adapters
- provider-neutrality fixture gate
- rubric observation compatibility path for current run JSONL

Known residual work from the predecessor slice:

- no live-provider ingestion
- no Claude/API production adapters
- no end-user CLI wiring for the new substrate path
- no migration report from v0 benchmark JSONL into the new observation model
- no production report surface

## Authoritative Inputs

Executors must read these before editing:

- `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/DECISION-REPORT.md`
- `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/NEXT-IMPLEMENTATION-PLAN.md`
- `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/audits/20260424T045822Z-independent-design-review/ARCHITECTURE-RESOLUTION.md`
- `.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/PLAN.md`
- `.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/VERIFICATION.md`
- `tooling/codex/model_benchmark/schema.py`
- `tooling/codex/model_benchmark/store.py`
- `tooling/codex/model_benchmark/rebuild.py`
- `tooling/codex/model_benchmark/query.py`
- `tooling/codex/model_benchmark/reports.py`
- `tooling/codex/model_benchmark/cli.py`
- existing tests under `tooling/codex/tests/test_model_benchmark*.py`

## Non-Goals

- No live Codex, Claude, OpenAI, Anthropic, or OTel calls.
- No provider config mutation.
- No home-directory ingestion by default.
- No raw transcript, prompt, assistant text, tool argument, tool result, file content, or raw API body persistence.
- No dashboard.
- No GSD phase/milestone domain plugin.
- No mandatory `telemetry_events` table.
- No provider-neutrality claim from a single-provider path.
- No removal of current v0 JSONL commands before migration compatibility is proven.

## Architecture Decisions To Preserve

- JSONL/raw artifacts are durable evidence; SQLite is a rebuildable query cache.
- Static YAML manifests are the human-reviewable registry source; canonical JSON registry payloads are used for hashing.
- Registry hash and source-set hash must flow through rebuild, query, and report boundaries.
- `runtime_response_items` is a generic runtime item concept, distinct from `model_calls`.
- Provider/runtime details live in namespaces or payloads, not provider-specific core columns.
- `score.overall` is legacy/view-only as `legacy.score.overall`; canonical quality is multidimensional rubric observations.
- Cost evidence modes keep API-equivalent estimates, provider-reported cost, pricing-table estimates, subscription/quota burn, and manual estimates separate.
- Missingness/status values must not be collapsed into zero.

## TDD Protocol

Every implementation task follows this protocol:

1. Write or extend failing tests first.
2. Run the focused test file and confirm the expected failure.
3. Implement the smallest code change to pass.
4. Run the focused test file.
5. Run `python3 -m unittest tooling.codex.tests.test_model_benchmark`.
6. If the task touches shared substrate modules or CLI, run the full relevant model benchmark suite:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark tooling.codex.tests.test_model_benchmark_manifest tooling.codex.tests.test_model_benchmark_fixtures tooling.codex.tests.test_model_benchmark_store tooling.codex.tests.test_model_benchmark_rebuild tooling.codex.tests.test_model_benchmark_report_parity tooling.codex.tests.test_model_benchmark_adapters tooling.codex.tests.test_model_benchmark_provider_neutrality
```

7. Run scoped `git diff --check` on the task write set.
8. Record verification commands in the task handoff or commit message.

If a test cannot fail first because the target module does not exist, the executor writes the test importing the intended module/API and confirms `ImportError` or assertion failure before implementation.

## Parallelization Strategy

The first two tasks are the foundation for the rest of the slice and should run sequentially.

Safe parallel workers after Task 02:

- Worker A: Task 03 local CLI commands.
- Worker B: Task 04 fixture-backed Claude adapter.

Do not parallelize:

- Task 02 before Task 01, because the migration report depends on the v0 compatibility import shape.
- Task 05 before Tasks 03 and 04, because it verifies the integrated CLI and adapter path.
- Any live provider experiment inside this slice.

All workers must be told they are not alone in the codebase and must not revert edits outside their write set.

## Task 01: V0 Run JSONL Compatibility Import

Owner: single executor

Write set:

- `tooling/codex/model_benchmark/migrate.py`
- `tooling/codex/tests/test_model_benchmark_migrate.py`
- optional small helper additions in `tooling/codex/model_benchmark/store.py`
- optional fixture additions under `tooling/codex/tests/fixtures/model_benchmark/v0_run_jsonl_compatibility/`

Goal:

- Import existing `model-benchmark-run/v1` JSONL records into the new SQLite observation/store model without losing v0 compatibility.

Test-first requirements:

- A synthetic v0 run JSONL fixture imports into `runs`, `observations`, `rubric_observations`, and `cost_estimates` where applicable.
- Legacy `score.overall` imports only as `legacy.score.overall` observation evidence and is labeled compatibility-only.
- New `rubric_observations` import as canonical rubric observations with evaluator/rubric-version provenance.
- Usage token fields import as observations with explicit status/missingness, not missing-as-zero.
- API-equivalent cost estimates import as `cost_evidence_mode=api_equivalent_estimate`, not provider-reported cost.
- Source artifact rows preserve source URI/hash and content contract without storing raw transcript content.
- Import result includes counts for runs, observations, rubric observations, legacy score observations, cost estimates, skipped records, and diagnostics.
- Malformed input records produce metadata-only diagnostics rather than partial raw content persistence.

Implementation notes:

- Reuse `schema.validate_run_record`; do not create a second v0 schema.
- Keep the importer path-explicit and local-only.
- Add store helpers only when they remove real duplication; do not redesign the store schema.
- Use namespaced metric IDs such as `usage.input_tokens`, `usage.reasoning_tokens`, `legacy.score.overall`, and `cost.api_equivalent`.

Focused verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark_migrate
```

Commit boundary:

`feat(model-benchmark): import v0 runs into telemetry store`

## Task 02: Migration Report And Query Surface

Owner: single executor after Task 01

Write set:

- `tooling/codex/model_benchmark/query.py`
- `tooling/codex/model_benchmark/reports.py`
- `tooling/codex/tests/test_model_benchmark_migration_report.py`
- optional additions in `tooling/codex/model_benchmark/migrate.py`

Goal:

- Add a migration report that makes compatibility state auditable before any legacy path is retired.

Test-first requirements:

- Report counts legacy scalar score observations separately from rubric observations.
- Report exposes missingness/status counts for usage/token observations.
- Report distinguishes API-equivalent cost estimates from provider-reported/pricing-table/manual cost evidence modes.
- Report includes source artifact count, registry hash when available, source-set hash when available, and diagnostics count.
- Report labels v0 compatibility as `compatibility_active`, not migrated-complete.
- Report does not include raw prompt, assistant, tool argument, tool result, or transcript content.
- Query/report strict mode rejects invalid enum values in observation or cost evidence rows.

Implementation notes:

- Keep this report small and structured; do not build a dashboard.
- The report may consume a SQLite connection and return a dict suitable for CLI JSON output.
- If registry hash is absent for v0 import-only runs, expose that as `not_collected` or `not_applicable` rather than inventing a hash.

Focused verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark_migration_report
python3 -m unittest tooling.codex.tests.test_model_benchmark_report_parity
```

Commit boundary:

`feat(model-benchmark): report v0 telemetry migration state`

## Task 03: Local-Only CLI For Rebuild, Query, And Reports

Owner: worker after Task 02

Write set:

- `tooling/codex/model_benchmark/cli.py`
- `tooling/codex/tests/test_model_benchmark_cli.py`
- optional tiny helper additions in `tooling/codex/model_benchmark/migrate.py`, `query.py`, or `reports.py`

Goal:

- Expose local-only commands for the new substrate path without changing existing v0 commands.

Required commands:

- `import-v0-runs --runs <jsonl> --db <sqlite> [--overwrite]`
- `migration-report --db <sqlite> --output <json> [--overwrite]`
- `rebuild-fixtures --manifest <yaml-or-json> --db <sqlite> --source <path>... [--overwrite]`
- `query-rebuild --db <sqlite> --output <json> [--registry-hash <hash>] [--overwrite]`

Test-first requirements:

- Existing `validate-runs`, `estimate-costs`, and `summarize-runs` commands still work.
- New commands operate on explicit local paths only.
- New commands refuse to overwrite output or SQLite files unless `--overwrite` is passed.
- New commands do not read `~/.codex`, `~/.claude`, provider config files, or environment credentials.
- CLI JSON output includes counts, registry/source hashes when available, and diagnostics.
- CLI errors are nonzero and do not dump raw input rows.

Implementation notes:

- If manifest loading currently only accepts YAML paths, support JSON registry input only if it is simple and tested; otherwise require YAML and document the restriction in help text.
- Keep commands thin wrappers around tested library functions.
- Use temp files in tests.

Focused verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark_cli
python3 -m unittest tooling.codex.tests.test_model_benchmark
```

Commit boundary:

`feat(model-benchmark): add local telemetry CLI commands`

## Task 04: Fixture-Backed Claude Local JSONL Adapter

Owner: worker after Task 02

Write set:

- `tooling/codex/model_benchmark/adapters/claude_local.py`
- `tooling/codex/model_benchmark/adapters/__init__.py`
- `tooling/codex/tests/test_model_benchmark_claude_adapter.py`
- optional fixture additions under `tooling/codex/tests/fixtures/model_benchmark/claude_local_jsonl_minimal_structure/`

Goal:

- Promote the current Claude-shaped provider-neutrality fixture handling into a dedicated path-explicit adapter, still fixture-only and local-only.

Test-first requirements:

- Adapter reads only caller-provided fixture paths.
- Adapter emits session/runtime item/tool/sidechain-or-agent structures without Codex field names.
- Adapter preserves redaction state, content contract, malformed-line diagnostics, and source line references.
- Adapter treats thinking summaries/facets/session metadata as substitute or derived structural signals, not reasoning-token or quality truth.
- Adapter output validation rejects undeclared enum values in strict mode.
- Adapter does not read `~/.claude`, hooks, plugins, skills, raw API bodies, or provider credentials.
- Adapter does not persist raw transcript content.

Implementation notes:

- Reuse `adapters.validate_adapter_output` where possible.
- If the first-slice provider-neutrality rebuild already contains Claude parsing logic, move only the reusable adapter-shaped part without changing the gate semantics.
- Keep Claude-specific names in `provider.anthropic` or `runtime.claude_code` payload namespaces.

Focused verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark_claude_adapter
python3 -m unittest tooling.codex.tests.test_model_benchmark_provider_neutrality
```

Commit boundary:

`feat(model-benchmark): add fixture backed Claude telemetry adapter`

## Task 05: Integrated Fixture And Compatibility Gate

Owner: coordinator or verification worker after Tasks 03 and 04

Write set:

- `tooling/codex/tests/test_model_benchmark_integration.py`
- optional minor fixes in modules touched by Tasks 01-04

Goal:

- Prove that v0 import, migration report, CLI commands, Codex fixtures, Claude fixture adapter, and provider-neutrality gate can coexist without registry/query/report drift.

Test-first requirements:

- A synthetic v0 run JSONL imports into a temp SQLite DB, produces a migration report, and can be queried through CLI without raw content output.
- Fixture rebuild/query still propagates registry hash and source-set hash.
- Provider-neutrality gate still fails for Codex-only input and passes for manual + Claude-shaped + denominator mismatch fixtures.
- Claude adapter output can feed or match the provider-neutrality path without Codex-only assumptions.
- `score.overall` remains absent from canonical declarations and appears only under legacy compatibility evidence.
- `runtime_response_items` remains distinct from `model_calls`.
- No test path reads home-level provider logs/configs.

Focused verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark_integration
python3 -m unittest tooling.codex.tests.test_model_benchmark tooling.codex.tests.test_model_benchmark_manifest tooling.codex.tests.test_model_benchmark_fixtures tooling.codex.tests.test_model_benchmark_store tooling.codex.tests.test_model_benchmark_rebuild tooling.codex.tests.test_model_benchmark_report_parity tooling.codex.tests.test_model_benchmark_adapters tooling.codex.tests.test_model_benchmark_provider_neutrality tooling.codex.tests.test_model_benchmark_migrate tooling.codex.tests.test_model_benchmark_migration_report tooling.codex.tests.test_model_benchmark_cli tooling.codex.tests.test_model_benchmark_claude_adapter
```

Commit boundary:

`test(model-benchmark): verify telemetry compatibility integration`

## Task 06: Final Verification Report

Owner: coordinator; report-only

Write set:

- `.planning/measurement/model-role-benchmark/implementation-plans/20260424T075728Z/VERIFICATION.md`

Goal:

- Verify the second slice is complete, committed, and not overclaiming. If verification fails, route fixes back to the owning implementation task instead of editing source under this task.

Required verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark tooling.codex.tests.test_model_benchmark_manifest tooling.codex.tests.test_model_benchmark_fixtures tooling.codex.tests.test_model_benchmark_store tooling.codex.tests.test_model_benchmark_rebuild tooling.codex.tests.test_model_benchmark_report_parity tooling.codex.tests.test_model_benchmark_adapters tooling.codex.tests.test_model_benchmark_provider_neutrality tooling.codex.tests.test_model_benchmark_migrate tooling.codex.tests.test_model_benchmark_migration_report tooling.codex.tests.test_model_benchmark_cli tooling.codex.tests.test_model_benchmark_claude_adapter tooling.codex.tests.test_model_benchmark_integration
git diff --check -- tooling/codex/model_benchmark tooling/codex/tests/test_model_benchmark.py tooling/codex/tests/test_model_benchmark_manifest.py tooling/codex/tests/test_model_benchmark_fixtures.py tooling/codex/tests/test_model_benchmark_store.py tooling/codex/tests/test_model_benchmark_rebuild.py tooling/codex/tests/test_model_benchmark_report_parity.py tooling/codex/tests/test_model_benchmark_adapters.py tooling/codex/tests/test_model_benchmark_provider_neutrality.py tooling/codex/tests/test_model_benchmark_migrate.py tooling/codex/tests/test_model_benchmark_migration_report.py tooling/codex/tests/test_model_benchmark_cli.py tooling/codex/tests/test_model_benchmark_claude_adapter.py tooling/codex/tests/test_model_benchmark_integration.py
```

If implementation touches broader portable-runtime or bootstrap surfaces, also run:

```bash
bash scripts/ci/check-deterministic.sh
bash scripts/ci/check-bootstrap.sh
```

Acceptance criteria:

- No live provider calls.
- No provider config mutation.
- No home-level provider log reads by default.
- No raw private content in fixtures, observations, reports, or CLI output.
- Current v0 run JSONL commands remain compatible.
- V0 import path records legacy scalar scores only as compatibility evidence.
- Migration report distinguishes rubric dimensions, legacy score observations, token missingness, cost evidence modes, source artifacts, and diagnostics.
- CLI commands are local-path explicit and overwrite-safe.
- Claude adapter remains fixture-backed and provider-neutrality gate remains multi-provider.
- Registry hash and source-set hash still propagate through rebuild/query/report paths where registry-backed rebuilds are used.

Commit boundary:

`test(model-benchmark): verify telemetry second slice integration`

## Delegation Prompt Template

Use this template for GPT-5.5 medium executor workers:

```text
You are implementing Task <N> from:
.planning/measurement/model-role-benchmark/implementation-plans/20260424T075728Z/PLAN.md

Read the plan section for Task <N>, the Authoritative Inputs, and ARCHITECTURE-RESOLUTION.md before editing.

Ownership:
- You own only the write set listed for Task <N>.
- You are not alone in the codebase. Do not revert or rewrite files outside your write set.
- If another worker has changed shared APIs, adapt to their public behavior instead of reverting them.

Protocol:
1. Write failing tests first.
2. Run the focused test and report the expected failure.
3. Implement the smallest passing change.
4. Run the focused verification command listed for the task.
5. Run scoped `git diff --check` on your write set.
6. Return changed files, verification commands, and unresolved questions.

Constraints:
- No live provider calls.
- No provider config mutation.
- No home-level provider log reads by default.
- No raw private transcript content.
- No provider-neutrality claim unless the explicit multi-provider fixture gate passes.
- Do not collapse missing values into zero.
- Keep `score.overall` legacy/view-only.
```

## Execution Order

Recommended sequence:

1. Task 01.
2. Task 02.
3. Tasks 03 and 04 in parallel, if the worktree is otherwise clean enough for delegation.
4. Task 05.
5. Task 06.

Before launching any executor, record the current dirty worktree boundary. Do not delegate substantial edits into an unresolved mixed worktree unless the worker has a disjoint worktree or a strictly isolated write set and the coordinator will review every returned diff before commit.
