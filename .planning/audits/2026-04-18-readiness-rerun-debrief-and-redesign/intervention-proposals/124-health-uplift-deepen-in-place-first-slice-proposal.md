Date: 2026-04-22
Status: active bounded proposal

# Health Uplift Deepen-In-Place First Slice Proposal

## Purpose

- [g:r:i] Open the next bounded `119` route after the landed milestone-boundary shared-reference slice in `123`.
- [g:r:i] Keep the slice inside the existing repair-facing carrier family:
  - `health.md`
  - `gsd-health`
- [g:r:i] The target is not to widen structural repair into compatibility adjudication.
- [g:r:i] The target is to keep repo-local uplift continuity explicit inside the health route when structural planning state is present and the live question has shifted from repair toward later posture follow-through.

## Why This Proposal Opens Now

- [e:c+i] `119` already classifies `health.md` as:
  - `deepen in place`
  - surfacing direction: `read-only`
  Source:
  - [119-uplift-consumer-chain-asymmetry-classification-return.md](119-uplift-consumer-chain-asymmetry-classification-return.md)
- [e:c+i] `70` already gave `health` the current route split:
  - structural repair stays structural repair
  - missing planning state routes to `new-project` or `ingest-docs`
  - later repo-local posture refresh routes separately to `$gsd-uplift-project --write`
  Source:
  - [70-health-and-migration-follow-through-first-slice-implementation.md](70-health-and-migration-follow-through-first-slice-implementation.md)
- [e:c+i] `121` and `123` now make the neighboring uplift continuity carriers explicit at phase boundary and milestone boundary instead of leaving them ambient:
  - [121-transition-state-uplift-continuity-first-slice-implementation.md](121-transition-state-uplift-continuity-first-slice-implementation.md)
  - [123-milestone-boundary-uplift-shared-reference-first-slice-implementation.md](123-milestone-boundary-uplift-shared-reference-first-slice-implementation.md)
- [d:r:i] That leaves the health route as the next adjacent single-carrier lift:
  - not another shared-reference family
  - not another whole-field proposal loop
  - but one bounded deepen-in-place move where repair-facing operators can see the compact uplift continuity chain when structural health is no longer the whole question

## Current Boundary

- [d:r:i] `health.md` already carries layered reading and route separation:
  - structural-health packet first
  - `.planning/UPLIFT-MANIFEST.json` or `.planning/UPLIFT-REPORT.md` only when the route shifts toward later repo-local posture refresh
  - no blending of structural repair, runtime update, and doctrine refresh into one unbounded pass
- [d:r:i] What it still does not carry is the explicit bounded follow-through grammar once that shift happens:
  - `STATE.md` `## Project Uplift` as the first compact reread
  - `UPLIFT-REPORT.md` as the next narrative read
  - `UPLIFT-MANIFEST.json` as the deeper typed read only when ambiguity remains
  - a clear distinction between read-only surfacing and later write-recommending uplift refresh

## Proposed First Slice

- [d:r:i] Deepen `tooling/portable-gsd/overlay/get-shit-done/workflows/health.md` in place with one explicit bounded step:
  - `Review Project Uplift Health Follow-Through`
- [d:r:i] Place that step explicitly:
  - after all structural validation, including `verify_repairs` when `--repair` was used
  - before `format_output`
- [d:r:i] Keep that step read-only in character:
  - start from `.planning/STATE.md` `## Project Uplift`
  - widen into `.planning/UPLIFT-REPORT.md` only when the compact digest does not carry enough route-local context
  - widen into `.planning/UPLIFT-MANIFEST.json` only when basis or annotation ambiguity remains after the first two reads
  - keep `compatibility_posture: observed_basis_only` explicit when surfaced
  - keep held runtime annotation as annotation rather than relabeling top-level posture
- [d:r:i] Structure the step with one local five-part grammar so the route-local reread stays consistent with neighboring continuity routes without turning into another shared-reference family:
  - `Primary Compact Read`
  - `Supporting Narrative Read`
  - `Deeper Typed Read`
  - `Interpretation Frame`
  - `When To Surface`
