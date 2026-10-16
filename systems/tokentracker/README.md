# TokenTracker design reference

A token set, component and pattern reference for TokenTracker's dashboard: a quiet, dense, neutral usage dashboard with one green accent, a borderless sidebar and a rounded content panel. It was read on 2026-10-17 from TokenTracker v1.4.3, the dashboard its CLI serves on the local machine (`http://127.0.0.1:7680`), with no account signed in, in headless Chromium at 1440 x 900 and 390 x 844, both at 2x, in dark (its default) and light. Pages: Tokens (the dashboard), Sessions, Limits, Skills, Settings, Menu Bar & Widgets, Achievements, Pet, Service Status and the signed-out Cloud page, plus the first-run Tokens page from a second, empty install. It refreshes the 2026-10-11 capture of v1.3.5; every reading, screenshot and crop was taken again from v1.4.3.

It is the reference for Quiver's macOS app, which takes TokenTracker's look and most of its features (see "Using it in Quiver").

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (261: neutral, brand, red, amber, orange, sky and blue ramps, status and heatmap colours, the font stacks, a 9-step size scale (`font.scale`, every size at least 10 rendered elements use), 17 named type roles plus 9 more type styles counted from the rendered text, a 2px-step spacing scale, radii, border width, sizes, the focus ring, shadows for each use, z-index layers, breakpoints, content widths, durations, easings) and `light` and `dark` (63 each: wash, panel, card, raised, overlay and scrim fills, text roles including disabled and link, borders including focus, the focus ring colour, accent default/hover/pressed, primary, danger and disabled buttons, switch tracks, status and heatmap aliases), plus `$themes`. Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | One self-contained page that rebuilds the shell, controls, lists and tables from the tokens, with a light and dark toggle, and lists every colour role, ramp, type role, radius, size and duration with its source. Open it from disk. |
| [components.md](components.md) | The pages captured, the shared values (hover, focus, pressed, disabled, motion, radii), one entry per component with dark and light state tables written in token names, crops, the icon index and the Gaps. |
| [patterns.md](patterns.md) | The app shell, page header, forms and validation, empty/loading/error states, destructive confirmation, feedback, search and filtering, data display and first run, each with its components, layout and screenshots. |
| [components/crops/](components/crops) | Element screenshots, `{component}[.light]-{state}.png`, at 2x. |
| [icons/](icons) | Lucide icons as SVG, named by their Lucide class, with [icons/INDEX.tsv](icons/INDEX.tsv). |
| [screenshots/](screenshots) | 80 `{page}-{theme}-{state}.png` captures: 1440 x 900 at 2x, `-full` for whole pages, `mobile-*` at 390 x 844, `onboarding-*` from the empty install, `sessions-loading-*` and `sessions-error-*` for those states. |
| [raw/](raw) | The readings: every custom property in the CSS bundle, resolved in both themes (`css-vars.json`); computed styles per component, state and theme (`components-computed.json`, and `measurements.md` built from it); every rendered value counted per page and theme, plus the stylesheet's breakpoints, reduced-motion rules and colour utilities (`census.json`). |
| [tools/](tools) | The three builders and the capture scripts. See Rebuild. |

## How the values were read

The dashboard is React with Tailwind v3 and ships one same-origin CSS bundle. [vars.mjs](tools/capture/vars.mjs) parses that bundle and resolves every custom property with `<html>` and `<html class="dark">`, which is how TokenTracker switches theme. That gives the brand ramp (`--brand-50` to `--brand-950`, emerald), the status colours and the font stacks.

