# Phase Prompt Template

> **Note:** Planning methodology is in `agents/gsd-planner.md`.
> This overlay copy preserves the repo-local PLAN artifact contract, including `future_preservation`.

Template for `.planning/phases/XX-name/{phase}-{plan}-PLAN.md` - executable phase plans optimized for parallel execution.

**Naming:** Use `{phase}-{plan}-PLAN.md` format (for example `01-02-PLAN.md` for Phase 1, Plan 2).

---

## File Template

```markdown
---
phase: XX-name
plan: NN
type: execute
wave: N
depends_on: []
files_modified: []
autonomous: true
requirements: []
user_setup: []
future_preservation:
  protected_seams: []
  non_decisions: []
  posture_assumptions: []

must_haves:
  truths: []
  artifacts: []
  key_links: []
---

<objective>
[What this plan accomplishes]

Purpose: [Why this matters for the project]
Output: [What artifacts will be created]
</objective>

<execution_context>
@__PROJECT_ROOT__/.codex/get-shit-done/workflows/execute-plan.md
@__PROJECT_ROOT__/.codex/get-shit-done/templates/summary.md
[If plan contains checkpoint tasks (type="checkpoint:*"), add:]
@__PROJECT_ROOT__/.codex/get-shit-done/references/checkpoints.md
</execution_context>

<context>
@.planning/PROJECT.md
@.planning/ROADMAP.md
@.planning/STATE.md

# Only reference prior plan SUMMARYs if genuinely needed:
# - This plan uses types/exports from prior plan
# - Prior plan made decision that affects this plan
# - Prior plan's output is input to this plan

[Relevant source files:]
@src/path/to/relevant.ts
</context>

<tasks>

<task type="auto">
  <name>Task 1: [Action-oriented name]</name>
  <files>path/to/file.ext, another/file.ext</files>
  <read_first>path/to/reference.ext, path/to/source-of-truth.ext</read_first>
  <action>[Specific implementation with concrete identifiers, values, signatures, commands, and file paths.]</action>
  <verify>[Command or check to prove it worked]</verify>
  <acceptance_criteria>
    - [Grep-verifiable condition]
    - [Measurable condition]
  </acceptance_criteria>
  <done>[Measurable acceptance criteria]</done>
</task>

<task type="auto">
  <name>Task 2: [Action-oriented name]</name>
  <files>path/to/file.ext</files>
  <read_first>path/to/reference.ext</read_first>
  <action>[Specific implementation with concrete values]</action>
  <verify>[Command or check]</verify>
  <acceptance_criteria>
    - [Grep-verifiable condition]
  </acceptance_criteria>
  <done>[Acceptance criteria]</done>
</task>

<task type="checkpoint:decision" gate="blocking">
  <decision>[What needs deciding]</decision>
  <context>[Why this decision matters]</context>
  <options>
    <option id="option-a"><name>[Name]</name><pros>[Benefits]</pros><cons>[Tradeoffs]</cons></option>
    <option id="option-b"><name>[Name]</name><pros>[Benefits]</pros><cons>[Tradeoffs]</cons></option>
  </options>
  <resume-signal>Select: option-a or option-b</resume-signal>
</task>

<task type="checkpoint:human-verify" gate="blocking">
  <what-built>[What the agent built] - server running at [URL]</what-built>
  <how-to-verify>Visit [URL] and verify: [visual checks only, NO CLI commands]</how-to-verify>
  <resume-signal>Type "approved" or describe issues</resume-signal>
</task>

</tasks>

<verification>
Before declaring plan complete:
- [ ] [Specific test command]
- [ ] [Build/type check passes]
- [ ] [Behavior verification]
</verification>

<success_criteria>
- All tasks completed
- All verification checks pass
- No errors or warnings introduced
- [Plan-specific criteria]
</success_criteria>

<output>
After completion, create `.planning/phases/XX-name/{phase}-{plan}-SUMMARY.md`
</output>
```

---

## Frontmatter Fields

| Field | Required | Purpose |
|-------|----------|---------|
| `phase` | Yes | Phase identifier (for example `01-foundation`) |
| `plan` | Yes | Plan number within phase (for example `01`, `02`) |
| `type` | Yes | Usually `execute`; use another value only when the workflow explicitly requires it |
| `wave` | Yes | Execution wave number assigned during planning |
| `depends_on` | Yes | Array of plan IDs this plan requires |
| `files_modified` | Yes | Files this plan touches |
| `autonomous` | Yes | `true` if no checkpoints, `false` if the plan includes blocking checkpoints |
| `requirements` | Yes | Requirement IDs from ROADMAP covered by this plan |
| `user_setup` | No | Human-required setup the agent cannot automate |
| `future_preservation` | Yes when CONTEXT future-awareness is non-empty | Structured record of preserved seams, explicit non-decisions, and posture assumptions carried forward from planning |
| `must_haves` | Yes | Goal-backward verification criteria |

**Wave is pre-computed:** execute-phase reads `wave` directly from frontmatter and groups plans by wave number.

**Future-preservation keeps planning intent reviewable:** when `CONTEXT.md` carries future-awareness, planners should capture the protected seams they preserved, the choices they intentionally left open, and the posture assumptions they relied on. This makes later review and replanning auditable.

---

## Context Rules

- Always include `.planning/PROJECT.md`, `.planning/ROADMAP.md`, and `.planning/STATE.md`.
- Include `CONTEXT.md`, `RESEARCH.md`, or prior `SUMMARY.md` files only when they materially affect this plan.
- Do not create false dependencies by reflexively chaining every plan to earlier summaries.

---

## Task Rules

- Every task must have a concrete `<read_first>` list.
- Every `<action>` must include exact identifiers, values, signatures, commands, or file paths.
- Every `<acceptance_criteria>` item must be verifiable by reading a file, running a command, or observing an exact output.
- If the phase steering brief includes future-awareness, the plan body and frontmatter should both reflect how that future-aware item was preserved or intentionally deferred.

---

## Parallelization Notes

- Independent subsystems with disjoint file ownership should land in the same wave.
- Genuine type, runtime, or artifact dependencies should move later work to a higher wave.
- Checkpoint plans should set `autonomous: false`.

---

## Output Standard

Plans should be specific enough that an execution agent can work from the plan text itself rather than rediscovering the intended target state from scratch.
