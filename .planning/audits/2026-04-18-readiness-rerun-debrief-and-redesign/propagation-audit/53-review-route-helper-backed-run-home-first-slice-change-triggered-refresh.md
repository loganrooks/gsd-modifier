Date: 2026-04-22
Status: active change-triggered refresh

# Review Route Helper-Backed Run-Home First Slice Change-Triggered Refresh

## Trigger

- [e:c+i] The review-workflow family now lands one helper-backed first slice through [145-gsd-review-helper-backed-run-home-first-slice-implementation.md](../intervention-proposals/145-gsd-review-helper-backed-run-home-first-slice-implementation.md).

## Carriers Refreshed

- [d:r:i] helper carrier:
  - `harness_modifier/capture/run_review_reviewer.py`
  - `tooling/codex/run_review_reviewer.py`
- [d:r:i] workflow carrier:
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md`
- [d:r:i] wrapper carrier:
  - `tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md`
- [d:r:i] test carrier:
  - `tooling/codex/tests/test_run_review_reviewer.py`
  - `tooling/codex/tests/test_review_route_contract.py`

## Consumer Chain Kept Explicit

- [d:r:i] producer-side review run artifacts now widen before synthesis:
  - durable run-home
  - launch-truth
  - timing
  - reviewer-state classification
  - bounded salvage
- [d:r:i] planner-facing consumer remains stable:
  - `{padded_phase}-REVIEWS.md`
  - `Review Consumer Contract`
  - `plan-phase.md` `--reviews`
  - planner / plan-checker / revision loop reread surfaces

## Held Later

- [d:r:i] subject-keyed review-route splits
- [d:r:i] retry / resume beyond bounded salvage
- [d:r:i] larger telemetry or routing system
- [d:r:i] wider parity/materialization redesign inside this family
