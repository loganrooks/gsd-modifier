# Lane 05 - Ontology And Storage Options

Run timestamp: `20260424T043427Z`
Lane: `05-ONTOLOGY-STORAGE-OPTIONS`
Write target: `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/05-ONTOLOGY-STORAGE-OPTIONS.md`

## Scope And Evidence Boundary

This lane designs ontology and storage options for the model-role benchmark telemetry substrate. It did not mutate provider configuration, run live provider/API calls, enable telemetry exporters, inspect private transcript content, or touch files outside this artifact.

The storage design below treats JSONL and raw local/provider artifacts as evidence inputs. SQLite is a rebuildable query cache and report substrate, not the permanent source of truth for private transcripts or provider-specific raw bodies.

## Evidence Register

| Evidence class | Source path / URL | Command / citation | Confidence | Gaps | Ontology / storage implication |
| --- | --- | --- | --- | --- | --- |
| `local-observed` | `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md` | `sed -n '1,240p' .../ORCHESTRATION.md` | High | None for Lane 05 scope. | Core ontology cannot contain provider-only field names; every material claim needs evidence class, source, command/citation, confidence, and gaps. |
| `local-observed` | `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/LANE-SPECS-AND-PROMPTS.md` | `sed -n '1,260p' .../LANE-SPECS-AND-PROMPTS.md` | High | None for Lane 05 scope. | Lane 05 must compare event-first and entity/edge/observation designs, include SQLite tables and rebuild behavior, and cross-review lanes 01-04 when present. |
| `repo-precedent` | `01-REFLECT-INHERITANCE-REVIEW.md` | Available lane artifact reviewed structurally. | High for recorded lane findings; medium as design authority. | Reflect remains precedent, not authority. | Adopt registry/store/query parity, semantic missingness, role-split provenance, and privacy/content contracts; reject Reflect loop names and `score.overall` as benchmark core. |
| `verified-doc` plus `local-observed` via lane | `02-CODEX-EXPOSURE.md` | Completed strict self-audit artifact reviewed structurally. | High for observed local SQLite/JSONL field presence; medium for future schema stability and OTel emitted schema. | Codex OTel emitted payload is deferred; response items are not proven one-to-one model calls; cost dollars are not directly observed locally. | Storage needs Codex-specific adapter payloads for `threads`, `thread_spawn_edges`, rollout `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted`; effective model/reasoning, sandbox, approval, git, subagents, compaction, token, and rate-limit observations should map into provider-neutral entities/observations. |
| `verified-doc` plus `local-observed` via lane | `03-CLAUDE-EXPOSURE.md` | Available lane artifact reviewed structurally. | Medium-high | Local Claude file schemas are undocumented; OTel not exercised locally. | Storage needs tolerant line-oriented ingestion, raw artifact references, source diagnostics, namespaced provider payloads, and derived/substitute signal labeling. |
| `verified-doc` plus `inferred` via lane | `04-API-AGENTS-TRACE-SURFACES.md` | Available lane artifact reviewed structurally. | High for documented API/trace fields; medium for unsampled exports. | No live trace/API export sampled. | Store traces/spans/model calls/tool calls/rate-limit/retry/cost as observations with source kind and provider namespace. |
| `local-observed` | `tooling/codex/model_benchmark/schema.py` | `sed -n '1,260p' tooling/codex/model_benchmark/schema.py` | High | Current schema is JSON-record-first and narrower than target ontology. | Preserve existing fields as compatibility/export view: `run_id`, `task_id`, `candidate_profile`, requested/effective model/reasoning, usage status, telemetry features. |
| `local-observed` | `tooling/codex/tests/test_model_benchmark.py` | `sed -n '1,260p' tooling/codex/tests/test_model_benchmark.py` | High | Tests still include `score.overall`; orchestration says target must not depend on it. | Store rubric observations one-to-many and treat `score.overall` as legacy/simple report projection only. |

## Cross-Review Status

| Lane | Status | Ontology implication | Coordinator revisit |
| --- | --- | --- | --- |
| Lane 01 - Reflect inheritance | Reviewed | Strong support for registry/store/query parity, missingness states, field-level provenance, and report views over query contracts. | Verify final schema does not import Reflect workflow loop names as core benchmark entities. |
| Lane 02 - Codex exposure | Reviewed after dependency repair | Confirms a split Codex adapter shape: SQLite is the session/thread/subagent index; rollout JSONL is the event stream for turns, response items, tool calls, compaction, token usage, rate limits, sandbox/approval, and subagent routing. `response_item` should not be assumed to equal a provider model call without correlation. | Revisit exact OTel emitted schema only after an approved local collector fixture; do not infer dollar cost from local token/quota fields. |
| Lane 03 - Claude exposure | Reviewed | Requires raw artifact references, tolerant JSONL ingestion, source diagnostics, redaction states, hook/plugin provenance, and separation between raw reasoning access and substitute signals. | Confirm privacy/content contract vocabulary with Lane 06. |
| Lane 04 - API/Agents/trace surfaces | Reviewed | Requires generic traces/spans plus provider calls, request IDs, rate limits, retries, service tier, tool-call category, cost evidence mode, and OTel mapping metadata. | Confirm final adapters do not collapse API traces and CLI/harness traces into one source kind. |

## Dependency Repair Review

The prior Lane 05 artifact partially relied on assumptions because Lane 02 was not available. It marked Codex cross-review as pending, used generic Codex-ready table names, and left exact Codex fixture fields unresolved.

