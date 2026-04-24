Date: 2026-04-22
Status: completed parent-thread packet

# Uplift Carrier Gap Identification Second Exercise Packet

## Runtime For Packet Consumption

- [g:r:i] Parent-thread second exercise

## Governing Question

- [g:r:i] Starting from the current uplift detect result, which neighboring carriers are already in tune, which should be refreshed now, and which should remain explicitly held so the uplift-assist family broadens coverage before a live route pointer broadens reach?

## Input Bundle

### 1. Current Uplift Detect Output

- [e:c+i] Current helper output:
  - `project_class`: `cross-runtime uplift`
  - `secondary_signals`: `mid_phase`, `doctrine_changed`, `has_pending_proposals`
  - `pending_doctrine_sensitive_proposals`: `AGENTS.md`, `.planning/AGENTS.md`
  - `runtime_dirs`: `.codex`, `.claude`
  - `recommend_detect_only`: `true`
  - `recommendation_reasons`:
    - doctrine reference fingerprint changed since the last uplift pass
    - doctrine-sensitive carriers still need review
- [e:c+i] Source:
  - `python3 tooling/codex/project_uplift.py detect . --json`

### 2. Upstream-Pristine Baseline

- [e:c+i] Baseline anchor:
  - [../../intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md](../../intervention-proposals/95-upstream-pristine-propagation-baseline-first-slice.md)

### 3. Repo-Local Delta

- [e:c+i] Delta anchor:
  - [../../intervention-proposals/96-repo-local-propagation-delta-first-slice.md](../../intervention-proposals/96-repo-local-propagation-delta-first-slice.md)

### 4. Packet-Time Propagation-Review Scope Note

- [d:r:i] Use [propagation-review.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md) here only as the wider neighboring route that would own a concrete multi-family contract-change review.
- [d:r:i] In this packet, keep the question narrower:
  - identify which carriers the current uplift-assist family still leaves thinner
  - do not widen into a full propagation-review note or a typed-registry refresh in the same move

### 5. Current Assist-Family Trail

- [e:c+i] First reference pair:
  - [../../intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md](../../intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md)
  - [../../intervention-proposals/103-uplift-agent-assist-patterns.md](../../intervention-proposals/103-uplift-agent-assist-patterns.md)
- [e:c+i] First pattern template and exercise:
  - [06-uplift-docs-governance-classification-packet-template.md](06-uplift-docs-governance-classification-packet-template.md)
  - [07-uplift-docs-governance-classification-first-exercise-packet.md](07-uplift-docs-governance-classification-first-exercise-packet.md)
  - [../outputs/06-uplift-docs-governance-classification-first-exercise.md](../outputs/06-uplift-docs-governance-classification-first-exercise.md)
  - [../dispositions/06-uplift-docs-governance-classification-first-exercise-disposition.md](../dispositions/06-uplift-docs-governance-classification-first-exercise-disposition.md)
- [e:c+i] Post-first-exercise reread:
  - [../outputs/07-uplift-assist-post-first-exercise-next-move-opus47-max-r1.md](../outputs/07-uplift-assist-post-first-exercise-next-move-opus47-max-r1.md)
  - [../dispositions/07-uplift-assist-post-first-exercise-next-move-inheritance.md](../dispositions/07-uplift-assist-post-first-exercise-next-move-inheritance.md)

## Output Shape

- [d:r:i] Group the output under:
  - `Direct Consumers`
  - `Narrative Mirrors`
  - `Runtime And Registry Carriers`
  - `Held-Later Neighbors`

## Write Boundary

- [d:r:i] Packet, output, and parent-thread disposition only
- [d:r:i] No live route edits
- [d:r:i] No helper or CLI widening
- [d:r:i] No durable uplift-memory mutation
- [d:r:i] No propagation-registry refresh inside this exercise
