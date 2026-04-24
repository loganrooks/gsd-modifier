# Lane 03 - Claude Code Exposure Research

Retrieval date: 2026-04-24

Scope: Claude Code local session metadata and project JSONL, official Anthropic/Claude Code documentation for OpenTelemetry, monitoring, data usage, hooks, plugins, skills, raw API body capture, compaction, and privacy controls. This pass did not mutate Claude configuration, enable telemetry, run providers, or copy transcript content.

## Executive Finding

Claude Code exposes several telemetry surfaces, but they are not equivalent:

| Surface | Availability | Evidence | Confidence | Adapter stance |
| --- | --- | --- | --- | --- |
| Local `~/.claude/usage-data/session-meta/*.json` | Local-file-only; aggregate session substitute signal | `local-observed`; command below | Medium | Use via Claude adapter only; schema is undocumented and locally imperfect. |
| Local `~/.claude/projects/**/*.jsonl` | Local-file-only; rich transcript/event store | `local-observed`; command below | Medium | Use only with strict redaction and structural extraction; not a stable public contract. |
| Claude Code OTel metrics/events/traces | OTel-only when explicitly enabled | `verified-doc`; monitoring docs | High | Preferred organization-grade telemetry path when operator consents and config exists. |
| OTel raw API request/response bodies | Raw-API-body-gated by `OTEL_LOG_RAW_API_BODIES` | `verified-doc`; monitoring docs | High | Treat as sensitive full-context capture; never required for benchmark core. |
| Hooks | Hook/plugin-visible for configured hook events | `verified-doc`; hooks docs | High | Useful for plugin adapters and online capture, but hooks see sensitive fields for some events. |
| Plugins and skills | Plugin-visible for installed/enabled plugins and activated skills | `verified-doc`; plugin/skills docs | High | Namespace plugin/skill data; do not promote plugin names into core ontology. |
| Raw reasoning / quality truth | Unavailable | `verified-doc` + `local-observed` | High | Thinking summaries/facets/session-meta are derived substitute signals only. |

This executive table is a summary only. The evidence class, source URL/path, retrieval date or local command, confidence, known gaps, and ontology/plugin/storage implications are made explicit in the evidence and coverage tables below.

## Local Inspection Evidence

Commands were structural only; they printed counts, field paths, and types rather than prompt, assistant, tool output, or transcript content.

