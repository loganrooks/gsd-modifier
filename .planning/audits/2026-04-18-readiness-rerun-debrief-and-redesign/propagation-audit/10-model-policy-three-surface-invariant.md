Date: 2026-04-21
Status: active invariant note

# Model-Policy Three-Surface Invariant

## Purpose

- [g:r:i] This note makes explicit one invariant that lane-02 surfaced but `08` did not yet name directly.
- [g:r:i] When model-policy changes in this repo, three different surfaces must move in tune:
  - repo doctrine
  - installer-applied reasoning defaults
  - live agent registry files

## The Three Surfaces

- [e:c+i] Repo doctrine currently carries the preferred reasoning policy in root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:140): orchestration prefers `gpt-5.4` `xhigh`, execution/verification prefers `gpt-5.4` `high`, and early architecture-setting planning may also use `xhigh`.
- [e:c+i] Installer-applied defaults carry the repo-local reasoning map in `QUALITY_REASONING` inside [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:19), and `apply_reasoning_defaults` rewrites both `.codex/config.toml` and every tracked high-stakes agent `.toml` during install/materialization [e:c+i]. Sources: [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py:214), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:32).
- [e:c+i] Live agent registry truth is then carried in `.codex/agents/*.toml`, which `project_uplift.py` samples as runtime-registry carriers with `normalized_toml_hash` fingerprints [e:c+i]. Source: [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:312).

## Invariant

- [d:r:i] The invariant is:
  - doctrine says what the reasoning policy should be
  - `portable_gsd_contract.py` says how that policy materializes into runtime files
  - `.codex/config.toml` and `.codex/agents/*.toml` show the actually materialized registry truth
- [d:r:i] A policy change is under-carried if it moves only one or two of those three surfaces.

## Propagation Obligation

- [d:r:i] When repo model-policy changes:
  1. update doctrine in root/planning instruction surfaces
  2. update `QUALITY_REASONING` and any related installer reasoning defaults
  3. rerun repo-local materialization
  4. verify the live registry truth that results
- [d:r:i] The propagation family should treat this as a named invariant, not as a best-effort reminder.

## Current Consequence

- [d:r:i] The model-policy question is no longer only part of the broad runtime-registry row.
- [d:r:i] It is now an explicit three-surface invariant inside the propagation family.
