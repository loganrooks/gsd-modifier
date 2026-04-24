Date: 2026-04-22
Status: landed first delta slice

# Repo-Local Propagation Delta First Slice

## Role

- [g:r:i] This artifact is the first operator-facing repo-local propagation delta layer.
- [g:r:i] Its job is to answer:
  - what this repo adds, changes, widens, or reroutes beyond the upstream-pristine baseline
  - which current local families materially shape operator routing and propagation obligations
  - how local propagation mapping is actually being updated now
- [g:r:i] Read this beside [95-upstream-pristine-propagation-baseline-first-slice.md](95-upstream-pristine-propagation-baseline-first-slice.md), not instead of it.

## Delta Rule

- [d:r:i] A surface belongs in this delta when at least one of the following is true:
  - it does not exist in pristine upstream GSD
  - it materially changes the contract or routing of an upstream surface
  - it is a local governance or registry carrier required to keep the modified network readable and in tune
- [d:r:i] This first slice stays bounded to the current highest-traffic local families:
  - uplift composition
  - seed specialist route and operator-facing bridge
  - propagation registry/governance carry
  - lifecycle/read-packet widening where that now shapes operator routing

## Delta Families

### 1. Uplift Composition Layer

- [e:c+i] Repo-local adds a new composition-layer workflow and wrapper family that pristine upstream does not ship:
  - [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
- [d:r:i] This family does not replace upstream entry surfaces.
- [d:r:i] It composes across them by classifying runtime/doctrine/posture movement and routing later follow-through without absorbing specialist-owner workflows.

### 2. Seed Specialist And Operator-Facing Bridge

- [e:c+i] Repo-local adds a specialist seed-migration route that pristine upstream does not ship:
  - [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md)
  - [gsd-seed-migration-inventory/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md)
- [e:c+i] Repo-local also widens upstream `progress` and `resume-project` through the uplift note so routine re-entry can disclose:
  - seed posture
  - migration candidate count
  - compact breakdown
  - inspect/write specialist commands
  Sources:
  - [progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)
  - [92-seed-migration-pointer-bridge-harden-follow-through-implementation.md](92-seed-migration-pointer-bridge-harden-follow-through-implementation.md)
  - [38-seed-migration-pointer-bridge-harden-change-triggered-refresh.md](../propagation-audit/38-seed-migration-pointer-bridge-harden-change-triggered-refresh.md)
- [d:r:i] This is a true local delta:
  - upstream already had `progress` and `resume-project`
  - repo-local widening gives those surfaces new seed-aware and uplift-aware carry

### 3. Propagation Registry And Governance Carry

- [e:c+i] Repo-local adds a governed propagation family that pristine upstream does not ship:
  - [propagation-audit/README.md](../propagation-audit/README.md)
  - [14-propagation-registry-generation-and-seeding-policy.md](../propagation-audit/14-propagation-registry-generation-and-seeding-policy.md)
  - [15-propagation-registry-v2-layered-first-refresh.md](../propagation-audit/15-propagation-registry-v2-layered-first-refresh.md)
  - [03-propagation-registry-v2-declared-contracts.json](../propagation-audit/artifacts/03-propagation-registry-v2-declared-contracts.json)
  - [04-propagation-registry-v2-semantic-map.json](../propagation-audit/artifacts/04-propagation-registry-v2-semantic-map.json)
  - [05-propagation-registry-v2-evidence-index.json](../propagation-audit/artifacts/05-propagation-registry-v2-evidence-index.json)
  - [06-propagation-registry-v2-coverage-and-refresh.json](../propagation-audit/artifacts/06-propagation-registry-v2-coverage-and-refresh.json)
- [d:r:i] This family is how propagation mapping is currently updated:
  - prose widening and inheritance lanes
  - layered `v2` registry artifacts
  - change-triggered slice refreshes when a local contract movement lands
- [d:r:i] This is the main answer to `how are we currently updating propagation mapping?`

### 4. Lifecycle And Read-Packet Widening

- [e:c+i] Repo-local widens upstream entry and boundary surfaces with stronger reading control and later carry across:
  - `progress`
  - `resume-project`
  - `uplift-project`
  - `new-project`
  - `new-milestone`
  - `ingest-docs`
  - `health`
  - `update`
  Sources:
  - [65-read-packet-and-relevance-control-first-slice-proposal.md](65-read-packet-and-relevance-control-first-slice-proposal.md)
  - [66-read-packet-and-relevance-control-first-slice-implementation.md](66-read-packet-and-relevance-control-first-slice-implementation.md)
  - [67-initialization-and-ingest-read-packet-first-slice-proposal.md](67-initialization-and-ingest-read-packet-first-slice-proposal.md)
  - [68-initialization-and-ingest-read-packet-first-slice-implementation.md](68-initialization-and-ingest-read-packet-first-slice-implementation.md)
  - [69-health-and-migration-follow-through-first-slice-proposal.md](69-health-and-migration-follow-through-first-slice-proposal.md)
  - [70-health-and-migration-follow-through-first-slice-implementation.md](70-health-and-migration-follow-through-first-slice-implementation.md)
  - [71-update-follow-through-first-slice-proposal.md](71-update-follow-through-first-slice-proposal.md)
  - [72-update-follow-through-first-slice-implementation.md](72-update-follow-through-first-slice-implementation.md)
- [d:r:i] This is another answer-back layer to the upstream baseline:
  - upstream already had the entry and boundary workflows
  - repo-local work retunes what they read, how they route, and how much future carry they preserve

### 5. Propagation Review Route

- [e:c+i] Repo-local now adds one operator-facing review route that pristine upstream does not ship:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md)
  - [gsd-propagation-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md)
  - [97-propagation-review-route-first-slice-proposal.md](97-propagation-review-route-first-slice-proposal.md)
  - [98-propagation-review-route-first-slice-implementation.md](98-propagation-review-route-first-slice-implementation.md)
- [d:r:i] This route reads the baseline/delta pair together with the typed propagation family, then uses repo-local tooling only as partial visibility while keeping contextual reread and explicit hold/update disposition sovereign.
- [d:r:i] This is another local delta rather than an upstream replacement:
  - upstream already ships many workflow and lifecycle carriers
  - repo-local work now adds a dedicated operator route for reviewing how concrete contract movement should propagate across them

## How To Read Baseline And Delta Together

- [d:r:i] Ask first:
  - does this carrier already exist in upstream baseline form?
- [d:r:i] Then ask:
  - if yes, what did the repo-local delta widen or reroute?
  - if no, what new local family introduced it and why?
- [d:r:i] This split gives a cleaner answer for cases like:
  - `progress`
    - baseline: upstream progress rendering and routing surface
    - delta: uplift note, read-packet control, seed-aware operator bridge
  - `resume-project`
    - baseline: upstream context restoration surface
    - delta: uplift consumer, seed-aware operator bridge, stronger reading tiers
  - `new-project` / `new-milestone`
    - baseline: shipped initialization and milestone-opening flows
    - delta: stronger read-packet doctrine and later uplift routing

## Current Consequence

- [d:r:i] The repo now has the first baseline/delta pair:
  - [95-upstream-pristine-propagation-baseline-first-slice.md](95-upstream-pristine-propagation-baseline-first-slice.md)
  - this artifact
- [d:r:i] The repo also now has one operator-facing review route for using that pair on concrete multi-family slices:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md)
  - [gsd-propagation-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md)
- [d:r:i] The next adjacent move in this family should decide whether to reread and sharpen that new route or widen later into the bounded uplift agent-assist question that `93` still keeps explicit.
