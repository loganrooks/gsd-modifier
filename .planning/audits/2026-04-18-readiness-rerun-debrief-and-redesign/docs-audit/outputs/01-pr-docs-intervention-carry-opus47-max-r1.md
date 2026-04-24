# PR Docs Intervention Carry — Opus 4.7 Max R1

Lane: `docs-audit/pr-docs-intervention-carry`
Spec: [../specs/01-pr-docs-intervention-carry-spec.md](../specs/01-pr-docs-intervention-carry-spec.md)
Packet: [../packets/01-pr-docs-intervention-carry-packet.md](../packets/01-pr-docs-intervention-carry-packet.md)
PR snapshot: `docs/pr4-consistency-drift-guards-r2` at `4f3de809`, pinned to upstream `v1.36.0`
Date: 2026-04-20

## 1. Overall Carry Judgment

- The submitted docs PR is a real contributor-orientation artifact: it converts upstream docs from loose prose into a roster-first, parity-guarded governance surface. That is the reusable pattern.
- It is a weak intervention-planning artifact for this repo: it describes upstream declared surfaces without speaking to effective repo-local runtime, mutation chains, or leverage ranking. The HARNESS-INTERVENTION-ONBOARDING layer the repo already drafted carries the intervention-planning load, not this PR.
- The governing asymmetry is not "how clear is the doc"; it is which authority the doc describes. The PR describes declared authority over the upstream source tree. Effective authority over this repo's behavior sits at `tooling/portable-gsd/overlay/`, `scripts/setup-portable-gsd.sh`, `.codex/agents/*.toml`, and `.codex/get-shit-done/bin/lib/*.cjs` — none of which the PR touches or indexes.
- Contributor/reference carry and intervention-planning carry must therefore be kept explicitly apart. Averaging them hides the asymmetry and produces an overstated verdict.

## 2. Load-Bearing Gains

Contributor/reference carry (strong):

- Inventory-first governance posture. INVENTORY.md declares the filesystem authoritative when the broad docs diverge, names the drift-guard tests (`tests/inventory-counts.test.cjs`, `tests/commands-doc-parity.test.cjs`, `tests/agents-doc-parity.test.cjs`, `tests/cli-modules-doc-parity.test.cjs`, `tests/hooks-doc-parity.test.cjs`, `tests/architecture-counts.test.cjs`, `tests/command-count-sync.test.cjs`) as mechanical enforcers, and fixes the write-order "new surfaces land in inventory first, then propagate outward" (`upstream-docs-pr-r2/docs/INVENTORY.md.txt:3-9`).
- Six-family enumeration with counts. Agents (31), commands (75), workflows (72), references (41), CLI modules (24), hooks (11) get structured tables with roles and source links rather than narrative lists (`INVENTORY.md.txt:13,55,166,249,322,357`).
- Architecture as a layered system stack. ARCHITECTURE.md exposes command → workflow → agent → CLI-tools → filesystem rather than a wrappers-first picture, and names installer, hooks, and CLI modules as first-class layers with counts and responsibilities (`ARCHITECTURE.md.txt:22-66,107,118,130,203,223-247`).
- Command and agent reference surfaces. COMMANDS.md gives flags, arguments, produces, prerequisites, and worked examples per command (`COMMANDS.md.txt:15-207,381-445,819-873,1065-1131`). AGENTS.md gives role cards, spawner, parallelism, tool permissions, model tier, and produced artifacts for 21 primary agents plus stubs for 10 advanced agents, with least-privilege call-out (`AGENTS.md.txt:33-470,473-675,677-710`).
- Explicit deferral from narrative docs to inventory. Both ARCHITECTURE.md and AGENTS.md route final-count truth back to INVENTORY.md rather than asserting it locally (`ARCHITECTURE.md.txt:141,221,225,277`; `AGENTS.md.txt:3,13,475,679`). This is the governance pattern that most deserves reuse.

Intervention-planning carry (narrow, mostly indirect):

