# Decision

## Selected Option

Option A, corrected: Repo-Owned File-Writing Wrapper With Runtime-Sensitive Targets.

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

The generated target policy preserves upstream runtime-sensitive behavior:

- Codex initializes `AGENTS.md`.
- Claude and other non-Codex runtimes initialize `CLAUDE.md`.

The body semantics must be filename-safe: the generated file may mention agents and GSD commands, but must not describe the generator as an `AGENTS.md`-only uplift or force Claude/non-Codex targets into `AGENTS.md`.

The conflict policy is marker-section refresh:

- create the runtime-selected instruction file if absent;
- replace existing GSD-managed sections when markers exist;
- append missing GSD-managed sections to an existing file;
- preserve content outside GSD markers;
- do not overwrite unmarked user content.

The verification boundary is source tests plus materialized-runtime proof because `new-project.md` and the new wrapper are runtime-facing overlay entries.

Catalog semantics are unchanged. `CLAUDE.md` remains a tracked doctrine-sensitive carrier and is also the generated initialization target for Claude/non-Codex runtime branches.

## Why This Option

Observed facts:

- The SDK command used by the workflow does not write the requested file.
- The installed CJS writer writes a file, but using it directly through a shared modifier overlay would reintroduce runtime-root and template ownership ambiguity.
- The current shared workflow is materialized for both Codex and Claude.
- Upstream `new-project.md` is runtime-sensitive: Codex uses `AGENTS.md`; non-Codex uses `CLAUDE.md`.

Inference:

A repo-owned wrapper is safer than leaving the SDK call because it restores a real file-write contract without depending on the SDK handler that ignores `--output`. The wrapper must not be used as a rationale to collapse runtime-selected instruction filenames.

## Rejected Or Deferred Options

- Option B is rejected for this slice because leaving the workflow unchanged would preserve a known false file-write claim in `new-project.md`.
- Option C is rejected for this slice because switching directly to runtime-local CJS generation would change template/body ownership and should be handled with a dedicated upstream-alignment pass if desired.
- Option D is deferred because generating both `AGENTS.md` and a companion file would change catalog semantics and broader authority posture beyond the current narrow defect.

## Authorized Write Set

- `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- focused tests under `tooling/codex/tests/`
- plan-local implementation disposition

## Tests Required

- A focused unit test must prove the wrapper creates `AGENTS.md` when Codex selects that output.
- A focused unit test must prove the wrapper honors `CLAUDE.md` when Claude/non-Codex runtime selection chooses that output.
- A focused unit test must prove the wrapper refreshes only GSD marker sections while preserving unmarked user content.
- A focused contract test must prove `new-project.md` no longer calls `gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"` and does call the repo-owned wrapper.
- Manifest validation must prove the wrapper is materialized for both supported runtimes.
- Materialized verification must be run before claiming runtime parity.
