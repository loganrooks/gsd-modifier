# Lane 06 - Plugin Protocol And Metrics

Run timestamp: `20260424T043427Z`

Scope: define adapter, extractor, and view/report plugin protocols for the model-role benchmark telemetry substrate. This lane performed no provider mutation, provider calls, quota-consuming runs, home-level telemetry changes, or transcript-content extraction.

## Summary Recommendation

Recommendation, not authority: use a small stable core plus three plugin classes:

1. Source adapter plugins read a bounded evidence surface and emit source events, raw payload references, and field-level observations.
2. Extractor plugins consume adapter output and emit normalized metric, identity, cost, rubric, and reliability observations.
3. View/report plugins consume normalized query output and registry metadata, then render coverage, comparison, quality, and diagnostic views without inventing metrics.

The core schema should likely own only provider-neutral entities, metric declarations, observation records, evidence references, and plugin manifests. Provider-specific, runtime-specific, harness-design, and domain-specific metrics should be added as namespaced metric declarations plus observation rows, not as new nullable columns. This lets harness-design metrics expand without core schema migration as long as the observation table supports dimensions, value payloads, provenance, missingness, and reliability. This is a Lane 06 recommendation that must be critiqued against Lane 05's final storage decision before implementation.

`score.overall` must not be a canonical storage target. Existing uses should be treated as a legacy/simple report projection until replaced by multidimensional rubric observations.

## Evidence Base

| Claim | Evidence class | Source path / URL | Command / citation | Confidence | Gaps | Implications |
| --- | --- | --- | --- | --- | --- | --- |
| This lane may write only its target file and must avoid provider mutation, paid calls, config edits, and private transcript copying. | local-observed | `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md`; `LANE-SPECS-AND-PROMPTS.md` | `sed -n '1,240p' .../ORCHESTRATION.md`; `sed -n '1,260p' .../LANE-SPECS-AND-PROMPTS.md` | high | None for lane scope. | Protocol must be research-only and privacy-first. |
| Current benchmark schema is provider-neutral but still stores usage and telemetry features in a run record shape. | local-observed | `tooling/codex/model_benchmark/schema.py` | `sed -n '1,280p' tooling/codex/model_benchmark/schema.py` | high | Storage design may change after Lane 05 lands. | Plugin protocol should preserve current run compatibility while moving extensibility into declarations and observations. |
| Current tests already enforce semantic missingness for usage and still use `score.overall` in summaries. | local-observed | `tooling/codex/tests/test_model_benchmark.py` | `sed -n '1,360p' tooling/codex/tests/test_model_benchmark.py`; `rg -n "score\\.overall|rubric|telemetry_features" tooling/codex -S` | high | This lane does not modify tests. | Treat `score.overall` as a migration gap, not a target protocol. |
| Reflect precedent supports source adapter -> extractor registry -> query/report layers, semantic missingness, privacy/content contracts, and registry/store/query parity. | repo-precedent | `01-REFLECT-INHERITANCE-REVIEW.md` | Lane 01 rows for three-layer architecture, registry parity, content contracts, report layer, and `score.overall` rejection. | high | Reflect is not authority for this repo; concepts must be adapted. | Use one registry source and report from normalized queries, not hardcoded report-only metrics. |
| Claude Code exposes distinct local, OTel, hook/plugin-visible, and raw-body-gated surfaces with different privacy and stability properties. | verified-doc via lane artifact plus local-observed lane review | `03-CLAUDE-EXPOSURE.md`; `https://code.claude.com/docs/en/monitoring-usage`; `https://code.claude.com/docs/en/discover-plugins`; `https://code.claude.com/docs/en/skills` | Lane 03 evidence table and adapter recommendations. | high for documented OTel/plugin concepts; medium for local JSONL/session-meta schema stability | This lane did not re-fetch docs; final synthesis should preserve Lane 03 citations. | Provider adapters need per-surface manifests, privacy modes, tolerant parsing, and fixture tests. |
| OpenAI Agents SDK traces, API usage, Anthropic API metadata, Claude Code OTel, and OTel GenAI can normalize into shared concepts only if provider fields remain namespaced. | verified-doc via lane artifact plus local-observed lane review | `04-API-AGENTS-TRACE-SURFACES.md`; `https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/` plus OpenAI/Anthropic docs cited there | Lane 04 summary, compatibility table, and storage recommendations. | high for cited docs; medium where Lane 04 marks API behavior as partial or inferred | This lane did not perform live API calls. | Use stable internal metric IDs with external semantic-convention mappings, not direct provider field names as core columns. |
| Lane 02 shows Codex adapter work should be layered across SQLite index, rollout JSONL stream, redacted config snapshot, and deferred OTel live capture. | verified-doc plus local-observed via lane artifact | `02-CODEX-EXPOSURE.md`; `https://developers.openai.com/codex/config-reference`; `https://developers.openai.com/codex/config-advanced`; `~/.codex/state_5.sqlite`; `~/.codex/sessions/**/*.jsonl` | Lane 02 evidence register and implementation implications. | high for local SQLite/JSONL structural fields; medium for future OTel capture; low for exact OTel emitted schema | This lane did not inspect private values or rerun Lane 02 commands. | Plugin protocol needs source-specific Codex adapters, explicit privacy exclusions, response-item vs model-call caution, and OTel fixture gating. |
| Lane 05 recommends entity/edge/observation SQLite as rebuildable query cache, with JSONL as durable evidence/import/export and first-class metric/rubric observations. | local-observed via lane artifact | `05-ONTOLOGY-STORAGE-OPTIONS.md` | Lane 05 recommendation, proposed tables, JSONL role, and rebuild behavior sections. | high for storage recommendation as lane output; medium until final synthesis accepts it | Lane 05 notes it originally lacked Lane 02; final coordinator must reconcile all lane revisions. | Plugin manifests should declare `metric_id`, `rubric_id`, `predicate`, `source_kind`, `content_contract`, privacy class, and missingness states for registry/store/query parity. |

