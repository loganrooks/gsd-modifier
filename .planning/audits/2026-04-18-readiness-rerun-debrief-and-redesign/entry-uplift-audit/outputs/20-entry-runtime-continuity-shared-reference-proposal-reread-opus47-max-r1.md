Date: 2026-04-22
Status: active reread output

# Entry Runtime Continuity Shared-Reference Proposal Reread — Opus 4.7 Max R1

## What The Proposal Places Well

- [d:r:i] `128` reopens the exact branch that `119` kept unfinished. The three earlier priority carriers — transition/state (`121`), milestone-boundary (`123`), and health deepen-in-place plus same-carrier harden (`125`/`127`) — have discharged the `deepen in place` classification for the carriers they cover, so `attach through a shared reference` is the next branch that still has live work rather than an ambient appetite for more mapping.
- [d:r:i] The chosen first-pair consumers track earliest-entry route position rather than easiest-edit-surface position. `new-project.md` is the first surface a fresh or vanilla repo hits; `ingest-docs.md` is the first surface a repo with older mixed-format docs hits. That pair broadens the carry of the emerging entry-runtime continuity doctrine across both the greenfield entry and the migration-into-planning entry at once, rather than adding a third single-carrier proof stacked on top of the phase-close / milestone-boundary / repair surfaces.
- [e:r:i] The provider horizon inside the proposed shared reference is stated repo-locally:
  - observed `.codex` basis
  - held `.claude` annotation
  - explicit sentence that broader provider-general runtime/install semantics remain separate
  Source:
  - [128-entry-runtime-continuity-shared-reference-proposal.md](../../intervention-proposals/128-entry-runtime-continuity-shared-reference-proposal.md)
- [d:r:i] The reread-order inside the shared reference reuses the pattern already proven by `121` and `123`:
  - `STATE.md` `## Project Uplift` compact digest first
  - `UPLIFT-REPORT.md` narrative second
  - `UPLIFT-MANIFEST.json` typed detail only when ambiguity remains
  That reuse intensifies the durability of the compact-to-narrative-to-typed grammar across a third carrier cluster rather than inventing a parallel reading shape for entry routes.
- [d:r:i] The read-only versus write-recommending split is restated explicitly, so the entry consumers inherit the same posture already carried at phase-close (`121`) and milestone-boundary (`123`): a consumer surface may surface uplift posture; it does not become the route that runs `$gsd-uplift-project --write`.
- [d:r:i] The held-later layer is named rather than left ambient. `update` + `gsd-update` and `from-gsd2` + `gsd-from-gsd2` are carried as the next adjacent branch rather than being absorbed into the first batch or quietly dropped.
- [d:r:i] The not-authorized list carries the same discipline as the surrounding family — no matrix claims, no version-window claims, no `.claude` parity push, no helper-side `project_uplift.py` widening, no extraction from `115`, no sweeping installer/runtime detection rewrite. That keeps the slice a real shared-reference bridge rather than a vehicle for smuggling later-family questions forward.
- [d:r:i] The proposal names the asymmetry between a topic-specific shared reference and broader installer/runtime reality and resists the temptation to answer the second through the first. That preserves the doctrine already held at `122`/`123` that read-packet grammar ownership (`mandatory-initial-read.md`) is distinct from topic-specific content ownership (a dedicated uplift-continuity reference).

## Where The Proposed Shared-Reference Shape Still Thins Or Blurs Distinct Jobs

- [d:r:i] The first slice lists `mandatory-initial-read.md` alongside the shared reference and the two entry workflows, but the role `mandatory-initial-read.md` plays in that list is more compressed than at `122`/`123`. The verification-gate phrase is "`mandatory-initial-read.md` carrying the new reference in the right packet tier." Two distinct interpretations of that sentence are live:
  - `mandatory-initial-read.md` is widened from grammar-only to grammar-plus-content-pointers, so the new reference appears named inside `mandatory-initial-read.md`
  - `mandatory-initial-read.md` stays grammar-only, and the new reference is a sibling pointed at directly by `new-project.md` and `ingest-docs.md`, the way `milestone-boundary-uplift-continuity.md` is pointed at directly by `new-milestone.md` and `complete-milestone.md` at `123`
  The proposal does not discriminate between these two paths. `122` explicitly chose the sibling path and stated why. `128` does not inherit that explicit split, so the relationship between read-packet grammar ownership and topic-specific reference ownership is less crisp here than at the last family precedent. That blurring is the one most likely to produce drift at implementation time.
