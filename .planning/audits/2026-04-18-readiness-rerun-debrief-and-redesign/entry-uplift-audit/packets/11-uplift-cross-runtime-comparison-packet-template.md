Date: 2026-04-22
Status: landed packet template

# Uplift Cross-Runtime Comparison Packet Template

## Purpose

- [g:r:i] Use this packet when the concrete uplift question is no longer doctrine-sensitive drift or additive-install absence, but how the current repo-local runtime topology should be compared across more than one runtime surface.
- [g:r:i] This packet narrows the question to one auditable comparison packet.
- [g:r:i] It does not itself decide cross-runtime composition.

## Input Bundle

- [d:r:i] Current uplift detect JSON
- [d:r:i] Current durable uplift outputs:
  - `.planning/UPLIFT-REPORT.md`
  - `.planning/UPLIFT-MANIFEST.json`
  - `STATE.md` uplift section
- [d:r:i] Current runtime topology note:
  - which runtime dirs are present
  - which runtime is treated as the observed basis
  - which runtime claims are still held later
- [d:r:i] One bounded runtime evidence bundle as relevant to the comparison:
  - runtime-visibility snapshot or report
  - manifest/install coherence artifact
  - observed runtime `VERSION` / manifest sources
- [d:r:i] Only the named cross-runtime governance or wrapper carriers under current review:
  - root `AGENTS.md`
  - root `CLAUDE.md`
  - specific `.claude/` or `.codex/` runtime surfaces when they are the actual comparison target

## Packet-Time Scope Note

- [d:r:i] Name the exact comparison question:
  - runtime presence only
  - shared basis versus divergence
  - wrapper or instruction-surface translation
  - held-later composition pressure
- [d:r:i] Keep the packet bounded to the current comparison question.
- [d:r:i] Do not let the packet silently widen into:
  - full cross-runtime composition
  - upstream-template drift machinery
  - runtime mutation

## Questions To Answer

- [d:r:i] Which runtimes are concretely present and which runtime currently serves as the observed basis?
- [d:r:i] Which comparison surfaces are shared enough to compare now without overclaiming?
- [d:r:i] Which divergences are already explicit and which remain held rather than settled?
- [d:r:i] Which later composition questions should remain explicit after the packet instead of being collapsed prematurely?

## Output Shape

```markdown
# Uplift Cross-Runtime Comparison

## Runtime Topology Under Comparison
- ...

## Shared Basis
- ...

## Runtime-Specific Divergences Or Unknowns
- ...

## Held Composition Questions
- ...

## Later Route Ownership
- ...
```

## Write Boundary

- [d:r:i] Packet plus bounded output plus parent-thread disposition only
- [d:r:i] No direct runtime mutation
- [d:r:i] No durable uplift-memory mutation inside the packet itself
- [d:r:i] No automatic spawn
- [d:r:i] No helper or CLI widening
- [d:r:i] No cross-runtime composition decision in the packet itself
