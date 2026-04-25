# AGENTS.md

## Scope

This repo is the standalone home for `gsd-modifier`.

- treat this repo as the modifier project, not as a host product repo
- do not import `prix-guesser` product-planning horizons as if they govern this repo
- use [WORKFLOW.md](WORKFLOW.md) and [docs/development.md](docs/development.md) as the primary operator surfaces

## Source Of Truth

- shipped/runtime-facing surfaces:
  - `harness_modifier/`
  - `tooling/portable-gsd/overlay/`
  - `scripts/setup-portable-gsd.sh`
  - `scripts/setup-portable-gsd-runtime.sh`
- development-support surfaces:
  - `tooling/codex/`
  - `tooling/codex/tests/`
- migration/provenance carry:
  - [docs/migration-origin.md](docs/migration-origin.md)
- carried origin audit dossier:
  - [docs/origin-audit](docs/origin-audit)

## Live Control Surface

- treat [docs/handoff/current.md](docs/handoff/current.md), [.planning/CURRENT-STATE.md](.planning/CURRENT-STATE.md), and [.planning/STATUS.md](.planning/STATUS.md) as the live operational state for current boundary, accepted direction, and next move
- treat [docs/install-profiles.md](docs/install-profiles.md) plus task-relevant measurement or audit artifacts as the active runtime/install claim surface
- do not treat generated runtime output or carried origin context as authority when it diverges from the live source and handoff surfaces

## Working Rules

- treat bootstrap and verification as load-bearing; do not change runtime/install surfaces without checking neighboring tests and scripts
- keep portability in view: source files should use `__PROJECT_ROOT__` placeholders where the materialization contract expects them
- keep the distinction explicit between:
  - shipped/runtime surfaces
  - development-program-only helpers
  - carried origin-audit context
- keep install-profile claims disciplined:
  - `codex-core` and `claude-core` are the active core profiles
  - parity means shared core outcomes, not identical wrapper/config files
  - `dual-runtime-core` is now active at the repo-self proof layer; keep the synthetic host matrix green before widening broader host/support language
- prefer changes that keep the extracted repo executable and auditable on its own, not ones that quietly depend on the old host repo

## Workflow Rules

- when the user invokes a repo-defined workflow, script, skill, or operator surface, follow that workflow for real rather than implementing first and backfilling artifacts later
- for ambiguous, architectural, policy-bearing, or contract-carrying changes, do not edit files or commit until the proposed change has been explained and the user gives explicit approval
- before seeking approval for those changes, state:
  - the observed problem
  - the proposed change
  - why that change is appropriate
  - alternatives considered
  - the expected write set
  - the verification plan
- read-only investigation is allowed before approval when needed to ground the proposal
- small mechanical fixes may proceed only when the user's request is already explicit and the change is low-risk
- if the user challenges the premise of a change, pause implementation and reconcile the premise before touching files
- if a task needs a proposal, audit, checkpoint, or measurement artifact to stay reviewable, create or update it in the same slice instead of leaving the reasoning in chat only
- when a non-trivial decision is made, capture a concise local explanation of the decision basis where later reviewers will actually look: proposal, audit artifact, handoff, review note, or commit message as appropriate
- if you must deviate from the normal workflow, state the deviation plainly and record the boundary in a repo artifact when it matters downstream
- do not silently flatten:
  - source edits vs materialized-runtime verification
  - observed state vs inferred explanation
  - planned work vs improvised repair
  - accepted boundary vs ambient untracked follow-up

## Contract Propagation

- when a change touches a contract-carrying surface such as a workflow, script, manifest, overlay file, contract checker, runtime adapter, or governing doc, do not stop at the local diff
- identify the direct producers, direct consumers, runtime carriers, narrative mirrors, and durable outputs that should stay aligned with that change
- update adjacent carriers in the same slice when the propagation path is already clear; if some neighbors are intentionally held, record that boundary explicitly instead of leaving it implicit
- use repo-local propagation and contract tools where they fit:
  - `python3 tooling/codex/audit_refmap.py`
  - `python3 harness_modifier/contract/portable_gsd_contract.py`
  - `python3 harness_modifier/contract/runtime_visibility.py`
  - `python3 harness_modifier/contract/manifest_install_coherence.py`
  - `python3 harness_modifier/contract/harness_canary.py`
