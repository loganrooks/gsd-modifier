Date: 2026-04-22
Status: landed first-slice implementation

# Entry Runtime Continuity Shared-Reference First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first live slice cleared by `129`.
- [g:r:i] The slice stayed bounded:
  - one dedicated shared reference
  - one overlay-manifest ownership entry
  - one `new-project.md` reader
  - one `ingest-docs.md` reader
- [g:r:i] The slice does not widen entry routes into write-side uplift dispatch, broader installer/runtime rewriting, or later update/from-gsd2 inheritance.

## What Landed

- [e:r:i] The tracked overlay now carries one dedicated entry/runtime continuity reference:
  - [tooling/portable-gsd/overlay/get-shit-done/references/entry-runtime-uplift-continuity.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/entry-runtime-uplift-continuity.md)
- [e:r:i] Overlay ownership for that reference is now explicit in:
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
  - ownership mode: `add`
- [d:r:i] That ownership widening was bounded to the new sibling reference only.
  - `new-project.md` and `ingest-docs.md` were already tracked `overwrite` carriers before this slice and were not introduced as new manifest rows here.
- [e:r:i] The shared reference now defines the minimum entry/runtime continuity grammar:
  - `Primary Compact Read`
  - `Supporting Narrative Read`
  - `Deeper Typed Read`
  - `Interpretation Frame`
  - `When To Surface`
- [e:r:i] `new-project.md` now points directly at the shared reference in its supporting packet and carries one bounded review step:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md)
- [e:r:i] `ingest-docs.md` now points directly at the shared reference in its supporting packet and carries one bounded review step:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md)

## What The Shared Reference Preserves

- [d:r:i] `mandatory-initial-read.md` remains grammar-only.
- [d:r:i] `Compatibility posture: observed_basis_only` remains the top-level posture.
- [d:r:i] Held runtime annotation remains annotation, not dual-basis relabeling.
- [d:r:i] The earliest entry pair now knows where to read:
  - route-state plus execution-context compact signal first
  - `STATE.md` `## Project Uplift` when it already exists
  - `UPLIFT-REPORT.md` only when narrative widening is needed
  - `UPLIFT-MANIFEST.json` only when typed ambiguity remains
- [d:r:i] The four route states are now explicit inside the shared reference:
  - greenfield `new-project.md`
  - brownfield `new-project.md`
  - new-mode `ingest-docs.md`
  - merge-mode `ingest-docs.md`
- [d:r:i] Entry routes still do not become the place that runs `$gsd-uplift-project --write`.

## Workflow Consequence

- [d:r:i] `new-project.md` now has a dedicated repo-local continuity reader instead of leaving entry-runtime continuity to ambient memory or later rediscovery.
- [d:r:i] `ingest-docs.md` now has the same explicit reader instead of flattening repo-local continuity into a later uplift route with no bounded entry-side grammar.
- [d:r:i] The slice keeps the asymmetry explicit:
  - broader installer/runtime detection language remains where it already lives
  - the new shared reference only governs repo-local `.codex` observed basis plus held `.claude` annotation carry
  - `update` plus `gsd-update` and `from-gsd2` remain the next adjacent consumer branch

## Verification

- [e:r:i] Focused contract coverage now exists at:
  - [tooling/codex/tests/test_entry_runtime_continuity_shared_reference_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_entry_runtime_continuity_shared_reference_contract.py)
- [e:r:i] That contract test proves:
  - overlay ownership is `add`
  - the new reference carries the required five-section minimum shape
  - the reference keeps observed `.codex` basis plus held `.claude` annotation explicit
  - each route-state section keeps at least one trigger bullet
  - `mandatory-initial-read.md` stays grammar-only
  - `new-project.md` points at the shared reference and keeps the route read-only
  - `ingest-docs.md` points at the shared reference and keeps the route read-only

## Current Consequence

- [d:r:i] The entry/runtime continuity route is no longer only a reread-cleared proposal.
- [d:r:i] It is now a real carried reference/workflow slice at the earliest entry pair.
- [d:r:i] The matching next follow-through is no longer another harden-only loop over the same landed surface.
- [d:r:i] The next adjacent branch is `update` plus `gsd-update`, with the small reference-side and contract-side sharpenings now folded into that consumer inheritance route before `from-gsd2` opens after it.
