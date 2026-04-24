# Lane 02 - Codex Exposure Research

Research date: 2026-04-24
Scope: Codex local SQLite state, rollout JSONL, OTel/config/provider/auth/rate/model/reasoning/log surfaces.
Mutation policy: read-only inspection only; no provider calls, no config edits, no OTel exporter run, no transcript content copied.

## Self-Audit Repair Note

Evidence class: `local-observed`; source: `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/LANE-SPECS-AND-PROMPTS.md`; command: `sed -n '20,87p' .../LANE-SPECS-AND-PROMPTS.md`; inspection date: 2026-04-24; confidence: high; known gaps: this artifact only repairs Lane 02 and does not disposition other lanes; implications: the Codex adapter section below now treats evidence metadata, missingness, privacy, and plugin boundaries as first-class storage requirements.

Repair disposition: revised. The initial artifact answered the lane prompt but under-specified the stricter repair contract in four ways: evidence rows lacked retrieval/inspection dates and implications, required Lane 02 questions were answered across sections rather than in a coverage map, pitfalls were implicit rather than explicit, and direct/provider/derived/substitute/unavailable signal classes were not separated enough for downstream ontology design.

## Executive Summary

Codex exposes enough local structure to build a high-value telemetry adapter without live provider calls:

- SQLite (`~/.codex/state_5.sqlite`) is the strongest local session/thread index. It exposes thread IDs, rollout paths, timestamps, source, provider, cwd, title, sandbox policy, approval mode, token total, git metadata, CLI version, agent role/nickname/path, model, reasoning effort, memory mode, dynamic tool schema rows, and parent-child spawn edges.
- Rollout JSONL (`~/.codex/sessions/**/*.jsonl`) is the richest per-turn/per-item source. It exposes record classes (`session_meta`, `turn_context`, `response_item`, `event_msg`, `compacted`), model/reasoning/sandbox/approval context, response item/tool-call structure, command execution metadata, token usage, rate-limit snapshots, subagent routing/status events, compaction replacement structure, and web-search/open/find actions.
- OTel is officially configurable for logs, traces, and metrics, with opt-in raw prompt logging. The current official config surface documents exporter knobs, not a full emitted-event schema. It is not currently observed locally in this pass because enabling/exporting it would require a configured exporter and a collector endpoint. CLI `--config` one-off overrides mean local OTel capture appears feasible without persistent config mutation for a future controlled run, but proving it is deferred because it would require setup and execution outside this lane's no-mutation/no-provider boundary.
- Codex docs/config expose model, reasoning effort, provider, auth, approval, sandbox, history, local logs, subagents, and rate-limit concepts. They do not by themselves expose cost dollars, per-model call latency for every request, full request/response bodies in a privacy-safe form, or a stable provider-neutral ontology.

## Evidence Register

