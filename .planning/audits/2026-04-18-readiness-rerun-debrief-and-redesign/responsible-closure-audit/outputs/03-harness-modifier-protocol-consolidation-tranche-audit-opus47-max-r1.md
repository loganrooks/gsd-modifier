Date: 2026-04-23
Status: frozen external-lane return

# Harness Modifier Protocol Consolidation Tranche Audit

## Audit Framing

- [g:r:i] The governing question is whether the bounded pair `169 + 60` defines the right next program-wide tranche for harness-modifier development, and where the pair still has under-cut edges that a bounded reread should sharpen before implementation.
- [d:r:i] This audit reads `169` as the candidate program-wide protocol object and `60` as its paired propagation companion over the already-landed `145 + 53` slice.
- [d:r:i] The posture is revision-over-replacement: the pair is directionally load-bearing, and the stronger move is to sharpen the reread's expected return rather than re-cut the tranche shape.

## Domain Split

- [d:r:i] The split `development-side protocol now` / `harness-in-action parallelization later` remains sharp along its primary seam:
  - development-side protocol governs how the modifier is *built and iterated*: audit / review-lane machinery, governance routing, propagation carry, verification, extraction, responsible-closure sequencing.
  - harness-in-action parallelization governs how the modifier *runs its own host workflows*: `execute-phase.md`, `review.md`, `map-codebase.md`, `ingest-docs.md`, `diagnose-issues.md`, `manager.md`, `config.json.parallelization`.
- [d:r:i] The carriers differ cleanly: development-side protocol lands primarily in `.planning/audits/`-family doctrine, `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`, `.planning/AGENTS.md`, `WORKFLOW.md`, and the `readiness.md` compaction prompt. Harness-in-action parallelization would land primarily in `.codex/get-shit-done/workflows/` and overlay-side workflow contracts. That is the concrete test of split sharpness: the two sets of target files barely intersect.
- [d:r:i] The remaining seam in view: `145 + 53` is itself a harness-in-action carrier change (review-workflow family — `review.md`, `gsd-review/SKILL.md`, helper under `harness_modifier/capture/`), and `60` uses it as the propagation test case for the development-side tranche. The pair handles this by routing the propagation question into development-side consequences (workflow doctrine, continuity/compaction, launch-truth/timing, safe-overlap logic, review-route family doctrine), not into review-run UX redesign. The scope guard is present inside `60` ("Keep broader review-route redesign, subject splits, retry/resume widening, and harness-in-action parallelization out of this audit"), which keeps the seam bounded rather than letting it become a smuggling channel for review-family rewrite appetite.
- [d:r:i] What the split could expose more deliberately: development-side protocol and harness-in-action parallelization both touch the composition-ownership question across compaction boundaries. That is a shared carrier (the `readiness.md` compaction prompt), and the tranche should name whether the compaction prompt carries development-side lifecycle-loop state explicitly or continues to carry only the Phase 01 readiness surface plus generic companion-lane state.

## Protocol Slice Judgment

- [d:r:i] The tranche is cut at a level that can be implemented without growing into a giant control system, because the four named scopes in `169` map to four bounded carrier operations rather than to new infrastructure:
  1. overlap protocol → per-lane declarative surface plus tightening of the existing `Bounded Parallelization And Overlap` section in `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`.
  2. composition-keeping delegation → explicit parent-thread retention list inside the same pattern library.
  3. intervention lifecycle loop → a required declaration shape on proposal/implementation artifacts plus a named disposition verb at inheritance.
  4. paired propagation obligation → one concrete propagation-audit note (`60`) over an already-landed slice, not a standing telemetry system.
- [d:r:i] Where the cut is still under-defined and the reread should sharpen before implementation:
  - The carrier-mapping decision is not yet resolved inside `169`. The proposal correctly asks "Which Carriers Should Actually Change?" and correctly warns against pushing everything into `AGENTS.md`, but it leaves the actual allocation for the reread. The reread should produce an explicit carrier map (see *What Must Land Now*) rather than letting implementation improvise it.
  - The lifecycle-verification definition is open. `169` rightly refuses to invent a telemetry stack and says "Name what counts as intervention success, under-carry, or mismatch," but the concrete answer (per-intervention declarative carrier plus disposition-verb discipline) is not yet stated. Keeping the question open through proposal is appropriate; letting implementation start without an answer would push the discipline back into operator habit.
  - The first-slice granularity is not yet named. A plausible first slice is pattern-library-dominant (overlap declaration template, parent-thread retention list, proposal-artifact intended-effects / propagation-obligations sections) with `.planning/AGENTS.md` and `readiness.md` touched only where the cross-family doctrine is actually thin. The reread should make the granularity explicit so the slice does not silently expand into root-doctrine rewrites.
