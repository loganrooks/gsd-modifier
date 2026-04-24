Date: 2026-04-21
Status: active widening map

# Broader Network Producer / Consumer And Carrier Map

## Purpose

- [g:r:i] This note widens the propagation family beyond the project-uplift example without collapsing the whole harness into an undifferentiated mesh.
- [g:r:i] The target is a stronger answer to the user’s recurring concern: when a contract changes, where else should that change surface, and which carriers should be reread or updated so the modification stays robust across the GSD network?

## What This Adds Beyond The Uplift Example

- [e:c+i] `02`, `05`, and `07` now make one worked family explicit: producer -> bridge -> consumers -> durable outputs -> materialization boundary. Sources: [02-project-uplift-producer-consumer-and-impact-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/02-project-uplift-producer-consumer-and-impact-map.md:24), [05-project-uplift-chain-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/05-project-uplift-chain-map.md:11), [07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md:6).
- [d:r:i] This widening asks the next question: what larger carrier families should be treated the same way, even when the exact helper/output chain is different?
- [e:c+i] Checkpoint-3 already argued that the honest mapping unit is a layer stack, not a flat skill list: workflow chain, shared contracts, agent-role contracts, and runtime/config/overlay seams [e:c+i]. Source: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:34).

## Broader Carrier Families

| Family | Main producers | Main consumers | Narrative / mirror carriers | Materialization or registry carriers | Typical propagation obligation |
| --- | --- | --- | --- | --- | --- |
| Governing doctrine | `AGENTS.md`, `.planning/AGENTS.md`, `CLAUDE.md`, `.planning/CLAUDE.md`, `LONG-ARC.md`, `CLAIM-TYPES.md` | agents, workflows, skills, audit specs, research lanes | `CURRENT-STATE.md`, `PLAIN-LANGUAGE-*`, workspace protocol docs | none directly; carried through reread and prompt assembly | if doctrine changes, reread agent/workflow/skill instructions and current audit/request surfaces that still operationalize the older doctrine |
| Runtime install / materialization | `setup-portable-gsd.sh`, `portable_gsd_contract.py`, `OVERLAY-MANIFEST.json` | live `.codex/` runtime frontier | `tooling/portable-gsd/README.md`, `tooling/codex/README.md`, propagation-audit notes | `backup-meta.json`, `.codex/gsd-file-manifest.json`, live `.codex/` files | if install semantics change, update manifest typing, installer, verifier, and the visibility/coherence tools that reason about the same boundary |
| Runtime registry / launch authority | `.codex/config.toml`, `.codex/agents/*.toml`, repo-local model doctrine | spawned workers, runtime role selection, launch-truth review | agent `.md` shadow docs, governance notes, audit artifacts | live Codex runtime, `state_5.sqlite`, launch-truth captures | if runtime authority changes, reread agent contracts, registry pointers, launch-truth protocol, and any docs that still describe the old active path |
| Workflow / template / reference contracts | `.codex/get-shit-done/workflows/*`, `templates/*`, `references/*`, `bin/lib/*` | phase execution chain, helper tools, phase artifacts under `.planning/` | workflow README-like docs, audit notes, plan/proposal artifacts | overlay copies plus installer materialization | if workflow output or semantic contracts change, reread the templates, references, helper scripts, durable outputs, and wrapper skills that consume them |
| Skill / wrapper routing | `.codex/skills/*/SKILL.md` and overlay skill owners | user invocation, workflow binding, bounded entry posture | skill discovery docs, command inventories | `.codex/config.toml` agent/skill pointers where relevant | if wrapper posture changes, reread the target workflow, the skill owner, and any governing docs that describe the entry contract |
| Helper -> durable output chains | `project_uplift.py`, future helper families, state/report emitters | `progress`, `resume-project`, reports/manifests/state sections, later audits | tooling README, held-later registries, family notes | write paths under `.planning/`, overlay consumer workflows | if helper schema changes, reread direct consumers, durable output readers, tests, and the family docs that treat those outputs as authoritative memory |
| Governance / audit carriers | packet/spec/prompt/output/disposition sets, `STATUS.md`, `CURRENT-STATE.md`, `INDEX.md`, `ARTIFACT-INVENTORY.md` | later reviewers, later lanes, future operator rereads | plain-language entry docs, onboarding docs | launch-truth artifacts, checkpoint commits | if a family meaningfully changes, update the governing synthesis and discovery surfaces so later rereads do not inherit stale routing or stale read order |