| Material claim | Evidence class | Source | Retrieval / inspection date | Command / citation | Confidence | Known gaps | Ontology / plugin / storage implications |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codex CLI runs locally, can inspect/edit/run code, and supports ChatGPT or API-key auth. | `verified-doc` | https://developers.openai.com/codex/cli | Retrieved 2026-04-24 | `web.open`, lines 571-600 | High | Does not define all local persistence formats. | `codex_cli_session` is a harness adapter source, not a core ontology assumption. |
| User/project config layers exist; project config loads only for trusted projects; CLI flags and `--config` have highest precedence. | `verified-doc` | https://developers.openai.com/codex/config-basic | Retrieved 2026-04-24 | `web.find`, lines 571-597 | High | Precedence documented, not empirically tested here. | Storage must separate configured/requested defaults from observed/effective runtime rows. |
| One-off `-c` / `--config` overrides can set arbitrary config keys for a single run. | `verified-doc` | https://developers.openai.com/codex/config-advanced | Retrieved 2026-04-24 | `web.find`, lines 599-618 | High | OTel-specific one-off syntax was not executed. | Enables a future `otel_live` plugin mode that avoids persistent config mutation, but fixture proof is deferred. |
| User config and state live under `CODEX_HOME`, defaulting to `~/.codex`; common files include config, auth, history, logs/caches. | `verified-doc` | https://developers.openai.com/codex/config-advanced | Retrieved 2026-04-24 | `web.find`, lines 619-629 | High | Does not enumerate SQLite or rollout JSONL schema. | Adapter discovery should be parameterized by `CODEX_HOME`, not hard-coded to one user path. |
| Config reference defines user/project config, approval/sandbox keys, auth storage, forced login method, history, log dir, model provider fields, and OTel fields. | `verified-doc` | https://developers.openai.com/codex/config-reference | Retrieved 2026-04-24 | `web.open`/`web.find`, lines 572-609, 685-688, 786-799, 805-807, 972-1027, 1077-1140 | High | Config reference is an option surface, not runtime proof. | Config ingestion should produce `requested` or `configured_default` observations, not overwrite effective telemetry. |
| OTel currently exposes configurable log, trace, and metrics exporter knobs, endpoint/headers/protocol/TLS settings, environment tag, and opt-in raw user prompt logging. | `verified-doc` | https://developers.openai.com/codex/config-reference | Retrieved 2026-04-24 | `web.find`, lines 1077-1140 | High for config surface; low for emitted schema | Docs page does not list emitted span/log/metric attribute schemas. | OTel storage should be namespaced and fixture-gated; raw prompt logging must be disabled by default. |
| Codex subagents are surfaced in app/CLI, are explicit, consume more tokens, inherit sandbox policy, and can use custom agent files with model/reasoning/sandbox overrides. | `verified-doc` | https://developers.openai.com/codex/subagents | Retrieved 2026-04-24 | `web.find`, lines 575-640 | High | Does not describe JSONL/SQLite persistence. | Core ontology should model child sessions/threads and edges; Codex role/nickname/path stay adapter payload. |
| GPT-5.1 Codex is Responses-only and docs expose model pricing/rate-limit tables for API usage. | `verified-doc` | https://developers.openai.com/api/docs/models/gpt-5.1-codex | Retrieved 2026-04-24 | `web.open`, lines 650-661 and 813-820 | Medium | API rate limits/pricing are not identical to ChatGPT-plan Codex quota snapshots. | Cost plugin must version pricing by retrieval date and distinguish API-equivalent estimate from provider-reported quota. |
| SQLite state includes `threads`, `thread_spawn_edges`, `thread_dynamic_tools`, `agent_jobs`, `agent_job_items`, and related job/memory tables. | `local-observed` | `~/.codex/state_5.sqlite` | Inspected 2026-04-24 | `sqlite3 ~/.codex/state_5.sqlite ".tables"; sqlite3 ~/.codex/state_5.sqlite ".schema"` | High | Schema can change across Codex releases. | Store a schema-version/field-presence snapshot and make the SQLite adapter tolerant of missing columns. |
| SQLite `threads` rows include session/thread, model/provider, sandbox/approval, token aggregate, git, role/nickname/path, model/reasoning, cwd, and rollout path. | `local-observed` | `~/.codex/state_5.sqlite` | Inspected 2026-04-24 | Same schema command plus grouped count queries | High | `first_user_message` and possibly `title` are private content and should not be copied. | SQLite is the canonical local index and join surface; sensitive columns require redaction policy. |
| Local SQLite currently has 1274 threads, 599 spawn edges, 0 dynamic tool rows, 0 agent job rows, and 0 agent job item rows. | `local-observed` | `~/.codex/state_5.sqlite` | Inspected 2026-04-24 | `sqlite3 -header -column ... SELECT ... COUNT(*) ...` | High | Counts are point-in-time only. | Missing/empty tables must be stored as `no_rows_observed`, not `unsupported`. |
| Rollout JSONL top-level records use `timestamp`, `type`, `payload`; observed record types include `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted`. | `local-observed` | `~/.codex/sessions/**/*.jsonl` | Inspected 2026-04-24 | Structural Python parser over 1432 files; keys/types only | High | Parser intentionally avoided private text values. | JSONL is the event stream source; importer should be structural-first and content-redacting. |
| Rollout JSONL exposes token totals and reasoning-token counts via `event_msg.info.last_token_usage` and `event_msg.info.total_token_usage`. | `local-observed` | `~/.codex/sessions/**/*.jsonl` | Inspected 2026-04-24 | Structural parser: `input_tokens`, `cached_input_tokens`, `output_tokens`, `reasoning_output_tokens`, `total_tokens` | High | Token usage is not directly linked to dollar cost. | Token observations need category columns, not one flattened total. |
| Rollout JSONL exposes rate-limit snapshots with primary/secondary windows, reset time, used percent, plan type, limit ID/name, and credit flags. | `local-observed` | `~/.codex/sessions/**/*.jsonl` | Inspected 2026-04-24 | Structural parser: `event_msg.rate_limits.*` | High | No user identity copied; semantics need provider-specific interpretation. | Quota/rate observations must remain provider aggregate signals separate from tokens and cost. |
| Local `~/.codex/config.toml` currently contains model/reasoning defaults, project trust entries, MCP server, and agent config references; no `otel` table was observed by key-only inspection. | `local-observed` | `~/.codex/config.toml` | Inspected 2026-04-24 | Redacted `awk` key/section pass | High | Values intentionally redacted; project-local config not exhaustively inspected. | Config snapshot plugin should record keys/sections and redacted values separately from effective runtime settings. |

