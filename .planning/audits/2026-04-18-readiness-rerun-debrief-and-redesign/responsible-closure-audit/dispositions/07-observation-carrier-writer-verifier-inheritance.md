Date: 2026-04-23
Status: completed local disposition

# Observation Carrier Writer Verifier Inheritance

## Launch Truth

- [d:r:i] Agent id: `019db90a-df38-7af1-ad03-56aad6d1310c`
- [d:r:i] Requested launch: `execution/verification -> gpt-5.4 -> high`
- [e:c+r:i] Effective runtime verification against `~/.codex/state_5.sqlite` matched the request:
  - `model: gpt-5.4`
  - `reasoning_effort: high`
  - `approval_mode: never`
  - `sandbox_policy: danger-full-access`
- [d:r:i] Estimated wall-clock: `6-12 minutes`
- [e:r:i] Actual elapsed from sqlite `updated_at - created_at`: `107s`
- [d:r:i] Timing calibration: this bounded verifier was materially faster than the estimate and should not be scheduled like an external Opus lane.

## Local Disposition

- [d:r:i] `revise -> accept`
- [d:r:i] The verifier caught two real contract gaps and one wording overreach; all three were incorporated before checkpointing the slice.

## Findings Accepted

1. [d:r:i] The writer needed a top-level allowlist so the JSON-only first carrier would reject leaked later-slice fields instead of silently persisting them.
2. [d:r:i] The writer needed to require canonical subtypes on subtype-bearing `semantic_deviation` and `positive_gain` rows instead of allowing structurally empty entries to pass validation.
3. [d:r:i] `harness_modifier/README.md` needed narrower wording so it did not claim observe-only host-exercise semantics before the packet contract exists.

## Carry Applied

- [d:r:i] `harness_modifier/closure/observation_record.json` now declares the required top-level field set.
- [d:r:i] `harness_modifier/closure/observation_writer.py` now:
  - rejects unexpected top-level fields
  - requires canonical subtype-bearing rows to actually carry canonical `signal_subtype` values
- [d:r:i] `tooling/codex/tests/test_closure_observation_writer.py` now covers:
  - unexpected top-level field rejection
  - missing `semantic_deviation.signal_subtype`
  - empty / subtype-missing `positive_gain` rows
- [d:r:i] `harness_modifier/README.md` now describes the current writer as the first JSON-only responsible-closure observation record writer, not a full observe-only host-exercise writer.

## Governance Consequence

- [d:r:i] The observation-carrier writer slice now has both local gate coverage and a separate bounded verifier pass.
- [d:r:i] The next adjacent move remains unchanged:
  1. checkpoint the observation-carrier writer slice
  2. open the host-exercise packet contract implementation slice
  3. keep the actual observe-only host run later
