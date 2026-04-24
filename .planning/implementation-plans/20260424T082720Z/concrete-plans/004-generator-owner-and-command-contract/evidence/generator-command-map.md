# Generator Command Map

## Observed Facts

- Current branch: `main`.
- Current HEAD before edits: `a5d32c2`.
- Worktree before edits: clean.
- Repo overlay workflow: `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md`.
- The repo overlay detects runtime from execution context or runtime env vars, but sets `INSTRUCTION_FILE="AGENTS.md"` for Codex and for all non-Codex runtimes.
- The repo overlay later calls:

```bash
gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"
```

- The repo overlay lists `$INSTRUCTION_FILE` as `AGENTS.md` for Codex and `AGENTS.md` for all other runtimes in output and success criteria.
- Installed upstream workflow at `/home/rookslog/.npm/_npx/9785a834b31d581d/node_modules/get-shit-done-cc/get-shit-done/workflows/new-project.md` sets `INSTRUCTION_FILE="AGENTS.md"` for Codex and `INSTRUCTION_FILE="CLAUDE.md"` otherwise.
- Installed upstream uses the same `gsd-sdk query generate-claude-md --output "$INSTRUCTION_FILE"` command.
- `gsd-sdk` resolves to `/home/rookslog/.npm-global/bin/gsd-sdk`.
- `readlink -f $(which gsd-sdk)` resolves to `/home/rookslog/.npm/_npx/9785a834b31d581d/node_modules/get-shit-done-cc/sdk/dist/cli.js`.
- The SDK registry imports `generateClaudeMd` from `sdk/dist/query/profile.js` and includes `generate-claude-md` in the mutation command set.
- The SDK handler signature is `generateClaudeMd = async (_args, projectDir)`.
- The SDK handler ignores command args, including `--output`.
- The SDK handler reads `.planning/PROJECT.md`, `.planning/codebase/STACK.md`, and `.planning/research/STACK.md`, then returns JSON sections.
- Probe command:

```bash
rm -f /tmp/gsd-modifier-generated-instruction-probe.md
gsd-sdk query generate-claude-md --output /tmp/gsd-modifier-generated-instruction-probe.md
test -e /tmp/gsd-modifier-generated-instruction-probe.md
```

returned JSON from `gsd-sdk` and did not create the output file.
- Installed CJS command exists at `/home/rookslog/.npm/_npx/9785a834b31d581d/node_modules/get-shit-done-cc/get-shit-done/bin/gsd-tools.cjs`.
- Installed CJS dispatch includes `generate-claude-md`, parses `--output`, `--auto`, and `--force`, and routes to `profileOutput.cmdGenerateClaudeMd`.
- The materialized repo-local runtime roots also contain CJS writers at `.codex/get-shit-done/bin/gsd-tools.cjs` and `.claude/get-shit-done/bin/gsd-tools.cjs`.
- The source overlay currently has no repo-owned instruction generator wrapper.

## Inferences

- The current workflow command is a false file-write contract: it can succeed while leaving `$INSTRUCTION_FILE` absent.
- The all-`AGENTS.md` target policy is a modifier overlay decision, not the installed upstream default.
- Directly switching the workflow to the CJS command would repair file creation, but it would bind the modifier's `AGENTS.md` policy to runtime-specific materialized CJS/template bodies whose semantics differ between Codex and Claude roots.
- A repo-owned wrapper is the least ambiguous ownership boundary because it can name `AGENTS.md` as the target, define runtime-neutral body semantics, and use one command contract for both materialized runtimes.
