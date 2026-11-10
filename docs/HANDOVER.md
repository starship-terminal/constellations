# Handover: capture batches

Everything a fresh agent needs to pick up the web-capture program
(batch-2 onward). Read [AGENTS.md](../AGENTS.md),
[CAPTURE.md](CAPTURE.md), and [FIELD-NOTES.md](FIELD-NOTES.md) first —
this file is the program-level glue, not a replacement.

## The queue

[webapps-manifest.json](../webapps-manifest.json) on `main` is the
source of truth: 418 catalog domains, `batch` 1–20 per app, ~20 per
batch. Batch 1 is done (`status: "captured"`, `package:
"systems/<slug>"`). Work the next `pending` batch in order. When a PR
merges, set `status: "captured"` + `package` in the same commit as the
last merge train (one manifest PR per batch is fine).

## Per app

1. **Worktree, always.** `git worktree add /private/tmp/ds-<slug> -b
   capture-<slug> origin/main` from the repo root. Never share a
   checkout between agents. Reuse an existing worktree's partial work
   if a prior run died.
2. Copy `tools/kit/` → `systems/<slug>/tools/`, adapt the page
   runners/selectors to the site's real DOM.
3. Playwright lives at `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright`;
   run `make setup` (or point `PYTHON` at the repo `.venv`) for Pillow.
4. Capture public surfaces honestly: desktop 1440×900 + mobile 390×844,
   consent/overlays handled per FIELD-NOTES (hide, never click a
   consent POST), authenticated regions documented as boundaries —
   never inferred.
5. `make brief && make design-md && make grade && make check` green;
   `python3 tools/refero/coverage.py` when check flags it stale; all
   binaries are LFS.
6. **Rubric review before done** — `python3 tools/grade.py --write
   --review <slug>=<grades.json> --method "<how>"`; every non-`yes`
   criterion gets a written justification (AGENTS.md rule).
7. One PR per app (`gh pr create`); catalog `capture` block carries
   `pr`, `durationMin`/`durationNote`, `route`, `model`, `date`.
8. Greptile will review: fix valid comments in the package's own
   builders, reply `in_reply_to` on every comment, resolve every
   thread via GraphQL `resolveReviewThread`. Then merge
   `origin/main` (`--theirs` for catalog.json/README.md/AGENTS.md/
   scorecard/refero-coverage/media-taxonomy; re-append your package's
   catalog entry + category keys; bump AGENTS "the packages (N)" to
   the real `systems/` dir count), regenerate, re-check, push.
9. Merge when every thread is resolved (`gh pr merge --squash`), then
   **clean up**: `git worktree remove`, delete `~/.design-systems/<slug>`,
   delete the merged branch.

## Batch-1 lessons (verified)

- ~200 Greptile comments across 19 packages clustered into a dozen
  recurring patterns — they are all in FIELD-NOTES.md; fixing them in
  the kit/tools once beats patching each package.
- GitHub's `mergeable` lags: after each squash merge, sibling PRs go
  CONFLICTING on the shared generated files. Budget one
  merge-main+regen cycle per PR; the procedure above is mechanical.
- CI (check/app/build/web jobs) fails fast on a repo billing issue —
  known, not a code failure; local `make check` is the gate.
- Parallelism: one worktree per app + background subagents works;
  transcripts die on session churn but worktrees survive on disk.
- Scratch dirs can fill the disk (an unbounded tiler once wrote
  111 GB) — the kit caps tiling at 8 chunks; delete dead runs' scratch.
