Date: 2026-04-20
Status: active gap register

# Long-Horizon Carry Gap Register

## Purpose

- [g:r:i] Record the concrete places where long-horizon carry is already strong, where it still weakens or disappears, and where the harness still lacks better structures for managing multiple horizons without foreclosing stronger future options.
- [d:r:i] This is meant to be good audit input, not private chat memory.
- [d:r:i] A later cross-vendor lane should be able to read this artifact, challenge the claimed gaps, add missing ones, or narrow overclaimed ones.
- [g:r:i] The aim is not only to identify what is missing or under-carried. It is also to identify how the harness could become a materially stronger version of itself even where no simple deficiency claim is available.
- [g:r:i] The method here is not “find only the top few gaps.” It is to map the full pressure field: narrow gaps, medium-scope carry failures, system-wide tensions, positive strength opportunities, and the relations among them.

## Governing Observation

- [e:c+i] Long-horizon carry is already explicit at the front of the harness: `discuss-phase` derives `future_awareness`, `context.md` has explicit `Protected Seams` and `Explicit Non-Decisions` buckets, `plan-phase` requires that future-aware items become auditable `future_preservation`, and the local intervention layer already routes long-horizon goals toward `spec-phase`, `ingest-docs`, and `mandatory-initial-read`. Sources: [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:480), [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:482), [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:483), [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:126), [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:129), [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:132), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:700), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:701), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:703), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:54), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:59).
- [d:r:i] The live pressure is no longer “add future awareness somewhere.” It is:
  - preserve it through later lifecycle surfaces
  - make cross-horizon tensions more explicit
  - and keep the harness iterating toward a stronger overall form instead of only patching local omissions
- [d:r:i] So the controlling question is not merely “where is the harness deficient?” It is also “where could the harness positively intensify its power to carry more horizons, preserve more optionality, and support stronger long-run intervention design?”

## Concrete Lifecycle Gaps

| Surface | What is already strong | The gap | Why this gap is real | Likely intervention shape |
| --- | --- | --- | --- | --- |
| `verify-phase.md` | Goal-backward verification of current phase truths, artifacts, wiring, behavior | It does not explicitly verify whether preserved seams, explicit non-decisions, or `future_preservation` were actually honored | A phase can verify as behaviorally correct while still collapsing future structure | Add a future-preservation verification lane or explicit seam-preservation verdict block |
| `transition.md` | Debt-aware phase completion and roadmap/state updates | It evolves requirements and decisions, but not preserved seams, activation pressure, or long-arc consequences | Future-aware carry can be present in planning and then disappear at phase close | Add transition-time seam carry and activation review |
| `new-milestone.md` | Milestone goal gathering, seed scan, roadmap restart | It reads `PROJECT.md`, `MILESTONES.md`, and `STATE.md`, but not `LONG-ARC.md` or a seam register | New milestone framing can forget durable long-arc doctrine unless the operator remembers to restate it | Require long-arc / seam reread during milestone opening |
| `complete-milestone.md` | Requirements, stats, accomplishment, and milestone archive flow | It lacks an explicit long-horizon doctrine and preserved-seam review before closing a milestone | Milestone close can archive current work without checking what future seams were protected, activated, or narrowed | Add a long-horizon carry review block to milestone close |
| `templates/spec.md` | Strong WHAT/WHY locking and falsifiability | No explicit place for protected seams, explicit non-decisions, current posture, or future-shape notes | Long-horizon carry is stronger in `CONTEXT.md` than in the earlier spec surface that shapes downstream thinking | Add a bounded future-aware section to SPEC |
| `templates/state.md` and `progress.md` | Good short-horizon execution memory and routing | No compact long-horizon watchlist, live seam register, or activation-trigger summary | First-read surfaces are still mostly short-horizon, so future pressure becomes easier to forget between planning rounds | Add a lightweight horizon watch section or summary line |
| seed system | Triggered recall exists | Seeds are still idea-shaped more than seam-shaped | Preserve-only seams and long-horizon tensions do not yet have a dedicated trigger-carry format | Add seam-aware seed typing or a sibling artifact family |

## Evidence For The Concrete Gaps

### 1. Verification Gap

- [e:c+i] `verify-phase.md` loads phase goal, requirements, plans, summaries, and milestone phases, then verifies truths, artifacts, links, requirements, and behavior. It does not mention `future_awareness`, `future_preservation`, `Protected Seams`, or `Explicit Non-Decisions`. Sources: [.codex/get-shit-done/workflows/verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:28), [.codex/get-shit-done/workflows/verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:53), [.codex/get-shit-done/workflows/verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:95), [.codex/get-shit-done/workflows/verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:177), [.codex/get-shit-done/workflows/verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:186).
- [d:r:i] That means the harness currently verifies “does this phase work?” much better than “did this phase preserve the future seams it claimed to preserve?”

