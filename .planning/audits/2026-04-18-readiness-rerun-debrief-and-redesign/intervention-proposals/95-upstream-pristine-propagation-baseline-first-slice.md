Date: 2026-04-22
Status: landed first baseline slice

# Upstream Pristine Propagation Baseline First Slice

## Role

- [g:r:i] This artifact is the first operator-facing upstream-pristine propagation baseline.
- [g:r:i] Its job is to answer:
  - what shipped GSD exposes before repo-local intervention
  - which propagation families are already present at that upstream frontier
  - what later repo-local delta work should answer back to rather than silently replacing
- [g:r:i] It is not a whole-upstream exhaustive map yet.
- [g:r:i] It is the first bounded baseline slice for the highest-traffic families we currently route through.

## Baseline Rule

- [e:c+i] The installer still begins from an upstream pristine local install before any repo-local overlay is applied. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:19).
- [e:c+i] Upstream `docs/INVENTORY.md` declares itself the authoritative shipped-surface roster frontier and says new surfaces should land there first. Source: [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:1).
- [d:r:i] This baseline therefore tracks the upstream shipped frontier, not the later repo-local overlay or governance delta.

## First-Slice Scope

- [d:r:i] This first slice covers the upstream families most relevant to current repo routing:
  - entry and orchestration surfaces
  - shared steering/state carriers
  - lifecycle and boundary carriers
  - internal command/runtime support surfaces that materially shape propagation
- [d:r:i] It does not yet attempt the full shipped surface inventory.
- [d:r:i] It does not yet include repo-local-only workflows, repo-local governance docs, or repo-local propagation refresh artifacts.

## Baseline Families

### 1. Entry And Orchestration

- [e:c+i] Upstream shipped command entry includes at least:
  - `/gsd-new-project`
  - `/gsd-discuss-phase`
  - `/gsd-plan-phase`
  - `/gsd-new-milestone`
  - `/gsd-progress`
  - `/gsd-plant-seed`
  - `/gsd-health`
  - `/gsd-ingest-docs`
  - `/gsd-update`
  Sources:
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:65)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:69)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:73)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:107)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:119)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:131)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:151)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:161)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:168)
- [e:c+i] Upstream shipped workflow carriers behind those entries include:
  - `new-project.md`
  - `discuss-phase.md`
  - `plan-phase.md`
  - `new-milestone.md`
  - `progress.md`
  - `plant-seed.md`
  - `health.md`
  - `ingest-docs.md`
  - `update.md`
  Sources:
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:199)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:220)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:221)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:228)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:230)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:233)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:209)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:213)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:256)
- [d:r:i] In the upstream baseline, these entry surfaces already form a propagation family:
  - commands expose workflow routes
  - workflow docs disclose the main human-facing boundary
  - agent/worker orchestration sits behind some of those workflows rather than appearing only as repo-local addition

### 2. Shared Steering And State Carriers

- [e:c+i] Upstream inventory explicitly includes `mandatory-initial-read.md` as a shared required-reading reference. Source: [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:287).
- [e:c+i] Upstream workflow inventory already includes `resume-project.md` and `transition.md`, which means upstream pristine already has first-read continuity and phase-boundary movement carriers before repo-local interventions widen them. Sources:
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:238)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:251)
- [e:c+i] Upstream internal helpers already include `roadmap.cjs` and `state.cjs`, so pristine upstream already carries typed state/roadmap parsing and update surfaces beneath human-facing workflows. Sources:
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:375)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:378)
- [d:r:i] In the upstream baseline, state continuity is not only a repo-local invention. The repo-local work widened and retuned it later, but it answers back to upstream steering/state carriers that already exist.

### 3. Lifecycle And Boundary Carriers

- [e:c+i] Upstream pristine already includes `verify-phase.md` and `transition.md` as internal lifecycle/boundary surfaces, even where they are not direct top-level user commands. Sources:
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:251)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:258)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:261)
- [e:c+i] Upstream pristine already includes the milestone opening boundary through `new-milestone.md`. Source: [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:220).
- [d:r:i] In the upstream baseline, lifecycle carry already exists as a family. Repo-local work later widened it across long-arc and future-carry doctrine, but did not create lifecycle propagation from nothing.

### 4. Runtime Support And Internal Infrastructure

- [e:c+i] Upstream inventory explicitly includes internal CLI/runtime helpers such as:
  - `docs.cjs`
  - `intel.cjs`
  - `roadmap.cjs`
  - `state.cjs`
  - update-related hooks and workers
  Sources:
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:363)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:368)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:375)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:378)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:396)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:397)
  - [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:404)
- [d:r:i] In the upstream baseline, propagation does not stop at human-facing workflows. Internal runtime helpers and hooks are already part of the shipped network and should remain visible in the baseline rather than appearing later only as repo-local complexity.

## What This Baseline Explicitly Excludes

- [d:r:i] Repo-local-only workflows such as `uplift-project.md` and `seed-migration-inventory.md`
- [d:r:i] Repo-local-only skills such as `gsd-uplift-project` and `gsd-seed-migration-inventory`
- [d:r:i] Repo-local governance surfaces such as this audit subtree, `CURRENT-STATE.md`, and `HARNESS-IMPROVEMENT-REGISTER.md`
- [d:r:i] Repo-local helper changes, registry refresh artifacts, and overlay-manifest typing
- [d:r:i] Repo-local propagation widening around lifecycle carry, strengthening routes, or seed-family bridges

## Current Consequence

- [d:r:i] The upstream-pristine baseline now exists as a separate first-slice object.
- [d:r:i] The next adjacent artifact should be the repo-local delta layer answering back to this baseline rather than another blended propagation summary.
