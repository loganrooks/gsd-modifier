# Inject Migration Comparative Uplift Borrowing Proposal

Date: 2026-05-16
Status: proposal-only
Scope: content comparison between local `inject-migration` and F1 Modeling Lab's local GSD uplift proposal

## Executive Summary

Recommended stance: **borrow the F1 proposal's consumer-chain discipline and proposal-layer clarity, adapt the optional `project_doctrine` lane into a generic future overlay capability, defer design-intake and workflow-doctrine features until after the Phase 3 inject pilot, and reject all F1-specific doctrine as local truth for `gsd-modifier`.**

The F1 initiative proposes a planning-doctrine uplift for a local GSD install: optional doctrine file discovery, CONTEXT/RESEARCH/PATTERNS/PLAN/SUMMARY/VERIFICATION propagation, plan-check gates, new-project/add-phase scaffolding, reference/docs/tests, and an optional Claude Design intake lane. Its substantive lesson is not the particular doctrine (`VISION.md`, `LONG-ARC.md`, Formula 1 UI concerns), but the insistence that any new artifact lane must name every producer, consumer, verifier, test, docs surface, and default-off/default-on boundary.

The local `inject-migration` initiative already has a strong mechanism layer: schema v4, `mode: inject`, seven operation kinds, marker idempotency, apply/verify semantics, `parity_intent`, phased carrier waves, and reviewer/operator gates. What it lacks is a single proposal-layer rollup that makes the mechanism, maintenance goal, bounded-overwrite doctrine, runtime-parity obligation, and upstream-compatibility story visible in one place for future adoption decisions. ADR-001 plus phase plans are enough for execution, but not enough as an operator-facing adoption proposal.

This proposal therefore recommends adding a future, proposal-only artifact after Phase 3 pilot evidence exists: an inject uplift adoption proposal that borrows F1's contract graph and upstream-compatible split, while staying inside `gsd-modifier`'s overlay/materialization domain.

## Scope And Non-Goals

This is a content review only. It does not implement borrowed items, edit manifests, edit contract code, edit overlay files, edit bootstrap scripts, or change governance docs outside this directory.

Non-goals:

- Do not import F1 product doctrine, Formula 1 vocabulary, design-system policy, or Claude Design assumptions into `gsd-modifier`.
- Do not re-open Phase 2 contract code or Phase 3 pilot scope.
- Do not add new `mode: inject` operation kinds based on F1; F1 is about planning-doctrine propagation, not overlay materialization operations.
- Do not treat a nicer document shape as evidence. The comparison below evaluates proposed content and contract implications.

## Source Grounding

Local governing surfaces read:

- `AGENTS.md` establishes this repo as the standalone modifier project and warns not to import host-product planning horizons; it identifies shipped/runtime-facing surfaces and the live control surfaces. See `AGENTS.md:3-31`.
- `AGENTS.md` requires propose-evidence-approve discipline for ambiguous, architectural, policy-bearing, or contract-carrying changes, and names overlay, contract, bootstrap, governance, plan-disposition, and inject-mechanism change classes. See `AGENTS.md:47-86`.
- `AGENTS.md` requires contract propagation, auditability, and explicit source/materialized distinctions. See `AGENTS.md:88-124`.
- `docs/handoff/current.md` identifies `inject-migration` as the active workstream and says Phase 2 is closed pending operator approval before Phase 3. See `docs/handoff/current.md:15-27` and `docs/handoff/current.md:106-119`.
- `.planning/CURRENT-STATE.md` and `.planning/STATUS.md` confirm `inject-migration` is active, Phase 2 is closed, and Phase 3 is not yet authorized. See `.planning/CURRENT-STATE.md:146-156` and `.planning/STATUS.md:157-162`.

Local inject-migration surfaces read:

