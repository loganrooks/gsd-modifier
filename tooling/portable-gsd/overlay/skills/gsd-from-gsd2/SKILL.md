---
name: "gsd-from-gsd2"
description: "Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format"
metadata:
  short-description: "Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format"
---

<codex_skill_adapter>
## A. Skill Invocation
- This skill is invoked by mentioning `$gsd-from-gsd2`.
- Treat all user text after `$gsd-from-gsd2` as `{{GSD_ARGS}}`.
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
Reverse-migrate a GSD-2 project (`.gsd/` directory) back to GSD v1 (`.planning/`) format.

Maps the GSD-2 hierarchy (Milestone → Slice → Task) to the GSD v1 hierarchy (Milestone sections in ROADMAP.md → Phase → Plan), preserving completion state, research files, and summaries.

This skill owns format migration. It does not by itself install the broader repo-local runtime, governing-doc, or doctrine posture after migration.

**CJS-only:** `from-gsd2` is not on the `gsd-sdk query` registry; call `gsd-tools.cjs` as shown below (see `docs/CLI-TOOLS.md`).
</objective>

<process>

1. **Locate the .gsd/ directory** — check the current working directory (or `--path` argument):
   ```bash
   node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" from-gsd2 --dry-run
   ```
   If no `.gsd/` is found, report the error and stop.

2. **Show the dry-run preview** — present the full file list and migration statistics to the user. Ask for confirmation before writing anything.

3. **Run the migration** after confirmation:
   ```bash
   node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" from-gsd2
   ```
   Use `--force` if `.planning/` already exists and the user has confirmed overwrite.

4. **Run structural health validation** on the migrated `.planning/` tree:
   ```bash
   gsd-sdk query validate.health
   ```
   Report the structural health result alongside the migration output instead of assuming format conversion alone completes the project-entry job.

5. **Report the result** — show:
   - `filesWritten`
   - `planningDir`
   - the preview summary
   - the post-migration health status and any warnings

6. **Keep later uplift explicit** — if the migrated project should also inherit the current repo-local runtime, governing-doc, or doctrine posture, route separately to `$gsd-uplift-project --write` rather than treating format migration as the full project-uplift story.

</process>

<notes>
- The migration is non-destructive: `.gsd/` is never modified or removed.
- Pass `--path <dir>` to migrate a project at a different path than the current directory.
- Slices are numbered sequentially across all milestones (M001/S01 → phase 01, M001/S02 → phase 02, M002/S01 → phase 03, etc.).
- Tasks within each slice become plans (T01 → plan 01, T02 → plan 02, etc.).
- Completed slices and tasks carry their done state into ROADMAP.md checkboxes and SUMMARY.md files.
- GSD-2 cost/token ledger, database state, and VS Code extension state cannot be migrated.
</notes>