| Evidence class | Path / URL | Command / citation | Finding | Confidence | Gaps |
| --- | --- | --- | --- | --- | --- |
| `local-observed` | `~/.claude/usage-data/session-meta/*.json` | `find ~/.claude/usage-data/session-meta -maxdepth 1 -type f -name '*.json' \| wc -l` | 471 session-meta files were present. | High | File count is local-machine state and can change immediately. |
| `local-observed` | `~/.claude/usage-data/session-meta/*.json` | parse loop with `jq -e type` | 468 of 471 files parsed as JSON; 3 paths failed parsing: `96ae5fc5-...json`, `6f97ee28-...json`, `8576521c-...json`. | High | Did not inspect invalid file content; failure may be truncation or local write race. |
| `local-observed` | `~/.claude/usage-data/session-meta/*.json` | `jq -r 'to_entries[] \| .key' ... \| sort \| uniq -c` | Common keys include `session_id`, `project_path`, `start_time`, `duration_minutes`, `input_tokens`, `output_tokens`, `assistant_message_count`, `user_message_count`, `tool_counts`, `tool_errors`, `files_modified`, `lines_added`, `lines_removed`, `languages`, `uses_task_agent`, `uses_mcp`, `uses_web_fetch`, and `uses_web_search`. | Medium | Undocumented schema; one command observed 469 key emissions despite 468 valid files, so readers should treat counts as sampled evidence, not a canonical schema. |
| `local-observed` | `~/.claude/projects/**/*.jsonl` | `find ~/.claude/projects -type f -name '*.jsonl' \| wc -l` | 2,581 project JSONL files were present. | High | File count is local-machine state and can change immediately. |
| `local-observed` | `~/.claude/projects/**/*.jsonl` | parse loop with `jq -e .` | One JSONL file failed full-file JSON parsing in the sampled run: `~/.claude/projects/-home-rookslog-workspace-projects-PDFAgentialConversion/c7204805-3c89-4731-845e-2be03079b3eb/subagents/agent-a1f8d96de8b7f0607.jsonl`. | Medium | JSONL can be append-active or contain partial/truncated lines; a robust reader should parse line-by-line and tolerate malformed terminal records. |
| `local-observed` | `~/.claude/projects/**/*.jsonl` | `jq -r 'select(type=="object") \| to_entries[] \| .key' ...` | Frequent top-level fields include `type`, `sessionId`, `timestamp`, `version`, `uuid`, `parentUuid`, `cwd`, `gitBranch`, `isSidechain`, `message`, `requestId`, `toolUseResult`, `agentId`, `promptId`, hook fields, and task/tool IDs. | Medium | Local schema is richer than public docs and should be treated as an internal implementation artifact. |
| `local-observed` | `~/.claude/projects/**/*.jsonl` | structural `jq paths(scalars)` over first 20 sorted JSONL files | `message` shapes resemble Anthropic Messages response objects: `message.id`, `message.type`, `message.role`, `message.model`, `message.content[].type`, `message.usage.*`, `message.stop_reason`; local samples also showed `thinking` and `signature` content block fields. | Medium | Presence in local files does not imply API stability or safe extraction; no content was copied. |
| `local-observed` | `~/.claude/projects/**/*.jsonl` | `find ~/.claude/projects -type f -name '*.jsonl' -print0 \| xargs -0 jq -r 'select(type=="object") \| paths(scalars) ...' \| rg -i 'token|cost|rate|quota|limit|usage|service_tier|cache|geo|speed|iteration|retry|error|sidechain|agent|parent|request|prompt|session|tool'` | Structural fields include `message.usage.input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation_input_tokens`, `cache_creation.ephemeral_*`, `service_tier`, `inference_geo`, `speed`, `server_tool_use.*`, `usage.iterations[]`, `requestId`, `promptId`, `sessionId`, `parentUuid`, `agentId`, `isSidechain`, `toolUseID`, and `parentToolUseID`. The same command also showed content-bearing fields such as prompts, stdout/stderr, file content, and tool results that must not be ingested in normal benchmark mode. | Medium | Local field presence is not a public contract; command output was structural but included field names that indicate sensitive content-bearing paths. |

Schema stability assessment: session-meta and JSONL should be treated as best-effort local stores, not official telemetry APIs. The local samples prove useful fields exist, but parse failures and undocumented keysets mean extractors need versioned adapters, tolerant parsers, fixture tests, and explicit unknown-field retention.

## Official Documentation Evidence

