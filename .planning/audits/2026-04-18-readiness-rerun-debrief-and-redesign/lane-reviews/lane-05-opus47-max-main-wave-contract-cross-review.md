# Lane-05 Opus 4.7 1M Main-Wave Contract Cross-Review

Status: challenge input, not sovereign doctrine
Date: 2026-04-19
Reviewer: Claude Opus 4.7 via `opus[1m]` Claude Code CLI
Governing spec: [OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md](../review-specs/OPUS-MAIN-WAVE-CONTRACT-CROSS-REVIEW-SPEC.md)

## Overall Judgment

- [d:r:i] The drafted [MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md](../main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md) is architecturally sound on its own terms. Its wave split, lane family set, packet discipline, shared output registers, and anti-failure rules all carry real work and map cleanly to the charter and question set. The contract does not fail the Required Posture test that would earn a reopened `should there be a main wave at all?` meta lane.
- [d:c+i] However, two bounded pre-Wave-1 tightenings are warranted before Wave 1 spec-writing begins. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:66-110, WORKFLOW.md:55-67, WORKFLOW.md:69-83.
  1. Concrete per-lane packet manifests (concrete file paths, not only evidence-family references) must be resolved before each Wave 1 lane spec is written, not deferred into the launch-prompt-writing step.
  2. The audit workspace must be committed to git before Wave 1 launches, with a bounded per-lane packet-freeze commit discipline adopted alongside.
- [d:r:i] Workspace organization is currently good enough to carry Wave 1 spec-writing without silent drift. The flat topology is at the edge of its usable range, but the Surface-A authority / force register plus naming conventions plus the read-order `INDEX.md` are doing real work and do not need restructuring now. Per-lane subdirectories are later-facing cleanup, not a blocker.
- [d:c+i] Version-control / change-management practice is the one surface where a real, concrete, bounded tightening is earned pre-Wave-1. The audit directory is entirely untracked in git, which violates existing [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md) doctrine for doctrine-sensitive delegated work. Sources: WORKFLOW.md:55-67, WORKFLOW.md:69-83, git ls-files /home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/ returns `(empty)`.

## Contract Strengths

- [e:c+i] Wave-structured rather than one mega-lane. Wave 1 parallel analytic, Wave 2 opportunity + rerun-shape, Wave 3 synthesis. Directly addresses the Proposal-A failure mode the setup already rejected. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:27-62, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/PLAN-PROPOSALS.md:28-33.
- [e:c+i] Lane set maps cleanly to the question set. Each Wave-1 lane has a primary question and a primary-output deliverable, and each matches a question-set cluster without double-counting. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:29-44, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/QUESTION-SET.md:3-79.
- [e:c+i] The `operator-orchestration-pressure` lane is carried as a first-class parallel lane rather than a subordinate footnote. That correctly refuses to let "mapping failure" become the easy universal explanation. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:42-44, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/EVIDENCE-ARCHITECTURE.md:136-138.
- [e:c+i] Anti-failure rules directly name the failure modes the setup has already earned the right to name: raw-corpus dumping, forgetting the bridge audit, under-reading runtime, single-lane sovereignty by rhetoric, and asymmetric packeting for `no-change` lanes. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:124-130.
- [e:c+i] Shared output registers let Wave-3 synthesis compare structurally comparable artifacts without flattening lane differences. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:111-123.
- [e:c+i] The contract keeps "non-intervention is not a neutral default" and "intervention is not a neutral default either" symmetric, which carries the charter's anti-regret rule forward without quietly tipping toward either side. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:18-22, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-CHARTER.md:12-16.
- [e:c+i] Cross-review rule already anticipates a bounded contract-level critique rather than a free-floating meta relaunch, which lets this very lane be scoped narrowly without needing a contract amendment first. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:132-134.

## Contract Weaknesses

