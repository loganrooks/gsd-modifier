<purpose>
Check project progress, summarize recent work and what's ahead, then intelligently route to the next action — either executing an existing plan or creating the next one. Provides situational awareness before continuing work.
</purpose>

<required_reading>
@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<supporting_reading>
Prefer the route-local surfaces this workflow already computes before widening:
- `roadmap analyze`
- `state-snapshot`
- recent `SUMMARY.md` one-liners
- `.planning/UPLIFT-MANIFEST.json` only when the uplift note says it should surface
</supporting_reading>

<deeper_reading>
Only widen into broader family or governance docs when the active route, anomaly, or user request points there. Do not reopen the full workspace just to report ordinary progress.
</deeper_reading>

<process>

<step name="init_context">
**Load progress context (paths only):**

```bash
INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" init progress)
if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
```

Extract from init JSON: `project_exists`, `roadmap_exists`, `state_exists`, `phases`, `current_phase`, `next_phase`, `milestone_version`, `completed_count`, `phase_count`, `paused_at`, `state_path`, `roadmap_path`, `project_path`, `config_path`.

```bash
DISCUSS_MODE=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" config-get workflow.discuss_mode 2>/dev/null || echo "discuss")
```

If `project_exists` is false (no `.planning/` directory):

```
No planning structure found.

Run $gsd-new-project to start a new project.
```

Exit.

If missing STATE.md: suggest `$gsd-new-project`.

**If ROADMAP.md missing but PROJECT.md exists:**

This means a milestone was completed and archived. Go to **Route F** (between milestones).

If missing both ROADMAP.md and PROJECT.md: suggest `$gsd-new-project`.
</step>

<step name="load">
**Use structured extraction from gsd-tools:**

Instead of reading full files, use targeted tools to get only the data needed for the report:
- `ROADMAP=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" roadmap analyze)`
- `STATE=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" state-snapshot)`

This minimizes orchestrator context usage.

Treat these structured outputs as the primary read packet for ordinary progress routing. Only widen into full project or family docs when a later route actually needs that depth.
</step>

<step name="analyze_roadmap">
**Get comprehensive roadmap analysis (replaces manual parsing):**

```bash
ROADMAP=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" roadmap analyze)
```

This returns structured JSON with:
- All phases with disk status (`complete`, `complete_with_debt`, `executed`, `partial`, `planned`, `empty`, `no_directory`)
- Goal and dependencies per phase
- Plan and summary counts per phase
- Completion metadata per phase (`completion_mode`, `debt_bearing`, `verification_status`, `completion_warnings`)
- Aggregated stats: total plans, summaries, progress percent
- Current and next phase identification

Use this instead of manually reading/parsing ROADMAP.md.
</step>

<step name="recent">
**Gather recent work context:**

- Find the 2-3 most recent SUMMARY.md files
- Use `summary-extract` for efficient parsing:
  ```bash
  node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" summary-extract <path> --fields one_liner
  ```
- This shows "what we've been working on"
  </step>

<step name="position">
**Parse current position from init context and roadmap analysis:**

- Use `current_phase` and `next_phase` from `$ROADMAP`
- Also load the current phase record from `$ROADMAP.phases[]` so you can read `disk_status`, `completion_mode`, and `completion_warnings`
- Note `paused_at` if work was paused (from `$STATE`)
- Count pending todos: use `init todos` or `list-todos`
- Check for active debug sessions: `(ls .planning/debug/*.md 2>/dev/null || true) | grep -v resolved | wc -l`
  </step>

<step name="report">
**Generate progress bar from gsd-tools, then present rich status report:**

```bash
# Get formatted progress bar
PROGRESS_BAR=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" progress bar --raw)
```

Present:

```
# [Project Name]

**Progress:** {PROGRESS_BAR}
**Profile:** [quality/balanced/budget/inherit]
**Discuss mode:** {DISCUSS_MODE}

## Recent Work
- [Phase X, Plan Y]: [what was accomplished - 1 line from summary-extract]
- [Phase X, Plan Z]: [what was accomplished - 1 line from summary-extract]

## Current Position
Phase [N] of [total]: [phase-name]
Plan [M] of [phase-total]: [status]
Execution State: [planned | partial | executed | complete_with_debt | complete]
CONTEXT: [✓ if has_context | - if not]

## Key Decisions Made
- [extract from $STATE.decisions[]]
- [e.g. jq -r '.decisions[].decision' from state-snapshot]

## Blockers/Concerns
- [extract from $STATE.blockers[]]
- [e.g. jq -r '.blockers[].text' from state-snapshot]

If any `$STATE.future_carry` bucket is non-empty, add:

```markdown
## Future Carry Forward
- Preserve: {comma-separated preserve items when present}
- Keep open: {comma-separated keep_open items when present}
- Posture: {comma-separated posture items when present}
- Seeded: {comma-separated seeded items when present}
```

Only show the lines whose buckets are non-empty.

## Pending Todos
- [count] pending — $gsd-check-todos to review

If `.planning/UPLIFT-MANIFEST.json` exists, or `.planning/` exists without any uplift manifest yet, load the uplift note:

```bash
UPLIFT_NOTE=$(python3 "__PROJECT_ROOT__/tooling/codex/project_uplift.py" progress-note "__PROJECT_ROOT__" --json 2>/dev/null || true)
```

When `UPLIFT_NOTE.show` is `true`, add:

```markdown
## Uplift Posture
- Last uplift class: {last_uplift_class or "none recorded yet"}
- Secondary signals: {last_uplift_secondary_signals or "none"}
- Recommendation: {recommendation}
- Reason: {reason 1}
- Reason: {reason 2}
- Report: `.planning/UPLIFT-REPORT.md`
- Manifest: `.planning/UPLIFT-MANIFEST.json`
```

## Active Debug Sessions
- [count] active — $gsd-debug to continue
(Only show this section if count > 0)

## What's Next
[Next phase/plan objective from roadmap analyze]
```

</step>

<step name="route">
**Determine next action based on verified counts.**

Before widening the read set, keep the route narrow:
- ordinary progress output should stay on the structured packet plus the phase-local files surfaced below
- if a route points into one family such as uplift, verification debt, or milestone-open planning, reread that family deliberately rather than loading unrelated workspace history

**Step 1: Count plans, summaries, and issues in current phase**

List files in the current phase directory:

```bash
(ls -1 .planning/phases/[current-phase-dir]/*-PLAN.md 2>/dev/null || true) | wc -l
(ls -1 .planning/phases/[current-phase-dir]/*-SUMMARY.md 2>/dev/null || true) | wc -l
(ls -1 .planning/phases/[current-phase-dir]/*-UAT.md 2>/dev/null || true) | wc -l
```

State: "This phase has {X} plans, {Y} summaries."

**Step 1.5: Check for unaddressed UAT gaps**

Check for UAT.md files with status "diagnosed" (has gaps needing fixes).

```bash
# Check for diagnosed UAT with gaps or partial (incomplete) testing
grep -l "status: diagnosed\|status: partial" .planning/phases/[current-phase-dir]/*-UAT.md 2>/dev/null || true
```

Track:
- `uat_with_gaps`: UAT.md files with status "diagnosed" (gaps need fixing)
- `uat_partial`: UAT.md files with status "partial" (incomplete testing)

**Step 1.6: Cross-phase health check**

Scan ALL phases in the current milestone for outstanding verification debt using the CLI (which respects milestone boundaries via `getMilestonePhaseFilter`):

```bash
DEBT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" audit-uat --raw 2>/dev/null)
```

Parse JSON for `summary.total_items` and `summary.total_files`.

Track: `outstanding_debt` — `summary.total_items` from the audit.

**If outstanding_debt > 0:** Add a warning section to the progress report output (in the `report` step), placed between "## What's Next" and the route suggestion:

```markdown
## Verification Debt ({N} files across prior phases)

| Phase | File | Issue |
|-------|------|-------|
| {phase} | {filename} | {pending_count} pending, {skipped_count} skipped, {blocked_count} blocked |
| {phase} | {filename} | human_needed — {count} items |

Review: `$gsd-audit-uat ${GSD_WS}` — full cross-phase audit
Resume testing: `$gsd-verify-work {phase} ${GSD_WS}` — retest specific phase
```

This is a WARNING for prior phases, not a blocker. Debt on the **current** phase is handled explicitly by the route table below and must not be flattened into ordinary phase-complete routing.

**Step 2: Route based on counts**

