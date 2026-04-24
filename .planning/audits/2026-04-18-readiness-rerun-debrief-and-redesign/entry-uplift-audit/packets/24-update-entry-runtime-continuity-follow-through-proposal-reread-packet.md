Date: 2026-04-22
Status: active packet

# Update Entry Runtime Continuity Follow-Through Proposal Reread Packet

## Purpose

- [g:r:i] This packet presents the next adjacent consumer proposal after the landed and reread earliest-entry continuity slice.
- [g:r:i] The target is not to reopen whether the shared-reference family exists at all.
- [g:r:i] The target is the proposed `update.md` plus `gsd-update` follow-through:
  - how the first workflow-plus-wrapper consumer should inherit the continuity surface
  - how the lane-17 harden points should fold into that same batch
  - what should still stay outside this slice

## Read Order

### Current Local Basis

1. [intervention-proposals/130-entry-runtime-continuity-shared-reference-first-slice-implementation.md](../../intervention-proposals/130-entry-runtime-continuity-shared-reference-first-slice-implementation.md)
2. [intervention-proposals/131-update-entry-runtime-continuity-follow-through-proposal.md](../../intervention-proposals/131-update-entry-runtime-continuity-follow-through-proposal.md)

### Prior Challenge And Inheritance

3. [entry-uplift-audit/outputs/21-landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1.md](../outputs/21-landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1.md)
4. [entry-uplift-audit/dispositions/21-landed-entry-runtime-continuity-first-slice-reread-inheritance.md](../dispositions/21-landed-entry-runtime-continuity-first-slice-reread-inheritance.md)

### Live Consumer And Comparison Surfaces

5. [tooling/portable-gsd/overlay/get-shit-done/references/entry-runtime-uplift-continuity.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/entry-runtime-uplift-continuity.md)
6. [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md)
7. [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md)
8. [tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-from-gsd2/SKILL.md)
9. [tooling/codex/tests/test_entry_runtime_continuity_shared_reference_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_entry_runtime_continuity_shared_reference_contract.py)

### Durable Repo-Local Continuity Carriers

10. [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
11. [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
12. [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
13. [propagation-audit/48-entry-runtime-continuity-shared-reference-change-triggered-refresh.md](../../propagation-audit/48-entry-runtime-continuity-shared-reference-change-triggered-refresh.md)

### Governing Context

14. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
15. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
16. [CURRENT-STATE.md](../../CURRENT-STATE.md)

## What The Reread Should Be Able To Judge

- [d:r:i] Whether `131` chooses the right adjacent consumer after the earliest-entry pair.
- [d:r:i] What `update.md` and `gsd-update` should each carry explicitly, and what should stay separated.
- [d:r:i] Whether folding the lane-17 harden into the same batch is cleaner than a standalone harden-only pass.
- [d:r:i] Where the proposed route still risks blurring:
  - runtime/package movement
  - structural-health routing
  - later write-side uplift refresh
  - broader multi-provider detection
- [d:r:i] What should remain explicit later-family work, especially:
  - `from-gsd2`
  - `.claude` parity/translation
  - version-window or matrix widening
  - broader provider-frontier narrowing
- [d:r:i] How this proposed consumer should be inherited next.
