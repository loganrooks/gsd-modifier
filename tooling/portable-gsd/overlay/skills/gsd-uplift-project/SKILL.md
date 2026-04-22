---
name: "gsd-uplift-project"
description: "Detect repo-local project uplift posture and optionally write durable uplift memory"
metadata:
  short-description: "Detect repo-local project uplift posture and optionally write durable uplift memory"
---

<codex_skill_adapter>
## A. Skill Invocation
- This skill is invoked by mentioning `$gsd-uplift-project`.
- Treat all user text after `$gsd-uplift-project` as `{{GSD_ARGS}}`.
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
Detect repo-local project uplift posture and, when explicitly requested, write a bounded detect-only uplift record (`UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, `STATE.md` uplift section).
</objective>

<execution_context>
@/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/uplift-project.md
</execution_context>

<process>
Execute the uplift-project workflow from @/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/uplift-project.md end-to-end.

Default posture is detect-only.
Pass `--write` only when the caller explicitly wants durable uplift memory written.
If the workflow reports runtime-basis movement, prefer rerunning with `--write` so the durable uplift memory and live routed note stay in tune.
If the workflow surfaces legacy-unversioned or noncurrent seed posture, keep migration separate but prefer `--write` once the operator wants that posture preserved in durable uplift memory too.
</process>
