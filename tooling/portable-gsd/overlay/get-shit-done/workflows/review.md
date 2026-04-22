<purpose>
Cross-AI peer review — invoke external AI CLIs to independently review phase plans.
Each CLI gets the same prompt (PROJECT.md context, phase plans, requirements) and
produces structured feedback. Results are combined into REVIEWS.md for the planner
to incorporate via --reviews flag. The synthesis is a consumer contract, not a soft
consensus summary: lone high-signal criticism, merely-adequate areas, and later-audit
risks stay visible even when they are not majority views.

This implements adversarial review: different AI models catch different blind spots.
A plan that survives review from 2-3 independent AI systems is more robust.
</purpose>

<process>

<step name="detect_clis">
Check which AI CLIs are available on the system:

```bash
# Check each CLI
command -v gemini >/dev/null 2>&1 && echo "gemini:available" || echo "gemini:missing"
command -v claude >/dev/null 2>&1 && echo "claude:available" || echo "claude:missing"
command -v codex >/dev/null 2>&1 && echo "codex:available" || echo "codex:missing"
command -v coderabbit >/dev/null 2>&1 && echo "coderabbit:available" || echo "coderabbit:missing"
command -v opencode >/dev/null 2>&1 && echo "opencode:available" || echo "opencode:missing"
```

Parse flags from `{{GSD_ARGS}}`:
- `--gemini` → include Gemini
- `--claude` → include the agent
- `--codex` → include Codex
- `--coderabbit` → include CodeRabbit
- `--opencode` → include OpenCode
- `--all` → include all available
- No flags → include all available

If no CLIs are available:
```
No external AI CLIs found. Install at least one:
- gemini: https://github.com/google-gemini/gemini-cli
- codex: https://github.com/openai/codex
- claude: https://github.com/anthropics/claude-code
- opencode: https://opencode.ai (leverages GitHub Copilot subscription models)

Then run /gsd-review again.
```
Exit.

Determine which CLI to skip based on the current runtime environment:

```bash
# Environment-based runtime detection (priority order)
if [ "$ANTIGRAVITY_AGENT" = "1" ]; then
  # Antigravity is a separate client — all CLIs are external, skip none
  SELF_CLI="none"
elif [ -n "$CLAUDE_CODE_ENTRYPOINT" ]; then
  # Running inside Claude Code CLI — skip claude for independence
  SELF_CLI="claude"
else
  # Other environments (Gemini CLI, Codex CLI, etc.)
  # Fall back to AI self-identification to decide which CLI to skip
  SELF_CLI="auto"
fi
```

Rules:
- If `SELF_CLI="none"` → invoke ALL available CLIs (no skip)
- If `SELF_CLI="claude"` → skip claude, use gemini/codex
- If `SELF_CLI="auto"` → the executing AI identifies itself and skips its own CLI
- At least one DIFFERENT CLI must be available for the review to proceed.
</step>

<step name="gather_context">
Collect phase artifacts for the review prompt:

```bash
INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" init phase-op "${PHASE_ARG}")
if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
```

Read from init: `phase_dir`, `phase_number`, `padded_phase`.

Then read:
1. `.planning/PROJECT.md` (first 80 lines — project context)
2. Phase section from `.planning/ROADMAP.md`
3. All `*-PLAN.md` files in the phase directory
4. `*-CONTEXT.md` if present (user decisions)
5. `*-RESEARCH.md` if present (domain research)
6. `.planning/REQUIREMENTS.md` (requirements this phase addresses)
</step>

<step name="build_prompt">
Build a structured review prompt:

```markdown
# Cross-AI Plan Review Request

You are reviewing implementation plans for a software project phase.
Provide structured feedback on plan quality, completeness, and risks.

## Project Context
{first 80 lines of PROJECT.md}

## Phase {N}: {phase name}
### Roadmap Section
{roadmap phase section}

### Requirements Addressed
{requirements for this phase}

### User Decisions (CONTEXT.md)
{context if present}

### Research Findings
{research if present}

### Plans to Review
{all PLAN.md contents}

## Review Instructions

Analyze each plan and provide:

1. **Summary** — One-paragraph assessment
2. **Strongest Justified Criticism** — The single most important criticism you can defend, with severity and reasoning
3. **What Is Already Strong** — What's well-designed and should be preserved (bullet points)
4. **What Is Merely Adequate** — Areas that technically work but are not yet strong (bullet points)
5. **Concerns** — Potential issues, gaps, risks (bullet points with severity: HIGH/MEDIUM/LOW)
6. **Later Audit Failures** — What would likely fail a later stringent audit by strong engineers, designers, or researchers
7. **Suggestions** — Specific improvements (bullet points)
8. **Risk Assessment** — Overall risk level (LOW/MEDIUM/HIGH) with justification

Focus on:
- Missing edge cases or error handling
- Dependency ordering issues
- Scope creep or over-engineering
- Security considerations
- Performance implications
- Whether the plans actually achieve the phase goals
- What must change before a later strong-engineer audit could honestly pass
- The strongest justified criticism, even if no other reviewer is likely to agree
- What is merely adequate but would not withstand a higher standard
- What could look closure-ready now but fail under later stringent audit
- Do not soften a criticism because the overall plan looks solid or because you expect disagreement from other reviewers
- If you think a concern can be deferred safely, say why it is non-load-bearing rather than leaving it implicit

Output your review in markdown format.
```

