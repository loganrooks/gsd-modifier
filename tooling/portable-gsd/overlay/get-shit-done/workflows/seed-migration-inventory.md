<purpose>
Inventory legacy or drifted seed-corpus posture and, when explicitly requested, write durable migration-planning memory without rewriting seed files.
</purpose>

<required_reading>
@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<supporting_reading>
Keep the initial packet narrow:
- `seed_migration_inventory.py` detect output
- `.planning/seeds/SEED-*.md` only when a seed corpus exists
- `.planning/UPLIFT-REPORT.md` and `.planning/UPLIFT-MANIFEST.json` only when this route was activated from uplift posture
</supporting_reading>

<deeper_reading>
Only widen into seed-family audit notes or broader uplift docs when a drift dispute, migration-planning choice, or later rewrite route depends on them.
</deeper_reading>

<process>

<step name="parse_args">
Detect-only is the default posture.

Supported flags for the first slice:
- `--write` — write `.planning/SEED-MIGRATION-REPORT.md` and `.planning/SEED-MIGRATION-MANIFEST.json`
- `--json` — print helper JSON verbatim after the human summary

Keep rewrite automation, direct file edits, and larger seed-corpus normalization separate from this first slice.
</step>

<step name="run_detect">
Run the repo-local helper:

```bash
SEED_MIGRATION_JSON=$(python3 "__PROJECT_ROOT__/tooling/codex/seed_migration_inventory.py" detect "__PROJECT_ROOT__" $([ "$WRITE" = "true" ] && printf '%s' -- --write) --json)
```

Parse the JSON for:
- `route_state`
- `seed_corpus_posture`
- `migration_candidate_count`
- `reasons`
- `entries`
- `written_outputs`
</step>

<step name="present">
Present a compact result:

```markdown
# Seed Migration Inventory

- Route state: {route_state}
- Corpus posture: {seed_corpus_posture.posture}
- Seed count: {seed_corpus_posture.seed_file_count}
- Migration candidate count: {migration_candidate_count}
- Recommendation: {recommendation}

## Reasons
- {reason}

## Candidate Seeds
- {seed_id}: {contract_vintage} | {migration move summary}
```

Only show `Candidate Seeds` when `migration_candidate_count > 0`.

If `written_outputs` exists, also show:

```markdown
## Written Outputs
- `.planning/SEED-MIGRATION-REPORT.md`
- `.planning/SEED-MIGRATION-MANIFEST.json`
```
</step>

<step name="route">
Route next action explicitly:

- If `route_state` is `dormant`:
  - continue with current seed routing
- If `route_state` is `surfaced` and `--write` was not used:
  - recommend rerunning with `--write` when the operator wants durable migration-planning memory
- If `route_state` is `surfaced` and `--write` was used:
  - treat the report and manifest as the compact planning packet for any later rewrite or normalization family

This workflow does not rewrite seed files.
It does not decide or execute a migration.
It makes the inventory explicit so a later migration family can work from a sharper packet.
</step>

</process>