## Dependency Repair Review

Prior Lane 06 status: the first artifact was written while Lanes 02 and 05 were absent, so it relied on partial lane availability for Codex adapter details, storage table implications, fixture names, and registry/rebuild mechanics. A later revision incorporated the newly present Lane 02 and Lane 05, but it still needed to be re-sequenced after Lane 05 repaired itself against all prerequisite lanes.

What changed after re-reading Lanes 01-05:

- Lane 01 makes registry/store/query parity, semantic missingness, content contracts, role-split provenance, and uncertainty-preserving reports stronger than optional niceties. Plugin registry declarations must be the source consumed by rebuild, query, and report plugins.
- Lane 02 makes the Codex plugin split concrete: `sqlite_index`, `rollout_stream`, `config_snapshot`, and deferred `otel_live`. It also requires a `runtime_response_item` concept or namespace because Codex `response_item` is not proven to equal a provider model call.
- Lane 03 requires Claude plugin boundaries to distinguish local session-meta, local JSONL, OTel, hook/plugin capture, skills/plugins as runtime phenomena, raw API body gates, and substitute signals. This expands the privacy contract beyond "metadata only" into per-surface reducer declarations.
- Lane 04 requires API/trace plugins to keep direct API, OpenAI Agents SDK traces, OTel GenAI, Anthropic API, Claude Code CLI/OTel, rate-limit headers, retries, cost modes, and tool categories separate. Provider denominators cannot be hidden behind a single normalized metric.
- Lane 05 now recommends an entity/edge/observation relational cache with JSONL as durable evidence, registry hashes in rebuilds, `runtime_response_items`, and fixture coverage for hierarchy, missingness, subagents, compaction, token accounting, rubric observations, malformed JSONL, and rebuild parity.

Remaining gaps:

- Codex OTel emitted payload shape remains deferred; docs prove config knobs, not exact spans/logs/metrics.
- Codex and Claude local schemas remain implementation artifacts and require drift-tolerant adapters plus golden fixtures.
- Cost dollars, subscription quota burn, provider-reported billing, and API-equivalent estimates remain separate and partly unresolved.
- Final table names, registry file format, enum names, and Python API shape are coordinator decisions. This lane recommends contracts and review criteria, not final schema authority.

## Load-Bearing Choices For High-Reasoning Review

These protocol/schema choices should receive coordinator or senior-review critique before final decision:

| Choice | Lane 06 recommendation | Why load-bearing | Evidence basis | Confidence | Review question |
| --- | --- | --- | --- | --- | --- |
| Three plugin classes | Adapter, extractor, and view/report plugins remain separate. | Collapsing them would recreate hidden extraction/report drift. | Lane 01 parity, Lane 05 rebuild/query parity. | high | Is a fourth evaluator/rubric plugin type needed, or is it an extractor subtype? |
| Registry-first implementation | Plugin, metric, rubric, predicate, source-kind, and namespace declarations should exist before broad adapters. | Reports and rebuilds need the same declaration source. | Lane 01 and Lane 05. | high | Should manifests be YAML/JSON files, Python metadata, or both? |
| `runtime_response_item` concept | Runtime response items should be distinct from provider `model_call`. | Codex JSONL response items are not proven one-to-one provider calls. | Lane 02 and Lane 05 Dependency Repair Review. | high | Should this be a first-class table or only `runtime.codex_cli.response_item.*` observations? |
| Entity/edge/observation cache binding | Lane 06 should target Lane 05's recommended relational cache, but as a recommendation. | Plugin outputs need stable storage semantics without overfitting to providers. | Lane 05. | medium-high | Is Option B accepted, or should implementation start JSONL-only with registry validation? |
| Missingness enum expansion | Use richer states than current `not_available`. | Provider/runtime absence, redaction, disabled telemetry, and deferred live calls mean different things. | Lanes 01-05. | high | Which enum names become canonical and which stay report-only? |
| Privacy/content contract vocabulary | Use per-plugin and per-metric contracts with raw-content default forbidden. | Codex/Claude local files, hooks, raw body modes, and OTel can expose sensitive content. | Lanes 02, 03, 04. | high | What consent and retention gate is required for `raw_content_allowed`? |
| `score.overall` migration | Keep `score.overall` legacy/view-only; make rubric dimensions canonical. | Current tests still use it, but orchestration forbids quality collapse. | Lanes 01 and 05 plus current tests. | high | What compatibility period and report behavior should exist for legacy records? |
| First implementation scope | Start with registry validator, synthetic fixtures, Codex SQLite/JSONL adapters, one usage extractor, one harness extractor, and one rubric/report path. | It proves the contract without provider mutation or platform sprawl. | Lane 02 and Lane 05. | medium-high | Should Claude local fixtures be included in the first slice to avoid Codex-shaped bias? |

## Stricter Contract Self-Audit

