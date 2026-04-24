# Immediate Implementation Plan

Date: 2026-04-24
Status: executable draft
Plan ID: `002-runtime-intervention-surface-inventory`

## Trace Links

- Package index: [../../README.md](../../README.md)
- Strategic horizon frame: [../../HORIZONS.md](../../HORIZONS.md)
- Short-horizon program plan: [../../SHORT-HORIZON.md](../../SHORT-HORIZON.md)
- Prior stabilization plan: [../001-audit-import-refmap-stabilization/PLAN.md](../001-audit-import-refmap-stabilization/PLAN.md)
- Runtime intervention boundary note: [../../../20260424T084414Z/RUNTIME-INTERVENTION-SURFACES.md](../../../20260424T084414Z/RUNTIME-INTERVENTION-SURFACES.md)
- Governing handoff: [../../../../../docs/handoff/current.md](../../../../../docs/handoff/current.md)
- Repo instructions: [../../../../../AGENTS.md](../../../../../AGENTS.md)

## Objective

Create a reviewable runtime intervention surface inventory before any bridge-harness behavior is changed.

This plan is an evidence and contract-mapping slice. It does not implement workflow-lane routing, project-governance artifact generation, `prix-guesser` deployment, or parity architecture rewrites. It prepares those later slices by making every runtime-facing carrier, generation path, materialization path, and verification hook visible.

Primary deliverable:

- `docs/runtime-intervention-surfaces.md`

Supporting deliverables:

- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/runtime-carriers.md`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/instruction-generation.md`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/materialization-contracts.md`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/open-questions.md`

## Current Observed State

Observed on `2026-04-24`:

- Branch: `main`
- Head: `49bb0b7`
- Dirty tracked file outside this plan: `tooling/portable-gsd/overlay/config.toml`
- Previous stabilization commits are present:
  - `bb5df84` refmap behavior and tests
  - `a039ba7` carried origin audit import
  - `e6a2067` origin audit README update
  - `d6b7ed8` runtime intervention boundary note
  - `49bb0b7` Conventional Commit protocol in `AGENTS.md`

The dirty `tooling/portable-gsd/overlay/config.toml` is not owned by this plan. Execution must either run in a clean linked worktree created from `HEAD`, or explicitly park/commit/restore that file under a separate user-approved slice before touching runtime-facing overlay behavior.

## Non-Goals

- Do not edit runtime behavior.
- Do not edit `tooling/portable-gsd/overlay/config.toml` in this slice.
- Do not deploy into `prix-guesser`.
- Do not generate or overwrite `CLAUDE.md`, `AGENTS.md`, `.planning/CLAUDE.md`, or `.planning/AGENTS.md`.
- Do not add new project-governance artifact generators.
- Do not broaden host matrix semantics.
- Do not claim bridge-harness release readiness.

## Success Criteria

- `docs/runtime-intervention-surfaces.md` exists and distinguishes:
  - runtime-facing carriers
  - operator guidance
  - generated files
  - hand-maintained files
  - materialized outputs
  - verification hooks
  - known gaps or deferred questions
- Each listed surface has:
  - source path
  - runtime relevance
  - producer
  - consumer
  - materialization or install path
  - verification command or explicit verification gap
  - parity posture: shared outcome, Codex-specific, Claude-specific, or unknown
- Evidence files record what was inspected and what was inferred.
- The plan leaves the worktree no dirtier than it found it, except for explicitly committed in-scope docs/planning artifacts.
- Conventional Commit protocol is followed for all commits.
- Verification passes or failures are explicitly recorded.

## Worktree Management Protocol

This plan must not be executed directly in a mixed worktree if write work is delegated.

Preferred execution model:

1. Keep the current checkout as orchestration/control only.
2. Create a clean linked worktree from `HEAD` for the implementation slice:

```bash
git worktree add ../gsd-modifier-runtime-surfaces-20260424 49bb0b7
```

3. In the linked worktree, create a topic branch:

```bash
git switch -c docs/runtime-intervention-surface-inventory
```

