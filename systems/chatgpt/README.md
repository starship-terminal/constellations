# ChatGPT design reference

A token set and component reference for ChatGPT's web app (chatgpt.com): the shell and sidebar, the thread and composer, menus and dialogs, the Library, Images, Plugins, the settings pages and the Upgrade dialog. ChatGPT is the chat most people already know, so its sizes and states are the baseline any chat product gets compared with.

It was read on 2026-10-17 from the owner's signed-in account (Free plan), in the built-in browser pane of the Claude desktop app, captured dark with the Blue accent and rendered in both themes, at 1440 x 900 and 390 x 844. This is a refresh: between the first capture (2026-10-04) and this one ChatGPT shipped a redesigned shell. The theme now switches on `data-theme` on `<html>` (it was a `dark` class), the palette is a new semantic system (`--color-text-*`, `--color-background-*`, `--color-surface-*`, a variant matrix per colour), and components come from a CSS-module library (`Button-*`, `itemBase-*`, `Table-*`) with `data-color`, `data-variant` and `data-size` attributes. Every page was captured again and every value read again; nothing here comes from the first capture.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout. `core` (theme-independent): the fixed colour ramps, font families and weights, the type scale and 30 named type styles, spacing (the 4px unit and the 17 steps the pages use), radii, border widths, control and icon sizes, the focus ring, durations, easings (and what reduced motion changes), breakpoints, containers, layout widths and z-index layers. `light` and `dark`: the semantic palette (`bg`, `surface`, `text`, `border`, `ring`, `variant`, `status` by way of `role`, `chatAccent`, `scrim`), the theme-flipping grey ramp, shadows, `elevation` by use, `role` (the checklist's roles pointed at ChatGPT's names) and `component` (measured component values, aliased to a token wherever one holds the value). Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | One self-contained page that renders every token and the main components from the token file, in both themes. |
| [components.md](components.md) | The discovery list of every page and state captured, the checklist coverage, the shared values (hover, pressed, focus, disabled, motion, layout), one entry per component with crops and its values written in tokens, the icon index and the Gaps. |
| [components/crops/](components/crops) | 578 element screenshots, `{component}-{state}.png`, at 2x. |
| [icons/](icons) | 66 SVGs lifted from the sprite symbols inlined in the page copies, with [icons/INDEX.tsv](icons/INDEX.tsv) indexing each by role. OpenAI's icons, kept for reference only. |
| [screenshots/](screenshots) | 63 `{page}-{theme}-{state}.png` captures: desktop at 1440 x 900 and 2x, `-full` whole pages of the dark home, Library and Plugins, `mobile-*` at 390 x 844 and 2x. Every state exists in both themes. |
| [raw/](raw) | The unprocessed readings: every custom property the stylesheets declare and the value each root-level name computes to in both themes (`css-vars.json`, with the reduced-motion rules, z-index and grid declarations and the Tailwind utility counts), per-component computed styles (`components-computed.json`, and `measurements.md` built from it), and page geometry (`layout.json`). |
| [tools/](tools) | The three builders and the capture kit. See Rebuild. |

## How the values were read

The owner was already signed in to chatgpt.com in the browser pane; nothing was typed for them. Each page state (a menu open, a dialog, a tooltip, a typed composer, the phone drawer) was copied with [snapshot.js](tools/capture/signed-in/snapshot.js), which inlines every same-origin stylesheet from the CSSOM (chatgpt.com serves its CSS from its own origin, so all of it was readable), copies the icon sprite symbols into the page, and removes scripts. The same script scrubs private text before the copy leaves the browser: every chat, project and file title the page shows is collected and replaced everywhere in the copy (attributes included) by "Sample title N", message text and Library file names become same-length neutral words (numbers stay), links and images inside messages become example.com and a blank image, the account's name becomes "Learner" and its photo a grey disc, the ids on `<html>` and every chat, project, file and account id in a URL are cut, and URLs carrying a signing parameter lose their query. [unsnap.py](tools/capture/signed-in/unsnap.py) refused any copy in which a redacted string, a signing parameter or an id survived. The redaction file and the copies stay outside the repository.