- [d:r:i] The `When To Surface` triggers are named as a structural slot but not concretized. `122` wrote out the milestone-open and milestone-close trigger sets line by line, so the implementation inherited a workable trigger list. `128` names the trigger slot but leaves the triggers themselves for later authorship, which thins the proposal relative to the `122` precedent. The specific triggers that still need concretization:
  - greenfield `new-project.md` entry where no `.planning/` state yet exists
  - brownfield `new-project.md` entry where `project_exists: true` already routes to `$gsd-uplift-project --write`
  - `ingest-docs.md` new-mode where `.planning/` will be authored fresh from ingested docs
  - `ingest-docs.md` merge-mode where existing `.planning/` state and `STATE.md` `## Project Uplift` may already exist
  The compact digest / narrative / typed read sequence is well defined at `121`/`123`, but those triggers are entry-surface specific and do not transfer cleanly from phase-close or milestone-boundary carry.
- [d:r:i] The proposal's Current Thinness framing tilts the motivation toward "narrow provider attention" (the runtime-detection listing across `codex`, `gemini`, `opencode`, `claude`, `kilo`). The proposed slice as written does not actually narrow that listing. What it adds is a bounded read-only continuity step beside ordinary runtime detection. That is a legitimate deliverable, but the proposal's framing leaves a reader expecting narrower runtime detection inside the workflows, which is not what the slice performs. This is the kind of framing slip that later readers can mistake for silent authorization of wider installer/runtime rewriting. A sharper framing is: the slice adds a bounded repo-local uplift continuity carrier at entry routes; it does not answer the separate, broader question of how the workflows should present runtime detection across the installer-supported provider set.
- [d:r:i] The verification gates are lighter than `122`'s. `122` named the sibling placement for the propagation refresh (compatibility-family sibling to `44`, not backfill to lifecycle-carry `22`), the overlay ownership mode (`add`), and the two governance-trace landing points (one disposition/inheritance note plus one intervention-proposals implementation note). `128` carries the abstract requirement that propagation refresh moves in the same batch, but does not name the next sibling slot (the natural next after `47` is `48`), the overlay ownership entry form, or the trace landing points. That lighter specification leaves more at implementation-time judgment than the surrounding family precedent supports.
- [d:r:i] The not-authorized list holds most of the adjacent later-family pressures but omits one adjacent pressure that can drift in during implementation: silent widening of `mandatory-initial-read.md` from a grammar-only reference to a grammar-plus-content-pointer reference. Without explicit mention, a later implementer could treat listing the new reference inside `mandatory-initial-read.md` as a bounded edit, when in fact it would shift the character of `mandatory-initial-read.md` itself. Naming the boundary protects the grammar surface.
- [d:r:i] The held-later layer names `update` plus `gsd-update` and `from-gsd2` plus `gsd-from-gsd2`, but does not distinguish that `from-gsd2` is a skill wrapper (`SKILL.md`) rather than a workflow file, while `update` pairs a workflow file with a wrapper. The verification pattern for wrappers already carries its own shape through `69`/`70` (structural health after migration) and `71`/`72` (route separation after update). The next adjacent branch will need to pick up both wrapper contracts, not only workflow-side continuity. Naming that wrapper-versus-workflow distinction in the held-later layer would make the next move more legible.

## How The First Live Slice Should Be Scoped

- [d:r:i] Keep the first slice at one shared reference plus `new-project.md` plus `ingest-docs.md`, with `mandatory-initial-read.md` held as a grammar-only reference that this slice does not rewrite. That preserves the `122`/`123` precedent: topic-specific references live beside `mandatory-initial-read.md`, not inside it. The reference route discipline stays:
  - grammar surface in `mandatory-initial-read.md`
  - topic-specific surface in the new `entry-runtime-continuity.md` (or similarly named) reference
  - consumer workflows point at both by name, each for its own role
- [d:r:i] If the slice instead chooses to widen `mandatory-initial-read.md` with a named pointer to the new reference, that widening becomes a substantive shift in `mandatory-initial-read.md`'s character (grammar-only → grammar-plus-content-pointer). That shift deserves an explicit separate authorization, not a quiet verification-gate clause. The more carry-yielding route is to keep `mandatory-initial-read.md` grammar-only and let each consumer workflow carry its own named pointer to the sibling topic reference, the way `123` landed the milestone-boundary carry.
- [d:r:i] Concretize the `When To Surface` section of the new reference before implementation so the first slice does not author that block from scratch. Each consumer surface should have trigger language that is evaluable route-locally rather than interpretive:
  - `new-project.md` greenfield: the new reference is not surfaced; ordinary entry behavior proceeds
  - `new-project.md` brownfield (`project_exists: true`): the new reference's compact/narrative/typed read block surfaces the current `STATE.md` `## Project Uplift` digest and the existing uplift-routing hook becomes the route pointer for later write-side refresh
  - `ingest-docs.md` new-mode: the new reference is not surfaced during fresh authoring; the later workflows that will read the newly produced `.planning/` state inherit continuity through their own carriers (already landed at `121`/`123`)
  - `ingest-docs.md` merge-mode with existing `.planning/`: the new reference's compact/narrative/typed read block surfaces uplift posture beside the existing merge-side conflict work, with a route pointer to `$gsd-uplift-project --write` when runtime/governing posture refresh rather than structural planning repair is the live question
