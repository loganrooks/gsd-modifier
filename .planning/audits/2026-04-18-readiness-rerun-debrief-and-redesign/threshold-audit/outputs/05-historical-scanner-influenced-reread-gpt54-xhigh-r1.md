Date: 2026-04-21
Status: bounded historical reread complete

# Historical Scanner-Influenced Reread

## Research Frame

- Mode: `synthesis`
- Question: which scanner-influenced doctrine/governance edits widened reread usefully, which drifted into wording control or governance distortion, and which artifacts now deserve `keep`, `patch`, `contextual reinterpretation`, or `revisit the earlier judgment`
- Scope: commits `53ee156`, `2908677`, `2834fd3`, `8340127`, `f29ea75`, `3921d3a`, `c4be7c9`, plus the packeted priority surfaces
- Non-goals: whole-repo threshold cleanup; scanner pass/fail adjudication; reopening unrelated uplift/propagation questions
- Stop condition: explicit disposition over corrections that should not have been made, edits that should remain, current patch/reinterpretation candidates, and recurring failure patterns

## Path Of Inquiry

- Entry point: [05-historical-scanner-influenced-reread-packet.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/packets/05-historical-scanner-influenced-reread-packet.md:1), [05-historical-scanner-influenced-reread-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/specs/05-historical-scanner-influenced-reread-spec.md:1), then the internal side-effects audit family under `03` and `04`
- Branches pursued:
  - reread the seven named commits in diff context
  - reread the current live doctrine/governance surfaces for role-sensitive judgment
  - spot-check the current scanner behavior where the prior internal audit said false-control pressure had appeared
- Branches deferred:
  - broader residue outside the packeted commit family
  - fresh scanner-led sweeps over unrelated audit/workflow surfaces

## Assumptions Surfaced

- [a:r:i] The live post-`c4be7c9` surfaces are the right baseline for judging whether earlier edits should remain or be treated as corrected drift.
- [a:r:i] Historical audit outputs may still contain threshold terms when they are functioning as evidence, quoted targets, or reread warnings; they should not be normalized into scanner-clean prose merely because the heuristic can see them.

## Historical Slices Reviewed

- `53ee156` `docs(audit): add threshold-language residue audit`
- `2908677` `docs(audit): map threshold residue and self-overcoming surfaces`
- `2834fd3` `docs(tooling): tighten anti-threshold enforcement`
- `8340127` `docs(doctrine): harden anti-threshold language guardrails`
- `f29ea75` `docs(doctrine): keep threshold scanner non-authoritative`
- `3921d3a` `harness(uplift): add compatibility anchor and scanner audit`
- `c4be7c9` `harness(uplift): route compatibility drift into live consumers`

## Evidence Base

### Direct Evidence

- [e:c+i] The first threshold-audit opening already made the right distinction: active steering contamination, threshold-shaped historical task framing, and quoted or anti-threshold mentions were never meant to collapse into one bucket. Sources: [threshold-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/README.md:6), [01-threshold-language-residue-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/01-threshold-language-residue-audit.md:62).
- [e:c+i] The second audit widened the doctrine correctly by distinguishing legitimate gate logic from terrain-mapping logic and by identifying positive carry already present in review, future-preservation, and `plant-seed`. Sources: [02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md:20), [02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md:40).
- [e:c+i] The later internal audit explicitly records the scanner-family failure mode as heuristic overreach in meta-prohibition contexts and narrows the fix to optional widening aid, no routine gate, and no scanner-driven weakening of explicit prohibitions, quoted examples, or historical evidence. Sources: [03-threshold-scanner-side-effects-internal-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/03-threshold-scanner-side-effects-internal-audit.md:28), [03-threshold-scanner-side-effects-internal-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/03-threshold-scanner-side-effects-internal-audit.md:37).
- [e:c+i] The bounded xhigh reviewer return confirms that scanner authority had still leaked into live governance after the internal audit: active surfaces still required wording to clear the scanner or celebrated wording quieted for the scanner, and that drift was later corrected. Sources: [04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/outputs/04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md:9), [04-scanner-side-effects-internal-audit-review-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/04-scanner-side-effects-internal-audit-review-inheritance.md:17).
- [e:c+i] The live doctrine baseline is now coherent on the central point: the scanner is optional intake only, live governance uses contextual reread rather than scanner-clearing, and explicit anti-pattern naming is allowed on doctrine/prompt-governing surfaces. Sources: [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:187), [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:80), [propagation-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/README.md:96), [42-project-uplift-signal-layer-harden-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/42-project-uplift-signal-layer-harden-slice.md:62), [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md:26).
- [e:r:i] The current heuristic still has a live brittle edge: a direct run of `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md` still flags the explicit prohibition at line `27`, which matches the current code shape because `is_meta_instruction_line()` only skips lines with backticks plus `do not|avoid|prefer|keep`. Sources: [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md:27), [scan_threshold_language.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/scan_threshold_language.py:64).