## Surface Findings

### SQLite State DB

Evidence: `local-observed`, path `~/.codex/state_5.sqlite`, command `sqlite3 ~/.codex/state_5.sqlite ".schema"` plus count/grouping queries.

Observed tables:

- `threads`: primary session/thread index.
- `thread_spawn_edges`: parent-child relation for subagent threads, with child thread as primary key and edge status.
- `thread_dynamic_tools`: per-thread dynamic tool definitions, with name, description, input schema, namespace, defer-loading flag.
- `agent_jobs` and `agent_job_items`: batch/job orchestration structures, currently empty locally.
- `stage1_outputs`, `jobs`, `backfill_state`, `remote_control_enrollments`, `_sqlx_migrations`: background/memory/job/remote-control state.

Important `threads` columns:

- Session/thread: `id`, `rollout_path`, `created_at`, `updated_at`, `created_at_ms`, `updated_at_ms`, `source`, `cwd`, `title`, `cli_version`, `archived`.
- Model/routing: `model_provider`, `model`, `reasoning_effort`, `agent_role`, `agent_nickname`, `agent_path`, `source`.
- Runtime policy: `sandbox_policy`, `approval_mode`.
- Tokens: `tokens_used`.
- Git: `git_sha`, `git_branch`, `git_origin_url`.
- Privacy-sensitive fields to avoid copying: `first_user_message`, `title` when derived from user content.

Implications:

- SQLite should be the adapter's canonical local index for thread/session discovery and subagent graph reconstruction.
- SQLite gives stable joins to rollout JSONL through `threads.rollout_path`.
- SQLite is appropriate for session-level metadata and routing evidence, not for full turn or tool-call detail.
- `thread_spawn_edges` should map to an ontology edge such as `spawned_child_thread`.
- `tokens_used` is a useful session aggregate but should not replace per-turn JSONL token observations.

Confidence: high for current local schema; medium for future compatibility because Codex schema is not a public stability contract.

### Rollout JSONL

Evidence: `local-observed`, path `~/.codex/sessions/**/*.jsonl`, command: structural Python JSON parser over 1432 JSONL files. The parser emitted keys, type discriminators, counts, and nested field names only; it did not print transcript text, tool arguments, or tool outputs.

Top-level shape:

- Keys: `timestamp`, `type`, `payload`.
- Record types observed: `session_meta`, `turn_context`, `response_item`, `event_msg`, `compacted`.

`session_meta` exposes:

- `id`, `timestamp`, `cwd`, `cli_version`, `model_provider`, `originator`, `source`, `git`.
- Optional subagent fields: `agent_nickname`, `agent_role`, `forked_from_id`.
- `base_instructions` exists and is private prompt-like content; record only its presence/hash if needed, not text.

`turn_context` exposes:

- `turn_id`, `cwd`, `model`, `effort`, `approval_policy`, `sandbox_policy`, `collaboration_mode`, `truncation_policy`, `personality`, `summary`, `user_instructions`, `current_date`, `timezone`, `realtime_active`.
- Optional `developer_instructions`, `permission_profile`, `file_system_sandbox_policy`, `final_output_json_schema`.
- Privacy-sensitive fields: `summary`, `user_instructions`, `developer_instructions`; adapter should store presence/length/hash or redacted references unless explicitly allowed.

`response_item` exposes:

- Model-visible item structure: `type`, `role`, `content`, `encrypted_content`, `summary`, `status`.
- Tool-call structure: `call_id`, `name`, `arguments`, `output`, `action`, `namespace`, `input`, `execution`, `tools`.
- Observed action type discriminators include web/search/open/find-like actions.
- Privacy-sensitive fields: `content[].text`, `arguments`, `output`, `input`, `summary[].text`; store structural metadata and byte lengths/hashes, not raw content.

`event_msg` exposes:

- Turn/routing: `turn_id`, `phase`, `collaboration_mode_kind`, `model`, `reasoning_effort`, `model_context_window`.
- Subagent routing/status: `new_thread_id`, `new_agent_role`, `new_agent_nickname`, `sender_thread_id`, `receiver_thread_id`, `receiver_agent_role`, `receiver_agent_nickname`, `agent_statuses`, `statuses`, `last_agent_message`.
- Tool/process execution: `command`, `parsed_cmd`, `cwd`, `process_id`, `started_at`, `completed_at`, `duration`, `duration_ms`, `exit_code`, `stdout`, `stderr`, `aggregated_output`, `formatted_output`, `status`.
- Token/quota: `info.last_token_usage`, `info.total_token_usage`, `rate_limits`.
- Web/action: `action`, `query`, `path`, `text`, `text_elements`, `images`, `local_images`.
- Patch/change indicators: `changes`, `success`.
- Privacy-sensitive fields: command arguments, stdout/stderr, aggregated/formatted output, prompts, last agent message, free text; treat as redacted payloads by default.

