# Model Role Benchmark Predictions

## Frame

These predictions are pre-registered before local experiments. They should be evaluated against local task results, public benchmark evidence, and qualified user reports.

Candidate profiles for the first matrix:

| Profile ID | Model | Reasoning | Intended comparison role |
| --- | --- | --- | --- |
| `54-high` | `gpt-5.4` | `high` | Current conservative baseline for general agent work |
| `54-xhigh` | `gpt-5.4` | `xhigh` | Reasoning-depth uplift without changing model generation |
| `55-high` | `gpt-5.5` | `high` | New stronger-model candidate without max reasoning cost |

## Primary Predictions

| ID | Prediction | Expected winner | Evidence needed |
| --- | --- | --- | --- |
| `P-EXEC-001` | For bounded execution from explicit plans, `gpt-5.4 high` will be close enough to `gpt-5.5 high` that defaulting executors to 5.5 is not justified. | `54-high` or tie | Equal test pass rate, lower or comparable overreach, materially lower usage cost |
| `P-PLAN-001` | For underspecified planning and architecture tasks, `gpt-5.5 high` will produce better decomposition, assumption handling, and propagation awareness than both 5.4 profiles. | `55-high` | Higher rubric score on ambiguity handling, downstream task quality, and auditability |
| `P-REVIEW-001` | For review and audit tasks, `gpt-5.5 high` will find more non-obvious contract and propagation issues without a proportional false-positive increase. | `55-high` | Higher true-positive count and stronger issue framing with controlled false positives |
| `P-REASON-001` | `gpt-5.4 xhigh` will improve some planning/review quality over `gpt-5.4 high`, but will not consistently match `gpt-5.5 high` on open-ended tasks. | `55-high` | Better open-task scores for 5.5 despite lower reasoning setting |
| `P-USAGE-001` | `gpt-5.5 high` may use fewer tokens on hard tasks, but not enough to assume better value for routine execution without local measurements. | Underdetermined | Token usage, wall time, retry count, and quota-burn anecdotes kept separate |

## Decision Thresholds

Do not change production defaults unless the evidence shows one of these outcomes:

- Executor promotion: `55-high` beats `54-high` on execution quality by at least one full rubric tier without higher overreach or materially worse usage.
- Planner/reviewer promotion: `55-high` shows repeated improvement on ambiguity, propagation, and issue quality across at least two task families.
- Reasoning uplift: `54-xhigh` beats `54-high` enough to justify xhigh for a specific role when `55-high` is unavailable or usage-limited.
- No-change result: If improvements are concentrated in open tasks only, keep `54-high` as the default executor profile and reserve `55-high` for deep roles.

## Known Threats To Validity

- Launch-period GPT-5.5 access and usage behavior may be unstable.
- Single-run comparisons are not enough; repeated runs or task diversity are needed.
- Human scoring can bias toward more confident prose unless the rubric penalizes unsupported claims.
- Token usage may not be directly visible for every Codex run; missing metrics must be recorded as `not_available`.
