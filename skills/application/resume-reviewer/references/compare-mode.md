# Compare mode workflow

One resume, **2+ roles/applications**: the job is a fit decision (which role suits the applicant's skill set better), not a critique. Detailed scoring rubric and output format live in `references/compare-guide.md` — follow it. Paths are relative to the skill's root folder.

1. **Get inputs** — the resume file + each role (company + job-posting link or pasted JD). Confirm any preferences that change the call (location, comp floor, IC vs. lead, what they want next).
2. **Build the capability profile** — run `scripts/check_resume.py` and read the resume to summarize the applicant's skills, domains, seniority, standout achievements, and trajectory.
3. **Research each role via subagents** — one job-posting+company digest subagent per role, run in parallel (briefed with `references/research-brief.md`). Same delegate-don't-browse rule as review mode (read-only web tools, `mode: "auto"`). Returns compact digests only. If multiple roles are at the same company, reuse one company digest.
4. **Score every role on the same dimensions** — requirement coverage, strength alignment, seniority/domain/trajectory fit, logistics gates, narrative distance, differentiation (rubric in `references/compare-guide.md`). Optionally spawn one hiring-manager-persona subagent per role (`references/review-personas.md`, "would you interview THIS candidate?") for sharper evidence.
5. **Deliver to `RESUME_COMPARISON.md`** (and summarize in chat) — capability profile, side-by-side matrix, per-role read, a clear recommendation that states the tradeoff (not just a winner), and what to emphasize if pursuing each. Be honest if neither fits well. Then offer to run **review mode** to tailor the resume to the chosen role.