- Parity-test pattern as transplantable governance. The drift-guard list above is the strongest reusable move the PR offers as a mechanism for any local doc layer that wants mechanical enforcement over assertion.
- Stack decomposition as a starting frame. The layered diagram at `ARCHITECTURE.md.txt:31-66` gives a shared vocabulary the repo-local intervention docs can reuse when naming surface families — without taking the narrative as a runtime map.

## 3. Blind Spots And Flattenings

- No repo-local composition surface. The PR has nothing on the install-plus-overlay composition that produces this repo's `.codex/`: upstream install → `tooling/portable-gsd/overlay/` copy → post-copy mutation in `scripts/setup-portable-gsd.sh`. The installer section in ARCHITECTURE.md (`ARCHITECTURE.md.txt:494-522`) describes the upstream installer but not the local three-stage chain that actually materializes runtime truth in this repo.
- Agent `.toml` plane hidden behind the `.md` role cards. AGENTS.md frames the `agents/*.md` file as the agent definition and implies the `.md` is what runtime spawns. In Codex runtime the spawned worker authority is `.codex/agents/*.toml` — the `.md` companion is not the effective authority. Reading the PR does not expose this.
- Runtime helper layer flattened. `.codex/get-shit-done/bin/lib/*.cjs` carries live routing and state semantics (HARNESS-INTERVENTION-ONBOARDING.md:27,29; checkpoint-5-gsd-local-topology-schema.md:185,200 as cited in the update lane). The PR's CLI Modules table enumerates module responsibilities (`INVENTORY.md.txt:326-351`) but treats them as documentation targets, not as intervention surfaces whose edits mutate behavior.
- Inventory is v1.36.0-pinned and already trailing. The PR self-declares the v1.36.0 pin and instructs operators to run `ls | wc -l` for live counts (`INVENTORY.md.txt:7`). Current upstream INVENTORY.md on `get-shit-done-upstream` reports 33 agents, 82 commands, 79 workflows, 49 references, plus new surfaces (`plan-review-convergence`, `ultraplan-phase`, `spike`, `sketch`, `ingest-docs`, `sketch-wrap-up`, `spike-wrap-up`, `mandatory-initial-read`, two additional `gsd-doc-*` advanced agents), and new references including `debugger-philosophy.md`, `mandatory-initial-read.md`, `project-skills-discovery.md`, `doc-conflict-engine.md`, plus the sketch reference cluster (`get-shit-done-upstream/docs/INVENTORY.md:13,57,74-77,175,213,247,265-323`). The PR's stated counts are stale by two shipped releases against active repo-local runtime (`v1.38.1`, per HARNESS-INTERVENTION-UPDATE-LANE.md:37-38).
- Manifest coherence not recognized as tooling debt. The PR has no line on the `gsd-file-manifest.json` hash-vs-filesystem drift documented in HARNESS-INTERVENTION-UPDATE-LANE.md:40-42. A reader of the PR docs alone will treat the manifest as authoritative; the isolated probe already found it is not.
- Intervention ranking absent. The enumerations are flat. Nothing in the PR names which surfaces carry the highest blast radius, which are pure reference, or which are effective-authority mutation points. Ranking sits in the repo-local intervention onboarding doc, not the PR.
- Spec-phase, ingest-docs, mandatory-initial-read, and thinking-partner-style surfaces either pinned-out or unranked. The PR pin excludes `spec-phase` and `ingest-docs` as contributor surfaces, and does not rank `mandatory-initial-read` as an inheritance-contract surface. The repo already treats all three as live intervention surfaces (HARNESS-INTERVENTION-ONBOARDING.md:56-59).
- Declared/effective split absent from the narrative. ARCHITECTURE.md frames one system stack. It does not acknowledge that upstream docs are not the same object as tracked-overlay canon, installer post-pass, live runtime, agent `.toml` surfaces, or `.planning/` artifacts.

## 4. Declared Versus Effective Authority Register

Register entries scope the PR's declared authority claims against the effective authority in this repo-local context today (`v1.38.1` runtime).