- [e:c+i] Core packet omits [INDEX.md](../INDEX.md) even though `INDEX.md` is the read-order document and source-of-truth hierarchy register. Wave-1 lanes that only receive the spine without `INDEX.md` may miss the explicit authority hierarchy that the spine depends on. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:66-74, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md:35-55.
- [e:c+i] Lane-specific packet additions reference evidence families ("heavy on Family A", "selected Family E") rather than concrete file paths. This defers packet resolution into the launch-prompt writing step, where drift is easiest to introduce silently. The evidence-family abstraction is useful for design; it is not sufficient as the frozen packet. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:76-109, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/EVIDENCE-ARCHITECTURE.md:26-98.
- [e:c+i] No explicit per-lane token band. [EVIDENCE-ARCHITECTURE.md](../governance/EVIDENCE-ARCHITECTURE.md) names `60k-140k` for substantive lanes and `20k-40k` for sharp stress tests. The contract does not carry that discipline forward, so each Wave-1 spec-writer would re-derive it. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/EVIDENCE-ARCHITECTURE.md:101-107.
- [o:r:i] Wave-1 lane dependency structure is treated as flat-parallel, but `outcome-and-underreach-audit` logically rests on a provisional mission statement that `mission-reconstruction` is the lane designed to produce. The contract does not say whether Wave-1 lanes may restate mission provisionally or whether `mission-reconstruction` runs a short precursor step before the other three launch. This is a minor structural ambiguity rather than a hard blocker.
- [e:c+i] No explicit rule about what to do if a Wave-1 lane returns weak, fails, or complains of packet drift mid-lane. The existing launch-ledger pattern records probe summaries post-hoc but does not prescribe a reroll, packet-revision, or escalation protocol. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md:1-103.
- [e:r:i] The Wave-3 synthesis rule says "prior lane outputs rather than the whole raw corpus by default", but does not name the countermeasure for the contract's own `false convergence` failure mode. Synthesis may need to spot-check Wave-1 packet framing where all four lanes agreed, to separate genuine convergence from spec-framing leakage. That countermeasure is the strongest natural defense against the false-convergence rule the contract already names as a failure mode.
- [e:r:i] `interventions considered and rejected ledger` is listed as a shared output register, and the question set sets a generative quota of at least three rejected interventions per serious lane. The contract does not restate that quota; a lane spec writer who reads only the contract will not see the `3` minimum. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/QUESTION-SET.md:102-110.

## Missing Pre-Wave-1 Concerns

- [e:c+i] Concrete per-lane packet manifest. Before each Wave-1 lane spec is written, the contract or a companion file should enumerate the actual files (with line ranges where applicable) that each lane reads. This is the packet-freeze step. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/EVIDENCE-ARCHITECTURE.md:26-98, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:76-109.
- [e:c+i] Git baseline for the audit workspace. The entire `2026-04-18-readiness-rerun-debrief-and-redesign/` directory is currently untracked. No lane has been launched against a committed packet state. Wave 1 would repeat that pattern at four-lane scale unless a baseline commit happens first. Sources: git status (reports `?? .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/` at review time), WORKFLOW.md:55-67.
- [e:r:i] Per-lane packet-freeze + launch-truth commit discipline. Each Wave-1 lane's launch prompt, packet manifest, and capture_launch_truth output should be committed before/with launch, and the LAUNCH-LEDGER entry should record the workspace commit SHA the packet was frozen against. Sources: WORKFLOW.md:69-83.
- [e:r:i] Explicit rule for weak-return / packet-drift handling. A lane that returns weak, returns incoherently, or complains mid-lane of packet drift should have a named disposition path (reroll with revised packet, accept narrowly as partial evidence, escalate to Wave 2 reshape) rather than an ad hoc decision.
- [o:r:i] Explicit Wave-1 parallelism rule. State whether the four Wave-1 lanes may restate mission provisionally and run truly parallel, or whether `mission-reconstruction` runs a short precursor pass and its theory-of-change summary seeds the other three lanes.
- [e:r:i] Per-lane token budget band. Restate or explicitly point to the `60k-140k` sizing band from the evidence architecture, so no lane silently balloons or starves.
- [e:r:i] Restate the generative anti-tame quota (`at least 3 rejected interventions per lane`) inside the contract so lane spec writers who do not reread the question set still see it.