| Required Lane 06 question | Covered where | Evidence class | Confidence | Known gaps | Implications |
| --- | --- | --- | --- | --- | --- |
| Plugin protocol for provider adapters, metric extractors, and domain views | `Plugin Classes`, `Plugin Manifest Shape` | local-observed plus repo-precedent plus lane-derived verified-doc | high | Exact registry API still depends on implementation slice. | Build three plugin interfaces, not one generic callback. |
| Harness metrics without core schema changes | `Adding Harness-Design Metrics Without Core Schema Changes` | local-observed, inferred | high | Final table names depend on Lane 05 synthesis. | Add metrics through declarations and observations. |
| Privacy/content contracts | `Privacy And Content Contracts`, manifest `content_contract` | local-observed plus Lane 03/04 verified-doc | high | Exact consent UX deferred. | Default to no raw content in observations. |
| Evidence/reliability semantics | `Evidence And Reliability Semantics`, `Missingness Behavior` | local-observed plus Lane 01/04/05 | high | Enum names need final canonicalization. | Reports must show evidence quality, not hide it. |
| Base metrics versus provider/domain plugins | `Metric Layers`, namespace rules | local-observed plus Lane 04 | high | Provider denominator mappings require adapter implementation tests. | Keep `core.*` stable and provider fields namespaced. |
| Multidimensional rubric observations | `Multidimensional Rubric Observation Storage` | local-observed plus Lane 05 | high | Current tests still use `score.overall`. | Store one observation per dimension and evaluator. |
| Required golden fixtures | `Golden Fixture Requirements` | inferred from Lane 01/02/03/05 drift and privacy risks | high | Fixtures are specified, not created in this lane. | First implementation should start with fixtures before broad adapters. |
| First implementation recommendation from plugin perspective | `First Implementation Recommendation` | inferred from Lane 02 and Lane 05 | medium-high | Depends on coordinator acceptance of storage option. | Start with manifest registry plus Codex SQLite/JSONL adapters and synthetic fixtures. |

## Research Pitfalls And Mitigations

| Pitfall | Lane 06 mitigation | Evidence class | Confidence | Remaining gap | Implication |
| --- | --- | --- | --- | --- | --- |
| Treating Reflect as authoritative | Reflect ideas are marked `repo-precedent` and adapted only where compatible. | repo-precedent | high | Final synthesis must keep Reflect loop names out of core. | Use architecture invariants, not GSD workflow ontology. |
| Designing around Codex only | Protocol includes Codex, Claude, API, Agents SDK, OTel, manual fixture, provider, runtime, harness, and domain namespaces. | local-observed plus lane-derived verified-doc | high | Exact non-Codex fixtures still need implementation. | Prevent Codex local DB fields from becoming core schema. |
| Flattening provider/auth/billing | Provider metrics own raw semantics; cost modes distinguish observed, estimated, aggregate allocated, and approximate. | Lane 02/04 | high | Pricing/billing plugins are deferred. | Avoid false per-request dollar-cost claims. |
| Over-trusting local logs | Local runtime artifacts are adapter inputs with schema drift and privacy caveats, not stable APIs. | Lane 02/03 | high | Drift tests need real fixtures. | Keep raw fields namespaced and parser tolerant. |
| Mutating config for OTel experiments | OTel live capture is a future gated adapter and requires explicit setup; this lane does not enable it. | local-observed plus Lane 02 | high | No local OTel fixture yet. | No hidden config writes or live runs. |
| Persisting sensitive transcript content | Content contracts default to `metadata_only` or stricter; raw content is forbidden for this package. | local-observed | high | Future consent policy must be separate. | Store references, hashes, lengths, or redaction states only. |
| Treating missing fields as zero | Missingness enum separates unavailable, not exposed, not enabled, redacted, not collected, deferred, unknown. | local-observed plus current tests | high | Current schema has narrower enum. | Observation layer should extend status semantics. |
| Treating thinking summaries as reasoning quality | Rubric observations require evaluator provenance; telemetry signals are process evidence, not quality truth. | local-observed plus Lane 03 | high | Rubric evaluators not implemented. | No `reasoning_quality` truth metric without caveat. |
| Reintroducing `score.overall` | `legacy.score.overall` is report-only migration shim; canonical quality is multidimensional rubric rows. | local-observed | high | Existing report tests still summarize it. | Migration should replace average score with rubric views. |
| Overbuilding a generic telemetry platform | First implementation recommendation is bounded to registry, observation envelope, Codex SQLite/JSONL, and fixtures. | inferred | medium-high | Provider adapters beyond Codex remain staged. | Avoid platform breadth before source facts are fixture-backed. |
| Under-specifying plugin boundaries | Adapter, extractor, and view/report protocols are separated with manifest fields and output contracts. | inferred | high | Concrete Python API is still deferred. | Boundary is auditable before code. |
| Query/rebuild registry drift | Manifests are the single declaration source; Lane 05 registry hash should be used by rebuild/query/report. | repo-precedent plus Lane 05 | high | Tests not written in this lane. | Add parity tests in implementation slice. |
| Sanitized reports hiding uncertainty | View plugins must surface evidence, confidence, reliability, missingness, content contract, and caveats. | local-observed | high | Report templates not implemented. | Human-facing summaries stay auditable. |

## Plugin Classes

### 1. Source Adapter Plugins

Purpose: read one source surface and emit normalized source events plus field-level raw evidence references.

Examples:

- `runtime.codex_cli.sqlite`
- `runtime.codex_cli.rollout_jsonl`
- `runtime.claude_code.session_meta`
- `runtime.claude_code.local_jsonl`
- `runtime.claude_code.otel`
- `provider.openai.api_response`
- `provider.openai.agents_sdk_trace`
- `provider.anthropic.api_response`
- `standard.otel_genai`
- `manual.fixture_jsonl`

Required behavior:

- Declare source kind, provider/runtime, supported source versions, parser tolerance, and content contract.
- Emit structural metadata and references, not private prompt/assistant/tool content by default.
- Preserve unknown provider fields under a versioned adapter payload or raw payload reference.
- Emit missingness states explicitly when an expected capability is unavailable, disabled, redacted, or unobserved.
- Never mutate provider config, enable exporters, or perform provider calls as part of ingestion.

