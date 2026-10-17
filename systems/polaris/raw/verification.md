# Verification

2026-09-25, local Chromium browser through Codex computer use.

- Built bundled React gallery successfully with esbuild.
- All 13 guide sections reached their expected heading and were captured as full-page PNGs.
- Modal open and popover open states captured separately.
- Browser console reported no warnings or errors during section traversal.
- Product title input edited; status select changed to Draft; Track quantity checkbox unchecked.
- Modal opened with dialog role and title; Cancel dismissed it.
- Popover opened and Duplicate dismissed it; Active tab updated selected state.
- Icon search for Search returned Search, SearchList, SearchRecent and SearchResource.
- Text-only medium buttons measured equal 12px left/right padding; micro measured 8px each. Icon buttons intentionally use component-defined asymmetric edge padding.
- Import page loaded all 43 board/component SVG preview images with nonzero natural width, and had no horizontal overflow at the tested desktop viewport.
- SVG board visually inspected in browser after final font embedding and layout change.
- All SVG files parsed as XML; token JSON parsed successfully.
- All archived theme token values match published token package 9.4.2; zero differences.

Scope: desktop reference gallery. Not an exhaustive automated accessibility audit, device matrix, or native Figma/Paper import test. Component SVGs are editable redraws, not full CSS effect equivalents. Archive source React 13.10.1 differs from published preview React 13.9.5.

## Refresh, 2026-10-17

Headless Chromium through Playwright (`tools/screenshots.mjs`), against the gallery rebuilt from the same pinned packages.

- `npm ci --ignore-scripts` into a throwaway folder, then `npm run build` before any change: every committed output came back byte-identical, `assets/gallery.js` included.
- After the change, all 1,812 theme tokens in `tokens.json` resolve (through the new ramp aliases) to exactly their values in `raw/polaris-themes.raw.json`; the builder also throws if any alias would not.
- Screenshots 01 to 15 re-shot at 1440 px by the script (the originals were 1327 px wide, taken through computer use). New: 16 to 21 (app shell, toasts, states, delete confirmation, open tooltip), `screenshots/dark/` (nine sections in `dark-experimental`) and `screenshots/phone/` (the same nine at 390 px). The browser console reported no errors or warnings while shooting.
- Focus-visible: 23 controls focused after a Tab key press; all 23 matched `:focus-visible`. Crops in `screenshots/focus/` at 2x, computed changes in `focus-states.json`. Tabs use a roving tabindex, so the selected tab is the one captured.
- `dark-experimental` keeps the light input surface (`color-input-bg-surface` `#FDFDFD`) while `color-text` becomes `#E3E3E3`: typed text on inputs is 1.26:1 and unreadable in [dark/07-forms](../screenshots/dark/07-forms.png). Critical tokens do not change either; see [dark/05-buttons](../screenshots/dark/05-buttons.png).

## Layout move, 2026-10-17

The package moved to the standard layout: the tokens to `tokens.json`, the raw token inputs and everything from `evidence/` to `raw/`, and the component findings into `components.md`. The builders write the new paths.

- `npm ci --ignore-scripts`, `npm run build` and `tools/build_vectors.py` were run before and after the move. Every output came back byte-identical at its new path except `assets/gallery.js`, which changed only by its two links (`raw/provenance.json`, `components.md`) and the minifier's renaming that follows from them.
- `assets/inter-preview.ttf` differs on every run of `build_vectors.py` by its `head.modified` timestamp alone, so the committed copy was kept.
- The style guide, served by `tools/catalog.py serve`, fetched `assets/library.json`, `assets/tokens.json` and `assets/icons.json`, and its links to `raw/provenance.json` and `components.md` resolved.