Prepare one durable run-home before reviewer invocation:

```bash
RUN_HOME_JSON=$(python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" prepare-run-home \
  --phase-dir "$phase_dir" \
  --padded-phase "$padded_phase")
RUN_HOME=$(python3 - <<'PY' "$RUN_HOME_JSON"
import json, sys
print(json.loads(sys.argv[1])["run_home"])
PY
)
PROMPT_PATH=$(python3 - <<'PY' "$RUN_HOME_JSON"
import json, sys
print(json.loads(sys.argv[1])["prompt_path"])
PY
)
mkdir -p "$RUN_HOME/raw" "$RUN_HOME/launch-truth"
```

Write the prompt to `"$PROMPT_PATH"` rather than to `/tmp`.
The canonical run-home shape is `.planning/phases/{padded_phase}/reviews/{run_id}/`.
</step>

<step name="invoke_reviewers">
For each selected CLI, invoke in sequence (not parallel — avoid rate limits) and preserve the raw reviewer trail under `"$RUN_HOME"` instead of `/tmp`.

Record one pre-launch estimate per reviewer before invocation. The first estimate may be naive; the route still has to preserve it for later calibration.

**Gemini:**
```bash
gemini -p "$(cat "$PROMPT_PATH")" \
  > "$RUN_HOME/raw/gemini.stdout.md" \
  2> "$RUN_HOME/raw/gemini.stderr.log"
python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" record-reviewer \
  --run-home "$RUN_HOME" \
  --reviewer gemini \
  --shape plain \
  --stdout-file "$RUN_HOME/raw/gemini.stdout.md" \
  --stderr-file "$RUN_HOME/raw/gemini.stderr.log" \
  --estimated-duration "operator estimate here" \
  --invocation 'gemini -p "$(cat "$PROMPT_PATH")"' \
  --exit-code "$?" \
  --elapsed-seconds "measured elapsed here"
```

**the agent (separate session):**
```bash
python3 "__PROJECT_ROOT__/tooling/codex/run_claude_probe.py" \
  --label "review-claude-${padded_phase}" \
  --model 'opus[1m]' \
  --effort high \
  --dangerously-skip-permissions \
  --output-dir "$RUN_HOME/raw/claude" \
  --prompt-file "$PROMPT_PATH" \
  > "$RUN_HOME/raw/claude/probe-summary.txt"
python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" record-reviewer \
  --run-home "$RUN_HOME" \
  --reviewer claude \
  --shape claude \
  --stream-file "$RUN_HOME/raw/claude/latest.stream.jsonl" \
  --stderr-file "$RUN_HOME/raw/claude/latest.stderr.log" \
  --probe-summary-file "$RUN_HOME/raw/claude/probe-summary.txt" \
  --estimated-duration "operator estimate here" \
  --requested-model "opus[1m]" \
  --requested-reasoning "high" \
  --requested-sandbox "danger-full-access" \
  --exit-code "probe exit code here" \
  --elapsed-seconds "measured elapsed here"
```

**Codex:**
```bash
SINCE=$(date +%s)
codex exec --skip-git-repo-check "$(cat "$PROMPT_PATH")" \
  > "$RUN_HOME/raw/codex.stdout.md" \
  2> "$RUN_HOME/raw/codex.stderr.log"
python3 "__PROJECT_ROOT__/tooling/codex/capture_launch_truth.py" \
  --since "$SINCE" \
  --label "review-codex-${padded_phase}" \
  --requested-model gpt-5.4 \
  --requested-reasoning high \
  --requested-approval never \
  --requested-sandbox danger-full-access \
  --output "$RUN_HOME/raw/codex-launch-truth.md"
python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" record-reviewer \
  --run-home "$RUN_HOME" \
  --reviewer codex \
  --shape codex \
  --stdout-file "$RUN_HOME/raw/codex.stdout.md" \
  --stderr-file "$RUN_HOME/raw/codex.stderr.log" \
  --launch-truth-markdown "$RUN_HOME/raw/codex-launch-truth.md" \
  --estimated-duration "operator estimate here" \
  --requested-model "gpt-5.4" \
  --requested-reasoning "high" \
  --requested-approval "never" \
  --requested-sandbox "danger-full-access" \
  --invocation 'codex exec --skip-git-repo-check "$(cat "$PROMPT_PATH")"' \
  --exit-code "$?" \
  --elapsed-seconds "measured elapsed here"
```

**CodeRabbit:**

Note: CodeRabbit reviews the current git diff/working tree — it does not accept a prompt. It may take up to 5 minutes. Use `timeout: 360000` on the Bash tool call.

