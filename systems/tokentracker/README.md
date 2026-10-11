# TokenTracker design reference

A token set and component reference for TokenTracker's dashboard: a quiet, dense, neutral usage dashboard with one green accent, a borderless sidebar and a rounded content panel. It was read on 2026-10-11 from TokenTracker v1.3.5, the dashboard its CLI serves on the local machine (`http://127.0.0.1:7680`), with no account signed in, in headless Chromium at 1440 x 900 and 390 x 844, both at 2x, in dark (its default) and light. Pages: Tokens (the dashboard), Sessions, Limits, Skills, Settings, Menu Bar & Widgets, Achievements, Pet and Service Status.

It is the reference for Quiver's macOS app, which takes TokenTracker's look and most of its features (see "Using it in Quiver").

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (161: the neutral and brand ramps, status and heatmap colours, the system font stacks, 16 composite type roles with their text transform, radii, border width, sizes, paddings, shadows, durations, easings) and `light` and `dark` (41 each: wash, panel, card, field, hover and selected fills, text roles, borders, accent, buttons, usage track, status and heatmap aliases), plus `$themes`. Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | One self-contained page that rebuilds the shell, controls, lists and tables from the tokens, with a light and dark toggle, and lists every colour role, ramp, type role, radius, size and duration with its source. Open it from disk. |
| [components.md](components.md) | The pages captured, the shared values (hover, focus, pressed, motion, radii), one entry per component (65) with dark and light state tables and crops, the icon index and the Gaps. |
| [components/crops/](components/crops) | 204 element screenshots, `{component}[.light]-{state}.png`, at 2x. |
| [icons/](icons) | 37 Lucide icons as SVG, named by their Lucide class, with [icons/INDEX.tsv](icons/INDEX.tsv). |
| [screenshots/](screenshots) | 58 `{page}-{theme}-{state}.png` captures: 1440 x 900 at 2x, `-full` for whole pages, `mobile-*` at 390 x 844. |
| [raw/](raw) | The readings: every custom property in the CSS bundle, resolved in both themes (`css-vars.json`); computed styles per component, state and theme (`components-computed.json`, and `measurements.md` built from it). |
| [tools/](tools) | The three builders and the capture scripts. See Rebuild. |

## How the values were read

The dashboard is React with Tailwind v3 and ships one same-origin CSS bundle. [vars.mjs](tools/capture/vars.mjs) parses that bundle and resolves every custom property with `<html>` and `<html class="dark">`, which is how TokenTracker switches theme. That gives the brand ramp (`--brand-50` to `--brand-950`, emerald), the status colours and the font stacks.

