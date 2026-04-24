# Wave-2 Spec: Suppressed Opportunity And Non-Intervention

Status: draft lane spec  
Date: 2026-04-20

## Lane

- wave: `2`
- lane: `suppressed-opportunity-and-non-intervention`
- packet: [../packets/05-suppressed-opportunity-and-non-intervention-packet.md](../packets/05-suppressed-opportunity-and-non-intervention-packet.md)

## Purpose

- [g:r:i] Judge which stronger interventions, design moves, or bounded experiments were prematurely excluded, softened, narrowed, or deferred across the readiness package and the audit setup.
- [g:r:i] Re-test the package's explicit non-intervention defenses against the accepted Wave-1 returns rather than letting prior disposition language stand as automatic justification.

## Primary Questions

1. Which stronger moves were visible and live, but not taken?
2. Which non-interventions were defensible then but no longer look defensible now?
3. Which `traceable undercarry` items have now crossed the line into `bounded experiment warranted`?
4. Which stronger moves are still not earned, even after Wave 1?
5. Which suppressed opportunities belong to local carrier/workspace changes, and which belong to rerun-program shape?

## Required Posture

- [g:r:i] Do not treat explicit prior disposition as self-justifying.
- [g:r:i] Do not let `too large`, `too risky`, or `not yet` stand without naming the execution model, mitigation path, and regret analysis.
- [g:r:i] Do not turn the register into a hidden scoring ladder where every suppressed opportunity becomes mandatory.
- [g:r:i] If the lane trends toward `nothing stronger is now warranted`, open the packet's challenge stage before finalizing.
- [g:r:i] If the lane trends toward `broad rewrite now`, open the packet's challenge stage before finalizing.

## Required Method

1. Read the packet in staged order.
2. Build a `Suppressed-Opportunity Register` first.
3. Build a `Non-Intervention Reassessment` second.
4. Distinguish at least:
   - `explicit miss`
   - `traceable undercarry`
   - `bounded experiment now warranted`
   - `still-unearned stronger move`
   - `program-shape pressure`
5. Re-test each stronger move against:
   - anti-regret burden
   - best-possible-outcome pressure
   - execution-capacity assumptions
   - reversal / rollback cost
6. Name which items should feed directly into `rerun-design` rather than being decided here.

## Required Output

Produce one markdown artifact under `wave-2/outputs/` with these sections:

1. `Overall Suppressed-Opportunity Judgment`
2. `Suppressed-Opportunity Register`
3. `Non-Intervention Reassessment`
4. `Bounded Experiments Or Local Proposals Now Warranted`
5. `Stronger Moves Still Rejected`
6. `Program-Shape Pressures For Rerun Design`
7. `Switch-Trigger Pressure Update`
8. `Interventions Considered And Rejected`

## Required Registers

- `suppressed-opportunity register`
- `non-intervention reassessment ledger`
- `bounded experiment / proposal-now-warranted register`
- `switch-trigger pressure update`
- `interventions considered and rejected ledger`

## Failure Conditions

- [g:r:i] Fails if it treats prior explicit disposition as sufficient warrant by itself.
- [g:r:i] Fails if it rejects stronger moves on size/risk language without naming mitigation and execution model.
- [g:r:i] Fails if it promotes every visible stronger move into immediate obligation.
- [g:r:i] Fails if it cannot name at least `5` stronger interventions it considered and rejected.
