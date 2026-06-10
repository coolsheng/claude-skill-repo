---
name: study-audit
description: Realism audit of active study goals — catches milestone slippage *before* the deadline passes by projecting current pace against required reps. Diagnostic only — names what's slipping and why, proposes scope changes (cut/extend/promote/swap), applies them only with user approval. Invoked automatically by `/study-plan` at session start when staleness conditions fire; also user-runnable ad-hoc. Use when the user asks to "review my goals", "audit my progress", "are my deadlines still honest?", or whenever pace-vs-deadline integrity needs checking.
---

# Study Audit — Track trajectory, not just past-due

By the time a milestone passes its target date, it's too late. This skill catches drift *early* — projects current pace forward, compares to deadline, flags milestones that will miss at current rate. Then proposes scope changes (cut / extend / promote / swap focus) for the user to confirm.

**Charter:** strictly diagnostic + advisory. Names the gap, proposes options, edits `index.md` only on user approval. Does NOT auto-cut milestones, does NOT decide priorities, does NOT replace `/study-goal` (which is for fresh diagnosis / re-diagnosis).

## Vault paths
- Vault root: `<vault-root>/`
- Study index: `Study/README.md`
- Goals: `Study/Goals/<slug>/index.md` and `Study/Goals/<slug>/log.md`

## Flow

### Step 1 — Read state
Read `Study/README.md` for the active goals list. For each active goal, read `index.md` (competencies + milestones + active focus) and `log.md` (recent activity, banked reps, deferrals).

### Step 2 — For each active milestone, compute a realism verdict

For each `[ ]` milestone in each active goal:

1. **Reps required** — parse from the milestone's evidence clause.
   - Numbered evidence ("4 essays at target", "≥20 test cases", "5 mock interviews") → integer count.
   - Binary evidence ("survive 10 minutes of adversarial follow-ups", "pinned post live", "ADR committed") → 1 rep + estimated prep sub-reps (default 2–3).
   - If evidence is unclear, skip the rep math and fall back on deferral + days-untouched signals.

2. **Reps banked** — scan `log.md` for entries that explicitly bank toward this milestone (e.g., "essay #1 of 4 for 1A BANKED"). Count them.

3. **Pace** — from the log, average days between banked reps for this milestone. If no reps banked yet, use the user's average session-to-rep cadence across the goal as fallback (or 7 days as a conservative default).

4. **Days remaining** — `target_date − today` (Sydney local, see Conventions).

5. **Projected finish** — `today + (reps_remaining × pace)`.

6. **Verdict:**
   - **On track** — projected finish ≤ deadline with ≥3 days buffer.
   - **Tight** — projected finish ≤ deadline but buffer <3 days.
   - **At risk** — projected finish 1–14 days past deadline.
   - **Will miss** — projected finish >14 days past deadline.
   - **Already missed** — today > target_date and not checked off.

### Step 3 — Detect non-pace triggers

In addition to pace projection, flag:
- **Deferral spiral:** same milestone called out as "next session", "non-negotiable", "still owed" 3+ times in the log without a banked rep in between.
- **Cold competency:** no log entry references a competency in 2+ weeks (catches whole-goal neglect, not just milestone delay).
- **Stale gap analysis:** `index.md`'s gap-analysis date >4 weeks behind today.

### Step 4 — Present the audit

Output a compact verdict block per goal (Sydney date, plain prose, no raw paths):

```
<Goal Name>
  Milestone <code> — <one-line outcome>
    Verdict: <on track / tight / at risk / will miss / already missed>
    Pace: X reps banked of Y needed; ~Z days/rep; deadline in N days; projects finish on DATE.
    Triggers: <deferred 5×, cold 2 weeks, stale gap analysis — list any that fire>
    Why: <one sentence on what's driving the verdict>

  [repeat per active milestone]

  Cold competencies: <list, or "none">
```

Then a **synthesis block** across all goals:
- What's actually achievable in the next N weeks at current pace?
- Where are the load-bearing conflicts (two goals pulling on the same scarce time)?
- One sentence per goal: keep / narrow / extend / pause.

### Step 5 — Propose scope changes (one per milestone that needs it)

