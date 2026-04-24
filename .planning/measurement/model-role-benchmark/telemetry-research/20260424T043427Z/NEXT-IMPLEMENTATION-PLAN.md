# Next Implementation Plan

Status: concrete follow-on outline, not implementation.

## Goal

Build the smallest telemetry substrate slice that proves the resolved architecture without live provider calls, provider config mutation, raw-content capture, or broad platform scope.

## Task Order

1. Schema and registry spec
   - Write a schema document for entities, edges, observations, runtime response items, rubric observations, cost estimates, artifacts, registries, and rebuild runs.
   - Define `telemetry-plugin-manifest/v1` as static YAML plus canonical JSON hash.
   - Include canonical enums from `ARCHITECTURE-RESOLUTION.md`.

2. Golden fixtures
   - Add synthetic fixtures:
     - `codex_sqlite_minimal_thread`
     - `codex_rollout_redacted_stream`
     - `manual_run_with_rubric_dimensions`
     - `claude_local_jsonl_minimal_structure`
     - `provider_denominator_mismatch`
     - malformed JSONL and rebuild-parity cases
   - Ensure fixtures contain no private transcript content.

3. SQLite skeleton
   - Implement rebuildable cache tables for:
     - source artifacts
     - sessions/work units/task definitions/task instances/runs
     - turns
     - runtime response items
     - model calls
     - tool calls
     - subagent/entity edges
     - observations
     - rubric observations
     - cost estimates
     - registries
     - rebuild runs
   - Do not require `telemetry_events` in first slice.

4. Manifest validator
   - Validate static YAML manifests.
   - Materialize canonical JSON.
   - Compute registry hash.
   - Reject undeclared metrics, rubrics, predicates, source kinds, namespaces, content contracts, statuses, reliability modes, and raw-content violations.

5. Rebuild/query parity
   - Rebuild from fixtures into SQLite.
   - Persist registry hash and source-set hash.
   - Query/report outputs must include the same hashes.
   - Add tests proving registry drift fails.

6. Codex fixture adapters
   - Implement read-only fixture-backed adapters for:
     - `runtime.codex_cli.sqlite_index`
     - `runtime.codex_cli.rollout_stream`
   - Emit structural observations only.
   - Keep Codex-specific field names in payload namespaces.

7. Provider-neutrality gate
   - Run manual rubric, Claude-shaped, and provider-denominator fixtures through the same registry/rebuild/query path.
   - Only after this gate may docs describe the slice as a provider-neutral substrate candidate.

8. Rubric migration path
   - Preserve `score.overall` as `legacy.score.overall`.
   - Add canonical multidimensional rubric observation import and reporting.
   - Update current benchmark tests to prefer rubric dimensions while retaining a legacy compatibility test.

## Test Strategy

- Unit tests for manifest validation, enum validation, canonical JSON hashing, and duplicate ID rejection.
- Fixture rebuild tests for every golden fixture.
- Rebuild/query/report parity tests checking registry hash and source-set hash.
- Privacy tests rejecting raw transcript-like fields in default fixtures.
- Missingness tests for `not_exposed`, `not_enabled`, `not_collected`, `redacted`, `deferred_live_call`, `malformed_source`, and `unknown`.
- Runtime-item tests proving `runtime_response_items` do not require `model_call_id`.
- Cost-mode tests proving API-equivalent estimates are not provider-reported costs.
- Rubric tests proving `score.overall` is legacy-only.

## Migration And Compatibility

- Keep current benchmark JSONL ingest as v0 compatibility until the new observation path is fixture-proven.
- Map current run records into `runs`, usage observations, telemetry feature observations, and legacy score observations.
- Do not delete existing `score.overall` support immediately; restrict it to legacy import/report compatibility.
- Add a migration report that counts legacy scalar score records versus multidimensional rubric records.

## First Adapter Recommendation

Start with Codex fixture adapters because Codex has the richest local structural evidence, but make the first acceptance gate provider-neutral:

- Codex adapters can be implemented first.
- The implementation is not accepted as provider-neutral until manual, Claude-shaped, and provider-denominator fixtures pass under strict registry validation.
- OTel, live API, raw-body, billing, and quota adapters remain deferred.

## Explicit Non-Goals

- No live provider runs.
- No OTel capture.
- No provider config mutation.
- No billing integration.
- No raw API body ingestion.
- No dashboard.
- No GSD phase/milestone domain plugin.
- No mandatory `telemetry_events` table.