After reading completed strict self-audits for Lanes 01-04, the main changes are:

- Lane 02 is no longer pending. Codex ontology mapping now has concrete local evidence: `~/.codex/state_5.sqlite` supplies thread/session metadata, `thread_spawn_edges`, configured/effective model and reasoning fields, sandbox/approval, token aggregate, git metadata, and rollout paths; rollout JSONL supplies `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted` records.
- The model now needs an explicit `runtime_response_items` concept or equivalent observation namespace because Lane 02 warns that a Codex `response_item` is not necessarily one provider model call.
- Session/run cardinality remains as previously designed, but the evidence is stronger: Codex threads and spawn edges, Claude sidechains/subagents, and OpenAI trace/span groups all support many-to-many correlation rather than session-as-run identity.
- The fixture plan is updated to include Codex SQLite and rollout JSONL structural fixtures instead of a generic "Lane 02 pending" note.

Remaining gaps:

- Codex OTel emitted span/log/metric schema remains deferred; official docs prove config knobs, not exact payload shape.
- Future Codex and Claude local schemas may drift because both local stores are implementation artifacts rather than stable public telemetry APIs.
- Cost dollars remain unavailable from Codex local SQLite/JSONL; API-equivalent estimates must stay separate from provider-reported or billing-truth cost.

## Design Goals

The substrate should:

- support sessions, work units, task definitions, task instances, runs, turns, model calls, tool calls, subagents, file changes, metric observations, rubric observations, cost estimates, artifacts, and entity edges
- preserve requested versus effective settings
- keep provider-specific field names out of core tables except as namespaced payloads or mapping rows
- encode missingness as semantic state, not zero
- preserve raw artifact references without copying private prompts, assistant text, tool arguments, tool outputs, raw bodies, or transcript content by default
- support rebuilds from JSONL, local metadata, OTel exports, API trace exports, manual evidence rows, and benchmark run JSON
- make query/report views consume the same registry and store metadata used by rebuild

Evidence basis: `local-observed` orchestration and lane spec files, reviewed with `sed`; `repo-precedent` Lane 01; `verified-doc`/`local-observed` findings summarized in Lanes 02, 03, and 04. Confidence: high for the required shape of this lane; medium for provider-specific mappings that depend on undocumented local SQLite/JSONL schemas or future OTel fixtures. Gap: exact Codex OTel emitted payload remains pending.

## Required Question Answers

| Required question | Answer | Evidence class and source | Confidence | Gaps and implications |
| --- | --- | --- | --- | --- |
| Task definition versus task instance | A task definition is the reusable benchmark contract: task ID, version, prompt/input specification reference, expected artifact shape, and rubric reference. A task instance is one assigned occurrence of that definition for a specific input set/case, work unit, candidate profile, or execution context. | `local-observed`: lane spec requires this distinction; `local-observed`: current `schema.py` has `task_id` and `candidate_profile` but no separate task instance table. | High for design need. | Existing JSON records can backfill `task_instance_id` deterministically from `task_id`, candidate profile, input-set metadata when present, and run ordinal; missing input-set data must be `unknown`, not invented. |
| Exact definition of run | A run is one attempt to execute one task instance under one candidate profile and requested runtime/model/reasoning configuration, producing an outcome status and zero or more model calls, tool calls, file changes, metric observations, rubric observations, and cost estimates. | `local-observed`: current `validate_run_record()` requires `run_id`, `task_id`, `candidate_profile`, model, reasoning, runtime provider, status, and usage; Lane 04 separates model calls and traces from benchmark runs. | High. | A run is not identical to a provider API call, trace, session, or GSD phase. Those attach through edges/foreign keys. |
| Can one session contain many runs? | Yes. A CLI, API trace group, or local work session may contain many benchmark runs, especially batch executions or resumed evaluator work. `sessions -> turns -> runs` is one-to-many in the common case. | `verified-doc`/lane summary: Lane 04 traces can group workflow spans; `local-observed`: Lane 03 local sessions aggregate many messages/tools. | High. | Adapters must not assume session ID equals run ID. |
| Can one run span sessions? | Default answer: model a run with one primary session for simple queries. If an execution attempt genuinely crosses sessions, link additional sessions through `run_sessions` and `entity_edges` with `continued_in`, `observed_in`, or `derived_from`. If the resumed work changes candidate profile, task input, or execution conditions, create a new run under the same task instance instead of stretching the old run. | `local-observed` via Lane 02 Codex threads/spawn edges and rollout paths; `local-observed` via Lane 03 Claude sidechain/session fields; `verified-doc`/`inferred` via Lane 04 trace groups. | High for many-session modeling need; medium for exact cross-session run identity rules. | Implementation should require explicit continuation evidence before spanning sessions; otherwise create sibling runs under the same task instance. |
| Minimum SQLite schema without GSD overfit | Core tables should describe benchmark telemetry concepts only: artifacts, sessions, work units, task definitions, task instances, runs, run sessions, turns, model calls, runtime response items, tool calls, subagents, file changes, metric observations, rubric observations, cost estimates, entity edges, registries, and rebuild runs. GSD phase/milestone/plan identifiers belong in generic `work_units`, artifacts, domain plugin payloads, or edges, not hard-coded core columns. | `local-observed`: strict contract says core ontology must remain harness-agnostic; Lane 01 rejects Reflect/GSD loop names as benchmark core; Lane 02 requires a response-item concept distinct from model calls. | High. | Lane 06 should declare the domain plugin path for GSD-specific views. |
| JSONL versus SQLite rebuild behavior | JSONL remains durable evidence/import/export/manual ledger/fixture format. SQLite is a deterministic, deletable query cache rebuilt from registries plus source artifacts. Rebuild must preserve raw evidence, record registry/source hashes, and surface diagnostics for drift or malformed input. | `repo-precedent`: Lane 01 registry/store/query parity; `local-observed`: current benchmark has JSONL IO tests. | High. | Implementation must test rebuild idempotence and query parity before reports depend on the cache. |
| Golden fixtures | Required fixtures: hierarchy, missingness, subagents, compaction, token accounting, rubric observations, raw artifact references, malformed JSONL, rebuild parity, Codex SQLite thread/spawn-edge rows, and Codex rollout JSONL records for `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted`. | `local-observed`: strict lane contract; Lane 02 Codex local findings; Lane 03 requires tolerant JSONL parsing; Lane 04 requires token/cache/reasoning/cost separation. | High. | Fixtures should be synthetic or consent-safe and must not include private transcript content, tool arguments, tool output, or raw command output. |