| Evidence class | Retrieval date | URL / path | Citation | Finding | Confidence | Gaps |
| --- | --- | --- | --- | --- | --- | --- |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/monitoring-usage | Lines 118-144, 168-187, 892-901 | Claude Code exports metrics, logs/events, and optional traces via OTel only when telemetry is explicitly enabled. Content-bearing fields are gated: prompts, tool details, tool content, and raw API bodies require explicit flags. | High | Docs say OTel support and details can change; adapter should retain doc retrieval date. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/monitoring-usage | Lines 184-187 and 900-901 | `OTEL_LOG_RAW_API_BODIES` emits full Anthropic Messages request/response JSON as inline bodies truncated at 60 KB or as `body_ref` files via `file:<dir>`. Bodies include conversation history, but extended-thinking content is always redacted. | High | Requires operator consent and config mutation; not exercised locally. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/monitoring-usage | Lines 406-430, 473-493, 516-540 | OTel exposes standard attributes, cost and token metrics, prompt correlation IDs, prompt-length events, command source, and optional prompt content. Token metric categories are `input`, `output`, `cacheRead`, and `cacheCreation`; cost and token metrics include `model`, `query_source`, `speed`, and `effort` where available. | High | OTel payloads were not locally collected; subscription quota bars are not exposed through this doc row. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/monitoring-usage | Lines 64-95 and 875-884 | Official OTel events include API request/error/body events, plugin installed, skill activated, hook execution, and compaction events, with `service.name=claude-code` and meter `com.anthropic.claude_code`. | High | Event attribute completeness depends on OTel config flags. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/hooks | Lines 587-599, 863-873, 947-949, 1416-1429, 1536-1574, 1821-1866, 1881-1893 | Hooks receive common JSON fields via stdin or HTTP body, including `session_id`, `transcript_path`, `cwd`, `permission_mode`, and, in subagent contexts, `agent_id` and `agent_type`. Some events expose user prompt text, tool input, last assistant message, subagent transcript paths, and compact summaries. | High | Hook capture requires configured hooks; no hooks were installed or run. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/discover-plugins | Lines 82-87, 286-331, 398-400 | Plugins can extend Claude Code with skills, agents, hooks, MCP servers, and LSP/code-intelligence behavior; installed plugins can be enabled/disabled/reloaded and are trusted components that can execute arbitrary code. | High | Specific installed plugin state was not inspected because this lane did not need config mutation or plugin execution. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/skills | Lines 83-90, 144-158, 214-241, 315-323 | Skills load from personal/project/plugin locations, can be invoked directly or automatically, have frontmatter such as `allowed-tools`, `model`, `effort`, `context`, and `hooks`, and invoked skill content is reattached across compaction within token budgets. | High | Skill behavior can affect model context and tool permissions but is not a direct quality metric. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/settings | Search result/opened page: settings files, environment variables, permissions, local transcript retention | Settings define user/project/local/managed hierarchy, permissions, local transcript retention via `cleanupPeriodDays`, environment variables, and privacy controls such as `permissions.deny`. | High | Settings were not read or changed in this lane. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/data-usage | Lines 107-128, 141-180 | Local transcripts are stored in plaintext under `~/.claude/projects/` for 30 days by default, configurable with `cleanupPeriodDays`; local Claude Code sends prompts and model outputs over the network to interact with the LLM. Statsig/Sentry operational telemetry can be disabled; provider-specific defaults disable non-essential traffic for Bedrock/Vertex/Foundry, and WebFetch preflight has a separate opt-out. | High | Account plan and current user privacy settings were not inspected. |
| `verified-doc` | 2026-04-24 | https://code.claude.com/docs/en/costs | Lines 74-88 | Claude Code charges by API token consumption; `/usage` shows session token usage and a locally computed dollar estimate that can differ from actual billing; subscribers see plan usage bars and activity stats. | High | `/usage` was not run; plan/quota state was not inspected. |
| `verified-doc` | 2026-04-24 | https://platform.claude.com/docs/en/api/rate-limits | Lines 126-142 | Anthropic API rate limits and spend limits are organization/workspace controls; limits are visible in Claude Console and vary by tier. | Medium | Dynamic page rendering was partial, and no authenticated Console/API state was queried. |
| `verified-doc` | 2026-04-24 | https://platform.claude.com/docs/en/build-with-claude/usage-cost-api | Lines 137-164 | The Usage and Cost Admin API provides historical usage/cost data for organizations and is unavailable for individual accounts. | Medium | No Admin API credentials or live calls were used. |
| `verified-doc` | 2026-04-24 | https://docs.anthropic.com/en/api/messages and https://docs.anthropic.com/en/api/messages-examples | API docs/search result | Anthropic Messages API response objects carry `id`, `type`, `role`, `content`, `model`, `stop_reason`, `stop_sequence`, and `usage`; token usage does not map one-to-one to visible content. | Medium | Dynamic API reference page was partially rendered through the fetch tool; search/open snippets provided the relevant fields. |

