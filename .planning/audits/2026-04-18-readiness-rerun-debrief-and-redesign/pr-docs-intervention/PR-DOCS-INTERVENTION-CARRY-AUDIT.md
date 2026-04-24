# PR Docs Intervention Carry Audit

Date: 2026-04-20
Status: draft working audit

## Purpose

- [g:r:i] This audit asks what the submitted docs-refresh PR corpus carries for harness-intervention planning, what it still flattens or hides, and how it should be transformed so it can support stronger short-horizon modifications and longer-horizon ecosystem planning.
- [d:r:i] This is not a threshold check about whether the docs are `adequate`, `good enough`, or `ready`. The governing question is how much intervention visibility, leverage, and planning power the docs create compared with stronger available forms.

## Bounds

- [e:c+i] Primary PR-docs snapshot under `upstream-docs-pr-r2/docs/`:
  - [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:1)
  - [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:1)
  - [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:1)
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:1)
- [e:c+i] Current upstream comparison anchor:
  - [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:1)
- [e:c+i] Local intervention framing anchors:
  - [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:1)
  - [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:1)
  - [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:1)
  - [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:1)
  - [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:1)

## Load-Bearing Gains The PR Docs Carry

### 1. Inventory-Backed Docs Truth

- [e:c+i] The strongest move in the PR corpus is the explicit claim that `docs/INVENTORY.md` and the filesystem outrank the broad narrative docs when they diverge, and that new surfaces should land in inventory first and then propagate outward through parity tests. Sources: [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:3), [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:7), [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:8), [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:9).
- [d:r:i] That is a real intervention gain because it converts docs from soft prose into a governed roster surface with explicit drift discipline. It is stronger than the earlier bridge-era state where broad docs could more easily float free of shipped reality.

### 2. Larger-System Visibility Than The Older Bridge Comparison Had

- [e:c+i] The PR `ARCHITECTURE.md` does more than generic description: it exposes the layered system stack from commands to workflows to agents to CLI tools to `.planning/`, gives explicit counts for commands, workflows, and agents, and names installer, hooks, and CLI modules as first-class layers. Sources: [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:22), [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:37), [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:107), [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:203), [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:223).
- [d:r:i] This matters because it carries more of the ecosystem than a wrappers-first reading. It gives a contributor or investigator a better chance of noticing that commands are not sovereign, workflows are orchestration, and CLI/file-state layers matter.

### 3. Stronger Command And Role Exposure

- [e:c+i] The PR `COMMANDS.md` turns a raw surface list into a structured command map with arguments, flags, products, and lifecycle position for core workflow commands like discuss, plan, execute, and verify. Sources: [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:15), [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:91), [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:138), [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:172), [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:196).
- [e:c+i] The PR `AGENTS.md` does the parallel move for agent roles, spawn points, tool surfaces, and outputs, while explicitly deferring final roster truth back to inventory. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:3), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:9), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:13), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:35), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:154).
- [d:r:i] These two docs carry a much better starting picture of how a reader enters and traverses the system than the earlier bridge-era broad docs did.

### 4. Governance Pressure That We Can Reuse Locally

- [e:c+i] The PR corpus already includes `spec-phase` and shows a stronger inventory-governed documentation posture. Sources: [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:68), [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:234).
- [d:c+i] That fits the local intervention map’s conclusion that the docs-refresh branch contributes its strongest value as governance pressure, not as a frozen replacement truth set. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:34), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:36), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:92), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:95).

## What The PR Docs Still Flatten, Hide, Or Misprioritize

### 1. Declared Authority Still Outruns Effective Authority

- [e:c+i] The PR `ARCHITECTURE.md` names commands, workflows, agents, CLI tools, templates, hooks, and `.planning/`, but it still tells the story primarily as a contributor-facing system stack. It does not make the local declared/effective split explicit: upstream docs are not the same thing as repo-local `.codex/` runtime truth, tracked overlay truth, installer post-pass truth, runtime helper truth, or agent `.toml` truth. Sources: [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:22), [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:43), [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:223), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:28), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:30), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:31).
- [d:r:i] This is the core reason the PR docs do not by themselves carry intervention planning strongly enough for our purposes: they help a reader understand the official system, but they do not yet tell the reader where actual leverage and actual runtime authority live in this repo.

