Date: 2026-04-22
Status: landed change-triggered refresh

# Harness Modifier In-Place Rehome Step 1 Change-Triggered Refresh

## Trigger

- [d:r:i] `138` moved from proposal into a landed code-helper rehome slice through [139-harness-modifier-in-place-rehome-step-1-implementation.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/139-harness-modifier-in-place-rehome-step-1-implementation.md).

## Propagation Effect

- [d:r:i] The generic helper carrier authority moved from `tooling/codex/*.py` to `harness_modifier/contract/*` plus `harness_modifier/capture/*`.
- [d:r:i] The old `tooling/codex/*.py` paths still exist, but only as thin compatibility shims. They no longer count as the semantic home of those carriers.
- [d:r:i] This affects:
  - install/materialization carrier paths
  - launch-truth and probe carrier paths
  - active script entrypoints
  - operator doctrine and review-route references
  - typed propagation registry `v2` carrier locations

## Refreshed Surfaces

- [d:r:i] installer/materialization bridge:
  - [setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:1)
- [d:r:i] doctrine/operator surfaces:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:62)
  - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:90)
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:75)
  - [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md:14)
- [d:r:i] local tooling/read surfaces:
  - [harness_modifier/README.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/README.md:1)
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:1)
  - [tooling/portable-gsd/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/README.md:44)
- [d:r:i] workflow-side operator route:
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:63)
- [d:r:i] typed propagation registry `v2` path carriers:
  - [14-propagation-registry-generation-and-seeding-policy.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/14-propagation-registry-generation-and-seeding-policy.md:33)
  - [artifacts/03-propagation-registry-v2-declared-contracts.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/03-propagation-registry-v2-declared-contracts.json:1)
  - [artifacts/04-propagation-registry-v2-semantic-map.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/04-propagation-registry-v2-semantic-map.json:1)
  - [artifacts/05-propagation-registry-v2-evidence-index.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/05-propagation-registry-v2-evidence-index.json:1)

## Held Boundary

- [d:r:i] No full whole-registry redesign in this slice.
- [d:r:i] No overlay/workflow/skill/template/reference rehome in this slice.
- [d:r:i] No standalone repo or npm/`npx` execution in this slice.