### 2. Transition Gap

- [e:c+i] `transition.md` reads `STATE.md`, `PROJECT.md`, `ROADMAP.md`, current plans, and summaries; checks completion debt; then updates roadmap/state and evolves requirements and decisions. It does not load `LONG-ARC.md`, seam registers, or future-preservation carry. Sources: [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:17), [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:41), [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:182), [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:209).
- [d:r:i] So the phase boundary that updates the project’s remembered state is still weak on future-aware carry-forward.

### 3. Milestone Boundary Gaps

- [e:c+i] `new-milestone.md` reads `PROJECT.md`, `MILESTONES.md`, and `STATE.md`, then scans seeds and gathers milestone goals. There is no explicit `LONG-ARC.md` or preserve-only seam reread in the opening sequence. Sources: [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:22), [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:30), [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:49), [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:136).
- [e:c+i] `complete-milestone.md` performs a full close and project evolution review, but its required reading and review checklist do not explicitly include `LONG-ARC.md`, seam preservation, or activation-trigger review. Sources: [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:7), [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:19), [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:84), [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:229).
- [d:r:i] Milestone open and close are therefore still weaker than phase discuss/plan at carrying cross-horizon doctrine.

### 4. SPEC Gap

- [e:c+i] `templates/spec.md` strongly locks goal, boundaries, constraints, and acceptance criteria, but contains no explicit section for future awareness, protected seams, explicit non-decisions, or future-shape notes. Sources: [.codex/get-shit-done/templates/spec.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/spec.md:5), [.codex/get-shit-done/templates/spec.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/spec.md:25), [.codex/get-shit-done/templates/spec.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/spec.md:47), [.codex/get-shit-done/templates/spec.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/spec.md:62).
- [d:r:i] That makes the early WHAT-stage narrower than the later context stage, which is the wrong direction if the harness is supposed to preserve long-horizon distinctions as early as it locks requirements.

### 5. STATE / Progress Gap

- [e:c+i] `templates/state.md` is a short-term execution memory artifact centered on current position, performance metrics, recent decisions, blockers, and session continuity. It has no explicit long-horizon carry section. Sources: [.codex/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/state.md:12), [.codex/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/state.md:47), [.codex/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/state.md:84), [.codex/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/state.md:123).
- [e:c+i] `progress.md` is strong on current execution status, debt, and route-to-next-action, but it does not surface long-horizon watchpoints, preserve-only seam triggers, or future-preservation risk. Sources: [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:93), [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:114), [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:135), [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:181).
- [d:r:i] Because these are first-read surfaces, their short-horizon bias matters more than it would in a less central artifact.

## Multi-Horizon Tension Gaps

- [d:r:i] The harness still lacks an explicit structure for handling tensions between:
  - what current execution needs now
  - what the next milestone should keep open
  - what the longer arc should not let current work foreclose
- [d:r:i] Right now, much of that tension is managed by good planning craft and by the existence of `future_awareness`, not by a dedicated tension-handling mechanism.

### Likely Missing Mechanisms

1. [d:r:i] **Horizon-tension register**
   - a compact structure that records when near-term optimization is in live tension with later seam preservation
   - not just “deferred,” but “active tension we are carrying deliberately”

2. [d:r:i] **Future-preservation verification**
   - a verification sub-pass or report block that checks whether declared preserved seams were actually preserved

3. [d:r:i] **Seam activation / seam closure lifecycle carry**
   - preserved seams exist, and activation-trigger doctrine now exists locally, but the lifecycle workflows do not yet visibly consume it

4. [d:r:i] **Long-horizon project-memory digest**
   - a way for `STATE.md` / `progress` to remind the operator what future structure is under active pressure without forcing a reread of the whole long arc

## Positive Self-Overcoming Pressure

- [g:r:i] The harness should not relate to its limits only negatively, as if its task were merely to heal deficiency back to some acceptable baseline.
- [g:r:i] A stronger framing is: which bounded interventions would let the harness carry more reality, more horizons, more optionality, and more deliberate self-transformation than it currently can?

### Likely Missing Positive Surfaces

1. [d:r:i] **Explicit strength-amplification register**
   - not just a list of gaps or weaknesses
   - a compact surface for recording the full field of next strengthening moves and their likely cross-effects across multiple dimensions

2. [d:r:i] **Cross-horizon strategy surface**
   - not only a place to preserve seams
   - a place to reason about how near-term moves can actively increase later strategic freedom rather than merely avoid collapse

3. [d:r:i] **Optionality-growth lens**
   - a way to ask, for any proposed intervention, whether it:
     - keeps options open
     - expands the space of viable future moves
     - or silently narrows later design possibilities

