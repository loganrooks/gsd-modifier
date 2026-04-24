Date: 2026-04-22
Status: active bounded proposal

# GSD Review Helper-Backed Run-Home First Slice Proposal

## Purpose

- [g:r:i] Turn the completed `review-route-audit` widening lane into one concrete local first slice instead of leaving the family as audit-only doctrine.
- [g:r:i] Harden `$gsd-review` in place through a helper-backed run-home / launch-truth / timing / salvage layer while keeping the existing `REVIEWS.md` planner-consumer contract stable.

## Why This Proposal Exists Now

- [e:c+i] The widening lane is already completed and inherited. It no longer leaves the family at “cross-vendor reviews are useful” or “the route could be improved.” It names one explicit first live slice. Sources:
  - [../review-route-audit/outputs/01-gsd-review-route-hardening-audit-opus47-max-r1.md](../review-route-audit/outputs/01-gsd-review-route-hardening-audit-opus47-max-r1.md)
  - [../review-route-audit/dispositions/01-gsd-review-route-hardening-audit-inheritance.md](../review-route-audit/dispositions/01-gsd-review-route-hardening-audit-inheritance.md)
- [e:c+i] The current route still collapses reviewer shapes into one thin `/tmp` and stdout-only pattern inside [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:156) while the repo now already carries stronger lane-home, launch-truth, timing-calibration, and salvage doctrine elsewhere.
- [d:r:i] The current user pressure is sharper too:
  - crossing over to different review targets should remain explicit
  - logging and launch truth should be durable
  - last recoverable messages should not disappear when a run fails
  - timing windows should support better parallel overlap instead of idle waiting

## First-Slice Boundary

- [d:r:i] Keep `$gsd-review` as the primary route.
- [d:r:i] Do not fork a sibling review-route family yet.
- [d:r:i] Do not change the downstream `REVIEWS.md` / `Review Consumer Contract` structure in this slice.
- [d:r:i] Put the widening under the runner and artifact layer:
  - per-run home
  - per-reviewer artifacts
  - requested/effective launch truth where the runner shape supports it
  - timing estimate / actual / calibration
  - `complete` / `partial` / `absent` reviewer state
  - last-message salvage where the runner shape supports it

## Proposed First-Slice Surfaces

- [d:r:i] new helper:
  - `tooling/codex/run_review_reviewer.py`
- [d:r:i] workflow and wrapper follow-through:
  - [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
  - [gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md)
- [d:r:i] focused tests:
  - helper classification and salvage fixtures
  - launch-truth source split for Claude versus Codex
  - review-route contract coverage after the route stops treating `/tmp` as the canonical home
- [d:r:i] one propagation refresh:
  - review producer -> `REVIEWS.md` -> planner / plan-checker / revision-loop / `--reviews` consumer chain

## Reviewer Shape Split

- [d:r:i] `claude`
  - stream-json capable
  - last-message salvage from stream
  - effective launch truth from stream/result metadata
- [d:r:i] `codex`
  - requested/effective launch truth from `capture_launch_truth.py`
  - first slice may keep plain stdout as the main review body artifact
  - no fake stream requirement in this slice
- [d:r:i] `plain-stdout reviewers`
  - invocation string
  - exit code
  - byte count
  - elapsed
  - no fake stream or fake parity claims

## Run-Home Shape

- [d:r:i] Canonical per-run home:
  - `.planning/phases/{padded_phase}/reviews/{run_id}/`
- [d:r:i] Canonical first-slice artifacts inside that home:
  - `prompt.md`
  - `{reviewer}.stdout.md` or `{reviewer}.stream.jsonl` where applicable
  - `{reviewer}.stderr.log`
  - `launch-truth/{reviewer}.md`
  - `timing.md`
  - optional classification/salvage note if the reviewer is `partial` or `absent`
- [d:r:i] Keep `{padded_phase}-REVIEWS.md` in the phase directory as the stable downstream consumer artifact.

## What This Proposal Should Settle

- [d:r:i] whether the helper-backed first slice should be implemented now on the current route rather than reopened as another widening lane
- [d:r:i] what the first helper must own directly versus what remains in workflow orchestration
- [d:r:i] what review-run artifacts become durable and canonical
- [d:r:i] how much salvage belongs in the first slice without widening into retry/resume machinery

## Propagation Obligations

- [d:r:i] `review.md`
- [d:r:i] `gsd-review/SKILL.md`
- [d:r:i] `planner-reviews.md`
- [d:r:i] `plan-phase.md` `--reviews` consumer assumptions
- [d:r:i] governed docs that describe the review-route family
- [d:r:i] review-route audit subtree status/read surfaces
- [d:r:i] timing/launch-truth operator doctrine if the route now inherits it directly

## Verification And Review Gates

- [d:r:i] focused helper tests
- [d:r:i] at least one dry-run or fixture-backed assembly path for route artifacts
- [d:r:i] one real acceptance run on the `.codex` / `.claude` primary horizon after the helper lands
- [d:r:i] propagation refresh note
- [d:r:i] governed-state update

## Held Later

- [d:r:i] subject-keyed review-route splitting by review target
- [d:r:i] retry / resume logic beyond last-message salvage
- [d:r:i] telemetry or larger reviewer-routing system
- [d:r:i] broader parity widening or `.claude` materialization redesign inside this family
- [d:r:i] cross-repo extraction/distribution of the review helper layer

## Exact Next Move

1. [d:r:i] Accept this first-slice proposal as the current local route for the review-workflow family.
2. [d:r:i] Implement `tooling/codex/run_review_reviewer.py` plus the bounded workflow / wrapper / test follow-through.
3. [d:r:i] Pair that implementation with one propagation refresh and one timing-calibrated real acceptance run.
