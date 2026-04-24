Date: 2026-04-22
Status: landed

# Harness Modifier In-Place Rehome Step 1 Implementation

## Purpose

- [g:r:i] Land the first filesystem carrier split for the later standalone harness-modifier project without widening into repo split, package distribution, or broader `.claude` materialization claims.

## Landed Shape

- [d:r:i] The authoritative generic helper home is now [harness_modifier/README.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/README.md:1).
- [d:r:i] The first rehomed carrier groups are:
  - `harness_modifier/contract/`
    - [portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/portable_gsd_contract.py:1)
    - [ensure_gsd_sdk_runtime.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/ensure_gsd_sdk_runtime.py:1)
    - [manifest_install_coherence.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/manifest_install_coherence.py:1)
    - [runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/runtime_visibility.py:1)
    - [harness_canary.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/contract/harness_canary.py:1)
  - `harness_modifier/capture/`
    - [run_claude_probe.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/capture/run_claude_probe.py:1)
    - [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/capture/capture_launch_truth.py:1)
    - [capture_runtime_visibility_snapshot.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/capture/capture_runtime_visibility_snapshot.py:1)
    - [extract_stream_text.py](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/capture/extract_stream_text.py:1)

## Explicit Boundary

- [d:r:i] The old `tooling/codex/*.py` paths for these moved helpers now remain only as thin compatibility shims.
- [d:r:i] Shared-boundary helpers still stay outside this first generic rehome:
  - [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:1)
  - [audit_refmap.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/audit_refmap.py:1)
  - [seed_migration_inventory.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/seed_migration_inventory.py:1)
- [d:r:i] Overlay-owned workflow / skill / template / reference carriers remain a later adjacent extraction step, not part of this first code-helper rehome.

## Propagation Follow-Through

- [d:r:i] The installer now calls the new authoritative contract helpers through [setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:1).
- [d:r:i] Active operator and doctrine surfaces now point at `harness_modifier` rather than at the old helper locations:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:62)
  - [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:90)
  - [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:75)
  - [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md:14)
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:1)
  - [tooling/portable-gsd/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/README.md:44)
  - [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:63)
- [d:r:i] Focused moved-helper tests now import from `harness_modifier`.

## Why This Shape

- [d:r:i] The slice creates a real filesystem and import boundary for a later standalone project without pretending the whole extraction problem is solved.
- [d:r:i] The importable underscore path keeps Python/package viability explicit now, while later repo/package branding remains reopenable.
- [d:r:i] Thin shims keep historical and held-boundary callers stable while the active authority moves to the new package.

## Held Later

- [d:r:i] compatibility declaration carrier
- [d:r:i] overlay/workflow/skill/template/reference rehome
- [d:r:i] standalone repo split
- [d:r:i] second-host exercise
- [d:r:i] npm/`npx` distribution
