Date: 2026-04-22
Status: landed packet template

# Uplift Carrier Gap Identification Packet Template

## Purpose

- [g:r:i] Use this packet when a concrete uplift result already exists and the next question is which neighboring carriers still need sharper follow-through or explicit hold.
- [g:r:i] This packet narrows from an uplift result toward nearby carriers.
- [g:r:i] It does not replace a wider `$gsd-propagation-review` when the question is already a concrete multi-family contract-changing slice.

## Input Bundle

- [d:r:i] Current uplift detect JSON
- [d:r:i] [95-upstream-pristine-propagation-baseline-first-slice.md](../../intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md)
- [d:r:i] [96-repo-local-propagation-delta-first-slice.md](../../intervention-proposals/96-repo-local-propagation-delta-first-slice.md)
- [d:r:i] One packet-time propagation-review scope note
- [d:r:i] Any already-landed assist-family artifacts that materially frame the current uplift result

## Packet-Time Propagation-Review Scope Note

- [d:r:i] Name the exact reason `propagation-review` is being read here.
- [d:r:i] Keep that scope note bounded to the current uplift-context narrowing.
- [d:r:i] Do not let the packet silently widen into a whole-network refresh.

## Questions To Answer

- [d:r:i] Which direct consumers are already in tune with the current uplift result, and which still stay thinner?
- [d:r:i] Which narrative mirrors should be refreshed now so the family does not hide its latest state in one subtree?
- [d:r:i] Which runtime or registry carriers should remain held, and why?
- [d:r:i] Which later neighbors should remain explicit so the slice does not foreclose later movement?

## Output Shape

```markdown
# Uplift Carrier Gap Identification

## Direct Consumers
- ...

## Narrative Mirrors
- ...

## Runtime And Registry Carriers
- ...

## Held-Later Neighbors
- ...
```

## Write Boundary

- [d:r:i] Packet plus bounded output plus parent-thread disposition only
- [d:r:i] No live route edits
- [d:r:i] No helper or CLI widening
- [d:r:i] No durable uplift-memory mutation
- [d:r:i] No propagation-registry refresh inside the packet itself
