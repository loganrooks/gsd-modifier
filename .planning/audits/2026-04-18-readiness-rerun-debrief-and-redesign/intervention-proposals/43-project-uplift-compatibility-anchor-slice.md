Date: 2026-04-21
Status: landed compatibility anchor slice

# Project-Uplift Compatibility Anchor Slice

## Purpose

- [g:r:i] This note records the bounded compatibility follow-through after the first uplift slice and the signal-layer harden pass.
- [g:r:i] The target is not a broad version-window claim. The target is an explicit observed-basis compatibility surface inside the existing uplift producer/output chain.

## What Landed

- [e:r:i] [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py) now records a `compatibility_basis` block during analysis and durable write.
- [e:r:i] The current compatibility block carries:
  - `compatibility_posture: observed_basis_only`
  - observed runtime version from `.codex/get-shit-done/VERSION`
  - observed runtime manifest version from `.codex/gsd-file-manifest.json`
  - version-alignment state between those two runtime anchors
  - overlay schema anchor
  - uplift schema anchor
  - a compact check protocol for later runtime movement
  - wider compatibility claims held rather than overclaimed
- [e:r:i] The durable uplift outputs now carry that same block in one write pass:
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - the `Project Uplift` section in [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [e:r:i] The operator workflow contract now names the compatibility block explicitly in [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md), and the helper docs now describe the block in [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md).

## Why This Shape

- [d:r:i] The compatibility question is now carried through the existing uplift producer/output chain rather than split off into a detached first-pass manifest family.
- [d:r:i] That keeps the current slice bounded:
  - one producer
  - the already existing durable outputs
  - no new routed consumer
  - no wide compatibility matrix
- [d:r:i] The slice therefore makes runtime-basis assumptions more explicit without pretending the repo already carries a broader compatibility doctrine than it actually does.

## What Remains Held

- [d:r:i] This slice does not claim a wider supported version range beyond the currently observed runtime basis.
- [d:r:i] This slice does not open:
  - cross-runtime compatibility matrix work
  - upstream-template drift compatibility
  - a separate standalone compatibility carrier
  - a richer compatibility consumer network

## Current Consequence

- [d:r:i] The project-uplift family now carries an explicit compatibility anchor instead of leaving compatibility only as a later open question.
- [d:r:i] The remaining question is narrower now: whether the embedded anchor should later stay inside the uplift family or grow into a broader standalone compatibility carrier after more runtime-change slices have exercised it.
