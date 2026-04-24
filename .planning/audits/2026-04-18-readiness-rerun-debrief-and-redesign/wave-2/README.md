# Wave-2 Artifact Topology

Status: active forward-looking workspace organization  
Date: 2026-04-20

## Purpose

- [d:r:i] This directory holds the second-wave artifacts that consume accepted Wave-1 returns and turn them into stronger opportunity pressure and rerun-design options.
- [d:r:i] Wave 2 is where the workspace should stop merely restating the first-wave stack and instead decide what stronger moves were left on the table and what second-attempt program shape is now actually justified.

## Layout

- `specs/`
  - Wave-2 lane specs
- `prompts/`
  - launch prompts written from the specs
- `packets/`
  - concrete staged read sets for Wave-2 lanes
- `outputs/`
  - returned Wave-2 lane outputs
- `dispositions/`
  - local inheritance / comparative disposition notes for Wave-2 lanes
- `launch-truth/`
  - launch-truth captures and adjacent launch-state artifacts

## Rule

- [g:r:i] New Wave-2 artifacts should land in this directory tree by function, not back in the flat audit root.
- [g:r:i] Treat `outputs/` as provisional until touched-root reference verification passes. After any external lane return lands, run `python3 tooling/codex/verify_touched_audit_refs.py` before accepting the output, writing a disposition, or checkpointing the workspace.
- [g:r:i] When a Wave-2 lane has multiple parallel returns, write a comparative disposition under `dispositions/` and treat that synthesis as the accepted feed for later lanes. Keep the raw outputs in `outputs/` as challenge material unless explicitly promoted further.
- [g:r:i] `rerun-design` is not launchable until the accepted `suppressed-opportunity-and-non-intervention` return has been inserted into its packet. Do not silently substitute memory of lane 05 for the actual returned artifact.
