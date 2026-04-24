Date: 2026-04-21
Status: landed first slice

# Read-Packet And Relevance-Control First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `65`.
- [g:r:i] The target stayed bounded: make repo-local reading control more explicit at the shared mandatory-read reference and the current operator-facing re-entry surfaces, without widening into a harness-wide packet retrofit.

## What Landed

- [e:r:i] The tracked overlay now owns the repo-local mandatory-read doctrine:
  - [tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] That reference now distinguishes three packet tiers:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [e:r:i] The reference also keeps contextual reread sovereign:
  - structured helpers, manifests, and snapshots should be the first route when they already exist
  - deeper packet widening waits for the active route, anomaly, or user request
  - explicit prohibitions, quoted anti-patterns, and historical evidence must remain sayable even when the packet is being kept narrow
- [e:r:i] The current re-entry surfaces now carry that layered reading doctrine explicitly:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
- [e:r:i] Those surfaces now make their first packet explicit instead of leaving the read posture ambient:
  - `progress` starts from structured roadmap/state extracts and only widens by route
  - `resume-project` starts from init/state/project/handoff and only widens when the chosen route actually needs more
  - `uplift-project` starts from helper detect output and current uplift outputs, with broader audit/proposal rereads held until helper routes point there

## Verification And Recovery Path

- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_read_packet_tiers_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_read_packet_tiers_contract.py), covering:
  - overlay ownership for the mandatory-read reference
  - packet-tier doctrine presence
  - layered packet carry in the three operator-facing entry surfaces
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`
- [e:r:i] Because this slice also moved doctrine-sensitive entry carriers and the `uplift-project` workflow, the repo-local uplift memory was refreshed too:
  - `python3 tooling/codex/project_uplift.py detect --write .`
  - the resulting `UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, and `STATE.md` uplift section now match the current doctrine fingerprints and return `Continue with current routing.`

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into initialization surfaces such as `new-project` or `new-milestone`.
- [d:r:i] It does not yet widen packet tiers across the broader spawned-agent fleet.
- [d:r:i] It does not yet add automatic relevance ranking or packet synthesis.

## Current Consequence

- [d:r:i] The harness now carries a bounded repo-local reading-packet doctrine rather than only a flat mandatory-read default.
- [d:r:i] The current operator-facing re-entry surfaces now give stronger control over what is primary, what is route-local support, and what should wait for deeper widening.
- [d:r:i] The next narrower question is which adjacent family should inherit after this slice:
  - initialization / onboarding surfaces
  - seed-consumer carry
  - or a later wider packet retrofit
