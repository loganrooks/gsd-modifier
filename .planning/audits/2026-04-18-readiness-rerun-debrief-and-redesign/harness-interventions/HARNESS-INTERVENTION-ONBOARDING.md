# Harness Intervention Onboarding

Date: 2026-04-20
Status: draft working map

## Purpose

- [g:r:i] This is a working onboarding/map artifact for planning harness interventions across the repo-local GSD ecosystem.
- [d:r:i] It exists because the earlier `C3`-style mapping pass and the later docs comparison were useful but insufficient for the actual job: deciding where and how to intervene in the harness so it can carry better short-term work and better long-horizon planning across complex design landscapes.
- [d:c+i] The governing correction is already explicit elsewhere: `R5.18` is one bounded obstruction/proof surface, not the sovereign point of the exercise, and the missing object is a purpose-built intervention-onboarding layer rather than another docs-vs-docs comparison. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:8), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:15), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:55), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:72).

## What C3 Actually Earned

- [e:c+i] The original surface-map checkpoint already made the right methodological move: do not treat skills as the primary unit; treat the harness as a layered system of workflows, shared contracts, agent-role contracts, and runtime/config/install seams. Sources: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:5), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:18), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:24), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:38).
- [e:c+i] Checkpoint 4 then sharpened the criticism: the biggest Codex-side losses were runtime-authoritative worker drift and launch-truth capture, not a lack of narrative docs alone. Sources: [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:17), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:70), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:72), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:78).
- [e:c+i] Checkpoint 5 then made the materialization picture explicit: effective runtime truth is upstream base -> tracked overlay -> installer post-pass -> live `.codex/` runtime -> `.planning/` outputs, and important behavior can drift into live runtime surfaces beyond the tracked overlay canon. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:12), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:15), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:185), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:200).
- [d:r:i] So C3 earned the layer model, but it did not yet expose the intervention-onboarding surface needed on its own. This document is the next object that should have existed after that work.

## Declared Vs Effective Authority

| Surface family | Declared authority | Effective authority now | Intervention use |
| --- | --- | --- | --- |
| Docs-refresh branch | stronger inventory/parity governance idea | not current shipped runtime truth | `governance/onboarding` |
| Current active `.codex/` runtime | live repo-local harness | effective runtime truth for this repo today | `primary intervention target` |
| `tooling/portable-gsd/overlay/` | tracked local intervention canon | important, but not exhaustive of live drift | `primary intervention target` |
| `scripts/setup-portable-gsd.sh` | install/materialization contract | load-bearing composition seam and mutation surface | `primary intervention target` |
| `.codex/get-shit-done/bin/lib/*` helpers | internal helper implementation | live routing/state semantics | `primary intervention target` |
| `.codex/skills/*` wrappers | visible command entry layer | thinner than they look; mostly adapter seams | `secondary target` |
| `.codex/agents/*.toml` | registered agent runtime surface | live spawned-worker authority | `primary intervention target` |
| `.planning/readiness/...` audits/reviews | review/package truth | not runtime canon | `review/control only` |

- [e:c+i] This declared/effective split follows directly from the update lane and topology work: the docs-refresh branch contributes governance ideas, but active runtime truth sits in repo-local `.codex/*`, the installer, the overlay, and runtime helper chains. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:46), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:47), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:12), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:15), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:192).

## Intervention Families

### 1. Runtime Authority And Materialization

- [e:c+i] The installer is a three-stage composition: upstream install, overlay copy, then post-copy mutation. That means reinstall truth cannot be read from one source file alone. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:20), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:23), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:46), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:185).
- [e:c+i] At the 2026-04-20 probe boundary, the active repo sat at published `v1.38.1`, and a fresh detached reinstall plus overlay came back semantically aligned with that runtime except for deliberate config defaults and stale manifest hashes; current live-version claims should now defer to the later `1.38.3` runtime carriers and uplift compatibility anchor. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:37), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:39), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:41), [/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:71).
- [d:r:i] Practical consequence: direct active-repo reinstall is not the current missing move. Better intervention targets here are manifest coherence, overlay/live drift visibility, and explicit upgrade/probe discipline.

### 2. Workflow And Artifact Contracts

- [e:c+i] The high-leverage workflow family remains the phase-critical chain plus shared contracts, not the wrapper layer: discuss/research/plan/execute/verify, templates, and references. Sources: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:24), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:25), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:26), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:39).
- [e:c+i] Checkpoint 5 already proved that important behavior drifted into live workflow/reference surfaces beyond the tracked overlay, especially planner review-consumption and debt-aware completion semantics. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:170), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:171), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:200).
- [d:r:i] Practical consequence: harness intervention planning should privilege workflow/reference/template/helper seams over “more wrapper docs” unless a wrapper is actually mutating behavior.

### 3. Runtime-Authoritative Agents And Launch Truth

