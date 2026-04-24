Date: 2026-04-22
Status: completed Opus widening lane over cross-runtime concern-family split

# Uplift Cross-Runtime Concern-Family Split — Opus 4.7 Max R1

## What The Concern-Family Split Now Clarifies

- [d:c+i] The split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md](../../intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md) adds one durable routing artifact that the first-exercise reread alone did not carry: a short, citable list of cross-runtime concern families at parent-thread level, plus an explicit commitment that the next Opus lane should act on the split itself rather than pick among the three near-term sub-families by ambient preference. That is a procedural carry, not only a field-content carry.
- [d:c+i] The split sharpens the routing posture against two specific drift modes named earlier in this audit: (a) collapsing the family back into one held-later `cross-runtime uplift composition` line [.planning/UPLIFT-MANIFEST.json:33-36] and (b) letting route-translation appetite widen silently into whole-runtime parity framing [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:10-11, 30-32]. Those two drift modes are different risks. Naming both at once carries more than naming either alone, because it makes `family-by-family` the durable posture rather than a one-off caveat.
- [d:c+i] Where the reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:31-41] carries ten distinct families, the split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:18-27] carries eight. The compression is a deliberate surface tradeoff (fewer rows for durability) and it thins three sub-decisions the reread had earned:
  - The distinction between family 2 (continuation-floor overlap at workflow-name level) and family 3 (consumer-chain asymmetry at the continuation edge) appears in the reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:33-34] but is preserved in the split note as a single line, "consumer-chain asymmetry" [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:20].
  - The distinction between family 5 (intervention-family slice) and family 6 (wider uncharted Codex-only route field) is preserved as two rows in the split note [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:22-23], which carries cleanly.
  - The sub-family inside family 1 (Claude-side translated doctrine as a carry-surface, not only a routing synonym) earned by the reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:21] is not visible in the split note's eight-row list.
- [d:c+i] The split sharpens the held surface in one additional way the reread named once but the split note preserves explicitly: the three near-term sub-families are surfaced as co-equal candidates rather than as an implicit ordering. [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:34-56] presents compatibility-family widening shape, wider route-asymmetry field mapping, and consumer-chain asymmetry scoping as three independent decision surfaces, each with its own question and its own candidate shapes. That framing shape carries more than "pick one" alone, because it lets the sequencing argument be itself the next judgment rather than the first narrow assumption.
- [d:r:i] The split note also carries one posture commitment worth naming separately: "The lane should stay Opus-led" [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:65]. That is the assist-pattern-layer posture being made explicit for this specific sub-family, not only inherited from [../../intervention-proposals/103-uplift-agent-assist-patterns.md:75, 119-125] in the abstract.
- [d:r:i] The split note's "Immediate Recommendation" at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:58-66] is itself a delegation: the current lane (this review) should produce a sharper concern-family map with carrier status and recommend a next bounded proposal. The split note anchors the next lane's output shape rather than prescribing its content, which keeps the Opus widening posture intact.

## What Still Needs Cleaner Carrier Separation