### 2. The PR Snapshot Is Already Outrun By Current Shipped Surface Growth

- [e:c+i] The PR snapshot inventories `31` agents and `75` commands against a `v1.36.0` pin. Sources: [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:7), [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:13), [INVENTORY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/INVENTORY.md.txt:55).
- [e:c+i] Current upstream inventory now reports `33` agents and `82` commands and includes newer surfaces such as `plan-review-convergence`, `ultraplan-phase`, `spike`, `sketch`, `ingest-docs`, `sketch-wrap-up`, `spike-wrap-up`, and `mandatory-initial-read`. Sources: [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:13), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:57), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:74), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:75), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:76), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:77), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:213), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:247), [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:287).
- [d:r:i] So the PR corpus is a major governance step, but it cannot be treated as current ecosystem truth. Its intervention value depends on being compared against live upstream and local runtime rather than being absorbed unquestioned.

### 3. Intervention Ranking Is Still Missing

- [e:c+i] The PR docs enumerate surfaces, but they do not rank which surfaces have the highest blast radius, the highest leverage, or the strongest authority over actual behavior. By contrast, the local intervention map now singles out agent `.toml` alignment, launch-truth capture, manifest/install coherence, and live-vs-overlay drift visibility as first-rank intervention families. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:61), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:67), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:73), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:88).
- [d:r:i] That means the PR docs improve visibility, but they still do not tell a modifier where to intervene first if the goal is to improve real behavior rather than simply know the roster.

### 4. Long-Horizon Modification Planning Still Needs A Different Layer

- [e:c+i] The PR docs are strongest as contributor-facing overview, command reference, role-card reference, and architecture narrative. They are weaker on how to plan modifications across upgrades, overlay carry, installer post-pass mutations, live-runtime drift, and future ecosystem growth. Sources: [ARCHITECTURE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt:3), [COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/COMMANDS.md.txt:3), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/upstream-docs-pr-r2/docs/AGENTS.md.txt:3), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:185), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:29), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:39).
- [d:r:i] For our purposes, the missing carry is not just `more explanation`. It is a doc layer that helps someone inherit the system strategically: what is authoritative, what mutates what, what drifts, what is safe to copy as governance, and what is highest-yield to change first.

## Transformation Pressure

### 1. Preserve The PR Docs As A Governance Foundation

- [d:r:i] The inventory-first and parity-guard posture should be preserved and extended. That is the strongest reusable move in the PR corpus.

### 2. Add A Distinct Intervention-Onboarding Layer

- [d:c+i] The local harness-intervention docs already point in the right direction: keep broad contributor docs broad, but add a separate intervention-onboarding layer that makes declared/effective authority, materialization chains, intervention families, and leverage ranking explicit. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:28), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:56), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:82), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:97).

### 3. Treat Architecture As An Intervention Surface, Not Only A Narrative Surface

- [d:r:i] A transformed architecture doc for our purposes should show:
  - the live materialization chain
  - declared authority vs effective authority
  - which layers mutate downstream behavior directly
  - where runtime truth can outrun tracked overlay truth
  - which surfaces are highest leverage for systemic intervention

### 4. Keep Stable Reference Docs Separate From Leverage Maps

- [d:r:i] `COMMANDS.md` and `AGENTS.md` should remain readable references. The stronger move is not to stuff them with every intervention idea, but to build companion intervention docs that point back into them while preserving their stable-reference role.

## Bottom Line

- [d:r:i] The submitted PR docs are a real gain. They create a stronger roster-governed documentation system, carry far more system visibility than the earlier bridge-era broad docs, and give us a reusable governance pattern.
- [d:r:i] They still do not by themselves carry the actual planning problem we now care about: how to intervene in the harness ecosystem with the strongest available leverage over real behavior and future evolution.
- [g:r:i] The right inheritance move is therefore:
  1. keep the PR docs as a governance foundation
  2. compare them continuously against live upstream and live local runtime truth
  3. build and maintain a separate intervention-onboarding layer for declared/effective authority, materialization, leverage ranking, and long-horizon modification planning
