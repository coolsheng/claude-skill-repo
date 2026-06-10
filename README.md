# claude-skill-repo

How I've been working with Claude Code — packaged as skills you can drop into your own setup.

Three skill sets: **substack writing**, a **study system**, and a **job-application pipeline**. Each skill lives in its own folder under `skills/<category>/` and is a self-contained Claude Code skill (a `SKILL.md` with frontmatter, plus any supporting files). Paths that pointed at my machine are replaced with placeholders like `<vault-root>` and `<writing-repo>` — swap in your own before use.

## Substack writing (`skills/substack/`)

| Skill | What it does |
|---|---|
| [substack-pipeline](skills/substack/substack-pipeline) | Entry point/orchestrator. Detects what stage an essay is at and routes it to the right sub-skill; maintains a living `voice-profile.md` the other skills calibrate from. |
| [substack-scaffolder](skills/substack/substack-scaffolder) | Turns a topic + braindump into a recommended outline (your fragments slotted under each heading) plus 1–2 alternative angles. |
| [substack-distiller](skills/substack/substack-distiller) | Distills a messy braindump or bloated draft into a coherent post — two passes, a faithful tighten and a bolder rewrite, so you can mix and match. Gates on thesis. |
| [substack-reviewer](skills/substack/substack-reviewer) | Surgical diagnosis of a draft. Auto-detects genre/tone, proposes a leaner restructure, then flags up to three named, line-referenced issues. Diagnostic only — does not rewrite. |
| [substack-polish-sweep](skills/substack/substack-polish-sweep) | Final mechanical sweep before ship — grammar, typos, hedge-budget breaches, and voice-drift patterns that survive earlier passes. |

### How to use

The skills chain along the life of one essay, with you doing the actual writing in between:

```
idea + braindump
   → /substack-scaffolder     outline with your fragments slotted in
   → (you write the draft)
   → /substack-distiller      two shaped passes — pick lines from each
   → /substack-reviewer       up to 3 named issues; you fix them
   → /substack-polish-sweep   typos/grammar/drift right before pasting into Substack
```

If you don't want to remember the stages, just run `/substack-pipeline` (or ask "where am I on this essay?") — it inspects the essay folder's artifacts, tells you the stage, and routes to the right sub-skill. Each skill also works standalone: paste a draft and ask for a review, or hand over a braindump and ask it to "tighten this".

Two conventions make the chain work: each essay lives in its own folder (`<writing-repo>/substack-draft-articles/<slug>/`) where every skill reads and writes its artifacts, and a single `voice-profile.md` next to those folders holds the current voice snapshot — the pipeline updates it after each ship, and the distiller/reviewer/polish-sweep read it for calibration.

## Study system (`skills/study/`)

| Skill | What it does |
|---|---|
| [study-goal](skills/study/study-goal) | Scaffolds a long-term learning goal — Socratic gap diagnosis, competencies, milestones with observable outcomes. |
| [study-plan](skills/study/study-plan) | Plans today's study session(s) dynamically against active goals; supports multiple goals in parallel. |
| [study-note](skills/study/study-note) | Captures an atomic insight mid-session as a linked note, auto-tagged to the active goal. |
| [study-audit](skills/study/study-audit) | Realism audit of active goals — catches milestone slippage *before* deadlines pass by projecting pace. |
| [quant-tutor](skills/study/quant-tutor) | Interactive quant/probability tutor — one problem at a time, free-typed answers, the named cognitive trap explained. |

### How to use

The study system is goal-first: structure lives in an Obsidian vault (set `<vault-root>` in each SKILL.md to yours), sessions are planned dynamically.

```
/study-goal      once per ambition — diagnose gaps, set competencies + milestones
/study-plan      each time you sit down — designs today's session against active goals
/study-note      mid-session, whenever something clicks — atomic note, auto-tagged
/study-audit     periodically (or auto-fired by study-plan) — are the deadlines still honest?
```

Start with `/study-goal` for anything ambitious ("get a job at X", "be fluent in Spanish"). It deliberately does *not* prescribe resources — `/study-plan` picks activities live each session, against the milestones, based on what you want to push on that day. `/quant-tutor` is a worked example of a drill skill that plugs into a study goal: it tracks calibration in a state file inside the goal and serves problems at your level.

## Job applications (`skills/application/`)

| Skill | What it does |
|---|---|
| [job-search-pipeline](skills/application/job-search-pipeline) | Orchestrates the end-to-end search — detects where each application stands and routes it to the right next step. |
| [resume-reviewer](skills/application/resume-reviewer) | Reviews/tailors a resume for a role+company (researches the company, stress-tests via hiring-manager + ATS persona subagents), or compares one resume across multiple roles. |
| [application-tracker](skills/application/application-tracker) | Tracks applications per company with a status lifecycle (drafting→applied→screen→interview→offer/rejected/withdrawn) and a cross-application patterns dashboard. |

### How to use

`/job-search-pipeline` is the entry point — share a job link or say "I want to apply to X" and it routes each application through the stages, stopping at every gate so you stay in control:

```
job link / "apply to X"
   → resume-reviewer        compare roles if undecided, then tailor the resume
   → application-tracker    log the application + tailoring choices used
   → (interview prep)       gaps get bridged via /study-plan in the study system
   → application-tracker    record the outcome; learnings feed the next tailoring run
```

You can also drive the workers directly: "review my resume for <role>" (resume-reviewer), "I got a screen at X" or "what's been converting?" (application-tracker). The tracker is the memory of the set — resume-reviewer consults it for prior learnings before tailoring, and the pipeline reads it to know what's next. Records live in the vault per company; outcomes are never fabricated.

## Install

Each skill is just a folder. Drop it into your Claude Code skills directory:

```bash
# user-level (available in every project) — install a whole category
cp -r skills/substack/* ~/.claude/skills/

# or just one
cp -r skills/substack/substack-distiller ~/.claude/skills/

# or project-level (scoped to one repo)
cp -r skills/substack/substack-distiller .claude/skills/
```

Restart Claude Code (or start a new session) and the skill will show up. Invoke it by name (`/substack-distiller`) or let it auto-trigger from its description. Before first use, search the skill's files for `<vault-root>`, `<writing-repo>`, and `/Users/<you>` and point them at your own setup.

## Layout

```
skills/
  substack/
  study/
  application/
    <skill-name>/
      SKILL.md          # frontmatter + instructions
      references/       # optional supporting files
```

The `SKILL.md` frontmatter follows the standard Claude Code skill format:

```yaml
---
name: skill-name
description: When to use this skill and what it does.
---
```

## License

MIT — see [LICENSE](LICENSE).
