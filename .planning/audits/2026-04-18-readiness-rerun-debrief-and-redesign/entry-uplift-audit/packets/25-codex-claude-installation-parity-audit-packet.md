Date: 2026-04-22
Status: active packet

# Codex Claude Installation Parity Audit Packet

## Purpose

- [g:r:i] This packet opens the bounded `.codex` / `.claude` installation-parity audit immediately after the landed `update + gsd-update` continuity consumer slice.
- [g:r:i] The target is not general multi-provider parity and not abstract wording cleanup.
- [g:r:i] The target is narrower:
  - what upstream already separates explicitly between Codex and Claude at install/materialization time
  - where this repo-local modifier layer stays in tune with that split
  - where the repo-local layer still blurs runtime-specific responsibilities, references, or install shapes
  - which surfaced `.claude` hits are real current defects versus contextual warnings inside runtime-detection or installer examples

## Read Order

### Opening Note And Recent Local Carry

1. [intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md](../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md)
2. [intervention-proposals/133-update-entry-runtime-continuity-follow-through-implementation.md](../../intervention-proposals/133-update-entry-runtime-continuity-follow-through-implementation.md)
3. [propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md](../../propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md)

### Repo-Local Installer And Materialization Layer

4. [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
5. [tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py)
6. [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)

### Repo-Local Runtime-Specific Consumer Surfaces

7. [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md)
8. [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md)
9. [.codex/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/update.md)
10. [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml)
11. [.codex/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml)

### Upstream Runtime-Specific Install Frontier

12. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md:110)
13. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:331)
14. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4104)
15. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4204)
16. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4339)
17. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4394)
18. [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4446)

### Governing Context

19. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
20. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
21. [CURRENT-STATE.md](../../CURRENT-STATE.md)

## What The Audit Should Be Able To Judge

- [d:r:i] What upstream already makes runtime-specific across `.codex` and `.claude`.
- [d:r:i] Which repo-local surfaces currently stay aligned with that upstream split.
- [d:r:i] Which repo-local surfaces still blur:
  - install shape
  - commands versus skills
  - agent conversion/config
  - hooks/runtime config
  - provider-specific reference wording
  - live materialization versus overlay source of truth
- [d:r:i] Which currently surfaced `.claude` references inside repo-local install/update surfaces are:
  - real current defects
  - contextual warnings inside runtime-detection/examples
  - later-family improvement pressure
- [d:r:i] What the sharpest next bounded parity slice should be after this audit.
