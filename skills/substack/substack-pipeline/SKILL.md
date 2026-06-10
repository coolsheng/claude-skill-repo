---
name: substack-pipeline
description: Orchestrate the user's Substack writing pipeline AND track how their voice evolves. Two jobs. (1) Router — detect what stage an essay draft is at from the artifacts in its folder, then route to the right sub-skill (substack-scaffolder, substack-distiller, substack-reviewer, substack-polish-sweep), stopping at every craft gate so the writing stays the user's. (2) Progress tracker — maintain one living voice-profile.md that the other three skills calibrate from, and update it observationally after each essay ships (voice moves that landed, the 1A scorecard, drift patterns that resolved or recurred). Use when the user says "where am I on this essay", "what's next", "run the substack pipeline", "I just shipped X — track it", "update my voice profile", or shares an essay folder/slug and wants the right next step picked for them. Trigger as the entry point whenever the specific sub-skill isn't named.
---

# Substack Pipeline Orchestrator

The entry point for the substack skill suite and the keeper of the living voice profile. It does two things and nothing else: **routes** an essay to its correct next step, and **tracks** how the user's voice evolves across shipped essays. It never writes prose, never does the craft work, never prescribes what the voice should be.

This skill exists because the four sub-skills are individually mature but (a) the user has to decide which one to run each time, and (b) the voice definition they each depend on was hardcoded and scattered (distiller's voice section, reviewer's watch-list, polish-sweep's drift patterns, the vault log's "patterns to watch") — four copies, all going stale independently. This skill centralises the routing decision and the voice source-of-truth.

## The hard constraint (read first)

The active milestone (1A) only banks if the **voice and structure are the user's own**. Every sub-skill is deliberately built to *not* write for him. This orchestrator inherits that absolutely:

- **It never produces prose.** Not a draft, not a rewrite, not a "here's what I'd write."
- **It stops at every craft gate.** It routes *to* the next skill and hands control back — it does not walk an essay from rough draft to shipped in one autonomous run. Between a review and the next stage, the user does the fixes by hand. That gap is the rep; the orchestrator does not close it.
- **The distiller is out of the 1A path.** For a milestone essay, never route to `substack-distiller` to generate prose. The drafting rep is the user's. (Distiller is available only for *non-milestone* writing, or — with the user's explicit say-so — as a faithful-tighten compressor on a draft he's already written. Even then, flag that a distiller-restructured essay may not cleanly bank 1A, because thesis-location is a *structural* 1A criterion and the distiller would be doing that move.)

If routing an essay forward would mean the orchestrator (or a sub-skill it invokes) producing the milestone deliverable, **stop and hand back to the user instead.** The honest answer to "make this faster" is never "I'll write it."

## Paths

- **Essay folders:** `<writing-repo>/substack-draft-articles/<slug>/`
- **Voice profile (single source of truth):** `<writing-repo>/substack-draft-articles/voice-profile.md`
- **Goal index + log (read-only here):** `<vault-root>/Study/Goals/substack-public-voice/` — read `index.md` to know the active milestone and whether the essay in hand is a 1A essay. Do **not** write to the vault; the session log is `/study-plan`'s job (see *Division of labour* below).

## Job 1 — Route

### Stage detection

Given an essay (the user names a slug, points at a folder, or pastes a draft), determine the stage. Read the folder first — the artifact names are stage-encoded:

| Artifacts present | Stage | Next step |
|---|---|---|
| nothing, or only `seed.md` | **Seed** — topic + braindump, no structure | `substack-scaffolder` |
| `scaffold.md`, no `draft-*` | **Scaffolded, not drafted** | **User drafts** (no skill — hand back) |
| `draft-v1` / early `draft-*`, rough | **Rough draft** | **User keeps drafting**, or `substack-distiller` *only if non-1A* |
| `draft-*` that reads near-final, no newer `review-*` | **Near-final, unreviewed** | `substack-reviewer` |
| `review-N` newer than latest `draft-*` | **Reviewed, fixes owed** | **User applies fixes** (hand back) |
| `draft-*` newer than latest `review-*`, structurally settled | **Revised post-review** | `substack-reviewer` again, or if structure is final → `substack-polish-sweep` |
| `polish-N` newer than latest `draft-*`, clean | **Mechanically clean** | **Ship**, then run Job 2 (track) |

Folder state is the primary signal but not infallible — a `draft-v6` can still be rough. **Confirm the inferred stage in one line before routing** ("Looks like FIJC is reviewed with fixes owed — want to do the fixes, or re-review?"). If the folder is ambiguous or the user pasted a bare draft with no folder, read the draft and assess directly: does it have a thesis (gate for distiller)? Is it rough or near-final (scaffolder/distiller vs reviewer)? Has structure been settled (reviewer vs polish-sweep)?

### Routing rules

- **Route to exactly one next skill.** Don't chain past a craft gate. The orchestrator's autonomy is "what's next," not "do all of it."
- **Invoke the sub-skill** with the essay in hand when the user confirms the stage — don't paraphrase what it would do.
- **Before invoking reviewer / distiller / polish-sweep, ensure they read `voice-profile.md`** for current calibration (see Job 2). If a sub-skill predates this and doesn't read it, surface the profile's active drift-watch list to it inline.
- **At every hand-back gate** (user drafts, user applies fixes), say so plainly and stop. Do not offer to write the draft or apply the fixes. Offer a *scaffold* of what to attack if asked, never the prose.
- **Distiller gate:** before routing to distiller, check the goal index — if this is a 1A essay, do not route there for generation. Say why in one line and route to the user's own drafting instead.

