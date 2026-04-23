# Model Role Benchmark Research Dispatch

## Dispatch Policy

Research runs before benchmark runner implementation. Agents are read-only and must not modify repo files. Their outputs should be written by the orchestrator into this packet after review, or returned as structured text for later checked-in synthesis.

Use `OPINION-MINING-PLAN.md` for token-efficient anecdote collection. This file governs source qualification and synthesis once evidence has been collected.

Use this requested profile for every synthesis and methodology lane:

```json
{
  "agent_type": "default",
  "model": "gpt-5.5",
  "reasoning_effort": "high",
  "mode": "read-only research"
}
```

Reasoning: this is meta-research and methodology design, not a candidate-scored benchmark run. Candidate comparisons begin only when the local task runner exists.

Use cheaper collection agents only for narrow fetch passes:

```json
{
  "agent_type": "default",
  "model": "gpt-5.4",
  "reasoning_effort": "medium",
  "mode": "read-only collection"
}
```

Collection agents must not synthesize conclusions. They only return compact source inventories and short evidence excerpts within the limits in `OPINION-MINING-PLAN.md`.

## Shared Research Rules

Every research agent must:

- State research mode: terrain mapping unless the lane says otherwise.
- Record query strings, source URLs, access date, and source type.
- Separate official claims, independent benchmarks, anecdotes, and inference.
- Tag claims as `official`, `benchmark`, `independent-analysis`, `anecdote`, `local-observation`, `inference`, or `unknown`.
- Include contrary evidence and limitations.
- Avoid long quotations; summarize instead.
- Treat launch-window user reports as weak evidence unless multiple independent reports converge.
- Return a source table and a claim table.

## Dispatch Wrapper

Use this wrapper for every lane, replacing `{LANE}` and `{LANE_BRIEF}` with the lane-specific section below:

```text
You are a read-only research agent for gsd-modifier's model-role benchmark design packet.

Requested runtime profile:
- model: gpt-5.5
- reasoning_effort: high
- write behavior: do not edit files; return structured Markdown only

Read these local packet files first:
- .planning/measurement/model-role-benchmark/README.md
- .planning/measurement/model-role-benchmark/PREDICTIONS.md
- .planning/measurement/model-role-benchmark/RUBRIC.md
- .planning/measurement/model-role-benchmark/SOURCES.md
- .planning/measurement/model-role-benchmark/OPINION-MINING-PLAN.md

Research lane: {LANE}

Lane brief:
{LANE_BRIEF}

Required output:
- Research Frame
- Path Of Inquiry
- Assumptions Surfaced
- Evidence Base
- Claim Table
- Source Table
- Unknowns And Deferrals
- Implications For Predictions
- Implications For Runner Design

Claim Table columns:
- claim
- claim_type: official | benchmark | independent-analysis | anecdote | local-observation | inference | unknown
- source
- confidence: high | medium | low
- caveat

Source Table columns:
- source
- type
- query_or_entrypoint
- access_date
- method_quality_notes

Do not print or inspect secrets. If a local source might contain credentials, describe the safe metadata that should be checked instead.
```

## Lane 1: Benchmark Methodology Researcher

Question: What model-evaluation methods are most relevant for agentic coding roles like planning, execution, and review?

Scope:

- Official GPT-5.5 and GPT-5.4 release claims.
- Coding benchmarks such as SWE-style and Terminal-style tasks.
- Known limitations of public coding benchmarks for repo-local agent workflows.
- Best practices for paired model comparisons.

Non-goals:

- Do not recommend production defaults.
- Do not rely on marketing claims without qualification.

Required output:

- Methodology risks.
- Benchmark categories relevant to this repo.
- Recommendations for local experiment design.
- Source quality assessment.

## Lane 2: Public Reaction Researcher

Question: What are users reporting about GPT-5.5 in Codex, and how reliable are those reports?

Scope:

- Reddit, Hacker News, OpenAI Community, GitHub discussions, and credible blog/forum writeups.
- Capability reports, failure reports, access/rollout reports, and usage-limit reports.
- Sampling window and search strategy.

Non-goals:

- Do not treat anecdotes as truth.
- Do not infer account-level policy from isolated complaints.

Required output:

- Anecdote clusters.
- Repeated complaints.
- Repeated positive reports.
- Credibility and sampling caveats.

## Lane 3: Usage Economics Researcher

Question: How should this project think about GPT-5.5 cost, token efficiency, usage limits, and quota burn compared with GPT-5.4?

Scope:

- Official API pricing and Codex usage-limit statements.
- Public claims about token efficiency.
- User anecdotes about quota burn.
- Distinction between API economics and ChatGPT-plan Codex limits.

Non-goals:

- Do not claim a precise Codex credit multiplier unless official documentation states it.
- Do not collapse token efficiency into cost efficiency.

Required output:

- Official knowns.
- Anecdotal unknowns.
- Metrics the local runner should capture.
- Interpretation risks.

## Lane 4: Local Feasibility Researcher

Question: What local Codex and repo surfaces can support requested-vs-effective model tracking and usage metrics?

Scope:

- `~/.codex/models_cache.json`
- `~/.codex/state_5.sqlite`
- Codex logs and login status surfaces, without exposing secrets.
- Repo-local `.planning/config.json`
- Repo-local `.codex/config.toml`
- Existing measurement provenance patterns in `harness_modifier/closure/`

Non-goals:

- Do not read or print secrets from auth files.
- Do not mutate config or logs.

Required output:

- Available local fields.
- Missing metrics and fallback markers.
- Safety rules for secret-bearing files.
- Recommended metadata schema for benchmark runs.

## Synthesis Requirement

After all lanes complete, synthesize findings into `RESEARCH-SYNTHESIS.md` with:

- `What Carries Strongly`
- `What Is Anecdotal Only`
- `What Local Experiments Must Resolve`
- `Changes To Predictions`
- `Changes To Runner Design`
- `Source Quality Notes`
