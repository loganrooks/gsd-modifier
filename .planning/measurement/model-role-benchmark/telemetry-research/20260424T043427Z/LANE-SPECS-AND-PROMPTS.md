# Lane Specs And Prompt Ledger

This file records the auditable delegation boundary for the telemetry exposure research pass. Lanes 01-04 were launched before this file existed; their exact prompts are recorded post-hoc from the coordinator tool calls. Lanes 05-06 are specified here before launch.

## Coordination Correction

The coordinator briefly performed main-lane evidence gathering after launching lanes 01-04. That was a process error against the intended lane-first orchestration. The gathered notes are not treated as lane evidence and are not authoritative for final synthesis unless independently present in lane artifacts or re-verified during synthesis with citation.

## Common Lane Rules

- Read `ORCHESTRATION.md` before research.
- Write only the lane target file.
- Do not mutate provider configuration, run live provider calls, or perform paid/quota-consuming operations.
- Use structural local inspection only; do not copy private transcript content, raw prompts, assistant messages, tool arguments, or tool outputs.
- Classify claims using the evidence taxonomy in `ORCHESTRATION.md`.
- Include source paths/URLs, commands or citations, confidence, known gaps, and ontology/plugin/storage implications.
- Treat prior Reflect artifacts as `repo-precedent`, not authority.
- You are not alone in the codebase; do not touch files outside the assigned target.

## Delegation Quality Gap And Repair

The initial lane prompts were too compressed. They pointed to `ORCHESTRATION.md` but did not inline enough of the plan's required research questions, artifact contracts, pitfalls, and auditability standards. This is a delegation quality gap because a lane can technically satisfy the short prompt while missing parts of the user's intended evidence package.

Repair action:
- send every lane agent a stricter follow-up self-audit instruction
- require each lane to revise its own target artifact if any required section, evidence table, confidence/gap statement, or research question answer is missing
- keep the original prompt ledger intact for accountability
- disposition lane outputs only after the stricter self-audit completes

## Strict Research Contract For All Lanes

Every lane artifact must be auditable by senior software engineers and AI researchers. That means:

- every material claim must carry an evidence class from `ORCHESTRATION.md`
- every material provider or architecture claim must include source path/URL and retrieval date or local command
- every section must include an evidence table, confidence level, known gaps, and implications for ontology/plugin/storage design
- uncertainty must be explicit; absence of evidence must not be converted into absence of capability
- local file inspection must be structural only and must not copy private prompts, assistant text, tool arguments, tool outputs, or raw transcript content
- official provider docs are primary evidence for provider capabilities; community reports are at most weak context
- Reflect artifacts are useful precedent but never authority
- reports must distinguish direct observation, provider aggregate, derived estimate, substitute signal, and unavailable/not exposed
- token categories, reasoning tokens, cache tokens, API-equivalent cost, provider-reported cost, subscription/quota burn, rate limits, and quota state must remain separate when discussed
- requested model/reasoning and effective model/reasoning must remain separate when discussed
- Claude thinking summaries/facets/session-meta must be labeled derived/substitute and not treated as reasoning tokens or quality truth
- benchmark quality must be multidimensional; do not collapse into `score.overall`
- core ontology must remain harness-agnostic; GSD phases/milestones/plans may attach as domain entities or edges, not core schema assumptions
- plugin boundaries must identify adapter, extractor, view/report, capability declarations, missingness semantics, privacy/content contracts, metric namespaces, and fixtures where relevant

## Required Question Coverage Map

The coordinator owns final coverage, but lanes must answer or explicitly defer the questions in their scope:

