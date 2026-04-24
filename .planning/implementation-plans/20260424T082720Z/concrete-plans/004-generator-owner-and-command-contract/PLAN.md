# Contract Decision Spike Plan

Date: 2026-04-24
Status: executable draft
Plan ID: `004-generator-owner-and-command-contract`
Task type: contract decision spike with a bounded implementation tail

## Trace Links

- Package index: [../../README.md](../../README.md)
- Short-horizon program plan: [../../SHORT-HORIZON.md](../../SHORT-HORIZON.md)
- Prior decision: [../003-instruction-surface-generation-parity/evidence/decision.md](../003-instruction-surface-generation-parity/evidence/decision.md)
- Prior generation evidence: [../003-instruction-surface-generation-parity/evidence/current-generation-flow.md](../003-instruction-surface-generation-parity/evidence/current-generation-flow.md)
- Consumer authority map: [../003-instruction-surface-generation-parity/evidence/consumer-authority-map.md](../003-instruction-surface-generation-parity/evidence/consumer-authority-map.md)
- Runtime intervention inventory: [../../../../../docs/runtime-intervention-surfaces.md](../../../../../docs/runtime-intervention-surfaces.md)
- Governing handoff: [../../../../../docs/handoff/current.md](../../../../../docs/handoff/current.md)
- Repo instructions: [../../../../../AGENTS.md](../../../../../AGENTS.md)

## Classification

This is not ordinary implementation and not open-ended research.

It is a contract decision spike: the first deliverable is a defensible decision about generator ownership, command semantics, and target instruction files. Implementation is allowed only after the decision artifact names an option and authorizes a concrete write set.

Why this classification matters:

- the prior slice found contradictory command behavior;
- choosing a command path changes a runtime-facing workflow contract;
- choosing `AGENTS.md`, `CLAUDE.md`, or both changes instruction authority semantics;
- source-only evidence is insufficient if behavior changes materialized runtime output.

## Objective

Resolve the instruction generator owner and command contract before changing instruction-file parity behavior.

The previous plan found that `new-project.md` claims to generate `$INSTRUCTION_FILE` through:

```bash
gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"
```

but the installed SDK handler ignores `--output` and returns JSON sections. The installed CJS command:

```bash
node .../get-shit-done/bin/gsd-tools.cjs generate-claude-md --output <path>
```

does write a file, but its template is documented as a `CLAUDE.md` generator.

This plan must produce a reviewable answer to:

1. who owns the generator contract;
2. what command initialization should call;
3. which instruction file or files should be generated;
4. what tests prove the command writes what the workflow claims.

## Required Deliverables

Create these plan-local artifacts before source behavior edits:

- `evidence/generator-command-map.md`
- `evidence/template-and-body-semantics.md`
- `evidence/runtime-path-contract.md`
- `evidence/decision.md`

If implementation proceeds, also create:

- `evidence/implementation-disposition.md`

Each evidence file must distinguish observed facts from inference.

## Pivotal Decisions Reserved To The Primary Operator

Agents or delegated reviewers may gather evidence, check claims, and propose options. They must not make or silently settle any load-bearing decision.

The primary operator must decide these points in `evidence/decision.md`:

1. Generator owner:
   - repo-owned wrapper
   - upstream SDK fix
   - direct CJS command
   - generated companion contract
2. Generated target policy:
   - `AGENTS.md` only
   - `CLAUDE.md` only for non-Codex
   - both files
   - defer all generation changes
3. Body semantics:
   - whether the existing `CLAUDE.md` template can honestly be used for `AGENTS.md`
   - whether a runtime-neutral template is required
4. Command path:
   - SDK query
   - materialized CJS path
   - repo-local wrapper path
   - upstream-only route
5. Conflict policy:
   - create-only
   - marker-section refresh
   - overwrite allowed only inside GSD markers
   - never overwrite without explicit user approval
6. Verification boundary:
   - source-only proof is enough
   - materialized runtime proof is required
   - host matrix proof is required
7. Catalog semantics:
   - `CLAUDE.md` remains tracked-only
   - `CLAUDE.md` becomes generated companion
   - catalog change deferred

If any of these remain undecided, implementation must stop at evidence and decision notes. Do not let an implementation worker, explorer, test failure, or convenient code path decide by default.

## Delegation Rules

Delegation is optional and evidence-only unless the user explicitly authorizes implementation delegation after `evidence/decision.md` exists.