Adapter output contract:

```json
{
  "adapter_id": "runtime.claude_code.otel",
  "adapter_version": "0.1.0",
  "source_kind": "otel",
  "source_ref": {
    "path": "not_available",
    "url": "not_available",
    "external_id": "trace-or-session-id",
    "content_policy": "metadata_only"
  },
  "events": [],
  "observations": [],
  "raw_payload_refs": []
}
```

### 2. Extractor Plugins

Purpose: transform adapter events and payload references into normalized metric, rubric, provenance, cost, identity, and relationship observations.

Examples:

- `extractor.core.usage_tokens`
- `extractor.core.request_identity`
- `extractor.core.tool_activity`
- `extractor.provider.openai.reasoning_tokens`
- `extractor.provider.anthropic.cache_tokens`
- `extractor.runtime.claude_code.session_activity`
- `extractor.harness.model_role.profile_consistency`
- `extractor.domain.benchmark.rubric_dimensions`

Required behavior:

- Consume only declared adapter inputs and registry metadata.
- Produce observation rows with `metric_id`, `entity_ref`, `granularity`, `value`, `value_type`, `status`, evidence, confidence, reliability, and provenance.
- Keep derivations explicit: measured, estimated, derived, inferred, or unavailable.
- Emit one observation per dimension where a value can vary independently.
- Avoid any canonical aggregate quality field named `score.overall`.

Extractor output contract:

```json
{
  "extractor_id": "extractor.harness.model_role.profile_consistency",
  "extractor_version": "0.1.0",
  "inputs": ["runtime.codex_cli.rollout_jsonl"],
  "observations": [
    {
      "metric_id": "harness.model_role.profile_consistency.status",
      "entity_ref": {"entity_type": "run", "entity_id": "run-001"},
      "granularity": "run",
      "status": "derived",
      "value_type": "categorical",
      "value": "matched",
      "evidence": [],
      "confidence": "medium",
      "reliability": {"mode": "derived_from_config_and_run_record"}
    }
  ]
}
```

### 3. View / Report Plugins

Purpose: render query results and registry declarations into human or machine reports.

Examples:

- `view.coverage.provider_capability_matrix`
- `view.cost.usage_and_estimates`
- `view.quality.rubric_dimension_matrix`
- `view.routing.requested_vs_effective`
- `view.privacy.content_contract_audit`
- `view.harness_design.profile_comparison`

Required behavior:

- Consume normalized query results and registry metadata only.
- Surface missingness, evidence class, confidence, reliability, and content contract in report output.
- Never parse provider-specific raw payloads directly unless also acting as a declared extractor.
- Never compute hidden metrics that are absent from the registry.
- May compute display-only rollups, but rollups must declare input metrics, formula, caveats, and non-canonical status.

## Plugin Manifest Shape

Each plugin ships one manifest. The manifest is the single declaration source for capability, privacy, fixtures, produced metrics, and compatibility.

```yaml
plugin_id: runtime.claude_code.otel
plugin_type: source_adapter
version: 0.1.0
schema_version: telemetry-plugin-manifest/v1
owner: gsd-modifier
status: research

runtime_support:
  providers: [anthropic]
  runtimes: [claude_code]
  source_kinds: [otel]
  requires_live_call: false
  mutates_provider_config: false
  quota_consuming: false

capabilities:
  emits_entities: [session, run, turn, model_call, tool_call]
  emits_metrics:
    - core.usage.input_tokens
    - core.usage.output_tokens
    - runtime.claude_code.cost.approximate_usd
  reads_content: false
  reads_metadata: true
  reads_raw_api_body: false
  supports_redaction: true
  supports_incremental_ingest: true
  supports_rebuild: true

content_contract:
  mode: metadata_only
  allowed_fields: [timestamps, ids, token_counts, event_names, provider_names]
  forbidden_fields: [prompt_text, assistant_text, tool_arguments, tool_outputs, file_contents, raw_api_body]
  raw_payload_policy: reference_only
  retention_policy: operator_defined

metric_namespace:
  prefixes_produced: [core.usage, runtime.claude_code]
  external_mappings:
    - standard: otel_genai
      version: declared_by_source
      keys: [gen_ai.usage.input_tokens, gen_ai.usage.output_tokens]

evidence_policy:
  allowed_evidence_classes: [verified-doc, local-observed, inferred, deferred]
  default_confidence: medium
  reliability_modes: [measured, approximate, derived, not_exposed]

fixtures:
  required:
    - name: minimal_valid_event
      content_safety: synthetic
    - name: redacted_content_event
      content_safety: synthetic
    - name: missing_optional_fields
      content_safety: synthetic
    - name: malformed_or_unknown_field
      content_safety: synthetic

compatibility:
  core_schema_min: model-benchmark-run/v1
  observation_schema_min: telemetry-observation/v1
  registry_api_min: telemetry-plugin-registry/v1
```

## Capability Declarations

Capability declarations must separate declared support from observed evidence.

Fields:

- `capability_id`: stable namespaced capability, for example `provider.openai.api.usage.reasoning_tokens`.
- `source_kind`: `api_response`, `agents_sdk_trace`, `otel_genai`, `cli_harness`, `local_artifact`, `hook_event`, `billing_aggregate`, `manual_fixture`.
- `provider` and `runtime`: optional but explicit when known.
- `granularity`: session, run, task, turn, model_call, tool_call, span, file_diff, config_profile, intervention_window.
- `availability_status`: `available`, `partially_available`, `not_exposed`, `not_enabled`, `redacted`, `requires_consent`, `requires_live_call`, `not_applicable`, `unknown`.
- `evidence_class`: from the orchestration taxonomy.
- `source_path_or_url`: local path, official URL, or `not_available`.
- `citation_or_command`: command or doc citation.
- `retrieved_or_observed_at`: timestamp or date.
- `confidence`: `high`, `medium`, `low`.
- `gaps`: known caveats.

