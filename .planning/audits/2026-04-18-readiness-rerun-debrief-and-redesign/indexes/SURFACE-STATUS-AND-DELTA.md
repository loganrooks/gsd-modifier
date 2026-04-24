Date: 2026-04-21
Status: active companion artifact

# Surface Status And Delta

## Purpose

- [g:r:i] This companion artifact keeps four different truth states visibly distinct so future harness intervention work does not flatten them into one misleading “the docs say” or “the harness is” statement.
- [d:r:i] The four states are:
  - frozen PR-doc governance/reference snapshot
  - current upstream/base runtime line
  - tracked repo-local overlay canon
  - live repo-local effective runtime

## Status Register

| Surface family | Frozen PR snapshot | Current upstream/base line | Tracked overlay canon | Live repo-local effective runtime | Current pressure |
| --- | --- | --- | --- | --- | --- |
| Stable docs/governance corpus | captured locally as `.md.txt` evidence | upstream docs inventory continues moving | not the same object | not runtime truth | preserve as governance/reference layer |
| Inventory/parity discipline | strongest explicit governance move in PR branch | still valuable against newer upstream surfaces | partly ported locally in audit/tooling practice | not yet fully hardened into harness-local guardrails | carry forward as governance pattern |
| `spec-phase`, `ingest-docs`, `mandatory-initial-read` | absent from frozen PR packet | shipped upstream surfaces | not part of overlay canon focus yet | present live locally | keep visible in planning/inheritance interventions |
| Install/materialization chain | not carried as runtime truth | begins at upstream install | overlay covers selected files | installer post-pass + live drift determine final state | intervene through chain, not one file |
| Agent runtime authority | flattened in docs layer | upstream provides base registry/contracts | overlay can patch some contracts | live `.codex/config.toml` + `.codex/agents/*.toml` decide spawn behavior | first-rank intervention target |
| Manifest/install coherence | not meaningfully addressed in frozen docs packet | base manifest exists | overlay does not solve trust by itself | stale-hash issue remains live tooling debt | bounded repair target |

## The Four States In Practice

### 1. Frozen PR Snapshot

- [e:c+i] The PR snapshot is a deliberately frozen local capture of the submitted docs branch, stored as `.md.txt` so it can serve as evidence without pretending to be a healthy live markdown subtree. Sources: [upstream-docs-pr-r2/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/README.md:1), [upstream-docs-pr-r2/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/README.md:5), [upstream-docs-pr-r2/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/README.md:9).
- [d:r:i] Its strongest value is governance/reference pressure, especially inventory/parity discipline, not current runtime truth.

### 2. Current Upstream/Base Line

- [e:c+i] Current upstream inventory already includes several shipped surfaces that matter for intervention planning and were not the center of the frozen PR packet: `spec-phase`, `plan-review-convergence`, `ultraplan-phase`, `spike`, `sketch`, `ingest-docs`, and `mandatory-initial-read`. Sources: [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:70), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:74), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:75), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:76), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:77), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:161), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:287).
- [d:r:i] So “the submitted docs PR” and “current upstream shipped surface set” are no longer interchangeable references.

### 3. Tracked Overlay Canon

- [e:c+i] The overlay remains the tracked repo-local intervention canon for the subset of files it ships into `.codex/`, but it is only one stage in the materialization chain. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:28), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:31).
- [d:r:i] So overlay truth is stronger than ad hoc live edits for persistence, but weaker than final live truth for current behavior unless you also account for later mutation/drift.

### 4. Live Repo-Local Effective Runtime

- [e:c+i] The live repo-local runtime is now at `1.38.3`, and the effective authority chain includes live `.codex/config.toml`, agent contracts, workflow/helper surfaces, and `.planning/config.json`. Sources: [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION:1), [.codex/gsd-file-manifest.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:2), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:40), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:46), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:57).
- [e:c+i] The live runtime also already shows a meaningful drift example: overlay+installer expectation says top-level reasoning defaults should be `high`, but the live `.codex/config.toml` says `xhigh`. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:35), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:41).

## Concrete Delta Notes

### PR Snapshot vs Current Upstream

- [e:c+i] The frozen PR snapshot contributes the stronger explicit inventory/parity posture, but current upstream carries a broader shipped surface roster. Sources: [upstream-docs-pr-r2/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/README.md:5), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:34), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:35).
- [d:r:i] Consequence: inherit the PR snapshot mainly as governance/reference pressure, while using current upstream inventory to keep newer shipped surfaces visible.

### Upstream/Base vs Live Runtime

- [e:c+i] The 2026-04-20 repo-local update probe established semantic alignment with a fresh `1.38.1` reinstall plus overlay, except for deliberate local config defaults and stale manifest hashes; the live runtime has since moved to `1.38.3`, so that earlier probe now serves as a historical comparison boundary rather than the current version claim. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:25), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:27), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:28), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:31), [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION:1).
- [d:r:i] Consequence: the live runtime should be read as a repo-local carried runtime, not simply as pristine upstream or as overlay canon.

### Overlay Canon vs Live Runtime

- [e:c+i] The overlay is the tracked persistence layer for covered files, but the live runtime can still outrun it through post-copy mutation and later local carry. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:30), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:35), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:41).
- [d:r:i] Consequence: any persistence-sensitive change should check both overlay and live runtime before claiming the intervention is fully carried.

### Manifest State vs Effective Truth

- [e:c+i] Manifest and backup metadata remain useful but non-sovereign. The manifest holds version evidence and recorded hashes, while the backup metadata only covers the replaced subset, and both can miss semantic truth about the final materialized state. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:67), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:68), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:69).
- [d:r:i] Consequence: manifest/install coherence stays a bounded tooling target rather than a settled trust surface.

## Use Rules

- [d:r:i] When citing docs-governance gains, cite the frozen PR snapshot or docs-audit outputs, not the live runtime.
- [d:r:i] When citing current shipped surface presence, cite current upstream inventory or live local runtime files, not the frozen PR snapshot.
- [d:r:i] When citing repo-local persistence/carry, cite overlay canon and installer composition together.
- [d:r:i] When citing actual current behavior, cite live `.codex/` and `.planning/config.json`.

## Bottom Line

- [g:r:i] The strongest discipline this note adds is simple: do not let different truth states borrow authority from each other. Stable docs, current upstream, tracked overlay, and live runtime each matter, but they matter differently, and future intervention planning should keep those differences explicit.
