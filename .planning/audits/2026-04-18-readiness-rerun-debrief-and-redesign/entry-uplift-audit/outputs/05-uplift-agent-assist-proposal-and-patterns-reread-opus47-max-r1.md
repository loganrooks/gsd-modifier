Date: 2026-04-22
Status: completed reread output (opus47-max-r1)

# Uplift Agent-Assist Proposal And Patterns Reread — Opus 4.7 Max R1

## Framing

- [g:r:i] This reread judges the new `102` + `103` pair — [102-uplift-agent-assist-first-slice-proposal.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md) and [103-uplift-agent-assist-patterns.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md) — against the live uplift and propagation-review surfaces rather than against memory of the open note in [93-uplift-agent-assist-and-propagation-baseline-split-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/93-uplift-agent-assist-and-propagation-baseline-split-note.md) alone.
- [g:r:i] Claim notation follows [AGENTS.md:120-133](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:120). Evidenced positive claims cite direct file:line with `[e:c+i]`; downstream design moves carry `[d:r:i]`; framing lines carry `[g:r:i]`.
- [g:r:i] The governing task is to describe what the pair exposes, preserves, thins, and intensifies relative to stronger available forms — not to ask whether it is adequate, sufficient, or ready.

## What The Current Pair Now Carries More Explicitly

### 1. A named non-monolithic shape with an explicit allowed-pattern list

- [e:c+i] `102` names the first-slice direction as "one explicit bounded assist pattern family" containing exactly four patterns: `docs_governance_classification`, `carrier_gap_identification`, `additive_install_packet`, `cross_runtime_comparison_packet`. Sources: [102-uplift-agent-assist-first-slice-proposal.md:24-28](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md:24).
- [e:c+i] `93` previously listed promising future subproblems ("docs/governance uplift classification", "carrier-gap identification", "doctrine-sensitive proposal routing", "cross-runtime or additive-install follow-through packets") but carried them only as prose. Source: [93-uplift-agent-assist-and-propagation-baseline-split-note.md:43-46](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/93-uplift-agent-assist-and-propagation-baseline-split-note.md:43).
- [d:r:i] The carry broadens here: the four patterns now exist as typed slots that a later route hook, subagent spawn, or packet builder can cite by name. The move from prose enumeration to named slot-shapes with per-slot input/output/write-boundary specs in `103:23-85` is what gives later delegation something concrete to answer back to.

### 2. Per-pattern input packet, output shape, and write boundary spec

- [e:c+i] Each of the four patterns in `103` carries an explicit triple — input packet, output, write boundary — at [103-uplift-agent-assist-patterns.md:23-38](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:23) for `docs_governance_classification`, [103:40-56](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:40) for `carrier_gap_identification`, [103:58-70](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:58) for `additive_install_packet`, and [103:72-85](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:72) for `cross_runtime_comparison_packet`.
- [e:c+i] `93` carried no equivalent triple. It named promising subproblems but did not specify what would be handed in, what would come out, or what the subagent could write. Source: [93-uplift-agent-assist-and-propagation-baseline-split-note.md:39-51](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/93-uplift-agent-assist-and-propagation-baseline-split-note.md:39).
- [d:r:i] The write-boundary row is the hardest-carrying addition: every pattern now says "packet only" or "read-only analysis or one bounded review note" in its boundary line. That keeps the distinction between delegated analysis and accepted uplift judgment visible at the pattern level rather than leaving it to launch-time discipline.

### 3. Output-lane home discipline inherited from the propagation-review route

- [e:c+i] `103` routes assist outputs through the same lane-home discipline that the propagation-review harden follow-through landed: `outputs/` for preserved external/composite returns, `dispositions/` for local inheritance or judgment, `*-change-triggered-refresh.md` when the note itself becomes a propagation carrier. Source: [103-uplift-agent-assist-patterns.md:90-93](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:90), inheriting from [propagation-review.md:123-130](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:123) and the harden slice recorded at [100-propagation-review-route-harden-follow-through-implementation.md:18-21](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/100-propagation-review-route-harden-follow-through-implementation.md:18).
- [d:r:i] That inheritance is the first place the pair commits to actually sharing a durable-note grammar with an adjacent repo-local route rather than inventing a new `uplift-assist-output/` path. Sharing the same lane-home vocabulary means later readers do not have to reconstruct where a delegated packet landed — the placement rule is the same as for propagation-review notes.

### 4. Explicit disposition vocabulary held in the parent thread

