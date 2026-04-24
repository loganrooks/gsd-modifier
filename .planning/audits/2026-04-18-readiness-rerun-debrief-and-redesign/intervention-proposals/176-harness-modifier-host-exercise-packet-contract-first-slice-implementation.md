Date: 2026-04-23
Status: completed implementation

# Harness Modifier Host-Exercise Packet Contract First Slice

## Role

- [d:r:i] This slice lands the second carrier-side responsible-closure move after `175`.
- [d:r:i] It implements the first package-owned host-exercise packet contract and writer, without widening into the actual observe-only host run.

## What Landed

- [d:r:i] New responsible-closure packet home under `harness_modifier/closure/`:
  - [../../../harness_modifier/closure/host_exercise_packet.json](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/closure/host_exercise_packet.json)
  - [../../../harness_modifier/closure/host_exercise_packet.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/closure/host_exercise_packet.py)
  - [../../../harness_modifier/closure/host_exercise_packet_writer.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/closure/host_exercise_packet_writer.py)
- [d:r:i] The packet contract now makes the audited first-host scope machine-legible:
  - `target_host_class: codex-disjoint-gsd-installed-no-reflect`
  - `runtime_class: codex-only`
  - `host_shape: disjoint-codex-only`
  - required regular-GSD posture
  - explicit no-Reflect-artifacts rule
  - explicit clean-worktree and known-basis-commit rule
  - explicit disjoint-from-`prix-guesser` host-path rule
- [d:r:i] The contract now owns the shared packet-side vocabulary that should not live as observation-side folklore:
  - required and conditional preflight reads
  - declaration-capture field set
  - output-pointer field set
  - enumerated abort-condition codes
  - enumerated Reflect-artifact abort list
  - canonical `check_outcome` vocabulary
  - canonical `automation_skip_reasons`
- [d:r:i] The writer now applies current compatibility-declaration defaults for:
  - `declaration_posture`
  - `observed_basis_runtime`
  - `held_annotation_runtime`
  - `compatibility_window_state`
- [d:r:i] The observation writer now consumes the packet contract for shared exercise vocabulary:
  - `target_host_class`
  - `check_outcome`
  - `skip_reason`
- [d:r:i] Packet list fields now canonicalize at validation time instead of allowing duplicate `preflight_reads` or `abort_conditions` to pass as set-equal noise.
- [d:r:i] Focused coverage landed in:
  - [../../../../tooling/codex/tests/test_closure_host_exercise_packet_writer.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_closure_host_exercise_packet_writer.py)
  - [../../../../tooling/codex/tests/test_closure_observation_writer.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_closure_observation_writer.py)

## Deliberate Boundaries

- [d:r:i] This slice does not yet run an actual observe-only host exercise.
- [d:r:i] This slice does not yet schedule recurring packet execution or automated host selection.
- [d:r:i] This slice does not broaden the first host class to mixed `.codex` + `.claude` or Reflect-carrying hosts.
- [d:r:i] This slice does not widen into any write-side deployment path.
- [d:r:i] This slice does not reopen `167`, harness-in-action parallelization, or the Phase 01 rerun boundary.

## Design Consequence

- [d:r:i] `174` is now real packet-side contract ownership, not just prose ownership.
- [d:r:i] The responsible-closure bundle now has both halves of the first carried shape:
  - observation record and writer under `175`
  - host-exercise packet contract and writer under `176`
- [d:r:i] The next adjacent move is therefore no longer packet-definition work.
- [d:r:i] The next adjacent move is a bounded reread over the landed packet slice before any actual host exercise is opened.

## Verification

- [d:r:i] `python3 -m py_compile harness_modifier/closure/observation_record.py harness_modifier/closure/observation_writer.py harness_modifier/closure/host_exercise_packet.py harness_modifier/closure/host_exercise_packet_writer.py`
- [d:r:i] `python3 -m unittest tooling.codex.tests.test_closure_observation_writer tooling.codex.tests.test_closure_host_exercise_packet_writer`
- [d:r:i] bounded internal verifier reread carried through [../responsible-closure-audit/dispositions/08-host-exercise-packet-contract-verifier-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/dispositions/08-host-exercise-packet-contract-verifier-inheritance.md)
- [d:r:i] `python3 -m json.tool harness_modifier/closure/observation_record.json`
- [d:r:i] `python3 -m json.tool harness_modifier/closure/host_exercise_packet.json`
- [d:r:i] `git diff --check`

## Exact Next Move

1. [d:r:i] Route this implementation into the responsible-closure and propagation/governance surfaces.
2. [d:r:i] Run one bounded reread on the landed packet-contract slice.
3. [d:r:i] Keep the actual observe-only host run later, after that reread.
