Date: 2026-04-22
Status: active mapping note

# Harness Parallelization Opportunity Map

## Role

- [d:r:i] This note maps two different parallelization fields that should not be collapsed:
  - parallelization inside the modified harness in action
  - parallelization inside harness-modifier development and uplift work
- [d:r:i] Its job is to keep `parallelization` from meaning only execution-wave splitting inside one phase or only overlap inside the harness-improvement program.

## Why This Note Exists

- [d:r:i] Time pressure is real.
- [d:r:i] The answer is not sloppy acceleration.
- [d:r:i] The answer is better-designed overlap, better task partitioning, and clearer rules about what can travel in parallel without degrading software quality, continuity, or judgment.
- [d:r:i] This note is not a completed diagnosis of vanilla GSD or of the modified harness.
- [d:r:i] It is a framing map plus a prompt for a stronger field-mapping pass.

## Existing Baselines

### Domain Split

- [d:r:i] `Harness in action`
  - means the modified harness as it operates on real project work:
    - discuss
    - research
    - plan
    - execute
    - verify
    - lateral supporting workflows
- [d:r:i] `Harness-improvement program`
  - means the work of developing, auditing, extracting, propagating, and governing the harness modifier itself
- [d:r:i] These two domains can inform each other, but they are not the same parallelization question and should not be routed through one flattened judgment.
- [d:r:i] The examples below are provisional current references, not exhaustive or sovereign claims about the total parallelization posture of vanilla GSD or the modified harness.

### Harness In Action

- [d:r:i] One visible current example is execution-wave splitting inside phase execution.
- [d:r:i] There may be other real or latent parallelization carriers in vanilla GSD and in the modified harness, but this note does not yet claim to have mapped them fully.

### Harness-Improvement Program

- [d:r:i] This workspace already carries one explicit overlap doctrine:
  - [../AUDIT-LANE-PATTERN-LIBRARY.md](../governance/AUDIT-LANE-PATTERN-LIBRARY.md) `Bounded Parallelization And Overlap`
- [d:r:i] That doctrine currently governs:
  - what can happen while external lanes run
  - what must wait for inheritance
  - what admin/governance work can safely travel alongside long-running reviews

## Opportunity Classes

### 1. Phase-Internal Execution Parallelization

- [d:r:i] Current baseline:
  - wave-based execution after planning has already assigned disjoint work
- [d:r:i] This remains the cleanest existing parallelization form because the plan itself encodes the partition.

### 2. Pre-Execution Research / Mapping Parallelization

- [d:r:i] Opportunity:
  - split bounded terrain questions
  - split codebase mapping across disjoint subsystems
  - split comparative research questions
- [d:r:i] Earned when:
  - the top-level framing is already coherent
  - the sub-questions are genuinely separable
  - the parent thread retains synthesis ownership

### 3. Verification-Family Parallelization

- [d:r:i] Opportunity:
  - code review
  - security review
  - validation gap checks
  - propagation review
  - docs verification
- [d:r:i] Earned when:
  - implementation is frozen enough for bounded review
  - each review has a clear subject and output carrier

### 4. Cross-Phase Parallelization

- [d:r:i] Opportunity exists, but only in a narrower form than `execute multiple phases at once`.
- [d:r:i] Responsible forms include:
  - preparatory research for a later phase on a frozen upstream basis
  - bounded spec or mapping work for a later phase when dependencies are already explicit
  - adjacent documentation / verification / telemetry work for an earlier completed phase while a new phase is in planning
- [d:r:i] Unsafe forms include:
  - executing a later phase whose requirements depend on an unsettled earlier phase
  - letting later-phase exploratory work harden into canon before the earlier phase settles the boundary

### 5. Lateral Workflow Parallelization

- [d:r:i] Opportunity:
  - lifecycle / propagation refresh work
  - review-route work
  - deployability preparation
  - telemetry / discrepancy carrier work
  - governance/admin updates
- [d:r:i] This matters because the harness is not only `discuss -> research -> plan -> execute -> verify`.
- [d:r:i] It also contains lateral workflows whose work can sometimes travel in parallel with the main line if their basis is frozen and their outputs stay bounded.

### 6. Harness-Improvement Program Overlap

- [d:r:i] Opportunity:
  - while an Opus lane reads a frozen basis, do unrelated governance carry, propagation refreshes, or bounded implementation on another already-settled family
  - use bounded sub-agents for classification, packet assembly, or narrower gap-identification while the parent thread retains composition ownership
- [d:r:i] This is already partly governed, but not yet mapped as one broader opportunity field.

## Domain Rule

- [d:r:i] If the question is `can the harness itself do more work in parallel when operating on a host project?`, route it through the `Harness In Action` classes above.
- [d:r:i] If the question is `can the harness-improvement program move faster or more cleanly by overlapping audits, implementation, governance carry, or delegated sub-work?`, route it through `Harness-Improvement Program Overlap`.
- [d:r:i] If a later note says only `parallelization` without naming which domain it means, sharpen the domain explicitly before using the note to justify design changes.

## Representation Rule

- [d:r:i] A parallelization map is more useful here than one scalar `parallelize more` doctrine.
- [d:r:i] The useful representation is:
  - opportunity class
  - prerequisite stability
  - ownership boundary
  - expected gains
  - likely risks
  - what carrier should preserve the result

## Anti-Patterns

- [d:r:i] launching parallel work before the governing boundary is coherent
- [d:r:i] treating `it could run in parallel` as if it should
- [d:r:i] letting delegated work collapse back into the parent thread without explicit disposition
- [d:r:i] using parallelization to hide admin/governance debt rather than carrying it
- [d:r:i] letting later-phase work become de facto canon before earlier-phase decisions settle

## Near Consequence

- [d:r:i] The next stronger move is not yet to rewrite multiple live workflows for parallelization.
- [d:r:i] The next stronger move is to run a proper field-mapping / diagnosis pass rather than treating the examples here as if they were already a full posture map.
- [d:r:i] That diagnosis should ask separately:
  - inside vanilla GSD, where parallelization is already explicit, implicit, absent, or artificially constrained
  - inside the modified harness, where new parallelization opportunities, frictions, or regressions have been introduced
  - inside the harness-improvement program, which overlap/delegation forms are already governed and which still rely too heavily on operator memory
- [d:r:i] Only after that diagnosis should later workflow rewrites, agent/protocol changes, or stronger operator-surface changes be judged.
