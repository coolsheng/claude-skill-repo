---
name: study-plan
description: Plan today's study session(s) dynamically against one or more active goals. Reads the user's competencies + active milestones from the Obsidian vault, then designs the session live based on what the user wants to push on today (and surfaces anything that's been falling behind). Supports working multiple goals in parallel. Use when the user wants to study, "pick up where I left off", plan today's learning, or push on a goal. Does NOT create new goals — that's `/study-goal`.
---

# Study Plan — Dynamic session designer

Each session is designed **live**. You read the user's goal maps (competencies + milestones), ask where they want to push today, optionally nudge them toward neglected areas, then build a time-blocked plan picking specific activities/resources right now (not weeks ago).

## Vault paths
- Vault root: `<vault-root>/`
- Study index: `Study/README.md`
- Goals: `Study/Goals/<slug>/index.md` and `Study/Goals/<slug>/log.md`

## Flow

### Step 1 — Survey active goals
Read `Study/README.md` for the active goals list. For each, read `index.md` to know:
- Active competency + milestone
- All competencies + their target levels
- Last activity date (parse `log.md` for most recent entry — if older than ~2 weeks, flag as "stale")

If there are no active goals, tell the user to run `/study-goal` first and stop.

### Step 1.5 — Run realism audit if any staleness condition fires
Cheaply check, across all active goals, whether any of these are true:
- **Deferral spiral:** any active milestone has been called out as "next session", "non-negotiable", "still owed", "still untouched", or similar 3+ times in the log without a banked rep in between.
- **Pace miss:** any active milestone's reps-required ÷ reps-banked-per-week projection would land past its target date (rough check — `/study-audit` does the precise math).
- **Cold competency:** no log entry references a competency in 2+ weeks.
- **Stale gap analysis:** `index.md`'s gap-analysis date is >4 weeks old.

**If any fire, invoke `/study-audit` before Step 2.** Surface its findings to the user — verdicts, proposed scope changes, what's slipping and why. The user can confirm changes (audit applies them), modify, dismiss ("not now"), or address selectively. After the audit completes (or the user dismisses), proceed to Step 2 with the updated goal state.

If no triggers fire, skip directly to Step 2.

**Don't block work for the audit.** If the user explicitly wants to work first ("just plan the session, audit later"), respect that — `/study-audit` will fire again next session if the conditions still hold.

### Step 2 — Ask the user where they want to push
Use `AskUserQuestion`. Combine in one message:

1. **Which goal(s) today?** Multi-select if >1 active goal. Show last-activity date next to each. Include any stale ones with a "(stale — N weeks)" tag.
2. **Total time available** — under 1 hr / 1–2 hrs / 3–4 hrs / full day.
3. **Start time** — now / morning / afternoon / custom.

### Step 3 — For each selected goal, dig in
For each chosen goal, ask the user (in conversation, not necessarily AskUserQuestion):

> Active milestone is **<X>**. Where do you want to push today — keep pressing on this, switch to another competency, or work on something specific that's been on your mind?

**Then surface gaps proactively.** Scan competencies for ones not touched in 2+ weeks. If found, flag it:

> Heads up: you haven't touched **<competency Y>** since <date>. Want to fold it in for part of today?

The user steers (1); you nudge (2) — combine their choice with your nudges into the final plan.

### Step 4 — Design the session live
Now you pick specific activities. This is where dynamism matters:

- **Match activity to milestone evidence.** If the milestone says "can explain X without notes," activities should build toward that — reading, drilling, then trying to teach it back.
- **Pick resources fresh.** Default to what's current and high-quality (e.g., recent talks, well-regarded explainers, the actual primary source). Don't default to a list from weeks ago.
- **Mix modes** — input (read/watch) + active (write/build/explain) + synthesis (consolidate).
- **Use `WebSearch` if relevant** — e.g., "latest interpretability paper from Anthropic" — when the user wants current state, not foundational material.
- **Route work to goal-specific skills.** Each goal's `index.md` may list its own skills under a `## Skills` section (e.g., a Substack goal might list `/substack-scaffolder`, `/substack-reviewer`, `/substack-distiller`). Read that section and surface candidate skills in the plan — name the skill in the relevant block and invoke it when the user reaches that block. Do not hard-code skill names in this file; they belong to the goal.
- **If no relevant skill exists for the activity, ask.** Before designing the block, ask the user: *"Is there an existing skill that fits this activity? If not, want to build one together after this session?"* Capture any "build one" agreements as a note so they don't get lost.

Format the plan as time-blocks (times in **Sydney local time** — see Conventions):

```
HH:MM–HH:MM · <activity name>
<one concrete sentence on what to do>
```

Rules:
- Real break (~15 min, off-screen) every ~75 min.
- End each goal's session with a 15–30 min **synthesis** block — write/explain in own words. "If you can't write it, you don't get it yet."
- For multi-goal days, cluster blocks per goal with clear transitions.
- For full-day, include a lunch break.

Show the plan to the user. Offer to adjust before they start.

### Step 4.5 — Run the session with the user, don't just hand them a plan
This skill is **not** a static plan-and-leave engagement. Once the user starts working, stay in the conversation as a coach and collaborator:

- **Engage with what they produce.** When the user shares a draft, an audit, a thesis, an outline, an answer to a self-test — read it and respond substantively. Push back on weak spots, confirm what's working, ask the question they're avoiding. Silent acknowledgement ("great, next block") is failure mode.
- **Hand off to the goal's skill at the right block.** When a block names a skill from the goal's `## Skills` section, actually invoke it when the user reaches that block, with their material. Don't paraphrase what the skill would do — run it.
- **Give feedback, not just process.** Call out the specific weaknesses *in the user's own work this session*, not abstract advice — buried theses, hedges, vibe endings, missing evidence, whatever the milestone is targeting.
- **Diagnostic only — never write the deliverable for them.** When the milestone is *the user's own craft work* (writing, whiteboarding, debugging, designing — anything where the rep is the point), do not produce the deliverable for them, even when asked. Specifically:
  - **No sample-line rewrites during review.** If a draft has a weak line, name *what's weak* and *what to do about it* — don't write a replacement line. The reviewer's charter is strictly diagnostic, like `/substack-reviewer`. Showing example prose so they can "see what voiced looks like" is rewriting under another name.
  - **No producing the next pass.** If they ask you to "rewrite this with X" or "draft it with the new structure," push back and offer a *scaffold* (section markers, beat prompts, traps to avoid) — not the prose. Capture any thesis/angle material from prior notes as anchor text in comments, but the prose has to be theirs.
  - **The rule of thumb:** if you produced it, it doesn't count toward the milestone's evidence. If your help would make the evidence not theirs, hold the line — even against direct requests. They will sometimes ask you to cross it; the answer is "I shouldn't, here's why, here's the scaffold instead."
- **Don't drain voice in service of structural criteria.** Structural craft milestones (thesis-first, hedge budget, ending strength, etc.) can produce *clinical, bland prose* if applied without a co-equal voice check. When reviewing a draft against a structural criterion:
  - **Voice is a co-equal pass, not a downstream concern.** "Thesis lands in first 3 paragraphs" + "≤1 hedge" is not enough — the open also has to read like *the writer* wrote it, not a competent paraphrase of the source material. If the structural fix produces something anyone-with-the-source could have written, flag it immediately, before the user has to.
  - **Watch for the trade your feedback induces.** Cutting hedges + cutting filler + compressing briefing all tend to drain voice. If your last round of feedback pulled all three levers, expect a more clinical v(n+1) and pre-empt it: "watch that this doesn't read clinical — voice still has to be on the page."
  - **Re-voicing is the writer's job, not yours.** When voice has been drained, your job is to *name what's missing* (lens, noticing, specific image, planted "I") — not to demonstrate it with example lines.
- **Adapt the plan on the fly.** If a block runs long, an activity isn't working, or something more important surfaces, propose a change rather than holding the line. Plans are scaffolding, not scripture.
- **Mark milestone progress in real time.** When the user produces evidence that satisfies a milestone's evidence clause, name it — "that's 3A evidence, want to pin it?" — instead of waiting for the end-of-session log.
- **Capture insights as they happen.** When something clicks for the user — a realization, a sharpened claim, a question worth keeping — invoke `/study-note` to save it as an atomic linked note under the active goal. Don't break flow to ask permission for every save; if the insight is clearly note-worthy, propose it ("Saving this as a note — okay?") and move on. The session `log.md` captures *what they did*; notes capture *what they learned*.

### Step 5 — Log at session end
When the user signals they're done (or before the conversation ends if they've been working), gather:
- **Focus** — which competency/milestone they pushed on
- **What they actually did** (vs. planned)
- **Progress toward milestone** — self-assessment delta, or "stayed flat"
- **Gaps surfaced** — anything that became visible they didn't expect
- **Milestones completed** — if any

