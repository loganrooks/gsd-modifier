# Development

## Current Shape

This repo currently carries three distinct but connected layers:

- runtime/shipped modifier surface
  - `harness_modifier/`
  - `tooling/portable-gsd/overlay/`
  - `scripts/setup-portable-gsd.sh`
- development-support and compatibility surface
  - `tooling/codex/`
  - `tooling/codex/tests/`
- origin/provenance carry
  - [docs/migration-origin.md](migration-origin.md)
  - [docs/origin-audit](origin-audit)

## Re-entry

Use [handoff/current.md](handoff/current.md) as the stable re-entry and current-boundary surface.

## Immediate Goal

Keep the extracted repo executable, auditable, and portable on its own.

That means:
- fix portability defects before widening features
- keep root onboarding clear
- keep verification runnable locally
- do not assume the old host repo is present

## Current Install Profile

Use [install-profiles.md](install-profiles.md) as the current runtime/install claim surface.

Right now:
- `codex-core` and `claude-core` are the active core profiles
- parity is defined at the shared capability layer, not the wrapper/config file layer
- `dual-runtime-core` is active at the repo-self proof layer
- the synthetic host matrix remains the manual release-readiness gate for broader host-shape language

Use [host-exercise-matrix.md](host-exercise-matrix.md) for the current Codex plus dual-runtime host proof matrix.

## Typical Verification

```bash
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest discover -s tooling/codex/tests
./scripts/setup-portable-gsd-runtime.sh --runtime both
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict
git diff --check
```

## CI Gates

Canonical CI entrypoints live in:
- `scripts/ci/check-deterministic.sh`
- `scripts/ci/check-bootstrap.sh`

GitHub Actions uses those scripts directly so local and remote verification stay aligned.