- [d:r:i] Only surface this step when structural planning state is present and the compact `Project Uplift` block signals live posture pressure rather than simple steady-state continuation.
- [d:r:i] Keep the wrapper boundary explicit in `tooling/portable-gsd/overlay/skills/gsd-health/SKILL.md`:
  - structural health remains the objective
  - repo-local uplift continuity may be reread after health
  - write-side refresh remains a later separate route, not something silently absorbed into the health run

## Why Deepen In Place Instead Of Adding Another Shared Reference

- [d:r:i] `119` already classifies this carrier as `deepen in place`, not `attach through a shared reference`.
- [d:r:i] `health.md` already owns the precise distinction that matters here:
  - structural planning integrity
  - limited low-risk repair
  - separate later repo-local posture follow-through
- [d:r:i] A new shared reference would widen the surface count without improving ownership clarity.
- [d:r:i] The stronger route is:
  - keep milestone-boundary continuity in the dedicated shared reference family
  - keep repair-facing uplift continuity inside the repair-facing carrier

## What The Slice Should Carry

- [d:r:i] The health route should say more clearly when uplift continuity matters after validation:
  - planning structure is present
  - health findings do not by themselves answer the repo-local posture question
  - the compact `Project Uplift` block still signals live posture pressure
- [d:r:i] The follow-through should keep the compact-versus-deeper split durable:
  - compact scalar digest in `STATE.md`
  - narrative route context in `UPLIFT-REPORT.md`
  - typed structural detail in `UPLIFT-MANIFEST.json`
- [d:r:i] The health output should keep the read-only versus write-recommending split explicit:
  - read-only reread happens inside the health route
  - later write-side uplift remains a separate recommendation when the live issue is repo-local posture refresh rather than structural repair
- [d:r:i] If `--repair` was used, the post-repair revalidation should still finish before any later uplift follow-through is surfaced.
- [d:r:i] The route should keep current helper ownership boundaries visible:
  - `gsd-sdk query validate.health` remains structural-health authority
  - `$gsd-uplift-project --write` remains the later posture-refresh authority
- [d:r:i] The route should state that three-way ownership split as the slice’s positive structural contribution:
  - structural-health authority
  - read-only uplift-continuity surfacing
  - separate later write-side refresh

## What This Proposal Does Not Authorize

- [d:r:i] No new shared reference for `health`.
- [d:r:i] No automatic launch of `$gsd-uplift-project --write`.
- [d:r:i] No compatibility matrix or version-window claims.
- [d:r:i] No `.claude` parity, translation, or third-runtime widening.
- [d:r:i] No structural-row promotion.
- [d:r:i] No widening of `validate.health` semantics into repo-local posture adjudication.
- [d:r:i] No widening of `from-gsd2`, `update`, or `mandatory-initial-read.md` through this slice.
- [d:r:i] No extraction/npm/`npx` movement.
- [d:r:i] No drift computation inside the health step.
- [d:r:i] No second-uplift-workflow footer widening.
- [d:r:i] No manifest mirroring or cache surface inside health output.

## Verification Gates

- [d:r:i] `health.md` should stay the structural-repair owner rather than becoming a second uplift workflow.
- [d:r:i] The new follow-through step must remain read-only and route-local.
- [d:r:i] The workflow and wrapper must agree on the structural-health versus later-uplift split.
- [d:r:i] The compact scalar digest in `STATE.md` must remain primary over direct manifest widening.
- [d:r:i] The landed slice must survive rematerialization through tracked overlay carry.
- [d:r:i] The landed slice should leave:
  - one focused contract test
  - one compatibility-family propagation refresh as the next sibling after `45`
  - one intervention-proposals implementation note

## Held Later

- [d:r:i] Broader read-packet widening for `health` beyond this one route-local uplift step.
- [d:r:i] Any auto-repair plus auto-refresh chaining.
- [d:r:i] Wider repair/migration/update family harmonization beyond the current route split.
- [d:r:i] Compatibility-family widening beyond observed basis plus held annotation discipline.
- [d:r:i] Cross-repo extraction and distribution work from `115`.

## Current Consequence

- [d:r:i] The next adjacent uplift-family object is now no longer ambient.
- [d:r:i] The active next object is:
  - `124-health-uplift-deepen-in-place-first-slice-proposal.md`
- [d:r:i] If this proposal survives reread, the next move should be:
  - one bounded `health.md` + `gsd-health` implementation slice
  - then the matching propagation refresh and implementation note