- [d:r:i] What broadens in this slice that was previously carried only as operator habit:
  - lane-local authority-surface naming moves from implicit to declarative, which intensifies future audit traceability when a lane later needs to be challenged, reread, or rerun.
  - parent-thread retention becomes an enumerated rule rather than a pattern note, which preserves composition ownership under delegation pressure.
  - intervention-lifecycle declarations become inspectable artifacts, which lets the `accept / revise / park / reject` discipline operate over named obligations instead of reconstructed intent.

## Lane-Local Overlap And Must-Wait Rules

- [d:r:i] The class-level rules already live in `AUDIT-LANE-PATTERN-LIBRARY.md § Bounded Parallelization And Overlap` (earned patterns, forbidden overlaps, companion carry list, recheck rule paired with the timing-estimate section) and in the parallelization disposition `01` (no packet/spec/prompt edits to a live lane, no refmap/topology rewrites, no installer/materialization rewrites that depend on the prior basis, no Phase 01 rerun crossing).
- [d:r:i] What the tranche should add beyond the class level is a lane-local declarative surface so each lane carries its own overlap facts on its face instead of requiring a reader to reconstruct them from family doctrine:
  - frozen basis (commit, packet/spec/prompt paths)
  - read set (the specific files the lane is reading)
  - authority surface (what it is allowed to write, and where)
  - companion-safe carry (what can travel alongside)
  - must-wait set (what inherits before this lane can be touched)
  - recheck window (first recheck at the timing-estimate boundary; second recheck if companion carry finishes first)
- [d:r:i] Concrete placement recommendation: extend the existing `Opening note` and `Packet` sections in `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md` to require these fields when the lane is parallelization-adjacent, rather than writing a new top-level doc. This preserves the progressive-disclosure shape in `.planning/AGENTS.md § Governance-Doc Progressive Disclosure`.
- [d:r:i] Recheck discipline should stay paired with the `Timing estimate` section rather than float as a standalone rule. The pair already says: use the timing estimate as the first recheck window; if companion carry finishes first, check the lane rather than idling. The tranche's contribution is to make per-lane recheck windows explicit on the lane's face, not to invent a new recheck doctrine.
- [d:r:i] What should remain explicitly outside this tranche:
  - promotion of single-writer / lane-exclusive authority surface maps into root/planning agent doctrine (disposition `01` holds this later until one more real overlap exercise).
  - fan-out packet template creation (same disposition, same trigger).
  - a `Parallelization Impact` extension inside `$gsd-propagation-review` (held later until a bounded proposal materially touches a parallelization-adjacent surface).

## Delegation And Composition Ownership

- [d:r:i] The pair's stronger carry here is the parent-thread retention list. The pattern library currently names "narrower delegated work with parent-thread composition ownership" as one earned pattern but does not enumerate what the parent retains, which leaves composition ownership as operator habit rather than declarative rule.
- [d:r:i] The retention list the tranche should make explicit:
  - disposition authority (`accept / revise / park / reject`)
  - governance carry (`INDEX.md`, `CURRENT-STATE.md`, `STATUS.md`, register files)
  - propagation carry (which neighbors move with the slice)
  - checkpoint boundaries (when a worktree is clean and where the checkpoint commit lands)
  - inheritance writing (the disposition artifact itself)
- [d:r:i] Work that is earned for bounded sub-agents, kept distinct from work the parent retains:
  - bounded classification (e.g., field-map production, pattern extraction)
  - packet assembly under a parent-owned spec
  - gap identification and candidate-list generation
  - focused audit reads with an explicit output shape
  - focused implementation slices under a governed proposal
