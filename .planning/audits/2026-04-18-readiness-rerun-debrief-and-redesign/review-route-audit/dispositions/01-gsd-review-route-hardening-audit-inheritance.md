Date: 2026-04-22
Status: completed local inheritance

# GSD Review Route Hardening Audit Inheritance

## Local Disposition

- [d:r:i] `accept with in-place hardening and helper-backed first slice`
- [d:r:i] Keep `$gsd-review` as the primary route.
- [d:r:i] Do not fork a sibling review-route family yet.
- [d:r:i] The route already owns a load-bearing planner consumer contract through `{phase}-REVIEWS.md`; the stronger move is to widen the runner / artifact / salvage layer underneath that contract rather than churn the consumer surface first.

## Carry Forward

- [d:r:i] Keep reviewer-shape differences explicit:
  - Claude stream-json + last-message salvage
  - Codex `codex exec` + `capture_launch_truth.py`
  - plain-stdout reviewers with launch-truth-lite only
- [d:r:i] Keep the first-slice helper narrow:
  - invocation
  - run-home writes
  - launch-truth and timing capture
  - `complete` / `partial` / `absent` classification
  - last-message salvage where the runner shape supports it
- [d:r:i] Keep workflow ownership explicit:
  - reviewer selection
  - prompt assembly
  - `REVIEWS.md` synthesis
  - Review Consumer Contract
- [d:r:i] Keep the run-home explicit at:
  - `.planning/phases/{padded_phase}/reviews/{run_id}/`
- [d:r:i] Keep the first live slice bounded to `.codex` and `.claude` as the primary local horizon while still allowing plain-stdout reviewers to inherit the simpler run-home discipline.

## Land Next

- [d:r:i] New helper:
  - `tooling/codex/run_review_reviewer.py`
- [d:r:i] Focused tests:
  - helper classification and salvage fixtures
  - launch-truth source split for Claude versus Codex
  - `review.md` contract coverage after the route stops using `/tmp` as the canonical artifact home
- [d:r:i] Workflow and wrapper follow-through:
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md`
  - `tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md`
- [d:r:i] Pair the implementation with:
  - one propagation `change-triggered-refresh`
  - one timing-calibrated real acceptance run

## Keep Explicitly Later

- [d:r:i] Subject-keyed review-route splitting
- [d:r:i] Retry / resume logic beyond last-message salvage
- [d:r:i] A larger telemetry or reviewer-routing system
- [d:r:i] `.claude` materialization widening or runtime-parity redesign inside this family
- [d:r:i] Cross-repo extraction/distribution of the helper layer

## Governance Consequence

- [d:r:i] The review-route family should now be visible in governed state as:
  - one completed widening lane
  - one accepted helper-backed in-place hardening next move
- [d:r:i] The broader workspace-state reread should inherit this family as one example of a route where:
  - external-lane timing created a usable local work window
  - audit findings sharpened not only a first implementation slice but also later adjacent uplift routes

## Exact Next Move

1. [d:r:i] Land the helper-backed first slice for `$gsd-review` in place.
2. [d:r:i] Pair it with focused tests plus one propagation refresh.
3. [d:r:i] Then open the broader workspace-state / horizon-inheritance / parallelization audit from the cleaner governed baseline rather than from pre-inheritance chat memory.
