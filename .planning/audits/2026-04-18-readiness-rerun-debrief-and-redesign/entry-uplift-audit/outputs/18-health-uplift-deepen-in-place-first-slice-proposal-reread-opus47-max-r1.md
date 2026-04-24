Date: 2026-04-22
Status: active reread output (Opus 4.7 max r1)

# Health Uplift Deepen-In-Place First Slice Proposal Reread — Opus 4.7 Max R1

## What The Proposal Chooses Well

- The proposal grounds the route shape in the existing `119` classification (`deepen in place`, `read-only`) instead of re-deriving a rationale. That inheritance keeps the silent-carrier classification return working as the load-bearing intermediate object it was meant to be rather than letting each implementation slice re-argue its own carrier shape.

- The slice is bounded to two carriers — `health.md` and `gsd-health` — with no shared reference, no new helper, and no new wrapper family. That bounded posture sharpens the contrast with the `123` milestone-boundary slice: where two boundary workflows needed a shared reference to coordinate grammar, a single repair-facing workflow paired with its wrapper carries route-local uplift continuity more directly through in-place deepening than through an additional surface.

- The proposal preserves the existing `70` route split — structural repair stays structural repair, missing planning state routes to `new-project` or `ingest-docs`, later repo-local posture refresh routes separately to `$gsd-uplift-project --write` — and threads the new step through that pre-existing three-way boundary rather than mutating it. The distinction the slice introduces (read-only uplift continuity surfacing) slots into the space that was already held open between structural repair and write-side posture refresh, so the new step deepens an existing division rather than inventing one.

- The compact-scalar-first reading gradient (STATE.md `## Project Uplift` → UPLIFT-REPORT.md → UPLIFT-MANIFEST.json) matches the grammar the milestone-boundary shared reference landed under `123` (`Primary Compact Read` → `Supporting Narrative Read` → `Deeper Typed Read`). That cross-family grammar convergence carries the compact-versus-typed split more durably than if each route invented its own reading order.

- The proposal keeps `compatibility_posture: observed_basis_only` explicit when surfaced and keeps held-runtime annotation as annotation rather than dual-basis relabel. Those two disciplines preserve the compatibility-shape decisions landed in `116` and reaffirmed in `119`, and extend them into a new consumer surface without pressuring the anchor toward matrix or translation framing.

- The out-of-scope list is directly propagated from `119`'s explicit-hold carriers plus the per-carrier later family in `115`. No new shared reference, no auto-launch of `$gsd-uplift-project --write`, no compatibility matrix, no `.claude` parity/translation, no third-runtime widening, no structural-row promotion, no widening of `validate.health` semantics, no widening of `from-gsd2`/`update`/`mandatory-initial-read.md`, no extraction movement. The list names the specific pressures the slice could absorb by accident and refuses each one by name rather than through ambient restraint.

- The proposal names its own next-sibling shape concretely: one focused contract test, one compatibility-family propagation refresh, one intervention-proposals implementation note. That mirrors the `121`/`123` sibling pattern and keeps the post-land verification chain predictable across slices rather than letting each slice invent its own follow-through form.

- The `--repair` ordering is explicit: post-repair revalidation finishes before any later uplift follow-through is surfaced. That route-local ordering protects the structural-repair-first posture from being silently compressed into the same pass as read-only uplift continuity.

## Whether Health Should Deepen In Place

- `health.md` carries the next adjacent silent-carrier field after the transition/state pair (`121`) and the milestone-boundary pair (`123`) each became explicit carriers of uplift continuity. Transition/state covers phase close, milestone-boundary covers milestone open and close, and repair-facing entry is the next workflow where structural pressure can silently shift into later-posture pressure without any compact carrier making that shift legible. Naming health as the next single-carrier route keeps the uplift-family surface count growing by one explicit step at a time rather than through broader wrapper-family harmonization.

- Deepen-in-place is the shape that matches where the distinction actually lives. `health.md` already owns the precise three-way distinction the new step expresses (structural planning integrity / limited low-risk repair / separate later repo-local posture refresh). A shared reference would add a surface without adding ownership clarity, because only one workflow-plus-wrapper pair would consume it. That asymmetry is what makes the shared-reference shape right for milestone boundaries (where two workflows need coordinated grammar) and the deepen-in-place shape right for repair (where one workflow carries the full route distinction already).

