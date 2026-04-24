Date: 2026-04-21
Status: landed first slice

# SPEC Lifecycle Carry First Slice Implementation

## Purpose

- [g:r:i] This note records the landed upstream lifecycle slice opened in `63`.
- [g:r:i] The target stayed bounded: make `SPEC` a real future-aware producer when doctrine materially constrains the phase, and make `discuss-phase` a real downstream consumer of that contract instead of relying on claims in prose alone.

## What Landed

- [e:r:i] The tracked overlay now owns the spec producer pair that previously remained upstream-only:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/spec-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/spec-phase.md)
  - [tooling/portable-gsd/overlay/get-shit-done/templates/spec.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/spec.md)
- [e:r:i] The tracked discuss consumer now carries the upstream spec contract explicitly:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `SPEC.md` now has an optional `Future-Aware Notes` section with the same bounded buckets used later in the lifecycle:
  - `Protected Seams`
  - `Explicit Non-Decisions`
  - `Current Posture`
  - `Future Shape Notes`
  - `Strengthening Opportunities`
- [e:r:i] `spec-phase.md` now reads `.planning/LONG-ARC.md` when present, derives bounded future-aware notes, and writes them only when they materially constrain the current phase rather than inflating current scope.
- [e:r:i] `discuss-phase.md` now reads `SPEC.md` when present, treats its requirements/boundaries/constraints/acceptance criteria as upstream steering, adds the spec path to canonical refs, and seeds `future_awareness` from `Future-Aware Notes` when present.

## Verification And Recovery Path

- [e:r:i] The new spec producer/consumer carriers became real overlay/materialization moves, not live-only patches:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`
- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_spec_future_carry_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_spec_future_carry_contract.py), covering:
  - spec producer `LONG-ARC.md` reread
  - spec template `Future-Aware Notes` buckets
  - discuss consumer `SPEC.md` reread and future-aware carry

## What This Slice Still Holds

- [d:r:i] This slice does not widen into a planner or verifier-side consumer for spec-borne future-aware notes.
- [d:r:i] It does not widen into seed-consumer carry or broader read-order control surfaces.
- [d:r:i] It does not collapse `SPEC` and `CONTEXT` into one artifact; it keeps the producer/consumer split but makes the carry between them more explicit.

## Current Consequence

- [d:r:i] Lifecycle carry now reaches the upstream spec boundary instead of starting only at discuss/plan entry.
- [d:r:i] The next narrower lifecycle question is no longer whether `SPEC` deserves a future-aware bridge at all.
- [d:r:i] The next narrower lifecycle question is which later surface should inherit next after this bridge:
  - seed consumers
  - or broader read-order / relevance-control surfaces
