Date: 2026-04-22
Status: landed bounded follow-through

# Seed Migration Operator-Facing Pointer Bridge Implementation

## Landed Revisions

- [e:r:i] `project_uplift.py` progress-note output now carries three additional specialist-packet fields:
  - `show_seed_migration_pointer`
  - `seed_migration_candidate_count`
  - `seed_migration_pointer`
- [e:r:i] Candidate counting now stays aligned with the helper-side migration packet scope:
  - legacy-unversioned seeds
  - noncurrent-version seeds
  - current-version seed shape gaps
- [e:r:i] `progress.md` now keeps specialist-packet disclosure visible for ordinary progress summaries when the uplift note says migration candidates are present.
- [e:r:i] `resume-project.md` now keeps the same bounded disclosure visible during first-read re-entry.
- [e:r:i] The disclosed packet remains narrow and detect-only:
  - candidate count
  - specialist command pointer
  - no rewrite implication
  - no auto-write implication

## Proof Surfaces

- [d:r:i] Helper proof:
  - [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
- [d:r:i] Focused behavior coverage:
  - [test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py)
  - [test_seed_operator_consumer_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_seed_operator_consumer_follow_through_contract.py)
- [d:r:i] Live consumer surfaces:
  - [progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)

## Verification

- [d:r:i] Focused tests now prove:
  - quiet state keeps the specialist pointer absent
  - legacy-unversioned seed posture surfaces the pointer
  - current-version shape-gap posture surfaces the pointer
  - tracked progress/resume consumers explicitly carry the new lines
- [d:r:i] The live helper was rerun with durable uplift-memory refresh so the current repo resolves the new progress-note fields against the live manifest/output pair.
- [d:r:i] The overlay is rematerialized after the workflow changes so live `.codex` routing stays in tune with tracked carry.

## Current Consequence

- [d:r:i] The seed-migration packet is now easier to find at the ordinary operator surfaces that already surface uplift posture, without flattening that packet into a generic uplift recommendation.
- [d:r:i] The next adjacent move is cleaner now:
  - bounded reread of the landed bridge
  - then decide whether later entry-wrapper widening or broader seed-consumer widening earns inheritance