## Required Question Coverage Self-Audit

| Required Lane 03 question | Answer | Evidence class, source, command/citation, date | Confidence | Known gaps | Ontology/plugin/storage implications |
| --- | --- | --- | --- | --- | --- |
| Stability of Claude session-meta schema | Unstable enough to require a Claude-specific tolerant adapter. Local files expose useful aggregate keys but are undocumented and some did not parse. | `local-observed`; `~/.claude/usage-data/session-meta/*.json`; `find ... \| wc -l`, `jq -e type`, `jq paths`; 2026-04-24. | Medium | No official schema found; invalid files were not content-inspected. | Store as adapter payload plus normalized aggregate observations; record parse diagnostics and unknown fields. |
| Stability of Claude local JSONL schema | Rich but internal. JSONL contains session/turn/message/tool/subagent structure, but one file failed full-file parsing and docs do not commit to this as a telemetry API. | `local-observed`; `~/.claude/projects/**/*.jsonl`; `find ... \| wc -l`, `jq -e .`, structural `jq paths`; 2026-04-24. | Medium | Local samples may reflect this machine/version only. | Use line-by-line parser, schema version guess, source path/line references, unknown-field retention, and redaction state. |
| Local-file-only vs OTel-only exposure | Local files are available without enabling telemetry; OTel metrics/events/traces require explicit telemetry/exporter configuration. | `local-observed` local paths and commands; `verified-doc` monitoring lines 118-144 and 168-187; retrieved 2026-04-24. | High | OTel not locally exercised. | Separate local-source adapters from OTel adapters; do not collapse missing OTel into absent capability. |
| Hook/plugin/skill-visible exposure | Hooks and plugin/skill lifecycle can expose structure and sometimes sensitive content when configured. Skills can set `model`, `effort`, `context`, and hooks; plugin systems can install skills, agents, hooks, MCP, and LSP. | `verified-doc`; hooks lines 587-599 and event-specific rows; skills lines 214-241; plugins lines 82-87 and 286-331; retrieved 2026-04-24. | High | Installed local hook/plugin state not inspected. | Capture as declared plugin capability and capture provenance; reducers should drop sensitive fields before storage. |
| Raw-API-body-only exposure | Full request/response bodies are exposed only through explicit OTel raw body flag, not normal local aggregate extraction. | `verified-doc`; monitoring lines 184-187 and 900-901; retrieved 2026-04-24. | High | No raw body mode exercised. | Treat raw bodies as optional sensitive attachments with consent bit and retention policy; do not require for benchmark core. |
| Privacy/data-use caveats | Local transcripts are plaintext under `~/.claude/projects/`; network model interaction sends prompts and model outputs; operational Statsig/Sentry and feedback/survey/WebFetch-preflight controls are separate. | `verified-doc`; data-usage lines 107-128 and 141-180; retrieved 2026-04-24. | High | Account-level privacy choices not inspected. | Store privacy policy snapshot and capture mode with every import; default to structural-only extraction. |
| Thinking summaries/facets as substitute signals | Treat local `thinking` fields, compact summaries, facets, and session-meta as derived/substitute signals, never raw reasoning access or quality truth. | `local-observed`; structural path sample found `message.content.[].thinking` and `signature`; `verified-doc` raw API bodies redact extended thinking; monitoring lines 900-901; 2026-04-24. | High | No content copied; exact local semantics of thinking blocks not verified. | Model these as `derived_signal` or skip; quality observations must come from rubrics/outcomes, not telemetry internals. |
| Token/cost exposure | Local session-meta exposes aggregate `input_tokens` and `output_tokens`; local JSONL exposes `message.usage.*`, including cache fields in sampled paths. OTel exposes token metrics by type and cost metrics with model/query_source/speed/effort. `/usage` has local cost estimates but was not run. | `local-observed`; structural `jq paths` over session-meta and JSONL; `verified-doc` monitoring lines 423-493 and costs lines 74-88; retrieved 2026-04-24. | Medium-High | No authoritative billing queried; local cost estimate absent from structural samples. | Keep token categories separate from cost estimates and billing truth; store provider-reported vs derived estimates separately. |
| Rate/quota exposure | OTel/API docs expose rate/spend concepts and terminal API error events, but this lane did not observe current quota state. Subscription usage bars are UI state, not captured locally here. | `verified-doc`; API rate limit lines 126-142, Usage/Cost API lines 137-164, monitoring lines 829-830 for API error/retry interpretation; retrieved 2026-04-24. | Medium | No authenticated Console/Admin API or live provider call; no local quota state verified. | Represent quota/rate as optional provider/account observations with `unavailable` or `deferred` missingness, not zero. |
| Hierarchy and subagent/sidechain recovery | Local JSONL exposes hierarchy fields: `sessionId`, `parentUuid`, `uuid`, `promptId`, `requestId`, `toolUseID`, `parentToolUseID`, `agentId`, `isSidechain`; hooks docs expose `agent_id`, `agent_type`, and subagent transcript paths. | `local-observed`; structural counts command over `~/.claude/projects/**/*.jsonl`; `verified-doc`; hooks lines 587-599 and 1416-1429; retrieved 2026-04-24. | Medium-High | Relationship semantics inferred from names and docs; local fields are not official schema. | Build entity-edge recovery with confidence per edge; preserve source refs and allow multiple hierarchy edges per event. |