| Surface family | Declared authority per PR docs | Effective authority in this repo | Delta that matters for intervention |
|---|---|---|---|
| `docs/INVENTORY.md` in upstream | Sovereign when broad docs differ; CI-enforced via named parity tests | Binds upstream source tree only; does not extend to `tooling/portable-gsd/overlay/` or `.codex/` runtime in this repo | The parity governance pattern is reusable; the specific file is not an authority over local runtime |
| `docs/ARCHITECTURE.md` counts (75/72/31) | Pinned to `v1.36.0`, deferred to INVENTORY for final-count truth | Local runtime is `v1.38.1`; upstream now ships 82/79/33 | Declared counts already mis-describe both the upstream and the local runtime |
| `docs/AGENTS.md` role cards | `agents/*.md` is authoritative; least-privilege table covers 21 primary agents | `.codex/agents/*.toml` is the spawned-worker authority; `.md` is a companion surface in Codex runtime | The PR's declared agent object is not the effective worker object; this is a load-bearing mis-framing for intervention |
| `docs/COMMANDS.md` flags/args | Command `.md` files as the user-facing contract | Codex install transcodes command files into skills + TOML; the runtime dispatch path is the installer + runtime helper chain, not the static `.md` | Declared and effective diverge through installer translation; flags can appear in docs without being wired in a given runtime and vice versa |
| Inventory-count and doc-parity tests | Drift fails CI in the upstream repo | No mirror exists in this repo for overlay, `.codex/`, or agent `.toml`; upstream tests do not bind the local install-plus-overlay composition | Governance intent does not extend to where it is needed most for intervention |
| Install flow described in ARCHITECTURE.md "Installer Architecture" | Single-stage upstream installer with runtime adaptation | Repo-local path is three-stage: upstream install → overlay copy → post-copy mutation via `scripts/setup-portable-gsd.sh` | The declared install story is incomplete for this repo; the mutation surface is invisible in the PR |
| `gsd-file-manifest.json` | Manifest tracked for clean uninstall (`ARCHITECTURE.md.txt:515`) | Active-repo manifest carries hashes that do not match on-disk content after overlay/patched-carry is reapplied | Declared-as-tracking conflicts with effective-as-unreliable; the PR invites trust that the probe has already withdrawn |
| `.codex/get-shit-done/bin/lib/*.cjs` helpers | Enumerated as "CLI Modules" with per-module responsibilities in INVENTORY.md | Carry live routing/state semantics; a single-line description is not a behavioral contract | Declared as documentation target; effective as behavior-mutating surface; the PR does not connect the two |
| `.planning/` file tree (`ARCHITECTURE.md.txt:442-490`) | Read/write target for workflows; inspectable state | Local runtime also carries audits/reviews that are review-only, not runtime canon | The PR's "state layer" framing does not distinguish runtime canon from review artifacts; a modifier treating all `.planning/*` as equally load-bearing will mis-prioritize |

Two principles that fall out of the register:

- The PR declares authority over a surface set that is strictly upstream-source-scoped. Effective authority in this repo is the composition of upstream, overlay, installer post-pass, runtime helpers, and agent `.toml` — a strict superset the PR does not name.
- The PR's most generalizable governance move (inventory-first + parity tests) is a mechanism, not a truth set. Importing the mechanism into repo-local tooling is strictly more valuable than importing the literal docs.

## 5. Intervention-Leverage Implications

- Intervention-leverage ranking must live outside the PR docs. The PR enumerates six families evenly; leverage is not evenly distributed. The existing repo-local ranking (agent `.toml` alignment, launch-truth capture, manifest/install coherence, live-vs-overlay drift visibility — HARNESS-INTERVENTION-ONBOARDING.md:71-74) is the object the PR is silent on.
- Reading the PR alone under-equips a modifier. A contributor reading these docs can map the roster but will not know whether editing `docs/AGENTS.md`, the companion `.md` file, the `.toml`, the overlay, the installer, or the runtime copy will change spawned-worker behavior — a question that decides where intervention work must land.
- Inheriting the parity-guard discipline, not the inventory file, is the high-leverage move. Local parity guards over overlay hashes, `.codex/` state, agent `.toml` rosters, and manifest coherence would give this repo the mechanical drift control the PR gave upstream.
- Treating the PR snapshot as a baseline for comparison rather than a truth source preserves its contribution. Using it as a runtime reference sets intervention planning up to mis-target surfaces that have already moved.
- The PR snapshot cannot be refreshed to close this gap by more docs writing alone. The missing object is a repo-local layer that holds declared/effective, materialization chain, and leverage ranking. That layer is companion, not replacement.

