Date: 2026-04-21
Status: accepted bounded proposal

# Resume-Project Second-Consumer Follow-Through Proposal

## Purpose

- [g:r:i] This note proposes the next bounded propagation move after the uplift producer / consumer map.
- [g:r:i] The aim is not to widen the whole entry family again. The aim is to decide whether `resume-project` should become the second live uplift consumer so re-entry does not depend on `progress` alone.

## Why This Surface Next

- [d:r:i] The local map now makes one thin route clear:
  - `progress` is already uplift-aware
  - `resume-project` still ignores uplift posture even though it already reads `STATE.md`, presents current status, and controls first re-entry after time away
- [d:r:i] That means the current uplift chain is stronger than before but still asymmetrical: ordinary progress rereads can surface uplift posture, while ordinary resume rereads still rely on reader memory.

## Proposed Shape

- [d:r:i] Add one bounded, read-only uplift note inside `resume-project`.
- [d:r:i] The note should reuse the existing helper bridge rather than introducing a second parsing path:
  - call `python3 "__PROJECT_ROOT__/tooling/codex/project_uplift.py" progress-note "__PROJECT_ROOT__" --json`
  - show the same bounded posture summary when `UPLIFT_NOTE.show` is `true`
- [d:r:i] The note should live in the `present_status` stage after project status / blockers and before route selection so it informs re-entry without hijacking it.
- [d:r:i] The note may add one bounded next-action option when `recommend_detect_only` is `true`:
  - `Run $gsd-uplift-project --detect-only`
- [d:r:i] Keep the move read-only:
  - no auto-write
  - no auto-refresh
  - no auto-routing away from the user’s resumed task

## Owner And Propagation Consequence

- [d:r:i] `resume-project.md` currently has no tracked overlay owner in this repo.
- [d:r:i] So implementation should not hand-patch the live `.codex` file directly.
- [d:r:i] The first implementation slice would need:
  - a tracked overlay owner at `tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md`
  - installer re-materialization through `./scripts/setup-portable-gsd.sh`
  - reread of any wrapper or docs surfaces whose invocation contract actually changes
- [d:r:i] Because the change reuses `progress-note` rather than inventing a new helper mode, the propagation burden stays bounded.

## What This Proposal Does Not Widen Into

- [d:r:i] no broader re-entry redesign
- [d:r:i] no `resume-project` parsing of `UPLIFT-MANIFEST.json` or `STATE.md` directly
- [d:r:i] no third consumer family yet
- [d:r:i] no additive install routing
- [d:r:i] no cross-runtime reconciliation work

## Review And Verification Gates

- [d:r:i] Before implementation:
  - confirm the insertion point in `resume-project.md`
  - keep the helper reuse explicit
  - keep the route read-only
- [d:r:i] After implementation:
  - rerun `./scripts/setup-portable-gsd.sh`
  - run `scan_threshold_language.py` on the new overlay workflow
  - verify that the live `.codex/get-shit-done/workflows/resume-project.md` re-materializes from the tracked overlay
  - update the propagation map to show `resume-project` as a second live consumer

## Current Consequence

- [d:r:i] This proposal is now accepted and implemented in `04`.
- [d:r:i] The family no longer needs to decide whether the second-consumer slice should land.
- [d:r:i] The next decision is what wider scrutiny or adjacent routed consumer should follow this stronger two-consumer baseline.