- [d:r:i] Keep the read-only character explicit at each consumer step. Neither `new-project.md` nor `ingest-docs.md` becomes the place that runs `$gsd-uplift-project --write`. The `new-project.md` brownfield hook already routes to `$gsd-uplift-project --write` through prose; the shared-reference surfacing adds the compact digest reread before that route pointer, not in place of it.
- [d:r:i] Carry the reference's five-section minimum from `122`/`123` unchanged:
  - `Primary Compact Read`
  - `Supporting Narrative Read`
  - `Deeper Typed Read`
  - `Interpretation Frame`
  - `When To Surface`
  The `Interpretation Frame` should keep `compatibility_posture: observed_basis_only` top-level and keep held runtime annotation distinct from dual-basis relabeling. That intensifies grammar consistency across three shared references rather than letting a third variant wash the pattern.
- [d:r:i] Refresh verification gates to at least match `122`'s detail level:
  - overlay ownership entry in `OVERLAY-MANIFEST.json` with mode `add`
  - focused contract coverage on shared-reference presence, five-section minimum, consumer workflows reading the reference by name, read-only character preserved at each consumer step, `.codex` observed basis plus held `.claude` annotation language staying explicit
  - propagation-family sibling refresh landing after `47` as the next non-uplift change-triggered refresh rather than as backfill into an older lifecycle carrier
  - governance trace landing in two places: one disposition/inheritance note in `entry-uplift-audit/dispositions/` and one intervention-proposals implementation note
- [d:r:i] Add one explicit not-authorized item covering the grammar-surface boundary: no silent widening of `mandatory-initial-read.md` from grammar-only to grammar-plus-content-pointer without a separate reopened proposal. That guards the grammar surface rather than leaving its boundary reconstructable from adjacent lines.

## What Should Stay As The Next Adjacent Consumer Branch

- [d:r:i] `update` plus `gsd-update` should stay the next adjacent consumer branch rather than join the first proof. Four reasons in the carrier-placement / propagation-visibility / maintainability / route-ownership frame:
  - carrier placement: `update.md` carries installer-supported runtime breadth across `codex`/`gemini`/`opencode`/`kilo`/`claude`. That breadth belongs to installer truth, not to repo-local operator continuity. Pulling `update` into the first slice would co-locate installer and repo-local operator jobs in the same implementation batch, which risks smuggling installer breadth into the new reference's provider horizon.
  - propagation visibility: `update.md` already owns runtime/package currentness, clean-install warning, custom-file backup, and patch recovery. Adding a shared-reference consumer step there in the same batch as the reference's first landing would combine at least two propagation families (compatibility-family refresh plus installer/materialization refresh) in one slice, when the broader family has been intentionally moving one family at a time per slice.
  - maintainability: the shared-reference shape should prove at the two smaller workflows before the most-complex one inherits. `update.md` is the largest of the four candidate workflows by line count and carries the widest runtime-detection block. A first-landing slice that widens it as well widens the edit surface more than `122`/`123` ever did in one batch.
  - route ownership: `update` owns runtime/package change, installer rerun, custom-file backup, patch recovery. The new shared reference owns repo-local uplift continuity. Keeping `update`'s first inheritance as a second adjacent batch keeps those route ownerships separate at their introduction moment rather than blending them under the same operator gesture.
- [d:r:i] `from-gsd2` plus `gsd-from-gsd2` should also stay the next adjacent consumer branch rather than join the first proof. Reasons:
  - carrier placement: `from-gsd2` is a skill wrapper, not a workflow file. Its contract shape differs from workflows. The shared-reference shape should prove at two workflow consumers first so the reference carries one coherent workflow-side precedent before a wrapper-side consumer inherits.
  - propagation visibility: `from-gsd2` already has an explicit uplift route pointer from `69`/`70` ("route separately to `$gsd-uplift-project --write` rather than treating format migration as the full project-uplift story"). That route pointer is the first consumer seam the new reference would reuse. Pulling it into the first batch would require re-authoring the existing route pointer language inside the wrapper during the same slice that introduces the reference itself.
  - maintainability: wrapper-side contract tests and workflow-side contract tests live at different levels; the first landing slice will prove cleaner if it proves one level first.
  - route ownership: `from-gsd2` owns `.gsd/` → `.planning/` format migration. The shared reference owns repo-local operator continuity. Keeping migration and continuity separate at introduction mirrors the `69`/`70` split that already landed.