- [e:c+i] `103` names an explicit four-term disposition vocabulary — `accept`, `revise`, `park`, `reject` — and states that assist output is never self-accepting. Source: [103-uplift-agent-assist-patterns.md:94-99](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:94).
- [e:c+i] `93` left the accept/judgment shape at the level of "main-thread orchestration keeps the composition layer and operator-facing judgment". Source: [93-uplift-agent-assist-and-propagation-baseline-split-note.md:48-50](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/93-uplift-agent-assist-and-propagation-baseline-split-note.md:48).
- [d:r:i] The four-term vocabulary also aligns with [AGENTS.md:167-169](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:167) where the repo-wide delegation rule already names the same four dispositions for agent returns. That means the uplift assist family now cites a disposition grammar that the parent thread already uses elsewhere, rather than introducing a local variant.

### 5. A delegation-shape rule that splits Codex subagent from external Opus lane

- [e:c+i] `103` separates "Codex subagent only when the subproblem is concrete, bounded, and has an auditable read/write boundary" from "an external Opus lane when the task is widening, field-mapping, or comparative challenge rather than repo-local packet work". Source: [103-uplift-agent-assist-patterns.md:102-105](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:102).
- [d:r:i] That split is load-bearing because the two runtimes have different write envelopes: Codex subagents can edit repo files inside an auditable boundary; the external Opus lane produces a report artifact the parent thread then inherits. Naming the split at the reference layer prevents a later route hook from silently blurring a Codex packet writer with an Opus widening read-out.

### 6. A negative list that names what the reference does not authorize

- [e:c+i] `103` carries an explicit four-line negative list: no monolithic uplift agent, no automatic spawn from `uplift-project`, no delegation of final uplift classification/durable writes/cross-route composition, no silent upgrade from detect-only into install/rewrite. Source: [103-uplift-agent-assist-patterns.md:107-112](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:107).
- [d:r:i] The negative list sharpens the carry against drift: a later reader who wants to add an "uplift helper agent" or "default-on agent spawn" will hit this list explicitly rather than running up against ambient caution language.

## Where The Ownership And Route Boundary Is Clearest

### Parent thread owns composition, final judgment, and durable uplift writes

- [e:c+i] The ownership rule runs consistently across three citation points: `102:29-30` keeps "final uplift judgment, durable uplift writes, and composition across neighboring routes in the parent thread"; `103:17-19` says "later uplift delegation should therefore sharpen narrower subproblems while leaving final uplift judgment, durable uplift writes, and multi-route composition in the parent thread"; `uplift-project.md:24-31` already keeps detect-only as the default posture and composition separate from current execution/verification routing.
- [d:r:i] The clarity here runs stronger than the analogous line in `93`, because the live uplift helper already carries the composition-layer language (`uplift-project.md:31`) and the repo-wide delegation rule in `AGENTS.md:167-179` already demands that parent-thread disposition precedes durable write. The three layers are now naming the same boundary in compatible terms.

### Delegated packet work owns one bounded subproblem at a time

- [e:c+i] `103:105` says "keep one assist lane per subproblem. Do not launch a generic 'uplift helper' agent with mixed ownership." Source: [103-uplift-agent-assist-patterns.md:105](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:105).
- [d:r:i] The one-lane-per-subproblem rule is the strongest line for preventing the assist family from collapsing back into a de facto monolithic agent. It also maps cleanly onto `AGENTS.md:148-150`, which forbids recursive GSD call graphs like `orchestrator -> generic agent -> gsd-plan-phase skill -> gsd-planner`.

### Route hook ideas are held explicitly outside the first slice

- [e:c+i] `102:76-80` names four boundaries — no auto spawn from `uplift-project`, no new CLI command, no durable uplift write delegated away, no broader propagation-map redesign. Source: [102-uplift-agent-assist-first-slice-proposal.md:76](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md:76).
- [d:r:i] That held boundary intensifies future carry: the route-hook question can be reopened later as its own slice, with its own verification gate, rather than quietly showing up as a default-on behavior change in `uplift-project.md` once the reference lands.

### Output-lane placement maps to existing propagation-review lane homes

- [e:c+i] `103:89-93` routes uplift assist outputs to the same `outputs/`, `dispositions/`, `*-change-triggered-refresh.md` lane homes that [propagation-review.md:123-130](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/propagation-review.md:123) uses.
- [d:r:i] The boundary is sharpest where it coincides with an existing route's durable-note placement rule. A reader following a later delegated packet will find it where they already look for propagation-review dispositions, rather than in a new `uplift-assist-output/` bucket.

