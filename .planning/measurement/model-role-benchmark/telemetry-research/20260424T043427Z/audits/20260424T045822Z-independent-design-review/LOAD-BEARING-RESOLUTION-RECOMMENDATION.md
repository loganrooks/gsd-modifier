# Load-Bearing Resolution Recommendation

Review timestamp: `20260424T045822Z`
Recommendation target: `LOAD-BEARING-RESOLUTION-RECOMMENDATION.md`
Coordinator synthesis target: `ARCHITECTURE-RESOLUTION.md`

## Evidence Boundary

This recommendation is architectural deliberation from the existing telemetry research artifacts. Provider/runtime claims below are artifact-derived from the lane files and independent design review; they are not independently provider-verified in this pass. I did not run live provider calls, mutate provider configuration, enable telemetry exporters, perform new external research, inspect private transcript content, or edit lane artifacts.

## Decision 1 - `runtime_response_items`

- verdict: `resolve-with-condition`
- recommended decision: Treat `runtime_response_items` as a first-architecture core concept and, if the first implementation accepts the Lane 05 relational cache, as a first-slice table. Define it generically as a runtime-emitted response/item envelope observed within a turn or session that may correlate with a provider model call, tool request, tool result, assistant message structure, compaction marker, or other runtime item. It is not a provider model call and must not be named or shaped as a Codex `response_item` transplant.
- rationale: Lane 02's Codex artifact-derived evidence says Codex rollout JSONL has `response_item` records but explicitly warns they are not proven one-to-one provider model calls. Lane 03's Claude artifact-derived evidence shows local JSONL/message/tool structures and sidechain fields that need structural representation without turning Claude local file fields into core schema. Lane 04's artifact-derived API/trace evidence separates provider calls, response IDs, tool spans, function spans, handoffs, and trace spans. A generic runtime item concept keeps these surfaces attachable without forcing false identity with `model_calls`.
- future-option preservation check: The concept must carry `source_kind`, provider/runtime namespace, `item_type`, role/status when present, redaction state, `source_artifact_id`, provider payload namespace, and `correlation_status`. `correlation_status` must distinguish `uncorrelated`, `correlates_with`, `same_as_model_call`, and `not_applicable` or equivalent states so future API/OTel/harness evidence can promote or refuse identity links.
- risk if wrong: If this becomes Codex-shaped, Claude/API/manual adapters will either fake response items or bypass core. If it is deferred entirely, early reports will likely re-collapse runtime items into `model_calls`, losing the main warning from Lane 02.
- implementation implication: Include `runtime_response_items` in the relational spine only as a provider-neutral table with nullable `model_call_id` and mandatory provenance/redaction/correlation fields. If the implementation starts JSONL-only before SQLite, require the same concept in the observation registry and golden fixtures before adapters emit it.
- evidence basis by artifact: `DESIGN-REVIEW.md` flags this as unresolved and warns against Codex overfit; `02-CODEX-EXPOSURE.md` provides artifact-derived Codex JSONL pressure; `03-CLAUDE-EXPOSURE.md` provides artifact-derived non-Codex local structure pressure; `04-API-AGENTS-TRACE-SURFACES.md` provides artifact-derived provider/API trace separation; `05-ONTOLOGY-STORAGE-OPTIONS.md` proposes the table; `06-PLUGIN-PROTOCOL-METRICS.md` requires the concept or namespace.
- confidence: medium-high.

## Decision 2 - `telemetry_events`

