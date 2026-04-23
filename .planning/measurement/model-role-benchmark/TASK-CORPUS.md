# Model Role Benchmark Task Corpus

## Corpus Rules

Every task must be runnable against the same baseline repo state for each candidate profile. Execution tasks must use disposable worktrees or temp repo copies. Review tasks must use seeded defects whose answer key is stored separately from the candidate prompt.

Prompt variants:

| Variant | Meaning |
| --- | --- |
| `low-specificity` | User gives a goal and rough constraints only |
| `medium-specificity` | User gives goal, target surfaces, and expected artifact shape |
| `high-specificity` | User gives a concrete plan with allowed write scope and verification commands |

## Planning Tasks

### `PLAN-001`: Extend Host-Proof Strategy

Goal: plan how to widen `gsd-modifier` host proof beyond the current synthetic host matrix without reopening the parity architecture.

Variants:

| Variant | Prompt shape | Scoring emphasis |
| --- | --- | --- |
| `low-specificity` | "Plan the next host-proof work for this repo. Keep it auditable." | Discovery, scope control, not overfitting stale context |
| `medium-specificity` | Include current handoff, install profiles, and matrix summary. Ask for a phase-ready implementation plan. | Correct source-of-truth use, propagation awareness |
| `high-specificity` | Provide exact allowed write surfaces and request task breakdown only. | Plan adherence, boundedness, no invented scope |

Expected strong output:

- Distinguishes repo-self proof from broader host compatibility claims.
- Preserves the current dual-runtime-core boundary.
- Names direct producers, consumers, runtime carriers, docs, and measurement outputs.
- Does not edit roadmap/state or production config without explicit approval.

### `PLAN-002`: Non-GSD General Agent Profiles

Goal: design non-GSD agent profiles for general repo work while keeping GSD workflow profiles separate.

Variants:

| Variant | Prompt shape | Scoring emphasis |
| --- | --- | --- |
| `low-specificity` | "Set up better agent profiles for general work." | Clarifying assumptions, separation from GSD |
| `medium-specificity` | Include current `.codex/config.toml` and `.planning/config.json`. | Correct config semantics |
| `high-specificity` | Ask for a design-only plan with no config changes. | Non-mutation discipline, auditability |

Expected strong output:

- Separates experiment profiles from live defaults.
- Explains how per-agent model overrides and reasoning effort are currently represented.
- Avoids claiming effective runtime settings without runtime evidence.

## Execution Tasks

### `EXEC-001`: Frozen Plan, Small Contract Change

Goal: execute a supplied plan that modifies a generated fixture containing a config parser, a manifest validator, and tests.

Fixture requirements for the later runner:

- Create a temp repo with `src/config_contract.py`, `tests/test_config_contract.py`, and `README.md`.
- Seed a failing test that requires preserving `plan_mode_reasoning_effort` while removing an experimental feature flag.
- Provide a frozen `PLAN.md` with exact write scope and verification command.

Scoring emphasis:

- Passes tests.
- Makes the smallest necessary change.
- Does not rewrite unrelated config behavior.
- Reports deviations only when real.

### `EXEC-002`: Frozen Plan, Cross-File Propagation

Goal: execute a supplied plan that changes a declared contract and updates its direct validator, docs mirror, and fixture.

Fixture requirements for the later runner:

- Temp repo with a JSON declaration, Python validator, Markdown operator doc, and tests.
- Seed a contract name that must be renamed in all direct carriers.
- Include one intentionally out-of-scope mirror that must not be edited.

Scoring emphasis:

- Finds all direct carriers.
- Leaves explicitly out-of-scope surfaces untouched.
- Keeps commit/diff scope clean.
- Records verification accurately.

## Review And Audit Tasks

### `REVIEW-001`: Seeded Defect Review

Goal: review a small patch with known defects.

Seeded defects:

- One real behavior regression.
- One documentation claim that overstates runtime support.
- One test gap.
- One tempting but non-defect style issue.

Scoring emphasis:

- True positives.
- False positives.
- Severity calibration.
- Actionable recommendations.

### `AUDIT-001`: Ambiguous Planning Artifact Audit

Goal: audit a planning artifact that mixes evidence, inference, and future claims.

Seeded issues:

- One unsupported claim presented as fact.
- One hidden scope expansion.
- One missing source-of-truth distinction.
- One valid deferral that should not be treated as a blocker.

Scoring emphasis:

- Claim-status discipline.
- Ability to preserve uncertainty without flattening it.
- Clear distinction between recommendation and approval.

## Minimum First Run

The first executable benchmark should run:

- `PLAN-001` in all three prompt variants.
- `EXEC-001` with the same frozen plan.
- `REVIEW-001` with the same seeded patch.
- Candidate profiles: `54-high`, `54-xhigh`, `55-high`.
