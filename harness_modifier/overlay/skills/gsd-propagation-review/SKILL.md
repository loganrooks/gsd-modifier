---
name: "gsd-propagation-review"
description: "Run a bounded propagation review for a concrete contract-changing slice across baseline, delta, and current carrier layers"
metadata:
  short-description: "Bounded propagation review for multi-family contract changes"
---

<codex_skill_adapter>
## A. Skill Invocation
- This skill is invoked by mentioning `$gsd-propagation-review`.
- Treat all user text after `$gsd-propagation-review` as `{{GSD_ARGS}}`.
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
Review one concrete contract-changing slice against the upstream-pristine baseline, the repo-local delta layer, and the current propagation family so neighboring carriers either move in the same batch or stay explicitly held.
</objective>

<execution_context>
@__PROJECT_ROOT__/.codex/get-shit-done/workflows/propagation-review.md
</execution_context>

<process>
Execute the propagation-review workflow from @__PROJECT_ROOT__/.codex/get-shit-done/workflows/propagation-review.md end-to-end.

Default posture is read-only.
Use `--write-note PATH` only when the caller explicitly wants a durable propagation review note.
Use `--strict-runtime` when the changed slice touches live runtime, overlay/materialization, or registry carriers and the review should include the bounded runtime/install gate packet.

When a durable note is requested, prefer an existing lane home over a new ad hoc path:
- `outputs/` for preserved external/model returns or transparent composites of one
- `dispositions/` for local inheritance or judgment
- `*-change-triggered-refresh.md` when the note itself becomes a new propagation-baseline carrier

If the note lands inside this audit workspace, preserve the local claim-type grammar rather than dropping into untyped prose.

Keep the route hybrid:
- baseline/delta docs and the typed registry guide the review
- tooling sharpens visibility where it fits
- contextual reread and explicit disposition stay sovereign

If the review surfaces project-uplift posture movement, route separately to `$gsd-uplift-project --write`.
If it surfaces older or drifted seed posture that deserves the deeper specialist packet, route separately to `$gsd-seed-migration-inventory` or `$gsd-seed-migration-inventory --write`.
</process>
