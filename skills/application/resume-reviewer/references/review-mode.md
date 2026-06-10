# Review mode workflow

One resume, one target role: critique + tailor it so it clears both the AI and human screens. Diagnose AND propose; never silently rewrite; never fabricate. Paths are relative to the skill's root folder.

## Step 1 — Get the target and the file

Ask up front (don't proceed without these):

1. **Target role + seniority + industry** — e.g. "Senior backend engineer, fintech" or "New-grad data analyst." Tailoring is impossible without this.
2. **Company + job-posting link** — the company name and the application/job-posting URL (or pasted JD text). These drive the research in Step 3 so the resume's wording syncs to how this employer talks and what this role demands. If the user has neither, proceed with generic role norms and say so.
3. **The resume base** — default to the master template per `references/master-template.md`: use `Applications/Resume_Master.md` as the tailoring base, run its **drift check** (what changed since it was last touched — new role, finished engagements, metrics that landed), and fold confirmed updates into the master *before* tailoring. If the master doesn't exist, set it up first per that reference — **import** an existing resume file into the master format, or **build it Socratically** section by section. A user-supplied file (PDF/Markdown path or pasted text) is still accepted for one-off reviews; suggest converting it into the master afterward. (DOCX isn't supported by the script — ask them to export to PDF or paste as Markdown.)

If they pasted the resume inline instead of a file, save it to a temp `.md` so the script can run on it. After delivery (Step 7), back-port approved improvements to the master per `references/master-template.md`.

## Step 2 — Run the structural/lint script

```
python3 scripts/check_resume.py <path-to-resume>
```

It extracts text (PDF via pdfplumber/pypdf if installed; Markdown/txt directly), then reports: sections found vs. missing, contact essentials, and flagged lines (pronouns, weak/filler verbs, un-quantified bullets, overlong bullets, tense inconsistency, passive voice). Treat its output as **signal, not verdict** — heuristics over-flag; use judgment. If a PDF lib is missing, the script says how to install it; relay that to the user or ask for Markdown.

## Step 3 — Research via subagents (always delegate)

Read `references/best-practices.md` yourself for the stable principles. **All web research is delegated to subagents** — never browse the web from the main thread. Subagents do the bulky reading and return only a tight digest, keeping main context lean.

These subagents need WebSearch/WebFetch, which are pre-authorized for this skill via the `allowed-tools` frontmatter — so web queries run without permission prompts. Spawn each research subagent in a non-prompting permission mode (Task/Agent `mode: "auto"`) so its read-only web calls don't interrupt the run. If a query is still blocked in this environment, tell the user to allowlist `WebSearch`/`WebFetch` in settings (the `/update-config` skill can do this) rather than falling back to manual browsing.

Spawn these subagents (run them in parallel — they're independent), each briefed with `references/research-brief.md`:

1. **Company-research subagent** — researches the target company: what it does, mission/values, voice/tone, recent news/products, and the vocabulary it uses about itself. Goal: surface the *language and priorities* the resume should echo.
2. **Job-posting subagent** — fetches the application/job-posting link (or reads pasted JD text) and extracts required + preferred skills, responsibilities, seniority signals, and the exact keywords/phrasing the resume should mirror (ATS + recruiter alignment).

Each must return ONLY the compact digest defined in `references/research-brief.md` — not raw pages. If the user gave no company/link, skip that subagent and note the gap. If a subagent comes back empty (offline, paywalled, dead link), proceed on the bundled reference and say so. Don't fan out beyond these two; don't re-research in the main thread.

## Step 4 — Analyze

Reason through, in this order:

1. **Section presence & order** — using `references/best-practices.md`, decide the *right* section order for THIS role + seniority (e.g. new-grad leads with education; senior leads with experience). Flag missing/needless sections.
2. **Experience & achievements** — for each entry, judge whether bullets show *impact* (outcome + metric) vs. duties. Apply the bullet patterns in `references/voice-and-bullets.md`.
3. **Voice consistency & employer sync** — check the resume reads with one coherent voice that matches the target seniority (see `references/voice-and-bullets.md`): consistent tense, strong verb-led bullets, no pronouns/filler, no over- or under-claiming relative to the level. Then **sync wording to the research digests**: surface the JD's required keywords/skills the resume is missing or burying, and align terminology and emphasis to the company's own language and priorities — honestly, never claiming experience the applicant lacks.
   - **Literal keyword diff (final sync check).** After wording is tailored, run an exact-token diff of the JD's concrete terms against the resume: does each appear *verbatim* (matching hyphenation/plurals), or only as a synonym? Legacy ATS and recruiter Boolean searches match literally, so a synonym can make a qualified candidate invisible — restore the JD's own phrasing wherever the applicant genuinely qualifies. **Caveat:** a de-buzzwording pass (cutting AI-tell adjectives) can accidentally strip phrases that are literally in the JD — re-run this diff *after* any such pass and keep JD-verbatim terms even while removing puffery. And trust a JD the user pastes over any third-party mirror: mirrors inherit generic/template keywords the specific posting may not actually contain.
4. **Work authorization** — if the role needs relocation/sponsorship the applicant lacks, this is often the dominant gate. Apply the "Work authorization & relocation" guidance in `references/best-practices.md` — frame the lowest-friction visa pathway as a selling point near the contact info (e.g. the E-3 for Australian nationals targeting US roles) rather than leaving it unstated. Only claim authorization the applicant genuinely has and will act on.

## Step 5 — Dual-persona stress test (subagents)

A resume must clear two gates: an **automated screen** and a **human**. Delegate one subagent per persona (run in parallel), each briefed with `references/review-personas.md`, and pass each the resume text plus the Step 2 script output and the Step 3 research digests. Keep the personas independent — don't let one bias the other.

1. **Hiring-manager persona** — reads like a busy hiring manager / recruiter for this exact role + company. Judges the 6–10-second skim, impact and relevance, seniority fit, and "would I interview?" — using the company digest's priorities.
2. **AI/ATS persona** — reads like an automated screener + LLM resume parser. Judges keyword/skill match to the JD, parseability, section detection, and formatting that breaks machine reading — using the job-posting digest's required keywords.

Each returns the compact verdict defined in `references/review-personas.md`. In the main thread, **reconcile** the two — note where they conflict (e.g. keyword coverage the AI wants vs. readability the human wants) and resolve toward changes that satisfy both honestly. Fold the reconciled findings into Step 6.

## Step 6 — Deliver the review

**Always write the full review to `RESUME_REVIEW.md`** (in the resume's directory; fall back to the cwd if that isn't writable) AND summarize it in chat. Overwrite the file each run so it stays current. The file is the addressable artifact; chat is the quick read.

Structure both with, in priority order:
- **Header** — target role, company, posting URL, resume file, date, and confidence caveats (research confidence; whether the lint script ran).
- **Persona verdicts** — the hiring-manager and AI/ATS verdicts (Step 5), reconciled.
- **Top findings** — the 3–6 highest-impact fixes, each with the why.
- **Recommended section order** for the target role, with one-line rationale.
- **Rewritten bullets** — for the weakest entries, show `before → after`, preserving the applicant's real accomplishments (never invent metrics; if a number is missing, prompt the user for it).
- **Voice notes** — any places the voice undershoots or overshoots the target level.
- **Open questions** — anything blocking a finished rewrite (location, honest keyword claims, ambiguous dates).

## Step 7 — Apply only with approval

If the resume is a Markdown/text file the user wants edited, apply approved changes to it. For PDFs, deliver the rewritten content as Markdown for them to paste — never claim to have edited a PDF. Never fabricate experience, dates, or metrics.
