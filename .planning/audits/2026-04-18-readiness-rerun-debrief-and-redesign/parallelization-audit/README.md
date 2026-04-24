Date: 2026-04-22
Status: active companion audit family

# Parallelization Audit

## Purpose

- [g:r:i] This subtree exists to diagnose parallelization and overlap as a real field rather than leaving it as one blurred vocabulary term.
- [d:r:i] Its focus is split across three distinct questions:
  - vanilla GSD parallelization posture
  - modified-harness parallelization posture
  - harness-improvement-program overlap posture

## Lane `01`

- [d:r:i] Lane `01` is the first explicit diagnosis pass on that split.
- [d:r:i] Attempt `1` used the full packet/spec/prompt tuple:
  - [packets/01-harness-parallelization-field-map-and-diagnosis-audit-packet.md](packets/01-harness-parallelization-field-map-and-diagnosis-audit-packet.md)
  - [specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md](specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md)
  - [prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md](prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md)
- [d:r:i] Attempt `1` stalled before any recoverable assistant text or final output:
  - [artifacts/01-harness-parallelization-field-map-and-diagnosis-audit-attempt-1-stall.md](artifacts/01-harness-parallelization-field-map-and-diagnosis-audit-attempt-1-stall.md)
- [d:r:i] The compact retry narrowed the frontier and wrote the final audit output:
  - [packets/01b-harness-parallelization-field-map-and-diagnosis-audit-compact-packet.md](packets/01b-harness-parallelization-field-map-and-diagnosis-audit-compact-packet.md)
  - [specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md](specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md)
  - [prompts/01b-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-compact-launch-prompt.md](prompts/01b-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-compact-launch-prompt.md)
  - [launch-truth/01-harness-parallelization-field-map-and-diagnosis-audit-launch-truth.md](launch-truth/01-harness-parallelization-field-map-and-diagnosis-audit-launch-truth.md)
  - [outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md](outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md)
  - [dispositions/01-harness-parallelization-field-map-and-diagnosis-audit-inheritance.md](dispositions/01-harness-parallelization-field-map-and-diagnosis-audit-inheritance.md)
- [d:r:i] The compact retry ran against frozen basis `8d9111d`.

## Current Consequence

- [d:r:i] `164` remains only the framing map.
- [d:r:i] `165` is now no longer only a route note; it now has a completed first lane under this subtree.
- [d:r:i] The paired internal cross-audit is now also preserved as a local inheritance companion under [dispositions/02-parallelization-internal-cross-audit-inheritance.md](dispositions/02-parallelization-internal-cross-audit-inheritance.md), with requested-versus-effective launch truth at [launch-truth/02-parallelization-internal-cross-audit-launch-truth.md](launch-truth/02-parallelization-internal-cross-audit-launch-truth.md).
- [d:r:i] This subtree should preserve:
  - the vanilla/modifier/program split
  - the difference between declared capability and governed live use
  - the difference between safe earned parallelization, promising but not-yet-governed parallelization, and parallelization that would likely degrade coherence or quality