- [d:r:i] The seam the proposal does not yet name and that the reread should surface: composition ownership is vulnerable across compaction. The `readiness.md` compaction prompt preserves the Phase 01 package state and companion-lane state, but it does not explicitly preserve an intervention-lifecycle declaration (intended effects, propagation obligations, current disposition) when the active work is a harness-program tranche. Extending the compaction prompt with a small harness-program block (active tranche id, lifecycle-loop state, paired propagation companion state) would keep composition ownership durable under compaction without growing the prompt into a generic telemetry system.
- [d:r:i] Out of scope here, and should remain so: this is about development work, not about harness-in-action workflow fan-out (e.g., parallel execute-phase workers, parallel reviewer runs, subject-keyed review-route fan-out). `166` and disposition `01` both hold those later explicitly.

## Intervention Lifecycle Review Monitor Iterate Loop

- [d:r:i] The loop the proposal names — plan intervention → name intended effects and propagation obligations → land slice → monitor actual effects → audit mismatches / under-carry → revise protocol or route later follow-through — is already being run by operator habit across the workspace (see `145 → 53 → 60`, `161 → responsible-closure lane 01 → 166 → 169`, `95 / 96 → propagation-audit/15 → propagation-audit/02-06`). The tranche's job is to move the loop from habit into declarative protocol.
- [d:r:i] The load-bearing addition is a required declaration shape on proposal and implementation artifacts, not a new telemetry stack:
  - `Intended Effects` section on each intervention proposal (what the slice should newly carry, intensify, or broaden).
  - `Propagation Obligations` section on each intervention proposal (direct producers, direct consumers, narrative mirrors, runtime/registry carriers, durable outputs — cross-referenced against the `.planning/AGENTS.md § Contract-Propagation Hygiene` list).
  - `Monitor Target` section on each implementation artifact (what would count as under-carry or mismatch, named without inventing automation).
  - Explicit disposition-verb close on every inheritance note (`accept / revise / park / reject`), already partly in use.
- [d:r:i] Verification without a telemetry stack: the verification surface is the paired propagation audit plus the disposition-verb close. A slice carries its obligations when the paired propagation note finds those obligations already moved across named neighbors; a slice is `under-carried` when the propagation note surfaces ownerless neighbors; a slice is in `mismatch` when observed effects diverge from the declaration. These states can be named in prose inside inheritance artifacts without a lifecycle state machine, per-phase signal caps, or sensor daemons.
- [d:r:i] What should remain explicitly later, carried forward from `166 § Held Later`: the full Reflect adaptive stack (auto-collection, reentrancy-locked sensor daemons, synthesizer / reflector agents, lifecycle state machine, per-phase signal caps, cross-project KB aggregation, hook-install wiring) and `automation.level >= 2` for modifier-owned features. The tranche should name the loop declaratively; it should not import Reflect infrastructure.
- [d:r:i] Where the proposal could sharpen: the relationship between the lifecycle loop and the already-active `$gsd-propagation-review` workflow is not yet stated. The natural routing is that `$gsd-propagation-review` is the operator-facing carrier for the `monitor actual effects` + `audit mismatches` stages when a slice spans several producer / consumer families. The reread should make this routing explicit rather than leaving it to re-derivation.

## Propagation Companion Judgment

- [d:r:i] `60` is pointed at the right already-landed slice. `145 + 53` already moved durable run-home ownership, launch-truth carry, timing calibration, last-message salvage, and reviewer-state classification — the same families the protocol tranche will govern more explicitly. Using a slice that has already touched those families (rather than a clean unrelated one) gives the propagation audit real surface to test against.
- [d:r:i] The scope guards in `60` hold the boundary: broader review-route redesign, subject-keyed splits, retry / resume widening, harness-in-action parallelization rewrites, and telemetry-system build-out are all explicitly out of scope. This keeps the propagation note from drifting into review-route-audit-family appetite or into review-family workflow-rewrite appetite.
- [d:r:i] Where `60` is still under-cut and the reread should sharpen it: the note asks "Which surfaces are still ownerless or under-carried?" without naming candidate surfaces. Without a candidate list, the audit risks returning "nothing found" and not earning its slice. The reread should load `60` with concrete candidate surfaces so the audit actually probes rather than surveys:
  - `tooling/portable-gsd/overlay/tooling/compact-prompts/readiness.md` — does it preserve the helper-backed reviewer-state classification vocabulary (`complete` / `partial` / `absent`) and the timing-calibration expectation when the active work is review-family?
  - `.codex/get-shit-done/workflows/propagation-review.md` — does it name the new timing-calibration and launch-truth-lite carriers as propagation surfaces for review-family slices?
  - `review-route-audit/README.md § Expected Artifact Pattern` — does it still carry the correct family-local artifact set now that helper-backed run-home is live?
  - `.planning/AGENTS.md § Launch-Truth Discipline` — does it carry the `launch-truth-lite` vs full `requested-versus-effective capture` distinction introduced by `145`?
  - `AUDIT-LANE-PATTERN-LIBRARY.md § Launch-truth note` and `§ Timing estimate` — do they still correctly describe the review-family case after helper-backed run-home?
  - `HARNESS-IMPROVEMENT-REGISTER.md` and the workspace `CURRENT-STATE.md` / `STATUS.md` — do they name the completed review-route first slice correctly in the active-family listing?
