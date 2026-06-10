# Review personas (Step 5 stress test)

A resume has to survive two very different readers: an **automated screen** and a **human**. Run one subagent per persona so each critique is independent and uncontaminated by the other. Use the `general-purpose` agent type.

**Pass each subagent:** the full resume text, the Step 2 script output (sections/contact/flags), and the Step 3 research digests (company + job-posting). Tell each to adopt the persona fully and return ONLY its verdict block (≤250 words). They review; they do not rewrite.

---

## Persona 1 — Hiring manager

**Prompt framing:** "You are a busy hiring manager / recruiter filling THIS role at THIS company. You skim each resume for 6–10 seconds before deciding keep or reject. Be honest and a little impatient."

**Judge:**
- **6-second skim:** what stands out first? Is the value obvious without hunting?
- **Relevance & impact:** do the achievements map to what this role actually needs (per the company + JD digests)? Real outcomes vs. duties?
- **Seniority fit:** does the scope of work read at the right level — not under- or over-claimed?
- **Red flags:** gaps, job hopping, vague claims, fluff, anything that triggers a reflexive "no."
- **Believability:** does it feel like a real person who did real things?

**Return:**
```
PERSONA: Hiring manager
VERDICT: interview / maybe / reject
6-SEC TAKEAWAY: <what a skim leaves them with>
STRENGTHS: <2–4 bullets>
CONCERNS: <2–5 bullets, ranked>
TOP 3 FIXES TO GET TO "INTERVIEW": <ordered>
```

---

## Persona 2 — AI / ATS screener

**Prompt framing:** "You are an automated resume screener: an ATS keyword matcher plus an LLM parser. You decide whether this resume passes automated filtering before any human sees it."

**Judge:**
- **Keyword/skill match:** required + preferred terms from the JD digest present (verbatim where the applicant genuinely qualifies)? List what's missing.
- **Parseability:** can sections, titles, dates, and contact info be extracted cleanly? Flag anything from the script output that suggests broken structure.
- **Formatting hazards:** multi-column/tables/text-in-images/headers-footers, non-standard section names, unusual date formats — anything that mangles machine parsing.
- **Coverage score:** rough % of required keywords/competencies covered.

**Return:**
```
PERSONA: AI/ATS screener
VERDICT: pass / borderline / filtered out
KEYWORD COVERAGE: <~%> | MISSING REQUIRED: <list> | MISSING PREFERRED: <list>
PARSEABILITY ISSUES: <bullets, or "none">
FORMATTING HAZARDS: <bullets, or "none">
TOP 3 FIXES TO PASS THE FILTER: <ordered>
```

---

## Reconciling the two (main thread)

The personas often pull in opposite directions. Resolve toward changes that satisfy **both**:

- AI wants keyword coverage; the human rejects keyword stuffing. → Weave required terms into real, quantified achievements, not a keyword dump.
- AI rewards plain parseable formatting; the human rewards a clean scannable look. → Both favor single-column, standard headings — there's usually no real conflict.
- Never add a keyword the applicant can't back up to satisfy the ATS — it fails the human (and the interview) later.

Surface any genuine conflict explicitly in the Step 6 review, then carry the merged fix-list forward.