| Condition | Meaning | Action |
|-----------|---------|--------|
| uat_partial > 0 | UAT testing incomplete | Go to **Route E.2** |
| uat_with_gaps > 0 | UAT gaps need fix plans | Go to **Route E** |
| current phase disk_status = `executed` | Plans are finished but clean verification has not landed yet | Go to **Route C.1** |
| current phase disk_status = `complete_with_debt` | Phase was advanced with explicit carried debt | Go to **Route E.3** |
| summaries < plans | Unexecuted plans exist | Go to **Route A** |
| current phase disk_status = `complete` | Phase cleanly complete | Go to Step 3 |
| plans = 0 | Phase not yet planned | Go to **Route B** |

---

**Route C.1: Verification pending after execution**

All plan summaries exist, but the current phase is still recorded as `executed`, not `complete`.

```
---

## Verification Pending

**Phase {phase_num}** has finished execution, but clean completion has not landed yet.

`$gsd-verify-work {phase} ${GSD_WS}`

---

**Also available:**
- `$gsd-audit-uat ${GSD_WS}` — inspect verification debt across the current milestone
- `$gsd-execute-phase {phase} ${GSD_WS}` — re-run execution only if implementation changed

---
```

---

**Route A: Unexecuted plan exists**

Find the first PLAN.md without matching SUMMARY.md.
Read its `<objective>` section.

```
---

## ▶ Next Up

**{phase}-{plan}: [Plan Name]** — [objective summary from PLAN.md]

`$gsd-execute-phase {phase} ${GSD_WS}`

---
```

---

**Route B: Phase needs planning**

Check if `{phase_num}-CONTEXT.md` exists in phase directory.

Check if current phase has UI indicators:

```bash
PHASE_SECTION=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" roadmap get-phase "${CURRENT_PHASE}" 2>/dev/null)
PHASE_HAS_UI=$(echo "$PHASE_SECTION" | grep -qi "UI hint.*yes" && echo "true" || echo "false")
```

**If CONTEXT.md exists:**

```
---

## ▶ Next Up

**Phase {N}: {Name}** — {Goal from ROADMAP.md}
<sub>✓ Context gathered, ready to plan</sub>

`$gsd-plan-phase {phase-number} ${GSD_WS}`

---
```

**If CONTEXT.md does NOT exist AND phase has UI (`PHASE_HAS_UI` is `true`):**

```
---

## ▶ Next Up

**Phase {N}: {Name}** — {Goal from ROADMAP.md}

`$gsd-discuss-phase {phase}` — gather context and clarify approach

---

**Also available:**
- `$gsd-ui-phase {phase}` — generate UI design contract (recommended for frontend phases)
- `$gsd-plan-phase {phase}` — skip discussion, plan directly
- `$gsd-list-phase-assumptions {phase}` — see the agent's assumptions

---
```

**If CONTEXT.md does NOT exist AND phase has no UI:**

```
---

## ▶ Next Up

**Phase {N}: {Name}** — {Goal from ROADMAP.md}

`$gsd-discuss-phase {phase} ${GSD_WS}` — gather context and clarify approach

---

**Also available:**
- `$gsd-plan-phase {phase} ${GSD_WS}` — skip discussion, plan directly
- `$gsd-list-phase-assumptions {phase} ${GSD_WS}` — see the agent's assumptions

---
```

---

**Route E: UAT gaps need fix plans**

UAT.md exists with gaps (diagnosed issues). User needs to plan fixes.

```
---

## ⚠ UAT Gaps Found

**{phase_num}-UAT.md** has {N} gaps requiring fixes.

`$gsd-plan-phase {phase} --gaps ${GSD_WS}`

---

**Also available:**
- `$gsd-execute-phase {phase} ${GSD_WS}` — execute phase plans
- `$gsd-verify-work {phase} ${GSD_WS}` — run more UAT testing

---
```

---

**Route E.2: UAT testing incomplete (partial)**

UAT.md exists with `status: partial` — testing session ended before all items resolved.

```
---

## Incomplete UAT Testing

**{phase_num}-UAT.md** has {N} unresolved tests (pending, blocked, or skipped).

`$gsd-verify-work {phase} ${GSD_WS}` — resume testing from where you left off

---

**Also available:**
- `$gsd-audit-uat ${GSD_WS}` — full cross-phase UAT audit
- `$gsd-execute-phase {phase} ${GSD_WS}` — execute phase plans

---
```

---

**Route E.3: Debt-carrying completion recorded**

