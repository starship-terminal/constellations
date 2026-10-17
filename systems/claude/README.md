# Claude design reference

A token set and component reference for the Claude web app (claude.ai), for self-learn's chat surfaces: the tutor chat on a concept, the sidebar, the library of things the agent made, courses as projects, and settings. It was read on 2026-10-04 from the owner's signed-in account (Max plan), in both themes, at 1440 wide and 390 wide: the home page with its greeting and composer, a chat (the user bubble, Claude's reply with a code block and a table, the message actions), Artifacts, Chats and tasks, Projects and a project page, the Settings dialog, search, every composer and sidebar menu, the hidden sidebar, and the phone layout (home, the drawer sheet, a chat). It was refreshed on 2026-10-17 from the same account, at 1440 wide, to fill the gaps the scorecard found: a tooltip, the checkbox in the Chats page's Select mode, the delete confirmation dialog, the Create a project form, the Chats filter menu and an empty search, a loading skeleton, the Account and Capabilities settings panes (text link, disabled button and switch), every pressed state, and the rules the stylesheets apply under breakpoints and reduced motion.

The earlier references cover learning products (Duolingo, Brilliant, NotebookLM, Coursera, Gauth) and one agent product (Manus). self-learn's tutor is a chat with a model, and claude.ai is the chat it is most often compared with: a quiet shell, a serif voice for the model and a sans for the interface, one composer that travels between the home page, a chat and a project. This is the reference for getting those surfaces to feel finished.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (779: the nine 35-step colour ramps, the brand pigments and the role scales; font families including the chat font options; weights with their dark-mode variation axis; the seven type roles as sizes, line heights and 24 composite styles; the cds density scale with its compact value in `$extensions.compact`; the control size steps; durations, easings, z-index, opacity; the sidebar frame's geometry; Tailwind's theme; the measured layout, radii and sizes; and from the refresh the breakpoints, page grids, border widths, the 4px spacing scale, the press scale, what reduced motion changes, the focus ring and the link underline), `light` (379) and `dark` (379): the semantic palette grouped by role (surface, text, fill, bg, border, on, alpha, neutral, chart, shadow, control, pictogram, git, editor), the sidebar frame's colours, the older palette Claude still reads (`legacy`), measured shadows (`component`), and the link and pressed roles (`text.link`, `fill.*-pressed`), plus `$themes`. Every token carries `$extensions.source`; a value DTCG cannot carry is listed under the set's `$extensions.notTokenised`. |
| [style-guide.html](style-guide.html) | One self-contained page that renders every token and the main components (the shell with the sidebar, the composer at rest and typed, buttons, menus, the thread, Artifacts, project cards, settings, the phone layout) with the real values, states side by side, with a Light/Dark toggle that sets `data-mode` the way Claude does. |
| [components.md](components.md) | The discovery list of every page and state captured, one entry per component (165) with crops of the real product, the shared values (hover washes, radii, focus ring, motion, rings), the icon index, and the Gaps. Every colour, shadow, radius, padding, type style, icon size, opacity, duration and curve in an entry is written as the token that holds it, with the measured value after it (90% of the values written; the rest no token holds, and content widths are written raw). |
| [components/crops/](components/crops) | 674 element screenshots, `{component}-{state}.png`, at 2x. |
| [icons/](icons) | 72 SVGs: 62 glyphs drawn from Claude's icon font (Anthropicons-Variable) and 10 inline SVGs from the pages, named by role, indexed in [icons/INDEX.tsv](icons/INDEX.tsv). They are Anthropic's property, kept for reference only. |
| [screenshots/](screenshots) | 64 `{page}-{theme}-{state}.png` captures (22 from the refresh). Desktop shots are 1440 x 900 at 2x, `-full` shots whole pages for the dark Artifacts and Chats pages, `mobile-*` shots 390 x 844 at 2x. Every other state exists in both themes. |
| [raw/](raw) | The unprocessed readings: every custom property the stylesheets declare, by selector and condition and sorted into Claude's own (`cds`, `app`), one-off utility overrides and Tailwind's internals, with each name resolved on a light, a dark and a compact root, and the font faces (`css-vars.json`); per-component computed styles (`components-computed.json`, and `measurements.md` built from it); the measured values the token builder reads (`component-tokens.json`); page geometry (`layout.json`) and the layout notes written from it (`pages.md`); and from the refresh, the ordinary declarations under conditions and states: @media widths, reduced-motion rules, :active rules, border and outline widths, grid columns and link rules (`css-rules.json`). |
| [tools/](tools) | The three builders and the capture kit. See Rebuild. |

## How the values were read

Claude's interface is built on its design system, cds: every themed root carries `class="cds-root"` and `data-theme="claude"`, `data-mode="light|dark|system"` (system follows `prefers-color-scheme`), `data-density="comfortable|compact"`, `data-font="anthropic|system"` and `data-color-version="v2"`. One stylesheet bundle declares nine colour ramps and the `--cds-role-*` scales on `:where(:root, :host)`, the semantic names on `.cds-root` for light and again under `data-mode="dark"`, and the density scale with a comfortable override (compact is the default when no density is set). The stylesheets are served from assets-proxy.anthropic.com with CORS headers, so the signed-in page's CSSOM could read them and the page copies carry them inline. [vars.mjs](tools/capture/vars.mjs) parses those blocks from the copies (they are identical in every copy and are deduplicated) in a headless Chromium with a constructed CSSStyleSheet, keeps every custom property with its selector and enclosing condition, and then resolves each name the way the browser does on a probe document with Claude's own root attributes, so a value like `hsl(from var(--cds-neutral-900) h s l / 10%)` comes back as `rgba(11, 11, 11, 0.1)`. The token builder aliases a token to another when its declaration is a plain `var()` of a token with the same resolved value.

The pages were captured in the built-in browser pane of the desktop app, signed in, without handing the account to a headless browser. In each page state, [snapshot.js](tools/capture/signed-in/snapshot.js) copied the DOM with every stylesheet inlined from the CSSOM, replaced the account's name and email by the patterns in a redaction file that lives outside the repository (shaped like [redact.example.json](tools/capture/signed-in/redact.example.json)), cut every signed URL back to its path, and marked every scrolled element. [unsnap.py](tools/capture/signed-in/unsnap.py) refuses a copy in which a redacted string or a signing parameter survived. The copies themselves hold the owner's chats, so they stay outside the repository too. [render.mjs](tools/capture/signed-in/render.mjs) renders each copy at 2x, and renders the light theme by setting every `[data-mode]` element to `light`, which is all Claude's own switch does, so no account setting changed: the account was on dark, and every capture started dark.

Claude's popups are Base UI. A closing popup is marked `data-ending-style` (with `data-closed`) and an opening one `data-starting-style`, and Base UI clears both from an animation frame. The pane was hidden while capturing, so no frame ran: closed menus stayed mounted and new ones stayed at their starting style. The copy drops the first and settles the second. The same frozen frames are why modal backdrops may render undimmed, and why the phone drawer could not be closed (it was hidden by hand before the phone chat was copied).

Component values are computed styles read per state with Playwright from the rendered copies ([measure.mjs](tools/capture/signed-in/measure.mjs)): hover with the pointer, focus-visible with a real keyboard focus, both themes by setting every `[data-mode]` to light as render.mjs does. States that need JavaScript (an open menu, the search dialog, the typed composer, the hidden sidebar, the settings dialog, the drawer) were each captured as their own copy, so they are measured in the state they were captured in. The chat is not virtualised, so one copy is read at three scroll positions. The sidebar is hidden in the account's own setting; it was shown for the captures and hidden again afterwards. Nothing was sent, created or deleted: a line was typed into the composer and deleted, and menus were opened and closed. The copies hold the owner's own chat, project and artifact titles, so nothing is rendered or measured from them as they are: [neutralise.py](tools/capture/signed-in/neutralise.py) first writes a second copy in which every text node and label that is not interface text reads `Conversation N`, `Pinned chat N`, `Artifact N`, `File N.ext` or filler words of the same length, and the account name reads "Learner". Every screenshot, crop and `raw/*.json` value comes from that second copy.

The 2026-10-17 refresh took nine more copies the same way, in the built-in browser pane signed in to the same account, starting dark, and ran them through the same neutraliser before anything was rendered or measured. Nothing was sent or created: the delete dialog was opened from a chat row's menu and dismissed with Escape, the Create a project dialog was opened, a name typed and cleared, and Cancel pressed, a checkbox was ticked in Select mode and Select mode was left, and a search for a nonsense word was typed and cleared. The sidebar was shown for these captures and hidden again after. Two more copies were taken later the same day for the patterns the first pass could not reach: opening `/chat/<id>` with an id that does not exist, which sends you home with a warning toast (a page load, nothing changed), and `/onboarding`, the account's first-run screen, which was snapshotted as it opened and left without ticking or pressing anything. Three readings are new. [rules.py](tools/capture/rules.py) walks every rule in the inlined stylesheets with its enclosing @media, @supports, @layer and @container and writes `raw/css-rules.json`, the source of the breakpoints, border widths, the press scale and the reduced-motion list. measure.mjs gained a `pressed` state: the pointer is held down on the element for 250 ms (`:active`), which makes a cds Button scale its paint layer, read as `squish`. And the error state of a text field was read by setting `data-invalid` on the field in the copy, which is what cds Field sets when validation fails; the ring and focus colour are Claude's own `data-[invalid]:` rules, but the error message text was never seen, because the form was never submitted. The stylesheet bundle was read again on the refresh day: every colour token resolves to the same value as on 2026-10-04 (the dark set's aliases differ only because a few dark declarations no longer point at a ramp step by `var()`), so `raw/css-vars.json` and the tokens it feeds were kept from the first capture.

