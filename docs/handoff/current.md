# Current Handoff

Date: 2026-04-23
Repo: `/home/rookslog/workspace/projects/gsd-modifier`
Branch: `main`
Head: `ba0236e`
Status: active standalone modifier repo

## Role

This is the current operator handoff for continuing `gsd-modifier` development after extraction from `prix-guesser`.

Use this file to re-enter the repo without depending on chat memory.

## What Is True Now

- migration is complete in the practical sense
- this repo is now the active home for modifier work
- `prix-guesser` is no longer the main execution home for modifier release-readiness work
- filtered history was preserved for the migrated project surface
- fresh bootstrap/onboarding/governance was added on top of that history
- the extracted repo is self-hosting and locally verifiable

## Governing Surfaces

Read in this order:

1. [AGENTS.md](../../AGENTS.md)
2. [WORKFLOW.md](../../WORKFLOW.md)
3. [docs/development.md](../development.md)
4. [docs/install-profiles.md](../install-profiles.md)
5. [docs/migration-origin.md](../migration-origin.md)

Historical carry:
- compact orientation: [docs/origin-audit/current-route.md](../origin-audit/current-route.md)
- historical archive: [docs/origin-audit/archive/README.md](../origin-audit/archive/README.md)

## Migration Boundary

Filtered history was carried for:
- `harness_modifier/`
- `tooling/codex/`
- `tooling/portable-gsd/overlay/`
- `scripts/setup-portable-gsd.sh`

Freshly created in this repo:
- root bootstrap docs
- root governance/operator docs
- `.planning/config.json`
- Codex and Claude onboarding docs
- carried origin-audit dossier and archive
- first standalone CI layer

Important consequence:
- the current internal layout is still transitional
- `tooling/portable-gsd/overlay/` and `harness_modifier/` remain one project even though they are not yet path-collapsed
- internal path collapse is later work, not a blocker on current development

## Current Runtime / Install Claim

Active profile:
- `codex-core`

Held later:
- `.claude` runtime-development widening
- mixed-runtime support
- broader optional install-profile matrix

Do not widen release or CI language beyond `codex-core` unless a later bounded widening slice is actually exercised and accepted.

## Latest Accepted Checkpoints

Migration/bootstrap:
- `86e9f1c` `bootstrap: make extracted repo self-hosting and auditable`

First standalone CI layer:
- `ba0236e` `ci: add first standalone verification gates`

Origin-side execution record:
- `prix-guesser` records the completed move at origin commit `156fca3`
- provenance summary is explained locally in [docs/migration-origin.md](../migration-origin.md)

## Verification Baseline

Canonical deterministic/package gate:

```bash
bash scripts/ci/check-deterministic.sh
```

Canonical bootstrap/integration gate:

```bash
bash scripts/ci/check-bootstrap.sh
```

Those currently cover:
- Python compile checks
- shell syntax checks for CI/bootstrap scripts
- deterministic unit subset
- full repo bootstrap via `./scripts/setup-portable-gsd.sh`
- full `tooling/codex/tests` suite
- overlay manifest validation
- materialized runtime verification
- local markdown refmap verification
- audit archive checksum verification
- `git diff --check`

Latest known result:
- both CI scripts passed locally at `ba0236e`
- full suite count: `147` tests passing

## Current Repo Shape

Runtime/shipped surfaces:
- `harness_modifier/`
- `tooling/portable-gsd/overlay/`
- `scripts/setup-portable-gsd.sh`

Development-support surfaces:
- `tooling/codex/`
- `tooling/codex/tests/`
- `.github/workflows/ci.yml`
- `scripts/ci/`

Historical carry:
- `docs/migration-origin.md`
- `docs/origin-audit/`

## Immediate Next Move

The next bounded release-readiness step should be the first host-fixture / canary deployment matrix.

That means:
- define the first 2-3 host shapes we actually want to support
- make those host shapes reproducible as fixtures, scripts, or packets
- use them as the next release-readiness gate before widening `.claude` or mixed-runtime claims

Recommended order:

1. codify first host-shape matrix
2. add reproducible host-exercise entrypoints
3. prove them locally
4. only then widen CI or release claims

## Explicitly Later

- `.claude` full materialization parity
- mixed-runtime claims
- richer optional install profiles
- internal path collapse / overlay rehome cleanup
- `modifier route vs own harness` strategy revisit

These are not forgotten. They are later because the current strongest carry comes from keeping the extracted repo stable, testable, and honest about what it actively supports.

## Resume Checklist

When resuming work:

1. confirm branch and head:
   - `git branch --show-current`
   - `git rev-parse --short HEAD`
2. re-read the governing surfaces above
3. run at least the deterministic gate if the work touches shipped or install-facing surfaces
4. run the bootstrap gate before closing any release-readiness boundary
5. leave a clean commit boundary

## Anti-Drift Rule

Do not let future work silently drift back into treating `prix-guesser` as the sovereign modifier workspace.

This repo is the modifier project now.
