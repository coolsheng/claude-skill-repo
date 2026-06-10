#!/usr/bin/env python3
"""Resume structural + lint checker.

Usage:
    python3 check_resume.py <path-to-resume.(pdf|md|txt)>

Extracts text from a PDF (via pdfplumber or pypdf, if installed) or reads a
Markdown/plain-text file directly, then reports:
  - which standard sections are present / missing
  - contact essentials (email, phone, LinkedIn)
  - flagged lines: pronouns, weak/filler verbs, un-quantified bullets,
    overlong bullets, passive voice, mixed tense signals

Heuristics over-flag by design. Treat output as SIGNAL for a human reviewer,
not a verdict. Pure stdlib except optional PDF libs.
"""

import re
import sys
from pathlib import Path

# --- Configuration ---------------------------------------------------------

SECTION_ALIASES = {
    "contact": ["contact", "email", "phone"],  # often unlabeled; handled separately
    "summary": ["summary", "profile", "objective", "about"],
    "experience": ["experience", "employment", "work history", "professional experience"],
    "education": ["education", "academic"],
    "skills": ["skills", "technical skills", "technologies", "competencies"],
    "projects": ["projects", "personal projects", "selected projects"],
}
EXPECTED_CORE = ["experience", "education", "skills"]

WEAK_OPENERS = [
    "responsible for", "worked on", "helped with", "helped to", "assisted",
    "duties included", "tasked with", "involved in", "in charge of",
    "participated in", "contributed to",
]
PRONOUNS = [r"\bI\b", r"\bme\b", r"\bmy\b", r"\bmine\b", r"\bwe\b", r"\bour\b"]
PASSIVE = re.compile(r"\b(was|were|been|being|is|are)\b\s+\w+ed\b", re.IGNORECASE)
PRESENT_VERB_HINT = re.compile(r"^\s*[-*•]?\s*(manage|lead|build|develop|design|create|maintain|own)s?\b", re.IGNORECASE)
PAST_VERB_HINT = re.compile(r"^\s*[-*•]?\s*\w+ed\b", re.IGNORECASE)
BULLET_RE = re.compile(r"^\s*[-*•·▪]\s+")
HAS_NUMBER = re.compile(r"[\d%$]")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"(\+?\d[\d\s().-]{7,}\d)")
LINKEDIN_RE = re.compile(r"linkedin\.com/\S+", re.IGNORECASE)
OVERLONG_WORDS = 32

# --- Text extraction -------------------------------------------------------

def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in (".md", ".txt", ".markdown", ""):
        return path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".pdf":
        return extract_pdf(path)
    raise SystemExit(
        f"Unsupported file type: {suffix or '(none)'}. "
        "Supported: .pdf, .md, .txt. For DOCX, export to PDF or paste as Markdown."
    )


def extract_pdf(path: Path) -> str:
    try:
        import pdfplumber  # type: ignore
        with pdfplumber.open(str(path)) as pdf:
            return "\n".join((page.extract_text() or "") for page in pdf.pages)
    except ImportError:
        pass
    try:
        from pypdf import PdfReader  # type: ignore
        reader = PdfReader(str(path))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except ImportError:
        pass
    raise SystemExit(
        "No PDF library found. Install one of:\n"
        "    pip install pdfplumber    (best extraction)\n"
        "    pip install pypdf\n"
        "...or re-export the resume as Markdown/plain text and pass that instead."
    )


def sanitize(text: str) -> str:
    # normalize whitespace, strip non-printable control chars (keep newlines/tabs)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "".join(ch for ch in text if ch == "\n" or ch == "\t" or ord(ch) >= 32)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

# --- Checks ----------------------------------------------------------------

def find_sections(text: str) -> dict:
    low = text.lower()
    found = {}
    for section, aliases in SECTION_ALIASES.items():
        if section == "contact":
            continue
        found[section] = any(
            re.search(rf"(?m)^\s*#*\s*{re.escape(a)}\b", low) or
            re.search(rf"(?m)^\s*{re.escape(a)}\s*:?\s*$", low)
            for a in aliases
        )
    return found


def check_contact(text: str) -> dict:
    head = "\n".join(text.splitlines()[:15])  # contact info is usually near the top
    return {
        "email": bool(EMAIL_RE.search(text)),
        "phone": bool(PHONE_RE.search(head)),
        "linkedin": bool(LINKEDIN_RE.search(text)),
    }


def lint_lines(text: str) -> list:
    findings = []
    present, past = 0, 0
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        low = line.lower()
        is_bullet = bool(BULLET_RE.match(raw)) or low.startswith(tuple(WEAK_OPENERS))

        for w in WEAK_OPENERS:
            if w in low:
                findings.append((i, "weak/filler verb", f"'{w}' → lead with a strong action verb", line))
                break
        for p in PRONOUNS:
            if re.search(p, line):
                findings.append((i, "first-person pronoun", "drop pronouns from resume bullets", line))
                break
        if is_bullet:
            words = len(line.split())
            if not HAS_NUMBER.search(line):
                findings.append((i, "no quantification", "add a metric/scope or confirm none exists", line))
            if words > OVERLONG_WORDS:
                findings.append((i, "overlong bullet", f"{words} words — tighten to one idea", line))
            if PASSIVE.search(line):
                findings.append((i, "possible passive voice", "rephrase as active, verb-led", line))
            if PRESENT_VERB_HINT.match(raw):
                present += 1
            elif PAST_VERB_HINT.match(raw):
                past += 1
    tense_note = None
    if present and past:
        tense_note = (f"Mixed tense across bullets (~{present} present-leaning, ~{past} past-leaning). "
                      "Use present for current role, past for prior roles — applied consistently.")
    return findings, tense_note

# --- Report ----------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 check_resume.py <path-to-resume.(pdf|md|txt)>")
    path = Path(sys.argv[1]).expanduser()
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    text = sanitize(extract_text(path))
    if not text.strip():
        raise SystemExit("No text extracted. If this is a scanned/image PDF, OCR it or paste as Markdown.")

    sections = find_sections(text)
    contact = check_contact(text)
    findings, tense_note = lint_lines(text)
    words = len(text.split())

    print(f"=== Resume check: {path.name} ===")
    print(f"Word count: {words}  (~{max(1, round(words/500))} page-equivalent)\n")

    print("SECTIONS")
    for sec, ok in sections.items():
        mark = "✓" if ok else "·"
        core = " (core, MISSING)" if (not ok and sec in EXPECTED_CORE) else ""
        print(f"  {mark} {sec}{core}")
    print()

    print("CONTACT ESSENTIALS")
    for k, ok in contact.items():
        print(f"  {'✓' if ok else '✗'} {k}")
    print()

    if tense_note:
        print("TENSE\n  ⚠ " + tense_note + "\n")

    print(f"FLAGGED LINES ({len(findings)})  — heuristic; verify before acting")
    if not findings:
        print("  none")
    else:
        for ln, kind, hint, line in findings[:80]:
            snippet = (line[:90] + "…") if len(line) > 90 else line
            print(f"  L{ln} [{kind}] {hint}")
            print(f"      {snippet}")
        if len(findings) > 80:
            print(f"  …and {len(findings) - 80} more")


if __name__ == "__main__":
    main()
