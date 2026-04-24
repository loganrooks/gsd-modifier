Date: 2026-04-22
Status: active launch-truth record

# Harness Extraction Field Map Audit Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `fc3275f`
- [e:c+i] Packet: [../packets/01-harness-extraction-field-map-audit-packet.md](../packets/01-harness-extraction-field-map-audit-packet.md)
- [e:c+i] Spec: [../specs/01-harness-extraction-field-map-audit-spec.md](../specs/01-harness-extraction-field-map-audit-spec.md)
- [e:c+i] Opus prompt: [../prompts/01-harness-extraction-field-map-audit-opus47-max-r1-launch-prompt.md](../prompts/01-harness-extraction-field-map-audit-opus47-max-r1-launch-prompt.md)

## Requested Output

- [e:c+i] Final lane output:
  - [../outputs/01-harness-extraction-field-map-audit-opus47-max-r1.md](../outputs/01-harness-extraction-field-map-audit-opus47-max-r1.md)

## Requested Launch Mode

- [d:r:i] Requested operator-facing model / reasoning: `Opus 4.7 Max` / `xhigh`
- [d:r:i] Effective Claude model string: `opus[1m]`
- [d:r:i] Launch mode: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`
- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label extraction-audit-01 --model 'opus[1m]' --effort xhigh --dangerously-skip-permissions --output-dir .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01 --prompt-file .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/prompts/01-harness-extraction-field-map-audit-opus47-max-r1-launch-prompt.md > .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01/probe-summary.txt`

## Timing

- [d:r:i] Pre-launch estimate: `14-22 minutes`
- [e:c+i] Actual elapsed seconds: `410.115`
- [d:r:i] Timing calibration: much shorter than expected at roughly `6.8 minutes`; the lane behaved like a bounded structural field-map reread rather than a broader multi-family packaging or migration audit.

## Launch Note

- [d:r:i] The first shell attempt only failed because the repo-local logs directory had not been created yet.
- [d:r:i] The lane was relaunched immediately after creating `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01/`.

## Return Summary

- [e:c+i] Exit code: `0`
- [e:c+i] Session id: `79650535-0a1a-4d0c-bbba-765e1e8803c5`
- [e:c+i] Total cost usd: `2.4960592499999996`
- [e:c+i] Repo-local artifacts:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01/probe-summary.txt`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01/extraction-audit-01-20260422-150133.tf9fstrc.stream.jsonl`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01/extraction-audit-01-20260422-150133.zex3wpon.stderr.log`
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/extraction-audit/logs/01/extraction-audit-01-20260422-150133.4xbvmstp.debug.log`
