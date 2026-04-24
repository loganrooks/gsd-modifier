Read only the target file and treat it as fully self-contained. Do not read, infer from, or rely on any other files, repo context, project background, or external sources unless they are explicitly included in the prompt.

Write the result to a new Markdown file rather than in place. The output filename must begin with a local datetime stamp in the format `YYYY-MM-DD-HHMMSS-`, followed by a descriptive slug. Do not overwrite the source file.

Composition process:
- Do not write directly to the final file on the first pass.
- First, read and mark the text's pressure points, recurrences, asymmetries, exclusions, qualifiers, and points of hesitation.
- Then draft one complete continuous essay for the commentary section in a single arc.
- Then derive the practical sections from that reading rather than writing them as if they were directly given by the text.
- Then perform exactly one deliberate revision pass focused on textual fidelity, anti-slop cleanup, removal of unearned Derridean vocabulary, and removal of generic theoretical filler.
- A final structure-only calibration pass is allowed if it only reorganizes headings, consequence count display, bounds/revisit notes, or similar presentation structure, and introduces no new interpretive claims.
- After that revision, write only the revised final version to the timestamped Markdown file.
- Do not produce multiple competing versions unless explicitly asked.

Chunked / deconstructive use:
- If the user asks for chunked, staged, deconstructive, or otherwise partial handling of a long text, do **not** read the whole target before drafting the first chunk unless the user explicitly asks for whole-text pre-reading.
- In chunked mode, the target note remains the primary object of reading; earlier chunk files are secondary aids for traceable revisit/revision only, not replacement authorities.
- In chunked mode, treat each chunk as its own mini-run of the composition process:
  - read only the chosen span
  - draft pass 1
  - revisit the whole chunk in pass 2
- In chunked mode, each chunk may become its own timestamped output file.
- In chunked mode, do **not** inherit a fixed count or shape of practical consequences from earlier chunks.
- During pass 1, judge what the current chunk actually earns:
  - how much commentary
  - how many operational consequences
  - how many workflow consequences
  - whether local subheaders are warranted
- During pass 2, you may add, remove, merge, split, rename, or otherwise restructure operational or workflow consequences if the reread warrants it.
- If pass 2 changes the number of operational or workflow consequences, append a short `Revision Note` inside the relevant section naming what was merged, dropped, split, or added and why.
- Later chunks may revise, refine, or partially correct earlier chunk commentaries or translations if recurrence or later distinctions warrant it, but that revising act must be explicit and traceable rather than silent.
- Later chunks may also *revisit* earlier chunks without fully revising them.
- A revisit may mark recurrence, extension, narrowing, rescaling, differentiation, or transformation of an earlier motif without claiming that the earlier chunk was simply wrong.
- If you mark an earlier chunk as revised or revisited, state whether that relation is grounded:
  - in the current chunk's wording alone
  - in earlier chunk text that is explicitly reopened in the current pass
  - or in both
- Do not import claims from earlier chunk files into the current commentary as if they were fresh evidence from the target note; use them only to make the revision/revisit relation legible.
- Chunking may move generally forward through the text while still allowing overlap, local backward touchpoints, and explicit revisions to earlier chunks.

Structure the output in exactly three top-level sections:
- `Commentary`
- `Operational Translation`
- `Workflow Translation`

For `Commentary`:
- Offer a Derrida-attuned commentary on this text as an act of inheritance rather than neutral analysis.
- In chunked mode, begin with a short `Commentary Bounds` block inside the `Commentary` section.
- That bounds block should state:
  - the primary span being commented on
  - any backward or lateral touchpoints being actively used
  - whether the reading relies on later sections or deliberately stops before them
- In chunked mode, you may also include a short optional `Revisits / Transformations` block inside the `Commentary` section.
- Use that block when the current chunk returns to an earlier motif, distinction, or translation without amounting to a full revision.
- In that block, say briefly:
  - what earlier chunk or motif is being revisited
  - whether the current chunk revisits, extends, narrows, differentiates, rescales, or revises it
  - what is preserved and what is transformed in the recurrence
  - what the grounding basis is: current chunk alone, reopened earlier chunk text, or both
- Do not pretend to speak for Derrida directly, and do not apply a preset checklist of “Derridean concepts.”
- Begin from the text’s own idiom, recurrences, tensions, asymmetries, exclusions, qualifiers, and points of hesitation.
- Introduce Derridean vocabulary only where the text itself seems to require or earn it.
- Treat terms such as trace, supplement, différance, gift, and deconstruction not as fixed doctrinal categories or a portable method, but as provisional and revisable handles if they become necessary.
- If they are not necessary, do not force them in.
- Do not reduce the reading to concept-application.
- Focus especially on the tension between fidelity and transformation in commentary: how the reading tries to receive the text responsibly while inevitably altering, selecting, organizing, and reinscribing it.
- Distinguish clearly between close reading and interpretive extension.
- Mark where the commentary is strongly grounded in the text, where it extrapolates, and where it risks reifying or domesticating what it is trying to preserve.
- If the current chunk revises an earlier chunk's reading, mark that revision plainly inside the commentary rather than implying the earlier reading never existed.
- If the current chunk merely revisits or transforms an earlier motif without fully revising it, mark that too rather than forcing the stronger language of revision.
- Do not reduce the response to generic “deconstruction” language.
- Do not resolve the aporia too quickly.
- Write this section as a continuous essay, not bullet points.
- Let the ending of this section remain open rather than pretending to achieve final closure.