`compacted` exposes:

- `message`.
- `replacement_history[]` with `type`, `role`, `content`, `phase`, and sometimes `encrypted_content`.

Implications:

- JSONL is the primary source for turns, model-call-ish response items, tool calls, subagent messages, compaction events, token usage, and rate-limit observations.
- It is also the riskiest source for private transcript content. The adapter needs field-level privacy policy, not just file-level ingestion.
- `response_item` is not necessarily a one-to-one "model call"; it is best modeled as provider/runtime response items attached to a turn until correlated with token deltas and event phases.

Confidence: high for observed local files; medium for provider-neutral semantics.

### OTel

Evidence: `verified-doc`, URL `https://developers.openai.com/codex/config-reference`, lines 1077-1140; `verified-doc`, URL `https://developers.openai.com/codex/config-advanced`, lines 599-618 for one-off config overrides.

Documented config surface:

- `otel.environment`: environment tag.
- `otel.exporter`: log exporter, values `none`, `otlp-http`, `otlp-grpc`.
- `otel.exporter.<id>.endpoint`, `headers`, `protocol`, TLS certificate keys.
- `otel.trace_exporter`: trace exporter, values `none`, `otlp-http`, `otlp-grpc`.
- `otel.trace_exporter.<id>.endpoint`, `headers`, `protocol`, TLS certificate keys.
- `otel.metrics_exporter`: values `none`, `statsig`, `otlp-http`, `otlp-grpc`; default documented as `statsig`.
- `otel.log_user_prompt`: opt-in raw user prompt export.

Local capture feasibility:

- Inferred from docs: a future run can likely point OTel at a local collector without persistent config mutation using `codex --config ...` because CLI `--config` overrides are highest precedence and can set arbitrary nested keys.
- Deferred proof: I did not start a collector, mutate config, or run Codex with OTel because this lane forbids setup/mutation/provider runs.
- Boundary: local OTel capture of a current already-running session is not established. The safe implementation plan should treat OTel capture as a future controlled-run mode, not a retroactive extractor.

Implications:

- OTel should be a live-capture adapter, not the only durable source.
- The privacy default should set `otel.log_user_prompt = false` unless a user explicitly opts in.
- Because docs expose exporter configuration but not a complete emitted-span schema here, OTel fields should enter the ontology as namespaced observations until fixture-backed.

Confidence: high that OTel config exists; medium that no-persistent-mutation capture works; low on exact emitted span/log schema until tested.

### Docs/Config Provider And Auth Surface

Evidence: `verified-doc`, `https://developers.openai.com/codex/config-reference`, `https://developers.openai.com/codex/config-basic`, `https://developers.openai.com/codex/config-advanced`, `https://developers.openai.com/codex/auth`; `local-observed`, redacted `~/.codex/config.toml` key pass.

Provider/config fields documented:

- `model`, `model_provider`, `model_reasoning_effort`, and `plan_mode_reasoning_effort`.
- `model_providers.<id>.base_url`, `env_key`, `env_key_instructions`, `http_headers`, `env_http_headers`, `query_params`, `request_max_retries`, `stream_max_retries`, `stream_idle_timeout_ms`, `supports_websockets`, `requires_openai_auth`, `wire_api`, and token-command auth settings.
- `wire_api` is documented as `responses` only.
- `openai_base_url` can redirect the built-in OpenAI provider to a proxy/router/data-residency project without defining a separate provider.

Auth fields documented:

- First-run auth supports ChatGPT account or API key.
- `cli_auth_credentials_store` controls file/keyring/auto storage.
- `forced_login_method` can restrict to `chatgpt` or `api`.
- `forced_chatgpt_workspace_id` can restrict ChatGPT login workspace.

Local config key observations:

- Present top-level keys include `model`, `model_reasoning_effort`, `plan_mode_reasoning_effort`, and `personality`.
- Present sections include trusted project entries, `[features]`, `[tui]`, `[mcp_servers.context7]`, and many `[agents.*]` role declarations.
- No `[otel]` section was observed in the redacted key pass.

Implications:

- The Codex adapter should distinguish configured defaults from effective runtime state. SQLite/JSONL are better for effective model/reasoning/sandbox/approval evidence; config is better for intent/defaults.
- Provider-specific fields should be stored in adapter payloads or `codex.*` namespaced observations rather than promoted into a core ontology.
- Auth mode should be captured from docs/config/runtime evidence only as a mode/source indicator; do not ingest credential files.

Confidence: high for documented fields; medium for local effective auth because credential files were not inspected.

## Concept Mapping

| Evidence concept | SQLite fields | JSONL fields | OTel/docs/config fields | Confidence | Implication |
| --- | --- | --- | --- | --- | --- |
| Session/thread | `threads.id`, `rollout_path`, `created_at(_ms)`, `updated_at(_ms)`, `source`, `cwd`, `cli_version` | `session_meta.id`, `timestamp`, `cwd`, `cli_version`, top-level `timestamp` | `CODEX_HOME`, history/log config | High | Use SQLite as index, JSONL as event stream. |
| Turn | None direct beyond updated timestamps | `turn_context.turn_id`, `event_msg.turn_id`, `turn_context.*` | None direct | High | Turn is JSONL-native. |
| Model call / response item | `threads.model`, `threads.reasoning_effort`, aggregate `tokens_used` | `turn_context.model`, `turn_context.effort`, `response_item.*`, token deltas in `event_msg.info.*` | `model`, `model_reasoning_effort`, model docs | Medium | Avoid one-to-one model-call assumptions until correlated. |
| Tool call | `thread_dynamic_tools` schema if populated | `response_item.call_id/name/arguments/output/action/namespace/status`, `event_msg.invocation`, command/process fields | MCP/app/tool config docs | High | JSONL is primary; redact args/output. |
| Subagent | `threads.agent_role`, `agent_nickname`, `agent_path`, `source`; `thread_spawn_edges.parent_thread_id`, `child_thread_id`, `status` | `session_meta.agent_*`, `forked_from_id`, `event_msg.new_thread_id`, `receiver_thread_id`, `agent_statuses`, `statuses` | Subagent docs, `[agents]` config | High | Build explicit parent-child graph. |
| Compaction | None observed in SQLite schema | `compacted.message`, `compacted.replacement_history[]`, `turn_context.truncation_policy` | `compact_prompt`, `experimental_compact_prompt_file`, compaction docs/config | High | Store event and structural replacement count, not text. |
| Token usage | `threads.tokens_used` | `event_msg.info.last_token_usage.*`, `total_token_usage.*`, `model_context_window`, `turn_context.truncation_policy` | Counting/model docs | High | Capture missing vs zero explicitly. |
| Cost/quota | None explicit except tokens | `event_msg.rate_limits.*`; token usage | API model pricing/rate docs | Medium | Quota is observed; dollar cost must be inferred separately and versioned. |
| Approval | `threads.approval_mode` | `turn_context.approval_policy` | `approval_policy` docs/config | High | Effective approval varies per turn; store both session and turn. |
| Sandbox | `threads.sandbox_policy` | `turn_context.sandbox_policy`, optional `file_system_sandbox_policy`, `permission_profile` | `sandbox_mode` docs/config | High | Runtime policy should be normalized but raw policy preserved. |
| Git | `git_sha`, `git_branch`, `git_origin_url` | `session_meta.git.branch`, `commit_hash`, `repository_url` | None needed | High | Good provenance anchor; redact private origin if policy requires. |
| Routing/provider | `source`, `model_provider`, `agent_role/path` | `session_meta.source`, `originator`, `model_provider`, subagent routing fields | `model_provider`, provider config, auth config | High | Separate effective provider from configured default. |

## Required Question Coverage

