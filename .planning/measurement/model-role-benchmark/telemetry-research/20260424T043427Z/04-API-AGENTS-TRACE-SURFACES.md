# Lane 04 - API, Agents, and Trace Surfaces

Retrieval date: 2026-04-24

Scope: OpenAI Agents SDK traces/evals, OpenAI API exposure, Anthropic API exposure, Claude Code differences, and OpenTelemetry GenAI conventions. No live provider/API calls were made. This file is a research artifact, not an implementation plan.

## Self-Audit Result

Revision required: yes. The first lane artifact answered the core direction but did not make every major claim auditable enough under the repaired delegation contract. This revision converts the work into explicit claim tables with evidence class, source URL/path, retrieval date, confidence, known gaps, and ontology/plugin/storage implications.

## Source Register

| ID | Source | Evidence class | URL/path | Retrieval date | Use |
| --- | --- | --- | --- | --- | --- |
| OAI-AGENTS-TRACE | OpenAI Agents SDK tracing docs | verified-doc | https://openai.github.io/openai-agents-python/tracing/ | 2026-04-24 | Trace/span concepts, default traced operations, sensitive-data controls, processors, ZDR caveat. |
| OAI-AGENTS-SPANS | OpenAI Agents SDK span data API reference | verified-doc | https://openai.github.io/openai-agents-python/ref/tracing/span_data/ | 2026-04-24 | Exported span-data classes and fields. |
| OAI-AGENT-EVALS | OpenAI agent evals guide | verified-doc | https://developers.openai.com/api/docs/guides/agent-evals | 2026-04-24 | Trace grading, datasets, eval runs for agent workflows. |
| OAI-TRACE-GRADING | OpenAI trace grading guide | verified-doc | https://developers.openai.com/api/docs/guides/trace-grading | 2026-04-24 | Graded traces and trace eval workflow. |
| OAI-RESPONSES | OpenAI Responses API reference | verified-doc | https://platform.openai.com/docs/api-reference/responses/object | 2026-04-24 | Usage fields, service tier, response model, tool controls, reasoning/caching fields. |
| OAI-DEBUG | OpenAI API request debugging reference | verified-doc | https://platform.openai.com/docs/api-reference/debugging-requests | 2026-04-24 | Request IDs, client request IDs, API meta headers, rate-limit headers. |
| OAI-USAGE | OpenAI organization usage API reference | verified-doc | https://platform.openai.com/docs/api-reference/usage | 2026-04-24 | Aggregate usage/cost fields and grouping dimensions. |
| OAI-PY-SDK | OpenAI Python SDK README | verified-doc | https://github.com/openai/openai-python/blob/main/README.md | 2026-04-24 | SDK `_request_id` and retry behavior. |
| ANT-MESSAGES | Anthropic Messages guide | verified-doc | https://docs.anthropic.com/en/api/messages-examples | 2026-04-24 | Messages response shape, model, stop reason, usage. |
| ANT-ERRORS | Anthropic API errors docs | verified-doc | https://docs.anthropic.com/en/api/errors | 2026-04-24 | Request-id header and error-body request_id. |
| ANT-RATE | Anthropic API rate-limit docs | verified-doc | https://docs.anthropic.com/en/api/rate-limits | 2026-04-24 | RPM/ITPM/OTPM, retry-after, rate-limit headers, cache-token limit semantics. |
| ANT-TIERS | Anthropic service tiers docs | verified-doc | https://docs.anthropic.com/en/api/service-tiers | 2026-04-24 | Requested and assigned service_tier, priority-tier headers. |
| CC-OTEL | Claude Code monitoring docs | verified-doc | https://docs.anthropic.com/en/docs/claude-code/monitoring-usage | 2026-04-24 | Claude Code OTel metrics/events and privacy defaults. |
| CC-COSTS | Claude Code cost docs | verified-doc | https://docs.anthropic.com/en/docs/claude-code/costs | 2026-04-24 | `/cost`, console cost tracking, background token usage. |
| OTEL-GENAI | OpenTelemetry GenAI semantic conventions | verified-doc | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/ | 2026-04-24 | Provider-neutral GenAI span/usage/tool attributes and privacy guidance. |
| ORCH | Research orchestration | local-observed | `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md` | 2026-04-24 | Evidence taxonomy, no-mutation policy, lane scope, ontology constraints. |
| LANE-SPECS | Repaired lane contract | local-observed | `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/LANE-SPECS-AND-PROMPTS.md` | 2026-04-24 | Strict research contract, required question map, pitfalls. |

## Executive Answer

OpenAI Agents SDK traces can normalize into the same ontology, but only as a provider/source adapter, not as the ontology itself. The shared ontology should model traces, spans, provider calls, tool calls, handoffs, guardrails, usage observations, request IDs, rate-limit observations, retry observations, cost observations, and routing observations with explicit source provenance. OpenAI, Anthropic, OTel, Codex CLI, Claude Code, and local harness logs should remain distinct source kinds.

