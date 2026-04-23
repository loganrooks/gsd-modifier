# Model Role Benchmark Runner Design

## Boundary

This document defines the later executable harness. It is not implemented in this slice.

Proposed code location:

- `tooling/codex/model_benchmark/`

Proposed output location:

- `.planning/measurement/model-role-benchmark/runs/<timestamp>/`

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

- `54-high`: `gpt-5.4`, `high`
- `54-xhigh`: `gpt-5.4`, `xhigh`
- `55-high`: `gpt-5.5`, `high`

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
  "usage": {
    "input_tokens": "not_available",
    "output_tokens": "not_available",
    "reasoning_tokens": "not_available",
    "usage_metric_status": "not_available"
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

## Runner Flow

1. Load candidate profiles and task specs.
2. Create a disposable worktree or temp repo copy for each execution run.
3. Start Codex with explicit model and reasoning overrides when the CLI supports both.
4. Capture requested settings before launch.
5. Capture effective settings from runtime evidence when available.
6. Preserve raw response, diff, test output, and run metadata.
7. Score outputs with the rubric.
8. Write a run summary and leave raw artifacts intact.

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

## Safety Rules

- Never print or store auth tokens.
- Never run execution tasks against the live dirty worktree.
- Never treat reviewer self-scoring as final scoring.
- Never overwrite prior runs; use timestamped run directories.
- Preserve failed runs because failures are evidence.

## Future Implementation Notes

The runner should prefer standard-library Python for the first implementation. It can reuse existing measurement-provenance conventions from `harness_modifier/closure/`, but should not force model benchmark records into host-exercise observation schemas unless the schema is extended deliberately.