Three things to read with care. Syntax-highlighted code keeps the dark theme's inline colours, so code colours in the light renders are wrong; read them from the dark copies. Artifact previews are iframes, kept as dark boxes. And the package mixes two capture days: the 2026-10-04 screenshots and crops were not retaken, so the Artifacts page in them is a list, while the 2026-10-17 copies show it as a grid of cards; each state in `raw/components-computed.json` records the copy it came from, and `_meta.snapshots` gives each copy's date.

Screenshots are stored as 256-colour PNGs to keep the folder small. Flat UI colours are exact; read values from the tokens, not the images.

## Fonts

| Family | Used for | Licence | Use instead |
|---|---|---|---|
| Anthropic Sans (`anthropic-sans`) | Everything in the interface, at the cds type roles: caption 12, footnote 13, body 14, heading 15, title 22 (comfortable). Semibold is 580, bold 600. | Anthropic's own face, served from assets-proxy.anthropic.com; no licence for reuse | The stack's own fallbacks, `system-ui, "Segoe UI", Roboto, Helvetica, Arial` (`fontFamily.sans`); Inter or SF Pro in Figma |
| Anthropic Serif (`anthropic-serif`, `--cds-font-voice`) | The "Claude" wordmark, the home greeting (38/47.5 at weight 300 with the opsz 48 axis), page titles (24/32, 500), and Claude's replies at 16/24, the chat font's default. | Anthropic's own face; no licence for reuse | Georgia, the stack's first real fallback (`fontFamily.serif`); the style guide uses Source Serif 4 from Google Fonts as a stand-in |
| Anthropic Mono (`anthropic-mono`) | Code blocks and code spans. | Anthropic's own face; no licence for reuse | `ui-monospace, "SF Mono", Menlo, Consolas`, the stack's fallbacks (`fontFamily.mono`) |
| Anthropicons-Variable | Every icon: one character per glyph, its weight thinned as the size grows. | Anthropic's own icon font; the 72 drawings in [icons/](icons) are kept for reference only | An open icon set of your choice, at the sizes and roles [icons/INDEX.tsv](icons/INDEX.tsv) lists |
| System, OpenDyslexic | The other chat font options in Settings > Appearance (System, Dyslexic friendly); `data-font="system"` swaps the UI sans for the platform face. | The platform's own face; OpenDyslexic is an open font under its own licence | The same |

