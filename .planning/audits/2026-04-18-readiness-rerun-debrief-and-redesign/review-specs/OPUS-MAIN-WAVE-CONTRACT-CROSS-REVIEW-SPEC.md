# Opus Main-Wave Contract Cross-Review Spec

Status: drafted for launch, not yet launched  
Reviewer target: `Opus 4.7 Max` via Claude Code CLI `opus[1m]` `max`  
Output mode: single markdown artifact

## Purpose

- [g:r:i] This is a contract-level cross-review, not a free-floating meta lane.
- [g:r:i] This lane exists to pressure-test the drafted main-wave launch contract before Wave 1 specs/prompts are written.
- [g:r:i] It should also judge whether any pre-Wave-1 tightening is still warranted around workspace organization, artifact topology, or version-control / change-management practice.
- [g:r:i] The lane is challenge input, not sovereign doctrine.

## Review Target

- [g:c+i] Primary review target: the drafted [MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md](../main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md) and the current local decision that this is now the next object to critique. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-READINESS-DECISION.md:5-15, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/STATUS.md:25-32.
- [g:r:i] Secondary target: whether the surrounding workspace is organized, governed, and versioned well enough that Wave 1 spec-writing will not quietly inherit avoidable confusion.

## Core Questions

1. Is the drafted main-wave contract strong enough to support Wave 1 spec-writing, or is it still under-specified, over-packed, or quietly biased?
2. Are the wave split, lane family set, and packet discipline actually the right architecture for the next serious audit wave?
3. Is the contract still missing any critical pre-Wave-1 concern that should be handled before Wave 1 specs are written?
4. Is the workspace organization and artifact topology good enough for this next step, or is a bounded cleanup still warranted first?
5. Should version-control / change-management practice be tightened before Wave 1, and if so, how narrowly?
6. If the contract should still be revised before launch, which revisions are real blockers versus strong preferences versus later-facing cleanup?

## Required Posture

- [g:r:i] Do not reopen a generic `should there be a main wave at all?` meta question unless the contract itself clearly fails to justify one.
- [g:r:i] Do not praise the workspace for being organized unless that organization actually improves launch quality and inheritance discipline.
- [g:r:i] Do not treat `workspace organization can wait` as a default-safe answer; justify it if recommended.
- [g:r:i] Do not treat `use git better` as an empty gesture. If version-control / change-management changes are recommended, they must be concrete and bounded.
- [g:r:i] Do not widen into repo-wide GSD redesign, readiness-package mutation, or doctrine rewrite.
- [g:r:i] Keep the question contract-scoped: what should be tightened before Wave 1 specs, what can wait, and what should not be changed yet.

## Read-Set Sizing Note

- [s:r:i] Token estimates below are planning bands, not exact counts.
- [s:r:i] They are word-count approximations intended to remain useful even if the current Opus tokenizer runs hotter than older rough rules.
- [s:r:i] Read the ranges as:
  - `low` = lighter tokenization
  - `mid` = planning default
  - `high` = conservative / hotter tokenization
- [d:r:i] Current estimated mass:
  - Stage 0 contract packet: `~11.8k / 14.8k / 16.6k` tokens
  - Stage 1 governance/domain packet: `~16.1k / 20.1k / 22.6k` tokens
  - Stage 2 optional reserve: `~1.1k / 1.4k / 1.6k` tokens
  - total planned packet without reserve: `~27.9k / 34.9k / 39.2k` tokens
  - total planned packet with reserve: `~29.0k / 36.3k / 40.8k` tokens

## Read Set

### Stage 0: Contract Packet First

Read these first.

Estimated size: `~11.8k / 14.8k / 16.6k` tokens.

- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-READINESS-DECISION.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-CHARTER.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/QUESTION-SET.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/EVIDENCE-ARCHITECTURE.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/PLAN-PROPOSALS.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/STATUS.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md`

### Stage 1: Governance / Domain Packet Second

Read these next.

Estimated size: `~16.1k / 20.1k / 22.6k` tokens.

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/readiness/phase-01-rerun/PLAN.md`
- `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md`

### Stage 2: Optional Reserve

Only open these if the Stage 0 / Stage 1 packet leaves a real ambiguity about how the current local contract was inherited.

Estimated size: `~1.1k / 1.4k / 1.6k` tokens.

- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-local-proposal-and-stress-test-disposition.md`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-patched-surface-reread.md`

## Required Method

1. Review the contract on its own terms first.
2. Review whether the surrounding workspace is strong enough to carry Wave 1 spec-writing without silent drift.
3. Distinguish clearly between:
   - `block_before_wave1_spec`
   - `tighten_soon_but_not_blocking`
   - `later_cleanup`
   - `not_earned`
4. Treat workspace organization and version-control / change-management as real candidate concern surfaces, not as optional footnotes.
5. If you recommend no additional pre-Wave-1 tightening, explicitly justify why the current workspace topology and change-management practice are good enough.

## Specific Concern Surfaces To Test

### A. Contract Architecture

- wave split and dependency structure
- lane family adequacy
- packet discipline
- shared output registers
- risk of false convergence or packet drift

### B. Workspace Organization / Artifact Topology

- whether the current directory shape still makes governing vs challenge vs exploratory vs historical artifacts easy to distinguish
- whether any bounded topology cleanup is warranted before Wave 1 spec-writing
- whether read-order and authority notes are enough, or whether file clustering / naming / supersession practice still needs tightening

### C. Version-Control / Change-Management Practice

Test whether Wave 1 should add any bounded practice around:

- branch strategy
- checkpoint commit boundaries
- frozen packet manifests for launched lanes
- explicit prompt/spec revisioning
- supersession markers for replaced launch artifacts
- audit-trail retention that avoids silent overwrite

Do not recommend generic git hygiene. Recommend only what is concretely useful for this audit wave.

## Required Output

Produce a markdown artifact in this directory named:

- `../lane-reviews/lane-05-opus47-max-main-wave-contract-cross-review.md`

Required sections:

1. `Overall Judgment`
2. `Contract Strengths`
3. `Contract Weaknesses`
4. `Missing Pre-Wave-1 Concerns`
5. `Workspace Organization / Artifact Topology`
6. `Version-Control / Change-Management Practice`
7. `Blockers Versus Later-Facing Cleanup`
8. `Recommended Revisions Before Wave 1 Spec-Writing`
9. `Whether Contract Is Strong Enough To Launch Wave 1 Spec-Writing`

## If Recommending No Major Revision

That recommendation must explicitly justify:

- why the contract is specific enough to launch
- why no additional wave/lane is needed first
- why workspace organization is good enough for Wave 1 spec-writing
- why version-control / change-management can remain as-is for now without creating avoidable audit drift

## Launch Notes

- use `--dangerously-skip-permissions`
- use repo-local spec/prompt paths
- update [LAUNCH-LEDGER.md](../root-support/LAUNCH-LEDGER.md) after launch
- do not modify any file other than the required output artifact
