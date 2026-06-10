# Job-search pipeline — stages, routing, study bridge

Source of truth for each application's stage is its application-tracker record (`status`). The orchestrator reads it, routes, and stops at each gate.

## Stage → action routing

| Stage (tracker `status`) | Situation | Route to | Output |
|---|---|---|---|
| (no record) | choosing between 2+ roles | resume-reviewer · **compare** | `RESUME_COMPARISON.md` + tracker records |
| (no record) / drafting | one chosen role, not yet tailored | resume-reviewer · **review** | `RESUME_REVIEW.md` + tracker update |
| drafting | tailored, ready to send | user applies → application-tracker | `status: applied` |
| applied | waiting / prep | **study bridge** (below) | `/study-plan` recommendation |
| screen / interview | interview ahead | JD gaps as probes (future: interview-prep) | prep notes |
| offer / rejected / withdrawn | terminal | application-tracker · **learn** | Learnings + dashboard patterns |

## Study bridge (gap → competency)
Link into the study system; don't duplicate it.
1. Collect the gaps the resume-reviewer personas surfaced — missing skills/keywords, weak areas, "would not interview because…".
2. Map each to a competency in the relevant study goal (default `Study/Goals/frontier-lab-fde/`). If a gap has no matching competency, flag it as a candidate to add via `/study-goal`.
3. Recommend `/study-plan` to push on the mapped competencies. Prep progress lives there, not in the pipeline.

## Worker ownership (don't cross these lines)
- **resume-reviewer** writes resume artifacts; the pipeline never edits resumes directly.
- **application-tracker** writes `Applications/**`; the pipeline never edits those records directly.
- **study-\*** owns prep tracking; the pipeline only surfaces and links.

## Run discipline
- Always re-read tracker state at the start — don't assume.
- Stop at each gate; the user approves transitions.
- After any worker acts, confirm application-tracker reflects the new state.
