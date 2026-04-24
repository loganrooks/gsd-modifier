Date: 2026-04-21
Status: active packet

# Landed Project Uplift First-Slice Reread Packet

## Purpose

- [g:r:i] This packet presents the landed project-uplift first slice for one bounded reread after implementation.
- [g:r:i] The target is no longer bundle design in the abstract. The target is the actual live slice:
  - helper behavior
  - workflow and skill carry
  - durable uplift outputs
  - read-only `progress` consumption
- [g:r:i] The question is how this landed slice should now be strengthened, what should remain explicit later-family work, and which adjacent route should come next without collapsing back into generic onboarding.

## Read Order

### Current Local Basis

1. [intervention-proposals/37-entry-surface-and-project-uplift-map.md](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md)
2. [intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md](../../intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md)
3. [intervention-proposals/39-project-uplift-workflow-proposal.md](../../intervention-proposals/39-project-uplift-workflow-proposal.md)
4. [intervention-proposals/40-project-uplift-first-slice-implementation.md](../../intervention-proposals/40-project-uplift-first-slice-implementation.md)

### Prior Challenge And Inheritance

5. [entry-uplift-audit/outputs/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1.md](../outputs/03-revised-entry-surface-project-uplift-bundle-reread-opus47-max-r1.md)
6. [entry-uplift-audit/dispositions/03-revised-entry-surface-project-uplift-bundle-reread-inheritance.md](../dispositions/03-revised-entry-surface-project-uplift-bundle-reread-inheritance.md)

### Live Implementation Surfaces

7. [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
8. [test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py)
9. [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
10. [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
11. [progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md)

### Live Repo Outputs

12. [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
13. [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
14. [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)

### Governing Context

15. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
16. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
17. [CURRENT-STATE.md](../../CURRENT-STATE.md)

## What The Reread Should Be Able To Judge

- [d:r:i] What the landed first slice now carries more strongly than the pre-implementation bundle.
- [d:r:i] Whether the helper, workflow, and output chain keep posture classification, durable memory, and routing distinct enough in live use.
- [d:r:i] Whether the read-only `progress` consumer now gives the family real downstream carry instead of only local report generation.
- [d:r:i] Which parts of the landed slice still thin, blur, or compress distinct jobs that should stay more explicit.
- [d:r:i] Which strengthening moves would sharpen this landed slice before any additive install route or cross-runtime uplift widening.
- [d:r:i] Which later families should remain explicit later-family work rather than being silently absorbed into the first slice.
