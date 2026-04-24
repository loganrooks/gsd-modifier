Date: 2026-04-23
Status: completed implementation

# Harness Modifier First Observe-Only Host Exercise

## Role

- [d:r:i] This slice lands the first actual observe-only host exercise after the carrier-side moves in `175`, `176`, and responsible-closure lane `06`.
- [d:r:i] It is the first real host-evidence slice for responsible closure, not another packet-definition or observation-shape pass.

## What Landed

- [d:r:i] A package-owned runner now exists under `harness_modifier/closure/`:
  - [../../../harness_modifier/closure/host_exercise_runner.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/closure/host_exercise_runner.py)
- [d:r:i] Focused coverage now exists in:
  - [../../../../tooling/codex/tests/test_closure_host_exercise_runner.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_closure_host_exercise_runner.py)
- [d:r:i] The first disjoint host evidence slice is now frozen against:
  - host repo: `/home/rookslog/workspace/projects/gsd-modifier-host-fixture-01`
  - host basis commit: `43bd1f4e11bbdd5741cd209d32827d1241ff8e11`
  - artifact bundle:
    - [first-host-exercise-001-packet.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/01-host-exercise-gsd-modifier-host-fixture-01/first-host-exercise-001-packet.json)
    - [first-host-exercise-001-observation.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/01-host-exercise-gsd-modifier-host-fixture-01/first-host-exercise-001-observation.json)
    - [first-host-exercise-001-runtime-visibility-snapshot.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/01-host-exercise-gsd-modifier-host-fixture-01/first-host-exercise-001-runtime-visibility-snapshot.json)
    - [first-host-exercise-001-verify-materialized-summary.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/01-host-exercise-gsd-modifier-host-fixture-01/first-host-exercise-001-verify-materialized-summary.md)
- [d:r:i] The packet now preserves the real first-host boundary instead of overclaiming modifier materialization:
  - `compatibility_window_state: inside-window`
  - no Reflect artifacts
  - clean worktree
  - known host basis commit
  - conditional preflight narrowed to required reads because the host does not yet carry the modifier-side pristine/materialization marker
- [d:r:i] The observation now preserves the actual first-host result:
  - `disposition: shift-mode`
  - `compatibility_window` accepted
  - `verify_materialized` intentionally skipped with `skip_reason: context_deferred`
  - semantic deviation preserved as `contract-mismatch`, not as fake hard failure
- [d:r:i] The summary now tells the truth of the run:
  - full `verify_materialized` did not run
  - skip reason: host lacks `.codex/gsd-local-patches/backup-meta.json`

## Corrective Reread Consequence

- [d:r:i] A bounded verifier pass forced a real correction before this slice was accepted:
  - declaration-side compatibility was previously not being evaluated
  - full modifier-side `verify_materialized` was previously being over-applied to a plain upstream regular-GSD host
  - skip-reason semantics were previously missing
- [d:r:i] The accepted runner now makes the sharper distinction explicit:
  - inside the observed-basis compatibility window
  - but not yet carrying modifier-side materialization truth
- [d:r:i] That distinction matters for release-readiness work because host compatibility and modifier materialization are related but not identical questions.

## Deliberate Boundaries

- [d:r:i] This slice does not mutate the host repo.
- [d:r:i] This slice does not widen to a second host.
- [d:r:i] This slice does not widen to mixed `.codex` + `.claude` runtime exercise.
- [d:r:i] This slice does not claim write-side deployability.
- [d:r:i] This slice does not reopen `167`, harness-in-action parallelization, or the Phase 01 rerun boundary.

## Design Consequence

- [d:r:i] Responsible closure now has first real host evidence instead of only packet/observation contract preparation.
- [d:r:i] The first host evidence says the modifier has a cleaner read-side posture than write-side posture:
  - the host matched the observed runtime basis
  - the host did not yet carry modifier-side pristine/materialization state
  - the run therefore stayed read-side and routed the next move toward classification rather than mutation
- [d:r:i] The next bounded move is now a shipped/install-contract classification pass across package families, installer entrypoints, live overlay workflows/skills, and compatibility-shim paths, not another abstract host-exercise placeholder.

## Verification

- [d:r:i] `python3 -m py_compile harness_modifier/closure/host_exercise_runner.py harness_modifier/contract/runtime_visibility.py harness_modifier/contract/portable_gsd_contract.py`
- [d:r:i] `python3 -m unittest tooling.codex.tests.test_runtime_visibility tooling.codex.tests.test_portable_gsd_contract tooling.codex.tests.test_closure_host_exercise_packet_writer tooling.codex.tests.test_closure_observation_writer tooling.codex.tests.test_closure_host_exercise_runner`
- [d:r:i] `python3 harness_modifier/closure/host_exercise_runner.py /home/rookslog/workspace/projects/gsd-modifier-host-fixture-01 --modifier-repo-root /home/rookslog/workspace/projects/prix-guesser --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/01-host-exercise-gsd-modifier-host-fixture-01 --exercise-id first-host-exercise-001 --host-reference gsd-modifier-host-fixture-01 --host-age-posture pristine --narrative-summary "Regular Codex GSD host stayed read-side; modifier-owned verification surfaced install-contract gap rather than mutating the host."`
- [d:r:i] `git diff --check`

## Exact Next Move

1. [d:r:i] Route this first host-evidence slice into the responsible-closure, release-readiness, propagation, and governing-state carriers.
2. [d:r:i] Open the shipped/install-contract classification pass as the next bounded release-readiness move.
3. [d:r:i] Keep second-host and mixed-runtime exercises explicitly later, and keep `167` sequential.
