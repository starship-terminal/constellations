# ChatGPT components

The discovery list of every page and state captured, the checklist coverage, the shared values, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from chatgpt.com on 2026-10-17, signed in to the owner's account (Free plan, dark theme, blue accent), as static copies of each page state rendered in headless Chromium at 1440 x 900 (the Phone group at 390 x 844), with computed styles read from the rendered copy in both themes. Nothing was sent, created or deleted in the account; the only actions were hovering, keyboard focus, opening menus and dialogs and closing them, and typing into the composer and the search fields without sending.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (114 components, 588 states). Page geometry is in [raw/layout.json](raw/layout.json).

How to read an entry:

- Values are written as tokens from [tokens.json](tokens.json): a colour is the token in that theme's set whose value is the same (`role.text.primary`, `surface.card`, `variant.primary.soft.bg-hover`), a padding, radius or control height the core token that holds it (`spacing.2`, `radius.2xl`, `size.control.lg`). Text is the typography style with the same size, line height and weight (`typography.text-sm`), that style at another weight, or a `fontSize` token with its line height and a `fontWeight` token, then its colour. A raw value is written only where no token holds it.
- Dark states come first (every page was captured dark), then the same states read in light. Each theme's first row lists every value; later rows of that theme list only what changes. A state with the same values as its theme's first is named in that label, for example "default (same: pressed)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component from the rendered copy, in [components/crops/](components/crops) (584 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`, 1440 x 900 at 2x; `-full` shots are whole pages of the dark home, Library and Plugins; phone shots are `mobile-{page}-{theme}-{state}.png`, 390 x 844 at 2x. Every state exists in both themes.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Captured at rest, with a tooltip, the + menu, a chat row's menu, the account menu, the delete confirmation, the search dialog (empty and with no results), a line typed in the composer, and with the sidebar hidden. | `/` | [chat-menu (dark)](screenshots/home-dark-chat-menu.png), [composer-typed (dark)](screenshots/home-dark-composer-typed.png), [delete-confirm (dark)](screenshots/home-dark-delete-confirm.png), [full (dark)](screenshots/home-dark-full.png), [plus-menu (dark)](screenshots/home-dark-plus-menu.png), [search-empty (dark)](screenshots/home-dark-search-empty.png), [search (dark)](screenshots/home-dark-search.png), [sidebar-collapsed (dark)](screenshots/home-dark-sidebar-collapsed.png), [tooltip (dark)](screenshots/home-dark-tooltip.png), [user-menu (dark)](screenshots/home-dark-user-menu.png), [default (dark)](screenshots/home-dark.png), [chat-menu (light)](screenshots/home-light-chat-menu.png), [composer-typed (light)](screenshots/home-light-composer-typed.png), [delete-confirm (light)](screenshots/home-light-delete-confirm.png), [plus-menu (light)](screenshots/home-light-plus-menu.png), [search-empty (light)](screenshots/home-light-search-empty.png), [search (light)](screenshots/home-light-search.png), [sidebar-collapsed (light)](screenshots/home-light-sidebar-collapsed.png), [tooltip (light)](screenshots/home-light-tooltip.png), [user-menu (light)](screenshots/home-light-user-menu.png), [default (light)](screenshots/home-light.png) |
| Two threads, their text replaced by same-length filler: one with code blocks (at the bottom, and at its user turn), one with a table and citations. | `/c/<id>` | [code (dark)](screenshots/thread-dark-code.png), [table (dark)](screenshots/thread-dark-table.png), [user-turn (dark)](screenshots/thread-dark-user-turn.png), [code (light)](screenshots/thread-light-code.png), [table (light)](screenshots/thread-light-table.png), [user-turn (light)](screenshots/thread-light-user-turn.png) |
| Library, grid view, Suggested tab; the error state (the capture guard refused the file list request) and a search with a partial-results banner. | `/library` | [error (dark)](screenshots/library-dark-error.png), [full (dark)](screenshots/library-dark-full.png), [search-error (dark)](screenshots/library-dark-search-error.png), [default (dark)](screenshots/library-dark.png), [error (light)](screenshots/library-light-error.png), [search-error (light)](screenshots/library-light-search-error.png), [default (light)](screenshots/library-light.png) |
| Images, Trending tab. | `/images` | [default (dark)](screenshots/images-dark.png), [default (light)](screenshots/images-light.png) |
| Plugins. | `/plugins` | [full (dark)](screenshots/plugins-dark-full.png), [default (dark)](screenshots/plugins-dark.png), [default (light)](screenshots/plugins-light.png) |
| Settings: General, Appearance (and its accent listbox), Keyboard, Data controls, Archived chats, Notifications (with a channel menu open). | `/settings/...` | [accent-menu (dark)](screenshots/settings-dark-accent-menu.png), [appearance (dark)](screenshots/settings-dark-appearance.png), [archived (dark)](screenshots/settings-dark-archived.png), [data-controls (dark)](screenshots/settings-dark-data-controls.png), [general (dark)](screenshots/settings-dark-general.png), [keyboard (dark)](screenshots/settings-dark-keyboard.png), [notifications-menu (dark)](screenshots/settings-dark-notifications-menu.png), [accent-menu (light)](screenshots/settings-light-accent-menu.png), [appearance (light)](screenshots/settings-light-appearance.png), [archived (light)](screenshots/settings-light-archived.png), [data-controls (light)](screenshots/settings-light-data-controls.png), [general (light)](screenshots/settings-light-general.png), [keyboard (light)](screenshots/settings-light-keyboard.png), [notifications-menu (light)](screenshots/settings-light-notifications-menu.png) |
| The Upgrade dialog over the home. | `/#pricing` | [default (dark)](screenshots/pricing-dark.png), [default (light)](screenshots/pricing-light.png) |
| Home at 390, and the drawer. | `/` | [drawer (dark)](screenshots/mobile-home-dark-drawer.png), [default (dark)](screenshots/mobile-home-dark.png), [drawer (light)](screenshots/mobile-home-light-drawer.png), [default (light)](screenshots/mobile-home-light.png) |
| The code thread at 390, top and bottom. | `/c/<id>` | [bottom (dark)](screenshots/mobile-thread-dark-bottom.png), [default (dark)](screenshots/mobile-thread-dark.png), [bottom (light)](screenshots/mobile-thread-light-bottom.png), [default (light)](screenshots/mobile-thread-light.png) |

## Checklist coverage

The 19 components of the checklist in [docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md), with the entries below that show each one and the states measured across them.

