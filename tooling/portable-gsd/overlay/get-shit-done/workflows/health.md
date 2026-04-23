<purpose>
Validate `.planning/` directory integrity and report actionable issues. Checks for missing files, invalid configurations, inconsistent state, and orphaned plans. Optionally repairs auto-fixable issues.
</purpose>

<required_reading>
@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md

Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<supporting_reading>
Start from the narrow structural-health packet:
- `.planning/PROJECT.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, and `.planning/config.json` when present
- command arguments and any immediately previous health output when this is a rerun
</supporting_reading>

<deeper_reading>
Only widen into broader runtime, governing-doc, or audit carriers when structural health is already understood and the next route actually becomes repo-local posture uplift. Keep the widening order compact first, narrative second, typed last. Do not blend structural repair, runtime update, and doctrine refresh into one unbounded pass.
</deeper_reading>

<process>

<step name="parse_args">
**Parse arguments:**

Check if `--repair` flag is present in the command arguments.

```
REPAIR_FLAG=""
if arguments contain "--repair"; then
  REPAIR_FLAG="--repair"
fi
```
</step>

<step name="run_health_check">
**Run health validation:**

```bash
gsd-sdk query validate.health $REPAIR_FLAG
```

Parse JSON output:
- `status`: "healthy" | "degraded" | "broken"
- `errors[]`: Critical issues (code, message, fix, repairable)
- `warnings[]`: Non-critical issues
- `info[]`: Informational notes
- `repairable_count`: Number of auto-fixable issues
- `repairs_performed[]`: Actions taken if --repair was used
</step>

<step name="keep_route_boundaries_explicit">
**Keep structural repair distinct from broader repo-local posture refresh:**

- The authoritative three-way split is stated in `review_project_uplift_health_follow_through` -> `Interpretation Frame`.
- `health` owns structural planning integrity and limited low-risk repair.
- If core planning state is missing entirely, route to `$gsd-new-project` or `$gsd-ingest-docs` as appropriate rather than treating the problem as project uplift.
- If planning structure is present but the project still carries older or thinner repo-local runtime, governing-doc, or doctrine posture, route separately to `$gsd-uplift-project --write` after health instead of mutating that posture inside repair.
</step>

<step name="offer_repair">
**If repairable issues exist and --repair was NOT used:**

Ask user if they want to run repairs:

```
Would you like to run $gsd-health --repair to fix N issues automatically?
```

If yes, re-run with --repair flag and display results.
</step>

<step name="verify_repairs">
**If repairs were performed:**

Re-run health check without --repair to confirm issues are resolved:

```bash
gsd-sdk query validate.health
```

Report final status.
</step>

<step name="review_project_uplift_health_follow_through">
**Review Project Uplift Health Follow-Through:**

Only surface this step after all structural health validation is complete, including `verify_repairs` when `--repair` was used.

This step is read-only and route-local. Do not run `$gsd-uplift-project --write` from inside it.

Only widen into `.planning/UPLIFT-REPORT.md` or `.planning/UPLIFT-MANIFEST.json` from inside this dedicated step, and only after the compact `STATE.md` `## Project Uplift` reread has shown that route-local posture pressure is still live.

Only surface the step when:
- structural planning state is present
- the route is no longer broken or missing-planning
- the compact `STATE.md` `## Project Uplift` block still shows live posture pressure rather than ordinary steady-state continuation

Treat the following as live posture pressure signals:
- `Compatibility posture` is not exactly `core_runtime_parity`
- `Mixed-runtime policy` is not exactly `dual-runtime-core (active)`
- `Secondary runtime observation` is present and not `none`
- `Current recommendation` is not exactly `Continue with ordinary routing.`
- `Observed runtime profiles` become route-local only when the current health pass follows runtime movement, migration, or another state change that makes the compact profile line newly consequential after validation

## Primary Compact Read

Start with `.planning/STATE.md` and reread `## Project Uplift` first.

Keep this compact digest primary over deeper widening. Use it to read:
- `Last uplift pass`
- `Last uplift class`
- `Compatibility posture: core_runtime_parity`
- `Observed runtime profiles`
- `Mixed-runtime policy`
- `Secondary runtime observation`
- `Current recommendation`

If the compact digest already resolves the route-local posture question, stop here.

## Supporting Narrative Read

Only widen into `.planning/UPLIFT-REPORT.md` when the compact digest does not carry enough route-local context.

Use the report to understand:
- `Before-State Posture`
- `Recommendation Reasons`
- `Compatibility Basis`
- `Held Runtime Annotation`
- `Wider Compatibility Claims Held`
- `Carrier Posture`

## Deeper Typed Read

Only widen into `.planning/UPLIFT-MANIFEST.json` when runtime-profile or policy ambiguity remains after the compact and narrative reads.

Use the typed manifest to resolve:
- `compatibility_basis`
- `mixed_runtime_policy`
- `held_runtime_annotation`
- `held_later_families`
- per-carrier fingerprints and typed posture fields

Do not mirror manifest content into a new health-local cache or output surface.

## Interpretation Frame