## Surface Classification

### Local-file-only

Session meta and project JSONL are locally available without enabling telemetry, but they are not official stable APIs.

Use:
- session-level aggregates: duration, token counts, message counts, tool counts, file/line-change counts, project path, start time
- JSONL structural events: turn boundaries, request IDs, tool-use structure, model IDs, usage objects, compaction/tool/hook markers where present

Do not use:
- prompt text, assistant text, tool arguments, tool outputs, file contents, compact summaries, or thinking block content in benchmark artifacts
- session-meta `first_prompt` as a feature unless separately redacted and explicitly consented
- `thinking`, `signature`, facets, summaries, or session-meta aggregates as raw reasoning or model quality truth

Ontology implication: core should store generic `session`, `turn`, `request`, `tool_call`, `usage`, `observation`, and `artifact_ref` entities. Claude-only fields belong under `provider_payload.claude_code` or adapter-specific observation namespaces.

Storage implication: line-oriented ingestion with `(source_path, line_number, uuid/sessionId/requestId, schema_version_guess, parsed_ok, redaction_state)`. Preserve malformed-line diagnostics without copying content.

### OTel-only

OTel is the official monitoring surface. It can capture metrics, structured events, and traces, but only when explicitly configured. It is the best production path for organization-level measurement because it has documented names, resource attributes, event types, privacy controls, and backend guidance.

Ontology implication: OTel events map cleanly into a provider-neutral event table with namespaced attributes. Avoid making `claude_code.*` metric names core ontology fields.

Storage implication: store OTel resources/spans/events separately from local transcript-derived observations. Link by `session.id`, timestamps, and request IDs where available.

### Hook/plugin-visible

Hooks can see sensitive event fields. `UserPromptSubmit` sees prompt text; tool hooks see tool inputs; `Stop` and `SubagentStop` can see last assistant messages; `PostCompact` sees compact summaries. Plugins can contribute hooks, skills, agents, MCP servers, and LSP behavior.

Ontology implication: plugin and hook visibility should be modeled as capture provenance and consent scope, not as inherent provider capability. A benchmark plugin should declare which hook events it subscribes to and which fields it drops before persistence.

Storage implication: if hooks are used later, write a privacy-first reducer at hook boundary. Store structural event envelopes and hashes/lengths where possible, not content.