## Option A - Event-First With Derived Entities

### Shape

The canonical imported record is an immutable event. Every adapter emits normalized event envelopes into `telemetry_events`; sessions, runs, calls, observations, file changes, and edges are derived by rebuild jobs.

Core idea:

- persist event envelopes in timestamp/source order
- derive entity snapshots and observation rows from event payloads
- treat JSONL import/export as the natural representation
- make SQLite primarily an event index plus materialized views

### Proposed Tables

```sql
CREATE TABLE source_artifacts (
  artifact_id TEXT PRIMARY KEY,
  source_kind TEXT NOT NULL,
  provider TEXT NOT NULL,
  source_path_or_url TEXT NOT NULL,
  retrieval_date TEXT,
  content_hash TEXT,
  privacy_class TEXT NOT NULL,
  content_contract TEXT NOT NULL,
  raw_ref TEXT,
  notes TEXT
);

CREATE TABLE telemetry_events (
  event_id TEXT PRIMARY KEY,
  artifact_id TEXT NOT NULL REFERENCES source_artifacts(artifact_id),
  source_event_id TEXT,
  source_kind TEXT NOT NULL,
  provider TEXT NOT NULL,
  event_type TEXT NOT NULL,
  event_time TEXT,
  ingest_time TEXT NOT NULL,
  sequence_index INTEGER,
  evidence_class TEXT NOT NULL,
  observed_state TEXT NOT NULL,
  confidence TEXT NOT NULL,
  redaction_state TEXT NOT NULL,
  payload_json TEXT NOT NULL,
  payload_schema TEXT,
  UNIQUE (artifact_id, sequence_index),
  UNIQUE (artifact_id, source_event_id)
);

CREATE TABLE derived_entities (
  entity_id TEXT PRIMARY KEY,
  entity_type TEXT NOT NULL,
  stable_key TEXT NOT NULL,
  first_event_id TEXT REFERENCES telemetry_events(event_id),
  last_event_id TEXT REFERENCES telemetry_events(event_id),
  attrs_json TEXT NOT NULL,
  derivation_version TEXT NOT NULL,
  UNIQUE (entity_type, stable_key, derivation_version)
);

CREATE TABLE derived_edges (
  edge_id TEXT PRIMARY KEY,
  subject_entity_id TEXT NOT NULL REFERENCES derived_entities(entity_id),
  predicate TEXT NOT NULL,
  object_entity_id TEXT NOT NULL REFERENCES derived_entities(entity_id),
  evidence_event_id TEXT REFERENCES telemetry_events(event_id),
  attrs_json TEXT NOT NULL,
  derivation_version TEXT NOT NULL
);

CREATE TABLE derived_observations (
  observation_id TEXT PRIMARY KEY,
  subject_entity_id TEXT NOT NULL REFERENCES derived_entities(entity_id),
  metric_id TEXT NOT NULL,
  value_json TEXT,
  unit TEXT,
  status TEXT NOT NULL,
  evidence_event_id TEXT REFERENCES telemetry_events(event_id),
  attrs_json TEXT NOT NULL,
  derivation_version TEXT NOT NULL
);
```

### Strengths

- Best fit for JSONL-heavy sources and append-only trace exports.
- Easy to re-import new provider events without first designing every entity table.
- Preserves source ordering and lets derivation logic improve over time.
- Useful when provider exposure is unstable or unknown.

### Weaknesses

- Important benchmark concepts become derived conventions rather than visible storage contracts.
- Queries such as "all rubric observations for task instance X by evaluator Y" require reliable derivations before they are ergonomic.
- Entity identity and edge semantics can drift if adapters derive them differently.
- Harder to enforce registry/store/query parity because metric declarations can be hidden inside derivation code unless separately modeled.

### Assessment

This is a good ingestion layer, especially for raw JSONL import/export and manual evidence. It should not be the main query model for the benchmark because the benchmark already has named concepts that need durable, auditable semantics.

## Option B - Entity / Edge / Observation Relational Model

### Shape

The canonical SQLite cache stores first-class entities and first-class observations. Raw events and artifacts remain referenced and optionally indexed, but benchmark queries operate on explicit tables for sessions, work units, tasks, runs, turns, calls, file changes, observations, costs, artifacts, and edges.

Core idea:

