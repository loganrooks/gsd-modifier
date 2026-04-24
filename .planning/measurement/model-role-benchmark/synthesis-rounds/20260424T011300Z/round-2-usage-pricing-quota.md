# Round 2 Shard: Usage, Pricing, Quota, Fast Mode, Context

## Scope

Input: `.planning/measurement/model-role-benchmark/evidence-packets/20260424T011119Z/packets.jsonl`.

Included only claims about usage limits, API pricing, token efficiency, quota burn, fast mode, and context window.

## Method

- Filtered records tagged with `usage`, `pricing`, `quota`, `fast-mode`, or `context-window`.
- Kept usage limits, API pricing, token efficiency, and quota burn separate.
- Weighted official docs first, first-party GitHub issues second, OpenAI Community third, Reddit/HN last.

## Claim Table

| Lane | Claim | Evidence status | Source IDs |
| --- | --- | --- | --- |
| Usage limits | Codex plans have explicit usage limits; Plus includes GPT-5.5/GPT-5.4 and higher-usage GPT-5.4-mini. | Official pricing page supports the broad claim; exact message ranges in this packet are Reddit-derived. | `openai-developers-codex-pricing-current`, `reddit-codex-2026-04-23-usage-it-is-over` |
| Usage limits | Codex may enforce multiple quota windows. | Anecdotal; official packet snippets do not settle 5h/daily/weekly structure. | `openai-community-2026-codex-usage-limits-cursor`, `reddit-codex-2026-04-23-usage-it-is-over`, `reddit-codex-2026-04-23-fast-mode-usage` |
| API pricing | GPT-5.4 has token-priced API billing and a 1,050,000-token context window. | Strong for GPT-5.4 API doc. | `openai-developers-gpt54-model-current` |
| API pricing | GPT-5-Codex has token-priced API billing and a 400,000-token context window. | Strong for GPT-5-Codex, not GPT-5.5. | `openai-developers-gpt5-codex-model-current` |
| API pricing | GPT-5.5 is more expensive than GPT-5.4. | User report only in this packet; no first-party numeric GPT-5.5 API price snippet captured. | `reddit-codex-2026-04-23-hour-use`, `reddit-codex-2026-04-23-pricing-2x` |
| Token efficiency | GPT-5.5 may use fewer tokens than GPT-5.4. | Repeated launch anecdotes, not locally measured. | `reddit-codex-2026-04-23-hour-use`, `reddit-codex-2026-04-23-here-lets-go`, `reddit-openai-2026-04-23-release-thread`, `reddit-codex-2026-04-23-pricing-2x` |
| Quota burn | Users report GPT-5.5 burns allowance faster than expected. | Multiple user/issue reports; still anecdotal. | `reddit-codex-2026-04-23-usage-it-is-over`, `github-openai-codex-issue-19215`, `openai-community-2026-codex-usage-consumption-change` |
| Quota burn | Quota/status surfaces can disagree with enforcement. | Repeated first-party issue evidence. | `github-openai-codex-issue-16909`, `github-openai-codex-issue-16847`, `github-openai-codex-issue-12299`, `github-openai-codex-issue-19215` |
| Fast mode | GPT-5.5 Fast mode is reported as consuming more plan usage. | Plausible, not officially pinned down in captured snippets. | `reddit-codex-2026-04-23-fast-mode-usage`, `github-openai-codex-issue-19241` |
| Fast mode | GPT-5.5 Fast mode may not reliably produce faster perceived speed. | One direct GitHub issue. | `github-openai-codex-issue-19241` |
| Context | Model-doc context maxima differ from effective Codex client exposure. | Strong contradiction between docs/config/UI reports. | `openai-developers-gpt54-model-current`, `openai-developers-gpt5-codex-model-current`, `github-openai-codex-issue-13738`, `github-openai-codex-issue-19185`, `github-openai-codex-issue-16140`, `reddit-codex-2026-04-23-context-disabled`, `reddit-codex-2026-04-23-vscode-context-display` |

## Contradictions

- Usage/status surfaces may show availability while task admission blocks execution.
- Higher price claims conflict with token-efficiency anecdotes; the packet lacks first-party GPT-5.5 pricing and local token telemetry.
- Fast mode may cost more without reliably feeling faster.
- Official context-window specs should not be treated as effective Codex runtime context.

## What Local Benchmarks Must Resolve

- Effective context-window matrix by model and runtime surface.
- Fast-mode value: wall-clock, queue delay, completion time, and quota delta.
- Quota/status consistency before and after prompts and compaction.
- Token-efficiency reality on fixed tasks.
- Cost per completed task, not list price alone.
- Actual usage-limit window shape for this account/workspace.