Headless Chromium then read the copies offline. [vars.mjs](tools/capture/vars.mjs) parsed every stylesheet and read each root-level custom property on `<html>` in dark (as captured) and light (every `data-theme="dark"` set to light, which is all ChatGPT's own switch does), letting the browser resolve the `var()` chains, `color-mix()` and relative colours into one sRGB value per theme. [measure.mjs](tools/capture/signed-in/measure.mjs) read 114 components in 588 states: at rest, with a real pointer hover, with real keyboard focus (focus-visible), with the mouse button held down (pressed), and in the states the copies were captured in (selected, active, checked, open, typed, highlighted, disabled). [layout.mjs](tools/capture/layout.mjs) read page geometry and [icons.mjs](tools/capture/icons.mjs) the icon set.

Nothing was sent, created or deleted. The capture hovered, focused, opened menus and dialogs and closed them, and typed into the composer and two search fields without sending. The delete confirmation was opened with a guard in the page that refused any request that could delete, archive or rename, then closed with Escape. The same guard briefly refused the Library's file-list request, which is how its error state was captured; the guard was then narrowed and the list loaded.

Screenshots and crops are stored as 256-colour PNGs. Flat UI colours are exact; read values from the tokens, not the images.

### What to distrust

- Pressed: ChatGPT switches its pressed styles from script (a data attribute set on press), so with scripts gone the pressed readings equal hover. The pressed colours exist as tokens (`variant.<colour>.<variant>.bg-active`) but no element was seen in that state.
- Hover and focus are real pointer and keyboard events on static copies. Anything ChatGPT changes on hover through script (Radix menu highlighting, the sidebar row actions) shows only as far as the CSS draws it.
- Light was read by flipping `data-theme`, not by changing the account's appearance; only the Blue accent was captured (the accent is an account setting). The other accents' text colours are in `chatAccent`, their fills are not.
- Message text, titles and Library file names are filler of the same length, so widths that depend on text are the filler's. Library thumbnails, the installed plugins and one Images template (round, so it matched the avatar rule) were blanked in the copies; the plugin store's own icons are served with a signed URL, which the capture cuts, so they render as broken images.
- Elevation `tooltip` and `dialog` are the measured layers; no single shadow token holds them (`--shadow-tooltip` declares the same shadow, its alpha rounds differently).

## Fonts

| Family | Weights | Used for |
|---|---|---|
| System stack (`-apple-system-body, ui-sans-serif, -apple-system, system-ui, Segoe UI, Helvetica, Arial`) | 400, 500, 510, 590, 600 | Everything measured, including the sidebar wordmark (600). `core.fontFamily.sans`. |
| ui-monospace stack (`ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas`) | 400, 500 | Code blocks and inline code (`core.fontFamily.mono`, `core.typography.code`). |
| OpenAI Sans | 300 to 700 | Declared with `@font-face` (and an "OpenAI Sans Fallback" metric face), served by OpenAI; no measured element used it. Proprietary, so no file is committed or needed. |
| KaTeX faces | 400, 700 | Maths in answers; declared, not seen. |

The type styles are ChatGPT's own `--font-heading-*`, `--font-text-*` and `--font-small-caps-*` sets: headings 16 to 72 at 600 with -0.025em tracking from 32 up, body 14/20, 16/24 and 18/29 at 400, small caps 11 and 13 at 600. Answers are 16/26 (`markdown` in [components.md](components.md#markdown)). The checklist's type roles map onto them as display (heading-3xl to 5xl), headings (heading-xs to 2xl; the home heading is 28), body (text-md, text-sm), label (control-label, small-caps), caption (text-xs, text-2xs) and code (code); the mapping is in `core.typography.$extensions.roles`.

## Colours

The checklist roles, as `role.*` in each theme set:

| Role | Dark | Light | ChatGPT name |
|---|---|---|---|
| Page | #000000 | #fcfcfc | `--color-token-main-surface-primary` |
| Surface | #212121 | #f9f9f9 | `--color-surface-tertiary` |
| Raised | #1b1b1b | #ffffff | `--color-surface-elevated` |
| Overlay (menus) | #303030 at 90% | #ffffff at 90% | measured on the menus, over a 16px backdrop blur |
| Scrim | black at 13% | black at 13% | measured on the dialog overlay |
| Text primary, secondary, tertiary | #ededed, #cdcdcd, #afafaf | #0d0d0d, #5d5d5d, #8f8f8f | `--color-text-primary`, `-secondary`, `-tertiary` |
| Text disabled | #afafaf | #8f8f8f | `--color-text-disabled` |
| On accent, link | #ffffff, #2c67c5 | #ffffff, #2c67c5 | `--color-text-accent-action`, `--color-token-text-link-foreground` |
| Border default, subtle, strong | white at 15%, 5%, 20% | black at 10%, 5%, 15% | `--color-token-border-default`, `--color-border-subtle`, `--color-border-strong` |
| Focus | #3a83f7 | #3a83f7 | `--color-ring` |
| Accent default, hover, pressed | #3a83f7, #0169cc, #0169cc | the same | `--color-background-info-solid` and its `-hover`, `-active` |
| Accent action (send, voice) | #2c67c5 | #3a83f7 | `--color-background-accent-action` |
| Success, warning, danger, info: fill | #011c0b, #281105, #280b0a, #133463 | #edfaf2, #fff5f0, #fff0f0, #e8f3fe | `--color-background-<status>-surface` |
| Status text | #04b84c, #ff8549, #fa423e, #339cff | #008635, #b9480d, #ba2623, #004f99 | `--color-text-<status>-surface` |
| Status border | each hue at 13 to 16% | each hue at 4 to 8% | `--color-border-<status>-surface` |

Every status and the primary and secondary neutrals also come in `soft`, `outline`, `ghost` and `solid` variants with hover and active, under `variant` in each theme set. The grey ramp (`gray.0` to `gray.1000`) flips with the theme; the fixed ramps (`core.color.gray-fixed`, `blue`, `green`, `red`, `orange`, `yellow`, `purple`, `pink`, ...) do not.

## Patterns

How ChatGPT combines its components for the common jobs, as captured.

**App shell and navigation.** A 340 wide sidebar (at 1440; it clamps between 240 and 520) on the page ground: search and hide at the top, destination rows (New chat, Images, Scheduled, Library, Plugins, Explore), then collapsible Pinned, Projects and Recents sections, and the account row at the bottom. The fixed 52 tall header carries the Chat / Work toggle centred and Upgrade at the end. Hiding the sidebar leaves a 52 wide rail of icon buttons; on a phone the sidebar is a 260 wide drawer over the page, opened from the header. Settings is a page of its own with its own left nav and a Back to app row. See [home-dark](screenshots/home-dark.png), [home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png), [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png) and [settings-dark-keyboard](screenshots/settings-dark-keyboard.png).

**Forms and validation.** Settings rows put the label (and a secondary line) at the start and one control at the end: a switch, a select button that opens a checkbox or radio menu, an outline button, or a hex field. Changes apply at once; there is no Save button and no inline validation on any captured row. A disabled control keeps its colours at 40% opacity. No form that validates was reachable without submitting it. See [settings-dark-data-controls](screenshots/settings-dark-data-controls.png), [settings-dark-notifications-menu](screenshots/settings-dark-notifications-menu.png) and [settings-dark-appearance](screenshots/settings-dark-appearance.png).

**Empty, loading and error states.** Empty is one centred line with a small icon in tertiary text, inside the surface that would hold the results ("No results" in search). A failed load replaces the content with one centred line and a small Try again button ("Failed to load files." in the Library); a partial failure is a one-line banner above the results with its own Try again ("Some search results could not be loaded"). No loading skeleton was on screen in any copy. See [home-dark-search-empty](screenshots/home-dark-search-empty.png), [library-dark-error](screenshots/library-dark-error.png) and [library-dark-search-error](screenshots/library-dark-search-error.png).

**Destructive confirmation.** A small dialog (420 wide, `radius.3xl`) on a light scrim: a bold title as a question ("Delete chat?"), one line that names the thing and says it cannot be undone, then Cancel (secondary) and the action named in full ("Delete chat") as a danger pill: red text on a red tint, not a solid red button. Bulk actions in settings use the same danger pill ("Delete all"). See [home-dark-delete-confirm](screenshots/home-dark-delete-confirm.png) and [settings-dark-data-controls](screenshots/settings-dark-data-controls.png).

**Feedback after an action.** Not captured: ChatGPT confirms copying, archiving and sharing with a transient toast or an icon swap, and the capture took no action. What was captured is feedback while composing: the voice button turns into Send as soon as there is text, and a tooltip names an icon button on focus or hover. See [home-dark-composer-typed](screenshots/home-dark-composer-typed.png) and [home-dark-tooltip](screenshots/home-dark-tooltip.png).

**Search and filtering.** Global search is a 720 wide dialog with the field at the top and Clear and close at the end; empty, it lists recent chats; typed, it adds filter tabs (All, Chats, Images, Documents, Projects) and the results or the empty state. The Library has its own field in the page header with a filter button beside it; Archived chats and Plugins put a field at the top of the list. See [home-dark-search](screenshots/home-dark-search.png), [home-dark-search-empty](screenshots/home-dark-search-empty.png) and [settings-dark-archived](screenshots/settings-dark-archived.png).

**Data display.** Lists are rows on the page ground divided by hairlines (`border.subtle`) or by nothing: sidebar chats, archived chats (title link, date, Unarchive and Delete at the end), plugin cards in two columns (a bordered card with one link laid over all of it). Files are a masonry grid of cards (4 columns at 1440; its classes step from 1 to 6 columns with the container width) with a hover checkbox for selection. Tables appear inside answers only, ruled by horizontal hairlines, with bold first-column cells. See [settings-dark-archived](screenshots/settings-dark-archived.png), [library-dark](screenshots/library-dark.png) and [thread-dark-table](screenshots/thread-dark-table.png).

**Onboarding.** Not captured: the account is past its first run. The stylesheets declare `--text-onboarding-*` styles (title 20, body 14, label 16), which are in `core.typography`.

## Do and don't

1. **Do keep the accent for the composer's primary action, the user's own message and what is switched on.** The send and voice button, the user bubble, a switch that is on and the Upgrade label are blue; answers, the sidebar, tabs and every other control are grey. See [thread-dark-user-turn](screenshots/thread-dark-user-turn.png), [home-dark-composer-typed](screenshots/home-dark-composer-typed.png) and [settings-dark-data-controls](screenshots/settings-dark-data-controls.png).
2. **Do mark the current item with the same translucent grey as hover.** The current destination, the open chat and the selected tab rest on `variant.primary.soft.bg-hover` (white at 10% in dark, black at 5% in light), with primary text and no accent, border or bar. See [nav-row-active](components/crops/nav-row-active.png), [chat-row-active](components/crops/chat-row-active.png) and [library-tab-selected](components/crops/library-tab-selected.png).
3. **Do leave the answer on the page ground, unboxed.** An assistant turn has no bubble, card or avatar; only code blocks get a surface (`radius.3xl`) and tables only hairlines. Only the user's turn sits in a shape. See [thread-dark-code](screenshots/thread-dark-code.png) and [thread-dark-table](screenshots/thread-dark-table.png).
4. **Do draw keyboard focus as one blue ring.** Buttons, tabs, switches and fields take a 2px `ring.default` ring with no offset, rows an inset 2px outline; nothing else changes. See [header-icon-button-focus-visible](components/crops/header-icon-button-focus-visible.png), [button-danger-focus-visible](components/crops/button-danger-focus-visible.png) and [switch-on-focus-visible](components/crops/switch-on-focus-visible.png).
5. **Don't use a solid red button for a destructive action.** Delete is red text on a 10% red pill, behind a confirmation dialog that names what goes. See [home-dark-delete-confirm](screenshots/home-dark-delete-confirm.png) and [settings-dark-data-controls](screenshots/settings-dark-data-controls.png).
6. **Do float menus and dialogs as translucent surfaces with a hairline, not heavy shadows.** Menus are the elevated grey at 90% over a 16px blur with a 0.5px ring and one soft drop (`elevation.menu`); the dialog scrim is only 13% black. See [home-dark-chat-menu](screenshots/home-dark-chat-menu.png) and [home-light-chat-menu](screenshots/home-light-chat-menu.png).

## Coverage

Graded against [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md). Captured on 2026-10-17 on the Free plan. Component entries are in [components.md](components.md).

| Item | Status | Where |
|---|---|---|
| Colour ramps | Captured | `core.color` (fixed ramps), `gray` per theme |
| Background roles: page, surface, raised, overlay, scrim | Captured | `role.bg` |
| Text roles: primary, secondary, disabled, on-accent, link | Captured | `role.text` |
| Border roles: default, strong, focus | Captured | `role.border` |
| Accent: default, hover, pressed | Captured as tokens; pressed never seen on an element (script-driven) | `role.accent` |
| Status: fill, text and border for success, warning, danger, info | Captured | `role.status`, `variant` |
| Theme parity | Captured: the same names in both themes (light adds `app.background-recovery` and one shadow) | `light`, `dark` |
| Type | Captured | `core.fontFamily`, `core.fontSize`, `core.lineHeight`, `core.fontWeight`, `core.typography` |
| Spacing | Captured: the 4px unit, and the 17 steps the pages use with their counts (Derived) | `core.spacing` |
| Radii, border widths | Captured | `core.radius`, `core.borderWidth` |
| Sizing and focus ring | Captured | `core.size.control`, `core.size.icon`, `core.size.focusRing` |
| Elevation | Captured: shadow levels and the shadow each surface uses | `shadow`, `elevation` |
| Motion | Captured, with what reduced motion changes | `core.duration` (and its `reducedMotion`), `core.easing` |
| Layout: breakpoints, widths, grid, z-index | Captured | `core.breakpoint`, `core.container`, `core.layout` (grid columns in its `$extensions`), `core.zIndex` |
| Button | Captured: default, hover, focus-visible, pressed, disabled | [button-secondary](components.md#button-secondary), [button-danger](components.md#button-danger), [promo-button](components.md#promo-button), [button-disabled](components.md#button-disabled) |
| Icon button | Captured: default, hover, focus-visible, pressed | [header-icon-button](components.md#header-icon-button), [send-button](components.md#send-button) |
| Link | Captured: default, hover, focus-visible, pressed | [md-link](components.md#md-link), [archived-link](components.md#archived-link), [text-link](components.md#text-link) |
| Text field | Captured: default, hover, focus-visible, typed | [search-field](components.md#search-field), [library-search](components.md#library-search) |
| Text area | Captured: default, focus-visible, typed | [composer](components.md#composer) |
| Select | Captured: default, hover, focus-visible, pressed, open | [select](components.md#select), [accent-menu](components.md#accent-menu) |
| Checkbox | Captured: hover, focus-visible; checked as a menu item | [checkbox](components.md#checkbox), [checkbox-menu-item](components.md#checkbox-menu-item) |
| Radio | Captured: default, hover, focus-visible, checked | [segmented-radio](components.md#segmented-radio) |
| Switch | Captured: on, off, hover, focus-visible | [switch-on](components.md#switch-on), [switch-off](components.md#switch-off) |
| Tabs | Captured: default, hover, focus-visible, selected | [library-tab](components.md#library-tab), [search-tab](components.md#search-tab) |
| Menu | Captured: open, item hover, danger item | [chat-menu](components.md#chat-menu), [menu-item](components.md#menu-item) |
| Tooltip | Captured | [tooltip](components.md#tooltip) |
| Dialog | Captured, with its scrim | [confirm-dialog](components.md#confirm-dialog), [search-dialog](components.md#search-dialog) |
| Toast | Not captured: appears only after an action, and the capture took none | |
| Card | Captured: default, hover | [library-card](components.md#library-card), [promo-card](components.md#promo-card), [pricing-card](components.md#pricing-card) |
| List row | Captured: default, hover, focus-visible, active | [chat-row](components.md#chat-row), [archived-row](components.md#archived-row) |
| Table | Captured | [md-table](components.md#md-table) |
| Avatar | Captured size and shape; the photo was replaced for privacy | [avatar](components.md#avatar) |
| Badge | Captured | [badge](components.md#badge) |
| App shell and navigation | Captured | [home-dark](screenshots/home-dark.png), [home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png) |
| Form with a validation error | Not captured: no form in reach validates without submitting | |
| Empty, loading and error states | Empty and error captured; loading not captured (nothing was loading in any copy) | [home-dark-search-empty](screenshots/home-dark-search-empty.png), [library-dark-error](screenshots/library-dark-error.png) |
| Destructive confirmation | Captured (opened and cancelled) | [home-dark-delete-confirm](screenshots/home-dark-delete-confirm.png) |
| Feedback after an action | Not captured: needs an action | |
| Search and filtering | Captured | [home-dark-search-empty](screenshots/home-dark-search-empty.png), [library-dark-search-error](screenshots/library-dark-search-error.png) |
| List or table | Captured | [settings-dark-archived](screenshots/settings-dark-archived.png), [thread-dark-table](screenshots/thread-dark-table.png) |
| Onboarding | Not captured: the account is past its first run | |
| Light and dark | Captured | every copy in both themes |
| Desktop and phone widths | Captured | 1440 everywhere; 390 for the home, the drawer and a thread |

Totals over 43 rows: 39 captured (states that were not reachable are named in their row), 0 not present, 4 not captured.

Also not captured: a streaming answer, voice mode, Work mode, Codex, Scheduled, a project page, the share dialog, and the Account, Billing and Personalization settings, since each either sends something, spends quota or shows account details.

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

`build_tokens.py` reads `raw/css-vars.json` and `raw/components-computed.json` and writes `tokens.json`; it refuses an alias that points at nothing and a dimension that is not one px or rem length. `build_style_guide.py` renders `style-guide.html` from `tokens.json` and `tools/style-guide.template.html`. `build_components_md.py` writes `components.md` from the measurements, the tokens, the screenshots and `icons/INDEX.tsv`. All three are deterministic.

`tools/capture/` holds the kit the captures came from. The Playwright scripts take `PLAYWRIGHT` as the path to a Playwright install's `index.mjs` and `SNAPS` as the directory of page copies, which are not committed since they hold the owner's content. The crop step needs Pillow on the `python3` in `PATH`.

```bash
PLAYWRIGHT=... SNAPS=<dir> tools/capture/signed-in/render-all.sh [label ...]
```

```bash
python3 tools/capture/quantize.py <dir>/renders
```

```bash
PLAYWRIGHT=... SNAPS=<dir> node tools/capture/vars.mjs
```

```bash
PLAYWRIGHT=... SNAPS=<dir> READ_DATE=2026-10-17 node tools/capture/signed-in/measure.mjs [label ...]
```

```bash
node tools/capture/signed-in/build-measurements.mjs
```

```bash
PLAYWRIGHT=... SNAPS=<dir> node tools/capture/layout.mjs
```

```bash
PLAYWRIGHT=... SNAPS=<dir> node tools/capture/icons.mjs
```

To take a new page copy: open the page in a signed-in tab, paste `snapshot.js` into its console, `await __sprites()`, then `__snap('<page>-dark-<state>', REDACT)` with the redaction file's contents (it needs `replace`, and `scrub` as `[selector, "filler"]` pairs for message text), save the returned string to a file and run `unsnap.py <file> <dir>`. Labels and their render flags are in [shots.tsv](tools/capture/signed-in/shots.tsv).

## Use in Figma

Import `tokens.json` with Tokens Studio and choose the Light or Dark theme. Set the UI font to SF Pro or Inter (the system face ChatGPT relies on is not a web font). Use `role.*` for colour decisions and `component.*` for the measured component values.

## The screen to get right

The thread. Everything else is a frame around one 768 wide column where the answer sits on the page ground at 16/26 under the user's single coloured bubble, with the composer pill pinned under both at the same width. Colour is spent on the user's words, the send button and what is switched on; the answer, the sidebar and every control stay grey, hover and selection are one translucent fill, and focus is one blue ring.
