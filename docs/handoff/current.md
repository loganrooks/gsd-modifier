# Current Handoff

Date: 2026-04-23
Repo: `/home/rookslog/workspace/projects/gsd-modifier`
Branch: `main`
Head baseline: `ba0236e`
Status: active standalone modifier repo with dual-runtime-core promotion in the live worktree

## Role

This is the current operator handoff for continuing `gsd-modifier` development after extraction from `prix-guesser`.

Use this file to re-enter the repo without depending on chat memory.

## What Is True Now

- migration is complete in the practical sense
- this repo is now the active home for modifier work
- the extracted repo is self-hosting and locally verifiable
- `codex-core`, `claude-core`, and `dual-runtime-core` are the active repo-self proof profiles
- `.planning/` remains the shared runtime-neutral project canon
- the synthetic host matrix now covers Codex-only and dual-runtime read-side, aligned, and conflict cases

## Governing Surfaces

Read in this order:

1. [AGENTS.md](../../AGENTS.md) — runtime-neutral governance
2. [CLAUDE.md](../../CLAUDE.md) — Claude-side carrier (points back to AGENTS.md for the rules)
3. [WORKFLOW.md](../../WORKFLOW.md)
4. [docs/development.md](../development.md)
5. [docs/install-profiles.md](../install-profiles.md)
6. [docs/host-exercise-matrix.md](../host-exercise-matrix.md)

Historical carry:
- compact orientation: [docs/origin-audit/current-route.md](../origin-audit/current-route.md)
- historical archive: [docs/origin-audit/archive/README.md](../origin-audit/archive/README.md)

## Current Runtime / Install Claim

Active core profiles:
- `codex-core`
- `claude-core`
- `dual-runtime-core`

Repo-self proof is now carried by:
- `./scripts/setup-portable-gsd-runtime.sh --runtime both`
- `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict`
- `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict`
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict`

The synthetic host matrix remains a manual release-readiness gate for broader host-language changes:
- [docs/host-exercise-matrix.md](../host-exercise-matrix.md)
- [matrix-summary.json](../../.planning/measurement/host-exercise-matrix/matrix-summary.json)

## Verification Baseline

Canonical deterministic/package gate:

```bash
bash scripts/ci/check-deterministic.sh
```

Canonical bootstrap/integration gate:

```bash
bash scripts/ci/check-bootstrap.sh
```

Manual host-proof gate:

```bash
python3 harness_modifier/closure/host_exercise_matrix.py . \
  --profile all \
  --output-dir .planning/measurement/host-exercise-matrix \
  --strict
```

Latest known local result:
- `bash scripts/ci/check-deterministic.sh` passed
- `bash scripts/ci/check-bootstrap.sh` passed
- `.planning/measurement/host-exercise-matrix/matrix-summary.json` is currently `status: ok` across all six synthetic scenarios

## Current Repo Shape

Runtime/shipped surfaces:
- `harness_modifier/`
- `tooling/portable-gsd/overlay/`
- `scripts/setup-portable-gsd.sh`
- `scripts/setup-portable-gsd-runtime.sh`

Development-support surfaces:
- `tooling/codex/`
- `tooling/codex/tests/`
- `.github/workflows/ci.yml`
- `scripts/ci/`

Historical carry:
- `docs/migration-origin.md`
- `docs/origin-audit/`

## Immediate Next Move

The next bounded release-readiness step is to widen host proof beyond the current synthetic matrix without reopening the parity architecture.

That means:
- keep the repo-self dual-runtime proof green
- extend the host matrix beyond the current synthetic aligned/read-side/conflict shapes
- start testing more realistic mixed-runtime host conditions and compatibility-drift cases

## Explicitly Later

- semantic merge tolerance for changed runtime-specific wrappers
- upstream-template drift compatibility beyond exact declared carriers
- richer optional install profiles beyond the current core contract
- internal path collapse / overlay rehome cleanup
- `modifier route vs own harness` strategy revisit

## Resume Checklist

When resuming work:

1. confirm branch and head:
   - `git branch --show-current`
   - `git rev-parse --short HEAD`
2. re-read the governing surfaces above
3. run at least the deterministic gate if the work touches shipped or install-facing surfaces
4. run the bootstrap gate before closing any repo-self proof boundary
5. rerun the host matrix if the work changes mixed-runtime host claims or host-proof semantics
6. leave a clean commit boundary

## Anti-Drift Rule

Do not let future work silently drift back into treating `prix-guesser` as the sovereign modifier workspace.

This repo is the modifier project now.
