Date: 2026-04-21
Status: active workflow proposal

# Project Uplift Workflow Proposal

## Purpose

- [g:r:i] This proposal turns the revised entry/uplift terrain in `37` and the stronger carrier-placement map in `38` into one bounded composition-layer workflow.
- [g:r:i] The target is not generic onboarding. The target is one explicit owned path for taking an existing project whose posture has thinned or aged and bringing runtime/install truth, governing posture, planning doctrine, and durable uplift memory into stronger alignment.

## Why This Workflow Now

- [e:c+i] `37` now maps the widened family directly: creation, milestone opening, docs bootstrap/merge, re-entry, repair, update, migration, workspace/worktree entry, phase-injection entry, installer rerun, governing-posture install, split uplift families, forensics entry, archived-milestone re-entry, and audit-subtree aging all now sit in one terrain map. Source: [37-entry-surface-and-project-uplift-map.md](./37-entry-surface-and-project-uplift-map.md:1).
- [e:c+i] `38` now records strongest placement for that family: runtime/install, governing-doc, required-reading, claim-type, long-horizon, state-boundary, discovery, cross-runtime, tooling, audit-aging, and uplift-output concerns are all mapped to primary carriers, supporting carriers, and non-owners. Source: [38-entry-surface-concern-and-carrier-placement-map.md](./38-entry-surface-concern-and-carrier-placement-map.md:1).
- [d:r:i] Those two artifacts are enough to define a workflow owner cleanly. What is still missing is the workflow shape itself.

## Working Handle

- [d:r:i] Preferred working handle: `gsd-uplift-project`
- [d:r:i] Alternate handle kept seeded: `gsd-upgrade-project`
- [d:r:i] This proposal uses `gsd-uplift-project` because the family is broader than version upgrade alone.

## Workflow Objective

- [d:r:i] The workflow should do four things well:
  1. detect when a project deserves uplift as its own action rather than silent continuation
  2. gather the right evidence from specialist owners without absorbing them
  3. refresh the strongest subset of repo-local carriers in one coherent pass
  4. write durable uplift memory and route the operator to the correct next action

## Ownership Boundary

### What This Workflow Should Own

- [d:r:i] posture detection for existing projects
- [d:r:i] composition of evidence from runtime/install, structural health, governing-doc posture, long-horizon posture, and repo-local tooling posture
- [d:r:i] compact refresh of the strongest first-slice carrier set
- [d:r:i] durable uplift outputs and routing

### What This Workflow Should Not Absorb

- [d:r:i] `new-project` creation flow
- [d:r:i] `new-milestone` milestone-opening flow
- [d:r:i] `ingest-docs` docs bootstrap/merge flow
- [d:r:i] `health` structural repair logic
- [d:r:i] `update` runtime install/version flow
- [d:r:i] `from-gsd2` migration flow
- [d:r:i] `mandatory-initial-read` enforcement
- [d:r:i] repo-local tooling behavior itself

## Entry Conditions

### Explicit Entry

- [d:r:i] The workflow should be invokable directly when the operator wants a repo-local posture reread or refresh:
  - `Run $gsd-uplift-project --detect-only`
- [d:r:i] Detect-only should be the default opening posture. Refresh or install should require explicit flags.

### Routed Entry

- [d:r:i] The workflow should later become a routed recommendation from:
  - `progress`
  - `resume-project`
  - `health`
  - `update`
  - `ingest-docs`
  - `new-milestone`
- [d:r:i] In the first slice, routed recommendation is enough. Those specialist surfaces do not need to absorb uplift logic.

## Detection Signals

- [d:r:i] A first-slice uplift pass should open when the project’s current carrier fingerprint differs from current repo-local doctrine in one or more bounded ways:
  - governing-doc carrier fingerprint differs across root/planning `AGENTS.md` or `CLAUDE.md` wrappers
  - `.planning/CLAIM-TYPES.md` carrier is absent or its fingerprint differs from the current repo-local doctrine fingerprint
  - `.planning/LONG-ARC.md` carrier is absent or its fingerprint differs from the current repo-local doctrine fingerprint
  - required-reading installation practice is not yet present on the project’s live packet/spec/prompt surfaces
  - strengthening-route carry is not yet present in the local discuss/context/plan/research chain where the repo now expects it
  - repo-local tooling inventory expected by doctrine is not yet present
  - the project resumed or opened a new milestone after a major doctrine move without an intervening uplift record
  - runtime-side registry or wrapper posture fingerprints differ from current local runtime expectations

