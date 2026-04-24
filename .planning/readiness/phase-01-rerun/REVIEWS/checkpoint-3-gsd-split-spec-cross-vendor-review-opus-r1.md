# Checkpoint 3 GSD Split Spec Cross-Vendor Review (Opus R1)

Reviewer: Claude Opus 4.6 (cross-vendor)  
Date: 2026-04-15  
Scope: Adequacy review of the Checkpoint 3 GSD split-spec bundle before deeper GSD mapping lanes launch

## Verdict

**Launch-ready.** The bundle is strong enough to launch the deeper GSD mapping lanes without creating later audit confusion or scope distortion.

Three recommended improvements are worth considering before launch but do not block it.

## Reviewed Artifacts

Target specs:

1. `AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts-spec.md`
2. `AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts-spec.md`
3. `AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth-spec.md`
4. `AUDITS/checkpoint-3-gsd-scope-synthesis-spec.md`
5. `AUDITS/checkpoint-3-scope-synthesis-spec.md`

Governing context:

- `AGENTS.md`, `.planning/AGENTS.md`
- `PLAN.md`, `STATUS.md`, `TASKS.md`
- `GATES/checkpoint-3.md`
- `AUDITS/checkpoint-3-workflow-harness-scope-launch-spec.md`
- `AUDITS/checkpoint-3-gsd-surface-map.md`

## Findings

### F1: Synthesis specs omit governing input references to agent instruction docs (low severity)

The three sublane specs all include `AGENTS.md` and `.planning/AGENTS.md` in their Governing Inputs sections (workflow-chain spec:32-33, agent-doctrine spec:32-33, runtime-config spec:32-33). This ensures sublane agents will read and honor the claim-typing discipline, research quality rules, and general conduct rules those docs carry.

Both synthesis specs omit these. The GSD scope synthesis spec lists only mapping artifacts, the gate, and readiness-package state docs as inputs (gsd-scope-synthesis-spec:34-43). The overall scope synthesis spec similarly omits them (scope-synthesis-spec:17-23).

The practical risk is low because synthesis agents will be reading sublane outputs that were themselves written under those governing instructions, so the discipline should propagate through the input artifacts. But making it explicit would prevent a synthesis agent from unknowingly relaxing claim-typing or source-basis standards.

**Recommendation:** Add a brief note to both synthesis specs—either as a "Governing Inputs" section or a line in the existing sections—noting that `.planning/AGENTS.md` claim-typing and research-quality discipline still applies even though the synthesis is reading derived artifacts rather than raw harness files.

### F2: `templates/config.json` appears as a minimum inspection target in both sublane A and sublane C (low severity)

The workflow-chain spec lists `.codex/get-shit-done/templates/config.json` as a minimum inspection target (workflow-chain spec:51). The runtime-config spec also lists it (runtime-config spec:48).

This is not inherently wrong—the two lanes have legitimately different angles on the same file. Sublane A cares about the config template as part of the artifact contract chain (what the template tells the planning workflow to expect). Sublane C cares about it as the stock baseline against which the repo-local `config.json` overlay is compared.

The risk is that both lanes produce independent observations about the same file without knowing the other lane's analysis, and the synthesis then has to reconcile without knowing which observations were intended as definitive versus incidental.

**Recommendation:** Add a one-line note to each spec clarifying the angle. For sublane A: "inspect `templates/config.json` for its artifact-contract role in the workflow chain, not for runtime/overlay truth." For sublane C: "inspect `templates/config.json` as the stock baseline for overlay comparison; workflow-chain implications are sublane A's concern."

### F3: Overall scope synthesis spec lacks a "cite concrete files and lines" constraint (low severity)

The three sublane specs all carry an explicit constraint: "cite concrete files and lines" (workflow-chain spec:91, agent-doctrine spec:91, runtime-config spec:91). The GSD scope synthesis spec has a "Decision Discipline" section but no equivalent citation constraint (gsd-scope-synthesis-spec:69-73). The overall scope synthesis spec similarly has "Decision Discipline" without a citation requirement (scope-synthesis-spec:44-48).

The synthesis lanes' citation discipline is inherently different—they should be citing their input mapping artifacts rather than re-citing original source files. But without any explicit citation expectation, synthesis agents might produce summary-level prose that later readers cannot trace back to specific mapping claims.

**Recommendation:** Add a constraint to both synthesis specs along the lines of "cite input mapping artifacts and specific sections when making scope claims; do not produce summary claims that a later reader cannot trace to a specific mapping finding."

### F4: "Implications For The Later Excellence Audit" section creates a mild excellence-drift vector (informational)

Each sublane spec's required output sections include "Implications For The Later Excellence Audit" (workflow-chain spec:81, agent-doctrine spec:81, runtime-config spec:81). This is the right framing—it asks where the later audit should concentrate, not what it will find. The core questions in each spec reinforce the mapping frame ("where does X actually live?" rather than "is X good enough?").

