Date: 2026-04-21
Status: active reread spec

# Propagation Chain Reread Spec

## Framing

- [g:r:i] Reread the current propagation family after the landed `resume-project` second-consumer slice.
- [g:r:i] The governing task is not to restage generic uplift design, not to ask only whether the local implementation “worked,” and not to reduce the problem to markdown link hygiene or install coherence alone.
- [g:r:i] The governing task is to reread the current chain in its wider form:
  - what it already carries strongly
  - how the producer / consumer / durable-output / materialization / governance relations now fit together
  - which surrounding carriers still stay too ambient, too weakly surfaced, or too narrowly mapped
  - which next bounded strengthening routes should come next
- [g:r:i] Keep the review out of threshold language, deficit-only framing, and binary recommendation shapes.

## Primary Questions

1. What does the current propagation chain already carry strongly after the landed two-consumer baseline?
2. How do the current roles now divide across:
   - producer logic
   - direct consumers
   - durable outputs
   - materialization bridge
   - wrapper and governance carriers
3. Which neighboring surfaces still remain too ambient, too weakly routed, or too easy to forget when contract changes move?
4. Which parts of the current docs/tooling layer now help later operators see dependency relations clearly, and which parts still need stronger carrier placement or disclosure?
5. Which additional workflow, skill, script, output, registry, or governing-doc surfaces deserve more explicit place inside the propagation family?
6. Which bounded strengthening routes would most intensify propagation architecture from the current baseline?
7. Which later families should stay explicit later-family work rather than being silently absorbed into this chain now?
8. How should this current family state be inherited locally?

## Required Output Shape

Use these exact section headings:

1. `What The Current Propagation Chain Already Carries Strongly`
2. `How The Current Roles Divide Across The Chain`
3. `Where Neighboring Carriers Still Stay Too Ambient Or Too Weakly Routed`
4. `What The Current Docs And Tooling Layer Already Makes Easier To See`
5. `What Still Deserves Stronger Carrier Placement Or Disclosure`
6. `Bounded Strengthening Routes From The Current Baseline`
7. `Later Families To Keep Explicit`
8. `How This Propagation Family Should Be Inherited`

Inside section `8`, separate:
- `Carry Forward`
- `Strengthen Next`
- `Hold For Later`

## Review Discipline

- [d:r:i] Map the relevant field before narrowing to a next sequence.
- [d:r:i] Do not judge the family only by local code correctness.
- [d:r:i] Keep producer logic, direct consumers, durable outputs, materialization carriers, wrappers, and governance carriers distinct rather than collapsing them into one blended verdict.
- [d:r:i] If you think a missing surface deserves inclusion, name the surface and the kind of carry it should own.
- [d:r:i] If you think current docs or tooling still under-disclose dependency relations, name the stronger disclosure route rather than only noting a weakness.
- [d:r:i] If you think a later external or wider local family should still wait, keep that hold explicit rather than implying a silent veto.

## Output Path

- Opus output:
  - [propagation-audit/outputs/01-propagation-chain-reread-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/outputs/01-propagation-chain-reread-opus47-max-r1.md)
