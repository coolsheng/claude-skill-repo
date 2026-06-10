# Steering log

Running history of user-approved improvements to this skill — the record of how it has grown to fit the user's taste. The steering loop in `SKILL.md` reads this (to avoid re-proposing past learnings) and appends to it (one dated line per applied change).

Format: `YYYY-MM-DD — <learning> → <file(s) changed>`

## Entries

- 2026-06-07 — Delegate all web research to subagents to keep main context lean → `references/review-mode.md`, `references/research-brief.md`
- 2026-06-07 — Sync resume wording to the target company + job posting → `references/research-brief.md`, `references/review-mode.md`
- 2026-06-07 — Stress-test every resume through hiring-manager + AI/ATS persona subagents so it clears both filters → `references/review-personas.md`
- 2026-06-07 — Always write the full review to `RESUME_REVIEW.md` each run → `references/review-mode.md`
- 2026-06-07 — Auto-run reviews on a watched folder (no manual trigger) → `scripts/scan_pending.sh`, `scripts/auto_review.sh`, `~/.claude/settings.json`
- 2026-06-07 — Add compare mode (one resume, 2+ roles → fit decision) → `references/compare-mode.md`, `references/compare-guide.md`
- 2026-06-07 — Self-improve via an end-of-run steering loop; delegate submode workflows to reference files → `SKILL.md`, `references/review-mode.md`, `references/compare-mode.md`
- 2026-06-07 — Track application outcomes in Obsidian (per company/role, study-goal style) and feed learnings back into tailoring → `references/outcome-tracking.md`, `SKILL.md`
- 2026-06-07 — Extract tracking into its own `application-tracker` skill + add `job-search-pipeline` orchestrator (bridges to study goals); resume-reviewer slimmed to review+compare → `application-tracker/*`, `job-search-pipeline/*`, `SKILL.md`
- 2026-06-08 — Don't editorialize/sell facts (AI-tell) — state credential/visa lines plainly, avoid benefit-selling parentheticals & slash-lists → `references/voice-and-bullets.md`
- 2026-06-08 — Run a literal exact-keyword diff vs. the JD as a final sync check; protect JD-verbatim phrasing when de-buzzwording (cutting AI-tell adjectives can strip JD-literal terms); trust a user-pasted JD over third-party mirrors (mirrors carry generic/template keywords) → `references/review-mode.md`
- 2026-06-10 — No em-dashes in resume output (AI tell): replace with colon/parens/comma/`·`; date-range en-dashes stay. Where prose needs a pronoun, third person ("his"), never "I/my" → `references/voice-and-bullets.md`
- 2026-06-10 — Dated bullets (e.g. consulting engagements) stay reverse-chronological; tailor by expanding/compressing, not reordering by relevance → `references/best-practices.md`
- 2026-06-10 — Maintain one master resume (`Applications/Resume_Master.md`) as the tailoring base; if missing, import an existing resume or build one Socratically; drift-check it at the start of every review and back-port approved improvements after → `references/master-template.md`, `references/review-mode.md`, `SKILL.md`
