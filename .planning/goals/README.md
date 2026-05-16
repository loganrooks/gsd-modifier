# Goal Prompts Registry

This directory stores `/goal` prompt strings used in this repo (Claude Code and Codex CLI). Each file is a complete, paste-ready `/goal` command for a specific workstream on a specific runtime.

Default file (`<workstream>.md`) is the Claude Code variant. Per-runtime siblings use a `-<runtime>` suffix (e.g., `<workstream>-codex.md`). Initiative governance under `.planning/initiatives/<workstream>/` is runtime-neutral and shared across siblings.

## Why

`/goal` prompts can be long and load-bearing (they encode the entire turn-by-turn discipline an autonomous loop must follow). Keeping them version-controlled here means:

- The exact prompt that drove a workstream is reconstructable from `git log`
- Refining the prompt is a normal review-able diff, not a chat artifact
- The operator can grep / open / copy from one canonical location instead of hunting through workstream-specific docs
- New workstreams can crib structure from existing ones

## Convention

- **One file per workstream**: `<workstream-slug>.md` (kebab-case matching the workstream's home directory under `.planning/`)
- **File header**: short context — what workstream, expected starting state, what conditions terminate the goal
- **The `/goal` block**: in a fenced code block, ready to copy-paste verbatim (the first line begins with `/goal `)
- **Cross-references**: link to the workstream's PROTOCOL / GUARDRAILS / STATE / phase plans so the operator can find them in one hop

The `/goal` block in this directory is the **single source of truth** for the prompt. If a workstream's own docs (e.g., `LOOP-PROMPT.md`) reference the prompt, they point here rather than duplicating it.

## How to use

1. Open the file for your workstream + runtime
2. Copy the `/goal` block (inside the fenced code block)
3. Paste into a fresh Claude Code session (v2.1.139+) or Codex CLI session at the repo root
4. Hit enter

The loop will fire turns automatically until the goal condition is met or a hard-stop terminates the goal. Check status anytime by running `/goal` (no args) on either runtime.

Codex variants require reviewer TOMLs under `.codex/agents/` to exist locally before invocation — see the variant file's Prerequisites section.

## Current goals

| Goal | Workstream | Runtime | Status |
|---|---|---|---|
| [`inject-migration.md`](inject-migration.md) | [Inject migration initiative](../initiatives/inject-migration/INITIATIVE.md) — overlay model migration from overwrite-heavy to surgical injection | Claude Code | Phase 2 complete; awaiting Phase 3 operator gate |
| [`inject-migration-codex.md`](inject-migration-codex.md) | Same initiative, Codex CLI sibling | Codex CLI | Same state (shared STATE.md) |

## Adding a new goal

1. Create `.planning/goals/<slug>.md` following the structure of an existing entry
2. Compose the `/goal` block with: completion condition, per-turn agent obligations, discipline constraints, runaway safety cap
3. If the workstream has its own operator-surface doc (a `LOOP-PROMPT.md` or similar), update it to point here for the canonical block
4. Add a row to "Current goals" above
5. Commit with subject `feat(planning): add <slug> goal` or equivalent

## Discipline notes

- **Keep `/goal` blocks parseable by an evaluator.** The completion condition must be ground-able from agent transcript output alone (the `/goal` evaluator does not call tools). Conditions like "STATE.md sentinel reads X" only work if the agent **echoes** the sentinel line in transcript output each turn.
- **Include a turn cap.** A `or stop after N turns` clause is the runaway safety floor. Without it, a misbehaving loop could spend tokens indefinitely.
- **Include forbidden-action / hard-stop semantics in the prompt.** The agent reads the prompt every turn; if hard-stop discipline isn't reinforced there, the agent may infer that running through stops is acceptable.