- [e:c+i] The biggest Codex-side criticism remains runtime-authoritative worker drift: registered `.toml` agents, not the nicer `.md` companions, shape spawned-worker behavior. Sources: [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:70), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:78), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:79).
- [e:c+i] Launch-truth checking is honest but still protocol-heavy: this repo already points operators to `state_5.sqlite`, but the truth is not yet durably captured at spawn/review boundaries. Sources: [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:28), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:72), [checkpoint-4-codex-load-bearing-surfaces-and-seams.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:80).
- [d:r:i] Practical consequence: any serious harness-improvement program should treat agent `.toml` alignment and launch-truth capture as first-rank intervention surfaces.

### 4. Long-Horizon Planning And Richer Inheritance

- [e:c+i] `spec-phase` is now a live workflow surface that splits `what/why` from `how`, uses ambiguity scoring, and locks falsifiable requirements before discuss/plan starts. Sources: [spec-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/spec-phase.md:1), [spec-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/spec-phase.md:20), [spec-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/spec-phase.md:95), [spec-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/spec-phase.md:189).
- [e:c+i] `ingest-docs` is now a live workflow surface for classifying and synthesizing mixed planning-document corpora into `.planning/`, with manifest support, conflict handling, and a dedicated doc-synthesis chain. Sources: [ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:1), [ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:79), [ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:152), [ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:173).
- [e:c+i] `mandatory-initial-read` is now an explicit reference contract: if a prompt includes a `<required_reading>` block, the files listed there must be read before any other actions. Source: [mandatory-initial-read.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/mandatory-initial-read.md:1).
- [d:r:i] Practical consequence: these are live intervention surfaces for longer-horizon management, not just new docs to admire. They can be used to structure better inheritance of doc corpora, phase intent, and required context before planning or execution.

### 5. Docs Governance And Inventory Discipline

- [e:c+i] The docs-refresh branch still matters because it made the strongest explicit move toward inventory-backed, mechanically guarded docs truth. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:28), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:47).
- [e:c+i] But it is not equivalent to current shipped truth, because the then-current `1.38.1` line already included many surfaces absent from that branch, and the live runtime has since moved again. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:46), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:49), [/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:71).
- [d:r:i] Practical consequence: adopt the inventory/parity governance idea, not the docs-refresh branch wholesale as if it were current runtime canon.

## Current Disposition By Surface

### Adopt Into Repo-Local Harness / Process Now

- [d:r:i] Treat agent `.toml` alignment as a prime future intervention lane.
- [d:r:i] Treat launch-truth capture as a real protocol/mechanism design target, not merely operator hygiene.
- [d:r:i] Treat manifest coherence in the install-plus-overlay flow as tooling debt worth fixing.
- [d:r:i] Treat live workflow/reference/helper drift beyond overlay as something that must be made legible before future upgrades.

### Use As Onboarding / Governance Now

- [d:r:i] Use the docs-refresh branch’s inventory/parity posture as a governance model.
- [d:r:i] Use `spec-phase`, `ingest-docs`, and `mandatory-initial-read` as part of a stronger intervention-planning and inheritance toolkit.
- [d:r:i] Use the checkpoint-3/4/5 layer model as the standing frame for future harness investigation.

### Hold As Future Pressure

- [d:r:i] Sketch/spike/ultraplan and other newly added specialist surfaces should stay visible, but they are not first-rank harness-quality interventions for this repo yet.
- [d:r:i] Upstream movement beyond the earlier `1.38.1` probe line should stay monitored, but the currently inspectable `1.39.0` branch delta is too small by itself to force a new upgrade wave.

## Recommended Sequence

1. Use this artifact, [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md), and [SURFACE-STATUS-AND-DELTA.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/SURFACE-STATUS-AND-DELTA.md) as the bounded onboarding set for future harness-intervention work.
2. Use the completed proposal batch under [intervention-proposals/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/README.md:1) as the bounded follow-through layer for:
   - agent `.toml` authority alignment
   - launch-truth capture
   - manifest/install coherence
   - live-vs-overlay drift visibility
3. Start disposition with [intervention-proposals/05-batch-routing-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/05-batch-routing-note.md:1), which sequences the first strongest pair as launch-truth capture plus agent `.toml` authority alignment.
4. Use `spec-phase` and `ingest-docs` explicitly when a future intervention lane needs better inheritance or clearer WHAT-before-HOW framing.
5. Preserve the docs-refresh branch mainly as governance pressure, not as a replacement truth set.
6. Re-run isolated upgrade probes before any future runtime jump beyond the current live basis.

## Bottom Line

- [d:r:i] The main pressure now is disciplined intervention planning against the right authority surfaces, not another round of comparison for its own sake.
- [d:r:i] The best onboarding for that work is no longer “read the docs” or “read the old mapping.” It is: read the authority split, the layer stack, the runtime/materialization seams, and the concrete intervention families above.
