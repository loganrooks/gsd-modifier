# Deferred Uplift Seeds

Date: 2026-05-16
Status: deferred-seed ledger
Scope: ideas surfaced by the comparative uplift review that should stay visible without changing the active Phase 3 pilot scope

## Purpose

This ledger preserves uplift ideas from the comparative review against the F1 local GSD uplift proposal.

The current inject-migration initiative is already in progress. Phase 2 is closed and Phase 3 is paused pending operator approval. These seeds do not authorize new runtime, manifest, contract, overlay, bootstrap, or governance changes. They are revisit triggers for later proposal, debrief, or closeout work.

## Current Implementation Stance

Do now:

- Keep these ideas visible in this initiative directory.
- Use them as prompts when writing the Phase 3 pilot debrief, if the evidence naturally supports them.
- Revisit them after the pilot produces materialized runtime evidence.

Do not do now:

- Do not widen Phase 3 beyond `references/mandatory-initial-read.md`.
- Do not edit `mode: inject` operation kinds, marker semantics, `parity_intent`, or schema v4 based on these seeds.
- Do not add optional host-project doctrine lanes before the pilot proves the inject mechanism on real materialized output.
- Do not import F1 product doctrine, Formula 1 vocabulary, or Claude Design-specific workflow into `gsd-modifier`.

## Seeds

### Seed 1: Post-Pilot Inject Adoption Proposal

- **Idea:** Create a post-pilot proposal, tentatively `INJECT-ADOPTION-PROPOSAL.md`, that decides whether to scale, revise, or park the inject migration after Phase 3 evidence exists.
- **Why preserve it:** ADR-001 documents mechanism semantics, and phase plans document execution. A separate adoption proposal would give future maintainers one decision surface for pilot proof, carrier waves, bounded overwrite, upstreamability, and verification confidence.
- **Revisit trigger:** Phase 3 pilot debrief exists.
- **Likely disposition:** Borrow with modification from the F1 proposal-layer pattern.
- **Boundary:** Do not create it before the pilot, unless the operator explicitly asks for a pre-pilot proposal artifact.

### Seed 2: Contract Consumer Map

- **Idea:** Add a map of inject producers and consumers: ADR, manifest entries, inject source files, validator, apply engine, marker extractor, verifier, materialized runtime files, canary or host proof, debriefs, and closeout docs.
- **Why preserve it:** The F1 proposal's strongest reusable move is naming the full consumer chain for any new artifact lane.
- **Revisit trigger:** Phase 3 debrief or post-pilot adoption proposal.
- **Likely disposition:** Borrow with modification.
- **Boundary:** Do not add new consumers before the pilot proves whether existing consumers are sufficient.

### Seed 3: Upstream-Compatible Vs Modifier-Specific Split

- **Idea:** Classify inject concepts into upstream-compatible, modifier-specific, and unknown or deferred.
- **Why preserve it:** The initiative currently says upstreaming is out of scope, but a split would help future reviewers see what could be proposed upstream later without turning this initiative into an upstreaming effort.
- **Revisit trigger:** Post-pilot proposal or Phase 10 retrospective.
- **Likely disposition:** Borrow with modification.
- **Boundary:** Does not initiate upstreaming and does not change the local schema.

### Seed 4: Bounded-Overwrite Disposition Ledger

- **Idea:** Track carriers that intentionally remain `mode: overwrite`, with reason, evidence, and revisit trigger.
- **Why preserve it:** Not migrating a carrier can be correct. A ledger prevents deliberate keep-overwrite decisions from looking like omissions.
- **Revisit trigger:** Phase 6, Phase 7, Phase 8, or Phase 10, when large or ambiguous carriers are evaluated.
- **Likely disposition:** Borrow with modification from F1's explicit disposition discipline.
- **Boundary:** Does not force migration of code files, high-modifier-ownership files, or unstable-anchor files.

### Seed 5: Source, Materialized, And Inferred Evidence Classes

- **Idea:** Require proposal and debrief claims to label whether they are grounded in source files, materialized runtime output, command results, or inference.
- **Why preserve it:** This matches local auditability rules and F1's lesson that verification should not rely on summary claims alone.
- **Revisit trigger:** Phase 3 pilot debrief.
- **Likely disposition:** Borrow with modification.
- **Boundary:** The evidence labels should improve debrief quality, not create a new gate that blocks the already-approved pilot slices.

### Seed 6: Optional Future Host-Local Doctrine Lane

- **Idea:** A future, separate capability could let host projects opt into local doctrine artifacts and carry them through planning workflows.
- **Why preserve it:** The F1 `project_doctrine` lane may be a useful generic pattern for host-project uplift, but it is not part of the inject mechanism.
- **Revisit trigger:** After inject migration closeout, or if a later host-project uplift initiative explicitly needs it.
- **Likely disposition:** Defer until after inject pilot or after inject closeout.
- **Boundary:** Not part of Phase 3, not part of schema v4, and not a reason to add F1 doctrine vocabulary to `gsd-modifier`.

### Seed 7: Explicit Do-Not-Borrow List

- **Idea:** Preserve the negative decisions so later work does not re-import them by accident.
- **Do not borrow:** F1 product doctrine, Formula 1 terms, Claude Design intake, design-system artifacts, hooks as enforcement surfaces, generic context profiles as enforcement surfaces, or GSDR-style signal and reflection machinery.
- **Why preserve it:** Deferred ideas can drift into accidental imports if the rejection rationale is not recorded near the active initiative.
- **Revisit trigger:** Any later proposal that references the F1 comparator initiative.
- **Likely disposition:** Reject or reference only.
- **Boundary:** These items are not local truth for this repo.

## When To Use This Ledger

Use this file as input when writing:

- the Phase 3 pilot debrief, if pilot evidence naturally bears on a seed;
- a post-pilot inject adoption proposal;
- Phase 7 or Phase 8 keep-overwrite decisions;
- the Phase 10 retrospective;
- any later, separate host-local doctrine uplift proposal.

## Current Recommendation

The only current implementation change is this ledger.

Do not modify Phase 3's migration scope now. If we want one additional change later, the safest next candidate is a small post-pilot proposal slice after `PILOT-DEBRIEF-mandatory-initial-read.md` exists.
