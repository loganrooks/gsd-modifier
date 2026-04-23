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
- `codex-core` is the only actively exercised profile
- `.claude` remains a held runtime-development surface
- mixed-runtime claims remain later

## Typical Verification

```bash
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest discover -s tooling/codex/tests
./scripts/setup-portable-gsd.sh
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --strict
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict
git diff --check
```

## CI Gates

Canonical CI entrypoints live in:
- `scripts/ci/check-deterministic.sh`
- `scripts/ci/check-bootstrap.sh`

GitHub Actions uses those scripts directly so local and remote verification stay aligned.
