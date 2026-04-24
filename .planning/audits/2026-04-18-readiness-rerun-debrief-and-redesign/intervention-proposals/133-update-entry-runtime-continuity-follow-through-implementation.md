Date: 2026-04-22
Status: landed first consumer follow-through implementation

# Update Entry Runtime Continuity Follow-Through Implementation

## What Landed

- [d:r:i] The `update` consumer branch now inherits the shared entry/runtime continuity carrier directly.
- [d:r:i] [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md) now:
  - points at `entry-runtime-uplift-continuity.md` from `<supporting_reading>`
  - carries a bounded review step between `keep_route_boundaries_explicit` and `show_changes_and_confirm`
  - gates that step evaluably on `PREFERRED_RUNTIME` being `codex` or `claude` plus repo-local `.codex/` or `.claude/` state
  - keeps the read-only boundary explicit inside the workflow's own voice
  - names the clean-install asymmetry directly: `update` reads the continuity reference before the later clean-install rematerialization rewrites the runtime copy
- [d:r:i] [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md) now carries the wrapper-side boundary at `<objective>`:
  - continuity may surface only for `.codex` / `.claude`
  - this wrapper does not widen that continuity into broader parity, matrix, or version-window claims

## What This Slice Deliberately Did Not Reopen

- [d:r:i] The lane-17 harden items did not travel as fresh work here.
- [d:r:i] They had already landed in commit `6f588ab` at the shared reference, the focused contract test, and the earlier implementation note.
- [d:r:i] This slice therefore stayed narrow:
  - workflow-side pointer plus review beat
  - provider-horizon gate
  - update-side read-only boundary
  - wrapper-side objective sentence
  - focused contract extension
  - re-materialization
  - propagation refresh `49`

## Verification Carry

- [d:r:i] [tooling/codex/tests/test_update_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_update_follow_through_contract.py) now locks the new contract surface explicitly:
  - shared-reference pointer present in `update.md`
  - provider-horizon gate present in `update.md`
  - update-side read-only boundary present in `update.md`
  - clean-install rematerialization asymmetry present in `update.md`
  - wrapper-side continuity boundary present in `gsd-update/SKILL.md`

## Propagation Consequence

- [d:r:i] The matching typed-registry refresh now lands at:
  - [../propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md](../propagation-audit/49-update-entry-runtime-continuity-follow-through-change-triggered-refresh.md)
- [d:r:i] The active compatibility-bearing chain is therefore no longer only:
  - uplift memory anchor
  - current-runtime consumers
  - transition/state preserve-versus-refresh
  - milestone-boundary shared-reference carry
  - repair-facing health continuity
  - earliest-entry shared-reference carry
- [d:r:i] It now also includes:
  - the first workflow-plus-wrapper runtime/package consumer that reads the shared entry/runtime continuity reference under an evaluable provider gate while still keeping broader runtime/package movement, structural-health routing, and later write-side uplift separate

## Next Adjacent Route

- [d:r:i] Inside the uplift continuity family, the next adjacent consumer remains:
  - `from-gsd2`
- [d:r:i] Cross-cutting runtime-specific install-parity work is now explicitly queued, but still separate:
  - [132-codex-claude-installation-parity-audit-deferred-note.md](132-codex-claude-installation-parity-audit-deferred-note.md)
