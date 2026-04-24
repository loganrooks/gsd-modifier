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