### Inference And Interpretation

- [d:r:i] The scanner family was directionally valuable when it widened attention toward real residue clusters and helped force a gate-vs-terrain distinction into doctrine.
- [d:r:i] The same family became distorting when its outputs were treated as cleanup pressure on wording rather than as prompts for contextual classification by file role.
- [d:r:i] The largest historical problem is therefore not the existence of the scanner or the threshold-audit subtree. The problem is the moments where heuristic pressure moved from intake to prose control or governance gating.

### Unknowns

- [o:r:i] This reread does not settle the best implementation shape for a safer scanner follow-through: broadened meta-detection, role-aware suppression, explicit classification mode, or a thinner documented caveat may all still be viable.
- [o:r:i] This reread does not decide whether any historical audit outputs should be lexically patched; it decides only where current carry requires patch, reinterpretation, or judgment revision.

## Corrections That Should Not Have Been Made

- [d:c+i] The pseudo-positive wording preference introduced in `2834fd3` and carried into `2908677` should not have hardened as preferred durable wording. Replacing deficit language with phrases like `already strong here` solved one residue family by creating a second static-positive evaluative family; the later reversal in [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:70) and [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:176) is the stronger form.
- [d:r:i] The `use the scanner as a first-pass detector rather than relying on memory alone` posture from `2834fd3` / `2908677` should not have remained durable guidance. That phrasing made the tool sound like the expected entry step rather than one optional widening aid; the current narrowed rule in [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:187) is the better boundary.
- [d:c+i] The scanner-as-gate carry that appeared inside `3921d3a` should not have been made. The propagation quality gate demanding wording clear the scanner, and the uplift note celebrating wording tightened away from explicit threshold-term enumeration, are exactly the governance drift later identified in [04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/outputs/04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md:10) and corrected in [propagation-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/README.md:99) and [42-project-uplift-signal-layer-harden-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/42-project-uplift-signal-layer-harden-slice.md:62).
- [d:r:i] The attempted weakening of the explicit prohibition line in [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md:27) should not have happened. The restored direct wording is correct for a prompt-governing file precisely because that file’s job is to say what must not become the governing question.

## Edits That Should Remain

- [d:c+i] The threshold-audit subtree opened by `53ee156` should remain. Its opening README and first disposition already preserve the essential distinctions between live contamination, task-shaping historical residue, quoted anti-threshold mentions, and commentary/philosophical uses. Sources: [threshold-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/README.md:6), [01-threshold-language-residue-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/01-threshold-language-residue-audit.md:37), [01-threshold-language-residue-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/01-threshold-language-residue-audit.md:62).
- [d:c+i] The gate-vs-terrain and self-overcoming mapping added in `2908677` should remain. It widened the question beyond lexical policing and prevented the threshold-audit family from flattening all gates into contamination. Sources: [02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md:20), [02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md:47).
- [d:c+i] The `8340127` hardening should remain. Static-positive evaluative residue is a real family, and the current root/planning doctrine is sharper because it names that family directly rather than leaving it ambient. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:73), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:179).
- [d:c+i] The `f29ea75` demotion of scanner authority should remain. The live docs and the tool’s own output now say clearly that findings are heuristic hits only and still require contextual reread and disposition. Sources: [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:82), [scan_threshold_language.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/scan_threshold_language.py:103).
- [d:c+i] The `c4be7c9` follow-through should remain. It did not overreact by rolling back the whole scanner family; it removed scanner-as-gate carry from live governance while preserving the bounded reread itself and routing the separate compatibility gap into the actual consumer chain. Sources: [04-scanner-side-effects-internal-audit-review-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/04-scanner-side-effects-internal-audit-review-inheritance.md:17), [propagation-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/README.md:99), [42-project-uplift-signal-layer-harden-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/42-project-uplift-signal-layer-harden-slice.md:62).

## Artifacts That Now Deserve Patch, Contextual Reinterpretation, Or Revisit

### Patch