## Which Assist Patterns Look Most Coherently Bounded

### `docs_governance_classification` carries the tightest shape

- [e:c+i] Its input packet is the current uplift detect JSON, the existing `UPLIFT-REPORT.md` / `UPLIFT-MANIFEST.json` / `STATE.md` uplift section, and the named governance docs under consideration. Source: [103-uplift-agent-assist-patterns.md:27-31](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:27).
- [e:c+i] Its output is one compact note listing carriers to refresh now, carriers to hold explicitly, and "reasons and later route ownership". Source: [103-uplift-agent-assist-patterns.md:32-35](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:32).
- [e:c+i] Its write boundary forbids direct edits of governance docs by the assist lane. Source: [103-uplift-agent-assist-patterns.md:36-38](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:36).
- [d:r:i] All three inputs are durable surfaces that already exist in the live repo. The helper produces a stable JSON shape at [project_uplift.py:39-98](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py:39) (carrier specs) and the three durable outputs exist as named artifacts. The output format names the exact downstream route owners. The write boundary forbids the one mutation that would cross into parent-thread judgment. This is the pattern whose packet could be assembled mechanically from existing helper output.

### `carrier_gap_identification` is almost as tightly bounded but overlaps with propagation-review

- [e:c+i] Its input packet is the uplift detect JSON, `95`, `96`, and the current `propagation-review` route. Source: [103-uplift-agent-assist-patterns.md:44-48](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:44).
- [e:c+i] Its output is a bounded gap list grouped by direct consumers, narrative mirrors, runtime/registry carriers, held-later neighbors. Source: [103-uplift-agent-assist-patterns.md:50-54](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:50).
- [d:r:i] The grouping vocabulary here is the same carrier taxonomy that `propagation-review.md:39-48` produces in its `map_the_slice` step. That alignment is a strength for shared reading posture but a source of blur for scope: `carrier_gap_identification` reads like a subset, prerequisite, or parallel lane to a propagation review depending on how the parent thread frames the request. See §Where The Pair Still Blurs §4.
- [d:r:i] When the blur is resolved — for example, by naming this pattern as "the uplift-context narrowing of a propagation review" — the boundary sharpens, because the packet is then a pre-review read-out rather than a rival judgment surface.

### `additive_install_packet` and `cross_runtime_comparison_packet` have named inputs but open downstream consumers

- [e:c+i] `additive_install_packet` inputs are `absent_additive_carriers`, "current runtime/materialization evidence", and "compatibility anchor". Source: [103-uplift-agent-assist-patterns.md:62-65](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:62).
- [e:c+i] `cross_runtime_comparison_packet` inputs are `runtime_dirs`, "observed runtime basis", "compatibility posture", and "relevant runtime snapshots or coherence artifacts". Source: [103-uplift-agent-assist-patterns.md:76-80](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:76).
- [d:r:i] Both are named as packets "for later review" without specifying the downstream consumer route. `additive_install_packet`'s input names an abstract "current runtime/materialization evidence" where the concrete options are either a runtime-visibility snapshot, a manifest/install coherence report, or the uplift helper's own `runtime_dirs` and `compatibility_basis`. `cross_runtime_comparison_packet` has the same openness. These slots carry the family shape but will need the consumer-side route named before either pattern can be exercised end-to-end.
- [d:r:i] Holding these two patterns at the slot level is the right move for the first slice. Specifying their downstream consumer before their first exercise would foreclose on what the first real delegated packet of that flavor teaches about its own output shape.

## Where The Pair Still Blurs Distinct Jobs

### 1. 102's "first slice" and 103's "landed reference" leave the slice boundary ambiguous

- [e:c+i] `102` is statused as "open bounded proposal". Source: [102-uplift-agent-assist-first-slice-proposal.md:2](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md:2).
- [e:c+i] `103` is statused as "landed bounded reference". Source: [103-uplift-agent-assist-patterns.md:2](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:2).
- [e:c+i] `102:34-42` names `103` as the first proposed carrier and names a later route-note update to `uplift-project.md` and `gsd-uplift-project/SKILL.md` as the second carrier. Source: [102-uplift-agent-assist-first-slice-proposal.md:33-42](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/102-uplift-agent-assist-first-slice-proposal.md:33).
- [d:r:i] Because `103` has landed but `102` is still "open", a reader cannot tell whether further action is gated on `102` (the proposal remains the governing artifact until the route-note update also lands) or on a new slice proposal that would treat `103` as the baseline. The two-carrier reading in `102:33-42` suggests the first slice is not complete until the route-note update lands; the `103` status line suggests the reference carrier has already landed independently. That ambiguity is the single largest load-bearing blur in the pair.