- Lane 01: which Reflect telemetry decisions should be inherited directly, adapted, rejected, or deferred; which artifacts are stale, incomplete, or GSD-specific; which anti-patterns must be avoided, especially registry drift, query/rebuild mismatch, source-family collapse, and sanitized reports hiding uncertainty.
- Lane 02: exactly what current Codex OTel exposes; whether Codex OTel can be captured locally without external services; what Codex exposes through `state_5.sqlite`, rollout JSONL, config/docs; requested versus effective model/reasoning; token/cost/quota exposure; hierarchy across sessions, turns, tools, subagents, compaction, approvals, sandbox, git, and routing evidence.
- Lane 03: stability of Claude session-meta and local JSONL schemas; local-file-only versus OTel-only versus hooks/plugins/skills/raw-API-body-only exposure; privacy/data-use caveats; thinking summaries/facets as substitute signals; token/cost/rate/quota exposure; hierarchy and subagent/sidechain recovery.
- Lane 04: OpenAI Agents SDK trace normalizability; OpenAI API and Anthropic API exposure beyond CLI logs; OTel GenAI mapping; token categories, cache/reasoning tokens, tool calls, request IDs, rate limits, retries, cost, and effective routing; generic API traces versus CLI/harness traces.
- Lane 05: task definition versus task instance; exact definition of run; whether one session can contain many runs and whether one run can span sessions; minimum SQLite schema for hierarchy without overfitting to GSD; JSONL as evidence/import/export and SQLite as rebuildable query cache; fixtures for hierarchy, missingness, subagents, compaction, token accounting, and rubric observations.
- Lane 06: plugin protocol for provider adapters, metric extractors, and domain views; how harness metrics are added without core schema changes; privacy/content contracts; evidence/reliability semantics; base metrics versus provider and domain plugins; multidimensional rubric observations; required golden fixtures; first implementation recommendation from a plugin perspective.

## Research Pitfalls That Must Be Addressed

Each lane should call out relevant pitfalls and mitigations:

- treating Reflect as authoritative
- designing around Codex only
- flattening provider/auth/billing
- over-trusting local logs
- mutating config for OTel experiments
- persisting sensitive transcript content
- treating missing fields as zero
- treating thinking summaries as reasoning quality
- reintroducing `score.overall`
- overbuilding a generic telemetry platform before provider surfaces are known
- under-specifying plugin boundaries
- query/rebuild registry drift
- sanitized reports hiding uncertainty

## Lane 01 Prompt Sent

Agent: `019dbdc5-9ea2-7193-9454-4a1d3cfd74a4` (`Kant`)
Model profile requested: `gpt-5.5 medium`
Disposition: `pending`

```text
You are Lane 01 - Critical Reflect Inheritance for the telemetry exposure research package in /home/rookslog/workspace/projects/gsd-modifier. Read .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md first. Write only .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/01-REFLECT-INHERITANCE-REVIEW.md. Read-only inspect /home/rookslog/workspace/projects/get-shit-done-reflect Phase 57, 57.5, 57.6, 57.7, 60.1 artifacts and relevant measurement source files. Classify inherited ideas as adopt/adapt/defer/reject, with evidence class, path, command, confidence, gaps, and ontology/plugin/storage implications. Include Phase 57.5 registry/store/query parity and Phase 60.1 provenance integration. Do not treat Reflect as authoritative; mark as repo-precedent unless independently verified. Do not copy private transcript content. You are not alone in the codebase; do not touch files outside your target.
```

## Lane 02 Prompt Sent

Agent: `019dbdc5-9f23-7751-8f92-5b48b918ede4` (`James`)
Model profile requested: `gpt-5.5 medium`
Disposition: `pending`

```text
You are Lane 02 - Codex Exposure Research for the telemetry exposure research package in /home/rookslog/workspace/projects/gsd-modifier. Read .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md first. Write only .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/02-CODEX-EXPOSURE.md. Inspect ~/.codex/state_5.sqlite and ~/.codex/sessions/**/*.jsonl read-only, structural fields only. Verify current official OpenAI/Codex docs for OTel, config, custom providers, auth modes, model/reasoning settings, rate limits, and local logs. Answer what Codex exposes through SQLite, rollout JSONL, OTel, and docs/config, and whether OTel can be captured locally without persistent config mutation; defer if mutation/setup required. Map observed fields to session, turn, model call, tool call, subagent, compaction, token, cost/quota, approval, sandbox, git, and routing evidence concepts. Include evidence class, URL/path, command/citation, confidence, gaps, and implications. Do not mutate config, run providers, or copy transcript content. You are not alone in the codebase; do not touch files outside your target.
```

## Lane 03 Prompt Sent

