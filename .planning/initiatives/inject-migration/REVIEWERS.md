# Reviewer Agents

Reviewer agents replace the operator at all formerly operator-gated checkpoints in this initiative. They are spawned by the main loop, return a structured verdict, and their decisions are logged. The operator audits decisions post-hoc, not synchronously.

The operator is involved only at:

1. Initial `/goal` invocation (the GO signal)
2. `/goal clear` or Ctrl+C (manual interrupt)
3. Hard-stop conditions (5 only — see [GUARDRAILS.md](GUARDRAILS.md))
4. Final retrospective review after `Sentinel: INITIATIVE-COMPLETE`

Everything else flows through reviewers.

## Reviewer Roster

### `adversarial-auditor-xhigh` — architectural critic

Grounded register-focused critique of plan-level artifacts at extended reasoning effort. Reads the artifact, the cited goals, and the relevant working rules. Returns a critique grounded in stated obligations rather than hostile-for-hostile-sake.

**Invoked at**:

- Phase 1 ADR-001 review (manifest schema v4)
- Phase 2 contract code review (pre-merge)
- Phase 3 pilot result review (proof-of-mechanism check)
- Phase 6 first new-operation-kind exercise review
- Phase 9 ADR-002 (codex skill mirror direction)
- Every phase debrief (before phase marked `[x]`)
- Premise-change suspicion (orientation or intervention-strategies premise may have shifted)
- Phase 10 closeout retrospective

### `trajectory-verifier` — goal-backward verifier

Verifies that work delivered what was promised, by reading the trajectory plan + the active phase under verification. Built for trajectory plans (no GSD orchestrator scaffolding required) — fits this initiative's `phases/<NN>-<slug>.md` shape.

**Invoked at**:

- Phase-boundary verification (after last slice of a phase commits, before marking phase complete)
- Initiative-level verification (Phase 10 slice 1, before sentinel transition to `INITIATIVE-COMPLETE`)

### `gsd-debugger` — recovery investigator

Investigates verification gate failures using scientific method. Proposes a root-cause hypothesis and a fix.

**Invoked at**:

- Verification gate fails on the slice's first retry
- Unrelated test regression detected
- Verification tooling itself errors (rare)

### `Explore` — read-only triangulator

Search-and-cite agent. Confirms or refutes a factual claim by reading code/docs.

**Invoked at**:

