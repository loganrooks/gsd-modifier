# Architecture Resolution

Resolution date: `2026-04-24`
Research package: `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/`
Status: load-bearing decisions resolved for coordinator synthesis

## Evidence Boundary

This resolution is based on the lane artifacts, the independent design review, and the high-reasoning load-bearing recommendation in this audit folder. Provider/runtime capability claims remain artifact-derived unless a later synthesis or implementation pass independently re-verifies them against official docs or live controlled fixtures.

No lane artifacts were edited. This file is the coordinator-owned decision layer that converts provisional lane recommendations into synthesis constraints.

## Summary Verdict

Proceed to coordinator synthesis with the decisions below.

Accepted as architecture invariants:

- JSONL/raw artifacts are durable evidence; SQLite is a rebuildable query cache.
- The default architecture is an entity/edge/observation relational cache, not a pure event-first query model.
- Core schema must remain provider-neutral; provider/runtime fields belong in namespaced payloads, observations, or plugin namespaces.
- Semantic missingness is mandatory and must not collapse to zero.
- Token, cache, reasoning, cost, quota, rate, auth, provider, and billing evidence remain separate axes.
- `score.overall` is legacy/view-only compatibility, not canonical quality truth.
- Registry/store/query/report parity is a first-slice implementation requirement.

## Resolved Decisions

| Decision | Resolution | Status | Key condition |
| --- | --- | --- | --- |
| `runtime_response_items` | Core generic runtime-item concept, distinct from `model_calls` | resolved-with-condition | Must not be Codex-shaped; must carry correlation status and provenance |
| `telemetry_events` | Optional replay/debug/import support, not first-slice required infrastructure | resolved | JSONL/raw artifacts remain durable evidence |
| Canonical enums | Adopt first implementation vocabularies in this file | resolved | Strict validators reject undeclared enum values after legacy import mapping |
| Manifest/registry enforcement | Static YAML manifests, canonical JSON registry payload/hash, SQLite registry cache | resolved-with-condition | Strict parity at manifest, rebuild, query, and report boundaries |
| Provider-neutrality gate | Codex-first allowed, but neutrality claim requires manual, Claude-shaped, and provider-denominator fixtures | resolved-with-condition | No provider-neutral substrate claim from Codex-only fixtures |
| `score.overall` migration | Import as `legacy.score.overall`; canonical quality is rubric observations | resolved | New canonical aggregate quality fields are forbidden |

## Decision 1: `runtime_response_items`

Resolution: `runtime_response_items` is a core first-architecture concept and may be a first-slice SQLite table if the relational cache is implemented. It represents a runtime-emitted item/envelope observed inside a session or turn. It may correspond to an assistant message structure, tool request, tool result, compaction marker, runtime status item, or provider-model-call-adjacent structure. It is not itself a provider `model_call`.

Required semantics:

- `runtime_response_items` must be generic, not named or shaped around Codex `response_item`.
- It must include `source_kind`, provider/runtime namespace, item type, status or role where available, redaction/content state, source artifact reference, and namespaced payload.
- It must include a correlation field for relationship to provider calls, with at least:
  - `uncorrelated`
  - `correlates_with`
  - `same_as_model_call`
  - `not_applicable`
  - `unknown`
- `model_call_id` must be nullable. A runtime item must never be forced into model-call identity.

Rationale: Codex local evidence creates pressure for runtime response/item structure, but Lane 02 warned that Codex `response_item` is not proven one-to-one with provider model calls. Claude local JSONL, OpenAI Agents/API traces, Anthropic API surfaces, OTel, manual imports, and future harnesses all need a way to represent runtime structure without pretending it is the same as provider inference.

Future-option preservation: A future adapter may either link runtime items to provider calls or leave them uncorrelated. Provider-specific fields remain in payload namespaces.

## Decision 2: `telemetry_events`

Resolution: `telemetry_events` is optional replay/debug/import support, not required first-slice infrastructure and not the canonical fact model.

Required semantics:

- Durable evidence remains source artifacts plus artifact manifests, hashes, and parse diagnostics.
- SQLite remains a rebuildable query cache over normalized entities, edges, observations, costs, rubrics, registries, and rebuild metadata.
- Adapters may later emit normalized event envelopes if a replay/debug/import need is proven by a fixture or adapter requirement.
- If added, `telemetry_events` rows are rebuildable indexes over source references and redaction states; they are not the only durable copy of evidence.

