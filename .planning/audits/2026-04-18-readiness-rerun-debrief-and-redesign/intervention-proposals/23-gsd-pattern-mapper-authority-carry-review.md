Date: 2026-04-20
Status: accepted bounded carry patch

# `gsd-pattern-mapper` Authority / Carry Review

## Purpose

- [g:r:i] This note resolves the fourth bounded live-only authority/carry review in the ordered tranche: whether `gsd-pattern-mapper` should stay a live-only authority-gap exception or be carried into the tracked repo-local harness.

## Why This Surface Earned Review-Now Pressure

- [e:c+i] `gsd-pattern-mapper` is planner-adjacent, not peripheral. The repo-local runtime still preserves `patterns_path` in phase initialization, and the model-profile registry still assigns an explicit model profile to this agent. Sources: [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:289), [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:318), [.codex/get-shit-done/bin/lib/model-profiles.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/model-profiles.cjs:22).
- [e:c+i] The targeted reread and ordered authority review already narrowed this surface to a real authority-gap case rather than a cleanup candidate. Sources: [13-live-only-agent-targeted-reread-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/13-live-only-agent-targeted-reread-disposition.md:14), [19-high-leverage-live-only-authority-review.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/19-high-leverage-live-only-authority-review.md:36).
- [e:c+i] Before this tranche, the post-intel runtime report still recorded `agents/gsd-pattern-mapper.toml` as an untracked live-only boundary surface outside the overlay subset. Sources: [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:19), [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:424), [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:437), [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:438).

## Accepted Carry

### 1. Carry the runtime-authoritative mapper `.toml` into tracked overlay

- [d:c+r:i] Accept tracked overlay carry for `gsd-pattern-mapper.toml`.
- [e:c+i] The carried runtime contract now reads repo-root `AGENTS.md` plus `.planning/AGENTS.md`, uses repo-local `.codex/skills/` and related `.codex` runtime surfaces rather than CLAUDE-era discovery, and explicitly tells the mapper not to flatten role/data-flow/authority distinctions into vague analogs. Sources: [.codex/agents/gsd-pattern-mapper.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.toml:26), [.codex/agents/gsd-pattern-mapper.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.toml:28), [.codex/agents/gsd-pattern-mapper.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.toml:38), [.codex/agents/gsd-pattern-mapper.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.toml:47).
- [d:r:i] Current consequence: `gsd-pattern-mapper.toml` no longer belongs in the unresolved live-only cohort. The planner-adjacent mapper now carries the same repo-local authority/runtime model as the reviewer, fixer, and intel-updater surfaces that precede it.

### 2. Carry the paired human-facing mapper `.md` contract too

- [d:c+r:i] Accept paired overlay carry for `gsd-pattern-mapper.md` in the same tranche.
- [e:c+i] The paired human-facing contract now matches the same AGENTS-governed project-context discovery, `.codex` runtime-surface discovery, anti-threshold mapping guidance, and broader discretion-section recognition. Sources: [.codex/agents/gsd-pattern-mapper.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.md:34), [.codex/agents/gsd-pattern-mapper.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.md:36), [.codex/agents/gsd-pattern-mapper.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.md:46), [.codex/agents/gsd-pattern-mapper.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.md:55).
- [d:r:i] Current consequence: reinstall/materialization no longer risks splitting the mapper surface between a carried runtime `.toml` and an installer-replaced `.md` that drifts back toward weaker project-context discovery.

## What This Rejects

- [d:r:i] Reject broad planner / plan-checker / PATTERNS consumer rewriting in the same tranche. This move was about carrying the mapper surface itself, not reopening the broader planning-chain doctrine stack.
- [d:r:i] Reject treating `gsd-pattern-mapper` as a note-only authority-gap surface forever. Its planner adjacency and current runtime routing are strong enough that continued live-only drift would just defer a warranted carry move.
- [d:r:i] Reject broad live-only cohort widening beyond this ordered quartet. The current carry is earned because this specific mapper sits directly on the planner’s pattern-assignment path, not because every remaining live-only agent now deserves symmetry carry.

## Initial Landing

- [e:c+i] The runtime-authoritative mapper contract is now carried in tracked overlay and currently materializes cleanly into live runtime. The post-carry runtime report records `agents/gsd-pattern-mapper.toml` as `intentional materialized carry` with `raw_equal` live/overlay hashes. Sources: [06-gsd-pattern-mapper-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/06-gsd-pattern-mapper-post-carry-runtime-visibility.json:424), [06-gsd-pattern-mapper-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/06-gsd-pattern-mapper-post-carry-runtime-visibility.json:437), [06-gsd-pattern-mapper-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/06-gsd-pattern-mapper-post-carry-runtime-visibility.json:438).
- [e:c+i] The paired human-facing mapper contract now materializes with exact live/overlay parity as well. Sources: [tooling/portable-gsd/overlay/agents/gsd-pattern-mapper.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-pattern-mapper.md:34), [.codex/agents/gsd-pattern-mapper.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.md:34).
- [e:c+i] The unresolved live-only cohort dropped again: the post-carry runtime report now records `12` `untracked_live_only_outside_overlay_subset` entries rather than `13`. Sources: [05-gsd-intel-updater-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/05-gsd-intel-updater-post-carry-runtime-visibility.json:19), [06-gsd-pattern-mapper-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/06-gsd-pattern-mapper-post-carry-runtime-visibility.json:19).

## Immediate Next Move

- [g:r:i] With the ordered four-agent authority/carry tranche now resolved, move next to the narrow judgment about whether any remaining package-truth or non-targeted parity residue still needs bounded follow-through before rerun-floor recomputation.