Evidence basis: OAI-AGENTS-TRACE, OAI-AGENTS-SPANS, OAI-RESPONSES, ANT-MESSAGES, CC-OTEL, OTEL-GENAI, ORCH, LANE-SPECS. Evidence class: verified-doc plus local-observed. Confidence: high for normalizability direction; medium for exact OpenAI trace dashboard payload because no live trace export/dashboard inspection was allowed. Known gaps: no live API call, no dashboard trace sample, no paid/provider run, no local provider config mutation. Ontology/plugin/storage implication: build stable internal concepts and versioned adapter mappings; do not store provider field names as core ontology names.

## Required Question Coverage

| Lane 04 question | Answer | Evidence | Confidence | Known gaps | Ontology/plugin/storage implication |
| --- | --- | --- | --- | --- | --- |
| Can OpenAI Agents SDK traces normalize into the same ontology? | Yes, if modeled as trace/span/source observations and not as the canonical schema. | OAI-AGENTS-TRACE, OAI-AGENTS-SPANS, OTEL-GENAI, ORCH | high | No live trace export sampled. | `source_kind=agents_sdk_trace`; adapter maps SDK spans to internal trace/span/provider_call/tool_call concepts. |
| What API exposure exists beyond CLI logs? | Direct APIs expose response usage, model/tier, request IDs, rate-limit headers, and some aggregate cost/usage surfaces that CLI logs may not expose. | OAI-RESPONSES, OAI-DEBUG, OAI-USAGE, ANT-MESSAGES, ANT-ERRORS, ANT-RATE, ANT-TIERS | high | No live headers sampled; only documented exposure. | API adapters must be separate from CLI/harness adapters and should store HTTP metadata observations. |
| How does OTel GenAI map? | OTel GenAI supplies useful external semantic keys for operations, provider, model, input/output/cache tokens, and tool spans, but conventions are development status. | OTEL-GENAI | high | No chosen OTel collector/exporter tested. | Store internal concepts plus `otel_semconv_key` and convention version/stability metadata. |
| Token categories, cache tokens, reasoning tokens? | Input/output are common; cache semantics differ; OpenAI exposes cached input and reasoning tokens; Anthropic exposes cache creation/read input tokens and no confirmed reasoning-token counter here. | OAI-RESPONSES, OAI-USAGE, ANT-RATE, ANT-TIERS, OTEL-GENAI | high for documented fields; medium for cross-provider equivalence | No raw examples from live calls. | Token plugin must keep categories separate and carry provider denominator semantics. |
| Tool calls? | OpenAI API and Agents SDK expose tool surfaces; Anthropic API exposes tool use through Messages content/stop reasons; Claude Code exposes tool-result events as CLI telemetry. | OAI-RESPONSES, OAI-AGENTS-SPANS, ANT-MESSAGES, CC-OTEL, OTEL-GENAI | high | Exact per-provider tool-call payloads were not sampled live. | Tool-call model needs requested tool, executed tool, built-in/server tool, MCP tool, function tool, and CLI/harness tool distinctions. |
| Cost? | OpenAI Responses and Anthropic Messages examples do not expose direct per-request dollar cost; OpenAI org usage has aggregate cost/usage; Claude Code exposes approximate session cost metrics. | OAI-RESPONSES, OAI-USAGE, ANT-MESSAGES, CC-OTEL, CC-COSTS | medium-high | Anthropic billing API not researched here; no billing export sampled. | Store cost evidence modes: `provider_reported`, `aggregate_allocated`, `estimated`, `approx_cli`, `not_exposed`. |
| Request IDs? | OpenAI documents `x-request-id`, SDK `_request_id`, and `X-Client-Request-Id`; Anthropic documents `request-id` header, error `request_id`, and SDK response property. | OAI-DEBUG, OAI-PY-SDK, ANT-ERRORS | high | No live headers sampled. | Store external IDs with provider/source scope and distinguish server-generated from client-supplied IDs. |
| Rate limits? | OpenAI documents `x-ratelimit-*`; Anthropic documents `anthropic-ratelimit-*`, priority headers, and `retry-after`. | OAI-DEBUG, ANT-RATE, ANT-TIERS | high | Header presence can vary by endpoint/account; no live sample. | Store rate-limit observations as header facts with timestamp/source, not as global quota truth. |
| Retries? | OpenAI Python SDK retries selected transient failures twice by default; Anthropic API documents retry-after and retryable rate/overload conditions but SDK retry defaults were not researched here. | OAI-PY-SDK, ANT-RATE, ANT-ERRORS | high for OpenAI SDK; medium for Anthropic retry policy | Anthropic SDK retry behavior deferred. | Store retry policy separately from retry attempts; missing attempts are `unknown`, not zero. |
| Effective routing? | OpenAI exposes response `model` and effective `service_tier` when tier is set; Anthropic exposes response `model` and assigned `usage.service_tier`. This is partial routing, not full internal router trace. | OAI-RESPONSES, ANT-MESSAGES, ANT-TIERS, OTEL-GENAI | high for exposed fields; medium for routing inference | No provider internal router visibility. | Store requested vs effective model/tier separately; mark internal routing as `not_exposed` unless observed. |
| Generic API traces versus CLI/harness traces? | Must remain distinct: API traces are request/span/header/body observations; CLI/harness traces are session/tool/activity/local-run observations. | OAI-DEBUG, OAI-AGENTS-TRACE, ANT-ERRORS, CC-OTEL, ORCH | high | Codex/Claude local lane details owned by lanes 02/03. | `source_kind` and privacy/content policy must drive adapters and storage. |

