# Application-tracking spec

The single source of truth for an application's stage. Mirrors the `/study-goal` layout (per-file progress, append-only logs), **segregated by company**.

## Vault layout
- Vault root: `<vault-root>/`
- Dashboard: `Applications/README.md`
- Per company: `Applications/<company-slug>/index.md`
- Per application: `Applications/<company-slug>/<role-slug>.md`

Slugs are kebab-case. Dates: anchor on Sydney time — `TZ=Australia/Sydney date '+%Y-%m-%d'`.

## Per-application file template
```yaml
---
company: <Name>
role: <Title>
posting: <url>
status: drafting | applied | screen | interview | offer | rejected | withdrawn
applied: <YYYY-MM-DD or "">
stage_updated: <YYYY-MM-DD>
resume_version: <which resume was sent — path/note>
fit_score: <0–5 from review/compare, optional>
related_goal: "[[Study/Goals/<slug>/index]]"   # if it maps to a study goal, else ""
outcome: ""    # filled at a terminal stage
---

# <Company> — <Role>

## Timeline
*Append-only, newest at top. One dated line per event.*
- YYYY-MM-DD — <event>   (e.g. "review run, fit 4.5" · "applied" · "recruiter screen" · "rejected post-screen")

## Tailoring choices
- <the framing / keywords / bullets emphasized for this application>

## Learnings
*Fill at a terminal stage.* What likely helped or hurt; what to do differently next time.
```

## Status lifecycle
`drafting → applied → screen → interview → offer / rejected / withdrawn`. On every change: update `status` + `stage_updated`, and append a Timeline line.

## Company `index.md`
Short: a one-paragraph company digest summary (reuse research), a list of role files, and cross-application **patterns** for this company ("ATS keeps dropping X", "they reward Y").

## Dashboard `README.md`
A table across all companies — company · role · status · applied · fit · outcome — plus a **Patterns & learnings** section aggregating what converts across applications.

## The feedback loop (how the search gets more successful)
1. **Before** a review/compare for a company: read `Applications/<company>/` and the dashboard Patterns to recall prior attempts — what was tried, what converted, what got rejected — and apply those learnings to the new tailoring.
2. **After** a review/compare: create or update the record (status, fit, tailoring choices, a Timeline line).
3. **On a reported outcome**: update status + Timeline; at terminal stages write Learnings and roll the insight up into the dashboard Patterns.

## Triggers
Maintain records on any review/compare run (usually driven by job-search-pipeline). Also respond to explicit logging: "log my application to X", "I got an interview/screen/offer at X", "I was rejected by X", "show my application tracker", "where am I with X".
