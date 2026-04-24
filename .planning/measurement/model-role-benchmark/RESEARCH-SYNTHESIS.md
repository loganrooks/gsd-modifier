# Research Synthesis

Date: 2026-04-24

Evidence packet: `.planning/measurement/model-role-benchmark/evidence-packets/20260424T011119Z/packets.jsonl`

Shard artifacts:

- `.planning/measurement/model-role-benchmark/synthesis-rounds/20260424T011300Z/round-2-usage-pricing-quota.md`
- `.planning/measurement/model-role-benchmark/synthesis-rounds/20260424T011300Z/round-2-access-rollout-runtime.md`
- `.planning/measurement/model-role-benchmark/synthesis-rounds/20260424T011300Z/round-2-capability-role-anecdotes.md`
- `.planning/measurement/model-role-benchmark/synthesis-rounds/20260424T011300Z/round-2-methodology-quality.md`

## What Carries Strongly

- Official docs carry for documented plan/model specs only, not runtime ranking: `openai-developers-codex-pricing-current`, `openai-developers-gpt54-model-current`, `openai-developers-gpt5-codex-model-current`.
- Requested model/settings can diverge from effective runtime state; runner design must preserve requested-vs-effective discipline: `github-openai-codex-issue-15177`, `github-openai-codex-issue-16548`, `github-openai-codex-issue-17933`, `github-openai-codex-issue-16984`.
- Quota/status and task admission can disagree; quota evidence must be measured locally, not inferred from dashboards: `github-openai-codex-issue-16909`, `github-openai-codex-issue-12299`, `github-openai-codex-issue-19215`.
- Documented context windows do not prove effective Codex runtime context: `openai-developers-gpt54-model-current`, `openai-developers-gpt5-codex-model-current`, `github-openai-codex-issue-13738`, `github-openai-codex-issue-19185`, `github-openai-codex-issue-16140`.

## What Is Anecdotal Only

- GPT-5.5 token efficiency, higher effective cost, and quota burn are plausible but unresolved: `reddit-codex-2026-04-23-hour-use`, `reddit-codex-2026-04-23-pricing-2x`, `github-openai-codex-issue-19215`.
- Frontend gains are the clearest positive capability anecdotes, but not local benchmark evidence: `reddit-codex-2026-04-23-frontend-better`, `openai-community-2026-codex-autonomous-openstack-frontend`.
- Planning, review, and long-horizon role claims remain weak-to-moderate and are contradicted by stale guidance, false completion, and workflow gaps: `openai-community-2026-codex-deprecated-api-suggestions`, `github-openai-codex-issue-14341`, `github-openai-codex-issue-14795`.
- Launch leaks, internal names, selector visibility, and stealth-rollout reports should not be treated as stable taxonomy or entitlement policy: `reddit-openai-2026-04-22-leak-thread`, `github-openai-codex-issue-19213`, `github-openai-codex-issue-19227`.

## What Local Experiments Must Resolve

- Effective model identity, reasoning effort, and runtime evidence source per run.
- Access by surface and account/client version before scoring quality.
- Fixed-workload token use, quota delta, wall-clock, retries, and price-to-completed-work.
- Effective context by model and runtime surface.
- Role-family outcomes: executor correctness/restraint, planner decomposition, reviewer true positives, frontend first pass and repair.
- Fast mode as a separate measured lane, not an assumed speed/value improvement.
- Repeated runs, sample size, and scorer discipline to avoid prose-confidence bias.

## Changes To Predictions

- Keep `P-EXEC-001` no-default-change posture; external evidence does not justify executor promotion.
- Keep `P-PLAN-001` and `P-REVIEW-001` as hypotheses, but label external support as anecdotal rather than benchmark-backed.
- Strengthen `P-USAGE-001`: require quota delta, fast-mode setting, effective context, retries, and price-to-completed-work, not token totals alone.
- Add a gating rule: any run without proven effective model/settings is qualitative only.
- Add launch/access instability as a validity threat.

## Changes To Runner Design

- Add access preflight records for surface, account tier, client version, model selector state, launch result, and failure class.
- Add quota/status probes before and after each run; preserve disagreements as artifacts.
- Add effective-context probes separate from documented context specs.
- Add fast-mode as an explicit candidate dimension or exclusion field.
- Add statuses for `access_failed`, `routing_unproven`, `quota_blocked`, and `completed`.
- Preserve failed runs and raw artifacts.

## Source Quality Notes

- No direct benchmark artifacts, eval cards, papers, dashboards, raw run logs, or task specs were captured in the evidence packet.
- Official docs are high quality for documented specs, but not for effective Codex client behavior.
- GitHub issues are useful for recurring failure modes, not comparative model quality.
- Reddit, HN, and forum sources are launch-biased and should not produce weighted model scores.
- The packet’s `source_type=anecdote` uniformity requires manual reliability override.

## Profile Implications Without Default Changes

- Keep `54-high` as the conservative executor baseline.
- Keep `54-xhigh` as the reasoning-depth comparison and possible fallback when `55-high` is unavailable or quota-limited.
- Treat `55-high` as a candidate for planner/reviewer/researcher and frontend-repair experiments, not as a production default.
- Do not recommend production default changes until local repeated runs clear the existing thresholds in `PREDICTIONS.md`.
