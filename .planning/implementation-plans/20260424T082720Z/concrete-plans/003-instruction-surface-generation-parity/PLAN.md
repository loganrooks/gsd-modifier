# Immediate Implementation Plan

Date: 2026-04-24
Status: executable draft
Plan ID: `003-instruction-surface-generation-parity`

## Trace Links

- Package index: [../../README.md](../../README.md)
- Strategic horizon frame: [../../HORIZONS.md](../../HORIZONS.md)
- Short-horizon program plan: [../../SHORT-HORIZON.md](../../SHORT-HORIZON.md)
- Prior runtime inventory plan: [../002-runtime-intervention-surface-inventory/PLAN.md](../002-runtime-intervention-surface-inventory/PLAN.md)
- Runtime intervention inventory: [../../../../../docs/runtime-intervention-surfaces.md](../../../../../docs/runtime-intervention-surfaces.md)
- Runtime inventory open questions: [../002-runtime-intervention-surface-inventory/evidence/open-questions.md](../002-runtime-intervention-surface-inventory/evidence/open-questions.md)
- Governing handoff: [../../../../../docs/handoff/current.md](../../../../../docs/handoff/current.md)
- Repo instructions: [../../../../../AGENTS.md](../../../../../AGENTS.md)

## Objective

Make project instruction-surface generation and parity explicit before changing bridge-harness behavior.

This plan traces how `AGENTS.md`, `CLAUDE.md`, `.planning/AGENTS.md`, and `.planning/CLAUDE.md` are generated, tracked, consumed, materialized, and verified. It then implements only the smallest safe parity correction required by the evidence.

Primary deliverables:

- `.planning/implementation-plans/20260424T082720Z/concrete-plans/003-instruction-surface-generation-parity/evidence/current-generation-flow.md`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/003-instruction-surface-generation-parity/evidence/consumer-authority-map.md`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/003-instruction-surface-generation-parity/evidence/decision.md`
- Source/docs/test changes approved by `evidence/decision.md`, if the decision requires them

Candidate implementation outcomes:

1. Keep `AGENTS.md` as the single generated project instruction file for all runtimes and document why `CLAUDE.md` remains a tracked-but-not-generated doctrine carrier.
2. Generate `AGENTS.md` plus a Claude-facing companion or mirror, with explicit conflict and update rules.
3. Defer generation changes and add only contract/test coverage proving the current posture is intentional.

The plan must choose one of these outcomes from evidence. It must not silently pick the easiest code edit.

## Current Observed State

Observed on `2026-04-24` from branch `docs/runtime-intervention-surface-inventory` at head `832b020`:

- The runtime inventory is committed:
  - `a29a973` `docs(runtime-surfaces): inventory bridge intervention carriers`
  - `832b020` `docs(planning): record runtime surface inventory evidence`
