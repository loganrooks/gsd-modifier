# Docs-Audit Packet: PR Docs Intervention Carry

Status: draft packet  
Date: 2026-04-20

## Lane

- area: `docs-audit`
- lane: `pr-docs-intervention-carry`
- governing spec: [../specs/01-pr-docs-intervention-carry-spec.md](../specs/01-pr-docs-intervention-carry-spec.md)

## Packet Purpose

- [g:r:i] Give the audit lane enough material to judge what the submitted docs PR carries for harness intervention planning, what it still flattens or hides, and what kind of doc-layer transformation pressure it creates.
- [g:r:i] Keep the packet narrow enough that the lane does not collapse into another whole-harness review or another broad rerun-program lane.

## Read Order

### Stage 0: Local Framing And Carry Pressure

Read these first:

1. [PR-DOCS-INTERVENTION-CARRY-AUDIT.md](../../pr-docs-intervention/PR-DOCS-INTERVENTION-CARRY-AUDIT.md)
2. [HARNESS-INTERVENTION-ONBOARDING.md](../../harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md)
3. [HARNESS-INTERVENTION-UPDATE-LANE.md](../../harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md)

Estimated words:

- `3,700`

Estimated tokens:

- low band: `~4.6k`
- planning band: `~5.6k`
- high band: `~6.1k`

### Stage 1: Submitted PR Docs Snapshot, Core Surfaces Only

Read these next:

4. [upstream-docs-pr-r2/README.md](../../upstream-docs-pr-r2/README.md)
5. [upstream-docs-pr-r2/docs/INVENTORY.md.txt](../../upstream-docs-pr-r2/docs/INVENTORY.md.txt)
6. [upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt](../../upstream-docs-pr-r2/docs/ARCHITECTURE.md.txt)
7. [upstream-docs-pr-r2/docs/COMMANDS.md.txt](../../upstream-docs-pr-r2/docs/COMMANDS.md.txt)
8. [upstream-docs-pr-r2/docs/AGENTS.md.txt](../../upstream-docs-pr-r2/docs/AGENTS.md.txt)

Estimated words:

- `17,681`

Estimated tokens:

- low band: `~22.1k`
- planning band: `~26.5k`
- high band: `~29.2k`

### Stage 2: Comparative Current-Upstream Anchor

Read this after the submitted PR snapshot:

9. [get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md)

Estimated words:

- `4,804`

Estimated tokens:

- low band: `~6.0k`
- planning band: `~7.2k`
- high band: `~7.9k`

### Stage 3: Reserve Only If Needed

Open these only if the lane cannot judge contributor-orientation versus intervention-orientation cleanly from the core packet:

10. [upstream-docs-pr-r2/docs/USER-GUIDE.md.txt](../../upstream-docs-pr-r2/docs/USER-GUIDE.md.txt)
11. [upstream-docs-pr-r2/docs/workflow-discuss-mode.md.txt](../../upstream-docs-pr-r2/docs/workflow-discuss-mode.md.txt)

Estimated reserve words:

- `5,038`

Estimated reserve tokens:

- low band: `~6.3k`
- planning band: `~7.6k`
- high band: `~8.3k`

## Packet Totals

Primary packet only:

- words: `26,185`
- low band: `~32.7k`
- planning band: `~39.3k`
- high band: `~43.2k`

Primary plus reserve:

- words: `31,223`
- low band: `~39.0k`
- planning band: `~46.8k`
- high band: `~51.5k`

## Packet Guardrails

- [g:r:i] Do not treat the submitted PR snapshot as current runtime truth.
- [g:r:i] Do not let current-upstream inventory become a whole-upstream reread invitation.
- [g:r:i] Do not expand into a broad harness-quality lane; stay on doc carry, intervention visibility, and transformation pressure.
- [g:r:i] Do not use threshold language like `adequate`, `good enough`, `passes`, or `ready` as the lane's governing frame.