Agent: `019dbdc5-9f92-75a2-81f7-f36beea876f7` (`Turing`)
Model profile requested: `gpt-5.5 medium`
Disposition: `pending`

```text
You are Lane 03 - Claude Code Exposure Research for the telemetry exposure research package in /home/rookslog/workspace/projects/gsd-modifier. Read .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md first. Write only .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/03-CLAUDE-EXPOSURE.md. Inspect ~/.claude/usage-data/session-meta/*.json and ~/.claude/projects/**/*.jsonl read-only, structural fields only. Verify current official Anthropic/Claude Code docs for OTel, monitoring, data usage, hooks, plugins, skills, raw API body refs, compaction, and privacy controls. Determine local-file-only, OTel-only, hook/plugin-visible, raw-API-body-gated, and unavailable surfaces. Assess schema stability of session-meta and JSONL from local samples and docs. Treat thinking summaries/facets/session-meta as derived/substitute signals, never raw reasoning or quality truth. Include evidence class, URL/path, command/citation, confidence, gaps, and ontology/plugin/storage implications. Do not mutate config, run providers, or copy transcript content. You are not alone in the codebase; do not touch files outside your target.
```

## Lane 04 Prompt Sent

Agent: `019dbdc5-a053-7691-9da7-b75b189abb12` (`Kuhn`)
Model profile requested: `gpt-5.5 medium`
Disposition: `pending`

```text
You are Lane 04 - API, Agents, and Trace Surfaces for the telemetry exposure research package in /home/rookslog/workspace/projects/gsd-modifier. Read .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/ORCHESTRATION.md first. Write only .planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/04-API-AGENTS-TRACE-SURFACES.md. Research official OpenAI Agents SDK traces/evals, OpenAI API usage fields, Anthropic API/Claude Code differences, and OTel GenAI conventions. Determine whether OpenAI Agents SDK traces can normalize into the same ontology. Identify API exposure for token categories, cache tokens, reasoning tokens, tool calls, cost, request IDs, rate limits, retries, and effective routing. Separate generic API traces from CLI/harness traces. Include evidence class, URL, retrieval date, confidence, gaps, and ontology/plugin/storage implications. No live API calls. You are not alone in the codebase; do not touch files outside your target.
```

## Lane 05 Spec Before Launch

Write target: `05-ONTOLOGY-STORAGE-OPTIONS.md`
Model profile requested: `gpt-5.5 medium`
Agent: `019dbdc9-f337-7391-9b22-e4efe0722ca3` (`Helmholtz`)
Disposition: `pending`

Responsibilities:
- Design at least two ontology/storage designs:
  - event-first with derived entities
  - entity/edge/observation relational model
- Recommend one design and justify it against provider exposure uncertainty.
- Include proposed SQLite tables, core IDs, edge semantics, JSON payload strategy, indexes, rebuild behavior, and raw artifact references.
- Model sessions, work units, task definitions, task instances, runs, turns, model calls, tool calls, subagents, file changes, metric observations, rubric observations, cost estimates, artifacts, and entity edges.
- Explain how JSONL remains useful as import/export/manual evidence while SQLite is a rebuildable query cache.
- Review lanes 01-04 for ontology implications when available; if not available yet, explicitly mark the review as pending and write assumptions that the coordinator must revisit.

## Lane 06 Spec Before Launch

Write target: `06-PLUGIN-PROTOCOL-METRICS.md`
Model profile requested: `gpt-5.5 medium`
Agent: `019dbdc9-f3ab-7372-a642-3e3e817c7848` (`Zeno`)
Disposition: `pending`

Responsibilities:
- Define adapter, extractor, and view/report plugin protocols.
- Separate base-core metrics from provider plugins and harness/domain plugins.
- Explain how harness-design metrics can be added without touching core schema.
- Include plugin manifest shape, capability declarations, missingness behavior, privacy/content contracts, metric namespace rules, evidence/reliability semantics, and fixture requirements.
- Define multidimensional rubric observation storage and explicitly avoid `score.overall`.
- Review lanes 01-05 for plugin extensibility gaps when available; if not available yet, explicitly mark the review as pending and write assumptions that the coordinator must revisit.
