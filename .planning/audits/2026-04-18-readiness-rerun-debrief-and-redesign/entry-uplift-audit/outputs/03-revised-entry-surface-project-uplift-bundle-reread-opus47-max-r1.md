Date: 2026-04-21
Status: completed reread output (opus47-max-r1)

# Revised Entry Surface / Project Uplift Bundle Reread — Opus 4.7 Max R1

## Framing

- [g:r:i] This reread reads the revised `37 + 38 + 39` as one bounded bundle against the live entry-surface set and the current governing/carrier context. The task is not to rerun the lane-02 challenge or to reopen generic terrain discovery; it is to judge what the Opus-led local revision pass now carries, what it still leaves thin, and what the strongest next move after this read should be.
- [g:r:i] Claim typing follows [AGENTS.md:93-106](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:93). Evidenced positive claims carry `[e:c+i]` with direct file and line refs; downstream design moves carry `[d:r:i]`; framing lines carry `[g:r:i]`.
- [g:r:i] Where the bundle's own language still drifts into threshold-shaped deficit comparison ("older local doctrine version"), this reread names the specific place in positive fingerprint/delta form, per [.planning/AGENTS.md:117-124](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:117).

## What The Revised Bundle Now Carries More Strongly

### 1. `37` Scenario Map now carries the full uplift typology at the entry of the document

- [e:c+i] `37` §Scenario Map now names the vanilla case plus the four-way split as five distinct ownerless scenarios directly at the entry of the map: `Existing vanilla project ...`, `Existing lightly aged project ...`, `Existing aged-bespoke project ...`, `Cross-runtime posture uplift`, `Upstream-template-drift uplift`. Source: [37:67-76](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:67).
- [d:r:i] This is the revision's strongest structural gain in `37`. Readers who entered the document from the Scenario Map previously saw one ownerless vanilla line and had to scroll to the Scattered section to discover the four-way split. The revised map now carries the same cardinality at both sections, which lets `39`'s classification list read from `37` instead of reconstructing the typology from memory.

### 2. Mid-phase uplift is now a first-class scenario with named adjacent carriers

- [e:c+i] `37` §Scenario Map carries `Existing active phase whose doctrine posture has moved mid-stream` with explicit adjacent-carrier naming: `phase CONTEXT.md`, `progress`, `discuss-phase`. Source: [37:49-51](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:49).
- [d:r:i] Mid-phase was the most frequent real case the repo itself will hit — Phase 01 sits at a pre-rerun boundary per [AGENTS.md:43](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:43). Naming the adjacent carriers in the Scenario Map means the later workflow does not need to invent a new steering surface; it reads `CONTEXT.md` and routes to `discuss-phase`, which is already a live specialist. The revision grounds the mid-phase case in existing carriers rather than inventing a new one.

### 3. Installer re-run has its own primary-owner seat separate from `update`

- [e:c+i] `37` §Scenario Map now lists `Installer re-run / materialization refresh without broader project uplift` as its own scenario with `scripts/setup-portable-gsd.sh` as current primary owner and `update` as strongest supporting owner. Source: [37:56-58](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:56).
- [d:r:i] This preserves the materialization chain in [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33-42](../../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33) directly in the Scenario Map. An overlay change that lands without a version bump is now a legitimate routable case rather than silently failing through `update`'s already-current refusal. The revision makes installer authority load-bearing rather than subordinate to version truth.

### 4. `38` now seats per-phase `CONTEXT.md` as primary for rerun-boundary posture

- [e:c+i] `38` §6 Doctrine Vintage / Pre-Rerun Boundary / Active Boundary Posture now lists primary carriers as `per-phase CONTEXT.md boundary stamp`, `STATE.md`, `UPLIFT-STATE.md or equivalent uplift history`, `progress / resume-project routing branches` in that order, with root/planning `AGENTS.md` and audit-artifact rerun-boundary notes as supporting. Source: [38:111-119](../../intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md:111).
- [d:r:i] This is the placement that the live repo rule at [AGENTS.md:43](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:43) already enforces as a per-phase fact. Seating `CONTEXT.md` first gives `resume-project` and `progress` a reading surface that already exists ([resume-project.md:216-220](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md:216)) rather than requiring a new parser. The revision closes the gap where single-frame `STATE.md` was being asked to carry per-phase vintage.

### 5. `38` now names a tooling inventory carrier as primary for repo-local tooling install

