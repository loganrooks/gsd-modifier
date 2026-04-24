# Entry Uplift Audit Launch Truth: Field Mapping

Status: completed and inherited  
Date: 2026-04-21

## Frozen Basis

- frozen launch basis commit: `73d4fb4`
- packet: [../packets/01-entry-surface-and-project-uplift-field-mapping-packet.md](../packets/01-entry-surface-and-project-uplift-field-mapping-packet.md)
- spec: [../specs/01-entry-surface-and-project-uplift-field-mapping-spec.md](../specs/01-entry-surface-and-project-uplift-field-mapping-spec.md)
- Opus prompt: [../prompts/01-entry-surface-and-project-uplift-field-mapping-opus47-max-r1-launch-prompt.md](../prompts/01-entry-surface-and-project-uplift-field-mapping-opus47-max-r1-launch-prompt.md)

## Requested Output

- Opus output:
  - [../outputs/01-entry-surface-and-project-uplift-field-mapping-opus47-max-r1.md](../outputs/01-entry-surface-and-project-uplift-field-mapping-opus47-max-r1.md)
- local inheritance:
  - [../dispositions/01-entry-surface-and-project-uplift-field-mapping-inheritance.md](../dispositions/01-entry-surface-and-project-uplift-field-mapping-inheritance.md)

## Request-Surface Language Check

- `python3 tooling/codex/scan_threshold_language.py` was run against:
  - [../README.md](../README.md)
  - [../packets/01-entry-surface-and-project-uplift-field-mapping-packet.md](../packets/01-entry-surface-and-project-uplift-field-mapping-packet.md)
  - [../specs/01-entry-surface-and-project-uplift-field-mapping-spec.md](../specs/01-entry-surface-and-project-uplift-field-mapping-spec.md)
  - [../prompts/01-entry-surface-and-project-uplift-field-mapping-opus47-max-r1-launch-prompt.md](../prompts/01-entry-surface-and-project-uplift-field-mapping-opus47-max-r1-launch-prompt.md)
- scanner result: `No threshold-language residue found.`

## Requested Launch Mode

- Opus:
  - operator-facing model / reasoning: `Opus 4.7 Max` / `max`
  - effective Claude model string: `opus[1m]`
  - mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
  - live command / process evidence:
    - `python3 tooling/codex/run_claude_probe.py --label entry-surface-and-project-uplift-field-mapping-opus47-max-r1 --model opus[1m] --effort max --prompt-file ... --dangerously-skip-permissions`
    - child process observed as `claude -p --dangerously-skip-permissions --model opus[1m] --effort max ...`

## Return Summary

- Opus:
  - exit code: `0`
  - elapsed seconds: `525.924`
  - session id: `a8acb26b-956e-4a63-9206-3b49439e8605`
  - total cost usd: `3.64128525`
  - stdout/stderr/debug artifacts:
    - `/tmp/entry-surface-and-project-uplift-field-mapping-opus47-max-r1-20260421-025208.7k046cof.stream.jsonl`
    - `/tmp/entry-surface-and-project-uplift-field-mapping-opus47-max-r1-20260421-025208.qe3alf9n.stderr.log`
    - `/tmp/entry-surface-and-project-uplift-field-mapping-opus47-max-r1-20260421-025208.sqoaootx.debug.log`

## Current Consequence

- [g:r:i] This lane is complete and now has a local inheritance note.
- [d:r:i] The current move is to carry the widened map into a revision of `37` before workflow-design artifact `38` is written.