- Potential counter-pressure: could `from-gsd2` also want similar uplift-continuity awareness, making a shared repair-family reference pay off? The `70` slice already separated `from-gsd2`'s migration/validation/later-uplift stages, and `from-gsd2` routes through `health` for post-migration structural validation. That routing makes `from-gsd2` an indirect consumer of health's new step rather than a parallel peer requiring its own shared-reference dependency, so the repair-family shared-reference pressure stays low for now. A later slice could reconsider this if a second repair-family wrapper acquires the same route-local uplift-continuity pressure that `health` carries now.

- Potential counter-pressure: could `update` be the next carrier instead? The proposal holds `update` for later. Update carries package/runtime version movement pressure, which sits adjacent to but distinct from repo-local posture refresh. Folding uplift-continuity awareness into `update` in this slice would blur the distinction between runtime/package basis movement and repo-local governing-doc/doctrine posture, and that distinction is exactly what the existing three-way route split in `health` is set up to preserve. Holding `update` as later-family work is coherent.

- The trigger predicate "route has actually shifted from repair to later posture follow-through" carries the right intent but is underspecified for operational evaluation. That under-specification is a local revision target, not a repudiation of the route shape — see Section 3 and Section 6 for the tightening.

- Net: health-next and deepen-in-place both intensify carry along the same dimension that `121` and `123` already widened (silent-carrier → explicit read-only uplift continuity), and they do so through the specific carrier where the three-way distinction already lives, without importing the coordinated-grammar pressure that only applies to two-workflow families.

## What The Health Route Should Read And When

### Primary Compact Read — STATE.md `## Project Uplift`

The live STATE.md block carries the scalar posture set that a repair-facing operator can read without opening the larger report:

- `Last uplift pass` (timestamp)
- `Last uplift class`
- `Phase boundary signal`
- `Compatibility posture: observed_basis_only`
- `Observed runtime basis`
- `Held runtime annotation`
- `Current recommendation`
- Pointers to `UPLIFT-REPORT.md` and `UPLIFT-MANIFEST.json`

That compact digest is the right first read because it carries the compatibility anchor, the observed-vs-held split, and the current recommendation in one contiguous scalar block that sits next to `Accumulated Context` and `Session Continuity` — i.e., in the same top-level carrier a repair-facing operator is already oriented toward. Starting here keeps the route-local read from pulling the typed manifest into the operator's immediate attention when the compact block already answers the live question.

### Supporting Narrative Read — UPLIFT-REPORT.md

Widen to the narrative report when the compact digest does not carry enough route-local context. The live report adds:

- `Before-State Posture` (planning surface, current state status, runtime directories, prior uplift memory, doctrine movement, phase boundary signal, phase context carrier)
- `Recommendation Reasons`
- `Compatibility Basis` with version alignment, schema versions, and the full `Compatibility Check Protocol`
- `Held Runtime Annotation` detail (runtime, version, source, annotation posture, note)
- `Wider Compatibility Claims Held`
- `Seed Corpus Posture` summary
- `Carrier Posture` table with fingerprints

Typical widen triggers: the operator needs to know which specific runtime-basis movement drives the current recommendation; the operator needs to know which check-protocol step still applies; the operator needs to know which held-later families block later write-side refresh.

### Deeper Typed Read — UPLIFT-MANIFEST.json

Widen to the typed manifest only when basis or annotation ambiguity remains after the first two reads. The live manifest adds:

- `schema_version`, `generated_at`, `mode`, `last_uplift_class`
- `phase_boundary_signal` typed object
- `doctrine_reference_hash`, `project_fingerprint_hash`
- `held_later_families` array with pointers
- `compatibility_basis` typed object including `held_runtime_annotation` substructure and `check_protocol` array
- `seed_corpus_posture` typed object
- `carriers` array with per-carrier fingerprint shape and value

This typed surface is the right last-resort read because it is the authoritative machine-readable form; widening here only when the compact and narrative reads leave ambiguity preserves the typed-detail-as-deepest grammar that `121` carries at phase close and `123` carries at milestone boundaries.

### When To Surface The Step At All

- After structural health validation (including `verify_repairs` when `--repair` was used) completes.
- Before `format_output`.
- Only when structural planning state is present. If missing, keep the existing `new-project` / `ingest-docs` routing.
- Only when the uplift compact block signals a live posture question — compatibility-posture movement, observed-basis change, held-runtime annotation change, or `Current recommendation` naming later repo-local refresh. If the block signals `Continue with ordinary routing` and the repair question has already been fully answered by validation, the step stays silent so repair output is not diluted by an inactive posture reread.