4. [d:r:i] **Harness self-transformation queue**
   - a standing, durable surface that records the next bounded moves that would raise the harness’s own quality, not just the quality of the project it is helping with

5. [d:r:i] **Multi-dimensional excellence basket**
   - a stable way to judge candidate interventions across dimensions such as:
     - maintainability
     - runtime authority clarity
     - long-horizon carry
     - operator legibility
     - auditability
     - update resilience
     - intervention yield
   - not to create a rigid scorecard, but to prevent one dimension from quietly dominating all others

## Best-Possible-Harness Pressure Gaps

- [d:r:i] If the target is not only “carry long-horizon distinctions better,” but “keep straining toward the best harness we can build,” then there are a few broader likely gaps too.

### 1. No Explicit Harness Self-Improvement Loop

- [d:r:i] The harness has many bounded audit and intervention lanes, but it still lacks one compact evergreen surface that says:
  - what the known harness weaknesses, tensions, and strength-opportunities are
  - what evidence supports each
  - how they relate, propagate, or conflict
  - what intervention slices are available across the whole field, not only the most obvious few
- [d:r:i] In practice, this is being carried by audit workspaces like this one rather than by a durable harness-self-improvement register.

### 2. Limited Cross-Dimensional Evaluation Of Harness Quality

- [d:r:i] The harness does not yet seem to evaluate itself explicitly across a stable basket like:
  - maintainability
  - runtime authority clarity
  - update resilience
  - long-horizon carry
  - operator legibility
  - auditability
  - cross-vendor reproducibility
  - intervention yield
- [d:r:i] Pieces of this exist, but not as one stable evaluative lens.

### 3. Weak Ideal-Oriented Iteration Surface

- [d:r:i] There is no dedicated recurring artifact that asks:
  - what would make this harness a materially stronger version of itself now
  - what still feels local, accidental, ceremonial, or too operator-memory-dependent
  - what bounded moves, taken together or in sequence, would increase long-run harness quality and expand future strategic freedom
- [d:r:i] That question keeps being asked by ad hoc audits rather than by a standing improvement surface.

## Whole-Field Mapping Rule

- [g:r:i] For this line of work, early narrowing is itself a risk.
- [g:r:i] The first obligation is to map the full surface set:
  - local lifecycle gaps
  - cross-horizon tensions
  - positive strength-building opportunities
  - system-memory weaknesses
  - self-improvement surfaces
  - and the interactions among them
- [d:r:i] Prioritization can come later, but only after the wider topology of pressures and opportunities is visible enough not to silently discard important paths.

### 4. Weak Positive Relation To Constraint

- [d:r:i] Constraint is still too easy to treat only as a brake, blocker, or deficiency marker.
- [d:r:i] A stronger harness would also ask:
  - which constraints are design-shaping and should be used productively
  - which constraints can be turned into better routing, better explicitness, or better memory structures
  - which current limitations are actually invitations to invent a stronger operating form
- [d:r:i] Without that positive relation, the harness risks becoming only good at diagnosing what it lacks rather than at inventing stronger forms of practice.

## Candidate Next Lanes

### Bounded Local Follow-Through

1. [d:r:i] Add a future-preservation verification layer to `verify-phase`
2. [d:r:i] Add preserve-only seam / activation review to `transition`
3. [d:r:i] Add long-arc / seam reread obligations to `new-milestone` and `complete-milestone`
4. [d:r:i] Add a bounded future-awareness block to `SPEC`
5. [d:r:i] Add a lightweight horizon-watch section to `STATE.md` / `progress`

### Cross-Vendor Audit Candidate

- [d:r:i] A later `Opus 4.7 Max` lane could use this artifact as its primary packet seed and answer:
  - how the full field of lifecycle, horizon-tension, and self-overcoming pressures should be mapped
  - which are overstated
  - which additional surfaces are missing
  - how the mapped pressures relate, cluster, propagate, or conflict
  - which intervention families become visible only once the whole field is mapped
  - whether the broader “best possible harness” and self-overcoming pressure is framed strongly enough or still too weakly / negatively

## Anti-Misread Rules

- [g:r:i] This register does not mean “the current harness has no long-horizon carry.”
- [g:r:i] It does not mean “future awareness must be embedded everywhere equally.”
- [g:r:i] It does not reduce harness improvement to deficiency-removal, healing, or movement toward mere adequacy.
- [g:r:i] It means the harness currently carries long-horizon thinking most strongly at discuss/plan entry and less strongly at later lifecycle and self-improvement surfaces.

## Current Consequence

- [g:r:i] The next strong move is not necessarily to patch all of these surfaces at once.
- [d:r:i] The immediate value of this artifact is:
  - preserve the gap reading durably
  - give future local or cross-vendor audit a real object to iterate on
  - and keep long-horizon carry from being treated as “already solved because `future_awareness` exists”
