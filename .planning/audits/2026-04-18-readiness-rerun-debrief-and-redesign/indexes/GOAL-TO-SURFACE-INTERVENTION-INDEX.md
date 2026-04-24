Date: 2026-04-20
Status: active companion artifact

# Goal To Surface Intervention Index

## Purpose

- [g:r:i] This companion artifact routes common harness-modification goals to the surfaces that can actually carry them, so future intervention work does not over-invest in the wrong layer.
- [d:r:i] Its job is not to restate the whole topology. Its job is to answer a narrower question quickly: given the change you want, where should you start, what should you check beside it, and which layers are most likely to mislead you if you treat them as sovereign?

## How To Use This Index

- [d:r:i] Start from the concrete goal, not the document family you happen to be reading.
- [d:r:i] Use the `Primary surfaces` column as the first intervention seam.
- [d:r:i] Use the `Check beside it` column to keep declared/effective authority drift visible.
- [d:r:i] Treat `Avoid starting here` as a warning against surfaces that may look authoritative but are thinner than they appear for that particular goal.

## Goal Routing Table

| Goal | Primary surfaces | Check beside it | Avoid starting here |
| --- | --- | --- | --- |
| Change spawned-worker behavior or authority | `.codex/config.toml`, `.codex/agents/*.toml` | `scripts/setup-portable-gsd.sh`, `../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md` | wrapper prose alone |
| Change planning/execution routing or status semantics | live `.codex/get-shit-done/workflows/*`, `references/*`, `bin/lib/*`, `.planning/config.json` | overlay copies of the same surfaces, transition/completion helpers | high-level docs alone |
| Preserve a repo-local runtime change across reinstall/update | `tooling/portable-gsd/overlay/`, `scripts/setup-portable-gsd.sh` | `.codex/gsd-local-patches/backup-meta.json`, `.codex/gsd-file-manifest.json` | editing live `.codex/` only |
| Make materialization truth more trustworthy | `scripts/setup-portable-gsd.sh`, `.codex/gsd-file-manifest.json`, refmap/verification tooling | live `.codex/` against fresh reinstall proof | backup metadata alone |
| Improve launch-truth capture and reviewability | agent `.toml` contracts, launch-truth artifacts, spawn/check procedure surfaces | `state_5.sqlite` verification practice, repo-local AGENTS contracts | after-the-fact narrative summaries alone |
| Improve contributor onboarding or docs governance | stable PR-doc layer, local companion docs, parity/inventory discipline | current upstream inventory, local runtime delta note | runtime files when the goal is explanation/governance only |
| Add stronger WHAT-before-HOW and long-horizon inheritance | `spec-phase`, `ingest-docs`, `mandatory-initial-read` | `.planning/config.json`, current package/read-order rules | ad hoc discussion-only framing |
| Evaluate whether a newer upstream surface should pressure local intervention | current upstream `docs/INVENTORY.md`, live `.codex/` presence, `SURFACE-STATUS-AND-DELTA.md` | `../harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md`, reinstall probes | frozen PR snapshot treated as current truth |

## Goal Families

### 1. Runtime Authority Goals

- [e:c+i] Runtime authority goals should begin at live registry and worker-contract surfaces, because spawned-worker behavior is carried by `.codex/config.toml` and `.codex/agents/*.toml`, not by nicer narrative wrapper docs. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:40), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:57), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:79).
- [d:r:i] If the goal is to change what actually happens at spawn time, the stable docs layer is context, not the first seam.

### 2. Routing / Semantic Goals

- [e:c+i] Routing, completion, transition, and helper-chain semantics live primarily in the live `.codex/get-shit-done/` workflow/reference/helper chain plus `.planning/config.json`, not in the skill wrappers. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:14), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:27), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:46), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:83).
- [d:r:i] If the goal is “change how the harness routes or interprets phase state,” start in live workflow/helper surfaces and check whether the overlay and installer actually preserve that change.

### 3. Materialization / Persistence Goals

- [e:c+i] Persistence across reinstall/update runs through the install composition seam, not just through live edits. The runtime is composed from upstream base, overlay copy, and post-copy mutation, so persistence work must touch the layer that actually survives rematerialization. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:23), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:28), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:75).
- [d:r:i] So “I changed the live file and it worked once” is not enough for this goal family.

### 4. Governance / Onboarding Goals

- [e:c+i] The docs-audit lane pair converged on a strong split: stable PR docs should carry contributor/reference and governance work, while heavier intervention-planning carry belongs in companion artifacts. Sources: [docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md:9), [docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md:13), [docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/docs-audit/dispositions/01-pr-docs-intervention-carry-comparative-disposition.md:24).
- [d:r:i] So if the goal is better contributor orientation or better docs governance, start with the stable docs layer and local companion docs, not with runtime surgery.

### 5. Long-Horizon Inheritance Goals

- [e:c+i] `spec-phase`, `ingest-docs`, and `mandatory-initial-read` are now live surfaces for stronger WHAT-before-HOW framing, corpus inheritance, and required-read discipline. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:56), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:57), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:58), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:70), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:161), [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md:287).
- [d:r:i] If the goal is stronger long-horizon planning rather than immediate runtime mutation, start with these inheritance-capable surfaces before reaching for lower-level intervention seams.

## Fast Routing Rules

- [d:r:i] If the goal mentions `spawned agent`, `authority`, `model`, or `reasoning`, start with `.codex/config.toml` and `.codex/agents/*.toml`.
- [d:r:i] If the goal mentions `routing`, `phase status`, `transition`, `review consumption`, or `completion`, start with live workflows/references/helpers and `.planning/config.json`.
- [d:r:i] If the goal mentions `survives reinstall`, `update`, `portable`, or `overlay parity`, start with `tooling/portable-gsd/overlay/` and `scripts/setup-portable-gsd.sh`.
- [d:r:i] If the goal mentions `docs`, `inventory`, `parity guard`, or `contributor orientation`, start with the stable PR-doc layer and companion docs.
- [d:r:i] If the goal mentions `inherit this corpus`, `falsifiable WHAT`, or `required reading`, start with `spec-phase`, `ingest-docs`, and `mandatory-initial-read`.

## Bottom Line

- [g:r:i] The strongest use of this index is not to decide whether a surface matters. It is to shorten the path from intervention intent to the surface that can actually carry it, while keeping neighboring authority seams visible enough to avoid flat or ceremonial changes.
