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
- [concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md](concrete-plans/002-runtime-intervention-surface-inventory/PLAN.md) - completed implementation plan for the runtime intervention surface inventory.
- [concrete-plans/003-instruction-surface-generation-parity/PLAN.md](concrete-plans/003-instruction-surface-generation-parity/PLAN.md) - executable draft for instruction-surface generation and parity.

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

The audit/reference-map blocker has been stabilized, and the runtime intervention surface inventory is committed. The next release slice is instruction-surface generation parity: deciding whether `AGENTS.md` remains the single generated project instruction surface or whether Claude needs a generated companion, then locking that posture with evidence and tests.

The current concrete plan for that blocker is [concrete-plans/003-instruction-surface-generation-parity/PLAN.md](concrete-plans/003-instruction-surface-generation-parity/PLAN.md).
