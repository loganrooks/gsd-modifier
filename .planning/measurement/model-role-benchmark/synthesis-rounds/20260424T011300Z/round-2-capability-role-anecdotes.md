# Round 2 Shard: Capability and Role-Family Anecdotes

## Scope

Input: `.planning/measurement/model-role-benchmark/evidence-packets/20260424T011119Z/packets.jsonl`.

Included planning, execution, review, frontend, long-context, long-horizon, and agent-workflow anecdotes.

## Method

- Filtered to community posts, GitHub issues, and discussion threads describing observed behavior.
- Treated launch summaries as weaker than firsthand bug reports or longer experience reports.
- Cited source IDs only.

## Claim Table

| Role family | Synthesis | Source IDs |
| --- | --- | --- |
| Planning | Anecdotes lean positive on intent understanding and multi-step decomposition, but there is a failure mode around stale APIs/shallow plans. | `reddit-codex-2026-04-23-here-lets-go`, `reddit-codex-2026-04-23-frontend-better`, `reddit-codex-2026-03-gpt54-experience`, `openai-community-2026-codex-autonomous-openstack-frontend`, `openai-community-2026-codex-deprecated-api-suggestions` |
| Execution | Anecdotes say execution is stronger on coding, UI repair, and large-codebase iteration; reliability is contested by false completion, slow first-turn startup, and completion-without-action failures. | `reddit-codex-2026-04-23-here-lets-go`, `reddit-codex-2026-04-23-frontend-better`, `openai-community-2026-codex-autonomous-openstack-frontend`, `github-openai-codex-issue-14341`, `github-openai-codex-issue-14795` |
| Review | Mixed signal: stronger self-checking/benchmark hints but workflow gaps and stale/deprecated guidance. | `reddit-codex-2026-04-23-here-lets-go`, `openai-community-2026-codex-deprecated-api-suggestions`, `openai-community-2026-codex-github-pr-review`, `github-openai-codex-issue-14341`, `hackernews-2026-gpt54-sre-benchmark` |
| Frontend | Clearest positive anecdotal lane: better UI adherence, weak-UI repair, image-to-UI replication, and existing-codebase behavior. First-pass frontend may still trail top Anthropic models. | `reddit-codex-2026-04-23-hour-use`, `reddit-codex-2026-04-23-frontend-better`, `reddit-codex-2026-03-gpt54-experience`, `openai-community-2026-codex-autonomous-openstack-frontend` |
| Long-context | Capability anecdotes say retrieval improved, but runtime anecdotes show effective limits/config/UI mismatches. | `reddit-codex-2026-04-23-long-context-better`, `reddit-codex-2026-04-23-context-disabled`, `github-openai-codex-issue-13738`, `github-openai-codex-issue-19185`, `github-openai-codex-issue-16140` |
| Long-horizon | More autonomous long tasks are plausible, especially with compaction/multi-window workflows, but direct evidence is thin and partly from adjacent variants. | `reddit-codex-2026-04-23-here-lets-go`, `openai-community-2026-gpt51-codex-max`, `openai-community-2026-codex-quality-degrading` |
| Agent workflow | Strong demand and dense failure-mode cluster: mode confusion, approval friction, PR/review gaps, subagent model mismatch, override drift, slash-skill regressions. | `reddit-codex-2026-04-23-here-lets-go`, `openai-community-2026-codex-edits-files-chat-mode`, `openai-community-2026-codex-github-pr-review`, `openai-community-2026-codex-pr-create-fail`, `github-openai-codex-issue-15177`, `github-openai-codex-issue-16548`, `github-openai-codex-issue-16984`, `github-openai-codex-issue-19249`, `hackernews-2026-codex-agent-loop` |

## Contradictions

- Planning/execution optimism conflicts with false-completion and deprecated-guidance reports.
- Frontend improvement is repeated, but first-pass frontier quality remains disputed.
- Long-context capability conflicts with effective runtime limits.
- Agentic autonomy conflicts with brittle workflow/runtime integration.

## Evidence Strength

- Strongest anecdotal lane: agent workflow, but failure-report biased.
- Moderate: frontend, execution, long-context.
- Weak-to-moderate: planning, review.
- Weakest: long-horizon.

## What Local Benchmarks Must Resolve

- Planning decomposition and ambiguity handling on same repo tasks.
- End-to-end execution completion without false done states.
- Review defect detection and deprecated-guidance avoidance.
- UI first-pass quality and iterative repair.
- Effective context in actual harness.
- Long-running session discipline.
- Subagent model preservation and chat/edit boundary behavior.
