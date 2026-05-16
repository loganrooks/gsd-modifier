# Pilot Debrief: mandatory-initial-read.md

Date: 2026-05-16
Phase: 3 (`03-pilot`)
Carrier: `get-shit-done/references/mandatory-initial-read.md`
Pilot result: mechanism proven; phase-boundary follow-up required before Phase 4

## Worked as designed

- The schema v4 `mode: inject` manifest entry materialized through both runtime profiles.
- Both Codex and Claude runtime outputs preserved the upstream mandatory initial read text exactly at the top of the file.
- Both runtime outputs contain the modifier-owned reading-packet tier content inside the expected marker pair:
  - `<!-- GSD_MODIFIER:start key:GSD_MODIFIER:references-mandatory-initial-read:extended-content -->`
  - `<!-- GSD_MODIFIER:end key:GSD_MODIFIER:references-mandatory-initial-read:extended-content -->`
- `verify_inject_state` correctly reported the pilot operation as verified for both runtimes:
  - target: `get-shit-done/references/mandatory-initial-read.md`
  - operation kind: `block_replace`
  - marker key: `GSD_MODIFIER:references-mandatory-initial-read:extended-content`
  - status: `verified`
  - detail: `marker present between anchors`
- The one-time schema v4 follow-through now reaches the compatibility declaration and current compatibility readers.
- The cross-runtime reviewer-dispatch `.claude` references in the Codex-local `adversarial-cross-vendor-audit` skill are now classified as intentional baseline, not unreviewed runtime drift.

## Surprised by

- The planned `schema_version` bump was not only a manifest edit. The compatibility declaration, project-uplift compatibility basis, and schema-version tests also needed the same v4 follow-through.
- `bash scripts/ci/check-bootstrap.sh` is a composite gate: it runs runtime materialization, then full `tooling/codex/tests` discovery, then later contract/canary/refmap checks. The materialization work can be clean while the script still exits 1 on stale non-pilot tests.
- A separate direct canary run exposed an inject-awareness gap in `runtime_visibility.py`: inject materializers intentionally have `source_path: ""`, but runtime visibility still treats every manifest spec as source-backed and tries to read `Path(".")`.

## Operator-visible risks

- `check-bootstrap.sh` currently cannot be treated as a single clean signal for this pilot. Its runtime materialization segment is green for the pilot, but the full-discover step still fails on non-pilot baseline tests before the script reaches its later contract gates.
- The full-discover baseline shape changed. Four failing assertions are the already-known stale source-reclassification tests for `gsd-from-gsd2` and `gsd-plant-seed`. Two failures are runtime-state-dependent tests against the materialized `.codex` surface: seed-audit helper and transition/uplift continuity. The current run did not reproduce the previously named state-snapshot future-carry failure.
- `runtime_visibility.py` is a Phase 3 phase-boundary blocker. Before the phase-boundary verifier can honestly run the plan's canary gate, a reviewer-mediated follow-up must teach runtime visibility how to classify `mode: inject` entries without reading an empty `source_path`.
- Two follow-up candidates should stay outside this slice:
  - Split `check-bootstrap.sh` into a scoped bootstrap/materialization gate and a broader full-regression gate.
  - Clean up the stale seed/migration/uplift full-discover tests in a separate non-inject cleanup slice.

## Schema feedback

No ADR amendment is needed for the schema itself. The schema's `mode: inject` shape, marker key requirements, parity intent, and mixed-mode coexistence model held under the real carrier.

The implementation ecosystem needed schema v4 follow-through in compatibility metadata and compatibility-basis readers. That has now been done in this slice under reviewer-mediated scope expansion.

## Operation-kind feedback

`block_replace` worked for this carrier. It is slightly indirect because the operation replaces an empty span between identical anchors, but the approach matches the Phase 3 design and avoids adding a one-off prepend kind.

No new operation kind is needed before Phase 4.

## Marker convention feedback

The marker convention survived the real Markdown content cleanly. The markers are visible enough for audit, unique enough for verification, and did not interfere with the upstream mandatory initial read prose.

No marker-key convention change is needed before Phase 4.

## Verification feedback

- `python3 -m unittest tooling.codex.tests.test_inject_back_compat tooling.codex.tests.test_portable_gsd_contract tooling.codex.tests.test_project_uplift` passed after the schema v4 compatibility fixture updates.
- `python3 -m py_compile harness_modifier/contract/portable_gsd_contract.py tooling/codex/project_uplift.py tooling/codex/tests/test_inject_back_compat.py tooling/codex/tests/test_portable_gsd_contract.py tooling/codex/tests/test_project_uplift.py` passed.
- `bash scripts/ci/check-deterministic.sh` passed.
- `./scripts/setup-portable-gsd-runtime.sh --runtime both` passed.
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict` passed with top-level `hard_failures: []`.
- Direct inspection of both materialized files confirmed the expected upstream text plus injected modifier block.
- `bash scripts/ci/check-bootstrap.sh` was run twice and exited 1 both times. The failure occurred at full unittest discovery after materialization had completed. This is recorded as a composite-gate failure, not as a failed pilot materialization.
- `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict` currently fails on the `runtime_visibility.py` inject `source_path` assumption. This must be closed before Phase 3 boundary verification.

Full-discover failure categories from the current run:

- Reclassified-source stale baseline:
  - `test_health_and_migration_follow_through_contract` still expects `skills/gsd-from-gsd2/SKILL.md` to be `overwrite` and reads the deleted old overlay path.
  - `test_seed_consumer_follow_through_contract` still expects `skills/gsd-plant-seed/SKILL.md` to be `overwrite` and reads the deleted old overlay path.
- Runtime-state-dependent materialized-surface baseline:
  - `test_seed_audit_gate_follow_through_contract` fails through a node helper against materialized runtime state.
  - `test_transition_uplift_continuity` fails through `.codex/get-shit-done/bin/gsd-tools.cjs phase complete` against materialized runtime state.

## Recommendation

Proceed with the inject migration design, but do not enter Phase 4 yet.

The next move should be a narrow reviewer-mediated Phase 3 follow-up slice that fixes `runtime_visibility.py` and its tests for `mode: inject` entries, then reruns the phase-boundary gates. After that follow-up passes, Phase 3 should move to boundary verification. If the boundary verifier passes, enter Phase 4.
