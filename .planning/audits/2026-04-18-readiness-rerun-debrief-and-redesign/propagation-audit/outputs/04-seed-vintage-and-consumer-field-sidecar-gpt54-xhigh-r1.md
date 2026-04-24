Date: 2026-04-21
Status: completed sidecar mapping memo

# Seed Vintage And Consumer Field Sidecar

## Seed Vintage

- [e:r:i] Filesystem inspection found no live `.planning/seeds/` directory in the current worktree, so there is no repo-local seed corpus here to classify by vintage.
- [e:c+i] The live canonical seed contract now lives in [tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plant-seed.md) and its milestone-open consumer in [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md).
- [e:c+i] The clearest live vintage ambiguity is a stale alternate producer: [.codex/get-shit-done/workflows/explore.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/explore.md) still describes legacy seed output shape with `.planning/seeds/{slug}.md`, `trigger_condition`, and `planted_date`.

## Current Consumer Field

- [e:c+i] Direct seed-file consumer: [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md).
- [e:c+i] Route/preservation carriers beyond milestone-open already exist in:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [.codex/get-shit-done/workflows/resume-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md)
  - [tooling/portable-gsd/overlay/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/state.md)
  - [tooling/portable-gsd/overlay/get-shit-done/templates/verification-report.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/verification-report.md)
- [e:c+i] A second live seed-file reader exists in [.codex/get-shit-done/bin/lib/audit.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/audit.cjs), but it thins meaning down to seed id, status, and title.

## Adjacent Carrier Candidates

- [d:r:i] `gsd-explore` is the strongest adjacent carrier because it still mints stale seed shape today.
- [d:r:i] `audit.cjs` is the next most natural reader to widen later because it already scans seed files but drops `Why This Matters`, `Strengthening Carry`, and any future vintage marker.
- [d:r:i] Uplift remains a plausible router later, not the first producer fix.

## Inherited Direction

- [d:r:i] The strongest bounded next slice after `73/74` is producer convergence:
  - bring `explore` onto the current seed contract
  - extend focused tests so the stale producer path cannot quietly return
- [d:r:i] This should happen before broader seed doctrine-vintage or wider entry-wrapper retrofit, because stale producer drift is the live route that could still mint mixed-vintage seeds.
