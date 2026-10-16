# Gemini Notebook (NotebookLM) design reference

A token set, component reference and pattern notes for Google's Gemini Notebook (formerly NotebookLM), for building mockups that match the product. Recaptured from notebook.google.com on 2026-10-17 while signed in, in the UI generation Google ships as "luminous": near-black and off-white surfaces, one variable family (Google Sans Flex) and pill buttons. The 2026-09-25 capture of the earlier lavender UI is replaced, not merged; the product no longer paints those values.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (palettes, type, radii, spacing, sizes, focus ring, breakpoints, layout, z-index, motion, reduced motion, opacities, Material's shadow levels), `light` and `dark` semantic sets with identical keys, and `$themes`. Every token has `$extensions.source` |
| [components.md](components.md) | 64 components, each state as a table of token names (dark and light), with crops. Built from the measurements |
| [patterns.md](patterns.md) | App shell, forms and validation, empty/loading/error, destructive confirmation, feedback, search, data display, onboarding |
| [style-guide.html](style-guide.html) | One page rendering every token and every component crop, with a light/dark switch |
| [icons/INDEX.tsv](icons/INDEX.tsv) | The 65 icon ligatures seen, by role, place, size and the font that drew them |
| [screenshots/](screenshots) | 60 full-page renders: every copy in dark and light, `{page}-{theme}-{state}.png`, 1440 x 900 and 390 x 844 at 2x |
| [components/crops/](components/crops) | 302 crops, one per component, state and theme |
| [raw/](raw) | The readings: [css-vars.json](raw/css-vars.json) (848 variables in both themes), [css-facts.json](raw/css-facts.json), [components-computed.json](raw/components-computed.json), [measurements.md](raw/measurements.md), [brand.json](raw/brand.json) |
| [tools/](tools) | The capture scripts (`tools/capture/`) and the builders |

## How the values were read

The signed-in pages were copied in the built-in browser with [snapshot.js](tools/capture/signed-in/snapshot.js): the DOM with every same-origin stylesheet inlined, scripts removed, the account photo replaced by a grey disc, and every notebook, source, output and chat text replaced by "Sample ..." before the copy left the browser. [unsnap.py](tools/capture/signed-in/unsnap.py) then applied the account's literal names and ids from a redaction file kept outside the repository, and refused any copy where one survived. 30 copies were taken, all in dark; the light theme is the same copy with `body.dark-theme` swapped for `light-theme`, which is what the in-app Light mode does (the product's own variables are `light-dark()` pairs and Material's are scoped to `.dark-theme`).

Everything else ran headless on the copies, with fonts served from a local cache and nothing requested from notebook.google.com:

- [read-css.mjs](tools/capture/read-css.mjs) resolved every `--nlm-*`, `--nb-*` and `--mat-sys-*` variable on `<body>` in both themes (colours through a probe element), and listed media queries, reduced-motion rules, transitions, z-index, grid columns at four widths and colour usage counts.
- [measure.mjs](tools/capture/signed-in/measure.mjs) found 64 components by role and class and read their computed styles in 336 states: hover with the real pointer, focus-visible with real keyboard focus, pressed with the mouse held down, and selected, open, typed, error and disabled from copies captured in those states. Each state was cropped.
- [build_tokens.py](tools/build_tokens.py) maps the readings into tokens. Labels: **Measured** is a declared variable or a computed style; **Derived** is worked out from measured values (the accent hover and pressed colours composite the measured state layer at its measured opacity; the assembled ramps order measured values by CIELAB L*). Nothing is sampled from a screenshot.

The brand evidence (`<meta name="theme-color">` is black in light, white in dark; the manifest names the app "Gemini Notebook") is in [raw/brand.json](raw/brand.json).

## What to distrust

