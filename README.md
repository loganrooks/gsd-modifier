# gsd-modifier

`gsd-modifier` is a standalone extracted project for modifier-owned GSD behavior.

It carries:
- `harness_modifier/` package code and carriers
- `tooling/portable-gsd/overlay/` live overlay/install-materialization contract
- `tooling/codex/` development-support and compatibility helpers
- `scripts/setup-portable-gsd.sh` installer entrypoint

Audience split:
- `runtime user`: installs and uses the modifier in a host repo
- `contributing user`: uses it locally and can surface improvements upstream
- `harness developer`: develops the modifier itself and uses the full audit/review/governance loop

Current posture:
- first extracted repo cut
- internal layout is intentionally transitional so the repo stays executable and testable immediately
- CI is not the lead move; bootstrap and verification come first
- `.codex` is the current observed runtime basis
- `.claude` remains a held parity/runtime-development surface, not a widened runtime claim

Start here:
- [AGENTS.md](AGENTS.md)
- [WORKFLOW.md](WORKFLOW.md)
- [docs/development.md](docs/development.md)
- [docs/onboarding/codex.md](docs/onboarding/codex.md)
- [docs/onboarding/claude.md](docs/onboarding/claude.md)
- [docs/migration-origin.md](docs/migration-origin.md)

Quick bootstrap:

```bash
./scripts/setup-portable-gsd.sh
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest discover -s tooling/codex/tests
```
