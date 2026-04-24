Date: 2026-04-20
Status: bounded authority-review disposition

# High-Leverage Live-Only Authority Review

## Purpose

- [g:r:i] This note reviews the four-agent next-tranche cluster named in [18-live-only-agent-authority-carry-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/18-live-only-agent-authority-carry-proposal.md:1) and orders it by actual intervention leverage rather than by filename symmetry.

## Reviewed Cluster

- `gsd-code-reviewer`
- `gsd-code-fixer`
- `gsd-intel-updater`
- `gsd-pattern-mapper`

## Disposition

### 1. `gsd-code-reviewer` is the first next-candidate

- [d:r:i] Promote `gsd-code-reviewer.toml` to the first bounded authority/carry candidate.
- [e:c+i] It is directly routed in the live review workflows and has already been named repeatedly in the readiness rerun work as a still-under-dispositioned review-surface authority boundary. Sources: [.codex/get-shit-done/workflows/code-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review.md:2), [.codex/get-shit-done/workflows/code-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review.md:347), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:26), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:705), [.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c4-bin-agent-overlay-omitted-surface-gap-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c4-bin-agent-overlay-omitted-surface-gap-audit-internal-r1.md:7), [.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:67).
- [d:r:i] This is the highest-yield next review because repo-local review doctrine and audit quality already matter in this workspace, and `gsd-code-reviewer` sits directly on that path.

### 2. `gsd-code-fixer` should be paired conceptually but reviewed second

- [d:r:i] Keep `gsd-code-fixer.toml` in the same thematic cluster, but do not let it outrun `gsd-code-reviewer`.
- [e:c+i] It is clearly active in the remediation chain, but earlier readiness work already framed it more as a follow-on quality opportunity than the immediate must-feed review boundary. Sources: [.codex/get-shit-done/workflows/code-review-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review-fix.md:2), [.codex/get-shit-done/workflows/code-review-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review-fix.md:181), [.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c4-bin-agent-overlay-omitted-surface-gap-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19c4-bin-agent-overlay-omitted-surface-gap-audit-internal-r1.md:49).
- [d:r:i] Current consequence: review after `gsd-code-reviewer`, ideally in a paired tranche if the reviewer pass exposes shared carry logic.

### 3. `gsd-intel-updater` is real but not first

- [d:r:i] Keep `gsd-intel-updater.toml` as a real later candidate, not a present first move.
- [e:c+i] It is active and important, but the current repo-local pressure is still stronger on review/remediation carry than on intel refresh carry. Sources: [.codex/get-shit-done/bin/lib/intel.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/intel.cjs:319), [.codex/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:34), [.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md:631).

### 4. `gsd-pattern-mapper` remains an authority-gap case, not a first carry patch

- [d:r:i] Keep `gsd-pattern-mapper.toml` out of the first next patch lane.
- [e:c+i] It is planner-adjacent and real, but the stronger immediate pressure is still routing/authority clarification rather than tracked overlay carry. Sources: [13-live-only-agent-targeted-reread-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/13-live-only-agent-targeted-reread-disposition.md:1), [.codex/get-shit-done/bin/lib/model-profiles.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/model-profiles.cjs:22), [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:289).

## Ordered Next-Tranche Sequence

- [d:r:i] Sequence the next bounded authority/carry work as:
  1. `gsd-code-reviewer`
  2. `gsd-code-fixer`
  3. `gsd-intel-updater`
  4. `gsd-pattern-mapper`

## Immediate Next Move

- [g:r:i] Run the next bounded authority/carry review on `gsd-code-reviewer.toml` first, with explicit attention to whether tracked overlay carry is actually needed or whether a narrower authority clarification would carry more with less widening.
