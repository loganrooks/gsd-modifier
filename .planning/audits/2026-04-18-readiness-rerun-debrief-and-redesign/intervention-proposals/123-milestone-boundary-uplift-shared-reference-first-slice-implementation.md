Date: 2026-04-22
Status: landed first-slice implementation

# Milestone-Boundary Uplift Shared-Reference First Slice Implementation

## Purpose

- [g:r:i] This note records the landed milestone-boundary uplift continuity slice cleared by `122` and reread in entry-uplift lane `13`.
- [g:r:i] The slice stayed bounded:
  - one dedicated shared reference
  - one overlay-manifest ownership entry
  - one milestone-open pointer plus read-only surfacing step
  - one milestone-close pointer plus read-only surfacing step
- [g:r:i] The slice does not widen milestone boundaries into helper-write posture, compatibility-matrix claims, or broader cross-runtime relabeling.

## What Landed

- [e:r:i] The tracked overlay now carries one dedicated milestone-boundary uplift reference:
  - [tooling/portable-gsd/overlay/get-shit-done/references/milestone-boundary-uplift-continuity.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/milestone-boundary-uplift-continuity.md)
- [e:r:i] Overlay ownership for that reference is now explicit in:
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
  - ownership mode: `add`
- [e:r:i] The shared reference now defines the minimum milestone-boundary uplift grammar:
  - `Primary Compact Read`
  - `Supporting Narrative Read`
  - `Deeper Typed Read`
  - `Interpretation Frame`
  - `When To Surface`
- [e:r:i] `new-milestone.md` now reads the shared reference directly and carries one bounded milestone-open continuity step:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md)
- [e:r:i] `complete-milestone.md` now reads the same shared reference directly and carries one bounded milestone-close continuity step:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md)

## What The Shared Reference Preserves

- [d:r:i] `Compatibility posture: observed_basis_only` remains the top-level posture.
- [d:r:i] Held runtime annotation remains annotation, not dual-basis relabeling.
- [d:r:i] Milestone boundaries now know where to read:
  - compact digest in `STATE.md`
  - narrative detail in `UPLIFT-REPORT.md`
  - typed detail in `UPLIFT-MANIFEST.json`
- [d:r:i] Milestone boundaries still do not become the place that runs `$gsd-uplift-project --write`.
- [d:r:i] This carrier sits beside:
  - long-arc and future-carry milestone-boundary review from `60`
  - transition/state preserve-versus-refresh continuity from `121`

## Workflow Consequence

- [d:r:i] Milestone open now has an explicit uplift-continuity reader instead of relying on ambient memory from earlier uplift writes.
- [d:r:i] Milestone close now has the same explicit reader instead of leaving compatibility-family continuity only in phase-close and ordinary re-entry surfaces.
- [d:r:i] The asymmetry between the milestone workflows remains explicit:
  - `new-milestone.md` still carries broader read-packet grammar through `mandatory-initial-read.md`
  - `complete-milestone.md` still does not adopt that broader grammar in this slice
  - this slice only gives both workflows a shared uplift-continuity reference

## Verification

- [e:r:i] Focused contract coverage now exists at:
  - [tooling/codex/tests/test_milestone_boundary_uplift_shared_reference_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_milestone_boundary_uplift_shared_reference_contract.py)
- [e:r:i] That contract test proves:
  - overlay ownership is `add`
  - the new reference carries the required five-section minimum shape
  - `new-milestone.md` points at the shared reference and keeps milestone-open read-only
  - `complete-milestone.md` points at the shared reference and keeps milestone-close read-only

## Current Consequence

- [d:r:i] The milestone-boundary route is no longer only a reread-cleared proposal.
- [d:r:i] It is now a real carried reference/workflow slice.
- [d:r:i] The matching next follow-through is the compatibility-family propagation refresh in `45`, not another proposal loop around the same boundary.