In dark mode the variable faces are drawn lighter: each weight also sets `font-variation-settings` to a lower `wght` (regular 360, medium 460, semibold 540, bold 560), recorded on each `fontWeight` token as `$extensions.darkVariationAxis`.

Anthropic's four faces are not in the repository and must not be shipped. No font file is committed or needed: the style guide falls back to the system sans, to Source Serif 4 from Google Fonts as a stand-in for the serif (named as such on the page), and to ui-monospace.

## Patterns

How Claude's components combine for the common jobs, read from the captures. Each row names the screen to look at.

| Pattern | How Claude does it | Components | Example |
|---|---|---|---|
| App shell and navigation | A 288px sidebar on its own ground (wordmark, Home/Code, New, Artifacts, More, Pinned, Chats and tasks, the account row) beside one content column with a 48px header; list pages centre a 960 column, a chat a 768 transcript. The sidebar can be hidden to one button, and on a phone it is a full-screen sheet. | `sidebar`, `nav-row`, `chat-row`, `pane-header`, `page-header` | [home-dark](screenshots/home-dark.png), [home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png), [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png) |
| Forms and validation | Forms live in a dialog: a title, labelled fields stacked with the label above (sentence-case question, 14px medium), then Cancel and the primary action at the end. The action stays enabled while the field is empty. An invalid field keeps its fill and swaps its hairline for a 1px `fill.danger` ring, and its focus ring for `shadow.focus-danger`; the message text that goes with it was not seen. | `form-dialog`, `field-label`, `text-field`, `text-field-invalid`, `text-area`, `button-primary`, `button-secondary` | [projects-dark-create](screenshots/projects-dark-create.png) |
| Empty, loading and error states | Empty is one centred `text.muted` line that quotes the query, with no picture and no action. Loading draws the page's real layout in `cds Skeleton` bars and cards that shimmer every 2 s (no shimmer under reduced motion). An error recovers rather than stops: opening a chat that no longer exists sends you to a fresh home page and says why in a warning toast ("That chat is no longer available. Starting a new one."). | `empty-state`, `skeleton`, `skeleton-card`, `toast` | [chats-dark-search-empty](screenshots/chats-dark-search-empty.png), [artifacts-dark-loading](screenshots/artifacts-dark-loading.png), [home-dark-toast](screenshots/home-dark-toast.png) |
| Destructive confirmation | A small `ConfirmationDialog` (role alertdialog, 400 wide): a question as the title ("Delete chat?"), one sentence, then Cancel (secondary) and the action in `fill.danger`. The red menu item that opens it is the only other red. Bulk delete in Select mode uses the same red button in the page header. | `confirm-dialog`, `button-danger`, `button-secondary`, `chat-menu-item-danger`, `selection-bar` | [chats-dark-delete-confirm](screenshots/chats-dark-delete-confirm.png), [home-dark-chat-menu](screenshots/home-dark-chat-menu.png) |
| Feedback after an action | Selection answers in place: ticking a row fills its checkbox with `fill.accent`, and the header swaps Select and New for a muted count, Select all and Delete. Pressing any cds button keeps its hover fill and squishes it to 97.5% in 60 ms. Copying (a message, the organization ID) raised no toast. A toast is kept for news the user did not ask for: bottom right, 360 wide, a status-coloured card (a `bg.*` layer over `surface.3`, a 1px `border.*` ring, `text.*` ink) with a glyph, one sentence and Dismiss; several stack upward. Information that stays on the page is a neutral `Banner` (role status) on `surface.1` with a hairline ring and an info glyph. | `checkbox`, `selection-bar`, `button-primary` (pressed), `toast`, `toast-dismiss`, `banner-info` | [chats-dark-select](screenshots/chats-dark-select.png), [home-dark-toast](screenshots/home-dark-toast.png), [settings-dark-capabilities](screenshots/settings-dark-capabilities.png) |
| Search and filtering | Global search is a 672 dialog over a dimmed page (Shift Cmd K); list pages put a search icon in the header that opens an inline field with a clear button, and a filter icon that opens a menu of mutually exclusive filters (All, Chat, Shared, Cowork, Archived) with a tick on the current one. | `search-dialog`, `search-field`, `search-input`, `filter-menu`, `filter-menu-item` | [home-dark-search](screenshots/home-dark-search.png), [chats-dark-filter-menu](screenshots/chats-dark-filter-menu.png) |
| Data display | Lists are full-width rows with the title at the start and a muted time at the end, hairlines between, a hover wash and the row's actions shown on hover; Chats is a table of such rows, Artifacts and Projects grids of cards (three and two columns, 24 gaps). Chats has a Sort by button beside its filter; tables inside a reply use the chat serif. No pagination was seen: lists scroll. | `chats-row`, `artifact-row`, `project-card`, `table`, `table-th` | [chats-dark](screenshots/chats-dark.png), [projects-dark](screenshots/projects-dark.png), [thread-dark-table](screenshots/thread-dark-table.png) |
| Onboarding and first run | First run is one screen at `/onboarding`: the wordmark at the top, a serif display title ("Let's create your account") with a secondary line, one 448-wide card on `surface.3` (radius 16, a hairline border, `shadow.sm`) holding the consent checkboxes (terms with inline links, and an opt-in for email) and a full-width 40px primary button, and the verified email with a "Use a different email" link at the foot. Nothing is pre-ticked. After it, the first thing a person sees is the home greeting and the composer, which is the empty state of a new chat. | `onboarding-card`, `onboarding-title`, `onboarding-checkbox`, `onboarding-button`, `greeting`, `composer` | [onboarding-dark](screenshots/onboarding-dark.png), [home-dark](screenshots/home-dark.png) |

