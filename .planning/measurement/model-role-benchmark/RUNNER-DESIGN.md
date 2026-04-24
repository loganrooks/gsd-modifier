# Model Role Benchmark Runner Design

## Boundary

This document defines the current manual-ingest layer and the later executable
harness. Live execution adapters are not implemented in this slice.

Proposed code location:

- `tooling/codex/model_benchmark/`

Proposed output location:

- `.planning/measurement/model-role-benchmark/runs/<timestamp>/`

Current implemented code:

- `tooling/codex/model_benchmark/schema.py`
- `tooling/codex/model_benchmark/profiles.py`
- `tooling/codex/model_benchmark/io.py`
- `tooling/codex/model_benchmark/costs.py`
- `tooling/codex/model_benchmark/reports.py`
- `tooling/codex/model_benchmark/cli.py`

This implementation is ingest-only. It validates manually collected run records,
checks candidate-profile consistency, attaches sourced API-equivalent cost
estimates, and summarizes already-recorded runs. It does not launch Codex,
Claude, API, or paid/quota-consuming model runs.

## Candidate Profile Schema

```json
{
  "profile_id": "55-high",
  "model": "gpt-5.5",
  "reasoning_effort": "high",
  "role_family": "planner|executor|reviewer|researcher|general"
}
```

First matrix:

- `54-medium`: `gpt-5.4`, `medium`
- `54-high`: `gpt-5.4`, `high`
- `54-xhigh`: `gpt-5.4`, `xhigh`
- `55-low`: `gpt-5.5`, `low`
- `55-medium`: `gpt-5.5`, `medium`
- `55-high`: `gpt-5.5`, `high`

The `55-low` and `55-medium` profiles are explicit execution-cost hypotheses. They must be scored against the same fixtures as higher-reasoning profiles before any default-setting change.

The default ingest registry currently contains exactly these six profiles. A run
whose `candidate_profile`, `model`, or `reasoning_effort` conflicts with the
registry is invalid for comparison rather than a soft warning. Legacy profile
records that use `role_family` normalize to `role_families` so older design text
and current ingest files remain compatible.

## Task Spec Schema

```json
{
  "task_id": "EXEC-001",
  "role_family": "executor",
  "prompt_variant": "high-specificity",
  "fixture": "contract-change-small",
  "prompt_file": "prompts/EXEC-001-high.md",
  "allowed_write_scope": ["src/config_contract.py", "tests/test_config_contract.py"],
  "success_checks": ["python3 -m unittest discover -s tests"],
  "rubric_dimensions": ["correctness", "plan_adherence", "minimal_diff", "verification", "restraint"]
}
```

## Run Record Schema

```json
{
  "run_id": "2026-04-23T210000Z_EXEC-001_55-high",
  "task_id": "EXEC-001",
  "candidate_profile": "55-high",
  "model": "gpt-5.5",
  "reasoning_effort": "high",
  "codex_version": "0.124.0",
  "requested_model": "gpt-5.5",
  "effective_model": "not_available",
  "requested_reasoning_effort": "high",
  "effective_reasoning_effort": "not_available",
  "started_at": "2026-04-23T21:00:00Z",
  "ended_at": "2026-04-23T21:05:00Z",
  "elapsed_seconds": 300,
  "git_baseline": "abc1234",
  "status": "completed",
  "access_preflight": {
    "surface": "cli|desktop|ide|subagent|not_available",
    "account_tier": "not_recorded",
    "client_version": "not_available",
    "model_selector_state": "not_available",
    "launch_result": "not_run|launched|access_failed|metadata_missing|model_not_found",
    "failure_class": "not_available"
  },
  "usage": {
    "input_tokens": "not_available",
    "cached_input_tokens": "not_available",
    "output_tokens": "not_available",
    "reasoning_tokens": "not_available",
    "initialization_tokens": "not_available",
    "tool_result_tokens": "not_available",
    "quota_delta": "not_available",
    "status_before": "not_available",
    "status_after": "not_available",
    "usage_metric_status": "not_available"
  },
  "telemetry_features": {
    "trace_id": "not_available",
    "parent_trace_id": "not_available",
    "runtime_provider": "codex_cli|claude_code|api|manual|not_available",
    "agent_role": "executor|planner|reviewer|researcher|general|not_available",
    "intervention_id": "not_available",
    "metric_granularity": "run",
    "provenance": "not_available",
    "derived_feature_version": "not_available"
  },
  "artifacts": {
    "prompt": "prompt.md",
    "response": "response.md",
    "diff": "diff.patch",
    "test_output": "tests.txt",
    "score": "score.json"
  }
}
```


## Usage And Reasoning Accounting

Cost and usage comparisons must keep reasoning effort visible. A lower-reasoning `gpt-5.5` execution profile can only be judged fairly if the runner preserves:

- input, cached-input, output, reasoning, initialization, and tool-result token categories separately
- whether each metric is `measured`, `estimated`, `derived`, or `not_available`
- retry-adjusted cost and verification-adjusted cost, not only first-attempt cost
- the pricing table source, retrieval time, currency, effective date, and provider-specific reasoning-token rule
- the caveat that API-equivalent cost is not direct ChatGPT/Codex plan quota burn

