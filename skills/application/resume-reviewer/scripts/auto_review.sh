#!/bin/bash
# Always-on watcher action (run by the launchd agent). For each job folder under
# $RESUME_WATCH_ROOT that needs a review, invoke `claude` headless to run the
# resume-reviewer skill and write RESUME_REVIEW.md — no interactive session needed.
#
# Folder convention: see scan_pending.sh.
#
# AUTONOMY: a headless run must use tools (web, bash, write) unattended. With the
# default permission mode it will stall on the first prompt. Set
#   RESUME_AUTOREVIEW_YOLO=1
# to pass --dangerously-skip-permissions, which is required for true hands-off
# operation. Only enable this for a folder containing your own resumes.

set -uo pipefail
WATCH_ROOT="${RESUME_WATCH_ROOT:-$HOME/Documents/resumes}"
CLAUDE_BIN="${CLAUDE_BIN:-$HOME/.local/bin/claude}"
LOG="$HOME/.claude/skills/resume-reviewer/auto_review.log"
mkdir -p "$(dirname "$LOG")"
log(){ echo "[$(date '+%F %T')] $*" >> "$LOG"; }

[ -d "$WATCH_ROOT" ] || { log "watch root missing: $WATCH_ROOT"; exit 0; }
[ -x "$CLAUDE_BIN" ] || { log "claude bin not executable: $CLAUDE_BIN"; exit 0; }

PERM=(--permission-mode acceptEdits)
[ "${RESUME_AUTOREVIEW_YOLO:-0}" = "1" ] && PERM=(--dangerously-skip-permissions)

shopt -s nullglob
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
  log "Reviewing: $dir (resume: $(basename "$resume"))"
  job="$(tr '\n' ' ' < "${dir}job.txt")"
  prompt="Use the resume-reviewer skill. Resume file: ${resume}. Target role/company/job-link (from job.txt): ${job}. Run the full workflow (research + both persona subagents) and write the result to RESUME_REVIEW.md in this folder. Do not ask questions; if an input is missing, note it in the review and proceed."
  if ( cd "$dir" && "$CLAUDE_BIN" -p "$prompt" "${PERM[@]}" >> "$LOG" 2>&1 ); then
    log "Done: $dir"
  else
    log "FAILED: $dir (exit $?). If it stalled on permissions, set RESUME_AUTOREVIEW_YOLO=1."
  fi
done
