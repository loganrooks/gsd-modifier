**Milestone-Boundary Uplift Continuity**

Use this reference at milestone open and milestone close when the route needs bounded project-uplift continuity. This surface is read-only in character: it tells the workflow what to read first, when to widen, and which claims must stay held.

## Primary Compact Read

- Start with `.planning/STATE.md`
- Read the top-level `## Project Uplift` block first when it exists
- Treat that compact block as the default milestone-boundary uplift digest

## Supporting Narrative Read

- Widen into `.planning/UPLIFT-REPORT.md` only when the compact digest does not carry enough operator-facing context for the active milestone-boundary judgment
- Keep the widening bounded to the uplift route; do not reopen broader governance or audit families unless the route explicitly depends on them

## Deeper Typed Read

- Widen into `.planning/UPLIFT-MANIFEST.json` only when runtime profile or policy ambiguity remains after the compact digest and narrative report
- Use the typed surface to clarify observed runtime profiles, mixed-runtime policy, secondary runtime observation, pending doctrine-sensitive proposals, or held-later family state when the milestone-boundary route depends on them

## Interpretation Frame

- `Compatibility posture: core_runtime_parity` remains the top-level posture
- `Observed runtime profiles` stay the compact runtime evidence line
- `Mixed-runtime policy` stays policy, not a claim that dual-runtime support is already green
- `Secondary runtime observation` remains a helper line, not the parity claim itself
- Milestone boundaries may surface uplift posture
- Milestone boundaries do not widen that posture into parity, translation, matrix, or version-window claims
- Do not run `$gsd-uplift-project --write` from milestone boundaries; they read uplift continuity here and do not become write-side compatibility dispatch
- This reference sits beside milestone-boundary long-arc and future-carry review
- This reference reads the `## Project Uplift` block preserved by transition/state continuity; it does not absorb that route into milestone workflows

## When To Surface

### Milestone Open

Surface the uplift route when one or more of these are true:

- observed runtime profiles moved since the previous milestone
- mixed-runtime policy changed since the previous milestone
- `pending_doctrine_sensitive_proposals` is greater than zero
- a `held_later_families` partial landing is relevant to the next milestone's target scope
- the current `phase_boundary_signal.mid_phase_signal` changes what belongs in the milestone-opening packet

### Milestone Close

Surface the uplift route when one or more of these are true:

- the milestone changed observed runtime profiles
- mixed-runtime policy changed during the milestone
- seed corpus posture changed during the milestone
- `held_later_families` gained or closed partial-landing entries during the milestone
- doctrine-sensitive carrier posture changed during the milestone's phases