## Workspace Organization / Artifact Topology

- [e:c+i] The audit directory currently holds `93` files in a flat structure at inspection time. That splits into roughly: `37` commentary corpus chunks, `19` lane-prefixed artifacts, `5` `OPUS-*-SPEC.md` files, plus governing-spine, procedural-scaffolding, and derivative files. The authority note's 5-class taxonomy plus `INDEX.md` read order plus `lane-NN-<model>-<purpose>` and `OPUS-<PURPOSE>-SPEC.md` naming conventions are currently doing real routing work. Sources: `ls .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/` output, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:38-157, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md:5-55.
- [p:r:i] Wave 1 will plausibly add roughly `20-28` new artifacts (4 specs + 4 launch prompts + 4 outputs + 4 dispositions + 4 rereads + 4 launch-truth captures). Wave 2 adds roughly `10-14` more. The flat directory would likely reach `~125-140` files before synthesis.
- [d:r:i] That is past the point where the flat topology is optimal but not past the point where it fails. Two factors keep it viable:
  - the naming conventions cluster lane families lexicographically (`lane-05-*`, `lane-06-*`, `lane-07-*`)
  - the Surface-A authority / force register tells readers which files govern regardless of filesystem depth
- [d:r:i] Bounded topology cleanup is tempting but not earned pre-Wave-1. Pre-Wave-1 restructuring would itself introduce drift risk (link rot, authority-note rewrite pressure, new precedent-setting work) disproportionate to its benefit. Per-lane subdirectories (`lane-05-mission-reconstruction/`, `lane-06-outcome-and-underreach-audit/`, etc.) become the right cleanup move if Wave-1 artifact growth confirms the strain; that is a post-Wave-1 decision.
- [d:c+i] What is worth doing pre-Wave-1 for topology is narrower:
  1. Confirm (in the contract or in a companion file) that Wave 1 continues the existing `lane-NN-<model>-<purpose>` convention, including the explicit launch prompt, output artifact, and disposition artifact name patterns.
  2. Confirm that the per-lane packet manifest file, if added, follows a stable name (e.g. `../main-wave/WAVE-1-PACKET-MANIFESTS.md` or `lane-NN-packet-manifest.md`).
  3. Nothing else.

## Version-Control / Change-Management Practice

- [e:c+i] Observed state at review time: `git ls-files .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/` returns empty; `git status` reports `?? .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/`. Zero files in this directory are tracked. Lanes 01-04 were launched against an entirely uncommitted workspace.
- [e:c+i] WORKFLOW.md already mandates: `Before delegating substantial bounded edits, establish an auditable baseline and clean task boundary. Prefer a checkpoint commit when the current state is coherent and reviewable. Do not delegate new substantial edits into an unresolved mixed worktree.` The current state is not meeting that mandate. Sources: WORKFLOW.md:55-67, AGENTS.md:114-117.
- [e:c+i] WORKFLOW.md also mandates, for doctrine-sensitive worker launches, that launch truth be captured as a reviewable artifact using `tooling/codex/capture_launch_truth.py`, so requested-versus-effective settings can be reconstructed later. That aligns with the existing LAUNCH-LEDGER probe-summary pattern but does not replace the need for a committed workspace SHA. Sources: WORKFLOW.md:69-83, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/root-support/LAUNCH-LEDGER.md:1-103.
- [d:r:i] For Wave 1 specifically, this is materially worse than for lanes 01-04, because Wave 1 launches four parallel lanes that all feed Wave 2. Cross-lane comparability depends on being able to reconstruct what each lane actually read. Without a committed baseline, that reconstruction is guesswork.
- [e:r:i] The concrete bounded practice recommendations are already licensed by the existing WORKFLOW.md text and do not require any new doctrine. They are:
  1. Create a checkpoint commit of the entire audit workspace before writing any Wave-1 spec. Suggested message shape: `docs(audit): checkpoint readiness-rerun workspace before Wave-1 spec writing`.
  2. Before launching each Wave-1 lane, commit the lane's spec, launch prompt, and packet manifest in one checkpoint. Suggested shape: `docs(audit): freeze Wave-1 lane-NN packet and spec`. This is the packet-freeze boundary.
  3. After each Wave-1 lane returns, commit the output artifact and the `capture_launch_truth.py` output together. Suggested shape: `docs(audit): land Wave-1 lane-NN output and launch-truth capture`.
  4. Record the frozen-packet commit SHA in the LAUNCH-LEDGER entry for each lane.