- verdict: `resolve-now`
- recommended decision: Do not require `telemetry_events` as first-slice infrastructure. Treat it as optional replay/debug/import support owned by adapters or rebuild tooling. Durable evidence remains JSONL/raw source artifacts plus artifact manifests; SQLite remains a rebuildable query cache over entities, edges, observations, costs, rubrics, registries, and rebuild metadata.
- rationale: Lane 05 recommends an entity/edge/observation relational model because benchmark concepts need stable query semantics. Its event-first option is useful as ingestion/replay support but weaker as the primary query model. Lane 02 and Lane 03 both show JSONL-like local sources, but both also require field-level redaction and tolerant parsing. A mandatory event table would add storage surface before the first adapters prove a replay/debug need.
- future-option preservation check: The architecture should reserve an optional `telemetry_events` registry/source kind and allow adapters to emit normalized event envelopes later. If introduced, event rows are rebuildable indexes with source refs and redaction states, not the only durable copy of evidence and not the canonical benchmark fact model.
- risk if wrong: If events are mandatory too early, the first slice may overbuild a generic telemetry platform and duplicate private/raw source concerns in SQLite. If events are permanently rejected, future OTel/API/JSONL replay and malformed-line diagnostics may be harder.
- implementation implication: First implementation should validate durable source artifacts, artifact hashes, parse diagnostics, and normalized observation output without requiring event persistence. Add `telemetry_events` only when a specific adapter or replay test needs it.
- evidence basis by artifact: `DESIGN-REVIEW.md` says keep `telemetry_events` optional until adapters prove replay/debug need; `05-ONTOLOGY-STORAGE-OPTIONS.md` recommends JSONL as durable evidence and SQLite as rebuildable cache; `02-CODEX-EXPOSURE.md` and `03-CLAUDE-EXPOSURE.md` show JSONL/local source value and privacy risk; `04-API-AGENTS-TRACE-SURFACES.md` supports source-kind separation.
- confidence: high.

## Decision 3 - Canonical Enums

- verdict: `resolve-now`
- recommended decision: Adopt implementation-ready enum vocabularies now, with schema aliases allowed only for importing existing artifact labels such as `verified-doc` into code-safe names like `verified_doc`.

### Missingness / Observation Status

Use one status vocabulary for observation availability and derivation state:

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

`raw_api_body_gated` and `raw_content_allowed` require explicit operator consent and separate retention policy. They are not allowed for this research package's default path.

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

- rationale: The artifacts converge on semantic missingness, evidence class, reliability, content contract, cost evidence, and comparability as hard architecture requirements, but they leave names open. Fixing names before implementation prevents adapters and reports from inventing incompatible local vocabularies.
- future-option preservation check: These vocabularies include provider-neutral states, local runtime states, fixture states, deferred/live-call states, and privacy-gated states. Provider-specific meanings still belong in namespaced payloads or metric declarations.
- risk if wrong: Too narrow an enum set will force fake zeros, hidden omissions, or provider-shaped one-offs. Too broad a set can make reports noisy. The proposed set is broad enough for first fixtures while still small enough to validate.
- implementation implication: Manifests and validators should reject undeclared enum values in strict mode. Importers may map legacy hyphenated artifact labels to canonical code-safe enum names, but reports should render the canonical names consistently.
- evidence basis by artifact: `ORCHESTRATION.md` defines the evidence taxonomy and semantic missingness rule; `LANE-SPECS-AND-PROMPTS.md` requires direct/provider/derived/substitute/unavailable separation; `01-REFLECT-INHERITANCE-REVIEW.md` supports statusful observations and parity; `02`, `03`, and `04` provide artifact-derived provider/runtime missingness and cost/rate/token distinctions; `05` and `06` propose status, content, reliability, and comparability semantics.
- confidence: high.

## Decision 4 - Manifest And Registry Enforcement

- verdict: `resolve-with-condition`
- recommended decision: First-slice manifests should be static, reviewable YAML files using `telemetry-plugin-manifest/v1`, validated into a canonical JSON registry representation. SQLite should store the canonical registry payload in `registries`; rebuilds should store `schema_version`, `registry_version`, `registry_hash`, and `source_set_hash` in `rebuild_runs`. Query and report outputs should include the same registry hash/version and source-set hash that produced their data.
- rationale: YAML is the most reviewable first-slice source artifact; canonical JSON gives stable hashing and validation. This preserves the Reflect-derived registry/store/query parity lesson without importing Reflect workflow ontology. A registry that only exists as Python metadata would be weaker as an audit artifact, while SQLite-only registry rows would obscure source review.
- future-option preservation check: The manifest format should allow plugin type, source kinds, provider/runtime namespaces, metric IDs, rubric IDs, predicates, content contracts, privacy class, allowed statuses, reliability modes, external mappings, fixtures, and compatibility minimums. Python package metadata can later point to the YAML manifest; it should not replace it as the source of truth in the first slice.
- risk if wrong: Weak validation will let adapters emit undeclared metrics and recreate report/query drift. Overly rigid validation of unknown provider payload keys will break drift-tolerant local adapters. The distinction should be hard on declared contract identifiers and tolerant inside namespaced provider payloads.
- implementation implication: Strict first-slice validation should hard-fail malformed manifests, duplicate IDs, undeclared emitted `metric_id`, `rubric_id`, predicate, source kind, provider namespace, content contract, missingness/status, reliability mode, and raw-content policy violation. It may warn, not fail, on unknown keys inside adapter-owned namespaced payloads when those keys are retained as raw payload metadata. Rebuild strict mode should hard-fail undeclared identifiers and record diagnostics for malformed lines, missing artifacts, duplicate IDs, and unresolved correlations.
- evidence basis by artifact: `01-REFLECT-INHERITANCE-REVIEW.md` identifies registry/store/query parity as an adopted invariant; `05-ONTOLOGY-STORAGE-OPTIONS.md` proposes `registries`, `rebuild_runs`, registry hashes, and source-set hashes; `06-PLUGIN-PROTOCOL-METRICS.md` proposes manifest shape and registry-first implementation; `DESIGN-REVIEW.md` requires manifest format and validator strictness before adapters.
- confidence: high.

