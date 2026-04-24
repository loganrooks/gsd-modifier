# Wave-2 R5.18 Materialization Proof

Status: local verification note  
Date: 2026-04-19

## Frame

- [d:r:i] This artifact records the first executed tranche of [09-r5-18-materialization-and-package-truth-fix-slice.md](09-r5-18-materialization-and-package-truth-fix-slice.md).
- [d:r:i] Its purpose is not to claim final closure of `R5.18`. It is to make one narrower fact reviewable: the targeted `R5.18` review/planning and completion-routing surfaces now survive the actual installer/materialization path rather than only one dirty worktree.

## What Was Patched

- [e:c+i] The transition workflow now treats `completion_mode: debt_carrying_execution`, `completion_mode: debt_carrying_completion`, and `completion_debt` as debt-bearing transition signals instead of only scanning for self-check failure text and testing-status markers. Sources: [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:82), [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:99).
- [e:c+i] The readiness package now records `R5.8` as an active bounded fix surface rather than a merely conditional future risk. Sources: [.planning/readiness/phase-01-rerun/STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:27), [.planning/readiness/phase-01-rerun/STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md:166), [.planning/readiness/phase-01-rerun/TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md:14), [.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md:28).
- [e:c+i] The tracked overlay now carries the targeted live `R5.18` surfaces for review/planning, router, completion, and materialization checks, including `agent-contracts.md`, `planner-reviews.md`, `plan-phase.md`, `review.md`, `do.md`, `progress.md`, `transition.md`, `verification-overrides.md`, `phase.cjs`, `roadmap.cjs`, the `gsd-review` / `gsd-plan-phase` / `gsd-do` skills, and the executor/verifier agent files. Sources: [tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:1), [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:1), [tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:1), [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:1), [tooling/portable-gsd/overlay/get-shit-done/workflows/do.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/do.md:1), [tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md:1), [tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md:1), [tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md:1), [tooling/portable-gsd/overlay/get-shit-done/bin/lib/phase.cjs](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/bin/lib/phase.cjs:1), [tooling/portable-gsd/overlay/get-shit-done/bin/lib/roadmap.cjs](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/bin/lib/roadmap.cjs:1), [tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-review/SKILL.md:1), [tooling/portable-gsd/overlay/skills/gsd-plan-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-plan-phase/SKILL.md:1), [tooling/portable-gsd/overlay/skills/gsd-do/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-do/SKILL.md:1), [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml:1), [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml:1).

## Verification Performed

- [e:r:i] Rendered-parity check passed on all `15` targeted surfaces after substituting `__PROJECT_ROOT__` back to the repo path. No targeted overlay/live mismatch remained.
- [e:c+r:i] The real installer/materialization path was then executed via [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:18), which performs a fresh local GSD install and reapplies every tracked overlay file into `.codex/`. A post-install parity check again returned `OVERLAY_PARITY_OK` for the same targeted surface set.

## What This Proves

- [d:r:i] The targeted `R5.18` frontier is no longer only local-runtime residue. For the bounded surface set named above, tracked overlay truth now reproduces the live `.codex` frontier through the actual installer path.
- [d:r:i] That is enough to retire the earlier narrower blocker `these targeted surfaces cannot survive reinstall` for this slice.

## What This Does Not Yet Prove

- [o:r:i] It does not prove that every repo-local GSD customization outside the targeted `R5.18` set is now perfectly tracked or version-upgrade-stable.
- [o:r:i] It does not by itself close the broader rerun program, rerun-floor recomputation, brake-exit doctrine, or activation-trigger doctrine.
- [o:r:i] It does not fully disposition whether any remaining non-targeted `.codex` / overlay divergence should stay later-lane work or needs further bounded inclusion now.

## Status Consequence

- [d:r:i] The bounded `R5.18` materialization slice has moved from proposal into partial execution with proof.
- [d:r:i] The next honest move is to checkpoint this batch cleanly, then decide whether any remaining package-truth or non-targeted parity residue needs one more narrow pass before rerun-floor recomputation proceeds.