The phase has full plan coverage, but the current completion state still carries explicit debt.

Use `completion_warnings` from the current phase record in `roadmap analyze` to explain what remains open.

```
---

## Debt-Carrying Completion

**Phase {phase_num}** is recorded as `complete_with_debt`.

Open debt:
- {warning 1}
- {warning 2}

This phase should not be narrated as cleanly complete while these items remain open.

`$gsd-verify-work {phase} ${GSD_WS}` — close or re-measure the carried debt

---

**Also available:**
- `$gsd-plan-phase {phase} --gaps ${GSD_WS}` — if VERIFICATION/UAT already identified concrete fix plans
- `$gsd-audit-uat ${GSD_WS}` — inspect all carried verification debt

---
```

---

**Step 3: Check milestone status (only when phase is cleanly complete)**

Read ROADMAP.md and identify:
1. Current phase number
2. All phase numbers in the current milestone section

Count total phases and identify the highest phase number.

State: "Current phase is {X}. Milestone has {N} phases (highest: {Y})."

**Route based on milestone status:**

| Condition | Meaning | Action |
|-----------|---------|--------|
| current phase < highest phase | More phases remain | Go to **Route C** |
| current phase = highest phase | Milestone complete | Go to **Route D** |

---

**Route C: Phase cleanly complete, more phases remain**

Read ROADMAP.md to get the next phase's name and goal.

Check if next phase has UI indicators:

```bash
NEXT_PHASE_SECTION=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" roadmap get-phase "$((Z+1))" 2>/dev/null)
NEXT_HAS_UI=$(echo "$NEXT_PHASE_SECTION" | grep -qi "UI hint.*yes" && echo "true" || echo "false")
```

**If next phase has UI (`NEXT_HAS_UI` is `true`):**

```
---

## ✓ Phase {Z} Complete

## ▶ Next Up

**Phase {Z+1}: {Name}** — {Goal from ROADMAP.md}

`$gsd-discuss-phase {Z+1}` — gather context and clarify approach

---

**Also available:**
- `$gsd-ui-phase {Z+1}` — generate UI design contract (recommended for frontend phases)
- `$gsd-plan-phase {Z+1}` — skip discussion, plan directly
- `$gsd-verify-work {Z}` — user acceptance test before continuing

---
```

**If next phase has no UI:**

```
---

## ✓ Phase {Z} Complete

## ▶ Next Up

**Phase {Z+1}: {Name}** — {Goal from ROADMAP.md}

`$gsd-discuss-phase {Z+1} ${GSD_WS}` — gather context and clarify approach

---

**Also available:**
- `$gsd-plan-phase {Z+1} ${GSD_WS}` — skip discussion, plan directly
- `$gsd-verify-work {Z} ${GSD_WS}` — user acceptance test before continuing

---
```

---

**Route D: Milestone complete**

```
---

## 🎉 Milestone Complete

All {N} phases finished!

## ▶ Next Up

**Complete Milestone** — archive and prepare for next

`$gsd-complete-milestone ${GSD_WS}`

---

**Also available:**
- `$gsd-verify-work ${GSD_WS}` — user acceptance test before completing milestone

---
```

---

**Route F: Between milestones (ROADMAP.md missing, PROJECT.md exists)**

A milestone was completed and archived. Ready to start the next milestone cycle.

Read MILESTONES.md to find the last completed milestone version.

```
---

## ✓ Milestone v{X.Y} Complete

Ready to plan the next milestone.

## ▶ Next Up

**Start Next Milestone** — questioning → research → requirements → roadmap

`$gsd-new-milestone ${GSD_WS}`

---
```

</step>

<step name="edge_cases">
**Handle edge cases:**

- Phase complete but next phase not planned → offer `$gsd-plan-phase [next] ${GSD_WS}`
- All work complete → offer milestone completion
- Blockers present → highlight before offering to continue
- Handoff file exists → mention it, offer `$gsd-resume-work ${GSD_WS}`
  </step>

</process>

<success_criteria>

- [ ] Rich context provided (recent work, decisions, issues)
- [ ] Current position clear with visual progress
- [ ] What's next clearly explained
- [ ] Smart routing: $gsd-execute-phase if plans exist, $gsd-plan-phase if not
- [ ] User confirms before any action
- [ ] Seamless handoff to appropriate gsd command
      </success_criteria>
