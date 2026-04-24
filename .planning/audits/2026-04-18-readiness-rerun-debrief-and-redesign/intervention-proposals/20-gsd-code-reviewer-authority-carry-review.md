Date: 2026-04-20
Status: accepted bounded carry patch

# `gsd-code-reviewer` Authority / Carry Review

## Purpose

- [g:r:i] This note resolves the first bounded live-only authority/carry review named in [19-high-leverage-live-only-authority-review.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/19-high-leverage-live-only-authority-review.md:1): whether `gsd-code-reviewer` should stay a live-only exception or be carried into the tracked repo-local harness.

## Why This Surface Earned Review-Now Pressure

- [e:c+i] `gsd-code-reviewer` is not peripheral. The live runtime registers it directly in config and routes it through both the dedicated code-review workflow and the quick workflow. Sources: [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:24), [.codex/get-shit-done/workflows/code-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review.md:347), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:700).
- [e:c+i] Earlier readiness work already treated this exact file as a named under-dispositioned review boundary rather than as harmless family remainder. Sources: [.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c4-bin-agent-overlay-omitted-surface-gap-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c4-bin-agent-overlay-omitted-surface-gap-audit-internal-r1.md:7), [.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:67), [.planning/readiness/phase-01-rerun/STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:161).
- [e:c+i] The clean-boundary runtime snapshot then confirmed the same thing in current runtime terms: before this patch, `agents/gsd-code-reviewer.toml` existed live with no overlay carry, no manifest carry, and no backup-meta carry. Sources: [01-second-tranche-clean-boundary-runtime-visibility-snapshot.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/01-second-tranche-clean-boundary-runtime-visibility-snapshot.json:128), [17-manifest-install-coherence-pass.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/17-manifest-install-coherence-pass.md:18).

## Accepted Carry

### 1. Carry the runtime-authoritative reviewer `.toml` into tracked overlay

- [d:c+r:i] Accept tracked overlay carry for `gsd-code-reviewer.toml`.
- [e:c+i] The live contract had stayed on the older project-context model: `./CLAUDE.md`, `.claude/skills/`, and CLAUDE-framed convention handling. That was weaker than the repo’s current runtime doctrine and weaker than the already-carried high-stakes `.toml` cohort. Sources: [.codex/agents/gsd-code-reviewer.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-code-reviewer.toml:17), [.codex/agents/gsd-code-reviewer.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-code-reviewer.toml:120), [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml:24), [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml:24).
- [d:r:i] Current consequence: `gsd-code-reviewer.toml` should no longer survive as an uncarried live-only exception. It now belongs in the tracked overlay subset.

### 2. Carry the paired human-facing reviewer `.md` contract too

- [d:c+r:i] Accept paired overlay carry for `gsd-code-reviewer.md` in the same tranche.
- [e:c+i] The first installer rerun showed why this is not gratuitous widening: the `.toml` patch survived once it was in overlay, but the reviewer `.md` patch did not survive because the installer still treated it as an unmanaged local modification. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:21), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:44), [tooling/portable-gsd/overlay/agents/gsd-code-reviewer.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-code-reviewer.md:25), [tooling/portable-gsd/overlay/agents/gsd-code-reviewer.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-code-reviewer.md:128).
- [d:r:i] Leaving the `.md` contract uncarried would preserve a nearby contradiction inside the same reviewer surface: the runtime-owned file would be repo-local and AGENTS-governed while the adjacent operator-facing contract would regress on every refresh.

### 3. Correct the installer’s top-level reasoning-default regression

- [d:c+r:i] Accept the adjacent installer fix in the same tranche.
- [e:c+i] The materialization pass exposed a live contradiction: after overlay application, `scripts/setup-portable-gsd.sh` forced `.codex/config.toml` back to `model_reasoning_effort = "high"` even though this repo’s top-level orchestration doctrine expects `xhigh`. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:46), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:57), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:122), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1).
- [d:r:i] Current consequence: the carry patch is not just new overlay files. It also needs the installer source corrected so the repo does not immediately degrade its own orchestration default on refresh.

## What This Rejects

- [d:r:i] Reject broad review-rubric rewriting of `gsd-code-reviewer`. This tranche only corrects project-context authority, doctrine-aware quality bar, reviewer identity/output phrasing, and durability through materialization.
- [d:r:i] Reject folding `gsd-code-fixer` into the same patch by symmetry alone. `gsd-code-fixer` remains second in sequence until this reviewer carry patch is fully recorded and verified.
- [d:r:i] Reject treating the installer-discovered `xhigh -> high` regression as acceptable ambient churn. If the repo says top-level orchestration should default to `xhigh`, the install path cannot quietly enforce the weaker setting.

## Initial Landing

- [e:c+i] The runtime-authoritative reviewer contract is now carried in tracked overlay and currently materializes cleanly into live runtime. The post-carry runtime-visibility report records `agents/gsd-code-reviewer.toml` as `intentional materialized carry` with raw-equal live/overlay hashes. Sources: [tooling/portable-gsd/overlay/agents/gsd-code-reviewer.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-code-reviewer.toml:1), [03-gsd-code-reviewer-post-carry-runtime-visibility.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/03-gsd-code-reviewer-post-carry-runtime-visibility.json:120).
- [e:c+i] The paired human-facing contract is now also carried through overlay rather than left as a reinstall-lost local modification. Sources: [tooling/portable-gsd/overlay/agents/gsd-code-reviewer.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-code-reviewer.md:25), [.codex/agents/gsd-code-reviewer.md](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-code-reviewer.md:25).
- [e:c+i] The installer source now preserves the repo’s intended top-level reasoning default, and the live config currently materializes with `model_reasoning_effort = "xhigh"`. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:46), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:1).

## Immediate Next Move

- [g:r:i] Move to the second ordered surface: run the same bounded authority/carry review on `gsd-code-fixer.toml`, now that the reviewer lane no longer sits as an unresolved live-only exception.
