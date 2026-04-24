# Wave-1 Spec: Operator Orchestration Pressure

Status: draft lane spec  
Date: 2026-04-19

## Lane

- wave: `1`
- lane: `operator-orchestration-pressure`
- packet: [04-operator-orchestration-pressure-packet.md](../packets/04-operator-orchestration-pressure-packet.md)

## Purpose

- [g:r:i] Test whether operator-bandwidth limits, sequencing choices, orchestration patterns, or workflow-carrier behavior materially contributed to readiness underreach independently of weak mapping.
- [g:r:i] Keep this as an explanatory pressure lane, not a universal excuse that explains everything after the fact.

## Primary Questions

1. Which operator or orchestration pressures were real and load-bearing?
2. Which pressures amplified existing mapping or judgment weaknesses rather than causing them directly?
3. Which workflow or carrier surfaces made stronger treatment harder to sustain?
4. Which explanations are post-hoc convenience rather than strong causal pressure?
5. What switch triggers should move the rerun shape toward stronger workflow, execution-capacity, or harness-facing intervention?

## Required Posture

- [g:r:i] Do not let `one operator under pressure` become a generic absolution.
- [g:r:i] Do not pathologize operator pressure if mapping or doctrine weakness explains more.
- [g:r:i] If operator pressure starts explaining everything, open the challenge stage before finalizing any causal ranking.

## Required Method

1. Read the packet in staged order.
2. Build an operator-pressure register.
3. Classify each pressure as:
   - primary causal pressure
   - amplifying pressure
   - weak / post-hoc explanation
4. Compare operator explanations against mapping, doctrine, and intervention-shape explanations rather than scoring them in isolation.
5. Produce rerun-shape implications and switch triggers with explicit execution-capacity assumptions.

## Required Output

Produce one markdown artifact under `wave-1/outputs/` with these sections:

1. `Overall Operator-Pressure Judgment`
2. `Operator-Pressure Register`
3. `Alternative Explanation Notes`
4. `Carrier And Workflow Surfaces Under Pressure`
5. `Switch-Trigger Register`
6. `Interventions Considered And Rejected`
7. `What This Lane Cannot Explain`

## Required Registers

- `operator-pressure register`
- `switch-trigger register`
- `non-intervention ledger`
- `interventions considered and rejected ledger`

## Failure Conditions

- [g:r:i] Fails if it reduces the whole readiness initiative to operator overload.
- [g:r:i] Fails if it cannot distinguish primary from amplifying pressure.
- [g:r:i] Fails if it recommends stronger workflow or harness moves without naming reversal cost and reopening triggers.
- [g:r:i] Fails if it cannot name at least `3` stronger interventions it considered and rejected.
