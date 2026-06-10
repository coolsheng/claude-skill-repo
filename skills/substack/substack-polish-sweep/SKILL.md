---
name: substack-polish-sweep
description: Run the final mechanical sweep on a near-final Substack draft — catches grammar, typos, subject-verb agreement, possessive/contraction errors, hedge-budget breaches, voice-drift patterns (hope/wish insertions, smileys, advisory closes, earnest-affirmation phrases), and other mechanical issues that survive multiple polish passes. Right-stage AFTER structural review is done and BEFORE pasting into Substack. Use when the draft is structurally final and the question is only "did any mechanical errors or voice-drift slip through?" Trigger phrases: "polish sweep", "final grammar pass", "mechanical sweep", "catch any typos before ship", "ready to publish — final check?", "pre-publish check".
---

# Substack Polish Sweep

A skill for the *final pre-publish pass* on a Substack draft. The user has already addressed structural issues via `/substack-reviewer` (or equivalent) and now needs a deterministic, exhaustive sweep for two classes of issues that recur across polish passes:

1. **Mechanical errors** — subject-verb agreement, possessive vs contraction, lead/led, spelling, hedge inventory, em-dash density.
2. **Voice-drift patterns** — documented polish-mode insertions (hope/wish clauses, smileys, advisory closes, earnest-affirmation phrases) that soften voice under publish pressure and were absent from the reviewed draft.

This skill is the *final gate before ship* — calibrated for the user's actual recurring failure modes, not generic prose advice. Voice-drift patterns are flagged for a conscious keep/cut decision, not auto-removed.

## What the user wants

The user has a near-final Substack draft. Structural review is done. They want a tool that:

- Scans the draft for mechanical errors *exhaustively*, not a curated top-3
- Names what's wrong with a specific label, line ref, and exact-text quote
- Suggests the mechanical fix (this is OK — these are not voice decisions)
- **Does not touch voice, structure, or argument** — those are `/substack-reviewer`'s territory
- Returns a flat list, not a triage. The user fixes all of them before ship.

If there are no mechanical errors, say so plainly and don't manufacture findings.

## What to produce

A single flat list of mechanical issues, each with:
- **Label** from the vocabulary below
- **Line/passage reference**
- **Exact quoted text** so the user can find it
- **Suggested mechanical fix** (one-word swap, agreement correction, etc.)

No structural commentary. No voice suggestions. No "consider tightening this section." If the issue isn't on the mechanical vocabulary list, don't flag it.

If something *looks* mechanical but is actually a voice choice (e.g., "Yeh" instead of "Yeah," intentional fragment, parenthetical aside), do not flag it. Voice is sacred; mechanics is the only territory.

## When to use vs not use

**Use when:**
- Draft has been through structural review
- User has decided the structure is final
- The question is only "did any mechanical errors slip through?"
- About to paste into Substack and publish

**Don't use when:**
- Draft is mid-rewrite (structural issues will swamp mechanical signal)
- User hasn't run `/substack-reviewer` yet (start there)
- Draft is a first-pass brain-dump (use `/substack-distiller` or `/substack-scaffolder`)

## The vocabulary (what to catch)

Use these exact labels. Don't invent new categories.

### Agreement errors
- **Subject-verb disagreement** — plural subject + singular verb or vice versa. Examples: *"the labs has,"* *"the mechanics means,"* *"models which sets,"* *"pillars when executed does,"* *"compute and talent multiplies."* The user's most-recurring mechanical error. Sweep aggressively.
- **Determiner-noun mismatch** — singular determiner + plural noun or vice versa. Examples: *"every non-compute countries,"* *"each engineers,"* *"all engineer."*
- **Pronoun-antecedent mismatch** — pronoun doesn't agree with referent. Examples: *"Their impacts does"* (their = plural, does = singular).

### Possessive vs contraction
- **It's vs its** — *"it's"* = "it is" / "it has"; *"its"* = possessive. The user confuses these reliably. Flag every instance and check the meaning.
- **Their / they're / there** — confusion between possessive, contraction, and locative.
- **Your / you're** — same pattern.

### Past-tense / participle confusion
- **Lead vs led** — *"lead"* = present tense or noun (metal); *"led"* = past tense. Examples: *"government-lead"* → *"government-led,"* *"AI-lead world"* → *"AI-led world,"* *"democractic-lead"* → *"democratic-led."* Sweep every hyphenated *-lead* compound.
- **Than vs then** — comparison vs temporal.