## OpenAI Agents SDK Trace Claims

| Claim | Evidence class | Source/citation | Retrieval date | Confidence | Known gaps | Ontology/plugin/storage implications |
| --- | --- | --- | --- | --- | --- | --- |
| Agents SDK traces represent end-to-end workflow operations and contain spans. Trace metadata includes workflow name, trace ID, optional group ID, disabled state, and metadata. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | No live dashboard trace inspected. | Internal schema should have `trace`, `trace_external_id`, `workflow_name`, `group_id`, and metadata payload refs. |
| SDK spans represent timed operations with trace ID, optional parent ID, and span-specific data. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | Exact backend-retained fields not verified. | Store span edges explicitly; do not infer hierarchy solely from ordering. |
| Default SDK tracing covers runner calls, agent runs, LLM generations, function tool calls, guardrails, handoffs, transcription, speech, and speech groups. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | Coverage may depend on SDK version and run configuration. | Adapter should map span type to internal `operation_name` and preserve unknown future span types. |
| SDK tracing is enabled by default but can be disabled by environment variable, code, or run config. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | No local SDK config inspected. | Missing traces may mean disabled/not-enabled, not that no operations happened. |
| ZDR organizations cannot use OpenAI tracing. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | Organization policy not inspected. | Storage must allow `not_available_due_to_policy`; plugins should not require OpenAI-hosted traces. |
| Custom trace processors can add or replace processors and can export traces to non-OpenAI destinations. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | No processor implementation tested. | OpenAI Agents adapter can be local/exporter-based, avoiding dashboard dependency. |
| SDK trace sensitive data capture is configurable; generation and function spans can include sensitive input/output unless disabled. | verified-doc | OAI-AGENTS-TRACE | 2026-04-24 | high | No actual captured content inspected. | Privacy contract must default to payload refs/redaction; raw content capture requires explicit opt-in fixture and policy. |
| `AgentSpanData` exports agent name, handoffs, tools, and output type. | verified-doc | OAI-AGENTS-SPANS | 2026-04-24 | high | Metadata behavior is not fully captured in the documented export excerpt. | Map to agent node plus advertised capabilities; do not treat listed tools as executed calls. |
| `TaskSpanData` and `TurnSpanData` can export usage bags. | verified-doc | OAI-AGENTS-SPANS | 2026-04-24 | high | Usage bag schema is not provider-normalized by the span-data doc. | Usage parser must be provider/version aware and retain raw field path. |
| `FunctionSpanData` exports function name, input, output, and optional MCP data. | verified-doc | OAI-AGENTS-SPANS | 2026-04-24 | high | Inputs/outputs may contain private content; no local sample copied. | Tool-call storage needs content redaction, payload refs, MCP namespace, and execution outcome fields. |
| `GenerationSpanData` exports input, output, model, model_config, and usage. | verified-doc | OAI-AGENTS-SPANS | 2026-04-24 | high | No live usage bag sampled. | Map to provider_call span; store request model/config separately from response/effective model when available. |
| `ResponseSpanData` exports response ID and usage. | verified-doc | OAI-AGENTS-SPANS | 2026-04-24 | high | Does not prove all response object fields are exported. | Link SDK trace spans to Responses API objects by `response_id` when present. |
| `HandoffSpanData` exports source and destination agents. | verified-doc | OAI-AGENTS-SPANS | 2026-04-24 | high | No sampled handoff chain. | Store handoffs as directed edges, not as generic tool calls. |

Normalizability decision: adopt. Evidence class: inferred from verified-docs OAI-AGENTS-TRACE, OAI-AGENTS-SPANS, OTEL-GENAI. Confidence: high. Known gap: live export not sampled. Implication: implement `openai_agents_sdk` as an adapter that emits internal trace/span/tool/handoff/guardrail/provider-call observations plus raw payload refs.

## OpenAI API Exposure Claims