- [d:r:i] [scan_threshold_language.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/scan_threshold_language.py:64) deserves a bounded patch. `--ignore-meta-instruction-lines` still misses explicit prohibition lines that use `forbid` or similarly direct governing language, which means the heuristic still creates false-control pressure exactly where the later doctrine says direct naming is allowed.

### Contextual Reinterpretation

- [d:r:i] The raw scan artifacts under `threshold-audit/artifacts/01-*` and `02-*` should be read only as widening intake. They are useful historical pressure surfaces, not authority surfaces or cleanup ledgers. Their correct reading is already closer to [threshold-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/README.md:6) than to any notion of scanner-certified contamination.
- [d:r:i] [01-threshold-language-residue-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/01-threshold-language-residue-audit.md:97) now needs the `03`/`04` caveat read back into its `improve the scanner later` recommendation. That recommendation remains directionally usable only if the improvement reduces false-control pressure rather than making the scanner a stronger gate.
- [d:r:i] [02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md:9) contains some threshold-shaped analytical wording of its own. That does not currently earn lexical cleanup by itself because the file is a bounded historical audit note, not the live governing doctrine; it should be reread as analysis, not mistaken for current instruction posture.

### Revisit The Earlier Judgment

- [d:r:i] The earlier judgment that the next scanner move was simply `better allowlists or classification` now deserves narrowing. After the side-effects reread, the better question is not how to make the scanner broader or quieter; it is how to make any future heuristic output more role-aware and less capable of turning into prose control.

## Recurring Failure Patterns

1. [d:r:i] `widening aid -> default workflow step`: scanner guidance moved from useful intake pressure toward a recommended first-pass detector, which made it easier for later users to treat the tool as expected doctrine rather than optional aid.
2. [d:r:i] `anti-deficit cleanup -> new wording orthodoxy`: rejecting deficit-oriented pseudo-positive phrasing first produced a preferred static-positive vocabulary, which then required a second corrective pass.
3. [d:r:i] `meta prohibition -> false residue`: quoted forbidden terms inside doctrine/prompt-governing files were treated as contamination, which incentivized euphemism exactly where explicit naming was pedagogically necessary.
4. [d:r:i] `audit pressure -> governance gate drift`: scanner cleanliness leaked out of the threshold-audit lane and into unrelated propagation/uplift quality gates, where it had no legitimate adjudicative authority.
5. [d:r:i] `clean result -> misplaced confidence`: scanner-passing language displaced contextual file-role judgment and rewarded quieter wording rather than stronger carry.
6. [d:r:i] `doctrine outran heuristic`: the repo’s current doctrine now says contextual reread is sovereign, but the present code still misses some explicit anti-pattern lines, so the live heuristic remains more brittle than the governing guidance around it.

## What Has Strong Carry Now

- [d:c+i] The current doctrine/governance baseline is coherent enough to keep: root/planning AGENTS, tooling README, propagation governance, uplift governance, and the PR-docs next-step note now align on the same hierarchy:
  - scanner widens reread
  - contextual judgment classifies by file role
  - explicit anti-pattern naming remains allowed where the file is teaching what to avoid

## What Still Needs Wider Carry

- [d:r:i] The scanner implementation should catch up to the doctrine boundary so explicit prohibition lines stop generating avoidable false-control pressure.
- [d:r:i] Any later scanner-improvement proposal should inherit `03` and `04` directly rather than speaking only in terms of stronger pattern coverage or cleaner results.
- [d:r:i] No broader rollback of the threshold-audit family is earned. The useful widening work should stay; only the wording-control and governance-drift carry needs continued resistance.

## Sources

- [05-historical-scanner-influenced-reread-packet.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/packets/05-historical-scanner-influenced-reread-packet.md:1)
- [05-historical-scanner-influenced-reread-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/specs/05-historical-scanner-influenced-reread-spec.md:1)
- [threshold-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/README.md:1)
- [01-threshold-language-residue-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/01-threshold-language-residue-audit.md:1)
- [02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md:1)
- [03-threshold-scanner-side-effects-internal-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/03-threshold-scanner-side-effects-internal-audit.md:1)
- [04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/outputs/04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md:1)
- [04-scanner-side-effects-internal-audit-review-inheritance.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/dispositions/04-scanner-side-effects-internal-audit-review-inheritance.md:1)
- [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:65)
- [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:172)
- [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md:80)
- [tooling/codex/scan_threshold_language.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/scan_threshold_language.py:1)
- [propagation-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/README.md:94)
- [42-project-uplift-signal-layer-harden-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/42-project-uplift-signal-layer-harden-slice.md:56)
- [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md:26)