## How Workflow And Wrapper Should Divide The Route

- `gsd-sdk query validate.health` stays the structural-health authority. The new step does not widen or alter validator semantics.

- `health.md` (workflow) carries the operational sequence: `parse_args` → `run_health_check` → `keep_route_boundaries_explicit` → (when `--repair`) `verify_repairs` → the new `Review Project Uplift Health Follow-Through` step → `format_output`. The new step reads the compact digest first and widens conditionally, and it stays read-only.

- `gsd-health` (wrapper/SKILL.md) carries the outer boundary: structural health remains the objective, read-only uplift continuity reread may follow health, and write-side refresh remains a later separate route. The wrapper already recommends routing to `$gsd-uplift-project --write` as a separate follow-through; the new step sits inside the wrapper's existing boundary rather than displacing it.

- `$gsd-uplift-project --write` stays the write-recommending authority. The new step never launches it.

This three-way ownership split is the slice's durable structural contribution:

1. structural-health authority lives in `validate.health`
2. route-local read-only uplift-continuity surfacing lives in the new `health.md` step
3. write-side posture-refresh authority lives in `$gsd-uplift-project --write`

The proposal's current Verification Gates section names the split as a gate to protect. The slice should also name the split as its positive structural shape — what the slice carries, not only what the slice must not breach.

One placement sharpening: the proposal says the step sits "after health validation and before final output formatting." That phrasing leaves open whether "health validation" means only the initial `run_health_check` or also the post-repair `verify_repairs`. The step should sit after all validation (including post-repair revalidation when `--repair` was used). The proposal already states this under `What The Slice Should Carry`, so the fix is to tighten the step-placement phrase in the workflow text itself during implementation.

## What Must Stay Out Of Scope

The proposal's own no-authorize list is appropriate and should be carried directly:

- No new shared reference for `health`.
- No automatic launch of `$gsd-uplift-project --write`.
- No compatibility matrix or version-window claims.
- No `.claude` parity, translation, or third-runtime widening.
- No structural-row promotion.
- No widening of `validate.health` semantics into repo-local posture adjudication.
- No widening of `from-gsd2`, `update`, or `mandatory-initial-read.md` through this slice.
- No extraction/npm/`npx` movement.

Three additions worth naming explicitly in the implementation note so they don't drift silently into the step during the landing pass:

- The new step must not compute compatibility drift or recommend basis changes. Drift detection lives in `project_uplift.py`'s `compatibility_drift_reasons`, which `119` classifies as `explicitly held, write-recommending`. The new step surfaces existing compatibility posture; it does not derive new posture judgments.

- The new step must not widen the health footer into a second uplift workflow. The existing footer already carries one-line routing to `$gsd-uplift-project --write` when structural health is acceptable but repo-local posture still needs refresh. The new step may cite the compact posture digest but must not duplicate or displace that footer routing.

- The new step must not cache, reformat, or republish uplift-manifest content inside the health output. The manifest remains the typed carrier; the health step reads it in place when ambiguity warrants the deeper read and does not mirror any of its fields into a new health-local surface.

## How This Proposal Should Be Inherited

### Carry Forward

- The `deepen in place`, `read-only` classification from `119`.
- The two-carrier bounded scope (`health.md` + `gsd-health`).
- The reading gradient (STATE.md compact → UPLIFT-REPORT.md narrative → UPLIFT-MANIFEST.json typed) with widen-only-when-ambiguity-remains discipline.
- Preservation of `compatibility_posture: observed_basis_only` and held-runtime annotation as annotation.
- The three-way ownership split: `validate.health` / new read-only step / `$gsd-uplift-project --write`.
- The trigger discipline: only surface when structural planning state is present AND the uplift compact block signals a live posture question.
- The `--repair` ordering: post-repair revalidation finishes before uplift-continuity surfacing.
- The next-sibling shape: one focused contract test, one compatibility-family propagation refresh, one implementation note.
- The explicit out-of-scope list copied directly from the proposal.

### Revise Locally

- Tighten the trigger predicate for "route has actually shifted from repair to later posture follow-through" into an operationally evaluable form. Suggested formulation: surface the step when health status is `healthy` or `degraded-non-structural` AND the STATE.md `## Project Uplift` block exhibits at least one of: a change in `Compatibility posture`, a change in `Observed runtime basis`, a change in `Held runtime annotation`, or a `Current recommendation` value naming later repo-local refresh. This makes the predicate reproducible across operators instead of interpretive.

