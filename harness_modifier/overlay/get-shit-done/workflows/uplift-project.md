<purpose>
Detect repo-local project uplift posture, compose the strongest current doctrine/runtime carriers into one report, and optionally write durable uplift memory without absorbing specialist-owner workflows.
</purpose>

<required_reading>
@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<supporting_reading>
Use the helper and the current uplift outputs as the first packet:
- the package-owned project uplift shim detect output
- `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, and `STATE.md` uplift section when they already exist or when `--write` is in play
- `.planning/seeds/SEED-*.md` only when the helper surfaces legacy-unversioned or noncurrent seed posture
- runtime/version surfaces only when compatibility movement is active
</supporting_reading>

<deeper_reading>
Only widen into entry-uplift audit artifacts, doctrine-sensitive proposal notes, or broader governance docs when the helper returns a route that actually depends on them.
</deeper_reading>

<process>

<step name="parse_args">
Treat detect-only as the default posture.

Supported flags for the first slice:
- `--write` — write `UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, and the `STATE.md` uplift section
- `--json` — print helper JSON verbatim after the human summary

All other uplift refresh/install routes stay held for later slices.
</step>

<step name="reading_control">
Keep uplift reading layered:

- Primary packet: execution-context paths plus helper detect output
- Supporting packet: existing uplift report/manifest/state outputs when they already exist or are being refreshed
- Deeper packet: doctrine-sensitive proposal or audit-family rereads only when the helper surfaces that route

Do not reopen the full uplift audit family just to deliver an ordinary detect-only result.
</step>

<step name="run_detect">
Run the repo-local helper:

```bash
UPLIFT_JSON=$(python3 "__PROJECT_ROOT__/harness_modifier/overlay/helpers/project_uplift.py" detect "__PROJECT_ROOT__" $([ "$WRITE" = "true" ] && printf '%s' -- --write) --json)
```

Parse the JSON for:
- `project_class`
- `secondary_signals`
- `current_status`
- `runtime_dirs`
- `compatibility_basis`
- `seed_corpus_posture`
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
- Observed runtime profiles: {compatibility_basis.observed_runtime_profiles or "unrecorded"}
- Mixed-runtime policy: {compatibility_basis.mixed_runtime_policy.profile_name or "unrecorded"} ({compatibility_basis.mixed_runtime_policy.state or "unrecorded"})
- Secondary runtime observation: {compatibility_basis.held_runtime_annotation_summary or "none"}
- Seed corpus posture: {seed_corpus_posture.posture} | current {seed_corpus_posture.current_contract_count} | legacy {seed_corpus_posture.legacy_unversioned_count} | noncurrent {seed_corpus_posture.noncurrent_version_counts or "none"}
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
  - keep them for explicit later review rather than folding them into detect-only, and only then widen into the supporting proposal/audit packet
  - when the operator wants one bounded assist-family packet before governance or durable uplift edits:
    - use the host uplift assist-family reference as the family reference
    - use the host docs-governance classification packet entry or the host carrier-gap identification packet entry as the bounded packet entry
    - record the packet result under `entry-uplift-audit/outputs/`
    - record the parent-thread judgment under `entry-uplift-audit/dispositions/`
    - keep the route operator-initiated: do not auto-spawn and do not widen the helper or CLI
- If seed corpus posture shows `legacy_unversioned`, noncurrent seed versions, or current-version shape gaps:
  - keep migration or rewrite separate from detect-only
  - preserve the posture in durable uplift memory with `--write` when the route activates
  - point the operator at `$gsd-seed-migration-inventory` when they want the deeper detect-only migration packet instead of only counts and examples
  - point the operator at `$gsd-seed-migration-inventory --write` when they want that packet preserved as durable migration-planning memory
- If the helper classifies the repo as `mid-phase uplift`:
  - keep uplift composition separate from current execution/verification routing
</step>

</process>
