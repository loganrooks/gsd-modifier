Date: 2026-04-22
Status: active packet

# Seed Migration Detect-Only First-Slice Reread Packet

## Purpose

- [g:r:i] This packet presents the landed legacy-seed migration detect-only slice for one bounded reread after implementation.
- [g:r:i] The target is not generic seed-family rediscovery and not rewrite design in the abstract.
- [g:r:i] The target is the actual live slice:
  - specialist helper behavior
  - workflow and skill carry
  - uplift-side handoff
  - propagation-registry refresh
  - current durable uplift memory
- [g:r:i] The question is how this landed slice now broadens operator control, maintainability, and propagation visibility, where it still compresses distinct jobs, and which adjacent route should inherit next without blurring detect-only inventory into rewrite.

## Read Order

### Adjacent Seed-Family Basis

1. [intervention-proposals/77-seed-doctrine-vintage-anchor-first-slice-proposal.md](../../intervention-proposals/77-seed-doctrine-vintage-anchor-first-slice-proposal.md)
2. [intervention-proposals/78-seed-doctrine-vintage-anchor-first-slice-implementation.md](../../intervention-proposals/78-seed-doctrine-vintage-anchor-first-slice-implementation.md)
3. [intervention-proposals/79-uplift-side-seed-corpus-posture-first-slice-proposal.md](../../intervention-proposals/79-uplift-side-seed-corpus-posture-first-slice-proposal.md)
4. [intervention-proposals/80-uplift-side-seed-corpus-posture-first-slice-implementation.md](../../intervention-proposals/80-uplift-side-seed-corpus-posture-first-slice-implementation.md)
5. [intervention-proposals/81-seed-operator-consumer-widening-first-slice-proposal.md](../../intervention-proposals/81-seed-operator-consumer-widening-first-slice-proposal.md)
6. [intervention-proposals/82-seed-operator-consumer-widening-first-slice-implementation.md](../../intervention-proposals/82-seed-operator-consumer-widening-first-slice-implementation.md)
7. [intervention-proposals/83-seed-audit-gate-widening-first-slice-proposal.md](../../intervention-proposals/83-seed-audit-gate-widening-first-slice-proposal.md)
8. [intervention-proposals/84-seed-audit-gate-widening-first-slice-implementation.md](../../intervention-proposals/84-seed-audit-gate-widening-first-slice-implementation.md)
9. [intervention-proposals/85-legacy-seed-corpus-migration-detect-only-first-slice-proposal.md](../../intervention-proposals/85-legacy-seed-corpus-migration-detect-only-first-slice-proposal.md)
10. [intervention-proposals/86-legacy-seed-corpus-migration-detect-only-first-slice-implementation.md](../../intervention-proposals/86-legacy-seed-corpus-migration-detect-only-first-slice-implementation.md)

### Propagation Carry

11. [propagation-audit/35-legacy-seed-corpus-migration-detect-only-change-triggered-refresh.md](../35-legacy-seed-corpus-migration-detect-only-change-triggered-refresh.md)
12. [propagation-audit/artifacts/03-propagation-registry-v2-declared-contracts.json](../artifacts/03-propagation-registry-v2-declared-contracts.json)
13. [propagation-audit/artifacts/04-propagation-registry-v2-semantic-map.json](../artifacts/04-propagation-registry-v2-semantic-map.json)
14. [propagation-audit/artifacts/05-propagation-registry-v2-evidence-index.json](../artifacts/05-propagation-registry-v2-evidence-index.json)
15. [propagation-audit/artifacts/06-propagation-registry-v2-coverage-and-refresh.json](../artifacts/06-propagation-registry-v2-coverage-and-refresh.json)

### Live Implementation Surfaces

16. [seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/seed_migration_inventory.py)
17. [test_seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory.py)
18. [test_seed_migration_inventory_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_migration_inventory_follow_through_contract.py)
19. [seed-migration-inventory.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/seed-migration-inventory.md)
20. [gsd-seed-migration-inventory/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md)
21. [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
22. [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
23. [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)

### Live Repo Outputs

24. [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
25. [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
26. [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
27. [UPLIFT-HELD-LATER.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/UPLIFT-HELD-LATER.md)

### Governing Context

28. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
29. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
30. [CURRENT-STATE.md](../../CURRENT-STATE.md)
31. [HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md)

## Current Repo Reality

- [e:r:i] The current repo does not carry a live `.planning/seeds/` corpus, so this reread must judge the slice as a route and inventory packet, not as an already-exercised rewrite family.
- [d:r:i] The absence of a live seed corpus does not erase the question of whether the route, outputs, propagation refresh, and neighboring carriers are now shaped in the strongest current form.

## What The Reread Should Be Able To Judge

- [d:r:i] What the landed detect-only slice now carries more explicitly than the prior uplift-side posture/counts/example route.
- [d:r:i] Whether helper, workflow, wrapper, uplift handoff, and propagation refresh now keep inventory, routing, and later rewrite pressure distinct enough in live use.
- [d:r:i] Whether the current no-seed-corpus repo posture still leaves any route ambiguity or misleading quietness in the landed slice.
- [d:r:i] Which neighboring carriers still deserve sharpening before any rewrite/normalization family or wider entry-wrapper follow-through.
- [d:r:i] Which adjacent route should inherit next:
  - later rewrite/normalization
  - later broader audit-open widening
  - later wider entry-wrapper retrofit
  - another bounded route the reviewer can justify concretely