### Sentence structure errors
- **Missing subject** — sentence starts with subordinator but no main subject. Examples: *"Although sounds ominous, ..."* (missing "it"). Flag unless clearly a voiced compression (rare).
- **Sentence-break-instead-of-clause** — period where comma/dash/conjunction belongs, leaving the second sentence with a dependent pronoun. Example: *"X plan. Their impacts..."* — "their" references X, so the period orphans the second sentence. Suggest merge with comma or em-dash.
- **Comma splice** — two independent clauses joined by comma without coordinator. Flag *only* when the result is confusing; don't flag voiced fragmenty rhythm.
- **Run-on em-dash chain** — 3 or more em-dashes in a single sentence. Suggest breaking into two sentences. (The user's polish-mode tendency.)

### Spelling
- **Misspelling** — actual typos. Examples from the FIJC sweep: *democractic, NVDIA, omninous, unpredicatble, receipe/recipie, harbringers.* Suggest correct spelling. If the misspelling could be intentional voice (rare — the user's voice doesn't lean on misspellings), flag with a "(verify intentional)" note rather than auto-correcting.

### Hedge budget
- **Hedge inventory** — count exact uses of the explicit hedge list: *I think, I fear, perhaps, maybe, arguably, in my opinion, I want to, might, would likely, will likely, I believe.* Report total count. Substack goal's 1A criterion is **≤1 hedge per essay**. If count > 1, flag each instance and note which are most easily cut without losing argument (typically the close-paragraph hedges are the load-bearing cuts; steelman hedges are often defensible).

### Voice-drift patterns
**Cross-check the living voice profile.** The current active drift-watch list lives in `<writing-repo>/substack-draft-articles/voice-profile.md`, maintained after each ship by `/substack-pipeline`. Read it before sweeping — if a drift pattern has been added there since this skill was last edited, sweep for it too. The list below is the baseline.

These patterns are documented polish-mode insertions — phrases that appear in the about-to-publish version but weren't in the reviewed draft, softening voice under publish pressure. Flag every instance; the user decides whether each is genuine voice or drift. These are not "safe to ignore" — the session pattern is that all three have survived explicit flags at the review stage and made it to publish anyway.

- **Hope/wish insertion** — *"I hope"*, *"hopefully"*, *"I wish"*, *"I'd like to"*, *"my hope is"*. The primary drift pattern across three sessions. Flag every instance without exception.
- **Smiley/emoji** — `:)`, `:-)`, `😊`, `🙂`, or any emoji in the body text. Polish-mode additions that shift register from cheeky-direct to earnest-soft. Flag every instance — even if intentional, it should be a conscious decision made after the flag, not a slip.
- **Advisory close** — sentences in the final ~3 paragraphs addressed to a third party: *"for anyone who"*, *"for someone looking for"*, *"if you're someone who"*, *"anyone looking for X"*. These redirect from a positional "I" close to advice-to-others, diluting the ending. Flag only when the sentence appears in the closing section.
- **Earnest-affirmation phrase** — *"positive voice"*, *"positive impact"*, *"I hope these [thoughts/words] can"*, *"I believe in a [X] world"*, *"be a positive"*, *"useful and inspiring"*. Earnest-register insertions that fight against the cheeky-direct voice signature. Flag every instance.

### Style mechanics
- **Padding** — flag only the egregious phrases: *"in order to,"* *"the fact that,"* *"due to the fact that,"* *"it is important to note that."* Suggest the cut. Don't flag minor wordiness.
- **Missing oxford comma** — only flag if the list creates genuine ambiguity. Don't flag every series.

## What NOT to flag

- **Voice patterns** — pop-culture refs (Bond, NVIDIA-as-South-Park, Dune ~spice~), Australian-informal markers ("Yeh", "HOT"), cheeky-meta asides ("(cough American cough)"), intentional fragments. These are voice. Never flag. **Exception:** smileys and hope-clauses are flagged under *Voice-drift patterns* even when they may be intentional — the point is to surface them for a conscious keep/cut decision, not to auto-remove them.
- **Structural issues** — buried thesis, loops, salience, archetype mismatches. That's `/substack-reviewer`'s job.
- **Argument quality** — whether a claim is right, whether evidence holds. Out of scope.
- **Tone preferences** — "this feels too snarky" / "this is too formal." Not mechanical.
- **Word-choice preferences** — synonyms that don't change meaning. The skill suggests *fixes*, not *improvements*.

If you're tempted to flag something not on the vocabulary list, the answer is: don't. The skill's value is being narrow and deterministic, not opinionated.

## Where to write the output

Same pattern as `/substack-reviewer`:

- **Location.** Save alongside the draft (same folder as input file). For the user's drafts, that's `<writing-repo>/substack-draft-articles/<essay-slug>/`. Never save into the Obsidian vault.
- **Filename.** `polish-N.md`, where `N` is the next integer in the sequence. List the folder first: if no `polish-*.md` exists, use `polish-1.md`. Otherwise find the highest existing `N` and increment.
- **Chat response.** Two things only: (1) one line with the saved path, then (2) the flat issue list reproduced inline so the user sees the verdict without opening the file. If there are zero mechanical issues, the chat response is one line ("Saved to ./<path>. No mechanical issues found — ship-ready.") and the file says the same.

If the user says "just show me" or "don't save," print the list in chat and skip the file write.

## Output template

```markdown
**Mechanical sweep — `<essay-slug>` (draft: `<input-file>`)**

Hedge count: N / 1 budget [PASS / FAIL]
Voice-drift: N instances [CLEAN / REVIEW BEFORE SHIP]

**Issues (M total):**

1. **[Label]** — line N. *"exact quoted text"* → suggested fix.
2. **[Label]** — line N. *"exact quoted text"* → suggested fix.
[...]

(If zero issues on both: "No mechanical issues or voice-drift found. Ship-ready.")
```

That's the whole output. No preamble, no postscript, no "let me know if you want me to expand."

## Tone

- **Mechanical, not opinionated.** "Subject-verb disagreement" not "this reads awkwardly."
- **Exact quotes only.** Never paraphrase the error — quote it verbatim so the user can find it with cmd-F.
- **Suggest the fix concretely.** *"every non-compute countries"* → *"every non-compute country."* The user can accept or reject; the skill commits to a specific fix.
- **No "consider" or "you might want to."** Either it's a mechanical error or it isn't.

## What not to do

- **Don't rewrite passages.** Mechanical fixes only — substituting one word, fixing one agreement, breaking one em-dash chain. If a fix would require rewriting more than the immediate phrase, flag the issue and leave the fix to the user.
- **Don't cheerlead or grade.** No "good draft overall." No "B+." The output is the list, full stop.
- **Don't second-guess voice.** If something *might* be voice and you can't tell, leave it alone. Better to miss a real error than to flag voice as a mistake.
- **Don't manufacture findings.** If the draft is clean, say so. The skill's credibility depends on its silence on clean drafts being meaningful.
- **Don't reference past sweeps.** Each pass is a clean read. If the user fixes issues from sweep N and runs sweep N+1, treat it as fresh.

## Iteration

After the sweep, the user may:

- **Push back on a flag** ("that 'Yeh' is intentional — don't flag it"). Add the specific exception to working memory for this session, drop the flag, and move on. Don't re-flag the same thing later in the session.
- **Send a revised draft** for a re-sweep. Run the full process again. Don't reference the prior sweep.
- **Ask for an explanation of why a fix matters.** Give one sentence. Don't lecture.

## Example

**Input:** a near-final Substack draft with 4 grammar issues and 2 hedges.

**Output:**

```markdown
**Mechanical sweep — `future-isnt-just-compute` (draft: `draft-v5.md`)**

Hedge count: 2 / 1 budget [FAIL]
Voice-drift: 2 instances [REVIEW BEFORE SHIP]

**Issues (8 total):**

1. **Subject-verb disagreement** — line 18. *"AI labs has to cook their own recipe"* → *"AI labs have to cook."*
2. **Lead vs led** — line 33. *"AI-lead world"* → *"AI-led world."*
3. **It's vs its** — line 19. *"It's impact does not model"* → *"Its impact does not model"* (possessive, not contraction).
4. **Determiner-noun mismatch** — line 52. *"for every non-compute countries out there"* → *"every non-compute country"* or *"all non-compute countries."*
5. **Hedge inventory** — line 56. *"which AI lab will likely dominate"* — "likely" is a listed hedge. Cut for budget compliance.
6. **Hedge inventory** — line 15. *"both sides would likely disregard safety"* — "would likely" is a listed hedge; defensible in steelman context but counts against budget. If line 56's hedge is cut, this can stay.
7. **Hope/wish insertion** — line 61. *"I hope this resonates with anyone thinking about"* — not present in reviewed draft. Keep or cut.
8. **Advisory close** — line 63. *"for anyone looking for meaning in their work, an FDE role might actually be the right choice"* — advisory beat in closing section redirecting from positional "I". Keep or cut.
```