- `INITIATIVE.md` mission, model, phase catalog, verification, out-of-scope list, and completion criteria. See `.planning/initiatives/inject-migration/INITIATIVE.md:7-23`, `.planning/initiatives/inject-migration/INITIATIVE.md:25-64`, `.planning/initiatives/inject-migration/INITIATIVE.md:66-86`, `.planning/initiatives/inject-migration/INITIATIVE.md:88-133`, `.planning/initiatives/inject-migration/INITIATIVE.md:135-156`.
- `STATE.md` current pause, Phase 2 status, counters, OOS items, and Phase 3 approval prerequisites. See `.planning/initiatives/inject-migration/STATE.md:5-17`, `.planning/initiatives/inject-migration/STATE.md:18-44`, `.planning/initiatives/inject-migration/STATE.md:68-83`, `.planning/initiatives/inject-migration/STATE.md:145-170`.
- ADR-001 schema v4, operation catalog, markers, parity intent, compatibility, apply/verify semantics, migration guidance, and boundaries. See `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md:24-43`, `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md:45-123`, `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md:125-190`, `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md:192-240`, `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md:242-267`, `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md:269-340`.
- Phase plans 03-08 define the pilot, reference wave, additive workflow wave, step-level wave, deferrable large-workflow wave, and template/agent triage. See `.planning/initiatives/inject-migration/phases/03-pilot.md:8-31`, `.planning/initiatives/inject-migration/phases/03-pilot.md:104-149`, `.planning/initiatives/inject-migration/phases/04-first-wave-references.md:8-35`, `.planning/initiatives/inject-migration/phases/05-second-wave-additive-workflows.md:8-30`, `.planning/initiatives/inject-migration/phases/06-third-wave-step-level.md:133-156`, `.planning/initiatives/inject-migration/phases/07-fourth-wave-large-workflows.md:8-39`, `.planning/initiatives/inject-migration/phases/08-templates-and-agents.md:130-151`.
- Readiness artifacts provide the initial overlay archetype, proposed schema, verification model, and posture triggers. See `.planning/readiness/intervention-strategies-2026-05-08.md:17-28`, `.planning/readiness/intervention-strategies-2026-05-08.md:500-626`, `.planning/readiness/intervention-strategies-2026-05-08.md:627-773`, `.planning/readiness/intervention-strategies-2026-05-08.md:789-870`, `.planning/readiness/release-readiness-orientation-2026-05-08.md:269-323`, `.planning/readiness/release-readiness-orientation-2026-05-08.md:327-430`.

F1 comparator surfaces read:

- `UPLIFT-PROPOSAL.md` names 11 changes and says the uplift is optional, upstream-compatible when file-presence/config-gated, and not GSDR-style machinery. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-PROPOSAL.md:10-18` and `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-PROPOSAL.md:20-30`.
- Its UPLIFT-01..11 records and contract graph were read. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-PROPOSAL.md:77-235` and `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-PROPOSAL.md:237-301`.
- Its upstream-compatible vs F1-specific split and out-of-scope section were read. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-PROPOSAL.md:303-349`.
- The paired review approves all 11 UPLIFTs with revisions A/B/C, requires user input on questions 8 and 9 before execution, and records a prior-review correction against stale reading. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-REVIEW-2026-05-16.md:20-40`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-REVIEW-2026-05-16.md:42-131`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-REVIEW-2026-05-16.md:133-156`.
- The prompt that produced the proposal emphasizes contract integrity: changing one side of a contract requires enumerating the other sides. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/codex-prompt-uplift-proposal.md:45-56` and `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/codex-prompt-uplift-proposal.md:176-235`.
- `codex-prompt.md` is a separate migration task that installs GSD locally before doctrine patches; its long-arc-aware patches are out of scope there. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/codex-prompt.md:13-22`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/codex-prompt.md:154-181`.
- `CLAUDE-DESIGN-GUIDE.md` frames Claude Design as visual exploration between framing and production, with design-system setup, dense briefs, cost-aware iteration, and reviewed handoff. See `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/CLAUDE-DESIGN-GUIDE.md:10-22`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/CLAUDE-DESIGN-GUIDE.md:65-92`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/CLAUDE-DESIGN-GUIDE.md:96-174`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/CLAUDE-DESIGN-GUIDE.md:226-253`, `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/CLAUDE-DESIGN-GUIDE.md:280-317`.

Stale or uncertain surfaces:

- The F1 proposal's citations are to a separate upstream clone and F1 repo state. This review did not independently re-run F1's upstream tests; it treats the F1 proposal and review as comparator artifacts, not as current upstream truth.
- The local `inject-migration` state file is current enough for this proposal: it records Phase 2 closure on 2026-05-16 and a pause before Phase 3. See `.planning/initiatives/inject-migration/STATE.md:5-17`.

## F1 Uplift Content Map

