# Wave-2 Spec: Rerun Design

Status: draft lane spec  
Date: 2026-04-20

## Lane

- wave: `2`
- lane: `rerun-design`
- packet: [../packets/06-rerun-design-packet.md](../packets/06-rerun-design-packet.md)

## Purpose

- [g:r:i] Judge what second-attempt program shape is now actually justified after the accepted Wave-1 returns and the lane-05 suppressed-opportunity reread.
- [g:r:i] Compare concrete option bundles rather than defaulting back to the incumbent program or jumping to the loudest stronger move.

## Primary Questions

1. What program shapes are now genuinely live?
2. What first slice, prerequisites, and execution-capacity model does each shape require?
3. Which option is now recommended, and why is it better than the nearest serious alternatives?
4. Which switch triggers should move the workspace away from the recommended path later?
5. Which organizational, version-control, and workflow-carrying surfaces are genuine prerequisites rather than background hygiene?

## Required Posture

- [g:r:i] Do not default back to `Proposal B-extended` because it is incumbent.
- [g:r:i] Do not default to `Proposal F` or `Proposal E` because they sound bolder.
- [g:r:i] Keep program-design judgment distinct from doctrine promotion. A stronger next program can be warranted without a broad canon rewrite.
- [g:r:i] If the lane trends toward `mostly keep the current shape`, open the packet's challenge stage before finalizing.
- [g:r:i] If the lane trends toward `broad machinery rewrite now`, open the packet's challenge stage before finalizing.

## Required Method

1. Read the packet in staged order.
2. Build an `Option Set` first.
3. For each option, state:
   - first slice
   - prerequisites
   - execution-capacity model
   - upside
   - regret / reversal cost
   - what evidence would count against it
4. Treat workspace organization, packet/launch discipline, and checkpoint hygiene as possible prerequisites where the evidence says they matter.
5. Produce an explicit `Recommended Next Program` with switch triggers rather than a generic preference statement.

## Required Output

Produce one markdown artifact under `wave-2/outputs/` with these sections:

1. `Overall Rerun-Design Judgment`
2. `Option Set And Baseline Assumptions`
3. `Comparative Option Matrix`
4. `Recommended Next Program`
5. `Prerequisites And Program-Carrying Surfaces`
6. `Switch-Trigger Register`
7. `What Must Stay Open`
8. `Interventions Considered And Rejected`

## Required Registers

- `comparative option matrix`
- `prerequisites and program-carrying surfaces register`
- `switch-trigger register`
- `unresolved register`
- `interventions considered and rejected ledger`

## Failure Conditions

- [g:r:i] Fails if it defaults to the incumbent option without anti-regret comparison.
- [g:r:i] Fails if it recommends a stronger option without a concrete first slice and execution-capacity model.
- [g:r:i] Fails if it treats workspace/hygiene prerequisites as irrelevant when the evidence says they shape execution honesty.
- [g:r:i] Fails if it cannot name at least `4` serious program alternatives and `4` stronger interventions it considered and rejected.