However, agents with strong quality-oriented tendencies could use this section to smuggle in premature excellence claims disguised as scope concentration recommendations (e.g., "this area doesn't need deep audit because it's already fine" is actually a premature excellence claim wearing a scoping hat).

The explicit constraints ("do not judge whether the chain is excellent yet," "do not smuggle in later Checkpoint 4 conclusions under the guise of mapping") provide adequate guardrails against this. The synthesis agent can catch and flag any such drift.

**No action required.** This is an informational finding about a residual risk that the existing constraints already mitigate.

## What Is Already Strong

**Motivating grounds are well-anchored.** Every spec traces its existence through a concrete chain: GSD surface map recommends split (gsd-surface-map:86-95) → launch spec accepts the split outcome (launch-spec:73-89) → gate tracks exit criteria (checkpoint-3.md:36) → each sublane spec cites the specific readiness-package files that justify it. No spec relies on ambient session memory for its motivation.

**The Checkpoint 3 / Checkpoint 4 boundary is clean and explicit.** All three sublane specs open with "This is still mapping work, not the later excellence audit" (workflow-chain spec:7, agent-doctrine spec:7, runtime-config spec:7). The constraints sections reinforce this with "do not smuggle in later Checkpoint 4 conclusions under the guise of mapping." The synthesis specs preserve this with "preserve the distinction between mapped scope and later excellence judgment" (gsd-scope-synthesis-spec:72).

**The staging order is correct and enforced by explicit preconditions.** The GSD scope synthesis spec requires all four GSD mapping artifacts to exist before it runs (gsd-scope-synthesis-spec:26-31). The overall scope synthesis spec requires the Codex map, initial GSD map, and (if split triggered) the deeper sublane outputs and GSD-only synthesis (scope-synthesis-spec:9-14). This prevents premature synthesis.

**The three-way split faithfully preserves the GSD surface map's earned distinctions.** The sublane specs map exactly to the three units recommended at gsd-surface-map:88-94. No unit was dropped, merged, or silently restructured.

**Each sublane has specific, non-generic core questions.** The questions are tailored to the lane's scope rather than being boilerplate. The workflow-chain spec asks about preserve-only seams and gate seams (workflow-chain spec:58). The agent-doctrine spec asks about reversal-sensitive seams and drift between role contracts and repo governance (agent-doctrine spec:57-58). The runtime-config spec asks about declared-vs-actual behavior and misleading surfaces (runtime-config spec:57-58).

**The required output sections are well-designed for downstream consumption.** Both synthesis specs list their required inputs, and the sublane output sections map directly to what the synthesis agents need. The overall scope synthesis even includes "How Checkpoint 3 resolved the GSD split" (scope-synthesis-spec:41), which creates an explicit audit trail for the split itself.

**The overlap between sublane B and sublane C on `.codex/agents/*.md` files is well-handled.** Sublane B inspects the doctrine content of agent files (agent-doctrine spec:44). Sublane C inspects the resolution mechanism and `.md`-vs-`.toml` drift (runtime-config spec:49-50). These are different angles on the same files, and the distinction is clear enough to avoid confusion.

**Package state is coherent with the spec bundle.** STATUS.md shows "deeper GSD mapping sublanes and GSD-only synthesis inside Checkpoint 3" as not started, with immediate next action to "checkpoint the refined Checkpoint 3 spec bundle, then launch." TASKS.md shows R3.3, R3.4, R3.5 as not started with correct output file paths. GATES/checkpoint-3.md exit criteria match the spec bundle's structure. No contradictions.

**The constraint "prefer readiness-package artifacts as authority"** appears in all three sublane specs and the GSD scope synthesis spec (workflow-chain spec:89, agent-doctrine spec:90, runtime-config spec:89, gsd-scope-synthesis-spec:73). This prevents agents from treating ephemeral thread corrections as authoritative over the checkpointed package state.

## What Must Change Before Launch

Nothing. The bundle is launch-ready as-is.

## What Can Wait Until Later

1. **F1–F3** are all low-severity improvements. They would strengthen the specs and are worth applying before launch if convenient, but omitting them will not create audit confusion or scope distortion. The natural discipline of the sublane outputs and the synthesis agent's job description cover the gaps well enough.

2. **F4** requires no action; it is an informational finding about a residual risk that is already mitigated by existing constraints.

3. If any sublane agent discovers that its scope needs adjustment (e.g., a file it was told to inspect is actually irrelevant, or a file not listed turns out to be load-bearing), the spec structure already supports this through the "Open Inquiry Debt" output section in each sublane and the "Reversal-Sensitive Boundaries" section in the synthesis specs.
