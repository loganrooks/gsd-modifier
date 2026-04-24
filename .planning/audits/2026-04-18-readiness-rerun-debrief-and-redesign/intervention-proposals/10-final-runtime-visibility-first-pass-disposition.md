Date: 2026-04-20
Status: local implementation disposition

# Final Runtime Visibility First-Pass Disposition

## Decision

- [d:r:i] Accept the `paired pattern` as the first implementation shape:
  - an on-demand verifier/snapshot command
  - with optional file output when a durable local record is useful
- [d:r:i] Land that first pass as [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:1), not as a rewrite of `gsd-file-manifest.json`.

## Why This Is The Strongest First Shape

- [e:c+i] The manifest semantic contract already ruled out overloading `gsd-file-manifest.json` with final-runtime truth. Sources: [08-manifest-semantic-contract-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/08-manifest-semantic-contract-disposition.md:23), [08-manifest-semantic-contract-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/08-manifest-semantic-contract-disposition.md:49).
- [e:c+i] The bounded follow-through proposal then identified the real design choice as verifier, artifact, or paired pattern. Sources: [09-final-runtime-visibility-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/09-final-runtime-visibility-proposal.md:26), [09-final-runtime-visibility-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/09-final-runtime-visibility-proposal.md:72).
- [d:r:i] The paired pattern is stronger than `artifact only` because it avoids ceremonial stale-state by default.
- [d:r:i] It is stronger than `verifier only` because optional write-out gives later audit/disposition work a durable local record when needed.

## What Landed

- [e:c+i] A new repo-local tool now exists at [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:1).
- [e:c+i] The tool currently covers the high-leverage families named in the proposal: `config.toml`, agent `.toml`, workflows, references, and `bin/lib`. Sources: [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:25), [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:33).
- [e:c+i] It classifies entries as `intentional materialized carry`, `repo-local config carry`, `selective overlay boundary`, or `unknown live drift`, and it can either print JSON or write it to a path with `--output`. Sources: [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:16), [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:82), [tooling/codex/runtime_visibility.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/runtime_visibility.py:225).
- [e:r:i] A local smoke test against the current `.codex` / overlay pair produced `185` entries with:
  - `23` intentional materialized carry
  - `1` repo-local config carry
  - `161` selective overlay boundary
  - `0` unknown live drift
- [d:r:i] That result does not mean the runtime is exhaustive or finished. It does mean the first-pass surface is already separating high-leverage live truth from mystery-drift panic.

## Constraints

- [d:r:i] This first pass does not auto-detect `obsolete live residue`.
- [d:r:i] It also does not yet classify hooks or repo-local skills, because the current bounded scope intentionally stayed with the higher-leverage runtime families from the second-tranche proposal.

## Immediate Next Move

- [g:r:i] Use the landed tool to decide whether the next tightening should be:
  - widening family coverage
  - adding durable ignored snapshots for selected audit lanes
  - or using the current output to sharpen a later overlay-expansion / cleanup decision
