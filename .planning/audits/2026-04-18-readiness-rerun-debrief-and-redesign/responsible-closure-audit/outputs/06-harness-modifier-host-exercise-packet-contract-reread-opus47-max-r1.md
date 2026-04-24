Date: 2026-04-23
Status: completed audit

# Harness Modifier Host-Exercise Packet Contract Reread

## Packet Contract Judgment

- [d:r:i] `176` moves `174` from prose ownership into writer-enforced ownership. The packet policy file (`harness_modifier/closure/host_exercise_packet.json`) is now the single declared home for:
  - `target_host_class_vocab`
  - `runtime_class_vocab`
  - `host_shape_vocab`
  - `host_age_posture_vocab`
  - `required_preflight_reads` and `conditional_preflight_reads`
  - `declaration_capture_fields`
  - `output_pointer_fields`
  - `abort_condition_codes`
  - `reflect_artifact_abort_list`
  - `check_outcome_vocab`
  - `automation_skip_reasons`
- [d:r:i] The writer enforces that sovereignty at validation time rather than letting it degrade to metadata: `validate_host_exercise_packet` rejects unexpected top-level fields, requires every `required_top_level_fields` entry, pins `bundle_family == responsible-closure`, pins `exercise_mode == observe-only`, canonicalizes `preflight_reads` and `abort_conditions` against the policy, and canonicalizes list fields with uniqueness instead of set-equality.
- [d:r:i] The shared exercise vocabulary check asked for by the spec now carries with explicit writer-side enforcement rather than discovery-by-convention:
  - `target_host_class`: observation writer sources its vocabulary from `host_exercise_packet_policy()["target_host_class_vocab"]` rather than redeclaring it; packet writer pins it to the same single-valued vocab for the first host class.
  - `check_outcome`: observation writer validates `expectation_vs_observation[].check_outcome` against `packet_policy["check_outcome_vocab"]`; packet writer owns the enumeration.
  - `skip_reason`: observation writer validates `expectation_vs_observation[].skip_reason` against `packet_policy["automation_skip_reasons"]`; packet writer owns the enumeration. The ownership correction noted in `dispositions/08` (skip-reasons moved from observation to packet) is visibly realized in code.
- [d:r:i] Pre-run-contract posture reads cleanly: the packet writer treats the packet document as a declared intention, not a run claim. No filesystem scan, no host mutation, no worktree touch at validation time. The `reflect_artifact_abort_list` is carried at policy layer for a later run-side scanner, but the packet writer only pins the boolean declaration `host_has_reflect_artifacts == False` — the enumerated list is staged for the run slice, which is where it belongs.
- [d:r:i] One detail worth carrying forward rather than expanding now: the packet declares `schema_version: 1` and `default_packet_version: 1` separately, and the observation declares `carrier_version`. The families are named differently but apply the same integer-version discipline; keeping them separate families rather than unifying them preserves the packet/observation split instead of blurring it.

## Observation Handoff Judgment

- [d:r:i] The observation writer now consumes rather than redeclares packet vocabulary. `validate_observation_record` loads `packet_policy = host_exercise_packet_policy()` at the top and references it three times (for `target_host_class_vocab`, `check_outcome_vocab`, `automation_skip_reasons`). That is the concrete realization of the inheritance rule in `dispositions/06` that shared fields should be declared once in `174` and referenced from `173`, not built as a competing second layer.
- [d:r:i] The row-family split preserves per-side ownership cleanly:
  - packet layer owns declaration-time facts about the host (`host_has_regular_gsd`, `host_has_reflect_artifacts`, `host_age_posture`, `declaration_capture`, `output_targets`) and the vocabularies the observation reuses.
  - observation layer owns per-run facts (`observation_id`, `observed_at`, `exercise_id`, `evidence_family`, `disposition`, the five signal families, `measurement_provenance`).
  - `target_host_class` is the only field redeclared on both sides, and it is bound to the same single-valued vocabulary rather than allowed to drift.
- [d:r:i] One narrow handoff gap remains, and it does not block the next move: the observation carries no explicit back-reference to the packet that produced it. `basis_commit`, `target_host_class`, and `exercise_id` on the observation can be joined against packet `declaration_capture.basis_commit`, `target_host_class`, and `packet_id`, but there is no enforced `packet_id` on the observation or `exercise_id` on the packet. Adding an optional `packet_id` pointer on the observation, or an `exercise_ref` on the packet, would tighten durable joinability. I would carry this as a small refinement candidate to fold into the first run slice rather than as a prior blocker.
- [d:r:i] The `skip_reason` / `check_outcome` validation currently only fires inside `expectation_vs_observation` rows; it does not fan out into `deployment_context`, `semantic_deviation`, or `positive_gain` rows. That is consistent with the current row-family design (those families carry subtypes rather than outcomes) and does not need to widen now, but is worth preserving as an explicit boundary rather than an implicit one.

## Boundary Enforcement Judgment