- [d:r:i] **Translated Claude-side doctrine as its own sub-family inside family 1**. [CLAUDE.md:23-31] and [.planning/CLAUDE.md:15-23] carry at least five pieces of translated doctrine (anti-threshold posture; deficit-pseudo-positive prohibition; static-positive prohibition; propagation-neighbor obligation; `do not mirror` boundary). These are doctrine, not routing. The current carriers are the wrapper files themselves. That works as long as the shared-doctrine family is read at the canon-plus-wrapper layer, and it thins when the family is read as "CLAUDE.md routes to AGENTS.md." The split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:18] collapses this into the single row "shared doctrine / wrapper carry," which reads more like a routing synonym than like a translation statement. A cleaner separation would keep "wrapper routing" and "wrapper-translated doctrine" as two rows, so future doctrine movement in AGENTS.md can be tracked against the Claude-side translations that should move with it rather than drift silently.
- [d:r:i] **Continuation-name overlap (family 2) distinct from consumer-edge asymmetry (family 3)**. The reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:24, 34] separates these: both runtimes carry `progress` and `resume-project` at the workflow-name layer, but the Codex side has absorbed the uplift-anchor consumer chain (`$project_uplift -> progress/resume-project`, posture visibility at propagation-audit/33) while the Claude side does not. Direct comparison confirms the asymmetry: [.codex/get-shit-done/workflows/progress.md:158-189] loads the uplift note and renders an "Uplift Posture" block when `UPLIFT_NOTE.show` is true; [.claude/get-shit-done/workflows/progress.md:91-136] has no equivalent section and no `project_uplift.py progress-note` call. The split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:20] carries only one line for this ("consumer-chain asymmetry"), which leaves the workflow-name overlap implicit. A cleaner separation would keep both.
- [d:r:i] **Intervention-family slice (family 5) distinct from wider uncharted Codex-only field (family 6)**. The reread names ten workflow routes in the wider field at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:22]: `spike`, `spike-wrap-up`, `sketch`, `sketch-wrap-up`, `spec-phase`, `ultraplan-phase`, `ai-integration-phase`, `ingest-docs`, `eval-review`, `extract_learnings`. Direct comparison of the two runtime workflow directories finds 13 Codex-only workflows (the three intervention-family routes plus the ten above), with no Claude-only workflows — the Claude workflow surface is a strict subset of the Codex workflow surface. The wider field is also wider than the reread named: [.codex/get-shit-done/references/] carries files not present under [.claude/get-shit-done/references/], most notably `mandatory-initial-read.md`, which the Codex continuation workflows load as required_reading [.codex/get-shit-done/workflows/progress.md:6-7, .codex/get-shit-done/workflows/resume-project.md:14]. The Claude continuation workflows point at `continuation-format.md` instead [.claude/get-shit-done/workflows/resume-project.md:13-15]. Without a dedicated field map, later translation triage would answer to a partial view.
- [d:r:i] **Compatibility-anchor posture (family 7) distinct from widening-shape sub-decision (family 10)**. The current anchor in [.planning/UPLIFT-MANIFEST.json:78-101] carries `compatibility_posture: observed_basis_only` with three held items (version-window beyond observed basis, cross-runtime matrix, upstream-template drift). That row owns posture. The widening-shape question — whether the later move should grow the anchor into dual-basis, add an annotation for `.claude`'s held version, or open a typed multi-runtime carrier outside the `.codex`-anchored uplift memory — is a different sub-decision. The split note keeps them separate at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:21, 36-44]; the current manifest does not.
- [d:r:i] **Consumer-chain asymmetry (family 3) relative to shape-choice (family 10)**. There is a not-yet-decided question that sits between these: whether consumer-chain asymmetry becomes its own carrier, or is folded into an annotation row inside the compatibility anchor, or becomes part of a narrower consumer-only translation candidate [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:87]. That decision is upstream of family 3's durable carrier, because family 10's shape choice determines which home is available.
- [d:r:i] **Route-translation pressure triage (family 8) as a carrier distinct from field 6 mapping**. The assist-pattern reference at [../../intervention-proposals/103-uplift-agent-assist-patterns.md:75-88] names `cross_runtime_comparison_packet` but does not yet carry a per-route translation triage grammar (per-route `.claude`-side consumer, per-route translation granularity, per-route ownership, per-route disposition home). The reread proposes that grammar at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:88-93]. The split note references family 8 only implicitly via "route-translation pressure" [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:24]. The triage grammar has no durable carrier.
- [d:r:i] **Propagation-review cross-runtime relation (family 9) as a held-later carrier**. [.codex/get-shit-done/workflows/propagation-review.md:1-4] is itself a Codex-only route. A later multi-family cross-runtime contract change would either route through this Codex-only workflow (creating an implicit cross-runtime dependency on a Codex-only review) or would need a distinct variant. The reread holds this at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:62]; the split note preserves the family at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:26] but without its own distinct article of held-later carrier.

## Carrier Map By Concern Family

Families listed in the order carried by the reread, with their carrier status and the gap to the next bounded move.