- use stable IDs for benchmark concepts
- store provider facts as observations with evidence/provenance/status
- store flexible provider payloads in JSON columns and raw artifact refs
- keep relationship semantics in typed edges
- rebuild the SQLite cache deterministically from JSONL/source artifacts/registries

### Recommended Core IDs

| Concept | ID pattern | Notes |
| --- | --- | --- |
| `artifact_id` | `art:{source_kind}:{hash_or_slug}` | Stable reference to local file, URL, OTel export, trace export, manual evidence, benchmark JSONL, or raw body ref. |
| `session_id` | `ses:{provider_or_runtime}:{external_or_hash}` | External CLI/session ID when safely available; otherwise deterministic hash over source identity and start time. |
| `work_unit_id` | `wu:{namespace}:{slug}` | Human/workflow unit such as phase, benchmark batch, evaluation package, or lane. |
| `task_def_id` | `taskdef:{task_id}:{version}` | Stable task definition, separate from one execution attempt. |
| `task_instance_id` | `taskinst:{task_def_id}:{input_set_or_case}:{ordinal}` | Specific benchmark case or assigned task occurrence. |
| `run_id` | Existing benchmark `run_id` when present; otherwise `run:{task_instance_id}:{candidate_profile}:{attempt}` | Compatibility with current schema is required. |
| `turn_id` | `turn:{session_id}:{turn_index_or_external_uuid}` | User/assistant/tool loop unit without storing content. |
| `model_call_id` | `mc:{provider}:{external_request_or_response_id_or_hash}` | One API/model generation request or trace generation span. |
| `tool_call_id` | `tc:{provider_or_harness}:{external_tool_id_or_hash}` | Model-requested or harness-executed tool call. |
| `subagent_id` | `sub:{session_id}:{external_agent_id_or_hash}` | Local subagent/thread/task agent identity. |
| `file_change_id` | `fc:{run_or_session}:{path_hash}:{ordinal}` | Structural file-change observation, not file content. |
| `observation_id` | `obs:{subject_id}:{metric_or_rubric_id}:{source_artifact}:{ordinal}` | Deterministic where possible; can include UUID for manual notes. |
| `edge_id` | `edge:{subject}:{predicate}:{object}:{source_or_hash}` | Typed relation with provenance. |

### Proposed SQLite Tables

