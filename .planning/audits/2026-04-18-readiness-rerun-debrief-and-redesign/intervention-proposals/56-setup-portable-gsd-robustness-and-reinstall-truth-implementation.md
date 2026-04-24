Date: 2026-04-21
Status: landed bounded implementation

# Setup Portable GSD Robustness And Reinstall Truth Implementation

## Purpose

- [g:r:i] This note records the bounded setup/reinstall robustness slice opened in `55`.
- [g:r:i] The slice makes the repo-local setup path more durable without blurring the difference between:
  - upstream install behavior
  - repo-local runtime repair
  - repo-local overlay/materialization contract

## What Landed

- [e:r:i] The repo now has a bounded `gsd-sdk` runtime helper:
  - [tooling/codex/ensure_gsd_sdk_runtime.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/ensure_gsd_sdk_runtime.py)
  - [tooling/codex/tests/test_ensure_gsd_sdk_runtime.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_ensure_gsd_sdk_runtime.py)
- [e:r:i] The helper:
  - verifies `command -v gsd-sdk` under `/bin/sh`
  - verifies `gsd-sdk --version` under `/bin/sh`
  - repairs the known executable-bit failure only when the discovered launcher target exists, carries a shebang, and lost readable/executable mode
  - leaves true off-PATH and broader install failures unresolved
- [e:r:i] The shared portable contract now carries a fresh-install pristine overwrite capture stage:
  - [tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py)
  - [tooling/codex/tests/test_portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_portable_gsd_contract.py)
- [e:r:i] That stage writes repo-local pristine overwrite copies from the fresh live `.codex/` frontier plus `.codex/gsd-file-manifest.json` before overlay application, then keeps the later strict overwrite/materialization checks intact.
- [e:r:i] The wrapper now routes through the new bounded stages:
  - [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
  - recoverable upstream exit `2` is allowed to proceed to repo-local runtime verification
  - fresh-install pristine overwrite capture now precedes strict manifest validation

## Proof

- [e:r:i] Direct local helper proof succeeded after intentionally degrading the real `gsd-sdk` launcher target from `0o755` to `0o600`.
- [e:r:i] The helper returned `status: repaired`, restored the real target to `0o755`, and re-established both `/bin/sh` command discovery and `/bin/sh` execution.
- [e:r:i] Fresh isolated-worktree proof also succeeded:
  - a throwaway worktree at `/tmp/prix-setup-verify-l5j289` was reset to a fresh-install shape
  - `./scripts/setup-portable-gsd.sh` completed there after:
    - upstream local install
    - repo-local `gsd-sdk` runtime verification
    - synthetic pristine overwrite capture
    - strict manifest validation
    - overlay application
    - reasoning-default application
    - strict post-materialization verification
- [e:r:i] That isolated proof surfaced and then closed a second real fragility:
  - fresh upstream installs no longer produced `gsd-local-patches/backup-meta.json`
  - the landed pristine-capture stage now supplies the strict overwrite baseline locally instead of weakening overwrite discipline

## Verification

- [e:r:i] Passed:
  - `python3 -m py_compile tooling/codex/portable_gsd_contract.py tooling/codex/ensure_gsd_sdk_runtime.py`
  - `python3 -m unittest tooling.codex.tests.test_portable_gsd_contract tooling.codex.tests.test_ensure_gsd_sdk_runtime tooling.codex.tests.test_project_uplift`
  - `bash -n scripts/setup-portable-gsd.sh`
  - isolated-worktree `./scripts/setup-portable-gsd.sh`
- [e:r:i] Later final batch gates remain required at commit boundary:
  - `portable_gsd_contract.py validate-manifest --strict`
  - `portable_gsd_contract.py verify-materialized --strict`
  - `harness_canary.py report --strict`
  - `audit_refmap.py verify`
  - `git diff --check`

## Current Consequence

- [d:r:i] Repo-local reinstall truth is now less brittle in two concrete ways:
  - the bounded `gsd-sdk` executable-bit failure no longer masquerades as an unexamined PATH mystery
  - strict overwrite ownership no longer depends on upstream leaving backup copies behind
- [d:r:i] The setup path is still not treated as closed or ceiling-state.
- [d:r:i] Later pressure remains on:
  - repeated reinstall durability across more runtime states
  - broader updater/frontier movement
  - later compatibility-window carry beyond the observed-basis anchor
