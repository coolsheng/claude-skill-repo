---
name: substack-scaffolder
description: Scaffold a Substack article (or blog post / longform essay) from a broad topic idea plus a rough braindump of thoughts. Produces a single recommended outline with the user's braindump fragments slotted as bullets under each heading, plus 1-2 alternative angles for the same material. Use this skill whenever the user wants to "kickstart", "scaffold", "outline", or "structure" a Substack post, blog post, essay, or longform piece — especially when they share a topic plus a messy collection of notes/fragments and want help organizing them into sections they can fill in themselves. Trigger even if the word "Substack" isn't used — phrasings like "help me start writing this", "I have all these thoughts on X, help me organize them into an essay", "what's the structure for an article about Y given these notes", or "turn this braindump into an outline" all qualify.
---
 
# Substack Article Scaffolder
 
A skill for turning a topic idea plus a messy braindump into a structured outline the user can fill in themselves. The output is a *scaffold*, not a draft. The user is the writer; this skill just hands them the shape.
 
## What the user wants
 
The user has an idea for an article and a pile of unsorted thoughts about it. They want to see the *shape* of the piece — narrative beats with their fragments organized under each one — so they can sit down and write into it. The beats are scaffolding for them to write against; they may end up as visible section headers in the final post, or they may dissolve into smooth flowing prose with implicit transitions. Either way, what the user wants from the skill is structure, not prose.
 
## What to produce
 
Output exactly two things, in this order:
 
### 1. The recommended outline
 
A working title, a one-line thesis, then 4-6 headings (narrative beats — see below) with the user's braindump fragments slotted as bullets under each. No prose. No purpose-notes. No transition copy. Just the structure.
 
### 2. Alternative angles
 
After the outline, list 1-2 *different shapes* the same material could take. One sentence each. Don't shuffle headings of the same archetype — propose genuinely different framings (e.g. if the recommendation is thesis-driven, alternatives might be narrative or steel-man). The point is to give the user a real choice, not the illusion of one.
 
## Output template
 
Use this exact format:
 
```markdown
**Working title:** [title]
 
**Thesis in one line:** [the central claim or arc, in one sentence]
 
---
 
## [Section 1 heading]
- [braindump fragment, lightly cleaned]
- [braindump fragment]
 
## [Section 2 heading]
- [braindump fragment]
 
## [Section 3 heading]
- [braindump fragment]
- [braindump fragment]
 
[etc. — usually 4-6 sections total]
 
---
 
**Alternative angles:**
- *[Angle name]*: [one sentence describing how the piece would be framed differently]
- *[Angle name]*: [one sentence]
```
 
That's the whole output. Don't add a preamble ("Here's your outline!"), don't add a postscript ("let me know if you want changes!"), don't summarize what you did. The user is fluent in this format and just wants the goods.
 
## Choosing the structure
 
Read the braindump and figure out what's actually being argued or explored before picking a shape. Most longform writing fits one of these archetypes:
 
- **Thesis-driven**: hook → claim → evidence → counterargument → restate
- **Explainer**: what this is → why it matters → how it works → implications
- **Narrative**: setup → turn → realization → so what
- **Steel-man / contrarian**: their best argument → my counter → what's actually going on
- **Reaction / live analysis**: the event → why the consensus take is wrong → what to watch
- **Mechanism breakdown**: phenomenon → cause 1 → cause 2 → cause 3 → consequence
- **Inventory / listicle**: premise → items → synthesis
Pick whichever shape best fits the *content* of the braindump, not whichever is most familiar. Signals to read:
 
- Braindump has a clear claim plus supporting evidence and a likely objection? → thesis-driven.
- Mostly "here's what's happening and why it's surprising"? → explainer or reaction.
- User is processing something through personal experience? → narrative.
- User is arguing against a prevailing view? → steel-man or contrarian.
- Braindump is a list of distinct items with a common theme? → inventory.
Then ask: of the *other* archetypes, which one or two would also produce a coherent piece from this material? Those are the alternatives.
 
## Slotting the fragments
 
Every fragment in the braindump should land somewhere in the outline. Don't drop fragments silently — if a fragment genuinely doesn't fit the recommended structure, that's a signal the structure is wrong, not that the fragment should be cut. Try a different shape.
 
