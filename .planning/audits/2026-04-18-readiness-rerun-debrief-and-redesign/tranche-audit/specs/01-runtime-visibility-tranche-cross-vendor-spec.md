Date: 2026-04-20
Status: active spec

# Runtime Visibility Tranche Cross-Vendor Spec

## Framing

- [g:r:i] Audit the recently landed runtime-visibility tranche for leverage, carry, gaps, and next-step improvement pressure.
- [g:r:i] Do not answer in threshold terms such as `adequate`, `sufficient`, `good enough`, `passes`, `ready`, or similar gate language unless you are naming a literal operational gate.
- [g:r:i] The governing question is not whether the tranche can barely carry. It is what this tranche now exposes, what it still flattens or leaves weakly carried, and what stronger next move would improve intervention planning across the harness ecosystem.

## Primary Questions

1. What are the tranche’s strongest load-bearing gains?
2. What still looks weak, under-classified, over-classified, or strategically under-carried?
3. Is the current `runtime_visibility.py` first pass shaped correctly for its purpose, or is there a stronger narrow design available?
4. What should the next improvement step be:
   - widen family coverage
   - persist selected ignored snapshots
   - sharpen overlay-expansion / cleanup decisions
   - something else
5. Should the repo’s `AGENTS.md` doctrine be translated into `CLAUDE.md`-equivalent surfaces for cross-vendor Claude lanes?
   - If yes, what should be mirrored directly?
   - What should stay repo-local to `AGENTS.md` only?
   - What risks come with naive mirroring?

## Output Shape

Use these exact section headings:

1. `Load-Bearing Gains`
2. `Gaps And Weak Spots`
3. `Runtime-Visibility Tool Judgment`
4. `AGENTS.md -> CLAUDE.md Translation Judgment`
5. `Recommended Next Moves`

Within `Recommended Next Moves`, separate:
- `Do Now`
- `Do Next`
- `Hold`

## Review Discipline

- [d:r:i] Be concrete about what in the packet supports each judgment.
- [d:r:i] Do not rest on generic praise or generic caution.
- [d:r:i] If you think a design choice is weak, name the stronger narrow alternative and why it is stronger.
- [d:r:i] If you think a proposed `CLAUDE.md` translation layer is warranted, distinguish:
  - direct mirroring
  - selective translation
  - translation plus local wrapper/launcher discipline

## Read Set And Token Estimates

Primary read set words:
- intervention tranche core (`07`-`10`): `2689`
- onboarding/materialization companions: `2534`
- runtime visibility tool + tooling note: `1097`
- repo instruction surfaces (`AGENTS.md`, `.planning/AGENTS.md`): `3160`
- primary total: `9480` words

Planning token band:
- low: `~12.0k`
- working: `~14.5k`
- high: `~17.0k`

Reserve only if truly needed:
- [CURRENT-STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md)
- [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/STATUS.md)

## Output Paths

- Opus output:
  - [tranche-audit/outputs/01-runtime-visibility-tranche-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/tranche-audit/outputs/01-runtime-visibility-tranche-opus47-max-r1.md)
- GPT-5.4 xhigh output:
  - [tranche-audit/outputs/01-runtime-visibility-tranche-gpt54-xhigh-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/tranche-audit/outputs/01-runtime-visibility-tranche-gpt54-xhigh-r1.md)
