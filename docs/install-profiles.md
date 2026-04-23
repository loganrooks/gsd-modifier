# Install Profiles

## Role

This file records the current installation/runtime profiles for `gsd-modifier`.

It separates:
- what is actively exercised now
- what is readable but still held later
- what is not yet claimed

## Active Profile

### `codex-core`

This is the current actively exercised profile.

It means:
- local runtime basis is `.codex`
- bootstrap/install path is `./scripts/setup-portable-gsd.sh`
- CI is allowed to assert this profile
- manifest/materialization verification and shipped-contract checks are expected to pass here

Current CI coverage:
- deterministic/package gate
- bootstrap/integration gate

## Held Later Profiles

### `claude-runtime-development`

This profile remains explicitly later.

It means:
- `.claude` is still a held parity/runtime-development surface
- the repo should remain readable and developable from Claude
- the repo does not yet claim full `.claude` materialization parity in CI

### `mixed-runtime`

This profile also remains later.

It means:
- no claim yet that one install pass, one CI pass, or one support window covers both `.codex` and `.claude`
- mixed-runtime behavior needs its own bounded widening lane before it becomes a release claim

## Rule

Do not widen CI or release language beyond `codex-core` until the later runtime profiles are exercised and accepted explicitly.