For `Operational Translation`:
- Shift explicitly from commentary into provisional operationalization.
- Do not present practical recommendations as if they were directly dictated by the text.
- Make the inferential step visible.
- Keep this section concise and structured.
- Let the current chunk determine how many operational consequences it actually earns.
- It is acceptable for the section to be brief if the chunk yields few operational consequences; do not pad it to match earlier chunks.
- Local subheaders are welcome when they clarify the distinctions being made.
- Those subheaders do not need to repeat from chunk to chunk and should be named from the current chunk's own pressures where possible.
- Promote flat consequences to named subheaders only when the reread still yields distinct pressures likely to matter as reusable local handles; otherwise keep numbered or plainly structured items.
- Do not create a standalone `Revision To Chunk N` operational consequence unless the current chunk yields a new audit-design implication that cannot be adequately carried by the commentary-side `Revisits / Transformations` block alone.
- For each practical implication, distinguish:
  - the textual pressure or problem that motivates it
  - the interpretive translation being made
  - the concrete audit-design implication
  - the scope of the implication
  - the confidence level or remaining uncertainty
- Focus on audit-design implications such as:
  - audit ontology
  - unit of analysis
  - warrant standards
  - contestation registers
  - evidence handling
  - framing and exclusion detection
  - revision and closure rules

For `Workflow Translation`:
- Shift again from audit-design implications into broader technical or organizational workflow implications.
- Keep the inferential step visible here too.
- Do not collapse philosophical vocabulary directly into technical jargon.
- Do not produce generic productivity advice or abstract “best practices.”
- If the target file is being treated as fully self-contained, keep recommendations generic and conditional rather than repo-specific.
- Let the current chunk determine how many workflow consequences it actually earns.
- It is acceptable for the section to be brief if the chunk yields few workflow consequences; do not pad it to match earlier chunks.
- Local subheaders are welcome here too when they sharpen the workflow consequences.
- Workflow consequences may be fewer or more numerous than in earlier chunks; do not stabilize their count by habit.
- Do not create a standalone chunk-revision workflow consequence unless the current chunk yields a new workflow implication that cannot be adequately carried by the commentary-side `Revisits / Transformations` block alone.
- Focus on workflows such as:
  - audit procedures
  - review protocols
  - prompt design
  - issue triage
  - requirements review
  - architecture review
  - postmortems
  - decision logs
  - handoff artifacts
  - governance or canon-update workflows
- Prefer a small number of sharp workflow consequences over a long list of generic abstractions.

Style constraints:
- Avoid AI-slop, canned academic prose, and generic “the text invites us to think” language.
- No throat-clearing, scene-setting, or meta filler.
- Do not flatter the text, dramatize the reading, or perform difficulty for its own sake.
- Prefer precise engagement with the wording, structure, syntax, and argumentative pressure points of the text over abstract performance.
- Quote or paraphrase only when needed to anchor a claim.
- Vary sentence length and rhythm. Avoid evenly shaped paragraphs and repetitive syntactic habits.
- Do not use a term unless it is doing real explanatory work.
- If a claim is interpretive extension rather than close reading, mark it plainly.

Model-specific anti-slop constraints:
- Avoid GPT-style balancing formulas unless strictly necessary: “not X but Y,” “less X than Y,” “both X and Y,” “at once X and Y,” “as much X as Y.”
- Do not rely on reusable theory filler such as “what is at stake,” “opens a space,” “invites us to think,” “stages,” “negotiates,” “traces out,” “works through,” “complicates,” or “calls into question” unless tied to a specific textual feature.
- Avoid hedge-stacking: “perhaps,” “in some sense,” “it seems,” “may be said to,” “might be read as,” repeated in the same passage.
- Avoid overusing abstract nouns common to this style: “gesture,” “register,” “logic,” “economy,” “movement,” “operation,” “field,” “space,” “closure,” “opening,” unless each is doing concrete analytical work.
- Do not manufacture depth through cadence alone: no symmetrical paragraphs, no serial triads, no rhythmic restatement of the same point in slightly different words.
- Do not ban Derridean vocabulary in advance, but do not use it ceremonially.
- Terms such as trace, supplement, différance, gift, or phrases such as always already should appear only where the reading has earned them and where they clarify something that plainer language would miss.
- Do not intensify prose with hallmark philosophical phrases such as “precisely,” “indeed,” “irreducibly,” or “always already” unless the phrase is necessary, textually earned, and doing analytic rather than atmospheric work.
- If you use a signature Derridean term or phrase, make it answerable to a specific textual pressure and not just to style or mood.
- Prefer one sharp, text-specific point over three abstract paraphrases.
- If a sentence could appear unchanged in a commentary on almost any Derrida- or Levinas-adjacent text, delete it.
- Before finalizing, cut every sentence that sounds like graduate-seminar atmosphere rather than a response to this file.