### Family 1 — Shared Doctrine / Wrapper Carry

- [e:c+i] Current carriers:
  - vendor-neutral canon: [AGENTS.md:1-187], [.planning/AGENTS.md] (via [.planning/CLAUDE.md:7-8])
  - Claude-side thin wrapper: [CLAUDE.md:3-42]
  - planning-scoped Claude wrapper: [.planning/CLAUDE.md:1-32]
  - uplift-memory fingerprints: [.planning/UPLIFT-REPORT.md:57-60], [.planning/UPLIFT-MANIFEST.json:123-167]
- [d:r:i] What carries:
  - canon doctrine is authored once in AGENTS.md; Claude work is routed back to AGENTS.md
  - the wrapper files also translate load-bearing doctrine (anti-threshold posture; deficit-pseudo-positive prohibition; static-positive prohibition; propagation-neighbor obligation; `do not mirror` boundary)
  - the four doctrine-sensitive carriers are fingerprinted in uplift memory and would surface any drift under `$gsd-uplift-project`
- [d:r:i] What thins:
  - "translated doctrine" is carried ambient inside CLAUDE.md and .planning/CLAUDE.md; there is no inventory listing which AGENTS.md clauses have been translated into the wrappers and which have not
  - any future move that edits AGENTS.md without updating the wrappers would not be caught by fingerprint alone (fingerprint catches the wrapper edit, not the AGENTS.md-to-wrapper diff)
- [d:r:i] Missing carrier:
  - a terse translated-doctrine-inventory carrier, as a sub-family inside the shared-doctrine family, would make that translation layer durable rather than ambient

### Family 2 — Continuation-Floor Overlap At Workflow-Name Level

- [e:c+i] Current carriers:
  - `.codex`: [.codex/get-shit-done/workflows/progress.md], [.codex/get-shit-done/workflows/resume-project.md]
  - `.claude`: [.claude/get-shit-done/workflows/progress.md], [.claude/get-shit-done/workflows/resume-project.md]
- [d:r:i] What carries:
  - both runtimes expose the same two continuation workflow names
  - both are operator-facing entry surfaces
- [d:r:i] What thins:
  - the overlap is name-level; the consumer behavior is not overlap (see family 3)
- [d:r:i] Missing carrier:
  - none for this family; the question is whether this family stays distinct from family 3 in the durable split

### Family 3 — Consumer-Chain Asymmetry At Continuation Edge

- [e:c+i] Current carriers:
  - Codex side carries the uplift consumer chain: [.codex/get-shit-done/workflows/progress.md:158-189], [.codex/get-shit-done/workflows/resume-project.md:148-209]
  - Claude side does not: [.claude/get-shit-done/workflows/progress.md:91-136], [.claude/get-shit-done/workflows/resume-project.md:114-153]
  - typed v2 registry row on posture visibility: propagation-audit/33-seed-operator-consumer-widening-change-triggered-refresh.md
- [d:r:i] What carries:
  - the Codex-side `$project_uplift -> progress/resume-project` chain is live and has one typed-registry refresh row
- [d:r:i] What thins:
  - the asymmetry is named in the reread and split note but has no durable inventory inside compatibility or propagation memory that says "the Claude continuation edge does not carry the uplift consumer chain"
  - a Claude operator running `/gsd-progress` or `/gsd-resume-work` will get a materially different re-entry report than a Codex operator running `$gsd-progress` or `$gsd-resume-work`, and that asymmetry is visible at the workflow surface but ambient everywhere else
- [d:r:i] Missing carrier:
  - either a consumer-chain row inside the compatibility anchor (if the family-10 widening shape chooses that home) or a distinct consumer-chain-asymmetry audit surface
- [o:r:i] The decision of which home this family should live in is downstream of family 10's widening-shape choice.

### Family 4 — Version-Alignment / Observed-Basis Anchor

