**Entry Runtime Uplift Continuity**

Use this reference at entry routes when initialization or doc ingest needs bounded repo-local runtime continuity. This surface is read-only in character: it tells the workflow what to read first, when to widen, and which claims must stay held without turning entry into write-side uplift dispatch.

## Primary Compact Read

- Start from the active route-state signal:
  - `new-project.md`: `init.new-project`, current execution-context runtime, and whether the route is greenfield or brownfield
  - `ingest-docs.md`: `MODE`, current execution-context runtime, and whether `.planning/STATE.md` already carries `## Project Uplift`
- If `.planning/STATE.md` already exists and carries `## Project Uplift`, read that compact block first
- When `.planning/` does not exist yet, keep the compact read at route-state plus current execution context rather than pretending durable uplift memory already exists

## Supporting Narrative Read

- Widen into `.planning/UPLIFT-REPORT.md` only when existing uplift memory exists and the compact route-state view does not carry enough entry continuity context
- Keep the widening bounded to entry/runtime continuity; do not reopen broader governance, audit, or installer families unless the route explicitly depends on them

## Deeper Typed Read

- Widen into `.planning/UPLIFT-MANIFEST.json` only when existing uplift memory exists and basis or annotation ambiguity remains after the compact digest plus narrative report
- Use the typed surface to clarify observed basis, held runtime annotation, pending doctrine-sensitive proposals, or held-later family state when the entry route materially depends on those distinctions

## Interpretation Frame

- `Compatibility posture: observed_basis_only` remains the top-level posture
- Held runtime annotation stays annotation, not dual-basis relabeling
- Repo-local entry continuity here is about observed `.codex` basis plus held `.claude` annotation
- Broader installer/runtime detection across additional providers remains a separate workflow concern in this slice
- Entry routes may surface this continuity; they do not widen it into parity, translation, matrix, or version-window claims
- Do not run `$gsd-uplift-project --write` from `new-project.md` or `ingest-docs.md`
- When `.planning/` does not exist yet, use this reference to keep generated canon and operator reasoning aligned, not to claim that durable uplift memory already exists

## When To Surface

### `new-project.md` Greenfield

Surface the continuity route only when one or more of these are true:

- repo-local runtime or governing doctrine is already present in the repo and should remain explicit in the first canon
- the initialization route explicitly raises runtime or governing continuity pressure that later uplift work would otherwise have to rediscover
- the operator needs to keep observed `.codex` basis plus held `.claude` annotation explicit while still leaving write-side uplift for later

### `new-project.md` Brownfield

Surface the continuity route when one or more of these are true:

- existing code or docs show this repo is not a blank start even though `.planning/` is absent
- brownfield mapping, prior findings, or repo-local doctrine suggests later uplift or migration pressure
- initialization needs to keep observed `.codex` basis plus held `.claude` annotation explicit without widening into write-side uplift

### `ingest-docs.md` New Mode

Surface the continuity route when one or more of these are true:

- imported docs are older or vanilla GSD docs entering a repo-local harness
- new-mode ingest is creating `.planning/` inside a repo where runtime or governing continuity should stay explicit from the start
- later repo-local uplift follow-through is likely, but should remain a separate route after import

### `ingest-docs.md` Merge Mode

Surface the continuity route when one or more of these are true:

- existing `.planning/STATE.md` already carries `## Project Uplift`
- merge review or conflict handling touches runtime, governance, or uplift-adjacent carriers
- imported docs predate current repo-local uplift continuity doctrine and could thin it if left ambient