- [e:c+i] `38` §9 Repo-Local Tooling Install now lists primary carriers as `explicit tooling inventory carrier such as tooling/codex/INVENTORY.md`, the uplift workflow/install pass, and the project doctrine manifest, with root/planning `AGENTS.md` and `UPLIFT-REPORT.md` and audit-subtree README conventions as supporting. Source: [38:163-170](../../intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md:163).
- [d:r:i] With the live tooling tree at `tooling/codex/` already named in [.planning/AGENTS.md:44-74](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:44), an inventory carrier turns uplift into diff-against-inventory rather than enumerate-at-write-time. Tool additions after first-slice ship-date stay legible without silent rot. This is one of the revisions whose consumer-side leverage shows up most clearly in later slices.

### 6. `38` now seats runtime-side registry as primary for cross-runtime posture

- [e:c+i] `38` §8 Cross-Runtime Posture now lists primary carriers as `.codex/config.toml`, `.codex/agents/*.toml`, and uplift outputs that record runtime posture and wrapper alignment, with root/planning `CLAUDE.md` wrappers, root/planning `AGENTS.md`, the generated instruction file, and `update` as supporting. Source: [38:147-153](../../intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md:147).
- [d:r:i] This is the placement the live authority companion already implied at [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:40-42](../../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:40). Runtime-side registry and wrapper-side operator truth can drift independently; the revision acknowledges that by giving registry files first seat. Later cross-runtime uplift work now has a carrier hierarchy to read rather than a wrapper prose scan.

### 7. `39` opens with detect-only as default posture rather than composite mutation

- [e:c+i] `39` §Entry Conditions now states `Detect-only should be the default opening posture. Refresh or install should require explicit flags.` Source: [39:57](../../intervention-proposals/39-project-uplift-workflow-proposal.md:57).
- [d:r:i] Every first invocation is now diagnostic, not mutating. That opens the workflow to aged-bespoke and cross-runtime cases without breaching the deferrals at [39:91-99](../../intervention-proposals/39-project-uplift-workflow-proposal.md:91), and it lets `progress` or `resume-project` consume a detect-only run as a read-only signal later without any absorption. This is the single change that made the rest of the revision pass safe.

### 8. `39` Detection Signals now mostly use fingerprint-differs-from-current form

- [e:c+i] `39` §Detection Signals carries lines like `governing-doc carrier fingerprint differs across root/planning AGENTS.md or CLAUDE.md wrappers`, `required-reading installation practice is not yet present on the project's live packet/spec/prompt surfaces`, `strengthening-route carry is not yet present in the local discuss/context/plan/research chain where the repo now expects it`, `repo-local tooling inventory expected by doctrine is not yet present`, `runtime-side registry or wrapper posture fingerprints differ from current local runtime expectations`. Source: [39:73-80](../../intervention-proposals/39-project-uplift-workflow-proposal.md:73).
- [d:r:i] This is a real shift away from deficit-shaped prose. "Differs from current" and "not yet present on surfaces where the repo now expects it" are positive fingerprint forms. The previous bundle's "thin or older," "materially older," and "clearly outside current repo posture" residue is now absent from most of the list. Two lines still carry "older local doctrine version" residue; that is named in the revision section below.

### 9. `39` splits first-slice refresh into low-ambiguity additive routes and doctrine-sensitive proposal routes

- [e:c+i] `39` §4 Apply Explicit First-Slice Refresh Flags now separates `Low-ambiguity additive routes` (install `CLAIM-TYPES.md`/`LONG-ARC.md`/thin manifest/tooling inventory where absent) from `Doctrine-sensitive proposal routes` (generate diffs/proposals for root/planning `AGENTS.md`, root/planning `CLAUDE.md`, required-reading practice, strengthening-route carry). Source: [39:149-163](../../intervention-proposals/39-project-uplift-workflow-proposal.md:149).
- [d:r:i] Those two lanes now carry different blast-radius labels and different authority rules. Install-where-absent is a write-if-new operation with zero content conflict; proposal generation defers the actual mutation to human review per [AI-GUARDRAILS.md:13-21](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:13). That split is the main reason the first slice can ship without overlapping with the aged-bespoke deferral.

### 10. `39` splits `CLAIM-TYPES.md` reference install from claim-type practice activation

- [e:c+i] `39` §4 now carries `Claim-type reference install and claim-type activation are separate: reference-file install may sit in the first slice; activation across existing load-bearing artifacts should require explicit operator consent because it rewrites project content.` Source: [39:160-162](../../intervention-proposals/39-project-uplift-workflow-proposal.md:160).
- [d:r:i] This closes the "install the rule book but no artifact uses it" failure mode. The rule book install lands in first slice; the practice activation stays with an explicit flag because it rewrites content. Future aged-bespoke work inherits the activation pathway without needing to re-argue the separation.

### 11. `39` lands the thin doctrine manifest in the first slice alongside `UPLIFT-REPORT.md` and `STATE.md` uplift section

