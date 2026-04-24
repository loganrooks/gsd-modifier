# Wave-1 Artifact Topology

Status: active forward-looking workspace organization  
Date: 2026-04-19

## Purpose

- [d:r:i] This directory is the bounded organization change that the workspace needed before Wave 1. It does not retroactively reshuffle the entire audit corpus; it gives all new Wave-1 artifacts a cleaner home so the flat root does not keep absorbing more spec/prompt/output/disposition clutter.

## Layout

- `specs/`
  - Wave-1 lane specs
- `prompts/`
  - launch prompts written from the specs
- `packets/`
  - packet manifests or packet overrides used by specific lanes
- `outputs/`
  - returned lane outputs
- `dispositions/`
  - local inheritance / comparative disposition notes for Wave-1 lanes
- `launch-truth/`
  - launch-truth captures and adjacent launch-state artifacts

## Rule

- [g:r:i] New Wave-1 artifacts should land in this directory tree by function, not back in the flat audit root, unless a later explicit decision supersedes this topology.
- [g:r:i] Historical pre-Wave-1 artifacts remain where they are for now. If they are migrated later, do that as a separate auditable move with link updates and explicit supersession notes.
- [g:r:i] Treat `outputs/` as provisional until touched-root reference verification passes. After any external lane return lands, run `python3 tooling/codex/verify_touched_audit_refs.py` before accepting the output, writing a disposition, or checkpointing the workspace.
