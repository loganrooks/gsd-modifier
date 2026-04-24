# Readiness Protocol

This file defines how to operate the readiness package without relying on ambient session memory.

## Read Order

1. [INDEX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/INDEX.md)
2. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
3. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
4. [STATE.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATE.yaml)
5. the active checkpoint file under [GATES/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES)
6. [CHECKPOINT-REVIEW-MATRIX.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md) when deciding checkpoint review depth
7. [REVIEW-POLICY.yaml](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml) for machine-readable closure and independence rules
8. [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md) when an audit or review needs explicit epistemic definitions rather than inherited philosophical shorthand
9. [CLAUDE-REVIEW-COMMANDS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/CLAUDE-REVIEW-COMMANDS.md) when a Claude cross-vendor lane is actually being run
10. [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md) when multiple audits or reviews address the same artifact under different specs or production conditions
11. [AUDIT-SPEC-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-SPEC-TEMPLATE.md) when writing or revising a reusable audit spec, adjudication spec, reread spec, or cross-vendor review prompt

## Mandatory Updates

Update `STATUS.md` and `STATE.yaml` whenever:

- the active checkpoint changes
- the next action changes
- a blocker is found or cleared
- commit readiness changes

Update the active gate file whenever:

- evidence is reviewed
- a gate is reopened
- a gate is provisionally or strongly satisfied
- a gate is closed

Write or update an explicit audit artifact under [AUDITS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS) whenever:

- the active checkpoint is primarily an audit or scoping pass
- the checkpoint needs a reusable task spec or onboarding surface
- a later patch or deeper audit will depend on the resulting audit output

When writing or revising a reusable audit spec or multi-lane bundle:

- use `AUDIT-SPEC-TEMPLATE.md`
- explicitly check read-set adequacy before launch
- distinguish candidate, consumer, and representation / chain-tail surfaces where relevant
- if the spec is an adjudication, include enough direct spot-check surfaces to verify contested lane claims
- if the spec is a reread, include enough material to judge evidence-base adequacy, not only conclusion quality
- if sibling lanes use parallel output structures, explicitly guard against false convergence in the adjudication lane

Write or update an explicit review artifact from [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md) whenever:

- a checkpoint receives `internal-verification-agent` review
- a checkpoint receives `cross-vendor-reread`
- a gate is closed on the strength of a non-trivial review judgment rather than only mechanical closure
- store review artifacts under [REVIEWS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS)
- when a review shape is likely to be rerun, persist the reusable base review spec alongside the outputs in `REVIEWS/`
- on later rereads, reuse the stored review spec and add only a short delta note rather than rewriting the full spec

If the review uses the Anthropic Claude lane:

- persist the prompt file in the repo first
- use the command patterns in `CLAUDE-REVIEW-COMMANDS.md`
- prefer alias-based selectors in live policy and commands: `sonnet` for routine external audit, `opus` for high-stakes external audit
- record the exact Claude selector and effort actually used in the review artifact
- on Opus 4.7, prefer `xhigh` as the default high-stakes effort tier; reserve `max` for the hardest adversarial or doctrine-reopening rereads
- for large doctrine / adjudication / reread lanes on Max, prefer explicit `opus[1m]` or the current CLI's full-name equivalent rather than relying on implicit Opus selection
- record when `1m` was used because this package has now observed a same-lane difference: non-`[1m]` Opus reread ended with `Prompt is too long`, while the explicit `1m` Opus rerun completed and wrote the artifact

Update `TASKS.md` whenever:

- a readiness-relevant task changes status
- a new blocking task is discovered
- a task is deferred or reactivated

Update `OPPORTUNITIES.md` whenever:

- review or research finds a non-blocking but meaningful quality-upside opportunity
- an opportunity changes route
- an opportunity is promoted into an active task or deferred further

Update `RESEARCH-INTAKE.md` whenever:

- a research bundle materially changes readiness understanding
- a research bundle is accepted, partially accepted, parked, or superseded
- research creates a new task, deferral, or gate condition
- a bundle previously treated as conditional becomes blocking or vice versa

Update `DEVIATIONS.md` whenever:

- the sequence changes materially
- a checkpoint is skipped, split, or reordered

Update `CHECKPOINT-LEDGER.md` whenever:

- a readiness checkpoint commit is created
- a planned boundary is intentionally postponed
- a meaningful readiness-support commit changes package doctrine, review policy, or intake behavior

Write an explicit comparison ledger under [REVIEWS/](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS) whenever:

- multiple audits or reviews materially disagree about a load-bearing artifact
- audits were run under different specs or epistemic framings
- the next revision depends on qualifying claims by epistemic standing rather than by simple agreement

## Commit Protocol

- Prefer checkpoint commits at meaningful reasoning or scope boundaries.
- Before delegating substantial bounded edits, establish an auditable baseline.
- Prefer a checkpoint commit when the current state is coherent and reviewable.
- If the state is not coherent enough to commit, split or park it rather than forcing a bad baseline.
- Do not merge unrelated readiness concerns into one checkpoint just because they happened close together in time.
- If a research bundle materially changes readiness doctrine or gate logic, checkpoint the package-side intake/update separately from the research bundle when that yields a cleaner audit trail.
- For major checkpoint closure, do not let the same lane both author and solely certify closure. Use the independence rule in `REVIEW-POLICY.yaml`.

## Stop / Escalate Conditions

Stop and escalate instead of pushing through if:

- the active checkpoint reveals a deeper checkpoint should become active first
- current canon looks inconsistent enough that readiness work is no longer the right next layer
- the rerun begins reintroducing asymmetries already corrected in `05-gap-closure`
- a worker output cannot be cleanly accepted, revised, parked, or rejected

## Gap Handling Rule

When review finds gaps, do not jump straight from "finding exists" to "patch something."

Classify the gap first using the disposition ladder in [REVIEW-TEMPLATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEW-TEMPLATE.md):

- `accept`
- `revise-current`
- `reopen-current`
- `reactivate-earlier`
- `escalate-cross-vendor`
- `user-consult`
- `defer-nonblocking`

The review artifact should make that classification explicit before further work proceeds.

If the classification is `strategic-opportunity`:

- do not bury it in prose
- route it into `OPPORTUNITIES.md`
- decide whether it belongs to a later checkpoint, deferred follow-through, or post-rerun seed work

If multiple audits exist for the same artifact:

- do not flatten them into one blended verdict immediately
- compare them using `AUDIT-COMPARISON-POLICY.md`
- classify claims by convergence, support, contestation, pressure-only status, or weakness
- revise from the strongest surviving claims first

If the artifact being reviewed is itself a spec or prompt bundle:

- do not stop at whether the spec is readable or demanding
- ask whether it is architected to make later under-scoping difficult
- ask what a strong later reviewer would still say the spec cannot read, cannot verify, or cannot adjudicate responsibly

## Quality Standard

The target is not mere pass/fail clearance.

Each gate should be judged in terms of:

- whether the work is strong enough to carry forward
- whether it would survive later stringent audit
- whether it reduces future re-litigation rather than merely unblocking the next step
- whether it reflects the best reasonable work that could have been produced at this stage rather than merely acceptable work

Review posture should therefore be:

- high-expectation
- gap-exposure and completeness-challenge oriented
- post-verificationist and post-falsificationist rather than naively either one
- firm and specific
- justified rather than arbitrary

Do not confuse rigor with rudeness.

- reviewers should not be soft for the sake of tone
- reviewers should not be harsh for the sake of posture
- reviewers should push clearly on thin reasoning, weak evidence, premature closure, and avoidable quality compromise
