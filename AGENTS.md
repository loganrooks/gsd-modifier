# AGENTS.md

## Scope

This repo is the standalone home for `gsd-modifier`.

- treat this repo as the modifier project, not as a host product repo
- do not import `prix-guesser` product-planning horizons as if they govern this repo
- use [WORKFLOW.md](WORKFLOW.md) and [docs/development.md](docs/development.md) as the primary operator surfaces

## Source Of Truth

- shipped/runtime-facing surfaces:
  - `harness_modifier/`
  - `tooling/portable-gsd/overlay/`
  - `scripts/setup-portable-gsd.sh`
- development-support surfaces:
  - `tooling/codex/`
  - `tooling/codex/tests/`
- migration/provenance carry:
  - [docs/migration-origin.md](docs/migration-origin.md)
- carried origin audit dossier:
  - [docs/origin-audit](docs/origin-audit)

## Working Rules

- treat bootstrap and verification as load-bearing; do not change runtime/install surfaces without checking neighboring tests and scripts
- keep portability in view: source files should use `__PROJECT_ROOT__` placeholders where the materialization contract expects them
- keep the distinction explicit between:
  - shipped/runtime surfaces
  - development-program-only helpers
  - carried origin-audit context
- keep install-profile claims disciplined:
  - `codex-core` is the active exercised profile
  - `.claude` is still held runtime-development carry
  - mixed-runtime claims are later
- prefer changes that keep the extracted repo executable and auditable on its own, not ones that quietly depend on the old host repo

## Verification

Default verification stack for substantive changes:
- `python3 -m py_compile ...`
- `python3 -m unittest ...`
- `./scripts/setup-portable-gsd.sh`
- `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --strict`
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict`
- `git diff --check`

Canonical CI scripts:
- `bash scripts/ci/check-deterministic.sh`
- `bash scripts/ci/check-bootstrap.sh`

If you change bootstrap/governance docs:
- `python3 tooling/codex/audit_refmap.py verify .`
- `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines ...` where relevant
