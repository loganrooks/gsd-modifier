Date: 2026-04-23
Status: revised after lane-05 audit

# Harness Modifier First Observation Carrier Proposal

## Role

- [d:r:i] This proposal defines the first durable observation carrier for responsible-closure work.
- [d:r:i] It is not a general telemetry system, not a cross-project signal database, and not a substitute for propagation or verification artifacts.

## Why This Carrier Exists

- [d:r:i] Responsible-closure lane `01` already fixed the first signal partition:
  - `deployment-context`
  - `expectation-vs-observation`
  - `semantic-deviation`
  - `positive-gain`
  - `measurement-provenance`
- [d:r:i] What is still missing is a modifier-owned carrier that can hold one host exercise or one deployability probe without degrading into:
  - prose-only narration
  - binary gate summary
  - breakage-only reporting

## Proposed Shape

### 1. Scope

- [d:r:i] One observation file per bounded host exercise or deployability probe.
- [d:r:i] Single-writer.
- [d:r:i] Written only by explicit operator-triggered workflow or helper.
- [d:r:i] Lives in the harness-modifier audit/governance space, not inside the exercised host project.

### 2. Required Top-Level Fields

- [d:r:i] `observation_id`
- [d:r:i] `carrier_version`
- [d:r:i] `provenance_schema`
- [d:r:i] `carrier_version` and `provenance_schema` move on different axes:
  - `carrier_version` changes when the observation-file shape changes
  - `provenance_schema` remains the governed split-provenance contract
- [d:r:i] `status`
  - initial expected vocabulary:
    - `recorded`
    - `reviewed`
    - `revised`
    - `superseded`
- [d:r:i] `automation_level`
  - initial expected value:
    - `1`
- [d:r:i] `observed_at`
- [d:r:i] `basis_commit`
- [d:r:i] `bundle_family`
  - first expected value:
    - `responsible-closure`
- [d:r:i] `exercise_id`
- [d:r:i] `target_host_class`
  - first-slice values are declared by the host-exercise packet and then referenced here
- [d:r:i] `evidence_family`
  - first expected vocabulary:
    - `runtime`
    - `derived`
    - `modifier`
- [d:r:i] `disposition`
- [d:r:i] optional `narrative_summary`
  - only as a terse in-record interpretive line when a reader genuinely needs one

### 3. Signal Families

- [d:r:i] `deployment_context`
  - compatibility declaration window and posture
  - runtime basis
  - overlay schema / uplift schema
  - parity baseline
  - target host description
- [d:r:i] `expectation_vs_observation`
  - what checks or reads were expected
  - what was actually observed
  - per-check `check_outcome`
  - whether the result was:
    - `accept`
    - `warn`
    - `refuse`
    - `shift-mode`
  - optional bounded `skip_reason` when a planned check is intentionally not run
  - `skip_reason` should bind to Reflect's canonical `automation_skip_reasons` vocabulary rather than an improvised per-run list
- [d:r:i] `semantic_deviation`
  - explicit discrepancy entries only
  - no flattening positive-gain into this family
  - recommended secondary classifier:
    - `config-mismatch`
    - `capability-gap`
    - `contract-mismatch`
    - `overlay-authority-drift`
    - `refmap-topology-drift`
    - `parity-classifier-drift`
  - distinction rule:
    - `config-mismatch` belongs to operator-side or declared-configuration mismatch
    - `contract-mismatch` belongs to declaration-versus-observed behavior mismatch
- [d:r:i] `positive_gain`
  - explicit gains only
  - examples:
    - stronger carry
    - clearer authority
    - more portable contract
    - more durable deployability evidence
  - recommended secondary classifier:
    - `carry-broadened`
    - `authority-clarified`
    - `portability-broadened`
    - `verification-surface-sharpened`
- [d:r:i] `measurement_provenance`
  - `detected_by`
  - `written_by`
  - `about_work`
  - optional run/session references when available
- [g:r:i] `detected_by` and `written_by` must remain distinct objects even when they resolve to the same runtime facts.

### 4. Provenance Rule

- [d:r:i] Split provenance should follow the Reflect-inspired `detected_by` / `written_by` distinction rather than flattening everything into one runtime echo.
- [d:r:i] `provenance_schema` should open at `v2_split`.
- [d:r:i] Missing facts should resolve to `not_available`, not invention.
- [d:r:i] Flat echoes, if any, should be compatibility echoes only and not the sovereign contract.

### 5. Review And Lifecycle Rule

- [d:r:i] This first slice should not import a full lifecycle state machine.
- [d:r:i] The minimal stronger carry is:
  - durable observation file
  - disposition verb on later review
  - ability to supersede with a later observation
- [d:r:i] Anything richer than that remains explicitly later.

## Recommended Physical Form

- [g:r:i] First slice should be JSON-only.
- [d:r:i] If a one-line human-readable interpretation is genuinely needed, keep it inside the typed record as `narrative_summary` rather than opening a second mirror artifact.

## Reference Absorption

- [d:r:i] Shapes worth absorbing from GSD Reflect:
  - split provenance
  - secondary signal-taxonomy discipline for discrepancy/gain rows
  - canonical `automation_skip_reasons` vocabulary where it materially improves comparison
  - rigor-over-cap posture
- [d:r:i] Shapes to avoid importing in this first slice:
  - automatic collection
  - background sensor daemons
  - synthesizer / reflector agents
  - cross-project KB aggregation
  - lifecycle state machine
  - per-phase caps

## Explicitly Later

- [d:r:i] automation level escalation beyond operator-triggered writes
- [d:r:i] aggregated observation index
- [d:r:i] `durability` ladder
- [d:r:i] recurrence counters
- [d:r:i] severity fields such as `severity_level` and `severity_conflict`
- [d:r:i] cross-project storage
- [d:r:i] reflective synthesis workflows

## Exact Next Move

1. [d:r:i] Treat responsible-closure lane `05` as the completed audit over this carrier plus `172` and `174`.
2. [d:r:i] Keep this carrier JSON-only with the optional in-record `narrative_summary`.
3. [d:r:i] Keep `174` as the owner of exercise vocabulary and packet-side scope.
4. [d:r:i] Open the observation-carrier writer as the first responsible-closure implementation slice.
