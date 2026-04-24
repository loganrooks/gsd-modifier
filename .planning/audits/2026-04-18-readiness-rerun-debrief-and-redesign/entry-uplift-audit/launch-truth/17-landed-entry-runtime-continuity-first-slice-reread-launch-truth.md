Date: 2026-04-22
Status: completed launch-truth capture

# Landed Entry Runtime Continuity First Slice Reread Launch Truth

- [g:r:i] Lane label:
  - `landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1`
- [g:r:i] Requested model / reasoning:
  - `opus[1m]`
  - `max`
- [g:r:i] Frozen launch basis commit:
  - `6b8f40d`
- [g:r:i] Requested launch mode:
  - headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
  - repo-local packet/spec/prompt paths
  - `--dangerously-skip-permissions`

## Packet Surface

- [e:c+i] Packet:
  - [../packets/23-landed-entry-runtime-continuity-first-slice-reread-packet.md](../packets/23-landed-entry-runtime-continuity-first-slice-reread-packet.md)
- [e:c+i] Governing spec:
  - [../specs/17-landed-entry-runtime-continuity-first-slice-reread-spec.md](../specs/17-landed-entry-runtime-continuity-first-slice-reread-spec.md)
- [e:c+i] Launch prompt:
  - [../prompts/17-landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1-launch-prompt.md](../prompts/17-landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1-launch-prompt.md)

## Timing Calibration

- [d:r:i] Pre-launch estimate:
  - `8-12 minutes`
- [e:c+i] Actual elapsed seconds:
  - `494.153`
- [d:r:i] Actual elapsed:
  - `8 minutes 14.153 seconds`
- [d:r:i] Calibration note:
  - landed inside the estimate and behaved like a real landed-slice reread rather than a compact same-carrier harden pass; future slices of similar packet size should still be budgeted in the high-single-digit-minute band rather than short polls

## Probe Summary

- [e:c+i] Exit code:
  - `0`
- [e:c+i] Session id:
  - `66109058-67c2-4732-942d-716ca887b756`
- [e:c+i] Total cost usd:
  - `2.8653725`
- [e:c+i] Probe artifacts:
  - stream: `/tmp/landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1-20260422-050859.pesgbj6y.stream.jsonl`
  - stderr: `/tmp/landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1-20260422-050859.sdudz6v4.stderr.log`
  - debug: `/tmp/landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1-20260422-050859.2rex8wfp.debug.log`

## Output Path

- [g:r:i] Reserved output:
  - [../outputs/21-landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1.md](../outputs/21-landed-entry-runtime-continuity-first-slice-reread-opus47-max-r1.md)