When slotting, lightly clean the language (typos, filler words, fix grammar) but preserve the user's voice and specific phrasings. Don't paraphrase claims into something blander. If the braindump says "BoJ hike is the live binary, everything else is noise," keep that energy — don't soften it to "the BoJ decision appears to be a key catalyst." The user wrote it that way for a reason; their voice is part of what makes the piece theirs.
 
Order bullets within a section logically (general → specific, weakest → strongest, or chronological), not in the order they appeared in the braindump.
 
## Headings as narrative beats, not section labels
 
The headings in the scaffold are *narrative beats* — anchors for what each part of the piece is doing — not necessarily section dividers the reader will see. Many Substack pieces flow as continuous prose with implicit structural moves rather than literal `##` headers; the writer decides later whether to expose each beat as a bold header, an italic divider, or just a paragraph transition inside the prose. So write headings that work as scaffolding for the writer's thinking, not labels announcing topics to a reader.
 
This means: avoid formulaic essay-trope headings. They feel hollow and generic, and they read as "here comes the next section of an essay" rather than "here is the next thread of thought." Specifically don't write headings in any of these templates:
 
- "What I learned by [X]"
- "Lessons from [topic]"
- "How I got into [thing]"
- "The day I realized..."
- "A reflection on..."
- "The questions I keep coming back to" (any "the [noun] I [verb]" template)
- "My journey with [X]"
These read as soulless because they describe the *meta-shape* of the essay (a reflection, a lesson, a journey) rather than the *content* of that beat. They break the spell of the piece before it starts.
 
What works instead:
 
- A specific image, scene, or moment: *"Two weeks in, I broke staging"*
- A claim the beat is making: *"Failure used to be a team sport"*
- A question the beat sits in: *"Are we lonelier now?"*
- A juxtaposition: *"Less broken, more alone"*
- A phrase pulled directly from the user's own braindump — often the strongest move, because it's their voice already sharpened to a point
The test: would a reader skim this heading and feel the *texture* of that thread, or would they feel the *genre* of an essay? Aim for the first.
 
## The headings should form an arc
 
Individual headings need to be evocative, but they also need to *connect*. Read the scaffold's headings in sequence, top to bottom, as if they were the only thing on the page. Do they tell a mini-story? Does each one hand off to the next? Or do they read as five disconnected slogans arranged in some order?
 
The chain of headings is the spine of the piece. A few techniques that help them link:
 
- **Lexical echo** — carry a word or image from one beat into the next. *"Now it gets caught before anyone sees"* → *"Less broken, more alone"* → *"Are we lonelier now?"* The alone / lonelier thread tightens the back half of the piece without being announced.
- **Parallelism** to mark related beats. Two consecutive *"used to be..."* headings make the pivot to the next *"Now..."* heading land harder. The repetition does the work.
- **Contrast pivot** to mark a turn. An explicit *then / now* structure, a heading that opens with *"But"* or *"Until,"* or a juxtaposition that flips the previous beat.
- **Cause → consequence** chains. A beat describing a state, followed by a beat describing what that state produces.
Test: read just the headings, top to bottom, ignoring the bullets. Do they sketch the shape of the piece on their own? If they read as a coherent skeleton — past, pivot, present, tension, resolution — the scaffold is doing its job. If they read as five independent claims that happen to be next to each other, tighten the links. Sometimes this means rewording one heading to echo a phrase from the next. Sometimes it means reordering. Sometimes it means recognising that the structure itself is wrong and the piece wants a different archetype.
 
## Beat count
 
4-6 beats is the sweet spot for most pieces. Three feels skeletal; eight feels like a textbook chapter. Within that range, let the content decide.
 
For very short pieces (<800 words), 3 beats is enough. For deep dives (>2500 words), 6-7 is fine. Don't pad with empty beats to hit a count.
 
## When the input is thin
 
If the user gives only a topic with no braindump, produce a leaner outline — 3-4 beats, no bullets — and one alternative angle. Don't refuse, don't run an interview. They're trying to start writing, not get questioned.
 
If the user gives only a braindump with no clear topic, infer the topic from the fragments and surface it as the working title plus thesis line. They can correct it.
 
