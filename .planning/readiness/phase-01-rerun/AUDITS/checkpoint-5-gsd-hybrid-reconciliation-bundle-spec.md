# Checkpoint 5 GSD Hybrid Reconciliation Bundle Spec

## Purpose

Reconcile the completed repo-local raw inventory against:

- the clean version-matched upstream baseline
- the later upstream `main` trajectory surface

This bundle exists because repo-local inventory alone is not enough. The current repo has already modified or overlaid parts of GSD, and a truthful high-level map must distinguish:

- what exists locally now
- what is clean upstream truth at the installed version
- what is repo-local intervention
- what is later upstream evolution that may soon matter

## Audit Stance

- high-level reconciliation
- anti-local-only misread
- anti-fake-upstream
- anti-future-blindness
- still anti-premature-deep-zoom

## Governing Inputs

1. [checkpoint-5-gsd-high-level-mapping-program-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-high-level-mapping-program-spec.md)
2. [checkpoint-5-gsd-upstream-reference-points.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-reference-points.md)
3. [checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces.md)
4. [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces.md)
5. [checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces.md)
6. [checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a4-artifact-state-install-policy-surfaces.md)

## Bundle Shape

Run these first:

1. [checkpoint-5-gsd-hybrid-reconciliation-b1-entry-workflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b1-entry-workflow-surfaces-spec.md)
2. [checkpoint-5-gsd-hybrid-reconciliation-b2-agent-helper-materialization-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b2-agent-helper-materialization-surfaces-spec.md)
3. [checkpoint-5-gsd-hybrid-reconciliation-b3-artifact-policy-trajectory-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b3-artifact-policy-trajectory-surfaces-spec.md)

Then run:

4. [checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis-spec.md)

## Core Questions

- which mapped local surfaces are clean upstream truth at `v1.36.0`?
- which local surfaces are repo-local overlays, mutations, or readiness-only additions?
- which important upstream surfaces exist in the clean baseline but are underrepresented in the local mapping outputs?
- which important surfaces exist on upstream `main` and therefore represent likely near-horizon carry-forward pressure?
- what taxonomy of `local`, `upstream-baseline`, `upstream-trajectory`, `overlay`, `materialized-only`, and `readiness-only` is actually emerging?

## Output

This bundle should produce:

- [checkpoint-5-gsd-hybrid-reconciliation-b1-entry-workflow-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b1-entry-workflow-surfaces.md)
- [checkpoint-5-gsd-hybrid-reconciliation-b2-agent-helper-materialization-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b2-agent-helper-materialization-surfaces.md)
- [checkpoint-5-gsd-hybrid-reconciliation-b3-artifact-policy-trajectory-surfaces.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b3-artifact-policy-trajectory-surfaces.md)
- [checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-hybrid-reconciliation-b4-synthesis.md)

## Constraints

- stay high-level; this is not a full file-by-file diff
- do not silently flatten `v1.36.0` baseline and `main`
- do not treat local install state as proof of clean upstream behavior
- preserve unknowns if parity cannot be established cleanly

## Lane

- classification: `initial architecture research/planning`
- model / reasoning: `gpt-5.4 xhigh`