The rendered neutrals do not come from custom properties. Components use Tailwind classes such as `bg-oai-gray-900`, and `tailwind.config.cjs` maps those to plain hex (Tailwind's neutral: `#fafafa` to `#0a0a0a`). So every surface, text and border token is the computed style of a real element, read per state and theme by [measure.mjs](tools/capture/public/measure.mjs). Hover used the pointer, focus-visible a real keyboard Tab, pressed was forced through DevTools, a field was typed into and cleared, and the only clicks were tabs, a filter select (closed with Escape), the cost button that opens the breakdown dialog, the sidebar collapse chevron and the mobile menu. Nothing was saved, copied, installed, signed into or sent.

The dashboard shows the owner's real usage. Before every screenshot, crop and reading, [lib.mjs](tools/capture/public/lib.mjs) replaces home-directory paths, session and project titles and installed skill names in the page, using a redaction file kept outside the repository. Usage figures, model names and plan names are left as they were.

Screenshots are 256-colour PNGs. Flat UI colours survive exactly; read values from the tokens, not the images.

## What to distrust

- **The green-tinted greys.** TokenTracker's own `DESIGN.md` and `styles.css` describe a green-tinted neutral ramp (`--oai-gray-*`, oklch hue 145). The components do not render it; they render plain Tailwind neutral hex. The tinted ramp is kept under `core.$extensions.notTokenised` and is not the look.
- **The source on disk is older than the app.** The running dashboard is v1.3.5; the TokenTracker checkout on this machine is 1.2.2. Where the two differ, the live readings win. One value comes from the source only: the 72px collapsed sidebar width (`size.sidebar.collapsedWidth`, Derived).
- **Focus states.** TokenTracker removes every focus ring, so the focus-visible readings equal the defaults. That is a gap in the product, not a token.
- **Provider colours** (Claude orange, Codex blue, OpenCode purple) come from a JavaScript map, not CSS. They are not tokenised; the style guide's share bar uses illustrative values.
- **The status badge** (`STALE`, `RE-AUTH`) reading is its wrapper. Use the crops and screenshots for it.

## Fonts

| Family | Used for |
|---|---|
| System UI (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, …`) | Everything. On macOS this is SF Pro. Numbers use `tabular-nums`. |
| SF Mono, then `ui-monospace`, Menlo | Code blocks and terminal copy on Limits. |

No font file is needed. The bundle also declares Geist Mono faces, but no rendered element uses them.

## Layout

| Region | Value |
|---|---|
| Sidebar | 220px (72px collapsed), no fill or border, on the page wash; 8px side padding; items 32px tall |
| Content panel | Starts at the sidebar's edge, 8px from the top and 12px from the right and bottom; 16px radius, 1px border, `0 1px 2px` at 5% |
| Page header | 36/40 semibold title at -0.9px tracking, 16/24 secondary subtitle, actions as 36px icon buttons top right |
| Tokens page | A 12-column grid: a 4-column stack of cards on the left, an 8-column overview and table on the right, 16px gaps (read from the source, matches the screenshots) |
| Breakpoints | Tailwind's defaults, `sm` 640, `md` 768, `lg` 1024; the sidebar shows from `lg` and becomes a drawer below it (Derived from the source) |
| Other pages | `max-w-6xl` (1152px) centred in the panel; Settings `max-w-5xl` with a 176px sub-nav (widths from the source, the sub-nav measured) |

## Do and don't

1. **Do let the surfaces carry the structure.** Wash, panel and card differ by one neutral step plus a hairline; the only resting shadow is `0 1px 2px` at 5%. See [dashboard-dark-default](screenshots/dashboard-dark-default.png) and [settings-light-default](screenshots/settings-light-default.png).
2. **Do keep green for money and "on".** Cost figures, the usage fill and the heatmap are green. The primary button is black in light and near-white in dark, never green. See [dashboard-light-default](screenshots/dashboard-light-default.png) and [limits-dark-default](screenshots/limits-dark-default.png).
3. **Do keep controls small and quiet.** Tabs, segments and buttons are 12/16 medium on 28 to 32px, 8px radius; hover changes colour only. See [settings-dark-segment-hover](screenshots/settings-dark-segment-hover.png).
4. **Don't copy the uppercase labels.** The older cards ("ACTIVITY HEATMAP", "USAGE LIMITS"), the hero label, sidebar group labels and Settings card titles use small tracked uppercase. TokenTracker's newer cards title themselves in sentence case at 14/500 primary. Use sentence case everywhere. See [dashboard-dark-full](screenshots/dashboard-dark-full.png).
5. **Don't copy the missing focus ring.** Add a visible 2px accent ring.

## Using it in Quiver

Quiver's app is SwiftUI on macOS 26, so the tokens map to native equivalents rather than CSS:

| Token | SwiftUI |
|---|---|
| `font.family.sans` | The system font (`.system`), which is SF Pro |
| `typography.pageTitle` (36/40, 600, -0.9) | `.system(size: 36, weight: .semibold)`, `.tracking(-0.9)` |
| `typography.nav` (13/19.5) | `.system(size: 13)`; current item `.medium` |
| `typography.control` (12/16, 500) | `.system(size: 12, weight: .medium)` |
| `typography.display` (72/72, 700, -1.8) | `.system(size: 72, weight: .bold)`, `.monospacedDigit()`, `.tracking(-1.8)` |
| `radius.2xl` 16, `radius.xl` 12, `radius.lg` 8 | `.rect(cornerRadius:)` with the same points |
| `border.default` | `.strokeBorder(color, lineWidth: 1)` |
| Lucide icons, 15px nav | SF Symbols at 13 to 15pt, regular weight, as Quiver's sidebar already does |

The sidebar group labels and card titles should be sentence case (Do and don't, rule 4). The desktop widget designs (usage summary, activity heatmap, top models, usage limits) are on [widgets-dark-full](screenshots/widgets-dark-full.png), for Quiver's WidgetKit milestone.

## Coverage

Graded against [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md).

| Item | Status | Where |
|---|---|---|
| Colour roles, light and dark | Captured | `tokens.json` `light`, `dark` |
| Type roles | Captured | `core.typography` (16 roles) |
| Spacing | Captured | `core.space` (measured paddings) |
| Radii, borders | Captured | `core.radius`, `core.border` |
| Elevation | Captured | `core.shadow` |
| Motion | Captured | `core.motion` |
| Sizing (controls, icons) | Captured | `core.size` |
| Focus ring | Not present | The product removes focus rings |
| Layout (widths, breakpoints) | Captured widths; breakpoints Derived from the source | Layout table above |
| Button | Captured | `primary-button`, `share-button` in components.md |
| Icon button | Captured | `icon-button` |
| Link | Captured | `footer-link`, `cost-button` |
| Text field | Captured | `search-input` (default, focused, filled) |
| Text area | Not present | |
| Select | Captured | `select`, `select-menu`, `select-option` |
| Checkbox | Not captured | None found on the pages measured |
| Radio | Not present | |
| Switch | Observed | Green toggles on [widgets-dark-full](screenshots/widgets-dark-full.png); not measured |
| Tabs | Captured | `period-tab`, `table-tab` |
| Menu | Captured | `select-menu` |
| Tooltip | Not captured | Hover shows none on the elements tried |
| Dialog | Captured | `dialog` (cost breakdown) |
| Toast | Not captured | Needs an action that changes data |
| Card | Captured | `card`, `provider-tile`, `stat-chip`, `status-row` |
| List row | Captured | `list-row`, `list-row-title` |
| Table | Captured | `table-header`, `table-cell`, `table-row` |
| Avatar | Not captured | Signed-out; only the placeholder circle |
| Badge | Captured | `beta-badge`; `status-badge` from crops only |
| App shell and navigation | Captured | `sidebar`, `nav-item`, `content-panel`, collapsed and mobile shots |
| Form with a validation error | Not captured | No form was submitted |
| Empty, loading, error states | Observed | "Not connected" rows on Limits, "Checking…" on Service Status |
| Destructive confirmation | Not present | |
| Feedback after an action | Not captured | Needs an action that changes data |
| Search and filtering | Captured | Sessions filters, search, select |
| List or table | Captured | Sessions list, Daily Breakdown |
| Onboarding | Not captured | Signed-out first run not reproduced |
| Light and dark | Captured | Every page and component |
| Desktop and phone widths | Captured | 1440 for all pages; 390 for Tokens, Sessions, Limits, Settings |

## Rebuild

```bash
python3 tools/build_tokens.py
```

```bash
python3 tools/build_style_guide.py
```

```bash
python3 tools/build_components_md.py
```

The builders are deterministic: re-running them reproduces their files byte for byte. Edit the raw inputs or the builders, never the generated files.

To capture again, start TokenTracker's dashboard, put the redaction file at `~/.design-systems/tokentracker-redact.json` (shaped like the kit's `redact.example.json`), then:

```bash
export PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs
```

```bash
RAW=~/.design-systems/tokentracker/raw-shots node tools/capture/public/public.mjs && python3 tools/capture/quantize.py ~/.design-systems/tokentracker/raw-shots
```

```bash
node tools/capture/public/measure.mjs && node tools/capture/public/build-measurements.mjs && node tools/capture/icons.mjs
```

`vars.mjs` reads a copy of the CSS bundle: fetch `/assets/*.css` from the running dashboard with curl, wrap it in `<style>` in `SNAPS/bundle.html`, then run `SNAPS=… node tools/capture/vars.mjs`. `quantize.py` and the crops need Pillow.
