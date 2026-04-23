# Workflow

## Role

This file is the short operator workflow for developing `gsd-modifier` in its extracted repo.

## Default Sequence

1. read [AGENTS.md](AGENTS.md)
2. read [docs/development.md](docs/development.md)
3. read [docs/handoff/current.md](docs/handoff/current.md) for the active execution boundary and next move
4. read [docs/migration-origin.md](docs/migration-origin.md) when the current task touches extraction rationale, carried doctrine, or deferred strategy
5. make bounded changes
6. run the relevant verification stack
7. leave an auditable commit boundary

## Priority

- keep the repo self-sufficient
- keep install/materialization behavior portable
- keep development bootstrap clear for both Codex and Claude
- keep shipped/runtime and development-only surfaces distinguishable

## Current Boundary

- this is the first extracted repo cut
- internal path collapse can happen later
- first priority is correctness, portability, onboarding clarity, and passing checks in the extracted repo itself