- [d:r:i] The first-host boundary is now enforced at writer level, not merely declared at prose level. Each spec bullet lands as real validator code:
  - disjoint host: `validate_host_exercise_packet` resolves `host_repo_path` and rejects any overlap with `REPO_ROOT` via `_paths_overlap`, which tests equality and both `in parents` directions — so it catches subdirectory, parent, and identity cases rather than only direct equality.
  - regular GSD already installed: rejects `host_has_regular_gsd == False`.
  - no Reflect artifacts: rejects `host_has_reflect_artifacts == True` and carries the enumerated `reflect_artifact_abort_list` at policy layer for the later run-side scanner.
  - clean worktree: rejects `declaration_capture.dirty_worktree == True`.
  - known basis commit: rejects `basis_commit` equal to `unknown` or `not_available` after case-folding and stripping.
- [d:r:i] The test corpus in `tooling/codex/tests/test_closure_host_exercise_packet_writer.py` exercises these boundaries directly: unknown `target_host_class`, Reflect-artifact host, missing required preflight read, incomplete abort conditions, same-repo `host_repo_path`, dirty worktree capture, unknown basis commit, duplicate `preflight_reads`, duplicate `abort_conditions`. The boundary enforcement is therefore not only declared but actively defended against a set of regression shapes.
- [d:r:i] Two things are intentionally left outside the pre-run contract and are correctly left later: filesystem scanning for Reflect artifacts on the actual host, and basis-commit agreement between the packet and the observation that gets produced against it. The first belongs to the run-side runner that consumes the packet; the second is a cross-artifact check that only becomes meaningful once a real observation exists.
- [d:r:i] The packet stays pre-run without leaking into a dress-rehearsal claim. That is the correct carry level for this slice.

## What Moves Now

- [d:r:i] The next bounded move can now be the actual observe-only host exercise. The four spec lenses — exercise-vocabulary owner, first-host-scope owner, observation-handoff surface, pre-run contract — are each carried at writer level, not only at prose level, and the slice is not overpacked.
- [d:r:i] The run slice, when opened, should stay at:
  - one disjoint `.codex`-only host
  - one packet authored against the current policy
  - one observation record produced from that run
  - one `runtime_visibility` snapshot file pointed to by `output_targets.runtime_visibility_snapshot_path`
  - one `verify_materialized_summary` file pointed to by `output_targets.verify_materialized_summary`
- [d:r:i] The run slice should carry the run-side pieces that are intentionally absent from the packet contract:
  - a filesystem scanner that walks `reflect_artifact_abort_list` against the declared `host_repo_path` and aborts on presence
  - a basis-commit agreement check between `packet.declaration_capture.basis_commit` and `observation.basis_commit`
  - a worktree-cleanliness re-check at run time, since the packet only captures the declared state
- [d:r:i] Two small refinements can be folded into the opening of that run slice without reopening `176`:
  - add an optional `packet_id` back-reference field on the observation record (or a symmetric `exercise_ref` forward-reference on the packet) so durable joins between packet and observation do not rely on the current three-field composite key
  - capture `input_packet_path` alongside `observation_record_path` in whatever runner metadata the run slice produces, so the observation can be traced back to the exact packet document that produced it

## What Remains Explicitly Later

- [d:r:i] Any widening of `target_host_class` beyond `codex-disjoint-gsd-installed-no-reflect`. Mixed `.codex` + held-annotation `.claude` and Reflect-carrying hosts remain explicitly later, not the first run.
- [d:r:i] Any write-side deployment path. The packet contract and the first run both remain observe-only.
- [d:r:i] Any recurrence, fleet, or dashboard appetite. Operator-triggered single-run execution remains the intended shape.
- [d:r:i] Any `automation_level` escalation beyond `1` on the observation carrier.
- [d:r:i] `167` stays sequential. The extraction-family install-contract pointer neutralization move does not bundle into this run, even if the run produces signals that make the `167` carry easier.
- [d:r:i] Phase 01 rerun boundary stays held.
- [d:r:i] Harness-in-action parallelization stays later.
- [d:r:i] Severity fields on the observation carrier stay later (still carried by sidecar disposition `05` as explicitly-later).
- [d:r:i] A second signal-subtype expansion, a narrative mirror artifact distinct from in-record `narrative_summary`, and a telemetry dashboard family are not on the next bounded move.

## Exact Next Moves

1. [d:r:i] Treat responsible-closure lane `06` as the completed reread over the landed packet-contract slice. Mark `176 + propagation-audit/63` as inherited.
2. [d:r:i] Open the actual observe-only host run as the next responsible-closure implementation slice. Keep its scope strictly: one disjoint `.codex`-only host, one packet, one observation, two output files. No host mutation, no write-side install path.
3. [d:r:i] Inside that run slice, land the run-side pieces intentionally absent from the packet: `reflect_artifact_abort_list` filesystem scanner, `basis_commit` agreement check, run-time worktree-cleanliness re-check.
4. [d:r:i] Inside that same run slice, fold the two small handoff refinements: optional `packet_id` back-reference on the observation, and `input_packet_path` in runner metadata. Do not reopen `176` for these; carry them as additive observation-side fields.
5. [d:r:i] Keep `167` sequential and explicit. Do not let the run slice absorb extraction-family appetite.
6. [d:r:i] Keep the Phase 01 rerun boundary held across every lane this run slice touches.
7. [d:r:i] Schedule the propagation refresh to travel with the run slice, not only with its observation artifact: `CURRENT-STATE.md`, `STATUS.md`, `INDEX.md`, `HARNESS-IMPROVEMENT-REGISTER.md`, `responsible-closure-audit/README.md`, and `intervention-proposals/166` should move in the same change.
