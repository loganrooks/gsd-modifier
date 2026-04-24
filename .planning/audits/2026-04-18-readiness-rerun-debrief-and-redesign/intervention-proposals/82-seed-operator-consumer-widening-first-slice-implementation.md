Date: 2026-04-22
Status: landed first slice

# Seed Operator-Consumer Widening First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `81`.
- [g:r:i] The target stayed bounded: progress and resume now carry seed corpus posture through the existing uplift-note bridge without widening into audit or migration routes.

## What Landed

- [e:r:i] The uplift helper now includes operator-facing seed posture fields in its progress-note payload:
  - [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
- [e:r:i] The progress-note payload now keeps three seed-specific fields explicit:
  - `show_seed_corpus_posture`
  - `seed_corpus_posture`
  - `seed_corpus_reasons`
- [e:r:i] That seed posture now surfaces in the two operator-facing consumers that already read the uplift note:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)
- [e:r:i] The operator-facing display keeps progressive disclosure explicit:
  - seed posture lines only appear when a seed corpus exists
  - seed posture reasons stay separate from generic uplift reasons
- [e:r:i] Focused proof now lives in:
  - [tooling/codex/tests/test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py)
  - [tooling/codex/tests/test_seed_operator_consumer_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_operator_consumer_follow_through_contract.py)

## What This Slice Still Holds

- [d:r:i] This slice does not widen `audit.cjs`.
- [d:r:i] It does not widen additional entry wrappers.
- [d:r:i] It does not migrate legacy seeds.

## Current Consequence

- [d:r:i] Seed corpus posture is now easier to see during ordinary progress and resume instead of staying concentrated at milestone-open or only inside durable uplift memory.
- [d:r:i] The next narrower seed-family question is cleaner:
  - later `audit.cjs` widening
  - later wider entry-wrapper retrofit
  - any later standalone legacy seed migration family