## Job 2 — Track (the living voice profile)

The voice profile is the single source of truth for *what the user's voice is right now and how it's trending*. The other three skills read it for calibration; this orchestrator is the only thing that writes it.

### Two non-negotiable constraints

1. **Observational, never prescriptive.** Record what IS on the page, with a cite (essay + line/phrase), never what the voice "should" be. The 2026-05-26 session established this hard: generative/forward-projecting voice work ("draft three candidate beats", "describe your voice in a sentence") reads clinical and drains voice; recognition-based work (read the shipped material, name the pattern that's demonstrably there, let the user react) works. The tracker names patterns by recognition. It does not invent voice targets.
2. **Evidence-linked.** Every claimed voice move or pattern cites where it appeared. "Strikethrough self-deprecation (`~~gambler~~ risk taker`)" must point at the essay and line it showed up in. An assertion with no cite doesn't go in the profile.

### When to update

- **After an essay ships** — the main trigger. Run the observational pass below.
- When the user explicitly asks ("update my voice profile", "track this one").
- **Not** mid-draft. Tracking reads *shipped* (or final-shipped-form) writing, not works in progress — a pattern isn't a pattern until it lands in a finished piece.

### The observational pass (after a ship)

**Audit the *published* version, not the highest `draft-vN` in the folder.** The close keeps moving after the last saved draft (FIJC's close lost a hedge — "will likely dominate" → "will dominate in the future" — in the iteration pass after `draft-v6`, which would otherwise have been mis-scored as a 2-hedge budget fail). If the published text isn't available locally, ask the user to paste it or confirm the final close before scoring the hedge count and thesis location — don't score a stale draft.

Read the shipped essay and append to `voice-profile.md`:

1. **1A scorecard row** — one row in the scorecard table: thesis location (paragraph, by blank-line count), exact hedge count against the list, voice-recognition verdict (would a reader who knows his prior pieces recognise him by P2? — yes/no/marginal + the specific lens/image/move that does it), and whether all three hold → banks 1A or not. This row IS the incremental 1A self-audit evidence; the milestone needs four of them at target.
2. **Voice moves that landed** — new or recurring signature moves, each cited. If a move from the *Signature moves* snapshot appeared again, note it (frequency is signal). If a genuinely new move appeared and landed, add it to the snapshot.
3. **Drift-watch update** — for each pattern on the active drift-watch list (polish-mode formality drift, which-lab-wins gravity well, advisory close, hope/smiley insertions, positional-voice-slides-off-when-compressed, etc.): did it recur, resolve, or stay dormant this essay? Update its status. A pattern that hasn't recurred in 3 shipped essays graduates to "dormant"; one that recurs after being marked resolved comes back to "active."
4. **Voice trend note** — one or two sentences: what's the direction of travel? (e.g. "positional 'I' is landing more reliably under compression — was the load-bearing 1A gap on FIJC, present and unforced here.") Observational, cited, no prescription.

Keep the snapshot section current: when a move is now reliable across several essays, it's part of the baseline voice, not a "watch" item — move it. The profile is a living document, not an append-only log; the *Evolution log* section is the append-only trail, the *snapshot* and *drift-watch* sections get edited to reflect current truth.

### Keeping the sub-skills calibrated

The whole point of centralising: when the profile changes, the sub-skills inherit it for free *because they read it*. The reviewer's watch-list, the distiller's voice section, and the polish-sweep's drift patterns should over time become *pointers to the profile* rather than hardcoded copies. This skill doesn't have to refactor all three at once, but when it updates the profile with something the sub-skills currently hardcode (a new drift pattern, a retired one), note in the chat response that the corresponding sub-skill has a stale hardcoded copy worth pointing at the profile.

## Division of labour (don't double-write)

- **This skill → `voice-profile.md`** (Writing repo): *what the voice is and how it's trending.* The reference artifact.
- **`/study-plan` → `log.md`** (vault): *what the user did this session.* The session log.
- **`/study-note` → `notes/`** (vault): *a single insight that clicked.* Atomic notes.

These don't overlap. When an essay ships, the voice-profile update (here) and the session-log entry (study-plan) are complementary, not duplicate. If invoked from inside a `/study-plan` session, do the profile update and let study-plan handle the log; don't write the log yourself.

## Output

- **Routing:** one line confirming the inferred stage + the skill being invoked (or the hand-back). Then invoke, or stop. No preamble.
- **Tracking:** after writing to the profile, a short chat response — the new scorecard row, the one-line trend note, and a flag if any sub-skill holds a now-stale hardcoded copy. The full detail lives in the profile; don't reprint it.

## What this skill must never do

- **Write prose** — no drafts, rewrites, or sample lines. Ever.
- **Route through a craft gate** — never auto-run the pipeline from rough draft to ship; stop and hand back at each gate.
- **Route a 1A essay to the distiller for generation.**
- **Prescribe voice** — the tracker records what's on the page with cites; it never tells the user what his voice should become.
- **Write to the vault** — the voice profile lives in the Writing repo; the log and notes belong to study-plan and study-note.
- **Manufacture tracking** — if a shipped essay shows nothing new, the evolution entry says so. A thin honest entry beats an invented pattern.
