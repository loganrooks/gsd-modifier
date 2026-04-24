# Decision

## Selected Option

Option A: Repo-Owned Runtime-Neutral Wrapper.

## Decision

Create a modifier-owned instruction generator wrapper at:

```text
tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs
```

Materialize it for both supported runtime roots as:

```text
get-shit-done/bin/generate-instruction.cjs
```

Update `new-project.md` to call the wrapper from the runtime root matching the detected `RUNTIME`:

```bash
node "$GSD_INSTRUCTION_GENERATOR" --output "$INSTRUCTION_FILE" --runtime "$RUNTIME"
```

The generated target policy is `AGENTS.md` only for the current supported shared initialization workflow.

The body semantics must be runtime-neutral: the generated file may mention agents and GSD commands, but must not describe the file as `CLAUDE.md` or tell readers that the body is Claude-specific.

The conflict policy is marker-section refresh:

- create `AGENTS.md` if absent;
- replace existing GSD-managed sections when markers exist;
- append missing GSD-managed sections to an existing file;
- preserve content outside GSD markers;
- do not overwrite unmarked user content.

The verification boundary is source tests plus materialized-runtime proof because `new-project.md` and the new wrapper are runtime-facing overlay entries.

Catalog semantics are unchanged. `CLAUDE.md` remains tracked-only unless a future plan proves it should become a generated companion.

## Why This Option

Observed facts:

- The SDK command used by the workflow does not write the requested file.
- The installed CJS writer writes a file, but its installed template is a `CLAUDE.md` generator.
- The current shared workflow is materialized for both Codex and Claude.
- The accepted modifier posture uses `AGENTS.md` as the instruction file for this initialization route.

Inference:

A repo-owned wrapper is safer than a direct CJS correction because it separates the modifier's `AGENTS.md` authority contract from the upstream command's Claude-named history and from runtime-specific materialized template drift.

## Rejected Or Deferred Options

- Option B is rejected for this slice because leaving the workflow unchanged would preserve a known false file-write claim in `new-project.md`.
- Option C is rejected because the available CJS command is not semantically neutral across materialized runtime roots when used to generate `AGENTS.md`.
- Option D is deferred because companion `CLAUDE.md` generation would change catalog semantics and broader authority posture beyond the current narrow defect.

## Authorized Write Set

- `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- focused tests under `tooling/codex/tests/`
- plan-local implementation disposition

## Tests Required

- A focused unit test must prove the wrapper creates `AGENTS.md`.
- A focused unit test must prove the wrapper refreshes only GSD marker sections while preserving unmarked user content.
- A focused contract test must prove `new-project.md` no longer calls `gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"` and does call the repo-owned wrapper.
- Manifest validation must prove the wrapper is materialized for both supported runtimes.
- Materialized verification must be run before claiming runtime parity.
