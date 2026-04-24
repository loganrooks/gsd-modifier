Date: 2026-04-22
Status: active bounded proposal

# Entry Runtime Continuity Shared-Reference First Slice Proposal

## Purpose

- [g:r:i] Turn the revised `128` branch into the first live implementation slice.
- [g:r:i] The target is not the full shared-reference cluster.
- [g:r:i] The target is one first proof across:
  - one new entry/runtime continuity reference
  - `new-project.md`
  - `ingest-docs.md`

## Why This Slice Opens

- [e:c+i] Lane `16` keeps the branch choice in `128` and says the remaining work is localized rather than structural. Source:
  - [entry-uplift-audit/dispositions/20-entry-runtime-continuity-shared-reference-proposal-reread-inheritance.md](../entry-uplift-audit/dispositions/20-entry-runtime-continuity-shared-reference-proposal-reread-inheritance.md)
- [d:r:i] The first live slice should prove the shared-reference shape at the earliest-entry pair before `update` or `from-gsd2` inherit it.

## Bounded First Slice

- [d:r:i] Add one new repo-local reference under the GSD references layer for entry/runtime continuity.
- [d:r:i] Keep `mandatory-initial-read.md` grammar-only.
- [d:r:i] Teach `new-project.md` and `ingest-docs.md` to point directly at the new sibling reference rather than widening `mandatory-initial-read.md` into a grammar-plus-content-pointer surface.
- [d:r:i] Keep the new reference read-only in character:
  - observed `.codex` basis
  - held `.claude` annotation
  - compact-to-narrative-to-typed reread order
  - explicit separation from later write-recommending uplift refresh
- [d:r:i] Concretize `When To Surface` for four route states:
  - greenfield `new-project.md`
  - brownfield `new-project.md`
  - new-mode `ingest-docs.md`
  - merge-mode `ingest-docs.md`

## Keep Route Boundaries Explicit

- [d:r:i] `new-project.md` and `ingest-docs.md` may surface entry/runtime continuity.
- [d:r:i] Neither route becomes the place that runs `$gsd-uplift-project --write`.
- [d:r:i] The slice does not rewrite the broader installer/runtime detection prose in the workflows.
- [d:r:i] The slice does not change top-level `compatibility_posture: observed_basis_only`.

## Held For The Next Adjacent Branch

- [d:r:i] `update` plus `gsd-update`
- [d:r:i] `from-gsd2` skill-wrapper route
- [d:r:i] broader installer/runtime detection rewriting
- [d:r:i] `.claude` translation or parity
- [d:r:i] compatibility matrix, version-window, third-runtime, or standalone compatibility-carrier widening

## Verification Gates

- [d:r:i] Add focused contract coverage for:
  - the new reference existing with the five-section minimum:
    - `Primary Compact Read`
    - `Supporting Narrative Read`
    - `Deeper Typed Read`
    - `Interpretation Frame`
    - `When To Surface`
  - `mandatory-initial-read.md` staying grammar-only
  - `new-project.md` and `ingest-docs.md` pointing directly at the new sibling reference
  - concrete trigger coverage for the four route states
  - read-only continuity staying distinct from later write-side uplift refresh
  - `.codex` observed basis plus held `.claude` annotation language staying explicit
- [d:r:i] Overlay ownership for the new reference should land as `add`.
- [d:r:i] Refresh propagation carriers in the same batch as the sibling after `47`.
- [d:r:i] Land one entry-uplift inheritance note plus one implementation note in intervention-proposals.

## Current Consequence

- [d:r:i] If this slice lands, the shared-reference branch is proven at the earliest-entry pair without blending installer/runtime breadth, wrapper-side migration, or later cross-runtime widening into the same batch.
- [d:r:i] The next adjacent move after that should be the `update` plus `gsd-update` and `from-gsd2` consumer branch, not another re-proposal of the same shared-reference shape.
