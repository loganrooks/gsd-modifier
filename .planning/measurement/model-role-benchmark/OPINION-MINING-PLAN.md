# Opinion Mining Plan

## Purpose

Mine public anecdote and opinion about GPT-5.5 vs GPT-5.4 in Codex without letting noisy launch chatter decide production defaults.

The collection flow is intentionally split:

- seed files record curated public URLs and queries
- extraction scripts fetch pages and normalize text outside the model context
- cheap collection agents gather compact, traceable evidence inventories
- stronger synthesis agents analyze only the curated evidence
- local benchmark results remain the strongest basis for project defaults

## Research Questions

| ID | Question | Why it matters |
| --- | --- | --- |
| `RQ-CAPABILITY` | What do users say GPT-5.5 does better or worse than GPT-5.4 in Codex? | Shapes expected task-family wins |
| `RQ-USAGE` | What do users report about usage limits, quota burn, token efficiency, and fast mode? | Shapes default-vs-reserved profile decisions |
| `RQ-ACCESS` | What failures or rollout issues are users reporting? | Prevents confusing rollout turbulence with model quality |
| `RQ-ROLE` | What role-specific anecdotes exist for planning, execution, review, UI, and long-running agents? | Maps anecdotes to our benchmark roles |
| `RQ-METHOD` | Which public claims provide prompts, artifacts, or reproducible comparisons? | Separates useful evidence from impressions |

## Platform Priority

| Priority | Platform | Collection method | Output target |
| --- | --- | --- | --- |
| 1 | Reddit | Search targeted subreddits and thread URLs; use official/public APIs only when available | Thread inventory and representative comments |
| 2 | X | Use official recent-search API if bearer-token access exists; otherwise search-indexed public posts only | Post inventory with engagement and timestamp |
| 3 | Hacker News | Search for GPT-5.5/Codex discussions and direct threads | Thread inventory and high-signal comments |
| 4 | OpenAI Community | Search public support/usage/access threads | Thread inventory and issue clusters |
| 5 | Bluesky | Use official AT Protocol/AppView search if needed | Supplemental post inventory |
| 6 | GitHub/blogs | Search issues, discussions, posts, and independent writeups | Reproducible claims and methodology notes |

## Query Bank

Use narrow queries first. Expand only when they return too little.

| Theme | Queries |
| --- | --- |
| Capability | `"GPT-5.5" Codex better than 5.4`, `"gpt-5.5" "codex" "frontend"`, `"gpt-5.5" "executor" "codex"` |
| Usage | `"GPT-5.5" "usage limits" Codex`, `"gpt-5.5" "burns" "usage"`, `"gpt-5.5" "quota" "codex"` |
| Access | `"gpt-5.5" "not found" Codex`, `"gpt-5.5" "do not have access" Codex`, `"gpt-5.5" rollout Codex` |
| Role | `"gpt-5.5" "code review" Codex`, `"gpt-5.5" "planning" Codex`, `"gpt-5.5" "long running" Codex` |
| Method | `"gpt-5.5" benchmark "gpt-5.4"`, `"gpt-5.5" "SWE-bench"`, `"gpt-5.5" "Terminal-Bench"` |

Platform-specific examples:

- Reddit: `site:reddit.com/r/codex "GPT-5.5" "usage"`
- Hacker News: `site:news.ycombinator.com "GPT-5.5" "Codex"`
- OpenAI Community: `site:community.openai.com "GPT-5.5" "Codex"`
- GitHub: `site:github.com "GPT-5.5" "Codex"`

## Cheap Collection Agent Protocol

Use `gpt-5.4` with `reasoning_effort=medium` for collection passes.

Collection agents must return only:

- source URL
- platform
- author handle only if already public in the source
- date posted or crawled
- query used
- relevance tags
- short summary
- short excerpt if needed for disambiguation
- engagement signal if visible
- collection caveat

They must not:

- decide whether GPT-5.5 is better
- merge claims across sources
- quote long passages
- scrape private or login-gated content
- store secrets, cookies, bearer tokens, or user identifiers beyond public handles

## Extraction Script Protocol

Use scripts under `tooling/codex/model_opinion_mining/` before model-based synthesis:

```bash
python3 tooling/codex/model_opinion_mining/fetch_pages.py \
  --seeds .planning/measurement/model-role-benchmark/seeds/focused-first-pass.jsonl \
  --raw-dir .planning/measurement/model-role-benchmark/raw-pages/<timestamp> \
  --metadata .planning/measurement/model-role-benchmark/source-inventories/<timestamp>/metadata.json

python3 tooling/codex/model_opinion_mining/extract_text.py \
  --raw-dir .planning/measurement/model-role-benchmark/raw-pages/<timestamp> \
  --text-dir .planning/measurement/model-role-benchmark/extracted-text/<timestamp> \
  --metadata .planning/measurement/model-role-benchmark/source-inventories/<timestamp>/metadata.json

python3 tooling/codex/model_opinion_mining/build_inventory.py \
  --seeds .planning/measurement/model-role-benchmark/seeds/focused-first-pass.jsonl \
  --text-dir .planning/measurement/model-role-benchmark/extracted-text/<timestamp> \
  --metadata .planning/measurement/model-role-benchmark/source-inventories/<timestamp>/metadata.json \
  --output .planning/measurement/model-role-benchmark/source-inventories/<timestamp>/inventory.jsonl
```

Raw pages and full extracted text are ignored by git. Compact inventories and metadata are commit-visible.

## Source Inventory Schema

Each collector returns JSON Lines or a Markdown table with these fields:

```json
{
  "source_id": "reddit-codex-2026-04-23-001",
  "platform": "reddit",
  "url": "https://www.reddit.com/...",
  "query": "site:reddit.com/r/codex \"GPT-5.5\" \"usage\"",
  "collected_at": "2026-04-23T00:00:00Z",
  "posted_at": "2026-04-23",
  "author_public_id": "public-handle-or-not_collected",
  "engagement": {"score": "visible-or-not_available", "comments": "visible-or-not_available"},
  "claim_tags": ["usage", "capability", "access", "role-execution"],
  "summary": "One or two sentence neutral summary.",
  "excerpt": "Short excerpt only when necessary.",
  "source_type": "anecdote",
  "collection_caveat": "Search-indexed sample; not representative."
}
```

## Sampling Rules

First pass targets:

- 10-20 Reddit threads or comments
- 10-20 X posts if official recent search is available; otherwise 5-10 search-indexed X references
- 5-10 Hacker News comments or threads
- 5-10 OpenAI Community threads
- 3-5 GitHub/blog/independent-analysis references

Stop early when:

- sources repeat the same claim pattern
- no new role-specific claims appear after two query expansions
- access constraints force unreliable scraping
- the source pool becomes mostly reposts, jokes, or unsourced claims

## Synthesis Protocol

Use `gpt-5.5` with `reasoning_effort=high` for synthesis after collection.

Synthesis output must include:

- `Clustered Anecdotes`
- `Repeated Positive Claims`
- `Repeated Negative Claims`
- `Usage-Limit Concerns`
- `Role-Specific Claims`
- `Contradictions`
- `What Is Only Anecdotal`
- `What Should Change In The Local Benchmark`
- `What Should Not Change Yet`

Synthesis must not:

- treat high engagement as truth
- present platform-specific opinion as broad user consensus
- collapse pricing, usage limits, token efficiency, and quota burn into one concept
- change production defaults without local benchmark support

## Token Efficiency Strategy

- Collection agents fetch source inventories only; no long-form analysis.
- Require one compact row per source.
- Cap excerpts to one short sentence unless the exact wording matters.
- Deduplicate by URL before synthesis.
- Analyze only sources tagged relevant to `RQ-CAPABILITY`, `RQ-USAGE`, `RQ-ROLE`, or `RQ-METHOD`.
- Preserve raw inventories separately from synthesized conclusions.

## Audit Trail

Every run should preserve:

- query strings
- collection timestamp
- platform and access method
- source URL
- claim tags
- collection caveats
- model and reasoning level used for collection
- model and reasoning level used for synthesis

Store future outputs under:

- `.planning/measurement/model-role-benchmark/seeds/`
- `.planning/measurement/model-role-benchmark/source-inventories/<timestamp>/`
- `.planning/measurement/model-role-benchmark/raw-pages/<timestamp>/` (ignored)
- `.planning/measurement/model-role-benchmark/extracted-text/<timestamp>/` (ignored)
- `.planning/measurement/model-role-benchmark/RESEARCH-SYNTHESIS.md`

Do not overwrite old inventories or synthesis files without marking the older version as superseded.