- **Two UI generations live in the CSS.** The legacy `--nlm-*` palette (lavender page `#edeffa`, blue `#4259ff`) is still declared and still paints a few things: the dialog Save button, links, the checked toggle chip, the lavender focus ring. Everything else is the newer `--nb-sys-*` set. Tokens named `legacy-*` are declared but no longer painted.
- **`--nlm-green-0` to `-40` and `-90` to `-99` are declared as `undefined`.** Only five green steps exist. The `neutral` (18 steps), `sky` (6), `red` (9), `green-status` (10), `amber` (7) and `info` (4) palettes are assembled from every value the product declares for that hue; the product itself declares no such ramps, and no further steps exist to read. The Studio and data-viz hues have one colour and one container each, so they have no ramp.
- **The scrim** is 32% black in both themes as painted, although `--nlm-fills-scrim` still says 60% in dark.
- **Success, warning and info** colours are the declared variables; no such message appeared, so their use as fill, text and border is the product's naming, not an observed screen. Danger was observed (the "Blocked by browser" chip and the URL field error).
- **Studio outputs** (audio and video players, mind map, flashcards, quiz, reports) were not opened; they render in other views and iframes. Their tile colours (`studio.*`, `tile.*`) are declared variables.
- **The list-view table header** read "Sample notebook 1" in its copy because the title-column scrub caught the header cell too; that one cell was set back to "Title" (the live wording) by hand before rendering.
- **The tooltip's text** is scrubbed in every image, since tooltips repeat titles. The measured one read "Audio Overview - Generate an AI podcast based on your sources".
- **Hover is not measured at 390**, and the 390 copies are measured at rest only.
- **The switch** is the only one in the product and is disabled (the browser blocks notifications), so no enabled or on state was seen.

## Colors

The luminous UI is nearly monochrome. Dark: page `#0f0f0f` (`bg.page`), cards and selected pills `#171717` (`surface.card`, `surface.selected`), panels, menus and dialog bodies `#1f1f1f` (`surface.panel`, `surface.overlay`, `surface.raised`), text `#e6e6e6` and 55% white (`text.primary`, `text.secondary`). Light: `#faf9f9`, `#f2f0f0`, `#ffffff`, black and 55% black. The one accent fill is the sky/navy pair on New notebook (`accent.default`: `#9dd2ff` light, `#1f3b9b` dark); dialog confirms and links still use the older brand blue `#4259ff` (`accent.brand`, `text.link`) in both themes. Borders are translucent on-surface (`border.default`: 8% black, 12% white). Colour otherwise comes from content: red PDF icons and one accent per Studio output type (`studio.*`).

## Fonts