Rationale: Event-first storage is useful for replay and diagnostics, but making it required now would overbuild a generic telemetry platform and enlarge privacy-sensitive storage before adapters prove the need.

## Decision 3: Canonical Enums

Resolution: adopt the following implementation vocabularies for the first synthesis and implementation plan. Importers may map legacy hyphenated research labels such as `verified-doc` to code-safe canonical values such as `verified_doc`.

### Observation Status / Missingness

- `measured`
- `estimated`
- `derived`
- `inferred`
- `not_available`
- `not_applicable`
- `not_exposed`
- `not_enabled`
- `not_collected`
- `redacted`
- `deferred_live_call`
- `malformed_source`
- `conflicting_sources`
- `unknown`

### Evidence Class

- `verified_doc`
- `local_observed`
- `repo_precedent`
- `inferred`
- `unverified`
- `deferred`
- `rejected`
- `synthetic_fixture`
- `manual_evidence`

### Reliability Mode

- `direct_field`
- `documented_field`
- `local_structural_field`
- `provider_emitted`
- `runtime_emitted`
- `harness_emitted`
- `aggregate`
- `approximate`
- `estimated_from_pricing`
- `aggregate_allocated`
- `derived_from_config`
- `derived_from_trace`
- `self_reported`
- `manual_label`
- `substitute_signal`
- `synthetic_fixture`
- `unknown`

### Content Contract

- `no_content_access`
- `metadata_only`
- `structural_only`
- `content_hash_or_length_only`
- `derived_features_only`
- `redacted_content_reference`
- `raw_api_body_gated`
- `raw_content_allowed`

Default rule: `raw_api_body_gated` and `raw_content_allowed` require explicit operator consent and a separate retention policy. They are not allowed in the default first-slice path.

### Cost Evidence Mode

- `not_exposed`
- `not_applicable`
- `provider_reported_per_request`
- `provider_reported_aggregate`
- `aggregate_allocated`
- `api_equivalent_estimate`
- `cli_approximate`
- `pricing_table_estimate`
- `manual_cost_entry`
- `unknown`

### Comparability

- `comparable`
- `comparable_with_caveat`
- `provider_semantics_differ`
- `surface_semantics_differ`
- `partial`
- `not_comparable`
- `insufficient_evidence`
- `unknown`

Validator implication: strict mode must reject undeclared enum values in manifests, normalized observations, and report inputs. Provider-specific sub-statuses belong in namespaced payloads or metric-specific metadata, not ad hoc core enum extensions.

## Decision 4: Manifest And Registry Enforcement

Resolution: first-slice plugin manifests are static YAML files using `telemetry-plugin-manifest/v1`. The manifest is the human-reviewable source. Validation materializes a canonical JSON registry representation for hashing and SQLite persistence.

Required first-slice registry behavior:

- Static YAML manifests are committed and reviewable.
- Canonical JSON is generated deterministically for hashing and storage.
- SQLite stores the canonical registry payload in `registries`.
- Rebuilds store `schema_version`, `registry_version`, `registry_hash`, and `source_set_hash` in `rebuild_runs`.
- Query outputs and report outputs include the registry hash/version and source-set hash used to produce them.

Strict validation must hard-fail:

- malformed manifests
- duplicate IDs
- undeclared emitted `metric_id`
- undeclared emitted `rubric_id`
- undeclared predicate
- undeclared source kind
- undeclared provider/runtime namespace
- undeclared content contract
- undeclared status/missingness value
- undeclared reliability mode
- raw-content policy violation

Strict validation may warn rather than fail on unknown keys inside adapter-owned namespaced payloads when those keys are retained as raw payload metadata and do not become core identifiers.

Rationale: This preserves the Reflect registry/store/query parity lesson without importing Reflect workflow ontology. YAML is reviewable; canonical JSON is stable for hashing; SQLite is a cache/query surface.

## Decision 5: First-Slice Provider-Neutrality Gate

Resolution: the first implementation may start with Codex fixture-backed adapters, but it cannot claim provider or harness neutrality until a non-Codex/provider-neutral fixture gate passes.