| Signal | Claim | Evidence class | Source/citation | Retrieval date | Confidence | Known gaps | Ontology/plugin/storage implications |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Token categories | Responses API exposes response `usage.input_tokens`, `usage.output_tokens`, and `usage.total_tokens`. | verified-doc | OAI-RESPONSES | 2026-04-24 | high | No live call sampled. | Store usage as observed provider counters with units and raw field paths. |
| Cache tokens | Responses API exposes `usage.input_tokens_details.cached_tokens`; org usage exposes aggregate `input_cached_tokens`. | verified-doc | OAI-RESPONSES, OAI-USAGE | 2026-04-24 | high | OpenAI docs reviewed here do not split cache read/write in per-response usage. | Do not map OpenAI cached tokens blindly to Anthropic cache read/write; keep provider namespace. |
| Reasoning tokens | Responses API exposes `usage.output_tokens_details.reasoning_tokens`; `max_output_tokens` includes visible output plus reasoning tokens. | verified-doc | OAI-RESPONSES | 2026-04-24 | high | No model-specific reasoning effort/effective reasoning field sampled. | Store `reasoning_tokens` as provider-specific token subtype; separate from visible output. |
| Reasoning content | Responses API include option lists `reasoning.encrypted_content` for stateless/ZDR use cases. | verified-doc | OAI-RESPONSES | 2026-04-24 | medium-high | This is encrypted continuation material, not inspectable reasoning text. | Store as sensitive provider payload ref if captured; do not treat as quality truth. |
| Tool controls | Requests include `tools`, `tool_choice`, `parallel_tool_calls`, and `max_tool_calls`; tools include built-in tools, MCP tools, and function calls. | verified-doc | OAI-RESPONSES | 2026-04-24 | high | Tool output item details were not live-sampled. | Tool plugin must distinguish model-declared tools from executed tool spans/results. |
| Effective model | Response object includes `model`. | verified-doc | OAI-RESPONSES | 2026-04-24 | high | Does not reveal internal router path. | Store requested_model and effective_model separately. |
| Effective tier | When `service_tier` is set, response body includes the service tier actually used and may differ from the requested parameter. | verified-doc | OAI-RESPONSES | 2026-04-24 | high | No account-specific tier sampled. | Store requested_service_tier and effective_service_tier separately. |
| Request ID | API headers include `x-request-id`; SDK exposes `_request_id`; failed SDK requests expose request IDs on `APIStatusError`. | verified-doc | OAI-DEBUG, OAI-PY-SDK | 2026-04-24 | high | No live header captured. | Store server request ID as provider-scoped external ID. |
| Client request ID | `X-Client-Request-Id` can be supplied by callers and OpenAI logs it for supported endpoints. | verified-doc | OAI-DEBUG | 2026-04-24 | high | Support lookup behavior not tested. | Store caller ID separately from provider server ID; useful for trace correlation. |
| Rate limits | API debugging reference lists `x-ratelimit-limit-*`, `x-ratelimit-remaining-*`, and `x-ratelimit-reset-*` headers for requests/tokens. | verified-doc | OAI-DEBUG | 2026-04-24 | high | Header availability may vary by endpoint/response. | Store rate-limit headers as request-time observations; do not promote to global quota state without aggregation rules. |
| Processing metadata | API headers include `openai-organization`, `openai-processing-ms`, and `openai-version`. | verified-doc | OAI-DEBUG | 2026-04-24 | high | Not all headers may be exposed through every SDK abstraction. | Store HTTP metadata payload separately from model usage. |
| Retries | OpenAI Python SDK retries connection errors, 408, 409, 429, and >=500 errors twice by default; configurable by `max_retries`. | verified-doc | OAI-PY-SDK | 2026-04-24 | high | Retry attempts are not necessarily represented in API response bodies. | Store retry policy, configured max retries, and observed attempts separately; absent attempt count is unknown. |
| Cost | Responses API exposes token usage but not per-response dollar cost in the documented response object. | verified-doc plus inferred | OAI-RESPONSES | 2026-04-24 | high | Pricing table and billing export not inspected here. | Per-request cost must be `not_exposed`, `estimated`, or allocated from aggregate billing, not observed. |
| Aggregate usage/cost | Org usage/cost surfaces expose bucketed aggregate usage/cost with grouping dimensions including model/project/user/api key and service tier for usage. | verified-doc | OAI-USAGE | 2026-04-24 | medium-high | Requires admin credentials/live API to retrieve actual account data; not done. | Aggregate billing adapter should produce aggregate observations, not overwrite per-request records. |

## Anthropic API And Claude Code Claims

| Surface | Claim | Evidence class | Source/citation | Retrieval date | Confidence | Known gaps | Ontology/plugin/storage implications |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Anthropic API usage | Messages examples expose `usage.input_tokens` and `usage.output_tokens` in successful responses. | verified-doc | ANT-MESSAGES | 2026-04-24 | high | No live response sampled. | Store as provider counters; preserve Anthropic-specific cache denominator rules where present. |
| Anthropic response model/routing | Messages examples include response `model`; service-tier docs show response `usage.service_tier` when tier assignment is used. | verified-doc | ANT-MESSAGES, ANT-TIERS | 2026-04-24 | high | Full internal routing is not exposed. | Store effective_model and assigned service_tier; internal route remains `not_exposed`. |
| Anthropic request ID | Every API response includes `request-id`; error bodies include `request_id`; SDKs expose request ID on top-level response objects. | verified-doc | ANT-ERRORS | 2026-04-24 | high | No live header sampled. | Store as provider-scoped request ID; keep body/header variants linked. |
| Anthropic rate limits | Rate limits are measured by RPM, ITPM, and OTPM; 429 responses include `retry-after`; response headers expose limits, remaining counts, and reset times. | verified-doc | ANT-RATE | 2026-04-24 | high | Account-specific values unavailable without live calls. | Rate-limit plugin must support request, input-token, output-token, and priority-tier dimensions. |
| Anthropic cache tokens | Anthropic distinguishes `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`; total input is the sum of all three, and cache reads usually do not count toward ITPM for most models. | verified-doc | ANT-RATE | 2026-04-24 | high | Model exceptions exist; actual model marker not sampled. | Token plugin must store cache creation/read separately and carry rate-limit inclusion semantics. |
| Anthropic service tier | `service_tier` request values include `auto` and `standard_only`; response usage includes assigned tier; priority headers can indicate priority capacity. | verified-doc | ANT-TIERS | 2026-04-24 | high | No account with priority tier inspected. | Store requested_tier, assigned_tier, and priority-capacity headers separately. |
| Anthropic cost | Messages response examples do not show per-response dollar cost. | verified-doc plus inferred | ANT-MESSAGES | 2026-04-24 | medium-high | Anthropic billing/usage APIs were not researched in this lane. | Mark per-request cost as `not_exposed` unless another adapter proves billing data. |
| Anthropic retry behavior | API docs expose retry-after and retryable rate/overload classes, but Anthropic SDK automatic retry defaults were not researched here. | verified-doc plus deferred | ANT-RATE, ANT-ERRORS | 2026-04-24 | medium | SDK retry defaults deferred. | Retry plugin should ingest API headers/errors now; SDK policy adapter can be added later. |
| Claude Code OTel | Claude Code OTel exports CLI metrics/events including session count, token usage, cost usage, active time, tool-result events, prompt events, and session/user/terminal attributes. | verified-doc | CC-OTEL | 2026-04-24 | high | Does not prove raw Anthropic request headers are exposed. | Treat as `source_kind=cli_harness`, not `anthropic_api`. |
| Claude Code cost | Claude Code cost metric is approximate; official billing data remains provider billing/console data. | verified-doc | CC-OTEL, CC-COSTS | 2026-04-24 | high | No local Claude Code OTel capture performed. | Store `cost_evidence_mode=approx_cli`; do not reconcile as authoritative billing. |
| Claude Code privacy | User prompt content is redacted by default in OTel logs unless opted in; metrics do not include API keys or file contents per docs. | verified-doc | CC-OTEL | 2026-04-24 | high | Local settings not inspected by this lane. | Privacy contract must preserve redaction defaults and avoid raw transcript persistence. |
| Claude Code background usage | Claude Code can consume tokens for background work such as summarization and command processing. | verified-doc | CC-COSTS | 2026-04-24 | medium-high | Amount is session/config/version dependent. | Token/cost observations from CLI must include background/substitute attribution when available. |