- [e:c+i] `39` §5 Write Durable Uplift Outputs now names first-slice outputs as `UPLIFT-REPORT.md`, `dedicated uplift section inside STATE.md`, and `thin doctrine manifest such as UPLIFT-MANIFEST.json`. Source: [39:167-170](../../intervention-proposals/39-project-uplift-workflow-proposal.md:167).
- [e:c+i] The manifest records `carrier fingerprints or version stamps`, `last detect-only pass`, `last explicit install pass`, `whether runtime-side registry and wrapper posture align`, `whether any doctrine-sensitive proposals are still pending human review`. Source: [39:182-187](../../intervention-proposals/39-project-uplift-workflow-proposal.md:182).
- [d:r:i] The manifest is the only object that lets `progress` and `resume-project` consume vintage without prose parsing. Moving it into first slice brings the consumer-side carry online at the same time as the producer-side carry, rather than leaving a one-slice gap where the workflow writes reports that downstream surfaces cannot read structurally.

### 12. `39` lands one read-only `progress` hook in the first slice

- [e:c+i] `39` §6 Route The Next Action now names `First live routed consumer: one read-only progress hook that notices the uplift section plus thin doctrine manifest and can recommend gsd-uplift-project --detect-only when posture has drifted or when pending doctrine-sensitive proposals are still unresolved.` Source: [39:198-200](../../intervention-proposals/39-project-uplift-workflow-proposal.md:198).
- [d:r:i] `progress` already reads `state-snapshot` at [progress.md:49](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:49) and has a route table that does not yet carry a posture-debt branch. A one-line read-only hook is where the first-slice consumer leverage actually meets the operator — without it the workflow writes reports only operators who already thought to invoke uplift would see.

### 13. `39` names the self-scan gate on the workflow's own output

- [e:c+i] `39` §Review And Verification Gates now carries `run scan_threshold_language.py on generated UPLIFT-REPORT.md before finalizing the pass`. Source: [39:227](../../intervention-proposals/39-project-uplift-workflow-proposal.md:227).
- [d:r:i] This prevents the workflow from becoming a regression surface for threshold language on its own authoring content. A doctrine-carrying workflow that can regress the doctrine it carries is a specific failure mode the gate now forecloses.

## Where The Revised Bundle Still Thins Or Compresses Distinct Jobs

### 1. Mid-phase reaches `37` scenario map but not `39` classification list

- [e:c+i] `39` §1 Open The Pass And Classify It lists five uplift classes: `vanilla uplift`, `lightly aged uplift`, `aged-bespoke uplift`, `cross-runtime uplift`, `upstream-template-drift uplift`. Source: [39:113-117](../../intervention-proposals/39-project-uplift-workflow-proposal.md:113).
- [e:c+i] `37` §Scenario Map now carries `Existing active phase whose doctrine posture has moved mid-stream` as its own scenario. Source: [37:49-51](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:49).
- [d:r:i] The mid-phase case has a seat in terrain but no seat in workflow classification. `39` routes to `discuss-phase` at line 196 when `a phase boundary should be reopened under current doctrine`, but that is downstream routing, not classification. Without a mid-phase class in §1, the workflow cannot record `mid-phase` into the `STATE.md` uplift section or the manifest, which means later passes cannot see the class continuity the bundle's own four-way split exists to preserve. This is the most consequential seam remaining.

### 2. Fingerprint is invoked by name but not specified as a shape

- [e:c+i] `39` §Detection Signals uses `fingerprint differs`; `39` §3 says the delta includes `current carrier fingerprints`; `39` §5 says the manifest records `carrier fingerprints or version stamps`. Source: [39:73](../../intervention-proposals/39-project-uplift-workflow-proposal.md:73), [39:139](../../intervention-proposals/39-project-uplift-workflow-proposal.md:139), [39:183](../../intervention-proposals/39-project-uplift-workflow-proposal.md:183).
- [d:r:i] The manifest line names `fingerprints or version stamps` as if they were interchangeable. They are not: a version-stamp carrier (for example a `version:` key in `CLAIM-TYPES.md` or an `AGENTS.md` doctrine-vintage line) is stable and cheap to compare; a content-hash carrier is precise but collides with any whitespace-level edit; a section-list hash is in between. Without one concrete table naming which carrier uses which fingerprint shape, the first implementer will pick per carrier and that pick will become the implicit contract. That is how ad hoc decisions become doctrine by accident.

### 3. Two Detection Signal lines still carry deficit-shaped comparison