## Decision 5 - First-Slice Provider-Neutrality Gate

- verdict: `resolve-with-condition`
- recommended decision: The first implementation may begin with Codex fixture-backed adapters, but it must not claim harness/provider neutrality until it passes a non-Codex/provider-neutral fixture gate. The mandatory gate is:
  - `manual_run_with_rubric_dimensions`: provider-neutral benchmark JSONL plus rubric observation JSONL proving multidimensional quality without `score.overall`.
  - `claude_local_jsonl_minimal_structure`: synthetic Claude-shaped local JSONL/session-meta fixture with session/message/tool/sidechain or agent fields, malformed-line diagnostics, and redaction states.
  - `provider_denominator_mismatch`: synthetic OpenAI/Anthropic-style usage fixture proving cache/reasoning token and cost-evidence semantics do not collapse into Codex local token fields.
- rationale: Codex has the richest local evidence in the package, so starting there is practical. But Lane 03 and Lane 04 show enough different structure that Codex-only fixtures cannot validate a provider-neutral core. A manual fixture proves benchmark-domain neutrality; a Claude-shaped fixture prevents Codex JSONL/SQLite overfit; a provider-denominator fixture prevents OpenAI/Anthropic token/cost flattening.
- future-option preservation check: The gate uses synthetic or consent-safe data and does not require provider calls, config mutation, or raw transcript content. It tests API shape and schema pressure without forcing implementation of every provider adapter.
- risk if wrong: If neutrality is claimed after Codex-only fixtures, the core schema may quietly encode Codex rollout assumptions. If the gate requires full non-Codex adapters before any work begins, the first slice becomes too broad.
- implementation implication: Reports and docs may say "Codex fixture-backed first slice" after Codex fixtures pass. They may say "provider-neutral substrate" only after the three-fixture gate passes under strict manifest/rebuild validation.
- evidence basis by artifact: `DESIGN-REVIEW.md` requires at least one non-Codex fixture or provider-neutral fixture gate before neutrality claims; `06-PLUGIN-PROTOCOL-METRICS.md` already names `manual_run_with_rubric_dimensions` and `provider_denominator_mismatch`; `03-CLAUDE-EXPOSURE.md` supplies artifact-derived Claude local-shape pressure; `04-API-AGENTS-TRACE-SURFACES.md` supplies artifact-derived provider denominator differences; `05-ONTOLOGY-STORAGE-OPTIONS.md` requires fixtures for hierarchy, missingness, subagents, compaction, token accounting, rubric observations, malformed JSONL, and rebuild parity.
- confidence: high.

## Decision 6 - `score.overall` Migration