- [e:c+i] Current carriers:
  - compatibility_basis in [.planning/UPLIFT-MANIFEST.json:78-101]
  - compatibility section in [.planning/UPLIFT-REPORT.md:23-43]
  - `.codex/get-shit-done/VERSION` at `1.38.3`
  - `.claude/get-shit-done/VERSION` at `1.34.2` (not inside the manifest's `observed_runtime_version_set`)
- [d:r:i] What carries:
  - the anchor records `observed_runtime_version_set: ["1.38.3"]` and names three held-later items explicitly
  - `project_uplift.py detect` refreshes the anchor on each run
- [d:r:i] What thins:
  - the anchor silently treats "observed" as `.codex` and does not record `.claude`'s version, even as a held entry; an operator reading the manifest sees only `1.38.3` and must read prose to learn that `.claude` is at `1.34.2`
  - the four-minor-version gap between runtimes is real and load-bearing (the newer Codex required_reading routes, the layered packet structure, and the uplift consumer chain all sit on the `.codex` side of that gap), yet the anchor carries no representation of it
- [d:r:i] Missing carrier:
  - this gap is the direct surface that family 10 would decide on; see family 10

### Family 5 — Route-Asymmetry Family (Intervention-Family Slice)

- [e:c+i] Current carriers:
  - [.codex/get-shit-done/workflows/uplift-project.md]
  - [.codex/get-shit-done/workflows/propagation-review.md]
  - [.codex/get-shit-done/workflows/seed-migration-inventory.md]
  - `.claude` has no counterparts
- [d:r:i] What carries:
  - the three Codex-only routes are the audit's intervention output; each has its own proposal/implementation chain and its own typed-v2 registry row history
- [d:r:i] What thins:
  - the intervention-family slice sits as three routes; there is no durable triage grammar for "which of these deserves a `.claude` counterpart, at what granularity"
- [d:r:i] Missing carrier:
  - a triage grammar (family 8) that answers to the intervention-family slice first

### Family 6 — Route-Asymmetry Family (Wider Uncharted Field)

- [e:c+i] Current carriers:
  - the Codex-only workflow set includes at least: `ai-integration-phase`, `eval-review`, `extract_learnings`, `ingest-docs`, `sketch`, `sketch-wrap-up`, `spec-phase`, `spike`, `spike-wrap-up`, `ultraplan-phase`
  - the Codex-only references set includes at least: `mandatory-initial-read.md`, `ai-evals.md`, `ai-frameworks.md`, `autonomous-smart-discuss.md`, `debugger-philosophy.md`, `doc-conflict-engine.md`, `executor-examples.md`, `ios-scaffold.md`, `planner-antipatterns.md`, `planner-source-audit.md`, `project-skills-discovery.md`, `sketch-interactivity.md`, `sketch-theme-system.md`, `sketch-tooling.md`, `sketch-variant-patterns.md`
  - the Claude workflow surface is a strict subset of the Codex workflow surface
  - the Claude references surface is a strict subset of the Codex references surface
- [d:r:i] What carries:
  - the reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:22] names the ten workflows
  - the first exercise packet at [../packets/12-uplift-cross-runtime-comparison-first-exercise-packet.md:55-57] names the route-asymmetry cluster but scopes only the intervention-family three
- [d:r:i] What thins:
  - no durable field map enumerates the wider Codex-only set
  - no durable field map enumerates the Codex-only references set (`mandatory-initial-read.md` is load-bearing because it gates the layered `required/supporting/deeper` packet pattern that later Codex routes inherit)
- [d:r:i] Missing carrier:
  - a full-field mapping audit surface that enumerates workflow-level and reference-level Codex-only carriers, tagged by whether each has a plausible `.claude`-side consumer

### Family 7 — Compatibility-Anchor Posture

- [e:c+i] Current carriers:
  - `compatibility_posture: observed_basis_only` at [.planning/UPLIFT-MANIFEST.json:79]
  - `held_later` array at [.planning/UPLIFT-MANIFEST.json:96-100]
  - check protocol at [.planning/UPLIFT-MANIFEST.json:90-95]
  - mirror in [.planning/UPLIFT-REPORT.md:23-43]
- [d:r:i] What carries:
  - posture is named explicitly and has an ingress (check protocol) and three held-later rows
