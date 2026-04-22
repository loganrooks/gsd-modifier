<purpose>
Review a concrete contract-changing slice against the upstream-pristine baseline, the repo-local delta layer, and the current propagation family so neighboring carriers either move in the same slice or stay explicitly held.
</purpose>

<required_reading>
@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md
Read the host repo's current propagation baseline pair when the invoking prompt or execution_context identifies it.
Read all files referenced by the invoking prompt's execution_context before starting.
</required_reading>

<supporting_reading>
Use these as the normal widening packet:
- the host repo's current propagation audit read surface
- the host repo's current typed propagation registry packet:
  - declared contracts
  - semantic map
  - evidence index
  - coverage and refresh
- the changed surfaces named in the invoking prompt or args
- the current local proposal, implementation, refresh, or disposition artifact for the active slice when one already exists
</supporting_reading>

<deeper_reading>
Only widen into older propagation lanes, long-horizon docs, or broader governance docs when the current slice cannot be judged from the baseline/delta pair plus the typed propagation layers.
</deeper_reading>

<process>

<step name="parse_args">
Treat all freeform args as the contract-change trigger.

Supported optional flags for the first slice:
- `--write-note PATH` — write the bounded propagation review to a repo-local markdown path
- `--strict-runtime` — require the runtime/install gate packet when the slice touches live materialization or registry carriers

If the invoking text does not name the changed surfaces directly, infer them from the active slice and state that inference explicitly.
</step>

<step name="map_the_slice">
State the trigger, then map the slice under these headings:

- trigger surfaces
- direct producers
- direct consumers
- narrative mirrors
- runtime and registry carriers
- durable outputs and state surfaces
- intentionally held neighbors

For each important carrier, say whether it belongs to:
- upstream-pristine baseline
- repo-local delta
- mixed baseline-plus-delta widening

Do not stop at the local file diff when the contract movement clearly crosses workflows, skills, wrappers, outputs, or governing docs.
</step>

<step name="choose_tools">
Use repo-local tooling only as partial visibility:

- `python3 harness_modifier/overlay/helpers/audit_refmap.py` when markdown-heavy topology changed
- `python3 harness_modifier/overlay/helpers/project_uplift.py detect . --json` when uplift outputs or routed consumers may move
- `python3 harness_modifier/contract/runtime_visibility.py .` when live-vs-overlay or materialized runtime carriers may move
- `python3 harness_modifier/contract/manifest_install_coherence.py . --snapshot <snapshot.json> --strict` when the slice crosses several materialization/runtime families together
- `python3 harness_modifier/contract/harness_canary.py report . --strict` when current runtime/install invariants are part of the live question

Do not let a clean tool result replace contextual reread. Tool output widens and sharpens the review; it does not finish it.
</step>

<step name="update_or_hold">
If the propagation path is already clear, update adjacent live carriers in the same slice.

If some neighbors stay held:
- name them explicitly
- state why they are held
- name the later route, proposal, or audit family that still owns them

Disposition bridge:
- when a partial tool flags a carrier and the route can move it now, say that explicitly under `Updated In This Slice`
- when a partial tool flags a carrier but the route is holding it, carry that under `Held With Explicit Boundary` with the specific reason
- when tools stay clean but contextual reread still sees a neighboring carrier that matters, keep that carrier explicit under `Held With Explicit Boundary` rather than letting the clean tool output silently erase it

Do not leave held boundaries ambient.
</step>

<step name="output_shape">
Produce a compact markdown review with these sections:

```markdown
# Propagation Review

## Trigger
- ...

## Baseline Versus Delta
- ...

## Producers
- ...

## Consumers
- ...

## Narrative Mirrors
- ...

## Runtime And Durable Carriers
- ...

## Updated In This Slice
- ...

## Held With Explicit Boundary
- ...

## Verification
- ...

## Next Route
- ...
```

If `--write-note PATH` is present, write the review there. Otherwise return it in the current response.

When a durable note is being written, prefer an existing lane home over an ad hoc new note path:
- `outputs/` when you are preserving an external/model return or a transparent composite of one
- `dispositions/` when you are recording local inheritance or judgment
- `*-change-triggered-refresh.md` when the note itself becomes a new propagation-baseline carrier

When the target path sits inside this audit workspace, preserve the local claim-type grammar instead of downgrading into untyped prose.
</step>

<step name="verification">
For overlay-backed workflow or skill changes in this repo:
- rerun `./scripts/setup-portable-gsd.sh`
- rerun the focused contract tests for the touched route
- keep `audit_refmap.py verify` and `git diff --check` in the batch boundary

If `--strict-runtime` is active or the slice touches live runtime/materialization carriers, include the runtime/install gate outputs in the verification section too.
</step>

</process>
