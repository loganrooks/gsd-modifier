# Checkpoint 5 R5.18b Review Planning Chain Launch Internal R1

## Outcome

- [d:c:i] `R5.18b` landed on the authorized review/planning trunk plus the admitted `gsd-do` / `workflows/do.md` router pair, matching the launch spec and `R5.18a1` boundary decision. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18b-review-planning-chain-launch-spec.md:3-28`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:199-203`.
- [d:c:i] The review consumer chain now carries an explicit planner-facing contract instead of a soft-consensus-only handoff: the review skill/workflow preserve lone high-signal criticism and later-audit risk, the planner reference classifies must-address versus rebuttal-required items, and the plan/check/revision workflow enforces that `--reviews` actually consumes that contract. Sources: `.codex/skills/gsd-review/SKILL.md:48-55`; `.codex/get-shit-done/workflows/review.md:1-10,121-145,242-315`; `.codex/get-shit-done/references/planner-reviews.md:7-68`; `.codex/skills/gsd-plan-phase/SKILL.md:48-61`; `.codex/get-shit-done/workflows/plan-phase.md:673-723,778-857,941-957`.
- [d:c:i] The admitted router pair is now treated symmetrically: the `gsd-do` wrapper and `do.md` dispatcher distinguish external plan review, replan-from-review-feedback, and verification of already-implemented work instead of collapsing them into one generic review route. Sources: `.codex/skills/gsd-do/SKILL.md:48-55`; `.codex/get-shit-done/workflows/do.md:35-96`.

## Changed Files

- `.codex/skills/gsd-review/SKILL.md` — reframed the skill as adversarial plan review and made the `REVIEWS.md` consumer contract explicit. Source: `.codex/skills/gsd-review/SKILL.md:2-5,48-55`.
- `.codex/get-shit-done/workflows/review.md` — strengthened reviewer instructions, added the `Review Consumer Contract` synthesis block, and surfaced a lone high-signal concern in the completion summary. Source: `.codex/get-shit-done/workflows/review.md:1-10,121-145,242-315`.
- `.codex/get-shit-done/references/planner-reviews.md` — formalized must-address, rebuttal-required, and safe-to-defer handling for `--reviews` replans. Source: `.codex/get-shit-done/references/planner-reviews.md:7-68`.
- `.codex/skills/gsd-plan-phase/SKILL.md` — made review-aware replanning explicit and added `planner-reviews.md` to execution context. Source: `.codex/skills/gsd-plan-phase/SKILL.md:2-5,48-61`.
- `.codex/get-shit-done/workflows/plan-phase.md` — added review-contract reading to the planner, required review-disposition sections on review-mode completions, gave the checker direct `REVIEWS.md` enforcement guidance, and kept the revision loop from dropping must-address review items. Source: `.codex/get-shit-done/workflows/plan-phase.md:673-723,778-857,941-957`.
- `.codex/skills/gsd-do/SKILL.md` — clarified that review, replan-from-review-feedback, and implemented-work verification are distinct routes. Source: `.codex/skills/gsd-do/SKILL.md:48-55`.
- `.codex/get-shit-done/workflows/do.md` — added explicit routing for `$gsd-review` and `$gsd-plan-phase --reviews` and preserved preset flags during dispatch. Source: `.codex/get-shit-done/workflows/do.md:35-96`.

## Restrictions Obeyed

- [d:c:i] Stayed inside the owned write set and the exact `R5.18b` authorization. No edits were made to `next`, `resume-project`, `manager`, chain-tail `R5.18c` surfaces, or any other non-promoted boundary item. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18b-review-planning-chain-launch-spec.md:13-35`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:199-203`.
- [d:c:i] Kept `R5.18a2` remainder ownership interpretive only. No broader later-lane concerns were pulled back into this wave, and no `R5.18a1` keep-out was revised. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-internal-r1.md:96-110`.
- No commit was created.

## Open Issues

- [o:c:i] The broader out-of-wave remainder stays open by design: `R8.1` through `R8.4`, the parked contradiction-ledger items, and the chain-tail/debt-carrier work were not part of this launch and remain owned elsewhere. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18b-review-planning-chain-launch-spec.md:30-35`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md:203-215`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-internal-r1.md:96-110`.
- The repo-local `.codex/*` runtime surface edited here is not tracked by Git in this repository, so tracked-path diff reporting was unavailable for these files; verification therefore relied on direct file-content checks instead of normal staged/tracked diff tooling.

## Verification

- `rg -n "Review Consumer Contract|Must Address In Replan|Review Feedback Addressed|lone high-signal|gsd-review|gsd-plan-phase --reviews|peer-reviewing plans|must-address review concern"` over the owned files confirmed the new review-consumer and router markers were present.
- `rg -n "[ \t]+$"` over the owned files returned no matches.
