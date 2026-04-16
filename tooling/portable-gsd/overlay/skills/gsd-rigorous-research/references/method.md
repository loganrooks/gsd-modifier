# Rigorous Research Method

## Core Commitment

Do not close the question more tightly than the evidence allows.

The job is not to sound decisive. The job is to make the terrain, the reasoning path, and the remaining uncertainty inspectable enough that later decisions are grounded and reversible.

## Mode Discipline

Pick one primary mode and state it up front.

### Terrain mapping
- Map the option space, hidden assumptions, and relevant precedents.
- Do not rank or recommend unless the user explicitly asks to switch modes.
- Good output: a legible map of what exists, what differs, and what remains unknown.

### Hypothesis testing
- Start from a candidate claim or approach.
- Look for failure cases and disconfirming evidence as aggressively as confirming evidence.
- Good output: whether the hypothesis survives, under what conditions, and what still underdetermines it.

### Solution evaluation
- Compare known options against explicit criteria.
- Only use this mode when the option space is already adequately mapped.
- Good output: comparison, tradeoffs, recommendation if warranted, and caveats if not.

### Synthesis
- Combine prior artifacts into one coherent decision structure.
- Preserve deferrals and unresolved tensions instead of flattening them away.
- Good output: integrated model, what can close now, what must stay open.

## Path Of Inquiry

Every substantial output should make the inquiry path visible:

- `Entry point` - what question or trigger started the work
- `Branches considered` - plausible lines of inquiry
- `Branches pursued` - which ones were followed and why
- `Branches deferred or abandoned` - what was set aside and why
- `Unexpected branches` - what surfaced during the work
- `Dead ends` - lines pursued that did not pay off
- `Reframings` - moments where the effective question changed

This is not narration for its own sake. It lets later readers inspect how the result was reached and what was not explored.

## Assumptions

Surface assumptions explicitly. At minimum:

- name the assumption
- explain why it is load-bearing
- state what could falsify or weaken it
- distinguish whether it came from project canon, user framing, or your own working model

Useful prompt: "What else am I committed to if I treat this as true?"

## Claim Vocabulary

Use this vocabulary when it helps clarify the status of a claim.

| Type | Meaning | What to do |
| --- | --- | --- |
| `evidenced` | Supported by a concrete artifact, measurement, citation, or code/doc reference | Verify and build on it |
| `decided` | Already chosen by user direction, canon, or explicit deliberation | Honor it unless the task is to reopen it |
| `assumed` | Working belief not yet verified | Test it or qualify it |
| `open` | Genuinely unresolved | Research it directly |
| `projected` | Justified by later phases, future wrappers, or anticipated needs | Validate the projection; do not silently enshrine it |
| `stipulated` | Chosen threshold, definition, or cutoff rather than measured fact | Say plainly that it is a choice |
| `governing` | Norm, doctrine, or value commitment that constrains the solution space | Respect it as a framework constraint |

Optional verification suffixes:

- `:cited` - directly checkable
- `:reasoned` - argued but not directly measured
- `:bare` - asserted without stated support

Examples:

- `[evidenced:cited]`
- `[assumed:reasoned]`
- `[open]`

## Evidence, Inference, And Unknowns

Keep these separate:

- `Evidence` - directly observed or cited facts
- `Inference` - reasoning built from evidence
- `Speculation` - plausible but weakly supported possibility
- `Unknown` - cannot honestly be assessed yet

Recommended confidence language:

- `known`
- `likely`
- `plausible`
- `speculative`
- `unknown`

Do not present speculation as fact. Do not blur an interpretation into a citation.

## Dependencies And Relations

Research should name relations, not just isolated facts.

Useful questions:

- What depends on this claim being true?
- What later decision does this constrain?
- What current assumption props up this conclusion?
- What future seam would be foreclosed if this closes too early?

A lightweight table is often enough:

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Claim / option / choice | upstream assumptions, canon, evidence | downstream design, planning, scope | low / medium / high |

## Scope Expansion Handling

When the work encounters a gray area beyond the original framing, respond explicitly:

### Defer
- The tangent exists but is not load-bearing for the current question.
- Record it as a known unknown and move on.

### Follow-and-mark
- The tangent is load-bearing and bounded enough to investigate now.
- Mark the expansion explicitly so the reader can see that the scope shifted.

### Revisit later
- The tangent is load-bearing but too large for the current round.
- Name why it matters, why it cannot be settled here, and what a later round should ask.

Never widen scope silently.

## Closure Rules

Always end with a direct statement of:

- what can close now
- what cannot close yet
- what remains deferred
- what evidence would change the current picture

If the evidence is thin, the correct outcome may be a bounded deferral rather than a recommendation.

## Anti-Patterns

Avoid:

- turning terrain mapping into premature solution evaluation
- hiding assumptions inside smooth prose
- citing canon selectively while ignoring conflicting docs
- silently importing future-scope concerns as if they were current requirements
- treating a later-phase projection as present-tense proof
- collapsing evidence, interpretation, and opinion into one paragraph
