Date: 2026-04-20
Status: first-pass local audit

# Threshold-Language Residue Audit

## Purpose

- [g:r:i] This note marks threshold-language and deficit-oriented framing residue across the current rerun-redesign workspace and the historical readiness package so future rereads do not silently inherit contaminated framing.
- [d:r:i] The task here is not merely lexical policing. It is to identify where threshold logic likely shaped the question, the burden of proof, or the outcome of an audit/review/spec strongly enough that later readers should reread it with caution.

## Scope And Inputs

- [e:c+i] The first-pass scan covered:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
  - `.planning/readiness/phase-01-rerun`
  Sources: [01-threshold-language-raw-scan.txt](../artifacts/01-threshold-language-raw-scan.txt:1), [01-threshold-language-raw-scan.txt](../artifacts/01-threshold-language-raw-scan.txt:922).
- [e:c+i] The raw scan found `486` residue hits in that combined corpus. Source: [01-threshold-language-raw-scan.txt](../artifacts/01-threshold-language-raw-scan.txt:925).
- [e:c+i] The highest-count files in the first pass include:
  - the source ontology note (`26`)
  - historical cross-vendor review artifacts and lane outputs (`6-8`)
  - the readiness `PLAN.md` (`6`)
  - live rerun-redesign steering / synthesis surfaces like [CURRENT-STATE.md](../../CURRENT-STATE.md), [MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md](../../main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md), and [wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md](../../wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md). Source: [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:1), [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:17), [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:18), [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:23).

## Residue Classes

### 1. Active Steering Contamination

- [d:c+i] Some current steering surfaces still contain threshold-shaped inherited formulations that can contaminate present-day rereads if left unmarked.
  Examples:
  - [CURRENT-STATE.md](../../CURRENT-STATE.md:136) still inherits the phrase `directionally adequate and structurally under-mapped` from the mapping lane.
  - [CURRENT-STATE.md](../../CURRENT-STATE.md:143) still compresses the converged stack using that same framing.
  - [HARNESS-INTERVENTION-ONBOARDING.md](../../harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:17) still says C3 was not a `sufficient` intervention-onboarding surface.
  - [HARNESS-INTERVENTION-UPDATE-LANE.md](../../harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:15) still repeats the `directionally adequate` verdict as a live summary surface.
  - [MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md](../../main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:154) still uses `sufficient` as part of a current anti-failure rule.
- [d:r:i] These are not all equivalent. Some are direct inherited verdicts, some are meta-rules about what not to accept. But they are live enough that a present-day reader can still absorb the threshold shape if the warning surface is absent.

### 2. Threshold-Shaped Task Framing

- [d:c+i] Some historical specs/prompts framed the task itself in threshold terms, which means the resulting lane or review should not be reread as neutral terrain disclosure.
  Strongest examples:
  - [wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md](../../wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md:1)
    - the lane name itself centers `adequacy`
    - Question 1 asks `How adequate was the original readiness map?`
    - failure conditions revolve around `mapping is sufficient`
  - [OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md](../../review-specs/OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md:17)
    - asks whether organization is `well enough` / `good enough` for Wave 1
  - [OPUS-CROSS-REVIEW-SPEC.md](../../review-specs/OPUS-CROSS-REVIEW-SPEC.md:40)
    - asks whether packeting is `well enough` for later lanes
  - [wave-1/packets/03-mapping-adequacy-and-comparative-mapping-packet.md](../../wave-1/packets/03-mapping-adequacy-and-comparative-mapping-packet.md:63)
    - explicitly warns against concluding that mapping is `sufficient` or `close enough`, meaning the threshold language is not incidental but task-structuring
- [d:r:i] These surfaces matter more than stray mentions inside prose because they shaped what the model was being asked to optimize for.

### 3. Revisit-Worthy Historical Sessions