- [d:r:i] What thins:
  - posture is orthogonal to shape; the anchor could remain `observed_basis_only` while shape moves through multiple candidates (annotation, dual-basis, typed carrier)
- [d:r:i] Missing carrier:
  - see family 10; shape is the next decision inside this anchor

### Family 8 — Route-Translation Pressure Triage

- [e:c+i] Current carriers:
  - `cross_runtime_comparison_packet` as a bounded pattern: [../../intervention-proposals/103-uplift-agent-assist-patterns.md:75-88]
  - one exercised round trip: [../packets/12-*], [../outputs/10-*], [../dispositions/10-*]
  - no per-route triage grammar yet
- [d:r:i] What carries:
  - the pattern exists; one comparison packet is exercised
- [d:r:i] What thins:
  - there is no durable triage grammar that names, per Codex-only route, the `.claude`-side consumer (if any), the translation granularity (full-workflow mirror, wrapper-plus-packet-guidance, consumer-only, narrower counterpart, explicit hold), the ownership, and the disposition home
  - without that grammar, per-route decisions would be made ad hoc and translation appetite would risk drifting into parity
- [d:r:i] Missing carrier:
  - a per-route triage proposal, downstream of family 6 mapping

### Family 9 — Propagation-Review Cross-Runtime Relation

- [e:c+i] Current carriers:
  - [.codex/get-shit-done/workflows/propagation-review.md] is the Codex-only review route
  - held-later line at [.planning/UPLIFT-MANIFEST.json:33-36]
  - held-later articulation at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:62] and [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:94]
- [d:r:i] What carries:
  - the route exists on the Codex side; the cross-runtime posture is held
- [d:r:i] What thins:
  - no carrier names under what condition `$gsd-propagation-review` should open a cross-runtime variant
  - no carrier names whether the variant should be a new route or a mode added to the existing one
- [d:r:i] Missing carrier:
  - deliberately held; see `Hold For Later` below

### Family 10 — Compatibility-Family Widening Shape

- [e:c+i] Current carriers:
  - candidate shapes enumerated in the reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:81-85]:
    - dual-basis posture: `observed_basis_.codex_plus_explicitly_held_.claude`
    - annotation posture: keep `observed_basis_only` and add a named held-`.claude`-version entry
    - typed-carrier posture: new multi-runtime compatibility carrier outside `.codex`-anchored uplift memory
  - candidate shapes listed more compactly in the split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:40-43]
- [d:r:i] What carries:
  - three candidate shapes are enumerated before the shape decision itself opens
  - the decision surface is concrete (uplift memory) and bounded (one proposal, no runtime mutation)
- [d:r:i] What thins:
  - no bounded proposal yet picks among the three shapes
  - the shape choice governs where family 3 (consumer-chain asymmetry) can live, which means family 3's carrier home is gated on family 10
- [d:r:i] Missing carrier:
  - one bounded sub-proposal in [../../intervention-proposals/] that picks a shape

## Which Near-Term Sub-Family Should Earn The Next Bounded Proposal

- [d:r:i] Recommended first move: **compatibility-family widening shape (family 10)**.
- [d:r:i] Reasoning without flattening the other two into irrelevance:

### Why family 10 should move first

