# Install Profiles

## Role

This file records the current installation/runtime profiles for `gsd-modifier`.

It separates:
- what is part of the active core parity contract
- what is runtime-specific by design
- what is not yet claimed

## Active Core Profiles

### `codex-core`

This is one active core profile.

It means:
- local runtime basis is `.codex`
- bootstrap/install path is `./scripts/setup-portable-gsd-runtime.sh --runtime codex`
- manifest/materialization verification and shipped-contract checks are expected to pass here

### `claude-core`

This is the other active core profile.

- local runtime basis is `.claude`
- bootstrap/install path is `./scripts/setup-portable-gsd-runtime.sh --runtime claude`
- shared modifier-owned workflow, reference, template, and agent-markdown carriers are expected to pass here

## Runtime-Specific Carriers

These are allowed to differ by runtime without failing parity on their own.

Current examples:
- Codex skill wrappers and TOML registry/config carriers
- Claude command wrappers and `settings.json` / hook carriers

Parity rule:
- shared core outcomes must stay aligned
- runtime-specific wrappers may differ when they are declared as such

## Mixed Runtime

### `dual-runtime-core`

This profile is now active.

It means:
- the repo-self bootstrap/install path is `./scripts/setup-portable-gsd-runtime.sh --runtime both`
- repo-self CI and bootstrap run manifest/materialization verification across both runtimes together
- `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict` is part of the active mixed-runtime proof surface

The manual host proof for this profile is still separate from standard CI:
- `python3 harness_modifier/closure/host_exercise_matrix.py . --profile all --output-dir .planning/measurement/host-exercise-matrix --strict`

## Rule

Keep repo-self dual-runtime proof in CI/bootstrap, and rerun the synthetic host matrix before widening broader host compatibility or release language beyond the current bounded matrix.
