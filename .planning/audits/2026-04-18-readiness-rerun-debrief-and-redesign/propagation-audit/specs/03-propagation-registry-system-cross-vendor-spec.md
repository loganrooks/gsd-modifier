Date: 2026-04-21
Status: active cross-vendor spec

# Propagation Registry System Cross-Vendor Spec

## Framing

- [g:r:i] Review the propagation registry system as a whole, not only the current `v1` snapshot.
- [g:r:i] The governing task is to map how this family should be structured so that propagation relations can be surfaced more fully, more explicitly, and with better control over what is being read and why.
- [g:r:i] Keep the review out of threshold language, binary accept/reject framing, and code-solution reflexes.

## Primary Questions

1. How should the propagation registry system be layered if the goal is to surface propagation relations more fully and controllably?
2. What should be seeded from maintained docs such as `docs/INVENTORY.md`, and what should stay outside that seed layer?
3. What parts of the propagation field should remain AI-authored semantic mapping rather than being handed to determinate extraction?
4. What parts can determinate tooling legitimately contribute without overclaiming semantic authority?
5. Is `runtime/tooling evidence` a coherent category, or should it be split into narrower layers such as runtime snapshots, ownership contracts, validation outputs, or materialization traces?
6. What does the current local direction in `14` still flatten, blur, or leave underspecified?
7. What stronger system design would let future propagation work preserve both full-field disclosure and practical operator control?
8. What bounded next design move would strengthen this family most from the current baseline?
9. How should this be inherited locally?

## Required Output Shape

Use these exact section headings:

1. `How The Registry System Should Be Layered`
2. `What Maintained Docs Should Seed`
3. `What Should Remain AI-Authored Semantic Mapping`
4. `What Determinate Tooling Can Legitimately Contribute`
5. `How The Current Runtime/Tooling-Evidence Idea Should Be Split Or Clarified`
6. `What The Current Local Direction Still Flattens`
7. `Stronger Design For The Propagation Registry Family`
8. `Bounded Next Design Move`
9. `How This Should Be Inherited Locally`

Inside section `9`, separate:
- `Carry Forward`
- `Revise`
- `Hold Explicit`

## Review Discipline

- [d:r:i] Do not reduce the answer to `manual` versus `automatic`.
- [d:r:i] Distinguish semantic mapping, maintained-doc seeding, generated evidence, validation contracts, and later operator tooling if they deserve separate layers.
- [d:r:i] If the current category `runtime/tooling evidence` is too blended, say how it should divide.
- [d:r:i] If a maintained doc surface such as `docs/INVENTORY.md` should own more than mere seeding, name the stronger ownership shape.
- [d:r:i] If a determinate tool would help, say what narrow claim it should make and what it should refuse to claim.
- [d:r:i] If the current local proposal is too compressed, widen it rather than only noting discomfort.

## Output Paths

- Opus output:
  - [propagation-audit/outputs/03-propagation-registry-system-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/outputs/03-propagation-registry-system-opus47-max-r1.md)
- Local parallel reviewer:
  - [propagation-audit/outputs/03-propagation-registry-system-gpt54-xhigh-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/outputs/03-propagation-registry-system-gpt54-xhigh-r1.md)
