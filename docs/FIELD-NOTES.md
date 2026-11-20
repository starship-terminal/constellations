# Field notes

Things that actually went wrong while extracting designs, and the fix that
worked. Read alongside [CAPTURE.md](CAPTURE.md); this is the scar tissue.

| Symptom | Cause | Fix |
|---|---|---|
| 111 GB of `*.partN.png` tiles in a scratch dir | `lazyScroll` grows `scrollHeight` unboundedly on infinite-scroll pages, so the tile loop never terminates | Kit now clears stale tiles per shot and truncates at 8 chunks, logging the boundary (`tools/kit/capture/public/public.mjs`) |
| Page crashes into an error card after dismissing cookies | Consent buttons can POST (untitled's "Reject all" → `/settings/cookies` 403 → Remix error boundary) | Hide the overlay; never click a consent button |
| Cloudflare "verify" page on every navigation | Headless fingerprint | `navigator.webdriver` mask, a fresh context per route, headed Chrome as last resort; still-blocked routes are documented boundaries, not failures |
| Components measure transparent wrapper divs (Tilda sites) | Tilda wraps painted atoms in zero-height `.t396__elem` wrappers | Measure the `.tn-atom` child; use `data-elem-type` + rect size to identify elements |
| Measurements land on invisible elements | Frameworks keep hidden animation duplicates in the DOM (opacity 0, negative x) | Require `opacity > 0` and an on-screen rect in selectors; mobile headlines may split one painted atom per line |
| A selector catches the whole page | Text search climbing past the component's bounds, or a fallback like `nav.last()` firing | Mark the target with `data-m-mark` from a constrained evaluate; never fall back to a generic wrapper — record the miss |
| Price/label selectors miss | Text split across sibling atoms ("$" + ".1 /month") | Match the leaf atom that carries the distinctive text |
| `focus-visible` saved but focus never landed | Element is not keyboard-focusable; `kbFocus` returns "focus failed" | Builders count a failed `via` as not captured |
| Re-run marks old readings with a new date | `comp()` rewrites `run` before the selector misses | Keep the earlier evidence's original page/run/url; record `recaptureMissed` |
| Old `.partN` tiles stitch over a fresh shot | Tiles from a previous taller capture left in raw/ | Clear `name.part*` before writing the new shot |
| `measure.mjs` never exits | Browser/contexts opened but never closed | `try/finally` that closes page, context and browser |
| Menu/button selector matches nothing | Icon-only controls have `aria-label` but no text | Select on `aria-label`/role, not `has-text` |
| App is unreachable, only marketing exists | Auth host 404s or gates headless (go.aaply.app "Not found", start.1password.com unsupported-browser) | Capture the public surface, record the boundary verbatim in README + catalog `capture.gaps` |
| Style guide renders empty swatches/samples | Template references names the builder never emits | Component tokens emit `--component-*`; a theme set strips its prefix (`light.page` → `--page`); resolve `{aliases}` to `var()` |
| A Refero style used as app evidence | Refero packages are interpreted landing-page snapshots | Only `systems/` packages are measured evidence; never infer flows from a style |

## Agent operation notes

- One worktree per app under `/private/tmp/ds-<slug>`; agents must not share a checkout.
- Scratch captures belong outside the repo (`~/.design-systems/<slug>/raw-full`); they are not committed and can be deleted when a run dies.
- Long-running node capture scripts need explicit browser/context cleanup or the shell looks hung.
- Greptile reviews land on every PR; the recurring valid findings are the first nine rows above — fixing them in the kit/tools once beats patching each package.
- A headless Linux homeserver can run the whole public-capture pipeline (the deel package was captured, built and PR'd from one). Without a `.venv` (it is gitignored; `make setup` creates one) use the system python (`PYTHON=/usr/bin/python3 make …`) — the repo tools are stdlib-only and `uv run --with pillow --with numpy` covers Pillow/numpy. Tesseract for `redact_images.py` installs user-level via `/nix/var/nix/profiles/default/bin/nix profile install nixpkgs#tesseract --profile ~/.nix-profile` when `~/.nix-profile/bin` is on PATH but `nix` is not; OCR is then identical to the Mac's. Liberation + Noto Color Emoji fonts are installed the same way for fallback-font parity (see HANDOVER.md "Running on the Linux homeserver" for the full toolchain and the Apple-fonts caveat).