For each at-risk / will-miss / already-missed milestone, propose **one** concrete change, not a menu. Pick the most honest move based on what the log shows:

- **Cut** — the milestone is no longer load-bearing (e.g., stretch milestones marked "cut without guilt" in the goal). Strike it from `index.md`, note rationale.
- **Extend** — deadline was always ambitious; push it back N weeks. Only if rep work has been happening (just slower than planned).
- **Narrow scope** — keep deadline, reduce reps required (e.g., "4 essays" → "3 essays"). Only if user has explicit slack and the lower count still earns the competency.
- **Promote priority** — milestone is on track to miss because *time* is going to other goals, not because the work is wrong. Recommend next session pushes it.
- **Swap active focus** — `active_milestone` in frontmatter is wrong for current pace; the goal would be better served pushing on a different milestone first.

**Present each proposal with: the change, the rationale, the trade-off it accepts.** Ask the user to confirm, modify, or reject each one — `AskUserQuestion` one at a time (see `feedback-ask-one-question-at-a-time` in memory).

### Step 6 — Apply approved changes

For each user-approved change, edit `index.md`:
- **Cut:** strike the milestone (`- [ ] **1C** ...` → `- [~] **1C** ... — **cut YYYY-MM-DD:** <rationale>`).
- **Extend:** update the date in the milestone line; add a "deadline extended YYYY-MM-DD: <rationale>" inline note.
- **Narrow:** edit the evidence clause + add inline "scope narrowed YYYY-MM-DD: <rationale>".
- **Promote:** flag in "Active focus" section; don't change frontmatter unless user explicitly says to swap active milestone.
- **Swap active:** update `active_competency` / `active_milestone` in frontmatter + rewrite "Active focus" section.

Do NOT silently rewrite log entries. The audit is a forward-looking edit on `index.md` only; the log is append-only history.

After applying changes, add a single line to `log.md` (at the top, after the `---` header):

```markdown
## YYYY-MM-DD — /study-audit run

**Triggers fired:** <list>
**Changes applied:** <list, e.g., "1C cut; 4A deadline extended to 2026-07-01">
**Carried forward:** <verdicts the user dismissed without changes — so the next audit can re-flag>
```

### Step 7 — Hand off

If invoked from `/study-plan`: return control to `/study-plan` with a summary of changes (so `/study-plan` can ask "given the scope updates, where do you want to push today?").

If invoked ad-hoc: tell the user it's done, suggest `/study-plan` if they want to keep working.

## Integration with `/study-plan`

`/study-plan` Step 1 should:
1. Read `Study/README.md` and each goal's `index.md` + last `log.md` entry as it does today.
2. Check staleness conditions cheaply (deferral counts, days since last entry, target dates relative to today).
3. **If any trigger fires, invoke `/study-audit` silently first**, surface the findings to the user, then proceed to Step 2 (which goal to push today). The audit's scope changes feed into Step 2's choices.
4. If no triggers fire, skip directly to Step 2.

The audit should never block session work — if the user dismisses it ("not now, let me work first"), `/study-plan` continues normally and the audit reschedules itself for next session.

## Conventions
- **Timezone: the user is in Sydney (Australia/Sydney).** Run `TZ=Australia/Sydney date '+%Y-%m-%d'` before computing days-remaining or writing log dates. The environment's `currentDate` may not match Sydney's local day.
- Don't show the user file paths or raw markdown — speak in goal/milestone terms.
- **One question at a time** (per `feedback-ask-one-question-at-a-time` memory). Use `AskUserQuestion` for each proposed scope change separately.
- **Pace math is a heuristic, not gospel.** If pace data is thin (few banked reps) or the milestone has irregular cadence (e.g., interview prep ramps near the deadline), say so in the "Why" line rather than presenting a false-precision projection.
- **Be honest about uncertain projections** — "this is a guess from N=1 banked rep" beats a confident wrong number.
- **Resist proposing menus of options.** Pick the single most honest move per milestone; the user can reject it and discuss alternatives.
- **Voice:** diagnostic and unsparing, not advisory and gentle. Same charter as `/substack-reviewer` — name what's slipping, don't soften it.