- The linked implementation worktree is clean.
- The original checkout has materialized `.codex/` and `.claude/` runtime roots; the linked worktree does not.
- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md` currently sets:

```bash
if [ "$RUNTIME" = "codex" ]; then INSTRUCTION_FILE="AGENTS.md"; else INSTRUCTION_FILE="AGENTS.md"; fi
```

- The same workflow later calls:

```bash
gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"
```

- The output/success criteria describe `$INSTRUCTION_FILE` as `AGENTS.md` for Codex and `AGENTS.md` for all other runtimes.
- `harness_modifier/uplift/carrier_catalog.json` fingerprints `AGENTS.md`, `.planning/AGENTS.md`, `CLAUDE.md`, and `.planning/CLAUDE.md`.
- Codex agent prompts load `AGENTS.md` and `.planning/AGENTS.md` as governing project instructions and explicitly reject `./CLAUDE.md` as governing truth for Codex.
- The runtime inventory identifies this as an unresolved parity question, not a defect already proven.

## Non-Goals

- Do not deploy into `prix-guesser`.
- Do not introduce project-governance artifact seeding beyond instruction surfaces.
- Do not edit compact-prompt behavior; that belongs to `004-compact-prompt-runtime-capability-contract`.
- Do not broaden host matrix semantics or support-language claims.
- Do not treat `CLAUDE.md` as Codex authority.
- Do not remove `CLAUDE.md` or `.planning/CLAUDE.md` from the uplift carrier catalog without a written decision and test update.
- Do not run `$gsd-uplift-project --write` from `new-project.md` or `ingest-docs.md`; existing entry routes intentionally defer write-side uplift refresh.
- Do not overwrite generated or materialized `.codex/` / `.claude/` runtime output by hand.

## Success Criteria

- The current generation flow is documented with exact producers, commands, outputs, and unresolved gaps.
- The consumer authority map distinguishes:
  - Codex agent authority
  - Claude command/operator authority
  - uplift drift-tracking carriers
  - generated project files
  - materialized runtime wrappers
- `evidence/decision.md` records:
  - chosen generation posture
  - rejected alternatives
  - conflict/update policy for `AGENTS.md` and `CLAUDE.md`
  - whether `.planning/AGENTS.md` / `.planning/CLAUDE.md` are generated, mirrored, tracked only, or deferred
  - verification required before execution closeout
- Any source changes are limited to the decision scope and include focused tests.
- If runtime-facing overlay/workflow/manifest files change, source and materialized verification both run.
- The short-horizon registry points at this concrete plan.
- Commit boundaries separate planning artifacts from runtime/source behavior changes.

## Worktree Management Protocol

Use the current linked implementation worktree unless it becomes dirty with out-of-scope changes:

```bash
/home/rookslog/workspace/projects/gsd-modifier-runtime-surfaces-20260424
```

Before edits, record:

```bash
git status --short --branch
git rev-parse --short HEAD
git branch --show-current
```

If executing in a different worktree:

- verify `docs/runtime-intervention-surfaces.md` and the 002 evidence commits are present
- verify no unrelated dirty files are staged
- do not copy materialized `.codex/` / `.claude/` outputs between worktrees as source evidence

## Commit Protocol

All commits must use Conventional Commit subjects:

```text
<type>(<scope>): <imperative summary>
```

Substantive commit bodies must include:

- `Why:`
- `Verification:`
- `Boundary:`

Expected commit buckets:

1. `docs(planning): plan instruction surface parity slice`
   - this plan file
   - package registry updates

2. `docs(planning): record instruction surface parity evidence`
   - `evidence/*.md`

3. Optional if implementation changes are made:
   - `fix(instructions): clarify generated instruction surface posture`
   - or `feat(instructions): add Claude instruction companion generation`
   - or `test(instructions): lock current instruction generation posture`

Do not mix behavior changes with evidence-only planning artifacts.

## Execution Strategy

### Step 0: Preflight

Actions:

1. Record branch, head, and status.
2. Confirm the 002 runtime inventory commits are present.
3. Create the plan-local `evidence/` directory.
4. Record whether materialized `.codex/` and `.claude/` roots exist in the active worktree.

Expected output:

- `evidence/current-generation-flow.md` starts with preflight facts.

### Step 1: Trace Generation Producers

Inspect and cite:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md`
- `tooling/portable-gsd/overlay/get-shit-done/references/entry-runtime-uplift-continuity.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/update.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md`
- `tooling/codex/project_uplift.py`
- `harness_modifier/uplift/carrier_catalog.json`
- tests under `tooling/codex/tests/` that mention `AGENTS.md`, `CLAUDE.md`, `project_uplift`, `entry-runtime-uplift-continuity`, or initialization

Required questions:

- Where is `INSTRUCTION_FILE` set?
- Where is `$INSTRUCTION_FILE` written?
- What does `gsd-sdk query generate-claude-md` actually produce, and is the generated body controlled by this repo or upstream SDK?
- Which workflows read, refresh, or preserve instruction surfaces after initialization?
- Which of those paths are source-only, and which materialize into runtime roots?

Deliverable:

- `evidence/current-generation-flow.md`

### Step 2: Trace Consumers And Authority

Map each consumer family:

- Codex agents in `tooling/portable-gsd/overlay/agents/*.toml` and shared Markdown agents
- Codex skills in `tooling/portable-gsd/overlay/skills/`
- Claude command wrappers in `harness_modifier/overlay/commands/gsd/`
- shared workflows in `tooling/portable-gsd/overlay/get-shit-done/workflows/`
- specialist workflows in `harness_modifier/overlay/get-shit-done/workflows/`
- uplift/reporting consumers in `tooling/codex/project_uplift.py`
- repo operator docs: `AGENTS.md`, `WORKFLOW.md`, `docs/development.md`, `docs/install-profiles.md`, `docs/onboarding/codex.md`, `docs/onboarding/claude.md`

Required distinctions:

- governing runtime instruction
- tracked doctrine carrier
- generated project output
- human onboarding guidance
- materialized runtime entrypoint
- stale or absent surface

Deliverable:

- `evidence/consumer-authority-map.md`

### Step 3: Decide The Parity Posture

Write `evidence/decision.md` before source changes.

The decision must pick exactly one posture:

#### Option A: Single Generated `AGENTS.md`

Use when evidence shows `AGENTS.md` is intentionally the runtime-agnostic project instruction surface and `CLAUDE.md` should be tracked only when a host already has it.

Required changes:

- clarify `new-project.md` comments and success text so `AGENTS.md for all runtimes` is intentional, not accidental
- add or update tests that lock this posture
- document why `CLAUDE.md` remains in `carrier_catalog.json`

#### Option B: Generated Runtime Companion

Use when evidence shows Claude runtime needs a generated `CLAUDE.md` companion for equivalent operator behavior.

Required changes:

- update generation flow to write `AGENTS.md` and Claude companion without making `CLAUDE.md` Codex authority
- define conflict handling when both files already exist
- update uplift carrier catalog/tests if the generated/tracked distinction changes
- update overlay manifest and materialization tests only if runtime-carried wrappers or source paths change

#### Option C: Defer Behavior, Add Contract Coverage

Use when evidence is insufficient to change generation safely.

Required changes:

- add a bounded contract test or doc note that records current behavior as observed but undecided
- park implementation behind a sharper follow-up plan

Decision rules:

- Do not choose Option B solely because the generator command is named `generate-claude-md`; the output path and runtime authority must justify it.
- Do not choose Option A solely because it is current behavior; it must have a documented authority model.
- If the exact upstream SDK generator body cannot be inspected, mark that as a verification gap and avoid claims about body semantics.

### Step 4: Implement The Chosen Minimal Slice

Allowed write surfaces depend on `evidence/decision.md`.

Always allowed:

- plan-local `evidence/*.md`
- this package's `README.md`, `SHORT-HORIZON.md`, and `HORIZONS.md`

Allowed for Option A:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`
- focused tests under `tooling/codex/tests/`
- docs explaining the authority distinction if needed

Allowed for Option B:

- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`
- possibly `tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md`
- `harness_modifier/uplift/carrier_catalog.json` only if catalog semantics change
- focused tests under `tooling/codex/tests/`
- docs explaining conflict/update policy

Allowed for Option C:

- focused tests or docs that preserve the observed behavior and name the open question

If an edit requires a new source file, manifest entry, setup-script change, or materialized runtime output, stop and revise this plan before continuing unless the decision explicitly authorized that class of change.

### Step 5: Verify

Minimum checks for evidence/docs-only execution:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .planning/implementation-plans/20260424T082720Z
```

If `docs/` changes:

```bash
python3 tooling/codex/audit_refmap.py verify docs
```

If workflow, overlay, carrier catalog, or tests change:

```bash
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest \
  tooling.codex.tests.test_initialization_read_packet_contract \
  tooling.codex.tests.test_entry_runtime_continuity_shared_reference_contract \
  tooling.codex.tests.test_project_uplift \
  tooling.codex.tests.test_runtime_adapter_parity
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
git diff --check
```

If runtime-facing overlay/workflow/manifest behavior changes:

```bash
./scripts/setup-portable-gsd-runtime.sh --runtime both
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict
python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict
```

Do not claim materialized parity unless the materialized checks were run.

### Step 6: Commit And Closeout

Before each commit:

```bash
git status --short
git diff --cached --stat
git diff --cached --check
```

Closeout must include:

- commit hashes
- chosen parity posture
- verification commands and results
- whether runtime-facing files changed
- whether materialized checks were required and run
- parked questions
- next recommended plan

## Expected Next Plan After This

If this plan chooses and verifies instruction-surface posture cleanly, the next concrete plan should be:

- `004-compact-prompt-runtime-capability-contract`

If the decision parks behavior because upstream SDK generation cannot be inspected, write a smaller follow-up plan for generator-body discovery before compact-prompt work.
