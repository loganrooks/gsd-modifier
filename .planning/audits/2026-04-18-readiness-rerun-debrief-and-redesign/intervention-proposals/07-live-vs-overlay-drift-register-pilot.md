Date: 2026-04-20
Status: draft pilot register

# Live Vs Overlay Drift Register Pilot

## Purpose

- [g:r:i] This pilot turns the second-tranche drift question into a discriminating register instead of a generic `overlay differs from live` complaint.
- [d:r:i] The target is not to erase all difference. The target is to classify what kind of difference the repo is actually carrying, so later persistence and manifest work can act on a stronger baseline.

## Pilot Scope

- [d:r:i] This pilot samples the load-bearing families already named in the proposal set:
  - `.codex/config.toml`
  - the high-stakes agent `.toml` cohort
  - selected workflow/reference surfaces
  - one out-of-cohort agent sample

## Classification Scheme

- [d:r:i] The earlier proposal’s four classes were close but still too coarse for the actual surface. This pilot keeps those pressures while making one missing distinction explicit.

| Class | Meaning |
| --- | --- |
| `intentional materialized carry` | overlay is templated or partial by design, and live runtime differs because install/materialization makes it concrete |
| `repo-local config carry` | live runtime intentionally carries repo-specific defaults or settings beyond generic overlay template values |
| `selective overlay boundary` | live runtime contains more surfaces than the tracked overlay subset currently claims; this is a boundary/coverage issue, not yet evidence of bad drift |
| `unknown live drift` | live behavior differs and the reason is not yet legible from current carry/materialization logic |
| `obsolete live residue` | live difference persists without a current carry reason and should likely be removed or reabsorbed |

## Register

| Surface | Current class | Why |
| --- | --- | --- |
| `.codex/config.toml` vs `overlay/config.toml` | `intentional materialized carry` + `repo-local config carry` | overlay keeps template placeholders and generic defaults, while live config carries absolute materialized agent paths plus repo-local defaults like `xhigh` base reasoning and the project compact prompt [e:c+i] |
| high-stakes agent cohort (`gsd-planner`, `gsd-plan-checker`, `gsd-executor`, `gsd-verifier`) | `intentional materialized carry` | after the first tranche, live and overlay now carry the same repo-quality posture; remaining difference is the expected template-to-materialized path substitution [e:c+i] |
| sampled workflow surfaces (`plan-phase.md`, `discuss-phase.md`) | `intentional materialized carry` | sampled diffs show `__PROJECT_ROOT__` template references becoming absolute repo-local paths in live runtime, not a distinct semantic branch [e:c+i] |
| sampled reference surface (`planning-config.md`) | `intentional materialized carry` | sampled diffs again show template path substitution rather than a new behavioral doctrine split [e:c+i] |
| sampled out-of-cohort agent (`gsd-phase-researcher.toml`) | `intentional materialized carry` | sampled diff follows the same placeholder-to-materialized-path pattern as the in-scope cohort [e:c+i] |
| live-only workflow/reference/bin-lib families beyond tracked overlay subset | `selective overlay boundary` | the current live `.codex/` line contains many newer or broader surfaces than the tracked overlay subset; this is a coverage/boundary issue and should not be mistaken for mystery drift by default [d:r:i] |

## Evidence Notes

- [e:c+i] The config pair is not merely a mismatch. Overlay uses template placeholders and a generic compact-prompt slot, while live config carries concrete repo-local paths and repo-local defaults. Sources: [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:1), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:4), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:9), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:4), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:9).
- [e:c+i] The high-stakes planner cohort now matches semantically across live and overlay on the newly landed repo-quality posture; the visible difference is materialized path handling, not doctrine split. Sources: [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml:15), [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml:52), [.codex/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml:15), [.codex/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml:52).
- [e:c+i] Sampled workflow and reference diffs also follow the materialization pattern: overlay carries `__PROJECT_ROOT__`-style references while live runtime carries repo-local absolute paths. Sources: [tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:8), [tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:30), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:8), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:30), [tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md:57), [.codex/get-shit-done/references/planning-config.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/planning-config.md:57).
- [d:r:i] The live-only workflow/reference/bin-lib surfaces should not yet be read as `unknown live drift` by default because this repo already knows the tracked overlay canon is selective rather than exhaustive, and the active `.codex/` line has expanded well beyond that subset. The pressure here is boundary visibility and later coverage decision, not immediate cleanup.

## What The Pilot Does Not Yet Show

- [d:r:i] It does not yet show sampled `obsolete live residue`.
- [d:r:i] It does not yet show sampled `unknown live drift` inside the file-level surfaces above.
- [d:r:i] That absence should not be overstated into `there is no problematic drift anywhere`; it only means the sampled load-bearing surfaces are currently better explained by materialization and selective overlay scope than by mystery divergence.

## Consequences

- [d:r:i] The next persistence/materialization move should not treat any overlay/live difference as automatically suspicious.
- [d:r:i] Manifest/install coherence should now be reframed against a sharper question:
  - what is supposed to be templated carry
  - what is supposed to be repo-local config carry
  - what is supposed to be tracked overlay coverage
  - what is actually unexplained drift
- [d:r:i] A second pass can widen this register later, but the strongest immediate value is already present: sampled high-leverage differences are mostly intelligible.

## Immediate Next Move

- [g:r:i] Use this pilot as the baseline when deciding the manifest/install coherence pass, and do not let that later pass collapse `materialized carry` or `selective overlay boundary` into generic defect language.