- Inherit the milestone-boundary reference's five-section headings inside the new health step's local structure: `Primary Compact Read`, `Supporting Narrative Read`, `Deeper Typed Read`, `Interpretation Frame`, `When To Surface`. Health does not consume the shared reference (it deepens in place), but using the same local grammar keeps cross-family reading order consistent without creating a shared-reference dependency.

- Sharpen the step-placement phrasing in the workflow text: "after all structural health validation (including `verify_repairs` when `--repair` was used) and before `format_output`." The current proposal has this intent but the exact phrasing in the inserted step should remove ambiguity about whether post-repair revalidation is included.

- State the three-way ownership split as the slice's positive structural contribution in `What The Slice Should Carry`, not only as a verification gate. This makes the slice's durable shape legible on first read rather than only implied through the gate list.

- Add three explicit holds to the no-authorize list (see Section 5 above): no drift computation, no second-uplift-workflow footer widening, no caching/reformatting of manifest content into health output.

### Keep Later

- Broader read-packet widening for `health` beyond this one route-local uplift step (carried in the proposal's Held Later list).
- Auto-repair-plus-auto-refresh chaining.
- Wider repair/migration/update family harmonization beyond the current route split.
- Compatibility-family widening beyond observed-basis + held-annotation discipline — matrix claims, version-window claims, upstream-template drift all stay in `118`/`119` explicit-hold space.
- Structural-row promotion for compatibility — held under `118`/`119` and reaffirmed in the `121` and `123` slices.
- `from-gsd2` uplift-continuity carrier: post-migration structural validation already routes through `health`, so the new step serves `from-gsd2` consumers indirectly; a parallel `from-gsd2`-side carrier can wait until a second repair-family route accumulates independent uplift-continuity pressure.
- `update` follow-through uplift-continuity carrier: package/runtime version movement is distinct from repo-local posture refresh, and merging those routes too early would blur the `71`/`72` hold.
- Cross-repo extraction and distribution from `115`.
- Live `.claude` translation or third-runtime widening: reachable only through family-6 route mapping when it opens, not through any repair-family appetite.

### Next Bounded Move

- Land the `health.md` + `gsd-health` slice with the local revisions above folded in, following the same tracked-overlay-plus-materialization discipline used for `121` and `123`.

- Match the slice with three sibling artifacts:

  - one focused contract test at `tooling/codex/tests/test_health_uplift_deepen_in_place_contract.py` (parallel shape to `test_transition_uplift_continuity.py` and `test_milestone_boundary_uplift_shared_reference_contract.py`). It should verify:
    - the new step exists in `health.md` with the expected heading
    - the reading gradient names STATE.md, UPLIFT-REPORT.md, and UPLIFT-MANIFEST.json in the declared order
    - the wrapper preserves the three-way ownership split (structural-health authority / read-only continuity / write-side refresh)
    - the step is read-only — never invokes `$gsd-uplift-project --write`
    - the step is guarded by the tightened trigger predicate
    - step placement sits after `verify_repairs` when `--repair` is passed and before `format_output`

  - one compatibility-family propagation refresh at `propagation-audit/46-health-uplift-deepen-in-place-change-triggered-refresh.md` (next sibling after `45`), recording the route-local uplift consumer surface the slice adds.

  - one intervention-proposals implementation note at `intervention-proposals/125-health-uplift-deepen-in-place-first-slice-implementation.md`, following the `121`/`123` implementation-note shape.

- After the slice lands and its sibling chain completes, the next `119` priority decision becomes a choice between:
  - picking up an explicitly-held carrier from `119` (discuss/plan/execute entry points, verifier lifecycle, write-recommending drift path, helper-side `RUNTIME_DIRS`/`HELD_CLAUDE_RUNTIME_VERSION_REL_PATH` asymmetry) — each still held for now;
  - picking up a held-later adjacent family (update follow-through uplift continuity, wider repair/migration harmonization) — still later-family work, not next-step absorption;
  - or, if `118`/`119` cross-runtime composition pressure re-opens, returning to the family-6 route-asymmetry mapping rather than to any route-translation appetite inside the repair family.

- The reread itself should not be read as a decision between those later routes. Its scope is whether `health.md` deepens in place next and how. That question carries explicitly, with the local revisions above, and the next bounded move is the implementation slice plus its sibling chain — not another proposal loop around the same carrier.