- [e:c+i] `39` §Detection Signals carries `.planning/CLAIM-TYPES.md carrier is absent or fingerprints to an older local doctrine version` and `.planning/LONG-ARC.md carrier is absent or fingerprints to an older local doctrine version`. Source: [39:74-75](../../intervention-proposals/39-project-uplift-workflow-proposal.md:74).
- [d:r:i] `older local doctrine version` is a threshold comparison against an implicit bar; the other detection lines in the same list already use the positive form (`fingerprint differs across X`, `not yet present on surfaces where the repo now expects it`). These two can be harmonized with `fingerprint differs from current doctrine fingerprint` without losing meaning. Leaving them shaped as `older than` is the last trace of the deficit form the revision pass reformed elsewhere.

### 4. `UPLIFT-STATE.md` and `STATE.md` uplift section are both still live as carrier names

- [e:c+i] `39` §5 first-slice outputs names `dedicated uplift section inside STATE.md`. Source: [39:169](../../intervention-proposals/39-project-uplift-workflow-proposal.md:169).
- [e:c+i] `38` §6 still names `UPLIFT-STATE.md or equivalent uplift history` as one of the primary carriers for doctrine-vintage. Source: [38:115](../../intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md:115). `37` §Output Record and §Candidate Ownership Split still name `UPLIFT-STATE.md` as a carrier candidate. Source: [37:207](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:207), [37:222](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:222).
- [d:r:i] The bundle has half-committed to the `STATE.md` section as the landing spot for state carry — which matches what `progress` and `resume-project` actually read ([progress.md:49](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:49), [resume-project.md:34-59](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md:34)) — but the `UPLIFT-STATE.md` name still appears across all three artifacts. For a first slice, two names pointing at the same concern produces the exact "weakly carried in several places" failure that `38`'s placement rule was written to avoid.

### 5. The `progress` hook reads two carriers for one recommendation

- [e:c+i] `39` §6 says the hook `notices the uplift section plus thin doctrine manifest`. Source: [39:199](../../intervention-proposals/39-project-uplift-workflow-proposal.md:199).
- [d:r:i] Two read paths for one recommendation invites reconciliation work when the manifest and `STATE.md` section disagree (for example after a partial run where one was written but the other failed). The manifest carries structural fingerprints; the `STATE.md` section carries operator-facing narrative. Naming the manifest as authoritative signal and `STATE.md` as narrative companion keeps the hook's routing logic one-sided without losing operator visibility.

### 6. Installer re-run posture reaches `37` as primary but is missing from `39`'s evidence list

- [e:c+i] `37` §Scenario Map now gives installer re-run its own primary owner at `scripts/setup-portable-gsd.sh`. Source: [37:56-58](../../intervention-proposals/37-entry-surface-and-project-uplift-map.md:56).
- [e:c+i] `39` §2 Gather Evidence From Specialist Owners lists runtime/install truth sources as `update posture`, `runtime_visibility.py`, `manifest_install_coherence.py`. Source: [39:122-125](../../intervention-proposals/39-project-uplift-workflow-proposal.md:122).
- [d:r:i] `scripts/setup-portable-gsd.sh` is absent from the evidence list even though the Scenario Map promoted it. If the workflow consumes runtime truth from `update` only, an installer-rerun-needed posture (overlay change without version bump) is invisible to the detector. The revision gained the right placement in `37` without propagating the evidence-source into `39`.

### 7. Audit-subtree doctrine-vintage stamp is named in `38` as primary but silent in `39`

- [e:c+i] `38` §10 Audit-Subtree And Companion-Carrier Aging now names `doctrine-vintage stamp on doctrine-carrying audit subtrees` as a primary carrier. Source: [38:182-183](../../intervention-proposals/38-entry-surface-concern-and-carrier-placement-map.md:182).
- [e:c+i] `39` §Detection Signals and §First-Slice Scope do not mention doctrine-carrying audit subtrees at all. Source: [39:71-99](../../intervention-proposals/39-project-uplift-workflow-proposal.md:71).
- [d:r:i] That is probably correct as a first-slice scope (audit-subtree aging is a separate later family), but the bundle should name that deferral explicitly in `39`'s first-slice hold-out list rather than leave the placement in `38` and the absence in `39` as silent disagreement. The active `2026-04-18-readiness-rerun-debrief-and-redesign/` tree itself carries doctrine-shaping artifacts, so the deferral is a live question, not a hypothetical.

### 8. Evidence sources in `39` §2 do not map to install flags in `39` §4

- [e:c+i] `39` §2 lists seven evidence sources (`update`, `runtime_visibility.py`, `manifest_install_coherence.py`, `health`, `STATE.md`, `progress`, `resume-project`, `ingest-docs`). Source: [39:122-133](../../intervention-proposals/39-project-uplift-workflow-proposal.md:122).
- [e:c+i] `39` §4 lists additive install flags only for four carriers (`CLAIM-TYPES.md`, `LONG-ARC.md`, thin manifest, tooling inventory) plus doctrine-sensitive proposal routes. Source: [39:150-159](../../intervention-proposals/39-project-uplift-workflow-proposal.md:150).
- [d:r:i] There is no explicit table showing which evidence source feeds which install/proposal route. For example, `runtime_visibility.py` output is pulled in §2 but no first-slice flag consumes it — which is the right outcome for the first slice, but the bundle should say so rather than leave the evidence-to-flag mapping as a reader inference. Otherwise the evidence step looks richer than the install step can justify and a future widening pass will add flags to match the evidence by default.