- [d:r:i] Whether a second propagation follow-through note is earned is something only the reread can decide. The right posture is: if the audit surfaces one or two ownerless carriers that can be patched inside the tranche's implementation slice, one follow-through note is not earned. If the audit surfaces a family of ownerless carriers that needs its own bounded carry (e.g., compaction-prompt uplift spanning multiple families), then one second propagation note *is* earned and should open cleanly rather than being packed into the protocol tranche.
- [d:r:i] Pairing cadence: the note correctly says "Read this note together with `169`" and "Run one bounded reread over the pair before implementation." This pairing is load-bearing because the audit's candidate under-carried surfaces feed directly into the protocol tranche's carrier-mapping decision. Running them separately would lose that feedback.

## What Must Land Now

- [d:r:i] One bounded reread over `169 + 60` together as a single lane, producing one composite return that answers:
  - the carrier-mapping decision (which piece of the protocol tranche lands in `../../governance/AUDIT-LANE-PATTERN-LIBRARY.md`, which in `.planning/AGENTS.md`, which in `readiness.md`, and which remains not-written because the existing doc already carries it)
  - the first-slice granularity (the smallest load-bearing slice, which should be pattern-library-dominant)
  - the lifecycle-verification definition (per-intervention declarative carrier plus disposition-verb discipline, explicitly not a Reflect-style stack)
  - the concrete list of ownerless or under-carried surfaces in the `145 + 53` neighborhood
  - whether a second propagation follow-through note is earned and what its scope would be
- [d:r:i] One sharpening of `60` before the reread runs: load it with the candidate under-carried surfaces enumerated in *Propagation Companion Judgment* so the audit probes rather than surveys. This can be a small edit to `60` itself rather than a new artifact.
- [d:r:i] One explicit preservation of `167` as the next extraction-family object, held outside this reread's implementation window because `167` would touch install-contract / overlay-roster authority surfaces that could collide with the tranche's authority-surface declarations if run concurrently.
- [d:r:i] The first protocol-slice landing should include:
  - an extension of `AUDIT-LANE-PATTERN-LIBRARY.md § Opening note` / `§ Packet` requiring lane-local declaration fields (frozen basis, read set, authority surface, companion-safe carry, must-wait set, recheck window) when the lane is parallelization-adjacent
  - a new subsection under `§ Bounded Parallelization And Overlap` enumerating the parent-thread retention list
  - a new subsection (likely under `§ Review And Quality Discipline` or a new `§ Intervention Lifecycle`) naming the required declaration shape for proposals (`Intended Effects`, `Propagation Obligations`, `Monitor Target`) and the required disposition-verb close
  - a small extension to the `readiness.md` compaction prompt adding a harness-program block (active tranche id, lifecycle-loop state, paired propagation companion state) so composition ownership survives compaction
  - a companion disposition artifact under `responsible-closure-audit/dispositions/` recording the reread's return and any follow-through routing

## What Should Remain Explicitly Later

- [d:r:i] `direct doctrine held later with named trigger`:
  - single-writer / lane-exclusive authority surface map as root / planning doctrine — trigger: one more real overlap exercise beyond this tranche (per parallelization disposition `01`).
  - fan-out packet template — trigger: one more real overlap exercise.
  - `Parallelization Impact` extension inside `$gsd-propagation-review` — trigger: a bounded proposal that materially touches a parallelization-adjacent surface.
