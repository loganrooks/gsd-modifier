Date: 2026-04-21
Status: accepted bounded proposal

# SPEC Lifecycle Carry First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded lifecycle-carry slice after the verifier, transition, milestone-boundary, and first-read consumer bridges.
- [g:r:i] The target is not a whole `SPEC` redesign. The target is the upstream contract boundary where WHAT/WHY can lock earlier than long-horizon carry unless the producer and first downstream consumer move together.

## Why This Slice Is Real

- [e:c+i] The long-horizon carry register already named `SPEC` as an under-carried lifecycle surface: the current spec template locks goals, requirements, boundaries, constraints, and acceptance criteria, but it has no explicit place for protected seams, explicit non-decisions, current posture, future-shape notes, or strengthening routes. Source: [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md).
- [e:r:i] `spec-phase.md` claims it produces a `SPEC.md` that `discuss-phase` treats as locked decisions, but the current discuss workflow does not actually read `SPEC.md` or inherit any future-aware notes from it.
- [e:r:i] That means the current spec boundary can still narrow the chain in two ways:
  - the spec producer has no explicit future-aware carrier
  - the first downstream consumer does not actually consume the spec contract it claims to respect

## Bounded First Slice

- [d:r:i] Bring `spec-phase.md` and `templates/spec.md` into tracked overlay ownership so the repo-local lifecycle contract is durable rather than ambient upstream drift.
- [d:r:i] Add an optional `Future-Aware Notes` section to `SPEC.md` for cases where long-arc doctrine or later-seam pressure materially constrains the current phase.
- [d:r:i] Keep that section bounded to the same five buckets already used in later lifecycle carry:
  - protected seams
  - explicit non-decisions
  - current posture
  - future shape notes
  - strengthening opportunities
- [d:r:i] Teach `spec-phase.md` to read `.planning/LONG-ARC.md` when present and derive bounded future-aware notes without smuggling later scope into the current phase.
- [d:r:i] Teach `discuss-phase.md` to read `SPEC.md` when present, treat its locked scope surfaces as upstream steering, and seed `future_awareness` from `Future-Aware Notes` when present.
- [d:r:i] Keep the slice bounded:
  - no planner/frontmatter redesign
  - no verifier change in this slice
  - no seed-consumer widening yet
  - no full discuss/spec consolidation

## Runtime / Contract Surfaces To Move Together

1. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/spec-phase.md`
2. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/templates/spec.md`
3. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
4. [d:r:i] `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`

## Verification Gates

- [d:r:i] Add a focused contract test that checks the spec producer and discuss consumer move together:
  - `spec-phase` reads `LONG-ARC.md` and emits `Future-Aware Notes`
  - `spec` template exposes the bounded future-aware buckets
  - `discuss-phase` reads `SPEC.md` and carries those notes forward
- [d:r:i] Re-materialize the overlay after the workflow/template move so the live `.codex` frontier carries the same contract.
- [d:r:i] Refresh the propagation artifacts because this slice changes an upstream workflow/template pair plus a first downstream consumer workflow.

## Held Later

- [d:r:i] This slice does not widen into a full `spec-phase` epistemic redesign.
- [d:r:i] It does not try to rewrite the ambiguity model or the gating logic of `spec-phase`.
- [d:r:i] It does not yet widen into planner, verifier, or seed-consumer follow-through for spec-borne future-aware notes.

## Current Consequence

- [d:r:i] If this slice lands, `SPEC` no longer stays a narrower upstream contract than the later discuss/plan chain on long-horizon carry.
- [d:r:i] The next lifecycle question becomes which later surface should inherit after the spec boundary:
  - seed consumers
  - or broader read-order / relevance-control surfaces
