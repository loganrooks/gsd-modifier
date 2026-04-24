Date: 2026-04-22
Status: completed parent-thread packet output

# Uplift Cross-Runtime Comparison First Exercise

## Runtime Topology Under Comparison

- [e:c+i] The current uplift baseline is explicitly `cross-runtime uplift`, with `.codex` and `.claude` both present, while the compatibility anchor remains `observed_basis_only` rather than a cross-runtime matrix. Sources:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:5)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:13)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:25)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:19)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:79)
- [e:b:i] The bounded runtime evidence for this packet is:
  - `.codex` runtime version / manifest version: `1.38.3` / `1.38.3`
  - `.claude` runtime version / manifest version: `1.34.2` / `1.34.2`
  - `.codex` has repo-local uplift/propagation/seed-migration routes
  - `.claude` currently does not

## Shared Basis

- [e:c+i] Repo doctrine is shared through the wrapper layer rather than duplicated canon:
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) is authoritative for repo doctrine
  - [CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/CLAUDE.md) routes Claude work back to `AGENTS.md`
  - [.planning/CLAUDE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/CLAUDE.md) routes planning-local Claude work back to `.planning/AGENTS.md`
- [d:r:i] Both runtimes still participate in the ordinary continuation floor:
  - `.codex` carries `progress` and `resume-project`
  - `.claude` carries `progress` and `resume-project`
- [e:c+i] Current uplift memory already refuses to collapse cross-runtime presence into a settled composition claim; it keeps that family explicit and held for later. Sources:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md:41)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json:33)

## Runtime-Specific Divergences Or Unknowns

- [d:r:i] `.codex` is the only runtime inside the current compatibility anchor. That means the current uplift memory certifies observed `.codex` basis discipline, not parity with `.claude`.
- [e:b:i] `.codex` now carries repo-local routes that do not yet have `.claude` counterparts:
  - `uplift-project`
  - `propagation-review`
  - `seed-migration-inventory`
- [d:r:i] The present cross-runtime difference is therefore not only version drift. It is also route asymmetry:
  - wrapper-level doctrine translation is present
  - continuation surfaces are present on both sides
  - newer repo-local harness routes remain Codex-only
- [o:r:i] What is still unresolved is not whether `.codex` and `.claude` differ. It is how that difference should later be carried:
  - direct `.claude` route translations
  - wrapper-only plus packet-driven guidance
  - another narrower consumer path
  - or a family-by-family staged mix

## Held Composition Questions

- [o:r:i] Should cross-runtime support mean shared doctrine only, or shared doctrine plus translation of selected repo-local routes?
- [o:r:i] Should the compatibility family later grow from `observed_basis_only` into an explicit `.codex` / `.claude` matrix?
- [o:r:i] Should `uplift-project`, `propagation-review`, and `seed-migration-inventory` remain Codex-only composition routes, or should some narrower `.claude` counterparts later exist?
- [o:r:i] If later translation is earned, should it happen per-family rather than as one wide cross-runtime parity push?

## Later Route Ownership

- [d:r:i] The next adjacent move is a bounded Opus widening lane over this first packet, not immediate `.claude` translation work and not a direct composition judgment.
- [d:r:i] Parent-thread ownership remains in force for:
  - any live runtime mutation
  - any durable uplift-memory refresh tied to later cross-runtime movement
  - any eventual composition judgment
- [d:r:i] If the question later becomes a concrete multi-family contract change rather than a packet-level comparison, route it through `$gsd-propagation-review`.
- [d:r:i] Until an explicit multi-runtime compatibility family is opened, the current compatibility anchor should keep owning observed-basis discipline only.