### Raw-API-body-gated

Raw API bodies are available only through explicit OTel configuration. `OTEL_LOG_RAW_API_BODIES=1` emits truncated inline request/response bodies; `OTEL_LOG_RAW_API_BODIES=file:<dir>` writes untruncated body files and emits `body_ref`. Docs state these bodies include full conversation history and that extended-thinking content is redacted regardless of flags.

Ontology implication: raw API bodies are optional evidence attachments, not required benchmark facts. The core benchmark should function without raw bodies.

Storage implication: if a future operator enables this, store only references plus redaction/retention policy by default. Inline raw body ingestion should require a separate consent bit and should not be mixed into normal observation rows.

### Unavailable or not quality truth

Raw hidden reasoning is unavailable. Extended-thinking content in raw API bodies is documented as redacted, and local `thinking`-related fields, compact summaries, session-meta, and usage aggregates are substitute or derived signals. They can support process analysis but cannot prove reasoning quality.

Ontology implication: model-quality observations must come from benchmark rubrics, task outcomes, reviewer labels, and external validation, not telemetry facets. Telemetry can explain process and cost, not score the model by itself.

## Recommended Claude Adapter Contract

1. `claude_local_session_meta_adapter`
   - Reads valid JSON from `~/.claude/usage-data/session-meta/*.json`.
   - Emits session aggregate observations only.
   - Drops `first_prompt` by default or stores only length/hash under explicit consent.
   - Records invalid JSON files as source diagnostics.

2. `claude_local_jsonl_adapter`
   - Parses JSONL line-by-line and tolerates malformed terminal lines.
   - Emits structural event rows, usage rows, tool-call envelopes, and relationships.
   - Redacts or skips `message.content[].text`, `toolUseResult.*.content`, tool inputs, Bash commands, compact summaries, and final assistant messages unless a future explicit content-capture mode is approved.
   - Namespaces local-only fields under `provider_payload.claude_code.local_jsonl`.

3. `claude_otel_adapter`
   - Ingests documented `claude_code.*` metrics/events/traces.
   - Treats `OTEL_LOG_*` flags as capture-policy metadata.
   - Supports `body_ref` as an attachment pointer but does not dereference raw body files unless an explicit raw-body import policy is enabled.

4. `claude_hook_plugin_adapter`
   - Future optional online capture path.
   - Requires a manifest declaring hook events, visible fields, reducer behavior, storage fields, and redaction tests.
   - Must treat plugin/skill names and activation events as namespaced metadata.

## Gaps and Open Questions for Coordinator

- `local-observed`: One JSONL parse-failure path was observed and recorded above; this is enough to require tolerant ingestion even if the exact failure reason remains uninspected.
- `verified-doc`: Official docs document surfaces but not local JSONL/session-meta schemas. Local adapters need fixtures from synthetic or consent-safe sessions before implementation.
- `deferred`: No OTel collector was started and no Claude telemetry flags were enabled, so event payloads were not locally verified.
- `deferred`: Current installed plugin and hook configuration was not inspected to avoid widening beyond structural sample needs.
- `inferred`: Mapping JSONL `message` shapes to Messages API response fields is plausible from field names and docs, but local persistence is not guaranteed to be raw API response identity.
- `deferred`: Account-level data-training/privacy settings were not inspected. Treat privacy controls as operator/account state, not repo state.

## Relevant Pitfalls and Mitigations

