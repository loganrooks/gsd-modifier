# Source Quality Scan: 2026-04-23

## Purpose

Token-efficient triage of the first extracted source batch plus candidate URLs returned by the first collection agents.

This is not a synthesis of claims. It is a source-quality gate before expanding the corpus to 60 sources.

## Probe Method

- Access date: 2026-04-23
- Method: deterministic `requests.get` URL probe from the repo environment
- Reddit probe behavior: direct thread URLs were converted to public `.json` endpoints
- Inputs:
  - existing inventory: `.planning/measurement/model-role-benchmark/source-inventories/20260423T225546Z/inventory.jsonl`
  - collection-agent candidate URLs returned in chat before this scan
- Probe result: `72` unique URLs checked

## Summary

| Bucket | Count | Disposition |
| --- | ---: | --- |
| Reddit direct/public JSON reachable | 23 | Mostly usable, but anecdotal and duplicate-heavy |
| OpenAI Community thread reachable | 7 | Usable as adjacent evidence; many are not GPT-5.5-vs-5.4 direct comparisons |
| Hacker News reachable in this probe | 3 | Usable but partial; `5` returned rate limits and need delayed retry or Algolia/HN API |
| Techmeme reachable | 6 | Use as discovery/launch context, not as primary user evidence |
| Official OpenAI/platform URLs | 9 | Probe returned `403`; verify via official docs access before using as evidence |
| GitHub issue URLs | 7 | Reachable, but titles were not extracted by simple probe; verify issue relevance before inclusion |
| Independent/blog URLs | 2 | One reachable, one `404`; use only after content-level verification |
| Failed first-pass article/forum URLs | 2 | Exclude from corpus unless alternate accessible URLs are found |
| Inferred X/Bluesky permalinks | 5 | Reject unless exact live posts are re-found from search or official API |

## Keep

- Existing Reddit Codex threads that fetched via `.json`, especially usage, pricing, context-window, and error threads.
- New Reddit candidates that fetched via `.json`:
  - `reddit-02` long-context comparison
  - `reddit-05` VS Code extension context-window report
  - `reddit-08` stealth-launch/access thread
  - `reddit-09` GPT-5.4 Codex baseline experience
  - `reddit-10` early GPT-5.4 results
  - `reddit-13` GPT-5.5 OpenAI release discussion
  - `reddit-14` CLI availability thread
- OpenAI Community thread pages with concrete titles:
  - `c2` usage limits in Cursor
  - `c3` sudden Codex usage consumption change
  - `c4` autonomous engineer/frontend example
  - `c5` GPT-5 Codex file-search limitation
  - `c6` deprecated API suggestion quality
- Hacker News pages that returned `200`:
  - `h1` GPT-5.4 discussion
  - `h3` GPT-5.4 launch/index thread
  - `h7` Codex CLI error string thread
- Techmeme pages with GPT-5.5-relevant titles:
  - `p48`, `p50`, `p53`

## Hold For Verification

- GitHub issue candidates. The URLs returned `200`, but the simple HTML probe did not extract titles. Use GitHub API or page parsing before admitting them.
- Official OpenAI and platform docs candidates. They returned `403` to the deterministic probe, so they cannot yet anchor official claims in the local artifact set.
- Hacker News candidates returning `429`. Retry later with throttling or use an HN/Algolia endpoint.
- OpenAI Community tag pages `c8` and `c9`. They are discovery hubs, not claim sources.

## Reject

- Inferred social URLs from the low-reasoning social collector:
  - `https://x.com/openai/status/1914940000000000000`
  - `https://x.com/openaidevs/status/1914940000000000001`
  - `https://x.com/agrimsingh/status/1914940000000000002`
  - `https://x.com/naderlikeladder/status/1914940000000000003`
  - `https://bsky.app/profile/webuiltthiscity.bsky.social/post/1914940000000000004`
- Techmeme pages whose titles are unrelated to GPT-5.5/Codex despite being returned by the collector:
  - `https://www.techmeme.com/260423/p52`
  - `https://www.techmeme.com/260423/p55`
  - `https://www.techmeme.com/260423/p59`
- Failed first-pass sources unless alternate URLs are found:
  - `https://www.gate.com/zh-tw/news/detail/gpt-55-appears-in-openai-codex-model-selector-ahead-of-official-20499731`
  - `https://linux.do/t/topic/2039946?tl=en`
- `https://www.techradar.com/pro/openai-gpt-5-4-is-here-and-openai-just-made-every-other-ai-model-look-slow` because the probe returned `404`.

## Collector Profile Correction

The first collection agents used `gpt-5.4-mini` with `reasoning_effort=low`, which was too weak for source validation. Evidence:

- inferred social permalinks were returned as if usable
- unrelated Techmeme pages were included
- hub pages were mixed with evidence pages
- indirect GPT-5 Codex sources were sometimes framed as GPT-5.5-vs-5.4 candidates

Future collection should use:

```json
{
  "model": "gpt-5.4",
  "reasoning_effort": "medium",
  "mode": "read-only collection"
}
```

Escalate to `gpt-5.4 high` only for source validation or deduplication when the candidate pool contains many social/search-indexed URLs.

## Decision

Do not proceed directly to a 60-source synthesis from the current candidate pool.

Next safe step:

1. build `second-pass-candidates.jsonl` only from `Keep` and selected `Hold For Verification`
2. add a deterministic verifier that records URL status, title, source-kind, directness, and rejection reason
3. require accepted sources to pass both URL reachability and source-kind validation before entering the 60-source seed file