| Lane 02 question | Answer | Evidence metadata | Confidence | Known gaps | Ontology / plugin / storage implications |
| --- | --- | --- | --- | --- | --- |
| Exactly what current Codex OTel exposes | Current official docs expose OTel configuration for environment tagging, log exporter, trace exporter, metrics exporter, endpoints, headers, OTLP HTTP protocol, TLS certificate paths, and opt-in raw prompt logging. The docs inspected here do not expose a complete emitted span/log/metric attribute schema. | `verified-doc`; https://developers.openai.com/codex/config-reference; retrieved 2026-04-24; `web.find`, lines 1077-1140 | High for config knobs; low for emitted schema | No local OTel run; no collector fixture; no exported payload inspected. | Create `otel_live` as optional adapter; store OTel attributes in a namespaced observation table until fixture-backed. |
| Whether Codex OTel can be captured locally without external services | Likely yes for a future controlled run if "external services" means hosted vendors: a local OTLP collector endpoint plus CLI `--config` overrides should avoid persistent config mutation. Deferred because this lane did not start a collector or run Codex with exporter settings. | `verified-doc` for `--config` precedence; https://developers.openai.com/codex/config-advanced; retrieved 2026-04-24; `web.find`, lines 599-618. `verified-doc` for OTel endpoints; config-reference lines 1077-1140 | Medium | Need a local collector fixture and a no-provider/minimal run approved by coordinator. | Treat local OTel capture as live-capture mode, not retroactive import; persist capture setup metadata and mutation boundary. |
| What Codex exposes through `state_5.sqlite` | Session/thread index, rollout path, timestamps, source, provider, cwd, title, sandbox, approval, token aggregate, git metadata, CLI version, user-event flag, archive fields, agent role/nickname/path, memory mode, model, reasoning effort, dynamic tool definitions, subagent spawn edges, and job tables. | `local-observed`; `~/.codex/state_5.sqlite`; inspected 2026-04-24; `.schema`, `.tables`, grouped count queries | High | Internal schema may drift; sensitive title/first-message fields must not be copied. | Use as primary index and graph source; store raw schema version/field presence. |
| What Codex exposes through rollout JSONL | Session meta, turn context, response items, event messages, compaction events, tool-call structure, command execution metadata, token usage, rate-limit snapshots, subagent routing/status, web-search actions, and patch/change indicators. | `local-observed`; `~/.codex/sessions/**/*.jsonl`; inspected 2026-04-24; structural Python parser over 1432 files | High | Content fields are private; schema stability is empirical. | Use as event stream; enforce field-level privacy; source pointers and hashes instead of raw transcript content. |
| What Codex exposes through config/docs | Requested/configured defaults for model, reasoning, providers, auth restrictions/storage, approval, sandbox, history, logs, OTel, MCP, and agents. Docs expose capabilities and knobs; config exposes local requested defaults. | `verified-doc` URLs in Evidence Register; retrieved 2026-04-24. `local-observed`; `~/.codex/config.toml`; inspected 2026-04-24; redacted key pass | High for config keys; medium for effective behavior | Credential files were not inspected; no config values copied. | Store config observations as `requested`/`configured_default`; never let config override effective SQLite/JSONL evidence. |
| Requested versus effective model/reasoning | Requested/configured settings appear in `~/.codex/config.toml` (`model`, `model_reasoning_effort`, `plan_mode_reasoning_effort`) and custom agent config references. Effective observed settings appear in SQLite `threads.model`/`threads.reasoning_effort` and JSONL `turn_context.model`/`turn_context.effort` plus `event_msg.model`/`event_msg.reasoning_effort`. | `verified-doc`; config-basic/config-reference retrieved 2026-04-24. `local-observed`; SQLite/JSONL/config commands inspected 2026-04-24 | High | Exact config values redacted; current turn's effective model is not singled out to avoid transcript overreach. | Schema needs `requested_model`, `requested_reasoning`, `effective_model`, `effective_reasoning`, and provenance/source columns. |
| Token, cost, quota exposure | Token categories are directly observed in JSONL as input, cached input, output, reasoning output, and total tokens. Quota/rate state is provider aggregate in `event_msg.rate_limits`. Cost dollars are not directly observed locally; API-equivalent cost can only be derived using timestamped pricing docs and provider/model mapping. | `local-observed`; JSONL structural parser inspected 2026-04-24. `verified-doc`; GPT-5.1 Codex model page retrieved 2026-04-24, lines 650-661 and 813-820 | High for tokens/quota fields; medium for API-equivalent cost estimate; unavailable for provider-reported dollars | ChatGPT-plan quota and API pricing may not match; no provider invoice/cost field observed. | Keep `token_observation`, `quota_observation`, `rate_limit_observation`, and `cost_estimate` separate. |
| Hierarchy across sessions, turns, tools, subagents, compaction, approvals, sandbox, git, and routing evidence | Sessions/threads: SQLite and `session_meta`. Turns: JSONL `turn_context` and `event_msg.turn_id`. Tools: `response_item.call_id/name/action` and process events. Subagents: SQLite spawn edges and JSONL agent status/routing fields. Compaction: JSONL `compacted` and truncation policy. Approvals/sandbox: SQLite session fields plus JSONL turn context. Git: SQLite and `session_meta.git`. Routing: provider/source/agent fields. | `local-observed`; SQLite and JSONL commands inspected 2026-04-24 | High | Model-call boundaries remain inferred from response items and token events. | Minimum storage needs entity tables for session/thread, turn, event/item, tool call, subagent edge, policy snapshot, git provenance, and observation facts. |

