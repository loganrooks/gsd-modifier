# Checkpoint 5 GSD Hybrid Reconciliation B2: Agent, Helper, And Materialization Surfaces

## Purpose

Compare agent, reference, helper, template, install, and materialization surfaces across local runtime and upstream baseline.

## Inputs

1. [checkpoint-5-gsd-hybrid-reconciliation-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-bundle-spec.md)
2. [checkpoint-5-gsd-upstream-reference-points.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-reference-points.md)
3. [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)
4. [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)

## Questions

- which helper, agent, reference, and template surfaces are clean upstream truth at `v1.36.0`?
- which ones are overlay or repo-local intervention layers?
- where is materialization/install behavior introducing a separate layer from tracked upstream?
- which helper/materialization surfaces on upstream `main` should be treated as near-horizon pressure?

## Output

Write:

- [checkpoint-5-gsd-hybrid-reconciliation-b2-agent-helper-materialization-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b2-agent-helper-materialization-surfaces.md)

Required sections:

- `Research Frame`
- `Path Of Inquiry`
- `Confirmed Clean-Upstream Surfaces`
- `Confirmed Repo-Local Intervention Surfaces`
- `Materialization-Layer Findings`
- `Missing Or Under-Mapped Upstream Surfaces`
- `Upstream-Main Trajectory Signals`
- `Implications For Later High-Level Map`

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
