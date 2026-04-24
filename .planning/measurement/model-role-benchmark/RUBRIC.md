# Model Role Benchmark Rubric

## Score Scale

Use a 0-4 scale for each dimension.

| Score | Meaning |
| --- | --- |
| 0 | Fails the task or fabricates key facts |
| 1 | Partially useful but unsafe or incomplete |
| 2 | Adequate result with notable gaps |
| 3 | Strong result with minor issues |
| 4 | Excellent result that is ready to use or nearly ready |

## Shared Dimensions

| Dimension | What To Score |
| --- | --- |
| Correctness | Does the output satisfy the requested task against observable repo or fixture facts? |
| Grounding | Does it use the right local sources and avoid unsupported claims? |
| Scope Control | Does it avoid unrelated work, unapproved rewrites, and hidden expansion? |
| Auditability | Can a later reviewer reconstruct evidence, decisions, assumptions, and uncertainty? |
| Efficiency | Token usage, elapsed time, tool count, retries, and unnecessary context loading |
| Reasoning-Cost Efficiency | Reasoning-token spend, retry-adjusted estimated cost, and cost per successful/verified task |
| Telemetry Readiness | Whether the run preserves enough provenance and granularity for later harness/config decisions |

## Planning Dimensions

| Dimension | What To Score |
| --- | --- |
| Decomposition | Produces implementable tasks with clear dependencies and write boundaries |
| Ambiguity Handling | Names assumptions and asks or defers only when needed |
| Propagation Awareness | Identifies producers, consumers, runtime carriers, docs mirrors, and measurement outputs |
| Decision Completeness | Leaves no avoidable decisions to the implementer |

## Execution Dimensions

| Dimension | What To Score |
| --- | --- |
| Plan Adherence | Follows the provided plan and records real deviations |
| Minimal Diff | Changes only needed files and preserves surrounding style |
| Verification | Runs or names appropriate checks and reports results truthfully |
| Restraint | Avoids freelancing, speculative cleanup, and unrelated refactors |

## Review And Audit Dimensions

| Dimension | What To Score |
| --- | --- |
| True Positives | Finds seeded real issues |
| False Positives | Avoids inflating non-issues |
| Severity Calibration | Ranks findings by actual risk |
| Recommendation Quality | Gives concrete, bounded, reviewable fixes |
| Uncertainty Handling | Separates evidence, inference, and unknowns |

## Metrics To Capture

Each run should record:

- `candidate_profile`
- `task_id`
- `prompt_variant`
- `model`
- `reasoning_effort`
- `codex_version`
- `started_at`
- `ended_at`
- `elapsed_seconds`
- `session_id` or `thread_id` when available
- `git_baseline`
- `status`
- `tests_run`
- `tests_passed`
- `diff_stat`
- `tool_call_count` when available
- `input_tokens`, `cached_input_tokens`, `output_tokens`, `reasoning_tokens`, `initialization_tokens`, and `tool_result_tokens` when available
- `usage_metric_status`: `measured`, `estimated`, `derived`, or `not_available`
- `trace_id`, `parent_trace_id`, `runtime_provider`, `intervention_id`, `metric_granularity`, and `derived_feature_version` when available

## Review Process

Use blind or semi-blind scoring when practical:

- Hide candidate profile during human scoring when outputs can be anonymized.
- Score seeded-defect tasks against an answer key before reading model self-assessments.
- Record scorer notes separately from numeric scores.
- Preserve raw outputs and diffs so later auditors can rescore.

## Decision Use

Do not use a single aggregate score to choose profiles. Compare by role:

- Executor defaults should prioritize correctness, restraint, and verification over prose quality.
- Planner defaults should prioritize ambiguity handling, decomposition, and propagation awareness.
- Reviewer defaults should prioritize true positives, severity calibration, and false-positive control.
- Usage metrics should influence default choices only after quality is acceptable.
- Lower-reasoning model profiles should be evaluated on quality first, then reasoning-token-adjusted total cost and friction.