```sql
CREATE TABLE rebuild_runs (
  rebuild_id TEXT PRIMARY KEY,
  started_at TEXT NOT NULL,
  completed_at TEXT,
  status TEXT NOT NULL,
  schema_version TEXT NOT NULL,
  registry_version TEXT NOT NULL,
  registry_hash TEXT NOT NULL,
  source_set_hash TEXT NOT NULL,
  command TEXT,
  diagnostics_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE registries (
  registry_id TEXT PRIMARY KEY,
  registry_type TEXT NOT NULL,
  registry_version TEXT NOT NULL,
  registry_hash TEXT NOT NULL,
  source_path TEXT NOT NULL,
  declaration_count INTEGER NOT NULL,
  payload_json TEXT NOT NULL,
  UNIQUE (registry_type, registry_version, registry_hash)
);

CREATE TABLE artifacts (
  artifact_id TEXT PRIMARY KEY,
  source_kind TEXT NOT NULL,
  provider TEXT NOT NULL,
  source_path_or_url TEXT NOT NULL,
  retrieval_date TEXT,
  observed_at TEXT,
  content_hash TEXT,
  raw_ref TEXT,
  privacy_class TEXT NOT NULL,
  content_contract TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  confidence TEXT NOT NULL,
  gaps TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE (source_kind, source_path_or_url, content_hash)
);

CREATE TABLE sessions (
  session_id TEXT PRIMARY KEY,
  provider TEXT NOT NULL,
  runtime_provider TEXT NOT NULL,
  external_session_id TEXT,
  project_path_hash TEXT,
  started_at TEXT,
  ended_at TEXT,
  status TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE work_units (
  work_unit_id TEXT PRIMARY KEY,
  work_unit_type TEXT NOT NULL,
  title TEXT NOT NULL,
  parent_work_unit_id TEXT REFERENCES work_units(work_unit_id),
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE task_definitions (
  task_def_id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  task_version TEXT NOT NULL,
  title TEXT NOT NULL,
  rubric_ref TEXT,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  payload_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE (task_id, task_version)
);

CREATE TABLE task_instances (
  task_instance_id TEXT PRIMARY KEY,
  task_def_id TEXT NOT NULL REFERENCES task_definitions(task_def_id),
  work_unit_id TEXT REFERENCES work_units(work_unit_id),
  candidate_profile TEXT,
  input_set_id TEXT,
  assigned_at TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE runs (
  run_id TEXT PRIMARY KEY,
  task_instance_id TEXT REFERENCES task_instances(task_instance_id),
  primary_session_id TEXT REFERENCES sessions(session_id),
  candidate_profile TEXT NOT NULL,
  runtime_provider TEXT NOT NULL,
  requested_model TEXT NOT NULL,
  effective_model TEXT NOT NULL,
  requested_reasoning_effort TEXT NOT NULL,
  effective_reasoning_effort TEXT NOT NULL,
  status TEXT NOT NULL,
  qualitative_only INTEGER NOT NULL,
  profile_consistency_status TEXT NOT NULL,
  started_at TEXT,
  ended_at TEXT,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  schema_version TEXT NOT NULL,
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE run_sessions (
  run_id TEXT NOT NULL REFERENCES runs(run_id),
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  relation TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  confidence TEXT NOT NULL,
  payload_json TEXT NOT NULL DEFAULT '{}',
  PRIMARY KEY (run_id, session_id, relation)
);

CREATE TABLE turns (
  turn_id TEXT PRIMARY KEY,
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  run_id TEXT REFERENCES runs(run_id),
  turn_index INTEGER,
  external_turn_id TEXT,
  role TEXT NOT NULL,
  started_at TEXT,
  ended_at TEXT,
  redaction_state TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  payload_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE (session_id, turn_index)
);

CREATE TABLE model_calls (
  model_call_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES runs(run_id),
  turn_id TEXT REFERENCES turns(turn_id),
  trace_id TEXT,
  span_id TEXT,
  parent_span_id TEXT,
  provider TEXT NOT NULL,
  source_kind TEXT NOT NULL,
  operation_name TEXT,
  external_request_id TEXT,
  client_request_id TEXT,
  response_id TEXT,
  requested_model TEXT,
  effective_model TEXT,
  requested_service_tier TEXT,
  effective_service_tier TEXT,
  started_at TEXT,
  ended_at TEXT,
  status TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  provider_payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE runtime_response_items (
  response_item_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES runs(run_id),
  turn_id TEXT REFERENCES turns(turn_id),
  model_call_id TEXT REFERENCES model_calls(model_call_id),
  provider TEXT NOT NULL,
  source_kind TEXT NOT NULL,
  external_item_id TEXT,
  item_type TEXT NOT NULL,
  item_status TEXT,
  role TEXT,
  redaction_state TEXT NOT NULL,
  correlation_status TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  provider_payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE tool_calls (
  tool_call_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES runs(run_id),
  turn_id TEXT REFERENCES turns(turn_id),
  model_call_id TEXT REFERENCES model_calls(model_call_id),
  provider TEXT NOT NULL,
  tool_name TEXT,
  tool_type TEXT NOT NULL,
  requested_by TEXT,
  executed_by TEXT,
  approval_state TEXT,
  started_at TEXT,
  ended_at TEXT,
  status TEXT NOT NULL,
  redaction_state TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  provider_payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE subagents (
  subagent_id TEXT PRIMARY KEY,
  session_id TEXT REFERENCES sessions(session_id),
  parent_run_id TEXT REFERENCES runs(run_id),
  parent_turn_id TEXT REFERENCES turns(turn_id),
  external_agent_id TEXT,
  agent_role TEXT,
  model_profile TEXT,
  started_at TEXT,
  ended_at TEXT,
  status TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE file_changes (
  file_change_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES runs(run_id),
  session_id TEXT REFERENCES sessions(session_id),
  path_hash TEXT NOT NULL,
  path_display TEXT,
  change_kind TEXT NOT NULL,
  lines_added INTEGER,
  lines_removed INTEGER,
  language TEXT,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE metric_observations (
  observation_id TEXT PRIMARY KEY,
  subject_type TEXT NOT NULL,
  subject_id TEXT NOT NULL,
  metric_id TEXT NOT NULL,
  metric_namespace TEXT NOT NULL,
  value_json TEXT,
  unit TEXT,
  status TEXT NOT NULL,
  observed_state TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  source_path_or_url TEXT,
  command_or_citation TEXT,
  confidence TEXT NOT NULL,
  gaps TEXT,
  implications TEXT,
  observed_at TEXT,
  extracted_by TEXT,
  provider_payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE rubric_observations (
  rubric_observation_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES runs(run_id),
  task_instance_id TEXT REFERENCES task_instances(task_instance_id),
  rubric_id TEXT NOT NULL,
  dimension_id TEXT NOT NULL,
  evaluator_id TEXT NOT NULL,
  value_json TEXT,
  scale_json TEXT,
  status TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  confidence TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  command_or_citation TEXT,
  gaps TEXT,
  implications TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE cost_estimates (
  cost_estimate_id TEXT PRIMARY KEY,
  run_id TEXT REFERENCES runs(run_id),
  model_call_id TEXT REFERENCES model_calls(model_call_id),
  estimate_mode TEXT NOT NULL,
  currency TEXT,
  total_cost_value TEXT,
  status TEXT NOT NULL,
  rate_table_ref TEXT,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  line_items_json TEXT NOT NULL DEFAULT '[]',
  caveats TEXT,
  confidence TEXT NOT NULL
);

CREATE TABLE entity_edges (
  edge_id TEXT PRIMARY KEY,
  subject_type TEXT NOT NULL,
  subject_id TEXT NOT NULL,
  predicate TEXT NOT NULL,
  object_type TEXT NOT NULL,
  object_id TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  source_artifact_id TEXT REFERENCES artifacts(artifact_id),
  confidence TEXT NOT NULL,
  valid_from TEXT,
  valid_to TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE (subject_type, subject_id, predicate, object_type, object_id, source_artifact_id)
);
```

### Edge Semantics

`entity_edges.predicate` should use a small controlled vocabulary. Provider- or plugin-specific edges may add namespaced predicates only after registry declaration.

Recommended core predicates:

- `contains`: session contains turn; run contains model call, runtime response item, tool call, or file change.
- `executes`: run executes task instance.
- `instantiates`: task instance instantiates task definition.
- `belongs_to`: run/session/task belongs to work unit.
- `observed_in`: entity or observation observed in artifact.
- `derived_from`: observation or entity derived from event/artifact/other observation.
- `requested`: model call requested tool call or requested model/tier relation when represented as entity.
- `executed_by`: tool call executed by harness/runtime/subagent.
- `spawned`: turn/run spawned subagent.
- `parent_of`: trace/span/turn/subagent hierarchy where a richer table does not already carry the parent.
- `evaluated_by`: rubric observation evaluated by evaluator.
- `estimated_from`: cost estimate estimated from usage observations and rate table.
- `supersedes`: rebuilt observation/entity supersedes older derivation version.
- `correlates_with`: weak link across sources, such as timestamp/request-id correlation, never identity.

Rules:

- Edges are not facts without provenance. Each edge needs `evidence_class`, source artifact, confidence, and payload notes when inferred.
- `correlates_with` must not be used as identity. Promotion from correlation to identity requires a stronger predicate such as `same_as` and stronger evidence.
- Parent/child trace semantics should use explicit `parent_span_id` columns for hot path queries and duplicate into edges only for generic graph traversal.

### JSON Payload Strategy

SQLite should keep a stable relational spine and flexible JSON leaves:

- Core identity, grouping, timestamps, status, evidence, and common query fields become columns.
- Provider-specific details go in `provider_payload_json` with namespaces such as `openai.responses`, `openai_agents_sdk`, `anthropic.messages`, `claude_code.local_jsonl`, `claude_code.otel`, `codex.sqlite`, `codex.rollout_jsonl`, and `otel.gen_ai`.
- Raw content-bearing fields are not stored by default. Store `raw_ref`, content hash, redaction state, length, schema version, or body-ref pointer when policy allows.
- JSON values should be valid JSON text; readers should treat unknown keys as adapter-owned.
- Observations should store values as JSON because values can be numbers, strings, objects, vectors, or semantic missingness objects.
- Namespaced provider payloads should include adapter version and source schema guess when the source is undocumented or evolving.

Recommended missingness object for `value_json` when a scalar cannot be emitted:

```json
{
  "state": "not_exposed",
  "reason": "provider surface did not document this field",
  "source": "adapter_or_lane_id"
}
```

Allowed states should include at least `measured`, `estimated`, `derived`, `not_available`, `not_applicable`, `not_emitted`, `not_enabled`, `not_exposed`, `redacted`, `not_collected`, `deferred_live_call`, `malformed_source`, and `unknown`.

### Indexes

```sql
CREATE INDEX idx_artifacts_source ON artifacts(source_kind, provider, source_path_or_url);
CREATE INDEX idx_sessions_provider_time ON sessions(provider, started_at);
CREATE INDEX idx_runs_task_profile ON runs(task_instance_id, candidate_profile, requested_model, requested_reasoning_effort);
CREATE INDEX idx_runs_status ON runs(status, qualitative_only, profile_consistency_status);
CREATE INDEX idx_run_sessions_session ON run_sessions(session_id, relation);
CREATE INDEX idx_turns_session_index ON turns(session_id, turn_index);
CREATE INDEX idx_model_calls_trace ON model_calls(trace_id, span_id, parent_span_id);
CREATE INDEX idx_model_calls_request ON model_calls(provider, external_request_id, response_id);
CREATE INDEX idx_response_items_turn ON runtime_response_items(turn_id, item_type, correlation_status);
CREATE INDEX idx_tool_calls_run_type ON tool_calls(run_id, tool_type, status);
CREATE INDEX idx_subagents_session ON subagents(session_id, agent_role, status);
CREATE INDEX idx_file_changes_run ON file_changes(run_id, path_hash, change_kind);
CREATE INDEX idx_metric_subject ON metric_observations(subject_type, subject_id, metric_namespace, metric_id);
CREATE INDEX idx_metric_evidence ON metric_observations(evidence_class, status, confidence);
CREATE INDEX idx_rubric_run_dimension ON rubric_observations(run_id, rubric_id, dimension_id, evaluator_id);
CREATE INDEX idx_cost_run ON cost_estimates(run_id, estimate_mode, status);
CREATE INDEX idx_edges_subject ON entity_edges(subject_type, subject_id, predicate);
CREATE INDEX idx_edges_object ON entity_edges(object_type, object_id, predicate);
```

If SQLite JSON1 is available, add expression indexes only for stable, high-value payload fields after profiling. Do not depend on JSON expression indexes for core query semantics.

### Rebuild Behavior

SQLite should be rebuildable from declared sources:

1. Read adapter/metric/rubric registries and record `registry_hash` in `rebuild_runs`.
2. Read source artifact manifests: JSONL files, benchmark run JSON, OTel exports, API trace exports, local structural metadata, manual evidence rows, and raw artifact references.
3. Insert/update `artifacts` with content hash, privacy class, content contract, evidence class, confidence, and gaps.
4. Run adapters in deterministic order. Adapters emit entity upserts, observations, edges, source diagnostics, and optional normalized event rows.
5. Validate registry/store/query parity: all emitted `metric_id`, `rubric_id`, source kinds, predicates, and provider namespaces must be declared.
6. Commit into a fresh cache or staging database, then replace the active cache atomically.
7. Preserve prior raw JSONL/manual evidence files; do not edit them during rebuild.
8. Report malformed lines, missing artifacts, schema drift, undeclared metrics, duplicate IDs, and unresolved correlations as diagnostics, not silent drops.