| Role | Family | Licence | Stack (the product's own) |
|---|---|---|---|
| Everything | Google Sans Flex, variable (wght, wdth, opsz, ROND) | SIL OFL 1.1 (google/fonts `ofl/googlesansflex`) | "Google Sans Flex", "Google Sans", "Roboto", sans-serif |
| Material text roles | Google Sans Flex, then Google Sans Text | Google Sans: OFL (`ofl/googlesans`); Google Sans Text: not published, falls back | Google Sans Flex, Google Sans Text, Google Sans, sans-serif |
| Code, extended caption | Google Sans Code | SIL OFL 1.1 (`ofl/googlesanscode`) | "Google Sans Code", then the code stack in `core.fontFamily.code` |
| Icons | Luminous Symbols | Not published; licence unknown | "Luminous Symbols", "Google Symbols", "Material Symbols Outlined" (Apache 2.0, google/material-design-icons) |
| Maths | KaTeX | MIT | KaTeX_Main, serif |

Licences were read from the google/fonts and google/material-design-icons repositories on 2026-10-17. The type scale is the product's `--nb-sys-typography-*`: sizes 13, 15, 17, 20, 22, 24, 28, 32, 36, 42px, weights from 280 (display) to 540 (emphasised body), and per-role width and optical-size axes (`$extensions.fontVariationSettings`). Labels are 15px at weight 370.

## Layout and geometry

Spacing is `--nb-sys-spacing`: 2, 4, 8, 12, 16, 20, 24, 28px (`spacing.*`), plus container paddings of 16, 24 and 32. Radii are the `--nb-sys-shape` scale (4 to 56px and full), and the product leans on large ones: pills for every button (`radius.button`), 40px cards, 32px panels and composer, 28px dialogs, 20px menus. Controls are 36px (header, small) or 48px (dialog actions); dialog buttons from Material are 40px. Breakpoints: the product's most used is `599.98px` (15 rules), then 600-959.98 and 1024; the notebook grid is `repeat(auto-fill, minmax(var(--project-card-min-width), 1fr))`, five columns at 1440, three at 1024, two at 800. Every overlay (dialog, menu, select, tooltip, toast) mounts in one container at z-index 1000; the Google bar sits at 999 and card actions at 10.

Elevation is three tied levels plus none: cards, panels and dialogs have no shadow (`shadow.none`); menus, the composer and the Studio banner share `shadow.level1` (a 20px blur at 28% black in dark, 4% in light); the select panel and the toast use Material's level 3 (`shadow.select`, `shadow.toast`). Focus is a 3px outline in `border.focus` 2px outside each pill (`focusRing.*`); Material controls (checkbox, toggle chips, menu items) draw a 3px ring in `border.focus-strong` instead, and outlined fields thicken their outline to 2px. Motion is Material's: 150-500ms with the standard curve `cubic-bezier(0.4, 0, 0.2, 1)` most common (34 declarations); under reduced motion the backdrop fade drops to 1ms and the segmented slider, search field and card entrance stop animating (`core.reducedMotion`).

## Components

The 19 checklist components are all present; [components.md](components.md) has each one's states as tokens. The product's own nb-buttons come in accent (filled sky), tonal (grey fill), text and outlined variants, all pills. Hover and press add a state layer of the label colour at 8% and 12% (`opacity.hover`, `opacity.pressed`), never a colour change. Radio groups are drawn as toggle chips (Configure Chat); select is Material's outlined select; tabs are pills in the header and a segmented bar at 390.

## Icons

Icons are ligatures in Luminous Symbols at 20px in controls and 24px in rows (`size.icon-*`), outlined (FILL 0). [icons/INDEX.tsv](icons/INDEX.tsv) lists the 65 seen with the control each labels; 28 of them are drawn by the Google Symbols fallback because Luminous Symbols lacks them. Material Symbols Outlined, the last font in the product's stack, is the public stand-in.

## Coverage

Graded against [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md). Captured on 2026-10-17, dark and light, 1440 and 390.

| Item | Status | Where |
|---|---|---|
| Colour ramps | Captured: grey and blue declared; neutral, sky, red, green-status, amber, info assembled from declared values; green only 5 declared steps | `core.palette.*` |
| Colour roles, dark and light | Captured | `dark.*`, `light.*` (144 keys each) |
| Status colours | Captured: danger observed; success, warning, info declared, not seen on screen | `status.*` |
| Type roles and fallbacks | Captured | `core.typography`, `core.fontFamily` |
| Spacing | Captured | `core.spacing` |
| Radii, border widths | Captured | `core.radius`, `core.borderWidth` |
| Elevation | Captured | `shadow.*`, `core.shadow` |
| Motion and reduced motion | Captured | `core.duration`, `core.easing`, `core.reducedMotion` |
| Sizing and focus ring | Captured | `core.size`, `core.focusRing` |
| Layout: breakpoints, widths, grid, z-index | Captured | `core.breakpoint`, `core.layout`, `core.zIndex` |
| Button | Captured: default, hover, focus-visible, pressed, disabled; loading not present | [button-accent](components.md#button-accent) and five more |
| Icon button | Captured: default, hover, focus-visible, pressed | [icon-button](components.md#icon-button) |
| Link | Captured: default, hover, focus-visible | [link](components.md#link) |
| Text field | Captured: default, hover, focus-visible, typed | [text-field](components.md#text-field), [search-field](components.md#search-field) |
| Text area | Captured: default, hover, focus-visible, typed, error | [text-area](components.md#text-area), [text-area-outlined](components.md#text-area-outlined) |
| Select | Captured: default, hover, focus-visible, open, option hover, selected option | [select](components.md#select) |
| Checkbox | Captured: checked, hover, focus-visible; unchecked not seen (every source was selected) | [checkbox](components.md#checkbox) |
| Radio | Captured as toggle chips: default, hover, focus-visible, pressed, selected | [radio](components.md#radio) |
| Switch | Captured: off and disabled, hover; on not reachable | [switch](components.md#switch) |
| Tabs | Captured: default, hover, focus-visible, pressed, selected; 390 tab bar | [tab](components.md#tab), [segmented](components.md#segmented), [mobile-tab](components.md#mobile-tab) |
| Menu | Captured: open, item hover, focus-visible, pressed; submenu | [menu](components.md#menu) |
| Tooltip | Captured | [tooltip](components.md#tooltip) |
| Dialog | Captured: small, large, announcement, scrim | [dialog](components.md#dialog) |
| Toast | Captured | [toast](components.md#toast) |
| Card | Captured: default, hover, focus-visible, pressed | [card](components.md#card), [studio-tile](components.md#studio-tile) |
| List row | Captured: default, hover, focus-visible, pressed | [list-row](components.md#list-row) |
| Table | Captured: row hover, header; 390 rows | [table-row](components.md#table-row) |
| Avatar | Captured size and shape; photo replaced for privacy | [avatar](components.md#avatar) |
| Badge | Captured | [badge-pro](components.md#badge-pro), [status-chip](components.md#status-chip) |
| App shell and navigation | Captured | [patterns.md](patterns.md#app-shell-and-navigation) |
| Form with a validation error | Captured (error on blur, no submit) | [patterns.md](patterns.md#forms-and-validation) |
| Empty, loading, error states | Captured: empty and loading; error as a toast; no page-level error | [patterns.md](patterns.md#empty-loading-and-error-states) |
| Destructive confirmation | Captured (opened and cancelled) | [patterns.md](patterns.md#destructive-confirmation) |
| Feedback after an action | Captured | [patterns.md](patterns.md#feedback-after-an-action) |
| Search and filtering | Captured | [patterns.md](patterns.md#search-and-filtering) |
| List or table | Captured | [patterns.md](patterns.md#data-display) |
| Onboarding | Announcement captured; first-run onboarding not reachable (the account is past it) | [patterns.md](patterns.md#onboarding-and-announcements) |
| Light and dark | Captured | every copy rendered in both |
| Desktop and phone widths | Captured | 1440 everywhere; 390 for home and the notebook (chat and Studio tabs) |
| Icons | Captured: 65 ligatures by role | [icons/INDEX.tsv](icons/INDEX.tsv) |

Totals over 40 rows: 40 captured, of which 7 name a state or variant that was not reachable (loading button, unchecked checkbox, switch on, page-level error, first-run onboarding, success/warning/info on screen, green ramp steps). None not present, none not captured.

## Do and don't

1. **Do separate regions by fill, not shadow.** Cards (`surface.card`), panels (`surface.panel`) and dialogs sit on `bg.page` with no border and no shadow; only floating things (menus, the composer, the Studio banner) cast `shadow.level1`. See [home-dark](screenshots/home-dark.png) and [notebook-dark](screenshots/notebook-dark.png).
2. **Do keep one accent-filled button per screen.** On home only New notebook is filled (`accent.default`); tabs, Add sources and Create notebook are grey tonal or text pills. Dialog confirms are the one exception and use the older brand blue. See [home-light](screenshots/home-light.png) and [notebook-dark-configure-chat](screenshots/notebook-dark-configure-chat.png).
3. **Do show selection with a quiet grey fill.** The selected header tab and the active 390 tab use `surface.selected`, not the accent; only Configure Chat's toggle chips fill blue with a leading check. See [tab-selected](components/crops/tab-selected.png) and [radio-selected](components/crops/radio-selected.png).
4. **Don't colour destructive actions red.** Delete in the confirmation is the same grey tonal pill as any other action, beside a text Cancel, and it takes focus. See [home-dark-delete-confirm](screenshots/home-dark-delete-confirm.png).
5. **Do draw keyboard focus as a thick outline around the whole pill.** A 3px `border.focus` outline 2px outside the control, following its radius; fields thicken their own outline instead. See [button-accent-focus-visible](components/crops/button-accent-focus-visible.png) and [text-area-outlined-focus-visible](components/crops/text-area-outlined-focus-visible.png).
6. **Don't put colour in the chrome.** Header, panel and menu icons are `text.primary`; colour is kept for content type: red PDF icons on sources and one accent per Studio output type. See [notebook-dark](screenshots/notebook-dark.png) and [mobile-notebook-dark-studio](screenshots/mobile-notebook-dark-studio.png).

## Rebuild

```bash
python3 tools/build_tokens.py && python3 tools/build_components_md.py && python3 tools/build_style_guide.py
```

From new readings (needs Playwright and the page copies in `~/.design-systems/snaps/notebooklm`, which hold the account's content and stay outside the repository):

```bash
export PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs SNAPS=~/.design-systems/snaps/notebooklm
tools/capture/signed-in/render-all.sh && python3 tools/capture/quantize.py "$SNAPS/renders"
node tools/capture/read-css.mjs && node tools/capture/signed-in/measure.mjs && node tools/capture/signed-in/build-measurements.mjs && node tools/capture/icons.mjs
```

`measure.mjs` and `quantize.py` need Pillow. Edit `raw/` only through these scripts and the builders, never the generated files.