## OTel GenAI Mapping Claims

| Claim | Evidence class | Source/citation | Retrieval date | Confidence | Known gaps | Ontology/plugin/storage implications |
| --- | --- | --- | --- | --- | --- | --- |
| OTel GenAI defines required/recommended span attributes including operation name, provider name, conversation ID, request model, response model, input tokens, output tokens, cache creation tokens, and cache read tokens. | verified-doc | OTEL-GENAI | 2026-04-24 | high | Semantic conventions are marked development. | Use as export/view mapping, not as immutable internal schema. |
| OTel GenAI well-known operations include `chat`, `text_completion`, `embeddings`, `retrieval`, `execute_tool`, `invoke_agent`, and `create_agent`. | verified-doc | OTEL-GENAI | 2026-04-24 | high | Future convention versions may add/rename fields. | Store `operation_name` internally and optional `otel_operation_name` mapping. |
| OTel GenAI has an `execute_tool` span convention with tool name/type/arguments/result; arguments and results are sensitive and opt-in. | verified-doc | OTEL-GENAI | 2026-04-24 | high | No OTel exporter tested. | Tool adapter should support content redaction and payload refs. |
| OTel GenAI says instructions, inputs, and outputs are sensitive and should not be captured by default. | verified-doc | OTEL-GENAI | 2026-04-24 | high | Local export policy not configured/tested. | Default storage should avoid raw prompts/outputs/tool args and retain only structural metadata unless explicitly opted in. |
| OTel GenAI development status requires version/stability handling. | verified-doc | OTEL-GENAI | 2026-04-24 | high | Exact emitted semconv version varies by instrumentation. | Store semconv namespace/version/stability with imported spans. |

Mapping recommendation:

| Internal concept | OTel GenAI view/export candidate | Evidence | Confidence | Gap/mitigation |
| --- | --- | --- | --- | --- |
| Provider call span | `gen_ai.operation.name=chat/generate_content/text_completion`, `gen_ai.provider.name`, model attrs | OTEL-GENAI | high | Use provider adapter for endpoint-specific naming. |
| Agent invocation span | `invoke_agent` or source-specific custom span plus internal `agent_run` | OTEL-GENAI, OAI-AGENTS-SPANS | medium-high | Agents SDK span taxonomy is richer than OTel core agent operations; preserve source type. |
| Tool execution span | `execute_tool`, `gen_ai.tool.*` | OTEL-GENAI, OAI-AGENTS-SPANS, CC-OTEL | high | Separate model-requested tool from actual execution. |
| Usage observation | `gen_ai.usage.*` where category matches | OTEL-GENAI, OAI-RESPONSES, ANT-RATE | high | Cache/reasoning categories need provider-specific extensions. |
| Routing observation | `gen_ai.request.model`, `gen_ai.response.model`, provider-specific tier attrs | OTEL-GENAI, OAI-RESPONSES, ANT-TIERS | medium-high | Full internal routing usually not exposed. |

## Exposure Matrix

