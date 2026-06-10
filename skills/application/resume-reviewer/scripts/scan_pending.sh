#!/bin/bash
# SessionStart hook: surface resumes awaiting review so Claude auto-runs the
# resume-reviewer skill in-session. Prints an instruction block to stdout (which
# the SessionStart hook injects as context). Silent + exit 0 when nothing pending.
#
# A "job folder" = a subfolder of $RESUME_WATCH_ROOT containing:
#   - job.txt          (target role/company + job-posting URL)
#   - one resume file  (*.pdf / *.md / *.markdown / *.txt)
# It "needs review" when RESUME_REVIEW.md is missing or older than the inputs.

WATCH_ROOT="${RESUME_WATCH_ROOT:-$HOME/Documents/resumes}"
[ -d "$WATCH_ROOT" ] || exit 0
shopt -s nullglob

pending=()
for dir in "$WATCH_ROOT"/*/; do
  [ -f "${dir}job.txt" ] || continue
  resume=""
  for f in "${dir}"*.pdf "${dir}"*.md "${dir}"*.markdown "${dir}"*.txt; do
    b="$(basename "$f")"
    [ "$b" = "job.txt" ] && continue
    [ "$b" = "RESUME_REVIEW.md" ] && continue
    resume="$f"; break
  done
  [ -n "$resume" ] || continue
  review="${dir}RESUME_REVIEW.md"
  if [ -f "$review" ] && [ ! "$resume" -nt "$review" ] && [ ! "${dir}job.txt" -nt "$review" ]; then
    continue
  fi
  pending+=("$dir")
done

[ ${#pending[@]} -eq 0 ] && exit 0

echo "AUTOMATED RESUME REVIEW — ${#pending[@]} resume(s) in $WATCH_ROOT need a review:"
for d in "${pending[@]}"; do echo "  - $d"; done
echo "For each folder above, run the resume-reviewer skill: read job.txt for the target role/company/job-link, review the resume file, and write RESUME_REVIEW.md into that same folder. Proceed without asking; note any missing inputs in the review."
exit 0
