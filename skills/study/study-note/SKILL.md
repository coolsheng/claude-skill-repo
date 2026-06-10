---
name: study-note
description: Capture an atomic insight from a study session as a linked Obsidian note. Designed for mid-session use — quick, low-friction, no breaking flow. Auto-tags the note with the active goal/competency/milestone (read from the goal's index.md) and files it under that goal's notes/ folder. Use whenever the user says something clicked, wants to "save this", "note that down", "capture this insight", or shares a realization mid-study. Invokable standalone (`/study-note`) or from inside `/study-plan` during Step 4.5 (mid-session) and Step 5 (synthesis). Does NOT replace the session log in log.md — that's still `/study-plan`'s job. Notes are the *what I learned*; the log is the *what I did*.
---

# Study Note — Atomic insight capture

The goal is **low friction**. The user just had something click. Capture it cleanly, link it to context, get out of the way.

## Vault paths
- Vault root: `<vault-root>/`
- Goal root: `Study/Goals/<slug>/`
- Notes folder: `Study/Goals/<slug>/notes/` (create on first use)

## Flow

### Step 1 — Determine context
If invoked from `/study-plan`, the active goal/competency/milestone is already known — use it directly, skip to Step 2.

If invoked standalone:
- Read `Study/README.md` for active goals.
- If exactly one active goal, assume that one. If multiple, ask which goal this note belongs to via `AskUserQuestion`.
- Read that goal's `index.md` to get current `active_competency` and `active_milestone`.

### Step 2 — Get the note from the user
The user has *already said the insight* in conversation, or is about to. Do NOT make them re-type it into a form. Either:

- **Extract from what they just said.** If they shared the insight in their last message (e.g. "oh — the reason attention is permutation-invariant without positional encodings is..."), use that verbatim as the body. Confirm: "Saving this as a note — title: `<X>`. Tweak or save as-is?"
- **Ask once, briefly.** If they said "save this" without context, ask: "What's the insight in one sentence?" Then propose a title from their answer.

The title should be a **claim or question**, not a topic. "Attention is permutation-invariant without positional encodings" beats "Attention notes." Atomic notes are about *one idea*.

### Step 3 — Look for links
Before writing, scan `Study/Goals/<slug>/notes/` for existing notes that might be related (same competency, overlapping concepts). If you find candidates, surface 1–3 as `[[wikilink]]` suggestions for the new note's body or a "Related" line. Don't force links — only if genuinely connected.

If the insight contradicts or refines an earlier note, flag it: "This sharpens [[earlier-note]] — want me to add a pointer there too?"

### Step 4 — Write the note
Filename: `YYYY-MM-DD-<short-kebab-slug>.md` in `Study/Goals/<slug>/notes/`. Use Sydney local date (run `TZ=Australia/Sydney date '+%Y-%m-%d'` if not already known from the parent session).

Format:

```markdown
---
date: YYYY-MM-DD
goal: <goal-slug>
competency: <active competency name>
milestone: <active milestone id, e.g. 3A>
tags: [study-note]
---

# <Title — a claim or question, not a topic>

<The insight, in the user's own words where possible. One short paragraph or a few bullets. Atomic — one idea per note.>

**Related:** [[other-note-slug]] (optional, only if real connection)
```

Keep the body tight. If the user gave you three sentences, write three sentences — don't pad. If they gave you a paragraph, keep the paragraph. Atomic ≠ skeletal; it means *one idea, fully expressed*.

### Step 4.5 — Pressure-test the insight (active recall)
A note that goes straight into the vault without resistance calcifies as fluency the user doesn't actually have. Before confirming, run a brief Socratic round to make the insight earn its place.

**Mid-session (invoked from `/study-plan` Step 4.5):** ask **2 questions max**. Keep friction low — the user is in flow.

**Synthesis or standalone:** ask **2–4 questions**, can go deeper.

Pick question types based on what's load-bearing in the claim. Don't ask all four — pick the 2 sharpest for *this* insight:

- **Mechanism — "why does this work?"** Forces them past the slogan to the underlying reason. Use when the insight is a *what* and the *why* is non-obvious.
- **Steelman — "what would someone who disagrees say?"** Forces them to hold the strongest counter, not the strawman. Use for any opinion, stance, or contested claim.
- **Failure mode — "where does this break? when would it NOT apply?"** Forces edge-case thinking. Use for any rule, heuristic, or pattern.
- **Concrete instance — "name a specific example from your own work / a paper / a real situation."** Forces them off abstraction. Use when the insight feels suspiciously clean or general.

Ask the questions **in conversation**, not in `AskUserQuestion` — this is dialogue, not a form. One at a time if the answer would change the next question; otherwise batch as a numbered list.

After the user answers:
- **If they answer cleanly**, confirm and save. The note stands.
- **If they retreat, hedge, or can't answer**, name it: *"Notice you couldn't defend the mechanism — that's a gap, not a failure. Want me to add a `**Gap:**` line to the note so future-you knows what to drill?"* Capturing the gap is more valuable than pretending it's not there.
- **If their answer sharpens the original claim**, offer to revise the note body before saving.

The user can always say "skip the quiz, just save" — respect it without argument. But default to asking; the friction is the point.

### Step 5 — Confirm and return
One line back to the user: `Saved → <title>` (don't show the file path). Then return to whatever they were doing. If invoked from `/study-plan`, hand control back to that flow without summarizing.

## When invoked from /study-plan Step 5 (synthesis)
Synthesis is where multiple insights get consolidated. If the user produced several notes this session, offer at the end:

> You captured N notes today. Want to consolidate them into a synthesis note, or leave them atomic?

Synthesis notes link to the atomic ones with `[[...]]` and live in the same `notes/` folder, prefixed `synthesis-` (e.g. `2026-05-17-synthesis-attention-mechanics.md`). Default to **leaving them atomic** unless the user wants to consolidate — premature synthesis loses information.

## Rules
- **No file paths or raw frontmatter shown to the user.** Saving is silent except for the one-line confirmation.
- **One idea per note.** If the user dumps three insights, propose three notes, not one.
- **Don't auto-link aggressively.** A bad `[[link]]` is worse than no link.
- **Never overwrite an existing file.** If the slug collides, append `-2`, `-3`, etc.
- **Don't ask permission for the obvious.** If the insight is clear from context, save it and confirm — don't run a four-question form.
- **The note is for future-you.** Write so a reader picking it up in 6 months understands the claim without needing the surrounding conversation.
