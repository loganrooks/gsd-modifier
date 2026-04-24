Date: 2026-04-22
Status: active implementation note

# GSD Review Helper-Backed Run-Home First Slice Implementation

## Landed Surfaces

- [e:c+i] authoritative helper:
  - [harness_modifier/capture/run_review_reviewer.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/capture/run_review_reviewer.py)
- [e:c+i] compatibility shim:
  - [tooling/codex/run_review_reviewer.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/run_review_reviewer.py)
- [e:c+i] operator-facing workflow and wrapper carry:
  - [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
  - [gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md)
- [e:c+i] focused tests:
  - [test_run_review_reviewer.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_run_review_reviewer.py)
  - [test_review_route_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_review_route_contract.py)

## What This Slice Now Carries

- [d:r:i] one durable run-home preparation step for review runs
- [d:r:i] one bounded reviewer-recording helper that writes:
  - canonical review body when recoverable
  - launch-truth markdown
  - timing markdown
  - reviewer state note
- [d:r:i] three reviewer states:
  - `complete`
  - `partial`
  - `absent`
- [d:r:i] last recoverable message salvage for Claude stream-json runs
- [d:r:i] launch-truth-lite for plain stdout reviewers and copied requested/effective capture for Codex
- [d:r:i] explicit durable reviewer trail language in the workflow and wrapper instead of `/tmp` cleanup framing

## Boundary Kept Explicit

- [d:r:i] `REVIEWS.md` and the downstream `Review Consumer Contract` remain the stable planner-facing consumer surface.
- [d:r:i] This slice does not add subject-keyed route splitting.
- [d:r:i] This slice does not add retry/resume logic beyond bounded last-message salvage.
- [d:r:i] This slice does not widen parity or `.claude` materialization claims.
- [d:r:i] The new helper is authored directly under `harness_modifier/` with a thin `tooling/codex/` shim so the review-route uplift stays aligned with the extraction family rather than creating fresh helper debt outside the rehome path.

## Verification

- [e:c+i] `python3 -m py_compile harness_modifier/capture/run_review_reviewer.py tooling/codex/run_review_reviewer.py tooling/codex/tests/test_run_review_reviewer.py tooling/codex/tests/test_review_route_contract.py`
- [e:c+i] `python3 -m unittest tooling.codex.tests.test_run_review_reviewer tooling.codex.tests.test_review_route_contract`
- [e:c+i] `./scripts/setup-portable-gsd.sh`
- [e:c+i] `python3 tooling/codex/audit_refmap.py verify .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
- [e:c+i] `git diff --check`

## Next Review-Route Move

- [d:r:i] Pair this implementation with one propagation refresh note now.
- [d:r:i] Later, run one real timing-calibrated acceptance exercise on the `.codex` / `.claude` primary horizon before widening into subject-split or retry/resume routes.
