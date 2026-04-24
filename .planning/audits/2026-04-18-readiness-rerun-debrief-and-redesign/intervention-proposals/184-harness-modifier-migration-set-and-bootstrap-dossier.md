Date: 2026-04-23
Status: completed execution dossier

# Harness Modifier Migration-Set And Bootstrap Dossier

## Role

- [d:r:i] This dossier turns the locked route in `183` into an execution-ready migration set.
- [g:r:i] It fixes what moves with filtered history, what is recreated fresh, and what origin-audit carry should travel into the extracted repo.

## Execution Decision

- [d:r:i] Create `~/workspace/projects/gsd-modifier` from filtered history over the modifier-owned executable and development-support surface, not only the narrow shipped runtime surface.
- [d:r:i] The wider development-support carry is earned because the extracted repo must be immediately usable for:
  - modifier development
  - local verification
  - audit/review continuity
  - Codex/Claude onboarding
- [g:r:i] This still does not mean migrating the entire host-project audit corpus with history.

## Move With Filtered History

- [d:r:i] `harness_modifier/`
  - package-owned modifier carriers and helpers
- [d:r:i] `tooling/portable-gsd/overlay/`
  - live overlay/install-materialization contract and payload
- [d:r:i] `scripts/setup-portable-gsd.sh`
  - installer entrypoint
- [d:r:i] `tooling/codex/`
  - current development-support and compatibility-helper surface required by the migrated tests, overlay contracts, launch/review helpers, and audit continuity

## Why `tooling/codex/` Travels

- [d:r:i] A narrower filtered set would leave the extracted repo with broken or hollow development posture because:
  - the current tests import `tooling.codex.*`
  - helper shims and route contracts still point into that tree
  - the harness-development audit/review loop still uses selected helpers there
- [d:r:i] The extracted repo can still classify `tooling/codex/` internally into:
  - product/runtime support
  - development-program-only tooling
  - transitional compatibility shims
- [g:r:i] That internal classification can sharpen later without blocking migration now.

## Recreate Fresh In The Extracted Repo

- [d:r:i] Root bootstrap/governance surfaces should be recreated fresh rather than history-filtered from `prix-guesser`:
  - `README.md`
  - `AGENTS.md`
  - `WORKFLOW.md`
  - `.gitignore`
  - `docs/onboarding/codex.md`
  - `docs/onboarding/claude.md`
  - `docs/development.md`
  - `docs/migration-origin.md`
- [d:r:i] A minimal fresh modifier-owned planning/governance surface should also be created:
  - `.planning/README.md`
  - `.planning/CURRENT-STATE.md`
  - `.planning/STATUS.md`

## Origin-Audit Carry

- [d:r:i] The current audit family should travel into the new repo, but not as wholesale filtered-history carry.
- [d:r:i] The correct shape is a carried origin dossier / snapshot for the harness-modifier development program.
- [d:r:i] The first carried dossier should include:
  - `177`
  - `180`
  - `181`
  - `182`
  - `183`
  - this dossier `184`
  - `.planning/HARNESS-IMPROVEMENT-REGISTER.md`
  - the current `responsible-closure-audit/README.md`
- [d:r:i] Those should travel as a fresh snapshot under a modifier-owned archive location, not as the entire mixed host-project `.planning/audits/...` tree with rewritten history.
- [d:r:i] That satisfies the requirement that the live audit work not be dropped while keeping the extracted repo from inheriting the whole host-project planning identity.

## First Extracted-Repo Shape

- [d:r:i] Preserve the current internal path layout for the first migration cut so the extracted repo remains executable and testable immediately.
- [d:r:i] This means the first cut still contains:
  - `harness_modifier/`
  - `tooling/codex/`
  - `tooling/portable-gsd/overlay/`
  - `scripts/`
- [d:r:i] The repo is still one project even if that internal transitional split remains for the first cut.
- [d:r:i] Internal path collapse can happen later as a dedicated follow-through slice once the extracted repo itself is stable and verified.

## Verification Target In The Extracted Repo

- [d:r:i] First migration verification should include:
  - `python3 -m py_compile` across migrated helper trees
  - focused or full `python3 -m unittest` across migrated `tooling/codex/tests`
  - `./scripts/setup-portable-gsd.sh`
  - `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest`
  - `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict`
  - `python3 tooling/codex/audit_refmap.py verify` on the migrated modifier-owned governance/audit surface
  - `git diff --check`

## Deliberate Boundary

- [g:r:i] This dossier does not say the first extracted repo is the final perfect internal taxonomy.
- [g:r:i] It says the first extracted repo should be executable, auditable, and development-ready on day one.

## Exact Next Move

1. [d:r:i] Create `~/workspace/projects/gsd-modifier` from the filtered path set above.
2. [d:r:i] Add the fresh bootstrap/governance surfaces and carried origin-audit dossier.
3. [d:r:i] Run the extracted-repo verification stack and repair migration breakage until it passes.
