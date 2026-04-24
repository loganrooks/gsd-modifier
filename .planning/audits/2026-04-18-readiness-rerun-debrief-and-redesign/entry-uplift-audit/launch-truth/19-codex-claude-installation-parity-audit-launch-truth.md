Date: 2026-04-22
Status: launched capture

# Codex Claude Installation Parity Audit Launch Truth

- [g:r:i] Lane label:
  - `codex-claude-installation-parity-audit-opus47-max-r1`
- [g:r:i] Requested model / reasoning:
  - `opus[1m]`
  - `max`
- [g:r:i] Frozen launch basis commit:
  - `a75cfe7`
- [g:r:i] Requested launch mode:
  - headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
  - repo-local packet/spec/prompt paths
  - `--dangerously-skip-permissions`

## Packet Surface

- [e:c+i] Packet:
  - [../packets/25-codex-claude-installation-parity-audit-packet.md](../packets/25-codex-claude-installation-parity-audit-packet.md)
- [e:c+i] Governing spec:
  - [../specs/19-codex-claude-installation-parity-audit-spec.md](../specs/19-codex-claude-installation-parity-audit-spec.md)
- [e:c+i] Launch prompt:
  - [../prompts/19-codex-claude-installation-parity-audit-opus47-max-r1-launch-prompt.md](../prompts/19-codex-claude-installation-parity-audit-opus47-max-r1-launch-prompt.md)

## Timing Calibration

- [d:r:i] Pre-launch estimate:
  - `12-18 minutes`
- [d:r:i] Calibration note:
  - wider than the last adjacent reread because it compares upstream installer behavior, repo-local materialization, runtime-specific references, and contextual-vs-real `.claude` warnings across two runtimes

## Output Path

- [g:r:i] Reserved output:
  - [../outputs/23-codex-claude-installation-parity-audit-opus47-max-r1.md](../outputs/23-codex-claude-installation-parity-audit-opus47-max-r1.md)

## Probe Status

- [e:r:i] Local monitoring session:
  - `63520`
- [e:r:i] Actual elapsed:
  - `786.116 seconds`
- [e:r:i] Exit code:
  - `0`
- [e:r:i] Claude session id:
  - `26c23312-de91-4bcb-85ba-d83e761a2a12`
- [e:r:i] Total cost usd:
  - `4.14505825`
- [e:r:i] Temp artifacts:
  - `/tmp/codex-claude-installation-parity-audit-opus47-max-r1-20260422-060042.n3yj88n0.stream.jsonl`
  - `/tmp/codex-claude-installation-parity-audit-opus47-max-r1-20260422-060042.l8sfr70c.stderr.log`
  - `/tmp/codex-claude-installation-parity-audit-opus47-max-r1-20260422-060042.8fwx94vl.debug.log`
- [d:r:i] Calibration note:
  - actual runtime landed inside the `12-18 minute` estimate window at roughly `13.1 minutes`, which fits the lane shape better than the earlier shorter waits did
