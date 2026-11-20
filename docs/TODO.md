# Open items

What is not finished in this library. Newest first.

## 2026-11-14

- [ ] **Authenticated capture pass** — 64 packages name sign-in/account/
  checkout/submission surfaces they never reached, 51 more mark a gate in
  their access text; the queue is generated into [GATED.md](GATED.md)
  (`python3 tools/gated.py`). Needs the owner's accounts and a capture
  contract for authenticated regions before it can start.

## 2026-11-11

- [ ] **Batch-1 scorecard flags** — follow-ups the rubric reviews (#463) surfaced,
  graded honestly rather than softened. Package fixes: untokenised measured values
  (airbnb status roles + control heights; aaply `#2015ff` focus ring + `Times 16`
  fallback readings leaking into the spec; appwrite components.md has zero token
  annotation → C4 missing; spacing/type scales measured-but-not-tokenised on
  amie, apollographql, appwrite, untitled-stream, acuityscheduling); internal
  contradictions (1password accent is unresolved Knox `#0364d3` while every CTA
  paints `#145fe4`; acnestudios README cites a missing `icons/` dir and a font
  name tokens disagree with; anam README cites `core.size`/`core.layout` keys
  that don't exist; apollographql components.md lacks the checklist-coverage
  table). Missing `icons/` dirs on amie, appwrite, untitled-stream. Kit fixes:
  ~~capture never probes `prefers-reduced-motion` (F13 capped at partly ×20)~~
  done 2026-11-14: `tools/kit/capture/motion-probe.mjs` runs the reduced-motion
  pass and `motion.py` writes `core.motion` ([decision](decisions/0001-motion-tokens.md),
  [CAPTURE.md](CAPTURE.md#motion)); packages gain it when next recaptured, and
  F13's wording could later require it (a rubric version bump and a re-review of
  every package). Still open: capture never records z-index layers (F14 capped at
  partly ×20).
- [x] **Capture batches 2–21.** Done: on 2026-11-20 every row in
  [webapps-manifest.json](../webapps-manifest.json) is `captured` (414) or
  `uncapturable` (4); none is pending. Procedure:
  [HANDOVER.md](HANDOVER.md).

## 2026-10-24

- [ ] **Hevy package gaps** (`systems/hevy`), each claim checked against the package on
  2026-10-24. Still open and still true: the font family is unknown (`core.fontFamily.base` is
  `system`, evidence Not captured); the light values of the sheet, filter-sheet and wheel-band
  fills are Derived, not captured (`light.color.surface.sheet`, `sheetFilter`, `wheelBand`);
  there is no motion, no pressed state and no software keyboard (iPhone Mirroring hides it);
  and no capture shows a toast or a loading state, though t24, t93, t98 and t130 are named for
  one. The middle of long pages is unseen, but not "captured from the top only": 24 captures
  show a page below its top. Not yet re-done: a recapture that writes `patterns.md` and
  `components/` crops.
- [x] **Hevy style guide opened in a browser.** Done on 2026-10-24: it loads from a local
  server with no console errors and no sideways scroll, and the Light/Dark toggle switches the
  page background to `#000000`.
- [x] **Alke's token build still passes.** `ios/scripts/gen_tokens.py --check` in alke-fitness
  reports "tokens up to date" against the current `tokens.json`. A token rename still breaks it.

## 2026-10-10

- [x] **No GitHub remote.** Pushed to `c-wenlong/designs` (renamed from `design-systems`) on 2026-10-10.
  It now lives at `starship-terminal/constellations`, which is public as of 2026-11-20; the
  rights position (notice and takedown, 2026-11-21) is in [RIGHTS.md](RIGHTS.md).
- [ ] **The owner's work design system was not copied.** It is that employer's own product
  system, not a capture of another product, so it was left out on purpose. Add it if wanted.
- [ ] **`ai-engineering/README.md` does not list `design/design-systems`.** That repo had
  other uncommitted changes, so it was left alone.
- [ ] **self-learn keeps its own copy** of the nine reference packages under
  `docs/design/reference/`. Keep both, or replace self-learn's copy with a pointer here.
- [x] **DESIGN.md tier.** Done on 2026-10-11 as clones rather than a vendored copy:
  awesome-design-md and four other references sit under `example/`, gitignored, with
  [example/README.md](https://github.com/starship-terminal/constellations/blob/main/example/README.md) as the pointer index. They are unverified and
  never a source of values.
- [ ] **Hevy package gaps** (added 2026-10-10): checked and updated under 2026-10-24 above.
