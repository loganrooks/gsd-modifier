# Round 2 Shard: Access, Rollout, Errors, Model Selection

## Scope

Input: `.planning/measurement/model-role-benchmark/evidence-packets/20260424T011119Z/packets.jsonl`.

Included only claims about access, rollout, error, model selection, and runtime visibility.

## Method

- Read all 75 packets.
- Weighted first-party GitHub issues above Reddit/HN/OpenAI Community reaction threads.
- Treated repeated cross-surface reports as stronger than one-off launch-day sightings.

## Claim Table

| Claim | Synthesis | Stability | Source IDs |
| --- | --- | --- | --- |
| GPT-5.5 access was uneven across surfaces/accounts during launch. | Best read as rollout turbulence, not stable entitlement policy. | Low-medium | `reddit-codex-2026-04-23-error-latest-codex`, `github-openai-codex-issue-19227`, `github-openai-codex-issue-19213`, `reddit-openai-2026-04-23-cli-not-updated`, `github-openai-codex-issue-14181` |
| UI visibility did not guarantee actual availability. | Menu/selector/leak visibility did not mean the model could be launched. | Low | `reddit-openai-2026-04-22-leak-thread`, `reddit-codex-2026-04-22-now-on-codex`, `github-openai-codex-issue-19213`, `github-openai-codex-issue-19227` |
| Internal model names surfaced during launch. | Useful as rollout-churn evidence, not public taxonomy. | Low | `reddit-openai-2026-04-22-leak-thread`, `reddit-codex-2026-04-22-now-on-codex`, `hackernews-2026-codex-cli-error-string` |
| Requested model can differ from effective runtime model. | Strongest stable pattern in this shard; predates GPT-5.5 and affects subagents/new threads/Desktop override behavior. | Medium | `github-openai-codex-issue-15177`, `github-openai-codex-issue-16548`, `github-openai-codex-issue-17933`, `github-openai-codex-issue-16984` |
| Access/quota signals can disagree across surfaces. | Client-side limit-hit behavior may disagree with dashboard/status signals. | Medium | `github-openai-codex-issue-16909`, `github-openai-codex-issue-12299`, `github-openai-codex-issue-19215` |
| Rollout/error turbulence was not unique to GPT-5.5. | Baseline/public model routes also had transient model-not-found/routing behavior. | Low-medium | `github-openai-codex-issue-18793`, `hackernews-2026-codex-cli-error-string`, `reddit-codex-2026-04-22-stealth-launch` |

## Contradictions

- CLI update advice conflicts with metadata-not-found and unsupported-model reports.
- GPT-5.5 can be selectable in one Desktop context and inert/unavailable in another.
- Requested-model state cannot be assumed to equal effective runtime state.
- Usage dashboards and task admission can disagree.

## Evidence Strength

- Strongest: repeated first-party GitHub issues about model-selection/runtime-visibility mismatch.
- Medium: first-party launch-day GPT-5.5 access failures.
- Weak: Reddit/HN leak, tooltip, stealth-launch, and internal-name sightings.

## What Local Benchmarks Must Resolve

- Effective model identity from runtime artifacts, not selector state.
- Access by surface: CLI, Desktop, project chat, non-project chat.
- Account tier and client version for every run.
- Separate routing/access failures from model-quality benchmark results.
- Requested-vs-effective model in subagents and new threads.
- Quota/status surfaces against real task admission.
