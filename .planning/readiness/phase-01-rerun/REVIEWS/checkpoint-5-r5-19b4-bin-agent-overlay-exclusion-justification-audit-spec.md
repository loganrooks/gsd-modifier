# Checkpoint 5 R5.19b4 Bin / Agent / Overlay / Runtime-Control Exclusion-Justification Audit Spec

This lane proves or disproves current exclusion / non-modification judgments for bin, agent, overlay, and runtime-control surfaces relevant to Checkpoint 5.

It is the runtime / chain-tail exclusion-proof lane.

## Audit Stance

- post-verificationist
- post-falsificationist
- gap-exposure / completeness-challenge
- anti-regret

## Governing Inputs

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
5. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
6. [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md)
7. [REVIEWS/checkpoint-5-r5-19b-preserved-exclusion-justification-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b-preserved-exclusion-justification-audit-spec.md)
8. [AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)

## Candidate Runtime / Chain-Tail Surfaces

- `.codex/get-shit-done/bin/lib/phase.cjs`
- `.codex/get-shit-done/bin/lib/roadmap.cjs`
- `.codex/get-shit-done/bin/lib/commands.cjs`
- `.codex/get-shit-done/bin/lib/uat.cjs`
- `.codex/get-shit-done/bin/lib/audit.cjs`
- `.codex/agents/`
- `tooling/portable-gsd/overlay/agents/gsd-executor.toml`
- `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`
- `tooling/codex/capture_launch_truth.py`

## Questions

- Which runtime / chain-tail exclusions survive?
- Which fail?
- Which excluded runtime-control surfaces are inside the sphere of influence because they route, summarize, or authorize behavior?
- Which are independently load-bearing even if the direct propagation chain is weak or disputed?
- Which exclusions leave meaningful quality gains on the table?

## Output

Write:

- [checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md)

Required sections:

1. `Summary`
2. `Exclusions That Survive`
3. `Exclusions That Fail`
4. `Runtime / Chain-Tail Surfaces That Must Move Into Active Consideration`
5. `Potential Quality Gains Left On The Table`
6. `Read-Set Adequacy`
