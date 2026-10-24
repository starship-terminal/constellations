# Open items

What is not finished in this library. Newest first.

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

- [x] **No GitHub remote.** Pushed to the private `c-wenlong/design-systems` on 2026-10-10.
  It must stay private ([RIGHTS.md](RIGHTS.md)).
- [ ] **The owner's work design system was not copied.** It is that employer's own product
  system, not a capture of another product, so it was left out on purpose. Add it if wanted.
- [ ] **`ai-engineering/README.md` does not list `design/design-systems`.** That repo had
  other uncommitted changes, so it was left alone.
- [ ] **self-learn keeps its own copy** of the nine reference packages under
  `docs/design/reference/`. Keep both, or replace self-learn's copy with a pointer here.
- [x] **DESIGN.md tier.** Done on 2026-10-11 as clones rather than a vendored copy:
  awesome-design-md and four other references sit under `example/`, gitignored, with
  [example/README.md](https://github.com/c-wenlong/design-systems/blob/main/example/README.md) as the pointer index. They are unverified and
  never a source of values.
- [ ] **Hevy package gaps** (added 2026-10-10): checked and updated under 2026-10-24 above.
