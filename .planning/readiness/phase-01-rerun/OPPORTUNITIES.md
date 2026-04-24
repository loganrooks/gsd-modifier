# Readiness Opportunities

This file records non-blocking but meaningful opportunities discovered during readiness work.

Use it for findings that:

- are not required to clear the current checkpoint
- would materially improve short-term readiness quality, long-term harness quality, or future planning honesty
- should not disappear just because they are not current blockers

## Fields

For each opportunity, record:

- item
- discovered_at
- why_it_matters_now
- short_term_upside
- long_term_upside
- current_route
  - `later-checkpoint`
  - `deferred-follow-through`
  - `seed-for-post-rerun`
- reactivation_trigger

## Active Opportunities

| Item | Discovered at | Why it matters now | Short-term upside | Long-term upside | Current route | Reactivation trigger |
|---|---|---|---|---|---|---|
| repo-local non-phase external-reread protocol/template | focused cross-model audit integration research | the repo now knows the likely later gap is protocol discipline rather than a new skill, and losing that finding would make later workflow/harness follow-through weaker | cleaner later cross-vendor rereads during readiness or post-rerun governance work | stronger durable review discipline without overbuilding the harness | `later-checkpoint` | if Checkpoints 1-4 settle and later harness follow-through still needs a repeatable non-phase external-reread surface |
| downstream claim-discipline and steering-traceability hardening | Checkpoint 4 workflow/doctrine audit bundle | the current rerun blocker is not “fix every later artifact,” but the audit proved that planning/review/verification still flatten evidence-basis and steering richness too early | clearer later review and stronger post-rerun planning honesty | more scrutiny-resistant planning/process artifacts across the repo | `deferred-follow-through` | if Checkpoint 5 or Checkpoint 6 shows these weaknesses are still distorting rerun-quality judgment |
| modernize `gsd-rigorous-research` into a more general, doctrine-current GSD research lane | current Checkpoint 5 runtime regression inspection plus user correction | the skill is repo-authoritative for non-phase research, but it still carries older claim discipline and too much project-shaped framing, so later harness work will lose quality if this stays stale | better standalone research lanes and cleaner later harness design work without overloading the active rerun-critical checkpoint | stronger epistemic research doctrine across GSD, better alignment with newer claim/status discipline, and a cleaner integration point with the rest of the workflow chain | `deferred-follow-through` | once Checkpoint 5 is stabilized and can cleanly spin out a dedicated improvement lane for the skill, its references, and its integration contract |
| split portable-GSD improvements into reusable core delta plus repo-local adoption layer | current Checkpoint 5 portability discussion plus internal review of `overlay/config.toml` | the repo is accumulating meaningful harness improvements, but some are genuinely general while others are tightly prix-guesser-specific, and that distinction will matter if we later want to adopt this stack in another repo like `f1-modeling` | clearer local reasoning now about what belongs to rerun-critical repo overlay versus later generalization work | a portable migration path, cleaner `new-project` / `new-milestone` future-awareness propagation, and a more reusable modified GSD distribution | `deferred-follow-through` | once the current rerun-critical slice is closed and the repo can spin up a dedicated portability/generalization lane without muddying Checkpoint 5 |

## Promoted Opportunities

| Item | Promoted from | Why promoted now | Active task / surface |
|---|---|---|---|
| propagate readiness gap-exposure review doctrine into repo-local GSD review/audit surfaces | readiness review-policy hardening plus current Checkpoint 5 discussion | the planning/research slice is now committed and Checkpoint 5 has returned to the Track B review / closure-pressure lane, so this is no longer merely a later opportunity | `R5.15`; `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md`; `tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md` |
| broader post-verificationist / post-falsificationist exclusion / modification-consideration audit across GSD and adjacent governance surfaces | current Checkpoint 5 discussion about stronger gap-exposure doctrine and wider downstream quality | `R5.18` is itself the current modification frontier, so the question `what is being excluded from modification consideration at all, and why?` can no longer sit downstream of it | `R5.19`; [checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-19-broader-exclusion-and-modification-disposition-audit-bundle-spec.md) |
