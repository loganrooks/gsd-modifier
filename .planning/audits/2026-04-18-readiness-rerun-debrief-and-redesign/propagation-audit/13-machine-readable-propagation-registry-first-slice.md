Date: 2026-04-21
Status: active registry first slice

# Machine-Readable Propagation Registry First Slice

## Purpose

- [g:r:i] The propagation family now has a stronger prose map, but the user’s dependency-visibility concern also asks for a more compact machine-readable surface.
- [g:r:i] This first slice does not attempt full automatic extraction. It freezes a curated registry snapshot so later tooling, audits, or diffs can inspect the current field without rereading every prose artifact first.

## What Lands Here

- [e:c+i] The first registry snapshot is now frozen at [artifacts/01-propagation-field-registry-v1.json](artifacts/01-propagation-field-registry-v1.json).
- [d:r:i] It carries four things:
  - named families
  - selected carriers
  - named cross-family edges
  - the basis commit and source-note set it was derived from

## Why This Is Worth Landing

- [d:r:i] The prose layer remains the richer explanatory layer.
- [d:r:i] The registry gives later work a compact surface for:
  - comparing two propagation snapshots
  - spotting whether a carrier or edge has been added, renamed, or dropped
  - seeding later machine-helped propagation tooling
  - giving future audits a smaller first read before they widen into the full prose family

## Limits

- [d:r:i] This is a curated snapshot, not automatic whole-harness extraction.
- [d:r:i] It currently focuses on the high-consequence carriers already named by `08`, `09`, `10`, `11`, and `12`.
- [d:r:i] It does not yet emit impact suggestions or derive changes from git diffs.
- [d:r:i] The next refresh should be seeded from the maintained inventory/docs frontier plus live runtime evidence, not from this file alone. See [14-propagation-registry-generation-and-seeding-policy.md](14-propagation-registry-generation-and-seeding-policy.md).

## Current Consequence

- [d:r:i] The propagation family now has:
  - top-level prose widening in `08`
  - sharpened sub-family and edge notes in `09-12`
  - one compact machine-readable registry snapshot in `artifacts/01-propagation-field-registry-v1.json`
- [d:r:i] The next stronger move is no longer hypothetical. It is now the layered `v2` first refresh recorded in [15-propagation-registry-v2-layered-first-refresh.md](15-propagation-registry-v2-layered-first-refresh.md) and `artifacts/02-06`.
