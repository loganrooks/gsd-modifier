# Checkpoint Review Template

Use this for explicit readiness checkpoint reviews.

## Review Stance

- Review against a high bar, not a minimal pass bar.
- Be firm, clear, and specific when the work is weak, thin, or settling for adequacy.
- Do not be rude, performatively harsh, or arbitrarily negative.
- Criticism must be justified in terms of a higher standard of work:
  - rigor
  - auditability
  - architectural soundness
  - future viability
  - quality of judgment
- Do not treat `technically passes` or `mostly fine` as sufficient if a stronger artifact was reasonably achievable.
- Challenge closure-readiness and completeness seriously before declaring an artifact strong.
- Do not reduce the stance to naive verification or naive falsification; the goal is justified gap exposure and completeness challenge.

## Header

- checkpoint:
- artifact(s) under review:
- review mode:
  - `local-reread`
  - `internal-verification-agent`
  - `cross-vendor-reread`
- authoring lane:
- reviewer:
- model / reasoning or vendor:
  - for `internal-verification-agent`, default is `gpt-5.4 high`
  - for `cross-vendor-reread`, name the exact Claude selector used, normally `sonnet` or `opus`
  - if a large-context Claude lane was used, record the exact selector too, for example `opus[1m]` or the current CLI's full-name equivalent
- baseline commit / artifact snapshot:
- independence relationship:
  - `independent`
  - `same-lane`
  - `cross-vendor`

## Review Questions

- What closure, completeness, or strength claim is this review trying to challenge?
- Which gate exit criteria are being tested?
- Which quality questions are being tested?
- Which regressions are most relevant here?
- What is the strongest justified criticism of this artifact?
- What is merely adequate here but should be stronger?
- What would fail later stringent audit by strong engineers, designers, or researchers?
- What meaningful quality opportunity is being left unused?

If the artifact under review is itself a spec, prompt, or audit bundle, also ask:

- Is the read set strong enough, or are there omitted producer / consumer / chain-tail / representation surfaces that would materially change the result?
- Can an adjudicator or reread lane directly verify contested claims, or is it forced to trust prior lane outputs too much?
- Does the spec ask whether its own read set may be incomplete?
- Does the output structure risk false convergence, false closure, or evidence-thin confidence?
- Does the spec give the reread lane enough material to judge evidence-base adequacy rather than only conclusion quality?

## Findings

List findings in severity order with concrete file references where possible.

- Do not soften a finding just to sound polite.
- Do not inflate a finding just to sound demanding.
- Tie every material criticism to a clear standard the artifact is not yet meeting.

## What Is Already Strong

State what is genuinely strong so the later fix pass preserves it rather than regressing it.

## Gap Classification

For each material problem, classify the required response as one of:

- `accept`
  No material gap found.
- `revise-current`
  Fix inside the current checkpoint, then rereview.
- `reopen-current`
  The checkpoint is not ready to close; more than a narrow fix is required.
- `reactivate-earlier`
  The problem actually belongs to an earlier checkpoint or upstream doctrine/harness layer.
- `escalate-cross-vendor`
  Internal review is insufficient; independent external reread should occur if available.
- `strategic-opportunity`
  Not a blocker, but a meaningful short- or long-term quality opportunity should be tracked explicitly.
- `user-consult`
  The result changes the sequence or exposes a real strategic choice.
- `defer-nonblocking`
  Real issue, but not a readiness blocker now.

## Verdict

- status:
  - `blocked`
  - `provisional`
  - `strong`
  - `ready-to-carry-forward`
- explanation:
  Explain whether the artifact is merely acceptable, genuinely strong, or still too thin to carry forward safely.

## Required Next Action

- exact next step:
- owner / lane:
- commit implication:
  - no commit yet
  - fix then commit
  - checkpoint now

## Independence Note

- Does this review satisfy the checkpoint's independent-review requirement?
- Was a cross-vendor lane available?
- If cross-vendor was available, which Claude lane was appropriate here and why?
- If not used, why not?
- If used, what did independence add?