- [d:c+i] The historical sessions most likely to warrant reinterpretation or revisit because threshold framing shaped the task or conclusion are:
  1. [wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md](../../wave-1/specs/03-mapping-adequacy-and-comparative-mapping-spec.md:1) and its output [wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md](../../wave-1/outputs/03-mapping-adequacy-and-comparative-mapping-opus47-max-r1.md:12)
  2. [OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md](../../review-specs/OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md:17) and the resulting lane-05 review family
  3. [wave-2/outputs/06-rerun-design-opus47-max-r1.md](../../wave-2/outputs/06-rerun-design-opus47-max-r1.md:76) and [wave-2/outputs/06-rerun-design-gpt54-xhigh-r1.md](../../wave-2/outputs/06-rerun-design-gpt54-xhigh-r1.md:125), where `sufficient` / `adequate` language is still carrying decision pressure
  4. readiness-era `R5.17`/`R5.19` adjudication families where `adequate` or `sufficient` evidence-base language was used to authorize bounded closure claims, e.g. [checkpoint-5-r5-19e-adjudication-reread-internal-r1.md](../../../../readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md:21)
- [d:r:i] This does not automatically invalidate those sessions. It does mean they should be reread with an explicit warning that the task or verdict may have been partially flattened by threshold logic.

### 4. Quoted / Anti-Threshold Mentions

- [d:c+i] A large portion of the residue surface is not contamination in the same sense.
  Examples:
  - [AUDIT-CHARTER.md](../../governance/AUDIT-CHARTER.md:12) mentions `passes review` / `good enough to proceed` in order to reject them.
  - [PR-DOCS-INTERVENTION-CARRY-AUDIT.md](../../pr-docs-intervention/PR-DOCS-INTERVENTION-CARRY-AUDIT.md:9) explicitly says the task is not a threshold check.
  - [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](../../../../readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:100) rejects pass/fail posture.
- [d:r:i] These still need to be distinguished by the audit, because a raw scanner count alone cannot tell rejection from adoption.

### 5. Philosophical / Commentary Corpus Mentions

- [d:c+i] The commentary/source-note family also generates many hits, but many of them are conceptual uses of `sufficient`, `adequate`, or similar terms inside philosophical argument rather than harness doctrine. Examples appear in the source note and chunk commentary files ranked at the top of the count list. Sources: [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:1), [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:36), [02-threshold-language-top-files.txt](../artifacts/02-threshold-language-top-files.txt:37).
- [d:r:i] That corpus should not be cleaned with the same reflex as the planning/doctrine surfaces. It needs a separate judgment about whether a flagged phrase is conceptual argument, quoted target language, or live planning contamination.

## First-Pass Conclusions

- [d:c+i] The residue problem is real and widespread enough that memory-only correction is not credible. The combined corpus scan found `486` hits, and several are in current steering surfaces or in historically load-bearing specs. Source: [01-threshold-language-raw-scan.txt](../artifacts/01-threshold-language-raw-scan.txt:925).
- [d:r:i] The strongest present contamination vector is not merely stray wording inside old prose. It is threshold-shaped task framing in specs, prompts, and adjudication logic.
- [d:r:i] The strongest immediate cleanup target is not the whole historical corpus at once. It is:
  1. active steering surfaces in the current audit workspace
  2. revisit-worthy specs/prompts whose framing shaped later reviews
  3. then selected historical review/adjudication families

## Recommended Next Moves

1. Patch active steering surfaces that still carry inherited threshold wording as live summaries:
   - `CURRENT-STATE.md`
   - `../../harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md`
   - `../../harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md`
2. Open a bounded `spec/prompt threshold-residue audit` focused first on:
   - `wave-1/specs/03-*`
   - `../../review-specs/OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md`
   - `../../review-specs/OPUS-CROSS-REVIEW-SPEC.md`
   - any directly descended prompts/packets
3. Mark reread-risk explicitly for the sessions most likely shaped by threshold framing rather than treating them as clean neutral judgments.
4. Improve the scanner later with allowlists or classification modes so anti-threshold references and quoted history can be separated more cheaply from actual contamination.

## Current Consequence

- [d:r:i] Future rereads of the historical readiness package or this rerun-redesign workspace should not rely on raw artifact text alone.
- [d:r:i] They should treat this note as the warning surface for threshold contamination until the next cleanup pass and spec-audit pass are complete.
