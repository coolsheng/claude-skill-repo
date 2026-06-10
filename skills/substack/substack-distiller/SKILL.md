---
name: substack-distiller
description: Distill a messy braindump, bloated draft, or bullets+salient-lines into a coherent Substack article in the user's voice. Produces TWO passes — a faithful tighten that preserves the user's exact lines and structure, then a bolder rewrite that's freer with phrasing — so the user can mix-and-match. Gates on thesis: if the input has no clear claim or the claim isn't earned by the material, the skill refuses to distill and surfaces the problem first. Use whenever the user shares conversational writing, a voice-memo-style braindump, or a too-long draft and wants it shaped into a publishable post — phrasings like "tighten this", "distill this into a post", "turn this into a Substack article", "make this coherent", "clean this up", "two passes — faithful and bolder", or sharing a draft alongside scattered notes all qualify. Trigger even when the word "Substack" isn't used, as long as the input is rough longform-style writing meant for publication.
---

# Substack Distiller

A skill for compressing the user's conversational drafts into publishable Substack posts in their voice, without laundering weak ideas.

## What this skill is and isn't

**Is:** a stylistic distiller and structural compressor. Takes rough input → two polished drafts (faithful + bolder).

**Isn't:** a reviewer (`substack-reviewer` does that — three named flaws). Isn't a scaffolder (`substack-scaffolder` turns a topic + braindump into an outline *before* writing). This skill assumes content exists and needs to be *shaped*.

If the user asks for a critique or outline rather than a finished draft, suggest the other two skills.

## The thesis gate (do this first)

Before producing any draft, read the input and identify the thesis — the single claim the piece is making. Then ask:

1. **Is there a thesis at all?** Not a topic ("AI trading"), a *claim* ("AI magnifies the trader you already are; it doesn't replace the judgment").
2. **Is the claim earned by the material?** Do the anecdotes, examples, and reasoning in the input actually support it? Or is the claim a punchline glued to material that's pointing somewhere else?
3. **Is the claim non-trivial?** "You should be passionate" isn't a thesis — it's a platitude. "You're not boring, you're a bad storyteller — and the fix is treating your life as material" is a thesis because it reframes.

If any of these fail, **stop**. Don't distill. Surface the problem in 2-4 sentences — what the thesis seems to be, why it's not landing, and one or two concrete questions to push on. Then ask whether the user wants to address them before proceeding.

The reason for this gate: this skill's job is to make the user's writing *more* itself, not to make weak ideas sound clever. A polished voice on a weak claim is voice-laundering — it actively damages the Substack by training readers to expect insight and delivering rhythm.

If the thesis passes, proceed silently — don't preamble about it. Just produce the two drafts.

## The user's voice (read this carefully)

**Read the living voice profile first.** Before distilling, read `<writing-repo>/substack-draft-articles/voice-profile.md` — it's the current, evidence-linked snapshot of the user's voice and signature moves, maintained after each ship by `/substack-pipeline`. The section below is a fuller written-out reference, but where the profile is more current (a new signature move, a retired one), the profile wins. If the profile is missing, use the section below.

The canonical references are his published pieces:
- `<url-of-published-post-1>` (AI trading)
- `<url-of-published-post-2>` (storytelling)

These are the *exemplars*, not a rigid template. The voice will evolve; lean on the patterns below as the current snapshot, and if the input itself uses a fresh device that feels in-voice, keep it.

### The single most important calibration: storyteller, not explainer

The user's voice is a *reflective storyteller* — they show you a scene, let you sit in it, and then name what they felt. They are **not** an explainer or thought-leader. The difference is subtle but it's the failure mode the skill needs to defend against hardest, because AI writing defaults to explainer voice.

**Storyteller voice:** "I wiped a production database on a Friday afternoon. We fixed it that night. Nine engineers learned from a mistake they didn't have to make."

**Explainer voice (off):** "Here's the thing about old-school engineering — failure was actually a feature, not a bug. Let me tell you why that matters."

Storyteller voice trusts the reader to feel the point. Explainer voice tells the reader what the point is. When in doubt, **cut the framing and keep the scene**.

There's also an emotional register to preserve. When the input contains something quiet and personal — loneliness, fear, loss, a thing the author misses — *that's the spine of the post*, not decoration around the argument. The structural claim ("we no longer share failure") might be the thesis, but the emotional thread ("I miss this") is what makes the thesis matter. Preserve emotional throughlines explicitly. Don't let them get cut as "tangential" while the argument gets tightened.

### Signature moves

**Pull-quote interlocutor.** A skeptical fake-reader question, formatted as a blockquote, used to transition between beats:
```
> "But why?"

Everyone should be a better story teller because...
```
Use these sparingly — 2-4 per post. They drive rhythm, not structure. Don't overdo or they read as gimmicky.

**Standalone aphorism as section landing.** A single bold or italic line that lands a beat:
- *The riskiest thing you can do in a casino is to win*
- *It's like Thor's hammer, you should only hold it if you're worthy*
- *Things with passion are infinitely more interesting than things without.*