4. Run all delegated write work inside that clean linked worktree.
5. Do not copy or stage the dirty `tooling/portable-gsd/overlay/config.toml` from the original checkout.
6. Before integrating back, verify:

```bash
git status --short
git diff --check
```

Fallback model if no linked worktree is used:

- Execution may proceed only after `git status --short` shows no dirty files except files deliberately owned by this plan.
- Do not use `git stash` or restore the dirty config file without explicit user approval.

## Commit Protocol

All commits must use Conventional Commit subjects:

```text
<type>(<scope>): <imperative summary>
```

Every substantive commit body must include:

- `Why:`
- `Verification:`
- `Boundary:`

Expected commit buckets:

1. `docs(runtime-surfaces): inventory bridge intervention carriers`
   - `docs/runtime-intervention-surfaces.md`
   - body records evidence sources and verification

2. `docs(planning): record runtime surface inventory evidence`
   - plan-local `evidence/*.md`
   - body records agent reports consumed and unresolved questions

3. Optional only if the short-horizon registry is updated after execution:
   - `docs(planning): update bridge harness plan registry`
   - `README.md`, `SHORT-HORIZON.md`, or `HORIZONS.md` under this implementation-plan package

Do not mix source behavior changes with this inventory slice. If an execution agent discovers a bug, record it in `evidence/open-questions.md` and park the fix for a later plan.

## Delegation Topology

Delegation is allowed only after the clean worktree protocol is satisfied.

Main thread responsibilities:

- own final synthesis
- own all commits
- review every delegated report
- record each delegated report disposition as `accept`, `revise`, `park`, or `reject`
- prevent overlap with dirty/out-of-scope config drift

Delegated reports are read-only analysis tasks unless explicitly upgraded. Each agent writes only its assigned evidence file.

Delegation briefs:

- [delegation/agent-a-runtime-carriers.md](delegation/agent-a-runtime-carriers.md)
- [delegation/agent-b-instruction-generation.md](delegation/agent-b-instruction-generation.md)
- [delegation/agent-c-materialization-contracts.md](delegation/agent-c-materialization-contracts.md)

Write ownership:

| Owner | Write scope |
| --- | --- |
| Agent A | `evidence/runtime-carriers.md` |
| Agent B | `evidence/instruction-generation.md` |
| Agent C | `evidence/materialization-contracts.md` |
| Main thread | `docs/runtime-intervention-surfaces.md`, `evidence/open-questions.md`, plan registry updates |

No delegated agent may edit source code, runtime overlay files, install scripts, or docs outside the assigned write scope during this plan.

## Execution Strategy

### Step 0: Preflight And Isolation

Actions:

1. Record:

```bash
git status --short --branch
git rev-parse --short HEAD
git branch --show-current
```

2. Confirm whether execution is happening in:
   - a clean linked worktree, or
   - the original checkout with the dirty config explicitly out of scope.
3. Confirm the dirty `tooling/portable-gsd/overlay/config.toml` is not staged.
4. Create the plan-local evidence directory.

Expected output:

- evidence file header recording branch, head, status, and worktree mode

Blockers:

- If any delegated write work is planned and no clean worktree exists, stop and create the clean worktree.
- If `tooling/portable-gsd/overlay/config.toml` becomes staged, stop and unstage it without discarding content.

### Step 1: Parallel Evidence Collection

Dispatch at most three bounded agents in parallel after Step 0.

Agent A: Runtime carriers and operator surfaces

- Brief: [delegation/agent-a-runtime-carriers.md](delegation/agent-a-runtime-carriers.md)
- Output: `evidence/runtime-carriers.md`
- Focus: runtime-facing files, operator docs, onboarding docs, overlay manifests, runtime-specific carriers

Agent B: Instruction generation and uplift paths

- Brief: [delegation/agent-b-instruction-generation.md](delegation/agent-b-instruction-generation.md)
- Output: `evidence/instruction-generation.md`
- Focus: producers that create or update instruction surfaces such as `AGENTS.md`, `CLAUDE.md`, planning mirrors, onboarding docs, and uplift carriers

