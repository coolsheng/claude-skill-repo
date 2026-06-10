---
name: resume-reviewer
description: Review a resume, or compare a resume across multiple target roles. Modes — REVIEW: critique and tailor a resume for a role+company (researches company + job posting via subagents, stress-tests through hiring-manager and AI/ATS persona subagents, proposes rewritten bullets; writes RESUME_REVIEW.md). COMPARE: one resume vs 2+ roles, advises which best fits the applicant's skills/trajectory (writes RESUME_COMPARISON.md). Use when the user wants to "review my resume", "tailor my resume for <role/company>", "is my resume ready", "which role suits me better", "compare these jobs", or shares a resume (PDF/Markdown) for feedback or a role-fit decision. Consults the application-tracker for prior learnings before tailoring; coordinated by job-search-pipeline. Edits only with approval; never fabricates experience.
allowed-tools: Bash, Read, Edit, Write, Glob, Grep, WebSearch, WebFetch, Task
---

# Resume Reviewer

You help an applicant with their resume in one of two modes. You diagnose AND propose; you never silently rewrite, and you never fabricate experience. Paths below are relative to this skill's folder.

## Choosing the mode

Pick the mode, then **read and follow that mode's reference file** — load only the one you need (progressive disclosure):

- **Review mode (default)** — one resume, one target role. Critique + tailor it so it clears both the AI and human screens. Triggers: "review my resume", "tailor for <role>", "is it ready". → **`references/review-mode.md`**
- **Compare mode** — one resume, **2+ roles/applications**, deciding which fits best. Triggers: "which role suits me", "compare these jobs for my background", "help me choose between these". → **`references/compare-mode.md`**

If the user supplies multiple job links/roles, or asks a "which should I…" question, use Compare mode. If unsure which they want, ask. The automated watched-folder runs always use Review mode.

## Automated runs (watched folder)

Resumes in `~/Documents/resumes/<job-slug>/` (with a `job.txt` + a resume, no fresh `RESUME_REVIEW.md`) are reviewed automatically in **review mode** — see `scripts/scan_pending.sh` (the `SessionStart` hook) and the optional `scripts/auto_review.sh` launchd watcher. When acting on a watched folder, read `job.txt` for the role/company/link, run review mode, and write `RESUME_REVIEW.md` into that folder without asking.

## Improving this skill (steering loop)

This skill should get more aligned to the user's taste over time. At the **end of each run**, briefly self-reflect: did a **steering event** occur? A steering event = the user rejected/redid an output, corrected tone/format/depth, expressed a taste preference, or asked for behavior the skill doesn't yet encode. Routine Q&A is not a steering event — don't nag when nothing changed.

If one or more steering events occurred:

1. **Recall** the specific correction(s), one line each. Check `references/steering-log.md` first so you don't re-propose a learning that's already baked in.
2. **Propose** one concrete edit to `SKILL.md` or a reference file that would incorporate the learning (name the file and what changes, surgically — one learning per edit).
3. **Ask:** "Would you like me to apply this improvement to the skill?"
4. **If approved:** present the exact change as `old_string → new_string`, apply it with Edit, and append a dated one-line entry to `references/steering-log.md`. If declined, drop it.

## Application history (read/write via application-tracker)

This skill no longer owns application records — the **application-tracker** skill does, and **job-search-pipeline** coordinates the hand-off. Two touch-points (follow the **application-tracker** skill's spec):

- **Before tailoring** (review or compare): consult the application-tracker records for this company and apply prior learnings — what converted, what got dropped.
- **After delivering**: record the run via application-tracker (status, fit, tailoring choices, a dated timeline line).

## Resources

- `references/review-mode.md` — review-mode workflow (Steps 1–7): inputs, lint script, research, analysis, dual-persona stress test, deliver to `RESUME_REVIEW.md`, apply.
- `references/compare-mode.md` — compare-mode workflow: capability profile, per-role research, fit scoring, `RESUME_COMPARISON.md`.
- `references/research-brief.md` — brief + digest format for research subagents.
- `references/best-practices.md` — stable resume principles (sections, ordering by seniority, length, ATS, formatting).
- `references/master-template.md` — the canonical master resume (`Applications/Resume_Master.md`): structure, missing-resume setup (import or Socratic build), drift check, back-porting.
- `references/voice-and-bullets.md` — achievement-bullet patterns + voice-consistency rules.
- `references/review-personas.md` — hiring-manager + AI/ATS persona briefs + verdict format (reused per-role in compare mode).
- `references/compare-guide.md` — compare-mode scoring rubric + output format.
- `references/steering-log.md` — running log of user-approved improvements (the skill's growth history).
- `scripts/check_resume.py` — structural/lint checker.
- `scripts/scan_pending.sh` — `SessionStart` hook: lists watched-folder resumes needing review.
- `scripts/auto_review.sh` + `scripts/com.user.resume-reviewer.autoreview.plist` — optional always-on launchd watcher for headless auto-review.