Append to `log.md` at the top (after the `---` header):

```markdown
## YYYY-MM-DD — Competency N, Milestone NX

**Time:** HH:MM–HH:MM (~Xh)
**Focus:** <what they chose to push on>
**Did:** <actual activities>
**Progress:** <delta, or "stayed flat">
**Gaps surfaced:** <new things visible>
**Milestones completed:** <list, or "none">
```

Update `index.md`:
- Check off any completed milestones.
- If active milestone completed, update frontmatter `active_milestone` to the next uncompleted one (same competency first; if competency done, move to next).
- Update the "Active focus" line.

If a competency hits its target, leave milestones checked but note it. If **all competencies done**, move goal to `## Archived Goals` in `Study/README.md` and set `status: completed`.

### Step 6 — Periodic re-diagnosis nudge
If a goal's gap analysis is **older than ~4 weeks**, mention it at end of session:

> Your gap analysis for **<goal>** was done <date> — worth re-running `/study-goal` to refresh it? Things often look different once you've put in real work.

## Conventions
- **Timezone: the user is in Sydney (Australia/Sydney).** The environment's `currentDate` is a date only and may not match Sydney's local day, and there is no `currentTime` field. Before planning time blocks, run `TZ=Australia/Sydney date '+%Y-%m-%d %H:%M %Z'` via Bash to get the actual local date and time. Use Sydney local time for all block timestamps and for the date in log entries.
- Don't show the user file paths or raw markdown.
- Be concrete in activity descriptions — "Watch 3B1B video 2, take notes, predict before each new concept" not "study backprop."
- If the user wants to start a new topic, redirect: "Sounds like a new goal — run `/study-goal` first."
- Working multiple goals in parallel is normal and supported — don't push them toward one at a time.
