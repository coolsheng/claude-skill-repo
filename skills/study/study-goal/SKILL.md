---
name: study-goal
description: Scaffold a long-term learning goal as a navigation system — diagnose the user's gaps Socratically, break the goal into competencies, and set milestones with observable outcomes. Does NOT prescribe specific resources (those go stale) — `/study-plan` picks activities dynamically each session. Use when the user wants to start a new ambitious goal (e.g. "get a job at Anthropic", "be fluent in Spanish", "ship a real iOS app"), add a new learning goal, or revisit/re-diagnose an existing goal.
---

# Study Goal — Build a navigation system, not a syllabus

`/study-goal` produces a **goal as a map of competencies + milestones**, not a list of resources to consume. The goal stays valid for months because it describes outcomes, not activities. `/study-plan` picks activities live each session.

## Vault paths
- Vault root: `<vault-root>/`
- Study index: `Study/README.md`
- Goal folder: `Study/Goals/<slug>/` containing `index.md` and `log.md`

## Flow

### Step 1 — Capture the aspiration
One open question (free-form):

> What's the goal, and what does success look like — the outcome you'd point at and say "I made it"?

Listen for: timeline (deadline or open-ended), and whether it's external/verifiable (job, exam) or internal (understanding, capability).

### Step 2 — Socratic gap analysis
**This is the core of the skill.** You actively conduct a diagnosis — don't just record what the user volunteers.

Ask 4–7 questions, one at a time (don't batch — let answers shape the next question). Goals for the diagnosis:
- **Surface what they haven't named.** Most people undercount their gaps. Probe.
- **Find the asymmetries.** What do they think they know but might not? What do they avoid?
- **Get concrete.** "I'm weak on ML" → "Can you explain backprop without notes? Have you implemented gradient descent? Read a paper end-to-end?"
- **Calibrate self-assessment.** When they rate themselves, ask for evidence.

Question patterns that work:
- "If you had to interview for this tomorrow, what would scare you most?"
- "What's something everyone in this field talks about that you'd nod along to without really understanding?"
- "What have you tried before and bounced off?"
- "Where do you feel solid? Walk me through what you can actually do today."
- "What's the part you keep saying 'I'll get to that' about?"

Synthesize: a 3–5 sentence diagnosis covering strongest areas, biggest gaps, and any tendencies (e.g. "drawn to theory, avoids implementation").

### Step 3 — Identify competencies (3–7)
From the diagnosis, name the competencies needed to hit the aspiration. Each competency:
- Is **a capability**, not a topic. ("Read & critique ML papers" not "ML papers")
- Has a **Today** line — one concrete observable thing the user can/can't do *right now*. No ratings, no adjectives like "weak" or "strong" — describe the actual behavior or artifact. ("Can read a transformer paper's abstract but stalls at the architecture diagram.")
- Has a **Target** line — one concrete observable thing the user will be able to do when the competency is hit. Must be testable by someone else. ("Can explain a transformer paper's contribution + critique its eval methodology in a 30-min conversation with an ML engineer.")

Avoid subjective ratings (1/5, "intermediate", "fluent"). If you find yourself reaching for one, replace it with a behavior or artifact instead. The Target should be specific enough that another person could watch the user and agree "yes, they hit it" or "no, they didn't."

Show this back to the user for approval / tweaking.

### Step 4 — Set milestones (2–4 per competency)
Each milestone:
- **Outcome** — something observable. ("Build a working transformer from scratch" not "Understand transformers")
- **Evidence** — how the user proves it. ("Can implement multi-head attention without reference, and it trains on tiny shakespeare")
- **Target date** — absolute date or relative ("by milestone X of competency Y")

Order milestones so each builds on prior ones. Don't pre-pick resources or activities — those are `/study-plan`'s job per session.

Show all competencies + milestones to user for approval / tweaking.

### Step 4.5 — Identify goal-specific skills
Before writing files, ask the user:

> Are there existing skills (yours or built-in) that fit the kind of work this goal will involve? E.g., a writing goal might use `/substack-scaffolder` or `/substack-reviewer`; a coding goal might use `/review` or `/security-review`.

If they name skills, capture them. If they identify activities with no matching skill, flag those as candidates to build later — note them in the goal but don't build them now (out of scope for `/study-goal`).

It's fine if a goal has zero skills today; the section can stay empty and `/study-plan` will prompt to fill it in later.

### Step 5 — Write the files
Once approved:

1. **Slug:** kebab-case from goal name.

2. **Create `Study/Goals/<slug>/index.md`:**

```markdown
---
goal: <Goal Name>
started: YYYY-MM-DD
deadline: YYYY-MM-DD or "open-ended"
status: active
active_competency: 1
active_milestone: 1A
---

# <Goal Name>

## Aspiration
<one paragraph — the outcome, not the activities>

## Gap analysis (as of YYYY-MM-DD)
<3–5 sentence diagnosis from Step 2>

## Competencies

### 1. <Competency name>
- **Today:** <concrete observable behavior — what they can/can't do right now>
- **Target:** <concrete observable behavior — testable by someone else>
- **Milestones:**
  - [ ] **1A** (by YYYY-MM-DD): <outcome>. *Evidence:* <how user proves it>.
  - [ ] **1B** (by YYYY-MM-DD): <outcome>. *Evidence:* ...
  - [ ] **1C**: ...

### 2. <Competency name>
- **Today:** ...
- **Target:** ...
- **Milestones:**
  - [ ] **2A**: ...

## Active focus
**Competency 1 → Milestone 1A**

## Skills
Goal-specific skills `/study-plan` should route work to when relevant:
- **`/<skill-name>`** — <one-line when-to-use>
- _(leave empty or omit bullets if none identified yet; `/study-plan` will prompt to add as activities surface)_

## Notes
- Re-diagnose gaps every ~4 weeks or after each milestone completion.
- Session logs in [[log]].
- `/study-plan` picks resources/activities dynamically — this doc is the map, not the route.
```

3. **Create `Study/Goals/<slug>/log.md`:**

```markdown
# <Goal Name> — Session Log

Append-only. Newest at top. Each entry references the milestone(s) pushed.

---
```

4. **Update `Study/README.md`** under `## Active Goals`:
   `- [[Goals/<slug>/index|<Goal Name>]] — <one-line aspiration>. Started YYYY-MM-DD.`

### Step 6 — Hand off
Tell the user: goal is saved, run `/study-plan` to start pushing on it. If they have other active goals, mention that `/study-plan` supports working multiple in parallel.

## Conventions
- **Timezone: the user is in Sydney (Australia/Sydney).** The environment's `currentDate` may not reflect Sydney's local day. Before writing the `started` date or any milestone dates, run `TZ=Australia/Sydney date '+%Y-%m-%d'` via Bash to anchor on Sydney's local date. Convert relative dates against that.
- Slugs are kebab-case.
- Don't show file paths or raw markdown to the user. Speak in goal/competency/milestone terms.
- Resist the urge to recommend specific resources here — it's not this skill's job. If a resource comes up in conversation, mention it but don't write it into the index.
- A goal with no observable milestones is not a goal — push back until the user names something concrete.
