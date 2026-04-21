<purpose>
Detect repo-local project uplift posture, compose the strongest current doctrine/runtime carriers into one report, and optionally write durable uplift memory without absorbing specialist-owner workflows.
</purpose>

<required_reading>
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<process>

<step name="parse_args">
Treat detect-only as the default posture.

Supported flags for the first slice:
- `--write` — write `UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, and the `STATE.md` uplift section
- `--json` — print helper JSON verbatim after the human summary

All other uplift refresh/install routes stay held for later slices.
</step>

<step name="run_detect">
Run the repo-local helper:

```bash
UPLIFT_JSON=$(python3 "__PROJECT_ROOT__/tooling/codex/project_uplift.py" detect "__PROJECT_ROOT__" $([ "$WRITE" = "true" ] && printf '%s' -- --write) --json)
```

Parse the JSON for:
- `project_class`
- `secondary_signals`
- `current_status`
- `runtime_dirs`
- `compatibility_basis`
- `recommend_write`
- `recommend_detect_only`
- `recommendation_reasons`
- `absent_additive_carriers`
- `pending_doctrine_sensitive_proposals`
- `written_outputs`
</step>

<step name="present">
Present a compact result:

```markdown
# Project Uplift

- Project class: {project_class}
- Secondary signals: {secondary_signals or "none"}
- Current state status: {current_status}
- Runtime directories: {runtime_dirs}
- Compatibility posture: {compatibility_basis.compatibility_posture}
- Observed runtime basis: {compatibility_basis.observed_runtime_version_set or "unrecorded"}
- Recommendation: {recommendation}

## Compatibility Check Protocol
- {compatibility step}

## Additive Install Routes
- {carrier}

## Doctrine-Sensitive Proposal Routes
- {carrier} — {proposal_state}

## Reasons
- {reason}
```

If `written_outputs` exists, show:

```markdown
## Written Outputs
- `.planning/UPLIFT-REPORT.md`
- `.planning/UPLIFT-MANIFEST.json`
- `STATE.md` uplift section refreshed
```
</step>

<step name="route">
Route next action explicitly:

- If `recommend_detect_only` is `true` and `--write` was not used:
  - recommend rerunning with `--write` when the operator wants durable uplift memory
- If `recommend_write` is `true`:
  - route directly to `--write`, because runtime-basis movement means the durable uplift memory is now stale
- If additive carriers remain absent:
  - keep those as future install routes, not silent edits
- If doctrine-sensitive proposal routes remain:
  - keep them for explicit later review rather than folding them into detect-only
- If the helper classifies the repo as `mid-phase uplift`:
  - keep uplift composition separate from current execution/verification routing
</step>

</process>
