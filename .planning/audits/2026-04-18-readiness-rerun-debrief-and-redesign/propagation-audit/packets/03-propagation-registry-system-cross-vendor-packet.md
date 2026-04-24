Date: 2026-04-21
Status: frozen review packet

# Propagation Registry System Cross-Vendor Packet

## Purpose

- [g:r:i] This packet asks for a cross-vendor reread of the propagation registry system itself, not only the current `v1` JSON snapshot.
- [g:r:i] The user is explicitly skeptical of a too-code-centric answer and wants the registry family widened toward a stronger hybrid design.
- [g:r:i] The review should challenge the current direction and say how this family could be made more explicit, more controllable, and more useful for propagation-aware work.

## Review Target

- [d:r:i] The governing question is:
  - how should this registry system be layered
  - what should seed it
  - what should remain AI-authored semantic mapping
  - what determinate tooling can legitimately contribute
  - where the current idea of `runtime/tooling evidence` is useful, too vague, too broad, or too compressed

## Current Local Direction To Challenge

- [d:r:i] The current local direction, now written in `14`, is:
  - future refreshes should be AI-authored
  - seeded from maintained docs, especially upstream `docs/INVENTORY.md`
  - then enriched with live runtime/tooling evidence
  - then dispositioned through the prose propagation family
- [d:r:i] This review should not treat that direction as settled. It should challenge, widen, split, or revise it where useful.

## What `Runtime/Tooling Evidence` Currently Refers To

- [d:r:i] The current local meaning is narrower than `all code truth`.
- [d:r:i] It mainly refers to generated or machine-validated surfaces that expose live repo state or contract validation:
  - `UPLIFT-MANIFEST.json`
  - `runtime_visibility.py` outputs and snapshots
  - `OVERLAY-MANIFEST.json` plus `portable_gsd_contract.py` validation/materialization logic
  - `manifest_install_coherence.py` outputs
- [d:r:i] Part of the review target is whether this category is coherent or whether it should be split into more precise layers.

## Read Set

Read these in order:

1. [propagation-audit/README.md](../README.md)
2. [propagation-audit/08-broader-network-producer-consumer-and-carrier-map.md](../08-broader-network-producer-consumer-and-carrier-map.md)
3. [propagation-audit/09-sharpened-propagation-field-split.md](../09-sharpened-propagation-field-split.md)
4. [propagation-audit/10-model-policy-three-surface-invariant.md](../10-model-policy-three-surface-invariant.md)
5. [propagation-audit/11-upstream-pristine-frontier-propagation-obligation.md](../11-upstream-pristine-frontier-propagation-obligation.md)
6. [propagation-audit/12-cross-family-edge-supplement.md](../12-cross-family-edge-supplement.md)
7. [propagation-audit/13-machine-readable-propagation-registry-first-slice.md](../13-machine-readable-propagation-registry-first-slice.md)
8. [propagation-audit/14-propagation-registry-generation-and-seeding-policy.md](../14-propagation-registry-generation-and-seeding-policy.md)
9. [propagation-audit/artifacts/01-propagation-field-registry-v1.json](../artifacts/01-propagation-field-registry-v1.json)
10. [/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md](/home/rookslog/workspace/projects/get-shit-done-upstream/docs/INVENTORY.md)
11. [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md)
12. [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
13. [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py)
14. [tooling/codex/portable_gsd_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py)
15. [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
16. [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)

## Desired Effect

- [d:r:i] The review should help answer:
  - what this registry system should become
  - what the maintained inventory frontier should own
  - what the propagation prose family should continue to own
  - what generated or validated artifacts should contribute without overclaiming semantic completeness
  - what bounded next design step would strengthen the family most
