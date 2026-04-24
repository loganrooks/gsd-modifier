Date: 2026-04-21
Status: active sequencing note

# Harness Improvement Follow-Through Sequencing

## Purpose

- [g:r:i] This note sequences the first bounded follow-through families after the full-field harness-improvement Opus widening.
- [g:r:i] The goal is not to collapse the field map into a single winner. The goal is to choose a first tranche that raises robustness, maintainability, propagation visibility, and future carry without reopening the rerun or losing the wider map.

## First Tranche

1. [d:r:i] `46` Harness-quality canary and invariant assertion.
   - Why first:
     - it converts already-named invariants into a machine-checkable surface
     - it raises robustness against silent runtime regressions
     - it makes later widening safer because helper/output/install movement will trip a visible signal sooner

2. [d:r:i] `47` Audit-program infrastructure, canon absorption, and audit-subtree aging.
   - Why second:
     - it raises maintainability of the audit ecosystem itself
     - it reduces repeated scaffold authoring and lowers the chance that landed doctrine remains trapped in a subtree
     - it gives later audits a cleaner inheritance path

3. [d:r:i] `48` Standing harness self-improvement register and cross-dimensional quality basket.
   - Why third:
     - it gives the widening field a durable non-subtree home
     - it keeps ownerless concerns, improvement pressure, and cross-dimensional tradeoffs visible after this audit family ages
     - it helps later sequencing avoid rediscovering the same field from chat memory

## Next After The First Tranche

- [d:r:i] Lifecycle carry beyond discuss/plan should remain a live next family rather than a forgotten one, but it stays second-tranche work here because it touches more live workflow surfaces at once:
  - verify
  - transition
  - milestone boundaries
  - SPEC
  - STATE / progress
  - seeds
- [d:r:i] Durable-memory / vintage, safety-cost-privacy carriers, and later cross-repo distribution also remain explicit later families rather than being silently dropped.

## Current Consequence

- [d:r:i] The immediate next move is not another full-field review.
- [d:r:i] The immediate next move is to open `46`, `47`, and `48`, then land the first bounded canary slice from `46`.