## Signal Classification

| Signal | Classification | Evidence metadata | Confidence | Known gaps | Implications |
| --- | --- | --- | --- | --- | --- |
| SQLite `threads.model`, `threads.reasoning_effort`, `threads.sandbox_policy`, `threads.approval_mode` | Direct local effective-session signal | `local-observed`; `~/.codex/state_5.sqlite`; inspected 2026-04-24; SQLite schema/grouping queries | High | Effective per-turn changes require JSONL correlation. | Store as session-level effective defaults/snapshots. |
| JSONL `turn_context.model`, `turn_context.effort`, `approval_policy`, `sandbox_policy` | Direct local effective-turn signal | `local-observed`; `~/.codex/sessions/**/*.jsonl`; inspected 2026-04-24; structural parser | High | Field names are internal and may drift. | Store as turn policy/model snapshots with raw adapter payload. |
| JSONL `event_msg.info.*token_usage` | Direct local token accounting signal | `local-observed`; JSONL structural parser; inspected 2026-04-24 | High | Does not expose dollars. | Store token categories independently; never collapse reasoning/cache/output into one opaque total. |
| JSONL `event_msg.rate_limits` | Provider aggregate quota/rate signal | `local-observed`; JSONL structural parser; inspected 2026-04-24 | High for field presence; medium for business meaning | Plan/account semantics not independently verified; no user identity copied. | Store as provider aggregate with raw snapshot and missingness semantics. |
| API-equivalent dollars from model pricing docs | Derived estimate | `verified-doc`; GPT-5.1 Codex model page; retrieved 2026-04-24 | Medium | May not equal subscription quota burn or provider invoice. | Use a cost-estimator plugin with pricing-version provenance. |
| OTel emitted spans/logs/metrics | Unavailable/not exposed in this pass | `verified-doc` only for config; no local OTel run | Low for exact payload | Requires future local collector fixture. | Keep OTel ingestion optional and namespaced until proven. |
| Response item as model call | Substitute/derived signal | `local-observed`; JSONL response item structure; inspected 2026-04-24 | Medium | Not guaranteed one response item equals one provider call. | Model `runtime_response_item`; derive `model_call` only with stronger correlation. |
| Config `model` and `model_reasoning_effort` | Requested/configured signal | `local-observed`; redacted config key pass; inspected 2026-04-24 | High for key presence | Values redacted; config may be overridden. | Store separately from effective model/reasoning. |

## Pitfalls And Mitigations

| Pitfall | Lane 02 disposition | Evidence metadata | Confidence | Known gaps | Ontology / plugin / storage implication |
| --- | --- | --- | --- | --- | --- |
| Treating Reflect as authoritative | Avoided. This lane used Codex docs and local Codex state, not Reflect artifacts, as authority. | `local-observed`; this artifact and command history; inspected 2026-04-24 | High | Cross-lane synthesis still needs Lane 01 review. | Reflect-derived schemas should enter as `repo-precedent`, not core. |
| Designing around Codex only | Mitigated by keeping Codex-specific fields namespaced and recommending provider-neutral entities. | `inferred`; based on concept mapping above; 2026-04-24 | Medium | Other lanes must validate Claude/API surfaces. | Core schema should not contain `turn_context` or `event_msg` as first-class provider-neutral names. |
| Flattening provider/auth/billing | Mitigated by separating auth mode, provider routing, token usage, rate/quota snapshots, and cost estimates. | `local-observed` plus `verified-doc`; sources in Evidence Register | High | Effective auth not proven from credentials. | Separate tables or observation types for provider, auth, tokens, quota, and cost. |
| Over-trusting local logs | Mitigated. Local logs are documented but not treated as primary structured telemetry. | `verified-doc`; config-reference `log_dir`; retrieved 2026-04-24 | Medium | Logs may still contain useful debug evidence. | Logs should be optional debug source with privacy filters, not canonical storage. |
| Mutating config for OTel experiments | Avoided. No config mutation or OTel run occurred; future capture should use one-off overrides and explicit fixture setup. | `local-observed`; `git status`; 2026-04-24. `verified-doc`; config-advanced `--config` | High | Future run still needs approval and collector setup. | Capture setup metadata must record mutation mode and endpoint locality. |
| Persisting sensitive transcript content | Avoided in research. Structural parsers emitted keys/types only. | `local-observed`; parser commands; inspected 2026-04-24 | High | Future importer must enforce this programmatically. | Add content contract: redact text/args/output by default; store hashes/lengths/source pointers. |
| Treating missing fields as zero | Mitigated by explicit `no_rows_observed`, `not_configured_observed`, `not_exposed`, and `deferred` states. | `local-observed`; SQLite counts and config key pass; 2026-04-24 | High | Needs schema support from Lane 05. | Missingness must be a typed semantic value. |
| Treating thinking summaries as reasoning quality | Not applicable to Codex in this lane; Codex has reasoning-token counts, but response summaries/content are not quality truth. | `local-observed`; JSONL structural fields; inspected 2026-04-24 | Medium | Claude-specific substitute signals belong to Lane 03. | Store reasoning tokens separately from summaries and rubric observations. |
| Reintroducing `score.overall` | Avoided. No benchmark quality scoring schema is proposed here. | `inferred`; this artifact; 2026-04-24 | High | Final benchmark schema belongs to coordinator/Lane 05/06. | Adapter should emit observations, not collapse quality. |
| Overbuilding before provider surfaces are known | Mitigated by recommending layered adapters and fixture-gated OTel. | `inferred`; current evidence limitations; 2026-04-24 | Medium | Needs synthesis with other lanes. | Build SQLite/JSONL import first; leave OTel/API adapters optional. |
| Under-specifying plugin boundaries | Repaired by identifying `sqlite_index`, `rollout_stream`, `config_snapshot`, `otel_live`, and cost estimator plugins. | `inferred`; implementation implications; 2026-04-24 | Medium | Interface details belong to Lane 06. | Capability declarations should include source type, privacy contract, metric namespace, fixture requirements. |
| Query/rebuild registry drift | Relevant by analogy: if SQLite is used as query cache, rebuild/import from JSONL and config must be deterministic and versioned. | `inferred`; local source hierarchy; 2026-04-24 | Medium | Lane 05 owns storage/rebuild design. | Keep raw source pointers and adapter version so query DB can be rebuilt. |
| Sanitized reports hiding uncertainty | Mitigated by carrying confidence, gaps, and deferred work explicitly. | `local-observed`; this revised artifact; 2026-04-24 | High | Synthesis must preserve gaps. | Reports should render unknown/deferred states visibly, not omit them. |