- [d:r:i] The shape decision is already narrowed to three candidate shapes in the reread at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:81-85]. The next lane is a decision surface, not a discovery surface, so the lead time from proposal opening to first decision is short.
- [d:r:i] Family 10's articulation home is the most durable carrier in the cross-runtime picture: [.planning/UPLIFT-MANIFEST.json:78-101] is the compatibility anchor that every `$gsd-uplift-project detect` run refreshes, and that every subsequent cross-runtime lane answers to. A shape decision moves that durable carrier; a shape deferral leaves it ambiguous while later moves risk silently reshaping it.
- [d:r:i] Family 10's decision gates family 3's carrier home. If family 10 picks the annotation posture (keep `observed_basis_only`; add a named held-`.claude`-version row), consumer-chain asymmetry can be annotated at the same row; if family 10 picks dual-basis, the anchor itself widens and family 3 becomes a sub-row inside the new shape; if family 10 picks the typed-carrier posture, family 3 (and family 4's gap, and any future matrix work) all move to a new carrier outside uplift memory. All three futures are coherent, and all three put family 3's home in a different place. Deciding family 10 first prevents family 3 from being prematurely carried in one home that later has to move.
- [d:r:i] Family 10's lane stays cleanly inside the `Hold For Later` boundary: it does not open any live `.claude` mutation, any compatibility-matrix claim, any cross-runtime composition judgment, or any parity framing. It moves the anchor's shape only, which is why [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:63] names this sub-family explicitly as "a bounded sub-proposal should open between observed-basis-only and a typed multi-runtime carrier."
- [d:r:i] Family 10's carry is also the broadest across horizons: every later cross-runtime lane — family 6 mapping, family 8 triage, family 9 propagation-review variant — answers to the compatibility anchor's shape. Moving the shape first widens the future optionality across all three downstream families; moving it later forces later families to guess at their home.

### Why family 6 should still earn its own bounded lane, not collapse under family 10

- [d:r:i] Family 6 is a discovery surface, not a decision surface. The reread's explicit precedence rule [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:64] is "A full-field mapping lane should precede any translation move that reaches beyond the three intervention-family routes; otherwise later translation would silently absorb the wider asymmetry into a parity appetite it has not earned." That precedence is distinct from family 10's precedence over family 3.
- [d:r:i] Family 6's field is wider than the reread's own ten-workflow list once the references set is included. That widening is load-bearing because `mandatory-initial-read.md` gates the layered `required/supporting/deeper` packet pattern that the newer Codex workflows inherit and that the Claude workflows do not. A family-6 mapping lane that enumerates both workflow-level and reference-level Codex-only carriers, tagged by whether each has a plausible `.claude`-side consumer, is the right terrain-disclosure move.
- [d:r:i] Family 6 does not need family 10 to land first. The field map is read-only. The two can proceed in sequence (family 10 first, family 6 second) or in parallel, because they touch different surfaces.
- [d:r:i] Skipping family 6 and jumping to family 8 (route-translation triage) would silently collapse the wider field into the intervention-family slice. That collapse is exactly the parity-appetite drift the split note warns against.

### Why family 3 should not yet earn its own bounded proposal

- [d:r:i] Family 3's carrier home is gated on family 10's shape choice, per the reasoning above. A family-3 proposal opened before family 10 would either have to carry its own ad hoc home (which risks being re-homed once family 10 lands) or would have to implicitly commit to a shape choice without naming it.
- [d:r:i] Family 3 is also where the sharpest immediate translation pressure is felt (the Claude continuation edge does not carry the uplift consumer chain), which makes it the family most at risk of sliding into a thin translation slice if opened prematurely. Keeping it downstream of family 10 preserves the `family-by-family` posture instead of letting the most pressured sub-family pull the lane toward translation.
- [d:r:i] Family 3 earns its own bounded proposal after family 10 — at which point the proposal can name its carrier home directly and can decide whether the scope is consumer-only translation, anchor annotation, or a dedicated sub-family carrier.

### Summary sequencing

- [d:r:i] Proposed family-by-family order:
  1. family 10 — compatibility-family widening shape (bounded sub-proposal)
  2. family 6 — wider route-asymmetry field mapping (can open in parallel with family 10 since surfaces do not collide; otherwise second)
  3. family 3 — consumer-chain asymmetry scoping, after family 10 lands its shape
  4. family 8 — route-translation pressure triage, after family 6 lands its field map
  5. family 9 — propagation-review cross-runtime relation remains held until a concrete multi-family cross-runtime contract change arrives
- [d:r:i] The sequencing preserves family-by-family movement and does not allow any move to silently collapse into parity framing.

## What Should Remain Explicitly Held

- [d:r:i] Any live `.claude` route translation, per [../dispositions/11-uplift-cross-runtime-comparison-first-exercise-reread-inheritance.md:51] and the split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:69].
- [d:r:i] Any durable multi-runtime compatibility matrix, per [.planning/UPLIFT-MANIFEST.json:96-100] and [../dispositions/11-uplift-cross-runtime-comparison-first-exercise-reread-inheritance.md:52].
- [d:r:i] Any cross-runtime composition judgment, per [../dispositions/11-uplift-cross-runtime-comparison-first-exercise-reread-inheritance.md:53] and [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:71].
- [d:r:i] Any move that folds compatibility-family widening into route translation, or route translation into compatibility-family widening, before each sub-family has its own bounded carrier, per [../dispositions/11-uplift-cross-runtime-comparison-first-exercise-reread-inheritance.md:54].
- [d:r:i] Any cross-runtime posture change for `$gsd-propagation-review` without its own explicit carrier, per [../dispositions/11-uplift-cross-runtime-comparison-first-exercise-reread-inheritance.md:55]. A later cross-runtime variant should open from [.codex/get-shit-done/workflows/propagation-review.md] when a concrete multi-family cross-runtime contract change arrives, not from inside an uplift packet family.
- [d:r:i] Any whole-harness parity push across `.codex` and `.claude` as an organizing frame, per [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:72] and the family-by-family clause in [../outputs/10-uplift-cross-runtime-comparison-first-exercise.md:55].
- [d:r:i] Any automatic agent spawn from the uplift route, per [../../intervention-proposals/103-uplift-agent-assist-patterns.md:130] and [../../intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md:77].
- [d:r:i] Upstream-template drift machinery, per [.planning/UPLIFT-MANIFEST.json:39-41].
- [d:r:i] Whether a cross-runtime comparison packet can itself upgrade the compatibility posture. This containment question should stay explicit and held until a later lane decides whether bounded comparisons tighten the anchor or annotate it.
- [d:r:i] Any durable uplift-memory refresh triggered by this review itself. The review is a parent-thread Opus widening lane and should not pull a write into [.planning/UPLIFT-REPORT.md] or [.planning/UPLIFT-MANIFEST.json] until a later slice earns that movement.
- [d:r:i] Any live mutation of [CLAUDE.md] or [.planning/CLAUDE.md] derived from this review. The translated-doctrine sub-family inside family 1 earns its own bounded proposal only when the next doctrine movement in AGENTS.md touches cross-runtime carry, per [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:95].