Provider capability declarations must not imply that a field was observed in a particular run. Run observations must carry their own evidence and missingness state.

## Metric Layers

### Base-Core Metrics

Base-core metrics are provider-neutral and should be stable enough for cross-runtime reports. They are declared under `core.*`.

Recommended base-core namespaces:

- `core.identity.requested_model`
- `core.identity.effective_model`
- `core.identity.requested_reasoning_effort`
- `core.identity.effective_reasoning_effort`
- `core.usage.input_tokens`
- `core.usage.cached_input_tokens`
- `core.usage.output_tokens`
- `core.usage.reasoning_tokens`
- `core.usage.tool_result_tokens`
- `core.usage.initialization_tokens`
- `core.cost.estimated_usd`
- `core.cost.observed_usd`
- `core.cost.aggregate_allocated_usd`
- `core.routing.service_tier_requested`
- `core.routing.service_tier_effective`
- `core.tool.requested_count`
- `core.tool.executed_count`
- `core.tool.error_count`
- `core.trace.trace_id`
- `core.trace.parent_trace_id`
- `core.privacy.content_contract`
- `core.evidence.confidence`

Core metrics may be absent, not exposed, or derived for a provider. They must not be backfilled with fake zeros.

### Provider Plugins

Provider plugins own provider/API-specific denominator and payload semantics. They may map into `core.*`, but they also retain provider namespaces.

Examples:

- `provider.openai.usage.input_tokens_details.cached_tokens`
- `provider.openai.usage.output_tokens_details.reasoning_tokens`
- `provider.openai.routing.service_tier_effective`
- `provider.openai.http.x_request_id`
- `provider.anthropic.usage.cache_creation_input_tokens`
- `provider.anthropic.usage.cache_read_input_tokens`
- `provider.anthropic.http.request_id`
- `provider.anthropic.rate_limit.input_tokens_remaining`

Rule: provider metrics can feed base-core observations only through declared mapping logic with evidence and caveats. If denominator semantics differ, store both raw provider metric and normalized interpretation.

### Runtime Plugins

Runtime plugins describe CLI/harness surfaces, not raw provider APIs.

Examples:

- `runtime.codex_cli.sqlite.session_id`
- `runtime.codex_cli.rollout_jsonl.model_requested`
- `runtime.codex_cli.rollout_jsonl.reasoning_requested`
- `runtime.claude_code.session_meta.active_time_minutes`
- `runtime.claude_code.otel.cost_approximate_usd`
- `runtime.claude_code.hook.tool_event_count`

Rule: runtime metrics can explain execution shape and local routing evidence, but they must not be treated as provider API truth unless a provider request ID or API payload evidence is actually exposed.

### Harness And Domain Plugins

Harness/domain plugins describe benchmark design, task structure, evaluation, and local experiment semantics.

Examples:

- `harness.model_role.profile_consistency.status`
- `harness.model_role.candidate_profile.family`
- `harness.model_role.intervention_window.id`
- `harness.execution.subagent_count`
- `domain.benchmark.task.expected_artifact_count`
- `domain.benchmark.rubric.correctness`
- `domain.benchmark.rubric.instruction_following`
- `domain.benchmark.rubric.evidence_quality`
- `domain.benchmark.rubric.privacy_compliance`
- `domain.benchmark.rubric.implementation_completeness`

These metrics must be added through declarations and observations, not through core schema columns.

## Adding Harness-Design Metrics Without Core Schema Changes

Harness-design metrics should use this path:

1. Add a manifest for `extractor.harness.<domain>.<name>`.
2. Declare produced `harness.*` or `domain.*` metric IDs with value type, granularity, dimensions, and allowed missingness states.
3. Emit `metric_observation` rows linked to existing entities such as task, run, task_instance, agent_role, intervention_window, or artifact.
4. Store any plugin-specific details in `dimensions_json`, `value_json`, or a namespaced payload reference.
5. Add fixtures proving normal, missing, malformed, and privacy-sensitive cases.
6. Add view/report plugins that consume the declared metrics.

Core schema only needs a stable observation envelope:

```json
{
  "observation_id": "obs-uuid",
  "metric_id": "harness.model_role.profile_consistency.status",
  "entity_type": "run",
  "entity_id": "run-001",
  "granularity": "run",
  "dimensions": {
    "candidate_profile": "55-medium",
    "task_id": "EXEC-001"
  },
  "value_type": "categorical",
  "value": "matched",
  "unit": "not_applicable",
  "status": "derived",
  "evidence_class": "local-observed",
  "source_path_or_url": "tooling/codex/model_benchmark/schema.py",
  "command_or_citation": "validate_run_record profile consistency",
  "confidence": "medium",
  "reliability": {
    "mode": "derived",
    "basis": "requested profile compared with normalized run fields"
  },
  "content_contract": "metadata_only",
  "plugin_id": "extractor.harness.model_role.profile_consistency",
  "plugin_version": "0.1.0"
}
```

## Missingness Behavior

Missing values are semantic states, not zeroes, empty strings, or omitted fields.

Recommended status vocabulary:

- `measured`: directly observed from a source field or event.
- `estimated`: computed from sourced rates or formulas.
- `derived`: computed from observed fields without claiming direct provider exposure.
- `inferred`: reasoned from indirect evidence and should be treated as lower confidence.
- `not_available`: generic unavailable state, mainly for backward compatibility.
- `not_exposed`: provider/runtime does not expose the field on this surface.
- `not_enabled`: surface exists but telemetry or capture was not enabled.
- `redacted`: source intentionally removed or suppressed content/value.
- `not_collected`: run was captured without that source or plugin.
- `not_applicable`: metric does not apply to this entity/provider/surface.
- `deferred_live_call`: confirmation would require a live/potentially paid call.
- `unknown`: parser cannot determine state.

Reports must distinguish `not_exposed`, `not_enabled`, `redacted`, `not_collected`, and `unknown`. They answer different operational questions.

## Privacy And Content Contracts

Every adapter, extractor, metric, and report must declare a content contract.

Recommended modes:

- `no_content_access`: plugin does not read prompts, assistant text, tool arguments, tool outputs, file contents, or raw API bodies.
- `metadata_only`: reads identifiers, timestamps, provider/runtime names, counts, status fields, and structural event names.
- `derived_features_only`: reads content transiently to emit derived features, but stores no raw content.
- `content_hash_or_length_only`: may store hashes, byte/token lengths, or redaction markers.
- `redacted_content_reference`: stores references to redacted artifacts, not inline raw content.
- `raw_content_allowed`: only with explicit operator consent and separate retention controls; not allowed for this research package.
- `raw_api_body_gated`: requires explicit provider/runtime telemetry flag and consent; default should be reference-only or unavailable.

Default rule: no raw prompt text, assistant text, tool arguments, tool outputs, file contents, or raw API bodies in metric observation rows.

## Metric Namespace Rules

Metric IDs are lowercase dotted names:

```text
<layer>.<owner_or_surface>.<concept>[.<subconcept>]
```

Allowed top-level layers:

- `core`
- `provider`
- `runtime`
- `standard`
- `harness`
- `domain`
- `view`
- `legacy`

Rules:

- `core.*` cannot contain provider-specific field names.
- `provider.<provider>.*` owns raw provider semantics.
- `runtime.<runtime>.*` owns CLI or local harness semantics.
- `standard.otel_genai.*` may mirror semantic-convention names, with version metadata.
- `harness.*` owns benchmark harness mechanics.
- `domain.*` owns task/rubric/domain evaluation metrics.
- `view.*` is display-only unless backed by declared source metrics and formula metadata.
- `legacy.*` contains migration shims such as `legacy.score.overall`; it must not be used as canonical quality truth.

Metric declarations must include value type, unit, allowed statuses, dimensions, content contract, owner plugin, and external mappings if any.

## Evidence And Reliability Semantics

Every observation should include both evidence and reliability.

Evidence fields:

- `evidence_class`: orchestration taxonomy value.
- `source_path_or_url`: path, URL, or `not_available`.
- `command_or_citation`: command, line citation, doc citation, or fixture name.
- `observed_at` or `retrieved_at`.
- `raw_provider_field`: optional namespaced raw field.
- `raw_payload_ref`: optional reference, with privacy policy.

Reliability fields:

- `confidence`: `high`, `medium`, or `low`.
- `reliability_mode`: `direct_field`, `documented_field`, `aggregate`, `approximate`, `estimated_from_pricing`, `derived_from_config`, `derived_from_trace`, `self_reported`, `manual_label`, `fixture`, `unknown`.
- `independence`: `provider_emitted`, `runtime_emitted`, `harness_emitted`, `evaluator_emitted`, `manual`, `inferred`.
- `freshness`: retrieval or observation timestamp and source version when available.
- `comparability_status`: `comparable`, `provider_semantics_differ`, `surface_semantics_differ`, `partial`, `not_comparable`, `unknown`.

Provider parity reports should compare reliability and availability. They should not imply equal measurement quality just because two plugins emit the same `core.*` metric.

## Golden Fixture Requirements

Every plugin must ship content-safe golden fixtures before being considered implementation-ready. "Golden" means the fixture has a stable expected normalized output checked into tests, including expected missingness, redaction, evidence, confidence, reliability, and namespace behavior.

Adapter golden fixtures:

- minimal valid source event or record
- missing optional fields
- missing required identity
- unknown future field
- malformed line or parse failure
- redacted sensitive content marker
- duplicate or out-of-order event where relevant
- version mismatch

Extractor golden fixtures:

- direct measured value
- estimated value with sourced formula
- derived value with input observations
- unavailable/not_exposed value
- redacted value
- conflicting source values with reliability ordering
- provider denominator mismatch where relevant

View/report golden fixtures:

- full coverage case
- partial coverage case
- asymmetric provider case
- all-missing case
- mixed confidence case
- legacy `score.overall` input proving it is not treated as canonical
- multidimensional rubric input proving no overall score is required

Fixture content safety:

- Use synthetic or explicitly consent-safe data.
- Do not include private prompts, assistant text, tool arguments, tool outputs, raw API bodies, or file contents.
- Include only structural fields, invented IDs, invented counts, and redaction markers.

First golden fixture set:

1. `codex_sqlite_minimal_thread`: synthetic SQLite rows for `threads` and `thread_spawn_edges`, expected session/subagent entities and `runtime.codex_cli.sqlite.*` observations.
2. `codex_rollout_redacted_stream`: synthetic JSONL records for `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted`, expected turns/tool/runtime response items with all content fields redacted or length/hash-only.
3. `manual_run_with_rubric_dimensions`: benchmark run JSONL plus rubric observation JSONL, expected `rubric_observations` for multiple dimensions and no canonical `score.overall`.
4. `provider_denominator_mismatch`: synthetic OpenAI/Anthropic usage records proving cache/reasoning token mappings preserve provider raw metrics and normalized caveats.
5. `report_uncertainty_matrix`: normalized observations with mixed measured/derived/redacted/not_exposed states, expected report output that surfaces uncertainty instead of dropping rows.