## 6. What Should Stay Stable

- `docs/INVENTORY.md` roster structure: six-family enumeration with source links and drift-guard names. Useful because it holds the "does this surface exist" question in one place.
- `docs/ARCHITECTURE.md` stack diagram and layer names. Useful because it gives a shared vocabulary even when the runtime picture is more composite.
- `docs/COMMANDS.md` flag/argument reference cards. Useful because flag-and-example reference material is exactly the stable surface contributors need.
- `docs/AGENTS.md` role cards + least-privilege tool table. Useful because the privilege pattern is a real contract even though the declared object is the `.md` companion.
- Inventory-first + parity-test pattern. Useful because it is the reusable governance mechanism the PR most deserves to be remembered for.

None of these should be loaded up with intervention content. Every attempt to stuff leverage ranking, materialization narrative, or effective-authority annotations into the existing broad docs weakens them as stable reference and weakens the intervention layer by camouflaging it inside prose.

## 7. What Needs A Paired Intervention Layer

- Declared/effective authority map per surface family. Table form, one row per surface, one column each for declared and effective authority with a named delta. The register in Section 4 is a prototype; the companion layer should own the durable version.
- Runtime materialization chain reference. Explicit documentation of upstream install → overlay copy → post-copy mutation → live `.codex/` → `.planning/` outputs, naming which step mutates what.
- Intervention-leverage ranking. Per-surface tier: primary-intervention, secondary target, review/control-only. Consumed before any change is scoped.
- Agent authority layer. Explicit mapping of `.codex/agents/*.toml` ↔ `agents/*.md` companions, naming which is spawn-authoritative in each runtime and how to detect drift between them.
- Launch-truth capture protocol. Written mechanism for capturing spawn/review-boundary truth at agent launch time (currently protocol-heavy via `state_5.sqlite` per HARNESS-INTERVENTION-ONBOARDING.md:51).
- Manifest/overlay coherence debt note. Documented fact that `gsd-file-manifest.json` hashes do not match on-disk after overlay re-application, with a rule that says manifest is not runtime truth until the mechanism is fixed.
- Stable-versus-transform register (below) as an explicit two-column catalogue.

Stable-versus-transform register:

| Object | Stable reference | Needs transform / companion |
|---|---|---|
| `docs/INVENTORY.md` roster | keep as upstream surface roster | companion local inventory for overlay, `.codex/`, agent `.toml`, installer post-pass |
| `docs/ARCHITECTURE.md` stack narrative | keep as shared vocabulary | companion `RUNTIME-MATERIALIZATION.md` for the actual three-stage local chain |
| `docs/AGENTS.md` role cards | keep as contributor reference | companion `AGENT-AUTHORITY.md` distinguishing `.toml` spawn authority from `.md` companions |
| `docs/COMMANDS.md` flag reference | keep as user-facing reference | companion surface-mutation ledger for commands whose runtime translation changes at install time |
| Parity-test pattern | keep; extend | extend with repo-local parity guards over overlay, manifest, agent `.toml`, `.codex/` roster |
| `gsd-file-manifest.json` | do not treat as runtime truth | tooling-debt note + replacement mechanism for coherence |
| Install-plus-overlay composition | not currently documented in stable reference at all | new intervention doc owns this |
| Leverage ranking per surface | do not embed in stable reference | companion intervention layer owns ranking |

## 8. Stronger Forms Considered

The instinct to say "the docs already carry this strongly enough" was tested against the following stronger forms. Each is recorded with an explicit adopt/modify/hold/reject verdict.

Stronger forms considered register:

| # | Alternative / companion form | Verdict | Rationale |
|---|---|---|---|
| 1 | Build a repo-local `INTERVENTION-MAP.md` companion document that cites the PR inventory but adds a declared/effective split, materialization chain, and leverage ranking per surface | Adopt at repo-local scope; not upstream | The intervention-planning object the PR cannot be turned into. Keeping it local protects the PR's stable-reference role and lets the map grow independently of upstream release cadence. |
| 2 | Rewrite ARCHITECTURE.md upstream into two views — a contributor view and an intervention view | Reject | Breaks the stable-reference role, couples intervention cadence to upstream release cadence, and assumes upstream readers share the repo-local intervention priorities. Equivalent of averaging contributor and intervention carry into one blurred object. |
| 3 | Add a new reference `get-shit-done/references/runtime-materialization.md` upstream | Hold | The artifact is right in principle but premature upstream; repo-local materialization is not symmetric across runtimes. Promote to upstream only after a repo-local version proves the shape and naming. |
| 4 | Extend `docs/INVENTORY.md` upstream with a leverage-tier column | Reject | Leverage is project-specific — overlay extent, patch discipline, install composition differ per consumer. A hardcoded tier in upstream docs would mis-rank surfaces for consumers without overlays. A sidecar annotation is the correct shape, not an inline column. |
| 5 | Port the PR's drift-guard test pattern into repo-local tooling — parity guards over overlay hashes, manifest coherence, `.codex/` roster, agent `.toml` registration | Adopt | Highest-yield reuse of the PR pattern. Converts the governance intent into a mechanical enforcer where intervention most needs it. |
| 6 | Build a `SURFACE-MUTATION-LEDGER.md` that records, per surface, which layer's edits change runtime behavior (declared-only, transcoded-at-install, mutated-by-post-pass, drift-on-overlay-reapply) | Adopt | Directly addresses the "where does editing this change behavior?" question the PR leaves unanswered. Small enough to co-live with the intervention-onboarding doc. |
| 7 | Split the intervention layer into per-family runbooks (`RUNBOOK-agent-toml-alignment.md`, `RUNBOOK-launch-truth-capture.md`, `RUNBOOK-manifest-coherence.md`, `RUNBOOK-overlay-drift.md`) | Adopt partially | Runbooks are the right shape once a family crystallizes. Before that, writing a runbook can over-freeze scope. Defer until each family has at least one bounded proposal. |
| 8 | Fold the intervention layer into CLAUDE.md or AGENTS.md | Reject | Overloads runtime-consumed docs with strategy content, invites silent drift between stable reference and intervention map, and ignores that this layer is for the repo maintainer, not for agents at runtime. |

Counted "stronger forms considered": 8. Adoptions/partial adoptions: 4 (#1, #5, #6, #7). Holds: 1 (#3). Rejections: 3 (#2, #4, #8).

## 9. Recommended Next Moves

- Keep the PR corpus as a governance foundation and a stable contributor reference. Do not absorb it as runtime truth and do not treat it as the missing intervention layer.
- Treat the PR's parity-test pattern as the primary reusable asset. Port it into repo-local tooling by defining drift guards over overlay hashes, `.codex/` roster, agent `.toml` registration, and `gsd-file-manifest.json` coherence. This is the highest-leverage move the PR makes available.
- Hold the existing HARNESS-INTERVENTION-ONBOARDING and HARNESS-INTERVENTION-UPDATE-LANE documents as the companion intervention layer. Extend them rather than merging them into the PR-style docs corpus.
- Add a thin repo-local `RUNTIME-MATERIALIZATION.md` that names the install-plus-overlay three-stage chain and cites the installer script and overlay directory explicitly. Reference it from the existing intervention docs.
- Record the manifest-coherence finding as tooling debt with a named owner and a rule that says manifest hashes are not runtime truth until the mechanism is repaired.
- Keep the PR snapshot as a comparison baseline for future runtime audits, not a runtime reference. Re-run comparisons against live upstream and live `.codex/` when planning any subsequent intervention.
- When any intervention family crystallizes (agent `.toml` alignment, launch-truth capture, manifest coherence, overlay drift), promote it into a bounded per-family runbook rather than expanding the broad intervention-onboarding doc indefinitely.
- Do not push repo-local intervention ranking upstream. Consumers of upstream GSD without overlays or patched carry have different leverage curves; pushing a tier column into `docs/INVENTORY.md` would mis-rank their surfaces.
