# Model Role Benchmark Sources

## Source Taxonomy

| Type | Meaning | How To Use |
| --- | --- | --- |
| `official` | OpenAI docs, release notes, pricing, status pages | Strong for stated availability, pricing, model features, and official claims |
| `benchmark` | Published benchmark results with methodology | Useful only with task-fit caveats |
| `independent-analysis` | Blogs, repos, or evaluations with reproducible methods | Qualify by method quality |
| `anecdote` | Individual forum, Reddit, HN, or social reports | Weak evidence; useful for generating hypotheses |
| `local-observation` | Measurements from this repo and local Codex runs | Strongest for project-specific default decisions |
| `inference` | Reasoned conclusion from mixed evidence | Must stay marked as inference |

## Seed Sources

| Source | Type | Current use |
| --- | --- | --- |
| https://openai.com/index/introducing-gpt-5-5/ | `official` | GPT-5.5 launch claims, benchmark framing, Codex positioning |
| https://openai.com/index/introducing-gpt-5-4/ | `official` | GPT-5.4 baseline claims and context-window/pricing comparison context |
| https://help.openai.com/en/articles/11369540-using-codex-with-chatgpt | `official` | ChatGPT-plan Codex access distinction |
| https://help.openai.com/en/articles/11369540-codex-in-chatgpt | `official` | Codex in ChatGPT availability and usage framing when accessible |
| https://docs.x.com/x-api/posts/search/introduction | `official` | X recent-search and full-archive search access boundaries |
| https://docs.x.com/x-api/posts/search/quickstart/recent-search | `official` | X recent-search prerequisites and bearer-token workflow |
| https://docs.x.com/x-api/posts/search/integrate/paginate | `official` | X search pagination and reverse-chronological result behavior |
| https://developers.reddit.com/docs/capabilities/server/reddit-api | `official` | Reddit API capability and private-data boundary |
| https://docs.bsky.app/ | `official` | Bluesky API and AT Protocol documentation entrypoint |

## Local Sources To Inspect During Research

| Path | Reason |
| --- | --- |
| `.planning/config.json` | Current GSD model overrides and workflow toggles |
| `.codex/config.toml` | Repo-local Codex model and agent registry |
| `tooling/portable-gsd/overlay/config.toml` | Source carrier that materializes repo-local Codex config |
| `harness_modifier/closure/observation_record.json` | Existing measurement provenance vocabulary |
| `harness_modifier/closure/observation_writer.py` | Existing validation pattern for measurement records |
| `docs/handoff/current.md` | Current project boundary and next work |

## Method Quality Checklist

For each external source, record:

- Access date.
- Author or organization.
- Whether the source is official, anecdotal, or independently reproducible.
- Sample size or number of observed reports.
- Whether raw data or prompts are available.
- Whether the source separates capability, cost, and availability.
- Whether the source gives enough detail to reproduce the claim.

## Platform Access Notes

| Platform | Collection posture | Caveat |
| --- | --- | --- |
| X | Prefer official recent-search API when bearer-token access exists; otherwise use web-search source discovery only. | Recent search is limited to the last 7 days; full archive has higher access requirements. |
| Reddit | Prefer official API or public pages surfaced by search; avoid undocumented bulk scraping as a first slice. | Access and throttling reports are inconsistent, so record the collection path for every item. |
| Hacker News | Use public item/thread pages surfaced by search and record thread IDs. | Sampling may overrepresent developer-heavy opinion. |
| OpenAI Community | Use public threads surfaced by search and record thread URLs. | Moderation and access may hide deleted or private context. |
| Bluesky | Prefer official AT Protocol/AppView search if needed. | Coverage differs from X/Reddit and should not be merged without platform tags. |

## Current Evidence Boundary

Official sources can justify testing GPT-5.5 seriously. They do not by themselves justify changing production defaults for `gsd-modifier`.

User reports can identify likely failure modes and usage concerns. They do not by themselves establish model quality, token efficiency, or quota economics.

Local benchmark results should carry the most weight for executor, planner, reviewer, and non-GSD agent profile decisions.
