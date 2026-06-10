---
name: application-tracker
description: Track job applications and their outcomes in Obsidian, segregated by company, and surface what converts. Maintains per-application records (status lifecycle drafting→applied→screen→interview→offer/rejected/withdrawn), an append-only timeline, the tailoring choices used, and a cross-application patterns dashboard. Use when the user wants to "log my application", "update my application status", "I got a screen/interview/offer at X", "I was rejected by X", "show my application tracker", "where am I with <company>", or "what's been converting". Feeds prior learnings back to resume-reviewer; coordinated by job-search-pipeline. Speaks in company/role/stage terms; never fabricates an outcome.
---

# Application Tracker

Owns the user's job-application records in their Obsidian vault so the wider job search learns what actually **converts** — not just what fits their taste. One folder per company, one file per application; mirrors the `/study-goal` layout (per-file, append-only logs, Sydney-dated). Speak in plain terms (company / role / stage) — don't show vault paths or raw markdown.

Follow `references/tracking-spec.md` for the exact layout, file templates, status lifecycle, and feedback loop.

## What this skill does

1. **Record** — create/update an application record when the user applies, when a review/compare is run, or when they report a change.
2. **Advance** — move status through the lifecycle, stamping the date and appending a timeline line on every change.
3. **Learn** — at terminal stages (offer/rejected/withdrawn) capture Learnings and roll the insight into the company `index.md` + the dashboard's Patterns section.
4. **Surface** — answer "where am I with X" / "what's converting" from the records, and hand prior learnings to resume-reviewer before it tailors.

## Operating rules
- Anchor dates on Sydney time: `TZ=Australia/Sydney date '+%Y-%m-%d'`.
- Never invent an outcome or date — only record what the user reports.
- Keep the dashboard table and Patterns section current after every change.
- If a record or company folder doesn't exist yet, create it per the spec.

## Resources
- `references/tracking-spec.md` — vault layout, per-application + company + dashboard templates, status lifecycle, feedback loop, triggers.
