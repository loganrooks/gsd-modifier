Date: 2026-04-22
Status: landed first-slice implementation

# Codex Claude Parity Classification Carrier Implementation

## What Landed

- [d:r:i] `portable_gsd_contract.py` now emits a typed `runtime_specific_reference_scan` inside `build_materialization_report`.
- [d:r:i] The report:
  - scans live `.codex/` `.md` and `.toml` files with the same `.claude` path pattern the upstream warning uses
  - preserves the current known baseline explicitly
  - classifies those baseline hits by context and ownership
  - marks non-baseline hits as `needs contextual reread`
- [d:r:i] Focused tests now freeze both:
  - the known three-hit baseline
  - the unreviewed-hit route that widens attention without pretending to settle the hit automatically
- [d:r:i] Tooling documentation now names the new report and keeps contextual reread sovereign over the helper output.

## What The Slice Deliberately Did Not Do

- [d:r:i] It did not widen into `.claude` installation or runtime-aware dispatch.
- [d:r:i] It did not convert comment-example quieting into a hidden success condition.
- [d:r:i] It did not make unreviewed hits fail `verify-materialized --strict`.
- [d:r:i] It did not claim the helper can infer active-pointer defects without contextual reread.

## Verification Carry

- [d:r:i] Focused coverage now lives in:
  - [tooling/codex/tests/test_portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_portable_gsd_contract.py)
- [d:r:i] The proof points are:
  - known baseline hit classification remains stable
  - unreviewed hits stay visibly separate
  - current strict materialization verification remains compatible with the new report

## Propagation Consequence

- [d:r:i] The parity branch is no longer only:
  - lane `19` output
  - lane `19` inheritance
- [d:r:i] It now also has a live contract carrier plus a propagation refresh:
  - [../propagation-audit/50-codex-claude-parity-classification-carrier-change-triggered-refresh.md](../propagation-audit/50-codex-claude-parity-classification-carrier-change-triggered-refresh.md)

## Next Adjacent Route

- [d:r:i] Keep this classified report exercised across later real materialization boundaries before reopening larger `.claude` carrier or install branching questions.
- [d:r:i] Keep `from-gsd2` as the next adjacent consumer inside the separate uplift-continuity chain.
