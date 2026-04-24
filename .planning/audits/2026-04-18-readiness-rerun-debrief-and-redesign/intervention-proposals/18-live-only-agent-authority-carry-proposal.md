Date: 2026-04-20
Status: bounded next-tranche proposal

# Live-Only Agent Authority / Carry Proposal

## Purpose

- [g:r:i] This note turns the remaining `16` live-only agent contracts into a bounded next-tranche proposal so the workspace stops treating them as one undifferentiated future problem.

## Starting Ground

- [e:c+i] The strict coherence pass found no selected-scope manifest/install blocker and narrowed the remaining pressure to the same `16` untracked live-only agent contracts. Sources: [17-manifest-install-coherence-pass.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/17-manifest-install-coherence-pass.md:1), [02-manifest-install-coherence-report.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/artifacts/02-manifest-install-coherence-report.json:1).
- [e:c+i] The cohort matrix and targeted reread also already ruled out a broad cleanup interpretation. Most of the cohort is active routed carry, `gsd-debug-session-manager` is active skill-routed carry, and `gsd-pattern-mapper` is planner-adjacent authority-gap carry. Sources: [12-live-only-agent-cohort-matrix.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/12-live-only-agent-cohort-matrix.md:1), [13-live-only-agent-targeted-reread-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/13-live-only-agent-targeted-reread-disposition.md:1).

## Proposed Split

### 1. Preserve as intentional live-only carry for now

- [d:r:i] Keep the following live-only for now, with no immediate overlay-carry patch:
  - `gsd-advisor-researcher`
  - `gsd-assumptions-analyzer`
  - `gsd-debug-session-manager`
  - `gsd-ai-researcher`
  - `gsd-domain-researcher`
  - `gsd-eval-auditor`
  - `gsd-eval-planner`
  - `gsd-framework-selector`
  - `gsd-doc-classifier`
  - `gsd-doc-synthesizer`
  - `gsd-security-auditor`
  - `gsd-user-profiler`
- [d:r:i] Reason:
  - these surfaces are active enough to reject cleanup
  - but they are not the highest current repo-local leverage for doctrine-sensitive planning/audit carry
  - widening tracked overlay carry across all of them now would be more breadth than yield

### 2. Put the next overlay-carry review tranche on a narrower high-leverage cluster

- [d:r:i] Elevate these to the next bounded authority/carry review tranche:
  - `gsd-code-reviewer`
  - `gsd-code-fixer`
  - `gsd-intel-updater`
  - `gsd-pattern-mapper`
- [d:r:i] Reason:
  - `gsd-code-reviewer` and `gsd-code-fixer` directly shape repo-local review/remediation quality, which is already a doctrine-sensitive surface here
  - `gsd-intel-updater` writes `.planning/intel/` outputs that later agents and workflows can rely on instead of rereading code, so drift or weak carry there propagates
  - `gsd-pattern-mapper` remains the clearest authority-gap case inside the cohort and is planner-adjacent rather than peripheral

### 3. Treat this as a review tranche, not an automatic patch

- [d:r:i] This proposal does **not** yet authorize copying all four `.toml` files into tracked overlay canon.
- [d:r:i] It authorizes a bounded next review on those four surfaces to decide:
  - whether repo-local overlay carry is actually needed
  - whether live-only status is still the stronger boundary
  - whether any routing/authority clarification should happen before carry expansion

## What This Rejects

- [d:r:i] Reject repo-wide overlay widening across all `16` live-only agents.
- [d:r:i] Reject returning to manifest/install semantics as the master question.
- [d:r:i] Reject another broad stale-agent cleanup story.

## Immediate Next Move

- [g:r:i] Run a bounded authority/carry review on `gsd-code-reviewer`, `gsd-code-fixer`, `gsd-intel-updater`, and `gsd-pattern-mapper` before any further overlay-carry expansion.