## First-Slice Scope

- [d:r:i] The first slice should cover:
  - one repo at a time
  - detect-only classification and reporting by default
  - vanilla and lightly aged projects first
  - single-runtime posture reread first
  - additive carrier installs only when explicitly requested
  - durable output plus one routable state carrier
- [d:r:i] The first slice should hold out:
  - full runtime reinstall
  - structural repair beyond `health`
  - cross-project batching
  - workstream reconciliation
  - aged-bespoke deep merge
  - full audit-tree restructuring
  - doctrine-carrying audit-subtree vintage stamping
  - full upstream-template expression pass
  - broad doctrine-sensitive wrapper rewrites by default

## Proposed Workflow Shape

### 1. Open The Pass And Classify It

- [d:r:i] Read the minimal current posture surfaces:
  - root `AGENTS.md`
  - `.planning/AGENTS.md`
  - root/planning `CLAUDE.md`
  - `STATE.md`
  - `.planning/LONG-ARC.md` if present
  - `.planning/CLAIM-TYPES.md` if present
- [d:r:i] Classify the uplift family:
  - vanilla uplift
  - lightly aged uplift
  - mid-phase uplift
  - aged-bespoke uplift
  - cross-runtime uplift
  - upstream-template-drift uplift
- [d:r:i] For first slice, only vanilla and lightly aged cases should proceed automatically; the others should be explicitly flagged and narrowed or deferred.

### 2. Gather Evidence From Specialist Owners

- [d:r:i] Pull runtime/install truth from:
  - `update` posture
  - installer/materialization posture from `scripts/setup-portable-gsd.sh`
  - `runtime_visibility.py`
  - `manifest_install_coherence.py` where helpful
- [d:r:i] Pull structural health from:
  - `health`
- [d:r:i] Pull project/milestone state from:
  - `STATE.md`
  - `progress`
  - `resume-project` context where relevant
- [d:r:i] Pull docs/bootstrap context from:
  - `ingest-docs` outputs where relevant
- [d:r:i] The workflow consumes these outputs. It does not reimplement them.
- [d:r:i] In the first slice, installer/materialization posture plus `runtime_visibility.py` and `manifest_install_coherence.py` feed detect-only reporting and routing; they do not by themselves open new install flags.

### 3. Produce A Doctrine-And-Posture Delta

- [d:r:i] Detect-only should produce a thin delta first:
  - current class
  - current carrier fingerprints
  - current runtime-side registry posture
  - current doctrine/install carriers present
  - current doctrine/install carriers absent
  - later-family pressure that should stay deferred
- [d:r:i] That delta should become operator-facing material inside `UPLIFT-REPORT.md` and machine-routable material inside the thin doctrine manifest.
- [d:r:i] The thin doctrine manifest should use a named fingerprint shape per carrier:
  - doctrine-version stamp where a carrier exposes an explicit doctrine vintage
  - content hash for thin wrapper or config carriers
  - section-list or inventory hash for tooling inventory and other enumerated carrier sets
  - runtime-registry hash for `.codex/config.toml` and `.codex/agents/*.toml`

### 4. Apply Explicit First-Slice Refresh Flags

- [d:r:i] First-slice refresh should be split into narrower per-carrier routes with explicit flags and blast-radius labels.
- [d:r:i] Low-ambiguity additive routes:
  - install `.planning/CLAIM-TYPES.md` where absent
  - install `.planning/LONG-ARC.md` where absent
  - install thin doctrine manifest and uplift state carriers
  - install tooling inventory carrier where absent
- [d:r:i] Doctrine-sensitive proposal routes:
  - generate diffs/proposals for root/planning `AGENTS.md`
  - generate diffs/proposals for root/planning `CLAUDE.md`
  - generate diffs/proposals for required-reading practice on request/spec/prompt surfaces
  - generate diffs/proposals for strengthening-route carry where the repo now expects it