| ID | Substantive proposed modification |
|---|---|
| UPLIFT-01 | Add optional doctrine artifact discovery to SDK/init results: `vision_path`, `long_arc_path`, `tech_debt_path`, and `doctrine_expected` when files/config exist. See F1 proposal lines 79-90. |
| UPLIFT-02 | Extend CONTEXT generation with Future Awareness, Protected Seams, Explicit Non-Decisions, Current Posture, Future Shape Notes, and Vision Impact when doctrine exists. See lines 92-103. Review revision B adds a distinct Vision Alignment Checkpoint. See review lines 60-76. |
| UPLIFT-03 | Carry doctrine constraints into phase research as `Project Doctrine Constraints`, preserving current scope boundaries. See lines 105-116. |
| UPLIFT-04 | Teach pattern mapping to distinguish code analogs from doctrine-carrying seams. See lines 118-129. |
| UPLIFT-05 | Add optional PLAN frontmatter fields: `future_preservation`, `tech_debt_disposition`, and `doctrine_alignment`. See lines 131-145. |
| UPLIFT-06 | Add a plan-check doctrine translation gate that checks Future Awareness dispositions, tech-debt IDs, named contract completion, and applicability of doctrine fields. See lines 147-162. Review revision A adds an explicit UPLIFT-02 dependency. See review lines 44-58. |
| UPLIFT-07 | Preserve doctrine closeout in execution summaries via `Doctrine Preservation`. See lines 164-180. |
| UPLIFT-08 | Verify doctrine outcomes in verification reports against evidence classes rather than SUMMARY claims. See lines 181-190 and proposal lines 191-192. |
| UPLIFT-09 | Document optional doctrine scaffolding in new-project/add-phase without auto-importing future scope. See lines 194-205. |
| UPLIFT-10 | Add references, docs, and tests as the contract boundary, while excluding hooks and generic context profiles as doctrine enforcement surfaces. See lines 207-218. |
| UPLIFT-11 | Add optional Claude Design prototype intake using reviewed `DESIGN-SYSTEM`, `DESIGN-BRIEF`, and `DESIGN-HANDOFF` artifacts; raw design outputs are not executable authority. See lines 220-235. Review revision C adds source-of-truth, drift, and save-error details. See review lines 78-105. |

## Inject-Migration Content Map

| Local item | Substantive proposed modification |
|---|---|
| Migration mission | Move modifier overlays from whole-file post-conversion snapshots to operation-based injection against upstream anchors, reducing drift and silent staleness. See `INITIATIVE.md:7-23`. |
| `mode: inject` | Add a new manifest materializer mode for additive or anchor-targetable changes. Operations apply to upstream-installed files in place with idempotency markers. See `INITIATIVE.md:25-44` and ADR-001 lines 24-43. |
| Operation catalog | Adopt seven v4 operation kinds: `section_insert_after`, `section_replace`, `step_remove`, `step_insert_after`, `include_add`, `include_remove`, `block_replace`. See ADR-001 lines 45-123. |
| Marker/idempotency contract | Use `<!-- GSD_MODIFIER:start key:KEY -->` / `end key:KEY` markers with globally unique keys. Marker presence controls idempotent application. See ADR-001 lines 125-163. |
| `parity_intent` | Declare whether per-runtime operations should produce aligned visible outcomes or runtime-independent modifier content. See ADR-001 lines 164-190. |
| Backward compatibility | Keep schema v3 `overwrite`/`add` valid; schema v4 accepts mixed `overwrite`, `add`, and `inject` entries; bump schema version on first real inject entry. See ADR-001 lines 192-215. |
| Apply semantics | Read target content, apply all operations in memory, skip exact idempotent markers, fail on conflicts, and write atomically only after success. See ADR-001 lines 217-240. |
| Verify semantics | Default V1 verification checks marker presence and position, with content-hash V2 deferred. Per-slice smoke tests and Phase 3 pilot equivalence mitigate V1 weakness. See ADR-001 lines 242-267. |
| Carrier decision tree | Keep modifier-net-new content as `mode: add`, keep high-modifier-ownership or non-markdown/code carriers as `mode: overwrite`, and use `mode: inject` for stable anchor-targeted additions. See ADR-001 lines 269-315. |
| Carrier wave plan | Pilot one reference in Phase 3, migrate four more references in Phase 4, additive workflows in Phase 5, step-level workflows in Phase 6, optionally large workflows in Phase 7, and triage templates/agents in Phase 8. See `INITIATIVE.md:72-84` and phase plans cited above. |
| Operator/audit obligations | Reviewer-mediated gates, phase-boundary verification, atomic commits, state updates, checkpoints, and final retrospective. See `INITIATIVE.md:158-171`, `STATE.md:111-143`, and `AGENTS.md:101-151`. |

