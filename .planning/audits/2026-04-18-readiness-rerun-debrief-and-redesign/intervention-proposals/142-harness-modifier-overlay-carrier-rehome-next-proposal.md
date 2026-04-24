Date: 2026-04-22
Status: active bounded proposal

# Harness Modifier Overlay Carrier Rehome Next Proposal

## Purpose

- [g:r:i] Open the next extraction object after the helper rehome plus portable compatibility declaration.
- [g:r:i] The goal is to separate the generic overlay/workflow/skill/reference tranche that a later standalone harness-modifier project would need to own, without yet splitting the repo or forcing a second-host exercise too early.

## Why This Next

- [d:r:i] The helper package plus compatibility declaration now give the later standalone project:
  - code-side contract helpers
  - probe/capture helpers
  - one portable compatibility carrier
- [d:r:i] But a later installable project still cannot stand on those alone.
- [d:r:i] The more meaningful operator-facing harness behavior still lives inside repo-local overlay carriers:
  - workflows
  - skills
  - references
  - templates
- [d:r:i] Until that tranche is separated more sharply, a standalone-project route would still blur:
  - generic harness behavior
  - host-product doctrine
  - wrapper-specific routing

## Candidate Carrier Set

- [d:r:i] likely generic overlay workflows:
  - `uplift-project.md`
  - `propagation-review.md`
  - `seed-migration-inventory.md`
  - generic read-control / re-entry / continuity widenings across:
    - `new-project.md`
    - `new-milestone.md`
    - `ingest-docs.md`
    - `resume-project.md`
    - `progress.md`
    - `health.md`
    - `update.md`
    - `from-gsd2`
- [d:r:i] likely generic matching skills:
  - `gsd-uplift-project`
  - `gsd-propagation-review`
  - `gsd-seed-migration-inventory`
  - `gsd-progress`
  - `gsd-resume-work`
  - `gsd-health`
  - `gsd-update`
  - `gsd-from-gsd2`
- [d:r:i] likely generic references/templates:
  - shared uplift continuity references
  - read-packet / relevance-control references
  - propagation review references
  - generic future-carry or strengthening references where they do not speak in host-product terms

## Explicit Boundary

- [d:r:i] Do not move host-product canon:
  - `.planning/PROJECT.md`
  - `.planning/ROADMAP.md`
  - `.planning/LONG-ARC.md`
  - readiness/rerun doctrine
- [d:r:i] Do not move repo-root or planning wrapper docs wholesale just because they mention the harness.
- [d:r:i] Do not treat compact-prompt content as generic only because the mechanism is generic.
- [d:r:i] Do not skip carrier-by-carrier classification in favor of a bulk “move the overlay” gesture.

## What This Proposal Should Settle

- [d:r:i] which overlay carriers are generic enough to travel
- [d:r:i] which still belong to shared-boundary territory
- [d:r:i] which should remain host-specific
- [d:r:i] whether the next extraction implementation slice should be:
  - a filesystem rehome inside `harness_modifier/overlay/`
  - or one more classification/mapping pass first

## Verification And Review Gates

- [d:r:i] explicit carrier roster, not umbrella language
- [d:r:i] propagation obligations named before any move
- [d:r:i] overlay manifest implications surfaced explicitly
- [d:r:i] no silent host-doctrine travel

## Held Later

- [d:r:i] second-host dry run
- [d:r:i] standalone repo split
- [d:r:i] npm/`npx` packaging
