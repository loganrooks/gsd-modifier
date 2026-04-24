# Threshold-Scanner Side-Effects Internal Review

Date: 2026-04-21
Requested reviewer: `gpt-5.4`
Requested reasoning: `xhigh`

## Findings

1. [e:c+i] The new compatibility anchor had not yet reached the live routed-consumer path. [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py) named runtime movement as a reason to rerun `$gsd-uplift-project --write`, but the active read-only consumer route still returned `Continue with current routing.` because `progress-note` was not yet comparing stored compatibility basis against current observed runtime basis. The reviewer reproduced that by changing only `.codex/get-shit-done/VERSION` and `.codex/gsd-file-manifest.json`.
2. [e:c+i] Scanner authority still remained too strong in live governance. [propagation-audit/README.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/README.md) still required wording to clear the scanner, and [42-project-uplift-signal-layer-harden-slice.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/42-project-uplift-signal-layer-harden-slice.md) still celebrated wording quieted for the scanner, which conflicted with the internal audit that demoted the scanner to widening aid only.
3. [e:c+i] The compatibility source contract was looser than the live runtime doctrine. The helper silently fell back from `.codex/get-shit-done/VERSION` to `.codex/VERSION`, even though the repo’s current regular-runtime basis is the canonical repo-local runtime under `.codex/get-shit-done`.

## Reviewer Consequence

- [d:r:i] No new broad anti-threshold regression was surfaced in the surrounding prose batch.
- [d:r:i] The remaining work was narrower and more concrete:
  - route compatibility drift into the live read-only consumer path
  - remove scanner-as-gate carry from active governance
  - tighten the observed runtime source contract to the canonical repo-local runtime path
