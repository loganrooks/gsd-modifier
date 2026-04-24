# Wave-1 Spec: Mapping Adequacy And Comparative Mapping

Status: draft lane spec  
Date: 2026-04-19

## Lane

- wave: `1`
- lane: `mapping-adequacy-and-comparative-mapping`
- packet: [03-mapping-adequacy-and-comparative-mapping-packet.md](../packets/03-mapping-adequacy-and-comparative-mapping-packet.md)

## Purpose

- [g:r:i] Judge how good the readiness package's actual map was, how that map compares to the bridge audit, the later docs corpus, and runtime / harness behavior, and what still separates current mapping from intervention-ready mapping.
- [g:r:i] Keep `mapping adequacy` and `comparative mapping` distinct enough that the lane does not average away different defect types.

## Primary Questions

1. How adequate was the original readiness map of GSD, Codex / Claude, seam behavior, side workflows, and producer-consumer chains?
2. Where did readiness mapping, the bridge audit, later docs work, and runtime / harness behavior agree or diverge?
3. Which mismatches are really docs defects, readiness mapping defects, bridge-inheritance defects, or runtime-missed-by-both defects?
4. What still separates current mapping from intervention-ready mapping?
5. What switch triggers should move the workspace away from `Proposal B-extended` toward stronger alternatives?

## Required Posture

- [g:r:i] Do not let docs quality masquerade as runtime adequacy.
- [g:r:i] Do not treat bridge-audit inheritance as neutral default.
- [g:r:i] If the lane starts leaning toward `mapping is sufficient`, `close enough`, or `no stronger mapping lane needed`, open the packet's challenge stage before finalizing that judgment.

## Required Method

1. Read the packet in staged order.
2. Write one subsection for `Mapping Adequacy`.
3. Write a separate subsection for `Comparative Mapping`.
4. Build a mismatch matrix rather than a prose-only impression.
5. Distinguish:
   - what was visible but underweighted
   - what was invisible
   - what was misclassified
   - what later docs clarified
   - what runtime still pressures against the docs picture
6. Produce switch triggers with explicit execution-capacity assumptions.

## Required Output

Produce one markdown artifact under `wave-1/outputs/` with these sections:

1. `Overall Mapping Judgment`
2. `Mapping Adequacy`
3. `Comparative Mapping`
4. `Mismatch Matrix`
5. `Mapping-Confidence Register`
6. `Runtime-Versus-Map Divergence Notes`
7. `Switch-Trigger Register`
8. `Interventions Considered And Rejected`

## Required Registers

- `mapping-confidence register`
- `inheritance-disposition matrix`
- `switch-trigger register`
- `interventions considered and rejected ledger`

## Failure Conditions

- [g:r:i] Fails if it blurs adequacy and comparison into one undifferentiated verdict.
- [g:r:i] Fails if it upgrades docs refresh into sufficient mapping without confronting runtime evidence.
- [g:r:i] Fails if it recommends `mapping is sufficient` without explicit challenge-packet engagement.
- [g:r:i] Fails if it cannot name at least `3` stronger interventions it considered and rejected.
