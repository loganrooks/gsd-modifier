# Claude Onboarding

## Role

This is the day-one Claude bootstrap for continuing `gsd-modifier` development in the extracted repo.

## Read First

1. [AGENTS.md](../../AGENTS.md)
2. [WORKFLOW.md](../../WORKFLOW.md)
3. [docs/development.md](../development.md)
4. [docs/migration-origin.md](../migration-origin.md)

## Current Claude Posture

- `.claude` is an active core runtime profile
- parity is carried through shared workflow/reference/template carriers plus runtime-specific Claude command wrappers where needed
- `dual-runtime-core` is active at the repo-self proof layer; the host matrix remains the manual release-readiness gate for broader host claims

## Bootstrap

Start with the same verification stack the Codex path uses:

```bash
./scripts/setup-portable-gsd-runtime.sh --runtime claude
python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')
python3 -m unittest discover -s tooling/codex/tests
```