## Comparative Findings

1. **Both initiatives are contract-propagation initiatives, but at different layers.** F1 changes planning artifacts and agent/workflow/verifier consumers; inject-migration changes overlay materialization and manifest/contract/verifier consumers. The reusable F1 idea is the consumer chain, not the doctrine vocabulary. [inferred]

2. **F1 is explicit about upstream-compatible vs project-local split; inject-migration is explicit about out-of-scope but less explicit about future upstreamability.** F1 has a dedicated split between upstream-compatible optional behavior and F1-specific overlay/application. See F1 proposal lines 303-321. Inject-migration says upstreaming is out of scope and the mechanism is modifier-internal, though it could later be proposed upstream. See `INITIATIVE.md:135-145`. A local split artifact would help future reviewers. [inferred]

3. **F1's proposal artifact is stronger as an adoption decision surface.** ADR-001 is excellent for schema semantics and Phase 2 implementation; phase plans are excellent for execution. But no single local artifact currently maps mechanism, carrier waves, bounded overwrite, verification, operator risk, and upstream compatibility into one approval/park/revise proposal. [inferred]

4. **F1's `project_doctrine` chain reveals a general missing-consumer pattern, not a direct missing consumer.** For inject-migration, the analogous consumers are manifest validation, apply, marker extraction, materialized verification, canary/host proof, docs/closeout, and per-carrier design/debrief artifacts. Many are already present or planned; the gap is a first-class adoption proposal and post-pilot consumer map. [inferred]

5. **F1 review revisions map cleanly to local inject concerns.** Revision A's missing contract edge maps to inject's need to explicitly link ADR-001, Phase 2 contract code, Phase 3 design/debrief, verifier/canary, and closeout docs. Revision B's "separate related doctrines" maps to keeping mechanism, maintenance goal, bounded-overwrite doctrine, runtime parity, and upstreamability separate. Revision C maps only as a general "optional lanes need operational details"; its Claude Design specifics do not matter locally.

6. **Several F1 ideas must wait for Phase 3.** Anything that depends on real-materialized behavior, pilot equivalence, marker ergonomics, or whether V1 verification is acceptable should wait until Phase 3 produces the pilot design and debrief. The local state explicitly says Phase 3 has not started and is pending operator approval. See `STATE.md:32-36`.

## Borrowing Disposition Table

