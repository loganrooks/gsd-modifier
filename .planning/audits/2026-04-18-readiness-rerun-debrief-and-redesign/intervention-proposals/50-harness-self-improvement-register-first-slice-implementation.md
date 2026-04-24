Date: 2026-04-21
Status: landed first slice

# Harness Self-Improvement Register First Slice Implementation

## Purpose

- [g:r:i] This note records the first landed slice of the standing self-improvement register family proposed in `48`.
- [g:r:i] The target is a durable cross-family register outside this audit subtree so the improvement field does not disappear when the subtree eventually ages.

## What Landed

- [e:r:i] A new durable planning artifact now exists at [.planning/HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md).
- [e:r:i] The first slice carries:
  - active improvement families
  - bounded next slices
  - ownerless concerns
  - a cross-dimensional quality basket
  - explicit held-later boundaries
- [e:r:i] Root and planning governance now have a stable path to this register:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
  - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)

## Why This Slice Matters

- [d:r:i] The harness-improvement field now lives somewhere durable outside the current audit subtree.
- [d:r:i] That means later operators do not need to reopen the whole `harness-improvement-audit/` family just to know what the current improvement families and ownerless concerns are.

## What This Slice Still Holds

- [d:r:i] This first slice does not yet add telemetry, freshness semantics, or automated ranking.
- [d:r:i] It stays a compact operator-facing register, not a machine-scored backlog.

## Current Consequence

- [d:r:i] The harness now has both:
  - a bounded machine-checkable canary for current runtime/install invariants
  - a durable non-subtree register for broader improvement pressure
- [d:r:i] The next strongest bounded move after this slice is the audit-program infrastructure family in `47`.
