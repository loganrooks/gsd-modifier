Date: 2026-04-23
Status: completed refresh

# Responsible Closure Shipped/Install Contract Classification First Slice Change-Triggered Refresh

## Trigger

- [d:r:i] [../intervention-proposals/180-harness-modifier-shipped-install-contract-classification-first-slice-implementation.md](../intervention-proposals/180-harness-modifier-shipped-install-contract-classification-first-slice-implementation.md)

## What Moved

- [d:r:i] Responsible closure now has a first durable shipped/install-contract ledger instead of only a reviewed proposal.
- [d:r:i] The current carried split is now explicit across:
  - runtime-core
  - runtime-support
  - transitional shipped/install support
  - pre-run experimental
  - development-program-only
- [d:r:i] The slice also now preserves two distinctions that were previously easier to blur:
  - installed-but-host-local compact prompts versus generic modifier-owned carry
  - typed shim authority classes instead of one undifferentiated `tooling/codex/*` bucket

## Propagation Consequence

- [d:r:i] Release-readiness and extraction planning now inherit a concrete classified baseline rather than only the orientation artifact in `177` and the revised proposal in `179`.
- [d:r:i] `harness_modifier/README.md` now carries the current shipped/install posture in package-facing form, so the classification result is no longer audit-tree-only memory.
- [d:r:i] The same boundary now also sharpens extracted-project planning: later repo extraction should move the modifier package together with the live overlay/install-materialization contract, and the later `modifier route versus own harness` strategy question is now kept explicit through `181` rather than chat memory alone.
- [d:r:i] The next adjacent move should consume this ledger when shaping:
  - CI tiers
  - install-profile boundaries
  - extracted repo packaging sequence
  - optionality rules

## Held Boundaries

- [d:r:i] This slice does not implement install profiles.
- [d:r:i] This slice does not create CI.
- [d:r:i] This slice does not widen second-host or mixed-runtime exercise coverage.
- [d:r:i] This slice does not reopen `167`.
