# Immediate Implementation Plan

Date: 2026-04-24
Status: executable draft
Plan ID: `004-generator-owner-and-command-contract`

## Trace Links

- Package index: [../../README.md](../../README.md)
- Short-horizon program plan: [../../SHORT-HORIZON.md](../../SHORT-HORIZON.md)
- Prior decision: [../003-instruction-surface-generation-parity/evidence/decision.md](../003-instruction-surface-generation-parity/evidence/decision.md)
- Prior generation evidence: [../003-instruction-surface-generation-parity/evidence/current-generation-flow.md](../003-instruction-surface-generation-parity/evidence/current-generation-flow.md)
- Consumer authority map: [../003-instruction-surface-generation-parity/evidence/consumer-authority-map.md](../003-instruction-surface-generation-parity/evidence/consumer-authority-map.md)
- Runtime intervention inventory: [../../../../../docs/runtime-intervention-surfaces.md](../../../../../docs/runtime-intervention-surfaces.md)
- Governing handoff: [../../../../../docs/handoff/current.md](../../../../../docs/handoff/current.md)
- Repo instructions: [../../../../../AGENTS.md](../../../../../AGENTS.md)

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

This plan decides and implements the smallest safe command/generator contract so initialization either writes the file it claims to write or explicitly routes the missing generator to upstream/follow-up.

## Non-Goals

- Do not broaden compact-prompt capability behavior.
- Do not seed broader project-governance artifacts.
- Do not change host matrix semantics or broader support language.
- Do not remove `CLAUDE.md` or `.planning/CLAUDE.md` from the uplift carrier catalog unless the generator decision explicitly proves that catalog semantics must change.
- Do not hand-edit generated `.codex/` or `.claude/` runtime output.

## Required Questions

1. Is the file-writing generator this repo should call the installed CJS command, a new repo-owned wrapper, or a fixed SDK query handler?
2. If the repo calls CJS directly, what command path works from both Codex and Claude materialized workflows?
3. Is the generated body acceptable for `AGENTS.md`, or does `AGENTS.md` need a runtime-neutral generator/template?
4. Should non-Codex host initialization generate `CLAUDE.md`, `AGENTS.md`, or both?
5. What happens when an instruction file already exists?
6. Which test proves the command actually writes the claimed file?

## Candidate Outcomes

### Option A: Repo-Owned Runtime-Neutral Wrapper

Create or expose a modifier-owned wrapper that writes the chosen instruction file and hides upstream command differences.

Use when the safest intervention is to own a stable command contract in this repo without changing upstream SDK internals.

### Option B: SDK Handler Fix Routed Upstream

Defer repo behavior changes and record that the real fix belongs in upstream `gsd-sdk query generate-claude-md`.

Use when local overlay changes would mask an upstream command contract defect.

### Option C: CJS Command Path Correction

Update `new-project.md` to call the installed file-writing CJS generator directly, with a runtime-safe command path and tests.

Use only if the generated body semantics and runtime path are acceptable for both target runtimes.

### Option D: Generated Companion Contract

Generate `AGENTS.md` plus runtime-native companion instructions with explicit conflict/update policy.

Use only if evidence shows a single generated instruction file cannot support the accepted Codex/Claude host behavior.

## Worktree Protocol

Before edits:

```bash
git status --short --branch
git rev-parse --short HEAD
git branch --show-current
```

Do not run install/materialization until the decision requires runtime-facing verification.

## Execution Steps

1. Re-read the prior 003 evidence and decision.
2. Trace all installed and repo-owned command paths for `generate-claude-md`.
3. Decide the generator owner and target file policy before source edits.
4. If editing behavior, update the workflow, adjacent docs, and focused tests together.
5. If deferring to upstream, write the upstream-boundary artifact and add a contract test or docs note that prevents silent reclassification.
6. Run source verification for docs/tests changes.
7. Run materialized verification if runtime-facing workflow behavior changes.

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

## Closeout

Closeout must record:

- chosen generator owner
- chosen target file policy
- exact command contract
- verification run
- materialized-runtime status
- whether compact-prompt work can proceed next