- [d:r:i] Claim-type reference install and claim-type activation are separate:
  - reference-file install may sit in the first slice
  - activation across existing load-bearing artifacts should require explicit operator consent because it rewrites project content
- [d:r:i] For first slice, prefer additive install or proposal generation over broad content rewrite.

### 5. Write Durable Uplift Outputs

- [d:r:i] First-slice outputs should be:
  - `UPLIFT-REPORT.md`
  - dedicated uplift section inside `STATE.md`
  - thin doctrine manifest such as `UPLIFT-MANIFEST.json`
- [d:r:i] `UPLIFT-REPORT.md` should record:
  - detected uplift class
  - before-state posture
  - current doctrine-and-posture delta
  - what was refreshed
  - what was intentionally not refreshed
  - what should be routed later
- [d:r:i] The `STATE.md` uplift section should record:
  - last uplift date
  - last uplift class
  - whether doctrine has materially moved since the last uplift
- [d:r:i] The thin doctrine manifest should record:
  - named carrier fingerprint shape and current fingerprint per carrier
  - last detect-only pass
  - last explicit install pass
  - whether runtime-side registry and wrapper posture align
  - whether any doctrine-sensitive proposals are still pending human review

### 6. Route The Next Action

- [d:r:i] After refresh, the workflow should route explicitly:
  - to `new-milestone` when the real next move is milestone opening
  - to `progress` when posture is refreshed and ordinary routing can resume
  - to `health` when structural issues block uplift follow-through
  - to `update` when install/runtime issues block posture refresh
  - to `discuss-phase` when a phase boundary should be reopened under current doctrine
  - to `plant-seed` when a stronger future move is out of scope for the current uplift slice
- [d:r:i] First live routed consumer:
  - one read-only `progress` hook that treats `UPLIFT-MANIFEST.json` as the authoritative fingerprint source, uses the `STATE.md` uplift section as narrative companion, and can recommend `gsd-uplift-project --detect-only` when posture has drifted or when pending doctrine-sensitive proposals are still unresolved

## Carrier Decisions

### Best Place For The Workflow To Live

- [d:r:i] Preferred form:
  - repo-local skill plus workflow surface
- [d:r:i] Why:
  - this family is composition-layer behavior, not a one-off audit note
  - it should be callable directly and routable later from specialist surfaces

### Best Place For Its Outputs

- [d:r:i] `UPLIFT-REPORT.md`
  - strongest for per-pass memory and operator-facing before/after truth
- [d:r:i] `STATE.md` uplift section
  - strongest for later routing by `progress` / `resume-project`
- [d:r:i] `UPLIFT-MANIFEST.json`
  - strongest for thin structured doctrine/runtime fingerprints that later consumers can read without prose parsing
- [d:r:i] seeds
  - strongest for out-of-slice deferred strengthening

## Review And Verification Gates

- [g:r:i] Before any implementation slice is accepted:
  - run `scan_threshold_language.py` on new request/spec/prompt/proposal surfaces
  - run `scan_threshold_language.py` on generated `UPLIFT-REPORT.md` before finalizing the pass
  - run `audit_refmap.py verify` on the active audit root
  - if runtime surfaces change, re-materialize through `./scripts/setup-portable-gsd.sh`
  - reread touched workflow/skill surfaces against `37` and `38`, not against memory
  - require explicit human review before accepting doctrine-sensitive diffs for root/planning `AGENTS.md`, root/planning `CLAUDE.md`, or other canon carriers
- [g:r:i] Before the first live slice is accepted:
  - test one vanilla project case
  - test one lightly aged project case
  - confirm the workflow routes rather than absorbs specialist-owner work
  - confirm the output artifacts make the before/after legible
  - confirm `progress` can read the uplift state carrier and thin doctrine manifest without prose parsing

## Current Consequence

- [d:r:i] The family now has:
  - `36` plan
  - revised `37` terrain map
  - `38` concern/carrier placement map
  - this bounded workflow proposal
- [d:r:i] The revised bundle has now also completed that bounded reread and the resulting harmonization pass.
- [d:r:i] The next move should therefore be first-slice implementation plus the bounded verification set already named here:
  - one vanilla project case
  - one lightly aged project case
  - one repo-local negative test on prix-guesser itself
