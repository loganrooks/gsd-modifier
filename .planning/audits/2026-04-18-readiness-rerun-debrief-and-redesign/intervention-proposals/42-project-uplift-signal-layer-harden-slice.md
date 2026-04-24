Date: 2026-04-21
Status: landed harden slice

# Project-Uplift Signal-Layer Harden Slice

## Purpose

- [g:r:i] This note records the bounded harden slice that lane-04 explicitly earned after the landed first-slice reread.
- [g:r:i] The job of this slice is not to widen project uplift into additive install, cross-runtime reconciliation, or broader entry-family composition. Its job is to make the existing first slice sharper, cleaner, and less ambiguous before wider families inherit it.

## What Landed

- [e:r:i] `tooling/codex/project_uplift.py` now carries multi-axis posture rather than a single flattened class:
  - `project_class` remains the primary route
  - `secondary_signals` now preserve orthogonal pressure such as `mid_phase`
- [e:r:i] The helper now records a bounded `phase_boundary_signal` drawn from active phase `CONTEXT.md` carry instead of inferring mid-phase posture only from coarse project status.
- [e:r:i] The carrier model is now sharper:
  - per-carrier `fingerprint_shape`
  - normalized TOML hashes for runtime-registry carriers
  - marker-local block hashes for strengthening carriers
  - narrower fingerprint semantics for `LONG-ARC.md` and tooling inventory carry
- [e:r:i] Runtime-registry carry is now inventory-based rather than hardcoded: the helper reads `.codex/agents/*.toml` and records the full current runtime agent cohort.
- [e:r:i] Doctrine-sensitive proposal routes are now typed more clearly:
  - `absent`
  - `drifted`
- [e:r:i] Held-later families are no longer ambient Python constants only; they now also live in [tooling/codex/UPLIFT-HELD-LATER.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/UPLIFT-HELD-LATER.md).
- [e:r:i] The overlay workflow and `progress` consumer now carry the stronger signal vocabulary:
  - secondary signals
  - typed doctrine-sensitive proposal states
- [e:r:i] The durable uplift outputs were rewritten on the stronger schema:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - the `Project Uplift` section in [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)

## Additional Corrections Surfaced By The Harden Slice

- [e:r:i] The harden pass surfaced one live consumer bug: `progress-note` was still reading stored pending doctrine-sensitive proposals from the old manifest rather than current analyzed ones. That meant live doctrine drift could stay hidden after the contract surface moved.
- [e:r:i] The harden pass surfaced one durable-output bug: a `--write` run could preserve transient pre-write drift language in the post-write manifest and state surfaces.
- [e:r:i] Both bugs are now corrected in the helper:
  - `progress-note` reads current analyzed proposal routes
  - post-write analysis clears transient `drifted` state and recomputes the stored recommendation layer on the new basis

## Verification And Review Gates

### Tooling Gates

- [e:r:i] `python3 -m py_compile tooling/codex/project_uplift.py`
- [e:r:i] `python3 -m unittest tooling.codex.tests.test_project_uplift`

### Behavior Gates

- [e:r:i] The widened synthetic verification now covers:
  - cross-runtime primary posture preserving `mid_phase` as a secondary signal
  - marker-local fingerprints remaining stable under unrelated whitespace outside the marker block
  - globbed runtime-agent inventory
  - `drifted` doctrine-sensitive proposal detection after later contract movement
- [e:r:i] The helper was rerun on this repo with durable output write plus read-only progress reread.
- [e:r:i] `./scripts/setup-portable-gsd.sh` was rerun so the live `.codex` runtime inherits the tracked overlay changes rather than depending on an unmaterialized local patch.

### Governance Gates

- [e:r:i] The touched uplift and tooling surfaces were contextually reread for binary-gate residue during this slice.
- [d:r:i] Later scanner-side-effects audit pressure now sharpens this boundary further: explicit anti-pattern naming remains allowed where the file itself is teaching what to avoid, and heuristic scan results do not govern wording by themselves. See [threshold-audit/dispositions/03-threshold-scanner-side-effects-internal-audit.md](../threshold-audit/dispositions/03-threshold-scanner-side-effects-internal-audit.md).
- [e:r:i] `audit_refmap.py verify` still reports `0` missing local links for this audit root.
- [e:r:i] `git diff --check` passes for the batch.

## Current Repo Result

- [e:r:i] The current repo now records:
  - primary posture: `cross-runtime uplift`
  - secondary signal: `mid_phase`
  - phase boundary signal: active phase `CONTEXT.md` carries explicit rerun-boundary posture
  - no currently pending doctrine-sensitive proposal routes after the post-write refresh
- [d:r:i] This is a stronger local baseline than the earlier first slice because the helper no longer collapses orthogonal posture into one bucket and no longer leaves transient recommendation noise in durable memory.

## What This Slice Still Holds

- [d:r:i] This slice still does not widen into:
  - additive install routes
  - cross-runtime reconciliation
  - upstream-template drift machinery
  - aged-bespoke uplift
  - wider entry-hook consumers beyond `progress`
- [d:r:i] Those routes remain explicit later families rather than being folded into the signal-layer pass.

## Current Consequence

- [d:r:i] The project-uplift family now has a cleaner signal layer for later inheritance and for later propagation scrutiny.
- [d:r:i] The next stronger move is no longer another local uplift reread.
- [d:r:i] The next stronger move is to open the broader contract-propagation / dependency-carry audit family on this cleaner basis.