- [d:r:i] `bounded-open branches`:
  - second overlay tranche classification beyond its current bounded opening note.
  - cross-vendor responsible-closure audit over payload-home closure plus the first observation-carrier slice (already scheduled by `161` commitment `#6`).
  - standalone harness-modifier repo / npm / `npx` distribution / broader host-context deployability.
- [d:r:i] `preserve-only seams`:
  - harness-in-action workflow parallelization rewrites (`execute-phase.md`, `review.md`, `map-codebase.md`, `ingest-docs.md`, `diagnose-issues.md`, `manager.md`, `config.json.parallelization`).
  - execute-family redesign.
  - subject-keyed review-route splits.
  - retry / resume redesign for review runs beyond bounded last-message salvage.
  - full `.claude` materialization claim beyond the held-annotation posture in `141`.
  - vanilla `--gemini` / `--opencode` / other-provider support.
- [d:r:i] `reversal-sensitive boundaries`:
  - Phase 01 rerun boundary — must stay held across every lane this tranche launches.
  - the cross-vendor responsible-closure audit's trigger — do not move it earlier just because this tranche produces a cleaner protocol baseline.
- [d:r:i] `inquiry debt`:
  - full Reflect adaptive stack (auto-collection, reentrancy-locked sensor daemons, synthesizer / reflector agents, lifecycle state machine, per-phase signal caps, cross-project KB aggregation, hook-install wiring, `automation.level >= 2`).
  - richer telemetry / semantic-signal capture, post-deploy correction loops.
  - workflow-level parallelization rewrites across harness-in-action routes.
  - promotion of `Horizon Routing` into `.planning/AGENTS.md`.
  - dogfooding the modifier against its own development program.

## Exact Next Moves

1. [d:r:i] Treat this audit as the inheritance boundary for the tranche's readiness-to-implement judgment: the pair `169 + 60` is directionally load-bearing, and the next move is a bounded reread rather than direct implementation.
2. [d:r:i] Edit `60` in place to load it with the candidate under-carried surfaces enumerated in *Propagation Companion Judgment* (`readiness.md` compaction prompt, `$gsd-propagation-review` workflow, `review-route-audit/README.md`, `.planning/AGENTS.md § Launch-Truth Discipline`, `AUDIT-LANE-PATTERN-LIBRARY.md § Launch-truth note` / `§ Timing estimate`, `HARNESS-IMPROVEMENT-REGISTER.md`, workspace `CURRENT-STATE.md` / `STATUS.md`). Keep the scope guards intact.
3. [d:r:i] Run one bounded reread over `169 + 60` together as a single lane. The reread's required return is the composite set in *What Must Land Now*: carrier map, first-slice granularity, lifecycle-verification definition, ownerless-surface list, follow-through-note earn judgment.
4. [d:r:i] Land the first protocol slice against the carrier map from step 3. The slice should be pattern-library-dominant, with a small harness-program extension in `readiness.md` and only the cross-family-doctrine pieces touching `.planning/AGENTS.md`. Do not touch root `AGENTS.md` or `WORKFLOW.md` in this slice unless the reread explicitly earns it.
5. [d:r:i] Pair the implementation with the propagation carry the reread earned: either fold the ownerless-surface patches into the same slice (if few and contained), or open a second bounded propagation follow-through note (if the ownerless surfaces form a distinct family such as compaction-prompt uplift).
6. [d:r:i] Write the responsible-closure-audit disposition for this tranche recording: the composite reread return, the first-slice boundary, what remained later, and the disposition verb on each held-later item.
7. [d:r:i] Keep `167` as the next extraction-family object and do not run it concurrently with the first protocol-slice implementation — the authority-surface declarations in the slice and the install-contract / overlay-roster surfaces `167` would touch should land in sequence, not in parallel.
8. [d:r:i] Keep harness-in-action parallelization explicit and later. Return to the responsible-closure deployability bundle (observation-carrier proposal, first host-exercise packet) from the cleaner protocol baseline as medium-horizon follow-through, per `166 § Medium Horizon`.
9. [d:r:i] Keep the Phase 01 rerun boundary held across every lane this tranche launches, including the reread, the implementation slice, and any second propagation follow-through note.