### 2. The delegation-shape rule does not route the 4 patterns onto Codex vs. Opus

- [e:c+i] `103:102-105` introduces the Codex-subagent versus Opus-widening split but does not assign any specific pattern to either runtime.
- [d:r:i] A reader looking at the four patterns has to re-derive the mapping. `docs_governance_classification` reads as Codex (concrete, auditable write boundary); `carrier_gap_identification` has a widening flavor that could go either way; `additive_install_packet` reads as Codex; `cross_runtime_comparison_packet` reads as a comparative lane that Opus is better suited to. Leaving that mapping implicit means a first delegated packet could misrun on the wrong runtime and surface the mismatch only at output-shape read time.

### 3. The disposition discipline names accept/revise/park/reject but not the durable carrier for the disposition

- [e:c+i] `103:94-99` requires the parent thread to disposition assist output as `accept`, `revise`, `park`, or `reject`, but it does not name where that disposition is carried durably.
- [e:c+i] The propagation-review route's harden follow-through explicitly carries dispositions to `dispositions/` inside the relevant audit workspace. Source: [100-propagation-review-route-harden-follow-through-implementation.md:18-21](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/100-propagation-review-route-harden-follow-through-implementation.md:18).
- [d:r:i] The uplift-assist pair inherits the lane-home grammar but does not name whether an uplift-assist disposition lands in `entry-uplift-audit/dispositions/`, in a new `.planning/UPLIFT-DISPOSITIONS.md`, or inside `UPLIFT-REPORT.md` as an appended disposition section. Without that pointer, a future reader cannot reconstruct whether a given packet was accepted, parked, or rejected. The propagation-review route solved this by using its audit workspace's existing `dispositions/` directory; the uplift-assist family has not yet named the equivalent home.

### 4. Packet assembly versus packet consumption is not separated

- [e:c+i] Every pattern names an input packet as a list of source artifacts (detect JSON, durable outputs, governance docs, baseline/delta pair). Sources: [103-uplift-agent-assist-patterns.md:27-31](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:27), [103:44-48](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:44), [103:62-65](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:62), [103:76-80](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:76).
- [e:c+i] Neither `102` nor `103` names how the input packet is assembled — whether by hand, by a new helper, by a template that the parent thread fills, or by the existing `project_uplift.py --json` plus a manual bundle.
- [d:r:i] Packet assembly is a distinct job from packet consumption. The current pair leaves assembly ambient. For `docs_governance_classification` — whose three inputs already exist as durable artifacts — a template or thin bundler is a straightforward next move. For `carrier_gap_identification` — whose fourth input is "the current `propagation-review` route when propagation widening matters" — assembly is less obvious because a "route" is not a single file. Without assembly guidance, the input-packet line reads as an expectation rather than a mechanism.

### 5. `carrier_gap_identification` output overlaps with propagation-review output

- [e:c+i] `carrier_gap_identification`'s output is a gap list grouped by direct consumers, narrative mirrors, runtime/registry carriers, held-later neighbors. Source: [103-uplift-agent-assist-patterns.md:50-54](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/103-uplift-agent-assist-patterns.md:50).
- [e:c+i] `propagation-review.md:39-48` produces a very similar multi-carrier map: trigger surfaces, direct producers, direct consumers, narrative mirrors, runtime and registry carriers, durable outputs and state surfaces, intentionally held neighbors.
- [d:r:i] The two outputs look like siblings. The pair does not say whether `carrier_gap_identification` is a prerequisite for a propagation review, a parallel uplift-context analysis, a subset of a propagation review, or an alternative route. Without that framing, a reader with a concrete carrier-gap question could reasonably run either the `$gsd-propagation-review` route or a `carrier_gap_identification` packet and land in slightly different places.

### 6. The live routes do not yet cite `102` or `103`

- [e:c+i] [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md) and [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md) do not reference `102` or `103`.
- [d:r:i] This is consistent with the held-later route-note update named in `102:40-42` and the "no automatic spawn" boundary in `102:76`. It is also a non-carry for a reader coming from the live uplift route: someone running `$gsd-uplift-project` today will not encounter any pointer toward `103`'s assist patterns even at the operator's explicit request. The pair carries its doctrine inside the audit workspace, not on the live route surface. That is the right first-slice posture but it also means the reference carry thins at the live-route boundary until the later opt-in hook lands.