The database may be deleted and rebuilt. The raw evidence files, registries, artifact manifests, and manual evidence JSONL are the durable source set.

## JSONL Role

JSONL remains useful as:

- import format for provider/local trace exports and benchmark run records
- export format for portable evidence packs and review handoff
- manual evidence ledger when a reviewer records a source path, URL, command/citation, confidence, gaps, and implication
- fixture format for adapters
- append-only capture surface for future hooks or local reducers

SQLite remains useful as:

- rebuildable query cache
- relational index over entities, observations, and edges
- report substrate for coverage, cost, usage, rubric, provenance, and provider-parity views
- registry/store/query parity checker

Decision boundary: JSONL is durable evidence and interchange; SQLite is the normalized, rebuildable cache. Do not make SQLite the only copy of raw or manual evidence.

Evidence basis: `local-observed` current benchmark JSONL IO tests; `repo-precedent` Lane 01 rebuild/query parity; `local-observed` via Lane 02 Codex rollout JSONL record types; `local-observed` via Lane 03 Claude local JSONL parse/field findings. Confidence: high. Gap: Codex and Claude local JSONL schemas can drift because they are not stable public telemetry APIs.

## Golden Fixtures

The first implementation should ship synthetic or consent-safe golden fixtures before ingesting real private telemetry. Fixtures should be small enough for review and should exercise both JSONL import/export and SQLite rebuild.

| Fixture | Required coverage | Evidence class and source | Confidence | Storage implication |
| --- | --- | --- | --- | --- |
| `hierarchy-basic` | One session containing two runs; each run has turns, one model call, one tool call, one artifact ref, and one metric observation. | `local-observed`: strict lane contract; Lane 04 trace hierarchy. | High | Proves session/run cardinality and hot-path indexes. |
| `run-spans-sessions` | One task instance with a run linked to primary and continuation sessions via `run_sessions`; also include a second clean run under the same task instance. | `inferred`: resume/session ambiguity from lane requirements. | Medium-high | Prevents session ID from becoming run identity. |
| `missingness-states` | Observations for `not_exposed`, `not_enabled`, `redacted`, `not_collected`, `deferred_live_call`, `not_available`, and `unknown`; no missing numeric field may become zero. | `local-observed`: orchestration missingness rule; Lane 01. | High | Validates semantic missingness in `metric_observations.value_json/status`. |
| `subagent-sidechain` | Parent session/run spawning a subagent with child tool calls and file-change observations, without transcript content. Include Codex `thread_spawn_edges`/agent fields and Claude `isSidechain`/agent fields as separate adapter payloads. | `local-observed` via Lane 02 and Lane 03. | High for fixture need; medium for exact local schema stability. | Validates `subagents` and `entity_edges.spawned` without making Codex or Claude field names core ontology. |
| `compaction-derived` | A compaction/summary marker stored as derived/substitute process signal, not quality truth and not raw reasoning. | `verified-doc` via Lane 03; orchestration. | High | Prevents compaction summaries or thinking facets from entering rubric truth. |
| `codex-rollout-structure` | Redacted records for Codex `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted`, including token usage and rate-limit snapshots but no prompt, command, stdout/stderr, tool arguments, or tool output. | `local-observed` via Lane 02. | High for field presence; medium for future stability. | Validates `runtime_response_items`, turn policy snapshots, compaction observations, token observations, and rate-limit observations. |
| `codex-sqlite-index` | Minimal `threads` and `thread_spawn_edges` rows with rollout paths, effective model/reasoning, sandbox/approval, git metadata, token aggregate, and child-thread status. | `local-observed` via Lane 02. | High for observed schema; medium for future stability. | Validates session index import, subagent graph recovery, and requested/effective separation without reading sensitive title/first-message content. |
| `token-accounting` | Input, cached input, cache creation/read when available, output, reasoning, initialization, tool-result, quota delta, rate limit, and partial cost estimate as distinct observations. Include Codex `reasoning_output_tokens` as a provider-specific source field mapped to normalized reasoning-token observation with raw field path. | `local-observed` via Lane 02; `verified-doc` via Lane 04; current schema tests. | High | Prevents provider/auth/billing flattening and API-equivalent cost confusion. |
| `rubric-multidimensional` | Multiple rubric dimensions for one run from at least two evaluator IDs; no dependency on `score.overall`. | `local-observed`: orchestration; current tests show legacy `score.overall`. | High | Validates `rubric_observations` as canonical quality storage. |
| `malformed-jsonl-diagnostic` | One malformed terminal JSONL line and one unknown provider key retained as adapter payload/diagnostic. | `local-observed` via Lane 03 local parse findings. | Medium-high | Validates tolerant parsing and source diagnostics. |
| `rebuild-parity` | Same fixture rebuilt twice yields same entity/observation/edge counts, registry hash, and query output. | `repo-precedent`: Lane 01 registry/store/query parity. | High | Makes SQLite safely rebuildable. |

## Pitfalls And Mitigations