## Gaps And Deferred Work

- Deferred: OTel local capture fixture. Requires a local collector endpoint and a controlled Codex run with `--config` OTel overrides. This should be done in a later slice with explicit permission because it is setup/execution, even if it avoids persistent config mutation.
- Deferred: Exact OTel span/log schema. Official config docs prove knobs, not emitted attribute names.
- Deferred: Effective auth mode proof. Credential files were intentionally not inspected; config/docs expose possible modes.
- Gap: Cost cannot be observed directly from local SQLite/JSONL. A cost plugin must combine token usage with a timestamped pricing source and provider/model mapping.
- Gap: `response_item` is not guaranteed to equal a provider request. The ontology should support `runtime_response_item` and only derive `model_call` when a stronger correlation is available.
- Gap: Local logs (`log_dir` / `codex-tui.log`) are documented but were not inspected. They may be useful for debugging, but JSONL/SQLite are better structured sources for benchmark telemetry.
- Gap: SQLite state is an internal runtime DB. Treat schema drift as expected and write adapter fixtures around observed versions.

## Implementation Implications

1. Build the Codex adapter in layers:
   - `sqlite_index`: session/thread/subagent graph and effective session metadata.
   - `rollout_stream`: turn, event, response item, token, quota, tool, compaction observations.
   - `config_snapshot`: redacted key/default/provider/auth intent capture.
   - `otel_live`: optional future live-capture adapter with fixture gating.

2. Keep core ontology provider-neutral:
   - Core concepts: session, turn, event, response item, tool call, subagent edge, token observation, quota observation, runtime policy, git provenance.
   - Codex-specific fields: keep raw field names in `adapter_payload.codex` or namespaced metric keys.

3. Enforce privacy at extraction time:
   - Do not ingest raw `content[].text`, prompts, tool arguments, stdout/stderr, tool output, first user message, or compaction replacement content by default.
   - Store structural fields, counts, byte lengths, hashes, redacted placeholders, and source pointers.

4. Treat observed absences as semantic states:
   - No OTel config observed locally is `not_configured_observed`, not proof that OTel is unsupported.
   - Empty `agent_jobs` tables mean `no_local_rows_observed`, not unsupported.
   - Missing cost is `not_exposed`, not zero.

5. Verification fixtures should include:
   - A minimal SQLite fixture with `threads` and `thread_spawn_edges`.
   - A redacted JSONL fixture covering `session_meta`, `turn_context`, `response_item`, `event_msg`, and `compacted`.
   - A future OTel fixture captured via one-off `--config` against a local collector, only after explicit setup approval.