The rendered neutrals do not come from custom properties. Components use Tailwind classes such as `bg-oai-gray-900`, and `tailwind.config.cjs` maps those to plain hex (Tailwind's neutral: `#fafafa` to `#0a0a0a`). So every surface, text and border token is the computed style of a real element, read per state and theme by [measure.mjs](tools/capture/public/measure.mjs). Hover used the pointer, focus-visible a real keyboard Tab, pressed was forced through DevTools, a field was typed into and cleared.

[census.mjs](tools/capture/public/census.mjs) walks every visible element on ten pages in both themes and counts each colour, shadow, z-index, padding, gap, radius and font size, with where it appears. The spacing scale, the status colours and the z-index layers come from those counts, so a value seen once does not become a token. It also reads the stylesheet's media queries (breakpoints, reduced motion) and the Tailwind colour utilities the bundle ships, which give the red, amber, orange, sky and blue ramps their steps.

Look, don't act. Every capture browser aborts any request that is not a read (GET, HEAD, OPTIONS), so no click could save, sync, remove or send anything. The only interactions: period and table tabs, the sidebar chevron, filter selects (closed with Escape), the mobile menu, page sub-navigation, a search typed and cleared, Share then Copy image (drawn and copied inside the headless browser, which has no clipboard, so it reports a failure), one Skills row ticked then its Remove confirmation opened and cancelled with Escape, and the Network proxy switched to Manual in the page, an invalid host typed and checked with Test connection, then cleared and switched back without saving. The loading and error states are Sessions with its request held back or aborted in the capture browser. The first run is a second TokenTracker started with an empty home folder on port 7681.

The dashboard shows the owner's real usage. Before every screenshot, crop and reading, [lib.mjs](tools/capture/public/lib.mjs) replaces home-directory paths, session and project titles and installed skill names in the page, using a redaction file kept outside the repository. Usage figures, model names and plan names are left as they were. Leaderboard (other people's handles and avatars) and Claude IP Check (the machine's IP address and location) were not captured.

Screenshots are 256-colour PNGs. Flat UI colours survive exactly; read values from the tokens, not the images.

## What to distrust

- **The green-tinted greys.** TokenTracker's own `DESIGN.md` and `styles.css` describe a green-tinted neutral ramp (`--oai-gray-*`, oklch hue 145). The components do not render it; they render plain Tailwind neutral hex. The tinted ramp is kept under `core.$extensions.notTokenised` and is not the look.
- **The source on disk is older than the app.** The running dashboard is v1.4.3; the TokenTracker checkout on this machine is 1.2.2. Where the two differ, the live readings win. Values from the source only are marked Derived: the 72px collapsed sidebar, the content widths and the 12-column Tokens grid.
- **Focus is mostly absent.** `styles.css` removes outlines and Tailwind rings on every element. Only the sidebar's theme toggle, star pill and collapse chevron, and the Cloud page's controls, draw a ring (2px solid in the ink colour, 2px out). Light text fields turn their border emerald on focus; dark ones do not change. Every other `focus-visible` reading equals its default.
- **Status colours are thin.** Success renders as emerald text, danger as the red toast and the danger button. Warning renders only as one amber notice on Limits in light, so it has no themed token. No info colour renders anywhere. The status triples (fill, text, border) are not complete.
- **The toast is the failure toast.** Copy image cannot reach a clipboard headless, so the product showed "Couldn't generate image" in red. The success toast was not reached.
- **Light secondary text is just under AA on the wash.** `text.secondary` (`#737373`) is 4.34:1 on `bg.wash` (`#f5f5f5`) and passes on the panel and cards. That is the product's value.
- **Provider colours** (Claude orange, Codex blue, OpenCode purple) come from a JavaScript map, not CSS. They are not tokenised; the style guide's share bar uses illustrative values.

## Fonts

| Family | Used for |
|---|---|
| System UI (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, …`) | Everything. On macOS this is SF Pro. Numbers use `tabular-nums`. |
| SF Mono, then `ui-monospace`, Menlo | Code blocks and terminal copy on Limits. |

No font file is needed. The bundle also declares Geist Mono faces, but no rendered element uses them.

## Icons

Lucide, through `lucide-react` (declared as `^1.48.0` in the TokenTracker source's `dashboard/package.json`), licensed ISC according to the npm registry (`npm view lucide-react license`, read 2026-10-17). Stroke 2, drawn in `currentColor`, 15px in the sidebar and 14 to 16px in controls. [icons/INDEX.tsv](icons/INDEX.tsv) lists each icon by name with its sizes, the pages it was seen on and its place (nav link, button, field). Provider logos, the pet and the menu bar art are brand material and were not collected ([RIGHTS.md](../../docs/RIGHTS.md)). The fonts are the operating system's own (SF Pro and SF Mono on macOS), so no font file or licence is needed; the fallback stacks are in `font.family.*`.

## Layout

| Region | Value |
|---|---|
| Sidebar | 220px (72px collapsed), no fill or border, on the page wash; 8px side padding; items 32px tall |
| Content panel | Starts at the sidebar's edge, 8px from the top and 12px from the right and bottom; 16px radius, 1px border, `0 1px 2px` at 5% |
| Page header | 36/40 semibold title at -0.9px tracking, 16/24 secondary subtitle, actions as 36px icon buttons top right |
| Tokens page | A 12-column grid: a 4-column stack of cards on the left, an 8-column overview and table on the right, 16px gaps (`layout.columns`, read from the source, matches the screenshots) |
| Breakpoints | `breakpoint.sm` 640, `md` 768, `lg` 1024, `xl` 1280, `2xl` 1536, read from the stylesheet's media queries; the sidebar shows from `lg` and becomes a drawer below it |
| Other pages | `layout.contentWidth.page` (1152px) centred in the panel; Settings `layout.contentWidth.settings` (1024px) with a 176px sub-nav |
| Spacing | `space.scale.*`: 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 36, 40, 64px, on Tailwind's 4px base with 2px half steps; 12, 8, 6, 4 and 2 carry most of the interface |
| Layers | `zIndex.sticky` 10 (table and page headers), `tooltip` 20, `scrim` 100, `dialog` 101, `shareSheet` 9999 |

## Motion and reduced motion

Colour changes on hover run 150ms (`motion.duration.fast`: nav, tabs, selects) or 200ms (`base`: buttons, tiles, fields) on `motion.easing.standard`. Dialogs ease in over 260ms on `motion.easing.emphasized`. Under `prefers-reduced-motion: reduce` the fade and modal keyframe animations stop, the Cloud page's action popup and backdrop drop their transitions and entry transform, and the plan cards' hover glow stops; spinners and the sidebar's width and position transitions only run under `no-preference`. Hover colour transitions do not change. The rules are listed in `core.$extensions.notTokenised.reducedMotion`.

## Do and don't

1. **Do let the surfaces carry the structure.** Wash, panel and card differ by one neutral step plus a hairline; the only resting shadow is `0 1px 2px` at 5%. See [dashboard-dark-default](screenshots/dashboard-dark-default.png) and [settings-light-default](screenshots/settings-light-default.png).
2. **Do keep green for money and "on".** Cost figures, the usage fill, switch tracks and the heatmap are green. The primary button is black in light and near-white in dark, never green; red is kept for the destructive confirm and failures. See [dashboard-light-default](screenshots/dashboard-light-default.png) and [skills-light-confirm](screenshots/skills-light-confirm.png).
3. **Do keep controls small and quiet.** Tabs, segments and buttons are 12/16 medium on 28 to 32px, 8px radius; hover changes colour only. See [settings-dark-segment-hover](screenshots/settings-dark-segment-hover.png).
4. **Don't copy the uppercase labels.** The older cards ("ACTIVITY HEATMAP", "USAGE TREND"), the hero label, sidebar group labels and Settings card titles use small tracked uppercase. TokenTracker's newer cards title themselves in sentence case at 14/500 primary. Use sentence case everywhere. See [dashboard-dark-full](screenshots/dashboard-dark-full.png).
5. **Don't copy the missing focus ring.** Most controls draw none. Give every control the ring the theme toggle already draws: 2px solid in the ink colour, 2px out (`focusRing.*`, `focus.ring`). See [theme-toggle-focus-visible](components/crops/theme-toggle-focus-visible.png).

## Patterns

[patterns.md](patterns.md) describes how the components combine: the app shell, page header, forms and validation, empty/loading/error states, destructive confirmation, feedback after an action, search and filtering, data display, and first run.

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
| Colour ramps | Captured | `core.color.neutral`, `brand`, `red`, `amber`, `orange`, `sky`, `blue` (the steps the stylesheet ships); thinner hues listed under `notTokenised.otherHues` |
| Background roles | Captured | `bg.wash` (page), `bg.panel` and `bg.card` (surface), `bg.raised` (menus), `bg.overlay` (dialogs), `bg.scrim` |
| Text roles | Captured | `text.primary`, `secondary`, `disabled`, `onPrimary`, `link`, `linkHover` |
| Border roles | Captured | `border.default`, `strong`, `hover`, `focus` (light changes on focus; dark does not) |
| Accent states | Captured | `accent.default`, `hover`, `pressed` (pressed equals hover); `button.primary.*` |
| Status colours | Partly captured | Success text and danger fill and text; warning renders only once in light, info never. See What to distrust |
| Type roles | Captured | `core.font.scale` (10, 11, 12, 13, 14, 16, 18, 36, 72px); `core.typography`: 17 named roles (display, headings, body, label, caption, code in the mono stack) and 9 styles counted from rendered text |
| Spacing | Captured | `core.space.scale` (counted from every rendered padding and gap) |
| Radii, borders | Captured | `core.radius`, `core.border` |
| Elevation | Captured | `core.shadow`: `ring` (1px, pills and marks), `sm` panel, `md` toast, `lg` menu, `lgBare` hint tooltip, `xl` heatmap tooltip, `dialog` and `confirm` per theme |
| Motion and reduced motion | Captured | `core.motion`; Motion and reduced motion above |
| Sizing (controls, icons) | Captured | `core.size` |
| Focus ring | Captured where it exists | `core.focusRing`, `focus.ring`: four sidebar and Cloud controls; the rest of the product draws none |
| Layout (widths, breakpoints, columns, layers) | Captured | `core.breakpoint` and `core.zIndex` measured; `core.layout` Derived from the source |
| Button | Captured | `primary-button`, `share-button`, `danger-button`, `cancel-button`, `retry-button`, `button-disabled` |
| Icon button | Captured | `icon-button`, `sidebar-toggle`, `theme-toggle` |
| Link | Captured | `link`, `footer-link`, `cost-button` |
| Text field | Captured | `search-input`, `text-field` (default, hover, focused, error), `field-error` |
| Text area | Not present | No page in v1.4.3 renders one |
| Select | Captured | `select`, `select-menu`, `select-option`, `select-disabled` |
| Checkbox | Captured | `checkbox` (default, hover, focus-visible, checked) on Skills |
| Radio | Not present | No page in v1.4.3 renders one |
| Switch | Captured, disabled only | `switch-on`, `switch-off`: every switch reached is disabled until the Mac app is connected |
| Tabs | Captured | `period-tab`, `table-tab`, `segment` |
| Menu | Captured | `select-menu` |
| Tooltip | Captured | `tooltip` (heatmap), `hint-tooltip` (Limits pill) |
| Dialog | Captured | `dialog` (cost breakdown), `share-dialog`, `confirm-dialog`, with their scrims |
| Toast | Captured, failure only | `toast` ("Couldn't generate image") |
| Card | Captured | `card`, `provider-tile`, `stat-chip`, `status-row`, `settings-card` |
| List row | Captured | `list-row`, `list-row-title` |
| Table | Captured | `table-header`, `table-cell`, `table-row` |
| Avatar | Not captured | Signed out: `account-control` shows the app mark and "Sign in" where an avatar would be. Leaderboard avatars are other people's |
| Badge | Captured | `badge`, `status-badge` |
| App shell and navigation | Captured | [patterns.md](patterns.md); collapsed and mobile shots |
| Form with a validation error | Captured | `settings-*-network-error`; [patterns.md](patterns.md) |
| Empty, loading, error states | Captured | `sessions-*-empty`, `sessions-loading-*`, `sessions-error-*` |
| Destructive confirmation | Captured | `skills-*-confirm` (cancelled) |
| Feedback after an action | Captured | `dashboard-*-toast` |
| Search and filtering | Captured | Sessions filters, search, selects |
| List or table | Captured | Sessions list, Daily Breakdown |
| Onboarding | Captured | `onboarding-*` from an empty install |
| Light and dark | Captured | Every page and component |
| Desktop and phone widths | Captured | 1440 for all pages; 390 for Tokens, Sessions, Limits, Settings |
| Signed-in pages | Not captured | Cloud (signed in), Leaderboard, Settings > Account need an account |

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

The builders are deterministic: re-running them reproduces their files byte for byte. Edit the raw inputs or the builders, never the generated files. `build_components_md.py` reads `tokens.json`, so run it last.

To capture again, start TokenTracker's dashboard with `npx tokentracker-cli serve --no-open --no-sync`. Its first run installs hooks into Claude Code, Codex and OpenCode on the machine; remove them afterwards if they were not wanted. For the first-run screens, start a second one with an empty home folder: `HOME=<empty dir> npx tokentracker-cli serve --port 7681 --no-open --no-sync`. Put the redaction file at `~/.design-systems/tokentracker-redact.json` (shaped like the kit's `redact.example.json`). The crops are quantized by `python3` with Pillow, so put an environment that has it first on `PATH`. Then:

```bash
export PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs
```

```bash
RAW=~/.design-systems/tokentracker/raw-shots node tools/capture/public/public.mjs && python3 tools/capture/quantize.py ~/.design-systems/tokentracker/raw-shots
```

```bash
node tools/capture/public/census.mjs && node tools/capture/public/measure.mjs && node tools/capture/public/build-measurements.mjs && node tools/capture/icons.mjs
```

`vars.mjs` reads a copy of the CSS bundle: fetch `/assets/*.css` from the running dashboard with curl, wrap it in `<style>` in `SNAPS/bundle.html`, then run `SNAPS=… node tools/capture/vars.mjs`.
