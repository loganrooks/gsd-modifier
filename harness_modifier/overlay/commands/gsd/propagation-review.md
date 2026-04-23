---
name: gsd:propagation-review
description: Run a bounded propagation review for a concrete contract-changing slice across baseline, delta, and current carrier layers
argument-hint: "[target] [--write-note PATH] [--strict-runtime]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---
<objective>
Review one concrete contract-changing slice against the upstream-pristine baseline, the repo-local delta layer, and the current propagation family so neighboring carriers either move in the same batch or stay explicitly held.
</objective>

<execution_context>
@__PROJECT_ROOT__/.claude/get-shit-done/workflows/propagation-review.md
</execution_context>

<process>
Execute the propagation-review workflow from @__PROJECT_ROOT__/.claude/get-shit-done/workflows/propagation-review.md end-to-end.

Default posture is read-only.
Use `--write-note PATH` only when the caller explicitly wants a durable propagation review note.
Use `--strict-runtime` when the changed slice touches live runtime, overlay/materialization, or registry carriers and the review should include the bounded runtime/install gate packet.
</process>