## Strongest First Live Implementation Move

### One delegated packet template exercising `docs_governance_classification`, paired with an explicit disposition carrier location

- [d:r:i] The move is to write one concrete packet template — including an input-bundle layout, an expected output shape, and a disposition endpoint — for `docs_governance_classification`. This is the pattern with the tightest input, the cleanest write boundary, and three durable inputs that already exist. Landing the template forces the packet-assembly question (blur §4) to become concrete for one pattern, and gives later patterns a form they can answer back to.
- [d:r:i] Pair the template with a named disposition carrier — for example, `entry-uplift-audit/dispositions/` used as the existing lane-home for uplift assist, or a new `.planning/UPLIFT-DISPOSITIONS.md` — so that the "accept/revise/park/reject" rule in `103:94-99` has a place to land that is discoverable from the uplift family's existing reading path.

### What the template should do

- [d:r:i] Define a concrete input-bundle layout with file or section names: e.g., `PACKET.md` naming the subproblem, `inputs/detect.json`, `inputs/UPLIFT-REPORT.md`, `inputs/UPLIFT-MANIFEST.json`, `inputs/STATE-uplift-section.md`, `inputs/governance-docs/` for the named docs under consideration.
- [d:r:i] Define the expected output shape as a bounded markdown note matching the four-row structure already in `103:32-35` — "carriers to refresh now", "carriers to hold explicitly", "reasons", "later route ownership" — so the parent thread's accept/revise judgment reads the same shape every time.
- [d:r:i] Name the disposition endpoint in the template itself: either a `dispositions/` path inside `entry-uplift-audit/` or a dedicated register, so that a reader finding the packet output can trace it forward to the disposition that accepted/parked/rejected it.
- [d:r:i] Name the runtime mapping explicitly: this pattern runs on a Codex subagent (bounded, auditable write boundary), not on an external Opus lane (widening/comparative flavor does not apply).

### What the template should not do

