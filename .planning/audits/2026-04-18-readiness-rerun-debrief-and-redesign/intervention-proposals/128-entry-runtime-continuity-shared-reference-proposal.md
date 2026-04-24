Date: 2026-04-22
Status: active bounded proposal

# Entry Runtime Continuity Shared-Reference Proposal

## Purpose

- [g:r:i] Reopen the shared-reference branch that `119` kept explicit after the three `deepen in place` carriers landed.
- [g:r:i] The target is not a full entry-wrapper sweep.
- [g:r:i] The target is one bounded shared-reference family for entry/runtime continuity across:
  - read-packet doctrine
  - `new-project`
  - `ingest-docs`
  - later `update`
  - later `from-gsd2`

## Why This Proposal Opens Now

- [e:c+i] `119` explicitly classifies `read-packet doctrine + initialization / ingest + repair / migration + update carriers` as `attach through a shared reference`. Source:
  - [119-uplift-consumer-chain-asymmetry-classification-return.md](119-uplift-consumer-chain-asymmetry-classification-return.md)
- [d:r:i] The three earlier priority carriers from `119` are now landed:
  - transition/state continuity
  - milestone-boundary shared reference
  - health deepen-in-place plus same-carrier harden
- [d:r:i] That means the next adjacent move is no longer another local carrier harden by default.
- [d:r:i] The remaining open branch is the shared-reference cluster, especially where repo-local entry surfaces still speak in wider all-provider terms even though this repo's meaningful provider horizon is `.codex` and `.claude`.

## Current Thinness

- [e:c+i] `new-project.md` and `ingest-docs.md` still infer runtime across `codex`, `gemini`, `opencode`, and fallback `claude`. Sources:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md)
- [e:c+i] `update.md` still carries a broader runtime/install frontier across `claude`, `opencode`, `gemini`, `kilo`, and `codex`. Source:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md)
- [d:r:i] That broader runtime language is not automatically wrong for installer truth.
- [d:r:i] The shared-reference branch is not about rewriting that installer/runtime reality in the same slice.
- [d:r:i] It is about adding one bounded repo-local continuity carrier at entry routes so later uplift, ingestion, migration, and update work does not keep rediscovering the same `.codex` / held `.claude` posture from scratch.

## Proposed Shared Reference Family

- [d:r:i] Add one repo-local shared reference under the GSD references layer for entry/runtime continuity.
- [d:r:i] Keep `mandatory-initial-read.md` grammar-only in this slice.
- [d:r:i] The new reference should be a sibling surface pointed at directly by consumer workflows, mirroring the shared-reference posture already proven by `122/123`.
- [d:r:i] That reference should carry:
  - the repo-local provider horizon:
    - observed `.codex` basis
    - held `.claude` annotation
  - the compact-to-narrative-to-typed reread order already used elsewhere:
    - `STATE.md` `## Project Uplift`
    - `UPLIFT-REPORT.md`
    - `UPLIFT-MANIFEST.json`
  - the distinction between:
    - read-only continuity surfacing
    - later write-recommending uplift refresh
  - the rule that broader provider-general runtime/install semantics remain separate from repo-local continuity doctrine unless a later slice explicitly joins them

## Bounded First Slice

- [d:r:i] The first implementation slice should stay at:
  - the new shared reference
  - `new-project.md`
  - `ingest-docs.md`
- [d:r:i] `mandatory-initial-read.md` remains the grammar surface in this slice.
- [d:r:i] `new-project.md` and `ingest-docs.md` should point directly at the sibling entry/runtime continuity reference rather than turning `mandatory-initial-read.md` into a grammar-plus-content-pointer surface.
- [d:r:i] `new-project` and `ingest-docs` are the first live consumers because they are the earliest repo-entry routes and they currently still widen attention across provider families that do not matter operationally here.
- [d:r:i] The first slice should teach those routes:
  - when to surface the repo-local `.codex` / `.claude` continuity question
  - when to stay at ordinary entry behavior
  - how to keep read-only continuity distinct from later write-side uplift
- [d:r:i] The first slice should concretize `When To Surface` for four route states before implementation opens:
  - greenfield `new-project.md`
  - brownfield `new-project.md`
  - new-mode `ingest-docs.md`
  - merge-mode `ingest-docs.md`
- [d:r:i] The first slice should not yet make `update` or `from-gsd2` inherit the new reference in the same batch.

## Later Adjacent Slice Held Explicitly

- [d:r:i] `update` plus `gsd-update`
- [d:r:i] `from-gsd2` skill-wrapper route
- [d:r:i] Those two later consumers should attach after the shared-reference shape is proven at the earlier entry pair, not in the same first implementation batch.

## What This Proposal Does Not Authorize

- [d:r:i] No runtime matrix or version-window claims.
- [d:r:i] No `.claude` route translation or parity push.
- [d:r:i] No helper-side widening of `project_uplift.py` beyond the already-held annotation discipline.
- [d:r:i] No sweeping rewrite of low-level installer/runtime detection just to erase wider provider names.
- [d:r:i] No silent widening of `mandatory-initial-read.md` from grammar-only to grammar-plus-content-pointer without a separate reopened proposal.
- [d:r:i] No extraction or npm/`npx` work from `115`.

## Verification Gates

- [d:r:i] The first implementation slice must add focused contract coverage for:
  - shared-reference presence and read shape
  - `mandatory-initial-read.md` staying grammar-only while `new-project.md` and `ingest-docs.md` point directly at the sibling reference
  - concrete `When To Surface` triggers for greenfield/brownfield `new-project.md` and new/merge `ingest-docs.md`
  - `new-project.md` and `ingest-docs.md` reading the new reference without collapsing read-only continuity into automatic uplift
  - `.codex` / `.claude` horizon discipline staying explicit in the repo-local operator layer
- [d:r:i] The slice must refresh propagation carriers in the same batch because it will move:
  - one shared reference
  - two entry workflow consumers
- [d:r:i] The propagation refresh should land as the sibling after `47`, not as backfill into an older lifecycle carrier.
- [d:r:i] The slice should also land one inheritance note and one implementation note so the governance trace matches the earlier shared-reference precedent.

## Current Consequence

- [d:r:i] The next bounded move after this proposal should be one implementation slice for:
  - the shared reference
  - `new-project.md`
  - `ingest-docs.md`
- [d:r:i] `update` and `from-gsd2` should stay as the next adjacent branch after that first proof, not be silently absorbed into the same initial batch.