## What The Revised Workflow Mechanics Improve

### Detect-Only Default

- [d:r:i] The detect-only default is the mechanic with the widest downstream effect in the revised bundle. Every first invocation now becomes diagnostic: read carriers, classify the pass, write `UPLIFT-REPORT.md` plus manifest plus `STATE.md` uplift section, exit with zero mutation of existing content. This is what makes aged-bespoke, cross-runtime, and upstream-template-drift cases safe to probe without breaching the first-slice deferrals. Without detect-only, the workflow could only be run against the cases it was already prepared to mutate, which collapses the detection half of the design back into the first-install half.

### Fingerprint/Delta Detection

- [d:r:i] The fingerprint frame is the mechanic that lets detection be implemented without re-inventing prose comparison. The revision carries `fingerprint differs across` and `not yet present on surfaces where the repo now expects it` as the detection vocabulary, which makes each detection signal a function over two carrier states (current repo-local, project-local) rather than a comparison against an implicit bar. The shape of the fingerprint still deserves one concrete specification (see §Still Deserves Revision §2), but the frame itself is already a load-bearing gain.

### Thin Doctrine Manifest In First Slice

- [d:r:i] Promoting the manifest from second-slice deferral to first-slice output brings the consumer-side leverage online one slice earlier. The manifest is the only object that `progress` and `resume-project` can consume without prose parsing; without it the `progress` hook would need a markdown extractor. Keeping the manifest thin (carrier-name → fingerprint, plus the five-line metadata at [39:182-187](../../intervention-proposals/39-project-uplift-workflow-proposal.md:182)) also keeps the blast radius contained.

### Read-Only `progress` Hook

- [d:r:i] The `progress` hook is where the first slice's leverage actually meets the operator. `progress` already runs as the default next-step-router; a one-line recommendation after it reads `state-snapshot` is what turns uplift from "a thing the operator has to remember to run" into "a thing `progress` surfaces when posture drifts." The deferral of the remaining five routed-entry hooks (`resume-project`, `health`, `update`, `ingest-docs`, `new-milestone`) is correct first-slice discipline; they can widen after live examples.

### Per-Carrier Install Flags With Blast-Radius Labels

- [d:r:i] Splitting the first-slice refresh into per-carrier flags replaces a single wide mutation step with an enumerable set of narrow ones. `--install-claim-types`, `--install-long-arc`, install-thin-manifest, install-tooling-inventory each carry the write-if-absent contract; proposal generation for `AGENTS.md`/`CLAUDE.md`/required-reading/strengthening-route keeps the doctrine-sensitive content behind human review. This is the mechanic that lets the first slice coexist with the aged-bespoke deferral without contradiction.

### Split Of Claim-Type Reference Install From Activation

- [d:r:i] This split is small in text but load-bearing in effect. Installing `CLAIM-TYPES.md` is write-if-absent; activating claim notation across load-bearing artifacts is a content rewrite with broad surface. Keeping them as separate flags forecloses the failure mode where a first-slice pass leaves the rule book in place with zero typed artifacts, which would be posture-shaped but not practice-shaped.

### Self-Scan Gate On `UPLIFT-REPORT.md`

- [d:r:i] Running `scan_threshold_language.py` on the workflow's own generated output before finalizing closes the regression seam where a doctrine-carrying workflow could regress the doctrine it carries. The scan already exists in the repo's tool inventory; the gate is a one-line addition in the workflow with an outsized effect on long-horizon integrity of the uplift memory chain.

## What Still Deserves Revision Before Implementation

The revisions named here are narrow. None of them reopens the family shape; each is a small harmonization between `37`, `38`, `39` and the live surfaces they route into. In aggregate they harden the implementation contract before code is written and should ship together as one pre-implementation revision pass.

### 1. Add a mid-phase classification to `39` §1

- [d:r:i] Add `mid-phase uplift` as a sixth class in `39:113-117`, alongside vanilla/lightly aged/aged-bespoke/cross-runtime/upstream-template-drift. Detection signal: the active phase's `CONTEXT.md` lacks a rerun-boundary stamp while governing doctrine has moved since the `CONTEXT.md` was authored. First-slice action: classify and report; route to `discuss-phase` through the existing routing list at [39:192-197](../../intervention-proposals/39-project-uplift-workflow-proposal.md:192). Without this class, the mid-phase case has terrain carry in `37` but no persistence path through the workflow's classification memory.