| Signal | OpenAI API | OpenAI Agents SDK | Anthropic API | Claude Code CLI/OTel | OTel GenAI | Evidence | Confidence | Known gaps | Design implication |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Input tokens | `usage.input_tokens` | Usage bags on generation/response/task/turn spans when populated | `usage.input_tokens` with Anthropic cache-breakpoint semantics | `claude_code.token.usage` metric by type per docs | `gen_ai.usage.input_tokens` | OAI-RESPONSES, OAI-AGENTS-SPANS, ANT-MESSAGES, ANT-RATE, CC-OTEL, OTEL-GENAI | high | No live samples. | Keep provider denominator semantics. |
| Output tokens | `usage.output_tokens` | Usage bags when populated | `usage.output_tokens` | `claude_code.token.usage` | `gen_ai.usage.output_tokens` | same as above | high | No live samples. | Generic category is feasible. |
| Cache tokens | `cached_tokens`; aggregate `input_cached_tokens` | Only if usage bag carries API details | `cache_creation_input_tokens`, `cache_read_input_tokens` | Not documented as cache-specific | cache creation/read attrs | OAI-RESPONSES, OAI-USAGE, ANT-RATE, OTEL-GENAI | high | OpenAI per-response read/write split not found. | Provider-specific cache model required. |
| Reasoning tokens | `reasoning_tokens` | Only if response/generation usage carries it | No confirmed raw counter here | Thinking summaries/facets are substitute in related lanes, not raw tokens | No direct field identified here | OAI-RESPONSES, ORCH | medium-high | Anthropic and OTel gaps. | Use provider extension and missingness states. |
| Tool calls | tools/tool_choice/output items | function spans, agent tools, handoffs, guardrails | Messages tool use by content/stop reason docs; not fully sampled here | tool-result events | `execute_tool` | OAI-RESPONSES, OAI-AGENTS-SPANS, ANT-MESSAGES, CC-OTEL, OTEL-GENAI | high | Exact payload samples deferred. | Store requested/executed/server/MCP/harness tools separately. |
| Cost | Aggregate usage/cost only; no per-response cost found | No per-span cost documented | No per-response cost found here | Approximate cost metric and `/cost` | No standard cost field identified | OAI-USAGE, OAI-RESPONSES, ANT-MESSAGES, CC-OTEL, CC-COSTS | medium | Billing APIs outside reviewed scope. | Cost evidence mode is mandatory. |
| Request IDs | `x-request-id`, SDK `_request_id`, `X-Client-Request-Id` | trace IDs and response IDs, not necessarily HTTP request IDs | `request-id`, error `request_id` | session ID, not raw API request ID per docs | Use generic span attrs/provider namespace | OAI-DEBUG, OAI-PY-SDK, OAI-AGENTS-SPANS, ANT-ERRORS, CC-OTEL | high | No live headers. | External IDs table scoped by source/provider. |
| Rate limits | `x-ratelimit-*` | Not inherent unless HTTP metadata captured by adapter | `anthropic-ratelimit-*`, priority headers, `retry-after` | Not raw API headers in docs | Generic HTTP/provider attrs | OAI-DEBUG, ANT-RATE, ANT-TIERS | high | Account-specific values unavailable. | Header-observation table. |
| Retries | Python SDK default retry policy documented | Not guaranteed as trace spans | API retry-after and retryable errors documented; SDK defaults deferred | Not documented as retry count | Span events can model attempts | OAI-PY-SDK, ANT-RATE, ANT-ERRORS | medium-high | Retry attempts need instrumentation/logs. | Policy and attempts separate. |
| Effective routing | response model and effective service tier | agent, handoff, model spans | response model and assigned service tier | CLI runtime/session attrs only | request/response model attrs | OAI-RESPONSES, OAI-AGENTS-SPANS, ANT-MESSAGES, ANT-TIERS, OTEL-GENAI | medium-high | Internal provider routers opaque. | Requested/effective fields plus `not_exposed` for internals. |

## Generic API Traces Versus CLI/Harness Traces

| Claim | Evidence class | Source/citation | Retrieval date | Confidence | Known gaps | Ontology/plugin/storage implications |
| --- | --- | --- | --- | --- | --- | --- |
| Generic API traces should represent direct provider/API/SDK observations: requests, responses, HTTP headers, provider-call spans, tool-call spans, usage, errors, request IDs, rate-limit headers, and retries. | inferred from verified-docs | OAI-DEBUG, OAI-RESPONSES, OAI-AGENTS-TRACE, ANT-ERRORS, ANT-RATE, OTEL-GENAI | 2026-04-24 | high | Exact runtime adapters not implemented. | `source_kind=api_response`, `agents_sdk_trace`, or `otel_genai`; payload refs for content. |
| CLI/harness traces should represent local execution observations: session, turn, command/tool event, file edit, approval, sandbox, active time, approximate cost, and local benchmark run state. | verified-doc plus inferred | CC-OTEL, CC-COSTS, ORCH | 2026-04-24 | high | Codex/Claude local structures are owned by lanes 02/03. | `source_kind=cli_harness` or `local_artifact`; never use as raw provider API truth without request/header evidence. |
| Claude Code OTel should not be merged with Anthropic API exposure because it is session/CLI telemetry and its cost is approximate. | verified-doc plus inferred | CC-OTEL, CC-COSTS, ANT-MESSAGES, ANT-RATE | 2026-04-24 | high | No local Claude Code OTel capture. | Adapters must declare provenance and reliability level for each observation. |
| OpenAI Agents SDK traces are closer to generic API/workflow traces than CLI logs, but still include application-level agent structure that direct API responses do not. | verified-doc plus inferred | OAI-AGENTS-TRACE, OAI-AGENTS-SPANS, OAI-RESPONSES | 2026-04-24 | high | No live SDK trace payload sampled. | Treat as a first-class adapter source with both provider-call and orchestration spans. |

