Date: 2026-04-22
Status: completed local inheritance

# Milestone-Boundary Uplift Shared-Reference First Slice Proposal Reread Inheritance

## Local Disposition

- [d:r:i] `accept with local revision`
- [d:r:i] Lane `13` keeps `122` as the next bounded `119` route after `121`.
- [d:r:i] The next move is no longer another proposal loop.
- [d:r:i] The next move is the bounded implementation slice for:
  - one dedicated shared reference
  - one overlay-manifest `add` entry
  - one `new-milestone.md` pointer plus surfacing step
  - one `complete-milestone.md` pointer plus surfacing step

## Carry Forward

- [d:r:i] Keep `122` as the second `119` route after `121`.
- [d:r:i] Keep the slice bounded to milestone open and milestone close.
- [d:r:i] Keep the carry as:
  - `attach through a shared reference`
  - surfacing direction: `read-only`
- [d:r:i] Keep the three-tier read shape:
  - primary compact read: `STATE.md` `## Project Uplift`
  - supporting narrative read: `.planning/UPLIFT-REPORT.md`
  - deeper typed read: `.planning/UPLIFT-MANIFEST.json`
- [d:r:i] Keep `compatibility_posture: observed_basis_only` as the top-level anchor.
- [d:r:i] Keep held runtime annotation visible as annotation, not as dual-basis relabel.
- [d:r:i] Keep the scalar-versus-structural split durable:
  - scalar digest in `STATE.md`
  - typed object remains in `UPLIFT-MANIFEST.json`
- [d:r:i] Keep `60` and `121` as neighboring carried surfaces, not absorbed ones:
  - long-arc / future-carry reread remains its own boundary schema
  - transition-side preserve/refresh remains its own phase-close schema
- [d:r:i] Keep the out-of-scope set explicit:
  - no write-side dispatcher
  - no parity or translation claims
  - no compatibility matrix or version-window claims
  - no structural-row promotion
  - no third-runtime annotation widening
  - no `health.md` widening inside this slice
  - no verifier/setup/materialization widening
  - no extraction/npm/`npx`
  - no silent family-6 pre-answer

## Revise Locally

- [d:r:i] In `122`, pin the dedicated reference path directly:
  - `tooling/portable-gsd/overlay/get-shit-done/references/milestone-boundary-uplift-continuity.md`
  - materialized into `.codex/get-shit-done/references/milestone-boundary-uplift-continuity.md`
  - owned through an explicit `add` entry in `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- [d:r:i] In `122`, state directly why this is a dedicated new reference instead of an expansion of `mandatory-initial-read.md`:
  - `mandatory-initial-read.md` owns read-packet grammar
  - this new reference owns milestone-boundary uplift content
- [d:r:i] In `122`, name the current asymmetry between the milestone workflows:
  - `new-milestone.md` already carries `required` plus `supporting` plus `deeper` reading blocks and already points at `mandatory-initial-read.md`
  - `complete-milestone.md` currently carries only a `required_reading` block and does not yet point at `mandatory-initial-read.md`
  - this slice adds the new uplift reference to both workflows' `required_reading` blocks without silently answering the broader read-packet question for `complete-milestone.md`
- [d:r:i] In `122`, split one generic workflow edit into two explicit edits:
  - add the new reference pointer to `new-milestone.md`
  - add the new reference pointer to `complete-milestone.md`
- [d:r:i] In `122`, add explicit per-boundary surfacing triggers instead of leaving only a generic `when it matters` phrase.
- [d:r:i] In `122`, add an explicit read-only voice clause:
  - the reference tells operators what to read and how to interpret it
  - it does not tell milestone boundaries to run helper commands
- [d:r:i] In `122`, name the relationship to `60` and `121` directly:
  - uplift continuity sits beside the long-arc / future-carry reread
  - boundary reading sits beside, not inside, the transition preserve/refresh step
- [d:r:i] In `122`, add a minimum content floor for the new reference:
  - `Primary Compact Read`
  - `Supporting Narrative Read`
  - `Deeper Typed Read`
  - `Interpretation Frame`
  - `When To Surface`
- [d:r:i] In `122`, pin the propagation refresh slot as a compatibility-family sibling to `44`, not as backfill into lifecycle-carry `22`.
- [d:r:i] In `122`, pin the governance-trace placement:
  - one entry-uplift inheritance/disposition note
  - one intervention-proposals implementation note
- [d:r:i] In `122`, add an explicit keep-later line:
  - no silent adoption of `mandatory-initial-read.md` into `complete-milestone.md` through this slice

## Keep Later

- [d:r:i] `health.md` as the adjacent single-carrier deepen-in-place route.
- [d:r:i] Broader family-6 route-asymmetry mapping.
- [d:r:i] Structural-row promotion into `MILESTONES.md`, archived roadmap/requirements, or retrospective outputs.
- [d:r:i] Dual-basis relabel or standalone compatibility carrier.
- [d:r:i] Third-runtime held-annotation widening.
- [d:r:i] Read-packet grammar widening for `complete-milestone.md` beyond the new uplift reference pointer.
- [d:r:i] Extraction/distribution work from `115`.

## Next Bounded Move

- [d:r:i] Revise `122` with the local changes above.
- [d:r:i] Then implement the milestone-boundary shared-reference slice:
  - create the dedicated reference file
  - add the overlay-manifest `add` entry
  - add the bounded `new-milestone.md` pointer plus surfacing follow-through
  - add the bounded `complete-milestone.md` pointer plus surfacing follow-through
- [d:r:i] After that implementation lands, add:
  - one compatibility-family propagation refresh as a sibling to `44`
  - one governance-trace implementation note
- [d:r:i] After the milestone-boundary slice lands, reopen the adjacent next route:
  - `health.md` deepen-in-place
