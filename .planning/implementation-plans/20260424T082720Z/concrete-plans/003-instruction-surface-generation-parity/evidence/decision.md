# Instruction Surface Generation Parity Decision

Date: 2026-04-24
Plan: `003-instruction-surface-generation-parity`
Decision: Option C - Defer Behavior, Add Contract Coverage

## Decision

Do not change instruction generation behavior in this slice.

Record the current posture and the generator mismatch as evidence, then route the next implementation to a sharper generator-owner plan before changing `new-project.md`, `carrier_catalog.json`, the overlay manifest, or materialized runtime behavior.

## Why This Option

This plan set out to choose among:

- Option A: single generated `AGENTS.md`
- Option B: generated runtime companion
- Option C: defer behavior and add contract coverage

The evidence does not yet support a safe Option A or Option B implementation.

Observed facts:

- The modifier overlay currently sets `INSTRUCTION_FILE="AGENTS.md"` for every runtime.
- Installed upstream GSD still sets `AGENTS.md` for Codex and `CLAUDE.md` otherwise.
- Both the modifier overlay and installed upstream workflow call `gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"`.
- The installed SDK `generate-claude-md` handler ignores `--output` and returns JSON sections instead of writing a file.
- The installed CJS `gsd-tools.cjs generate-claude-md --output ...` command does write a marker-bounded file.
- The CJS template is explicitly documented as a project-root `CLAUDE.md` template.
- This linked worktree has no materialized `.codex/` or `.claude/` roots, so no live runtime output was observed.

Inference:

- The current workflow has a real generation-command mismatch.
- The all-`AGENTS.md` filename policy may still be the right modifier posture, but the repo does not yet own or document a runtime-neutral `AGENTS.md` generator body.
- Switching to the CJS generator in this slice would silently choose both a command-path policy and a body semantics policy that this plan has not proved.

## Rejected Alternatives

### Rejected: Option A In This Slice

Single generated `AGENTS.md` remains plausible and may still be the preferred direction for this repo.

It is not implemented now because:

- the available real writer is named and templated as `generate-claude-md`;
- the installed SDK command currently does not write the requested file;
- no repo-owned `AGENTS.md` generator body or wrapper was found;
- a runtime-root-safe CJS command path for workflows mapped to both Codex and Claude is not settled here.

### Rejected: Option B In This Slice

Generating both `AGENTS.md` and a Claude companion may be valid for host projects, especially because installed upstream GSD still defaults non-Codex runtimes to `CLAUDE.md`.

It is not implemented now because:

- this repo's live Claude onboarding starts from `AGENTS.md`;
- Codex agents explicitly reject `CLAUDE.md` as governing truth;
- adding a companion would require conflict/update rules for two generated files;
- uplift carrier semantics would need to distinguish generated companion from tracked doctrine carrier;
- materialized runtime behavior would need verification after changing the workflow.

### Rejected: Remove `CLAUDE.md` Catalog Carriers

Do not remove `CLAUDE.md` or `.planning/CLAUDE.md` from `harness_modifier/uplift/carrier_catalog.json`.

Reason:

- Codex non-authority is not the same as irrelevant doctrine.
- The catalog can validly track Claude-facing doctrine as drift-sensitive even when Codex agents do not govern themselves from it.

## Conflict And Update Policy For Now

Until the follow-up generator-owner plan lands:

- Treat `AGENTS.md` as the governing project instruction surface for this repo and for Codex agents.
- Treat `.planning/AGENTS.md` as governing when present and in scope for planning artifacts.
- Treat `CLAUDE.md` and `.planning/CLAUDE.md` as tracked doctrine carriers, not Codex authority.
- Do not claim that `new-project.md` currently performs a verified project instruction file write through `gsd-sdk query generate-claude-md --output`.
- Do not claim materialized runtime parity for instruction generation from this slice.

## Verification Required For This Slice

Because this slice records evidence and defers behavior:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .planning/implementation-plans/20260424T082720Z
```

If package-level planning docs are edited, the same refmap scope covers them.

Materialized runtime checks are not required for this decision-only slice because no runtime-facing overlay behavior is changed.

## Follow-Up Plan

Create the next concrete plan before `004-compact-prompt-runtime-capability-contract` unless the user explicitly chooses to skip it:

```text
004-generator-owner-and-command-contract
```

Minimum questions for that follow-up:

- Should `gsd-modifier` own a runtime-neutral `AGENTS.md` generator wrapper?
- Should the installed SDK handler be fixed upstream to honor `--output`, or should workflows call the CJS writer directly?
- If workflows call CJS directly, what runtime-root path works for both Codex and Claude materialization?
- Should host projects get only `AGENTS.md`, only runtime-native instruction files, or both?
- What exact conflict policy applies when `AGENTS.md` and `CLAUDE.md` already exist?
- Which tests should prove the command writes the file it says it writes?

## Boundary

No source workflow, carrier catalog, manifest, setup, or materialized runtime files were intentionally changed by this decision.

The `/tmp` generator probes are disposable evidence and are not repo artifacts.