- verdict: `resolve-now`
- recommended decision: Accept legacy `score.overall` records as importable legacy observations only. Store them under `legacy.score.overall` or in a legacy payload namespace with `reliability_mode=manual_label` or `self_reported` as appropriate, `comparability=not_comparable` or `partial`, and explicit source provenance. Render them as compatibility-only display fields with a warning that they are not canonical quality truth. Canonical quality storage is multidimensional `rubric_observations`.
- rationale: Current target tests still expose `score.overall`, but orchestration and lanes consistently reject a single aggregate as canonical benchmark quality. The migration must preserve old records without letting legacy convenience determine the new ontology.
- future-option preservation check: Report plugins may compute display-only `view.*` rollups from declared rubric dimensions with formula and caveats, but those rollups must not be stored or queried as canonical quality. Future evaluators can add dimensions without schema migration.
- risk if wrong: If `score.overall` remains canonical, process telemetry and benchmark quality collapse into a false scalar and multidimensional rubric work becomes ornamental. If legacy records are rejected outright, current data and tests lose compatibility.
- implementation implication: Importers should preserve legacy values, validators should reject new canonical metric declarations named `score.overall`, `core.quality.overall`, or equivalent aggregate quality truth, and reports should prefer dimension matrices. Existing tests should migrate toward rubric observations while retaining a legacy compatibility test.
- evidence basis by artifact: `ORCHESTRATION.md` says the target must not depend on `score.overall`; `01-REFLECT-INHERITANCE-REVIEW.md`, `05-ONTOLOGY-STORAGE-OPTIONS.md`, and `06-PLUGIN-PROTOCOL-METRICS.md` all reject canonical `score.overall`; `DESIGN-REVIEW.md` lists the migration as pass-with-condition; current test references are artifact-derived from lanes 01, 05, and 06 rather than re-inspected here.
- confidence: high.

## Synthesis Instructions

The coordinator should carry these exact constraints into `DECISION-REPORT.md` and then `ARCHITECTURE-RESOLUTION.md`:

- Mark provider/runtime capability claims as lane-artifact-derived unless synthesis independently re-verifies them.
- Accept Lane 05 Option B as the architecture default: entity/edge/observation relational cache, JSONL/raw artifacts as durable evidence, SQLite as rebuildable cache.
- Keep `runtime_response_items` as a provider-neutral runtime-item concept distinct from `model_calls`; require correlation status before linking to provider calls.
- Keep `telemetry_events` optional replay/debug support, not first-slice required infrastructure.
- Use the enum vocabularies in this recommendation as the canonical first implementation names.
- Use static YAML manifests as the reviewable source, canonical JSON for hashing, `registries` for persisted registry payloads, and `rebuild_runs` for registry/source-set hashes.
- Enforce registry parity at manifest validation, rebuild, query, and report boundaries in strict mode.
- Require the manual, Claude-shaped, and provider-denominator fixture gate before any provider-neutrality claim.
- Treat `legacy.score.overall` as compatibility-only; canonical quality is multidimensional rubric observations.
- Preserve content contracts and raw-content defaults: no private prompts, assistant text, tool arguments, tool outputs, raw API bodies, file contents, or transcript content in default observation rows.

## Do Not Do

- Do not rename Codex `response_item` into a core schema without generic runtime-item semantics.
- Do not force every runtime item to be a provider `model_call`.
- Do not make `telemetry_events` the canonical fact model for first implementation.
- Do not make SQLite the only durable copy of source evidence.
- Do not use provider field names as core columns except for stable generic concepts such as requested/effective model and service tier.
- Do not treat local runtime logs or local JSONL schemas as stable provider APIs.
- Do not collapse token, cache, reasoning, quota, rate-limit, billing, cost estimate, and auth evidence into one usage/cost field.
- Do not claim provider neutrality from Codex-only fixtures.
- Do not reintroduce `score.overall` as canonical quality truth under a new name.
- Do not hide `not_exposed`, `not_enabled`, `redacted`, `not_collected`, `deferred_live_call`, or `unknown` in reports.

## Open Questions

- Exact final table and Python API names remain implementation decisions, provided they preserve the decisions above.
- Whether evaluator/rubric logic is an extractor subtype or a fourth plugin class remains legitimately deferred; either path must emit `rubric_observations` and preserve evaluator provenance.
- Exact raw-body consent UX and retention policy remain deferred and are out of scope for the default first slice.
- Exact OTel emitted payload schemas remain deferred until controlled fixture capture is explicitly approved.
- Exact cost allocation formulas remain deferred; first slice should store cost evidence mode and provenance, not invent billing truth.
- Exact provider SDK retry defaults beyond the artifact-reviewed evidence remain deferred.