| Pitfall | Mitigation in this design | Evidence class and source | Confidence | Remaining gap |
| --- | --- | --- | --- | --- |
| Treating Reflect as authoritative | Reflect contributes parity/provenance patterns only; GSD loop names are excluded from core schema. | `repo-precedent`: Lane 01. | High | Final synthesis should keep this boundary. |
| Designing around Codex only | Core tables remain provider-neutral even after Codex review; Codex `threads`, `thread_spawn_edges`, `turn_context`, `event_msg`, `response_item`, and `compacted` names stay in adapter payloads or fixture names, not core column names. | `local-observed` via Lane 02; `verified-doc`/`local-observed` via Lanes 03/04. | High. | Lane 06 must enforce provider namespace rules in plugin manifests. |
| Flattening provider/auth/billing | Cost, quota, rate limits, token categories, provider-reported cost, and estimates are separate observations/cost rows. | `verified-doc` via Lane 04. | High | Exact pricing/allocation policy deferred. |
| Over-trusting local logs | Local logs become artifacts with evidence class/confidence, not authoritative truth. | `local-observed` via Lane 03. | High | Fixture parser should record malformed/unknown fields. |
| Mutating config for OTel experiments | No OTel capture is required for core schema; OTel exports are optional artifacts. | `local-observed`: orchestration no-mutation policy. | High | Future experiments need explicit operator consent. |
| Persisting sensitive transcript content | Store refs, hashes, redaction state, content contract, and structural envelopes by default. | `verified-doc` via Lanes 03/04. | High | Raw-body import policy must be separate. |
| Treating missing fields as zero | Missingness states are explicit observation values/statuses and fixture requirements. | `local-observed`: current schema tests and orchestration. | High | Existing legacy summaries may still need migration. |
| Treating thinking summaries as reasoning quality | Compaction/thinking/facets are substitute process observations only, never rubric truth. | `verified-doc`/Lane 03 and orchestration. | High | Rubric plugins must enforce evaluator provenance. |
| Reintroducing `score.overall` | `rubric_observations` are canonical; `score.overall` is legacy/simple projection only. | `local-observed`: tests plus orchestration. | High | Report migration remains future work. |
| Overbuilding before surfaces are known | Recommend a minimum relational spine plus JSON payloads and raw refs; provider-specific richness stays in adapters. Lane 02 now supports adding Codex SQLite/JSONL fixtures without expanding core into a Codex-shaped schema. | `inferred` from Lanes 01-04. | Medium-high | Lane 06 may alter plugin registry details. |
| Under-specifying plugin boundaries | Registries declare metrics/rubrics/predicates/source kinds; Lane 06 owns protocol details. | `local-observed`: strict contract. | Medium-high | Must be completed in Lane 06. |
| Query/rebuild registry drift | Rebuild records registry hash and query/report must verify parity. | `repo-precedent`: Lane 01. | High | Needs implementation tests. |
| Sanitized reports hiding uncertainty | Observations carry evidence class, confidence, gaps, implications, and raw artifact refs. | `local-observed`: orchestration. | High | Report plugins must render these fields. |

## Recommendation

Recommend Option B: entity / edge / observation relational model, with an event-first import ledger available as an adapter layer.

Rationale:

- Provider exposure is uneven. Lane 02 shows Codex SQLite is a session/thread index while rollout JSONL is a richer event stream whose `response_item` rows are not guaranteed provider model calls. Lane 03 shows Claude local files, OTel, hooks, and raw API body refs have different stability and privacy properties. Lane 04 shows API responses, Agents traces, OTel GenAI, CLI telemetry, and billing aggregates expose different units. First-class observations handle this better than a single event stream.
- The benchmark already has stable concepts: task, profile, run, requested/effective model, requested/effective reasoning, usage, cost estimate, and rubric observation. These should be queryable without reverse-engineering event payloads.
- Lane 01's strongest inheritance is registry/store/query parity. A relational model with declared metrics/rubrics/predicates makes parity testable.
- JSON payloads and raw artifact refs still preserve provider-specific details without polluting the core ontology.
- Multidimensional rubric observations need one-to-many storage. A pure event-first store would invite reports to rederive rubric facts inconsistently.

Implementation posture:

- Start with the relational spine and artifact/observation/edge tables.
- Add a `telemetry_events` table only if early adapters need raw normalized events for replay/debugging.
- Keep benchmark JSONL as the first durable import/export surface.
- Do not migrate private transcript content into SQLite.

## Minimum Implementation Slice

For the first implementation, the smallest useful subset is:

- `rebuild_runs`
- `registries`
- `artifacts`
- `sessions`
- `work_units`
- `task_definitions`
- `task_instances`
- `runs`
- `run_sessions`
- `turns`
- `model_calls`
- `runtime_response_items`
- `tool_calls`
- `subagents`
- `file_changes`
- `metric_observations`
- `rubric_observations`
- `cost_estimates`
- `entity_edges`

This minimum is deliberately not GSD-specific. GSD phases, milestones, plans, and handoff artifacts can attach through `work_units`, `artifacts`, payload namespaces, or `entity_edges`, but they should not become required columns in benchmark core tables. `telemetry_events` is optional unless adapters need event replay.

## Coordinator Revisit Items

1. Codex implementation should use Lane 02's layered adapter split: `sqlite_index`, `rollout_stream`, `config_snapshot`, and later `otel_live`. `otel_live` remains deferred until an approved local collector fixture proves emitted payloads.
2. Lane 06 should confirm plugin manifest declarations for `metric_id`, `rubric_id`, `predicate`, `source_kind`, `content_contract`, privacy class, and missingness states.
3. The final decision report should state that `score.overall` is legacy/simple projection only. Canonical quality storage is `rubric_observations`.
4. The implementation plan should include registry/store/query parity tests before any report plugin claims provider parity.
5. Raw artifact references need a retention and redaction policy before any raw body or content-bearing hook capture is enabled.
