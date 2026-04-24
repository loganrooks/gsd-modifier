Date: 2026-04-22
Status: active bounded proposal

# Update Entry Runtime Continuity Follow-Through Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent consumer branch after the landed and reread entry/runtime shared-reference first slice.
- [g:r:i] The question here is not whether the shared-reference family should exist.
- [g:r:i] The question is how `update.md` plus `gsd-update` should inherit that continuity surface without:
  - collapsing runtime/package movement into broader posture uplift
  - silently broadening provider-horizon claims
  - reopening `from-gsd2` at the same time

## Why This Branch Now

- [d:r:i] Lane `17` kept the landed first slice and pressed the next adjacent move toward `update` plus `gsd-update` rather than another same-slice reread loop.
- [d:r:i] `update` is the first workflow-plus-wrapper consumer branch after the earliest-entry pair.
- [d:r:i] That makes it the right place to prove the shared continuity surface across:
  - one workflow carrier
  - one wrapper carrier
  - one runtime/package-owner route that already separates structural health and later uplift

## Proposed Slice

- [d:r:i] Teach [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md) to point directly at `entry-runtime-uplift-continuity.md` as a bounded supporting continuity surface and to surface one explicit review beat between `compare_versions` and `show_changes_and_confirm`.
- [d:r:i] Teach [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md) to preserve the same continuity route at the wrapper boundary, specifically at `<objective>`.
- [d:r:i] Treat the lane-17 reference-side harden as already landed in commit `6f588ab`, not as pending work inside this slice:
  - early compact-read provider-horizon wording in the reference
  - greenfield route-evaluable trigger
  - explicit entry-side `_when_present` asymmetry
  - widened focused contract test
  - clarified implementation note carry for overlay ownership
- [d:r:i] Keep `update` route ownership explicit:
  - runtime/package movement first
  - structural-health route separate
  - later write-side uplift route separate

## What This Slice Should Carry More Explicitly

- [d:r:i] When `update` is run in this repo, entry/runtime continuity should remain readable as:
  - observed `.codex` basis
  - held `.claude` annotation
  - optional compact `Project Uplift` digest when present
- [d:r:i] The continuity surface should help the operator understand repo-local continuity after update movement, before the clean-install step rewrites the runtime copy of the reference via overlay rematerialization.
- [d:r:i] The continuity surface should surface only when `PREFERRED_RUNTIME` is `codex` or `claude` and repo-local `.codex/` or `.claude/` state is present.
- [d:r:i] It should not flatten runtime/package movement, structural repair, and later posture refresh into one blended update story.
- [d:r:i] `mandatory-initial-read.md` should remain grammar-only through this slice; the sibling reference stays the content-bearing continuity carrier.

## Verification

- [d:r:i] Add focused contract coverage for:
  - `update.md` pointing at the shared reference
  - the provider-horizon gate inside `update.md`
  - the update-side read-only boundary line
  - `gsd-update` preserving the wrapper-side boundary sentence at `<objective>`
  - continued separation between update-owned movement, structural-health routing, and later write-side uplift refresh
- [d:r:i] Re-materialize the overlay into live `.codex` after the overlay edits.
- [d:r:i] Refresh the typed propagation family in the same batch at slot `49` because a new consumer branch and wrapper edge will move.

## Hold Outside This Slice

- [d:r:i] `from-gsd2` wrapper carry.
- [d:r:i] Narrowing the broader runtime-detection prose across all supported providers.
- [d:r:i] `.claude` translation or parity work.
- [d:r:i] Matrix, version-window, or standalone compatibility-carrier widening.
- [d:r:i] Extraction and npm/`npx` distribution from `115`.

## Next Bounded Objects

- [d:r:i] If accepted, the implementation note should land as:
  - `133-update-entry-runtime-continuity-follow-through-implementation.md`
- [d:r:i] The matching propagation refresh should land as:
  - `propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md`
- [d:r:i] The adjacent runtime-specific install-parity audit stays queued in:
  - [132-codex-claude-installation-parity-audit-deferred-note.md](132-codex-claude-installation-parity-audit-deferred-note.md)