- [d:r:i] That is bounded. It does not:
  - require a new branch strategy
  - require rewriting WORKFLOW.md
  - require enforced pre-commit hooks
  - require mandatory squash or rebase policy
  - touch repo branch protection or CI
- [d:r:i] It also does not import generic "use git better" rhetoric. It names four concrete commit boundaries and one ledger field.
- [d:r:i] Explicit supersession markers for superseded launch artifacts are not currently earned as a Wave-1 prerequisite. The existing `../root-support/LAUNCH-LEDGER.md` plus commit history carries supersession adequately. If Wave 1 revisits a launch prompt mid-lane (e.g. revises and relaunches), a supersession note inside the prompt file plus a clear commit message is sufficient. A broader branch strategy (e.g. branch-per-lane or worktree-per-lane) is not earned here and would probably add more coordination cost than it recovers.

## Blockers Versus Later-Facing Cleanup

Classified per the spec's required four-way distinction.

### block_before_wave1_spec

- [d:c+i] Commit the current audit workspace to git as a checkpoint before any Wave-1 spec is written. Sources: WORKFLOW.md:55-67, AGENTS.md:114-117, git ls-files empty for this directory at review time.
- [d:c+i] Resolve per-lane packet references from evidence-family abstractions into concrete file-path manifests before the corresponding Wave-1 spec is written. Either inline in the contract or in a companion `../main-wave/WAVE-1-PACKET-MANIFESTS.md`. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:76-109, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/EVIDENCE-ARCHITECTURE.md:26-98.

### tighten_soon_but_not_blocking

- [d:r:i] Add `INDEX.md` to the Core Packet.
- [d:r:i] Restate the `60k-140k` per-lane token band (or a lane-specific override) inside the contract.
- [d:r:i] Restate the `at least 3 rejected interventions per lane` generative quota inside the contract.
- [d:r:i] Adopt per-lane packet-freeze + launch-truth commit discipline as described above. Can be introduced alongside the Wave-1 spec writing rather than strictly before it.
- [d:r:i] Add an explicit weak-return / packet-drift disposition rule (reroll / accept partial / escalate).
- [d:r:i] Clarify Wave-1 parallelism: either "fully parallel, provisional mission allowed" or "mission-reconstruction runs a short precursor".

### later_cleanup

- [d:r:i] Per-lane subdirectories once the flat topology strains past the point the naming conventions can carry.
- [d:r:i] Reviewer-register vocabulary curation note (from open question in `STATUS.md`).
- [d:r:i] A later pass on whether audit workspaces should establish a stable directory template before the next audit after this one.

### not_earned

- [d:r:i] Repo-wide GSD redesign or branch-strategy rewrite.
- [d:r:i] Readiness-package mutation from this workspace.
- [d:r:i] Wholesale pre-Wave-1 workspace reorganization, including moving files into new directories, renaming existing lane artifacts, or rewriting the authority note.
- [d:r:i] Enforced pre-commit hooks, mandatory branch protection policy, or worktree-per-lane infrastructure.
- [d:r:i] Broader audit-doctrine rewrite.

## Recommended Revisions Before Wave 1 Spec-Writing

Ordered by sequencing rather than importance; each step is narrowly bounded.