| Component | Entries | States measured |
|---|---|---|
| Button | [promo-button](#promo-button), [button-secondary](#button-secondary), [button-danger](#button-danger), [button-outline](#button-outline), [library-new](#library-new), [pricing-primary](#pricing-primary), [button-disabled](#button-disabled) | default, hover, focus-visible, pressed, disabled |
| Icon button | [header-icon-button](#header-icon-button), [sidebar-icon-button](#sidebar-icon-button), [composer-plus](#composer-plus), [voice-button](#voice-button), [send-button](#send-button), [code-block-button](#code-block-button) | default, hover, focus-visible, pressed |
| Link | [md-link](#md-link), [text-link](#text-link), [archived-link](#archived-link), [header-upgrade](#header-upgrade) | default, hover, focus-visible, pressed |
| Text field | [search-field](#search-field), [library-search](#library-search), [plugins-search](#plugins-search), [archived-search](#archived-search), [color-field](#color-field) | default, hover, focus-visible, typed |
| Text area | [composer](#composer) | default, focus-visible, typed, thread |
| Select | [select](#select), [code-theme-select](#code-theme-select), [accent-menu](#accent-menu) | default, hover, focus-visible, pressed, open |
| Checkbox | [checkbox](#checkbox), [checkbox-menu-item](#checkbox-menu-item) | default, hover, focus-visible |
| Radio | [segmented-radio](#segmented-radio), [mode-segment](#mode-segment) | default, hover, focus-visible, pressed, selected, checked, selected-hover |
| Switch | [switch-on](#switch-on), [switch-off](#switch-off), [keyboard-switch](#keyboard-switch) | default, hover, focus-visible, pressed |
| Tabs | [library-tab](#library-tab), [search-tab](#search-tab), [images-tab](#images-tab), [plugins-tab](#plugins-tab) | default, hover, focus-visible, pressed, selected |
| Menu | [chat-menu](#chat-menu), [menu-item](#menu-item), [menu-item-danger](#menu-item-danger), [plus-menu](#plus-menu), [user-menu](#user-menu) | default, hover, pressed |
| Tooltip | [tooltip](#tooltip) | default |
| Dialog | [confirm-dialog](#confirm-dialog), [search-dialog](#search-dialog), [pricing-dialog](#pricing-dialog), [dialog-backdrop](#dialog-backdrop) | default |
| Toast | not captured: ChatGPT shows a toast only after an action (copying, archiving, sharing), and the capture took no action | - |
| Card | [promo-card](#promo-card), [library-card](#library-card), [pricing-card](#pricing-card), [image-card](#image-card) | default, hover |
| List row | [chat-row](#chat-row), [nav-row](#nav-row), [search-result](#search-result), [archived-row](#archived-row), [plugin-row](#plugin-row), [plugin-row-link](#plugin-row-link), [settings-row](#settings-row) | default, hover, focus-visible, pressed, active, active-library |
| Table | [md-table](#md-table), [md-th](#md-th), [md-td](#md-td) | default |
| Avatar | [avatar](#avatar) | default |
| Badge | [badge](#badge) | default |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** `radius.full` (260), `radius.lg` (90), `radius.xl` (50), `radius.2xl` (44), `radius.sm` (12), `radius.3xl` (11), 26px (8), `radius.md` (6), `radius.token-composer-single-line` (4), 3.72px (2).

**Hover.** Dark: no change on the element (25), transparent to `variant.primary.soft.bg-hover` (18), transparent to `token.border-light` (3), opacity 1 to 0.8 (2), `surface.elevated-secondary` to `variant.primary.soft.bg-hover` (2), `component.button-danger.bg` to `component.button-danger.bg-hover` (2). Light: no change on the element (25), transparent to `variant.primary.soft.bg-hover` (18), transparent to rgba(0, 0, 0, 0.03) (3), text `role.text.secondary` to `role.text.primary` (2), opacity 1 to 0.8 (2), `bg.user-message-compact` to `variant.primary.soft.bg-hover` (2). Ghost buttons, menu items, rows and tabs all hover to `variant.primary.soft.bg-hover` (white at 10% in dark, black at 5% in light); solid neutral buttons drop to 80% opacity instead; the accent send and voice buttons do not change.

**Pressed.** 42 of 43 pressed readings (the mouse button held down) look the same as hover. The product's `Button` styles pressed through a data attribute its script sets, so with scripts gone `:active` changes nothing; the pressed colours exist only as tokens (`variant.*.*.bg-active`).

**Focus.** Of 57 elements given a real keyboard focus in dark: a 2px box-shadow ring in `role.border.focus` (27), the browser's own outline (auto) (7), no ring on the element (6), a 2px box-shadow ring (inset) in `role.border.focus` (5), a 2px outline in `role.border.focus`, offset -2px (4), a 2px outline on ::after, offset -1px (3), a 2px outline in `text.info`, offset 0px (2), a 2px outline on ::after, offset 0px (1). In light: a 2px box-shadow ring in `role.border.focus` (27), the browser's own outline (auto) (7), no ring on the element (6), a 2px box-shadow ring (inset) in `role.border.focus` (5), a 2px outline in `role.border.focus`, offset -2px (4), a 2px outline in `role.border.focus`, offset 0px (3), a 2px outline on ::after, offset -1px (3), a 2px outline on ::after, offset 0px (1). The ring is `ring.default` (#3a83f7) at `size.focusRing.width` (2px) with no offset; rows draw it as an inset outline, ghost buttons on their ::after, links and segments fall back to the browser's outline.

**Disabled.** A disabled button keeps its variant's colours at 40% opacity (`component.button-disabled.opacity`): Restore defaults in Keyboard settings and Your current plan in the pricing dialog.

**Motion.** 0.15s ease (38), 0.15s cubic-bezier(0.4, 0, 0.2, 1) (28), 0.075s ease (8), 0.2s cubic-bezier(0, 0, 0.2, 1) (5), 0.3s cubic-bezier(0.23, 1, 0.32, 1) (2). Colour and opacity changes run at `duration.basic` (150 ms) on `easing.basic` or `easing.in-out`; the reduced-motion rules are listed under `core.duration.$extensions.reducedMotion` in [tokens.json](tokens.json).

**Layout.** The sidebar is 340 wide at 1440 (`--spacing-token-sidebar` clamps it between 240 and 520), the rail 52, the header 52 tall. The composer and thread share one 768 wide centred column. Settings panes are 768 wide. The Library is a masonry grid of 4 columns at 1440 (`core.layout.grid-columns-library`; `--masonry-columns` steps from 1 to 6 with the container width), Images a 5 column grid and the plugin store 2 columns. On a phone the sidebar is a 260 wide drawer over the page and the column is 358 wide at x 16.

## Components

### Sidebar

The sidebar every page shares (`aside.LeftPanel`, 340 wide at 1440): a 52px header with search and hide, the destination rows (New chat, Images, Scheduled, Library, Plugins, Explore), then the Pinned, Projects and Recents sections and the account row. Rows are 36 tall and fully round; hover and the current row rest on the same translucent fill. Hiding it leaves the 52 wide rail.

#### Sidebar (expanded)

<a id="sidebar"></a>`sidebar`, on home-dark. `aside.LeftPanel`, 340 wide at 1440 (`--spacing-token-sidebar`, clamp(240px, 340px, ...)); header row, nav rows, then the Pinned, Projects and Recents sections and the account row.

<img src="components/crops/sidebar-default.png" alt="Sidebar (expanded), default" height="120"> <img src="components/crops/sidebar-light.png" alt="Sidebar (expanded), light" height="120"> 

| State | Values |
|---|---|
| default | size 340 x 900; background `role.bg.page`; text `typography.text-sm`, `role.text.primary`; icon 77.13 x 18, `role.text.primary` |
| light | size 340 x 900; background `role.bg.page`; text `typography.text-sm`, `role.text.primary`; icon 77.13 x 18, `role.text.primary` |

#### Icon button (sidebar Search)

<a id="sidebar-icon-button"></a>`sidebar-icon-button`, on home-dark. `Button` with data-color=secondary, data-variant=ghost, data-size=xl: 36x36.

<img src="components/crops/sidebar-icon-button-default.png" alt="Icon button (sidebar Search), default" height="36"> <img src="components/crops/sidebar-icon-button-hover.png" alt="Icon button (sidebar Search), hover" height="36"> <img src="components/crops/sidebar-icon-button-focus-visible.png" alt="Icon button (sidebar Search), focus-visible" height="36"> <img src="components/crops/sidebar-icon-button-pressed.png" alt="Icon button (sidebar Search), pressed" height="36"> <img src="components/crops/sidebar-icon-button-light.png" alt="Icon button (sidebar Search), light" height="36"> <img src="components/crops/sidebar-icon-button-light-hover.png" alt="Icon button (sidebar Search), light-hover" height="36"> <img src="components/crops/sidebar-icon-button-light-focus-visible.png" alt="Icon button (sidebar Search), light-focus-visible" height="36"> <img src="components/crops/sidebar-icon-button-light-pressed.png" alt="Icon button (sidebar Search), light-pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 36 x `size.control.lg`; radius `radius.lg`; background transparent; text `fontSize.sm`/14 `fontWeight.medium`, `role.text.disabled`; transition opacity 0.15s ease, color 0.15s ease; icon 20 x 20, `role.text.disabled` |
| light (same: light-hover, light-focus-visible, light-pressed) | size 36 x `size.control.lg`; radius `radius.lg`; background transparent; text `fontSize.sm`/14 `fontWeight.medium`, `role.text.disabled`; transition opacity 0.15s ease, color 0.15s ease; icon 20 x 20, `role.text.disabled` |

Child layers: button 36pxx36px background `variant.primary.soft.bg-hover` radius 8px

#### Nav row (Images)

<a id="nav-row"></a>`nav-row`, on home-dark, library-dark. A 36 tall row with a 20px icon and 14px label. The current destination is filled (`active`).

<img src="components/crops/nav-row-default.png" alt="Nav row (Images), default" height="35"> <img src="components/crops/nav-row-hover.png" alt="Nav row (Images), hover" height="35"> <img src="components/crops/nav-row-focus-visible.png" alt="Nav row (Images), focus-visible" height="35"> <img src="components/crops/nav-row-pressed.png" alt="Nav row (Images), pressed" height="35"> <img src="components/crops/nav-row-light.png" alt="Nav row (Images), light" height="35"> <img src="components/crops/nav-row-light-hover.png" alt="Nav row (Images), light-hover" height="35"> <img src="components/crops/nav-row-active.png" alt="Nav row (Images), active" height="35"> <img src="components/crops/nav-row-active-library.png" alt="Nav row (Images), active-library" height="35"> <img src="components/crops/nav-row-light-active.png" alt="Nav row (Images), light-active" height="35"> <img src="components/crops/nav-row-light-active-library.png" alt="Nav row (Images), light-active-library" height="35"> <img src="components/crops/nav-row-light-focus-visible.png" alt="Nav row (Images), light-focus-visible" height="35"> <img src="components/crops/nav-row-light-pressed.png" alt="Nav row (Images), light-pressed" height="35"> 

| State | Values |
|---|---|
| default | size 328 x 35; padding `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(237, 237, 237, 0.85); icon 20 x 20, rgba(237, 237, 237, 0.85) |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | outline 2px solid `role.border.focus`, offset -2px |
| pressed | background `variant.primary.soft.bg-hover` |
| active, active-library | background `variant.primary.soft.bg-hover`; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light | size 328 x 35; padding `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(13, 13, 13, 0.85); icon 20 x 20, rgba(13, 13, 13, 0.85) |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset -2px |
| light-pressed | background `variant.primary.soft.bg-hover` |
| light-active, light-active-library | background `variant.primary.soft.bg-hover`; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |

#### Section header (Pinned)

<a id="section-toggle"></a>`section-toggle`, on home-dark. Collapsible section label in tertiary text.

<img src="components/crops/section-toggle-default.png" alt="Section header (Pinned), default" height="36"> <img src="components/crops/section-toggle-hover.png" alt="Section header (Pinned), hover" height="36"> <img src="components/crops/section-toggle-focus-visible.png" alt="Section header (Pinned), focus-visible" height="36"> <img src="components/crops/section-toggle-light.png" alt="Section header (Pinned), light" height="36"> <img src="components/crops/section-toggle-light-hover.png" alt="Section header (Pinned), light-hover" height="36"> <img src="components/crops/section-toggle-light-focus-visible.png" alt="Section header (Pinned), light-focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 316 x `size.control.lg`; padding `spacing.0_5` `spacing.1`; radius `radius.md`; background transparent; text `fontSize.sm`/18 `fontWeight.medium`, `role.text.disabled`; icon 12 x 12, `role.text.disabled` |
| focus-visible | outline 2px solid `role.border.focus`, offset 0px |
| light (same: light-hover) | size 316 x `size.control.lg`; padding `spacing.0_5` `spacing.1`; radius `radius.md`; background transparent; text `fontSize.sm`/18 `fontWeight.medium`, `role.text.disabled`; icon 12 x 12, `role.text.disabled` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset 0px |

#### List row (sidebar chat)

<a id="chat-row"></a>`chat-row`, on home-dark, thread-dark-code. A chat in Recents: 36 tall, full radius (`--radius-token-row`), the title truncated; hover fills it and shows Chat actions and Pin. The open chat is filled (`active`).

<img src="components/crops/chat-row-default.png" alt="List row (sidebar chat), default" height="36"> <img src="components/crops/chat-row-hover.png" alt="List row (sidebar chat), hover" height="36"> <img src="components/crops/chat-row-light.png" alt="List row (sidebar chat), light" height="36"> <img src="components/crops/chat-row-light-hover.png" alt="List row (sidebar chat), light-hover" height="36"> <img src="components/crops/chat-row-active.png" alt="List row (sidebar chat), active" height="36"> <img src="components/crops/chat-row-light-active.png" alt="List row (sidebar chat), light-active" height="36"> 

| State | Values |
|---|---|
| default | size 328 x `size.control.lg`; padding `spacing.1_5` `spacing.1_5` `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(237, 237, 237, 0.85); icon 14 x 14, `role.text.secondary` |
| hover, active | background `variant.primary.soft.bg-hover` |
| light | size 328 x `size.control.lg`; padding `spacing.1_5` `spacing.1_5` `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(13, 13, 13, 0.85); icon 14 x 14, `role.text.secondary` |
| light-hover, light-active | background `variant.primary.soft.bg-hover` |

#### Chat row link (keyboard focus)

<a id="chat-row-link"></a>`chat-row-link`, on home-dark. The row's own link, focused from the keyboard.

<img src="components/crops/chat-row-link-focus-visible.png" alt="Chat row link (keyboard focus), focus-visible" height="24"> <img src="components/crops/chat-row-link-light-focus-visible.png" alt="Chat row link (keyboard focus), light-focus-visible" height="24"> 

| State | Values |
|---|---|
| focus-visible | size 253 x `size.control.4xs`; background transparent; outline 1px auto #99c8ff, offset 1px; text `typography.text-sm`, rgba(237, 237, 237, 0.85) |
| light-focus-visible | size 253 x `size.control.4xs`; background transparent; outline 1px auto #005fcc, offset 1px; text `typography.text-sm`, rgba(13, 13, 13, 0.85) |

Child layers: a 253x20; a 328pxx36px

#### Chat actions button

<a id="chat-row-actions"></a>`chat-row-actions`, on home-dark. A 20x20 `Button` (size 3xs, transparent, pill), shown when its row is hovered; measured while the row is hovered.

<img src="components/crops/chat-row-actions-hover.png" alt="Chat actions button, hover" height="24"> <img src="components/crops/chat-row-actions-light-hover.png" alt="Chat actions button, light-hover" height="24"> 

| State | Values |
|---|---|
| hover | size 20 x `size.control.4xs`; radius `radius.full`; background transparent; text `fontSize.xs`/12 `fontWeight.medium`, `role.text.secondary`; transition opacity 0.15s ease, color 0.15s ease; icon 14 x 14, `role.text.secondary` |
| light-hover | size 20 x `size.control.4xs`; radius `radius.full`; background transparent; text `fontSize.xs`/12 `fontWeight.medium`, `role.text.secondary`; transition opacity 0.15s ease, color 0.15s ease; icon 14 x 14, `role.text.secondary` |

#### Project row

<a id="project-row"></a>`project-row`, on home-dark. Each project with its own icon; hover reveals project actions and a new-chat button.

<img src="components/crops/project-row-default.png" alt="Project row, default" height="36"> <img src="components/crops/project-row-hover.png" alt="Project row, hover" height="36"> <img src="components/crops/project-row-focus-visible.png" alt="Project row, focus-visible" height="36"> <img src="components/crops/project-row-light.png" alt="Project row, light" height="36"> <img src="components/crops/project-row-light-hover.png" alt="Project row, light-hover" height="36"> <img src="components/crops/project-row-light-focus-visible.png" alt="Project row, light-focus-visible" height="36"> 

| State | Values |
|---|---|
| default | size 328 x `size.control.lg`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(237, 237, 237, 0.85); icon 19.5 x 19.5, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | outline 2px solid `role.border.focus`, offset -2px |
| light | size 328 x `size.control.lg`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(13, 13, 13, 0.85); icon 19.5 x 19.5, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset -2px |

#### Account row

<a id="account-row"></a>`account-row`, on home-dark, home-dark-user-menu. `Button` primary ghost size 4xl: the 24px avatar, the name over the plan.

<img src="components/crops/account-row-default.png" alt="Account row, default" height="48"> <img src="components/crops/account-row-hover.png" alt="Account row, hover" height="48"> <img src="components/crops/account-row-focus-visible.png" alt="Account row, focus-visible" height="48"> <img src="components/crops/account-row-pressed.png" alt="Account row, pressed" height="48"> <img src="components/crops/account-row-light.png" alt="Account row, light" height="48"> <img src="components/crops/account-row-light-hover.png" alt="Account row, light-hover" height="48"> <img src="components/crops/account-row-open.png" alt="Account row, open" height="48"> <img src="components/crops/account-row-light-focus-visible.png" alt="Account row, light-focus-visible" height="48"> <img src="components/crops/account-row-light-open.png" alt="Account row, light-open" height="48"> <img src="components/crops/account-row-light-pressed.png" alt="Account row, light-pressed" height="48"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed, open) | size 248.11 x `size.control.3xl`; padding 0 `spacing.2`; radius `radius.xl`; background transparent; text `fontSize.xs`/12 `fontWeight.semibold`, `role.text.on-accent`; transition opacity 0.15s ease, color 0.15s ease |
| light (same: light-hover, light-focus-visible, light-pressed, light-open) | size 248.11 x `size.control.3xl`; padding 0 `spacing.2`; radius `radius.xl`; background transparent; text `fontSize.xs`/12 `fontWeight.semibold`, `role.text.inverse`; transition opacity 0.15s ease, color 0.15s ease |

Child layers: button 248.109pxx48px background `variant.primary.soft.bg-hover` radius 12px; div 24x24 background #8a8a8a radius 9999px

#### Avatar

<a id="avatar"></a>`avatar`, on home-dark. Redacted to a grey disc with an L; the real one is the account photo at 24px.

<img src="components/crops/avatar-default.png" alt="Avatar, default" height="24"> <img src="components/crops/avatar-light.png" alt="Avatar, light" height="24"> 

| State | Values |
|---|---|
| default | size 24 x `size.control.2xs`; radius `radius.full`; background #8a8a8a; text `fontSize.xs`/12 `fontWeight.semibold`, `role.text.on-accent` |
| light | size 24 x `size.control.2xs`; radius `radius.full`; background #8a8a8a; text `fontSize.xs`/12 `fontWeight.semibold`, `role.text.inverse` |

#### Outline pill button (account Upgrade)

<a id="sidebar-upgrade"></a>`sidebar-upgrade`, on home-dark.

<img src="components/crops/sidebar-upgrade-default.png" alt="Outline pill button (account Upgrade), default" height="28"> <img src="components/crops/sidebar-upgrade-hover.png" alt="Outline pill button (account Upgrade), hover" height="28"> <img src="components/crops/sidebar-upgrade-focus-visible.png" alt="Outline pill button (account Upgrade), focus-visible" height="28"> <img src="components/crops/sidebar-upgrade-pressed.png" alt="Outline pill button (account Upgrade), pressed" height="28"> <img src="components/crops/sidebar-upgrade-light.png" alt="Outline pill button (account Upgrade), light" height="28"> <img src="components/crops/sidebar-upgrade-light-hover.png" alt="Outline pill button (account Upgrade), light-hover" height="28"> <img src="components/crops/sidebar-upgrade-light-focus-visible.png" alt="Outline pill button (account Upgrade), light-focus-visible" height="28"> <img src="components/crops/sidebar-upgrade-light-pressed.png" alt="Outline pill button (account Upgrade), light-pressed" height="28"> 

| State | Values |
|---|---|
| default | size 71.89 x `size.control.sm`; padding 0 `spacing.2_5`; border 1px solid `role.border.default`; radius `radius.full`; background `role.bg.surface`; text `fontSize.xs`/16 `fontWeight.medium`, `role.text.on-accent` |
| hover | background #2f2f2f |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background #2f2f2f; opacity 0.8 |
| light | size 71.89 x `size.control.sm`; padding 0 `spacing.2_5`; border 1px solid `role.border.strong`; radius `radius.full`; background `role.bg.raised`; text `fontSize.xs`/16 `fontWeight.medium`, `role.text.primary` |
| light-hover | background `role.bg.surface` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `role.bg.surface`; opacity 0.8 |

#### Sidebar collapsed to the rail

<a id="sidebar-rail"></a>`sidebar-rail`, on home-dark-sidebar-collapsed. 52 wide: show sidebar, new chat, search, pinned, recents, library, then the avatar.

<img src="components/crops/sidebar-rail-default.png" alt="Sidebar collapsed to the rail, default" height="120"> <img src="components/crops/sidebar-rail-light.png" alt="Sidebar collapsed to the rail, light" height="120"> 

| State | Values |
|---|---|
| default | size 52 x 900; background `role.bg.page`; text `fontSize.xs`/12 `fontWeight.semibold`, `role.text.on-accent`; icon 24 x 24, `role.text.primary` |
| light | size 52 x 900; background `role.bg.page`; text `fontSize.xs`/12 `fontWeight.semibold`, `role.text.inverse`; icon 24 x 24, `role.text.primary` |

#### Rail button (New chat)

<a id="rail-button"></a>`rail-button`, on home-dark-sidebar-collapsed.

<img src="components/crops/rail-button-default.png" alt="Rail button (New chat), default" height="35"> <img src="components/crops/rail-button-hover.png" alt="Rail button (New chat), hover" height="35"> <img src="components/crops/rail-button-focus-visible.png" alt="Rail button (New chat), focus-visible" height="35"> <img src="components/crops/rail-button-light.png" alt="Rail button (New chat), light" height="35"> <img src="components/crops/rail-button-light-hover.png" alt="Rail button (New chat), light-hover" height="35"> <img src="components/crops/rail-button-light-focus-visible.png" alt="Rail button (New chat), light-focus-visible" height="35"> 

| State | Values |
|---|---|
| default (same: hover) | size 36 x 35; padding 5px `spacing.2`; radius `radius.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm`, `role.text.primary`; icon 19.5 x 19.5, `role.text.primary` |
| focus-visible | outline 2px solid `role.border.focus`, offset -2px |
| light (same: light-hover) | size 36 x 35; padding 5px `spacing.2`; radius `radius.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm`, `role.text.primary`; icon 19.5 x 19.5, `role.text.primary` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset -2px |

### Top bar

The 52px page header (`<header>`, fixed, z-index 30): the Chat / Work toggle centred on the home, Upgrade and the temporary-chat button at the end; in a thread Upgrade, Share and More.

#### Page header

<a id="page-header"></a>`page-header`, on home-dark. 52 tall: the Chat / Work toggle centred, Upgrade and temporary chat at the end.

<img src="components/crops/page-header-default.png" alt="Page header, default" height="52"> <img src="components/crops/page-header-light.png" alt="Page header, light" height="52"> 

| State | Values |
|---|---|
| default | size 1100 x `size.height.height-toolbar`; padding 0 `spacing.2`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `text.header-upgrade`; icon 20 x 20, `text.header-upgrade` |
| light | size 1100 x `size.height.height-toolbar`; padding 0 `spacing.2`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `text.tip`; icon 20 x 20, `text.tip` |

Child layers: button 106.2x34 border 1px solid transparent radius 8px; button 36x36 border 1px solid transparent radius 8px

#### Chat / Work segmented toggle

<a id="mode-toggle"></a>`mode-toggle`, on home-dark. A pill track with two 112x36 segments; the selected one carries a filled thumb.

<img src="components/crops/mode-toggle-default.png" alt="Chat / Work segmented toggle, default" height="120"> <img src="components/crops/mode-toggle-light.png" alt="Chat / Work segmented toggle, light" height="120"> 

| State | Values |
|---|---|
| default | size 1100 x 900; border L: 1px solid `role.border.default`; background `role.bg.page`; text `typography.text-sm` at `fontWeight.medium`, `text.header-upgrade`; icon 20 x 20, `text.header-upgrade`; placeholder `role.text.disabled` |
| light | size 1100 x 900; border L: 1px solid `role.border.default`; background `role.bg.page`; text `typography.text-sm` at `fontWeight.medium`, `text.tip`; icon 20 x 20, `text.tip`; placeholder `role.text.disabled` |

#### Mode segment (Work, not selected)

<a id="mode-segment"></a>`mode-segment`, on home-dark.

<img src="components/crops/mode-segment-default.png" alt="Mode segment (Work, not selected), default" height="36"> <img src="components/crops/mode-segment-hover.png" alt="Mode segment (Work, not selected), hover" height="36"> <img src="components/crops/mode-segment-focus-visible.png" alt="Mode segment (Work, not selected), focus-visible" height="36"> <img src="components/crops/mode-segment-pressed.png" alt="Mode segment (Work, not selected), pressed" height="36"> <img src="components/crops/mode-segment-light.png" alt="Mode segment (Work, not selected), light" height="36"> <img src="components/crops/mode-segment-light-hover.png" alt="Mode segment (Work, not selected), light-hover" height="36"> <img src="components/crops/mode-segment-selected.png" alt="Mode segment (Work, not selected), selected" height="36"> <img src="components/crops/mode-segment-light-focus-visible.png" alt="Mode segment (Work, not selected), light-focus-visible" height="36"> <img src="components/crops/mode-segment-light-pressed.png" alt="Mode segment (Work, not selected), light-pressed" height="36"> <img src="components/crops/mode-segment-light-selected.png" alt="Mode segment (Work, not selected), light-selected" height="36"> <img src="components/crops/mode-segment-light-selected-hover.png" alt="Mode segment (Work, not selected), light-selected-hover" height="36"> <img src="components/crops/mode-segment-selected-hover.png" alt="Mode segment (Work, not selected), selected-hover" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 112 x `size.control.lg`; padding 0 `spacing.3_5` 0 `spacing.1_5`; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.on-accent`; icon 12 x 12, `role.text.on-accent` |
| focus-visible | outline 1px auto #99c8ff, offset 0px |
| selected, selected-hover | padding 0 `spacing.1_5` 0 `spacing.3_5`; icon none |
| light (same: light-hover, light-pressed) | size 112 x `size.control.lg`; padding 0 `spacing.3_5` 0 `spacing.1_5`; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 12 x 12, `role.text.primary` |
| light-focus-visible | outline 1px auto #005fcc, offset 0px |
| light-selected, light-selected-hover | padding 0 `spacing.1_5` 0 `spacing.3_5`; icon none |

#### Link-style button (header Upgrade)

<a id="header-upgrade"></a>`header-upgrade`, on home-dark. Transparent pill, accent sparkle and label in `--color-text-header-upgrade`.

<img src="components/crops/header-upgrade-default.png" alt="Link-style button (header Upgrade), default" height="34"> <img src="components/crops/header-upgrade-hover.png" alt="Link-style button (header Upgrade), hover" height="34"> <img src="components/crops/header-upgrade-focus-visible.png" alt="Link-style button (header Upgrade), focus-visible" height="34"> <img src="components/crops/header-upgrade-pressed.png" alt="Link-style button (header Upgrade), pressed" height="34"> <img src="components/crops/header-upgrade-light.png" alt="Link-style button (header Upgrade), light" height="34"> <img src="components/crops/header-upgrade-light-hover.png" alt="Link-style button (header Upgrade), light-hover" height="34"> <img src="components/crops/header-upgrade-light-focus-visible.png" alt="Link-style button (header Upgrade), light-focus-visible" height="34"> <img src="components/crops/header-upgrade-light-pressed.png" alt="Link-style button (header Upgrade), light-pressed" height="34"> 

| State | Values |
|---|---|
| default | size 106.16 x `size.height.nav-row`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.lg`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `text.header-upgrade`; icon 20 x 20, `text.header-upgrade` |
| hover | background rgba(164, 205, 251, 0.2) |
| focus-visible | background rgba(164, 205, 251, 0.2); focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background rgba(164, 205, 251, 0.2) |
| light | size 106.16 x `size.height.nav-row`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.lg`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `text.tip`; icon 20 x 20, `text.tip` |
| light-hover | background `component.badge.bg` |
| light-focus-visible | background `component.badge.bg`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `component.badge.bg` |

#### Icon button (Temporary chat)

<a id="header-icon-button"></a>`header-icon-button`, on home-dark.

<img src="components/crops/header-icon-button-default.png" alt="Icon button (Temporary chat), default" height="36"> <img src="components/crops/header-icon-button-hover.png" alt="Icon button (Temporary chat), hover" height="36"> <img src="components/crops/header-icon-button-focus-visible.png" alt="Icon button (Temporary chat), focus-visible" height="36"> <img src="components/crops/header-icon-button-pressed.png" alt="Icon button (Temporary chat), pressed" height="36"> <img src="components/crops/header-icon-button-light.png" alt="Icon button (Temporary chat), light" height="36"> <img src="components/crops/header-icon-button-light-hover.png" alt="Icon button (Temporary chat), light-hover" height="36"> <img src="components/crops/header-icon-button-light-focus-visible.png" alt="Icon button (Temporary chat), light-focus-visible" height="36"> <img src="components/crops/header-icon-button-light-pressed.png" alt="Icon button (Temporary chat), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 36 x `size.control.lg`; border 1px solid transparent; radius `radius.lg`; background transparent; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 36 x `size.control.lg`; border 1px solid transparent; radius `radius.lg`; background transparent; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Secondary button (Share)

<a id="share-button"></a>`share-button`, on thread-dark-code.

<img src="components/crops/share-button-default.png" alt="Secondary button (Share), default" height="36"> <img src="components/crops/share-button-hover.png" alt="Secondary button (Share), hover" height="36"> <img src="components/crops/share-button-focus-visible.png" alt="Secondary button (Share), focus-visible" height="36"> <img src="components/crops/share-button-pressed.png" alt="Secondary button (Share), pressed" height="36"> <img src="components/crops/share-button-light.png" alt="Secondary button (Share), light" height="36"> <img src="components/crops/share-button-light-hover.png" alt="Secondary button (Share), light-hover" height="36"> <img src="components/crops/share-button-light-focus-visible.png" alt="Secondary button (Share), light-focus-visible" height="36"> <img src="components/crops/share-button-light-pressed.png" alt="Secondary button (Share), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 87.27 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.lg`; background transparent; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 87.27 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.lg`; background transparent; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Icon button (More, thread)

<a id="more-button"></a>`more-button`, on thread-dark-code.

<img src="components/crops/more-button-default.png" alt="Icon button (More, thread), default" height="36"> <img src="components/crops/more-button-hover.png" alt="Icon button (More, thread), hover" height="36"> <img src="components/crops/more-button-focus-visible.png" alt="Icon button (More, thread), focus-visible" height="36"> <img src="components/crops/more-button-pressed.png" alt="Icon button (More, thread), pressed" height="36"> <img src="components/crops/more-button-light.png" alt="Icon button (More, thread), light" height="36"> <img src="components/crops/more-button-light-hover.png" alt="Icon button (More, thread), light-hover" height="36"> <img src="components/crops/more-button-light-focus-visible.png" alt="Icon button (More, thread), light-focus-visible" height="36"> <img src="components/crops/more-button-light-pressed.png" alt="Icon button (More, thread), light-pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 36 x `size.control.lg`; radius `radius.lg`; background transparent; text `fontSize.sm`/14 `fontWeight.medium`, `role.text.primary`; transition opacity 0.15s ease, color 0.15s ease; icon 20 x 20, `role.text.primary` |
| light (same: light-hover, light-focus-visible, light-pressed) | size 36 x `size.control.lg`; radius `radius.lg`; background transparent; text `fontSize.sm`/14 `fontWeight.medium`, `role.text.primary`; transition opacity 0.15s ease, color 0.15s ease; icon 20 x 20, `role.text.primary` |

Child layers: button 36pxx36px background `variant.primary.soft.bg-hover` radius 8px

### Home

The new-chat page: one heading over the composer, three suggestion rows, and the Plus nudge card at the bottom.

#### Home heading

<a id="home-heading"></a>`home-heading`, on home-dark.

<img src="components/crops/home-heading-default.png" alt="Home heading, default" height="28"> <img src="components/crops/home-heading-light.png" alt="Home heading, light" height="28"> 

| State | Values |
|---|---|
| default | size 212.8 x `size.control.sm`; background transparent; text `fontSize.2xl`/28.8 `fontWeight.normal`, `role.text.primary` |
| light | size 212.8 x `size.control.sm`; background transparent; text `fontSize.2xl`/28.8 `fontWeight.normal`, `role.text.primary` |

#### Suggestion row

<a id="suggestion-row"></a>`suggestion-row`, on home-dark. 768x52, icon and 16px tertiary text; hover fills with `--color-background-home-suggestion-hover`.

<img src="components/crops/suggestion-row-default.png" alt="Suggestion row, default" height="52"> <img src="components/crops/suggestion-row-hover.png" alt="Suggestion row, hover" height="52"> <img src="components/crops/suggestion-row-focus-visible.png" alt="Suggestion row, focus-visible" height="52"> <img src="components/crops/suggestion-row-pressed.png" alt="Suggestion row, pressed" height="52"> <img src="components/crops/suggestion-row-light.png" alt="Suggestion row, light" height="52"> <img src="components/crops/suggestion-row-light-hover.png" alt="Suggestion row, light-hover" height="52"> <img src="components/crops/suggestion-row-light-focus-visible.png" alt="Suggestion row, light-focus-visible" height="52"> <img src="components/crops/suggestion-row-light-pressed.png" alt="Suggestion row, light-pressed" height="52"> 

| State | Values |
|---|---|
| default | size 768 x `size.height.height-toolbar`; padding 0 `spacing.11` 0 `spacing.2`; radius `radius.2xl`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; transition color 0.075s ease |
| hover | text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus`; text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |
| pressed | text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |
| light | size 768 x `size.height.height-toolbar`; padding 0 `spacing.11` 0 `spacing.2`; radius `radius.2xl`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; transition color 0.075s ease |
| light-hover | text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus`; text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |
| light-pressed | text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |

#### Card (Plus nudge)

<a id="promo-card"></a>`promo-card`, on home-dark. 768x74 card pinned under the suggestions: icon, title and line, a filled Get Plus button and a dismiss button.

<img src="components/crops/promo-card-default.png" alt="Card (Plus nudge), default" height="74"> <img src="components/crops/promo-card-light.png" alt="Card (Plus nudge), light" height="74"> 

| State | Values |
|---|---|
| default | size 768 x 74; padding `spacing.4`; radius `radius.3xl`; background `role.bg.raised`; shadow rgba(0, 0, 0, 0.05) 0px 4px 16px 0px; outline 1px solid `role.border.subtle`, offset -0.5px; text `typography.text-sm` at 510, `role.text.primary`; icon 20 x 20, `role.text.disabled` |
| light | size 768 x 74; padding `spacing.4`; radius `radius.3xl`; background `role.bg.raised`; shadow rgba(0, 0, 0, 0.05) 0px 4px 16px 0px; outline 1px solid `variant.primary.surface.bg`, offset -0.5px; text `typography.text-sm` at 510, `role.text.primary`; icon 20 x 20, `role.text.disabled` |

#### Primary button (Get Plus)

<a id="promo-button"></a>`promo-button`, on home-dark.

<img src="components/crops/promo-button-default.png" alt="Primary button (Get Plus), default" height="36"> <img src="components/crops/promo-button-hover.png" alt="Primary button (Get Plus), hover" height="36"> <img src="components/crops/promo-button-focus-visible.png" alt="Primary button (Get Plus), focus-visible" height="36"> <img src="components/crops/promo-button-pressed.png" alt="Primary button (Get Plus), pressed" height="36"> <img src="components/crops/promo-button-light.png" alt="Primary button (Get Plus), light" height="36"> <img src="components/crops/promo-button-light-hover.png" alt="Primary button (Get Plus), light-hover" height="36"> <img src="components/crops/promo-button-light-focus-visible.png" alt="Primary button (Get Plus), light-focus-visible" height="36"> <img src="components/crops/promo-button-light-pressed.png" alt="Primary button (Get Plus), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 85.98 x `size.control.lg`; padding 0 `spacing.4`; radius `radius.full`; background `variant.primary.solid.bg`; text `typography.text-sm` at 510, `role.text.inverse` |
| hover | opacity 0.8 |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | opacity 0.8 |
| light | size 85.98 x `size.control.lg`; padding 0 `spacing.4`; radius `radius.full`; background `variant.primary.solid.bg`; text `typography.text-sm` at 510, `role.text.inverse` |
| light-hover | opacity 0.8 |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | opacity 0.8 |

#### Dismiss button

<a id="promo-dismiss"></a>`promo-dismiss`, on home-dark.

<img src="components/crops/promo-dismiss-default.png" alt="Dismiss button, default" height="24"> <img src="components/crops/promo-dismiss-hover.png" alt="Dismiss button, hover" height="24"> <img src="components/crops/promo-dismiss-focus-visible.png" alt="Dismiss button, focus-visible" height="24"> <img src="components/crops/promo-dismiss-light.png" alt="Dismiss button, light" height="24"> <img src="components/crops/promo-dismiss-light-hover.png" alt="Dismiss button, light-hover" height="24"> <img src="components/crops/promo-dismiss-light-focus-visible.png" alt="Dismiss button, light-focus-visible" height="24"> 

| State | Values |
|---|---|
| default | size 20 x `size.control.4xs`; radius `radius.full`; background transparent; text `typography.text-sm`, `role.text.disabled`; icon 20 x 20, `role.text.disabled` |
| hover | opacity 0.8 |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light | size 20 x `size.control.4xs`; radius `radius.full`; background transparent; text `typography.text-sm`, `role.text.disabled`; icon 20 x 20, `role.text.disabled` |
| light-hover | opacity 0.8 |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |

### Composer

The composer shared by the home and a thread: a 768 wide pill with the + button, the ProseMirror field, Think, Dictate and the voice button, which becomes Send once there is text.

#### Text area (composer)

<a id="composer"></a>`composer`, on home-dark, home-dark-composer-typed, thread-dark-code. A pill on the home page, 768 wide: + button, the ProseMirror field, Think, dictate, voice.

<img src="components/crops/composer-default.png" alt="Text area (composer), default" height="52"> <img src="components/crops/composer-focus-visible.png" alt="Text area (composer), focus-visible" height="52"> <img src="components/crops/composer-light.png" alt="Text area (composer), light" height="52"> <img src="components/crops/composer-typed.png" alt="Text area (composer), typed" height="52"> <img src="components/crops/composer-light-focus-visible.png" alt="Text area (composer), light-focus-visible" height="52"> <img src="components/crops/composer-light-thread.png" alt="Text area (composer), light-thread" height="52"> <img src="components/crops/composer-light-typed.png" alt="Text area (composer), light-typed" height="52"> <img src="components/crops/composer-thread.png" alt="Text area (composer), thread" height="52"> 

| State | Values |
|---|---|
| default (same: focus-visible, thread) | size 768 x `size.height.height-toolbar`; radius 26px; background `role.bg.raised`; shadow rgba(255, 255, 255, 0.2) 0px 0px 1px 0px inset; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.primary`; placeholder `role.text.disabled` |
| typed | text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary`; placeholder none |
| light (same: light-focus-visible, light-thread) | size 768 x `size.height.height-toolbar`; radius 26px; background `role.bg.raised`; shadow rgba(255, 255, 255, 0.2) 0px 0px 1px 0px inset; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.primary`; placeholder `role.text.disabled` |
| light-typed | text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary`; placeholder none |

#### Composer placeholder

<a id="composer-placeholder"></a>`composer-placeholder`, on home-dark.

<img src="components/crops/composer-placeholder-default.png" alt="Composer placeholder, default" height="26"> <img src="components/crops/composer-placeholder-light.png" alt="Composer placeholder, light" height="26"> 

| State | Values |
|---|---|
| default | size 528.03 x `size.control.xs`; background transparent; placeholder `role.text.disabled` |
| light | size 528.03 x `size.control.xs`; background transparent; placeholder `role.text.disabled` |

#### Icon button (composer +)

<a id="composer-plus"></a>`composer-plus`, on home-dark.

<img src="components/crops/composer-plus-default.png" alt="Icon button (composer +), default" height="36"> <img src="components/crops/composer-plus-hover.png" alt="Icon button (composer +), hover" height="36"> <img src="components/crops/composer-plus-focus-visible.png" alt="Icon button (composer +), focus-visible" height="36"> <img src="components/crops/composer-plus-pressed.png" alt="Icon button (composer +), pressed" height="36"> <img src="components/crops/composer-plus-light.png" alt="Icon button (composer +), light" height="36"> <img src="components/crops/composer-plus-light-hover.png" alt="Icon button (composer +), light-hover" height="36"> <img src="components/crops/composer-plus-light-focus-visible.png" alt="Icon button (composer +), light-focus-visible" height="36"> <img src="components/crops/composer-plus-light-pressed.png" alt="Icon button (composer +), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 36 x `size.control.lg`; border 1px solid transparent; radius `radius.full`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 36 x `size.control.lg`; border 1px solid transparent; radius `radius.full`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Think chip

<a id="think-chip"></a>`think-chip`, on home-dark.

<img src="components/crops/think-chip-default.png" alt="Think chip, default" height="36"> <img src="components/crops/think-chip-hover.png" alt="Think chip, hover" height="36"> <img src="components/crops/think-chip-focus-visible.png" alt="Think chip, focus-visible" height="36"> <img src="components/crops/think-chip-pressed.png" alt="Think chip, pressed" height="36"> <img src="components/crops/think-chip-light.png" alt="Think chip, light" height="36"> <img src="components/crops/think-chip-light-hover.png" alt="Think chip, light-hover" height="36"> <img src="components/crops/think-chip-light-focus-visible.png" alt="Think chip, light-focus-visible" height="36"> <img src="components/crops/think-chip-light-pressed.png" alt="Think chip, light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 91.97 x `size.control.lg`; padding 0 `spacing.3_5` 0 `spacing.3`; radius `radius.full`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.disabled` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 91.97 x `size.control.lg`; padding 0 `spacing.3_5` 0 `spacing.3`; radius `radius.full`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.disabled` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Icon button (Dictate)

<a id="dictate-button"></a>`dictate-button`, on home-dark.

<img src="components/crops/dictate-button-default.png" alt="Icon button (Dictate), default" height="36"> <img src="components/crops/dictate-button-hover.png" alt="Icon button (Dictate), hover" height="36"> <img src="components/crops/dictate-button-focus-visible.png" alt="Icon button (Dictate), focus-visible" height="36"> <img src="components/crops/dictate-button-pressed.png" alt="Icon button (Dictate), pressed" height="36"> <img src="components/crops/dictate-button-light.png" alt="Icon button (Dictate), light" height="36"> <img src="components/crops/dictate-button-light-hover.png" alt="Icon button (Dictate), light-hover" height="36"> <img src="components/crops/dictate-button-light-focus-visible.png" alt="Icon button (Dictate), light-focus-visible" height="36"> <img src="components/crops/dictate-button-light-pressed.png" alt="Icon button (Dictate), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 36 x `size.control.lg`; border 1px solid transparent; radius `radius.full`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 36 x `size.control.lg`; border 1px solid transparent; radius `radius.full`; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.disabled`; icon 20 x 20, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Accent icon button (Start Voice)

<a id="voice-button"></a>`voice-button`, on home-dark. A 36px circle in `--color-background-composer-primary`, the accent.

<img src="components/crops/voice-button-default.png" alt="Accent icon button (Start Voice), default" height="36"> <img src="components/crops/voice-button-hover.png" alt="Accent icon button (Start Voice), hover" height="36"> <img src="components/crops/voice-button-focus-visible.png" alt="Accent icon button (Start Voice), focus-visible" height="36"> <img src="components/crops/voice-button-pressed.png" alt="Accent icon button (Start Voice), pressed" height="36"> <img src="components/crops/voice-button-light.png" alt="Accent icon button (Start Voice), light" height="36"> <img src="components/crops/voice-button-light-hover.png" alt="Accent icon button (Start Voice), light-hover" height="36"> <img src="components/crops/voice-button-light-focus-visible.png" alt="Accent icon button (Start Voice), light-focus-visible" height="36"> <img src="components/crops/voice-button-light-pressed.png" alt="Accent icon button (Start Voice), light-pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 36 x `size.control.lg`; padding `spacing.0_5`; radius `radius.full`; background `bg.accent-action`; text `typography.text-md`, `role.text.primary`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, `role.text.on-accent` |
| focus-visible | outline 2px solid `text.info`, offset 0px |
| light (same: light-hover, light-pressed) | size 36 x `size.control.lg`; padding `spacing.0_5`; radius `radius.full`; background `bg.accent-action`; text `typography.text-md`, `role.text.primary`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, `role.text.inverse` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset 0px |

#### Accent icon button (Send, typed)

<a id="send-button"></a>`send-button`, on home-dark-composer-typed.

<img src="components/crops/send-button-default.png" alt="Accent icon button (Send, typed), default" height="36"> <img src="components/crops/send-button-hover.png" alt="Accent icon button (Send, typed), hover" height="36"> <img src="components/crops/send-button-focus-visible.png" alt="Accent icon button (Send, typed), focus-visible" height="36"> <img src="components/crops/send-button-pressed.png" alt="Accent icon button (Send, typed), pressed" height="36"> <img src="components/crops/send-button-light.png" alt="Accent icon button (Send, typed), light" height="36"> <img src="components/crops/send-button-light-hover.png" alt="Accent icon button (Send, typed), light-hover" height="36"> <img src="components/crops/send-button-light-focus-visible.png" alt="Accent icon button (Send, typed), light-focus-visible" height="36"> <img src="components/crops/send-button-light-pressed.png" alt="Accent icon button (Send, typed), light-pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 36 x `size.control.lg`; padding `spacing.0_5`; radius `radius.full`; background `bg.accent-action`; text `typography.text-md`, `role.text.primary`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, `role.text.on-accent` |
| focus-visible | outline 2px solid `text.info`, offset 0px |
| light (same: light-hover, light-pressed) | size 36 x `size.control.lg`; padding `spacing.0_5`; radius `radius.full`; background `bg.accent-action`; text `typography.text-md`, `role.text.primary`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, `role.text.inverse` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset 0px |

#### Tooltip (Dictate)

<a id="tooltip"></a>`tooltip`, on home-dark-tooltip. Opened by keyboard focus on the Dictate button: `--color-background-tooltip` fill, rounded, 14px text.

<img src="components/crops/tooltip-default.png" alt="Tooltip (Dictate), default" height="30"> <img src="components/crops/tooltip-light.png" alt="Tooltip (Dictate), light" height="30"> 

| State | Values |
|---|---|
| default | size 73.66 x 30; padding 5px `spacing.3`; border 1px solid `border.tooltip`; radius `radius.2xl`; background `surface.elevated-secondary`; shadow rgba(15, 23, 42, 0.2) 0px 8px 18px 0px; text `fontSize.sm`/18 `fontWeight.semibold`, `role.text.primary`; transform translate(1167.5px, 428px) |
| light | size 73.66 x 30; padding 5px `spacing.3`; border 1px solid `border.tooltip`; radius `radius.2xl`; background `variant.primary.solid.bg`; shadow rgba(15, 23, 42, 0.2) 0px 8px 18px 0px; text `fontSize.sm`/18 `fontWeight.semibold`, `role.text.inverse`; transform translate(1167.5px, 428px) |

### Thread

A conversation: the user bubble in the accent colour, the assistant's markdown (paragraphs, headings, strong, inline code, code blocks, tables, links), the actions under a turn and the scroll-to-bottom button. Message text in the copies is same-length filler.

#### User message bubble

<a id="user-bubble"></a>`user-bubble`, on thread-dark-user-turn. `--color-background-user-message` / `--color-text-user-message`; right-aligned, rounded.

<img src="components/crops/user-bubble-default.png" alt="User message bubble, default" height="120"> <img src="components/crops/user-bubble-light.png" alt="User message bubble, light" height="120"> 

| State | Values |
|---|---|
| default | size 537.59 x 462; padding `spacing.2_5` `spacing.4`; radius `radius.token-composer-single-line`; background `bg.user-message`; text `fontSize.base`/26 `fontWeight.normal`, `text.user-message` |
| light | size 537.59 x 462; padding `spacing.2_5` `spacing.4`; radius `radius.token-composer-single-line`; background `bg.user-message`; text `fontSize.base`/26 `fontWeight.normal`, `text.user-message` |

#### Assistant markdown body

<a id="markdown"></a>`markdown`, on thread-dark-table.

<img src="components/crops/markdown-default.png" alt="Assistant markdown body, default" height="120"> <img src="components/crops/markdown-light.png" alt="Assistant markdown body, light" height="120"> 

| State | Values |
|---|---|
| default | size 768 x 2695; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary`; icon 12 x 12, `role.text.secondary` |
| light | size 768 x 2695; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary`; icon 12 x 12, `role.text.secondary` |

Child layers: th 128x33 border 1px solid `role.border.strong`; th 448x33 border 1px solid `role.border.strong`; th 128x33 border 1px solid `role.border.strong`

#### Markdown paragraph

<a id="md-paragraph"></a>`md-paragraph`, on thread-dark-table.

<img src="components/crops/md-paragraph-default.png" alt="Markdown paragraph, default" height="78"> <img src="components/crops/md-paragraph-light.png" alt="Markdown paragraph, light" height="78"> 

| State | Values |
|---|---|
| default | size 768 x 78; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |
| light | size 768 x 78; background transparent; text `fontSize.base`/26 `fontWeight.normal`, `role.text.primary` |

#### Markdown heading

<a id="md-heading"></a>`md-heading`, on thread-dark-table.

<img src="components/crops/md-heading-default.png" alt="Markdown heading, default" height="28"> <img src="components/crops/md-heading-light.png" alt="Markdown heading, light" height="28"> 

| State | Values |
|---|---|
| default | size 768 x `size.control.sm`; background transparent; text `fontSize.lg`/28 `fontWeight.semibold`, `role.text.primary` |
| light | size 768 x `size.control.sm`; background transparent; text `fontSize.lg`/28 `fontWeight.semibold`, `role.text.primary` |

#### Markdown strong

<a id="md-strong"></a>`md-strong`, on thread-dark-table.

<img src="components/crops/md-strong-default.png" alt="Markdown strong, default" height="24"> <img src="components/crops/md-strong-light.png" alt="Markdown strong, light" height="24"> 

| State | Values |
|---|---|
| default | size 357.2 x `size.icon.md`; background transparent; text `fontSize.base`/26 `fontWeight.semibold`, `role.text.primary` |
| light | size 357.2 x `size.icon.md`; background transparent; text `fontSize.base`/26 `fontWeight.semibold`, `role.text.primary` |

#### Inline code

<a id="md-inline-code"></a>`md-inline-code`, on thread-dark-code.

<img src="components/crops/md-inline-code-default.png" alt="Inline code, default" height="24"> <img src="components/crops/md-inline-code-light.png" alt="Inline code, light" height="24"> 

| State | Values |
|---|---|
| default | size 17.28 x 19.47; padding 0.744px 4.1664px; radius 3.72px; background rgba(33, 33, 33, 0.82); text Mono 14.88/26 500, `role.text.primary` |
| light | size 17.28 x 19.47; padding 0.744px 4.1664px; radius 3.72px; background rgba(243, 243, 243, 0.82); text Mono 14.88/26 500, `role.text.primary` |

#### Link (citation in an answer)

<a id="md-link"></a>`md-link`, on thread-dark-table.

<img src="components/crops/md-link-default.png" alt="Link (citation in an answer), default" height="24"> <img src="components/crops/md-link-hover.png" alt="Link (citation in an answer), hover" height="24"> <img src="components/crops/md-link-focus-visible.png" alt="Link (citation in an answer), focus-visible" height="24"> <img src="components/crops/md-link-light.png" alt="Link (citation in an answer), light" height="24"> <img src="components/crops/md-link-light-hover.png" alt="Link (citation in an answer), light-hover" height="24"> <img src="components/crops/md-link-light-focus-visible.png" alt="Link (citation in an answer), light-focus-visible" height="24"> 

| State | Values |
|---|---|
| default | size 129.94 x `size.icon.md`; padding 0 `spacing.2` 0 `spacing.1`; radius `radius.xl`; background `surface.elevated-secondary`; text System 9/9 500, `role.text.secondary`; icon 12 x 12, `role.text.secondary` |
| hover | background `variant.primary.soft.bg-hover`; text System 9/9 500, `role.text.primary`; icon 12 x 12, `role.text.primary` |
| focus-visible | outline 1px auto #99c8ff, offset 1px |
| light | size 129.94 x `size.icon.md`; padding 0 `spacing.2` 0 `spacing.1`; radius `radius.xl`; background `bg.user-message-compact`; text System 9/9 500, `role.text.secondary`; icon 12 x 12, `role.text.secondary` |
| light-hover | background `variant.primary.soft.bg-hover`; text System 9/9 500, `role.text.primary`; icon 12 x 12, `role.text.primary` |
| light-focus-visible | outline 1px auto #005fcc, offset 1px |

#### Code block

<a id="code-block"></a>`code-block`, on thread-dark-code.

<img src="components/crops/code-block-default.png" alt="Code block, default" height="120"> <img src="components/crops/code-block-light.png" alt="Code block, light" height="120"> 

| State | Values |
|---|---|
| default | size 768 x 262; border 1px solid `role.border.subtle`; radius `radius.3xl`; background `surface.elevated-secondary`; image linear-gradient(`variant.primary.soft.bg-hover`, `variant.primary.soft.bg-hover`); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light | size 768 x 262; border 1px solid `role.border.subtle`; radius `radius.3xl`; background `bg.user-message-compact`; image linear-gradient(`variant.primary.soft.bg-hover`, `variant.primary.soft.bg-hover`); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.primary` |

#### Code text (inside a code block)

<a id="code-text"></a>`code-text`, on thread-dark-code. The `code` element itself, not the language label in the block header; `typography.code` is read from it.

<img src="components/crops/code-text-default.png" alt="Code text (inside a code block), default" height="120"> <img src="components/crops/code-text-light.png" alt="Code text (inside a code block), light" height="120"> 

| State | Values |
|---|---|
| default | size 462.45 x 194; background transparent; text `typography.code`, #f8a6c8 |
| light | size 462.45 x 194; background transparent; text `typography.code`, #ab4f7a |

#### Code block icon button

<a id="code-block-button"></a>`code-block-button`, on thread-dark-code.

<img src="components/crops/code-block-button-default.png" alt="Code block icon button, default" height="36"> <img src="components/crops/code-block-button-hover.png" alt="Code block icon button, hover" height="36"> <img src="components/crops/code-block-button-focus-visible.png" alt="Code block icon button, focus-visible" height="36"> <img src="components/crops/code-block-button-pressed.png" alt="Code block icon button, pressed" height="36"> <img src="components/crops/code-block-button-light.png" alt="Code block icon button, light" height="36"> <img src="components/crops/code-block-button-light-hover.png" alt="Code block icon button, light-hover" height="36"> <img src="components/crops/code-block-button-light-focus-visible.png" alt="Code block icon button, light-focus-visible" height="36"> <img src="components/crops/code-block-button-light-pressed.png" alt="Code block icon button, light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 36 x `size.control.lg`; radius `radius.full`; background transparent; icon 20 x 20, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 36 x `size.control.lg`; radius `radius.full`; background transparent; icon 20 x 20, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Table

<a id="md-table"></a>`md-table`, on thread-dark-table.

<img src="components/crops/md-table-default.png" alt="Table, default" height="120"> <img src="components/crops/md-table-light.png" alt="Table, light" height="120"> 

| State | Values |
|---|---|
| default | size 1408 x 447; background transparent; text `fontSize.sm`/16 `fontWeight.semibold`, `role.text.primary`; icon 12 x 12, `role.text.secondary` |
| light | size 1408 x 447; background transparent; text `fontSize.sm`/16 `fontWeight.semibold`, `role.text.primary`; icon 12 x 12, `role.text.secondary` |

Child layers: th 128x33 border 1px solid `role.border.strong`; th 448x33 border 1px solid `role.border.strong`; th 128x33 border 1px solid `role.border.strong`

#### Table header cell

<a id="md-th"></a>`md-th`, on thread-dark-table.

<img src="components/crops/md-th-default.png" alt="Table header cell, default" height="33"> <img src="components/crops/md-th-light.png" alt="Table header cell, light" height="33"> 

| State | Values |
|---|---|
| default | size 128 x 33; padding `spacing.2` `spacing.6` `spacing.2` 0; border B: 1px solid `role.border.strong`; background transparent; text `fontSize.sm`/16 `fontWeight.semibold`, `role.text.primary` |
| light | size 128 x 33; padding `spacing.2` `spacing.6` `spacing.2` 0; border B: 1px solid `role.border.strong`; background transparent; text `fontSize.sm`/16 `fontWeight.semibold`, `role.text.primary` |

Child layers: th 128x33 border 1px solid `role.border.strong`

#### Table cell

<a id="md-td"></a>`md-td`, on thread-dark-table.

<img src="components/crops/md-td-default.png" alt="Table cell, default" height="120"> <img src="components/crops/md-td-light.png" alt="Table cell, light" height="120"> 

| State | Values |
|---|---|
| default | size 128 x 125; padding `spacing.2_5` `spacing.6` `spacing.2_5` 0; border B: 1px solid `role.border.subtle`; background transparent; text `fontSize.sm`/26 `fontWeight.semibold`, `role.text.primary` |
| light | size 128 x 125; padding `spacing.2_5` `spacing.6` `spacing.2_5` 0; border B: 1px solid `role.border.subtle`; background transparent; text `fontSize.sm`/26 `fontWeight.semibold`, `role.text.primary` |

Child layers: td 128x125 border 1px solid `role.border.subtle`

#### Turn action button (Copy)

<a id="turn-action"></a>`turn-action`, on thread-dark-code.

<img src="components/crops/turn-action-default.png" alt="Turn action button (Copy), default" height="32"> <img src="components/crops/turn-action-hover.png" alt="Turn action button (Copy), hover" height="32"> <img src="components/crops/turn-action-focus-visible.png" alt="Turn action button (Copy), focus-visible" height="32"> <img src="components/crops/turn-action-pressed.png" alt="Turn action button (Copy), pressed" height="32"> <img src="components/crops/turn-action-light.png" alt="Turn action button (Copy), light" height="32"> <img src="components/crops/turn-action-light-hover.png" alt="Turn action button (Copy), light-hover" height="32"> <img src="components/crops/turn-action-light-focus-visible.png" alt="Turn action button (Copy), light-focus-visible" height="32"> <img src="components/crops/turn-action-light-pressed.png" alt="Turn action button (Copy), light-pressed" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.control.md`; border 1px solid transparent; radius `radius.lg`; background transparent; icon 20 x 20, `role.text.disabled` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 32 x `size.control.md`; border 1px solid transparent; radius `radius.lg`; background transparent; icon 20 x 20, `role.text.disabled` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Scroll to bottom button

<a id="scroll-button"></a>`scroll-button`, on thread-dark-user-turn.

<img src="components/crops/scroll-button-default.png" alt="Scroll to bottom button, default" height="32"> <img src="components/crops/scroll-button-hover.png" alt="Scroll to bottom button, hover" height="32"> <img src="components/crops/scroll-button-focus-visible.png" alt="Scroll to bottom button, focus-visible" height="32"> <img src="components/crops/scroll-button-pressed.png" alt="Scroll to bottom button, pressed" height="32"> <img src="components/crops/scroll-button-light.png" alt="Scroll to bottom button, light" height="32"> <img src="components/crops/scroll-button-light-hover.png" alt="Scroll to bottom button, light-hover" height="32"> <img src="components/crops/scroll-button-light-focus-visible.png" alt="Scroll to bottom button, light-focus-visible" height="32"> <img src="components/crops/scroll-button-light-pressed.png" alt="Scroll to bottom button, light-pressed" height="32"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 32 x `size.control.md`; border 1px solid `role.border.default`; radius `radius.full`; background `role.bg.page`; text `typography.text-md`, `role.text.secondary`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, `role.text.primary` |
| focus-visible | outline 1px auto #99c8ff, offset 0px |
| light (same: light-hover, light-pressed) | size 32 x `size.control.md`; border 1px solid `role.border.default`; radius `radius.full`; background `role.bg.page`; text `typography.text-md`, `role.text.secondary`; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, `role.text.primary` |
| light-focus-visible | outline 1px auto #005fcc, offset 0px |

#### Thread disclaimer

<a id="thread-disclaimer"></a>`thread-disclaimer`, on thread-dark-code.

<img src="components/crops/thread-disclaimer-default.png" alt="Thread disclaimer, default" height="24"> <img src="components/crops/thread-disclaimer-light.png" alt="Thread disclaimer, light" height="24"> 

| State | Values |
|---|---|
| default | size 1067 x `size.icon.sm`; background transparent; text `fontSize.xs`/16 `fontWeight.normal`, `role.text.disabled` |
| light | size 1067 x `size.icon.sm`; background transparent; text `fontSize.xs`/16 `fontWeight.normal`, `role.text.disabled` |

### Menus

The popovers: the chat row menu, the composer + menu (a popover of buttons, not a role=menu), the account menu, a notification channel's checkbox menu and the accent colour listbox. Menus are 90% surfaces with a 16px backdrop blur.

#### Menu (chat row)

<a id="chat-menu"></a>`chat-menu`, on home-dark-chat-menu. Rename, Pin, Share, Archive, Delete (danger), Move to project; hairline separators between groups.

<img src="components/crops/chat-menu-default.png" alt="Menu (chat row), default" height="120"> <img src="components/crops/chat-menu-light.png" alt="Menu (chat row), light" height="120"> 

| State | Values |
|---|---|
| default | size 188.88 x 287; padding `spacing.2_5`; radius `radius.2xl`; background `role.bg.overlay`; shadow rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.12) 0px 8px 16px -4px; backdrop blur(8px); text `typography.text-sm`, `role.text.primary`; icon 16 x 16, `role.text.primary` |
| light | size 188.88 x 287; padding `spacing.2_5`; radius `radius.2xl`; background `role.bg.overlay`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.12) 0px 8px 16px -4px; backdrop blur(8px); text `typography.text-sm`, `role.text.primary`; icon 16 x 16, `role.text.primary` |

#### Menu item

<a id="menu-item"></a>`menu-item`, on home-dark-chat-menu.

<img src="components/crops/menu-item-default.png" alt="Menu item, default" height="36"> <img src="components/crops/menu-item-hover.png" alt="Menu item, hover" height="36"> <img src="components/crops/menu-item-pressed.png" alt="Menu item, pressed" height="36"> <img src="components/crops/menu-item-light.png" alt="Menu item, light" height="36"> <img src="components/crops/menu-item-light-hover.png" alt="Menu item, light-hover" height="36"> <img src="components/crops/menu-item-light-pressed.png" alt="Menu item, light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 168.88 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary` |
| hover, pressed | background `variant.primary.soft.bg-hover` |
| light | size 168.88 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary` |
| light-hover, light-pressed | background `variant.primary.soft.bg-hover` |

Child layers: span 18x18 background `variant.primary.solid.bg`

#### Menu item (Delete, danger)

<a id="menu-item-danger"></a>`menu-item-danger`, on home-dark-chat-menu.

<img src="components/crops/menu-item-danger-default.png" alt="Menu item (Delete, danger), default" height="36"> <img src="components/crops/menu-item-danger-hover.png" alt="Menu item (Delete, danger), hover" height="36"> <img src="components/crops/menu-item-danger-light.png" alt="Menu item (Delete, danger), light" height="36"> <img src="components/crops/menu-item-danger-light-hover.png" alt="Menu item (Delete, danger), light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 168.88 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm`, `text.danger` |
| hover | background `variant.primary.soft.bg-hover` |
| light | size 168.88 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm`, `text.danger` |
| light-hover | background `variant.primary.soft.bg-hover` |

Child layers: span 18x18 background `variant.danger.soft.text`

#### Menu (composer +)

<a id="plus-menu"></a>`plus-menu`, on home-dark-plus-menu. Not a role=menu: a popover of buttons at the composer's width, each with a title and a grey hint.

<img src="components/crops/plus-menu-default.png" alt="Menu (composer +), default" height="36"> <img src="components/crops/plus-menu-light.png" alt="Menu (composer +), light" height="36"> 

| State | Values |
|---|---|
| default | size 750 x `size.control.lg`; padding `spacing.1_5` `spacing.2`; radius `radius.xl`; background `variant.primary.soft.bg-hover`; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light | size 750 x `size.control.lg`; padding `spacing.1_5` `spacing.2`; radius `radius.xl`; background `variant.primary.soft.bg-hover`; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |

#### Menu item with hint (composer +)

<a id="plus-menu-item"></a>`plus-menu-item`, on home-dark-plus-menu.

<img src="components/crops/plus-menu-item-default.png" alt="Menu item with hint (composer +), default" height="36"> <img src="components/crops/plus-menu-item-hover.png" alt="Menu item with hint (composer +), hover" height="36"> <img src="components/crops/plus-menu-item-light.png" alt="Menu item with hint (composer +), light" height="36"> <img src="components/crops/plus-menu-item-light-hover.png" alt="Menu item with hint (composer +), light-hover" height="36"> <img src="components/crops/plus-menu-item-highlighted.png" alt="Menu item with hint (composer +), highlighted" height="36"> <img src="components/crops/plus-menu-item-light-highlighted.png" alt="Menu item with hint (composer +), light-highlighted" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 750 x `size.control.lg`; padding `spacing.1_5` `spacing.2`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| highlighted | background `variant.primary.soft.bg-hover` |
| light (same: light-hover) | size 750 x `size.control.lg`; padding `spacing.1_5` `spacing.2`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light-highlighted | background `variant.primary.soft.bg-hover` |

#### Menu (account)

<a id="user-menu"></a>`user-menu`, on home-dark-user-menu.

<img src="components/crops/user-menu-default.png" alt="Menu (account), default" height="120"> <img src="components/crops/user-menu-light.png" alt="Menu (account), light" height="120"> 

| State | Values |
|---|---|
| default | size 324 x 316; padding `spacing.2_5`; radius `radius.2xl`; background `role.bg.overlay`; shadow rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.12) 0px 8px 16px -4px; backdrop blur(8px); text `fontSize.xs`/17.14 `fontWeight.semibold`, `role.text.on-accent`; icon 16 x 16, `role.text.disabled` |
| light | size 324 x 316; padding `spacing.2_5`; radius `radius.2xl`; background `role.bg.overlay`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.12) 0px 8px 16px -4px; backdrop blur(8px); text `fontSize.xs`/17.14 `fontWeight.semibold`, `role.text.inverse`; icon 16 x 16, `role.text.disabled` |

#### Checkbox menu item (checked)

<a id="checkbox-menu-item"></a>`checkbox-menu-item`, on settings-dark-notifications-menu. `menuitemcheckbox`, aria-checked=true, a trailing check.

<img src="components/crops/checkbox-menu-item-default.png" alt="Checkbox menu item (checked), default" height="36"> <img src="components/crops/checkbox-menu-item-hover.png" alt="Checkbox menu item (checked), hover" height="36"> <img src="components/crops/checkbox-menu-item-light.png" alt="Checkbox menu item (checked), light" height="36"> <img src="components/crops/checkbox-menu-item-light-hover.png" alt="Checkbox menu item (checked), light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 220 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 16 x 16, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| light | size 220 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 16 x 16, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |

#### Select listbox (accent colour)

<a id="accent-menu"></a>`accent-menu`, on settings-dark-accent-menu. Default, Blue (checked), Green, Yellow, Pink, Orange, Purple, White, Custom; each with a colour dot.

<img src="components/crops/accent-menu-default.png" alt="Select listbox (accent colour), default" height="120"> <img src="components/crops/accent-menu-light.png" alt="Select listbox (accent colour), light" height="120"> 

| State | Values |
|---|---|
| default | size 240 x 344; padding `spacing.2_5`; radius `radius.2xl`; background `role.bg.overlay`; shadow rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.12) 0px 8px 16px -4px; backdrop blur(8px); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 18 x 18, `role.text.primary` |
| light | size 240 x 344; padding `spacing.2_5`; radius `radius.2xl`; background `role.bg.overlay`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.12) 0px 8px 16px -4px; backdrop blur(8px); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 18 x 18, `role.text.primary` |

#### Select option (accent)

<a id="accent-item"></a>`accent-item`, on settings-dark-accent-menu.

<img src="components/crops/accent-item-default.png" alt="Select option (accent), default" height="36"> <img src="components/crops/accent-item-hover.png" alt="Select option (accent), hover" height="36"> <img src="components/crops/accent-item-light.png" alt="Select option (accent), light" height="36"> <img src="components/crops/accent-item-light-hover.png" alt="Select option (accent), light-hover" height="36"> <img src="components/crops/accent-item-checked.png" alt="Select option (accent), checked" height="36"> <img src="components/crops/accent-item-light-checked.png" alt="Select option (accent), light-checked" height="36"> 

| State | Values |
|---|---|
| default | size 220 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| checked | icon 18 x 18, `role.text.primary` |
| light | size 220 x `size.control.lg`; padding `spacing.1_5` `spacing.2_5`; radius `radius.xl`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-checked | icon 18 x 18, `role.text.primary` |

Child layers: span 12x12 background #04bb9f border 1px solid `role.border.default` radius 9999px

### Dialogs

The delete confirmation (420 wide, a danger action and Cancel) and the global search dialog with its filter tabs and empty state.

#### Dialog (delete confirmation)

<a id="confirm-dialog"></a>`confirm-dialog`, on home-dark-delete-confirm. 420 wide: title, body naming the chat, Cancel and a danger Delete chat, close in the corner.

<img src="components/crops/confirm-dialog-default.png" alt="Dialog (delete confirmation), default" height="120"> <img src="components/crops/confirm-dialog-light.png" alt="Dialog (delete confirmation), light" height="120"> 

| State | Values |
|---|---|
| default | size 420 x 164; radius `radius.3xl`; background `role.bg.overlay`; shadow rgba(255, 255, 255, 0.15) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.1) 0px 4px 8px -2px; backdrop blur(24px); text `fontSize.xl`/28 `fontWeight.semibold`, `role.text.primary`; transition height 0.3s cubic-bezier(0.23, 1, 0.32, 1); icon 16 x 16, `text.tooltip-tertiary` |
| light | size 420 x 164; radius `radius.3xl`; background `role.bg.overlay`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.1) 0px 4px 8px -2px; backdrop blur(24px); text `fontSize.xl`/28 `fontWeight.semibold`, `role.text.primary`; transition height 0.3s cubic-bezier(0.23, 1, 0.32, 1); icon 16 x 16, rgba(13, 13, 13, 0.8) |

#### Dialog backdrop

<a id="dialog-backdrop"></a>`dialog-backdrop`, on home-dark-delete-confirm.

| State | Values |
|---|---|
| default | size 1440 x 900; background `role.bg.scrim` |
| light | size 1440 x 900; background `role.bg.scrim` |

#### Danger button (Delete chat)

<a id="button-danger"></a>`button-danger`, on home-dark-delete-confirm.

<img src="components/crops/button-danger-default.png" alt="Danger button (Delete chat), default" height="32"> <img src="components/crops/button-danger-hover.png" alt="Danger button (Delete chat), hover" height="32"> <img src="components/crops/button-danger-focus-visible.png" alt="Danger button (Delete chat), focus-visible" height="32"> <img src="components/crops/button-danger-pressed.png" alt="Danger button (Delete chat), pressed" height="32"> <img src="components/crops/button-danger-light.png" alt="Danger button (Delete chat), light" height="32"> <img src="components/crops/button-danger-light-hover.png" alt="Danger button (Delete chat), light-hover" height="32"> <img src="components/crops/button-danger-light-focus-visible.png" alt="Danger button (Delete chat), light-focus-visible" height="32"> <img src="components/crops/button-danger-light-pressed.png" alt="Danger button (Delete chat), light-pressed" height="32"> 

| State | Values |
|---|---|
| default | size 116.86 x `size.control.md`; padding `spacing.1_5` `spacing.4`; border 1px solid transparent; radius `radius.full`; background `component.button-danger.bg`; text `fontSize.base`/18 `fontWeight.normal`, `text.danger` |
| hover | background `component.button-danger.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `component.button-danger.bg-hover` |
| light | size 116.86 x `size.control.md`; padding `spacing.1_5` `spacing.4`; border 1px solid transparent; radius `radius.full`; background `component.button-danger.bg`; text `fontSize.base`/18 `fontWeight.normal`, `text.danger` |
| light-hover | background `component.button-danger.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `component.button-danger.bg-hover` |

#### Secondary button (Cancel)

<a id="button-secondary"></a>`button-secondary`, on home-dark-delete-confirm.

<img src="components/crops/button-secondary-default.png" alt="Secondary button (Cancel), default" height="32"> <img src="components/crops/button-secondary-hover.png" alt="Secondary button (Cancel), hover" height="32"> <img src="components/crops/button-secondary-focus-visible.png" alt="Secondary button (Cancel), focus-visible" height="32"> <img src="components/crops/button-secondary-pressed.png" alt="Secondary button (Cancel), pressed" height="32"> <img src="components/crops/button-secondary-light.png" alt="Secondary button (Cancel), light" height="32"> <img src="components/crops/button-secondary-light-hover.png" alt="Secondary button (Cancel), light-hover" height="32"> <img src="components/crops/button-secondary-light-focus-visible.png" alt="Secondary button (Cancel), light-focus-visible" height="32"> <img src="components/crops/button-secondary-light-pressed.png" alt="Secondary button (Cancel), light-pressed" height="32"> 

| State | Values |
|---|---|
| default | size 83.89 x `size.control.md`; padding `spacing.1_5` `spacing.4`; border 1px solid `role.border.default`; radius `radius.full`; background `surface.elevated-secondary`; text `fontSize.base`/18 `fontWeight.normal`, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 83.89 x `size.control.md`; padding `spacing.1_5` `spacing.4`; border 1px solid `role.border.default`; radius `radius.full`; background `bg.user-message-compact`; text `fontSize.base`/18 `fontWeight.normal`, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Dialog close button

<a id="dialog-close"></a>`dialog-close`, on home-dark-delete-confirm.

<img src="components/crops/dialog-close-default.png" alt="Dialog close button, default" height="24"> <img src="components/crops/dialog-close-hover.png" alt="Dialog close button, hover" height="24"> <img src="components/crops/dialog-close-focus-visible.png" alt="Dialog close button, focus-visible" height="24"> <img src="components/crops/dialog-close-pressed.png" alt="Dialog close button, pressed" height="24"> <img src="components/crops/dialog-close-light.png" alt="Dialog close button, light" height="24"> <img src="components/crops/dialog-close-light-hover.png" alt="Dialog close button, light-hover" height="24"> <img src="components/crops/dialog-close-light-focus-visible.png" alt="Dialog close button, light-focus-visible" height="24"> <img src="components/crops/dialog-close-light-pressed.png" alt="Dialog close button, light-pressed" height="24"> 

| State | Values |
|---|---|
| default | size 24 x `size.control.2xs`; padding `spacing.1`; radius `radius.sm`; background transparent; text `typography.onboarding-label`, `text.tooltip-tertiary`; icon 16 x 16, `text.tooltip-tertiary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 24 x `size.control.2xs`; padding `spacing.1`; radius `radius.sm`; background transparent; text `typography.onboarding-label`, rgba(13, 13, 13, 0.8); icon 16 x 16, rgba(13, 13, 13, 0.8) |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Dialog (global search)

<a id="search-dialog"></a>`search-dialog`, on home-dark-search.

<img src="components/crops/search-dialog-default.png" alt="Dialog (global search), default" height="120"> <img src="components/crops/search-dialog-light.png" alt="Dialog (global search), light" height="120"> 

| State | Values |
|---|---|
| default | size 720 x 460; border 1px solid `role.border.default`; radius `radius.2xl`; background `role.bg.surface`; shadow rgba(0, 0, 0, 0.19) 0px 16px 32px -8px; text `typography.text-sm`, `role.text.secondary`; transform translate(-360px, -230px); icon 20 x 20, `role.text.secondary`; placeholder `role.text.disabled` |
| light | size 720 x 460; border 1px solid `role.border.default`; radius `radius.2xl`; background `role.bg.raised`; shadow rgba(0, 0, 0, 0.19) 0px 16px 32px -8px; text `typography.text-sm`, `role.text.secondary`; transform translate(-360px, -230px); icon 20 x 20, `role.text.secondary`; placeholder `role.text.disabled` |

#### Text field (search)

<a id="search-field"></a>`search-field`, on home-dark-search, home-dark-search-empty.

<img src="components/crops/search-field-default.png" alt="Text field (search), default" height="24"> <img src="components/crops/search-field-focus-visible.png" alt="Text field (search), focus-visible" height="24"> <img src="components/crops/search-field-light.png" alt="Text field (search), light" height="24"> <img src="components/crops/search-field-typed.png" alt="Text field (search), typed" height="24"> <img src="components/crops/search-field-light-focus-visible.png" alt="Text field (search), light-focus-visible" height="24"> <img src="components/crops/search-field-light-typed.png" alt="Text field (search), light-typed" height="24"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 642 x `size.control.2xs`; background transparent; text `typography.text-md`, `role.text.primary`; placeholder `role.text.disabled` |
| typed | size 565.13 x `size.control.2xs` |
| light (same: light-focus-visible) | size 642 x `size.control.2xs`; background transparent; text `typography.text-md`, `role.text.primary`; placeholder `role.text.disabled` |
| light-typed | size 565.13 x `size.control.2xs` |

#### List row (search result)

<a id="search-result"></a>`search-result`, on home-dark-search.

<img src="components/crops/search-result-default.png" alt="List row (search result), default" height="48"> <img src="components/crops/search-result-hover.png" alt="List row (search result), hover" height="48"> <img src="components/crops/search-result-focus-visible.png" alt="List row (search result), focus-visible" height="48"> <img src="components/crops/search-result-light.png" alt="List row (search result), light" height="48"> <img src="components/crops/search-result-light-hover.png" alt="List row (search result), light-hover" height="48"> <img src="components/crops/search-result-light-focus-visible.png" alt="List row (search result), light-focus-visible" height="48"> 

| State | Values |
|---|---|
| default (same: hover) | size 694 x `size.control.3xl`; padding `spacing.2` `spacing.3`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| focus-visible | outline 2px solid `role.border.strong`, offset -2px |
| light (same: light-hover) | size 694 x `size.control.3xl`; padding `spacing.2` `spacing.3`; radius `radius.xl`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light-focus-visible | outline 2px solid `role.border.strong`, offset -2px |

#### Tab (search filter)

<a id="search-tab"></a>`search-tab`, on home-dark-search-empty.

<img src="components/crops/search-tab-default.png" alt="Tab (search filter), default" height="36"> <img src="components/crops/search-tab-hover.png" alt="Tab (search filter), hover" height="36"> <img src="components/crops/search-tab-focus-visible.png" alt="Tab (search filter), focus-visible" height="36"> <img src="components/crops/search-tab-pressed.png" alt="Tab (search filter), pressed" height="36"> <img src="components/crops/search-tab-light.png" alt="Tab (search filter), light" height="36"> <img src="components/crops/search-tab-light-hover.png" alt="Tab (search filter), light-hover" height="36"> <img src="components/crops/search-tab-selected.png" alt="Tab (search filter), selected" height="36"> <img src="components/crops/search-tab-light-focus-visible.png" alt="Tab (search filter), light-focus-visible" height="36"> <img src="components/crops/search-tab-light-pressed.png" alt="Tab (search filter), light-pressed" height="36"> <img src="components/crops/search-tab-light-selected.png" alt="Tab (search filter), light-selected" height="36"> 

| State | Values |
|---|---|
| default | size 61.52 x `size.control.lg`; padding 0 `spacing.3`; radius `radius.full`; background transparent; text `typography.text-sm`, `role.text.secondary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| selected | size 40.08 x `size.control.lg`; background `bg.disabled`; text `typography.text-sm`, `role.text.primary` |
| light | size 61.52 x `size.control.lg`; padding 0 `spacing.3`; radius `radius.full`; background transparent; text `typography.text-sm`, `role.text.secondary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |
| light-selected | size 40.08 x `size.control.lg`; background `bg.disabled`; text `typography.text-sm`, `role.text.primary` |

#### Empty state (no results)

<a id="search-empty"></a>`search-empty`, on home-dark-search-empty.

<img src="components/crops/search-empty-default.png" alt="Empty state (no results), default" height="120"> <img src="components/crops/search-empty-light.png" alt="Empty state (no results), light" height="120"> 

| State | Values |
|---|---|
| default | size 718 x 333; padding `spacing.5` `spacing.6`; background transparent; text `typography.text-md`, `role.text.disabled`; icon 20 x 20, `role.text.disabled` |
| light | size 718 x 333; padding `spacing.5` `spacing.6`; background transparent; text `typography.text-md`, `role.text.disabled`; icon 20 x 20, `role.text.disabled` |

### Library

The file library: title, filter, grid and list view buttons, search, New, pill tabs, then a masonry grid of file cards with a hover checkbox. Also its error state and a partial-results banner.

#### Page title (Library)

<a id="library-title"></a>`library-title`, on library-dark.

<img src="components/crops/library-title-default.png" alt="Page title (Library), default" height="36"> <img src="components/crops/library-title-light.png" alt="Page title (Library), light" height="36"> 

| State | Values |
|---|---|
| default | size 74.11 x `size.control.lg`; background transparent; text `fontSize.2xl`/28.8 `fontWeight.medium`, `role.text.primary` |
| light | size 74.11 x `size.control.lg`; background transparent; text `fontSize.2xl`/28.8 `fontWeight.medium`, `role.text.primary` |

#### Icon button (List view)

<a id="library-icon-button"></a>`library-icon-button`, on library-dark.

<img src="components/crops/library-icon-button-default.png" alt="Icon button (List view), default" height="36"> <img src="components/crops/library-icon-button-hover.png" alt="Icon button (List view), hover" height="36"> <img src="components/crops/library-icon-button-focus-visible.png" alt="Icon button (List view), focus-visible" height="36"> <img src="components/crops/library-icon-button-pressed.png" alt="Icon button (List view), pressed" height="36"> <img src="components/crops/library-icon-button-light.png" alt="Icon button (List view), light" height="36"> <img src="components/crops/library-icon-button-light-hover.png" alt="Icon button (List view), light-hover" height="36"> <img src="components/crops/library-icon-button-selected.png" alt="Icon button (List view), selected" height="36"> <img src="components/crops/library-icon-button-light-focus-visible.png" alt="Icon button (List view), light-focus-visible" height="36"> <img src="components/crops/library-icon-button-light-pressed.png" alt="Icon button (List view), light-pressed" height="36"> <img src="components/crops/library-icon-button-light-selected.png" alt="Icon button (List view), light-selected" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 36 x `size.control.lg`; radius `radius.full`; background transparent; text `fontSize.sm`/14 `fontWeight.medium`, `role.text.secondary`; transition opacity 0.15s ease, color 0.15s ease; icon 20 x 20, `role.text.secondary` |
| hover, pressed, selected | text `fontSize.sm`/14 `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light (same: light-focus-visible) | size 36 x `size.control.lg`; radius `radius.full`; background transparent; text `fontSize.sm`/14 `fontWeight.medium`, `role.text.secondary`; transition opacity 0.15s ease, color 0.15s ease; icon 20 x 20, `role.text.secondary` |
| light-hover, light-pressed, light-selected | text `fontSize.sm`/14 `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.primary` |

Child layers: button 36pxx36px background `variant.primary.soft.bg-hover` radius 9999px

#### Text field (Search library)

<a id="library-search"></a>`library-search`, on library-dark.

<img src="components/crops/library-search-default.png" alt="Text field (Search library), default" height="36"> <img src="components/crops/library-search-hover.png" alt="Text field (Search library), hover" height="36"> <img src="components/crops/library-search-focus-visible.png" alt="Text field (Search library), focus-visible" height="36"> <img src="components/crops/library-search-light.png" alt="Text field (Search library), light" height="36"> <img src="components/crops/library-search-light-hover.png" alt="Text field (Search library), light-hover" height="36"> <img src="components/crops/library-search-light-focus-visible.png" alt="Text field (Search library), light-focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 240 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid `role.border.strong`; radius `radius.full`; background transparent; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 20 x 20, `role.text.secondary`; placeholder `role.text.disabled` |
| light (same: light-hover, light-focus-visible) | size 240 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid `role.border.strong`; radius `radius.full`; background transparent; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 20 x 20, `role.text.secondary`; placeholder `role.text.disabled` |

#### Inverted button (New)

<a id="library-new"></a>`library-new`, on library-dark.

<img src="components/crops/library-new-default.png" alt="Inverted button (New), default" height="36"> <img src="components/crops/library-new-hover.png" alt="Inverted button (New), hover" height="36"> <img src="components/crops/library-new-focus-visible.png" alt="Inverted button (New), focus-visible" height="36"> <img src="components/crops/library-new-pressed.png" alt="Inverted button (New), pressed" height="36"> <img src="components/crops/library-new-light.png" alt="Inverted button (New), light" height="36"> <img src="components/crops/library-new-light-hover.png" alt="Inverted button (New), light-hover" height="36"> <img src="components/crops/library-new-light-focus-visible.png" alt="Inverted button (New), light-focus-visible" height="36"> <img src="components/crops/library-new-light-pressed.png" alt="Inverted button (New), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 74.78 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid `role.border.default`; radius `radius.full`; background `variant.primary.solid.bg`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.inverse`; icon 16 x 16, `role.text.inverse` |
| hover | background `text.tooltip-tertiary` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `text.tooltip-tertiary` |
| light | size 74.78 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid `role.border.default`; radius `radius.full`; background `variant.primary.solid.bg`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.inverse`; icon 16 x 16, `role.text.inverse` |
| light-hover | background rgba(13, 13, 13, 0.8) |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background rgba(13, 13, 13, 0.8) |

#### Tab (Library)

<a id="library-tab"></a>`library-tab`, on library-dark.

<img src="components/crops/library-tab-default.png" alt="Tab (Library), default" height="36"> <img src="components/crops/library-tab-hover.png" alt="Tab (Library), hover" height="36"> <img src="components/crops/library-tab-focus-visible.png" alt="Tab (Library), focus-visible" height="36"> <img src="components/crops/library-tab-pressed.png" alt="Tab (Library), pressed" height="36"> <img src="components/crops/library-tab-light.png" alt="Tab (Library), light" height="36"> <img src="components/crops/library-tab-light-hover.png" alt="Tab (Library), light-hover" height="36"> <img src="components/crops/library-tab-selected.png" alt="Tab (Library), selected" height="36"> <img src="components/crops/library-tab-light-focus-visible.png" alt="Tab (Library), light-focus-visible" height="36"> <img src="components/crops/library-tab-light-pressed.png" alt="Tab (Library), light-pressed" height="36"> <img src="components/crops/library-tab-light-selected.png" alt="Tab (Library), light-selected" height="36"> 

| State | Values |
|---|---|
| default | size 94.03 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.secondary` |
| hover | background `token.border-light`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| pressed | background `token.border-light`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| selected | size 105.28 x `size.control.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light | size 94.03 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.secondary` |
| light-hover | background rgba(0, 0, 0, 0.03); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| light-pressed | background rgba(0, 0, 0, 0.03); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light-selected | size 105.28 x `size.control.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |

#### Card (Library file)

<a id="library-card"></a>`library-card`, on library-dark. Masonry grid cards (5 columns at 1440): a thumbnail (blanked in the copies) over the file name.

<img src="components/crops/library-card-default.png" alt="Card (Library file), default" height="120"> <img src="components/crops/library-card-hover.png" alt="Card (Library file), hover" height="120"> <img src="components/crops/library-card-light.png" alt="Card (Library file), light" height="120"> <img src="components/crops/library-card-light-hover.png" alt="Card (Library file), light-hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 238.75 x 159.83; border 1px solid `role.border.subtle`; radius `radius.2xl`; background `role.bg.raised`; shadow rgba(0, 0, 0, 0.05) 0px 4px 16px 0px; icon 20 x 20, `role.text.on-accent` |
| light (same: light-hover) | size 238.75 x 159.83; border 1px solid `role.border.subtle`; radius `radius.2xl`; background `role.bg.raised`; shadow rgba(0, 0, 0, 0.05) 0px 4px 16px 0px; icon 20 x 20, `role.text.inverse` |

#### Checkbox (select a file)

<a id="checkbox"></a>`checkbox`, on library-dark. A 20x20 `role=checkbox` button on each card, shown on hover.

<img src="components/crops/checkbox-hover.png" alt="Checkbox (select a file), hover" height="24"> <img src="components/crops/checkbox-focus-visible.png" alt="Checkbox (select a file), focus-visible" height="24"> <img src="components/crops/checkbox-light-hover.png" alt="Checkbox (select a file), light-hover" height="24"> <img src="components/crops/checkbox-light-focus-visible.png" alt="Checkbox (select a file), light-focus-visible" height="24"> 

| State | Values |
|---|---|
| hover | size 20 x `size.control.4xs`; border 1px solid `role.border.default`; radius `radius.sm`; background `role.bg.page`; shadow rgba(0, 0, 0, 0.13) 0px 2px 4px -1px; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | border 1px solid `role.border.focus`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-hover | size 20 x `size.control.4xs`; border 1px solid `role.border.default`; radius `radius.sm`; background `role.bg.page`; shadow rgba(0, 0, 0, 0.13) 0px 2px 4px -1px; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| light-focus-visible | border 1px solid `role.border.focus`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |

#### Error state (Failed to load files)

<a id="library-error"></a>`library-error`, on library-dark-error. Shown when the file list request fails (the capture guard refused it); a centred line and a Try again button.

<img src="components/crops/library-error-default.png" alt="Error state (Failed to load files), default" height="120"> <img src="components/crops/library-error-light.png" alt="Error state (Failed to load files), light" height="120"> 

| State | Values |
|---|---|
| default | size 1003 x 160; padding 48px 0; background transparent; text `typography.text-md`, `role.text.primary` |
| light | size 1003 x 160; padding 48px 0; background transparent; text `typography.text-md`, `role.text.primary` |

Child layers: button 77x24 background `variant.primary.solid.bg` border 1px solid `role.border.default` radius 9999px

#### Small button (Try again)

<a id="retry-button"></a>`retry-button`, on library-dark-error.

<img src="components/crops/retry-button-default.png" alt="Small button (Try again), default" height="24"> <img src="components/crops/retry-button-hover.png" alt="Small button (Try again), hover" height="24"> <img src="components/crops/retry-button-focus-visible.png" alt="Small button (Try again), focus-visible" height="24"> <img src="components/crops/retry-button-pressed.png" alt="Small button (Try again), pressed" height="24"> <img src="components/crops/retry-button-light.png" alt="Small button (Try again), light" height="24"> <img src="components/crops/retry-button-light-hover.png" alt="Small button (Try again), light-hover" height="24"> <img src="components/crops/retry-button-light-focus-visible.png" alt="Small button (Try again), light-focus-visible" height="24"> <img src="components/crops/retry-button-light-pressed.png" alt="Small button (Try again), light-pressed" height="24"> 

| State | Values |
|---|---|
| default | size 77.05 x `size.control.2xs`; padding `spacing.0_5` `spacing.2`; border 1px solid `role.border.default`; radius `radius.full`; background `variant.primary.solid.bg`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.inverse` |
| hover | background `text.tooltip-tertiary` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `text.tooltip-tertiary` |
| light | size 77.05 x `size.control.2xs`; padding `spacing.0_5` `spacing.2`; border 1px solid `role.border.default`; radius `radius.full`; background `variant.primary.solid.bg`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.inverse` |
| light-hover | background rgba(13, 13, 13, 0.8) |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background rgba(13, 13, 13, 0.8) |

#### Inline error (partial search results)

<a id="inline-error"></a>`inline-error`, on library-dark-search-error.

<img src="components/crops/inline-error-default.png" alt="Inline error (partial search results), default" height="56"> <img src="components/crops/inline-error-light.png" alt="Inline error (partial search results), light" height="56"> 

| State | Values |
|---|---|
| default | size 1003 x 56; padding `spacing.4` 0; background transparent; text `typography.text-md`, `role.text.primary` |
| light | size 1003 x 56; padding `spacing.4` 0; background transparent; text `typography.text-md`, `role.text.primary` |

Child layers: button 77x24 background `variant.primary.solid.bg` border 1px solid `role.border.default` radius 9999px

### Images

The Images page: Trending and Templates tabs over a grid of template cards (OpenAI's own sample images).

#### Tab (Images)

<a id="images-tab"></a>`images-tab`, on images-dark.

<img src="components/crops/images-tab-default.png" alt="Tab (Images), default" height="36"> <img src="components/crops/images-tab-hover.png" alt="Tab (Images), hover" height="36"> <img src="components/crops/images-tab-focus-visible.png" alt="Tab (Images), focus-visible" height="36"> <img src="components/crops/images-tab-pressed.png" alt="Tab (Images), pressed" height="36"> <img src="components/crops/images-tab-light.png" alt="Tab (Images), light" height="36"> <img src="components/crops/images-tab-light-hover.png" alt="Tab (Images), light-hover" height="36"> <img src="components/crops/images-tab-selected.png" alt="Tab (Images), selected" height="36"> <img src="components/crops/images-tab-light-focus-visible.png" alt="Tab (Images), light-focus-visible" height="36"> <img src="components/crops/images-tab-light-pressed.png" alt="Tab (Images), light-pressed" height="36"> <img src="components/crops/images-tab-light-selected.png" alt="Tab (Images), light-selected" height="36"> 

| State | Values |
|---|---|
| default | size 102.16 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.secondary` |
| hover | background `token.border-light`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| pressed | background `token.border-light`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| selected | size 92.25 x `size.control.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light | size 102.16 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.secondary` |
| light-hover | background rgba(0, 0, 0, 0.03); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| light-pressed | background rgba(0, 0, 0, 0.03); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light-selected | size 92.25 x `size.control.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |

#### Card (image template)

<a id="image-card"></a>`image-card`, on images-dark.

<img src="components/crops/image-card-default.png" alt="Card (image template), default" height="120"> <img src="components/crops/image-card-hover.png" alt="Card (image template), hover" height="120"> <img src="components/crops/image-card-light.png" alt="Card (image template), light" height="120"> <img src="components/crops/image-card-light-hover.png" alt="Card (image template), light-hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 139.19 x 173.98; radius `radius.2xl`; background `role.bg.page`; text `typography.text-sm` at `fontWeight.medium`, `role.text.on-accent` |
| light (same: light-hover) | size 139.19 x 173.98; radius `radius.2xl`; background `role.bg.page`; text `typography.text-sm` at `fontWeight.medium`, `role.text.inverse` |

### Plugins

The plugin store: Plugins / Skills tabs, a search field and plugin rows. The installed plugins were blanked in the copy.

#### Text field (Search plugins)

<a id="plugins-search"></a>`plugins-search`, on plugins-dark.

<img src="components/crops/plugins-search-default.png" alt="Text field (Search plugins), default" height="44"> <img src="components/crops/plugins-search-hover.png" alt="Text field (Search plugins), hover" height="44"> <img src="components/crops/plugins-search-focus-visible.png" alt="Text field (Search plugins), focus-visible" height="44"> <img src="components/crops/plugins-search-light.png" alt="Text field (Search plugins), light" height="44"> <img src="components/crops/plugins-search-light-hover.png" alt="Text field (Search plugins), light-hover" height="44"> <img src="components/crops/plugins-search-light-focus-visible.png" alt="Text field (Search plugins), light-focus-visible" height="44"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 920 x `size.control.2xl`; padding 0 `spacing.2_5`; border 1px solid `role.border.strong`; radius `radius.full`; background `role.bg.raised`; text `fontSize.base`/18 `fontWeight.normal`, `role.text.primary`; icon 18 x 18, `role.text.secondary`; placeholder `role.text.disabled` |
| light (same: light-hover, light-focus-visible) | size 920 x `size.control.2xl`; padding 0 `spacing.2_5`; border 1px solid `role.border.strong`; radius `radius.full`; background `role.bg.raised`; text `fontSize.base`/18 `fontWeight.normal`, `role.text.primary`; icon 18 x 18, `role.text.secondary`; placeholder `role.text.disabled` |

#### Tab (Plugins / Skills)

<a id="plugins-tab"></a>`plugins-tab`, on plugins-dark.

<img src="components/crops/plugins-tab-default.png" alt="Tab (Plugins / Skills), default" height="36"> <img src="components/crops/plugins-tab-hover.png" alt="Tab (Plugins / Skills), hover" height="36"> <img src="components/crops/plugins-tab-focus-visible.png" alt="Tab (Plugins / Skills), focus-visible" height="36"> <img src="components/crops/plugins-tab-light.png" alt="Tab (Plugins / Skills), light" height="36"> <img src="components/crops/plugins-tab-light-hover.png" alt="Tab (Plugins / Skills), light-hover" height="36"> <img src="components/crops/plugins-tab-selected.png" alt="Tab (Plugins / Skills), selected" height="36"> <img src="components/crops/plugins-tab-light-focus-visible.png" alt="Tab (Plugins / Skills), light-focus-visible" height="36"> <img src="components/crops/plugins-tab-light-selected.png" alt="Tab (Plugins / Skills), light-selected" height="36"> 

| State | Values |
|---|---|
| default | size 68.73 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.secondary` |
| hover | background `token.border-light`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| selected | size 82.39 x `size.control.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light | size 68.73 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.secondary` |
| light-hover | background rgba(0, 0, 0, 0.03); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| light-selected | size 82.39 x `size.control.lg`; background `variant.primary.soft.bg-hover`; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |

#### List row (plugin card)

<a id="plugin-row"></a>`plugin-row`, on plugins-dark. A bordered card with a link laid over the whole of it; hover fills the card, keyboard focus rings the link (see the next row).

<img src="components/crops/plugin-row-default.png" alt="List row (plugin card), default" height="65"> <img src="components/crops/plugin-row-hover.png" alt="List row (plugin card), hover" height="65"> <img src="components/crops/plugin-row-pressed.png" alt="List row (plugin card), pressed" height="65"> <img src="components/crops/plugin-row-light.png" alt="List row (plugin card), light" height="65"> <img src="components/crops/plugin-row-light-hover.png" alt="List row (plugin card), light-hover" height="65"> <img src="components/crops/plugin-row-light-pressed.png" alt="List row (plugin card), light-pressed" height="65"> 

| State | Values |
|---|---|
| default | size 448 x 64.75; padding `spacing.2`; radius `radius.2xl`; background transparent; text `typography.text-md` at `fontWeight.medium`, `role.text.primary`; icon 18 x 18, `role.text.disabled` |
| hover, pressed | background `bg.disabled` |
| light | size 448 x 64.75; padding `spacing.2`; radius `radius.2xl`; background transparent; text `typography.text-md` at `fontWeight.medium`, `role.text.primary`; icon 18 x 18, `role.text.disabled` |
| light-hover, light-pressed | background `bg.disabled` |

Child layers: span 36x36 background `role.bg.page` border 1px solid `role.border.default` radius 8px

#### List row link (plugin card, focus ring)

<a id="plugin-row-link"></a>`plugin-row-link`, on plugins-dark.

<img src="components/crops/plugin-row-link-focus-visible.png" alt="List row link (plugin card, focus ring), focus-visible" height="65"> <img src="components/crops/plugin-row-link-light-focus-visible.png" alt="List row link (plugin card, focus ring), light-focus-visible" height="65"> 

| State | Values |
|---|---|
| focus-visible | size 448 x 64.75; radius `radius.2xl`; background transparent; focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |
| light-focus-visible | size 448 x 64.75; radius `radius.2xl`; background transparent; focus ring `size.focusRing.width` box-shadow ring (inset) in `role.border.focus` |

### Settings

The settings page (a full page since the redesign, not a dialog): a left nav, then panes of 60 to 64 tall rows with switches, select buttons, outline buttons and danger buttons.

#### Settings nav item

<a id="settings-nav-item"></a>`settings-nav-item`, on settings-dark-appearance.

<img src="components/crops/settings-nav-item-default.png" alt="Settings nav item, default" height="35"> <img src="components/crops/settings-nav-item-hover.png" alt="Settings nav item, hover" height="35"> <img src="components/crops/settings-nav-item-focus-visible.png" alt="Settings nav item, focus-visible" height="35"> <img src="components/crops/settings-nav-item-pressed.png" alt="Settings nav item, pressed" height="35"> <img src="components/crops/settings-nav-item-light.png" alt="Settings nav item, light" height="35"> <img src="components/crops/settings-nav-item-light-hover.png" alt="Settings nav item, light-hover" height="35"> <img src="components/crops/settings-nav-item-selected.png" alt="Settings nav item, selected" height="35"> <img src="components/crops/settings-nav-item-light-focus-visible.png" alt="Settings nav item, light-focus-visible" height="35"> <img src="components/crops/settings-nav-item-light-pressed.png" alt="Settings nav item, light-pressed" height="35"> <img src="components/crops/settings-nav-item-light-selected.png" alt="Settings nav item, light-selected" height="35"> 

| State | Values |
|---|---|
| default | size 328 x 35; padding `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | outline 2px solid `role.border.focus`, offset -2px |
| pressed, selected | background `variant.primary.soft.bg-hover` |
| light | size 328 x 35; padding `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | outline 2px solid `role.border.focus`, offset -2px |
| light-pressed, light-selected | background `variant.primary.soft.bg-hover` |

#### Settings row

<a id="settings-row"></a>`settings-row`, on settings-dark-data-controls.

<img src="components/crops/settings-row-default.png" alt="Settings row, default" height="60"> <img src="components/crops/settings-row-light.png" alt="Settings row, light" height="60"> 

| State | Values |
|---|---|
| default | size 766 x 60; padding `spacing.3` `spacing.4`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |
| light | size 766 x 60; padding `spacing.3` `spacing.4`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |

Child layers: div 734pxx1px background `token.border`; button 92.5x36 background `bg.disabled` border 1px solid transparent radius 9999px

#### Switch (on)

<a id="switch-on"></a>`switch-on`, on settings-dark-data-controls.

<img src="components/crops/switch-on-default.png" alt="Switch (on), default" height="24"> <img src="components/crops/switch-on-hover.png" alt="Switch (on), hover" height="24"> <img src="components/crops/switch-on-focus-visible.png" alt="Switch (on), focus-visible" height="24"> <img src="components/crops/switch-on-pressed.png" alt="Switch (on), pressed" height="24"> <img src="components/crops/switch-on-light.png" alt="Switch (on), light" height="24"> <img src="components/crops/switch-on-light-hover.png" alt="Switch (on), light-hover" height="24"> <img src="components/crops/switch-on-light-focus-visible.png" alt="Switch (on), light-focus-visible" height="24"> <img src="components/crops/switch-on-light-pressed.png" alt="Switch (on), light-pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 32 x `size.control.4xs`; background transparent; text `typography.text-sm`, `role.text.primary` |
| focus-visible | radius `radius.full`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light (same: light-hover, light-pressed) | size 32 x `size.control.4xs`; background transparent; text `typography.text-sm`, `role.text.primary` |
| light-focus-visible | radius `radius.full`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |

Child layers: span 32x20 background `variant.primary.soft.ring` radius 9999px; span 16x16 background `variant.danger.solid.text` border 1px solid `variant.danger.solid.text` radius 9999px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 1px 2px -1px

#### Switch (off)

<a id="switch-off"></a>`switch-off`, on settings-dark-data-controls.

<img src="components/crops/switch-off-default.png" alt="Switch (off), default" height="24"> <img src="components/crops/switch-off-hover.png" alt="Switch (off), hover" height="24"> <img src="components/crops/switch-off-focus-visible.png" alt="Switch (off), focus-visible" height="24"> <img src="components/crops/switch-off-pressed.png" alt="Switch (off), pressed" height="24"> <img src="components/crops/switch-off-light.png" alt="Switch (off), light" height="24"> <img src="components/crops/switch-off-light-hover.png" alt="Switch (off), light-hover" height="24"> <img src="components/crops/switch-off-light-focus-visible.png" alt="Switch (off), light-focus-visible" height="24"> <img src="components/crops/switch-off-light-pressed.png" alt="Switch (off), light-pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 32 x `size.control.4xs`; background transparent; text `typography.text-sm`, `role.text.primary` |
| focus-visible | radius `radius.full`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light (same: light-hover, light-pressed) | size 32 x `size.control.4xs`; background transparent; text `typography.text-sm`, `role.text.primary` |
| light-focus-visible | radius `radius.full`; focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |

Child layers: span 32x20 background `bg.segmented-selected` radius 9999px; span 16x16 background `variant.danger.solid.text` border 1px solid `variant.danger.solid.text` radius 9999px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 1px 2px -1px

#### Outline button (Archive all)

<a id="button-outline"></a>`button-outline`, on settings-dark-data-controls.

<img src="components/crops/button-outline-default.png" alt="Outline button (Archive all), default" height="36"> <img src="components/crops/button-outline-hover.png" alt="Outline button (Archive all), hover" height="36"> <img src="components/crops/button-outline-focus-visible.png" alt="Outline button (Archive all), focus-visible" height="36"> <img src="components/crops/button-outline-pressed.png" alt="Outline button (Archive all), pressed" height="36"> <img src="components/crops/button-outline-light.png" alt="Outline button (Archive all), light" height="36"> <img src="components/crops/button-outline-light-hover.png" alt="Outline button (Archive all), light-hover" height="36"> <img src="components/crops/button-outline-light-focus-visible.png" alt="Outline button (Archive all), light-focus-visible" height="36"> <img src="components/crops/button-outline-light-pressed.png" alt="Outline button (Archive all), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 92.5 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.full`; background `bg.disabled`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary` |
| hover | background `bg.segmented-selected` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `bg.segmented-selected` |
| light | size 92.5 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.full`; background `bg.disabled`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary` |
| light-hover | background `bg.segmented-selected` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `bg.segmented-selected` |

#### Danger outline button (Delete all)

<a id="button-danger-outline"></a>`button-danger-outline`, on settings-dark-data-controls.

<img src="components/crops/button-danger-outline-default.png" alt="Danger outline button (Delete all), default" height="36"> <img src="components/crops/button-danger-outline-hover.png" alt="Danger outline button (Delete all), hover" height="36"> <img src="components/crops/button-danger-outline-focus-visible.png" alt="Danger outline button (Delete all), focus-visible" height="36"> <img src="components/crops/button-danger-outline-pressed.png" alt="Danger outline button (Delete all), pressed" height="36"> <img src="components/crops/button-danger-outline-light.png" alt="Danger outline button (Delete all), light" height="36"> <img src="components/crops/button-danger-outline-light-hover.png" alt="Danger outline button (Delete all), light-hover" height="36"> <img src="components/crops/button-danger-outline-light-focus-visible.png" alt="Danger outline button (Delete all), light-focus-visible" height="36"> <img src="components/crops/button-danger-outline-light-pressed.png" alt="Danger outline button (Delete all), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 85.94 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.full`; background `component.button-danger.bg`; text `fontSize.sm`/18 `fontWeight.normal`, `text.danger` |
| hover | background `component.button-danger.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `component.button-danger.bg-hover` |
| light | size 85.94 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.full`; background `component.button-danger.bg`; text `fontSize.sm`/18 `fontWeight.normal`, `text.danger` |
| light-hover | background `component.button-danger.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `component.button-danger.bg-hover` |

#### Button (disabled, Restore defaults)

<a id="button-disabled"></a>`button-disabled`, on settings-dark-keyboard.

<img src="components/crops/button-disabled-default.png" alt="Button (disabled, Restore defaults), default" height="36"> <img src="components/crops/button-disabled-hover.png" alt="Button (disabled, Restore defaults), hover" height="36"> <img src="components/crops/button-disabled-light.png" alt="Button (disabled, Restore defaults), light" height="36"> <img src="components/crops/button-disabled-light-hover.png" alt="Button (disabled, Restore defaults), light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 142.05 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid `role.border.default`; radius `radius.full`; background `variant.primary.solid.bg`; text `typography.text-sm` at `fontWeight.medium`, `role.text.inverse`; opacity 0.4 |
| light (same: light-hover) | size 142.05 x `size.control.lg`; padding 0 `spacing.4`; border 1px solid `role.border.default`; radius `radius.full`; background `variant.primary.solid.bg`; text `typography.text-sm` at `fontWeight.medium`, `role.text.inverse`; opacity 0.4 |

#### Switch (keyboard shortcut on)

<a id="keyboard-switch"></a>`keyboard-switch`, on settings-dark-keyboard.

<img src="components/crops/keyboard-switch-default.png" alt="Switch (keyboard shortcut on), default" height="24"> <img src="components/crops/keyboard-switch-light.png" alt="Switch (keyboard shortcut on), light" height="24"> 

| State | Values |
|---|---|
| default | size 32 x `size.control.4xs`; background transparent |
| light | size 32 x `size.control.4xs`; background transparent |

Child layers: span 32x20 background `variant.primary.soft.ring` radius 9999px; span 16x16 background `variant.danger.solid.text` border 1px solid `variant.danger.solid.text` radius 9999px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 1px 2px -1px

#### Select (notification channel)

<a id="select"></a>`select`, on settings-dark-notifications-menu.

<img src="components/crops/select-default.png" alt="Select (notification channel), default" height="36"> <img src="components/crops/select-hover.png" alt="Select (notification channel), hover" height="36"> <img src="components/crops/select-focus-visible.png" alt="Select (notification channel), focus-visible" height="36"> <img src="components/crops/select-pressed.png" alt="Select (notification channel), pressed" height="36"> <img src="components/crops/select-light.png" alt="Select (notification channel), light" height="36"> <img src="components/crops/select-light-hover.png" alt="Select (notification channel), light-hover" height="36"> <img src="components/crops/select-open.png" alt="Select (notification channel), open" height="36"> <img src="components/crops/select-light-focus-visible.png" alt="Select (notification channel), light-focus-visible" height="36"> <img src="components/crops/select-light-open.png" alt="Select (notification channel), light-open" height="36"> <img src="components/crops/select-light-pressed.png" alt="Select (notification channel), light-pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 78.03 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid `role.border.default`; radius `radius.full`; background `surface.elevated-secondary`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 16 x 16, `role.text.disabled` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| open | background `variant.primary.soft.bg-hover` |
| light (same: light-hover, light-pressed) | size 78.03 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid `role.border.default`; radius `radius.full`; background `bg.user-message-compact`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary`; icon 16 x 16, `role.text.disabled` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-open | background `variant.primary.soft.bg-hover` |

#### Select (code theme)

<a id="code-theme-select"></a>`code-theme-select`, on settings-dark-appearance.

<img src="components/crops/code-theme-select-default.png" alt="Select (code theme), default" height="36"> <img src="components/crops/code-theme-select-hover.png" alt="Select (code theme), hover" height="36"> <img src="components/crops/code-theme-select-focus-visible.png" alt="Select (code theme), focus-visible" height="36"> <img src="components/crops/code-theme-select-pressed.png" alt="Select (code theme), pressed" height="36"> <img src="components/crops/code-theme-select-light.png" alt="Select (code theme), light" height="36"> <img src="components/crops/code-theme-select-light-hover.png" alt="Select (code theme), light-hover" height="36"> <img src="components/crops/code-theme-select-light-focus-visible.png" alt="Select (code theme), light-focus-visible" height="36"> <img src="components/crops/code-theme-select-light-pressed.png" alt="Select (code theme), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 176 x `size.control.lg`; padding 0 `spacing.3` 0 7px; border 1px solid `role.border.default`; radius `radius.full`; background `role.bg.page`; text `fontSize.xs`/12 `fontWeight.semibold`, `variant.info.solid.bg`; icon 16 x 16, `role.text.disabled` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 176 x `size.control.lg`; padding 0 `spacing.3` 0 7px; border 1px solid `role.border.default`; radius `radius.full`; background `role.bg.page`; text `fontSize.xs`/12 `fontWeight.semibold`, `text.tip`; icon 16 x 16, `role.text.disabled` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

#### Text field (colour hex)

<a id="color-field"></a>`color-field`, on settings-dark-appearance.

<img src="components/crops/color-field-default.png" alt="Text field (colour hex), default" height="24"> <img src="components/crops/color-field-hover.png" alt="Text field (colour hex), hover" height="24"> <img src="components/crops/color-field-focus-visible.png" alt="Text field (colour hex), focus-visible" height="24"> <img src="components/crops/color-field-light.png" alt="Text field (colour hex), light" height="24"> <img src="components/crops/color-field-light-hover.png" alt="Text field (colour hex), light-hover" height="24"> <img src="components/crops/color-field-light-focus-visible.png" alt="Text field (colour hex), light-focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 56 x `size.icon.sm`; background transparent; text `fontSize.xs`/16 `fontWeight.normal`, `role.text.primary`; placeholder `role.text.primary` |
| light (same: light-hover, light-focus-visible) | size 56 x `size.icon.sm`; background transparent; text `fontSize.xs`/16 `fontWeight.normal`, `role.text.primary`; placeholder `role.text.primary` |

#### Text field (Search archived chats)

<a id="archived-search"></a>`archived-search`, on settings-dark-archived.

<img src="components/crops/archived-search-default.png" alt="Text field (Search archived chats), default" height="44"> <img src="components/crops/archived-search-hover.png" alt="Text field (Search archived chats), hover" height="44"> <img src="components/crops/archived-search-focus-visible.png" alt="Text field (Search archived chats), focus-visible" height="44"> <img src="components/crops/archived-search-light.png" alt="Text field (Search archived chats), light" height="44"> <img src="components/crops/archived-search-light-hover.png" alt="Text field (Search archived chats), light-hover" height="44"> <img src="components/crops/archived-search-light-focus-visible.png" alt="Text field (Search archived chats), light-focus-visible" height="44"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 432 x `size.control.2xl`; padding 0 `spacing.2_5`; border 1px solid `role.border.strong`; radius `radius.full`; background `role.bg.raised`; text `fontSize.base`/18 `fontWeight.normal`, `role.text.primary`; icon 18 x 18, `role.text.secondary`; placeholder `role.text.disabled` |
| light (same: light-hover, light-focus-visible) | size 432 x `size.control.2xl`; padding 0 `spacing.2_5`; border 1px solid `role.border.strong`; radius `radius.full`; background `role.bg.raised`; text `fontSize.base`/18 `fontWeight.normal`, `role.text.primary`; icon 18 x 18, `role.text.secondary`; placeholder `role.text.disabled` |

#### List row (archived chat)

<a id="archived-row"></a>`archived-row`, on settings-dark-archived.

<img src="components/crops/archived-row-default.png" alt="List row (archived chat), default" height="62"> <img src="components/crops/archived-row-hover.png" alt="List row (archived chat), hover" height="62"> <img src="components/crops/archived-row-light.png" alt="List row (archived chat), light" height="62"> <img src="components/crops/archived-row-light-hover.png" alt="List row (archived chat), light-hover" height="62"> 

| State | Values |
|---|---|
| default (same: hover) | size 766 x 62; padding `spacing.3` `spacing.4`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.link`; icon 18 x 18, `role.text.primary` |
| light (same: light-hover) | size 766 x 62; padding `spacing.3` `spacing.4`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.link`; icon 18 x 18, `role.text.primary` |

Child layers: div 734pxx1px background `token.border`; button 90.8x36 background `bg.disabled` border 1px solid transparent radius 9999px; button 67.8x36 background `component.button-danger.bg` border 1px solid transparent radius 9999px

#### Link (archived chat title)

<a id="archived-link"></a>`archived-link`, on settings-dark-archived.

<img src="components/crops/archived-link-default.png" alt="Link (archived chat title), default" height="24"> <img src="components/crops/archived-link-hover.png" alt="Link (archived chat title), hover" height="24"> <img src="components/crops/archived-link-focus-visible.png" alt="Link (archived chat title), focus-visible" height="24"> <img src="components/crops/archived-link-pressed.png" alt="Link (archived chat title), pressed" height="24"> <img src="components/crops/archived-link-light.png" alt="Link (archived chat title), light" height="24"> <img src="components/crops/archived-link-light-hover.png" alt="Link (archived chat title), light-hover" height="24"> <img src="components/crops/archived-link-light-focus-visible.png" alt="Link (archived chat title), light-focus-visible" height="24"> <img src="components/crops/archived-link-light-pressed.png" alt="Link (archived chat title), light-pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 90.61 x `size.control.4xs`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.link` |
| focus-visible | outline 1px auto #99c8ff, offset 1px |
| light (same: light-hover, light-pressed) | size 90.61 x `size.control.4xs`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.link` |
| light-focus-visible | outline 1px auto #005fcc, offset 1px |

#### Outline button (Unarchive)

<a id="unarchive-button"></a>`unarchive-button`, on settings-dark-archived.

<img src="components/crops/unarchive-button-default.png" alt="Outline button (Unarchive), default" height="36"> <img src="components/crops/unarchive-button-hover.png" alt="Outline button (Unarchive), hover" height="36"> <img src="components/crops/unarchive-button-focus-visible.png" alt="Outline button (Unarchive), focus-visible" height="36"> <img src="components/crops/unarchive-button-pressed.png" alt="Outline button (Unarchive), pressed" height="36"> <img src="components/crops/unarchive-button-light.png" alt="Outline button (Unarchive), light" height="36"> <img src="components/crops/unarchive-button-light-hover.png" alt="Outline button (Unarchive), light-hover" height="36"> <img src="components/crops/unarchive-button-light-focus-visible.png" alt="Outline button (Unarchive), light-focus-visible" height="36"> <img src="components/crops/unarchive-button-light-pressed.png" alt="Outline button (Unarchive), light-pressed" height="36"> 

| State | Values |
|---|---|
| default | size 90.84 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.full`; background `bg.disabled`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary` |
| hover | background `bg.segmented-selected` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `bg.segmented-selected` |
| light | size 90.84 x `size.control.lg`; padding 0 `spacing.3`; border 1px solid transparent; radius `radius.full`; background `bg.disabled`; text `fontSize.sm`/18 `fontWeight.normal`, `role.text.primary` |
| light-hover | background `bg.segmented-selected` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `bg.segmented-selected` |

#### Link (Manage tasks)

<a id="text-link"></a>`text-link`, on settings-dark-notifications-menu.

<img src="components/crops/text-link-default.png" alt="Link (Manage tasks), default" height="24"> <img src="components/crops/text-link-hover.png" alt="Link (Manage tasks), hover" height="24"> <img src="components/crops/text-link-focus-visible.png" alt="Link (Manage tasks), focus-visible" height="24"> <img src="components/crops/text-link-pressed.png" alt="Link (Manage tasks), pressed" height="24"> <img src="components/crops/text-link-light.png" alt="Link (Manage tasks), light" height="24"> <img src="components/crops/text-link-light-hover.png" alt="Link (Manage tasks), light-hover" height="24"> <img src="components/crops/text-link-light-focus-visible.png" alt="Link (Manage tasks), light-focus-visible" height="24"> <img src="components/crops/text-link-light-pressed.png" alt="Link (Manage tasks), light-pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 78.11 x 15; background transparent; text `fontSize.xs`/16 `fontWeight.normal`, `role.text.secondary` |
| focus-visible | outline 1px auto #99c8ff, offset 1px |
| light (same: light-hover, light-pressed) | size 78.11 x 15; background transparent; text `fontSize.xs`/16 `fontWeight.normal`, `role.text.secondary` |
| light-focus-visible | outline 1px auto #005fcc, offset 1px |

### Pricing

The Upgrade dialog: a full-screen sheet with a Personal / Business radio segment and plan cards.

#### Full-screen dialog (pricing)

<a id="pricing-dialog"></a>`pricing-dialog`, on pricing-dark.

| State | Values |
|---|---|
| default | size 1440 x 900; background transparent; text `fontSize.4xl`/40 `fontWeight.semibold`, `role.text.on-accent`; icon 20 x 20, `role.text.secondary` |
| light | size 1440 x 900; background transparent; text `fontSize.4xl`/40 `fontWeight.semibold`, `role.text.primary`; icon 20 x 20, `role.text.secondary` |

Child layers: main 1440x900 background `role.bg.surface`; button 32x32 border 1px solid transparent radius 9999px; div 352x44 background #424242 radius 20px

#### Radio segment (Business, not checked)

<a id="segmented-radio"></a>`segmented-radio`, on pricing-dark.

<img src="components/crops/segmented-radio-default.png" alt="Radio segment (Business, not checked), default" height="36"> <img src="components/crops/segmented-radio-hover.png" alt="Radio segment (Business, not checked), hover" height="36"> <img src="components/crops/segmented-radio-focus-visible.png" alt="Radio segment (Business, not checked), focus-visible" height="36"> <img src="components/crops/segmented-radio-pressed.png" alt="Radio segment (Business, not checked), pressed" height="36"> <img src="components/crops/segmented-radio-light.png" alt="Radio segment (Business, not checked), light" height="36"> <img src="components/crops/segmented-radio-light-hover.png" alt="Radio segment (Business, not checked), light-hover" height="36"> <img src="components/crops/segmented-radio-checked.png" alt="Radio segment (Business, not checked), checked" height="36"> <img src="components/crops/segmented-radio-light-checked.png" alt="Radio segment (Business, not checked), light-checked" height="36"> <img src="components/crops/segmented-radio-light-focus-visible.png" alt="Radio segment (Business, not checked), light-focus-visible" height="36"> <img src="components/crops/segmented-radio-light-pressed.png" alt="Radio segment (Business, not checked), light-pressed" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 170 x `size.control.lg`; padding `spacing.2` `spacing.5`; radius `radius.2xl`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.disabled` |
| focus-visible | outline 1px auto #99c8ff, offset 0px |
| checked | text `typography.text-sm` at `fontWeight.medium`, `role.text.on-accent` |
| light (same: light-hover, light-pressed) | size 170 x `size.control.lg`; padding `spacing.2` `spacing.5`; radius `radius.2xl`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.disabled` |
| light-focus-visible | outline 1px auto #005fcc, offset 0px |
| light-checked | text `typography.text-sm` at `fontWeight.medium`, `role.text.primary` |

#### Card (Free plan)

<a id="pricing-card"></a>`pricing-card`, on pricing-dark.

<img src="components/crops/pricing-card-default.png" alt="Card (Free plan), default" height="120"> <img src="components/crops/pricing-card-light.png" alt="Card (Free plan), light" height="120"> 

| State | Values |
|---|---|
| default | size 384 x 736; padding 23px 23px 25px 23px; border 1px solid `role.border.default`; radius `radius.3xl`; background `role.bg.surface`; shadow rgba(0, 0, 0, 0.05) 0px 4px 8px 0px; text `fontSize.lg`/32 `fontWeight.semibold`, `role.text.on-accent`; transition color and 9 more 0.2s cubic-bezier(0, 0, 0.2, 1); icon 20 x 20, `role.text.on-accent` |
| light | size 336 x 294; background `role.bg.page`; text `fontSize.lg`/32 `fontWeight.semibold`, `role.text.primary` |

#### Card (Plus plan, recommended)

<a id="pricing-card-plus"></a>`pricing-card-plus`, on pricing-dark.

<img src="components/crops/pricing-card-plus-default.png" alt="Card (Plus plan, recommended), default" height="120"> <img src="components/crops/pricing-card-plus-light.png" alt="Card (Plus plan, recommended), light" height="120"> 

| State | Values |
|---|---|
| default | size 384 x 736; padding 23px 23px 25px 23px; border 1px solid rgba(58, 131, 247, 0.5); radius `radius.3xl`; background transparent; image linear-gradient(`role.bg.surface` 0%, #274b72 100%); shadow rgba(0, 0, 0, 0.05) 0px 4px 8px 0px; text `fontSize.lg`/32 `fontWeight.semibold`, `role.text.on-accent`; transition color and 9 more 0.2s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, `role.text.on-accent` |
| light | size 384 x 736; padding 23px 23px 25px 23px; border 1px solid rgba(58, 131, 247, 0.5); radius `radius.3xl`; background transparent; image linear-gradient(`role.bg.raised` 0%, #eef6ff 100%); shadow rgba(0, 0, 0, 0.05) 0px 4px 8px 0px; text `fontSize.lg`/32 `fontWeight.semibold`, `role.text.primary`; transition color and 9 more 0.2s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, `role.text.inverse` |

#### Badge (RECOMMENDED)

<a id="badge"></a>`badge`, on pricing-dark.

<img src="components/crops/badge-default.png" alt="Badge (RECOMMENDED), default" height="27"> <img src="components/crops/badge-light.png" alt="Badge (RECOMMENDED), light" height="27"> 

| State | Values |
|---|---|
| default | size 103.45 x 27; padding `spacing.1_5` `spacing.2` 5px `spacing.2`; radius `radius.4xl`; background `component.badge.bg`; text System 11/16 600, `component.badge.text` |
| light | size 103.45 x 27; padding `spacing.1_5` `spacing.2` 5px `spacing.2`; radius `radius.4xl`; background `component.badge.bg`; text System 11/16 600, `role.text.link` |

#### Button (disabled, Your current plan)

<a id="button-disabled-plan"></a>`button-disabled-plan`, on pricing-dark.

<img src="components/crops/button-disabled-plan-default.png" alt="Button (disabled, Your current plan), default" height="44"> <img src="components/crops/button-disabled-plan-light.png" alt="Button (disabled, Your current plan), light" height="44"> 

| State | Values |
|---|---|
| default | size 336 x `size.control.2xl`; padding 0 `spacing.4`; border 1px solid `role.border.default`; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.on-accent`; opacity 0.4 |
| light | size 336 x `size.control.2xl`; padding 0 `spacing.4`; border 1px solid `role.border.default`; radius `radius.full`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; opacity 0.4 |

#### Accent button (Rejoin Plus)

<a id="pricing-primary"></a>`pricing-primary`, on pricing-dark.

<img src="components/crops/pricing-primary-default.png" alt="Accent button (Rejoin Plus), default" height="44"> <img src="components/crops/pricing-primary-hover.png" alt="Accent button (Rejoin Plus), hover" height="44"> <img src="components/crops/pricing-primary-focus-visible.png" alt="Accent button (Rejoin Plus), focus-visible" height="44"> <img src="components/crops/pricing-primary-pressed.png" alt="Accent button (Rejoin Plus), pressed" height="44"> <img src="components/crops/pricing-primary-light.png" alt="Accent button (Rejoin Plus), light" height="44"> <img src="components/crops/pricing-primary-light-hover.png" alt="Accent button (Rejoin Plus), light-hover" height="44"> <img src="components/crops/pricing-primary-light-focus-visible.png" alt="Accent button (Rejoin Plus), light-focus-visible" height="44"> <img src="components/crops/pricing-primary-light-pressed.png" alt="Accent button (Rejoin Plus), light-pressed" height="44"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 336 x `size.control.2xl`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background `variant.primary.soft.ring`; text `typography.text-sm` at `fontWeight.medium`, `role.text.on-accent`; icon 16 x 16, `role.text.on-accent` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light (same: light-hover, light-pressed) | size 336 x `size.control.2xl`; padding 0 `spacing.4`; border 1px solid transparent; radius `radius.full`; background `bg.accent-action`; text `typography.text-sm` at `fontWeight.medium`, `role.text.inverse`; icon 16 x 16, `role.text.inverse` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |

#### Icon button (Close pricing)

<a id="pricing-close"></a>`pricing-close`, on pricing-dark.

<img src="components/crops/pricing-close-default.png" alt="Icon button (Close pricing), default" height="32"> <img src="components/crops/pricing-close-hover.png" alt="Icon button (Close pricing), hover" height="32"> <img src="components/crops/pricing-close-focus-visible.png" alt="Icon button (Close pricing), focus-visible" height="32"> <img src="components/crops/pricing-close-pressed.png" alt="Icon button (Close pricing), pressed" height="32"> <img src="components/crops/pricing-close-light.png" alt="Icon button (Close pricing), light" height="32"> <img src="components/crops/pricing-close-light-hover.png" alt="Icon button (Close pricing), light-hover" height="32"> <img src="components/crops/pricing-close-light-focus-visible.png" alt="Icon button (Close pricing), light-focus-visible" height="32"> <img src="components/crops/pricing-close-light-pressed.png" alt="Icon button (Close pricing), light-pressed" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.control.md`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-md`, `role.text.secondary`; icon 20 x 20, `role.text.secondary` |
| hover | background `variant.primary.soft.bg-hover` |
| focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| pressed | background `variant.primary.soft.bg-hover` |
| light | size 32 x `size.control.md`; border 1px solid transparent; radius `radius.full`; background transparent; text `typography.text-md`, `role.text.secondary`; icon 20 x 20, `role.text.secondary` |
| light-hover | background `variant.primary.soft.bg-hover` |
| light-focus-visible | focus ring `size.focusRing.width` box-shadow ring in `role.border.focus` |
| light-pressed | background `variant.primary.soft.bg-hover` |

### Phone

The same app at 390 wide: the header, the two-row composer, the drawer, the user bubble and a code block.

#### Phone header

<a id="m-header"></a>`m-header`, on mobile-home-dark.

<img src="components/crops/m-header-default.png" alt="Phone header, default" height="52"> <img src="components/crops/m-header-light.png" alt="Phone header, light" height="52"> 

| State | Values |
|---|---|
| default | size 390 x `size.height.height-toolbar`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.on-accent`; icon 20 x 20, `role.text.disabled` |
| light | size 390 x `size.height.height-toolbar`; background transparent; text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.disabled` |

Child layers: div 36x36 background `role.bg.page` radius 8px; button 36pxx36px background `variant.primary.soft.bg-hover` radius 8px; button 36x36 border 1px solid transparent radius 8px

#### Phone composer

<a id="m-composer"></a>`m-composer`, on mobile-home-dark.

<img src="components/crops/m-composer-default.png" alt="Phone composer, default" height="87"> <img src="components/crops/m-composer-light.png" alt="Phone composer, light" height="87"> 

| State | Values |
|---|---|
| default | size 358 x 87; radius 28px; background `role.bg.raised`; shadow rgba(255, 255, 255, 0.2) 0px 0px 1px 0px inset; icon 20 x 20, `role.text.primary`; placeholder `role.text.disabled` |
| light | size 358 x 87; radius 28px; background `role.bg.raised`; shadow rgba(255, 255, 255, 0.2) 0px 0px 1px 0px inset; icon 20 x 20, `role.text.primary`; placeholder `role.text.disabled` |

#### Phone drawer

<a id="m-drawer"></a>`m-drawer`, on mobile-home-dark-drawer.

<img src="components/crops/m-drawer-default.png" alt="Phone drawer, default" height="120"> <img src="components/crops/m-drawer-light.png" alt="Phone drawer, light" height="120"> 

| State | Values |
|---|---|
| default | size 260 x 844; border R: 1px solid `role.border.default`; background `role.bg.page`; shadow rgba(0, 0, 0, 0.1) 0px 4px 8px -2px; text `typography.text-sm`, `role.text.primary`; transition transform and 3 more 0.2s cubic-bezier(0, 0, 0.2, 1); icon 77.13 x 18, `role.text.primary` |
| light | size 260 x 844; border R: 1px solid `role.border.default`; background `role.bg.page`; shadow rgba(0, 0, 0, 0.1) 0px 4px 8px -2px; text `typography.text-sm`, `role.text.primary`; transition transform and 3 more 0.2s cubic-bezier(0, 0, 0.2, 1); icon 77.13 x 18, `role.text.primary` |

#### Phone drawer row

<a id="m-drawer-row"></a>`m-drawer-row`, on mobile-home-dark-drawer.

<img src="components/crops/m-drawer-row-default.png" alt="Phone drawer row, default" height="35"> <img src="components/crops/m-drawer-row-light.png" alt="Phone drawer row, light" height="35"> 

| State | Values |
|---|---|
| default | size 247 x 35; padding `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(237, 237, 237, 0.85); icon 20 x 20, rgba(237, 237, 237, 0.85) |
| light | size 247 x 35; padding `spacing.1_5` `spacing.2_5`; radius `radius.lg`; background transparent; text `typography.text-sm`, rgba(13, 13, 13, 0.85); icon 20 x 20, rgba(13, 13, 13, 0.85) |

#### Phone user bubble

<a id="m-user-bubble"></a>`m-user-bubble`, on mobile-thread-dark.

<img src="components/crops/m-user-bubble-default.png" alt="Phone user bubble, default" height="120"> <img src="components/crops/m-user-bubble-light.png" alt="Phone user bubble, light" height="120"> 

| State | Values |
|---|---|
| default | size 250.59 x 574; padding `spacing.2_5` `spacing.4`; radius `radius.token-composer-single-line`; background `bg.user-message`; text `fontSize.base`/26 `fontWeight.normal`, `text.user-message`; icon 16 x 16, `text.user-message` |
| light | size 250.59 x 574; padding `spacing.2_5` `spacing.4`; radius `radius.token-composer-single-line`; background `bg.user-message`; text `fontSize.base`/26 `fontWeight.normal`, `text.user-message`; icon 16 x 16, `text.user-message` |

#### Phone code block

<a id="m-code-block"></a>`m-code-block`, on mobile-thread-dark-bottom.

<img src="components/crops/m-code-block-default.png" alt="Phone code block, default" height="120"> <img src="components/crops/m-code-block-light.png" alt="Phone code block, light" height="120"> 

| State | Values |
|---|---|
| default | size 358 x 250.25; border 1px solid `role.border.subtle`; radius `radius.3xl`; background `surface.elevated-secondary`; image linear-gradient(`variant.primary.soft.bg-hover`, `variant.primary.soft.bg-hover`); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.primary` |
| light | size 358 x 250.25; border 1px solid `role.border.subtle`; radius `radius.3xl`; background `bg.user-message-compact`; image linear-gradient(`variant.primary.soft.bg-hover`, `variant.primary.soft.bg-hover`); text `typography.text-sm` at `fontWeight.medium`, `role.text.primary`; icon 20 x 20, `role.text.primary` |

## Icon index

66 icons were lifted from the sprite symbols inlined in the page copies into [icons/](icons), named by their sprite id. [icons/INDEX.tsv](icons/INDEX.tsv) indexes each by role, where it is drawn most (action 34, header action 11, message action 7, composer action 6, menu item 6, navigation 1, content 1), with every role it plays, its sprite id, viewBox, the sizes it was drawn at and the control it labels. ChatGPT draws them through `<use href="sprites-core-*.svg#name">` at 20px (`size.icon.lg`), 16px (`size.icon.sm`) or 12px, filled in currentColor, paired with 14px labels in rows and menus and alone (with an aria-label) in 36px icon buttons. A few glyphs are CSS masks or inline SVG and are not in the folder. The icons are OpenAI's property, kept for reference only.

| Icon | Role | Sizes | Where it was used |
|---|---|---|---|
| `books-light-20` | navigation | 20 | Library |
| `chat-bubble-dashed-light-20` | header action | 20 | Temporary chat |
| `chevron-down-md-light-20` | header action | 20 | Add |
| `drag-light-16` | header action |  | Dock Chat |
| `gear-light-16` | header action |  | Manage |
| `gear-light-20` | header action | 20 | Manage |
| `minus-sm-light-20` | header action |  | Minimize chat |
| `sidebar-hidden-light-16` | header action |  | Show sidebar |
| `sidebar-hidden-light-20` | header action | 20 | Show sidebar |
| `sparkle-fill-light-12` | header action | 12 | Work |
| `sparkle-fill-light-20` | header action | 20 | Upgrade |
| `xmark-md-light-16` | header action | 16 | Dismiss upgrade reminder |
| `brain-regular-20` | composer action | 20 | Think |
| `microphone-light-16` | composer action |  | Dictate |
| `microphone-light-20` | composer action | 20 | Dictate |
| `plus-lg-regular-16` | composer action |  | Add files and more |
| `plus-lg-regular-20` | composer action | 20 | Add files and more |
| `voice-regular-20` | composer action | 20 | Start Voice |
| `arrow-down-lg-light-20` | message action | 20 | Scroll to bottom |
| `arrow-up-right-arrow-down-left-md-light-16` | message action |  | - |
| `arrow-up-right-arrow-down-left-sm-light-20` | message action | 20 | - |
| `globe-light-12` | message action | 12 | - |
| `square-on-square-light-16` | message action |  | - |
| `square-on-square-light-20` | message action | 20 | Copy Dark theme |
| `text-overflow-light-20` | message action | 20 | - |
| `chat-bubble-light-20` | menu item | 20 | Sample title 11 |
| `help-light-20` | menu item | 20 | Help |
| `open-base-arrow-forward-light-16` | menu item |  | Log out |
| `open-base-arrow-forward-light-20` | menu item | 20 | Log out |
| `personalization-light-20` | menu item | 20 | Personalization |
| `sparkles-light-20` | menu item | 20 | Upgrade plan |
| `arrow-down-open-base-light-20` | action | 20 | Import Dark theme |
| `arrow-left-lg-light-16` | action |  | Back to app |
| `arrow-left-lg-light-20` | action | 20 | Back to app |
| `arrow-up-open-base-light-20` | action | 20 | Share |
| `arrows-clockwise-rotate-lg-light-16` | action | 16 | - |
| `brain-light-16` | action |  | Thinking |
| `brain-light-20` | action | 20 | Thinking |
| `chevron-down-md-light-16` | action | 16 | New |
| `chevron-right-md-light-16` | action | 16 | Advanced |
| `credit-card-light-20` | action | 20 | Billing |
| `ellipsis-horizontal-light-16` | action | 14 16 | Chat actions |
| `ellipsis-horizontal-light-20` | action | 20 | More |
| `filter-light-16` | action | 16 | Filter chats and work |
| `filter-light-20` | action | 20 | Open filters |
| `folder-light-16` | action | 16 | Filter archived chats by project |
| `folder-light-20` | action | 20 | Storage |
| `laptop-light-20` | action | 20 | - |
| `list-bullet-light-20` | action | 20 | List view |
| `magnifying-glass-lg-light-16` | action | 16 | Search |
| `magnifying-glass-lg-light-20` | action | 20 | Search |
| `person-circle-light-16` | action |  | Parental controls |
| `person-circle-light-20` | action | 20 | Parental controls |
| `pin-fill-light-16` | action | 14 | Unpin chat |
| `pin-light-16` | action | 14 | Pin chat |
| `plus-lg-light-20` | action | 20 | Install Health |
| `plus-md-light-16` | action | 16 | Add new project |
| `shield-light-16` | action |  | Data controls |
| `shield-light-20` | action | 20 | Data controls |
| `sidebar-light-16` | action |  | Hide sidebar |
| `sidebar-light-20` | action | 20 | Hide sidebar |
| `sliders-light-20` | action | 20 | Settings |
| `square-grid-2x2-light-20` | action | 20 | Grid view |
| `xmark-circle-fill-regular-16` | action | 16 | Clear search |
| `xmark-md-light-20` | action | 20 | Dismiss suggestion |
| `code-light-20` | content | 20 | - |

## Gaps

- Toast: ChatGPT shows one only after an action (copy, archive, share, delete), and the capture took none.
- Pressed: the product switches its pressed styles from script, so the pressed readings equal hover; the `-active` colours are in the tokens only.
- Loading: no skeleton or spinner was on screen in any copy; the streaming text speed (`duration.animation-duration-streaming-text`, 700 ms) is from the CSS only.
- Forms with a validation error: no form in reach validates without submitting it.
- Onboarding: the account is past its first run.
- Message text, chat, project and file titles, Library thumbnails and the installed plugins were replaced or blanked in the copies before they left the browser, so widths that depend on text are those of the filler.
- Hover and focus on the 390 wide copies were not measured (a phone has neither).
- The light theme was read by setting every `data-theme="dark"` to light in the copies, not by changing the account's appearance. Only the Blue accent was captured; switching it is an account setting.
- Not captured: a streaming answer, voice mode, Work mode, Codex, Scheduled, a project page, the share dialog, the Account, Billing and Personalization panes, since each either sends something, spends quota or shows account details.

