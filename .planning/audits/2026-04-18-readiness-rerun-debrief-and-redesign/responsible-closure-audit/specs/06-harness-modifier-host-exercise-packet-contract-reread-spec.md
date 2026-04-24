Date: 2026-04-23
Status: prepared spec

# Harness Modifier Host-Exercise Packet Contract Reread Spec

## Governing Question

- [g:r:i] After the landed `176` packet-contract slice, what is the sharpest judgment on packet ownership, first-host boundary enforcement, and observation handoff, and is the next bounded move now the actual observe-only host exercise or one more narrower refinement?

## Review Tasks

1. [d:r:i] Judge whether `176` now makes `174` real packet-side ownership rather than only prose ownership.
2. [d:r:i] Judge whether the packet layer now cleanly owns the shared exercise vocabulary:
   - `target_host_class`
   - `check_outcome`
   - `skip_reason`
3. [d:r:i] Judge whether the first-host boundary is enforced strongly enough for the current slice:
   - disjoint host
   - regular GSD already installed
   - no Reflect artifacts
   - clean worktree
   - known basis commit
4. [d:r:i] Judge whether the observation-writer handoff is now cleaner or whether the packet/observation split still leaves ambiguous ownership.
5. [d:r:i] Keep the sequence explicit against:
   - actual observe-only host run still later unless earned here
   - `167` remaining explicit and sequential
   - no broader parity or deployment widening

## Avoid

- [d:r:i] ship-gate framing
- [d:r:i] broader telemetry-system appetite
- [d:r:i] mixed-host or Reflect-host widening
- [d:r:i] actual host-run design overreach unless it is directly required by the packet judgment

## Required Output Sections

1. `Packet Contract Judgment`
2. `Observation Handoff Judgment`
3. `Boundary Enforcement Judgment`
4. `What Moves Now`
5. `What Remains Explicitly Later`
6. `Exact Next Moves`

## Output Constraints

- [d:r:i] Be concrete about ownership, sequence, and boundary enforcement.
- [d:r:i] Prefer narrower stronger carry over blended ambition.
- [d:r:i] If the current packet slice still needs one more refinement before the host run, say that directly and name the smallest such refinement.