### 2. Name fingerprint shape per carrier

- [d:r:i] Add a small table in `39` (either §1 or §5) naming each carrier's fingerprint shape: version-stamp for `CLAIM-TYPES.md`/`LONG-ARC.md`/`AGENTS.md` when those carry a doctrine-vintage marker; content hash for `CLAUDE.md` wrappers; section-list hash for tooling inventory; registry-file hash for `.codex/config.toml`. The table is small and turns "fingerprints or version stamps" from interchangeable terms at [39:183](../../intervention-proposals/39-project-uplift-workflow-proposal.md:183) into a concrete contract the first implementer reads rather than invents.

### 3. Harmonize the two remaining deficit-shaped detection lines

- [d:r:i] Rewrite [39:74](../../intervention-proposals/39-project-uplift-workflow-proposal.md:74) and [39:75](../../intervention-proposals/39-project-uplift-workflow-proposal.md:75) to match the positive form the rest of the list uses: `.planning/CLAIM-TYPES.md carrier is absent or its fingerprint differs from the current repo-local doctrine fingerprint`, `.planning/LONG-ARC.md carrier is absent or its fingerprint differs from the current repo-local doctrine fingerprint`. This is a small edit with direct effect on the scan_threshold_language.py gate, which will catch `older` as threshold residue on the `39` surface itself.

### 4. Commit to `STATE.md` uplift section and demote `UPLIFT-STATE.md` from primary carrier status

- [d:r:i] Update `38:115` so the primary carrier is `STATE.md uplift section` and `UPLIFT-STATE.md` moves to a later-family option. Update `37:207` and `37:222` to match. `39:169` already lands on the `STATE.md` section for first-slice output; the other two artifacts should follow. `progress` and `resume-project` already read `STATE.md` directly, so the `STATE.md` section is where the consumer hook actually reaches live code without a new parser.

### 5. Add installer-rerun posture as its own evidence source in `39` §2

- [d:r:i] Add `scripts/setup-portable-gsd.sh posture` or equivalent to the evidence list at [39:122-125](../../intervention-proposals/39-project-uplift-workflow-proposal.md:122). The detector needs a read path for "installer ran; overlay copy is current; manifest coherence reports clean" distinct from "npm version is current." Without it the installer-rerun scenario in `37` has no evidence carrier in `39`.

### 6. Name manifest as authoritative fingerprint source for the `progress` hook

- [d:r:i] Update `39:199` so the hook reads the manifest as the structural signal and the `STATE.md` uplift section as the narrative companion: `progress reads UPLIFT-MANIFEST.json fingerprints and posture-drift flags; the STATE.md uplift section provides operator-facing narrative when the hook fires.` This makes the hook logic single-sourced rather than two-read-paths-needing-reconciliation.

### 7. Name the audit-subtree aging deferral explicitly in `39` §First-Slice Scope

- [d:r:i] Add to the hold-out list at [39:91-99](../../intervention-proposals/39-project-uplift-workflow-proposal.md:91): `doctrine-carrying audit subtree vintage stamping`. This keeps `38:182-183`'s primary placement honest by explicitly saying the first slice does not act on it, rather than leaving the placement and the workflow silently disagreeing.

### 8. Add one line to `39` §2 declaring that some evidence sources are detect-only in first slice

- [d:r:i] After [39:133](../../intervention-proposals/39-project-uplift-workflow-proposal.md:133), add: `In the first slice, runtime_visibility.py and manifest_install_coherence.py outputs feed detect-only reporting; they route to update/installer-rerun rather than to any install flag.` This closes the evidence-to-install mismatch without widening the install surface.

## Later Families To Keep Explicit

### Mid-Phase Uplift Routing

- [d:r:i] First slice should detect and classify mid-phase cases (per revision §1 above) and route to `discuss-phase`. Actually defining what happens inside `discuss-phase` when doctrine has moved mid-phase — how the steering brief gets reopened, what `CONTEXT.md` carries forward, what `progress` shows — stays with later family work. The detection/classification carry is what makes the later family implementable without retro-fabrication.

### Aged-Bespoke Uplift

- [d:r:i] Project whose governing docs carry bespoke local content that current doctrine should respect rather than overwrite. Detection shape needs section-level diff with bespoke carve-outs before drift reporting. Deferring keeps the first slice small and preserves bespoke value; the `39:91-99` deferral should stay.

### Cross-Runtime Uplift

- [d:r:i] First slice detects the cross-runtime class via `.codex/config.toml` and `.codex/agents/*.toml` fingerprints per `38:147-149`; action stays deferred. The runtime-side registry as primary carrier is the placement that makes the later family implementable.

