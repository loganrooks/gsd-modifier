Date: 2026-04-22
Status: completed launch-truth record

# Propagation Review Route Reread Launch Truth

## Frozen Basis

- [g:r:i] Frozen launch basis commit: `306f1d8`
- [e:c+i] Packet: [../packets/07-propagation-review-route-reread-packet.md](../packets/07-propagation-review-route-reread-packet.md)
- [e:c+i] Spec: [../specs/07-propagation-review-route-reread-spec.md](../specs/07-propagation-review-route-reread-spec.md)
- [e:c+i] First reply-only Opus prompt: [../prompts/07-propagation-review-route-reread-opus47-max-r1-reply-launch-prompt.md](../prompts/07-propagation-review-route-reread-opus47-max-r1-reply-launch-prompt.md)
- [e:c+i] Continuation prompt after the first partial: [../prompts/07-propagation-review-route-reread-opus47-max-r1-continuation-launch-prompt.md](../prompts/07-propagation-review-route-reread-opus47-max-r1-continuation-launch-prompt.md)
- [d:r:i] A third compact continuation retry was also used after the second stall, but its oversized embedded packet is not retained as a canonical markdown artifact because it inlined many live markdown links from other docs and would pollute reference verification.

## Requested Output

- [e:c+i] Final lane output:
  - [../outputs/07-propagation-review-route-reread-opus47-max-r1.md](../outputs/07-propagation-review-route-reread-opus47-max-r1.md)
- [e:c+i] Preserved partial from the first stalled attempt:
  - [../artifacts/07-propagation-review-route-reread-opus47-max-r1-attempt-2-partial.md](../artifacts/07-propagation-review-route-reread-opus47-max-r1-attempt-2-partial.md)
- [e:c+i] Local inheritance:
  - [../dispositions/07-propagation-review-route-reread-inheritance.md](../dispositions/07-propagation-review-route-reread-inheritance.md)

## Requested Launch Mode

- [d:r:i] Requested operator-facing model / reasoning: `Opus 4.7 Max` / `max`
- [d:r:i] Effective Claude model string requested on every attempt: `opus[1m]`
- [d:r:i] Launch mode on every attempt: headless Claude CLI probe via `tooling/codex/run_claude_probe.py`

## Attempt Record

### Attempt 1: reply-only full reread

- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label propagation-review-route-reread-opus47-max-r1-reply --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file .../07-propagation-review-route-reread-opus47-max-r1-reply-launch-prompt.md`
- [e:c+i] Parent exec session id: `72835`
- [e:c+i] Temp artifacts:
  - `/tmp/propagation-review-route-reread-opus47-max-r1-reply-20260421-232125.5llij0gn.stream.jsonl`
  - `/tmp/propagation-review-route-reread-opus47-max-r1-reply-20260421-232125.i_7jveln.stderr.log`
  - `/tmp/propagation-review-route-reread-opus47-max-r1-reply-20260421-232125.0o1nieok.debug.log`
- [e:c+i] Outcome:
  - returned full section `1`
  - returned full section `2`
  - began section `3`
  - then stalled without a clean stop or final answer
- [d:r:i] Consequence:
  - preserve the completed portion as evidence
  - do not inherit the incomplete artifact as if it were a finished lane return

### Attempt 2: continuation from the partial

- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label propagation-review-route-reread-opus47-max-r1-continuation --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file .../07-propagation-review-route-reread-opus47-max-r1-continuation-launch-prompt.md`
- [e:c+i] Parent exec session id: `6971`
- [e:c+i] Temp artifacts:
  - `/tmp/propagation-review-route-reread-opus47-max-r1-continuation-20260421-232726.hrms2hgl.stream.jsonl`
  - `/tmp/propagation-review-route-reread-opus47-max-r1-continuation-20260421-232726.405xgmj2.stderr.log`
  - `/tmp/propagation-review-route-reread-opus47-max-r1-continuation-20260421-232726.f906rxg8.debug.log`
- [e:c+i] Outcome:
  - reread the spec
  - reread the preserved partial
  - reread the original packet
  - stalled before producing any final text
- [d:r:i] Consequence:
  - cut the attempt
  - do not treat read-phase movement as a finished review

### Attempt 3: compact continuation packet

- [e:c+i] Command shape:
  - `python3 tooling/codex/run_claude_probe.py --label propagation-review-route-reread-opus47-max-r1-compact-continuation --model 'opus[1m]' --effort max --dangerously-skip-permissions --prompt-file .../07b-propagation-review-route-reread-compact-continuation-opus47-max-r1-launch-prompt.md`
- [e:c+i] Parent exec session id: `30207`
- [e:c+i] Temp artifacts:
  - `/tmp/propagation-review-route-reread-opus47-max-r1-compact-continuation-20260421-232949.9vhc7ib1.stream.jsonl`
  - `/tmp/propagation-review-route-reread-opus47-max-r1-compact-continuation-20260421-232949.0s0sxpm7.stderr.log`
  - `/tmp/propagation-review-route-reread-opus47-max-r1-compact-continuation-20260421-232949.ww614rny.debug.log`
- [e:c+i] Outcome:
  - the compact packet kept the read set repo-local and bounded
  - the probe still defaulted into repeated `Read` calls against that packet
  - the attempt stalled before returning final text
- [d:r:i] Consequence:
  - cut the attempt
  - preserve the evidence
  - complete the lane transparently as a composite rather than laundering the stall into a fake clean return

## Current Consequence

- [d:r:i] This lane preserves Opus as the widening lead through the completed first-return sections.
- [d:r:i] The missing sections were completed locally against the same frozen basis after two continuation attempts stalled.
- [d:r:i] The result is a completed composite lane output with explicit stall evidence rather than a falsely clean single-return story.
