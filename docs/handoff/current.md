# Current Handoff

Date: 2026-05-16
Repo: `/home/rookslog/workspace/projects/gsd-modifier`
Branch: `main`
Head baseline: `979a525` (Phase 1 boundary commit; subsequent operator-approval commits land on top)
Status: active standalone modifier repo; **inject-migration initiative is the live workstream** (Phases 0+1 closed 2026-05-16; Phase 2 contract tools cleared to start after operator approval of ADR-001)

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
- **inject-migration initiative is the active workstream** (state at `.planning/initiatives/inject-migration/STATE.md`):
  - Phase 0 (surface cleanup) closed 2026-05-16T00:22:40Z — 4 stale-overwrite carriers reclassified to `mode: add`; change-class trigger taxonomy added to AGENTS.md/CLAUDE.md
  - Phase 1 (schema foundation) closed 2026-05-16T01:09:41Z — ADR-001 manifest schema v4 (`mode: inject`) approved by operator 2026-05-16T01:53Z
  - Phase 2 (contract tools) cleared to start; OOS #3 (installer-block) means Phase 2 verification is unit-test-only; bootstrap-chain remains BLOCKED and out of scope for Phase 2

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

The active priority is the **inject-migration initiative** at `.planning/initiatives/inject-migration/`. Phase 2 (contract tools) is cleared to start: implement validate/apply/extract/verify functions in `harness_modifier/contract/` for `mode: inject` per ADR-001, with per-slice unit tests on synthetic content.

To enter Phase 2:
- read `.planning/initiatives/inject-migration/STATE.md` for current sentinel
- read `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md` for the schema being implemented
- read `.planning/initiatives/inject-migration/phases/02-contract-tools.md` for the slice plan (note the "Note on OOS #3" subsection scoping verification to unit tests)
- invoke `/goal` to re-fire the autonomous loop, OR execute slices manually per `.planning/initiatives/inject-migration/PROTOCOL.md`

Deferred to a separate workstream (was the prior priority pre-inject-migration):
- widen host proof beyond the current synthetic matrix
- resolve OOS #3 (upstream installer hooks-classification block) — needed before inject-migration Phase 3 (pilot) can attempt end-to-end materialization

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
