---
name: gsd:uplift-project
description: Detect repo-local project uplift posture and optionally write durable uplift memory
argument-hint: "[--write]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---
<objective>
Detect repo-local project uplift posture and, when explicitly requested, write a bounded detect-only uplift record.
</objective>

<execution_context>
@__PROJECT_ROOT__/.claude/get-shit-done/workflows/uplift-project.md
</execution_context>

<process>
Execute the uplift-project workflow from @__PROJECT_ROOT__/.claude/get-shit-done/workflows/uplift-project.md end-to-end.

Default posture is detect-only.
Pass `--write` only when the caller explicitly wants durable uplift memory written.
If the workflow reports compatibility-basis movement, prefer rerunning with `--write` so the durable uplift memory and routed note stay in tune.
If doctrine-sensitive proposals remain and the operator wants one bounded assist-family packet before governance or durable uplift edits, keep that route operator-initiated and follow the workflow's route block rather than inventing a helper path here.
</process>
