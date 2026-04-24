Date: 2026-04-22
Status: landed first packet exercise

# Uplift Cross-Runtime Comparison First Exercise Packet

## Packet Header

- Trigger: `111` plus the current durable uplift memory after the docs-governance runtime-proof refresh
- Exact comparison question: given the current observed-basis-only uplift posture, what is the current shared basis and divergence between `.codex` and `.claude`, especially around governance wrappers and the repo-local uplift/propagation routes, and what should stay held before any cross-runtime composition judgment?
- Runtime for packet consumption: parent-thread first exercise
- Explicit write boundary: bounded comparison note and parent-thread disposition only
- Expected disposition home: `entry-uplift-audit/dispositions/`

## Input Packet

### Detect Summary

- [e:c+i] Current durable uplift memory classifies the repo as `cross-runtime uplift`, records `.codex` and `.claude` as the present runtime directories, keeps ordinary routing as the current recommendation, and keeps wider cross-runtime compatibility claims held for later. Sources:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:5)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:13)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:25)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:39)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:5)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:19)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:78)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:96)
- [e:c+i] The same uplift memory still keeps `cross-runtime uplift composition` as a held-later family rather than a settled route. Source: [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:33)

### Governance And Wrapper Carriers Under Comparison

- [e:c+i] Root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) remains the vendor-neutral doctrine carrier for this repo, and it explicitly keeps repo-local harness work tied to `.codex/get-shit-done`, propagation follow-through, and layered reading packets. Sources:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:5)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:41)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:57)
- [e:c+i] Root [CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/CLAUDE.md) is still a thin cross-vendor wrapper that routes Claude work back to `AGENTS.md` rather than acting as a second canon. Sources:
  - [CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/CLAUDE.md:3)
  - [CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/CLAUDE.md:5)
  - [CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/CLAUDE.md:18)
- [e:c+i] [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md) does the same planning-local routing toward `.planning/AGENTS.md`. Sources:
  - [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md:3)
  - [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md:7)
  - [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md:12)

### Bounded Runtime Evidence Bundle

- [e:c+i] The observed compatibility basis still belongs to `.codex`: uplift memory records `1.38.3` for both runtime version and runtime manifest version. Sources:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:25)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:27)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:80)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:82)
  - [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION:1)
- [e:b:i] A bounded runtime reread on 2026-04-22 shows `.claude/get-shit-done/VERSION` at `1.34.2` and `.claude/gsd-file-manifest.json` at `1.34.2`, so the present co-runtime topology is version-divergent even before any route-level comparison.
- [e:c+i] The live Codex uplift route already keeps assist-family packet work operator-initiated and points it back to the assist-family references rather than auto-spawning or mutating runtime state. Source: [.codex/get-shit-done/workflows/uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/uplift-project.md:104)
- [e:b:i] The same bounded runtime reread shows route asymmetry:
  - `.codex` carries repo-local `uplift-project`, `propagation-review`, and `seed-migration-inventory` workflows plus their skill wrappers
  - `.claude` currently exposes `progress` and `resume-project`, but not direct `.claude` workflow or command counterparts for those three repo-local routes

## Explicit Exclusions

- [d:r:i] This packet does not authorize:
  - live `.claude` translation work
  - runtime mutation
  - compatibility-matrix claims
  - cross-runtime composition judgment
  - propagation-registry refresh folded into the packet itself