## Multidimensional Rubric Observation Storage

Rubric observations should be one-to-many records linked to run, task, candidate profile, evaluator, and rubric version. Do not store or require `score.overall`.

Recommended record:

```json
{
  "rubric_observation_id": "rubric-obs-uuid",
  "run_id": "run-001",
  "task_id": "EXEC-001",
  "candidate_profile": "55-medium",
  "rubric_id": "domain.benchmark.rubric.v1",
  "rubric_dimension_id": "domain.benchmark.rubric.evidence_quality",
  "dimension_label": "evidence_quality",
  "scale": {
    "type": "ordinal",
    "min": 1,
    "max": 5,
    "anchors_ref": "rubric:v1:evidence_quality"
  },
  "value": 4,
  "status": "measured",
  "evaluator": {
    "evaluator_type": "human_or_model_or_rule",
    "evaluator_id": "not_available",
    "independence": "not_available"
  },
  "evidence": [
    {
      "evidence_class": "local-observed",
      "source_path_or_url": "not_available",
      "command_or_citation": "fixture_or_review_note",
      "confidence": "medium"
    }
  ],
  "content_contract": "derived_features_only",
  "gaps": ["No canonical overall score is stored."]
}
```

Rubric report plugins may compute display rollups such as means by dimension, coverage by evaluator, or profile deltas, but those rollups are `view.*` outputs. They are not stored as canonical `score.overall`.

## Cross-Review For Plugin Extensibility Gaps

### Lane 01 Available

Plugin extensibility implications:

- Registry/store/query parity is a plugin contract requirement, not just a storage concern. Adapters and extractors should emit only declared `metric_id`, `rubric_id`, `source_kind`, `predicate`, and namespace values.
- Reflect's `content_contract` precedent should become a manifest field for every adapter/extractor/report plugin, but Reflect workflow loop names must remain out of core plugin taxonomy.
- Role-split provenance should attach to plugin output: adapters are `observed_by`, extractors are `extracted_by`, evaluators are `evaluated_by`, reports are `written_by`.
- Report plugins must preserve uncertainty and missingness rather than sanitizing rows out of the view.
- Reflect precedent remains `repo-precedent`; it supports invariants and seams, not provider truth or final table shape.

Coordinator/reviewer critique needed:

- Decide whether registry parity is enforced at manifest validation time, rebuild time, query time, report time, or all four.
- Decide how much of Reflect's status vocabulary to import versus rename for benchmark semantics.

### Lane 02 Available

Plugin extensibility implications:

- Codex requires multiple source adapters: `runtime.codex_cli.sqlite_index`, `runtime.codex_cli.rollout_stream`, `runtime.codex_cli.config_snapshot`, and deferred `runtime.codex_cli.otel_live`.
- The SQLite adapter should emit session/thread/subagent graph, rollout path, effective model/reasoning, sandbox/approval, token aggregate, and git observations. It should not read or persist sensitive `first_user_message` or title-like content by default.
- The rollout adapter should emit turns, runtime response items, tool-call structures, compaction markers, token observations, rate-limit snapshots, subagent routing/status, sandbox/approval snapshots, and redacted payload references.
- The config adapter should emit configured/default/requested observations and must not overwrite effective runtime evidence from SQLite/JSONL.
- The OTel adapter must remain `deferred_live_call` / fixture-gated until a controlled local collector run proves emitted payload shape.
- `runtime_response_item` needs either a first-class entity/table binding or a namespaced observation family because `response_item` is not proven to equal a provider `model_call`.

Coordinator/reviewer critique needed:

- Decide whether `runtime_response_item` becomes a core table from Lane 05 or remains adapter-specific until non-Codex evidence needs it.
- Decide whether first implementation must include a Claude fixture too, to avoid Codex-shaped adapter APIs.

### Lane 03 Available

Plugin extensibility implications:

- Claude requires distinct adapters for local session-meta aggregates, local JSONL, documented OTel, and optional hook/plugin capture.
- Local session-meta should emit aggregate substitute/process observations only; it is not a stable official schema and cannot become core.
- Local JSONL requires line-oriented tolerant parsing, parse diagnostics, unknown-field retention, source path/line references, and redaction state.
- Claude hook/plugin capture must be modeled as capture provenance and consent scope. Claude Code plugins/skills are runtime features under observation, not the same thing as this benchmark's plugin registry.
- Raw API bodies are a gated sensitive attachment mode. A plugin may declare `raw_api_body_gated`, but default storage should use references plus redaction/retention policy and should not inline raw body content.
- Thinking summaries, facets, compaction summaries, and session-meta aggregates are derived/substitute signals; rubric/evaluator plugins must not treat them as reasoning tokens or quality truth.

Coordinator/reviewer critique needed:

- Align final content contract enum names with Claude hook/raw-body realities.
- Decide whether hook reducers are source adapters, privacy pre-processors, or both.

### Lane 04 Available

Plugin extensibility implications:

- API/trace adapters must be separate from CLI/harness adapters. `provider.openai.api_response`, `provider.openai.agents_sdk_trace`, `provider.anthropic.api_response`, `runtime.claude_code.otel`, and `standard.otel_genai` should remain distinct source kinds.
- OpenAI Agents SDK traces should be a first-class adapter source for traces/spans/tool calls/handoffs/guardrails/provider calls, but SDK span taxonomy should not become canonical schema.
- OTel GenAI should be an external mapping/export/view vocabulary with convention version/stability metadata, not an internal schema dependency.
- Provider token plugins must preserve denominator semantics: OpenAI cached tokens, Anthropic cache creation/read tokens, OpenAI reasoning tokens, missing Anthropic reasoning-token counter, and cache rate-limit inclusion rules are not interchangeable.
- Cost plugins must support `provider_reported`, `aggregate_allocated`, `estimated`, `approx_cli`, and `not_exposed`; per-request dollars should not be fabricated from token fields.
- Tool plugins must distinguish requested tools, executed tools, server/built-in tools, MCP tools, function tools, harness tools, handoffs, and guardrails.
- Retry and rate-limit plugins must separate documented policy, observed attempts, headers, reset values, and retry-after signals.

Coordinator/reviewer critique needed:

- Decide exact `core.*` versus `provider.*` mappings for cache/reasoning tokens and tool-call categories.
- Decide whether OpenAI trace grading/evals become rubric extractors, evaluator plugins, or a separate adapter-plus-extractor pair.

### Lane 05 Available

Plugin extensibility implications:

- Lane 05's repaired recommendation means plugins should target a relational query cache with first-class entities, edges, metric observations, rubric observations, cost estimates, artifacts, registries, and rebuild runs, while JSONL remains durable evidence/import/export.
- Plugin manifests must declare `metric_id`, `rubric_id`, `predicate`, `source_kind`, `provider namespace`, `content_contract`, privacy class, missingness states, raw artifact reference policy, and fixture coverage.
- Rebuild must validate that all adapter/emitter outputs are declared. Undeclared metrics, predicates, source kinds, provider namespaces, and rubric dimensions should be diagnostics or hard failures based on mode.
- View/report plugins should receive registry version/hash and source-set hash with query results so reports cannot silently drift from the rebuild that produced the data.
- Golden fixtures should include hierarchy, missingness, subagents, compaction, Codex SQLite index, Codex rollout structure, token accounting, multidimensional rubric observations, malformed JSONL diagnostics, and rebuild parity.

Coordinator/reviewer critique needed:

- Decide whether Lane 05 Option B is accepted before naming final plugin APIs around its tables.
- Decide whether `telemetry_events` is optional replay/debug infrastructure or required adapter output.
- Decide whether registry manifests live beside code, in SQLite `registries`, in JSONL evidence ledgers, or all three.

## Open Gaps For Coordinator

1. Reconcile Lane 02's Codex adapter split with final source-kind names, fixture names, and whether `runtime_response_item` is core or adapter-owned.
2. Reconcile Lane 05's storage recommendation with final table names, index strategy, registry hash/version storage, raw artifact reference policies, and optional/required `telemetry_events`.
3. Existing `score.overall` summary tests need a migration plan to multidimensional rubric reports.
4. The final package should define canonical enum names for missingness, reliability, confidence, content contract, cost evidence mode, and comparability so adapters do not drift.
5. The final package should decide whether plugin manifests are YAML, JSON, Python module metadata, or generated registry rows. YAML is readable; JSON is easier to validate; Python metadata is easier to package but weaker as a static audit artifact.
6. The final package should decide whether the first slice includes only Codex local adapters or includes a minimal Claude local fixture to test provider-neutrality early.

## First Implementation Recommendation

From a plugin perspective, the first slice should not start with every provider. Recommended path, subject to coordinator critique: implement the smallest registry-backed path that proves the protocol end to end without provider mutation:

1. Add a static plugin manifest validator for `telemetry-plugin-manifest/v1`.
2. Add a metric/rubric declaration registry with hash/version output that Lane 05's rebuild/query flow can record.
3. Add synthetic golden fixtures for `codex_sqlite_minimal_thread`, `codex_rollout_redacted_stream`, and `manual_run_with_rubric_dimensions`.
4. Implement two read-only Codex source adapters against fixtures first: `runtime.codex_cli.sqlite_index` and `runtime.codex_cli.rollout_stream`.
5. Implement one core extractor, `extractor.core.usage_tokens`, and one harness extractor, `extractor.harness.model_role.profile_consistency`.
6. Implement one rubric extractor/report pair that writes and renders multidimensional rubric observations without `score.overall`.
7. Implement one uncertainty-first report, `view.coverage.provider_capability_matrix`, that proves missingness, evidence class, confidence, reliability, and content contract survive the pipeline.

Evidence: inferred from Lane 02's Codex source split, Lane 05's entity/edge/observation recommendation, current local benchmark tests, and Lane 01's registry parity precedent. Confidence: medium-high. Gap: final table names and Python API shape still require coordinator synthesis.

## Decision Boundary

Implementation-ready recommendations, pending coordinator acceptance of Lane 05 storage direction:

- Use manifest-declared adapter, extractor, and view/report plugins.
- Keep core metrics provider-neutral and add provider/runtime/harness/domain metrics through namespaced declarations.
- Store all metric and rubric outputs as observations with evidence, confidence, missingness, reliability, and content contract.
- Treat `score.overall` as legacy/report-only, not canonical.
- Require synthetic/privacy-safe golden fixtures for every plugin.

Deferred until high-reasoning coordinator/reviewer synthesis:

- Final Codex-specific capability declarations and source-kind IDs.
- Final table/index names.
- Registry storage format and registry hash enforcement.
- Exact migration path from current JSONL run records to observation-backed reports.
- Whether `runtime_response_item`, `telemetry_events`, and evaluator/rubric plugins are core concepts or implementation-layer conveniences.