Allowed delegated tasks before the decision:

- inspect installed SDK/CJS command behavior and report exact command outputs;
- inspect template body semantics and identify runtime-specific language;
- inspect manifest/materialization command paths and report whether shared workflows map to Codex, Claude, or both;
- review the decision artifact for missing evidence or unsupported inference.

Delegated agents must return one of:

- `evidence-only: no recommendation`
- `recommendation: non-binding`
- `blocker: evidence missing or contradictory`

Delegated agents must not:

- edit `new-project.md`;
- edit `carrier_catalog.json`;
- edit `OVERLAY-MANIFEST.json`;
- edit setup or contract scripts;
- choose the target file policy;
- choose the command path;
- claim materialized parity without running the materialized checks.

## Non-Goals

- Do not broaden compact-prompt capability behavior.
- Do not seed broader project-governance artifacts.
- Do not change host matrix semantics or broader support language.
- Do not remove `CLAUDE.md` or `.planning/CLAUDE.md` from the uplift carrier catalog unless `evidence/decision.md` explicitly proves that catalog semantics must change.
- Do not hand-edit generated `.codex/` or `.claude/` runtime output.
- Do not silently fix only the filename while leaving the command unwritten or untested.

## Worktree Protocol

Before edits:

```bash
git status --short --branch
git rev-parse --short HEAD
git branch --show-current
```

If the worktree is dirty with unrelated changes, stop and bucket or ask before editing.

Do not run install/materialization until the decision requires runtime-facing verification.

## Phase 1: Evidence

Write `evidence/generator-command-map.md`.

Required observations:

- repo overlay `new-project.md` generator command and `INSTRUCTION_FILE` policy;
- installed upstream `new-project.md` generator command and `INSTRUCTION_FILE` policy;
- `gsd-sdk` executable path and package source path;
- SDK registry entry for `generate-claude-md`;
- SDK handler behavior with and without `--output`;
- CJS `gsd-tools.cjs generate-claude-md --output` behavior;
- whether repo-owned overlay code currently provides a generator wrapper.

Write `evidence/template-and-body-semantics.md`.

Required observations:

- source of the file-writing template;
- marker sections generated by the CJS command;
- whether the generated body says Claude-specific things, runtime-neutral things, or mixed things;
- whether using that body as `AGENTS.md` would be semantically honest;
- whether a runtime-neutral template exists in this repo or upstream package.

Write `evidence/runtime-path-contract.md`.

Required observations:

- how shared workflows currently call CJS tools from materialized Codex paths;
- whether equivalent Claude materialized paths exist after setup;
- whether `new-project.md` is mapped to Codex, Claude, or both by `OVERLAY-MANIFEST.json`;
- whether a command path can be source-valid before runtime roots exist;
- what materialized checks are required if the workflow command changes.

## Phase 2: Decision

Write `evidence/decision.md` before source edits.

The decision must select exactly one option:

### Option A: Repo-Owned Runtime-Neutral Wrapper

Create or expose a modifier-owned wrapper that writes the chosen instruction file and hides upstream command differences.

Required decision proof:

- why repo ownership is safer than direct upstream/CJS calls;
- exact wrapper path;
- exact command contract;
- target file policy;
- tests that prove file write behavior.

### Option B: Upstream SDK Contract Defect

Defer repo behavior changes and record that the fix belongs in upstream `gsd-sdk query generate-claude-md`.

Required decision proof:

- why local overlay edits would mask the defect;
- where the upstream defect is observed;
- what local guard prevents future agents from assuming generation works;
- whether compact-prompt work can proceed while this remains open.

### Option C: CJS Command Path Correction

Update `new-project.md` to call the installed file-writing CJS generator directly, with a runtime-safe command path and tests.

Required decision proof:

- the command path is valid for every runtime the workflow materializes into;
- generated body semantics are acceptable for the chosen target file;
- existing-file conflict behavior is known;
- materialized checks are planned.

### Option D: Generated Companion Contract

Generate `AGENTS.md` plus runtime-native companion instructions with explicit conflict/update policy.

Required decision proof:

- why single-file generation cannot meet the accepted authority model;
- which file is governing for Codex;
- which file is governing for Claude;
- whether companion files are generated, mirrored, or tracked-only;
- how conflicts are resolved when both files already exist.

## Phase 3: Implementation Tail

Only implement the write set authorized by `evidence/decision.md`.