## How This State Should Be Inherited

### Carry Forward

- [d:r:i] Keep the split note at [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md] as the durable eight-row carrier for the cross-runtime concern families at parent-thread level.
- [d:r:i] Keep the ten-row reread map at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:31-41] as the sharper companion artifact when a later lane needs the family-2/family-3 and family-5/family-6 splits explicitly rather than compressed.
- [d:r:i] Keep the Opus-led posture for this sub-family, per [intervention-proposals/113-uplift-cross-runtime-concern-family-split-next-move.md:65] and [../../intervention-proposals/103-uplift-agent-assist-patterns.md:75, 119-125].
- [d:r:i] Keep the parent-thread write boundary intact: no live runtime mutation, no `.claude` translation, no compatibility-matrix claim, no composition judgment, no parity push.
- [d:r:i] Keep the family-by-family posture: later translation, if earned, moves per family rather than under one parity frame.
- [d:r:i] Keep the three-layer first cut (shared doctrine / continuation-floor overlap / route asymmetry) from the first exercise as a first-cut frame, now ready for further sub-family splitting per this review's carrier map.
- [d:r:i] Keep the compatibility-anchor containment: `observed_basis_only` certifies `.codex` only, with three held-later compatibility items intact, until a family-10 sub-proposal earns a durable shape change.
- [d:r:i] Keep the assist-pattern discipline: `cross_runtime_comparison_packet` is the third exercised pattern of the four at [../../intervention-proposals/103-uplift-agent-assist-patterns.md], and the parent-thread disposition grammar (`accept`/`revise`/`park`/`reject`) continues to apply to later lanes in this family.

### New Proposal Opening

