# Runtime Path Contract

## Observed Facts

- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` maps `get-shit-done/workflows/new-project.md` to both Codex and Claude materializers.
- Both materializers use `mode: overwrite` and source `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`.
- The shared workflow therefore affects both `.codex/get-shit-done/workflows/new-project.md` and `.claude/get-shit-done/workflows/new-project.md` after materialization.
- Repo-local materialized runtime roots currently exist for both `.codex` and `.claude`.
- Existing materialized Codex and Claude roots both contain `get-shit-done/bin/gsd-tools.cjs`.
- Existing workflow and skill surfaces often call `__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs`, but this plan's target command is in a shared initialization workflow that is explicitly materialized for both Codex and Claude.
- `scripts/setup-portable-gsd-runtime.sh --runtime both` is the canonical materialization entrypoint for both runtime roots.
- `portable_gsd_contract.py validate-manifest . --all-supported --strict` checks source and materialized manifest coherence.
- `portable_gsd_contract.py verify-materialized . --all-supported --strict` checks materialized runtime output against the overlay contract.

## Inferences

- A command path embedded in `new-project.md` should not assume the Codex root when running from the Claude materialized workflow.
- A source-valid command is not enough here because `new-project.md` is runtime-facing and materialized into both supported runtime roots.
- The workflow should derive the runtime root from the same `RUNTIME` value it already computes, then call a wrapper materialized into that runtime root.
- If the workflow command changes, materialized-runtime checks are required before claiming parity.
- The supported proof boundary for this slice is Codex plus Claude. Other runtime names appear in detection prose, but the current overlay manifest only materializes this workflow for Codex and Claude.