Allowed write sets by option:

- Option A:
  - generator wrapper source or script named in the decision;
  - `new-project.md`;
  - focused tests proving write behavior;
  - adjacent docs only if they carry the command contract.
- Option B:
  - evidence and planning docs only;
  - focused guard test or docs note that prevents false claims about the SDK command.
- Option C:
  - `new-project.md`;
  - focused tests under `tooling/codex/tests/`;
  - adjacent docs only if command-path semantics change.
- Option D:
  - `new-project.md`;
  - target-file conflict/update policy docs;
  - focused tests;
  - carrier catalog only if generated/tracked semantics change.

If a needed write is outside the selected write set, stop and revise the decision artifact before editing.

## Pitfalls And Mitigations

| Pitfall | Why it matters | Mitigation |
| --- | --- | --- |
| Treating `generate-claude-md` name as proof that Claude needs `CLAUDE.md` | Naming can be stale or historical; target-file policy needs authority evidence. | Require template/body semantics evidence and consumer authority evidence before choosing target files. |
| Treating current all-`AGENTS.md` behavior as proof it is correct | The modifier overlay changed upstream behavior, but the rationale is not yet fully recorded. | Require the decision artifact to justify single-file generation from consumers and onboarding docs. |
| Fixing the filename but leaving the command non-writing | The current SDK command can return success without writing the file. | Add a guard test or probe that proves the selected command creates or updates the target file. |
| Calling CJS from a Codex-only path inside a shared workflow | Shared workflows may materialize into Claude too. | Runtime-path evidence must prove the command path works for each materialized runtime or route through a repo-owned wrapper. |
| Using a `CLAUDE.md` body as `AGENTS.md` without semantic review | The generated file may contain Claude-specific assumptions. | Template evidence must classify each generated section as runtime-neutral, Claude-specific, or unsafe for `AGENTS.md`. |
| Removing `CLAUDE.md` from uplift tracking because Codex does not govern from it | Tracked doctrine carrier is not the same as Codex authority. | Catalog changes are allowed only if the decision proves generated/tracked semantics changed. |
| Letting tests define product semantics | A passing test can lock the wrong contract if the decision is under-specified. | Write the decision first; tests must encode the named contract, not discover it. |
| Claiming source validation as runtime parity | Source checks do not prove materialized runtime roots. | If workflow behavior changes, run setup plus strict materialized verification before claiming runtime parity. |
| Hiding upstream defects behind local overlay workarounds | A local workaround may make this repo pass while upstream workflows remain broken. | Option B must remain available; if local work is a workaround, record that boundary explicitly. |
| Expanding into compact prompt or governance seeding | This task sits before those workstreams and can easily absorb them. | Keep compact-prompt and governance artifacts out of scope unless a decision artifact records a direct dependency. |

## Auditability Requirements

Before closeout, write `evidence/implementation-disposition.md` if any source behavior changes.

It must record:

- selected option;
- files changed;
- why each changed file belongs in the write set;
- tests run;
- materialized-runtime status;
- intentionally held surfaces;
- remaining risks.

If no behavior changes, the decision artifact must explicitly say implementation was deferred and name the next owner.

## Verification

Minimum docs/evidence checks:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .planning/implementation-plans/20260424T082720Z
```

If workflow or tests change:

```bash
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest tooling.codex.tests.test_initialization_read_packet_contract
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
git diff --check
```

If runtime-facing workflow behavior changes:

```bash
./scripts/setup-portable-gsd-runtime.sh --runtime both
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict
python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict
```

Do not claim materialized parity unless the materialized checks were run.

## Commit Protocol

Use separate commits when both evidence and behavior changes occur:

1. `docs(planning): decide instruction generator contract`
   - evidence files;
   - decision artifact;
   - registry updates if needed.
2. Optional behavior commit named for the selected option, for example:
   - `fix(instructions): route initialization to file-writing generator`
   - `feat(instructions): add runtime-neutral instruction generator`
   - `test(instructions): guard instruction generator command contract`

Commit bodies must include:

- `Why:`
- `Verification:`
- `Boundary:`

## Closeout

Closeout must record:

- chosen task classification;
- chosen generator owner;
- chosen target file policy;
- exact command contract;
- verification commands and results;
- whether runtime-facing files changed;
- whether materialized-runtime checks were required and run;
- whether compact-prompt work can proceed next.