- [d:r:i] Both next-adjacent consumers should inherit the reference by name once the first slice has proven the shape at `new-project.md` and `ingest-docs.md`. Neither should be silently absorbed into the first batch under a verification-gate line.

## Later Work To Keep Explicit

- [d:r:i] `update` plus `gsd-update` as next adjacent shared-reference consumer after the first proof lands
- [d:r:i] `from-gsd2` plus `gsd-from-gsd2` as next adjacent shared-reference consumer after the first proof lands
- [d:r:i] The installer/runtime breadth question inside workflows (narrowing the `codex`/`gemini`/`opencode`/`kilo`/`claude` runtime detection prose, or reframing it as installer-supported rather than repo-local-operator listing) stays a separate later question. This reread does not materially change that judgment; the shared-reference slice is not the vehicle for that rewrite.
- [d:r:i] Live `.claude` route translation or parity pressure stays held. The shared reference uses held `.claude` annotation as its provider horizon note; it does not authorize translation work.
- [d:r:i] Compatibility matrix claims, version-window claims, and third-runtime held-annotation widening remain later-family work.
- [d:r:i] Helper-side `RUNTIME_DIRS` versus `HELD_CLAUDE_RUNTIME_VERSION_REL_PATH` asymmetry from `119` stays held; this reread does not relax that hold.
- [d:r:i] Structural-row promotion inside `STATE.md` or `UPLIFT-MANIFEST.json`, standalone compatibility carrier, and write-recommending `compatibility_drift_reasons` widening from `119` remain held.
- [d:r:i] Extraction and npm/`npx` distribution work from `115` stays held until the current uplift, cross-runtime, and propagation contracts sharpen farther.
- [d:r:i] Whether `complete-milestone.md` eventually adopts the full `required`/`supporting`/`deeper` packet grammar remains a separate later-family question, carried forward from `122`.
- [d:r:i] Whether `mandatory-initial-read.md` later widens from grammar-only to grammar-plus-content-pointer remains a separate later question. This reread recommends leaving that grammar surface alone in the first slice.
- [d:r:i] Family-6 wider route-asymmetry mapping stays parallelizable rather than silently sequenced behind this shared-reference branch.

## Strongest Next Move

- [d:r:i] Move to implementation rather than reopen another proposal loop. The branch choice in `128` is the right next bounded object, and the remaining sharpening is localized rather than structural.
- [d:r:i] Before implementation opens, carry four revisions into `128` (or into an implementation-side proposal that stacks on `128`):
  - name `mandatory-initial-read.md` as grammar-only in this slice, with the new reference as a sibling pointed at directly by `new-project.md` and `ingest-docs.md`
  - write the `When To Surface` trigger sets concretely for greenfield `new-project.md`, brownfield `new-project.md`, new-mode `ingest-docs.md`, and merge-mode `ingest-docs.md`
  - tighten verification gates to match `122`'s detail: overlay ownership `add`, focused contract coverage items enumerated, propagation-family sibling refresh after `47`, governance trace in disposition plus implementation note
  - add one not-authorized item covering silent widening of `mandatory-initial-read.md` from grammar-only to grammar-plus-content-pointer
- [d:r:i] With those four sharpenings, the next concrete step is the implementation slice itself, followed by the matching propagation-family refresh as the sibling after `47` and the disposition/inheritance note under `entry-uplift-audit/dispositions/`.
- [d:r:i] Do not pull `update` or `from-gsd2` into that implementation. Hold both for the next adjacent consumer branch, which will have a cleaner basis once the reference shape is proven at the entry pair.

## How Proposal 128 Should Be Inherited

### Carry Forward

