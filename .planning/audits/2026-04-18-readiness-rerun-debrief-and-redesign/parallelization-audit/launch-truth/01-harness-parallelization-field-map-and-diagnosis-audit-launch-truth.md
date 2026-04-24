Date: 2026-04-22
Status: completed launch-truth record

# Harness Parallelization Field Map And Diagnosis Audit Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `6f2dc74`
- [e:c+i] Packet:
  - [../packets/01-harness-parallelization-field-map-and-diagnosis-audit-packet.md](../packets/01-harness-parallelization-field-map-and-diagnosis-audit-packet.md)
- [e:c+i] Spec:
  - [../specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md](../specs/01-harness-parallelization-field-map-and-diagnosis-audit-spec.md)
- [e:c+i] Opus prompt:
  - [../prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md](../prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md)

## Requested Output

- [e:c+i] Final lane output:
  - [../outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md](../outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md)
- [e:c+i] Local inheritance:
  - [../dispositions/01-harness-parallelization-field-map-and-diagnosis-audit-inheritance.md](../dispositions/01-harness-parallelization-field-map-and-diagnosis-audit-inheritance.md)

## Requested Launch Mode

- [d:r:i] Requested operator-facing model / reasoning: `Opus 4.7 Max` / `xhigh`
- [d:r:i] Effective Claude model string requested on every attempt: `opus[1m]`
- [d:r:i] Launch mode on every attempt: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`

## Attempt 1: full packet reread

- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label parallelization-audit-01 --model 'opus[1m]' --effort xhigh --dangerously-skip-permissions --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01 --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/prompts/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-launch-prompt.md > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/probe-summary.txt`
- [e:c+i] Parent exec session id:
  - `23887`
- [d:r:i] Pre-launch estimate:
  - `14-22 minutes`
- [e:c+i] Repo-local artifacts:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/probe-summary.txt`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/parallelization-audit-01-20260422-222056.dkqbcr7b.stream.jsonl`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/parallelization-audit-01-20260422-222056.l0sg6lnx.stderr.log`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01/parallelization-audit-01-20260422-222056.ajq2b5wh.debug.log`
- [e:c+i] Observed stream fields:
  - first stream timestamp: `2026-04-23T02:21:01.501Z`
  - last stream timestamp: `2026-04-23T02:23:20.127Z`
  - last observed external session id: `63b4e661-0c15-4f1f-a81c-c193bc5ca3d4`
  - recoverable assistant text blocks: `0`
  - result events: `0`
- [e:c+i] Outcome:
  - the run never wrote the requested audit output
  - the probe summary file remained empty
  - the stream shows repeated `Read` calls across the oversized governance/workflow frontier, then stops before any final judgment
  - the stalled-attempt evidence is preserved at [../artifacts/01-harness-parallelization-field-map-and-diagnosis-audit-attempt-1-stall.md](../artifacts/01-harness-parallelization-field-map-and-diagnosis-audit-attempt-1-stall.md)
- [d:r:i] Consequence:
  - do not treat attempt `1` as a finished lane return
  - preserve the stall evidence
  - open a compact retry under the same lane

## Compact Retry Prepared

- [e:c+i] Compact retry packet:
  - [../packets/01b-harness-parallelization-field-map-and-diagnosis-audit-compact-packet.md](../packets/01b-harness-parallelization-field-map-and-diagnosis-audit-compact-packet.md)
- [e:c+i] Compact retry prompt:
  - [../prompts/01b-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-compact-launch-prompt.md](../prompts/01b-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-compact-launch-prompt.md)
- [d:r:i] Compact retry estimate:
  - `8-14 minutes`

## Attempt 2: compact retry launch

- [d:r:i] Frozen launch basis commit for the compact retry: `8d9111d`
- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label parallelization-audit-01b --model 'opus[1m]' --effort xhigh --dangerously-skip-permissions --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01b --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/prompts/01b-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1-compact-launch-prompt.md > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01b/probe-summary.txt`
- [e:c+i] Parent exec session id:
  - `8307`
- [e:c+i] Repo-local artifacts:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01b/probe-summary.txt`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01b/parallelization-audit-01b-20260422-222817.jj2bdmk9.stream.jsonl`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01b/parallelization-audit-01b-20260422-222817.rryv4rl3.stderr.log`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/parallelization-audit/logs/01b/parallelization-audit-01b-20260422-222817.7_irxt93.debug.log`
- [e:c+i] Observed stream fields:
  - first stream timestamp: `2026-04-23T02:28:22.944Z`
  - last stream timestamp: `2026-04-23T02:33:53.324Z`
  - observed stream elapsed seconds: `330.380`
  - last observed external session id: `9f42fe52-4e38-41f3-8474-18aa51e5a9ec`
  - recoverable assistant text blocks: `2`
  - result events: `0`
- [e:c+i] Outcome:
  - the compact retry wrote the requested audit output to [../outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md](../outputs/01-harness-parallelization-field-map-and-diagnosis-audit-opus47-max-r1.md)
  - the wrapper never flushed `probe-summary.txt`
  - a late write-tool correction appears in the stream, but the final output file is complete and well-formed
  - after the file stabilized and the wrapper remained hung, the local operator cut the lingering wrapper process instead of waiting for a summary that was not going to flush
- [d:r:i] Calibration note:
  - the compact retry estimate `8-14 minutes` overshot the useful return time; the audit artifact was written in roughly `5.5 minutes`, and the remaining wall time was wrapper hang rather than model latency
