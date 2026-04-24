# Source Verification Summary: 2026-04-24

## Inputs

- Candidate seeds: `.planning/measurement/model-role-benchmark/seeds/third-pass-candidates.jsonl`
- Verification report: `.planning/measurement/model-role-benchmark/source-quality/20260424T010734Z/verification.jsonl`
- Accepted split: `.planning/measurement/model-role-benchmark/source-quality/20260424T010734Z/accepted-sources.jsonl`
- Held split: `.planning/measurement/model-role-benchmark/source-quality/20260424T010734Z/held-sources.jsonl`
- Rejected split: `.planning/measurement/model-role-benchmark/source-quality/20260424T010734Z/rejected-sources.jsonl`

## Counts

- Total candidates: `44`
- `accept`: `36`
- `hold`: `7`
- `reject`: `1`

## Source Kinds

- `article`: `2`
- `discussion_thread`: `16`
- `issue`: `17`
- `official`: `9`

## Held Or Rejected Sources

- `hold` `openai-official-gpt55-release-current`: `official_fetch_blocked_403` — openai-official-gpt55-release-current
- `hold` `openai-official-gpt55-system-card-current`: `official_fetch_blocked_403` — openai-official-gpt55-system-card-current
- `hold` `openai-official-gpt54-release-current`: `official_fetch_blocked_403` — openai-official-gpt54-release-current
- `hold` `openai-help-chatgpt-gpt53-gpt54-current`: `official_fetch_blocked_403` — openai-help-chatgpt-gpt53-gpt54-current
- `hold` `openai-help-codex-with-chatgpt-current`: `official_fetch_blocked_403` — openai-help-codex-with-chatgpt-current
- `hold` `openai-help-codex-rate-card-current`: `official_fetch_blocked_403` — openai-help-codex-rate-card-current
- `hold` `artificial-analysis-gpt55-model-current`: `reachable_secondary_or_uncertain_source` — GPT-5.5 (xhigh) - Intelligence, Performance &amp; Price Analysis
- `reject` `artificial-analysis-methodology-current`: `topic_not_confirmed` — Intelligence Benchmarking | Artificial Analysis

## Decision

- Add accepted third-pass sources to the evidence corpus.
- Keep held official/secondary/aggregator sources out of synthesis until content-level verification is available.
- Rejected sources should not be used unless a corrected URL is found.
