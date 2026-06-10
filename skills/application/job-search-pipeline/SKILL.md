---
name: job-search-pipeline
description: Orchestrate the end-to-end job search — detect where each application stands and route it to the right next step. Reads the application-tracker records to establish stage, then dispatches: decide between roles or tailor the resume (resume-reviewer) → apply & record (application-tracker) → prep by bridging role-gaps into the study system (recommends /study-plan against the relevant goal) → capture the outcome and learn. Use when the user asks "where am I in my job search", "what's next for <company>", "run my job search", "I want to apply to <role/company>", "help me land <role>", or shares a job link to pursue end-to-end. Stops at each gate so the user stays in control; doesn't do the workers' jobs or duplicate the study system.
---

# Job Search Pipeline

Entry point and router for the whole job search — the way `substack-pipeline` routes essays. You do **not** do the work yourself: you detect each application's stage and dispatch to the right worker skill, stopping at each gate. The **application-tracker** records are the source of truth for stage.

## Worker skills (what each owns)
- **resume-reviewer** — review / compare / tailor the resume → `RESUME_REVIEW.md`, `RESUME_COMPARISON.md`.
- **application-tracker** — Obsidian application records: status, outcomes, convert-vs-fail patterns.
- **study-\*** (`study-plan` / `study-goal` / `study-audit`) — interview/skill prep. **Bridge to these; never duplicate them.**
- *Future workers the pipeline can route to once built: cover-letter, interview-prep, referrals/outreach.*

## How to run
1. **Establish state** — read the application-tracker dashboard (`Applications/README.md`) + the relevant company folder.
2. **Report + locate** — tell the user where things stand in plain terms and name the next stage.
3. **Dispatch** — route to the worker for that stage (or the study bridge), per `references/pipeline.md`. **Stop and confirm at each gate** — the user steers transitions.
4. **Keep state current** — ensure application-tracker is updated after each step.

## The pipeline (brief)
Full routing table + study-bridge mapping in `references/pipeline.md`.

1. **Decide** — 2+ candidate roles → resume-reviewer **compare**. One role → next.
2. **Tailor** — resume-reviewer **review** for the chosen role+company (folds in tracker learnings + work-auth framing).
3. **Apply & record** — user applies → application-tracker logs `applied` + the resume version used.
4. **Prep (study bridge)** — turn the gaps review/compare surfaced into prep items, map them to the relevant study goal's competencies (e.g. `frontier-lab-fde`), recommend `/study-plan`. Prep is tracked there, not here.
5. **Interview** — advance status; use the JD gaps as likely probes (future: interview-prep worker).
6. **Outcome & learn** — application-tracker captures result + Learnings and rolls patterns into the dashboard; surface those for the next application.

## Boundaries
- Coordinate; don't produce workers' artifacts directly. Invoke the owning skill's behavior.
- Bridge to the study system — don't re-implement prep tracking.
- The user approves every stage transition.

## Resources
- `references/pipeline.md` — stage→action routing table, study-bridge gap→competency mapping, worker ownership.
