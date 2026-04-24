Date: 2026-04-21
Status: accepted bounded proposal

# State / Progress / Resume Future-Carry Consumer Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded lifecycle-carry slice after the verifier, transition, and milestone-boundary bridges.
- [g:r:i] The target is not a full `STATE.md` redesign. The target is the first-read consumer layer where carried context can still thin before operators or later workflows see it.

## Why This Slice Is Real

- [e:r:i] The lifecycle family already landed producer-side carry at phase transition and milestone boundaries, including the compact `Future Carry Forward` digest shape in the state template plus explicit reread duties in `transition`, `new-milestone`, and `complete-milestone`.
- [e:r:i] `progress.md` already depends on `state-snapshot`, but the current snapshot helper does not expose `Future Carry Forward`, and the current helper shape is also out of tune with the current template’s `Decisions`, `Blockers/Concerns`, and `Session Continuity` sections.
- [e:r:i] `resume-project.md` still treats future carry as reader-memory rather than an explicit first-read surface, even though it is one of the main re-entry workflows.
- [e:r:i] That means the producer side has moved farther than the consumer side: later-boundary carry can be written, but the first-read operator surfaces still do not present it coherently.

## Bounded First Slice

- [d:r:i] Bring the state consumer helper into tracked overlay ownership so the repo-local contract is durable instead of ambient live drift.
- [d:r:i] Extend the helper-side structured snapshot to keep four bounded consumer buckets explicit:
  - decisions
  - blockers/concerns
  - future carry
  - session continuity
- [d:r:i] Teach `progress.md` to surface `Future Carry Forward` when any bucket remains live.
- [d:r:i] Teach `resume-project.md` to treat future carry as an explicit first-read re-entry surface rather than reader-memory.
- [d:r:i] Keep the slice bounded:
  - no full `STATE.md` parser rewrite
  - no broader `SPEC` widening
  - no seed-consumer redesign
  - no generic new dashboard layer

## Runtime / Contract Surfaces To Move Together

1. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/bin/lib/state.cjs`
2. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md`
3. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md`
4. [d:r:i] `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`

## Verification Gates

- [d:r:i] Add a focused helper test proving that the current template-aligned `STATE.md` shape yields structured decisions, blockers, future-carry buckets, and session continuity.
- [d:r:i] Re-materialize the overlay after the helper and workflow move so the live `.codex` frontier carries the same contract.
- [d:r:i] Refresh the propagation artifacts because this slice changes both a helper carrier and two routed consumer workflows.

## Held Later

- [d:r:i] This slice does not try to settle every current-position parsing issue in `state-snapshot`.
- [d:r:i] It does not yet widen into `SPEC`, seed consumers, or a whole first-read control panel redesign.
- [d:r:i] It keeps the question narrow: make the current carried context reach the first-read consumers more clearly and more durably.

## Current Consequence

- [d:r:i] If this slice lands, the next lifecycle question is no longer whether first-read consumer carry deserves a bridge at all.
- [d:r:i] The next lifecycle question becomes which later consumer family should inherit after this bridge:
  - `SPEC`
  - seed consumers
  - or broader state/read-order control surfaces
