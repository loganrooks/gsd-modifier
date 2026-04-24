# Threshold Scanner Side-Effects Internal Audit

Date: 2026-04-21
Status: active internal audit note

## Purpose

- [g:r:i] This note audits the side effects created by `scan_threshold_language.py` and by scanner-led cleanup decisions, so heuristic widening does not quietly become wording control or doctrine drift.
- [d:r:i] The trigger was direct user challenge during the compatibility-anchor batch: the scanner had started pressuring clear anti-threshold prohibitions into weaker euphemism, which is the reverse of the intended effect.

## Scope

- [e:c+i] This audit rereads the scanner-introduction and scanner-hardening commits:
  - `2834fd3` `docs(tooling): tighten anti-threshold enforcement`
  - `8340127` `docs(doctrine): harden anti-threshold language guardrails`
  - `f29ea75` `docs(doctrine): keep threshold scanner non-authoritative`
- [e:c+i] It also rereads the current uncommitted compatibility-anchor batch where the scanner most clearly pushed a bad rewrite in [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md).

## What The Scanner Helped With

- [d:c+i] The scanner did widen attention toward real residue clusters in older specs, prompts, and review artifacts. That widening pressure helped motivate the threshold-audit subtree and later doctrine hardening.
- [d:c+i] The scanner also helped surface two distinct residue families that were easy to miss by memory alone:
  - deficit-oriented pseudo-positive phrasing
  - static-positive evaluative phrasing that can smuggle back minimum-bar logic

## Where It Started To Harm The Work

- [e:r:i] The clearest failure mode is heuristic overreach in meta-prohibition contexts. A line that explicitly names forbidden wording so a future reviewer will avoid it was treated as if it were itself contamination.
- [e:r:i] In the current uncommitted batch, this caused a direct regression attempt: a clear prohibition line in `../../pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md` was being laundered into weaker euphemistic wording purely to quiet the scanner.
- [d:r:i] That is not a benign false positive. It inverts the intended hierarchy:
  - the scanner should widen reread
  - contextual judgment should classify the hit
  - direct anti-pattern naming should remain allowed when the file is explicitly teaching what to avoid

## Audit Judgment

- [d:r:i] No broader rollback is earned for the whole scanner family.
- [d:r:i] A narrower correction is earned:
  - keep the scanner as an optional widening aid for explicit framing-residue audits
  - stop treating it as a routine completion gate
  - forbid scanner-driven rewrites that weaken explicit prohibitions, quoted examples, or historical evidence without a contextual argument
- [d:r:i] The strongest current harm appears concentrated in wording-control pressure, not in core runtime or propagation logic.

## Concrete Dispositions

1. [d:r:i] Restore direct explicit anti-pattern naming where the file is itself a doctrine or prompt-governance surface.
2. [d:r:i] Treat scanner findings as items for classification, not as automatic edit prompts.
3. [d:r:i] When a hit is in a doctrine or instruction file, classify it first:
   - `meta prohibition, keep explicit`
   - `quoted historical evidence, keep with note`
   - `actual residue, revise`
   - `unclear, reread wider context`
4. [d:r:i] Do not run the scanner as a routine “clean batch” gate on ordinary work. Use it when the task is explicitly a framing-residue audit or when a doctrine-sensitive reread already warrants it.
5. [d:r:i] Keep contextual reread sovereign over heuristic output, even when the scanner appears numerically clean.

## Immediate Follow-Through

- [d:r:i] The current batch restores the explicit prohibition wording in `../../pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md`.
- [d:r:i] `.planning/AGENTS.md` and `tooling/codex/README.md` should now be tightened so scanner use is explicitly optional, audit-specific, and subordinate to contextual review.

## Bottom Line

- [g:r:i] The scanner can remain in the repo only as a narrow widening aid. The moment it starts steering prose by itself, it degrades the doctrine it was meant to protect.