## Why These Families Matter

### 1. Workflow And Shared-Contract Families

- [e:c+i] Checkpoint-3 already showed that workflows, templates, and references are a coupled contract layer rather than independent prose islands [e:c+i]. Sources: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:24), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:35), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:51).
- [d:r:i] That means a workflow change rarely stops in the workflow file. It usually has adjacent template/reference consumers even before any runtime install question appears.

### 2. Runtime Install And Registry Families

- [e:c+i] Checkpoint-3 and the newer propagation work together now show two distinct runtime families:
  - install/materialization truth
  - spawned-worker/registry truth
  Sources: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:38), [07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md:15), [runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:1).
- [d:r:i] Those two families touch each other, but they are not the same family. Treating them as one blob would flatten different propagation duties.

### 3. Skill / Wrapper Families

- [e:c+i] Checkpoint-3 explicitly warned against treating the full skill set as the primary truth surface; skills are mostly adapters into deeper workflow contracts [e:c+i]. Source: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:34).
- [d:r:i] That means skills usually inherit from workflow changes, but they still need explicit reread when the entry contract or invocation posture changes.

### 4. Governance Carriers

- [e:c+i] The propagation family already proved that a local code/runtime change can stay under-carried if the governing synthesis and discovery surfaces do not move with it [e:c+i]. Sources: [06-bounded-propagation-strengthening-batch-a-b-d-e-f.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/06-bounded-propagation-strengthening-batch-a-b-d-e-f.md:6), [07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/07-overlay-add-vs-overwrite-contract-and-post-materialization-gate.md:42).
- [d:r:i] So governance docs are not “after the real work.” They are part of whether a family can survive later reread without stale assumptions.

## Propagation Obligations By Change Type

### If A Governing Doctrine Surface Changes

- [d:r:i] Check:
  - agent contracts
  - workflow request language
  - skill entry instructions
  - current audit packet/spec/prompt surfaces
  - short governing synthesis and read-order docs

### If A Runtime Install / Overlay Surface Changes

- [d:r:i] Check:
  - `OVERLAY-MANIFEST.json`
  - `portable_gsd_contract.py`
  - `setup-portable-gsd.sh`
  - `runtime_visibility.py`
  - `manifest_install_coherence.py`
  - overlay discovery docs and propagation-family notes

### If A Runtime Registry / Agent Contract Changes

- [d:r:i] Check:
  - `.codex/config.toml`
  - affected `.codex/agents/*.toml`
  - any overlay owner of the same runtime surface
  - launch-truth capture protocol
  - doctrine docs that still describe the older active authority path

### If A Workflow / Template / Reference Contract Changes

- [d:r:i] Check:
  - the direct workflow
  - adjacent templates/references/helpers
  - wrapper skills that route into the workflow
  - durable `.planning/` outputs or audit artifacts that treat the old contract as authoritative
  - installer/materialization layer if the touched file is overlay-owned

### If A Helper / Durable Output Chain Changes

- [d:r:i] Check:
  - helper logic
  - output schema
  - direct consumer workflows
  - wrapper skills for those workflows
  - durable output readers
  - tests
  - governance/docs surfaces that point later readers at those outputs

## Current Stronger Reading

- [d:r:i] The propagation family now has enough structure to stop asking only “did this local edit seem coherent?”
- [d:r:i] The stronger question is now:
  - which carrier family changed
  - which adjacent carrier families should have moved with it
  - which neighbors are direct consumers
  - which neighbors are only mirrors
  - which held neighbors are explicit rather than ambient

## Current Consequence

- [d:r:i] The family is now widened beyond the uplift example in a structured way.
- [d:r:i] The next stronger move is no longer another local worked-example note.
- [d:r:i] The next stronger move is a bounded challenge lane over this broader carrier map, asking whether the family split is strong enough, what carriers are still missing, and where the next widening should land.
