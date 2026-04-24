# Round 2 Shard: Official, Benchmark, and Methodology Evidence Quality

## Scope

Input: `.planning/measurement/model-role-benchmark/evidence-packets/20260424T011119Z/packets.jsonl`.

Focused on evidence quality for official docs, benchmark evidence, and methodology support.

## Method

- Re-bucketed sources manually because `source_type` is `anecdote` for all rows, including official docs.
- Treated official developer docs as authoritative for documented pricing/model specs only.
- Treated benchmark evidence as direct only if the packet contained benchmark artifact/methodology; none do.
- Treated GitHub issues, forums, Reddit, and HN as symptom/failure-mode evidence, not model-ranking evidence.

## Source Quality Table

| Category | Count | Evidence value | Main limitations | Representative source IDs |
| --- | ---: | --- | --- | --- |
| Official docs | 3 | High for documented plans, model availability, documented context specs. | No eval/system-card/methodology docs captured; no direct GPT-5.5 benchmark artifact; JS extraction risk. | `openai-developers-codex-pricing-current`, `openai-developers-gpt54-model-current`, `openai-developers-gpt5-codex-model-current` |
| Third-party benchmarks | 0 direct / 3 indirect mentions | Low for current packet. | Only discussion-layer references. | `reddit-codex-2026-03-gpt54-early-results`, `reddit-codex-2026-04-23-long-context-better`, `hackernews-2026-gpt54-sre-benchmark` |
| GitHub issues | 24 | Moderate for recurring failure modes and effective-behavior drift. | Complaint-biased, user-env confounds, unresolved-status ambiguity, not comparative evals. | `github-openai-codex-issue-13738`, `github-openai-codex-issue-16984`, `github-openai-codex-issue-14341`, `github-openai-codex-issue-19185`, `github-openai-codex-issue-19215`, `github-openai-codex-issue-19241` |
| Forums | 13 | Low-moderate for workload symptoms and operator reports. | User/support reports; first-party hosted but not first-party commitments. | `openai-community-2026-codex-usage-consumption-change`, `openai-community-2026-codex-usage-limits-cursor`, `openai-community-2026-codex-autonomous-openstack-frontend` |
| Reddit | 19 | Low. | Launch/reaction bias, unverifiable anecdotes, indirect benchmark paraphrase. | `reddit-codex-2026-03-gpt54-early-results`, `reddit-codex-2026-04-23-long-context-better`, `reddit-openai-2026-04-23-gpt55-official-discussion` |
| Hacker News | 16 | Low. | Often link shells or discussion stubs; benchmark rows are indirect. | `hackernews-2026-gpt54-launch-index`, `hackernews-2026-gpt54-codex-model-thread`, `hackernews-2026-gpt54-sre-benchmark` |
| Secondary articles | 0 | None. | Absent from packet. | None |

## Methodology Risks

- The packet schema marks all rows as `source_type=anecdote`, so reliability scoring needs manual override.
- No direct benchmark artifacts are present: no eval cards, papers, dashboards, raw run logs, or task specs.
- Benchmark-like evidence is mostly secondhand or discussion-of-discussion.
- Official docs describe API/model surfaces, while GitHub issues show effective Codex client behavior can diverge.
- Launch-window timing contaminates GPT-5.5 access, quota, fast-mode, and error reports.
- Many workload claims are self-normalized and not reproducible.

## What Should Be Held Out

- Any model leaderboard/ranking conclusion from this packet alone.
- Claims that GPT-5.5 long-context superiority is established.
- Claims that higher token price is or is not offset by token efficiency.
- Claims that documented context windows equal effective Codex runtime context.
- Any weighted benchmark score from Reddit, HN, OpenAI Community, or GitHub issues.

## What Local Benchmarks Must Resolve

- Effective context window by runtime surface and model.
- Actual model routing correctness under config/thread/subagent delegation.
- Fixed-workload usage burn and quota accounting by model and speed mode.
- Price-to-completed-work.
- Role-execution fidelity.
- Latency under comparable tasks.
- Long-context retrieval and large-codebase task performance.
- Sample size, confidence intervals, and effort-level normalization.
