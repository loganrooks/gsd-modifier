# Bridge Harness Stabilization Planning Package

Date: 2026-04-24
Status: draft planning package

## Purpose

This package separates strategic horizon framing from concrete executable implementation plans.

It exists because one short horizon may contain multiple concrete plans, and some concrete plans may change or refine the upstream horizon. The package therefore keeps each layer separate but cross-cited.

## Files

- [HORIZONS.md](HORIZONS.md) - strategic immediate, short, medium, and long horizon framing.
- [SHORT-HORIZON.md](SHORT-HORIZON.md) - short-horizon program plan for a deployable bridge harness.
- [concrete-plans/001-audit-import-refmap-stabilization/PLAN.md](concrete-plans/001-audit-import-refmap-stabilization/PLAN.md) - completed implementation plan for stabilizing the audit import and reference-map state.
- [concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md](concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md) - executable draft for the runtime intervention surface inventory.

## Traceability Model

Use this package from broadest to narrowest:

```text
HORIZONS.md
  -> SHORT-HORIZON.md
    -> concrete-plans/<plan-id>/PLAN.md
```

Concrete plans should cite their parent horizon/workstream and record when execution discovers something that should revise the upstream plan.

## Current Boundary

The current blocking concern is still not adding new bridge-harness behavior yet.

The audit/reference-map blocker has been stabilized. The next release slice is the runtime intervention surface inventory, which should expose carriers, producers, consumers, materialization paths, and verification hooks before behavior changes are planned.

The current concrete plan for that blocker is [concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md](concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md).