### Upstream-Template-Drift Uplift

- [d:r:i] First slice detects that package version and local posture are current while shipped templates have moved; action stays deferred. Requires a carrier that records the upstream-template version the project was last aligned with — that carrier's design belongs in the upstream-drift slice itself.

### Audit-Subtree Aging With Doctrine-Carrying Subtrees

- [d:r:i] Per `38:180-184`, doctrine-carrying audit subtrees (this workspace being the clearest live example) need per-audit doctrine-vintage stamps. That machinery stays with audit-subtree aging work; first slice should name the deferral explicitly.

### Required-Reading Template Seeding Upstream

- [d:r:i] First slice installs the practice in project-local templates only; upstream-template seeding is where the practice propagates across repos. Separate ownership, separate blast radius, separate slice.

### Workstream Parent↔Child Posture Drift

- [d:r:i] Uplift can note workspace drift in reports when detected; actual parent-driven reconciliation stays with workstream-family work. The uplift workflow should not merge across workstreams.

### Forensics And Archived-Milestone Re-Entry

- [d:r:i] Stay specialist. Uplift consumes forensic output as one input only when relevant.

### Routed-Entry Hooks In `resume-project`, `health`, `update`, `ingest-docs`, `new-milestone`

- [d:r:i] Deferred per `39:62-68`. First slice carries only the `progress` hook; the remaining five widen after live examples show which routings the operator actually wants.

### Aged-Bespoke Claim-Type Activation Across Load-Bearing Artifacts

- [d:r:i] First slice installs `CLAIM-TYPES.md` reference only; artifact-content rewrite to expose terse claim status requires explicit operator consent per `39:160-162` and belongs with aged-bespoke slice work.

### Rich Doctrine-Manifest Content Diffs Beyond Thin Version-Marker Form

- [d:r:i] First slice carries carrier-name → fingerprint pairs plus the five-line metadata. Rich section-level content diffs, bespoke carve-out logic, and cross-carrier correlation land in later slices.

## Strongest Next Move

- [d:r:i] The revised bundle now carries enough structural form that first-slice implementation is a workable next action — with the qualification that the eight narrow revisions in §What Still Deserves Revision Before Implementation should land first as one small pre-implementation pass. They are small, local, and concrete; none of them reopens terrain or placement.
- [d:r:i] Sequence after this reread:
  1. Apply the eight narrow revisions to `37`, `38`, `39` as one bounded pass. Run `scan_threshold_language.py` on the three artifacts. Run `audit_refmap.py verify` on the audit root.
  2. Implement the first slice: detect-only default, fingerprint-based detection per the carrier table, four additive install flags, proposal generation for doctrine-sensitive carriers behind human review, `UPLIFT-REPORT.md` plus `STATE.md` uplift section plus thin manifest as outputs, one read-only `progress` hook, self-scan gate on generated output.
  3. Verify against the two-case pilot (one vanilla project, one lightly aged project) plus the negative test on prix-guesser itself (classification should be `already current`, delta should be empty, no refresh proposed).
  4. Only after the first slice produces real examples, open the next widening pass.
- [d:r:i] Reason the next move is narrow revision plus implementation rather than another cross-vendor challenge: the revised bundle's remaining seams are small and specific (class missing, fingerprint shape undefined, carrier-name disagreement, evidence-to-flag mapping, two deficit lines). Those do not need another bundle-level review; they need a harmonization pass and then live use. Another cross-vendor challenge at this point would produce generic restatement of concerns already traceable at file:line in the three artifacts.
- [d:r:i] Reason a pre-implementation harmonization pass matters: without it, the first implementer will pick the fingerprint shape and the state-carrier name implicitly, and that pick will become the contract later slices inherit. Harmonizing eight lines up front is cheaper than deprecating the first implementer's implicit choices after they ship.

## How This Revised Bundle Should Be Inherited

### Carry Forward

