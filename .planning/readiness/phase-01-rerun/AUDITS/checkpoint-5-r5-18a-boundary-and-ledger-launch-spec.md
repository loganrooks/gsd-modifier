# Checkpoint 5 R5.18a Boundary Split Launch Spec

Purpose: split the old one-piece `R5.18a` lane into two distinct decision lanes so current-wave boundary/ledger work does not get conflated with broader later-lane / quiet-drop adjudication.

This is not the main edit wave.

## Split

### `R5.18a1`

Current-wave boundary and contradiction-ledger decisions.

This lane decides the live `Bucket 3` / active-frontier questions that must be settled before `R5.18b` and `R5.18c` can patch.

### `R5.18a2`

Named-later-lane and quiet-drop adjudication.

This lane decides what broader governance concerns remain live but outside current rerun-critical ownership, and forces them into explicit later-lane ownership instead of silence.

## Why Split

The split 2026-04-15 comparison showed that the old one-piece `R5.18a` had to answer two different questions:

1. what must be decided now to authorize the current patch wave
2. what broader governance concerns remain live enough to require named later-lane ownership

Keeping those together makes it too easy to:

- smuggle broader concerns into current-wave authorization
- or quietly drop them while pretending the current-wave boundary is complete

## Sequencing

1. run `R5.18a1`
2. run `R5.18a2`
3. let `R5.18b` and `R5.18c` consume the resulting current-wave authorization plus later-lane restrictions
4. then run `R5.18d`

## Governing Inputs

1. [checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-launch-spec.md)
2. [checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-spec.md)
3. [checkpoint-5-r5-18a-boundary-challenge-checklist.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-challenge-checklist.md)
