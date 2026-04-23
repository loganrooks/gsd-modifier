# Codex Onboarding

## Role

This is the day-one Codex bootstrap for continuing `gsd-modifier` development in the extracted repo.

## Read First

1. [AGENTS.md](../../AGENTS.md)
2. [WORKFLOW.md](../../WORKFLOW.md)
3. [docs/development.md](../development.md)
4. [docs/migration-origin.md](../migration-origin.md)

## Bootstrap

```bash
./scripts/setup-portable-gsd.sh
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest discover -s tooling/codex/tests
```

## What Matters

- this repo now owns the modifier project directly
- `tooling/portable-gsd/overlay/` is still part of the same project even though the internal layout is transitional
- the carried origin-audit context is in [docs/origin-audit](../origin-audit), not in chat memory