| Pitfall | Lane 03 risk | Evidence class, source, command/citation, date | Confidence | Known gaps | Ontology/plugin/storage mitigation |
| --- | --- | --- | --- | --- | --- |
| Designing around Codex only | Claude has different local files, OTel names, hooks, plugins, skills, and raw-body gates. | `verified-doc`; Claude docs cited above; retrieved 2026-04-24. | High | Cross-lane synthesis still needed. | Use provider adapters and namespaced metric payloads, not Codex-shaped core tables. |
| Flattening provider/auth/billing | Claude subscription usage, API billing, Usage/Cost Admin API, local `/usage` estimate, OTel cost metric, and rate/spend limits are different surfaces. | `verified-doc`; costs lines 74-88, monitoring lines 423-493, rate-limits lines 126-142, Usage/Cost API lines 137-164; retrieved 2026-04-24. | High | No authenticated billing/quota state queried. | Separate `token_usage`, `local_cost_estimate`, `provider_reported_cost`, `billing_truth`, `rate_limit`, and `quota_state`; missing quota is `deferred`, not zero. |
| Over-trusting local logs | Local session-meta/JSONL are rich but undocumented and locally imperfect. | `local-observed`; parse/count/path commands over `~/.claude`; 2026-04-24. | High | No upstream schema contract. | Treat local files as evidence artifacts with adapter versioning, parse diagnostics, and confidence per extracted edge. |
| Mutating config for OTel experiments | Enabling OTel/raw bodies would change capture behavior and may expose sensitive data. | `verified-doc`; monitoring lines 118-187 and 892-901; retrieved 2026-04-24. | High | No OTel payloads collected. | Keep OTel as deferred unless operator explicitly enables it; never enable in research lanes. |
| Persisting sensitive transcript content | Local JSONL and hook/raw-body surfaces can expose prompts, assistant text, tool inputs/outputs, file content, compact summaries, stdout/stderr, and raw conversations. | `local-observed`; structural sensitive path names; `verified-doc`; hooks and monitoring privacy lines; 2026-04-24. | High | Redaction implementation not built in this lane. | Default reducers persist structure, IDs, lengths, hashes, counts, and source refs only; content capture requires explicit mode. |
| Treating missing fields as zero | Rate/quota/cost/billing fields are absent or gated in many surfaces. | `local-observed` and `verified-doc`; cited local commands and docs; 2026-04-24. | High | Current quota state unknown. | Store missingness reason: `not_exposed`, `not_configured`, `redacted`, `deferred`, `parse_failed`, or `not_applicable`. |
| Treating thinking summaries as reasoning quality | Local thinking-related paths and compact summaries are substitute/derived signals; raw hidden reasoning is not available and extended thinking is redacted from raw API body capture. | `local-observed`; structural `message.content.[].thinking`; `verified-doc`; monitoring lines 900-901; 2026-04-24. | High | Local field semantics unknown. | Do not map to quality score; store as derived signal metadata or skip. |
| Reintroducing `score.overall` | Telemetry surfaces can tempt single-number process scoring. | `inferred`; orchestration contract; 2026-04-24. | High | Final rubric design belongs to Lane 05/06/coordinator. | Store multidimensional rubric observations separately from telemetry observations; no `score.overall` dependency. |
| Under-specifying plugin boundaries | Hooks/plugins/skills can change model context, tools, and visible capture fields. | `verified-doc`; plugin/skill/hook docs cited above; retrieved 2026-04-24. | High | Installed plugin state not inspected. | Plugin manifests should declare adapter/extractor/view roles, hook subscriptions, capture policy, metric namespace, and fixtures. |
| Sanitized reports hiding uncertainty | Structural-only research can sound cleaner than the actual local evidence. | `local-observed`; invalid JSON/session-meta and malformed JSONL evidence above; 2026-04-24. | High | Some exact failure causes uninspected by design. | Persist diagnostics and confidence/gap fields alongside extracted observations. |

## Bottom Line

For the model-role benchmark telemetry substrate, Claude Code should be supported through three distinct provider adapters: local aggregate/session transcript structure, documented OTel, and optional hook/plugin capture. Core ontology should not depend on Claude-only field names, raw body capture, or local transcript internals. Missing or redacted values should be stored as semantic states. Derived signals such as thinking summaries, facets, compaction summaries, and session-meta aggregates may explain execution shape, but they must not be treated as raw reasoning access or quality ground truth.
