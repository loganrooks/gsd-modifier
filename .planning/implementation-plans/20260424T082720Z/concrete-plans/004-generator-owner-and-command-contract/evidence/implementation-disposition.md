# Implementation Disposition

## Selected Option

Option A, corrected: Repo-Owned File-Writing Wrapper With Runtime-Sensitive Targets.

## Files Changed

- `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- `tooling/codex/tests/test_initialization_read_packet_contract.py`
- `.planning/implementation-plans/20260424T082720Z/concrete-plans/004-generator-owner-and-command-contract/evidence/*.md`

## Write Set Basis

- `generate-instruction.cjs` is the selected repo-owned wrapper and owns the file-write contract.
- `new-project.md` is the runtime-facing workflow whose previous SDK command did not write `$INSTRUCTION_FILE`.
- `OVERLAY-MANIFEST.json` is the materialization contract that makes the wrapper available in both supported runtime roots.
- `test_initialization_read_packet_contract.py` already covers the initialization workflow ownership surface, so the command-contract and wrapper behavior tests belong there.
- Plan-local evidence files are required by the executable plan before and after behavior changes.

## Command Contract

`new-project.md` now resolves the runtime root from `RUNTIME`, then runs:

```bash
node "$GSD_INSTRUCTION_GENERATOR" --output "$INSTRUCTION_FILE" --runtime "$RUNTIME"
```

The wrapper contract is:

- output target is the runtime-selected `$INSTRUCTION_FILE`: `AGENTS.md` for Codex and `CLAUDE.md` for Claude/non-Codex;
- body is filename-safe and does not claim that all runtimes should use `AGENTS.md`;
- missing files are created;
- GSD marker sections are refreshed;
- unmarked user content is preserved.

## Tests Run

- `node --check tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs`
- `python3 -m unittest tooling.codex.tests.test_initialization_read_packet_contract`
- `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict`
- `python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')`
- `git diff --check`
- `./scripts/setup-portable-gsd-runtime.sh --runtime both`
- `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict`
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict`
- `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict`

## Materialized Runtime Status

Materialized runtime proof was required because `new-project.md` changed and a new runtime-facing wrapper was added.

Result: both Codex and Claude runtime roots materialized the wrapper and passed strict manifest, materialized coherence, and harness canary checks.

## Intentionally Held Surfaces

- `CLAUDE.md` companion generation remains held, but Claude/non-Codex initialization now preserves the upstream-compatible `CLAUDE.md` target.
- The SDK `generate-claude-md` handler remains an upstream defect or migration gap; this repo no longer depends on it for `new-project.md` instruction-file writes.
- Broader compact-prompt, host-matrix semantics, and governance seeding are unchanged.
- Other runtime names in detection prose are not broadened into support claims; this slice proves Codex and Claude because those are the manifest-supported runtime roots.

## Remaining Risks

- The wrapper is intentionally narrower than the legacy CJS `generate-claude-md` command. If future work wants both generated companion files, richer profile integration, or direct upstream CJS reuse, it should be planned as a separate generated-instruction contract.
- The command name `generate-instruction.cjs` is repo-owned; upstream may later repair SDK generation semantics under a different name. If that happens, this wrapper should be reassessed rather than silently replaced.

## Premise Update — 2026-05-08

The Plan 004 decision was made on 2026-04-24 against upstream evidence that distinguished three states: snapshot v1.36.0, latest npm stable v1.38.3 (where `gsd-sdk query generate-claude-md --output` did not write a file), and upstream `origin/main` (which had a fix in PR #2341 / commit `c5b14455` not yet released).

A subsequent temp handoff (`docs/handoff/DELETE-AFTER-INGESTION-2026-04-24-release-readiness-and-plan-004.md`) framed the modifier wrapper as a possible release-bound shim that should be removed once #2341 shipped in a stable release.

That framing is rejected on the corrected evidence:

- PR #2341 / commit `c5b14455` shipped in `v1.38.4` on 2026-04-25 (one day after the original decision) and is in every stable release through `v1.41.0` (2026-05-07).
- Tag-membership verified by `git tag --contains c5b14455` against `~/workspace/projects/get-shit-done-upstream` (`gsd-build/get-shit-done`), refs refreshed 2026-05-08.

The release-window for a "shim" no longer exists. More importantly, the wrapper is not a shim. It carries modifier-specific content that upstream's `generateClaudeMd` writer does not provide:

- `--runtime` flag for runtime-targeted output path selection (`AGENTS.md` for Codex, `CLAUDE.md` otherwise) — implemented at `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs:56`;
- multi-runtime skill discovery across `.codex/skills/`, `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/` — at `generate-instruction.cjs:47`;
- modifier-owned `## GSD Workflow Enforcement` section content — at `generate-instruction.cjs:29-38`;
- `<!-- GSD:profile-start -->` placeholder for `$gsd-profile-user` — at `generate-instruction.cjs:39-46`;
- marker-section update model preserving user content outside markers — at `generate-instruction.cjs:212-228`.

Upstream's writer is Claude-specific and writes a Claude-context file. Modifier's wrapper is runtime-neutral and writes a runtime-targeted instruction file with multi-runtime content. They are not equivalents; there is no swap.

Conclusion: Option A's selection stands as recorded. The wrapper remains modifier-owned content under `parity_tier: core_required` for both Codex and Claude. The "Remaining Risks" entry that says the wrapper "should be reassessed rather than silently replaced" if upstream later repairs SDK generation under a different name still applies and is reaffirmed.

No source, contract, or manifest changes follow from this update. This entry exists so future readers do not re-litigate the disposition based on the temp handoff's stale framing.

### Evidence reference

Full upstream-gap snapshot, drift inventory, and downstream proposal sequence are recorded in `.planning/readiness/release-readiness-orientation-2026-05-08.md`. That file is a dated snapshot and will be archived after the short-term proposal slice closes.
