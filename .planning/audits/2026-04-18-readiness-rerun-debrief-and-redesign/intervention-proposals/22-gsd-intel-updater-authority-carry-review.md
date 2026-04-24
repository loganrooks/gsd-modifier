Date: 2026-04-20
Status: accepted bounded carry patch

# `gsd-intel-updater` Authority / Carry Review

## Purpose

- [g:r:i] This note resolves the third bounded live-only authority/carry review in the ordered tranche: whether `gsd-intel-updater` should stay a live-only exception or be carried into the tracked repo-local harness.

## Why This Surface Earned Review-Now Pressure

- [e:c+i] `gsd-intel-updater` is not just an internal helper. The repo-local intel layer routes through it, and that layer is explicitly meant to become a reusable knowledge surface other agents consult instead of re-reading the codebase. Sources: [.codex/get-shit-done/bin/lib/intel.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/intel.cjs:308), [.codex/get-shit-done/bin/lib/intel.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/intel.cjs:323), [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:34).
- [e:c+i] The post-fixer runtime report still showed `agents/gsd-intel-updater.toml` as an untracked live-only boundary surface before this tranche, even after reviewer and fixer were carried. Sources: [04-gsd-code-fixer-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/04-gsd-code-fixer-post-carry-runtime-visibility.json:19), [04-gsd-code-fixer-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/04-gsd-code-fixer-post-carry-runtime-visibility.json:386).
- [e:c+i] The live intel-updater contract was still carrying the wrong authority and topology model for this repo: CLAUDE-era skill discovery, prohibition on reading `AGENTS.md`, and a `.claude/.kilo` runtime layout instead of this repo’s `.codex` runtime with paired runtime-authoritative `.toml` plus human-facing `.md` agent surfaces. Sources: [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:13), [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:20), [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:62), [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:85).

## Accepted Carry

### 1. Carry the runtime-authoritative intel-updater `.toml` into tracked overlay

- [d:c+r:i] Accept tracked overlay carry for `gsd-intel-updater.toml`.
- [e:c+i] The carried runtime contract now reads repo-root `AGENTS.md` plus `.planning/AGENTS.md`, uses repo-local `.codex` skills/runtime surfaces, and treats `.codex` as the canonical harness root for this repo rather than inventing `.claude` or `.kilo` layouts. Sources: [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:13), [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:28), [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:62), [.codex/agents/gsd-intel-updater.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.toml:85).
- [d:r:i] Current consequence: `gsd-intel-updater.toml` no longer belongs in the unresolved live-only cohort. The intel writer now carries the same runtime topology truths that the intervention workspace itself is using.

### 2. Carry the paired human-facing intel-updater `.md` contract too

- [d:c+r:i] Accept paired overlay carry for `gsd-intel-updater.md` in the same tranche.
- [e:c+i] The adjacent human-facing contract now matches the same AGENTS-governed authority model and `.codex` runtime topology, so a reinstall no longer leaves the intel surface split between a carried `.toml` and an installer-lost `.md`. Sources: [tooling/portable-gsd/overlay/agents/gsd-intel-updater.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-intel-updater.md:21), [tooling/portable-gsd/overlay/agents/gsd-intel-updater.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-intel-updater.md:36), [tooling/portable-gsd/overlay/agents/gsd-intel-updater.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-intel-updater.md:70), [tooling/portable-gsd/overlay/agents/gsd-intel-updater.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-intel-updater.md:93).

## What This Rejects

- [d:r:i] Reject treating intel carry as merely a docs polish issue. This surface shapes downstream planning/intelligence reuse, so wrong topology assumptions here propagate farther than a local wording defect.
- [d:r:i] Reject broader `intel.cjs` or `.planning/intel/` schema rewriting in the same tranche. The current need was to align the writer’s authority/topology model before reopening file-format or freshness semantics.
- [d:r:i] Reject pulling `gsd-pattern-mapper` into the same patch by symmetry alone. Its remaining pressure is still more authority-gap/routing clarification than obvious carry widening.

## Initial Landing

- [e:c+i] The runtime-authoritative intel-updater contract is now carried in tracked overlay and currently materializes cleanly into live runtime. The post-carry runtime report records `agents/gsd-intel-updater.toml` as `intentional materialized carry` with `raw_equal` live/overlay hashes. Sources: [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:386), [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:399), [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:400).
- [e:c+i] The paired human-facing intel-updater contract now materializes with exact live/overlay parity as well. Sources: [tooling/portable-gsd/overlay/agents/gsd-intel-updater.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-intel-updater.md:21), [.codex/agents/gsd-intel-updater.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-intel-updater.md:21).
- [e:c+i] The unresolved live-only cohort dropped again: the post-carry runtime report now records `13` `untracked_live_only_outside_overlay_subset` entries rather than `14`. Sources: [04-gsd-code-fixer-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/04-gsd-code-fixer-post-carry-runtime-visibility.json:19), [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:19).

## Immediate Next Move

- [g:r:i] Advance to the fourth ordered surface: revisit `gsd-pattern-mapper.toml` as the remaining authority-gap case, and decide whether that surface really wants tracked carry or a narrower routing/authority clarification instead.
