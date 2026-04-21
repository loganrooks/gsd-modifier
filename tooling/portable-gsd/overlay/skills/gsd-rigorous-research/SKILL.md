---
name: "gsd-rigorous-research"
description: "Run an epistemically rigorous repo-local research pass for terrain mapping, hypothesis testing, solution evaluation, or synthesis. Use outside phase workflows or when later GSD work needs a stronger research lane."
metadata:
  short-description: "Repo-local rigorous research for terrain mapping, hypothesis testing, solution evaluation, or synthesis"
---

<objective>
Run a research pass that makes the path of inquiry inspectable, keeps evidence separate from inference, and carries conclusions only as strongly as the evidence actually supports.
</objective>

<when_to_use>
Use this skill when the user wants rigorous research, comparison, hypothesis stress-testing, or synthesis that is not well served by a normal phase workflow.

Typical fits:
- standalone repo-aware research outside milestone or phase execution
- phase-adjacent research that needs stronger epistemic discipline before planning
- comparative or ambiguous questions where premature recommendations would be misleading
- synthesis work across existing research, audits, phase docs, and external sources
</when_to_use>

<repo_first>
This skill is repo-local first.

- Treat `.planning/` as the source of truth for project posture, requirements, deferrals, and prior findings.
- Read only the canon that is relevant to the current question. Use `references/repo-canon.md` to choose.
- If the task is phase-specific, this skill can harden the research lane, but it does not replace normal phase workflows unless the user explicitly wants a standalone pass.
</repo_first>

<mode_selection>
Pick one primary mode before starting. If the request mixes modes, split or stage the work explicitly.

- `terrain mapping` - map the option space and hidden assumptions; do not rank or pick just to be tidy
- `hypothesis testing` - stress-test a candidate and prioritize disconfirming evidence
- `solution evaluation` - compare known options against explicit criteria and recommend only when the option space has enough breadth, relation clarity, and contrary-pressure coverage to support an honest comparison
- `synthesis` - integrate prior artifacts into a planning-ready or decision-ready structure without faking closure

Read `references/method.md` before starting if the lane is ambiguous, high-stakes, or likely to expand.
</mode_selection>

<process>
1. Frame the research:
   - state the question
   - state the chosen mode
   - define scope and non-goals
   - note what would count as a good stopping point
2. Build a path of inquiry before diving deep:
   - entry point
   - branches considered
   - branches pursued
   - branches deferred or abandoned
3. Surface assumptions and load-bearing dependencies early.
4. Gather evidence from local canon, code, and external sources as needed.
5. Keep a hard split between:
   - direct evidence
   - inference or interpretation
   - unresolved unknowns
6. Handle scope expansion explicitly:
   - defer
   - follow-and-mark
   - revisit later
7. Produce an output using `references/output-template.md`.
</process>

<required_behaviors>
- Make the path of inquiry visible, not just the conclusion.
- Separate evidence from inference in every major section.
- Surface assumptions rather than smuggling them in.
- Name dependencies and relations, not just isolated findings.
- Be explicit about unknowns, weak evidence, and deferrals.
- Preserve bounded strengthening opportunities when the research surfaces them; do not let them dissolve into generic future work or ambient prose.
- Do not silently broaden scope.
- Do not recommend in `terrain mapping` mode unless the user explicitly changes modes.
</required_behaviors>

<claim_handling>
When helpful, use the claim vocabulary from `references/method.md`:
- `evidenced`
- `decided`
- `assumed`
- `open`
- `projected`
- `stipulated`
- `governing`

Optional inline markers such as `[assumed:reasoned]` are allowed when they improve clarity, especially in research artifacts that will feed later GSD work.
</claim_handling>

<phase_handoff>
If the research will feed later planning, translate findings into steering-relevant outputs:
- what now carries strongly enough to treat as decided
- what remains assumed or open
- what constraints were derived
- what future seams or deferrals must remain protected
- what strengthening opportunities surfaced, and whether each belongs in current-phase intensification or seeded later resurfacing

For that shape, consult `references/repo-canon.md` and the local discuss/context materials it points to.
</phase_handoff>

<output>
Use the lightweight contract in `references/output-template.md`.

Minimum output qualities:
- honest mode declaration
- explicit path of inquiry
- assumptions surfaced
- evidence and inference separated
- dependencies and relations named
- unknowns and deferrals stated plainly
- sources listed
</output>