- [d:r:i] Not modify `uplift-project.md`, `gsd-uplift-project/SKILL.md`, `project_uplift.py`, or any live route surface. The opt-in route hook is still the right held-later step.
- [d:r:i] Not write to `UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, or `STATE.md`'s uplift section. Those durable outputs stay parent-thread-owned.
- [d:r:i] Not claim to be "automatic" or add a CLI flag to invoke the assist lane. The first exercise should be a manual operator-driven packet-plus-disposition round trip.
- [d:r:i] Not pre-specify templates for `carrier_gap_identification`, `additive_install_packet`, or `cross_runtime_comparison_packet` in the same slice. Their assembly questions differ enough that each deserves its own template slice when it is actually needed.

### Why a route hook is not the strongest first move

- [d:r:i] An opt-in route hook in `uplift-project.md` without at least one exercised packet template would commit the route surface to a carrier shape that no delegated packet has actually produced yet. That is the sequencing mistake that `102:90-91` already implicitly flags by naming the template-first-then-hook order: "the next bounded move is to write the assist-pattern reference surface itself, then decide whether one opt-in uplift-route hook should inherit from it." The reference has landed; the template is the intermediate step between reference and hook.
- [d:r:i] A reference revision of `103` alone carries less than a template exercise. The few revisions `103` would benefit from — pattern-to-runtime mapping, named disposition carrier — can ride along with the template slice rather than landing as a bare doctrine revision.

## Later Families To Keep Explicit

### Must stay held until the first delegated packet has run once

- [d:r:i] The opt-in uplift-route hook in `uplift-project.md` and `gsd-uplift-project/SKILL.md`. Inherit from `102:40-42` and hold until one packet template has been exercised end-to-end.
- [d:r:i] Consumer-side downstream routes for `additive_install_packet` and `cross_runtime_comparison_packet`. Hold until their specific subproblem becomes the concrete next bounded question, rather than pre-specifying the consumer.
- [d:r:i] Any CLI flag or automatic spawn for assist lanes. Inherit from `102:77` and `103:109-110`.
- [d:r:i] Codex-vs-Claude cross-runtime uplift comparison. The live `UPLIFT-MANIFEST.json:9-12` records `runtime_dirs: [".codex", ".claude"]`, so a cross-runtime comparison is a real later question, but it should ride inside `cross_runtime_comparison_packet`'s first exercise, not pre-empt it.

### Must stay held for sequencing reasons

- [d:r:i] Broader propagation-map redesign. Inherit from `102:79`. The baseline/delta pair and propagation-review route are now a coherent family at `95`, `96`, `97-100`, and should be given time to carry a real multi-slice contract change before the map itself is reshaped.
- [d:r:i] Monolithic uplift agent. Inherit from `102:23` and `103:108-109`. This is not a later family; it is an absorbed-into-forbidden direction that should stay in the negative list.
- [d:r:i] Route-local tests for delegation behavior. Inherit from `102:86` which names this as a later-slice move. A route-local test surface would need at least one exercised packet to have a real signal to assert on.

### Must stay held because they belong to different families

- [d:r:i] Rerun-floor honesty-rule batch landing into governing surfaces. See [CURRENT-STATE.md:125](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md:125). That is a rerun-program family, not an uplift-assist family.
- [d:r:i] Broader whole-network widening of the propagation family. See [CURRENT-STATE.md:124](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md:124) — "later refreshes should keep following actual contract movement rather than abstract appetite for bigger maps."
- [d:r:i] Compatibility anchor graduating into a standalone carrier. See [CURRENT-STATE.md:144](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md:144). The uplift assist family may use the compatibility anchor as input (pattern #3), but graduating the anchor is a propagation-family question, not an uplift-assist one.

## How This Pair Should Be Inherited

### Carry Forward

- [d:r:i] `102`'s explicit non-monolithic framing and the four named assist patterns as the uplift-assist family shape.
- [d:r:i] `103` as the active landed reference surface for the pattern family, including its per-pattern input/output/write-boundary triples, the output-discipline lane-home rule inherited from propagation-review, the disposition vocabulary, the Codex/Opus delegation-shape split, and the negative list.
- [d:r:i] The repo-wide disposition vocabulary shared with [AGENTS.md:167-169](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:167) so the uplift assist family uses the same accept/revise/park/reject terms the rest of the delegation surface already uses.
- [d:r:i] The composition-layer ownership rule stated compatibly across `102:29-30`, `103:17-19`, `uplift-project.md:24-31`, and `AGENTS.md:148-179`.

### Revise Before Live Hooking

- [d:r:i] Resolve the `102`/`103` status ambiguity. Either re-status `102` as "first slice reference landed via 103, route-note update held for later" so the pair reads as proposal-plus-landing, or split `102` into two bounded proposals (one for the reference, one for the later route-note update) and mark the first as consumed.
- [d:r:i] Name the pattern-to-runtime mapping in `103`'s Delegation Shape section: `docs_governance_classification` → Codex subagent; `carrier_gap_identification` → Opus widening (or Codex when the gap list is already concrete); `additive_install_packet` → Codex subagent; `cross_runtime_comparison_packet` → Opus widening. Make the defaults explicit so a first delegated packet does not silently land on the wrong runtime.
- [d:r:i] Name the durable disposition carrier for uplift assist. Either reuse `entry-uplift-audit/dispositions/` (consistent with propagation-audit's lane-home pattern) or create a compact `.planning/UPLIFT-DISPOSITIONS.md` carrier. Add the pointer to `103`'s Output Discipline section so the disposition rule has a home a reader can trace.
- [d:r:i] Name `carrier_gap_identification`'s relation to the propagation-review route explicitly in `103`: whether it is a pre-review uplift-context narrowing, a parallel lane, or a subset of propagation-review output. Pick one and say so, to prevent the two lanes from producing overlapping judgments without a framing that says which the reader should prefer.
- [d:r:i] Name the packet-assembly expectation for at least `docs_governance_classification` before that pattern is cited as actionable doctrine — a short `103` section or the accompanying template slice.

### Hold For Later

- [d:r:i] The opt-in uplift-route hook in `uplift-project.md` and `gsd-uplift-project/SKILL.md`. Do not land this until at least one packet template has been exercised end-to-end and at least one disposition has landed in the named carrier.
- [d:r:i] Consumer-side downstream specs for `additive_install_packet` and `cross_runtime_comparison_packet`. Hold until their respective subproblems become concrete. Their current slot shapes carry the family; prematurely naming their consumers would foreclose on what a real exercise teaches.
- [d:r:i] Route-local tests for delegation behavior, new CLI flags, automatic spawn behavior, and broader propagation-map redesign. Keep these on the `102:76-80` negative list.
- [d:r:i] Cross-repo distribution of the uplift-assist pattern family. That lives inside the broader harness-improvement family ([CURRENT-STATE.md:69](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md:69) names "later cross-repo distribution" as held later work). Hold until the in-repo pair has carried at least one real slice.