| F1 idea | Local relevance | Disposition | Translation needed | Target local surface if later approved | Verification need |
|---|---|---|---|---|---|
| UPLIFT-01 optional artifact discovery | Useful as a future overlay capability pattern, not current inject scope | `defer_until_after_inject_pilot` | Translate `project_doctrine` files into optional modifier/host-context metadata only if a later initiative needs host-local doctrine lanes | Future initiative, not current inject phases | Config/file-presence tests and no-op absent-file behavior |
| UPLIFT-02 CONTEXT future-awareness blocks | Shows how proposal lanes feed downstream consumers | `reference_only` | Use the consumer-chain idea, not CONTEXT doctrine blocks | Future proposal template | Proposal completeness review |
| UPLIFT-03 research doctrine constraints | Planning-layer only | `reference_only` | No direct injection equivalent | None | None |
| UPLIFT-04 doctrine-carrying seams | Strong analogy to protected overlay anchors and bounded overwrite decisions | `borrow_with_modification` | Translate "doctrine-carrying seams" to "anchor/consumer-carrying seams": upstream tags, process steps, include blocks, runtime converters, and materialized carriers | Post-Phase-3 inject adoption proposal and Phase 7/8 triage docs | Carrier design docs must distinguish copied content vs preserved anchor/consumer boundary |
| UPLIFT-05 PLAN doctrine fields | Useful shape for explicit dispositions | `borrow_with_modification` | Translate to `inject_disposition` records: migrated, kept overwrite, kept add, deferred, or separate initiative | Future proposal and Phase 10 retrospective | Verify every candidate carrier has a disposition or explicit exclusion |
| UPLIFT-06 plan-check gate | Useful as a contract-gate pattern | `borrow_with_modification` | Translate to source/materialized gate coverage: validate-manifest, apply, verify-materialized, canary, smoke tests, design/debrief artifacts | Phase 3+ debrief template or future proposal | Checklist mapping each operation kind and carrier wave to a gate |
| UPLIFT-07 SUMMARY doctrine preservation | Relevant to closeout/debrief evidence | `borrow_with_modification` | Translate to `Inject Preservation` debrief/retrospective: what upstream drift is now absorbed, what remains overwrite, what failures surfaced | Phase debriefs and Phase 10 retrospective | Debrief must cite actual materialized outputs and gates |
| UPLIFT-08 verification reports | Already strongly local via Phase 2 verify engine and phase gates | `borrow_with_modification` | Add a future proposal recommendation to make the verifier coverage map explicit after pilot evidence | Post-Phase-3 proposal | Confirm `verify_inject_state`, `verify-materialized`, and canary cover each claim |
| UPLIFT-09 optional scaffolding | Potential future overlay capability, but not current inject mechanism | `defer_until_after_inject_pilot` | Translate to optional host-project overlay capability only if modifier later supports project-local doctrine add-ons | Separate future initiative | No-op defaults and docs tests |
| UPLIFT-10 references/docs/tests boundary | Directly relevant | `borrow_with_modification` | Translate to inject reference/docs/tests boundary: ADR + contract docs + operation tests + carrier smoke tests + closeout docs | Post-Phase-3 proposal, Phase 10 docs | Test list must cover docs/reference drift, operation coverage, and default boundaries |
| UPLIFT-11 Claude Design intake | Not relevant to overlay materialization | `reject` | Reject as F1/product-design-specific; only retain the generic lesson that external artifact lanes need reviewed handoffs | None | None |
| Review revision A: missing contract edge | Directly relevant | `borrow_with_modification` | Require every local proposed uplift to name producer, consumer, verifier, tests, docs, and closeout carrier | Future proposal template | Prompt-to-artifact checklist |
| Review revision B: split related doctrines | Directly relevant | `borrow_as_is` | Use the exact discipline: do not collapse mechanism, maintenance goal, bounded-overwrite doctrine, runtime parity, upstreamability | This proposal and future proposal template | Cold-read for category collapse |
| Review revision C: optional operational details | Partly relevant | `reference_only` | Retain as reminder that optional lanes require ownership/drift/workaround details; ignore design-specific details | Future optional-lane proposals | Optional-lane checklist |

## Proposed Local Uplift Proposal For `gsd-modifier`

### IM-UPLIFT-01 — Add A Post-Pilot Inject Adoption Proposal

- **What is being uplifted:** Add a proposal-layer artifact after Phase 3, tentatively `.planning/initiatives/inject-migration/decisions/INJECT-ADOPTION-PROPOSAL.md`, that summarizes pilot evidence, mechanism status, carrier-wave plan, bounded-overwrite doctrine, upstream-compatible split, and approval choices.
- **Why it matters:** ADR-001 carries schema semantics; phase plans carry execution. Future maintainers need one adoption-decision artifact that explains whether to approve scaling, revise the mechanism, or park remaining waves. [inferred]
- **Scope effect:** Modifies future closeout/proposal layer, not current Phase 3 execution scope.
- **Later touched artifacts if approved:** Phase 3 debrief, Phase 4 entry decision, Phase 10 retrospective, possibly `INITIATIVE.md` cross-reference.
- **Verification if implemented:** Cold-read checklist: can a maintainer answer what was proven, what was not proven, which carriers are next, which stay overwrite, and which gates cover the claims?
- **Boundary:** No manifest, contract code, overlay, bootstrap, or governance edits.

### IM-UPLIFT-02 — Add A Contract Consumer Map For Inject

- **What is being uplifted:** Explicitly map inject producers and consumers: ADR-001, manifest entries, inject source files, `validate_inject_operations`, `apply_inject_operations`, `extract_inject_markers`, `verify_inject_state`, materialized runtime files, canary/host proof, debriefs, and closeout docs.
- **Why it matters:** F1's strongest lesson is that artifact lanes fail when producers exist without consumers. Inject has many consumers already, but the map is distributed across ADR, code, tests, and phase plans. [inferred]
- **Scope effect:** Future proposal/Phase 3 debrief addition.
- **Later touched artifacts if approved:** `PILOT-DEBRIEF-mandatory-initial-read.md`, future `INJECT-ADOPTION-PROPOSAL.md`, Phase 10 retrospective.
- **Verification if implemented:** Each consumer must have a concrete command, test, or artifact reference; no "docs mention it" as a proxy for consumption.
- **Boundary:** Does not add new consumers before the pilot proves existing ones.

