# Runtime Intervention Surface Inventory Boundary

Date: 2026-04-24
Status: queued

## Purpose

This note opens the next short-horizon bridge-harness slice after audit import/refmap stabilization.

The next implementation step is a runtime intervention surface inventory. It should identify where generated runtime instructions, workflow entrypoints, portable overlay files, runtime adapters, and contract checks would need to change before any bridge-harness behavior is implemented.

## Completed Prerequisite

The audit import/refmap stabilization prerequisite is complete:

- `audit_refmap.py` now supports batch move manifests with moved-source relative-link recalculation.
- The imported audit corpus is committed under `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`.
- `.planning/readiness/phase-01-rerun` and `.planning/research/2026-04-15-multilayer-harness-governance-audit` are committed as carried origin context.
- `docs/origin-audit/README.md` identifies the carried origin audit location without claiming `.planning/topology-map` exists.

## Inventory Scope

Include:

- shipped/runtime-facing overlay and portable setup surfaces
- Codex and Claude runtime instruction generation paths
- contract tools that prove source-vs-materialized behavior
- docs that would become stale if runtime intervention behavior changes

Exclude for the inventory pass:

- implementation of workflow-lane routing
- deploys into `prix-guesser`
- parity architecture rewrites
- broader host matrix semantics

## Verification Baseline

Use the audit refmap baseline from the stabilization slice as the starting reference:

- markdown files scanned: `800`
- markdown links scanned: `7834`
- local existing links: `7787`
- local missing links: `47`

The remaining missing links are preserved origin-context references to absent old-host artifacts or sibling audit paths, not unresolved reorganization fallout.
