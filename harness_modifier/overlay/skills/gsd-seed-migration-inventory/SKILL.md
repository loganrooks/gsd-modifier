---
name: "gsd-seed-migration-inventory"
description: "Inventory legacy or drifted seed corpora and optionally write a bounded migration-planning packet"
metadata:
  short-description: "Inventory legacy or drifted seed corpora and optionally write a bounded migration-planning packet"
---

<codex_skill_adapter>
## A. Skill Invocation
- This skill is invoked by mentioning `$gsd-seed-migration-inventory`.
- Treat all user text after `$gsd-seed-migration-inventory` as `{{GSD_ARGS}}`.
- If no arguments are present, treat `{{GSD_ARGS}}` as empty.

## B. AskUserQuestion → request_user_input Mapping
GSD workflows use `AskUserQuestion` (Claude Code syntax). Translate to Codex `request_user_input`:

Parameter mapping:
- `header` → `header`
- `question` → `question`
- Options formatted as `"Label" — description` → `{label: "Label", description: "description"}`
- Generate `id` from header: lowercase, replace spaces with underscores

Batched calls:
- `AskUserQuestion([q1, q2])` → single `request_user_input` with multiple entries in `questions[]`

Multi-select workaround:
- Codex has no `multiSelect`. Use sequential single-selects, or present a numbered freeform list asking the user to enter comma-separated numbers.

Execute mode fallback:
- When `request_user_input` is rejected (Execute mode), present a plain-text numbered list and pick a reasonable default.

## C. Task() → spawn_agent Mapping
GSD workflows use `Task(...)` (Claude Code syntax). Translate to Codex collaboration tools:

Direct mapping:
- `Task(subagent_type="X", prompt="Y")` → `spawn_agent(agent_type="X", message="Y")`
- `Task(model="...")` → omit (Codex uses per-role config, not inline model selection)
- `fork_context: false` by default — GSD agents load their own context via `<files_to_read>` blocks

Parallel fan-out:
- Spawn multiple agents → collect agent IDs → `wait(ids)` for all to complete

Result parsing:
- Look for structured markers in agent output: `CHECKPOINT`, `PLAN COMPLETE`, `SUMMARY`, etc.
- `close_agent(id)` after collecting results from each agent
</codex_skill_adapter>

<objective>
Produce a detect-only inventory for legacy or drifted seed corpora and, when explicitly requested, write `.planning/SEED-MIGRATION-REPORT.md` plus `.planning/SEED-MIGRATION-MANIFEST.json` as a compact migration-planning packet.
</objective>

<execution_context>
@__PROJECT_ROOT__/.codex/get-shit-done/workflows/seed-migration-inventory.md
</execution_context>

<process>
Execute the seed-migration-inventory workflow from @__PROJECT_ROOT__/.codex/get-shit-done/workflows/seed-migration-inventory.md end-to-end.

Default posture is detect-only.
Point operators at `$gsd-seed-migration-inventory` when they want the deeper detect-only packet.
Point operators at `$gsd-seed-migration-inventory --write` only when they explicitly want durable migration-planning memory.
Keep direct seed rewrites or normalization separate from this workflow; the first slice is a detect-only inventory.
</process>