## Coverage

Graded against [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md). Rows read on 2026-10-04 unless they name the 2026-10-17 refresh; both from the owner's Max account.

| Item | Status | Where |
|---|---|---|
| Colour primitives | Captured: nine 35-step ramps, gray first | `core.color` |
| Backgrounds: page, surface, raised, overlay, scrim | Captured | `surface.page`, `surface.0` to `3`, `surface.panel`, `surface.popover`, `surface.backdrop` |
| Text: primary, secondary, disabled, on-accent, link | Captured; link from the refresh (cds TextLink: `text.accent`, underlined at 40%) | `text.*`, `on.accent`, `text.link`, `text.link-underline` |
| Borders: default, strong, focus | Captured | `border.default`, `border.strong`, `border.stronger`, `shadow.focus` |
| Accent: default, hover, pressed | Captured; a held button keeps its hover fill and squishes (refresh; accent pressed derived from the primary and danger buttons) | `fill.accent`, `fill.accent-hover`, `fill.accent-pressed`, `core.press` |
| Status: success, warning, danger, info | Captured. Success, warning and danger have their own hues with fill, bg, text and border. Info has no hue in cds: Claude informs with the neutral `Banner` (role status), measured on the refresh and tokened as `bg.info` (`surface.1`), `text.info` and `fill.info` (the glyph, `text.primary`) and `border.info` (the ring, `border.default`) | `fill.*`, `bg.*`, `text.*`, `border.*`, `banner-info` |
| Type | Captured: families with fallback stacks, ten sizes, four weights, line heights, 24 composite roles plus display, page title, chat, and a label role measured on a form (refresh) | `core.fontFamily`, `core.fontSize`, `core.typography` |
| Spacing | Captured: Tailwind's 4px unit with half steps (refresh); 90% of measured paddings and gaps sit on the 2px half grid, 45% on 4px | `core.space`, `core.density`, `core.tailwind.spacing` |
| Shape: radii, border widths | Captured; border widths from the refresh | `core.radius`, `core.borderWidth` |
| Sizing: control heights, icons, focus ring | Captured; the focus ring's widths and outline offset as their own tokens (2026-10-17) | `core.density`, `core.size`, `shadow.focus`, `core.focusRing` |
| Elevation | Captured | `shadow.sm`, `md`, `lg`, `popover`, `panel`, `component.*` |
| Motion, and reduced motion | Captured; what reduced motion changes from the refresh (125 rules, plus Claude's own Motion setting) | `core.duration`, `core.easing`, `core.duration.$extensions.reducedMotion` |
| Layout: breakpoints, widths, grid, z-index | Captured; breakpoints and grids from the refresh | `core.breakpoint`, `core.layout`, `core.grid`, `core.zIndex` |
| Button | Captured: default, hover, focus-visible, pressed, disabled. Loading not captured (it needs a sent message) | `button-primary`, `button-primary-page`, `button-secondary`, `button-danger`, `button-disabled`, `send-button`, `header-button`, `card-button` |
| Icon button | Captured: default, hover, focus-visible (the sidebar Search button and a chat row's more button re-read with keyboard focus on the 2026-10-17 copy). Pressed read once in the live page (`--cds-btn-press-sx: 0.9375`), not measured headless | `sidebar-icon-button`, `header-icon-button`, `message-action`, `composer-plus` |
| Link | Captured: default, hover, focus-visible, pressed (refresh); underline offset and mix as tokens | `text-link`, `core.link` |
| Text field | Captured: default, hover, focus-visible, error (refresh; error read with `data-invalid` set on the copy) | `text-field`, `text-field-invalid`, `search-input`, `settings-search` |
| Text area | Captured: default, hover, focus-visible (refresh), and the composer | `text-area`, `composer` |
| Select | Captured: default, hover, focus-visible. The open list not captured | `select` |
| Checkbox | Captured: default, hover, focus-visible, pressed, checked, checked hover (refresh) | `checkbox` |
| Radio | Captured: the Theme picker is a radio group (`role=radio`): default, hover, checked; the Chat/Cowork segments are the same cds radio group and their checked radio was read with keyboard focus (2026-10-17); the filter menu's items are radio menu items | `theme-option`, `segment`, `filter-menu-item` |
| Switch | Captured: off, on, hover, focus-visible, disabled (refresh) | `switch`, `switch-disabled` |
| Tabs | Captured: default, hover, focus-visible (the ring sits on the tab's inner button), selected | `tab` |
| Menu | Captured: six menus, item hover, keyboard focus (the highlight wash, 2026-10-17), checked, submenu, danger item | `plus-menu`, `model-menu`, `user-menu`, `chat-menu`, `more-menu`, `filter-menu`, `menu-item`, `menu-item-keyboard` |
| Tooltip | Captured (refresh) | `tooltip` |
| Dialog | Captured: search, settings, form and confirmation dialogs, the backdrop | `search-dialog`, `settings-dialog`, `form-dialog`, `confirm-dialog`, `dialog-backdrop` |
| Toast | Captured (refresh): the warning toast raised by opening a chat that no longer exists, with its Dismiss button (default, hover, focus-visible) | `toast`, `toast-dismiss` |
| Card | Captured: default, hover, focus-visible (a project card re-read on the 2026-10-17 copy: the ring sits on its inner link) | `project-card`, `template-card`, `notice-card`, `instructions-card` |
| List row | Captured: default, hover, selected, pinned, focus-visible (sidebar and Chats rows, 2026-10-17: the ring sits on the row's inner link) | `chat-row`, `artifact-row`, `chats-row`, `search-result` |
| Table | Captured | `table`, `table-th`, `table-td`, `chats-row` |
| Avatar | Captured (the photo replaced by a disc) | `account-avatar` |
| Badge | Captured | `badge` |
| App shell and navigation | Captured | see Patterns |
| Form with a validation error | Captured, with the error drawn on the copy; message text not captured (the form was not submitted) | see Patterns |
| Empty, loading and error states | Captured (refresh): empty search, loading skeletons, and the missing-chat redirect with its warning toast | see Patterns |
| Destructive confirmation | Captured (refresh), dismissed without deleting | see Patterns |
| Feedback after an action | Captured: selection, press, the toast and the information banner | see Patterns |
| Search and filtering | Captured | see Patterns |
| List or table | Captured | see Patterns |
| Onboarding | Captured (refresh): the `/onboarding` screen, looked at only; nothing on it was ticked or pressed | see Patterns |
| Light and dark | Captured: every copy rendered and measured in both | |
| Desktop and phone widths | Captured: 1440 everywhere; 390 for home, the drawer and a chat (2026-10-04 only) | `mobile-*` |

Totals over 42 rows: 42 captured (the states and parts that were not reachable are named in their row).

## Do and don't

1. **Do give each colour one job.** Clay (`fill.brand`, #c6613f) appears only on the greeting's asterisk and the send button. Blue (`fill.accent`, #2a78d6) only marks something that is on (a switch, the ticks in the plus and model menus) and the focus ring. See [home-light-composer-typed](screenshots/home-light-composer-typed.png), [home-light-plus-menu](screenshots/home-light-plus-menu.png) and [settings-light-general](screenshots/settings-light-general.png).
2. **Do give a page at most one filled button, and fill it with ink.** "New project" on Projects, "New" on Chats and tasks and "Migrate team design systems" on Artifacts are filled with `fill.primary`, black in light and white in dark. The actions beside them (Select, Share, "Visit the standalone homepage") are quiet buttons with a faint wash (`alpha.2` in dark) or bare icons, and no page button is clay. See [projects-light](screenshots/projects-light.png), [projects-dark](screenshots/projects-dark.png), [chats-light](screenshots/chats-light.png) and [artifacts-light](screenshots/artifacts-light.png).
3. **Do set Claude's words in the serif and everything else in the sans.** A reply, including the table inside it, is Anthropic Serif 16/24, while the user's bubble beside it is Anthropic Sans 15/20. The serif also sets page titles and the greeting; rows, menus, buttons and labels stay sans. See [thread-light-table](screenshots/thread-light-table.png), [user-message-light](components/crops/user-message-light.png) and [projects-light](screenshots/projects-light.png).
4. **Do keep resting surfaces flat; only the composer and floating layers cast a shadow.** Project cards, the Artifacts notice card and the project page's rail are edged by a 1px hairline at 10% with no drop, and the user bubble is a 5% wash with no edge. The composer adds a soft `0 4px 20px` at 4%, and menus a larger `0 8px 24px` drop. See [projects-light](screenshots/projects-light.png), [project-dark](screenshots/project-dark.png) and [home-light-plus-menu](screenshots/home-light-plus-menu.png).
5. **Do keep section labels small, muted and in sentence case.** "Pinned", "Chats and tasks", "Make something new", the month headings, "Recents" and the Settings nav groups ("Settings", "Customize") are all `text.muted` at 12 to 14px, never uppercase. See [home-dark](screenshots/home-dark.png), [artifacts-light](screenshots/artifacts-light.png), [project-dark](screenshots/project-dark.png) and [settings-light-general](screenshots/settings-light-general.png).
6. **Do hide per-item controls in the sidebar and the chat until the pointer arrives.** A sidebar chat row shows only its 6px ring and title at rest; the more button comes in with the hover wash. Under a reply the copy, rating and retry row is not drawn at rest, and the code block's copy button shows only on hover. See [chat-row-default](components/crops/chat-row-default.png), [chat-row-hover](components/crops/chat-row-hover.png) and [thread-light-table](screenshots/thread-light-table.png).

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

`build_tokens.py` reads `raw/css-vars.json`, `raw/component-tokens.json`, `raw/css-rules.json` and `raw/components-computed.json` and writes `tokens.json`; it refuses an alias that points at nothing, an alias to a token of another type, and a dimension that is not one px or rem length. `build_style_guide.py` renders `style-guide.html` from `tokens.json` and `tools/style-guide.template.html`, turning every token into a CSS variable so the page cannot drift from the file. `build_components_md.py` writes `components.md` from `raw/components-computed.json`, `raw/layout.json`, `tokens.json`, the screenshots and `icons/INDEX.tsv`. All three are deterministic.

`tools/capture/` holds the kit the captures came from. The Playwright scripts take `PLAYWRIGHT` as the path to a Playwright install's `index.mjs` (this repository has one under `tools/tldrawkc/node_modules/playwright/`), and the signed-in scripts take `SNAPS` as the directory of page copies, which are not committed. Fonts and images the copies load come from assets-proxy.anthropic.com through a cache beside the copies (`<SNAPS>-cdn-cache`); nothing is requested from claude.ai.

```bash
PLAYWRIGHT=$PWD/../../../../tools/tldrawkc/node_modules/playwright/index.mjs SNAPS=<dir> node tools/capture/vars.mjs
```

```bash
python3 tools/capture/signed-in/neutralise.py <page copies> <dir>   # SNAPS is <dir> from here on; <page copies>-cdn-cache is linked beside it as <dir>-cdn-cache
PLAYWRIGHT=... SNAPS=<dir> tools/capture/signed-in/render-all.sh && python3 tools/capture/quantize.py <dir>/renders
```

```bash
PLAYWRIGHT=... SNAPS=<dir> node tools/capture/signed-in/measure.mjs && node tools/capture/signed-in/build-measurements.mjs
```

```bash
PLAYWRIGHT=... SNAPS=<dir> node tools/capture/layout.mjs
```

```bash
SNAPS=<dir> python3 tools/capture/rules.py
```

`measure.mjs <label ...>` re-measures only the components on those copies and merges them into the JSON, which is how the refresh was added without the 2026-10-04 copies (deleted on 2026-10-11). The crops are quantised with Pillow, so `python3` must have it.

```bash
PLAYWRIGHT=... HB=<harfbuzzjs dir> WAWOFF2=<wawoff2 dir> SNAPS=<dir> node tools/capture/icons.mjs
```

`icons.mjs` draws the icon-font glyphs with harfbuzzjs after decompressing the font with wawoff2; both default to the copies under `tools/tldrawkc/node_modules/`. Names come from [icon-names.tsv](tools/capture/icon-names.tsv). To take a new page copy: open the page in a signed-in tab, paste `snapshot.js` into its console, call `__snap('<page>-dark-<state>', REDACT)` with the redaction file's contents, save the returned string to a file and run `unsnap.py <file> <dir>`; add the label to [shots.tsv](tools/capture/signed-in/shots.tsv). The neutraliser keeps only the interface strings it lists, so a new page's labels go into its `KEEP` list or they render as filler. Before committing images, run `python3 tools/catalog.py scan systems/claude --redact ~/.design-systems/claude-redact.json` and `python3 tools/redact_images.py check systems/claude --patterns ~/.design-systems/cleanup-redact.json --rules tools/redact-rules/claude.json` from the library root.

## Use in Figma

Import `tokens.json` with Tokens Studio and choose the Light or Dark theme. Set the UI font to Inter or SF Pro and the serif to a book serif such as Source Serif 4 or Tiempos (Anthropic's faces are not available). Sizes are the comfortable density; the compact values are in each token's `$extensions.compact`.

## Claude's surfaces and self-learn's

| Claude | Layout | self-learn |
|---|---|---|
| Sidebar | 288 px on its own ground, a step darker than the page in dark: the serif wordmark with Hide sidebar and Search, the Home/Code pills, New (⇧⌘O), Artifacts and More, a Pinned section, "Chats and tasks" whose rows lead with a 6px hollow ring and fade at the end, the account row with the plan. Hidden, it leaves one button in the corner; on a phone it is a full-screen sheet. | The sidebar in `apps/web/src/components/shell/AppSidebar.tsx`, whose list is New chat (the studio) and `DESTINATIONS` in `apps/web/src/lib/nav.ts` (Home, Courses, Learn, Library), with the studio's conversations where Claude puts its chats |
| Home greeting and composer | The serif greeting led by the clay asterisk, over a 672 px composer: radius 20 on surface-3 with a 1px ring, the editor, then +, a Chat/Cowork segmented control, the model and effort, dictation and voice; typing swaps voice for the clay send button. | `/home` and its Ask box, and the new-chat screen of the studio |
| Chat | A 768 px transcript: the user's right-aligned bubble (a 5% wash, radius 12), "Thought for 6s", the reply in Anthropic Serif 16/24 with code blocks and tables, actions that show on hover, the composer docked at the bottom with the disclaimer under it. | the tutor on `/learn/<concept>` and `/ask` |
| Artifacts | A 960 px page: a serif title, tabs (All, Yours, Shared with you), Make something new tiles, then month groups of rows (icon, title, a muted line, visibility, date, more). | `/library` and the studio's diagrams and videos |
| Projects and a project page | A two-column grid of cards; a project has a breadcrumb, a title, its own composer, Recents, and a right rail of Instructions, Memory and Context cards. | courses (`/courses` and a course page) |
| Settings | A 1024 x 800 dialog: a 192 px nav with search and two groups, a pane of titled groups whose rows put the control at the end (a System/Light/Dark icon picker, selects, switches). | `/settings` |

## The screen to get right

The chat. Everything Claude does to make a model feel calm happens there: the reply is set in a serif at reading size on a 768 px measure, the user's words sit in a faint bubble at the right edge, the reasoning folds into one muted line, and the controls (copy, rating, retry) stay hidden until the pointer reaches the turn. The composer is the only raised object on the page, a 20 px card with a hairline ring that darkens on focus, and the one colour in the whole view is the clay of the send button. self-learn's tutor on `/learn/<concept>` has to read the same way: a serif voice for the tutor, a sans for the interface, one docked composer, and nothing coloured except the action that sends.