1. [d:r:i] Checkpoint-commit the current audit workspace to git. Single commit, single scope: `docs(audit): checkpoint readiness-rerun workspace before Wave-1 spec writing`. This alone moves the workspace from "no auditable baseline" to "auditable baseline", which is the core prerequisite everything else depends on.
2. [d:r:i] Resolve per-lane packet references into concrete file-path manifests before each Wave-1 spec is written. Do this in one companion file, `../main-wave/WAVE-1-PACKET-MANIFESTS.md`, rather than expanding the contract itself. Commit that manifest file before any Wave-1 spec-writing begins. One commit: `docs(audit): add concrete Wave-1 per-lane packet manifests`.
3. [d:r:i] Minimal contract edits, as one focused commit `docs(audit): tighten main-wave contract before Wave-1 spec-writing`:
   - add `INDEX.md` to the Core Packet list
   - point to the `60k-140k` sizing band
   - restate the `≥3 rejected interventions` quota
   - add a weak-return / packet-drift disposition rule
   - name Wave-1 parallelism explicitly
   - add a rule that each Wave-1 lane's launch artifacts are committed as a frozen packet before launch, and the LAUNCH-LEDGER entry records the frozen-packet commit SHA
4. [d:r:i] Only then begin writing Wave-1 lane specs.
5. [d:r:i] Do not reopen lane-04 dispositions, the workspace authority map, or the charter as part of this pre-Wave-1 tightening. If any of those look unstable after the above edits, record that as an open question in `STATUS.md` rather than absorbing it into Wave-1 prep.

## Whether Contract Is Strong Enough To Launch Wave 1 Spec-Writing

- [d:c+i] The contract itself is structurally strong enough on its own terms. It would survive direct adversarial rereading by a later strong reviewer on architecture, lane family, and packet-discipline dimensions. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:27-130, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/AUDIT-CHARTER.md:30-50, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/QUESTION-SET.md:3-100.
- [d:c+i] The contract's Current-Consequence section is correct that the next decision is no longer "what kind of lane family might exist in theory"; it is what concrete pre-Wave-1 tightening is earned and what should be deferred. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:136-140.
- [d:r:i] With the two blockers above resolved (git baseline + concrete per-lane packet manifests), the setup is strong enough to launch Wave 1 spec-writing.
- [d:r:i] Without those two blockers resolved, Wave 1 would launch against an unauditable packet state and against evidence-family abstractions, which re-creates exactly the packet-drift and comparability risk the anti-failure rules already name.
- [d:r:i] The additional `tighten_soon_but_not_blocking` items can be folded into one small pre-Wave-1 contract edit commit without material delay.
- [d:r:i] No additional external cross-review lane is warranted between this one and Wave 1 spec-writing. This lane is itself the contract-level cross-review the contract's own Cross-Review Rule anticipated.

## Required Posture Self-Check

- [d:r:i] I did not reopen a generic `should there be a main wave at all?` meta question. The contract justifies one on its own terms. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-CONTRACT-AND-PACKET.md:6-14, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/main-wave/MAIN-WAVE-LAUNCH-READINESS-DECISION.md:5-21.
- [d:r:i] I did not praise workspace organization for its own sake. I recommended keeping the flat topology only because the authority-note plus naming plus `INDEX.md` are doing real routing work, and because pre-Wave-1 restructuring would itself introduce drift risk.
- [d:r:i] I did not treat `workspace organization can wait` as a default-safe answer. I justified it specifically on the tradeoff between topology-churn cost and marginal clarity gain at current file count.
- [d:r:i] I did not treat `use git better` as an empty gesture. The version-control recommendations are four concrete commit boundaries and one ledger field, licensed directly by existing WORKFLOW.md doctrine that the workspace is currently not meeting.
- [d:r:i] I did not widen into repo-wide GSD redesign, readiness-package mutation, or doctrine rewrite. All recommendations stay inside this audit workspace and its launch discipline.

## Claim-Typing Note

- [a:r:i] Claim markers in this artifact follow the repo-local `[type:support:basis]` minimal form from `AGENTS.md`, applied selectively to load-bearing orientation, evidence, decision, and open-question claims rather than every sentence.
