# Master resume template (the canonical base)

The user maintains ONE master resume at `Applications/Resume_Master.md` (vault: `<vault-root>/Applications/`). Every review-mode run starts from it; tailored copies live in `Applications/<company>/Resume_<Company>_<Role>.md`. **Never send or review the master as if it were an application resume — it's the source, not the artifact.**

## Why a master

Tailoring from a previous company's tailored resume carries that company's framing (header gates, compressed details, dropped keywords) into the new application — the exact trap that cost a "filtered out" ATS verdict once. The master keeps the richest truthful version; tailoring only ever *removes or rewords*, never un-tailors.

## Structure rules

- Guidance lives in Obsidian `%%…%%` comments (visible while editing, invisible in preview, stripped on export).
- Top-of-file `%%` block = tailoring checklist (header-gate recheck, literal keyword diff, no em-dashes / no first person, outcome-based bullets, vendor-name compression policy, semantic-ATS mirroring).
- Header contains a `<ROLE-GATE LINE>` placeholder plus `%%` comment listing the known gate patterns (US relocation + E-3; remote timezone band + EOR + travel). Pick/adapt per role.
- Section-level `%%` comments mark tailoring levers (Summary first sentence in the JD's dimensions; Skills reordered so required skills lead; dated client bullets stay reverse-chronological, tailored by expand/compress).
- Content rules follow `best-practices.md` + `voice-and-bullets.md` (outcome-based bullets, no fabrication, targets labeled as targets).

## At the start of every review run

1. **Exists?** If `Applications/Resume_Master.md` exists, use it as the tailoring base (alongside any prior tailored version for the same company).
2. **Missing?** Offer the user two paths — never silently skip:
   - **Import:** they point to an existing resume (PDF/Markdown); convert it into the master format (add the `%%` checklist, gate-line placeholder, section levers) and confirm content survived intact.
   - **Build Socratically:** interview them section by section — contact/links; each role (company, title, dates, then per engagement: what changed because they were there, pressing for a number or scope per bullet); ventures/projects; education; skills last (derived from the bullets, not asserted). One section at a time, draft as you go, read each back for correction. Never invent — a missing metric stays missing until they supply it.
3. **Drift check (always, even when the master exists):** ask the user what has changed since the master was last touched — new role/promotion, finished engagements, fresh metrics (targets that became results), new tools/projects. Fold confirmed changes into the **master first**, then tailor from the updated master. The master's value decays silently without this.

## After a run

If tailoring surfaced content worth keeping (a newly quantified bullet, a better framing the user approved), back-port it to the master so future applications inherit it.