- Subagent contradiction (second-pair-of-eyes verification of a contested claim)
- Anchor-presence checks (does the slice spec's anchor actually exist in the upstream file?)
- Premise-evidence triangulation (does this evidence really invalidate the premise?)

### `Plan` agent — ambiguity disambiguator

Plans an approach when slice spec is genuinely ambiguous. Returns a plan + critical files.

**Invoked at**:

- Slice ambiguity that prevents safe single-interpretation execution
- Surface-change requests (a write outside declared write set may be justified — Plan reviews and recommends scope)

## Verdict Format

Every reviewer must return its verdict in this exact JSON-in-markdown shape (parsable by the main agent):

```text
VERDICT: <PASS | FAIL | ESCALATE | HALT>
REASONING: <one paragraph; what the reviewer evaluated and why it landed on this verdict>
RECOMMENDATION: <if PASS: empty or "proceed". if FAIL: actionable next step. if ESCALATE: what second reviewer to invoke and why. if HALT: which hard-stop condition fires.>
EVIDENCE: <bullets of cited file:line refs, commit SHAs, tool outputs the reviewer used to ground its verdict>
```

The main agent parses this verdict block from the reviewer's tool-result message. If the reviewer's output cannot be parsed (malformed verdict block), the main agent treats it as ESCALATE and triangulates.

## Verdict Semantics

| Verdict | Main Agent's Next Step |
|---|---|
| **PASS** | Proceed with the action under review. Log to STATE.md Reviewer Decisions Log. |
| **FAIL** | Do not proceed. Apply the reviewer's RECOMMENDATION if actionable (e.g., re-execute slice with adjustment); if the recommendation requires writing outside the slice's declared write set, treat as ESCALATE. |
| **ESCALATE** | Spawn a second reviewer of a different type, passing the first reviewer's verdict as context. Take the majority verdict. If still split, hard-stop with `HARD-STOP: reviewer-deadlock`. |
| **HALT** | Hard-stop immediately. The reviewer detected a load-bearing condition (premise change, governance corruption, schema collapse). Emit `HARD-STOP: <reason>` and end the turn. |

## Triangulation Discipline

When ambiguity or contradiction requires multiple reviewers:

1. Spawn reviewer A; capture verdict
2. If A returns `ESCALATE` or the situation warrants triangulation: spawn reviewer B with the same input + reviewer A's verdict block as context
3. If A and B agree (both PASS, both FAIL): proceed per joint verdict
4. If A and B disagree: hard-stop with `HARD-STOP: reviewer-deadlock` and log both verdicts to the checkpoint

Triangulation pairs by gate type:

| Gate | Reviewer A | Reviewer B (if escalation) |
|---|---|---|
| ADR | `adversarial-auditor-xhigh` | second `adversarial-auditor-xhigh` with steel-man prompt |
| Phase boundary | `trajectory-verifier` | `adversarial-auditor-xhigh` reviewing the verifier's report |
| Slice ambiguity | `Plan` | `adversarial-auditor-xhigh` |
| Subagent contradiction | `Explore` | `adversarial-auditor-xhigh` |
| Premise change | `adversarial-auditor-xhigh` | `Explore` (does the evidence cited really say what's claimed?) |
| Gate failure | `gsd-debugger` | `adversarial-auditor-xhigh` reviewing debugger's hypothesis |

## Reviewer Invocation Protocol (main agent's responsibility)

For each invocation:

1. **Compose input**: gather the artifact under review (file paths, diff, commit SHA, ADR text, debug context), the relevant phase plan section, and the prompt template (below)
2. **Invoke**: `Agent({subagent_type: '<reviewer>', description: '...', prompt: '<composed input>'})`
3. **Parse verdict**: extract the VERDICT/REASONING/RECOMMENDATION/EVIDENCE block
4. **Record**: append to STATE.md Reviewer Decisions Log; append full output to slice checkpoint
5. **Act on verdict**: per semantics above

## Prompt Templates

Reviewers must receive enough context to make grounded verdicts. Use these templates verbatim, filling the `{{placeholders}}`.

### Template: ADR Review (`adversarial-auditor-xhigh`)

```text
You are reviewing ADR-{{NN}} for the inject-migration initiative.

Context paths (read in this order):
1. {{ADR path}}
2. .planning/initiatives/inject-migration/INITIATIVE.md (mission + completion criteria)
3. .planning/initiatives/inject-migration/phases/{{phase-plan-path}}
4. .planning/readiness/intervention-strategies-2026-05-08.md (the underlying strategy)
5. AGENTS.md (governance)

Critique the ADR against:
- Does the proposed design serve the initiative's mission as stated in INITIATIVE.md?
- Are alternatives considered honestly? Is the chosen path the right one given the cited evidence?
- Does the design respect the "Working Rules" in AGENTS.md (propose-evidence-approve, no half-finished implementations)?
- Are the cited dependencies (Phase 0 cleanup, schema versions, etc.) real and stable?
- Are the boundary statements honest? What is NOT being decided that perhaps should be?
- Risk inventory: any high-likelihood / high-impact risk omitted?

This is not a code audit. Focus on plan-level reasoning.

Return your verdict in the format documented in REVIEWERS.md → "Verdict Format". A PASS means the ADR is sound enough to proceed to implementation. A FAIL means the design has load-bearing problems that must be revised. ESCALATE if your reasoning is genuinely uncertain. HALT if you detect a premise-level error in INITIATIVE.md itself.
```

### Template: Phase Boundary Verification (`trajectory-verifier`)

```text
You are verifying phase {{NN}} ({{slug}}) of the inject-migration initiative.

Trajectory plan path: .planning/initiatives/inject-migration/phases/{{NN}}-{{slug}}.md
Phase under verification: phase {{NN}} (the whole phase, all slices)

Goal-backward verification: does the codebase at HEAD deliver what the phase's "Exit Criteria" section promised? Read:
1. The phase plan's Exit Criteria section
2. The slice commits since phase start (git log)
3. STATE.md for the recorded slice outcomes
4. Slice checkpoints in .planning/initiatives/inject-migration/checkpoints/

For each Exit Criterion, confirm or refute:
- Is the artifact actually produced at the expected path?
- Does its content satisfy what the slice spec promised?
- Do the verification gates the slice ran actually attest the claim?

Return your verdict in REVIEWERS.md format. PASS = all exit criteria met. FAIL = at least one not met; specify which. ESCALATE = ambiguous evidence (verifier cannot decide alone). HALT = phase outcome contradicts INITIATIVE.md's stated mission.
```

### Template: Gate Failure Recovery (`gsd-debugger`)

```text
You are investigating a verification gate failure during the inject-migration initiative.

Slice: {{phase NN slice MM}} ({{slug}})
Gate that failed: {{gate name, e.g., audit_refmap.py verify .}}
Failure output: {{full stderr/stdout from the gate}}
Slice's write set (files just edited): {{list of paths}}
Slice's intended purpose: {{the slice spec's "Action" + "Verification" sections, copy-pasted}}

Diagnose the root cause. Hypotheses to consider:
1. Gate is flaky (rare; usually deterministic in this repo)
2. The slice's edit was incomplete or wrong
3. The slice exposed a pre-existing latent issue
4. The gate itself has a bug

Propose a fix. Cite file:line evidence. Estimate effort.

Return your verdict in REVIEWERS.md format. PASS = you have a confident root cause + fix that can be applied within the slice's write set. FAIL = root cause is outside the slice's write set; the slice cannot self-recover. ESCALATE = you need a second opinion (e.g., the failure pattern is unfamiliar). HALT = the failure indicates a contract corruption or a forbidden-action attempt.
```

### Template: Subagent Contradiction Triangulation (`Explore`)

```text
You are triangulating a contradiction in the inject-migration initiative.

A previous subagent ({{prior-agent-type}}) claimed: {{the contested claim, verbatim}}
Cited source: {{the prior agent's cited file:line or evidence}}
The contradiction: {{what the main agent observed that contradicts the prior claim}}

Read the cited source and any cross-references. Report:
- Does the cited source actually say what the prior agent claimed?
- Is there additional context that resolves the apparent contradiction?
- What does the file actually say at the cited line?

Cite file:line. Be terse.

Return your verdict in REVIEWERS.md format. PASS = no real contradiction; the prior claim is accurate; main agent's observation was a misread. FAIL = the prior claim is wrong; main agent's observation is correct; subagent should be re-run with corrected input. ESCALATE = both readings have evidence; need adversarial review. HALT = the contradiction reveals a corrupted source file.
```

### Template: Premise Change Investigation (`adversarial-auditor-xhigh`)

```text
You are investigating a possible premise change for the inject-migration initiative.

Foundational artifacts that establish the premise:
1. .planning/readiness/release-readiness-orientation-2026-05-08.md
2. .planning/readiness/intervention-strategies-2026-05-08.md
3. .planning/initiatives/inject-migration/INITIATIVE.md → "Why This Initiative Exists"

New evidence that may invalidate the premise:
{{the evidence — file diffs, upstream PR links, test output, etc.}}

Question to answer: does this new evidence change the load-bearing reasoning of the initiative?
- If the orientation's claim that "modifier carries post-conversion content" has been falsified, halt.
- If the intervention-strategies analysis's enumeration of overwrite-pressure decomposition has been falsified, halt.
- If only a peripheral detail shifted but the central thesis holds, proceed.

Return your verdict in REVIEWERS.md format. PASS = the premise still holds; continue the initiative. FAIL = a substantive but not load-bearing claim shifted; phase plans may need adjustment, but the mission stands. HALT = a load-bearing premise has been falsified; the operator must re-orient the initiative.
```

### Template: Slice Ambiguity Resolution (`Plan`)

```text
You are resolving an ambiguity in slice {{NN}}.{{MM}} of the inject-migration initiative.

Slice spec: {{copy-paste the slice spec from phases/<NN>-<slug>.md}}
The ambiguity: {{what the main agent could not safely decide between}}
Alternatives: {{list, with evidence for each}}

Resolve by reading the relevant code/docs. Recommend ONE alternative with rationale. If neither alternative is safe, recommend a third (smaller) write set that preserves the slice's purpose.

Return your verdict in REVIEWERS.md format. PASS = you have a single recommended interpretation backed by file:line evidence. FAIL = the ambiguity reveals the slice spec is broken and needs operator revision before execution. ESCALATE = the alternatives have equal evidence; adversarial review required. HALT = the slice spec contradicts INITIATIVE.md.
```

## Decision Audit Trail

Every reviewer decision lives in three places:

1. **STATE.md → Reviewer Decisions Log** (summary table; one row per invocation)
2. **Slice checkpoint → `## Reviewer Verdict` section** (full reviewer output; the parsed verdict block; what the main agent did next)
3. **Git commit body → `Reviewer:` trailer** (if a reviewer's verdict influenced the commit; e.g., `Reviewer: adversarial-auditor-xhigh PASS @ ADR-001`)

This trail allows the operator to audit every advisory decision after the initiative completes. If a decision was wrong, the operator can revert the slice and replay with adjusted reviewer input.

## Forbidden Reviewer Patterns

These are constraints on how the main agent uses reviewers, not on the reviewers themselves.

1. **Reviewers never write files** in the main loop's worktree. The main agent applies any edits, not the reviewer.
2. **Reviewers do not chain to other reviewers** — chaining happens only via the main agent's triangulation logic.
3. **Reviewers do not decide operator-only matters** — initiative scope change, abort, or sentinel transition is hard-stop only.
4. **Main agent does not skip the reviewer when reviewer is mandated** by REVIEWERS.md. The reviewer-mediated gates are not optional.
5. **Main agent does not act on a malformed verdict** — if the verdict block cannot be parsed, treat as ESCALATE.
6. **Main agent does not spawn more than 2 reviewers per gate event** — triangulation pairs only. Beyond 2 = hard-stop with deadlock.
7. **Main agent does not invoke a reviewer outside its declared use case** — only the matchups in the "Invoked at" subsections above and the triangulation table.

## Escalation Chain Summary

Lowest cost to highest cost:

1. **Auto-recover**: retry once with the same input (gate flake)
2. **Reviewer**: spawn the matched reviewer per "Invoked at"; act on verdict
3. **Triangulation**: spawn second reviewer per triangulation table; majority wins
4. **Hard-stop**: emit `HARD-STOP: <reason>`, write `paused-for-operator` checkpoint, terminate the turn

The /goal evaluator terminates the goal on `Sentinel: INITIATIVE-COMPLETE`, `Sentinel: ABORTED`, or any `HARD-STOP:` line in the turn output.

## Reviewer Failure Modes (and what the main agent does)

| Failure | Main agent response |
|---|---|
| Reviewer agent itself errors or times out | Retry once with same prompt. If still failing, hard-stop with `HARD-STOP: reviewer-tool-failure`. Do not silently skip. |
| Reviewer returns no verdict block | Treat as ESCALATE; triangulate. |
| Reviewer returns contradictory verdict (e.g., VERDICT: PASS but RECOMMENDATION: do-not-proceed) | Treat as ESCALATE; triangulate. |
| Reviewer recommends edits outside the slice's declared write set | Treat as FAIL with a surface-change-request; spawn `Plan` reviewer to evaluate scope; if Plan PASS, expand write set within that slice and log the expansion; if Plan FAIL, hard-stop. |
| Two triangulating reviewers deadlock (one PASS, one FAIL) | Hard-stop with `HARD-STOP: reviewer-deadlock`. |
| Reviewer's evidence cites a non-existent file:line | Treat verdict as untrustworthy; ESCALATE. |

## Adversarial Self-Check (for the main agent)

Before invoking a reviewer, the main agent should ask itself:

- Am I invoking this reviewer because the gate requires it, or because I want a rubber-stamp? (Only the former is valid.)
- Have I composed the input with enough context that a verdict can be grounded? (If not, the reviewer's output will be noise.)
- Am I prepared to act on a FAIL verdict? (If not, I should not invoke yet.)

The reviewer is not a checkbox. Its verdict directs the next action.
