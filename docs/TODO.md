# Open items

What is not finished in this library. Newest first.

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
- [ ] **Hevy package gaps** (`systems/hevy`, added 2026-10-10): font family unknown; light
  values of sheets, filter tiles and the wheel band derived, not captured; no motion, pressed
  states or keyboard; long pages captured from the top only. Its style guide has not been
  opened in a browser yet. The Alke app generates its Swift theme from this package's
  `tokens.json`, so a token rename breaks that build (`ios/scripts/gen_tokens.py --check`).