```bash
coderabbit review --prompt-only \
  > "$RUN_HOME/raw/coderabbit.stdout.md" \
  2> "$RUN_HOME/raw/coderabbit.stderr.log"
python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" record-reviewer \
  --run-home "$RUN_HOME" \
  --reviewer coderabbit \
  --shape plain \
  --stdout-file "$RUN_HOME/raw/coderabbit.stdout.md" \
  --stderr-file "$RUN_HOME/raw/coderabbit.stderr.log" \
  --estimated-duration "operator estimate here" \
  --invocation "coderabbit review --prompt-only" \
  --exit-code "$?" \
  --elapsed-seconds "measured elapsed here"
```

**OpenCode (via GitHub Copilot):**
```bash
cat "$PROMPT_PATH" | opencode run - \
  > "$RUN_HOME/raw/opencode.stdout.md" \
  2> "$RUN_HOME/raw/opencode.stderr.log"
python3 "__PROJECT_ROOT__/tooling/codex/run_review_reviewer.py" record-reviewer \
  --run-home "$RUN_HOME" \
  --reviewer opencode \
  --shape plain \
  --stdout-file "$RUN_HOME/raw/opencode.stdout.md" \
  --stderr-file "$RUN_HOME/raw/opencode.stderr.log" \
  --estimated-duration "operator estimate here" \
  --invocation 'cat "$PROMPT_PATH" | opencode run -' \
  --exit-code "$?" \
  --elapsed-seconds "measured elapsed here"
```

If a CLI fails, preserve the raw artifacts anyway and let `record-reviewer` classify the result as `partial` or `absent`. Do not collapse recoverable last-message text into a blank heading.

Display progress:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GSD ► CROSS-AI REVIEW — Phase {N}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

◆ Reviewing with {CLI}... done ✓
◆ Reviewing with {CLI}... done ✓
```
</step>

<step name="write_reviews">
Combine all review responses into `{phase_dir}/{padded_phase}-REVIEWS.md`:

```markdown
---
phase: {N}
reviewers: [gemini, claude, codex, coderabbit, opencode]
reviewed_at: {ISO timestamp}
plans_reviewed: [{list of PLAN.md files}]
---

# Cross-AI Plan Review — Phase {N}

## Gemini Review

{gemini review content or absence note from $RUN_HOME/gemini.review.md and gemini.status.md}

---

## the agent Review

{claude review content or partial-state note from $RUN_HOME/claude.review.md and claude.status.md}

---

## Codex Review

{codex review content or partial/absence note from $RUN_HOME/codex.review.md and codex.status.md}

---

## CodeRabbit Review

{coderabbit review content or absence note}

---

## OpenCode Review

{opencode review content or absence note}

---

## Review Synthesis

{synthesize overlap, lone high-signal criticism, merely-adequate areas, later-audit risks, and meaningful disagreement without flattening them into false consensus. Name source reviewer(s) for each synthesized item.}

### Review Consumer Contract

#### Must Address In Replan
{all HIGH-severity agreed concerns, any lone high-signal criticism that would likely fail later audit if ignored, and any merely-adequate area or later-audit risk that leaves the plan weak against the repo quality bar}

#### Explicit Rebuttal Required If Not Accepted
{criticisms that may be rejected only on the merits. Silence or "no consensus" is not a valid disposition.}

#### Safe To Defer
{non-load-bearing improvements or low-severity ideas that can wait without misrepresenting plan readiness}

### Agreed Strengths
{strengths mentioned by 2+ reviewers}

### Agreed Concerns
{concerns raised by 2+ reviewers — important overlap, not the only route to importance}

### Lone High-Signal Concerns
{single-reviewer criticisms that are well-justified, severe, or likely to fail later stringent audit}

### Merely Adequate Areas
{themes reviewers describe as acceptable but not strong enough for a higher bar}

### Later Audit Risks
{issues that may read as closure-ready now but would likely fail later stringent audit}

### Divergent Views
{where reviewers disagreed — worth investigating with explicit judgment, not automatic dismissal}
```

Commit:
```bash
node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" commit "docs: cross-AI review for phase {N}" --files {phase_dir}/{padded_phase}-REVIEWS.md
```
</step>

<step name="present_results">
Display summary:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GSD ► REVIEW COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase {N} reviewed by {count} AI systems.

Shared concerns:
{top 3 shared concerns}

Top lone high-signal concern:
{single strongest well-justified criticism that is not just a consensus item}

Full review: {padded_phase}-REVIEWS.md
Durable reviewer trail: {RUN_HOME}

To incorporate feedback into planning:
  /gsd-plan-phase {N} --reviews
```

Do not delete the run-home. It is the canonical raw reviewer trail for launch truth, timing, salvage, and later reread.
</step>

</process>

<success_criteria>
- [ ] At least one external CLI invoked successfully
- [ ] REVIEWS.md written with structured feedback
- [ ] Review synthesis preserves shared concerns, lone high-signal criticism, and divergent views
- [ ] Durable run-home populated with per-reviewer artifacts
- [ ] User knows how to use feedback (/gsd-plan-phase --reviews)
</success_criteria>
