Date: 2026-04-22
Status: accepted bounded proposal

# Seed Operator-Consumer Widening First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent seed-family move after the landed uplift-side posture slice in `79/80`.
- [g:r:i] The target is operator-facing visibility:
  - keep seed corpus posture visible during ordinary `progress` and `resume-project` re-entry
  - use the existing uplift-note bridge instead of opening a new scan path
  - keep later audit widening and wider wrapper retrofit separate

## Why This Slice Is Real

- [e:r:i] Seed meaning no longer lives only at milestone-open, but ordinary operator-facing re-entry still relies on a generic uplift note that does not explicitly surface seed corpus posture.
- [e:r:i] That means a live seed corpus can remain muted during routine progress or resume even after uplift now knows how to classify it.
- [e:r:i] The typed propagation map already treats `progress` and `resume-project` as seed-posture consumers, so the current live operator route should inherit that expectation explicitly.

## Bounded First Slice

- [d:r:i] Keep the slice narrow:
  - `project_uplift.py` progress-note payload
  - `progress.md`
  - `resume-project.md`
  - focused contract tests
- [d:r:i] Add a compact seed corpus posture summary to the progress-note payload.
- [d:r:i] Keep seed posture reasons separate from generic uplift reasons so seed compatibility does not dissolve into one mixed reason bucket.
- [d:r:i] Show the seed posture lines only when a seed corpus actually exists, preserving progressive disclosure.
- [d:r:i] Keep `audit.cjs` widening, wider entry-wrapper retrofit, and legacy-seed migration as later routes.

## Verification Gates

- [d:r:i] Extend project uplift tests so they prove:
  - operator-facing note payload includes seed posture when seed files exist
  - seed posture reasons remain visible even when no new drift triggered a rewrite recommendation
- [d:r:i] Add a focused contract test for `progress` / `resume-project` wording so the new operator-facing seed route does not silently drift.
- [d:r:i] Refresh the typed propagation registry because this slice changes the helper -> progress/resume consumer bridge.

## Current Consequence

- [d:r:i] If this slice lands, ordinary operator-facing re-entry will keep seed corpus posture visible through the existing uplift-note bridge instead of leaving it concentrated at milestone-open or buried in durable uplift memory.
