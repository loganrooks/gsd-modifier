Date: 2026-04-22
Status: landed first-slice implementation

# Transition-State Uplift Continuity First Slice Implementation

## Purpose

- [g:r:i] This note records the landed implementation slice cleared by `119`, sharpened by `120`, and reread in entry-uplift lane `12`.
- [g:r:i] The target stayed narrow:
  - keep the compact `Project Uplift` digest explicit through phase-close state regeneration
  - keep that carry inside the `transition.md` + `templates/state.md` pair plus the existing helper
  - keep the compatibility family read-only in character instead of widening into matrix, parity, or translation claims

## What Landed

- [e:r:i] The tracked overlay now carries the transition/state continuity pair as an explicit compatibility-family consumer surface:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md)
  - [tooling/portable-gsd/overlay/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/state.md)
- [e:r:i] The state template now declares a top-level `## Project Uplift` placeholder with the minimum scalar field set:
  - last uplift class
  - compatibility posture
  - observed runtime basis
  - held runtime annotation
  - current recommendation
- [e:r:i] The template now carries the continuity rule directly:
  - `Project Uplift` stays top-level and adjacent to `Accumulated Context`
  - the block remains helper-filled and summary-shaped
  - typed detail stays in `.planning/UPLIFT-MANIFEST.json`
- [e:r:i] The helper-side co-ownership move is now real in [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py):
  - if `## Project Uplift` already exists, replace it in place
  - if it is missing, insert it before `## Deferred Items` when that top-level continuity slot exists
  - fall back to `## Session Continuity` only when the newer top-level slot is absent
- [e:r:i] The transition workflow now carries one bounded `review_project_uplift_continuity` step:
  - preserve path:
    - keep the block when the current uplift note does not recommend `--write`
  - refresh path:
    - rerun `project_uplift.py detect --write` when uplift-basis movement is detected
  - the step stays separate from `load_future_preservation_carry` and `review_accumulated_context`

## Proven Preservation Seam

- [e:r:i] The `gsd-tools.cjs phase complete` seam is now directly proved rather than only assumed.
- [e:r:i] [test_transition_uplift_continuity.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_transition_uplift_continuity.py) now verifies:
  - `phase complete` preserves the `## Project Uplift` block
  - the block still carries `Compatibility posture: observed_basis_only`
  - the held runtime annotation line survives the CLI edit path
- [e:r:i] The same test file also verifies:
  - `transition.md` names the bounded uplift continuity step
  - helper insertion prefers the declared top-level slot before `## Deferred Items`

## What This Slice Preserves

- [d:r:i] `compatibility_posture: observed_basis_only` remains the top-level anchor.
- [d:r:i] The state block remains scalar and compact:
  - no structural-row promotion
  - no standalone compatibility carrier
  - no `.claude` translation or parity claim
  - no third-runtime widening through this consumer surface
- [d:r:i] The consumer-chain split also remains explicit:
  - template declares the slot
  - helper fills the slot
  - transition reviews preserve-versus-refresh
  - the manifest remains the typed carrier

## Verification

- [e:r:i] Focused helper and continuity coverage passed:
  - `python3 -m unittest tooling.codex.tests.test_project_uplift tooling.codex.tests.test_transition_uplift_continuity tooling.codex.tests.test_state_snapshot_future_carry`
- [e:r:i] Helper syntax check passed:
  - `python3 -m py_compile tooling/codex/project_uplift.py`
- [e:r:i] Overlay was re-materialized into live `.codex` after the slice:
  - `./scripts/setup-portable-gsd.sh`
- [e:r:i] The repo-local uplift outputs still carry the compact digest after the slice:
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)

## Current Consequence

- [d:r:i] The compatibility family now carries a bounded state-continuity bridge instead of relying on recent helper writes staying ambiently fresh.
- [d:r:i] The next matching move is no longer to argue whether this pair opens first. That move is now landed.
- [d:r:i] The next matching move is the change-triggered propagation refresh on top of `43`, followed by the next `119` priority decision:
  - milestone-boundary pair through a shared reference
  - or `health.md` as the next single-carrier deepen-in-place route