- prefer the repo's contract and matrix tools over ad hoc rereads of generated runtime output when the question is whether materialized behavior still matches source intent

## Auditability And Review

- assume substantive work may later be audited by expert senior software engineers and external AI reviewers
- produce code, docs, plans, and rationale that can survive adversarial rereading without hidden chat context, implied intent, or hand-wavy summaries
- transparency here means concise decision rationale, evidence, tradeoffs, and uncertainty, not a verbatim dump of private chain-of-thought
- write decision explanations so a careful future maintainer can follow the basis of the change even if they are not already expert in software engineering or AI harness design
- make reviewable distinctions explicit:
  - observed state vs inference
  - decision vs open question
  - source verification vs materialized-runtime verification
  - durable artifact vs disposable byproduct
- when recording a meaningful decision, prefer to capture:
  - what was decided
  - why this option was chosen now
  - what nearby alternatives were rejected, deferred, or held
  - what evidence, constraint, or verification result drove the choice
  - what uncertainty or follow-up remains
- when domain-specific language is unavoidable, define it briefly or point to the file that carries the fuller explanation instead of assuming the reader already knows the term
- leave reconstructable audit trails:
  - clean commit boundaries
  - explicit verification commands
  - explicit review or disposition notes for delegated work
  - durable artifacts when a boundary, exception, or propagation decision matters
- if something is intentionally not propagated, not verified, or left parked for later, record that fact explicitly so later failure forensics and cross-vendor review do not have to infer it from silence

## Delegation And Review

- before delegating substantial bounded work, establish a clean task boundary and make the owned files or artifact surface explicit
- do not delegate new substantial edits into an unresolved mixed worktree
- after delegated work returns, review it and disposition it explicitly as `accept`, `revise`, `park`, or `reject` before integrating or committing it
- do not use delegation performatively after the critical work is already done

## Commit Hygiene

- keep commits scoped to one coherent change
- use Conventional Commit subjects for every commit:
  - format: `<type>(<scope>): <imperative summary>`
  - common types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `build`, `ci`
  - scope should name the affected subsystem or artifact family, for example `audit-refmap`, `origin-audit`, `planning`, `portable-gsd`, `contracts`, or `model-benchmark`
  - avoid subject-only bucket labels such as `Import origin audit into planning`; write the actual type, scope, and action instead
- write commit messages and adjacent artifacts so a later reviewer can tell both what changed and why it changed
- for substantive commits, include a body with concise `Why`, `Verification`, and `Boundary` notes unless the change is truly trivial
- prefer separate commits for:
  - shipped/runtime or overlay behavior changes
  - contract or verification-tool changes
  - docs, handoff, or planning-state updates
  - generated measurement, audit, or provenance artifacts
- do not bundle source fixes, generated drift, and governance or audit artifacts into one commit unless they are truly inseparable
- if the worktree is already mixed, stabilize it into explicit buckets before committing and keep durable audit or measurement artifacts unless they are clearly disposable byproducts
- when verification is performed against a materialized runtime rather than source alone, record that distinction explicitly
- prefer additive follow-up commits for important missed artifacts over cleanup-by-deletion unless the user explicitly asks for deletion or history rewrite

## Verification

Default verification stack for substantive changes:
- `python3 -m py_compile ...`
- `python3 -m unittest ...`
- `./scripts/setup-portable-gsd-runtime.sh --runtime both`
- `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict`
- `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict`
- `git diff --check`

Canonical CI scripts:
- `bash scripts/ci/check-deterministic.sh`
- `bash scripts/ci/check-bootstrap.sh`

If you change bootstrap/governance docs:
- `python3 tooling/codex/audit_refmap.py verify .`
- `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines ...` where relevant
