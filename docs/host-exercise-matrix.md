# Host Exercise Matrix

## Role

This document defines the synthetic host-fixture matrix for `gsd-modifier`.

It is the manual release-readiness proof route for bounded external host shapes. Repo-self dual-runtime proof already lives in bootstrap/CI; this matrix checks whether the modifier behaves coherently against synthetic disjoint hosts.

## Current Boundary

This matrix stays inside the current first-host contract:

- disjoint host repo
- regular GSD already present
- no Reflect artifacts
- observe-only execution
- synthetic host fixtures, not product-host fixtures

Profiles:
- `codex`
- `dual-runtime`
- `all`

## Scenarios

### `pristine-read-side`

- profile: `codex`
- expected disposition: `shift-mode`
- proves: the Codex lane emits packet, observation, runtime snapshot, and skipped verify-materialized evidence cleanly for a read-side host

### `materialized-aligned`

- profile: `codex`
- expected disposition: `accept`
- proves: the current tracked Codex overlay contract can be synthesized into a deterministic aligned host without verify-materialized hard failures

### `version-drift`

- profile: `codex`
- expected disposition: `refuse`
- proves: version-window refusal still triggers before broader host compatibility language is widened

### `dual-runtime-read-side`

- profile: `dual-runtime`
- expected disposition: `shift-mode`
- proves: a host carrying both `.codex` and `.claude` can be observed safely before modifier-side materialization exists

### `dual-runtime-aligned`

- profile: `dual-runtime`
- expected disposition: `accept`
- proves: both runtime trees can be synthesized together into an aligned mixed-runtime host shape

### `dual-runtime-core-conflict`

- profile: `dual-runtime`
- expected disposition: `refuse`
- proves: composed mixed-runtime refusal is exercised when one runtime drifts off the observed basis even if both runtime trees are otherwise materialized

## Run

Run everything:

```bash
python3 harness_modifier/closure/host_exercise_matrix.py . \
  --profile all \
  --output-dir .planning/measurement/host-exercise-matrix \
  --strict
```

Run only one lane:

```bash
python3 harness_modifier/closure/host_exercise_matrix.py . \
  --profile dual-runtime \
  --output-dir .planning/measurement/host-exercise-matrix \
  --strict
```

Outputs:

- one synthetic host per scenario under a disjoint sibling staging root recorded in `matrix-summary.json`
- one packet, runtime-visibility snapshot, verify-materialized summary, and observation record per scenario
- one top-level `matrix-summary.json`

`--strict` exits non-zero when any scenario misses its expected disposition or parity state, any expected artifact is missing, or an aligned case produces verify-materialized hard failures.

## Relationship To `harness_canary`

Use `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict` for repo-self runtime/install invariants.

Use the host exercise matrix when the question is whether the current modifier surface can be exercised against the bounded external host-shape set.

They answer different questions:

- `harness_canary` checks the modifier repo’s own live runtime/install invariants across both runtimes
- the host exercise matrix checks synthetic external host shapes for Codex-only and dual-runtime profiles