Agent C: Materialization contracts and verification hooks

- Brief: [delegation/agent-c-materialization-contracts.md](delegation/agent-c-materialization-contracts.md)
- Output: `evidence/materialization-contracts.md`
- Focus: install scripts, manifest contract checks, runtime visibility checks, canary checks, host matrix surfaces

Main thread during delegation:

- read `docs/install-profiles.md`, `docs/host-exercise-matrix.md`, `harness_modifier/uplift/carrier_catalog.json`, and `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- sketch the final inventory schema
- do not duplicate delegated scans

### Step 2: Review And Disposition Delegated Reports

For each delegated report:

1. Read the report.
2. Check that every claim points to a file path or command.
3. Mark disposition in `evidence/open-questions.md`:
   - `accept`: ready to synthesize
   - `revise`: needs correction before synthesis
   - `park`: useful but out of scope
   - `reject`: not evidence-backed or outside scope
4. If any report is `revise`, correct only the report or ask the same agent for a bounded revision.

No report may be synthesized silently without disposition.

### Step 3: Build The Inventory Document

Create `docs/runtime-intervention-surfaces.md` with this structure:

1. Purpose and boundary
2. Inventory table
3. Runtime-facing carriers
4. Operator guidance surfaces
5. Instruction generation paths
6. Materialization and install paths
7. Verification hooks
8. Parity posture table
9. Known gaps and deferred questions
10. Next implementation candidates

Required table columns:

- Surface
- Current path
- Runtime relevance
- Producer
- Consumer
- Generated or maintained
- Codex posture
- Claude posture
- Verification hook
- Open concern

Rules:

- Distinguish observed file relationships from inferred relationships.
- If a producer is not found, write `unknown` and add an open question.
- If a verification hook does not exist, write `none yet` and add a future contract candidate.
- Do not describe a runtime-specific surface as parity unless both runtime carriers and verification evidence exist.

### Step 4: Verify The Inventory Slice

Minimum verification:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify docs
python3 tooling/codex/audit_refmap.py verify .planning/implementation-plans/20260424T082720Z
python3 tooling/codex/audit_refmap.py map \
  .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign \
  --output .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/reorganization-refmap-after.md
```

Expected audit refmap baseline for the imported audit corpus:

- markdown files scanned: `800`
- markdown links scanned: `7834`
- local existing links: `7787`
- local missing links: `47`

If the map count changes, explain why before committing.

Do not run full bootstrap or materialization gates unless this inventory slice changes shipped/runtime, overlay, install, or contract files. If those files are changed, this plan has been exceeded and must be revised before continuing.

### Step 5: Commit

Before each commit:

```bash
git status --short
git diff --cached --stat
git diff --cached --check
```

Commit with Conventional Commit subjects and body sections.

Example:

```text
docs(runtime-surfaces): inventory bridge intervention carriers

Why: The bridge-harness short horizon needs an explicit map of runtime-facing carriers before behavior changes can be planned safely.

Verification: git diff --check; python3 tooling/codex/audit_refmap.py verify docs; python3 tooling/codex/audit_refmap.py verify .planning/implementation-plans/20260424T082720Z

Boundary: Inventory only. No runtime behavior, overlay config, install scripts, or parity architecture changes are included.
```

### Step 6: Closeout

Final response or handoff must include:

- commit hashes
- verification commands and results
- whether the dirty `tooling/portable-gsd/overlay/config.toml` remained untouched
- accepted delegated report list
- parked or unresolved questions
- next recommended concrete plan

## Expected Next Plan After This

If this plan completes cleanly, the next concrete plan should be one of:

- `003-instruction-surface-generation-parity`
- `004-compact-prompt-runtime-capability-contract`
- a smaller contract-tooling plan if the inventory exposes missing verification hooks that block safe parity work

Do not start those plans until this inventory is committed and the worktree state is explicitly understood.
