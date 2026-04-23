---
name: gsd:seed-migration-inventory
description: Inventory legacy or drifted seed corpora and optionally write a bounded migration-planning packet
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
Produce a detect-only inventory for legacy or drifted seed corpora and, when explicitly requested, write a compact migration-planning packet.
</objective>

<execution_context>
@__PROJECT_ROOT__/.claude/get-shit-done/workflows/seed-migration-inventory.md
</execution_context>

<process>
Execute the seed-migration-inventory workflow from @__PROJECT_ROOT__/.claude/get-shit-done/workflows/seed-migration-inventory.md end-to-end.

Default posture is detect-only.
Use `--write` only when the caller explicitly wants durable migration-planning memory.
Keep direct seed rewrites or normalization separate from this workflow; the first slice remains a detect-only inventory.
</process>
