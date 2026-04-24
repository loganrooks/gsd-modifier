Date: 2026-04-20
Status: active disposition

# First Tranche Disposition

## Purpose

- [g:r:i] This note records how the first bounded intervention proposal batch is actually inherited, so `proposal exists` does not get mistaken for `nothing has been decided`.

## Accepted Now

### 1. Launch-truth capture

- [d:c+i] Accept with narrowing: the right move is not to invent a brand-new launch-truth protocol from scratch. It is to carry the already-existing helper and governance surfaces into the repo’s active runtime doctrine. Sources: [02-launch-truth-capture-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/02-launch-truth-capture-proposal.md:1), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:66), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:90), [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:1).
- [d:r:i] Immediate consequence: make durable launch-truth capture explicit in the active AGENTS/runtime instruction layer for doctrine-sensitive and other high-stakes spawned work.

### 2. Agent `.toml` authority alignment

- [d:c+i] Accept as a bounded high-stakes cohort pass. The proposal is strong because it acts on the runtime-authoritative surfaces that actually shape spawned-worker behavior, and it stays narrow enough to verify concretely. Sources: [01-agent-toml-authority-alignment-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/01-agent-toml-authority-alignment-proposal.md:1), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:40).
- [d:r:i] Immediate consequence: align the `gsd-planner`, `gsd-plan-checker`, `gsd-executor`, and `gsd-verifier` cohort to the repo’s actual anti-threshold, repo-local, AGENTS-governed doctrine without widening to the full agent fleet.

## Held For Second Tranche

### 3. Live-vs-overlay drift visibility

- [d:r:i] Hold for the second tranche, not because it lacks value, but because it will be more discriminating once launch-truth capture and high-stakes `.toml` alignment make the runtime baseline sharper.

### 4. Manifest/install coherence

- [d:r:i] Hold behind the drift-visibility tranche. The semantic contract question remains real, but it will be stronger once the live/overlay picture is less ambiguous.

## What This Rejects

- [d:r:i] Reject the weaker move of treating all four proposals as equivalent parallel backlog with no inheritance order.
- [d:r:i] Reject the weaker move of writing more companion explanation without touching the runtime-owned or launch-owned seams already named here.

## Immediate Next Move

- [g:r:i] Land the first accepted pair now:
  - explicit launch-truth capture in the active repo instruction layer
  - bounded authority alignment across the four high-stakes `.toml` agents

## Initial Landing

- [e:c+i] The launch-truth part of the first tranche is now carried in the active instruction layer: root [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:135) now requires durable requested-vs-effective capture for doctrine-sensitive or otherwise high-stakes spawned work, and [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:89) now carries the same rule for planning/audit/review work inside `.planning/`.
- [e:c+i] The `.toml` authority part of the first tranche is now carried both in live runtime and in tracked overlay canon: [gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml:15), [gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-plan-checker.toml:48), [gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-executor.toml:41), and [gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-verifier.toml:39) now match the same repo-quality posture carried in [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml:15), [tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml:48), [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml:41), and [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml:39).
