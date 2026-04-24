Date: 2026-04-23
Status: completed locked route

# Harness Modifier Filtered-History, Bootstrap, And Onboarding Route

## Role

- [d:r:i] This note locks the currently recommended extraction/migration route after `177`, `180`, `181`, and `182`.
- [g:r:i] It is not the execution of migration yet.
- [g:r:i] It is the governing answer for how migration should happen once the first extraction execution tranche opens.

## Chosen Route

- [d:r:i] Use a filtered-history extraction route, not a full `prix-guesser` repo-history copy.
- [d:r:i] The later standalone project should be bootstrapped as one modifier-owned project that carries:
  - modifier package code
  - live overlay/install-materialization contract
  - installer entrypoints
  - product-owned tests, fixtures, and docs
  - fresh modifier-owned onboarding/governance surfaces for continued development
- [d:r:i] Do not extract `harness_modifier/` alone.
- [d:r:i] Do not lead with CI before the extracted repo exists and is usable for Codex and Claude development.

## Why This Route Wins

- [d:r:i] Full repo-history carry would drag large amounts of unrelated `prix-guesser` product history into the standalone modifier project.
- [d:r:i] Package-only extraction would repeat the current transitional split between package authority and live install/materialization authority.
- [d:r:i] Copying the current full audit/governance tree into the new repo would keep host-project and harness-program horizons entangled instead of clarifying them.
- [d:r:i] The stronger route is therefore:
  - preserve product-history where the modifier actually lived
  - preserve install/materialization history where the live contract actually lived
  - rebuild modifier-owned development onboarding/governance cleanly in the new repo instead of replaying the entire current mixed host-project audit corpus there

## History-Preservation Decision

- [d:r:i] Preserve filtered history for modifier-product surfaces.
- [d:r:i] Do not preserve full `prix-guesser` history in the new repo.
- [d:r:i] Use `git filter-repo` as the primary history-carry mechanism because the migration set spans multiple path families and historical authority moved across them over time.
- [d:r:i] Treat `git subtree split` as the fallback only if the eventual migration set collapses to one much narrower path family, which current evidence does not support.

## Product-History Carry Boundary

- [d:r:i] The mandatory first migration-set rows are:
  - `harness_modifier/`
  - `tooling/portable-gsd/overlay/`
  - `scripts/setup-portable-gsd.sh`
- [d:r:i] The next migration-set rows should include only product-owned or runtime-support files that are still materially part of the shipped/install contract:
  - selected tests for migrated helpers and runtime/install behavior
  - selected helper bridges still required by the classified shipped/install surface
  - selected product docs/readiness surfaces that explain shipped behavior or developer setup for the modifier project itself
- [g:r:i] Do not migrate the broad `tooling/codex/` tree by default.
- [d:r:i] Only move specific `tooling/codex/*` entries if the shipped/install classification and current live invocation path still show them as modifier-owned transitional support rather than repo-local development tooling.

## Development-Governance Carry Decision

- [d:r:i] The new repo should not inherit the current `.planning/audits/...` tree wholesale.
- [d:r:i] The current audit corpus remains the origin archive inside `prix-guesser`.
- [d:r:i] The extracted repo should instead start with a fresh modifier-owned development/governance bootstrap that carries forward the sharpened doctrine without reimporting the entire mixed host-project trace.
- [d:r:i] The carried-forward bootstrap should include:
  - root `README.md`
  - root `AGENTS.md`
  - root `WORKFLOW.md`
  - modifier-development onboarding docs
  - a fresh modifier-specific `.planning/` bootstrap or equivalent governed planning surface
  - one compact migration/origin dossier that summarizes where the project came from and what source archive still holds the deeper trail

## First Extracted-Repo Layout

- [d:r:i] The first extracted repo should be shaped as one project with clearly separated product strata:
  - `harness_modifier/`
    - Python/control-plane/package-owned helpers and carriers
  - `overlay/`
    - live installable runtime payload plus `OVERLAY-MANIFEST.json`
  - `scripts/`
    - installer entrypoints and bounded setup helpers
  - `tests/`
    - migrated product-owned tests
  - `fixtures/`
    - synthetic host fixtures and later install/materialization smoke harnesses
  - `docs/`
    - product docs, developer onboarding, migration/origin dossier, release/readiness notes
- [g:r:i] Do not keep the future extracted project split across `harness_modifier/` and `tooling/portable-gsd/overlay/` the way the host repo currently is.
- [d:r:i] The current split is transitional and should collapse in the extracted repo.

## Codex And Claude Day-One Onboarding Requirement

- [g:r:i] The extracted repo is not ready for development relocation unless both Codex and Claude can enter it cleanly without reconstructing the project model from chat memory.
- [d:r:i] Day-one onboarding in the extracted repo should include:
  - repo purpose and audience split
  - what ships versus what is development-only
  - how local install/materialization testing works
  - canonical verify/test commands
  - where modifier-owned governance lives
  - how to dogfood the modifier locally against fixture or host repos
  - what the current compatibility posture is for `.codex` and `.claude`
- [d:r:i] The minimum day-one files should be:
  - `README.md`
  - `AGENTS.md`
  - `WORKFLOW.md`
  - `docs/onboarding/codex.md`
  - `docs/onboarding/claude.md`
  - `docs/development.md`
  - `docs/migration-origin.md`

## CI Sequencing Consequence

- [d:r:i] CI is still required.
- [d:r:i] It is not the lead move.
- [d:r:i] The correct order is:
  1. lock extracted-project boundary
  2. freeze migration-set manifest
  3. create the extracted repo
  4. land day-one onboarding/bootstrap there
  5. then add first deterministic CI there
  6. later add slower integration/materialization smoke
  7. later still add packaging/release checks

## Migration Risk Controls

- [d:r:i] Use a fresh filtered clone or mirror, not the main working tree, when constructing the extracted repo history.
- [d:r:i] Freeze the migration-set manifest before running `git filter-repo`.
- [d:r:i] Expect commit SHAs to change in the new repo.
- [d:r:i] Do not copy existing tags blindly into the new repo.
- [d:r:i] Keep a provenance note that explains:
  - origin repo
  - filtered-history method
  - migration-set boundary
  - what was intentionally left behind
- [d:r:i] Keep the current host repo as the provenance archive for mixed host-project plus modifier-program audit history rather than trying to make the new repo carry both identities at once.

## What Stays Behind

- [d:r:i] `prix-guesser` product-planning surfaces stay behind.
- [d:r:i] Mixed host-project audit history stays behind as the origin archive.
- [d:r:i] Repo-local development tooling that is not part of the modifier shipped/install contract stays behind unless a later explicit classification moves it.
- [d:r:i] `.planning/measurement/` stays outside the migration route unless later governed explicitly.

## Deliberate Boundaries

- [g:r:i] This route does not yet execute `git filter-repo`.
- [g:r:i] This route does not yet create `~/workspace/projects/gsd-modifier`.
- [g:r:i] This route does not yet settle install-profile implementation.
- [g:r:i] This route does not reopen `modifier route versus own harness`.
- [g:r:i] This route does not widen `.claude` runtime claims beyond the current parity posture.

## Exact Next Move

1. [d:r:i] Cut one bounded migration-set and bootstrap dossier artifact from this route:
   - exact filtered path manifest
   - explicit moved-with-history versus recreated-fresh bootstrap surfaces
   - first extracted-repo top-level tree
2. [d:r:i] Only after that, open the actual extracted-repo creation tranche.
3. [d:r:i] Only after the extracted repo exists with day-one onboarding, cut the first CI implementation slice there.