If a provider reports total tokens without a reasoning-token split, preserve the total and mark the split `not_available`. Never infer zero reasoning tokens from absent data.

## Manual Ingest Protocol

Manual benchmark records are newline-delimited JSON objects. Use JSONL so
completed, failed, partial, and routing-unproven runs can be appended and
validated independently without overwriting prior evidence.

Validation:

```bash
python3 -m tooling.codex.model_benchmark.cli validate-runs \
  --runs path/to/runs.jsonl \
  --profiles path/to/profiles.json
```

The `--profiles` argument is optional. When omitted, the CLI uses the built-in
six-profile matrix from this document. Validation preserves unknown top-level
and telemetry fields, but normalizes known usage categories to explicit values.
Missing token categories become `not_available`; negative or boolean token
values fail validation.

Cost estimation:

```bash
python3 -m tooling.codex.model_benchmark.cli estimate-costs \
  --runs path/to/runs.jsonl \
  --rates path/to/rates.json \
  --output path/to/estimated.jsonl
```

The rate table must include `model`, `currency`, `source_url`, `retrieved_at`,
and `effective_date`. The first committed tests use synthetic `example.test`
pricing metadata only. Synthetic fixtures are not benchmark evidence and should
stay under `tooling/codex/tests/`, not under
`.planning/measurement/model-role-benchmark/runs/`. Real pricing tables must cite
official sources and retrieval dates before they are used for decision evidence.

Cost output is API-equivalent only. It is not direct ChatGPT, Claude, or Codex
plan quota burn. If any token category or required rate is missing, the estimate
is `partial`; if no token categories are available, it is `not_available`.

Summaries:

```bash
python3 -m tooling.codex.model_benchmark.cli summarize-runs \
  --runs path/to/estimated.jsonl \
  --output path/to/summary.json
```

Summaries group by `task_id`, `candidate_profile`, and `reasoning_effort`. They
include qualitative-only counts, partial-cost counts, score averages when
present, known-token averages, and reasoning-token aggregates when available.
They intentionally do not rank profiles, declare a global winner, or imply any
production default change.

The CLI refuses to overwrite outputs unless `--overwrite` is supplied. This is
part of the evidence-preservation rule: reruns should usually write a new output
artifact or deliberately replace a disposable derived file.

## Future Telemetry Horizon

The benchmark record is the seed of a broader harness telemetry system. This slice only implements ingest and comparison helpers, but the schema reserves fields for later telemetry that can inform harness design and config decisions:

- intervention tracking for model, reasoning, prompt, delegation, tool, workflow, and config changes
- friction markers such as retries, interruptions, user corrections, approval loops, stalled runs, false completion, and scope creep
- efficiency features such as tokens per tool call, tokens per accepted diff, initialization tokens, compaction frequency, and estimated delegation savings
- responsibility tracing across session, run, task, turn, agent, tool-call, file/diff, config-profile, and intervention-window levels
- semantic/friction analyzers that may later identify frustration or repeated points of failure, with versioned feature extractors and auditable provenance

The initial implementation must not hard-code a cost-only worldview. Cost is one feature among quality, reliability, friction, traceability, and intervention effectiveness.

Current ingest validation preserves unknown run-record and telemetry keys so
future adapters can add intervention, friction, delegation-economics,
responsibility-tracing, and semantic-friction features without changing the
basic run-record contract first.

## Runner Flow

1. Load candidate profiles and task specs.
2. Create a disposable worktree or temp repo copy for each execution run.
3. Start Codex with explicit model and reasoning overrides when the CLI supports both.
4. Capture requested settings before launch.
5. Capture effective settings from runtime evidence when available.
6. Capture access preflight, quota/status before, and effective context evidence where available.
7. Preserve raw response, diff, test output, and run metadata.
8. Score outputs with the rubric.
9. Write a run summary and leave raw artifacts intact.

## Requested-Vs-Effective Discipline

Do not trust requested model settings as proof of effective runtime settings. The runner must record:

- `requested_model`
- `effective_model`
- `requested_reasoning_effort`
- `effective_reasoning_effort`
- `effective_settings_source`

Allowed `effective_settings_source` values:

- `state_sqlite`
- `codex_log`
- `model_cache`
- `self_report`
- `not_available`

If effective settings cannot be proven, record `not_available` and keep the run usable only for qualitative review.

Allowed run status values:

- `completed`
- `access_failed`
- `routing_unproven`
- `quota_blocked`
- `execution_failed`
- `verification_failed`

## Safety Rules

- Never print or store auth tokens.
- Never run execution tasks against the live dirty worktree.
- Never treat reviewer self-scoring as final scoring.
- Never overwrite prior runs; use timestamped run directories.
- Preserve failed runs because failures are evidence.
- Never treat missing token categories as zero usage.
- Never compare lower-reasoning profiles without preserving reasoning-token visibility or explicit `not_available` markers.

## Future Implementation Notes

The runner should prefer standard-library Python for the first implementation. It can reuse existing measurement-provenance conventions from `harness_modifier/closure/`, but should not force model benchmark records into host-exercise observation schemas unless the schema is extended deliberately.

Live Codex and Claude execution adapters remain deferred. When implemented, they
must normalize their output into the same run-record contract used by manual
ingest and must keep requested settings separate from effective routing evidence.
