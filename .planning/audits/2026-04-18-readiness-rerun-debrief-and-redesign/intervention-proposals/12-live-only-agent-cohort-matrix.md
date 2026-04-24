Date: 2026-04-20
Status: first routing matrix

# Live-Only Agent Cohort Matrix

## Purpose

- [g:r:i] This note performs the first move accepted in [11-second-tranche-sequencing-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/11-second-tranche-sequencing-disposition.md:1): type the remaining `16` live-only agent surfaces so cleanup, snapshots, and later coherence work stop sharing one undifferentiated target.

## Starting Constraint

- [e:c+i] The sharpened runtime-visibility report shows that the remaining `untracked_live_only_outside_overlay_subset` cohort is entirely `agent_toml`, not a mixed family set. Sources: [01-runtime-visibility-report.json](../tranche-audit/artifacts/01-runtime-visibility-report.json:15), [01-runtime-visibility-report.json](../tranche-audit/artifacts/01-runtime-visibility-report.json:20), [01-runtime-visibility-report.json](../tranche-audit/artifacts/01-runtime-visibility-report.json:23).

## Matrix

### 1. Active routed live-only carry

- [d:r:i] These should not be treated as immediate cleanup candidates. They are currently active enough in the harness that their live-only status is first a runtime-authority / overlay-boundary question, not a residue conclusion.

| Agent | Current signal | Provisional reading |
| --- | --- | --- |
| `gsd-advisor-researcher` | overlay config entry + `discuss-phase` spawn path + agent-contracts entry | active routed live-only carry |
| `gsd-assumptions-analyzer` | overlay config entry + `discuss-phase-assumptions` spawn path + agent-contracts entry | active routed live-only carry |
| `gsd-code-fixer` | overlay config entry + `code-review-fix` workflow spawn path | active routed live-only carry |
| `gsd-code-reviewer` | overlay config entry + `quick` and `code-review-fix` workflow usage | active routed live-only carry |
| `gsd-intel-updater` | overlay config entry + `bin/lib/intel.cjs` / agent-contracts pressure | active routed live-only carry |
| `gsd-security-auditor` | overlay config entry + `secure-phase` workflow usage | active routed live-only carry |
| `gsd-user-profiler` | overlay config entry + `profile-user` workflow / `user-profiling.md` reference pressure | active routed live-only carry |
| `gsd-ai-researcher` | `ai-integration-phase` workflow usage + `AI-SPEC.md` / `ai-frameworks.md` reference pressure | active routed live-only carry |
| `gsd-domain-researcher` | `ai-integration-phase` workflow usage + `AI-SPEC.md` grounding | active routed live-only carry |
| `gsd-eval-auditor` | `eval-review` workflow usage + `ai-evals.md` / `AI-SPEC.md` pressure | active routed live-only carry |
| `gsd-eval-planner` | `ai-integration-phase` workflow usage + `ai-evals.md` pressure | active routed live-only carry |
| `gsd-framework-selector` | `ai-integration-phase` workflow usage + `ai-frameworks.md` pressure | active routed live-only carry |
| `gsd-doc-classifier` | `ingest-docs` workflow spawn path | active routed live-only carry |
| `gsd-doc-synthesizer` | `ingest-docs` workflow spawn path | active routed live-only carry |

### 2. Weakly routed / authority-gap carry

- [d:r:i] These are not strong deletion candidates yet, but they are weaker than the cohort above. The next move for them is a targeted routing/authority reread, not automatic preservation and not immediate retirement.

| Agent | Current signal | Provisional reading |
| --- | --- | --- |
| `gsd-pattern-mapper` | on-disk agent file + model-profile entry + `PATTERNS.md` artifact pressure in `init.cjs`, but no clear current workflow spawn path in local `get-shit-done/` | weakly routed live-only carry; candidate for authority/routing clarification |

### 3. Strong orphan-suspicion carry

- [d:r:i] This is the first cleaner cleanup candidate surfaced by the matrix. It still needs a targeted reread before any retirement, but it no longer deserves to hide inside the same bucket as obviously active surfaces.

| Agent | Current signal | Provisional reading |
| --- | --- | --- |
| `gsd-debug-session-manager` | on-disk agent file only in current local harness read-set; no current `get-shit-done/` workflow/reference/bin-lib hit surfaced in this pass | strong orphan-suspicion carry; first targeted cleanup/routing reread candidate |

## Evidence Anchors

- [e:c+i] `gsd-advisor-researcher` is clearly active in the current local harness: it has a live `discuss-phase` spawn path and an `agent-contracts` entry. Sources: [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:527), [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:636), [tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:32), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:20).
- [e:c+i] `gsd-assumptions-analyzer` is clearly active in the current local harness: `discuss-phase-assumptions` names and spawns it, and `agent-contracts` records its role. Sources: [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md:11), [tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md:235), [tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:29), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:24).
- [e:c+i] `gsd-code-fixer` and `gsd-code-reviewer` both have direct current workflow routing in the local harness. Sources: [.codex/get-shit-done/workflows/code-review-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review-fix.md:2), [.codex/get-shit-done/workflows/code-review-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review-fix.md:181), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:26), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:705), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:28), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:32).
- [e:c+i] `gsd-security-auditor` and `gsd-user-profiler` both have current local workflow/reference routing, not just on-disk presence. Sources: [.codex/get-shit-done/workflows/secure-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/secure-phase.md:11), [.codex/get-shit-done/workflows/secure-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/secure-phase.md:83), [.codex/get-shit-done/workflows/profile-user.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/profile-user.md:4), [.codex/get-shit-done/workflows/profile-user.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/profile-user.md:162), [.codex/get-shit-done/references/user-profiling.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/user-profiling.md:3), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:92).
- [e:c+i] The AI-integration cluster is also clearly active in current local workflow logic rather than ambient residue. Sources: [.codex/get-shit-done/workflows/ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:2), [.codex/get-shit-done/workflows/ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:92), [.codex/get-shit-done/workflows/ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:140), [.codex/get-shit-done/workflows/ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:170), [.codex/get-shit-done/workflows/ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:200), [.codex/get-shit-done/workflows/eval-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/eval-review.md:72), [.codex/get-shit-done/workflows/ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:160), [.codex/get-shit-done/workflows/ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ingest-docs.md:175).
- [e:c+i] `gsd-pattern-mapper` and `gsd-debug-session-manager` are materially weaker than the active cohort in current local routing evidence. `gsd-pattern-mapper` still has some artifact/model-profile pressure, while `gsd-debug-session-manager` currently shows on-disk presence without a matching local workflow/reference/bin-lib hit in this pass. Sources: [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:289), [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:318), [.codex/get-shit-done/bin/lib/model-profiles.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/model-profiles.cjs:22), [.codex/agents/gsd-pattern-mapper.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-pattern-mapper.toml:1), [.codex/agents/gsd-debug-session-manager.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-debug-session-manager.toml:1).

## Consequences

- [d:r:i] No repo-wide stale-agent cleanup is warranted yet.
- [d:r:i] A narrower cleanup/routing reread is now warranted for:
  - `gsd-debug-session-manager` first
  - `gsd-pattern-mapper` second
- [d:r:i] Durable snapshot discipline should follow this narrower reread rather than come first, because the matrix has already shown that most of the `16` are active carry rather than clutter.

## Immediate Next Move

- [g:r:i] Run a bounded targeted reread on `gsd-debug-session-manager` and then `gsd-pattern-mapper` to decide whether each is:
  - intentionally live-only carry,
  - candidate for tracked overlay canon,
  - or a real retirement / cleanup target.
