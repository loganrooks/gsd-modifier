# Docs-Audit Spec: PR Docs Intervention Carry

Status: draft lane spec  
Date: 2026-04-20

## Lane

- area: `docs-audit`
- lane: `pr-docs-intervention-carry`
- packet: [../packets/01-pr-docs-intervention-carry-packet.md](../packets/01-pr-docs-intervention-carry-packet.md)

## Purpose

- [g:r:i] Judge what the submitted docs PR carries for harness intervention planning, what it still flattens or hides, and what that means for future doc-layer transformation.
- [g:r:i] Keep contributor/reference value and intervention-planning value distinct enough that the lane does not average them into one blurred verdict.

## Primary Questions

1. What real carry gains does the submitted docs PR create for understanding and navigating the harness ecosystem?
2. What intervention surfaces does it newly expose, and what surfaces does it still flatten, hide, or mis-rank?
3. Where does the docs PR still confuse or understate declared authority versus effective authority?
4. Which parts of the docs corpus should remain stable contributor/reference docs, and which pressures require a paired intervention-oriented layer?
5. What stronger transformations or companion docs should be considered before treating the docs work as a durable intervention-onboarding surface?

## Required Posture

- [g:r:i] Do not use `adequate`, `good enough`, `passes`, `ready`, `works well`, or equivalent threshold language as the lane's governing question.
- [g:r:i] Do not treat the submitted docs PR as current runtime truth.
- [g:r:i] Do not turn this into a broad harness-quality or rerun-program lane.
- [g:r:i] If the lane starts leaning toward `the docs already carry this strongly enough`, it must still open a `Stronger Forms Considered` section and test that instinct against at least three stronger alternatives or companion-layer options.

## Required Method

1. Read the packet in staged order.
2. Keep `carry gains`, `blind spots`, and `transformation pressure` as distinct internal moves.
3. Distinguish at least:
   - contributor/reference carry
   - intervention-planning carry
   - declared-authority story
   - effective-authority story
4. Compare the submitted PR snapshot against current-upstream inventory only far enough to expose drift or missing surfaces relevant to the doc-carry question.
5. Name stronger forms or companion layers that were considered and explain why each should be adopted, held, or rejected.

## Required Output

Produce one markdown artifact with these sections:

1. `Overall Carry Judgment`
2. `Load-Bearing Gains`
3. `Blind Spots And Flattenings`
4. `Declared Versus Effective Authority Register`
5. `Intervention-Leverage Implications`
6. `What Should Stay Stable`
7. `What Needs A Paired Intervention Layer`
8. `Stronger Forms Considered`
9. `Recommended Next Moves`

## Required Registers

- `declared versus effective authority register`
- `stable-versus-transform register`
- `stronger forms considered register`

## Failure Conditions

- [g:r:i] Fails if it uses threshold language as the main frame.
- [g:r:i] Fails if it treats the docs PR as equivalent to live runtime truth.
- [g:r:i] Fails if it recommends broad doc rewriting without distinguishing stable reference docs from intervention-oriented companion layers.
- [g:r:i] Fails if it cannot name at least `3` stronger forms or companion-layer moves it considered.
