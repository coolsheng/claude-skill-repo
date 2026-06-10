# Research brief for subagents

All web research for this skill is delegated to subagents so the main thread stays lean. Give each subagent the relevant brief below and require it to return **only the digest** — not raw pages, not its browsing trace. Keep each digest under ~250 words.

Use the `general-purpose` agent type (it has WebSearch/WebFetch). Run the two subagents in parallel when both inputs exist.

## Subagent A — Company research

**Input:** company name (+ website if known), target role, applicant's industry.

**Task:** Identify what the company does, its mission/values, the tone/voice it uses about itself, notable recent products/news, and — most importantly — the vocabulary and priorities it repeats. The point is to surface language the resume should honestly echo.

**Return exactly this digest:**
```
COMPANY: <name>
WHAT THEY DO: <1–2 lines>
MISSION/VALUES: <bullets>
VOICE/TONE: <how they describe themselves — formal/scrappy/mission-driven/etc.>
KEY VOCABULARY: <8–15 words/phrases they repeat (products, values, domain terms)>
PRIORITIES/SIGNALS: <what they seem to reward in candidates>
RECENT/NOTABLE: <0–3 items, only if relevant to framing>
SOURCES: <urls>
CONFIDENCE: <high/med/low + why>
```

## Subagent B — Job-posting research

**Input:** application/job-posting URL (or pasted JD text), target role + seniority.

**Task:** Fetch the posting and extract what the resume must align to. Distinguish required vs. preferred. Capture the *exact* keywords/phrasing (for ATS + recruiter scanning).

**Return exactly this digest:**
```
ROLE: <title> | SENIORITY: <level signals>
REQUIRED SKILLS: <list, verbatim terms where possible>
PREFERRED SKILLS: <list>
CORE RESPONSIBILITIES: <bullets>
KEYWORDS TO MIRROR: <the literal terms the resume should contain if true>
SCOPE/IMPACT EXPECTED: <e.g. ownership, leadership, scale>
RED FLAGS / MUST-HAVES: <hard gates, e.g. clearance, years, location>
SOURCES: <url>
CONFIDENCE: <high/med/low + why>
```

## Rules for the caller (main thread)

- Never browse the web yourself — delegate. Only synthesize the returned digests.
- If an input is missing, skip that subagent and note the gap to the user.
- If a digest returns low confidence or empty (dead link, paywall, offline), say so and fall back to generic role norms from `best-practices.md`.
- Mirror keywords/language **only when the applicant genuinely has the experience** — never fabricate to match a JD.
