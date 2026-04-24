Date: 2026-04-22
Status: frozen lane packet

# Harness Extraction Field Map Audit Packet

## Lane Purpose

- [g:r:i] Challenge the current local extraction field map for turning the bundled harness modifier into its own standalone project installable into other repos.

## Why This Lane Exists Now

- [e:c+i] The workspace-state lane and its local inheritance exposed a live scope leak: host-project planning doctrine can be mistaken for harness doctrine when both remain co-located. Sources:
  - [../../workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md](../../workspace-state-audit/dispositions/01-where-are-we-now-horizon-inheritance-and-parallelization-audit-inheritance.md)
  - [../../intervention-proposals/136-harness-extraction-escalation-and-scope-boundary-note.md](../../intervention-proposals/136-harness-extraction-escalation-and-scope-boundary-note.md)
- [e:c+i] The modifier layer now owns enough workflows, skills, helpers, parity disclosure, propagation disclosure, and governance carry that later extraction is no longer just packaging appetite. Sources:
  - [../../intervention-proposals/101-repo-local-workflow-additions-and-propagation-map-orientation.md](../../intervention-proposals/101-repo-local-workflow-additions-and-propagation-map-orientation.md)
  - [../../intervention-proposals/115-harness-modifier-extraction-and-npx-distribution-route.md](../../intervention-proposals/115-harness-modifier-extraction-and-npx-distribution-route.md)
  - [../../intervention-proposals/137-harness-extraction-field-map.md](../../intervention-proposals/137-harness-extraction-field-map.md)

## Read Set

Read these exact files:

1. [../../intervention-proposals/115-harness-modifier-extraction-and-npx-distribution-route.md](../../intervention-proposals/115-harness-modifier-extraction-and-npx-distribution-route.md)
2. [../../intervention-proposals/136-harness-extraction-escalation-and-scope-boundary-note.md](../../intervention-proposals/136-harness-extraction-escalation-and-scope-boundary-note.md)
3. [../../intervention-proposals/137-harness-extraction-field-map.md](../../intervention-proposals/137-harness-extraction-field-map.md)
4. [../../CURRENT-STATE.md](../../CURRENT-STATE.md)
5. [../../WORKSPACE-AUTHORITY-AND-ORGANIZATION.md](../../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md)
6. [../../GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md](../../governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md)
7. [../../../../HARNESS-IMPROVEMENT-REGISTER.md](../../../../HARNESS-IMPROVEMENT-REGISTER.md)
8. [../../intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md](../../intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md)
9. [../../intervention-proposals/96-repo-local-propagation-delta-first-slice.md](../../intervention-proposals/96-repo-local-propagation-delta-first-slice.md)
10. [../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md](../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md)
11. [../../intervention-proposals/134-codex-claude-parity-classification-carrier-proposal.md](../../intervention-proposals/134-codex-claude-parity-classification-carrier-proposal.md)
12. [../../intervention-proposals/135-codex-claude-parity-classification-carrier-implementation.md](../../intervention-proposals/135-codex-claude-parity-classification-carrier-implementation.md)
13. [/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
14. [/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py)
15. [/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)

## Governing Questions

- [g:r:i] Is the current field split between generic harness carriers, host-project-specific carriers, and shared boundary carriers sharp enough, or where does it still blur?
- [g:r:i] What would a standalone harness project need to own directly?
  - workflows / skills
  - helpers / tooling
  - governance / doctrine
  - compatibility declaration
  - installer / update / materialization bridge
- [g:r:i] What should remain host-repo-local even after extraction?
- [g:r:i] What is the cleaner distribution shape:
  - separate repo first
  - package later
  - package plus installer
  - other bounded sequence
- [g:r:i] How should `.codex`, `.claude`, and `get-shit-done` installation/materialization differences be carried by the extracted project?
- [g:r:i] What migration sequence would preserve local override control, propagation clarity, and update resilience?

## Anti-Misread Notes

- [g:r:i] Do not collapse the answer into immediate yes/no extraction.
- [g:r:i] Do not widen into all-provider portability; keep `.codex` and `.claude` as the primary runtime horizon.
- [g:r:i] Do not assume npm packaging is automatically the right first move.
- [g:r:i] Do not treat host-project planning doctrine as if it should automatically move with the extracted harness project.

## Output Target

- [d:r:i] Write the lane return to:
  - [../outputs/01-harness-extraction-field-map-audit-opus47-max-r1.md](../outputs/01-harness-extraction-field-map-audit-opus47-max-r1.md)