- [d:r:i] The four-artifact family shape (`36` plan → `37` terrain → `38` placement → `39` workflow) as the standing pattern for composition-layer intervention families.
- [d:r:i] The two-layer per-surface framing in `37` (strongest carry, then thinner edge) as the default form for entry-surface maps.
- [d:r:i] The primary/supporting/non-owner triad in `38` as the standing placement grammar for every concern family, including the explicit non-owner column — that is what keeps `39`'s ownership boundary positive rather than reactive.
- [d:r:i] The full five-scenario uplift typology (vanilla / lightly aged / aged-bespoke / cross-runtime / upstream-template-drift) plus the mid-phase case from `37:49-76`, both now carried in the Scenario Map rather than only the Scattered section.
- [d:r:i] Installer re-run as its own Scenario Map primary owner at `37:56-58`, preserving the materialization chain from [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33-42](../../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33).
- [d:r:i] Per-phase `CONTEXT.md` as primary carrier for doctrine-vintage/rerun-boundary posture at `38:111-119`.
- [d:r:i] Tooling inventory carrier as primary for repo-local tooling install at `38:163-170`.
- [d:r:i] `.codex/config.toml` and `.codex/agents/*.toml` as primary runtime-side registry carriers at `38:147-153`, with wrappers as supporting.
- [d:r:i] Detect-only default opening posture in `39:57`.
- [d:r:i] Fingerprint/delta framing throughout `39` Detection Signals, with the two remaining deficit lines to be harmonized per revision §3.
- [d:r:i] Per-carrier install flags split into low-ambiguity additive routes and doctrine-sensitive proposal routes at `39:149-163`.
- [d:r:i] Claim-type reference install separated from claim-type activation at `39:160-162`.
- [d:r:i] Thin doctrine manifest promoted into first-slice output at `39:167-170` and `39:182-187`.
- [d:r:i] One read-only `progress` hook as first live routed consumer at `39:198-200`.
- [d:r:i] Self-scan gate on `UPLIFT-REPORT.md` at `39:227`.
- [d:r:i] The first-slice hold-out list (no full reinstall, no full migration, no cross-project batching, no workstream reconciliation, no aged-bespoke deep merge, no full audit-tree restructuring, no full upstream-template expression pass, no broad doctrine-sensitive wrapper rewrites by default) at `39:91-99`.
- [d:r:i] `gsd-uplift-project` as the working handle per `39:19-21`.

### Revise Before Carry

- [d:r:i] Add `mid-phase uplift` as a sixth classification in `39` §1 with detection signal and first-slice action per revision §1 above.
- [d:r:i] Add a per-carrier fingerprint-shape table in `39` so the manifest contract is concrete rather than `fingerprints or version stamps` interchangeably per revision §2.
- [d:r:i] Harmonize the two `older local doctrine version` lines in `39` §Detection Signals with the positive `fingerprint differs from current` form per revision §3.
- [d:r:i] Commit `38` §6 and `37` output-carrier references to `STATE.md uplift section` as primary and move `UPLIFT-STATE.md` to later-family option per revision §4.
- [d:r:i] Add installer-rerun posture as its own evidence source in `39` §2 per revision §5.
- [d:r:i] Name `UPLIFT-MANIFEST.json` as authoritative fingerprint source and `STATE.md` uplift section as narrative companion for the `progress` hook per revision §6.
- [d:r:i] Add audit-subtree aging to the first-slice hold-out list in `39` per revision §7.
- [d:r:i] Add one line declaring detect-only evidence sources in `39` §2 per revision §8.

### Hold For Later

- [d:r:i] Mid-phase routing mechanics inside `discuss-phase` (first slice classifies and routes; later family defines what the route does).
- [d:r:i] Aged-bespoke refresh of existing doctrine-sensitive content (root/planning `AGENTS.md`, root/planning `CLAUDE.md` wrappers).
- [d:r:i] Cross-runtime refresh touching registry and wrappers together.
- [d:r:i] Upstream-template-drift diff against shipped templates.
- [d:r:i] Audit-subtree aging machinery for doctrine-carrying subtrees.
- [d:r:i] Required-reading template seeding upstream.
- [d:r:i] Workstream parent↔child posture reconciliation.
- [d:r:i] Forensics and archived-milestone re-entry integration.
- [d:r:i] Routed-entry hooks in `resume-project`, `health`, `update`, `ingest-docs`, `new-milestone` beyond the first `progress` hook.
- [d:r:i] Aged-bespoke claim-type activation across existing load-bearing artifacts.
- [d:r:i] Rich doctrine-manifest content diffs with bespoke carve-out logic.

## Internal Coherence Notes

- [d:r:i] This reread judges the revised bundle against the current live surfaces (`.codex/get-shit-done/` workflows, `AGENTS.md`, `.planning/AGENTS.md`, `../../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md`) rather than against memory of the lane-02 bundle. Each `[e:c+i]` claim points at file:line in either the revised bundle or the live surface it routes to.
- [d:r:i] The revisions named above in §What Still Deserves Revision Before Implementation are narrower than the lane-02 revise-before-carry list; that is what the revision pass earned. The next move is harmonization plus implementation, not another bundle-level challenge.
- [d:r:i] Threshold-language and deficit-pseudo-positive bans from [AGENTS.md:53-56](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:53) and [.planning/AGENTS.md:117-124](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:117) shape this review's phrasing; where the bundle itself still carries residue (two detection lines, the `fingerprints or version stamps` phrase), this reread names the specific place and proposes a positive form.