These typically follow a paragraph of build-up, then sit alone on their own line. They're the "salient lines" — the takeaways readers screenshot. Aim for 2-4 per post.

**Short paragraphs.** Often one sentence. White space does work. If a paragraph has more than three sentences, ask whether it should be broken.

**Strikethrough self-deprecation.** `~~gambler~~ risk taker`. Sparing, one or two per post max, used to puncture his own seriousness.

**Em-dashes and italics for emphasis.** Bold is rare. Italics for stress, em-dashes for pivots — like this. Avoid the overuse of bold that AI-written prose defaults to.

**Light section headers as scene breaks.** `## How did I get here?`, `## The Outcome`, `## Closing Thoughts`. Headers are conversational, not corporate. Avoid headers like "Key Takeaways" or "Conclusion."

**Philosophical pivot near the end.** Both reference pieces swerve from the concrete anecdote (trading P&L, water-cooler talk) into a broader claim about agency, identity, or how to live. This isn't optional — it's the move that lifts a post from "thing that happened" to "thing worth reading." If the input doesn't contain raw material for this pivot, flag it in the diff note rather than fabricating one.

**Casual sign-off.** Sometimes a `:)`, sometimes a shout-out, sometimes a one-line aphorism. Not "In conclusion."

### Tone calibration

- **Australian English.** "realised", "haemorrhaging", "aye" — keep these.
- **First person, conversational.** "I've", "I am", "I do not think" — contractions are fine but not forced.
- **Self-aware, not self-important.** When a claim sounds grand, the next line often punctures it.
- **No corporate hedging.** Avoid "it could be argued", "some might say", "in my opinion" — the user asserts, then earns it.
- **No AI-tells.** No "delve", "tapestry", "in the realm of", "navigate the complexities", "it's important to note", parallel-structure triplets, or sentences that fear committing.
- **No LinkedIn / thought-leader / explainer tells.** This is the most common drift. Banned openings and connectives include:
  - "Here's the thing —"
  - "Here's what nobody tells you —"
  - "Let me tell you —"
  - "The truth is —"
  - "But here's the catch —" (occasional use is fine, but it's a crutch — prefer just *showing* the catch)
  - "The counter-argument writes itself" (lazy — either write the counter-argument or trust the reader to see it)
  - "It's not just X, it's Y" (a real line in this voice uses this construction sparingly with specific content; the empty rhetorical version is off)
  - "X isn't a [noun], it's a [noun]." — same problem when used as filler rather than for a sharp specific reframe
  - "And that's the [point/lesson/thing]."
  - Any phrase that announces a takeaway is coming instead of just delivering it.
  
  The test: if the sentence is doing rhetorical *setup* rather than carrying content or feeling, cut it. The reader knows a point is coming — they don't need to be warned.

- **No knowing-narrator moves.** This is a subtle but distinct failure mode. Avoid phrases that gesture at shared knowing with the reader rather than just stating the thing:
  - "You already know which one I'd pick."
  - "We both know how this ends."
  - "I think we can all agree —"
  - "You know the feeling."
  - "If you've ever [X], you know what I mean."
  - "There's something we don't talk about —"
  - Any closing that winks at the reader instead of landing the point.
  
  These look like intimacy with the reader, but the intimacy is unearned — they ask the reader to nod along rather than handing them the thing and letting them sit with it. The user's voice trusts the reader by *being direct*, not by *winking*. Compare: *"It's the company."* (direct, trusting) vs *"You already know what I'd say."* (performative, gesturing).
  
  The test: if a closing line gestures at what's coming rather than *being* what's coming, cut it. Three direct words almost always beat a sentence of knowing-gesture.

## The two passes

### Pass 1 — Faithful tighten

Goal: the post the user would write if they had more time to edit themselves.

- **Preserve his exact lines wherever they already land.** If a sentence in the input is already in-voice, keep it verbatim. Don't paraphrase what's already working.
- **Preserve his structural choices** — section order, anecdote sequence, where the pivot sits.
- **Cut bloat.** Repeated points, throat-clearing, sentences that say the same thing twice with different words. Be ruthless about this — it's the main lift.
- **Slot signature moves** where the rhythm calls for them. If the input has a buried aphorism inside a paragraph, pull it out onto its own line. If there's a natural skeptical-reader moment, formalize it as a pull-quote interlocutor.
- **Fix the closing** if it trails off. The philosophical pivot needs to land.

If you find yourself rewriting more than ~30% of the words, you've drifted from "faithful tighten" into "bolder rewrite." Pull back.

### Pass 2 — Bolder rewrite

Goal: a structurally different shot at the same thesis, in the same voice.

**The two failure modes Pass 2 must avoid:**

1. **Drifting into thought-leader voice.** Adding declarative explainer-isms, rhetorical scaffolding ("Here's the thing", "The counter-argument writes itself"), or switching from reflective to instructive. Pass 2 stays in the user's reflective storyteller register.

2. **Looking like Pass 1 with synonyms.** If Pass 2 has the same opening hook, the same section order, the same pivot placement, and the same closing structure as Pass 1, it has failed. The user gets two passes precisely because they want to see *the same idea shaped two different ways* — if both passes converge on the same shape, the skill is wasting their reading time.

**Pass 2 must differ from Pass 1 on at least two of these structural axes:**
- **Opening hook** — different first line, different first scene, different angle of entry. (If Pass 1 opens with the anecdote, Pass 2 might open with the present-day observation. If Pass 1 opens with the rhetorical question, Pass 2 opens with the scene.)
- **Section order or count** — collapse two sections into one, split one into two, reorder them, or remove section headers entirely.
- **Pivot placement** — move the philosophical pivot earlier or later in the piece.
- **Aphorism placement** — surface a different line as the salient takeaway, or place the same aphorism in a different structural position.
- **Closing shape** — if Pass 1 ends on a punchline-triple ("Neither. / It's the company."), Pass 2 might end on a longer reflective beat, or vice versa. The *thesis* the closing lands is the same; the *shape* of how it lands differs.

What "bolder" actually means, executed in-voice:
- **Cut more.** Pass 2 is usually shorter than Pass 1, not longer. Confidence is brevity.
- **Sharper signature moves** — better-placed interlocutor, a more landed aphorism, a closing that lands harder.
- **One creative liberty** — pick one thing in the piece to take a real risk with: a metaphor, a structural choice, an opening, a single image. Don't take liberties everywhere or it stops being recognisably the same post.

What "bolder" must NOT mean:
- Adding declarative thought-leader sentences ("Here's what nobody tells you")
- Adding rhetorical scaffolding ("The counter-argument writes itself")
- Switching from reflective to instructive
- Adding "punchy" lines that don't carry feeling, only rhythm

**Same thesis. Same anecdotes. Same emotional register. Same voice.** Don't invent material. The bolder pass should read like the user wrote it on a different day, having made different structural calls — not like a different writer wrote it, and not like the same writer wrote it twice.

## Output format

**Write to disk, don't print.** The drafts go into a `README.md` file — not the chat response. The chat response is just a short pointer to the file plus the diff note.

### The README file

Write to `README.md` inside a new folder under the current working directory (default: `<writing-repo>`).

- **Folder name.** Derive from the post's thesis or working title — short, kebab-case, 2-5 words. Examples: `failure-has-no-audience`, `youre-not-boring`, `ai-trading-workflow`. Pick from the title or the most salient aphorism, not from the input filename.
- **If the folder already exists**, append a short disambiguator (`-v2`, `-2026-05-14`) rather than overwriting. Never clobber existing work without checking.
- **File contents**, in this order, separated by `---`:

```
## Pass 1 — Faithful tighten

[full article in Markdown, ready to paste into Substack]

---

## Pass 2 — Bolder rewrite

[full article in Markdown, ready to paste into Substack]

---

## Diff note

- [2-5 bullets on what changed between the passes and why]
- [Flag anything missing — e.g., "the philosophical pivot is thin because the input didn't have raw material for it; consider adding X"]
- [Flag any line you cut from the input that you think might be worth keeping despite the cut]
```

No frontmatter, no extra wrapper.

### The chat response

After writing the file, output only:

1. One line with the saved path, e.g. `Saved to ./failure-has-no-audience/README.md`.
2. The diff note (same bullets as in the file) — so the user can see the seams without opening the file.

Do **not** print Pass 1 or Pass 2 in the chat response. They live in the README.

The diff note is what makes this skill collaborative rather than a black box — it gives the user the seams to mix-and-match lines between passes and to see what got dropped. That's why it appears in both the file and the chat response.

If the user explicitly says "don't save" or "just show me", flip the behaviour: print both passes + diff note in the chat response and skip the file write.

## Anti-patterns to avoid

- **Don't preamble.** No "Great draft! Here's the distilled version:" — straight into Pass 1.
- **Don't soften the thesis to make it more palatable.** The user's voice is assertive; hedging is off-voice.
- **Don't add material the input didn't have.** No invented anecdotes, no statistics, no quotes from imaginary experts. If a beat needs more material to land, flag it in the diff note rather than fabricating.
- **Don't normalize Australian spelling to American.**
- **Don't impose corporate structure** — no "TL;DR" boxes, no bulleted "Key takeaways", no numbered "5 lessons learned" headings unless the input was already structured that way and it works.
- **Don't over-aphorize.** Three to four salient lines per post is the target. Twelve is parody.
- **Don't write a different post.** Both passes must serve the *same* thesis the input was reaching for. If you think the input is reaching for a different thesis than it states, surface that in the diff note — don't silently substitute.

## When the input is mixed (braindump + bullets + draft)

This is the common case. Treat it as one corpus:
1. Pull the thesis from whichever piece states it clearest (often the bullets, sometimes a single sentence buried in the draft).
2. Pull anecdotes and examples from the braindump.
3. Pull the existing draft's structure as the starting skeleton, but don't be precious — if a braindump fragment lands harder than a drafted paragraph, use the fragment.
4. The "salient lines" the user marks (or that obviously read as aphorism-shaped) are sacrosanct in Pass 1 — keep them verbatim. In Pass 2 they're still preserved unless you can do measurably better.
