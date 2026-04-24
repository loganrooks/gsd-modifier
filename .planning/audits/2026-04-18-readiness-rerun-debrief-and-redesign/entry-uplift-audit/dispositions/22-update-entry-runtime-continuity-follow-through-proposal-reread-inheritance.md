Date: 2026-04-22
Status: completed local inheritance

# Update Entry Runtime Continuity Follow-Through Proposal Reread Inheritance

## Local Disposition

- [d:r:i] `accept with local revision and landed consumer follow-through`
- [d:r:i] Lane `18` keeps the `update + gsd-update` branch as the next adjacent consumer after the landed earliest-entry pair.
- [d:r:i] The main correction is scope, not route reversal:
  - the lane-17 harden items had already landed
  - the current slice should not pretend to be redoing them
  - the real work is the workflow-side pointer and review beat, the provider-horizon gate, the wrapper-side boundary, the focused contract extension, the re-materialization, and propagation refresh `49`

## Carry Forward

- [d:r:i] Keep `update.md` plus `gsd-update/SKILL.md` ahead of `from-gsd2` as the next adjacent consumer order.
- [d:r:i] Keep the shared entry/runtime continuity reference as the continuity carrier:
  - `entry-runtime-uplift-continuity.md`
- [d:r:i] Keep the workflow-side review beat between `compare_versions` and `show_changes_and_confirm`.
- [d:r:i] Keep the provider-horizon gate evaluable:
  - `PREFERRED_RUNTIME` is `codex` or `claude`
  - repo-local `.codex/` or `.claude/` state is present
- [d:r:i] Keep the update-side read-only boundary explicit:
  - do not run `$gsd-uplift-project --write` from `update.md`
- [d:r:i] Keep the wrapper-side boundary at `<objective>` instead of duplicating workflow-step content in the wrapper.
- [d:r:i] Keep `mandatory-initial-read.md` grammar-only through this slice.
- [d:r:i] Keep the clean-install asymmetry explicit:
  - `update` reads the continuity reference before the later rematerialization rewrites the runtime copy

## Revise In The Proposal Layer

- [d:r:i] Proposal `131` should stop describing the lane-17 harden as pending same-batch work and instead state that commit `6f588ab` already landed that harden in-place.
- [d:r:i] Proposal `131` should name propagation refresh slot `49` rather than leaving the slot ambient.
- [d:r:i] Proposal `131` should separate the workflow-side job from the wrapper-side job, instead of stating them as near-parallel without carrier distinction.

## Land Now

- [d:r:i] The landed implementation note is:
  - [../../intervention-proposals/133-update-entry-runtime-continuity-follow-through-implementation.md](../../intervention-proposals/133-update-entry-runtime-continuity-follow-through-implementation.md)
- [d:r:i] The matching propagation refresh is:
  - [../../propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md](../../propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md)

## Keep Later

- [d:r:i] `from-gsd2` wrapper carry as the next adjacent consumer after this slice.
- [d:r:i] Narrowing the broader multi-provider `RUNTIME_DIRS` block.
- [d:r:i] `.claude` translation or broader parity claims inside this slice.
- [d:r:i] Matrix, version-window, or standalone compatibility-carrier widening.
- [d:r:i] Extraction and npm/`npx` distribution from `115`.
- [d:r:i] The bounded `.codex` / `.claude` installation-parity audit until this `update` consumer branch is fully settled and checkpointed.

## Next Bounded Move

- [d:r:i] After this consumer branch settles, open the deferred runtime-specific install-parity audit recorded at:
  - [../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md](../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md)