### IM-UPLIFT-03 — Add An Upstream-Compatible Vs Modifier-Specific Split

- **What is being uplifted:** A split that distinguishes generic upstreamable concepts (`mode: inject`, operation sequences, idempotency markers, fail-loud anchor drift, optional content-hash V2) from modifier-specific choices (`GSD_MODIFIER` namespace, current carrier waves, runtime profile names, bootstrap/canary machinery).
- **Why it matters:** F1 made this split explicit; local inject says upstreaming is out of scope but does not yet give a reusable split for future upstream proposal decisions.
- **Scope effect:** Future proposal/closeout docs.
- **Later touched artifacts if approved:** Future proposal, Phase 10 retrospective, maybe a reference doc.
- **Verification if implemented:** Every IM-UPLIFT and every operation-kind claim classified as upstream-compatible, modifier-specific, or unknown/deferred.
- **Boundary:** Does not initiate upstreaming.

### IM-UPLIFT-04 — Add A Bounded-Overwrite Disposition Ledger

- **What is being uplifted:** A ledger of carriers that stay `mode: overwrite` with reasons: code file, high modifier ownership, unstable anchors, large-restructure economics, or deferral pending evidence.
- **Why it matters:** ADR-001's decision tree already says some carriers stay overwrite. Phase 6/7/8 plans also allow keep-overwrite decisions. A ledger prevents "not migrated" from reading as omission. See ADR-001 lines 269-315 and Phase 7 lines 96-108.
- **Scope effect:** Phase 7/8/10 planning and closeout; does not alter Phase 3.
- **Later touched artifacts if approved:** Phase 6/7/8 decision docs and Phase 10 retrospective.
- **Verification if implemented:** Every overwrite carrier has a reason, citation to its decision artifact, and revisit trigger if any.
- **Boundary:** Does not force migration for high-risk carriers.

### IM-UPLIFT-05 — Add A Pilot-Evidence Gate For Borrowed Optional Capabilities

- **What is being uplifted:** A rule that optional artifact lanes such as future `project_doctrine` overlays, host-local doctrine scaffolding, or design-intake analogs cannot enter inject scope until after Phase 3 pilot evidence.
- **Why it matters:** Current state is paused before Phase 3; anything depending on real materialization would be premature. See `STATE.md:32-36` and Phase 3 objectives at `phases/03-pilot.md:8-31`.
- **Scope effect:** Future initiative routing.
- **Later touched artifacts if approved:** Future proposal open questions and deferred-items list.
- **Verification if implemented:** Confirm Phase 3 debrief exists and recommends entering Phase 4 before promoting any optional lane.
- **Boundary:** Does not block the already planned Phase 3 pilot.

### IM-UPLIFT-06 — Add Source-Vs-Materialized Evidence Classes To Proposal Reviews

- **What is being uplifted:** Adopt a proposal-review table that separates source-level evidence, materialized-runtime evidence, and inferred claims.
- **Why it matters:** `AGENTS.md` already requires source/materialized distinctions; F1's verifier lesson reinforces not trusting summary claims alone. See `AGENTS.md:101-124` and F1 UPLIFT-08 lines 181-190.
- **Scope effect:** Future proposal and review artifacts.
- **Later touched artifacts if approved:** Phase 3 debrief, future adoption proposal, Phase 10 retrospective.
- **Verification if implemented:** Each claim must cite either source file, materialized output, command result, or be labeled `[inferred]`.
- **Boundary:** Does not require running state-mutating gates inside this proposal-only review.

## Required Analysis Questions

### Should `gsd-modifier` borrow F1's optional `project_doctrine` lane as an overlay capability?

Recommendation: **not now; defer until after the inject pilot and treat it as a separate future capability, not a comparator-only local patch.**

Reasoning: The generic mechanic, optional file/config discovery feeding a consumer chain, could eventually fit `gsd-modifier` as a host-project overlay capability. But `inject-migration` is currently about materialization mechanics, not project planning doctrine. Importing it before Phase 3 would collapse mechanism and host-project doctrine. That violates the local discipline against flattening accepted boundary vs ambient follow-up. See `AGENTS.md:64-68`.

### Should `inject-migration` add a first-class proposal artifact like F1's `UPLIFT-PROPOSAL`, or is ADR-001 plus phase plans enough?

Recommendation: **add a first-class proposal artifact after Phase 3.**