If the braindump genuinely doesn't cohere — fragments point in unrelated directions — say so briefly (one line) and offer to scaffold around the strongest thread, with the others held aside.
 
## What not to do
 
- Don't write prose. No section intros, no transitions, no "in this piece I'll argue..." opener. The user is the writer.
- Don't add purpose-of-section notes ("this section establishes the context for..."). The user explicitly doesn't want these — clean headings only.
- Don't fact-check or editorialize the braindump *inside* the scaffold. If something seems off, you can flag it briefly *after* the output, but the scaffold itself should reflect the user's intended argument.
- Don't pad with generic writing advice ("consider a strong hook," "know your audience"). The user knows.
- Don't write the article. The whole point is that they fill it in.
- Don't ask follow-up questions before producing the output. Produce it first; the user can iterate.
## Saving the scaffold

After producing the scaffold inline, check whether a relevant draft directory already exists under `<writing-repo>/substack-draft-articles/`. The directory is usually named after a phrase from the piece — a heading, a thesis fragment, or a working-title slug (e.g. `caught-before-anyone-sees/`).

- If a clearly matching directory exists, save the scaffold to `<that-dir>/scaffold.md` using the same template as the inline output.
- If `scaffold.md` already exists there, overwrite the body with the new version (the directory always holds the current scaffold) AND append a changelog entry at the bottom of the file under a `## Changelog` heading. Each entry is one date-stamped line summarising what changed since the previous version — e.g. archetype switched, beats reordered, headings renamed, new fragments slotted, thesis sharpened. Date format: `YYYY-MM-DD`. Keep entries terse; the diff is the source of truth, the changelog is the human-readable trail.
- If no `## Changelog` heading exists yet (first overwrite), create one at the end of the file before adding the entry.
- If no matching directory exists, do not create one and do not save — the user hasn't started a draft folder for this piece yet.
- Match on semantic relevance, not exact-string match. If you're unsure whether a directory belongs to this piece, ask the user in one line rather than guessing.

Don't announce the save with prose; a one-line confirmation after the scaffold is enough.

## Iteration
 
After delivering the scaffold, the user will often want to:
 
- Pick one of the alternative angles and have it expanded into a full outline → just regenerate using that archetype.
- Add or remove beats → adjust and re-output the whole scaffold so they have a clean version.
- Hand you more braindump fragments → re-slot everything; don't just append the new ones to the end.
Default to re-outputting the whole scaffold rather than describing changes, so the user always has one clean current version they can copy.
 
## Example
 
**Input from user:**
> "I want to write about why most retail options traders should never sell premium. My braindump:
> - vol-of-vol kills you when you're short
> - tail risk is mispriced systemically
> - the seductive thing is the high win rate, it flatters you
> - Taleb is right but for slightly the wrong reasons
> - your real edge as a retail trader is asymmetric payoffs, not theta
> - market makers can hedge gamma you can't
> - I've blown up twice this way
> - the math on a 90% win rate strategy looks great until the 10% shows up clustered"
 
**Output:**
 
**Working title:** Stop Selling Premium
 
**Thesis in one line:** Retail traders systematically misallocate to short-vol because the high win rate flatters them, when their actual edge sits on the long-convexity side they can't capture as sellers.
 
---
 
## The seductive math
- The win rate looks great — that's the whole problem
- The math on a 90% win rate strategy looks great until the 10% shows up clustered
- I've blown up twice this way
- Taleb is right, but for slightly the wrong reasons
## What you're actually short
- Vol-of-vol kills you when you're short — the second-order move is what gets you
- Tail risk is mispriced systemically, and as a seller you're the one absorbing it
- Market makers can hedge gamma in ways retail can't
## Where retail edge actually lives
- Your real edge isn't theta — it's asymmetric payoffs
- Convexity rewards small accounts, not big ones
## Buy convexity, not theta
- [no fragment yet — heading is the claim the closing beat lands on; fill in]
---
 
**Alternative angles:**
- *Personal post-mortem*: open with the two blowups and let the structural argument emerge from the wreckage, rather than arguing the thesis upfront.
- *Steel-man the premium sellers*: lead with the strongest case for selling premium (income, defined risk, institutions do it) and then dismantle each pillar.