## Pitfalls And Mitigations

| Pitfall | Relevance to Lane 04 | Evidence basis | Confidence | Mitigation / implication |
| --- | --- | --- | --- | --- |
| Treating Reflect as authoritative | This lane did not rely on Reflect as capability authority. | ORCH, LANE-SPECS | high | Provider capabilities are grounded in official docs; Reflect can only be precedent in other lanes. |
| Designing around Codex only | Lane 04 covers OpenAI API, OpenAI Agents SDK, Anthropic API, Claude Code, and OTel. | Source Register | high | Core ontology must be harness-agnostic and provider-adapter driven. |
| Flattening provider/auth/billing | OpenAI API, Anthropic API, Claude Code cost, and aggregate usage are distinct. | OAI-USAGE, ANT-TIERS, CC-COSTS | high | Store cost/token/quota/rate-limit observations separately with evidence modes. |
| Over-trusting local logs | CLI/harness telemetry is explicitly separated from API/provider traces. | CC-OTEL, ORCH | high | Do not infer provider request headers or per-request cost from CLI logs unless exposed. |
| Mutating config for OTel experiments | No telemetry/exporter config was changed. | ORCH, local process | high | OTel capture remains a future adapter/fixture task. |
| Persisting sensitive transcript content | Agents SDK and OTel docs warn about sensitive inputs/outputs/tool args. | OAI-AGENTS-TRACE, OTEL-GENAI, CC-OTEL | high | Default storage uses structural metadata and payload refs; raw content opt-in only. |
| Treating missing fields as zero | Many fields are not exposed by some surfaces. | ORCH plus all exposure tables | high | Missing states: `not_exposed`, `not_enabled`, `redacted`, `not_collected`, `deferred_live_call`, `unknown`. |
| Treating thinking summaries as reasoning quality | Lane 04 found OpenAI reasoning-token counters but did not equate summaries/facets with reasoning truth. | OAI-RESPONSES, ORCH | high | Reasoning tokens, encrypted reasoning content, summaries, and quality observations are separate concepts. |
| Reintroducing `score.overall` | This lane discusses traces/evals but does not collapse quality into a scalar. | OAI-AGENT-EVALS, OAI-TRACE-GRADING, ORCH | high | Evals should store multidimensional criteria/observations. |
| Overbuilding before provider surfaces are known | This artifact recommends a minimum stable core and adapter mappings, not a generic platform. | LANE-SPECS, all verified docs | high | Build adapters and fixtures around observed/documented surfaces first. |
| Under-specifying plugin boundaries | This artifact names adapter/extractor/view/report/cost/token/tool/rate-limit boundaries. | LANE-SPECS | high | See plugin/storage sections below. |
| Query/rebuild registry drift | Relevant as a storage design pitfall, not directly researched in provider docs. | LANE-SPECS | medium | Store raw payload refs and deterministic adapter outputs so SQLite query cache can be rebuilt. |
| Sanitized reports hiding uncertainty | This revision includes confidence and known gaps for every major claim. | LANE-SPECS | high | Reports should expose evidence mode and missingness, not only normalized summaries. |

## Plugin Boundary Implications

| Plugin boundary | Responsibility | Evidence basis | Confidence | Known gaps | Storage implication |
| --- | --- | --- | --- | --- | --- |
| Provider adapters | Parse OpenAI Responses, OpenAI Agents SDK spans, Anthropic Messages, Anthropic headers, Claude Code OTel, and OTel GenAI into internal observations. | All source docs | high | No implementation yet. | Adapter output should be deterministic and rebuildable from payload refs. |
| Metric extractors | Convert usage/cost/rate/retry/routing fields into typed metric observations with missingness semantics. | OAI-RESPONSES, OAI-USAGE, ANT-RATE, ANT-TIERS, CC-OTEL, OTEL-GENAI | high | Cost estimation policy unresolved. | Metric rows need category, unit, raw field, evidence mode, and provider semantics. |
| View/report plugins | Render provider-neutral benchmark reports without hiding provider-specific caveats. | ORCH, LANE-SPECS | high | Cross-lane synthesis pending. | Views consume normalized facts and include evidence/confidence/gaps. |
| Capability declarations | Declare what each adapter can and cannot expose, such as per-request cost, rate headers, reasoning tokens, cache split, and request IDs. | Exposure matrix | high | Live capability probes deferred. | Capabilities table should distinguish documented, observed, unavailable, and deferred. |
| Privacy/content contracts | Control prompt/output/tool-arg capture, redaction, payload refs, and opt-in raw content. | OAI-AGENTS-TRACE, OTEL-GENAI, CC-OTEL | high | Exact retention policy not chosen. | Raw content should not be in default metric tables. |
| Metric namespaces | Keep core metrics provider-neutral and put provider-only fields under namespaces such as `openai.*`, `anthropic.*`, `claude_code.*`, `otel.gen_ai.*`. | ORCH, OTEL-GENAI | high | Naming convention not implemented. | Avoid provider field names as core schema columns except stable common concepts. |
| Fixtures | Need fixtures for OpenAI cached/reasoning tokens, Anthropic cache read/write, request/rate headers, retry policy, Agents SDK function/handoff spans, and CLI approximate cost. | Exposure matrix | high | Live data cannot be generated in this research pass. | Synthetic or redacted fixtures should exercise missingness and provider-specific denominators. |

