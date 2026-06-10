# Compare mode — role-fit analysis

Used when the applicant has ONE resume and is deciding between **2+ roles/applications**. Goal: a clear, honest recommendation on which role best fits their skill set and trajectory — not a resume critique (that's review mode).

## Build the capability profile first

From the resume (use `scripts/check_resume.py` + a read), extract the applicant's:
- **Core skills & stack** (with depth/recency), **domains** (e.g. fintech, BaaS), **scope/seniority** evidenced, **standout achievements** (quantified), **trajectory** (where they're heading), and stated **preferences/constraints** if given (location, comp, IC vs. lead).

## Score each role on the same dimensions

Research each role via subagents (one job-posting+company digest per role, in parallel — see `research-brief.md`). Then score every role 1–5 on:

| Dimension | What it measures |
|---|---|
| **Requirement coverage** | % of required/preferred skills the applicant genuinely has |
| **Strength alignment** | Does the role *use their best work*, or sideline it? |
| **Seniority fit** | Level match — under-leveled (bored/underpaid) vs. over-reach |
| **Domain fit** | Industry/domain overlap with their experience |
| **Trajectory fit** | Does it move them toward their stated goals / a stronger next step? |
| **Logistics** | Location, comp band, IC/lead, and **visa pathway feasibility** — hard gates first. A low-friction pathway materially de-risks a cross-border role (e.g. the E-3 for Australians targeting US roles); a sponsorship-dependent role with no clear pathway scores low. |
| **Narrative distance** | How much the resume must be reworked to be competitive (less = easier win) |
| **Differentiation** | Would the applicant stand out vs. a typical applicant pool, or blend in? |

Keep it honest: a role the applicant *wants* but isn't competitive for should score low on coverage/differentiation even if trajectory is high — say so.

## Optional per-role fit check (subagent)

For a sharper read, spawn one hiring-manager-persona subagent per role (see `review-personas.md`) asking "would you interview THIS candidate for THIS role, and why/why not?" Use the verdicts as evidence in the comparison.

## Deliver the comparison (write to `RESUME_COMPARISON.md`)

- **Header** — resume file, the roles compared (title/company/link), date, confidence caveats.
- **Capability profile** — short summary of the applicant's strengths/trajectory.
- **Side-by-side matrix** — roles as columns, the dimensions above as rows, with 1–5 scores.
- **Per-role read** — 2–3 lines each: where they're strong, where they're short, hard gates.
- **Recommendation** — which role fits better and *why*, in plain terms. State the tradeoff, not just a winner (e.g. "Role A is the higher-probability offer; Role B is the better long-term bet but needs X").
- **If you pursue each** — the 2–3 things to emphasize/add on the resume for that specific role (hand off to review mode for the full tailoring).
- **Open questions** — preferences that would change the call (comp floor, relocation, IC vs. lead).

Never fabricate fit. If the resume genuinely suits neither well, or a third path fits better, say that.
