# Telemetry Substrate First Slice Implementation Plan

Plan timestamp: `20260424T061025Z`
Status: ready for review, not implementation
Target executor profile: GPT-5.5 medium
Research basis: `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/`

## Purpose

Implement the smallest telemetry substrate slice that proves the research decisions without live provider calls, provider config mutation, raw-content capture, or broad platform scope.

This plan is intentionally executor-friendly: each task has a bounded write set, test-first protocol, verification gate, and explicit handoff output. A GPT-5.5 medium executor should be able to complete one task at a time without reopening architecture.

## Authoritative Inputs

Executors must read these before editing:

- `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/DECISION-REPORT.md`
- `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/NEXT-IMPLEMENTATION-PLAN.md`
- `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/audits/20260424T045822Z-independent-design-review/ARCHITECTURE-RESOLUTION.md`
- `tooling/codex/model_benchmark/schema.py`
- `tooling/codex/model_benchmark/io.py`
- `tooling/codex/model_benchmark/reports.py`
- `tooling/codex/tests/test_model_benchmark.py`

## Non-Goals

- No live Codex, Claude, OpenAI, Anthropic, or OTel calls.
- No provider config mutation.
- No raw transcript, prompt, assistant text, tool argument, tool result, file content, or raw API body persistence.
- No dashboard.
- No GSD phase/milestone domain plugin.
- No mandatory `telemetry_events` table.
- No provider-neutrality claim from Codex-only fixtures.

## Architecture Decisions To Preserve

- JSONL/raw artifacts are durable evidence; SQLite is a rebuildable query cache.
- `runtime_response_items` is a generic runtime item concept, distinct from `model_calls`.
- `telemetry_events` is optional and must not be first-slice required infrastructure.
- Static YAML manifests are the human-reviewable source; canonical JSON registry payloads are used for hashing.
- Registry hash and source-set hash must flow through rebuild, query, and report boundaries.
- `score.overall` is legacy/view-only as `legacy.score.overall`; canonical quality is multidimensional rubric observations.
- Provider/runtime details live in namespaces or payloads, not provider-specific core columns.

## Canonical Enums

Use exactly the vocabularies from `ARCHITECTURE-RESOLUTION.md` for:

- observation status / missingness
- evidence class
- reliability mode
- content contract
- cost evidence mode
- comparability

Implementation may expose them as constants in a new module, but tests must reject undeclared values in strict paths.

## Proposed Module Shape

Keep the implementation under the existing package:

- `tooling/codex/model_benchmark/enums.py`
- `tooling/codex/model_benchmark/manifest.py`
- `tooling/codex/model_benchmark/fixtures.py`
- `tooling/codex/model_benchmark/store.py`
- `tooling/codex/model_benchmark/rebuild.py`
- `tooling/codex/model_benchmark/query.py`
- `tooling/codex/model_benchmark/adapters/__init__.py`
- `tooling/codex/model_benchmark/adapters/codex_sqlite.py`
- `tooling/codex/model_benchmark/adapters/codex_rollout.py`

Tests:

- `tooling/codex/tests/test_model_benchmark_manifest.py`
- `tooling/codex/tests/test_model_benchmark_store.py`
- `tooling/codex/tests/test_model_benchmark_rebuild.py`
- `tooling/codex/tests/test_model_benchmark_adapters.py`
- Extend `tooling/codex/tests/test_model_benchmark.py` only for compatibility/migration tests.

Fixtures:

- `tooling/codex/tests/fixtures/model_benchmark/`

## TDD Protocol

Every implementation task follows this protocol:

1. Write or extend failing tests first.
2. Run the focused test file and confirm the expected failure.
3. Implement the smallest code change to pass.
4. Run the focused test file.
5. Run `python3 -m unittest tooling.codex.tests.test_model_benchmark`.
6. If the task touches shared package imports or CLI, run the full relevant model benchmark test set:
   - `python3 -m unittest tooling.codex.tests.test_model_benchmark tooling.codex.tests.test_model_benchmark_manifest tooling.codex.tests.test_model_benchmark_store tooling.codex.tests.test_model_benchmark_rebuild tooling.codex.tests.test_model_benchmark_adapters`
7. Run `git diff --check`.
8. Record verification commands in the task handoff or commit message.

If a test cannot fail first because the target module does not exist, the executor writes the test importing the intended module/API and confirms `ImportError` or assertion failure before implementation.

## Parallelization Strategy

Parallelization is possible only after Task 01 defines shared constants and manifest primitives.

Safe parallel workers:

- Worker A after Task 01: fixtures and privacy fixture lints.
- Worker B after Task 01: SQLite schema/store skeleton.
- Worker C after Task 01: manifest validation and canonical registry hashing.

Do not parallelize:

- Rebuild/query parity before manifest and store APIs exist.
- Codex adapters before fixture contracts and store insert APIs exist.
- Report/rubric migration before rubric observation schema exists.

All workers must be told they are not alone in the codebase and must not revert edits outside their write set.

## Phase 0: Plan Gate

Goal: ensure this plan is review-approved before code.

Tasks:

- Review this plan against `ARCHITECTURE-RESOLUTION.md`.
- Confirm every load-bearing decision is carried into task gates.
- Confirm each worker write set is disjoint enough for delegation.

Verification:

- `git diff --check -- .planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/PLAN.md`

## Task 01: Canonical Enums And Manifest Skeleton

Owner: single executor
Write set:

- `tooling/codex/model_benchmark/enums.py`
- `tooling/codex/model_benchmark/manifest.py`
- `tooling/codex/tests/test_model_benchmark_manifest.py`
- dependency/config file only if required to use an already-approved YAML parser
- optional: `tooling/codex/model_benchmark/__init__.py`

Goal:

- Add canonical enum constants from `ARCHITECTURE-RESOLUTION.md`.
- Add a static manifest loader/validator for `telemetry-plugin-manifest/v1`.
- Generate canonical JSON bytes/string with deterministic ordering.
- Compute registry hash.

Test-first requirements:

- Test valid minimal manifest passes.
- Test malformed schema version fails.
- Test duplicate metric/rubric/source IDs fail.
- Test undeclared enum values fail.
- Test raw-content modes require explicit consent flag or fail by default.
- Test canonical JSON hash is stable across YAML key ordering.

Implementation notes:

- First-slice manifests are static YAML. Do not downgrade to JSON manifests or invent a different manifest source format.
- Before implementation, check whether a YAML parser is already available in the repo environment. If no approved YAML parser is available, stop and ask the coordinator whether to add a dependency or implement a deliberately tiny YAML subset parser. Do not make that architecture choice inside the worker task.
- Keep validator strict for declared identifiers and tolerant only inside namespaced provider payload metadata.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark_manifest`

Commit boundary:

- `feat(model-benchmark): add telemetry manifest validation skeleton`

## Task 02: Golden Fixture Corpus

Owner: worker can run in parallel after Task 01 API is stable
Write set:

- `tooling/codex/tests/fixtures/model_benchmark/**`
- `tooling/codex/tests/test_model_benchmark_fixtures.py`
- optional: `tooling/codex/model_benchmark/fixtures.py`

Goal:

- Add synthetic, privacy-safe fixtures required by the provider-neutrality gate.

Required fixtures:

- `codex_sqlite_minimal_thread`
- `codex_rollout_redacted_stream`
- `manual_run_with_rubric_dimensions`
- `claude_local_jsonl_minimal_structure`
- `provider_denominator_mismatch`
- malformed JSONL fixture
- rebuild parity fixture set

Test-first requirements:

- Fixture linter rejects obvious raw prompt/assistant/tool-result fields in default fixtures.
- Fixture manifest lists every fixture, source kind, expected privacy contract, and expected outputs.
- Claude-shaped fixture must not require Codex field names and must include session/message/tool/sidechain-or-agent structure, malformed-line diagnostics, redaction states, and no private transcript content.
- Provider-denominator fixture must preserve different token/cache/reasoning/cost semantics.
- Manual rubric fixture must not require canonical `score.overall`.

Implementation notes:

- Use tiny synthetic records, not copied local logs.
- Store expected normalized outputs as JSON fixtures if useful.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark_fixtures`

Commit boundary:

- `test(model-benchmark): add telemetry substrate golden fixtures`

## Task 03: SQLite Store Skeleton

Owner: worker can run in parallel after Task 01 API is stable
Write set:

- `tooling/codex/model_benchmark/store.py`
- `tooling/codex/tests/test_model_benchmark_store.py`

Goal:

- Add a rebuildable SQLite cache skeleton.

Minimum tables:

- `source_artifacts`
- `task_definitions`
- `task_instances`
- `runs`
- `sessions`
- `turns`
- `runtime_response_items`
- `model_calls`
- `tool_calls`
- `entity_edges`
- `observations`
- `rubric_observations`
- `cost_estimates`
- `registries`
- `rebuild_runs`

Explicitly excluded:

- required `telemetry_events`

Test-first requirements:

- Store initializes all minimum tables.
- Store records schema version.
- `runtime_response_items.model_call_id` is nullable.
- `runtime_response_items` requires source kind, provider/runtime namespace, item type, status or role when present, redaction/content state, source artifact reference, namespaced payload, provenance, and correlation status.
- Runtime item correlation status accepts only `uncorrelated`, `correlates_with`, `same_as_model_call`, `not_applicable`, and `unknown`.
- Observations require status, evidence class, reliability mode, content contract, source artifact reference, and value payload/provenance.
- Store insertion rejects undeclared status, evidence class, reliability mode, content contract, cost evidence mode, and comparability values when strict validation is enabled.
- Registry and rebuild tables support registry hash and source-set hash.
- No table requires provider-specific columns such as Codex `response_item` or Claude `parentUuid`.

Implementation notes:

- Use `sqlite3` from standard library.
- Prefer small helper functions and explicit DDL.
- Keep namespaced provider payloads as JSON text with validation at adapter/manifest layer.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark_store`

Commit boundary:

- `feat(model-benchmark): add telemetry SQLite cache skeleton`

## Task 04: Rebuild And Query Parity

Owner: single executor after Tasks 01, 02, and 03
Write set:

- `tooling/codex/model_benchmark/rebuild.py`
- `tooling/codex/model_benchmark/query.py`
- `tooling/codex/model_benchmark/reports.py`
- `tooling/codex/tests/test_model_benchmark_rebuild.py`
- `tooling/codex/tests/test_model_benchmark_report_parity.py`
- optional CLI wiring in `tooling/codex/model_benchmark/cli.py`

Goal:

- Prove registry/store/query/report parity on fixtures.

Test-first requirements:

- Rebuild stores registry hash and source-set hash.
- Query output includes registry hash and source-set hash.
- Report output includes registry hash and source-set hash.
- Registry hash mismatch fails strict query/report mode.
- Malformed JSONL source records parse diagnostics without raw content persistence.
- Rebuild is deterministic for the same fixture source set.
- Report input validation rejects undeclared status, evidence class, reliability mode, content contract, cost evidence mode, and comparability values in strict mode.

Implementation notes:

- Do not build a broad query language.
- A small query function returning structured dicts is enough.
- CLI wiring is optional; if added, keep commands fixture/local only.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark_rebuild`
- `python3 -m unittest tooling.codex.tests.test_model_benchmark_report_parity`

Commit boundary:

- `feat(model-benchmark): enforce telemetry rebuild query parity`

## Task 05: Fixture-Backed Codex Adapters

Owner: worker after Tasks 01, 02, 03
Write set:

- `tooling/codex/model_benchmark/adapters/__init__.py`
- `tooling/codex/model_benchmark/adapters/codex_sqlite.py`
- `tooling/codex/model_benchmark/adapters/codex_rollout.py`
- `tooling/codex/tests/test_model_benchmark_adapters.py`

Goal:

- Implement read-only adapters against synthetic fixtures, not home files.

Adapter outputs:

- sessions/thread entities
- subagent/entity edges
- turns
- runtime response items
- tool calls where structurally present
- token observations
- sandbox/approval/git/model/reasoning observations
- parse diagnostics

Test-first requirements:

- SQLite fixture produces session and subagent edge without reading sensitive title/first-message content.
- Rollout fixture produces runtime response items distinct from model calls.
- Runtime response items emitted by adapters include source kind, namespace, item type, redaction/content state, source artifact reference, provenance, namespaced payload, and correlation status.
- Adapter output validation rejects undeclared status, evidence class, reliability mode, content contract, cost evidence mode, and comparability values in strict mode.
- Compaction marker becomes a structural observation or runtime item with no content.
- Codex-specific field names are retained only in provider namespace/payload.
- Adapter does not open `~/.codex` in tests.

Implementation notes:

- Keep adapters pure and path-explicit.
- Use source artifact references and line numbers/hashes, not raw content.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark_adapters`

Commit boundary:

- `feat(model-benchmark): add fixture backed Codex telemetry adapters`

## Task 06: Provider-Neutrality Gate

Owner: single executor after Tasks 02, 03, 04, 05
Write set:

- `tooling/codex/tests/test_model_benchmark_provider_neutrality.py`
- optional helper code in `tooling/codex/model_benchmark/rebuild.py` or `query.py`

Goal:

- Make provider-neutrality a test gate, not a claim. The gate passes only under strict manifest/rebuild/query validation.

Test-first requirements:

- `manual_run_with_rubric_dimensions` passes through rebuild/query and emits rubric observations without canonical `score.overall`.
- `claude_local_jsonl_minimal_structure` passes through source/artifact parsing without Codex fields and proves malformed-line diagnostics plus redaction states.
- `provider_denominator_mismatch` preserves cache/reasoning/cost evidence differences.
- A Codex-only fixture run cannot set a provider-neutrality flag or report claim.
- The provider-neutrality gate fails if strict manifest validation, rebuild hash recording, or query hash propagation is bypassed.

Implementation notes:

- This can be a test-only gate at first.
- Do not implement full Claude or API adapters unless required to parse the synthetic fixture shape.
- The gate must prove strict manifest/rebuild/query validation, not just fixture file existence.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark_provider_neutrality`

Commit boundary:

- `test(model-benchmark): enforce provider neutrality fixture gate`

## Task 07: Rubric Observation Migration

Owner: single executor after Tasks 01, 03, and 04
Write set:

- `tooling/codex/model_benchmark/schema.py`
- `tooling/codex/model_benchmark/reports.py`
- `tooling/codex/tests/test_model_benchmark.py`
- optional: `tooling/codex/model_benchmark/rubrics.py`

Goal:

- Keep current run JSONL compatibility while introducing canonical multidimensional rubric observations.

Test-first requirements:

- Existing `score.overall` is accepted only as legacy compatibility.
- New rubric observation records validate dimension, evaluator, rubric version, value/status, evidence, reliability, and provenance.
- Reports prefer rubric dimension summaries when available.
- Reports that render legacy overall score label it as compatibility-only.
- New canonical metric declarations named `score.overall` or `core.quality.overall` are rejected by manifest validation.

Implementation notes:

- Avoid breaking existing tests until replacement coverage exists.
- Keep aggregate view computations report-only.

Focused verification:

- `python3 -m unittest tooling.codex.tests.test_model_benchmark`
- `python3 -m unittest tooling.codex.tests.test_model_benchmark_manifest`
- `python3 -m unittest tooling.codex.tests.test_model_benchmark_report_parity`

Commit boundary:

- `feat(model-benchmark): add rubric observation compatibility path`

## Task 08: Final Integration Gate

Owner: coordinator or verification worker
Write set:

- `.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/VERIFICATION.md`

Goal:

- Verify the first slice is complete and does not overclaim. This task is report-only. If verification fails, route fixes back to the owning implementation task instead of editing source or tests here.

Required verification:

```bash
python3 -m unittest tooling.codex.tests.test_model_benchmark
python3 -m unittest tooling.codex.tests.test_model_benchmark_manifest
python3 -m unittest tooling.codex.tests.test_model_benchmark_fixtures
python3 -m unittest tooling.codex.tests.test_model_benchmark_store
python3 -m unittest tooling.codex.tests.test_model_benchmark_rebuild
python3 -m unittest tooling.codex.tests.test_model_benchmark_report_parity
python3 -m unittest tooling.codex.tests.test_model_benchmark_adapters
python3 -m unittest tooling.codex.tests.test_model_benchmark_provider_neutrality
git diff --check
```

If implementation touches broader portable-runtime or bootstrap surfaces, also run:

```bash
bash scripts/ci/check-deterministic.sh
bash scripts/ci/check-bootstrap.sh
```

Acceptance criteria:

- No live provider calls.
- No provider config mutation.
- No raw private content in fixtures, observations, or reports.
- Registry hash and source-set hash are visible in rebuild/query/report outputs.
- `runtime_response_items` remains distinct from `model_calls`.
- `telemetry_events` remains optional/absent from required first-slice schema.
- Provider-neutrality gate prevents Codex-only neutrality claims.
- `score.overall` is legacy/view-only.

Commit boundary:

- `test(model-benchmark): verify telemetry first slice integration`

## Delegation Prompts

### Worker Prompt Template

Use this template for GPT-5.5 medium executor workers:

```text
You are implementing Task <N> from:
.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/PLAN.md

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
5. Run `git diff --check`.
6. Return changed files, verification commands, and any unresolved questions.

Constraints:
- No live provider calls.
- No provider config mutation.
- No raw private transcript content.
- No provider-neutrality claim unless the explicit fixture gate passes.
```

### Verification Worker Prompt

```text
You are verifying the telemetry substrate first slice against:
.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/PLAN.md

This is report-only verification. You may write only:
.planning/measurement/model-role-benchmark/implementation-plans/20260424T061025Z/VERIFICATION.md

Do not edit source, tests, fixtures, manifests, or reports. Run the required verification commands, inspect whether the acceptance criteria are satisfied, and write a concise report with pass/fail, evidence, and blockers. Route any failures back to the owning implementation task listed in the plan.
```

## Stop Conditions

Stop and ask for coordinator decision if:

- A task needs a dependency not already in the repo.
- A worker believes `telemetry_events` must become mandatory.
- A worker needs live provider data or home-level logs.
- A worker wants to store raw content.
- A worker finds the first-slice schema cannot support the provider-neutrality gate.
- Existing benchmark compatibility requires breaking current CLI behavior.

## Commit Strategy

- Commit each task separately.
- Keep generated fixtures and source changes in the same commit only when inseparable.
- Do not bundle research/planning artifacts with implementation code.
- If multiple workers run in parallel, integrate one commit at a time after review.