- [d:r:i] The branch-choice itself: `attach through a shared reference` is the correct next `119` classification to open now that `121`/`123`/`125`/`127` have discharged the deepen-in-place carriers.
- [d:r:i] The first-slice consumer pair of `new-project.md` plus `ingest-docs.md` as earliest-entry routes.
- [d:r:i] The proposed five-section minimum shape for the new reference, matching `122`/`123`.
- [d:r:i] The compact-to-narrative-to-typed reread order through `STATE.md` `## Project Uplift`, `UPLIFT-REPORT.md`, and `UPLIFT-MANIFEST.json`.
- [d:r:i] The repo-local provider horizon of observed `.codex` basis plus held `.claude` annotation as the reference's provider-discipline line.
- [d:r:i] The explicit read-only character for the consumer surfacing step, with write-side refresh routed through `$gsd-uplift-project --write` as a separate later route pointer.
- [d:r:i] `Compatibility posture: observed_basis_only` staying top-level, with held runtime annotation distinct from dual-basis relabel.
- [d:r:i] The held-later naming of `update` plus `gsd-update` and `from-gsd2` plus `gsd-from-gsd2` as the next adjacent consumer branch.
- [d:r:i] The not-authorized items already in the proposal: no matrix claims, no version-window claims, no `.claude` parity push, no helper-side `project_uplift.py` widening, no sweeping installer/runtime detection rewrite, no extraction or npm/`npx` work from `115`.
- [d:r:i] The requirement that propagation carriers refresh in the same batch because the slice moves a new shared reference plus a shared read-packet doctrine surface plus two entry workflow consumers.

### Revise Before Implementation

- [d:r:i] Clarify the role of `mandatory-initial-read.md` in the first slice. Preferred: `mandatory-initial-read.md` stays grammar-only and the new reference is a sibling pointed at directly by `new-project.md` and `ingest-docs.md`, mirroring the `123` pattern. If implementation instead chooses to widen `mandatory-initial-read.md` with a named pointer, that widening needs its own authorization rather than a verification-gate clause.
- [d:r:i] Concretize the `When To Surface` trigger sets for the four live consumer surfaces (greenfield `new-project.md`, brownfield `new-project.md`, new-mode `ingest-docs.md`, merge-mode `ingest-docs.md`) so the first slice inherits a workable trigger list rather than authoring it during implementation.
- [d:r:i] Sharpen the motivation framing so the first slice is described as adding a bounded repo-local uplift continuity carrier at entry routes, distinct from the separate later question of how the workflows present installer-supported runtime detection across the provider set.
- [d:r:i] Tighten verification gates to match the `122` precedent:
  - overlay ownership entry in `OVERLAY-MANIFEST.json` with mode `add`
  - focused contract coverage on shared-reference presence, five-section minimum, consumer workflows reading the reference by name, read-only character preserved per consumer, `.codex` observed basis plus held `.claude` annotation language staying explicit
  - propagation-family sibling refresh landing after `47` as the next non-uplift change-triggered refresh, not backfill into an older lifecycle carrier
  - governance trace landing in two places: one `entry-uplift-audit/dispositions/` inheritance note, one `intervention-proposals/` implementation note
- [d:r:i] Add one not-authorized item: no silent widening of `mandatory-initial-read.md` from grammar-only to grammar-plus-content-pointer without a separate reopened proposal.
- [d:r:i] Distinguish `from-gsd2` as a skill wrapper versus `update` as a workflow-plus-wrapper pair in the held-later layer so the next adjacent branch inherits both contract levels explicitly rather than leaving the wrapper-versus-workflow split for implementation-time discovery.

### Hold For Later

- [d:r:i] Pulling `update` into the first slice. The installer/runtime breadth inside `update.md` belongs to installer truth, not to the new shared reference's repo-local operator horizon. Bringing it into the first batch risks smuggling installer breadth into the reference's provider line.
- [d:r:i] Pulling `from-gsd2` into the first slice. Wrapper-side inheritance shape should follow workflow-side precedent rather than land alongside the first reference authorship.
- [d:r:i] Narrowing the runtime detection prose across `codex`/`gemini`/`opencode`/`kilo`/`claude` inside the entry workflows. That broader rewriting stays a separate later question; this slice does not authorize it.
- [d:r:i] `.claude` route translation or parity work.
- [d:r:i] Compatibility matrix, version-window, or third-runtime held-annotation widening.
- [d:r:i] Helper-side `RUNTIME_DIRS` versus `HELD_CLAUDE_RUNTIME_VERSION_REL_PATH` asymmetry, `compatibility_drift_reasons` widening, standalone compatibility carrier, structural-row promotion inside `STATE.md` or `UPLIFT-MANIFEST.json`.
- [d:r:i] Extraction and npm/`npx` distribution work from `115`.
- [d:r:i] Whether `complete-milestone.md` later adopts the full `required`/`supporting`/`deeper` packet grammar.
- [d:r:i] Whether `mandatory-initial-read.md` itself later widens from grammar-only to grammar-plus-content-pointer as a deliberate separate move.
- [d:r:i] Family-6 wider route-asymmetry mapping, which stays parallelizable rather than silently sequenced behind this branch.