- [d:r:i] **Family-10 compatibility-family widening shape sub-proposal** as the next bounded proposal. Bounded shape:
  - articulation home: [../../intervention-proposals/] as a proposal-only carrier
  - decision surface: pick one of three candidate shapes (annotation posture, dual-basis posture, typed-carrier posture) from [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:81-85] or name a refinement
  - write boundary: proposal text only; no live `.planning/UPLIFT-MANIFEST.json` edit
  - disposition home: [../dispositions/] with the existing `accept`/`revise`/`park`/`reject` grammar
  - posture: operator-initiated, parent-thread-owned, packet-first discipline
  - delegation: parent-thread packet work is sufficient for this narrow decision; an external Opus lane is only needed if the three candidate shapes prove insufficient and field-mapping is required
- [d:r:i] **Family-6 wider route-asymmetry field mapping** as a distinct lane, opening in parallel or immediately after family 10. Bounded shape:
  - articulation home: an audit surface under this workspace
  - read boundary: enumerate Codex-only workflow and reference carriers; tag each by whether a plausible `.claude`-side consumer exists
  - write boundary: field-map artifact only; no translation work, no triage, no `.claude` mutation
  - posture: Opus-led if the mapping is still widening; parent-thread-led if the question has already narrowed to a finite enumeration
- [d:r:i] **Family-3 consumer-chain asymmetry scoping** as a bounded proposal after family 10 lands. Bounded shape:
  - articulation home: depends on family 10's shape choice (inside the anchor if annotation/dual-basis; a separate carrier if typed-carrier)
  - decision surface: whether consumer-chain asymmetry is carried as its own sub-family, annotated as a row inside the compatibility anchor, or folded into a narrower consumer-only translation candidate
  - write boundary: proposal-only
- [d:r:i] **Family-8 route-translation pressure triage grammar** as a later proposal once family 6 mapping lands. The triage grammar at [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:88-93] already names the fields; the proposal would codify them against the intervention-family three first, with the wider field handled per family 6 mapping.

### Hold For Later

- [d:r:i] All items listed in `What Should Remain Explicitly Held` above.
- [d:r:i] Any combined move that crosses compatibility-family widening and route translation before each has its own bounded proposal.
- [d:r:i] Any change to `$gsd-propagation-review` that would assume cross-runtime ownership without its own explicit proposal carrier.
- [d:r:i] Any translation move that reaches outside the intervention-family three before family-6 mapping lands.
- [d:r:i] Any automated or helper-driven composition routing between `.codex` and `.claude`. Composition remains parent-thread-owned.
- [d:r:i] Any move that treats translated Claude-side doctrine as its own first-class family before the next AGENTS.md doctrine movement that touches cross-runtime carry.

### Next Bounded Move

- [d:r:i] Open one bounded family-10 sub-proposal in [../../intervention-proposals/] that:
  - names the three candidate shapes (annotation, dual-basis, typed-carrier) verbatim from [../outputs/11-uplift-cross-runtime-comparison-first-exercise-reread-opus47-max-r1.md:81-85]
  - records which shape the parent thread picks and why
  - states what that shape does not yet authorize (no live anchor edit until a later implementation slice; no compatibility-matrix claim; no cross-runtime composition judgment)
  - names family 3 as the next sub-family that becomes unblocked by the shape choice
  - names family 6 as a distinct lane that may open in parallel
  - keeps the disposition at [../dispositions/] with the `accept`/`revise`/`park`/`reject` grammar
- [d:r:i] Keep the write boundary of the family-10 sub-proposal to proposal text only. A later implementation slice (if the proposal lands `accept`) would earn its own carrier: a durable edit to [.planning/UPLIFT-MANIFEST.json] and [.planning/UPLIFT-REPORT.md] under `$gsd-uplift-project --write`.
- [d:r:i] Keep the family-6 field mapping lane ready to open but do not let its absence block the family-10 sub-proposal. Shape choice is not gated on field completeness; the inverse is also true.
- [d:r:i] If a later lane earns a narrower live implementation move, open it from whichever sub-family proposal lands first (family 10 shape, family 6 field map, then family 3 scoping), family by family, rather than as one widening parity push across the runtime boundary.