Mandatory neutrality gate:

1. `manual_run_with_rubric_dimensions`
   - Provider-neutral benchmark JSONL plus rubric observation JSONL.
   - Proves multidimensional quality without canonical `score.overall`.

2. `claude_local_jsonl_minimal_structure`
   - Synthetic Claude-shaped local JSONL/session-meta fixture.
   - Includes session/message/tool/sidechain or agent fields, malformed-line diagnostics, redaction states, and no private transcript content.

3. `provider_denominator_mismatch`
   - Synthetic OpenAI/Anthropic-style usage fixture.
   - Proves cache-token, reasoning-token, cost-evidence, quota/rate, and denominator semantics do not collapse into Codex local token fields.

Allowed claim before the gate: "Codex fixture-backed first slice."

Allowed claim after the gate passes under strict manifest/rebuild validation: "provider-neutral substrate candidate" or equivalent cautious phrasing.

Forbidden claim before the gate: "harness-neutral telemetry platform" or "provider-neutral substrate" based only on Codex fixtures.

## Decision 6: `score.overall` Migration

Resolution: legacy `score.overall` is importable as compatibility evidence only. Canonical quality storage is multidimensional `rubric_observations`.

Required migration behavior:

- Existing records with `score.overall` may be imported as `legacy.score.overall`.
- Legacy values must carry provenance, evidence class, reliability mode, and comparability.
- Suggested defaults:
  - `reliability_mode=manual_label` or `self_reported`, depending on source
  - `comparability=not_comparable` or `partial`
- Reports may render legacy values as compatibility-only display fields with a warning.
- New canonical metric declarations named `score.overall`, `core.quality.overall`, or equivalent aggregate quality truth are forbidden.
- View/report plugins may compute explicit display rollups from declared rubric dimensions, but rollups are `view.*` outputs and not canonical stored quality.

Rationale: Current benchmark tests and older records may still use `score.overall`, but the new benchmark must not collapse quality into a single scalar.

## Synthesis Constraints

Coordinator synthesis must:

- Mark provider/runtime capability claims as artifact-derived unless independently reverified.
- Carry Lane 05 Option B as the architecture default but not as a maximal first implementation.
- Keep `runtime_response_items` distinct from `model_calls`.
- Keep `telemetry_events` optional unless a concrete adapter fixture proves need.
- Use the enum vocabularies above.
- Require static YAML manifests plus canonical JSON registry hashing.
- Enforce registry parity at manifest validation, rebuild, query, and report boundaries.
- Require the manual, Claude-shaped, and provider-denominator fixture gate before provider-neutrality claims.
- Treat `legacy.score.overall` as compatibility-only.
- Preserve default no-private-content policy across source artifacts, observations, and reports.

## Do Not Do

- Do not rename Codex `response_item` into core without generic runtime-item semantics.
- Do not force runtime items to be provider `model_calls`.
- Do not make `telemetry_events` the canonical fact model in the first implementation.
- Do not make SQLite the only durable copy of evidence.
- Do not use provider-specific field names as core columns except stable generic concepts such as requested/effective model, requested/effective reasoning, service tier, request ID, and source kind.
- Do not treat local runtime logs or JSONL schemas as stable provider APIs.
- Do not collapse token, cache, reasoning, quota, rate-limit, billing, cost estimate, and auth evidence into one usage or cost field.
- Do not claim provider neutrality from Codex-only fixtures.
- Do not reintroduce `score.overall` as canonical quality under a new name.
- Do not hide `not_exposed`, `not_enabled`, `redacted`, `not_collected`, `deferred_live_call`, or `unknown` in reports.

## Deferred Questions

These are intentionally not resolved here:

- Exact final table names and Python API shape.
- Whether evaluator/rubric logic is an extractor subtype or a fourth plugin class.
- Raw-body consent UX and retention policy.
- Live Codex/Claude/OpenAI/Anthropic OTel payload schemas.
- Live API response headers and retry behavior.
- Provider billing truth and subscription/quota burn formulas.
- Cost allocation formulas beyond evidence-mode storage.

## Verification Notes

This artifact resolves design decisions for synthesis only. It does not implement schema, adapters, plugins, validators, migrations, reports, or tests.