## Storage Recommendations

Minimum fields for Lane 04-derived records:

| Field group | Fields | Evidence basis | Confidence | Gap/implication |
| --- | --- | --- | --- | --- |
| Provenance | `observation_id`, `source_kind`, `provider`, `provider_surface`, `evidence_class`, `source_url_or_path`, `retrieval_date`, `confidence`, `observed_state` | ORCH, LANE-SPECS | high | Required to prevent sanitized uncertainty. |
| Trace/span | `trace_id`, `span_id`, `parent_span_id`, `workflow_name`, `group_id`, `operation_name`, `span_type`, `started_at`, `ended_at` | OAI-AGENTS-TRACE, OAI-AGENTS-SPANS, OTEL-GENAI | high | Allow nulls with missingness reason. |
| Request identity | `external_request_id`, `client_request_id`, `response_id`, `conversation_id`, `api_organization`, `api_version` | OAI-DEBUG, OAI-RESPONSES, ANT-ERRORS, OTEL-GENAI | high | Scope IDs by provider/source to avoid collisions. |
| Model/routing | `requested_model`, `effective_model`, `requested_service_tier`, `effective_service_tier`, `routing_evidence_mode` | OAI-RESPONSES, ANT-MESSAGES, ANT-TIERS, OTEL-GENAI | high | Internal provider routing usually `not_exposed`. |
| Usage | `usage_category`, `usage_value`, `usage_unit`, `raw_provider_field`, `provider_denominator_semantics`, `cache_rate_limit_inclusion` | OAI-RESPONSES, OAI-USAGE, ANT-RATE, OTEL-GENAI | high | Anthropic/OpenAI cache meanings differ. |
| Tooling | `tool_call_id`, `tool_name`, `tool_type`, `tool_surface`, `tool_request_or_execution`, `approval_state`, `payload_ref` | OAI-RESPONSES, OAI-AGENTS-SPANS, CC-OTEL, OTEL-GENAI | medium-high | Approval state is more CLI/harness specific and needs lanes 02/03. |
| Cost | `cost_value`, `cost_currency`, `cost_evidence_mode`, `billing_bucket_id`, `pricing_source_ref` | OAI-USAGE, CC-OTEL, CC-COSTS | medium | Per-request provider cost mostly not exposed in reviewed response docs. |
| Rate/retry | `rate_limit_header_name`, `rate_limit_value`, `rate_limit_dimension`, `rate_limit_reset`, `retry_policy_ref`, `retry_attempt_count`, `retry_after` | OAI-DEBUG, OAI-PY-SDK, ANT-RATE, ANT-ERRORS | high for headers/policy; medium for attempts | Attempts need SDK/log instrumentation, not just API docs. |
| Raw payload | `raw_provider_payload_ref`, `payload_redaction_state`, `content_capture_policy` | OAI-AGENTS-TRACE, OTEL-GENAI, CC-OTEL, ORCH | high | Do not store private transcript content by default. |

## Open Questions And Deferred Work

| Question | Evidence class | Status | Reason deferred | Implication |
| --- | --- | --- | --- | --- |
| What exact JSON payload does a live OpenAI Agents SDK processor emit for a multi-agent/tool/handoff run? | deferred | open | Live/provider run and trace export not allowed. | Build adapter against documented span data first; add fixture later. |
| Does OpenAI expose per-request dollar cost in any endpoint outside the reviewed response object? | deferred | open | Billing/cost endpoint details beyond aggregate org usage were not fully researched with credentials. | Cost model must support `not_exposed` and aggregate allocation. |
| What are Anthropic SDK automatic retry defaults? | deferred | open | Lane scope verified API retry-after/errors but not SDK repository behavior. | Add SDK-policy adapter later; do not infer retry attempts now. |
| Which OTel GenAI convention version will target instrumentation emit? | deferred | open | No exporter/instrumentation run allowed. | Store semconv version/stability metadata. |
| Can Claude Code expose raw provider request IDs/rate-limit headers locally? | deferred | open | Lane 03 owns local Claude exposure; Claude Code OTel docs reviewed here do not document raw API headers. | CLI/harness adapter should not claim raw API IDs unless lane 03 proves it. |
| How should multidimensional trace grading map to benchmark rubric observations? | deferred | open | Lane 04 only verified trace grading/evals surfaces. | Evals adapter should map grader criteria to rubric observations, not `score.overall`. |

## Final Recommendation

Adopt a harness-agnostic core with provider/source adapters. Treat OpenAI Agents SDK traces as a first-class source because they expose workflow structure absent from generic API responses, but do not make their span taxonomy the core ontology. Use OTel GenAI as an export/interchange vocabulary where it fits, while storing provider-specific fields in namespaces with raw payload refs, evidence mode, confidence, and missingness. Keep direct API observations separate from CLI/harness observations, especially for request IDs, rate limits, retries, cost, quota, and effective routing.
