Date: 2026-04-21
Status: accepted bounded proposal

# Setup Portable GSD Robustness And Reinstall Truth Proposal

## Purpose

- [g:r:i] This proposal opens the bounded robustness family already carried in `.planning/HARNESS-IMPROVEMENT-REGISTER.md`: make the repo-local setup/reinstall path more durable without pretending we control upstream install semantics.
- [g:r:i] The target is not a broad installer rewrite. The target is the concrete repo-local path through `scripts/setup-portable-gsd.sh`, `portable_gsd_contract.py`, and the observed `gsd-sdk` launcher/runtime boundary.

## Trigger

- [e:r:i] The landed verifier-lifecycle slice preserved one still-live fragility instead of hiding it: direct local `./scripts/setup-portable-gsd.sh` reruns were not yet a dependable restore path.
- [e:r:i] Narrow investigation established two concrete failure sources:
  - upstream local install can emit a misleading `gsd-sdk` PATH banner when the real problem is a non-executable shebang target behind `/home/rookslog/.npm-global/bin/gsd-sdk`
  - fresh upstream installs no longer leave `gsd-local-patches/backup-meta.json` behind, while the local overwrite contract still expects pristine overwrite copies before overlay application

## Bounded First Slice

- [d:r:i] Add one narrow helper for repo-local `gsd-sdk` runtime verification and bounded repair:
  - verify `command -v gsd-sdk` and `gsd-sdk --version` under `/bin/sh`
  - if the discovered launcher target exists, has a shebang, and only lost execute bits, restore readable/executable mode
  - keep real off-PATH and broader install failures visible instead of muting them
- [d:r:i] Add one narrow pristine-capture stage inside the shared portable contract helper:
  - after upstream local install and before overlay application
  - synthesize repo-local pristine overwrite copies from the fresh live `.codex/` frontier plus `gsd-file-manifest.json`
  - keep strict overwrite ownership intact rather than weakening validation
- [d:r:i] Route the wrapper through those two new bounded stages before overlay application, then keep the existing strict overlay/materialization verification path.

## Verification Gates

- [d:r:i] Unit coverage for:
  - healthy `gsd-sdk` runtime
  - non-executable shebang-target repair
  - unresolved no-candidate case
  - synthetic pristine overwrite capture from a fresh live `.codex/` frontier
- [d:r:i] Direct helper proof on the real local `gsd-sdk` target after a temporary permission downgrade.
- [d:r:i] Fresh isolated worktree proof of the full `./scripts/setup-portable-gsd.sh` path after the wrapper and contract changes land.
- [d:r:i] Keep existing strict gates:
  - `portable_gsd_contract.py validate-manifest --strict`
  - `portable_gsd_contract.py verify-materialized --strict`
  - `harness_canary.py report --strict`
  - `audit_refmap.py verify`
  - `git diff --check`

## Held Later

- [d:r:i] This slice does not claim upstream installer control.
- [d:r:i] This slice does not widen into version-window compatibility policy, cross-runtime reconciliation, or broader updater-template drift handling.
- [d:r:i] This slice does not replace the existing strict overlay/materialization contract; it makes the repo-local entry path answer back to it more durably.
