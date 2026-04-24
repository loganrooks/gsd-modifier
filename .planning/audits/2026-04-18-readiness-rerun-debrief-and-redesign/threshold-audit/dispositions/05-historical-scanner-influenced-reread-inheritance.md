Date: 2026-04-21
Status: accepted bounded historical reread

# Historical Scanner-Influenced Reread Inheritance

## Launch Truth

- [e:c+i] Requested-versus-effective launch truth is preserved at [launch-truth/05-historical-scanner-influenced-reread-launch-truth.md](../launch-truth/05-historical-scanner-influenced-reread-launch-truth.md).
- [e:c+i] The captured row matches the intended reviewer lane:
  - model `gpt-5.4`
  - reasoning `xhigh`
  - sandbox `danger-full-access`
  - thread `019db1c2-87cb-7bc0-b2f7-4c36f66a55b7`

## Accepted Findings

- [d:c+i] Accept the historical reread's main split: the threshold-audit family widened attention usefully, but some later turns let heuristic pressure drift into wording control or governance gating.
- [d:c+i] Accept the historical correction set:
  - the pseudo-positive/static-positive wording preference should not remain durable doctrine
  - scanner-as-default-workflow-step carry should not remain durable doctrine
  - scanner-as-gate carry inside live governance should not remain
  - the attempted weakening of explicit anti-threshold prohibition wording should stay reversed
- [d:c+i] Accept the historical keep-set:
  - the threshold-audit family itself remains worth keeping
  - the gate-vs-terrain and self-overcoming split remains worth keeping
  - the scanner-authority demotion remains worth keeping
  - the later compatibility-consumer and governance follow-through remains worth keeping
- [d:c+i] Accept the bounded live-code follow-through: the reviewer identified a still-live false-control edge in `scan_threshold_language.py`, and that edge is now narrowed directly rather than left as ambient future work.

## Follow-Through

- [e:c+i] The scanner helper now treats explicit `forbid` / `prohibit` style anti-pattern lines as meta-instruction examples too, which removes the concrete false-control hit verified on [PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md](../../pr-docs-intervention/PR-DOCS-INTERVENTION-AUDIT-NEXT-STEPS.md).
- [e:c+i] The helper now also has direct unit coverage at [tooling/codex/tests/test_scan_threshold_language.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_scan_threshold_language.py).
- [e:c+i] The historical reread output is preserved at [outputs/05-historical-scanner-influenced-reread-gpt54-xhigh-r1.md](../outputs/05-historical-scanner-influenced-reread-gpt54-xhigh-r1.md).

## Reinterpretation Carry

- [d:r:i] Read [dispositions/01-threshold-language-residue-audit.md](01-threshold-language-residue-audit.md) and [dispositions/02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md](02-spec-prompt-threshold-residue-and-self-overcoming-surface-audit.md) through the later `03`-`05` caveat layer rather than as scanner-expansion doctrine by themselves.
- [d:r:i] The raw scan artifacts remain widening intake only. They do not become cleanup ledgers, authority surfaces, or prose-policing justification.

## Boundary

- [d:r:i] This inheritance note does not reopen the whole threshold-audit family for lexical cleanup.
- [d:r:i] It records one bounded historical reread, accepts the parts that survive contextual scrutiny, narrows one still-live heuristic edge in code, and preserves the stronger rule that contextual reread stays sovereign.
