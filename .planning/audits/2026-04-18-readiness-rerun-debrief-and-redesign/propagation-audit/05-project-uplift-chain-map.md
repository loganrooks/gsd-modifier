Date: 2026-04-21
Status: landed chain-flow disclosure

# Project Uplift Chain Map

## Purpose

- [g:r:i] This note makes the current propagation route visible as a directed chain rather than only as a per-surface role table.
- [g:r:i] The target is not only to list surfaces. The target is to show where contract changes enter the chain, where they are consumed, and what kind of verification currently anchors each edge.

## Directed Flow

1. sampled doctrine/runtime carriers  
   `AGENTS.md`, `.planning/AGENTS.md`, `CLAUDE.md`, `.planning/CLAUDE.md`, `.planning/CLAIM-TYPES.md`, `.planning/LONG-ARC.md`, `tooling/codex/README.md`, `.codex/config.toml`, `.codex/agents/*.toml`, strengthening markers, active-phase `CONTEXT.md`

2. authoritative producer  
   [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)

3. structured bridge contract  
   `build_progress_note` JSON + detect/write output schema

4. direct consumers  
   - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
   - [progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
   - [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)

5. wrapper consumers  
   - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
   - [gsd-progress/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-progress/SKILL.md)
   - [gsd-resume-work/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-resume-work/SKILL.md)

6. durable outputs  
   - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
   - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
   - uplift section in [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
   - [UPLIFT-HELD-LATER.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/UPLIFT-HELD-LATER.md)

7. materialization bridge  
   [setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)

8. governance and discovery carriers  
   - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
   - [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
   - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md)
   - [propagation-audit/README.md](README.md)
   - [CURRENT-STATE.md](../CURRENT-STATE.md)

## Edge Map

| From | To | Current contract shape | Current verification shape |
|---|---|---|---|
| sampled carriers | `project_uplift.py` | carrier-specific fingerprints + typed proposal states | unit tests on classification, fingerprints, runtime agent globbing |
| `project_uplift.py` | `build_progress_note` JSON | shared producer-owned note shape | Route A test now anchors note keys against consumer prose |
| `build_progress_note` JSON | `progress.md` / `resume-project.md` | read-only `Uplift Posture` block, helper reuse, no reparsing | Route A test + manual workflow reread |
| direct workflows | wrapper skills | execution-context binding from skill to workflow | overlay ownership now keeps `gsd-progress` and `gsd-resume-work` in the tracked set |
| `project_uplift.py` detect/write | durable outputs | schema-versioned manifest + report + state section + typed held-later registry | unit tests + real repo write refresh |
| overlay tree | live `.codex` runtime | installer-backed materialization with `__PROJECT_ROOT__` substitution | `./scripts/setup-portable-gsd.sh` + live reread |
| current family state | governance/discovery carriers | doctrine pointer + worked-example routing + inventory disclosure | audit artifacts + governance reread |

## Edge Strength Labels

- [d:r:i] Strongest current edges:
  - sampled carriers -> helper
  - helper -> durable outputs
  - helper JSON -> `progress` / `resume-project`
- [d:r:i] Still partly manual edges:
  - overlay -> live materialization
  - consumer prose -> output labels
- [d:r:i] Newly strengthened ambient edges:
  - workflow -> skill binding for read-only consumers
  - held-later registry -> durable output memory
  - governance rule -> worked-example family

## Current Consequence

- [d:r:i] The propagation family now has both a role map (`02`) and a chain-flow map (`05`).
- [d:r:i] This makes later propagation work easier to route because the family no longer depends on only one disclosure shape.