Keep the ownership split explicit:
- `gsd-sdk query validate.health` remains the structural-health authority
- this step owns only read-only uplift-continuity surfacing after validation
- `$gsd-uplift-project --write` remains the later write-side posture-refresh authority
- The footer remains the write-side route pointer when later posture refresh is still live.
- This step remains the read-only continuity reread.
- Both may surface in one pass without duplicating ownership or turning health into a second uplift workflow.

Do not compute compatibility drift here.
Do not widen the health footer into a second uplift workflow.
Do not relabel held runtime annotation into a top-level compatibility posture row.

## When To Surface

Place this step:
- after all structural health validation, including `verify_repairs` when `--repair` was used
- before `format_output`

Keep it silent when:
- planning structure is missing and the correct route is `$gsd-new-project` or `$gsd-ingest-docs`
- structural health itself is still the unresolved question
- the compact `Project Uplift` block resolves to ordinary routing without later posture pressure, including:
  - `Compatibility posture: core_runtime_parity`
  - `Mixed-runtime policy: dual-runtime-core (active)`
  - `Secondary runtime observation: none`
  - `Current recommendation: Continue with ordinary routing.`
</step>

<step name="format_output">
**Format and display results:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GSD Health Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Status: HEALTHY | DEGRADED | BROKEN
Errors: N | Warnings: N | Info: N
```

**If repairs were performed:**
```
## Repairs Performed

- ✓ config.json: Created with defaults
- ✓ STATE.md: Regenerated from roadmap
```

**If errors exist:**
```
## Errors

- [E001] config.json: JSON parse error at line 5
  Fix: Run $gsd-health --repair to reset to defaults

- [E002] PROJECT.md not found
  Fix: Run $gsd-new-project to create
```

**If warnings exist:**
```
## Warnings

- [W002] STATE.md references phase 5, but only phases 1-3 exist
  Fix: Review STATE.md manually before changing it; repair will not overwrite an existing STATE.md

- [W005] Phase directory "1-setup" doesn't follow NN-name format
  Fix: Rename to match pattern (e.g., 01-setup)
```

**If info exists:**
```
## Info

- [I001] 02-implementation/02-01-PLAN.md has no SUMMARY.md
  Note: May be in progress
```

**Footer (if repairable issues exist and --repair was NOT used):**
```
---
N issues can be auto-repaired. Run: $gsd-health --repair
```

**Footer (if structural health is acceptable but repo-local posture still needs refresh):**
```
---
Structural health is not the same thing as repo-local posture refresh.
If runtime/governing-doc/doctrine posture is the live issue, run: $gsd-uplift-project --write
```
</step>

</process>

<error_codes>

| Code | Severity | Description | Repairable |
|------|----------|-------------|------------|
| E001 | error | .planning/ directory not found | No |
| E002 | error | PROJECT.md not found | No |
| E003 | error | ROADMAP.md not found | No |
| E004 | error | STATE.md not found | Yes |
| E005 | error | config.json parse error | Yes |
| W001 | warning | PROJECT.md missing required section | No |
| W002 | warning | STATE.md references invalid phase | No |
| W003 | warning | config.json not found | Yes |
| W004 | warning | config.json invalid field value | No |
| W005 | warning | Phase directory naming mismatch | No |
| W006 | warning | Phase in ROADMAP but no directory | No |
| W007 | warning | Phase on disk but not in ROADMAP | No |
| W008 | warning | config.json: workflow.nyquist_validation absent (defaults to enabled but agents may skip) | Yes |
| W009 | warning | Phase has Validation Architecture in RESEARCH.md but no VALIDATION.md | No |
| I001 | info | Plan without SUMMARY (may be in progress) | No |

</error_codes>

<repair_actions>

| Action | Effect | Risk |
|--------|--------|------|
| createConfig | Create config.json with defaults | None |
| resetConfig | Delete + recreate config.json | Loses custom settings |
| regenerateState | Create STATE.md from ROADMAP structure when it is missing | Loses session history |
| addNyquistKey | Add workflow.nyquist_validation: true to config.json | None — matches existing default |

**Not repairable (too risky):**
- PROJECT.md, ROADMAP.md content
- Phase directory renaming
- Orphaned plan cleanup

</repair_actions>

<stale_task_cleanup>
**Windows-specific:** Check for stale Claude Code task directories that accumulate on crash/freeze.
These are left behind when subagents are force-killed and consume disk space.

When `--repair` is active, detect and clean up:

```bash
# Check for stale task directories (older than 24 hours)
TASKS_DIR="__PROJECT_ROOT__/.codex/tasks"
if [ -d "$TASKS_DIR" ]; then
  STALE_COUNT=$( (find "$TASKS_DIR" -maxdepth 1 -type d -mtime +1 2>/dev/null || true) | wc -l )
  if [ "$STALE_COUNT" -gt 0 ]; then
    echo "⚠️  Found $STALE_COUNT stale task directories in __PROJECT_ROOT__/.codex/tasks/"
    echo "   These are leftover from crashed subagent sessions."
    echo "   Run: rm -rf __PROJECT_ROOT__/.codex/tasks/*  (safe — only affects dead sessions)"
  fi
fi
```

Report as info diagnostic: `I002 | info | Stale subagent task directories found | Yes (--repair removes them)`
</stale_task_cleanup>
