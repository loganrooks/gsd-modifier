Date: 2026-04-21
Status: active plan

# Initialization, Onboarding, And Project Uplift Strengthening Plan

## Purpose

- [g:r:i] This plan turns entry-surface strengthening into an explicit intervention family.
- [g:r:i] The target is not only cleaner setup. The target is stronger project entry carry across:
  - new project initialization
  - brownfield project initialization
  - milestone opening
  - repo-local governing-doc onboarding
  - vanilla-project uplift into the stronger repo-local harness posture

## Why This Family Now

- [e:c+i] `new-project` already carries deep questioning, brownfield mapping, spike/sketch discovery, research choice, requirements, roadmap, and config creation. Source: [.codex/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-project.md:1).
- [e:c+i] `new-milestone` already carries milestone goal gathering, seed scanning, research choice, requirements, roadmap, and state/project updates. Source: [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:1).
- [e:c+i] `ingest-docs`, `mandatory-initial-read`, `health`, `update`, and `from-gsd2` already provide meaningful inheritance, repair, and migration surfaces around project setup and continuity. Sources: [.codex/get-shit-done/workflows/ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:1), [.codex/get-shit-done/references/mandatory-initial-read.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/mandatory-initial-read.md:1), [.codex/skills/gsd-health/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-health/SKILL.md:1), [.codex/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/update.md:1), [.codex/skills/gsd-from-gsd2/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-from-gsd2/SKILL.md:1).
- [d:r:i] What is not yet carried as one coherent family is repo-local project uplift: a disciplined path for taking a vanilla or older GSD project and bringing runtime, governing docs, planning doctrine, required-reading posture, and long-horizon carry into stronger alignment.

## Family Objective

- [g:r:i] Intensify the harness so entry surfaces do more than start work.
- [g:r:i] They should also:
  - surface governing posture early
  - carry long-horizon and strengthening routes from the start
  - distinguish declared authority from effective runtime authority
  - help older or vanilla projects inherit stronger repo-local doctrine without scattered manual rereads
  - leave an auditable record of what changed, what stayed local, and what still needs later reread

## Surfaces In Scope

### Primary Entry Surfaces

- [d:r:i] `new-project`
- [d:r:i] `new-milestone`
- [d:r:i] `ingest-docs`

### Project Uplift / Continuity Surfaces

- [d:r:i] `health`
- [d:r:i] `progress`
- [d:r:i] `resume-project`
- [d:r:i] `update`
- [d:r:i] `from-gsd2`

### Governing And Onboarding Carriers

- [d:r:i] root `AGENTS.md`
- [d:r:i] `.planning/AGENTS.md`
- [d:r:i] root `CLAUDE.md`
- [d:r:i] `.planning/CLAUDE.md`
- [d:r:i] `mandatory-initial-read`
- [d:r:i] repo-local companion onboarding artifacts under this audit subtree

## Main Strengthening Pressure

- [d:r:i] Initialization already has real questioning and planning carry.
- [d:r:i] The next strengthening move is to make entry surfaces better at:
  - orienting a project to governing doctrine
  - detecting when a project carries older or thinner harness posture
  - routing that project into a bounded uplift path
  - preserving stronger long-horizon and strengthening carry from the start instead of relying on later audits to recover it

## Proposed Sequence

### 1. Entry-Surface Audit

- [d:r:i] Write one bounded map artifact for this family.
- [d:r:i] It should compare:
  - greenfield init
  - brownfield init
  - milestone opening
  - docs-ingest bootstrap/merge
  - repair/recovery surfaces
  - version/runtime update surfaces
- [d:r:i] It should name:
  - what each surface already carries
  - what each surface leaves scattered
  - where they overlap
  - where a single uplift path should own the work instead of relying on operator memory

### 2. Concern And Carrier Placement Pass

- [d:r:i] Before workflow design, write one explicit placement map for this family.
- [d:r:i] It should answer not only what the concerns are, but where each one should surface most strongly:
  - entry workflow question flow
  - required reading
  - governing docs
  - `PROJECT.md`, `STATE.md`, `ROADMAP.md`, `LONG-ARC.md`
  - runtime / install / update checks
  - uplift report / uplift state carriers
  - seeds and later-routing surfaces
  - audit / repair / re-entry surfaces
- [d:r:i] The point is not mere mention. The point is strongest placement and strongest form.

### 3. Uplift Path Design

- [d:r:i] Design one repo-local workflow or skill for project uplift.
- [d:r:i] Working handle:
  - `gsd-uplift-project`
  - or `gsd-upgrade-project`
- [d:r:i] The design should cover:
  - runtime / overlay / install posture check
  - `.planning/` health and continuity check
  - governing-doc install or refresh
  - required-reading / long-horizon / strengthening carry install
  - explicit disposition output

### 4. First Live Slice

- [d:r:i] Land the thinnest high-yield slice first:
  - post-init / post-ingest / post-milestone orientation carry
  - uplift detection in `progress` or `health`
  - one durable project-uplift note or report surface
- [d:r:i] Keep the first slice compact enough that it can be tested on fresh and existing projects without widening into a full harness rewrite.

### 5. Widening After Live Use

- [d:r:i] Only after the first slice produces real examples:
  - widen into milestone-opening carry
  - widen into docs-ingest merge carry
  - widen into stronger resume/re-entry carry
  - widen into richer upgrade/migration families

## Candidate Artifacts

1. [d:r:i] `37-entry-surface-and-project-uplift-map.md`
2. [d:r:i] `38-entry-surface-concern-and-carrier-placement-map.md`
3. [d:r:i] `39-project-uplift-workflow-proposal.md`
4. [d:r:i] `40-project-uplift-first-slice-implementation.md`
5. [d:r:i] `41-project-uplift-example-packet.md`

## Verification And Quality Discipline

- [g:r:i] Scan new request/spec/prompt surfaces with `scan_threshold_language.py`.
- [g:r:i] Verify audit references with `audit_refmap.py verify`.
- [g:r:i] If runtime surfaces change:
  - re-materialize through `./scripts/setup-portable-gsd.sh`
  - then re-check the touched live / overlay surfaces
- [g:r:i] Test this family against multiple real entry situations, not only one:
  - fresh greenfield repo
  - brownfield repo without `.planning/`
  - existing vanilla `.planning/` project
  - docs-heavy repo using `ingest-docs`
  - existing project starting a new milestone
- [g:r:i] Preserve durable disposition notes so uplift does not become invisible silent mutation.

## Current Consequence

- [d:r:i] The next intervention family after the strengthening benchmark/reference pair should include initialization, onboarding, and project uplift directly.
- [d:r:i] The next exact sequence for this family is now:
  1. finish the current widening-lane inheritance boundary
  2. revise `37` so it inherits the widened field cleanly
  3. write the concern/carrier placement pass as `38`
  4. only then draft the uplift workflow proposal
