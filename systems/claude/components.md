# Claude components

The discovery list of every page and state captured, then one entry per component with crops of the real product, the shared values, the icon index and the Gaps. Captured from claude.ai on 2026-10-04 and refreshed on 2026-10-17, signed in, as static copies of each page state rendered in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the rendered copy in both themes. Nothing was sent, created or deleted in the account: a line was typed into the composer and deleted, menus and dialogs were opened and closed (the delete confirmation with Escape, Create a project with Cancel), a checkbox was ticked in Select mode and the mode left, and the sidebar was shown for the captures and hidden again.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (157 components, 662 states). The page layouts are described in [raw/pages.md](raw/pages.md).

How to read an entry:

- Values are written as tokens: a colour, shadow, radius, padding, type style, icon size, opacity, duration or easing reads as the token in [tokens.json](tokens.json) that holds it in that theme, then the measured value in brackets, for example `` `text.primary` (#f0efec) ``. Where several tokens hold the value, the one the element's own utility classes name wins (`bg-fill-danger` is `fill.danger`), then a role that fits the property (text and on for text, fill and surface for backgrounds, border for edges). A focus ring drawn on another surface reads `` `shadow.focus on this surface` ``, and a hairline ring names its colour as a border. A height is named by the control-height, size or layout token that holds it; a width only when a layout width token holds it or the box is square, and otherwise it is the instance's content width, written raw and not counted below. A colour with zero alpha reads `transparent`. A value no token holds is written raw: a few line heights (14/21), odd paddings and some drop shadows inside components. Of the 2566 values written in the state rows and child-layer lines below (zeros and content widths aside), 2307 (90%) name a token.
- Text is written as its typography token, then family size/line-height weight in brackets, then its colour, for example `` `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) ``, and is read from the first text node inside the component. A glyph from the icon font reads `Anthropicons` with its icon size step and weight.
- Dark states come first (every page was captured dark), then the same states read in light. Each theme's first row lists every value; later rows of that theme list only what changes. A state with the same values as its theme's first is named in that label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do: a cds Button paints its fill on an inner span, so its hover shows there.
- Crops are images of the component from the rendered copy, in [components/crops/](components/crops) (644 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages at 2x, kept for the dark Artifacts and Chats pages; phone shots are `mobile-{page}-{theme}-{state}.png`, 390 x 844 at 2x. Every state exists in both themes.

| Surface | URL | Screenshots |
|---|---|---|
| Home (new chat). The greeting and the composer. Captured at rest, with the plus menu, the model menu, the account menu, a chat row's menu, the search dialog, a line typed in the composer, and with the sidebar hidden (the account's own setting); on 2026-10-17 also with the Search button's tooltip open. | `/new` | [chat-menu (dark)](screenshots/home-dark-chat-menu.png), [composer-typed (dark)](screenshots/home-dark-composer-typed.png), [model-menu (dark)](screenshots/home-dark-model-menu.png), [plus-menu (dark)](screenshots/home-dark-plus-menu.png), [search (dark)](screenshots/home-dark-search.png), [sidebar-collapsed (dark)](screenshots/home-dark-sidebar-collapsed.png), [tooltip (dark)](screenshots/home-dark-tooltip.png), [user-menu (dark)](screenshots/home-dark-user-menu.png), [default (dark)](screenshots/home-dark.png), [chat-menu (light)](screenshots/home-light-chat-menu.png), [composer-typed (light)](screenshots/home-light-composer-typed.png), [model-menu (light)](screenshots/home-light-model-menu.png), [plus-menu (light)](screenshots/home-light-plus-menu.png), [search (light)](screenshots/home-light-search.png), [sidebar-collapsed (light)](screenshots/home-light-sidebar-collapsed.png), [tooltip (light)](screenshots/home-light-tooltip.png), [user-menu (light)](screenshots/home-light-user-menu.png), [default (light)](screenshots/home-light.png) |
| A chat, one copy read at three scroll positions: the top (user message, Thought for 6s, the code block), the table (scroll 1150) and the follow-up (scroll 1780). | `/chat/<id>` | [followup (dark)](screenshots/thread-dark-followup.png), [table (dark)](screenshots/thread-dark-table.png), [default (dark)](screenshots/thread-dark.png), [followup (light)](screenshots/thread-light-followup.png), [table (light)](screenshots/thread-light-table.png), [default (light)](screenshots/thread-light.png) |
| Artifacts. Tabs, the notice card, Make something new, month groups of rows; also with the sidebar's More menu open. On 2026-10-17 the page had become a grid of cards, captured while loading (skeletons). | `/artifacts` | [full (dark)](screenshots/artifacts-dark-full.png), [loading (dark)](screenshots/artifacts-dark-loading.png), [more-menu (dark)](screenshots/artifacts-dark-more-menu.png), [default (dark)](screenshots/artifacts-dark.png), [loading (light)](screenshots/artifacts-light-loading.png), [more-menu (light)](screenshots/artifacts-light-more-menu.png), [default (light)](screenshots/artifacts-light.png) |
| Chats and tasks. The table of chats and tasks with their times; on 2026-10-17 also in Select mode with one row ticked, with the filter menu open, with a search that matches nothing, and with a chat's delete confirmation open. | `/chats` | [delete-confirm (dark)](screenshots/chats-dark-delete-confirm.png), [filter-menu (dark)](screenshots/chats-dark-filter-menu.png), [full (dark)](screenshots/chats-dark-full.png), [search-empty (dark)](screenshots/chats-dark-search-empty.png), [select (dark)](screenshots/chats-dark-select.png), [default (dark)](screenshots/chats-dark.png), [delete-confirm (light)](screenshots/chats-light-delete-confirm.png), [filter-menu (light)](screenshots/chats-light-filter-menu.png), [search-empty (light)](screenshots/chats-light-search-empty.png), [select (light)](screenshots/chats-light-select.png), [default (light)](screenshots/chats-light.png) |
| Projects. The two project cards; on 2026-10-17 also with the Create a project dialog open. | `/projects` | [create (dark)](screenshots/projects-dark-create.png), [default (dark)](screenshots/projects-dark.png), [create (light)](screenshots/projects-light-create.png), [default (light)](screenshots/projects-light.png) |
| A project page. | `/project/<id>` | [default (dark)](screenshots/project-dark.png), [default (light)](screenshots/project-light.png) |
| Settings dialog: the General pane; on 2026-10-17 also the Account pane (text fields, a text area, a disabled button, links) and the Capabilities pane (a disabled switch, inline links). | `/settings/general` | [account (dark)](screenshots/settings-dark-account.png), [capabilities (dark)](screenshots/settings-dark-capabilities.png), [general (dark)](screenshots/settings-dark-general.png), [account (light)](screenshots/settings-light-account.png), [capabilities (light)](screenshots/settings-light-capabilities.png), [general (light)](screenshots/settings-light-general.png) |
| Home at 390 wide, and the drawer. | `/new` | [drawer (dark)](screenshots/mobile-home-dark-drawer.png), [default (dark)](screenshots/mobile-home-dark.png), [drawer (light)](screenshots/mobile-home-light-drawer.png), [default (light)](screenshots/mobile-home-light.png) |
| The chat at 390 wide. | `/chat/<id>` | [default (dark)](screenshots/mobile-thread-dark.png), [default (light)](screenshots/mobile-thread-light.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Plus menu | home | the composer's + button | [home-dark-plus-menu](screenshots/home-dark-plus-menu.png), [plus-menu](#plus-menu) |
| Model menu | home | the model selector | [home-dark-model-menu](screenshots/home-dark-model-menu.png), [model-menu](#model-menu) |
| Account menu | home | the account row | [home-dark-user-menu](screenshots/home-dark-user-menu.png), [user-menu](#user-menu) |
| Chat row menu | home | a sidebar chat row's more button | [home-dark-chat-menu](screenshots/home-dark-chat-menu.png), [chat-menu](#chat-menu) |
| Search dialog | home | the sidebar's Search button | [home-dark-search](screenshots/home-dark-search.png), [search-dialog](#search-dialog) |
| Composer with text | home | a line typed, then deleted | [home-dark-composer-typed](screenshots/home-dark-composer-typed.png), [send-button](#send-button) |
| Sidebar hidden | home | the account's own state; the sidebar was shown for every other capture and hidden again after | [home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png), [sidebar-collapsed](#sidebar-collapsed) |
| More menu | Artifacts | the sidebar's More row | [artifacts-dark-more-menu](screenshots/artifacts-dark-more-menu.png), [more-menu](#more-menu) |
| Settings dialog | any page | Settings in the account menu; closed with Escape | [settings-dark-general](screenshots/settings-dark-general.png), [settings-dialog](#settings-dialog) |
| Tooltip | home | synthetic pointer events on the sidebar Search button (2026-10-17) | [home-dark-tooltip](screenshots/home-dark-tooltip.png), [tooltip](#tooltip) |
| Select mode | Chats | the Select button, then one row's checkbox; left with the exit button (2026-10-17) | [chats-dark-select](screenshots/chats-dark-select.png), [checkbox](#checkbox) |
| Filter menu | Chats | the header's filter button (2026-10-17) | [chats-dark-filter-menu](screenshots/chats-dark-filter-menu.png), [filter-menu](#filter-menu) |
| Empty search | Chats | the header's search button, then a word that matches nothing, cleared after (2026-10-17) | [chats-dark-search-empty](screenshots/chats-dark-search-empty.png), [empty-state](#empty-state) |
| Delete confirmation | Chats | a sidebar chat row's menu, Delete; dismissed with Escape (2026-10-17) | [chats-dark-delete-confirm](screenshots/chats-dark-delete-confirm.png), [confirm-dialog](#confirm-dialog) |
| Create a project | Projects | New project; closed with Cancel (2026-10-17) | [projects-dark-create](screenshots/projects-dark-create.png), [form-dialog](#form-dialog) |
| Loading | Artifacts | the snapshot taken 120 ms after clicking Artifacts in the sidebar (2026-10-17) | [artifacts-dark-loading](screenshots/artifacts-dark-loading.png), [skeleton](#skeleton) |
| Drawer sheet | home at 390 | the Show sidebar button; it could not be closed in the copy, so it was hidden by hand before the phone chat copy | [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png), [m-drawer](#m-drawer) |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** 8px (274), 6px (40), 7px (40), 12px (28), 9999px (26), 4px (14), 20px (12), 5px (12), 2px (12), 14px (6). Most of the interface is 8 (rows, icon buttons, menu items, list hover fills, the code block: the comfortable `--cds-radius`); 12 is cards, menus, dialogs and the user bubble (`rounded-card`, radius + 4); 7 and 6 are segmented tracks and their thumbs; 20 is the composer alone; 14 the Make something new tiles; 9999 avatars and switches.

**Hover.** Claude hovers with a translucent wash of the text colour. Dark: no change on the element (50), transparent to `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) (6), text `text.secondary` (#c3c2b7) to `fill.primary` (#ffffff) (3), text `text.muted` (#898781) to `text.primary` (#f0efec) (3), text `text.muted` (#898781) to `text.secondary` (#c3c2b7) (3), opacity 0 to 1 (1). Light: no change on the element (50), transparent to `frame.hover` (#f0efec) (4), text `text.secondary` (#52514e) to `text.primary` (#0b0b0b) (3), text `text.muted` (#898781) to `text.primary` (#0b0b0b) (3), text `text.muted` (#898781) to `text.secondary` (#52514e) (3), transparent to `alpha.1` (rgba(11, 11, 11, 0.05)) (2). The wash is `fill.ghost-hover` (`rgba(255, 255, 255, 0.075)` in dark, `rgba(11, 11, 11, 0.05)` in light) on buttons, menu items and list rows; sidebar rows use `frame.hover`, the same wash in dark and a solid `#f0efec` in light; a selected row is `frame.selected` (15% white, or `#edece8`). A cds Button paints that fill on its inner `.cds-btn-squish` span, so the button itself reads "no change".

**Focus.** Of 54 elements given a real keyboard focus in dark: the shadow.focus ring (or shadow.focus-danger), on the element or an inner layer (47), a 2px solid outline in `legacy.accent-100` (#5598e7), offset 2px (4), its own ring turns border.strong (the composer, a field that holds the caret) (1), nothing visible on the element or its first layers (1). In light: the shadow.focus ring (or shadow.focus-danger), on the element or an inner layer (47), a 2px solid outline in `legacy.accent-100` (#256abf), offset 2px (4), its own ring turns border.strong (the composer, a field that holds the caret) (1), nothing visible on the element or its first layers (1). The common ring is `shadow.focus`: a 1px inset of the page colour, a 1px `fill.accent` blue (`#2a78d6`) ring and a 6px blue glow, so focus reads as a blue outline with a halo. The composer's mic and voice buttons, the Thought for N s pill and the message actions use a 2px blue outline offset 2 instead. A row (sidebar row, Chats row, settings nav item) puts the ring on its inner link or button and the sidebar rows add the hover wash; a tab puts it on its inner button. The segmented controls (Chat/Cowork, the Theme picker) are radio groups whose checked radio takes the ring. Menu items take no ring: keyboard focus in a cds Menu is the same `fill.ghost-hover` wash as the pointer ([menu-item-keyboard](#menu-item-keyboard)). The one element that shows nothing is the search dialog's field row, whose focus is the caret in its text area. States named `refresh-focus-visible` were read on the 2026-10-17 copies for components whose 2026-10-04 copy had no focus reading.

**Motion.** 0.06s cubic-bezier(0.4, 0, 0.2, 1) (166), 0.2s ease (66), 0.2s cubic-bezier(0.4, 0, 0.2, 1) (22), 0.06s cubic-bezier(0.165, 0.84, 0.44, 1) (10), 0.06s ease (8). Buttons press on `duration.fast` (60 ms) and colour changes run 200 ms on the standard curve; the cds tokens name five durations (60, 120, 200, 300, 450 ms) and three curves (out, snap, overshoot), plus a `linear()` spring for button presses that DTCG cannot carry.

**Rings.** Claude draws hairlines as box-shadows, not borders: a 1px ring of `border.default` (10% ink) that sits outside the element in light (`--cds-ring-outer: 1px`) and inside it in dark (`--cds-ring-inner: 1px`). The composer, menus, dialogs and cards all carry it.

**Layout grid.** The sidebar is 288 wide on its own ground, the content column starts 8 further on and a 48 tall header runs over it. The home composer is 672 wide, the chat transcript 768, list pages a 960 column. On a phone the sidebar becomes a full-screen sheet. The numbers per page are in [raw/pages.md](raw/pages.md).

## Components

### Sidebar

The 288px sidebar every desktop page shares, on its own ground a step darker than the page in dark: a 44px title row (the serif "Claude" wordmark, Hide sidebar, Search), the Home/Code pills, New, Artifacts and More, then the Pinned and "Chats and tasks" sections whose rows lead with a 6px hollow ring, and the account row with the plan. Hiding it leaves one Show sidebar button in the corner.

#### Sidebar (expanded)

<a id="sidebar"></a>`sidebar`, on home-dark. aside.dframe-sidebar, 288 wide (--df-sidebar-width) and full height, on its own ground (--df-web-sidebar-bg: #111111 in dark, a step darker than the page; #fbfbf9 in light), with no rule between it and the content.

<img src="components/crops/sidebar-default.png" alt="Sidebar (expanded), default" height="120"> <img src="components/crops/sidebar-light.png" alt="Sidebar (expanded), light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.sidebar-width` (288) x 900; border R: `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)); background `frame.web-sidebar-bg` (#111111); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7); icon 68.33 x `density.icon` (20), `text.primary` (#f0efec) |
| light | size `layout.sidebar-width` (288) x 900; border R: `borderWidth.default` (1px) solid `border.default` (rgba(11, 11, 11, 0.1)); background `frame.web-sidebar-bg` (#fbfbf9); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e); icon 68.33 x `density.icon` (20), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--cds-shortcut-cap-ink`, `--df-hover`, `--df-nav-scrollbar-lane`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`.

#### Sidebar title row

<a id="sidebar-titlebar"></a>`sidebar-titlebar`, on home-dark. 44 tall: the "Claude" serif wordmark at the start, Hide sidebar and Search icon buttons at the end.

<img src="components/crops/sidebar-titlebar-default.png" alt="Sidebar title row, default" height="44"> <img src="components/crops/sidebar-titlebar-light.png" alt="Sidebar title row, light" height="44"> 

| State | Values |
|---|---|
| default | size 287 x `layout.sidebar-titlebar-height` (44); padding `space.1` (4px) `density.pad-sm` (8px) 0 `density.pad-sm` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7); icon 68.33 x `density.icon` (20), `text.primary` (#f0efec) |
| light | size 287 x `layout.sidebar-titlebar-height` (44); padding `space.1` (4px) `density.pad-sm` (8px) 0 `density.pad-sm` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e); icon 68.33 x `density.icon` (20), `text.primary` (#0b0b0b) |

Child layers: a 68.3x20

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Claude wordmark

<a id="sidebar-wordmark"></a>`sidebar-wordmark`, on home-dark. An inline SVG, 68x20, in the text colour.

<img src="components/crops/sidebar-wordmark-default.png" alt="Claude wordmark, default" height="24"> <img src="components/crops/sidebar-wordmark-hover.png" alt="Claude wordmark, hover" height="24"> <img src="components/crops/sidebar-wordmark-light.png" alt="Claude wordmark, light" height="24"> <img src="components/crops/sidebar-wordmark-light-hover.png" alt="Claude wordmark, light-hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size 68.33 x `density.h-control-nested--sm` (20); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 14/21 400, `text.primary` (#f0efec); icon 68.33 x `density.icon` (20), `text.primary` (#f0efec) |
| light (same: light-hover) | size 68.33 x `density.h-control-nested--sm` (20); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 14/21 400, `text.primary` (#0b0b0b); icon 68.33 x `density.icon` (20), `text.primary` (#0b0b0b) |

Child layers: a 68.3x20

#### Sidebar icon button (Hide sidebar)

<a id="sidebar-icon-button"></a>`sidebar-icon-button`, on home-dark. A cds Button, ghost, 32x32 with a 16px glyph from the Anthropicons icon font.

<img src="components/crops/sidebar-icon-button-default.png" alt="Sidebar icon button (Hide sidebar), default" height="32"> <img src="components/crops/sidebar-icon-button-hover.png" alt="Sidebar icon button (Hide sidebar), hover" height="32"> <img src="components/crops/sidebar-icon-button-light.png" alt="Sidebar icon button (Hide sidebar), light" height="32"> <img src="components/crops/sidebar-icon-button-light-hover.png" alt="Sidebar icon button (Hide sidebar), light-hover" height="32"> <img src="components/crops/sidebar-icon-button-focus-visible.png" alt="Sidebar icon button (Hide sidebar), focus-visible" height="32"> <img src="components/crops/sidebar-icon-button-light-focus-visible.png" alt="Sidebar icon button (Hide sidebar), light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7) |
| hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `on.accent` (#ffffff) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e) |
| light-hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Sidebar Search button

<a id="sidebar-search-button"></a>`sidebar-search-button`, on home-dark, home-dark-tooltip.

<img src="components/crops/sidebar-search-button-default.png" alt="Sidebar Search button, default" height="32"> <img src="components/crops/sidebar-search-button-hover.png" alt="Sidebar Search button, hover" height="32"> <img src="components/crops/sidebar-search-button-light.png" alt="Sidebar Search button, light" height="32"> <img src="components/crops/sidebar-search-button-light-hover.png" alt="Sidebar Search button, light-hover" height="32"> <img src="components/crops/sidebar-search-button-light-refresh.png" alt="Sidebar Search button, light-refresh" height="32"> <img src="components/crops/sidebar-search-button-light-refresh-focus-visible.png" alt="Sidebar Search button, light-refresh-focus-visible" height="32"> <img src="components/crops/sidebar-search-button-refresh.png" alt="Sidebar Search button, refresh" height="32"> <img src="components/crops/sidebar-search-button-refresh-focus-visible.png" alt="Sidebar Search button, refresh-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: refresh) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7) |
| hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `on.accent` (#ffffff) |
| refresh-focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-refresh) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e) |
| light-hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b) |
| light-refresh-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Home/Code segmented control

<a id="mode-pills"></a>`mode-pills`, on home-dark. Two pills (Home, Code) in a track the full width of the sidebar; a sliding indicator sits under the active one.

<img src="components/crops/mode-pills-default.png" alt="Home/Code segmented control, default" height="32"> <img src="components/crops/mode-pills-light.png" alt="Home/Code segmented control, light" height="32"> 

| State | Values |
|---|---|
| default | size 271 x `density.h-control` (32); padding 1px; radius `radius.row` (8px); background rgba(255, 255, 255, 0.06); text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#f0efec) |
| light | size 271 x `density.h-control` (32); padding 1px; radius `radius.row` (8px); background `frame.selected` (#edece8); text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#0b0b0b) |

#### Mode pill

<a id="mode-pill"></a>`mode-pill`, on home-dark.

<img src="components/crops/mode-pill-default.png" alt="Mode pill, default" height="30"> <img src="components/crops/mode-pill-hover.png" alt="Mode pill, hover" height="30"> <img src="components/crops/mode-pill-light.png" alt="Mode pill, light" height="30"> <img src="components/crops/mode-pill-light-hover.png" alt="Mode pill, light-hover" height="30"> <img src="components/crops/mode-pill-active.png" alt="Mode pill, active" height="30"> <img src="components/crops/mode-pill-focus-visible.png" alt="Mode pill, focus-visible" height="30"> <img src="components/crops/mode-pill-light-active.png" alt="Mode pill, light-active" height="30"> <img src="components/crops/mode-pill-light-focus-visible.png" alt="Mode pill, light-focus-visible" height="30"> 

| State | Values |
|---|---|
| default | size 132.89 x `size.mode-pill-height` (30); padding 0 `space.1` (4px); radius `radius.segment-thumb` (6px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.muted` (#898781); transition box-shadow `duration.fast` (0.06s) ease |
| hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#f0efec) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#f0efec) |
| active | size 136.11 x `size.mode-pill-height` (30); text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#f0efec) |
| light | size 132.89 x `size.mode-pill-height` (30); padding 0 `space.1` (4px); radius `radius.segment-thumb` (6px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.muted` (#898781); transition box-shadow `duration.fast` (0.06s) ease |
| light-hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b) |
| light-active | size 136.11 x `size.mode-pill-height` (30); text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#0b0b0b) |

Child layers: button 132.9x30 radius `radius.segment-thumb` (6px)

#### Mode pill indicator

<a id="mode-pill-indicator"></a>`mode-pill-indicator`, on home-dark.

<img src="components/crops/mode-pill-indicator-default.png" alt="Mode pill indicator, default" height="30"> <img src="components/crops/mode-pill-indicator-light.png" alt="Mode pill indicator, light" height="30"> 

| State | Values |
|---|---|
| default | size 136 x `size.mode-pill-height` (30); radius `radius.segment-track` (7px); background `fill.control` (rgba(255, 255, 255, 0.1)); shadow `component.mode-pill-indicator-shadow` (rgba(255, 255, 255, 0.08) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.3) 0px 1px 2px 0px, rgba(0, 0, 0, 0.25) 0px 2px 6px -1px); transition background-color `duration.sheet` (0.3s) `easing.snap` (cubic-bezier(0.32, 0.72, 0, 1)); transform translate(1px, 0px) |
| light | size 136 x `size.mode-pill-height` (30); radius `radius.segment-track` (7px); background `surface.0` (#f9f9f7); shadow `component.mode-pill-indicator-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.05) 0px 2px 6px -1px); transition background-color `duration.sheet` (0.3s) `easing.snap` (cubic-bezier(0.32, 0.72, 0, 1)); transform translate(1px, 0px) |

#### New row

<a id="nav-new-row"></a>`nav-new-row`, on home-dark. The first nav row: a 22px circle with a plus, "New", the ⇧⌘O shortcut, and a Quick task button at the end.

<img src="components/crops/nav-new-row-default.png" alt="New row, default" height="32"> <img src="components/crops/nav-new-row-hover.png" alt="New row, hover" height="32"> <img src="components/crops/nav-new-row-light.png" alt="New row, light" height="32"> <img src="components/crops/nav-new-row-light-hover.png" alt="New row, light-hover" height="32"> <img src="components/crops/nav-new-row-focus-visible.png" alt="New row, focus-visible" height="32"> <img src="components/crops/nav-new-row-light-focus-visible.png" alt="New row, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 271 x `density.h-control` (32); padding 0 0 0 `space.0-5` (2px); radius `radius.row` (8px); background `fill.ghost-selected` (rgba(255, 255, 255, 0.15)); text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#f0efec) |
| focus-visible | focus ring on the inner a: `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| light (same: light-hover) | size 271 x `density.h-control` (32); padding 0 0 0 `space.0-5` (2px); radius `radius.row` (8px); background `frame.selected` (#edece8); text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#0b0b0b) |
| light-focus-visible | focus ring on the inner a: `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--cds-shortcut-cap-ink`, `--df-hover`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`.

#### New row circle

<a id="nav-new-circle"></a>`nav-new-circle`, on home-dark.

<img src="components/crops/nav-new-circle-default.png" alt="New row circle, default" height="24"> <img src="components/crops/nav-new-circle-hover.png" alt="New row circle, hover" height="24"> <img src="components/crops/nav-new-circle-light.png" alt="New row circle, light" height="24"> <img src="components/crops/nav-new-circle-light-hover.png" alt="New row circle, light-hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control-nested` (22) x `density.h-control-nested` (22); radius `radius.full` (9999px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#f0efec) |
| light (same: light-hover) | size `density.h-control-nested` (22) x `density.h-control-nested` (22); radius `radius.full` (9999px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 700), `text.primary` (#0b0b0b) |

#### Shortcut hint

<a id="nav-shortcut"></a>`nav-shortcut`, on home-dark. cds Shortcut, text variant: each key a <kbd> in caption size; held at opacity 0 until its row is hovered.

<img src="components/crops/nav-shortcut-default.png" alt="Shortcut hint, default" height="24"> <img src="components/crops/nav-shortcut-hover.png" alt="Shortcut hint, hover" height="24"> <img src="components/crops/nav-shortcut-light.png" alt="Shortcut hint, light" height="24"> <img src="components/crops/nav-shortcut-light-hover.png" alt="Shortcut hint, light-hover" height="24"> 

| State | Values |
|---|---|
| default | size 39.78 x 12; background transparent; text Anthropic Sans 12/12 400, `text.muted` (#898781); opacity 0 |
| hover | opacity 1 |
| light | size 39.8 x 12; background transparent; text Anthropic Sans 12/12 400, `text.muted` (#898781); opacity 0 |
| light-hover | opacity 1 |

Tokens named in its classes: `--cds-shortcut-cap-ink`, `--df-radius-pill`.

#### Nav row (Artifacts)

<a id="nav-row"></a>`nav-row`, on home-dark. 32 tall (--df-row-h), radius 8 (--df-radius-pill), a 20px glyph in a 28px leading slot, 14px text in text-secondary; hover fills --df-hover.

<img src="components/crops/nav-row-default.png" alt="Nav row (Artifacts), default" height="32"> <img src="components/crops/nav-row-hover.png" alt="Nav row (Artifacts), hover" height="32"> <img src="components/crops/nav-row-light.png" alt="Nav row (Artifacts), light" height="32"> <img src="components/crops/nav-row-light-hover.png" alt="Nav row (Artifacts), light-hover" height="32"> <img src="components/crops/nav-row-focus-visible.png" alt="Nav row (Artifacts), focus-visible" height="32"> <img src="components/crops/nav-row-light-focus-visible.png" alt="Nav row (Artifacts), light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size 271 x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#c3c2b7) |
| hover | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| focus-visible | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); focus ring on the inner a: `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| light | size 271 x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#52514e) |
| light-hover | background `frame.hover` (#f0efec) |
| light-focus-visible | background `frame.hover` (#f0efec); focus ring on the inner a: `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |

Child layers: a 271x32 radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--df-hover`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`.

#### More row

<a id="nav-row-more"></a>`nav-row-more`, on home-dark, artifacts-dark-more-menu.

<img src="components/crops/nav-row-more-default.png" alt="More row, default" height="32"> <img src="components/crops/nav-row-more-hover.png" alt="More row, hover" height="32"> <img src="components/crops/nav-row-more-light.png" alt="More row, light" height="32"> <img src="components/crops/nav-row-more-light-hover.png" alt="More row, light-hover" height="32"> <img src="components/crops/nav-row-more-open.png" alt="More row, open" height="32"> <img src="components/crops/nav-row-more-focus-visible.png" alt="More row, focus-visible" height="32"> <img src="components/crops/nav-row-more-light-focus-visible.png" alt="More row, light-focus-visible" height="32"> <img src="components/crops/nav-row-more-light-open.png" alt="More row, light-open" height="32"> 

| State | Values |
|---|---|
| default | size 271 x `density.h-control` (32); padding 0 `space.0-5` (2px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#c3c2b7) |
| hover | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| focus-visible | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); shadow `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| open | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| light | size 271 x `density.h-control` (32); padding 0 `space.0-5` (2px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#52514e) |
| light-hover | background `frame.hover` (#f0efec) |
| light-focus-visible | background `frame.hover` (#f0efec); shadow `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| light-open | background `frame.hover` (#f0efec) |

Child layers: button 271x32 radius `radius.row` (8px)

Tokens named in its classes: `--cds-fill-accent`, `--df-hover`, `--df-radius-pill`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`.

#### Section label (Pinned)

<a id="section-label"></a>`section-label`, on home-dark. Caption-size text in text-muted with a caret that shows on hover.

<img src="components/crops/section-label-default.png" alt="Section label (Pinned), default" height="24"> <img src="components/crops/section-label-hover.png" alt="Section label (Pinned), hover" height="24"> <img src="components/crops/section-label-light.png" alt="Section label (Pinned), light" height="24"> <img src="components/crops/section-label-light-hover.png" alt="Section label (Pinned), light-hover" height="24"> <img src="components/crops/section-label-focus-visible.png" alt="Section label (Pinned), focus-visible" height="24"> <img src="components/crops/section-label-light-focus-visible.png" alt="Section label (Pinned), light-focus-visible" height="24"> 

| State | Values |
|---|---|
| default | size 265 x `density.h-control--xs` (24); padding `space.1` (4px) 0 `space.1` (4px) `space.1` (4px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 13/16 400, `text.muted` (#898781) |
| hover | text Anthropic Sans 13/16 400, `text.secondary` (#c3c2b7) |
| focus-visible | shadow `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| light | size 265 x `density.h-control--xs` (24); padding `space.1` (4px) 0 `space.1` (4px) `space.1` (4px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 13/16 400, `text.muted` (#898781) |
| light-hover | text Anthropic Sans 13/16 400, `text.secondary` (#52514e) |
| light-focus-visible | shadow `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |

Child layers: button 265x24 radius `radius.row` (8px)

Tokens named in its classes: `--cds-fill-accent`, `--df-radius-pill`.

#### Section action button (View all)

<a id="section-action"></a>`section-action`, on home-dark, home-dark-tooltip. Revealed when its section label row is hovered, or when it takes keyboard focus.

<img src="components/crops/section-action-default.png" alt="Section action button (View all), default" height="24"> <img src="components/crops/section-action-hover.png" alt="Section action button (View all), hover" height="24"> <img src="components/crops/section-action-light.png" alt="Section action button (View all), light" height="24"> <img src="components/crops/section-action-light-hover.png" alt="Section action button (View all), light-hover" height="24"> <img src="components/crops/section-action-light-refresh.png" alt="Section action button (View all), light-refresh" height="24"> <img src="components/crops/section-action-light-refresh-focus-visible.png" alt="Section action button (View all), light-refresh-focus-visible" height="24"> <img src="components/crops/section-action-refresh.png" alt="Section action button (View all), refresh" height="24"> <img src="components/crops/section-action-refresh-focus-visible.png" alt="Section action button (View all), refresh-focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover, refresh) | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7); opacity 0 |
| refresh-focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease; opacity 1 |
| light (same: light-hover, light-refresh) | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e); opacity 0 |
| light-refresh-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease; opacity 1 |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Chat row

<a id="chat-row"></a>`chat-row`, on home-dark, home-dark-tooltip, thread-dark. A 6px hollow ring as the bullet (role=img "Idle"), the title faded at the end (.dframe-fade-label, a mask, not an ellipsis), a more button on hover.

<img src="components/crops/chat-row-default.png" alt="Chat row, default" height="32"> <img src="components/crops/chat-row-hover.png" alt="Chat row, hover" height="32"> <img src="components/crops/chat-row-light.png" alt="Chat row, light" height="32"> <img src="components/crops/chat-row-light-hover.png" alt="Chat row, light-hover" height="32"> <img src="components/crops/chat-row-selected.png" alt="Chat row, selected" height="32"> <img src="components/crops/chat-row-pinned.png" alt="Chat row, pinned" height="32"> <img src="components/crops/chat-row-light-pinned.png" alt="Chat row, light-pinned" height="32"> <img src="components/crops/chat-row-light-refresh.png" alt="Chat row, light-refresh" height="32"> <img src="components/crops/chat-row-light-refresh-focus-visible.png" alt="Chat row, light-refresh-focus-visible" height="32"> <img src="components/crops/chat-row-light-selected.png" alt="Chat row, light-selected" height="32"> <img src="components/crops/chat-row-refresh.png" alt="Chat row, refresh" height="32"> <img src="components/crops/chat-row-refresh-focus-visible.png" alt="Chat row, refresh-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: refresh, pinned) | size 271 x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropic Sans 14/21 400, `text.secondary` (#c3c2b7) |
| hover | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| refresh-focus-visible | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); focus ring on the inner a: `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| selected | background `fill.ghost-selected` (rgba(255, 255, 255, 0.15)); text Anthropic Sans 14/21 400, `text.primary` (#f0efec) |
| light (same: light-refresh, light-pinned) | size 271 x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropic Sans 14/21 400, `text.secondary` (#52514e) |
| light-hover | background `frame.hover` (#f0efec) |
| light-refresh-focus-visible | background `frame.hover` (#f0efec); focus ring on the inner a: `component.sidebar-row-focus` (#2a78d6 0px 0px 0px 1px inset, rgba(42, 120, 214, 0.2) 0px 0px 6px 0px) |
| light-selected | background `frame.selected` (#edece8); text Anthropic Sans 14/21 400, `text.primary` (#0b0b0b) |

Child layers: a 271x32 radius `radius.row` (8px); span 6x6 border `borderWidth.default` (1px) solid `text.muted` (#898781) radius `radius.full` (9999px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--df-hover`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-indent`, `--df-row-px`, `--df-selected`.

#### Chat row bullet

<a id="chat-row-bullet"></a>`chat-row-bullet`, on home-dark.

<img src="components/crops/chat-row-bullet-default.png" alt="Chat row bullet, default" height="24"> <img src="components/crops/chat-row-bullet-light.png" alt="Chat row bullet, light" height="24"> 

| State | Values |
|---|---|
| default | size `size.chat-bullet` (6) x `size.chat-bullet` (6); border `borderWidth.default` (1px) solid `text.muted` (#898781); radius `radius.full` (9999px); background transparent; opacity 0.5 |
| light | size `size.chat-bullet` (6) x `size.chat-bullet` (6); border `borderWidth.default` (1px) solid `text.muted` (#898781); radius `radius.full` (9999px); background transparent; opacity 0.5 |

#### Chat row more button

<a id="chat-row-more"></a>`chat-row-more`, on home-dark, home-dark-tooltip, home-dark-chat-menu.

<img src="components/crops/chat-row-more-default.png" alt="Chat row more button, default" height="24"> <img src="components/crops/chat-row-more-hover.png" alt="Chat row more button, hover" height="24"> <img src="components/crops/chat-row-more-light.png" alt="Chat row more button, light" height="24"> <img src="components/crops/chat-row-more-light-hover.png" alt="Chat row more button, light-hover" height="24"> <img src="components/crops/chat-row-more-open.png" alt="Chat row more button, open" height="24"> <img src="components/crops/chat-row-more-light-open.png" alt="Chat row more button, light-open" height="24"> <img src="components/crops/chat-row-more-light-refresh.png" alt="Chat row more button, light-refresh" height="24"> <img src="components/crops/chat-row-more-light-refresh-focus-visible.png" alt="Chat row more button, light-refresh-focus-visible" height="24"> <img src="components/crops/chat-row-more-refresh.png" alt="Chat row more button, refresh" height="24"> <img src="components/crops/chat-row-more-refresh-focus-visible.png" alt="Chat row more button, refresh-focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover, refresh) | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| refresh-focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| open | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#f0efec) |
| light (same: light-hover, light-refresh) | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-refresh-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-open | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--df-row-ctl`.

#### Account row

<a id="account-row"></a>`account-row`, on home-dark, home-dark-user-menu. Avatar, name, a dot and the plan ("Max") in text-muted, a chevron.

<img src="components/crops/account-row-default.png" alt="Account row, default" height="32"> <img src="components/crops/account-row-hover.png" alt="Account row, hover" height="32"> <img src="components/crops/account-row-light.png" alt="Account row, light" height="32"> <img src="components/crops/account-row-light-hover.png" alt="Account row, light-hover" height="32"> <img src="components/crops/account-row-open.png" alt="Account row, open" height="32"> <img src="components/crops/account-row-focus-visible.png" alt="Account row, focus-visible" height="32"> <img src="components/crops/account-row-light-focus-visible.png" alt="Account row, light-focus-visible" height="32"> <img src="components/crops/account-row-light-open.png" alt="Account row, light-open" height="32"> 

| State | Values |
|---|---|
| default (same: open) | size 164.11 x `density.h-control` (32); padding 0 `density.pad-sm` (8px) 0 `space.0-5` (2px); radius `radius.row` (8px); background transparent; text Anthropic Sans 14/21 400, `text.secondary` (#c3c2b7) |
| hover | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-open) | size 164.84 x `density.h-control` (32); padding 0 `density.pad-sm` (8px) 0 `space.0-5` (2px); radius `radius.row` (8px); background transparent; text Anthropic Sans 14/21 400, `text.secondary` (#52514e) |
| light-hover | background `frame.hover` (#f0efec) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Child layers: span 24x24 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.full` (9999px)

Tokens named in its classes: `--cds-avatar-sm`, `--cds-rem-scale`, `--df-footer-btn-size`, `--df-hover`, `--df-leading-slot`, `--df-radius-pill`, `--df-row-font`, `--df-row-gap`, `--df-row-px`.

#### Avatar

<a id="account-avatar"></a>`account-avatar`, on home-dark.

<img src="components/crops/account-avatar-default.png" alt="Avatar, default" height="24"> <img src="components/crops/account-avatar-light.png" alt="Avatar, light" height="24"> 

| State | Values |
|---|---|
| default | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.full` (9999px); background `fill.control` (rgba(255, 255, 255, 0.1)) |
| light | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.full` (9999px); background `fill.control` (rgba(11, 11, 11, 0.1)) |

Tokens named in its classes: `--cds-avatar-sm`, `--cds-rem-scale`.

#### Plan label

<a id="account-plan"></a>`account-plan`, on home-dark.

<img src="components/crops/account-plan-default.png" alt="Plan label, default" height="24"> <img src="components/crops/account-plan-light.png" alt="Plan label, light" height="24"> 

| State | Values |
|---|---|
| default | size 24.42 x `density.h-control-nested--xs` (18); background transparent; text Anthropic Sans 12/18 400, `text.muted` (#898781) |
| light | size 24.69 x `density.h-control-nested--xs` (18); background transparent; text Anthropic Sans 12/18 400, `text.muted` (#898781) |

#### Get apps button

<a id="footer-apps-button"></a>`footer-apps-button`, on home-dark.

<img src="components/crops/footer-apps-button-default.png" alt="Get apps button, default" height="32"> <img src="components/crops/footer-apps-button-hover.png" alt="Get apps button, hover" height="32"> <img src="components/crops/footer-apps-button-light.png" alt="Get apps button, light" height="32"> <img src="components/crops/footer-apps-button-light-hover.png" alt="Get apps button, light-hover" height="32"> <img src="components/crops/footer-apps-button-focus-visible.png" alt="Get apps button, focus-visible" height="32"> <img src="components/crops/footer-apps-button-light-focus-visible.png" alt="Get apps button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7) |
| hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `on.accent` (#ffffff) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e) |
| light-hover | text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Sidebar resize handle

<a id="resize-handle"></a>`resize-handle`, on home-dark.

| State | Values |
|---|---|
| default (same: hover) | size 12 x 900; background transparent; text Anthropic Sans 14/21 400, `text.primary` (#f0efec) |
| light (same: light-hover) | size 12 x 900; background transparent; text Anthropic Sans 14/21 400, `text.primary` (#0b0b0b) |

Child layers: div 3x48 background `text.muted` (#898781) radius `radius.full` (9999px)

Tokens named in its classes: `--cds-resize-pill-force`, `--cds-ring-inner`, `--cds-ring-outer`.

#### Sidebar hidden (the show button)

<a id="sidebar-collapsed"></a>`sidebar-collapsed`, on home-dark-sidebar-collapsed. Hidden, the sidebar leaves only a 32x32 box at 8,8 holding the Show sidebar button; the content pane takes the full width.

<img src="components/crops/sidebar-collapsed-default.png" alt="Sidebar hidden (the show button), default" height="32"> <img src="components/crops/sidebar-collapsed-light.png" alt="Sidebar hidden (the show button), light" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7) |
| light | size `density.h-control` (32) x `density.h-control` (32); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e) |

Child layers: div 288x900 background `surface.3` (#20201f) border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)) shadow `frame.shadow-pop` (rgba(255, 255, 255, 0.08) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.4) 0px 4px 12px 0px, rgba(0, 0, 0, 0.5) 0px 16px 40px 0px); div 270x32 background rgba(255, 255, 255, 0.06) radius `radius.row` (8px); div 136x30 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-track` (7px) shadow `component.mode-pill-indicator-shadow` (rgba(255, 255, 255, 0.08) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.3) 0px 1px 2px 0px, rgba(0, 0, 0, 0.25) 0px 2px 6px -1px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--cds-shortcut-cap-ink`, `--df-hover`, `--df-nav-scrollbar-lane`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`, `--df-surface-primary`.

#### Show sidebar button

<a id="sidebar-show-button"></a>`sidebar-show-button`, on home-dark-sidebar-collapsed.

<img src="components/crops/sidebar-show-button-default.png" alt="Show sidebar button, default" height="24"> <img src="components/crops/sidebar-show-button-hover.png" alt="Show sidebar button, hover" height="24"> <img src="components/crops/sidebar-show-button-light.png" alt="Show sidebar button, light" height="24"> <img src="components/crops/sidebar-show-button-light-hover.png" alt="Show sidebar button, light-hover" height="24"> <img src="components/crops/sidebar-show-button-focus-visible.png" alt="Show sidebar button, focus-visible" height="24"> <img src="components/crops/sidebar-show-button-light-focus-visible.png" alt="Show sidebar button, light-focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control--xs` (24) x `density.h-control--xs` (24); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

### Header

The 48px row over the content column: empty on the home page but for Use incognito; on a chat, the title button with its more menu, and Share.

#### Content pane header

<a id="pane-header"></a>`pane-header`, on home-dark. 48 tall (--df-header-h) across the content pane.

<img src="components/crops/pane-header-default.png" alt="Content pane header, default" height="48"> <img src="components/crops/pane-header-light.png" alt="Content pane header, light" height="48"> 

| State | Values |
|---|---|
| default | size 1136 x `layout.header-height` (48); background transparent; icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec) |
| light | size 1136 x `layout.header-height` (48); background transparent; icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Content pane

<a id="pane"></a>`pane`, on home-dark. The content column: it starts 8px past the sidebar and paints nothing itself, so the page shows the app ground (surface-1).

<img src="components/crops/pane-default.png" alt="Content pane, default" height="120"> <img src="components/crops/pane-light.png" alt="Content pane, light" height="120"> 

| State | Values |
|---|---|
| default | size 1136 x 900; background transparent; text `typography.display` (Anthropic Serif 38/47.5 300), `text.primary` (#f0efec); transition filter `duration.snap` (0.12s) ease-out; icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec); placeholder `text.muted` (#898781) |
| light | size 1136 x 900; background transparent; text Anthropic Serif 38/47.5 330, `text.primary` (#0b0b0b); transition filter `duration.snap` (0.12s) ease-out; icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b); placeholder `text.muted` (#898781) |

Child layers: div 672x120 background `surface.3` (#20201f) border `borderWidth.default` (1px) solid transparent radius `radius.composer` (20px) shadow `component.composer-shadow` (rgba(0, 0, 0, 0.04) 0px 4px 20px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset); div 119.2x28 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius `radius.segment-track` (7px); div 49.5x26 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-thumb` (6px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)) + `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--app-visual-viewport-height`, `--band-slot-lift`, `--cds-cursor-interactive`, `--cds-h-control--xs`, `--cds-page-bg`, `--chorus-composer-lift`, `--new-page-card-px`, `--organization-banner-column-height`, `--prerender-activation-viewport-height`.

#### Incognito button

<a id="incognito-button"></a>`incognito-button`, on home-dark.

<img src="components/crops/incognito-button-default.png" alt="Incognito button, default" height="32"> <img src="components/crops/incognito-button-hover.png" alt="Incognito button, hover" height="32"> <img src="components/crops/incognito-button-light.png" alt="Incognito button, light" height="32"> <img src="components/crops/incognito-button-light-hover.png" alt="Incognito button, light-hover" height="32"> <img src="components/crops/incognito-button-focus-visible.png" alt="Incognito button, focus-visible" height="32"> <img src="components/crops/incognito-button-light-focus-visible.png" alt="Incognito button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Chat title button

<a id="chat-title-button"></a>`chat-title-button`, on thread-dark.

<img src="components/crops/chat-title-button-default.png" alt="Chat title button, default" height="28"> <img src="components/crops/chat-title-button-hover.png" alt="Chat title button, hover" height="28"> <img src="components/crops/chat-title-button-light.png" alt="Chat title button, light" height="28"> <img src="components/crops/chat-title-button-light-hover.png" alt="Chat title button, light-hover" height="28"> <img src="components/crops/chat-title-button-focus-visible.png" alt="Chat title button, focus-visible" height="28"> <img src="components/crops/chat-title-button-light-focus-visible.png" alt="Chat title button, light-focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size 117.97 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size 118.77 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-page-bg`.

#### Chat title more button

<a id="chat-title-more"></a>`chat-title-more`, on thread-dark.

<img src="components/crops/chat-title-more-default.png" alt="Chat title more button, default" height="28"> <img src="components/crops/chat-title-more-hover.png" alt="Chat title more button, hover" height="28"> <img src="components/crops/chat-title-more-light.png" alt="Chat title more button, light" height="28"> <img src="components/crops/chat-title-more-light-hover.png" alt="Chat title more button, light-hover" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control--sm` (28) x `density.h-control--sm` (28); radius `radius.segment-track` (7px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light (same: light-hover) | size `density.h-control--sm` (28) x `density.h-control--sm` (28); radius `radius.segment-track` (7px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Share button

<a id="share-button"></a>`share-button`, on thread-dark.

<img src="components/crops/share-button-default.png" alt="Share button, default" height="28"> <img src="components/crops/share-button-hover.png" alt="Share button, hover" height="28"> <img src="components/crops/share-button-light.png" alt="Share button, light" height="28"> <img src="components/crops/share-button-light-hover.png" alt="Share button, light-hover" height="28"> <img src="components/crops/share-button-focus-visible.png" alt="Share button, focus-visible" height="28"> <img src="components/crops/share-button-light-focus-visible.png" alt="Share button, light-focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size 57.66 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size 58 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Child layers: span 57.7x28 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-track` (7px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

### Home and composer

The new-chat page: the serif greeting led by the clay asterisk, and the composer, the same card on the home page, in a chat and on a project page: a 20px-radius card on surface-3 with a ring, the editor, then +, the Chat/Cowork segments, the model selector (model and effort), dictation and voice. Typing swaps voice for the clay send button.

#### Home greeting

<a id="greeting"></a>`greeting`, on home-dark. Anthropic Serif at the display size (`.font-display`: 2.375rem, weight 300 with the "opsz" 48 axis in dark), the orange asterisk mark first.

<img src="components/crops/greeting-default.png" alt="Home greeting, default" height="48"> <img src="components/crops/greeting-light.png" alt="Home greeting, light" height="48"> 

| State | Values |
|---|---|
| default | size 302.97 x 47.5; background transparent; text `typography.display` (Anthropic Serif 38/47.5 300), `text.primary` (#f0efec); icon 36.47 x 36.47, `text.primary` (#f0efec) |
| light | size 305.11 x 47.5; background transparent; text Anthropic Serif 38/47.5 330, `text.primary` (#0b0b0b); icon 36.47 x 36.47, `text.primary` (#0b0b0b) |

#### Greeting mark (the asterisk)

<a id="greeting-mark"></a>`greeting-mark`, on home-dark.

<img src="components/crops/greeting-mark-default.png" alt="Greeting mark (the asterisk), default" height="36"> <img src="components/crops/greeting-mark-light.png" alt="Greeting mark (the asterisk), light" height="36"> 

| State | Values |
|---|---|
| default | size 36.47 x 36.47; background transparent; icon 36.47 x 36.47, `text.primary` (#f0efec) |
| light | size 36.47 x 36.47; background transparent; icon 36.47 x 36.47, `text.primary` (#0b0b0b) |

#### Composer

<a id="composer"></a>`composer`, on home-dark, home-dark-composer-typed, thread-dark, project-dark. A card on surface-3 with radius 20 (rounded-[20px]; 12 at compact), a 1px ring of --cds-border (border-strong on focus) and a soft 4/20 drop (shadow-composer); the editor (Tiptap) above a 32px tool row.

<img src="components/crops/composer-default.png" alt="Composer, default" height="120"> <img src="components/crops/composer-light.png" alt="Composer, light" height="120"> <img src="components/crops/composer-typed.png" alt="Composer, typed" height="120"> <img src="components/crops/composer-thread.png" alt="Composer, thread" height="100"> <img src="components/crops/composer-focus-visible.png" alt="Composer, focus-visible" height="120"> <img src="components/crops/composer-light-focus-visible.png" alt="Composer, light-focus-visible" height="120"> <img src="components/crops/composer-light-project.png" alt="Composer, light-project" height="120"> <img src="components/crops/composer-light-thread.png" alt="Composer, light-thread" height="100"> <img src="components/crops/composer-light-typed.png" alt="Composer, light-typed" height="120"> <img src="components/crops/composer-project.png" alt="Composer, project" height="120"> 

| State | Values |
|---|---|
| default | size `layout.search-dialog-width` (672) x 120; border `borderWidth.default` (1px) solid transparent; radius `radius.composer` (20px); background `surface.3` (#20201f); shadow `component.composer-shadow` (rgba(0, 0, 0, 0.04) 0px 4px 20px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.muted` (#898781); transition background-color and 3 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec); placeholder `text.muted` (#898781) |
| focus-visible | shadow `component.composer-shadow-focus` (rgba(0, 0, 0, 0.07) 0px 4px 20px 0px, rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset) |
| typed | text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| thread | size `layout.transcript-width` (768) x 100; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| project | size 680 x 120 |
| light | size `layout.search-dialog-width` (672) x 120; border `borderWidth.default` (1px) solid transparent; radius `radius.composer` (20px); background `surface.3` (#ffffff); shadow `component.composer-shadow` (rgba(0, 0, 0, 0.04) 0px 4px 20px 0px, rgba(11, 11, 11, 0.1) 0px 0px 0px 1px); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.muted` (#898781); transition background-color and 3 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b); placeholder `text.muted` (#898781) |
| light-focus-visible | shadow `component.composer-shadow-focus` (rgba(0, 0, 0, 0.07) 0px 4px 20px 0px, rgba(11, 11, 11, 0.2) 0px 0px 0px 1px) |
| light-typed | text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |
| light-thread | size `layout.transcript-width` (768) x 100; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |
| light-project | size 680 x 120 |

Tokens named in its classes: `--cds-border`, `--cds-cursor-interactive`, `--cds-page-bg`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Composer placeholder

<a id="composer-placeholder"></a>`composer-placeholder`, on home-dark. Two stacked spans that cross-fade ("How can I help you today?", "Type / for skills").

<img src="components/crops/composer-placeholder-default.png" alt="Composer placeholder, default" height="40"> <img src="components/crops/composer-placeholder-light.png" alt="Composer placeholder, light" height="40"> 

| State | Values |
|---|---|
| default | size 636 x `density.h-control--lg` (40); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.muted` (#898781) |
| light | size 636 x `density.h-control--lg` (40); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.muted` (#898781) |

#### Composer typed text

<a id="composer-text"></a>`composer-text`, on home-dark-composer-typed.

<img src="components/crops/composer-text-default.png" alt="Composer typed text, default" height="24"> <img src="components/crops/composer-text-light.png" alt="Composer typed text, light" height="24"> 

| State | Values |
|---|---|
| default | size 636 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec) |
| light | size 636 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b) |

#### Composer + button

<a id="composer-plus"></a>`composer-plus`, on home-dark, home-dark-plus-menu.

<img src="components/crops/composer-plus-default.png" alt="Composer + button, default" height="32"> <img src="components/crops/composer-plus-hover.png" alt="Composer + button, hover" height="32"> <img src="components/crops/composer-plus-light.png" alt="Composer + button, light" height="32"> <img src="components/crops/composer-plus-light-hover.png" alt="Composer + button, light-hover" height="32"> <img src="components/crops/composer-plus-open.png" alt="Composer + button, open" height="32"> <img src="components/crops/composer-plus-focus-visible.png" alt="Composer + button, focus-visible" height="32"> <img src="components/crops/composer-plus-light-focus-visible.png" alt="Composer + button, light-focus-visible" height="32"> <img src="components/crops/composer-plus-light-open.png" alt="Composer + button, light-open" height="32"> 

| State | Values |
|---|---|
| default (same: hover, open) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover, light-open) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Chat/Cowork segmented control

<a id="segmented-control"></a>`segmented-control`, on home-dark. cds SegmentedControl: a track of --cds-segmented-control-track, the checked option on --cds-segmented-control-thumb.

<img src="components/crops/segmented-control-default.png" alt="Chat/Cowork segmented control, default" height="28"> <img src="components/crops/segmented-control-light.png" alt="Chat/Cowork segmented control, light" height="28"> 

| State | Values |
|---|---|
| default | size 119.17 x `density.h-control--sm` (28); padding 1px; radius `radius.segment-track` (7px); background `fill.disabled` (rgba(255, 255, 255, 0.05)); text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| light | size 119.78 x `density.h-control--sm` (28); padding 1px; radius `radius.segment-track` (7px); background `neutral.30` (#f6f6f4); text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-border`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Segment option

<a id="segment"></a>`segment`, on home-dark, home-dark-tooltip.

<img src="components/crops/segment-default.png" alt="Segment option, default" height="26"> <img src="components/crops/segment-hover.png" alt="Segment option, hover" height="26"> <img src="components/crops/segment-light.png" alt="Segment option, light" height="26"> <img src="components/crops/segment-light-hover.png" alt="Segment option, light-hover" height="26"> <img src="components/crops/segment-checked.png" alt="Segment option, checked" height="26"> <img src="components/crops/segment-light-checked.png" alt="Segment option, light-checked" height="26"> <img src="components/crops/segment-light-refresh.png" alt="Segment option, light-refresh" height="26"> <img src="components/crops/segment-light-refresh-focus-visible.png" alt="Segment option, light-refresh-focus-visible" height="26"> <img src="components/crops/segment-refresh.png" alt="Segment option, refresh" height="26"> <img src="components/crops/segment-refresh-focus-visible.png" alt="Segment option, refresh-focus-visible" height="26"> 

| State | Values |
|---|---|
| default | size 67.45 x 26; padding 0 `space.2-5` (10px); radius 5px; background transparent; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.muted` (#898781); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#f0efec) |
| refresh | size 49.72 x 26; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#f0efec) |
| refresh-focus-visible | size 49.72 x 26; shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#f0efec) |
| checked | size 49.72 x 26; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#f0efec) |
| light | size 67.83 x 26; padding 0 `space.2-5` (10px); radius 5px; background transparent; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.muted` (#898781); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#0b0b0b) |
| light-refresh | size 49.95 x 26; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#0b0b0b) |
| light-refresh-focus-visible | size 49.95 x 26; shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#0b0b0b) |
| light-checked | size 49.95 x 26; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-radius`.

#### Model selector

<a id="model-selector"></a>`model-selector`, on home-dark, home-dark-model-menu. "Opus 5.5" in text-primary, "Medium" (the effort) in text-muted, a chevron.

<img src="components/crops/model-selector-default.png" alt="Model selector, default" height="32"> <img src="components/crops/model-selector-hover.png" alt="Model selector, hover" height="32"> <img src="components/crops/model-selector-light.png" alt="Model selector, light" height="32"> <img src="components/crops/model-selector-light-hover.png" alt="Model selector, light-hover" height="32"> <img src="components/crops/model-selector-open.png" alt="Model selector, open" height="32"> <img src="components/crops/model-selector-focus-visible.png" alt="Model selector, focus-visible" height="32"> <img src="components/crops/model-selector-light-focus-visible.png" alt="Model selector, light-focus-visible" height="32"> <img src="components/crops/model-selector-light-open.png" alt="Model selector, light-open" height="32"> 

| State | Values |
|---|---|
| default (same: hover, open) | size 141.98 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover, light-open) | size 142.5 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Dictation button

<a id="mic-button"></a>`mic-button`, on home-dark.

<img src="components/crops/mic-button-default.png" alt="Dictation button, default" height="32"> <img src="components/crops/mic-button-hover.png" alt="Dictation button, hover" height="32"> <img src="components/crops/mic-button-light.png" alt="Dictation button, light" height="32"> <img src="components/crops/mic-button-light-hover.png" alt="Dictation button, light-hover" height="32"> <img src="components/crops/mic-button-focus-visible.png" alt="Dictation button, focus-visible" height="32"> <img src="components/crops/mic-button-light-focus-visible.png" alt="Dictation button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); padding 0 `density.pad-xs` (6px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition color and 9 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `alpha.2` (rgba(255, 255, 255, 0.1)) |
| focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#5598e7), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |
| light | size `density.h-control` (32) x `density.h-control` (32); padding 0 `density.pad-xs` (6px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition color and 9 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `alpha.2` (rgba(11, 11, 11, 0.1)) |
| light-focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#256abf), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |

Child layers: button 32x32 radius `radius.row` (8px)

#### Voice mode button

<a id="voice-button"></a>`voice-button`, on home-dark.

<img src="components/crops/voice-button-default.png" alt="Voice mode button, default" height="32"> <img src="components/crops/voice-button-hover.png" alt="Voice mode button, hover" height="32"> <img src="components/crops/voice-button-light.png" alt="Voice mode button, light" height="32"> <img src="components/crops/voice-button-light-hover.png" alt="Voice mode button, light-hover" height="32"> <img src="components/crops/voice-button-focus-visible.png" alt="Voice mode button, focus-visible" height="32"> <img src="components/crops/voice-button-light-focus-visible.png" alt="Voice mode button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); padding 0 `density.pad-xs` (6px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#f0efec); transition color and 9 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec) |
| hover | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#5598e7), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |
| light | size `density.h-control` (32) x `density.h-control` (32); padding 0 `density.pad-xs` (6px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#0b0b0b); transition color and 9 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b) |
| light-hover | background `fill.ghost-hover` (rgba(11, 11, 11, 0.05)) |
| light-focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#256abf), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |

Child layers: button 32x32 radius `radius.row` (8px)

#### Send button

<a id="send-button"></a>`send-button`, on home-dark-composer-typed. Takes the voice button's place once there is text: a filled clay (--cds-fill-brand) square with an arrow.

<img src="components/crops/send-button-default.png" alt="Send button, default" height="32"> <img src="components/crops/send-button-hover.png" alt="Send button, hover" height="32"> <img src="components/crops/send-button-light.png" alt="Send button, light" height="32"> <img src="components/crops/send-button-light-hover.png" alt="Send button, light-hover" height="32"> <img src="components/crops/send-button-focus-visible.png" alt="Send button, focus-visible" height="32"> <img src="components/crops/send-button-light-focus-visible.png" alt="Send button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `on.brand` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `on.brand` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Child layers: span 31x31 background `fill.brand` (#c6613f) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Disclaimer under the composer

<a id="disclaimer"></a>`disclaimer`, on thread-dark.

<img src="components/crops/disclaimer-default.png" alt="Disclaimer under the composer, default" height="24"> <img src="components/crops/disclaimer-light.png" alt="Disclaimer under the composer, light" height="24"> 

| State | Values |
|---|---|
| default | size 382.83 x 15; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 12/16 400, `text.muted` (#898781); transition color and 22 more `duration.tailwind-default` (0.15s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size 385.66 x 15; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 12/16 400, `text.muted` (#898781); transition color and 22 more `duration.tailwind-default` (0.15s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |

Child layers: a 382.8x15

### Menus and dialogs

Base UI popovers on surface-popover with radius 12, a 1px ring (outset in light, inset in dark) and the popover drop: the plus menu, the model menu, the account menu, a chat row's menu, the sidebar's More menu, and the search dialog over its backdrop.

#### Plus menu

<a id="plus-menu"></a>`plus-menu`, on home-dark-plus-menu. cds Menu: surface-popover, --cds-panel-radius, a ring plus --cds-shadow-popover; 4px inset, 32px rows.

<img src="components/crops/plus-menu-default.png" alt="Plus menu, default" height="120"> <img src="components/crops/plus-menu-light.png" alt="Plus menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 228.33 x 379; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `component.panel-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 8px 24px 0px, rgba(0, 0, 0, 0.2) 0px 2px 6px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec) |
| light | size 229.22 x 378; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `component.panel-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 8px 24px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--available-height`, `--cds-h-control`, `--cds-leading-body`, `--cds-ring-inner`, `--cds-shortcut-cap-ink`, `--cds-text-muted`.

#### Menu item

<a id="menu-item"></a>`menu-item`, on home-dark-plus-menu. A 20px glyph, body text, an optional shortcut or chevron at the end; hover fills --cds-fill-ghost-hover.

<img src="components/crops/menu-item-default.png" alt="Menu item, default" height="32"> <img src="components/crops/menu-item-hover.png" alt="Menu item, hover" height="32"> <img src="components/crops/menu-item-light.png" alt="Menu item, light" height="32"> <img src="components/crops/menu-item-light-hover.png" alt="Menu item, light-hover" height="32"> <img src="components/crops/menu-item-checkbox.png" alt="Menu item, checkbox" height="32"> <img src="components/crops/menu-item-light-checkbox.png" alt="Menu item, light-checkbox" height="32"> <img src="components/crops/menu-item-light-submenu.png" alt="Menu item, light-submenu" height="32"> <img src="components/crops/menu-item-submenu.png" alt="Menu item, submenu" height="32"> 

| State | Values |
|---|---|
| default (same: hover, checkbox, submenu) | size 220.33 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light (same: light-hover, light-checkbox, light-submenu) | size 221.22 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-text-muted`.

#### Menu item shortcut

<a id="menu-item-shortcut"></a>`menu-item-shortcut`, on home-dark-plus-menu.

<img src="components/crops/menu-item-shortcut-default.png" alt="Menu item shortcut, default" height="24"> <img src="components/crops/menu-item-shortcut-light.png" alt="Menu item shortcut, light" height="24"> 

| State | Values |
|---|---|
| default | size 25.2 x 17; background transparent; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.muted` (#898781) |
| light | size 25.22 x 17; background transparent; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.muted` (#898781) |

Tokens named in its classes: `--cds-shortcut-cap-ink`.

#### Model menu

<a id="model-menu"></a>`model-menu`, on home-dark-model-menu. Four models as two-line radio items (name, description in footnote), then Effort and More models as submenu rows.

<img src="components/crops/model-menu-default.png" alt="Model menu, default" height="120"> <img src="components/crops/model-menu-light.png" alt="Model menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 294.61 x 291; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `component.panel-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 8px 24px 0px, rgba(0, 0, 0, 0.2) 0px 2px 6px 0px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light | size 296.48 x 290; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `component.panel-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 8px 24px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--available-height`, `--available-width`, `--cds-font-size-body`, `--cds-font-size-footnote`, `--cds-h-control`, `--cds-leading-body`, `--cds-leading-footnote`, `--cds-ring-inner`, `--cds-text-muted`.

#### Model menu item

<a id="model-menu-item"></a>`model-menu-item`, on home-dark-model-menu.

<img src="components/crops/model-menu-item-default.png" alt="Model menu item, default" height="50"> <img src="components/crops/model-menu-item-hover.png" alt="Model menu item, hover" height="50"> <img src="components/crops/model-menu-item-light.png" alt="Model menu item, light" height="50"> <img src="components/crops/model-menu-item-light-hover.png" alt="Model menu item, light-hover" height="50"> <img src="components/crops/model-menu-item-checked.png" alt="Model menu item, checked" height="50"> <img src="components/crops/model-menu-item-light-checked.png" alt="Model menu item, light-checked" height="50"> 

| State | Values |
|---|---|
| default (same: hover, checked) | size 286.61 x `size.menu-row-two-line` (50); padding `density.pad-xs` (6px) `space.2-5` (10px) 7px `space.2-5` (10px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light (same: light-hover, light-checked) | size 288.48 x `size.menu-row-two-line` (50); padding `density.pad-xs` (6px) `space.2-5` (10px) 7px `space.2-5` (10px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-font-size-body`, `--cds-font-size-footnote`, `--cds-h-control`, `--cds-leading-body`, `--cds-leading-footnote`, `--cds-text-muted`.

#### Effort row

<a id="model-menu-effort"></a>`model-menu-effort`, on home-dark-model-menu.

<img src="components/crops/model-menu-effort-default.png" alt="Effort row, default" height="32"> <img src="components/crops/model-menu-effort-hover.png" alt="Effort row, hover" height="32"> <img src="components/crops/model-menu-effort-light.png" alt="Effort row, light" height="32"> <img src="components/crops/model-menu-effort-light-hover.png" alt="Effort row, light-hover" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 286.61 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light (same: light-hover) | size 288.48 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-text-muted`.

#### Account menu

<a id="user-menu"></a>`user-menu`, on home-dark-user-menu. Opens above the account row: the email as a muted header, then Settings, Usage, Language, Get help, plans, apps, Learn more, API keys, Log out.

<img src="components/crops/user-menu-default.png" alt="Account menu, default" height="120"> <img src="components/crops/user-menu-light.png" alt="Account menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 272 x 367; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `component.panel-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 8px 24px 0px, rgba(0, 0, 0, 0.2) 0px 2px 6px 0px); text `typography.footnote-medium` (Anthropic Sans 13/17 500), `text.muted` (#898781) |
| light | size 272 x 366; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `component.panel-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 8px 24px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px); text `typography.footnote-medium` (Anthropic Sans 13/17 500), `text.muted` (#898781) |

Tokens named in its classes: `--available-height`, `--cds-font-size-body`, `--cds-font-size-footnote`, `--cds-h-control`, `--cds-leading-body`, `--cds-leading-footnote`, `--cds-ring-inner`, `--cds-shortcut-cap-ink`, `--cds-text-muted`.

#### Account menu header

<a id="user-menu-header"></a>`user-menu-header`, on home-dark-user-menu.

<img src="components/crops/user-menu-header-default.png" alt="Account menu header, default" height="25"> <img src="components/crops/user-menu-header-light.png" alt="Account menu header, light" height="25"> 

| State | Values |
|---|---|
| default | size 264 x 25; padding `space.1` (4px) `space.2-5` (10px); background transparent; text `typography.footnote-medium` (Anthropic Sans 13/17 500), `text.muted` (#898781) |
| light | size 264 x 25; padding `space.1` (4px) `space.2-5` (10px); background transparent; text `typography.footnote-medium` (Anthropic Sans 13/17 500), `text.muted` (#898781) |

#### Account menu item

<a id="user-menu-item"></a>`user-menu-item`, on home-dark-user-menu.

<img src="components/crops/user-menu-item-default.png" alt="Account menu item, default" height="32"> <img src="components/crops/user-menu-item-hover.png" alt="Account menu item, hover" height="32"> <img src="components/crops/user-menu-item-light.png" alt="Account menu item, light" height="32"> <img src="components/crops/user-menu-item-light-hover.png" alt="Account menu item, light-hover" height="32"> <img src="components/crops/user-menu-item-light-twoLine.png" alt="Account menu item, light-twoLine" height="50"> <img src="components/crops/user-menu-item-twoLine.png" alt="Account menu item, twoLine" height="50"> 

| State | Values |
|---|---|
| default (same: hover) | size 264 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| twoLine | size 264 x `size.menu-row-two-line` (50); padding `density.pad-xs` (6px) `space.2-5` (10px) 7px `space.2-5` (10px); background transparent |
| light (same: light-hover) | size 264 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background `fill.ghost-hover` (rgba(11, 11, 11, 0.05)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |
| light-twoLine | size 264 x `size.menu-row-two-line` (50); padding `density.pad-xs` (6px) `space.2-5` (10px) 7px `space.2-5` (10px); background transparent |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-shortcut-cap-ink`, `--cds-text-muted`.

#### Chat row menu

<a id="chat-menu"></a>`chat-menu`, on home-dark-chat-menu.

<img src="components/crops/chat-menu-default.png" alt="Chat row menu, default" height="120"> <img src="components/crops/chat-menu-light.png" alt="Chat row menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 170.61 x 178; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `component.panel-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 8px 24px 0px, rgba(0, 0, 0, 0.2) 0px 2px 6px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light | size 171.2 x 177; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `component.panel-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 8px 24px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--available-height`, `--cds-h-control`, `--cds-leading-body`, `--cds-ring-inner`, `--cds-shortcut-cap-ink`, `--cds-text-muted`.

#### Chat menu Delete item

<a id="chat-menu-item-danger"></a>`chat-menu-item-danger`, on home-dark-chat-menu.

<img src="components/crops/chat-menu-item-danger-default.png" alt="Chat menu Delete item, default" height="32"> <img src="components/crops/chat-menu-item-danger-hover.png" alt="Chat menu Delete item, hover" height="32"> <img src="components/crops/chat-menu-item-danger-light.png" alt="Chat menu Delete item, light" height="32"> <img src="components/crops/chat-menu-item-danger-light-hover.png" alt="Chat menu Delete item, light-hover" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 162.61 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.danger` (#ec7e7e) |
| light (same: light-hover) | size 163.2 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.danger` (#8e2626) |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-shortcut-cap-ink`, `--cds-text-muted`.

#### Sidebar More menu

<a id="more-menu"></a>`more-menu`, on artifacts-dark-more-menu.

<img src="components/crops/more-menu-default.png" alt="Sidebar More menu, default" height="120"> <img src="components/crops/more-menu-light.png" alt="Sidebar More menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 149.75 x 178; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `component.panel-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 8px 24px 0px, rgba(0, 0, 0, 0.2) 0px 2px 6px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light | size 150.23 x 177; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `component.panel-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 8px 24px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--available-height`, `--cds-h-control`, `--cds-leading-body`, `--cds-ring-inner`, `--cds-text-muted`.

#### More menu item

<a id="more-menu-item"></a>`more-menu-item`, on artifacts-dark-more-menu.

<img src="components/crops/more-menu-item-default.png" alt="More menu item, default" height="32"> <img src="components/crops/more-menu-item-hover.png" alt="More menu item, hover" height="32"> <img src="components/crops/more-menu-item-light.png" alt="More menu item, light" height="32"> <img src="components/crops/more-menu-item-light-hover.png" alt="More menu item, light-hover" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 141.75 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light (same: light-hover) | size 142.23 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background `fill.ghost-hover` (rgba(11, 11, 11, 0.05)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-text-muted`.

#### Search dialog

<a id="search-dialog"></a>`search-dialog`, on home-dark-search. 672 wide, a field row over a list of results with a time group at the end of each row.

<img src="components/crops/search-dialog-default.png" alt="Search dialog, default" height="120"> <img src="components/crops/search-dialog-light.png" alt="Search dialog, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.search-dialog-width` (672) x 506.48; border `borderWidth.default` (1px) solid `border.strong` (rgba(255, 255, 255, 0.2)); radius `radius.card` (12px); background `surface.3` (#20201f); shadow rgba(0, 0, 0, 0.25) 0px 25px 50px -12px; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781) |
| light | size `layout.search-dialog-width` (672) x 506.48; border `borderWidth.default` (1px) solid `border.strong` (rgba(11, 11, 11, 0.2)); radius `radius.card` (12px); background `surface.3` (#ffffff); shadow rgba(0, 0, 0, 0.25) 0px 25px 50px -12px; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781) |

Tokens named in its classes: `--cds-black`, `--cds-cursor-interactive`, `--cds-page-bg`, `--cp-top`, `--cp-visible-h`.

#### Dialog backdrop

<a id="dialog-backdrop"></a>`dialog-backdrop`, on home-dark-search.

| State | Values |
|---|---|
| default | size 1440 x 900; background `surface.backdrop` (rgba(0, 0, 0, 0.5)); transition none `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)) |
| light | size 1440 x 900; background `surface.backdrop` (rgba(0, 0, 0, 0.4)); transition none `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)) |

#### Search field row

<a id="search-field"></a>`search-field`, on home-dark-search.

<img src="components/crops/search-field-default.png" alt="Search field row, default" height="64"> <img src="components/crops/search-field-light.png" alt="Search field row, light" height="64"> <img src="components/crops/search-field-focus-visible.png" alt="Search field row, focus-visible" height="64"> <img src="components/crops/search-field-light-focus-visible.png" alt="Search field row, light-focus-visible" height="64"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 670 x 63.98; padding 17.6px `space.2-5` (10px) 14.4px `density.pad-xl` (24px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781) |
| light (same: light-focus-visible) | size 670 x 63.98; padding 17.6px `space.2-5` (10px) 14.4px `density.pad-xl` (24px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781) |

Child layers: textarea 544x20 shadow none

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Search result row

<a id="search-result"></a>`search-result`, on home-dark-search.

<img src="components/crops/search-result-default.png" alt="Search result row, default" height="36"> <img src="components/crops/search-result-hover.png" alt="Search result row, hover" height="36"> <img src="components/crops/search-result-light.png" alt="Search result row, light" height="36"> <img src="components/crops/search-result-light-hover.png" alt="Search result row, light-hover" height="36"> <img src="components/crops/search-result-selected.png" alt="Search result row, selected" height="36"> <img src="components/crops/search-result-light-selected.png" alt="Search result row, light-selected" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 650 x 36; padding `density.pad-sm` (8px) `density.pad-md` (12px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#c3c2b7) |
| selected | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light (same: light-hover) | size 650 x 36; padding `density.pad-sm` (8px) `density.pad-md` (12px); radius `radius.row` (8px); background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#52514e) |
| light-selected | background `fill.ghost-hover` (rgba(11, 11, 11, 0.05)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Child layers: button 650x36 radius `radius.row` (8px)

#### Search result time

<a id="search-result-time"></a>`search-result-time`, on home-dark-search.

<img src="components/crops/search-result-time-default.png" alt="Search result time, default" height="24"> <img src="components/crops/search-result-time-light.png" alt="Search result time, light" height="24"> 

| State | Values |
|---|---|
| default | size 32.89 x `size.switch-knob` (16); background transparent; text Anthropic Sans 12/16 400, `text.muted` (#898781) |
| light | size 32.89 x `size.switch-knob` (16); background transparent; text Anthropic Sans 12/16 400, `text.muted` (#898781) |

#### Dialog close button

<a id="dialog-close"></a>`dialog-close`, on home-dark-search.

<img src="components/crops/dialog-close-default.png" alt="Dialog close button, default" height="32"> <img src="components/crops/dialog-close-hover.png" alt="Dialog close button, hover" height="32"> <img src="components/crops/dialog-close-light.png" alt="Dialog close button, light" height="32"> <img src="components/crops/dialog-close-light-hover.png" alt="Dialog close button, light-hover" height="32"> <img src="components/crops/dialog-close-focus-visible.png" alt="Dialog close button, focus-visible" height="32"> <img src="components/crops/dialog-close-light-focus-visible.png" alt="Dialog close button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus on this surface` (#20201f 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus on this surface` (#ffffff 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

### Settings

The settings dialog: a 192px nav with a search field and two groups (Settings, Customize), and the General pane: section titles, rows with a title, an optional description and a control (the System/Light/Dark theme picker, selects, segmented controls, switches), split by hairlines.

#### Settings dialog

<a id="settings-dialog"></a>`settings-dialog`, on settings-dark-general. 1024x800 at 1440: a 192 nav column with a right rule, the General pane to the right.

<img src="components/crops/settings-dialog-default.png" alt="Settings dialog, default" height="120"> <img src="components/crops/settings-dialog-light.png" alt="Settings dialog, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.settings-dialog-width` (1024) x `layout.settings-dialog-height` (800); border `borderWidth.default` (1px) solid `alpha.1` (rgba(255, 255, 255, 0.05)); radius `radius.card` (12px); background `surface.2` (#1a1a19); shadow `component.dialog-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.24) 0px 2px 8px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); transition opacity `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), scale `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)); icon `density.icon` (20) x `density.icon` (20), `text.secondary` (#c3c2b7); placeholder `text.muted` (#898781) |
| light | size `layout.settings-dialog-width` (1024) x `layout.settings-dialog-height` (800); radius `radius.card` (12px); background `surface.2` (#ffffff); shadow `shadow.panel` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(11, 11, 11, 0.08) 0px 2px 8px 0px); text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); transition opacity `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), scale `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)); icon `density.icon` (20) x `density.icon` (20), `text.secondary` (#52514e); placeholder `text.muted` (#898781) |

#### Settings nav column

<a id="settings-nav"></a>`settings-nav`, on settings-dark-general.

<img src="components/crops/settings-nav-default.png" alt="Settings nav column, default" height="120"> <img src="components/crops/settings-nav-light.png" alt="Settings nav column, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.settings-nav-width` (192) x 798; border R: `borderWidth.default` (1px) solid `alpha.2` (rgba(255, 255, 255, 0.1)); background `surface.1` (#151515); text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); icon `density.icon` (20) x `density.icon` (20), `text.secondary` (#c3c2b7); placeholder `text.muted` (#898781) |
| light | size `layout.settings-nav-width` (192) x `layout.settings-dialog-height` (800); border R: `borderWidth.default` (1px) solid `alpha.2` (rgba(11, 11, 11, 0.1)); background `surface.1` (#fcfcfb); text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); icon `density.icon` (20) x `density.icon` (20), `text.secondary` (#52514e); placeholder `text.muted` (#898781) |

#### Settings search field

<a id="settings-search"></a>`settings-search`, on settings-dark-general.

<img src="components/crops/settings-search-default.png" alt="Settings search field, default" height="32"> <img src="components/crops/settings-search-hover.png" alt="Settings search field, hover" height="32"> <img src="components/crops/settings-search-light.png" alt="Settings search field, light" height="32"> <img src="components/crops/settings-search-light-hover.png" alt="Settings search field, light-hover" height="32"> <img src="components/crops/settings-search-focus-visible.png" alt="Settings search field, focus-visible" height="32"> <img src="components/crops/settings-search-light-focus-visible.png" alt="Settings search field, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 167 x `density.h-control` (32); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); placeholder `text.muted` (#898781) |
| focus-visible | focus ring on the inner div: `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light (same: light-hover) | size 167 x `density.h-control` (32); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); placeholder `text.muted` (#898781) |
| light-focus-visible | focus ring on the inner div: `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

Child layers: div 167x32 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius `radius.row` (8px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1))

#### Settings nav group label

<a id="settings-nav-label"></a>`settings-nav-label`, on settings-dark-general.

<img src="components/crops/settings-nav-label-default.png" alt="Settings nav group label, default" height="29"> <img src="components/crops/settings-nav-label-light.png" alt="Settings nav group label, light" height="29"> 

| State | Values |
|---|---|
| default | size 167 x 29; padding `density.pad-md` (12px) `density.pad-sm` (8px) 0 `density.pad-sm` (8px); background transparent; text `typography.caption-regular` (Anthropic Sans 12/17 400), `text.muted` (#898781) |
| light | size 167 x 29; padding `density.pad-md` (12px) `density.pad-sm` (8px) 0 `density.pad-sm` (8px); background transparent; text `typography.caption-regular` (Anthropic Sans 12/17 400), `text.muted` (#898781) |

#### Settings nav item

<a id="settings-nav-item"></a>`settings-nav-item`, on settings-dark-general, settings-dark-account.

<img src="components/crops/settings-nav-item-default.png" alt="Settings nav item, default" height="32"> <img src="components/crops/settings-nav-item-hover.png" alt="Settings nav item, hover" height="32"> <img src="components/crops/settings-nav-item-light.png" alt="Settings nav item, light" height="32"> <img src="components/crops/settings-nav-item-light-hover.png" alt="Settings nav item, light-hover" height="32"> <img src="components/crops/settings-nav-item-active.png" alt="Settings nav item, active" height="32"> <img src="components/crops/settings-nav-item-focus-visible.png" alt="Settings nav item, focus-visible" height="32"> <img src="components/crops/settings-nav-item-active-hover.png" alt="Settings nav item, active-hover" height="32"> <img src="components/crops/settings-nav-item-light-active.png" alt="Settings nav item, light-active" height="32"> <img src="components/crops/settings-nav-item-light-active-hover.png" alt="Settings nav item, light-active-hover" height="32"> <img src="components/crops/settings-nav-item-light-focus-visible.png" alt="Settings nav item, light-focus-visible" height="32"> <img src="components/crops/settings-nav-item-light-refresh.png" alt="Settings nav item, light-refresh" height="32"> <img src="components/crops/settings-nav-item-light-refresh-focus-visible.png" alt="Settings nav item, light-refresh-focus-visible" height="32"> <img src="components/crops/settings-nav-item-refresh.png" alt="Settings nav item, refresh" height="32"> <img src="components/crops/settings-nav-item-refresh-focus-visible.png" alt="Settings nav item, refresh-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, active, active-hover) | size 167 x `density.h-control` (32); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#c3c2b7) |
| refresh | size 187 x `density.h-control` (32) |
| refresh-focus-visible | size 187 x `density.h-control` (32); focus ring on the inner button: `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light (same: light-hover, light-focus-visible, light-active, light-active-hover) | size 167 x `density.h-control` (32); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#52514e) |
| light-refresh | size 187 x `density.h-control` (32) |
| light-refresh-focus-visible | size 187 x `density.h-control` (32); focus ring on the inner button: `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

Child layers: button 167x32 radius `radius.row` (8px)

#### Settings section title (h3)

<a id="settings-section-title"></a>`settings-section-title`, on settings-dark-general.

<img src="components/crops/settings-section-title-default.png" alt="Settings section title (h3), default" height="24"> <img src="components/crops/settings-section-title-light.png" alt="Settings section title (h3), light" height="24"> 

| State | Values |
|---|---|
| default | size 87.94 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-semibold` (Anthropic Sans 15/20 580), `text.primary` (#f0efec) |
| light | size 88.47 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-semibold` (Anthropic Sans 15/20 580), `text.primary` (#0b0b0b) |

#### Settings row

<a id="settings-row"></a>`settings-row`, on settings-dark-general. Title (and an optional description) at the start, the control at the end; groups separated by hairlines (.settings-group-dividers).

<img src="components/crops/settings-row-default.png" alt="Settings row, default" height="56"> <img src="components/crops/settings-row-light.png" alt="Settings row, light" height="56"> 

| State | Values |
|---|---|
| default | size 782 x 56; padding `density.pad-md` (12px) 0; background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| light | size 784 x 56; padding `density.pad-md` (12px) 0; background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |

Child layers: div 92x32 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius `radius.row` (8px); input 1x1; input 1x1

Tokens named in its classes: `--cds-border`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Settings row title

<a id="settings-row-title"></a>`settings-row-title`, on settings-dark-general.

<img src="components/crops/settings-row-title-default.png" alt="Settings row title, default" height="24"> <img src="components/crops/settings-row-title-light.png" alt="Settings row title, light" height="24"> 

| State | Values |
|---|---|
| default | size 62.08 x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light | size 62.58 x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

#### Settings row description

<a id="settings-row-desc"></a>`settings-row-desc`, on settings-dark-general.

<img src="components/crops/settings-row-desc-default.png" alt="Settings row description, default" height="24"> <img src="components/crops/settings-row-desc-light.png" alt="Settings row description, light" height="24"> 

| State | Values |
|---|---|
| default | size 718 x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| light | size 720 x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |

#### Settings row group

<a id="settings-divider-group"></a>`settings-divider-group`, on settings-dark-general.

<img src="components/crops/settings-divider-group-default.png" alt="Settings row group, default" height="120"> <img src="components/crops/settings-divider-group-light.png" alt="Settings row group, light" height="120"> 

| State | Values |
|---|---|
| default | size 782 x 182; background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| light | size 784 x 182; background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |

Child layers: div 92x32 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius `radius.row` (8px); input 1x1; input 1x1

Tokens named in its classes: `--cds-border`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Theme picker

<a id="theme-picker"></a>`theme-picker`, on settings-dark-general. Three icon segments: System, Light, Dark.

<img src="components/crops/theme-picker-default.png" alt="Theme picker, default" height="32"> <img src="components/crops/theme-picker-light.png" alt="Theme picker, light" height="32"> 

| State | Values |
|---|---|
| default | size 92 x `density.h-control` (32); padding 1px; radius `radius.row` (8px); background `fill.disabled` (rgba(255, 255, 255, 0.05)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| light | size 92 x `density.h-control` (32); padding 1px; radius `radius.row` (8px); background `fill.disabled` (rgba(11, 11, 11, 0.05)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-border`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Theme option

<a id="theme-option"></a>`theme-option`, on settings-dark-general.

<img src="components/crops/theme-option-default.png" alt="Theme option, default" height="30"> <img src="components/crops/theme-option-hover.png" alt="Theme option, hover" height="30"> <img src="components/crops/theme-option-light.png" alt="Theme option, light" height="30"> <img src="components/crops/theme-option-light-hover.png" alt="Theme option, light-hover" height="30"> <img src="components/crops/theme-option-checked.png" alt="Theme option, checked" height="30"> <img src="components/crops/theme-option-light-checked.png" alt="Theme option, light-checked" height="30"> 

| State | Values |
|---|---|
| default | size `size.mode-pill-height` (30) x `size.mode-pill-height` (30); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover, checked | text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light | size `size.mode-pill-height` (30) x `size.mode-pill-height` (30); radius `radius.segment-thumb` (6px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.muted` (#898781); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover, light-checked | text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-radius`.

#### Text segmented control (Motion)

<a id="text-segment"></a>`text-segment`, on settings-dark-general.

<img src="components/crops/text-segment-default.png" alt="Text segmented control (Motion), default" height="32"> <img src="components/crops/text-segment-light.png" alt="Text segmented control (Motion), light" height="32"> 

| State | Values |
|---|---|
| default | size 156.42 x `density.h-control` (32); padding 1px; radius `radius.row` (8px); background `fill.disabled` (rgba(255, 255, 255, 0.05)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| light | size 157.22 x `density.h-control` (32); padding 1px; radius `radius.row` (8px); background `fill.disabled` (rgba(11, 11, 11, 0.05)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-border`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Select (Chat font)

<a id="select"></a>`select`, on settings-dark-general. cds Combobox: the value and a chevron in a control-height field.

<img src="components/crops/select-default.png" alt="Select (Chat font), default" height="32"> <img src="components/crops/select-hover.png" alt="Select (Chat font), hover" height="32"> <img src="components/crops/select-light.png" alt="Select (Chat font), light" height="32"> <img src="components/crops/select-light-hover.png" alt="Select (Chat font), light-hover" height="32"> <img src="components/crops/select-focus-visible.png" alt="Select (Chat font), focus-visible" height="32"> <img src="components/crops/select-light-focus-visible.png" alt="Select (Chat font), light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size 140.36 x `density.h-control` (32); padding 0 `density.pad-sm` (8px) 0 0; radius `radius.row` (8px); background transparent; text Anthropic Serif 14/20 400, `text.primary` (#f0efec); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light | size 141.42 x `density.h-control` (32); padding 0 `density.pad-sm` (8px) 0 0; radius `radius.row` (8px); background transparent; text Anthropic Serif 14/20 400, `text.primary` (#0b0b0b); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.ghost-hover` (rgba(11, 11, 11, 0.05)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

#### Switch

<a id="switch"></a>`switch`, on settings-dark-general. 36x20 track (--cds-switch-track), a 16px knob with shadow-sm that slides on --cds-dur-snap.

<img src="components/crops/switch-default.png" alt="Switch, default" height="24"> <img src="components/crops/switch-hover.png" alt="Switch, hover" height="24"> <img src="components/crops/switch-light.png" alt="Switch, light" height="24"> <img src="components/crops/switch-light-hover.png" alt="Switch, light-hover" height="24"> <img src="components/crops/switch-on.png" alt="Switch, on" height="24"> <img src="components/crops/switch-focus-visible.png" alt="Switch, focus-visible" height="24"> <img src="components/crops/switch-light-focus-visible.png" alt="Switch, light-focus-visible" height="24"> <img src="components/crops/switch-light-on.png" alt="Switch, light-on" height="24"> <img src="components/crops/switch-light-on-hover.png" alt="Switch, light-on-hover" height="24"> <img src="components/crops/switch-on-hover.png" alt="Switch, on-hover" height="24"> 

| State | Values |
|---|---|
| default | size `size.switch-width` (36) x `density.h-control-nested--sm` (20); padding `space.0-5` (2px); radius `radius.full` (9999px); background `fill.control` (rgba(255, 255, 255, 0.1)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| hover | background `fill.control-hover` (rgba(255, 255, 255, 0.2)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| on | background `fill.accent` (#2a78d6) |
| on-hover | background `fill.accent-hover` (#3987e5) |
| light | size `size.switch-width` (36) x `density.h-control-nested--sm` (20); padding `space.0-5` (2px); radius `radius.full` (9999px); background `fill.control-hover` (rgba(11, 11, 11, 0.2)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |
| light-hover | background `alpha.4` (rgba(11, 11, 11, 0.35)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |
| light-on | background `fill.accent` (#2a78d6) |
| light-on-hover | background `fill.accent-hover` (#3987e5) |

Tokens named in its classes: `--cds-switch-h`, `--cds-switch-knob`, `--cds-switch-track`, `--cds-switch-track-hover`.

#### Switch knob

<a id="switch-knob"></a>`switch-knob`, on settings-dark-general.

<img src="components/crops/switch-knob-default.png" alt="Switch knob, default" height="24"> <img src="components/crops/switch-knob-light.png" alt="Switch knob, light" height="24"> 

| State | Values |
|---|---|
| default | size `size.switch-knob` (16) x `size.switch-knob` (16); radius `radius.full` (9999px); background `fill.primary` (#ffffff); shadow `shadow.sm` (rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.24) 0px 2px 8px 0px); transition transform and 3 more `duration.snap` (0.12s) `easing.overshoot` (cubic-bezier(0.34, 1.3, 0.64, 1)) |
| light | size `size.switch-knob` (16) x `size.switch-knob` (16); radius `radius.full` (9999px); background `surface.2` (#ffffff); shadow `shadow.sm` (rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(11, 11, 11, 0.08) 0px 2px 8px 0px); transition transform and 3 more `duration.snap` (0.12s) `easing.overshoot` (cubic-bezier(0.34, 1.3, 0.64, 1)) |

Tokens named in its classes: `--cds-switch-h`, `--cds-switch-knob`.

#### Settings close button

<a id="settings-close"></a>`settings-close`, on settings-dark-general.

<img src="components/crops/settings-close-default.png" alt="Settings close button, default" height="32"> <img src="components/crops/settings-close-hover.png" alt="Settings close button, hover" height="32"> <img src="components/crops/settings-close-light.png" alt="Settings close button, light" height="32"> <img src="components/crops/settings-close-light-hover.png" alt="Settings close button, light-hover" height="32"> <img src="components/crops/settings-close-focus-visible.png" alt="Settings close button, focus-visible" height="32"> <img src="components/crops/settings-close-light-focus-visible.png" alt="Settings close button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

### Thread

A chat: the 768px transcript, the user's bubble, "Thought for 6s", Claude's reply in the chat font (Anthropic Serif by default) with a code block and a table, the message actions, and the dock that holds the composer.

#### Transcript column

<a id="transcript"></a>`transcript`, on thread-dark. 768 wide (--transcript-width 48rem), centred in the pane.

<img src="components/crops/transcript-default.png" alt="Transcript column, default" height="120"> <img src="components/crops/transcript-light.png" alt="Transcript column, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.transcript-width` (768) x 3142.5; padding `space.1` (4px) `density.pad-lg` (16px) 0 `density.pad-lg` (16px); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec); icon 32 x 32, `text.primary` (#f0efec) |
| light | size `layout.transcript-width` (768) x 3142.5; padding `space.1` (4px) `density.pad-lg` (16px) 0 `density.pad-lg` (16px); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b); icon 32 x 32, `text.primary` (#0b0b0b) |

Child layers: div 623x288 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius `radius.card` (12px); button 1x1; button 732x28

Tokens named in its classes: `--cds-bg-user-message`, `--cds-message-bubble-measure`, `--cds-message-bubble-pad-x`, `--cds-message-bubble-pad-y`, `--cds-message-bubble-radius`, `--chat-list-inset`, `--df-ceded-gutter`, `--msg-assistant-pb`, `--msg-block-inset`, `--msg-gap`, `--msg-inset-end`, `--msg-pill-py`, `--msg-text-inset`, `--transcript-width`.

#### User message bubble

<a id="user-message"></a>`user-message`, on thread-dark, thread-dark-followup. Right-aligned, at most 85% of the column (--cds-message-bubble-measure), --cds-bg-user-message, radius --cds-message-bubble-radius, padding pad-md / pad-lg.

<img src="components/crops/user-message-default.png" alt="User message bubble, default" height="120"> <img src="components/crops/user-message-light.png" alt="User message bubble, light" height="120"> <img src="components/crops/user-message-short.png" alt="User message bubble, short" height="44"> <img src="components/crops/user-message-light-short.png" alt="User message bubble, light-short" height="44"> 

| State | Values |
|---|---|
| default | size 623 x 288; padding `density.pad-md` (12px) `density.pad-lg` (16px); radius `radius.card` (12px); background `fill.disabled` (rgba(255, 255, 255, 0.05)); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec) |
| short | size 234.63 x `layout.sidebar-titlebar-height` (44) |
| light | size 623 x 288; padding `density.pad-md` (12px) `density.pad-lg` (16px); radius `radius.card` (12px); background `fill.disabled` (rgba(11, 11, 11, 0.05)); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b) |
| light-short | size 236.06 x `layout.sidebar-titlebar-height` (44) |

Tokens named in its classes: `--cds-bg-user-message`, `--cds-message-bubble-measure`, `--cds-message-bubble-pad-x`, `--cds-message-bubble-pad-y`, `--cds-message-bubble-radius`.

#### User message paragraph

<a id="user-message-text"></a>`user-message-text`, on thread-dark.

<img src="components/crops/user-message-text-default.png" alt="User message paragraph, default" height="24"> <img src="components/crops/user-message-text-light.png" alt="User message paragraph, light" height="24"> 

| State | Values |
|---|---|
| default | size 591 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec) |
| light | size 591 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b) |

#### User message list item

<a id="user-message-li"></a>`user-message-li`, on thread-dark.

<img src="components/crops/user-message-li-default.png" alt="User message list item, default" height="24"> <img src="components/crops/user-message-li-light.png" alt="User message list item, light" height="24"> 

| State | Values |
|---|---|
| default | size 559 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec) |
| light | size 559 x `density.h-control-nested--sm` (20); background transparent; text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b) |

#### Thought for 6s

<a id="thinking-pill"></a>`thinking-pill`, on thread-dark. The collapsed reasoning row: text-muted, a caret that shows on hover.

<img src="components/crops/thinking-pill-default.png" alt="Thought for 6s, default" height="28"> <img src="components/crops/thinking-pill-hover.png" alt="Thought for 6s, hover" height="28"> <img src="components/crops/thinking-pill-light.png" alt="Thought for 6s, light" height="28"> <img src="components/crops/thinking-pill-light-hover.png" alt="Thought for 6s, light-hover" height="28"> <img src="components/crops/thinking-pill-focus-visible.png" alt="Thought for 6s, focus-visible" height="28"> <img src="components/crops/thinking-pill-light-focus-visible.png" alt="Thought for 6s, light-focus-visible" height="28"> 

| State | Values |
|---|---|
| default | size 732 x `density.h-control--sm` (28); padding `space.1` (4px) 0; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| hover | text `typography.body-regular` (Anthropic Sans 14/20 400), `text.secondary` (#c3c2b7) |
| focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#5598e7), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |
| light | size 732 x `density.h-control--sm` (28); padding `space.1` (4px) 0; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| light-hover | text `typography.body-regular` (Anthropic Sans 14/20 400), `text.secondary` (#52514e) |
| light-focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#256abf), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |

Child layers: button 732x28

#### Assistant prose block

<a id="assistant-prose"></a>`assistant-prose`, on thread-dark-table. The response in the chat font (Anthropic Serif by default, .font-claude-response).

| State | Values |
|---|---|
| default | size `layout.transcript-feed-width` (736) x 1309.5; background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light | size `layout.transcript-feed-width` (736) x 1309.5; background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Child layers: div 736x834.5 background rgba(32, 32, 31, 0.5) border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)) radius `radius.row` (8px); table 728x355 border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)) radius `radius.row` (8px); th 170.7x39 background `fill.disabled` (rgba(255, 255, 255, 0.05)) border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)) radius 7px 0px 0px

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--msg-block-radius`.

#### Assistant paragraph

<a id="prose-paragraph"></a>`prose-paragraph`, on thread-dark-table.

<img src="components/crops/prose-paragraph-default.png" alt="Assistant paragraph, default" height="24"> <img src="components/crops/prose-paragraph-light.png" alt="Assistant paragraph, light" height="24"> 

| State | Values |
|---|---|
| default | size `layout.transcript-feed-width` (736) x `density.h-control--xs` (24); padding 0 `space.8` (32px) 0 `space.1` (4px); background transparent; text `typography.chat` (Anthropic Serif 16/24 400), `text.primary` (#f0efec) |
| light | size `layout.transcript-feed-width` (736) x `density.h-control--xs` (24); padding 0 `space.8` (32px) 0 `space.1` (4px); background transparent; text `typography.chat` (Anthropic Serif 16/24 400), `text.primary` (#0b0b0b) |

#### Code block

<a id="code-block"></a>`code-block`, on thread-dark. A half-strength --bg-000 fill, a 1px hairline (the class says border-border-400, which computes to --cds-border), radius 8 (--msg-block-radius); a "markdown" label row, a copy button shown on hover, then the <pre>.

<img src="components/crops/code-block-default.png" alt="Code block, default" height="120"> <img src="components/crops/code-block-light.png" alt="Code block, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.transcript-feed-width` (736) x 834.5; border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)); radius `radius.row` (8px); background rgba(32, 32, 31, 0.5); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec) |
| light | size `layout.transcript-feed-width` (736) x 834.5; border `borderWidth.default` (1px) solid `border.default` (rgba(11, 11, 11, 0.1)); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.5)); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--msg-block-radius`.

#### Code block language label

<a id="code-label"></a>`code-label`, on thread-dark.

<img src="components/crops/code-label-default.png" alt="Code block language label, default" height="31"> <img src="components/crops/code-label-light.png" alt="Code block language label, light" height="31"> 

| State | Values |
|---|---|
| default | size 734 x 31; padding `space.3-5` (14px) `space.3-5` (14px) 0 `space.3-5` (14px); background transparent; text `typography.caption-regular` (Anthropic Sans 12/17 400), `text.muted` (#898781) |
| light | size 734 x 31; padding `space.3-5` (14px) `space.3-5` (14px) 0 `space.3-5` (14px); background transparent; text `typography.caption-regular` (Anthropic Sans 12/17 400), `text.muted` (#898781) |

#### Code block copy button

<a id="code-copy"></a>`code-copy`, on thread-dark. Shown when the block is hovered.

<img src="components/crops/code-copy-default.png" alt="Code block copy button, default" height="32"> <img src="components/crops/code-copy-hover.png" alt="Code block copy button, hover" height="32"> <img src="components/crops/code-copy-light.png" alt="Code block copy button, light" height="32"> <img src="components/crops/code-copy-light-hover.png" alt="Code block copy button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | backdrop blur(12px) |
| light | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | backdrop blur(12px) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Code block body

<a id="code-pre"></a>`code-pre`, on thread-dark.

| State | Values |
|---|---|
| default | size 734 x 801.5; padding `space.3-5` (14px); radius `radius.row` (8px); background transparent; text Anthropic Mono 14/22.75 400, #d3d7de |
| light | size 734 x 801.5; padding `space.3-5` (14px); radius `radius.row` (8px); background transparent; text Anthropic Mono 14/22.75 400, #d3d7de |

Tokens named in its classes: `--msg-block-radius`.

#### Code token (heading marker)

<a id="code-token"></a>`code-token`, on thread-dark. Syntax colours are inline styles from the highlighter and do not change with the theme; read them from the dark copy.

<img src="components/crops/code-token-default.png" alt="Code token (heading marker), default" height="24"> <img src="components/crops/code-token-light.png" alt="Code token (heading marker), light" height="24"> 

| State | Values |
|---|---|
| default | size 8.41 x `density.h-control-nested--xs` (18); background transparent; text Anthropic Mono 14/22.75 400, #d3d7de |
| light | size 8.41 x `density.h-control-nested--xs` (18); background transparent; text Anthropic Mono 14/22.75 400, #d3d7de |

#### Table

<a id="table"></a>`table`, on thread-dark-table.

<img src="components/crops/table-default.png" alt="Table, default" height="120"> <img src="components/crops/table-light.png" alt="Table, light" height="120"> 

| State | Values |
|---|---|
| default | size 728 x 355; border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)); radius `radius.row` (8px); background transparent; text Anthropic Serif 16/24 500, `text.primary` (#f0efec) |
| light | size 728 x 355; border `borderWidth.default` (1px) solid `border.default` (rgba(11, 11, 11, 0.1)); radius `radius.row` (8px); background transparent; text Anthropic Serif 16/24 500, `text.primary` (#0b0b0b) |

#### Table header cell

<a id="table-th"></a>`table-th`, on thread-dark-table.

<img src="components/crops/table-th-default.png" alt="Table header cell, default" height="39"> <img src="components/crops/table-th-light.png" alt="Table header cell, light" height="39"> 

| State | Values |
|---|---|
| default | size 170.66 x 39; padding 7px `density.pad-md` (12px); border B: `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)); radius 7px 0px 0px 0px; background `fill.disabled` (rgba(255, 255, 255, 0.05)); text Anthropic Serif 16/24 500, `text.primary` (#f0efec) |
| light | size 170.97 x 39; padding 7px `density.pad-md` (12px); border B: `borderWidth.default` (1px) solid `border.default` (rgba(11, 11, 11, 0.1)); radius 7px 0px 0px 0px; background `fill.disabled` (rgba(11, 11, 11, 0.05)); text Anthropic Serif 16/24 500, `text.primary` (#0b0b0b) |

#### Table cell

<a id="table-td"></a>`table-td`, on thread-dark-table.

<img src="components/crops/table-td-default.png" alt="Table cell, default" height="62"> <img src="components/crops/table-td-light.png" alt="Table cell, light" height="62"> 

| State | Values |
|---|---|
| default | size 170.66 x 62; padding 7px `density.pad-md` (12px); background transparent; text `typography.chat` (Anthropic Serif 16/24 400), `text.primary` (#f0efec) |
| light | size 170.97 x 62; padding 7px `density.pad-md` (12px); background transparent; text `typography.chat` (Anthropic Serif 16/24 400), `text.primary` (#0b0b0b) |

#### Message actions

<a id="message-actions"></a>`message-actions`, on thread-dark-table. Copy, rating and retry icon buttons under a response; they reveal on hover of the row (--cds-message-actions-opacity).

<img src="components/crops/message-actions-default.png" alt="Message actions, default" height="24"> <img src="components/crops/message-actions-light.png" alt="Message actions, light" height="24"> 

| State | Values |
|---|---|
| default | size 738 x `density.h-control--xs` (24); background transparent |
| light | size 738 x `density.h-control--xs` (24); background transparent |

Child layers: button 1x1

Tokens named in its classes: `--msg-text-inset`.

#### Message action button

<a id="message-action"></a>`message-action`, on thread-dark-table.

<img src="components/crops/message-action-default.png" alt="Message action button, default" height="24"> <img src="components/crops/message-action-hover.png" alt="Message action button, hover" height="24"> <img src="components/crops/message-action-light.png" alt="Message action button, light" height="24"> <img src="components/crops/message-action-light-hover.png" alt="Message action button, light-hover" height="24"> <img src="components/crops/message-action-focus-visible.png" alt="Message action button, focus-visible" height="24"> <img src="components/crops/message-action-light-focus-visible.png" alt="Message action button, light-focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size 1 x 1; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 14/21 400, `text.primary` (#f0efec) |
| focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#5598e7), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size 1 x 1; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropic Sans 14/21 400, `text.primary` (#0b0b0b) |
| light-focus-visible | outline `borderWidth.thick` (2px) solid `legacy.accent-100` (#256abf), offset `focusRing.outline-offset` (2px); transition outline `duration.base` (0.2s) ease |

Child layers: button 1x1

#### Scroll to bottom button

<a id="jump-to-latest"></a>`jump-to-latest`, on thread-dark. Held at opacity 0 at this scroll position; measured as found.

<img src="components/crops/jump-to-latest-default.png" alt="Scroll to bottom button, default" height="36"> <img src="components/crops/jump-to-latest-light.png" alt="Scroll to bottom button, light" height="36"> 

| State | Values |
|---|---|
| default | size `size.switch-width` (36) x 36; padding `space.1` (4px); border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)); radius `radius.full` (9999px); background rgba(32, 32, 31, 0.8); shadow `shadow.md` (rgba(11, 11, 11, 0.07) 0px 2px 4px 0px, rgba(0, 0, 0, 0.24) 0px 6px 16px 0px); backdrop blur(8px); outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition opacity `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); opacity 0 |
| light | size `size.switch-width` (36) x 36; padding `space.1` (4px); border `borderWidth.default` (1px) solid `border.default` (rgba(11, 11, 11, 0.1)); radius `radius.full` (9999px); background rgba(255, 255, 255, 0.8); shadow `shadow.md` (rgba(11, 11, 11, 0.07) 0px 2px 4px 0px, rgba(11, 11, 11, 0.08) 0px 6px 16px 0px); backdrop blur(8px); outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition opacity `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); opacity 0 |

Tokens named in its classes: `--composer-banners-h`.

### Pages

The list pages share one 960px page column with a serif page title: Artifacts (tabs, a notice card, the Make something new tiles, month groups of rows), Chats and tasks (a table of rows with times), Projects (a two-column grid of cards) and a project page (breadcrumb, title, composer, Recents, the Instructions, Memory and Context cards).

#### Page header

<a id="page-header"></a>`page-header`, on artifacts-dark. cds PageHeader on a 960 wide page: the title in Anthropic Serif (font-voice) 24/32, actions at the end.

<img src="components/crops/page-header-default.png" alt="Page header, default" height="96"> <img src="components/crops/page-header-light.png" alt="Page header, light" height="96"> 

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x 96; background transparent; text `typography.page-title` (Anthropic Serif 24/32 500), `text.primary` (#f0efec) |
| light | size `layout.page-width` (960) x 96; background transparent; text `typography.page-title` (Anthropic Serif 24/32 500), `text.primary` (#0b0b0b) |

Child layers: button 40.5469pxx32px background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) radius `radius.row` (8px); span 130.8x28 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-track` (7px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--cds-page-header-title-leading`, `--cds-page-header-title-size`.

#### Page title (h1)

<a id="page-title"></a>`page-title`, on artifacts-dark, chats-dark, projects-dark.

<img src="components/crops/page-title-default.png" alt="Page title (h1), default" height="32"> <img src="components/crops/page-title-light.png" alt="Page title (h1), light" height="32"> <img src="components/crops/page-title-chats.png" alt="Page title (h1), chats" height="32"> <img src="components/crops/page-title-light-chats.png" alt="Page title (h1), light-chats" height="32"> <img src="components/crops/page-title-light-projects.png" alt="Page title (h1), light-projects" height="32"> <img src="components/crops/page-title-projects.png" alt="Page title (h1), projects" height="32"> 

| State | Values |
|---|---|
| default | size 100.08 x `density.h-control` (32); background transparent; text `typography.page-title` (Anthropic Serif 24/32 500), `text.primary` (#f0efec) |
| chats | size 178.41 x `density.h-control` (32) |
| projects | size 91.33 x `density.h-control` (32) |
| light | size 101.06 x `density.h-control` (32); background transparent; text `typography.page-title` (Anthropic Serif 24/32 500), `text.primary` (#0b0b0b) |
| light-chats | size 179.91 x `density.h-control` (32) |
| light-projects | size 92.17 x `density.h-control` (32) |

Tokens named in its classes: `--cds-page-header-title-leading`, `--cds-page-header-title-size`.

#### Tabs

<a id="tabs"></a>`tabs`, on artifacts-dark.

<img src="components/crops/tabs-default.png" alt="Tabs, default" height="32"> <img src="components/crops/tabs-light.png" alt="Tabs, light" height="32"> 

| State | Values |
|---|---|
| default | size 233.64 x `density.h-control` (32); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#f0efec) |
| light | size 234.45 x `density.h-control` (32); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#0b0b0b) |

Child layers: button 40.5469pxx32px background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) radius `radius.row` (8px)

#### Tab

<a id="tab"></a>`tab`, on artifacts-dark, artifacts-dark-loading.

<img src="components/crops/tab-default.png" alt="Tab, default" height="32"> <img src="components/crops/tab-hover.png" alt="Tab, hover" height="32"> <img src="components/crops/tab-light.png" alt="Tab, light" height="32"> <img src="components/crops/tab-light-hover.png" alt="Tab, light-hover" height="32"> <img src="components/crops/tab-selected.png" alt="Tab, selected" height="32"> <img src="components/crops/tab-focus-visible.png" alt="Tab, focus-visible" height="32"> <img src="components/crops/tab-light-focus-visible.png" alt="Tab, light-focus-visible" height="32"> <img src="components/crops/tab-light-refresh.png" alt="Tab, light-refresh" height="32"> <img src="components/crops/tab-light-refresh-focus-visible.png" alt="Tab, light-refresh-focus-visible" height="32"> <img src="components/crops/tab-light-selected.png" alt="Tab, light-selected" height="32"> <img src="components/crops/tab-light-selected-hover.png" alt="Tab, light-selected-hover" height="32"> <img src="components/crops/tab-refresh.png" alt="Tab, refresh" height="32"> <img src="components/crops/tab-refresh-focus-visible.png" alt="Tab, refresh-focus-visible" height="32"> <img src="components/crops/tab-selected-hover.png" alt="Tab, selected-hover" height="32"> 

| State | Values |
|---|---|
| default (same: refresh) | size 61.33 x `density.h-control` (32); padding 0 `density.pad-md` (12px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.muted` (#898781) |
| hover | text `typography.body-medium` (Anthropic Sans 14/20 500), `text.secondary` (#c3c2b7) |
| focus-visible, refresh-focus-visible | focus ring on the inner button: `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| selected, selected-hover | size 41.55 x `density.h-control` (32); text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#f0efec) |
| light (same: light-refresh) | size 61.5 x `density.h-control` (32); padding 0 `density.pad-md` (12px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.muted` (#898781) |
| light-hover | text `typography.body-medium` (Anthropic Sans 14/20 500), `text.secondary` (#52514e) |
| light-focus-visible, light-refresh-focus-visible | focus ring on the inner button: `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-selected, light-selected-hover | size 41.66 x `density.h-control` (32); text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#0b0b0b) |

#### Page header icon button

<a id="header-icon-button"></a>`header-icon-button`, on artifacts-dark.

<img src="components/crops/header-icon-button-default.png" alt="Page header icon button, default" height="32"> <img src="components/crops/header-icon-button-hover.png" alt="Page header icon button, hover" height="32"> <img src="components/crops/header-icon-button-light.png" alt="Page header icon button, light" height="32"> <img src="components/crops/header-icon-button-light-hover.png" alt="Page header icon button, light-hover" height="32"> <img src="components/crops/header-icon-button-focus-visible.png" alt="Page header icon button, focus-visible" height="32"> <img src="components/crops/header-icon-button-light-focus-visible.png" alt="Page header icon button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Page header button (New project)

<a id="header-button"></a>`header-button`, on projects-dark, chats-dark.

<img src="components/crops/header-button-default.png" alt="Page header button (New project), default" height="32"> <img src="components/crops/header-button-hover.png" alt="Page header button (New project), hover" height="32"> <img src="components/crops/header-button-light.png" alt="Page header button (New project), light" height="32"> <img src="components/crops/header-button-light-hover.png" alt="Page header button (New project), light-hover" height="32"> <img src="components/crops/header-button-focus-visible.png" alt="Page header button (New project), focus-visible" height="32"> <img src="components/crops/header-button-light-focus-visible.png" alt="Page header button (New project), light-focus-visible" height="32"> <img src="components/crops/header-button-light-link.png" alt="Page header button (New project), light-link" height="32"> <img src="components/crops/header-button-link.png" alt="Page header button (New project), link" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 105.56 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| link | size 54.53 x `density.h-control` (32) |
| light (same: light-hover) | size 105.92 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-link | size 54.63 x `density.h-control` (32) |

Child layers: span 104.6x31 background `fill.primary` (#ffffff) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Notice card

<a id="notice-card"></a>`notice-card`, on artifacts-dark.

<img src="components/crops/notice-card-default.png" alt="Notice card, default" height="120"> <img src="components/crops/notice-card-light.png" alt="Notice card, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x 138; radius `radius.card` (12px); background transparent; text `typography.body-semibold` (Anthropic Sans 14/20 580), `text.primary` (#f0efec) |
| light | size `layout.page-width` (960) x 138; radius `radius.card` (12px); background transparent; text `typography.body-semibold` (Anthropic Sans 14/20 580), `text.primary` (#0b0b0b) |

Child layers: div 960pxx138px radius `radius.card` (12px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); span 960x138 background `surface.1` (#151515) radius `radius.card` (12px); span 242.3x28 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-track` (7px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Secondary button in a card

<a id="card-button"></a>`card-button`, on artifacts-dark.

<img src="components/crops/card-button-default.png" alt="Secondary button in a card, default" height="28"> <img src="components/crops/card-button-hover.png" alt="Secondary button in a card, hover" height="28"> <img src="components/crops/card-button-light.png" alt="Secondary button in a card, light" height="28"> <img src="components/crops/card-button-light-hover.png" alt="Secondary button in a card, light-hover" height="28"> <img src="components/crops/card-button-focus-visible.png" alt="Secondary button in a card, focus-visible" height="28"> <img src="components/crops/card-button-light-focus-visible.png" alt="Secondary button in a card, light-focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size 242.31 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size 243.83 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Child layers: span 242.3x28 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-track` (7px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Dismiss button

<a id="dismiss-button"></a>`dismiss-button`, on artifacts-dark.

<img src="components/crops/dismiss-button-default.png" alt="Dismiss button, default" height="28"> <img src="components/crops/dismiss-button-hover.png" alt="Dismiss button, hover" height="28"> <img src="components/crops/dismiss-button-light.png" alt="Dismiss button, light" height="28"> <img src="components/crops/dismiss-button-light-hover.png" alt="Dismiss button, light-hover" height="28"> <img src="components/crops/dismiss-button-focus-visible.png" alt="Dismiss button, focus-visible" height="28"> <img src="components/crops/dismiss-button-light-focus-visible.png" alt="Dismiss button, light-focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control--sm` (28) x `density.h-control--sm` (28); radius `radius.segment-track` (7px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control--sm` (28) x `density.h-control--sm` (28); radius `radius.segment-track` (7px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Section caption (Make something new)

<a id="section-caption"></a>`section-caption`, on artifacts-dark.

<img src="components/crops/section-caption-default.png" alt="Section caption (Make something new), default" height="24"> <img src="components/crops/section-caption-light.png" alt="Section caption (Make something new), light" height="24"> 

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x 17; background transparent; text `typography.caption-medium` (Anthropic Sans 12/17 500), `text.muted` (#898781) |
| light | size `layout.page-width` (960) x 17; background transparent; text `typography.caption-medium` (Anthropic Sans 12/17 500), `text.muted` (#898781) |

#### Make something new card

<a id="template-card"></a>`template-card`, on artifacts-dark. 136 wide: a preview tile with --cds-radius-composer, then the name and a Beta badge.

<img src="components/crops/template-card-default.png" alt="Make something new card, default" height="119"> <img src="components/crops/template-card-hover.png" alt="Make something new card, hover" height="119"> <img src="components/crops/template-card-light.png" alt="Make something new card, light" height="119"> <img src="components/crops/template-card-light-hover.png" alt="Make something new card, light-hover" height="119"> <img src="components/crops/template-card-focus-visible.png" alt="Make something new card, focus-visible" height="119"> <img src="components/crops/template-card-light-focus-visible.png" alt="Make something new card, light-focus-visible" height="119"> 

| State | Values |
|---|---|
| default (same: hover) | size 136 x 119; radius `radius.template-card` (14px); background transparent; text `typography.footnote-medium` (Anthropic Sans 13/17 500), `text.primary` (#f0efec); transition transform and 3 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon 5 x 5, `text.primary` (#f0efec) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size 136 x 119; radius `radius.template-card` (14px); background transparent; text `typography.footnote-medium` (Anthropic Sans 13/17 500), `text.primary` (#0b0b0b); transition transform and 3 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon 5 x 5, `text.primary` (#0b0b0b) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Child layers: span 136x96 background `surface.2` (#1a1a19) radius `radius.template-card` (14px) shadow `shadow.sm` (rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.24) 0px 2px 8px 0px); span 136pxx96px radius `radius.template-card` (14px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); span 124x84

Tokens named in its classes: `--cds-rem-scale`, `--hue`, `--ink`, `--neutral`, `--tile-ring`.

#### Badge (Beta)

<a id="badge"></a>`badge`, on artifacts-dark, projects-dark.

<img src="components/crops/badge-default.png" alt="Badge (Beta), default" height="24"> <img src="components/crops/badge-light.png" alt="Badge (Beta), light" height="24"> <img src="components/crops/badge-light-project.png" alt="Badge (Beta), light-project" height="24"> <img src="components/crops/badge-project.png" alt="Badge (Beta), project" height="24"> 

| State | Values |
|---|---|
| default | size 29.94 x `size.switch-knob` (16); padding 0 `space.1` (4px); radius `radius.badge` (4px); background `bg.neutral` (rgba(255, 255, 255, 0.05)); text Anthropic Sans 10/12 500, `text.secondary` (#c3c2b7) |
| project | size 108.91 x `density.h-control-nested--sm` (20); padding 0 `density.pad-sm` (8px); radius 5.5px; text Anthropic Sans 12/15 500, `text.secondary` (#c3c2b7) |
| light | size 30.03 x `size.switch-knob` (16); padding 0 `space.1` (4px); radius `radius.badge` (4px); background `bg.neutral` (rgba(11, 11, 11, 0.05)); text Anthropic Sans 10/12 500, `text.secondary` (#52514e) |
| light-project | size 109.41 x `density.h-control-nested--sm` (20); padding 0 `density.pad-sm` (8px); radius 5.5px; text Anthropic Sans 12/15 500, `text.secondary` (#52514e) |

Tokens named in its classes: `--cds-rem-scale`.

#### List group heading (September)

<a id="month-heading"></a>`month-heading`, on artifacts-dark.

<img src="components/crops/month-heading-default.png" alt="List group heading (September), default" height="29"> <img src="components/crops/month-heading-light.png" alt="List group heading (September), light" height="29"> 

| State | Values |
|---|---|
| default | size 984 x 29; padding `density.pad-xs` (6px) `density.pad-md` (12px); background transparent; text `typography.caption-medium` (Anthropic Sans 12/17 500), `text.muted` (#898781) |
| light | size 984 x 29; padding `density.pad-xs` (6px) `density.pad-md` (12px); background transparent; text `typography.caption-medium` (Anthropic Sans 12/17 500), `text.muted` (#898781) |

#### Artifact list row

<a id="artifact-row"></a>`artifact-row`, on artifacts-dark. Icon, title in text-primary, a muted line ("Shared with you"), then Pin, visibility, Created or Edited with the date, and a more button.

<img src="components/crops/artifact-row-default.png" alt="Artifact list row, default" height="52"> <img src="components/crops/artifact-row-hover.png" alt="Artifact list row, hover" height="52"> <img src="components/crops/artifact-row-light.png" alt="Artifact list row, light" height="52"> <img src="components/crops/artifact-row-light-hover.png" alt="Artifact list row, light-hover" height="52"> 

| State | Values |
|---|---|
| default (same: hover) | size 984 x `layout.list-row-height` (52); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#c3c2b7) |
| light (same: light-hover) | size 984 x `layout.list-row-height` (52); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#52514e) |

Child layers: div 36x36 background `fill.disabled` (rgba(255, 255, 255, 0.05)); button 24x24 radius `radius.row` (8px); span 3x3 background `fill.control-hover` (rgba(255, 255, 255, 0.2)) radius `radius.full` (9999px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--list-header-scroll-offset`.

#### Artifact row subtitle

<a id="artifact-row-meta"></a>`artifact-row-meta`, on artifacts-dark.

<img src="components/crops/artifact-row-meta-default.png" alt="Artifact row subtitle, default" height="32"> <img src="components/crops/artifact-row-meta-light.png" alt="Artifact row subtitle, light" height="32"> 

| State | Values |
|---|---|
| default | size 130.77 x `density.h-control` (32); padding 0 `density.pad-md` (12px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.muted` (#898781) |
| light | size 131.3 x `density.h-control` (32); padding 0 `density.pad-md` (12px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.muted` (#898781) |

#### Artifact row date

<a id="artifact-row-time"></a>`artifact-row-time`, on artifacts-dark.

<img src="components/crops/artifact-row-time-default.png" alt="Artifact row date, default" height="24"> <img src="components/crops/artifact-row-time-light.png" alt="Artifact row date, light" height="24"> 

| State | Values |
|---|---|
| default | size 42.47 x `size.switch-knob` (16); background transparent; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.secondary` (#c3c2b7) |
| light | size 42.64 x `size.switch-knob` (16); background transparent; text `fontSize.footnote` / `lineHeight.footnote` at `fontWeight.regular` (Anthropic Sans 13/17 400), `text.secondary` (#52514e) |

#### Artifact row more button

<a id="artifact-row-more"></a>`artifact-row-more`, on artifacts-dark.

<img src="components/crops/artifact-row-more-default.png" alt="Artifact row more button, default" height="32"> <img src="components/crops/artifact-row-more-hover.png" alt="Artifact row more button, hover" height="32"> <img src="components/crops/artifact-row-more-light.png" alt="Artifact row more button, light" height="32"> <img src="components/crops/artifact-row-more-light-hover.png" alt="Artifact row more button, light-hover" height="32"> <img src="components/crops/artifact-row-more-focus-visible.png" alt="Artifact row more button, focus-visible" height="32"> <img src="components/crops/artifact-row-more-light-focus-visible.png" alt="Artifact row more button, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--list-header-scroll-offset`.

#### Chats list row

<a id="chats-row"></a>`chats-row`, on chats-dark, chats-dark-filter-menu. A cds Table row, 53 tall: title, then the relative time in text-muted and a more button.

<img src="components/crops/chats-row-default.png" alt="Chats list row, default" height="53"> <img src="components/crops/chats-row-hover.png" alt="Chats list row, hover" height="53"> <img src="components/crops/chats-row-light.png" alt="Chats list row, light" height="53"> <img src="components/crops/chats-row-light-hover.png" alt="Chats list row, light-hover" height="53"> <img src="components/crops/chats-row-light-refresh.png" alt="Chats list row, light-refresh" height="53"> <img src="components/crops/chats-row-light-refresh-focus-visible.png" alt="Chats list row, light-refresh-focus-visible" height="53"> <img src="components/crops/chats-row-refresh.png" alt="Chats list row, refresh" height="53"> <img src="components/crops/chats-row-refresh-focus-visible.png" alt="Chats list row, refresh-focus-visible" height="53"> 

| State | Values |
|---|---|
| default (same: hover, refresh) | size 984 x `layout.table-row-height` (53); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); placeholder `text.primary` (#f0efec) |
| refresh-focus-visible | focus ring on the inner a: `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light (same: light-hover, light-refresh) | size 984 x `layout.table-row-height` (53); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); placeholder `text.primary` (#0b0b0b) |
| light-refresh-focus-visible | focus ring on the inner a: `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

Child layers: td 984x53 border `borderWidth.default` (1px) solid transparent

Tokens named in its classes: `--cds-alpha-1`, `--cds-checkbox`, `--cds-checkbox-radius`, `--cds-cursor-interactive`, `--cds-pad-md`, `--cds-page-bg`.

#### Chats row time

<a id="chats-time"></a>`chats-time`, on chats-dark.

<img src="components/crops/chats-time-default.png" alt="Chats row time, default" height="24"> <img src="components/crops/chats-time-light.png" alt="Chats row time, light" height="24"> 

| State | Values |
|---|---|
| default | size 74.45 x `density.h-control-nested--xs` (18); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| light | size 74.83 x `density.h-control-nested--xs` (18); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |

#### Project card

<a id="project-card"></a>`project-card`, on projects-dark, projects-dark-2. Two columns of cards: name, an optional badge, a three-line description in text-secondary, the date.

<img src="components/crops/project-card-default.png" alt="Project card, default" height="120"> <img src="components/crops/project-card-hover.png" alt="Project card, hover" height="120"> <img src="components/crops/project-card-light.png" alt="Project card, light" height="120"> <img src="components/crops/project-card-light-hover.png" alt="Project card, light-hover" height="120"> <img src="components/crops/project-card-light-refresh.png" alt="Project card, light-refresh" height="120"> <img src="components/crops/project-card-light-refresh-focus-visible.png" alt="Project card, light-refresh-focus-visible" height="120"> <img src="components/crops/project-card-refresh.png" alt="Project card, refresh" height="120"> <img src="components/crops/project-card-refresh-focus-visible.png" alt="Project card, refresh-focus-visible" height="120"> 

| State | Values |
|---|---|
| default (same: hover, refresh) | size 468 x 161; background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#f0efec) |
| refresh-focus-visible | focus ring on the inner div: `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light (same: light-hover, light-refresh) | size 468 x 161; background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#0b0b0b) |
| light-refresh-focus-visible | focus ring on the inner div: `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

Child layers: div 468x161 background `surface.1` (#151515) radius `radius.card` (12px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); span 108.9x20 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius 5.5px

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--list-header-scroll-offset`.

#### Project breadcrumb

<a id="breadcrumb"></a>`breadcrumb`, on project-dark.

<img src="components/crops/breadcrumb-default.png" alt="Project breadcrumb, default" height="28"> <img src="components/crops/breadcrumb-hover.png" alt="Project breadcrumb, hover" height="28"> <img src="components/crops/breadcrumb-light.png" alt="Project breadcrumb, light" height="28"> <img src="components/crops/breadcrumb-light-hover.png" alt="Project breadcrumb, light-hover" height="28"> <img src="components/crops/breadcrumb-focus-visible.png" alt="Project breadcrumb, focus-visible" height="28"> <img src="components/crops/breadcrumb-light-focus-visible.png" alt="Project breadcrumb, light-focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size 75.22 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light (same: light-hover) | size 75.53 x `density.h-control--sm` (28); padding 0 `space.2-5` (10px); radius `radius.segment-track` (7px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Project title

<a id="project-title"></a>`project-title`, on project-dark.

<img src="components/crops/project-title-default.png" alt="Project title, default" height="31"> <img src="components/crops/project-title-light.png" alt="Project title, light" height="31"> 

| State | Values |
|---|---|
| default | size 103.02 x 31.19; background transparent; text Anthropic Serif 24/31.2 500, `text.primary` (#f0efec) |
| light | size 103.66 x 31.19; background transparent; text Anthropic Serif 24/31.2 500, `text.primary` (#0b0b0b) |

#### Project section title (Recents)

<a id="project-section-title"></a>`project-section-title`, on project-dark.

<img src="components/crops/project-section-title-default.png" alt="Project section title (Recents), default" height="24"> <img src="components/crops/project-section-title-light.png" alt="Project section title (Recents), light" height="24"> 

| State | Values |
|---|---|
| default | size 680 x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| light | size 680 x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |

#### Project recents row

<a id="project-recent-row"></a>`project-recent-row`, on project-dark.

<img src="components/crops/project-recent-row-default.png" alt="Project recents row, default" height="54"> <img src="components/crops/project-recent-row-hover.png" alt="Project recents row, hover" height="54"> <img src="components/crops/project-recent-row-light.png" alt="Project recents row, light" height="54"> <img src="components/crops/project-recent-row-light-hover.png" alt="Project recents row, light-hover" height="54"> 

| State | Values |
|---|---|
| default (same: hover) | size 704 x 54; background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light (same: light-hover) | size 704 x 54; background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Child layers: td 704x54 border `borderWidth.default` (1px) solid transparent

Tokens named in its classes: `--cds-alpha-1`, `--cds-cursor-interactive`, `--cds-pad-md`, `--cds-page-bg`.

#### Instructions card

<a id="instructions-card"></a>`instructions-card`, on project-dark. The right rail: Instructions, Memory and Context cards, each an h3 with an edit action and a two-line muted preview.

<img src="components/crops/instructions-card-default.png" alt="Instructions card, default" height="120"> <img src="components/crops/instructions-card-light.png" alt="Instructions card, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.project-rail-width` (352) x 559.5; border `borderWidth.default` (1px) solid `border.default` (rgba(255, 255, 255, 0.1)); radius `radius.rail-card` (16px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.secondary` (#c3c2b7); icon `density.icon--sm` (16) x `density.icon--sm` (16), `text.muted` (#898781); placeholder `text.primary` (#f0efec) |
| light | size `layout.project-rail-width` (352) x 559.5; border `borderWidth.default` (1px) solid `border.default` (rgba(11, 11, 11, 0.1)); radius `radius.rail-card` (16px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.secondary` (#52514e); icon `density.icon--sm` (16) x `density.icon--sm` (16), `text.muted` (#898781); placeholder `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

### Mobile

The same app at 390 wide: a Show sidebar button, the greeting and the pinned composer whose segments drop to icons, the sidebar as a full-screen drawer sheet with 44px rows, and a chat.

#### Phone menu button

<a id="m-show-sidebar"></a>`m-show-sidebar`, on mobile-home-dark.

<img src="components/crops/m-show-sidebar-default.png" alt="Phone menu button, default" height="32"> <img src="components/crops/m-show-sidebar-light.png" alt="Phone menu button, light" height="32"> 

| State | Values |
|---|---|
| default | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#c3c2b7); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size `density.h-control` (32) x `density.h-control` (32); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.secondary` (#52514e); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Phone greeting

<a id="m-greeting"></a>`m-greeting`, on mobile-home-dark.

<img src="components/crops/m-greeting-default.png" alt="Phone greeting, default" height="38"> <img src="components/crops/m-greeting-light.png" alt="Phone greeting, light" height="38"> 

| State | Values |
|---|---|
| default | size 271.59 x 37.5; padding 0 28.8px; background transparent; text Anthropic Serif 30/37.5 300, `text.primary` (#f0efec); icon 28.78 x 28.78, `text.primary` (#f0efec) |
| light | size 273.3 x 37.5; padding 0 28.8px; background transparent; text Anthropic Serif 30/37.5 330, `text.primary` (#0b0b0b); icon 28.78 x 28.78, `text.primary` (#0b0b0b) |

#### Phone composer

<a id="m-composer"></a>`m-composer`, on mobile-home-dark. Pinned to the bottom; the Chat/Cowork segments drop to icons below 360 px.

<img src="components/crops/m-composer-default.png" alt="Phone composer, default" height="100"> <img src="components/crops/m-composer-light.png" alt="Phone composer, light" height="100"> 

| State | Values |
|---|---|
| default | size 358 x 100; border `borderWidth.default` (1px) solid transparent; radius `radius.composer` (20px); background `surface.3` (#20201f); shadow `component.composer-shadow` (rgba(0, 0, 0, 0.04) 0px 4px 20px 0px, rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.muted` (#898781); transition background-color and 3 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#f0efec); placeholder `text.muted` (#898781) |
| light | size 358 x 100; border `borderWidth.default` (1px) solid transparent; radius `radius.composer` (20px); background `surface.3` (#ffffff); shadow `component.composer-shadow` (rgba(0, 0, 0, 0.04) 0px 4px 20px 0px, rgba(11, 11, 11, 0.1) 0px 0px 0px 1px); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.muted` (#898781); transition background-color and 3 more `duration.base` (0.2s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); icon `density.icon` (20) x `density.icon` (20), `text.primary` (#0b0b0b); placeholder `text.muted` (#898781) |

Tokens named in its classes: `--cds-border`, `--cds-cursor-interactive`, `--cds-page-bg`, `--cds-radius`, `--cds-segmented-control-thumb`, `--cds-segmented-control-track`.

#### Phone segment (icon only)

<a id="m-segment"></a>`m-segment`, on mobile-home-dark.

<img src="components/crops/m-segment-default.png" alt="Phone segment (icon only), default" height="26"> <img src="components/crops/m-segment-light.png" alt="Phone segment (icon only), light" height="26"> 

| State | Values |
|---|---|
| default | size `size.switch-width` (36) x 26; padding 0 `space.2-5` (10px); radius 5px; background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size `size.switch-width` (36) x 26; padding 0 `space.2-5` (10px); radius 5px; background transparent; text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--cds-radius`.

#### Drawer sheet

<a id="m-drawer"></a>`m-drawer`, on mobile-home-dark-drawer. The sidebar as a full-screen sheet: a close button and the wordmark, a full-width Search button, then the same rows at 44 tall.

<img src="components/crops/m-drawer-default.png" alt="Drawer sheet, default" height="120"> <img src="components/crops/m-drawer-light.png" alt="Drawer sheet, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.phone-width` (390) x 844; padding 0 `density.pad-sm` (8px) `density.pad-sm` (8px) `density.pad-sm` (8px); background `frame.web-sidebar-bg` (#111111); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition transform `duration.sheet` (0.3s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)); icon 68.33 x `density.icon` (20), `text.primary` (#f0efec) |
| light | size `layout.phone-width` (390) x 844; padding 0 `density.pad-sm` (8px) `density.pad-sm` (8px) `density.pad-sm` (8px); background `frame.web-sidebar-bg` (#fbfbf9); text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition transform `duration.sheet` (0.3s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)); icon 68.33 x `density.icon` (20), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--cds-shortcut-cap-ink`, `--df-hover`, `--df-nav-scrollbar-lane`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`, `--df-surface-primary`.

#### Drawer Search button

<a id="m-drawer-search"></a>`m-drawer-search`, on mobile-home-dark-drawer.

<img src="components/crops/m-drawer-search-default.png" alt="Drawer Search button, default" height="40"> <img src="components/crops/m-drawer-search-light.png" alt="Drawer Search button, light" height="40"> 

| State | Values |
|---|---|
| default | size 374 x `density.h-control--lg` (40); padding 0 `density.pad-lg` (16px); radius 10px; background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size 374 x `density.h-control--lg` (40); padding 0 `density.pad-lg` (16px); radius 10px; background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |

Child layers: span 374x40 background `fill.control` (rgba(255, 255, 255, 0.1)) radius 10px shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Drawer row

<a id="m-drawer-row"></a>`m-drawer-row`, on mobile-home-dark-drawer.

<img src="components/crops/m-drawer-row-default.png" alt="Drawer row, default" height="44"> <img src="components/crops/m-drawer-row-light.png" alt="Drawer row, light" height="44"> 

| State | Values |
|---|---|
| default | size 374 x `layout.sidebar-titlebar-height` (44); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#c3c2b7) |
| light | size 374 x `layout.sidebar-titlebar-height` (44); radius `radius.row` (8px); background transparent; text Anthropicons `density.icon` (20px, weight 433.25), `text.secondary` (#52514e) |

Child layers: a 374x44 radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-fill-accent`, `--cds-page-bg`, `--df-hover`, `--df-radius-pill`, `--df-row-ctl`, `--df-row-font`, `--df-row-gap`, `--df-row-h`, `--df-row-px`, `--df-selected`.

#### Phone chat header

<a id="m-thread-header"></a>`m-thread-header`, on mobile-thread-dark.

<img src="components/crops/m-thread-header-default.png" alt="Phone chat header, default" height="48"> <img src="components/crops/m-thread-header-light.png" alt="Phone chat header, light" height="48"> 

| State | Values |
|---|---|
| default | size `layout.phone-width` (390) x `layout.header-height` (48); padding 0 `space.5` (20px) 0 `space.14` (56px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light | size `layout.phone-width` (390) x `layout.header-height` (48); padding 0 `space.5` (20px) 0 `space.14` (56px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Child layers: div 378x72 background `surface.1` (#151515); span 57.7x28 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.segment-track` (7px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--df-ceded-gutter`, `--df-header-start-inset`.

#### Phone user message

<a id="m-user-message"></a>`m-user-message`, on mobile-thread-dark.

<img src="components/crops/m-user-message-default.png" alt="Phone user message, default" height="120"> <img src="components/crops/m-user-message-light.png" alt="Phone user message, light" height="120"> 

| State | Values |
|---|---|
| default | size 283 x 256; padding `density.pad-md` (12px) `density.pad-lg` (16px); radius `radius.card` (12px); background `fill.disabled` (rgba(255, 255, 255, 0.05)); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#f0efec) |
| light | size 283 x 256; padding `density.pad-md` (12px) `density.pad-lg` (16px); radius `radius.card` (12px); background `fill.disabled` (rgba(11, 11, 11, 0.05)); text `typography.heading-regular` (Anthropic Sans 15/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-bg-user-message`, `--cds-cursor-interactive`, `--cds-message-bubble-measure`, `--cds-message-bubble-pad-x`, `--cds-message-bubble-pad-y`, `--cds-message-bubble-radius`, `--cds-page-bg`.

### Forms and feedback

Added on 2026-10-17 from nine new copies: the tooltip, the text link, the checkbox, the confirmation and form dialogs with their primary, secondary, danger and disabled buttons, the text field (with its error state) and text area, the list search, empty result, filter menu, loading skeleton and the two page grids. Every button here was also read pressed, with the pointer held down: cds keeps the hover fill and squishes the paint layer to 97.5% (`core.press.button-scale`).

#### Text link

<a id="text-link"></a>`text-link`, on settings-dark-capabilities, settings-dark-account. cds TextLink (`a, .prose-link` in the base layer): text.accent, underlined 3px below in the link colour at 40% (--_text-link-line), the full colour on hover and focus; colour and line change on --cds-dur-fast with ease-out.

<img src="components/crops/text-link-default.png" alt="Text link, default" height="38"> <img src="components/crops/text-link-hover.png" alt="Text link, hover" height="38"> <img src="components/crops/text-link-light.png" alt="Text link, light" height="38"> <img src="components/crops/text-link-light-hover.png" alt="Text link, light-hover" height="38"> <img src="components/crops/text-link-focus-visible.png" alt="Text link, focus-visible" height="38"> <img src="components/crops/text-link-learn-more.png" alt="Text link, learn-more" height="24"> <img src="components/crops/text-link-learn-more-hover.png" alt="Text link, learn-more-hover" height="24"> <img src="components/crops/text-link-light-focus-visible.png" alt="Text link, light-focus-visible" height="38"> <img src="components/crops/text-link-light-learn-more.png" alt="Text link, light-learn-more" height="24"> <img src="components/crops/text-link-light-learn-more-hover.png" alt="Text link, light-learn-more-hover" height="24"> <img src="components/crops/text-link-light-pressed.png" alt="Text link, light-pressed" height="38"> <img src="components/crops/text-link-pressed.png" alt="Text link, pressed" height="38"> 

| State | Values |
|---|---|
| default (same: pressed) | size 671.34 x 38; radius 2px; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.accent` (#6da7ec); underline rgba(109, 167, 236, 0.4), offset `link.underline-offset` (3px); transition color `duration.fast` (0.06s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), text-decoration-color `duration.fast` (0.06s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), box-shadow `duration.fast` (0.06s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)) |
| hover | underline `text.accent` (#6da7ec), offset `link.underline-offset` (3px) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); underline `text.accent` (#6da7ec), offset `link.underline-offset` (3px); transition outline `duration.base` (0.2s) ease |
| learn-more | size 144.86 x `density.h-control-nested--xs` (18); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781); underline rgba(137, 135, 129, 0.4), offset `link.underline-offset` (3px) |
| learn-more-hover | size 144.86 x `density.h-control-nested--xs` (18); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781); underline `text.muted` (#898781), offset `link.underline-offset` (3px) |
| light (same: light-pressed) | size 676.75 x 38; radius 2px; background transparent; outline `borderWidth.thick` (2px) solid transparent, offset `focusRing.outline-offset` (2px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.accent` (#184f95); underline rgba(24, 79, 149, 0.4), offset `link.underline-offset` (3px); transition color `duration.fast` (0.06s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), text-decoration-color `duration.fast` (0.06s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), box-shadow `duration.fast` (0.06s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)) |
| light-hover | underline `text.accent` (#184f95), offset `link.underline-offset` (3px) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); underline `text.accent` (#184f95), offset `link.underline-offset` (3px); transition outline `duration.base` (0.2s) ease |
| light-learn-more | size 146.08 x `density.h-control-nested--xs` (18); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781); underline rgba(137, 135, 129, 0.4), offset `link.underline-offset` (3px) |
| light-learn-more-hover | size 146.08 x `density.h-control-nested--xs` (18); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781); underline `text.muted` (#898781), offset `link.underline-offset` (3px) |

Child layers: a 671.3x38 radius 2px

#### Tooltip

<a id="tooltip"></a>`tooltip`, on home-dark-tooltip. Base UI tooltip on the sidebar Search button: --cds-tooltip-bg / --cds-tooltip-fg, radius 6, 13/18 text, the shortcut keys inside; opens on the snap curve (--cds-dur-snap) from 98% scale, no transition under reduced motion.

<img src="components/crops/tooltip-default.png" alt="Tooltip, default" height="24"> <img src="components/crops/tooltip-light.png" alt="Tooltip, light" height="24"> 

| State | Values |
|---|---|
| default | size 100.61 x `density.h-control--xs` (24); padding 3px `density.pad-sm` (8px); radius `radius.segment-thumb` (6px); background `surface.3` (#20201f); shadow `component.dialog-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(0, 0, 0, 0.24) 0px 2px 8px 0px); text Anthropic Sans 13/18 400, `text.primary` (#f0efec); transition opacity `duration.snap` (0.12s) `easing.snap` (cubic-bezier(0.32, 0.72, 0, 1)), scale `duration.snap` (0.12s) `easing.snap` (cubic-bezier(0.32, 0.72, 0, 1)) |
| light | size 101.09 x `density.h-control--xs` (24); padding 3px `density.pad-sm` (8px); radius `radius.segment-thumb` (6px); background `fill.primary` (#0b0b0b); shadow `shadow.sm` (rgba(11, 11, 11, 0.06) 0px 1px 2px 0px, rgba(11, 11, 11, 0.08) 0px 2px 8px 0px); text Anthropic Sans 13/18 400, `on.accent` (#ffffff); transition opacity `duration.snap` (0.12s) `easing.snap` (cubic-bezier(0.32, 0.72, 0, 1)), scale `duration.snap` (0.12s) `easing.snap` (cubic-bezier(0.32, 0.72, 0, 1)) |

Tokens named in its classes: `--cds-rem-scale`, `--cds-shortcut-cap-ink`, `--cds-text-muted`, `--cds-tooltip-bg`, `--cds-tooltip-fg`, `--transform-origin`.

#### Checkbox

<a id="checkbox"></a>`checkbox`, on chats-dark-select. cds Checkbox, size xs, in the Chats table once Select is on: a --cds-checkbox square with --cds-checkbox-radius and a border-strong edge, filled with the accent and a check glyph when checked.

<img src="components/crops/checkbox-default.png" alt="Checkbox, default" height="24"> <img src="components/crops/checkbox-hover.png" alt="Checkbox, hover" height="24"> <img src="components/crops/checkbox-light.png" alt="Checkbox, light" height="24"> <img src="components/crops/checkbox-light-hover.png" alt="Checkbox, light-hover" height="24"> <img src="components/crops/checkbox-checked.png" alt="Checkbox, checked" height="24"> <img src="components/crops/checkbox-focus-visible.png" alt="Checkbox, focus-visible" height="24"> <img src="components/crops/checkbox-checked-hover.png" alt="Checkbox, checked-hover" height="24"> <img src="components/crops/checkbox-light-checked.png" alt="Checkbox, light-checked" height="24"> <img src="components/crops/checkbox-light-checked-hover.png" alt="Checkbox, light-checked-hover" height="24"> <img src="components/crops/checkbox-light-focus-visible.png" alt="Checkbox, light-focus-visible" height="24"> <img src="components/crops/checkbox-light-pressed.png" alt="Checkbox, light-pressed" height="24"> <img src="components/crops/checkbox-pressed.png" alt="Checkbox, pressed" height="24"> 

| State | Values |
|---|---|
| default | size `size.switch-knob` (16) x `size.switch-knob` (16); border `borderWidth.default` (1px) solid `border.strong` (rgba(255, 255, 255, 0.2)); radius `radius.badge` (4px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 700), `on.accent` (#ffffff) |
| hover | border `borderWidth.default` (1px) solid `border.stronger` (rgba(255, 255, 255, 0.4)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| pressed | border `borderWidth.default` (1px) solid `border.stronger` (rgba(255, 255, 255, 0.4)) |
| checked | border `borderWidth.default` (1px) solid transparent; background `fill.accent` (#2a78d6) |
| checked-hover | border `borderWidth.default` (1px) solid transparent; background `fill.accent-hover` (#3987e5) |
| light | size `size.switch-knob` (16) x `size.switch-knob` (16); border `borderWidth.default` (1px) solid `border.strong` (rgba(11, 11, 11, 0.2)); radius `radius.badge` (4px); background transparent; text Anthropicons `density.icon--sm` (16px, weight 700), `on.accent` (#ffffff) |
| light-hover | border `borderWidth.default` (1px) solid `border.stronger` (rgba(11, 11, 11, 0.4)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |
| light-pressed | border `borderWidth.default` (1px) solid `border.stronger` (rgba(11, 11, 11, 0.4)) |
| light-checked | border `borderWidth.default` (1px) solid transparent; background `fill.accent` (#2a78d6) |
| light-checked-hover | border `borderWidth.default` (1px) solid transparent; background `fill.accent-hover` (#3987e5) |

Tokens named in its classes: `--cds-checkbox`, `--cds-checkbox-radius`.

#### Selection actions (Select mode)

<a id="selection-bar"></a>`selection-bar`, on chats-dark-select. Replaces Select and New in the page header: a muted count, Select all (secondary), Delete (danger, filled) and an exit button.

<img src="components/crops/selection-bar-default.png" alt="Selection actions (Select mode), default" height="32"> <img src="components/crops/selection-bar-light.png" alt="Selection actions (Select mode), light" height="32"> 

| State | Values |
|---|---|
| default | size 283.5 x `density.h-control` (32); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| light | size 284.73 x `density.h-control` (32); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |

Child layers: span 82.7x32 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.row` (8px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px); span 67x31 background `fill.danger` (#d03b3b) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--cds-page-header-title-size`.

#### Danger button

<a id="button-danger"></a>`button-danger`, on chats-dark-delete-confirm. fill.danger with on.danger text; the only red control, used for the confirming action of a destructive dialog and the bulk Delete.

<img src="components/crops/button-danger-default.png" alt="Danger button, default" height="32"> <img src="components/crops/button-danger-hover.png" alt="Danger button, hover" height="32"> <img src="components/crops/button-danger-light.png" alt="Danger button, light" height="32"> <img src="components/crops/button-danger-light-hover.png" alt="Danger button, light-hover" height="32"> <img src="components/crops/button-danger-focus-visible.png" alt="Danger button, focus-visible" height="32"> <img src="components/crops/button-danger-light-focus-visible.png" alt="Danger button, light-focus-visible" height="32"> <img src="components/crops/button-danger-light-pressed.png" alt="Danger button, light-pressed" height="32"> <img src="components/crops/button-danger-pressed.png" alt="Danger button, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 67.95 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.danger` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus-danger on this surface` (#20201f 0px 0px 0px 1px inset, #d03b3b 0px 0px 0px 1px, rgba(142, 38, 38, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| pressed | shadow `shadow.focus-danger on this surface` (#20201f 0px 0px 0px 1px inset, #d03b3b 0px 0px 0px 1px, rgba(142, 38, 38, 0.6) 0px 0px 6px 1px); press paint layer `press.button-scale` (scale(0.975)) |
| light (same: light-hover) | size 68.16 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.danger` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus-danger on this surface` (#ffffff 0px 0px 0px 1px inset, #d03b3b 0px 0px 0px 1px, #fad6d6 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-pressed | shadow `shadow.focus-danger on this surface` (#ffffff 0px 0px 0px 1px inset, #d03b3b 0px 0px 0px 1px, #fad6d6 0px 0px 6px 1px); press paint layer `press.button-scale` (scale(0.975)) |

Child layers: span 67x31 background `fill.danger` (#d03b3b) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Secondary button

<a id="button-secondary"></a>`button-secondary`, on chats-dark-delete-confirm. fill.secondary with a 1px ring (fill.secondary-ring); takes the focus when the dialog opens, so the safe choice is the default.

<img src="components/crops/button-secondary-default.png" alt="Secondary button, default" height="32"> <img src="components/crops/button-secondary-hover.png" alt="Secondary button, hover" height="32"> <img src="components/crops/button-secondary-light.png" alt="Secondary button, light" height="32"> <img src="components/crops/button-secondary-light-hover.png" alt="Secondary button, light-hover" height="32"> <img src="components/crops/button-secondary-focus-visible.png" alt="Secondary button, focus-visible" height="32"> <img src="components/crops/button-secondary-light-focus-visible.png" alt="Secondary button, light-focus-visible" height="32"> <img src="components/crops/button-secondary-light-pressed.png" alt="Secondary button, light-pressed" height="32"> <img src="components/crops/button-secondary-pressed.png" alt="Secondary button, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 69.7 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus on this surface` (#20201f 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| pressed | press paint layer `press.button-scale` (scale(0.975)) |
| light (same: light-hover) | size 70.05 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus on this surface` (#ffffff 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-pressed | press paint layer `press.button-scale` (scale(0.975)) |

Child layers: span 69.7x32 background `fill.control` (rgba(255, 255, 255, 0.1)) radius `radius.row` (8px) shadow `shadow.field-drop` (rgba(0, 0, 0, 0.05) 0px 1px 2px 0px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Confirmation dialog

<a id="confirm-dialog"></a>`confirm-dialog`, on chats-dark-delete-confirm. cds ConfirmationDialog (role=alertdialog), at most 400 wide: a heading, one sentence, then Cancel and the action at the end; surface-3, radius card, shadow-panel-lg, over the page backdrop.

<img src="components/crops/confirm-dialog-default.png" alt="Confirmation dialog, default" height="120"> <img src="components/crops/confirm-dialog-light.png" alt="Confirmation dialog, light" height="120"> 

| State | Values |
|---|---|
| default | size 400 x 138; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)) + `shadow.lg` (rgba(11, 11, 11, 0.08) 0px 4px 8px 0px, rgba(0, 0, 0, 0.24) 0px 12px 28px -2px); text `typography.heading-medium` (Anthropic Sans 15/20 500), `text.primary` (#f0efec); transition opacity `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), scale `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), filter `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)) |
| light | size 400 x 138; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `borderWidth.default` (1px) ring `border.default` (rgba(11, 11, 11, 0.1)) + `shadow.lg` (rgba(11, 11, 11, 0.08) 0px 4px 8px 0px, rgba(11, 11, 11, 0.08) 0px 12px 28px -2px); text `typography.heading-medium` (Anthropic Sans 15/20 500), `text.primary` (#0b0b0b); transition opacity `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), scale `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), filter `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--desktop-titlebar-inset`.

#### Form dialog (Create a project)

<a id="form-dialog"></a>`form-dialog`, on projects-dark-create. A cds Dialog with a title, two labelled fields, and Cancel / Create project at the end.

<img src="components/crops/form-dialog-default.png" alt="Form dialog (Create a project), default" height="120"> <img src="components/crops/form-dialog-light.png" alt="Form dialog (Create a project), light" height="120"> 

| State | Values |
|---|---|
| default | size 520 x 348; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)) + `shadow.lg` (rgba(11, 11, 11, 0.08) 0px 4px 8px 0px, rgba(0, 0, 0, 0.24) 0px 12px 28px -2px); text `typography.title-semibold` (Anthropic Sans 22/28 580), `text.primary` (#f0efec); transition opacity `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), scale `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), filter `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)); placeholder `text.muted` (#898781) |
| light | size 520 x 348; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `borderWidth.default` (1px) ring `border.default` (rgba(11, 11, 11, 0.1)) + `shadow.lg` (rgba(11, 11, 11, 0.08) 0px 4px 8px 0px, rgba(11, 11, 11, 0.08) 0px 12px 28px -2px); text `typography.title-semibold` (Anthropic Sans 22/28 580), `text.primary` (#0b0b0b); transition opacity `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), scale `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)), filter `duration.base` (0.2s) `easing.out` (cubic-bezier(0.165, 0.84, 0.44, 1)); placeholder `text.muted` (#898781) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--desktop-titlebar-inset`.

#### Field label

<a id="field-label"></a>`field-label`, on projects-dark-create.

<img src="components/crops/field-label-default.png" alt="Field label, default" height="24"> <img src="components/crops/field-label-light.png" alt="Field label, light" height="24"> 

| State | Values |
|---|---|
| default | size 472 x 14; background transparent; text `typography.label` (Anthropic Sans 14/14 500), `text.primary` (#f0efec) |
| light | size 472 x 14; background transparent; text `typography.label` (Anthropic Sans 14/14 500), `text.primary` (#0b0b0b) |

#### Text field

<a id="text-field"></a>`text-field`, on projects-dark-create. cds TextInput: control height, fill.field with a 1px fill.field-ring, border-strong on hover, the focus ring on focus.

<img src="components/crops/text-field-default.png" alt="Text field, default" height="32"> <img src="components/crops/text-field-hover.png" alt="Text field, hover" height="32"> <img src="components/crops/text-field-light.png" alt="Text field, light" height="32"> <img src="components/crops/text-field-light-hover.png" alt="Text field, light-hover" height="32"> <img src="components/crops/text-field-focus-visible.png" alt="Text field, focus-visible" height="32"> <img src="components/crops/text-field-light-focus-visible.png" alt="Text field, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size 472 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.05)); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| hover | shadow `borderWidth.default` (1px) ring inset `border.strong` (rgba(255, 255, 255, 0.2)) |
| focus-visible | shadow `shadow.focus on this surface` (#20201f 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light | size 472 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.5)); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(11, 11, 11, 0.1)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| light-hover | shadow `borderWidth.default` (1px) ring inset `border.strong` (rgba(11, 11, 11, 0.2)) |
| light-focus-visible | shadow `shadow.focus on this surface` (#ffffff 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

#### Text field, invalid

<a id="text-field-invalid"></a>`text-field-invalid`, on projects-dark-create. The error state, read by setting data-invalid on the field in the copy, which is what cds Field does when validation fails: Claude's own `data-[invalid]:` rules then draw a 1px fill.danger ring, keep it on hover, and switch the focus ring to shadow.focus-danger. The live form was never submitted, so the message text cds shows under the field was not seen.

<img src="components/crops/text-field-invalid-default.png" alt="Text field, invalid, default" height="32"> <img src="components/crops/text-field-invalid-hover.png" alt="Text field, invalid, hover" height="32"> <img src="components/crops/text-field-invalid-light.png" alt="Text field, invalid, light" height="32"> <img src="components/crops/text-field-invalid-light-hover.png" alt="Text field, invalid, light-hover" height="32"> <img src="components/crops/text-field-invalid-focus-visible.png" alt="Text field, invalid, focus-visible" height="32"> <img src="components/crops/text-field-invalid-light-focus-visible.png" alt="Text field, invalid, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 472 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.05)); shadow `borderWidth.default` (1px) ring inset `fill.danger` (#d03b3b); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| focus-visible | shadow `shadow.focus-danger on this surface` (#20201f 0px 0px 0px 1px inset, #d03b3b 0px 0px 0px 1px, rgba(142, 38, 38, 0.6) 0px 0px 6px 1px) |
| light (same: light-hover) | size 472 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.5)); shadow `borderWidth.default` (1px) ring inset `fill.danger` (#d03b3b); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| light-focus-visible | shadow `shadow.focus-danger on this surface` (#ffffff 0px 0px 0px 1px inset, #d03b3b 0px 0px 0px 1px, #fad6d6 0px 0px 6px 1px) |

#### Text area

<a id="text-area"></a>`text-area`, on projects-dark-create. cds TextArea: the text field's fill, ring and focus, several lines tall, resizable.

<img src="components/crops/text-area-default.png" alt="Text area, default" height="80"> <img src="components/crops/text-area-hover.png" alt="Text area, hover" height="80"> <img src="components/crops/text-area-light.png" alt="Text area, light" height="80"> <img src="components/crops/text-area-light-hover.png" alt="Text area, light-hover" height="80"> <img src="components/crops/text-area-focus-visible.png" alt="Text area, focus-visible" height="80"> <img src="components/crops/text-area-light-focus-visible.png" alt="Text area, light-focus-visible" height="80"> 

| State | Values |
|---|---|
| default | size 472 x 80; padding `density.pad-sm` (8px) `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.05)); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| hover | shadow `borderWidth.default` (1px) ring inset `border.strong` (rgba(255, 255, 255, 0.2)) |
| focus-visible | shadow `shadow.focus on this surface` (#20201f 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light | size 472 x 80; padding `density.pad-sm` (8px) `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.5)); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(11, 11, 11, 0.1)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| light-hover | shadow `borderWidth.default` (1px) ring inset `border.strong` (rgba(11, 11, 11, 0.2)) |
| light-focus-visible | shadow `shadow.focus on this surface` (#ffffff 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

#### Primary button

<a id="button-primary"></a>`button-primary`, on projects-dark-create. fill.primary (ink: white in dark, black in light) with on.primary text.

<img src="components/crops/button-primary-default.png" alt="Primary button, default" height="32"> <img src="components/crops/button-primary-hover.png" alt="Primary button, hover" height="32"> <img src="components/crops/button-primary-light.png" alt="Primary button, light" height="32"> <img src="components/crops/button-primary-light-hover.png" alt="Primary button, light-hover" height="32"> <img src="components/crops/button-primary-focus-visible.png" alt="Primary button, focus-visible" height="32"> <img src="components/crops/button-primary-light-focus-visible.png" alt="Primary button, light-focus-visible" height="32"> <img src="components/crops/button-primary-light-pressed.png" alt="Primary button, light-pressed" height="32"> <img src="components/crops/button-primary-pressed.png" alt="Primary button, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 120.98 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus on this surface` (#20201f 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| pressed | press paint layer `press.button-scale` (scale(0.975)) |
| light (same: light-hover) | size 121.45 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus on this surface` (#ffffff 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-pressed | press paint layer `press.button-scale` (scale(0.975)) |

Child layers: span 120x31 background `fill.primary` (#ffffff) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Disabled button

<a id="button-disabled"></a>`button-disabled`, on settings-dark-account. Delete account while a paid plan is active: the secondary button at the disabled opacity; hover and press change nothing.

<img src="components/crops/button-disabled-default.png" alt="Disabled button, default" height="32"> <img src="components/crops/button-disabled-hover.png" alt="Disabled button, hover" height="32"> <img src="components/crops/button-disabled-light.png" alt="Disabled button, light" height="32"> <img src="components/crops/button-disabled-light-hover.png" alt="Disabled button, light-hover" height="32"> <img src="components/crops/button-disabled-light-pressed.png" alt="Disabled button, light-pressed" height="32"> <img src="components/crops/button-disabled-pressed.png" alt="Disabled button, pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 124.64 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); opacity `opacity.disabled` (0.4) |
| light (same: light-hover, light-pressed) | size 125.09 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); opacity `opacity.disabled` (0.4) |

Child layers: span 123.6x31 background `fill.primary` (#ffffff) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

#### Disabled switch

<a id="switch-disabled"></a>`switch-disabled`, on settings-dark-capabilities. Artifacts, on and locked while another setting needs it: the switch at the disabled opacity.

<img src="components/crops/switch-disabled-default.png" alt="Disabled switch, default" height="24"> <img src="components/crops/switch-disabled-hover.png" alt="Disabled switch, hover" height="24"> <img src="components/crops/switch-disabled-light.png" alt="Disabled switch, light" height="24"> <img src="components/crops/switch-disabled-light-hover.png" alt="Disabled switch, light-hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size `size.switch-width` (36) x `density.h-control-nested--sm` (20); padding `space.0-5` (2px); radius `radius.full` (9999px); background `fill.accent` (#2a78d6); opacity `opacity.disabled` (0.4) |
| light (same: light-hover) | size `size.switch-width` (36) x `density.h-control-nested--sm` (20); padding `space.0-5` (2px); radius `radius.full` (9999px); background `fill.accent` (#2a78d6); opacity `opacity.disabled` (0.4) |

Tokens named in its classes: `--cds-switch-h`, `--cds-switch-knob`, `--cds-switch-track`, `--cds-switch-track-hover`.

#### List search field

<a id="search-input"></a>`search-input`, on chats-dark-search-empty. Chats and tasks search, opened from the header icon: a text field with a leading glyph and a clear button.

<img src="components/crops/search-input-default.png" alt="List search field, default" height="32"> <img src="components/crops/search-input-light.png" alt="List search field, light" height="32"> <img src="components/crops/search-input-focus-visible.png" alt="List search field, focus-visible" height="32"> <img src="components/crops/search-input-light-focus-visible.png" alt="List search field, light-focus-visible" height="32"> 

| State | Values |
|---|---|
| default | size 384 x `density.h-control` (32); padding 0 5px 0 `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.05)); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.muted` (#898781); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px) |
| light | size 384 x `density.h-control` (32); padding 0 5px 0 `density.pad-md` (12px); radius `radius.row` (8px); background `fill.field` (rgba(255, 255, 255, 0.5)); shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(11, 11, 11, 0.1)); text Anthropicons `density.icon--sm` (16px, weight 533.25), `text.muted` (#898781); transition color and 22 more `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `text.muted` (#898781) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px) |

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-h-control`, `--cds-h-control-nested`, `--cds-pad-sm`, `--cds-page-bg`, `--cds-radius`, `--cds-text-muted`, `--cds-text-stays-secondary`, `--fh`, `--fhn`, `--fr`.

#### Empty result

<a id="empty-state"></a>`empty-state`, on chats-dark-search-empty. One centred muted line quoting the query; no illustration, no action.

<img src="components/crops/empty-state-default.png" alt="Empty result, default" height="24"> <img src="components/crops/empty-state-light.png" alt="Empty result, light" height="24"> 

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |
| light | size `layout.page-width` (960) x `density.h-control-nested--sm` (20); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.muted` (#898781) |

#### Filter menu

<a id="filter-menu"></a>`filter-menu`, on chats-dark-filter-menu. The Chats filter: All, Chat, Shared, Cowork, Archived, the current one ticked in the accent.

<img src="components/crops/filter-menu-default.png" alt="Filter menu, default" height="120"> <img src="components/crops/filter-menu-light.png" alt="Filter menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 128 x 169; radius `radius.card` (12px); background `surface.3` (#20201f); shadow `component.panel-shadow` (rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.32) 0px 8px 24px 0px, rgba(0, 0, 0, 0.2) 0px 2px 6px 0px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light | size 128 x 168; radius `radius.card` (12px); background `surface.3` (#ffffff); shadow `component.panel-shadow` (rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.12) 0px 8px 24px 0px, rgba(0, 0, 0, 0.08) 0px 2px 6px 0px); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--available-height`, `--cds-h-control`, `--cds-leading-body`, `--cds-menu-gutter`, `--cds-radius`, `--cds-rem-scale`, `--cds-ring-inner`, `--cds-text-muted`.

#### Filter menu item

<a id="filter-menu-item"></a>`filter-menu-item`, on chats-dark-filter-menu.

<img src="components/crops/filter-menu-item-default.png" alt="Filter menu item, default" height="32"> <img src="components/crops/filter-menu-item-hover.png" alt="Filter menu item, hover" height="32"> <img src="components/crops/filter-menu-item-light.png" alt="Filter menu item, light" height="32"> <img src="components/crops/filter-menu-item-light-hover.png" alt="Filter menu item, light-hover" height="32"> <img src="components/crops/filter-menu-item-checked.png" alt="Filter menu item, checked" height="32"> <img src="components/crops/filter-menu-item-light-checked.png" alt="Filter menu item, light-checked" height="32"> 

| State | Values |
|---|---|
| default (same: hover, checked) | size 120 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light (same: light-hover, light-checked) | size 120 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background transparent; text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-text-muted`.

#### Menu item, keyboard focus

<a id="menu-item-keyboard"></a>`menu-item-keyboard`, on chats-dark-filter-menu. Keyboard focus in a cds Menu: Base UI moves focus to the item with the arrow keys and marks it data-highlighted, which paints the same fill.ghost-hover wash as the pointer; there is no ring. Read by setting data-highlighted and focusing the item in the copy, since the copy runs no scripts. Every cds Menu (plus, model, account, chat row, More, filter) uses this item.

<img src="components/crops/menu-item-keyboard-default.png" alt="Menu item, keyboard focus, default" height="32"> <img src="components/crops/menu-item-keyboard-light.png" alt="Menu item, keyboard focus, light" height="32"> 

| State | Values |
|---|---|
| default | size 120 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#f0efec) |
| light | size 120 x `density.h-control` (32); padding `density.pad-xs` (6px) `space.2-5` (10px); radius `radius.row` (8px); background `fill.ghost-hover` (rgba(11, 11, 11, 0.05)); text `typography.body-regular` (Anthropic Sans 14/20 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-h-control`, `--cds-leading-body`, `--cds-text-muted`.

#### Loading skeleton

<a id="skeleton"></a>`skeleton`, on artifacts-dark-loading. cds Skeleton: a --cds-skeleton-base bar with a --cds-skeleton-sheen band sweeping across every 2s (cds-shimmer); the sheen is hidden under reduced motion.

<img src="components/crops/skeleton-default.png" alt="Loading skeleton, default" height="120"> <img src="components/crops/skeleton-light.png" alt="Loading skeleton, light" height="120"> 

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x 148; radius `radius.row` (8px); background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); text Anthropic Sans 14/21 400, `text.primary` (#f0efec) |
| light | size `layout.page-width` (960) x 148; radius `radius.row` (8px); background `fill.disabled` (rgba(11, 11, 11, 0.05)); text Anthropic Sans 14/21 400, `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-skeleton-base`, `--cds-skeleton-sheen`.

#### Loading card

<a id="skeleton-card"></a>`skeleton-card`, on artifacts-dark-loading.

<img src="components/crops/skeleton-card-default.png" alt="Loading card, default" height="24"> <img src="components/crops/skeleton-card-light.png" alt="Loading card, light" height="24"> 

| State | Values |
|---|---|
| default | size 138 x 11; radius `radius.row` (8px); background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)); text `typography.caption-regular` (Anthropic Sans 12/17 400), `text.primary` (#f0efec) |
| light | size 138 x 11; radius `radius.row` (8px); background `fill.disabled` (rgba(11, 11, 11, 0.05)); text `typography.caption-regular` (Anthropic Sans 12/17 400), `text.primary` (#0b0b0b) |

Tokens named in its classes: `--cds-skeleton-base`, `--cds-skeleton-sheen`.

#### Artifacts card grid

<a id="artifacts-grid"></a>`artifacts-grid`, on artifacts-dark-loading. The Artifacts page as a grid of cards (loading), read for its column count and gap.

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x 492; background transparent; text Anthropic Sans 14/21 400, `text.primary` (#f0efec) |
| light | size `layout.page-width` (960) x 492; background transparent; text Anthropic Sans 14/21 400, `text.primary` (#0b0b0b) |

Child layers: div 304x234 background `surface.2` (#1a1a19) radius `radius.card` (12px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); div 302x1 border `borderWidth.default` (1px) solid `alpha.1` (rgba(255, 255, 255, 0.05)); div 193.2x14 background `fill.ghost-hover` (rgba(255, 255, 255, 0.07)) radius `radius.row` (8px)

Tokens named in its classes: `--cds-skeleton-base`, `--cds-skeleton-sheen`.

#### Projects card grid

<a id="projects-grid"></a>`projects-grid`, on projects-dark-2. The Projects page grid of cards, read for its column count and gap.

| State | Values |
|---|---|
| default | size `layout.page-width` (960) x 161; background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#f0efec) |
| light | size `layout.page-width` (960) x 161; background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `text.primary` (#0b0b0b) |

Child layers: div 468x161 background `surface.1` (#151515) radius `radius.card` (12px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1)); span 108.9x20 background `fill.disabled` (rgba(255, 255, 255, 0.05)) radius 5.5px; div 468x161 background `surface.1` (#151515) radius `radius.card` (12px) shadow `borderWidth.default` (1px) ring inset `border.default` (rgba(255, 255, 255, 0.1))

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`, `--list-header-scroll-offset`.

#### Primary button on a page (New project)

<a id="button-primary-page"></a>`button-primary-page`, on projects-dark-2.

<img src="components/crops/button-primary-page-default.png" alt="Primary button on a page (New project), default" height="32"> <img src="components/crops/button-primary-page-hover.png" alt="Primary button on a page (New project), hover" height="32"> <img src="components/crops/button-primary-page-light.png" alt="Primary button on a page (New project), light" height="32"> <img src="components/crops/button-primary-page-light-hover.png" alt="Primary button on a page (New project), light-hover" height="32"> <img src="components/crops/button-primary-page-focus-visible.png" alt="Primary button on a page (New project), focus-visible" height="32"> <img src="components/crops/button-primary-page-light-focus-visible.png" alt="Primary button on a page (New project), light-focus-visible" height="32"> <img src="components/crops/button-primary-page-light-pressed.png" alt="Primary button on a page (New project), light-pressed" height="32"> <img src="components/crops/button-primary-page-pressed.png" alt="Primary button on a page (New project), pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 105.56 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#0b0b0b); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | shadow `shadow.focus` (#151515 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, rgba(24, 79, 149, 0.6) 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| pressed | press paint layer `press.button-scale` (scale(0.975)) |
| light (same: light-hover) | size 105.92 x `density.h-control` (32); padding 0 `density.pad-md` (12px); radius `radius.row` (8px); background transparent; text `typography.body-medium` (Anthropic Sans 14/20 500), `on.primary` (#ffffff); transition box-shadow `duration.fast` (0.06s) `easing.tailwind-default` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | shadow `shadow.focus` (#fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px); transition outline `duration.base` (0.2s) ease |
| light-pressed | press paint layer `press.button-scale` (scale(0.975)) |

Child layers: span 104.6x31 background `fill.primary` (#ffffff) radius `radius.row` (8px)

Tokens named in its classes: `--cds-cursor-interactive`, `--cds-page-bg`.

## Icon index

74 icons were lifted from the pages into [icons/](icons), indexed in [icons/INDEX.tsv](icons/INDEX.tsv). Claude draws nearly every glyph with its own variable icon font, Anthropicons-Variable: one private-use character per icon in a `span[data-cds=Icon]`, at 12, 16 or 20 px, with the weight thinned as the size grows (577.8 at 12, 533.3 at 16, 433.3 at 20) so the stroke looks the same. [icons.mjs](tools/capture/icons.mjs) draws each glyph's outline from the font at the weight it was shown at; the names come from the labels of the controls they sat in. The few inline SVGs are the Claude wordmark, the clay asterisk, the incognito ghost, the voice bars and the GitHub mark. All are Anthropic's property (GitHub's mark is GitHub's), kept for reference only.

| Icon | Source | Sizes | Seen with |
|---|---|---|---|
| `more-vertical` | icon font U+E062 | 16px 20px | More options for |
| `code` | icon font U+E048 | 20px 16px | Code // Search results // Settings |
| `artifacts` | icon font U+E017 | 20px | Search results |
| `pin` | icon font U+E0BD | 16px 20px | Pin // Pin project //  |
| `plus` | icon font U+E001 | 16px 20px | New from a template // Add files, connectors, and more // Add files |
| `chevron-down` | icon font U+E027 | 12px 20px 16px | Sidebar // More navigation items // More options for |
| `lock` | icon font U+E0A1 | 16px | - |
| `chevron-right` | icon font U+E02A | 12px 16px |  // Effort // More models |
| `check` | icon font U+E03B | 16px 20px | Opus 5.5 //  //  |
| `arrow-up-right` | icon font U+E015 | 16px 20px | View all |
| `search` | icon font U+E0D3 | 16px 20px | Search // Sidebar // Search your artifacts |
| `filter` | icon font U+E070 | 16px 20px | Filter and group recents // Filter by type: All types // Filter by |
| `apps` | icon font U+E18A | 16px 20px | Get apps and extensions //  |
| `home` | icon font U+E08A | 16px | Home |
| `sidebar` | icon font U+E0DD | 16px | Hide sidebar // Show sidebar |
| `quick-task` | icon font U+E120 | 16px | Quick task |
| `globe` | icon font U+E082 | 16px 20px |  // Settings |
| `arrow-up` | icon font U+E013 | 20px | Send message |
| `chat-bubble` | icon font U+E031 | 20px | Search results |
| `microphone` | icon font U+E0AB | 20px | Press and hold to record // Turn on microphone |
| `copy` | icon font U+E056 | 20px 16px | Copy to clipboard // Copy |
| `cowork` | icon font U+E0F1 | 16px 20px | Cowork //  // Search results |
| `chat` | icon font U+E037 | 16px | Chat //  |
| `palette` | icon font U+E0B8 | 20px |  // Settings |
| `close` | icon font U+E10F | 20px | Close sidebar // Close // Dismiss |
| `retry` | icon font U+E11D | 16px | Retry |
| `organization` | icon font U+E0B6 | 16px | - |
| `speaker` | icon font U+E0E4 | 16px | Read aloud |
| `thumbs-down` | icon font U+E0F9 | 16px | Bad response |
| `thumbs-up` | icon font U+E0FB | 16px | Good response |
| `arrow-down` | icon font U+E009 | 20px | Scroll to bottom |
| `clock` | icon font U+E043 | 20px | Search results //  |
| `pencil` | icon font U+E064 | 16px 20px | Edit // Edit instructions //  |
| `project` | icon font U+E0C9 | 20px |  |
| `connectors` | icon font U+E055 | 20px | Settings //  |
| `grid` | icon font U+E084 | 20px | Grid view |
| `memory` | icon font U+E0A8 | 20px | Settings //  |
| `plugin` | icon font U+E0C5 | 20px | Settings //  |
| `scroll` | icon font U+E0D2 | 20px | Settings //  |
| `settings` | icon font U+E0D6 | 20px | Settings //  |
| `briefcase` | icon font U+E100 | 20px | Settings //  |
| `usage` | icon font U+E130 | 20px | Settings //  |
| `external-link` | icon font U+E00E | 16px |  |
| `return` | icon font U+E00F | 16px | Search results |
| `paperclip` | icon font U+E019 | 20px |  |
| `screenshot` | icon font U+E025 | 20px |  |
| `checklist` | icon font U+E03F | 20px |  |
| `monitor` | icon font U+E053 | 20px | System |
| `credit-card` | icon font U+E058 | 20px | Settings |
| `folder` | icon font U+E072 | 20px |  |
| `help` | icon font U+E088 | 20px |  |
| `info` | icon font U+E08F | 20px |  |
| `key` | icon font U+E091 | 20px |  |
| `shield` | icon font U+E0A3 | 20px | Settings |
| `log-out` | icon font U+E0A4 | 20px |  |
| `moon` | icon font U+E0B0 | 20px | Dark |
| `moon-sparkle` | icon font U+E0B2 | 20px | Settings |
| `research` | icon font U+E0D0 | 20px |  |
| `sort` | icon font U+E0E3 | 20px | Sort projects |
| `sun` | icon font U+E0EE | 20px | Light |
| `trash` | icon font U+E101 | 20px |  |
| `user` | icon font U+E105 | 20px | Settings |
| `claude-wordmark` | inline svg | 68x20 | Claude |
| `voice-bars` | inline svg | 20x20 | Use voice mode |
| `claude-asterisk` | inline svg | 36x36 29x29 32x32 | - |
| `incognito` | inline svg | 20x20 | Use incognito |
| `cursor-a` | inline svg | 12x14 | Design, Beta // Docs, Beta // Slides, Beta |
| `cursor-b` | inline svg | 12x14 | Design, Beta // Docs, Beta // Slides, Beta |
| `template-tile-dot` | inline svg | 5x5 | Docs, Beta |
| `lock-small` | inline svg | 16x16 | - |
| `github` | inline svg | 20x20 | Add from GitHub |
| `reflect` | inline svg | 20x20 | Settings |

## Gaps

- Captured 2026-10-04 from the owner's signed-in account (Max plan) in dark mode, at 1440 x 900 and 390 x 844. The light readings and screenshots come from the same copies with every `[data-mode]` set to light, which is all Claude's own switch does; no account setting changed. Anything Claude swaps per theme in JavaScript rather than CSS would not have swapped.
- The capture pane was hidden, so the page ran no animation frames. Base UI clears a popup's `data-starting-style` and unmounts a closed one from a frame, so entrance animations froze and closed menus stayed mounted; [snapshot.js](tools/capture/signed-in/snapshot.js) drops closed popups and settles opening ones. Modal backdrops may render undimmed. The first model in the model menu shows a highlight that is the frozen keyboard highlight, not a hover. On the phone the drawer sheet could not be closed (its exit animation never ran), so it was hidden by hand before the phone chat copy.
- Syntax-highlighted code keeps the dark theme's inline colours, so code colours in the light renders are not trustworthy; read them from the dark copies.
- The thread is not virtualised: one copy rendered at three scroll positions (`thread-dark`, `-table` at 1150, `-followup` at 1780). Its replies hold a code block, a table and paragraphs but no visible heading or list; the prose heading sizes are in [raw/css-vars.json](raw/css-vars.json) (`--_prose-h*`), not measured. The user message carries the only list.
- Artifact previews are iframes and render as dark boxes where present.
- Hover and focus on the 390 wide copies were not measured (a phone has neither). The segmented controls' radio spans take no focus in a static copy, so their focus-visible state is skipped.
- Refreshed 2026-10-17 with nine more copies (Forms and feedback, and the overlays marked with that date). The 2026-10-04 screenshots and crops were not retaken, so the two days sit side by side: the Artifacts page is a list in the first and a grid of cards in the second.
- Focus was not read on the code block's copy button, the chat title's more button, search results, Artifacts list rows and a project's recent rows: their 2026-10-04 copies are gone and no 2026-10-17 copy shows them. The search dialog's field row shows no ring when its text area takes focus; the caret is the only sign.
- A toast was not captured: the toast region is mounted on every page but stayed empty, and the actions that raise one change the account. The text field's error state was read by setting `data-invalid` on the copy, so its ring is Claude's own CSS but the message under the field was never seen. A button's loading state needs a sent message.
- Streaming (a reply being written, the stop button), the artifact panel beside a chat, the Code mode, Cowork, the share sheet, and the Privacy, Billing and Usage settings panes were not captured: each would need sending a message or shows account and billing details.
- Chat and artifact titles are the owner's own. The account's name was replaced with "Learner" and its email with an example address, and two health-related titles were replaced with neutral ones, by the redaction file, which lives outside the repository.