ADR-001 plus phase plans are enough for implementation. They are not enough for the adoption decision because they distribute the answer across schema, code slices, phase plans, and state. The new artifact should be content-oriented: what was proven by pilot, what should scale, what remains bounded overwrite, what stays modifier-specific, and what is deferred. It should not be created before Phase 3 evidence, because otherwise it would restate intent rather than evaluate proof.

### Does F1's `project_doctrine` chain reveal missing consumers in `inject-migration`?

Yes, in a limited sense. It does not reveal a missing code consumer for the Phase 2 mechanism: validation, apply, extraction, and verify engines already exist per `STATE.md:74-80`. It does reveal missing **narrative consumers**: a post-pilot proposal and final closeout should explicitly consume pilot evidence, phase debriefs, keep-overwrite decisions, and source/materialized gates. [inferred]

### Does `inject-migration` have an equally explicit upstream-compatible vs modifier-specific split?

Not yet as a standalone decision surface. It has out-of-scope rules and says upstreaming is a separate effort. See `INITIATIVE.md:135-145`. It also defines modifier-specific carriers and runtime profiles across the initiative. But it lacks F1's explicit split table. Add one post-pilot.

### Which F1 review revisions map to local inject concerns?

- Revision A maps to contract-edge completeness: every inject proposal should link ADR/design → manifest/source → apply → verify → debrief/closeout.
- Revision B maps directly: separate mechanism, maintenance goal, bounded-overwrite doctrine, runtime-parity obligation, and upstreamability.
- Revision C maps only as an optional-lane diligence pattern; Claude Design specifics are rejected as F1/product-design-specific.

### Which ideas must wait until Phase 3 pilot evidence exists?

Wait on IM-UPLIFT-01 through IM-UPLIFT-06 adoption, any `project_doctrine` overlay capability, any host-local scaffolding lane, and any change to verify semantics beyond ADR-001 V1/V2 discussion. Phase 3 is the first real-content proof of the mechanism. See `phases/03-pilot.md:8-31` and `phases/03-pilot.md:104-149`.

## Explicit Do Not Borrow

- Do not borrow F1's exact doctrine terms: Vision Impact, Vision Alignment Checkpoint, Honesty Surface, Accessibility and Thin-Client, Performance Budget, Migration Discipline, Phase-4 Contract Completion.
- Do not borrow Formula 1-specific artifacts, UI/product terms, `AccessibleChartContract`, `AnchorRegistry`, telemetry, regulation, puzzle/practice, or visualization-surface vocabulary.
- Do not borrow Claude Design as a local inject-migration lane; it belongs to product/design workflows, not overlay materialization.
- Do not borrow GSDR-style validators, signals, persistent knowledge base, or reflection machinery. The F1 prompt itself forbids reintroducing GSDR-style enforcement. See F1 prompt lines 254-265.
- Do not add hooks or generic context profiles as enforcement surfaces for inject. F1 explicitly excludes hooks/context profiles for doctrine enforcement; locally, Codex hook support is also not part of the active runtime capability. See F1 proposal lines 207-218 and local `AGENTS.md` runtime notes.
- Do not collapse keep-overwrite decisions into failure. Some overwrite carriers are correct by design.

## Open Questions For Operator

1. After Phase 3, do you want a distinct `INJECT-ADOPTION-PROPOSAL.md`, or should the Phase 3 debrief be expanded to carry the adoption proposal role?
2. Should the upstream-compatible vs modifier-specific split be written before Phase 4 entry, or deferred to Phase 10 closeout?
3. Should bounded-overwrite dispositions be centralized in one ledger, or remain per-phase with Phase 10 synthesizing them?
4. Is a future generic `project_doctrine` overlay capability desirable for host repos, or should `gsd-modifier` stay strictly focused on runtime/materialization mechanics for now?
5. Should Phase 3's debrief template be amended before the pilot starts to include the consumer map and source/materialized evidence classes, or should that wait for a post-pilot proposal slice?

## Suggested Next Action

**Approve with timing constraint:** accept the borrowing stance, but do not change Phase 3 before operator approval of Phase 2 and Phase 3 start. The concrete next action is to hold this proposal as a post-pilot input. After `PILOT-DEBRIEF-mandatory-initial-read.md` exists, decide whether to create `INJECT-ADOPTION-PROPOSAL.md` or amend the debrief template.

If rejected or parked, no current inject-migration work is blocked; this proposal is intentionally outside the active runtime write path.

