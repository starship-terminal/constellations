# Manus components

The discovery list of every page and state captured, then one entry per component with crops of the real product, the shared values, the icon index and the Gaps. Captured from manus.im/app on 2026-10-04 and refreshed on 2026-10-17, signed in, as static copies of each page state rendered in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the rendered copy in both themes. Nothing was sent or deleted in the account; the changes made were opening menus and dialogs, switching the Library's view options and switching them back, typing into the composer and into two dialog fields without submitting, and toggling the sidebar. On 2026-10-17 one click landed on a popover's "Continue in new task" by mistake and branched an existing task; the owner was told and the branch is theirs to remove.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (268 components, 1112 states). The page layouts are described in [raw/pages.md](raw/pages.md).

How to read an entry:

- Every value is written token first: `` `token` (value) ``. A plain token is exact: for a colour, the variable the component's own classes name for that property in that state (bg-[var(--x)], text-, border-); for a size, radius, padding, type style, duration, easing, shadow or opacity, the core token whose value it is. `` `≈ token` `` names a colour token only by its value in that theme, for colours no class on the element names (inherited text, browser defaults). A value with no token is written alone. Text is family size/line-height weight, for example `` `typography.sm` (System 14/20 400) ``, read from the first text node inside the component. Each component's class-named colour tokens are also in tokens.json under `component.<key>` in each theme.
- Dark states come first (every page was captured dark), then the same states read in light. Each theme's first row lists every value; later rows of that theme list only what changes. A state with the same values as its theme's first is named in that label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component from the rendered copy, in [components/crops/](components/crops) (896 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).
- Coverage: of 4378 values written in the entries below (colours, dimensions, heights, icon sizes, text styles, durations, easings, shadows and opacities; widths and zeros aside), 2958 (68%) name an exact token, 766 (17%) name a colour token by value (`≈`) and 654 (15%) are raw: text styles and heights off Manus's scales, hairline offsets and one-off shadows. A colour's exact token comes from the element's own class; a dimension's from the core tokens meant for that kind of value (radii from `core.radius`, heights from the control sizes in `core.size`, icons from `core.size.icon*`, paddings from `core.space`, borders from `core.borderWidth` and `core.focusRing`), generic before component-specific; text to `core.typography` and its roles; transitions to `core.duration` and `core.easing`; shadows to `elevation.*`; opacity to `core.opacity`.

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages at 2x, kept for the base pages only; mobile shots are `mobile-{page}-{theme}-{state}.png`, 390 x 844 at 2x. Every state exists in both themes.

| Surface | URL | Screenshots |
|---|---|---|
| Home. The logo and promo carousel, Build and Create, Start from a local file, the composer. Captured at rest, with the model menu, the + attach menu, a line typed in the composer, the sidebar collapsed, the search dialog and the notifications panel. | `/app` | [attach-menu (dark)](screenshots/home-dark-attach-menu.png), [composer-typed (dark)](screenshots/home-dark-composer-typed.png), [full (dark)](screenshots/home-dark-full.png), [model-menu (dark)](screenshots/home-dark-model-menu.png), [notifications (dark)](screenshots/home-dark-notifications.png), [search (dark)](screenshots/home-dark-search.png), [sidebar-collapsed (dark)](screenshots/home-dark-sidebar-collapsed.png), [default (dark)](screenshots/home-dark.png), [attach-menu (light)](screenshots/home-light-attach-menu.png), [composer-typed (light)](screenshots/home-light-composer-typed.png), [model-menu (light)](screenshots/home-light-model-menu.png), [notifications (light)](screenshots/home-light-notifications.png), [search (light)](screenshots/home-light-search.png), [sidebar-collapsed (light)](screenshots/home-light-sidebar-collapsed.png), [default (light)](screenshots/home-light.png) |
| Library. The title bar, the type tabs, groups by day. Captured on All, on Slides, on Images in grid view, with the view options open, grouped by task, with a row's menu open, with the document previewer open, and with the account menu open. | `/app/documents` | [full (dark)](screenshots/library-dark-full.png), [images-grid-by-task-full (dark)](screenshots/library-dark-images-grid-by-task-full.png), [images-grid-by-task (dark)](screenshots/library-dark-images-grid-by-task.png), [images-grid-view-options (dark)](screenshots/library-dark-images-grid-view-options.png), [images-grid (dark)](screenshots/library-dark-images-grid.png), [preview-doc-full (dark)](screenshots/library-dark-preview-doc-full.png), [preview-doc (dark)](screenshots/library-dark-preview-doc.png), [row-menu (dark)](screenshots/library-dark-row-menu.png), [slides (dark)](screenshots/library-dark-slides.png), [user-menu (dark)](screenshots/library-dark-user-menu.png), [default (dark)](screenshots/library-dark.png), [images-grid-by-task (light)](screenshots/library-light-images-grid-by-task.png), [images-grid-view-options (light)](screenshots/library-light-images-grid-view-options.png), [images-grid (light)](screenshots/library-light-images-grid.png), [preview-doc (light)](screenshots/library-light-preview-doc.png), [row-menu (light)](screenshots/library-light-row-menu.png), [slides (light)](screenshots/library-light-slides.png), [user-menu (light)](screenshots/library-light-user-menu.png), [default (light)](screenshots/library-light.png) |
| Settings dialog. General (language, theme cards, chat and communication toggles) and Keyboard shortcuts; on 2026-10-17 also Developers (the API key table, a row's menu, the delete confirmation, the Create API Key form empty, typed and with its select open), Personalization and Usage & Billing while its history loads. | `/app#settings` | [create-key-typed (dark)](screenshots/settings-dark-create-key-typed.png), [create-key (dark)](screenshots/settings-dark-create-key.png), [delete-confirm (dark)](screenshots/settings-dark-delete-confirm.png), [developers-table (dark)](screenshots/settings-dark-developers-table.png), [general-full (dark)](screenshots/settings-dark-general-full.png), [general (dark)](screenshots/settings-dark-general.png), [key-menu (dark)](screenshots/settings-dark-key-menu.png), [personalization (dark)](screenshots/settings-dark-personalization.png), [select-open (dark)](screenshots/settings-dark-select-open.png), [shortcuts (dark)](screenshots/settings-dark-shortcuts.png), [usage-loading (dark)](screenshots/settings-dark-usage-loading.png), [create-key-typed (light)](screenshots/settings-light-create-key-typed.png), [create-key (light)](screenshots/settings-light-create-key.png), [delete-confirm (light)](screenshots/settings-light-delete-confirm.png), [developers-table (light)](screenshots/settings-light-developers-table.png), [general (light)](screenshots/settings-light-general.png), [key-menu (light)](screenshots/settings-light-key-menu.png), [personalization (light)](screenshots/settings-light-personalization.png), [select-open (light)](screenshots/settings-light-select-open.png), [shortcuts (light)](screenshots/settings-light-shortcuts.png), [usage-loading (light)](screenshots/settings-light-usage-loading.png) |
| The invite dialog (2026-10-17): share tabs, Copy invitation link, the social row and the email field, empty and typed. | `/app#invitation` | [dialog (dark)](screenshots/invite-dark-dialog.png), [email-error (dark)](screenshots/invite-dark-email-error.png), [email-typed (dark)](screenshots/invite-dark-email-typed.png), [dialog (light)](screenshots/invite-light-dialog.png), [email-error (light)](screenshots/invite-light-email-error.png), [email-typed (light)](screenshots/invite-light-email-typed.png) |
| Creations. Tabs and two creation cards. | `/app/creations` | [full (dark)](screenshots/creations-dark-full.png), [default (dark)](screenshots/creations-dark.png), [default (light)](screenshots/creations-light.png) |
| Computers. The setup cards and the Customize and Connect bands. | `/app/computers` | [full (dark)](screenshots/computers-dark-full.png), [default (dark)](screenshots/computers-dark.png), [default (light)](screenshots/computers-light.png) |
| Agents. Meet Cue. | `/app/agents` | [full (dark)](screenshots/agents-dark-full.png), [default (dark)](screenshots/agents-dark.png), [default (light)](screenshots/agents-light.png) |
| Automations. The empty state with three example cards. | `/app/automation?tab=updates` | [full (dark)](screenshots/automations-dark-full.png), [default (dark)](screenshots/automations-dark.png), [default (light)](screenshots/automations-light.png) |
| Plugins. The gallery; also the More menu and a project's context menu, opened from the sidebar on this page. | `/app/plugins` | [full (dark)](screenshots/plugins-dark-full.png), [more-menu (dark)](screenshots/plugins-dark-more-menu.png), [project-context-menu (dark)](screenshots/plugins-dark-project-context-menu.png), [default (dark)](screenshots/plugins-dark.png), [more-menu (light)](screenshots/plugins-light-more-menu.png), [project-context-menu (light)](screenshots/plugins-light-project-context-menu.png), [default (light)](screenshots/plugins-light.png) |
| Project page (Hackathons). | `/app/project/<id>` | [full (dark)](screenshots/project-dark-full.png), [default (dark)](screenshots/project-dark.png), [default (light)](screenshots/project-light.png) |
| A finished task. The end of the thread with the deliverable card, the files dialog, the split view with New tab and with the Files tab, the sidebar task menu, and the thread scrolled to its top and middle. | `/app/<task id>` | [completed (dark)](screenshots/task-dark-completed.png), [files-dialog (dark)](screenshots/task-dark-files-dialog.png), [files-tab (dark)](screenshots/task-dark-files-tab.png), [side-panel (dark)](screenshots/task-dark-side-panel.png), [sidebar-task-menu (dark)](screenshots/task-dark-sidebar-task-menu.png), [thread-mid (dark)](screenshots/task-dark-thread-mid.png), [thread-top (dark)](screenshots/task-dark-thread-top.png), [completed (light)](screenshots/task-light-completed.png), [files-dialog (light)](screenshots/task-light-files-dialog.png), [files-tab (light)](screenshots/task-light-files-tab.png), [side-panel (light)](screenshots/task-light-side-panel.png), [sidebar-task-menu (light)](screenshots/task-light-sidebar-task-menu.png), [thread-mid (light)](screenshots/task-light-thread-mid.png), [thread-top (light)](screenshots/task-light-thread-top.png) |
| Home at 390: the app gate, the hero and composer, the drawer. | `/app` | [app-gate (dark)](screenshots/mobile-home-dark-app-gate.png), [drawer (dark)](screenshots/mobile-home-dark-drawer.png), [full (dark)](screenshots/mobile-home-dark-full.png), [default (dark)](screenshots/mobile-home-dark.png), [app-gate (light)](screenshots/mobile-home-light-app-gate.png), [drawer (light)](screenshots/mobile-home-light-drawer.png), [default (light)](screenshots/mobile-home-light.png) |
| Library at 390, and its type dropdown. | `/app/documents` | [full (dark)](screenshots/mobile-library-dark-full.png), [type-menu (dark)](screenshots/mobile-library-dark-type-menu.png), [default (dark)](screenshots/mobile-library-dark.png), [type-menu (light)](screenshots/mobile-library-light-type-menu.png), [default (light)](screenshots/mobile-library-light.png) |
| The finished task at 390. | `/app/<task id>` | [default (dark)](screenshots/mobile-task-dark.png), [default (light)](screenshots/mobile-task-light.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Manus Flex promo dialog | home, on load | at rest; dismissed with Got it, not re-opened | not captured as a copy (seen only in the live pane) |
| Model menu | home | the model picker | [home-dark-model-menu](screenshots/home-dark-model-menu.png), [model-menu](#model-menu) |
| Attach menu | home | the composer's + button | [home-dark-attach-menu](screenshots/home-dark-attach-menu.png), [attach-menu](#attach-menu) |
| Composer with text | home | a line typed, then deleted | [home-dark-composer-typed](screenshots/home-dark-composer-typed.png) |
| Collapsed sidebar | home | the collapse button; Cmd+. restores it | [home-dark-sidebar-collapsed](screenshots/home-dark-sidebar-collapsed.png), [sidebar-collapsed](#sidebar-collapsed) |
| Search dialog | home | the sidebar's search button (also Cmd+K) | [home-dark-search](screenshots/home-dark-search.png), [search-dialog](#search-dialog) |
| Notifications panel | home | the bell in the account row | [home-dark-notifications](screenshots/home-dark-notifications.png), [notifications-panel](#notifications-panel) |
| Account menu | Library | the account row | [library-dark-user-menu](screenshots/library-dark-user-menu.png) |
| Settings dialog | Library | Settings in the account menu, then Shortcuts in its nav; closed with Escape | [settings-dark-general](screenshots/settings-dark-general.png), [settings-dark-shortcuts](screenshots/settings-dark-shortcuts.png), [settings-dialog](#settings-dialog) |
| Type tabs, grid view, view options, group by task | Library | the Slides and Images tabs, the grid control, the view options button, Group by task toggled on and back off | [library-dark-slides](screenshots/library-dark-slides.png), [library-dark-images-grid](screenshots/library-dark-images-grid.png), [library-dark-images-grid-view-options](screenshots/library-dark-images-grid-view-options.png), [library-dark-images-grid-by-task](screenshots/library-dark-images-grid-by-task.png) |
| Row menu | Library | a row's more button | [library-dark-row-menu](screenshots/library-dark-row-menu.png), [row-menu](#row-menu) |
| Document previewer | Library | a row pressed; closed with Escape | [library-dark-preview-doc](screenshots/library-dark-preview-doc.png), [previewer](#previewer) |
| More menu | sidebar | the More tab | [plugins-dark-more-menu](screenshots/plugins-dark-more-menu.png), [more-menu](#more-menu) |
| Project context menu | sidebar | right-click on the project row; View project opened the project page | [plugins-dark-project-context-menu](screenshots/plugins-dark-project-context-menu.png), [context-menu](#context-menu) |
| Task menu | sidebar | the more button on a hovered task row | [task-dark-sidebar-task-menu](screenshots/task-dark-sidebar-task-menu.png), [task-menu](#task-menu) |
| Files dialog | task | View all files in this task; closed with Escape | [task-dark-files-dialog](screenshots/task-dark-files-dialog.png), [files-dialog](#files-dialog) |
| Split view | task | the panel toggle, then Files in Start from scratch; closed with the Close sidebar button | [task-dark-side-panel](screenshots/task-dark-side-panel.png), [task-dark-files-tab](screenshots/task-dark-files-tab.png) |
| Mobile app gate and drawer | home at 390 | on load, Continue with web; then the menu button | [mobile-home-dark-app-gate](screenshots/mobile-home-dark-app-gate.png), [mobile-home-dark-drawer](screenshots/mobile-home-dark-drawer.png) |
| Mobile type dropdown | Library at 390 | the All chip | [mobile-library-dark-type-menu](screenshots/mobile-library-dark-type-menu.png) |
| API key row menu and delete confirmation | Settings > Developers (2026-10-17) | a row's more button, then Delete; closed with Cancel, nothing deleted | [settings-dark-key-menu](screenshots/settings-dark-key-menu.png), [settings-dark-delete-confirm](screenshots/settings-dark-delete-confirm.png), [confirm-dialog](#confirm-dialog) |
| Create API Key form | Settings > Developers (2026-10-17) | Create new; a name typed, the Expiration select opened; closed with Cancel, nothing created | [settings-dark-create-key](screenshots/settings-dark-create-key.png), [settings-dark-create-key-typed](screenshots/settings-dark-create-key-typed.png), [settings-dark-select-open](screenshots/settings-dark-select-open.png), [form-dialog](#form-dialog) |
| Usage history loading | Settings > Usage & Billing (2026-10-17) | the pane opened, copied while its history fetched | [settings-dark-usage-loading](screenshots/settings-dark-usage-loading.png), [spinner](#spinner) |
| Invite dialog | account row banner (2026-10-17) | the Share Manus banner; an invalid address typed, not sent; closed | [invite-dark-dialog](screenshots/invite-dark-dialog.png), [invite-dark-email-typed](screenshots/invite-dark-email-typed.png), [invite-dialog](#invite-dialog) |
| Invalid email (validation error) and toast | invite dialog (2026-10-17) | with the owner's go-ahead, "not-an-email" typed and Send pressed; Manus refused it client-side with a toast, so nothing was sent | [invite-dark-email-error](screenshots/invite-dark-email-error.png), [toast](#toast), [email-field](#email-field) |
| Toast while a task starts | task (2026-10-17) | seen once, "Creating new task…" with a spinner, top centre | not captured as a copy; the same toast frame is measured from the validation error |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** 8px (400), 12px (128), 9999px (68), 6px (60), 10px (58), 22px (18), 16px (10), 100px (8), 5px (8), 4px (6). The density tokens name four of them: `radius.row` 10 (nav tabs, list rows), `radius.small` 8 (icon buttons, chips, the segmented control), `radius.card` 12 (cards, menus, dialogs), `radius.composer` 22. The 6 is the segmented control's thumb and the smaller icon buttons; 9999 is avatars, pills and the send button.

**Hover.** Manus hovers with a translucent fill, not a colour change. Dark: transparent to `≈ fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) (48), no change on the element (35), transparent to `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) (17), opacity 1 to 0.9 (7), `≈ fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) to `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) (4), `≈ background.live-events-end` (#242424) to `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) (3). Light: transparent to `≈ background.tsp-card-gray` (rgba(55, 53, 47, 0.04)) (48), no change on the element (35), transparent to `≈ fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) (17), opacity 1 to 0.9 (7), `≈ background.tsp-card-gray` (rgba(55, 53, 47, 0.04)) to `≈ fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) (4), `≈ background.menu-white` (#ffffff) to `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.08)) (3). The two fills are `fill.tsp-white-light` (4%) and `fill.tsp-white-main` (6%); the current nav tab rests on the 6% fill and hovers to it.

**Focus.** Of 66 elements given a real keyboard focus in dark: no ring on the element (50), 1px solid `≈ border.image-preview-toolbar` (rgba(255, 255, 255, 0.12)) offset -1px (9), 2px solid `≈ text.blue` (#1a93fe) offset 2px (3), 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) offset -1px (2), 2px solid `≈ text.secondary` (#b3b3b3) offset 0px (1), 2px solid transparent offset 2px (1). In light: no ring on the element (50), 1px solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)) offset -1px (9), 2px solid `≈ text.blue` (#0081f2) offset 2px (3), 1px solid `≈ border.menu-arrow` (rgba(0, 0, 0, 0.06)) offset -1px (2), 2px solid `≈ text.secondary` (#4d4d4d) offset 0px (1), 2px solid transparent offset 2px (1). Most of the focused elements are real `<button>`s, and most draw no ring; the 1px rings at offset -1px are the resting hairline of outlined buttons and the composer's chips, the same with or without focus; the 2px blue ring (`text.blue`, offset 2) is on the promo card, the Computers setup card and the Computers Customize band, and not on the send button or the theme cards, which draw none.

**Motion.** 0.15s cubic-bezier(0.4, 0, 0.2, 1) (292), 0.2s cubic-bezier(0.4, 0, 0.2, 1) (32), 0.15s cubic-bezier(0, 0, 0.2, 1) (18), 0.3s cubic-bezier(0.4, 0, 0.2, 1) (14), 0.2s cubic-bezier(0, 0, 0.2, 1) (4), 0.1s cubic-bezier(0.4, 0, 0.2, 1) (2). Nearly every transition is Tailwind's `transition-colors` at 150 ms on the standard curve; the sidebar's width is 200 ms, the task column's theme cross-fade 500 ms, the segmented thumb 200 ms on transform.

**Layout grid.** The sidebar is 300 wide (52 as a rail), the main column the rest, with a 48 tall bar over it. The home, plugins and task pages set a 768 to 800 wide centred column; the Library, Creations, Computers and Automations a 960 to 1000 wide one. On a phone the sidebar is the same 300 wide column parked off-screen and slid in as a drawer. The numbers per page are in [raw/pages.md](raw/pages.md).

## Components

### Sidebar

The 300px sidebar every page shares: a 48px logo row with search and collapse, eight nav tabs, a Projects section of folders and a Tasks section of recent threads (each with its type glyph, a dashed ring while it runs), the share banner, and the account row with the desktop and notification buttons. Cmd+. folds it to a 52px rail of glyphs.

#### Sidebar (expanded)

<a id="sidebar"></a>`sidebar`, on home-dark. 300 wide, full height, its own --background-nav fill; a 1px rule drawn by nav::after at the inline end.

<img src="components/crops/sidebar-default.png" alt="Sidebar (expanded), default" height="120"> <img src="components/crops/sidebar-light.png" alt="Sidebar (expanded), light" height="120"> 

| State | Values |
|---|---|
| default | size 300 x 900; background `background.nav` (#1f1f1f); text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#e6e6e6); transition transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 28 x 28, `≈ text.primary` (#e6e6e6) |
| light | size 300 x 900; background `background.nav` (#f0f0f0); text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#1a1a1a); transition transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 28 x 28, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-nav`, `--border-light`, `--border-main`, `--fill-tsp-white-light`, `--icon-secondary`, `--text-primary`, `--text-tertiary`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-nav-item-padding-start`, `--ui-density-outer-padding`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-font-size-sm`.

#### Sidebar logo row

<a id="sidebar-logo-row"></a>`sidebar-logo-row`, on home-dark. 48 tall: the mark and wordmark at the start, search and collapse icon buttons at the end.

<img src="components/crops/sidebar-logo-row-default.png" alt="Sidebar logo row, default" height="48"> <img src="components/crops/sidebar-logo-row-light.png" alt="Sidebar logo row, light" height="48"> 

| State | Values |
|---|---|
| default | size 300 x `size.header` (48px); padding `space.2` (8px) `space.2_5` (10px); background transparent; icon 28 x 28, `≈ text.primary` (#e6e6e6) |
| light | size 300 x `size.header` (48px); padding `space.2` (8px) `space.2_5` (10px); background transparent; icon 28 x 28, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`.

#### Sidebar logo (mark and wordmark)

<a id="sidebar-logo"></a>`sidebar-logo`, on home-dark.

<img src="components/crops/sidebar-logo-default.png" alt="Sidebar logo (mark and wordmark), default" height="28"> <img src="components/crops/sidebar-logo-hover.png" alt="Sidebar logo (mark and wordmark), hover" height="28"> <img src="components/crops/sidebar-logo-light.png" alt="Sidebar logo (mark and wordmark), light" height="28"> <img src="components/crops/sidebar-logo-light-hover.png" alt="Sidebar logo (mark and wordmark), light-hover" height="28"> 

| State | Values |
|---|---|
| default (same: hover) | size 94.83 x `size.control-small` (28px); background transparent; icon 28 x 28, `≈ text.primary` (#e6e6e6) |
| light (same: light-hover) | size 94.83 x `size.control-small` (28px); background transparent; icon 28 x 28, `≈ text.primary` (#1a1a1a) |

#### Sidebar search icon button

<a id="sidebar-search-button"></a>`sidebar-search-button`, on home-dark. 32x32, radius 6, the hover fill is --fill-tsp-white-light.

<img src="components/crops/sidebar-search-button-default.png" alt="Sidebar search icon button, default" height="32"> <img src="components/crops/sidebar-search-button-hover.png" alt="Sidebar search icon button, hover" height="32"> <img src="components/crops/sidebar-search-button-light.png" alt="Sidebar search icon button, light" height="32"> <img src="components/crops/sidebar-search-button-light-hover.png" alt="Sidebar search icon button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`.

#### Sidebar collapse icon button

<a id="sidebar-collapse-button"></a>`sidebar-collapse-button`, on home-dark.

<img src="components/crops/sidebar-collapse-button-default.png" alt="Sidebar collapse icon button, default" height="32"> <img src="components/crops/sidebar-collapse-button-hover.png" alt="Sidebar collapse icon button, hover" height="32"> <img src="components/crops/sidebar-collapse-button-light.png" alt="Sidebar collapse icon button, light" height="32"> <img src="components/crops/sidebar-collapse-button-light-hover.png" alt="Sidebar collapse icon button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`.

#### Nav tab

<a id="nav-tab"></a>`nav-tab`, on home-dark, library-dark. A `.group/nav-tab` row, 36 tall at this density, an 18px icon in a 20px box and 14px text. Hover reveals the shortcut hint (⌘⇧O). The current page gets a filled row (`active`, from the Library snapshot).

<img src="components/crops/nav-tab-default.png" alt="Nav tab, default" height="36"> <img src="components/crops/nav-tab-hover.png" alt="Nav tab, hover" height="36"> <img src="components/crops/nav-tab-light.png" alt="Nav tab, light" height="36"> <img src="components/crops/nav-tab-light-hover.png" alt="Nav tab, light-hover" height="36"> <img src="components/crops/nav-tab-active.png" alt="Nav tab, active" height="36"> 

| State | Values |
|---|---|
| default | size 284 x `size.row` (36px); padding 0px `space.0_5` (2px) 0px `space.2` (8px); radius `radius.row` (10px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| active | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| active-hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 284 x `size.row` (36px); padding 0px `space.0_5` (2px) 0px `space.2` (8px); radius `radius.row` (10px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-active | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |
| light-active-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-nav-item-padding-start`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-font-size-sm`.

#### Nav tab shortcut hint

<a id="nav-tab-shortcut"></a>`nav-tab-shortcut`, on home-dark. Opacity 0 at rest, shown with group-hover; measured while its row is hovered.

<img src="components/crops/nav-tab-shortcut-hover.png" alt="Nav tab shortcut hint, hover" height="24"> <img src="components/crops/nav-tab-shortcut-light-hover.png" alt="Nav tab shortcut hint, light-hover" height="24"> 

| State | Values |
|---|---|
| hover | size 35.59 x 16.5; padding 0px `space.1_5` (6px) 0px 0px; background transparent; text System 11/16.5 400, `text.tertiary` (#8c8c8c); transition opacity `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | size 35.59 x 16.5; padding 0px `space.1_5` (6px) 0px 0px; background transparent; text System 11/16.5 400, `text.tertiary` (#737373); transition opacity `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--text-tertiary`.

#### Nav badge (Cue!)

<a id="nav-badge-cue"></a>`nav-badge-cue`, on home-dark.

<img src="components/crops/nav-badge-cue-default.png" alt="Nav badge (Cue!), default" height="24"> <img src="components/crops/nav-badge-cue-light.png" alt="Nav badge (Cue!), light" height="24"> 

| State | Values |
|---|---|
| default | size 40.39 x 20; padding 0px `space.2` (8px); radius `radius.full` (9999px); background `fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)); icon 24.39 x 9.2, `≈ text.primary` (#e6e6e6) |
| light | size 40.39 x 20; padding 0px `space.2` (8px); radius `radius.full` (9999px); background `fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)); icon 24.39 x 9.2, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--text-primary`.

#### Nav section header (Projects)

<a id="nav-section-header"></a>`nav-section-header`, on home-dark. A label in --text-tertiary; hover fills the row and reveals its action buttons (new project, more).

<img src="components/crops/nav-section-header-default.png" alt="Nav section header (Projects), default" height="36"> <img src="components/crops/nav-section-header-hover.png" alt="Nav section header (Projects), hover" height="36"> <img src="components/crops/nav-section-header-light.png" alt="Nav section header (Projects), light" height="36"> <img src="components/crops/nav-section-header-light-hover.png" alt="Nav section header (Projects), light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 284 x `size.row` (36px); padding `space.0_5` (2px) `space.0_5` (2px) `space.0_5` (2px) `space.2_5` (10px); background `background.nav` (#1f1f1f); text System 13/18 500 tracking -0.091px, `≈ icon.tertiary` (#8c8c8c); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover, light-pressed) | size 284 x `size.row` (36px); padding `space.0_5` (2px) `space.0_5` (2px) `space.0_5` (2px) `space.2_5` (10px); background `background.nav` (#f0f0f0); text System 13/18 500 tracking -0.091px, `≈ icon.tertiary` (#737373); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-nav`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--icon-tertiary`, `--text-tertiary`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-density-section-padding-start`, `--ui-density-section-row-gap`, `--ui-font-size-label`, `--ui-line-height-label`.

#### Nav section header (Tasks)

<a id="nav-section-header-tasks"></a>`nav-section-header-tasks`, on home-dark. Same row; three actions on hover (filter, sort, new).

<img src="components/crops/nav-section-header-tasks-default.png" alt="Nav section header (Tasks), default" height="36"> <img src="components/crops/nav-section-header-tasks-hover.png" alt="Nav section header (Tasks), hover" height="36"> <img src="components/crops/nav-section-header-tasks-light.png" alt="Nav section header (Tasks), light" height="36"> <img src="components/crops/nav-section-header-tasks-light-hover.png" alt="Nav section header (Tasks), light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 284 x `size.row` (36px); padding `space.0_5` (2px) `space.0_5` (2px) `space.0_5` (2px) `space.2_5` (10px); background `background.nav` (#1f1f1f); text System 13/18 500 tracking -0.091px, `≈ icon.tertiary` (#8c8c8c); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover, light-pressed) | size 284 x `size.row` (36px); padding `space.0_5` (2px) `space.0_5` (2px) `space.0_5` (2px) `space.2_5` (10px); background `background.nav` (#f0f0f0); text System 13/18 500 tracking -0.091px, `≈ icon.tertiary` (#737373); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-nav`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-tertiary`, `--text-tertiary`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-density-section-padding-start`, `--ui-density-section-row-gap`, `--ui-font-size-label`, `--ui-line-height-label`.

#### Nav section action button

<a id="nav-section-action"></a>`nav-section-action`, on home-dark. A 28x28 icon button shown once the section header is hovered (hovering it also hovers the header).

<img src="components/crops/nav-section-action-hover.png" alt="Nav section action button, hover" height="28"> <img src="components/crops/nav-section-action-light-hover.png" alt="Nav section action button, light-hover" height="28"> 

| State | Values |
|---|---|
| hover | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); icon `size.icon` (18 x 18), `icon.tertiary` (#8c8c8c) |
| light-hover | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); icon `size.icon` (18 x 18), `icon.tertiary` (#737373) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-tertiary`.

#### Project row

<a id="nav-project-row"></a>`nav-project-row`, on home-dark. The folder icon swaps for a chevron on hover, and a more button appears at the end.

| State | Values |
|---|---|
| default (same: focus-visible) | size 284 x `size.row` (36px); padding 0px `space.0_5` (2px) 0px `space.2` (8px); background `background.nav` (#1f1f1f); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | radius `radius.row` (10px); shadow rgba(255, 255, 255, 0.04) 0px 0px 0px 100px inset |
| light (same: light-focus-visible) | size 284 x `size.row` (36px); padding 0px `space.0_5` (2px) 0px `space.2` (8px); background `background.nav` (#f0f0f0); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | radius `radius.row` (10px); shadow rgba(55, 53, 47, 0.04) 0px 0px 0px 100px inset |

Tokens named in its classes: `--background-nav`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-nav-item-padding-start`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-density-section-row-gap`.

#### Task row

<a id="nav-task-row"></a>`nav-task-row`, on home-dark, task-dark-completed. Inside `[data-context-menu=session]`; the title is masked at the end by a scroll-shadow gradient, not an ellipsis.

| State | Values |
|---|---|
| default | size 284 x `size.row` (36px); padding 0px `space.0_5` (2px) 0px `space.2` (8px); radius `radius.row` (10px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| active | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 284 x `size.row` (36px); padding 0px `space.0_5` (2px) 0px `space.2` (8px); radius `radius.row` (10px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-active | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Child layers: div 238pxx21px

Tokens named in its classes: `--background-nav`, `--fill-tsp-white-light`, `--scroll-shadow-background`, `--scroll-shadow-block-end-offset`, `--scroll-shadow-block-start-offset`, `--scroll-shadow-height`, `--scroll-shadow-inline-end-offset`, `--scroll-shadow-inline-start-offset`, `--scroll-shadow-width`, `--scroll-shadow-z-index`, `--text-primary`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-nav-item-padding-start`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-font-size-sm`.

#### Task row icon

<a id="nav-task-icon"></a>`nav-task-icon`, on home-dark. An 18px glyph tinted grey with a CSS filter on an <img>.

<img src="components/crops/nav-task-icon-default.png" alt="Task row icon, default" height="24"> <img src="components/crops/nav-task-icon-light.png" alt="Task row icon, light" height="24"> 

| State | Values |
|---|---|
| default | size 18 x 18; background transparent |
| light | size 18 x 18; background transparent |

#### Task row status spinner (running task)

<a id="nav-task-running"></a>`nav-task-running`, on home-dark. A dotted amber ring in place of the task icon.

<img src="components/crops/nav-task-running-default.png" alt="Task row status spinner (running task), default" height="24"> <img src="components/crops/nav-task-running-light.png" alt="Task row status spinner (running task), light" height="24"> 

| State | Values |
|---|---|
| default | size 18 x 18; background transparent; icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| light | size 18 x 18; background transparent; icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |

#### Task list loading skeleton

<a id="nav-skeleton"></a>`nav-skeleton`, on home-dark. Pulsing rows at the end of the task list while more load; the list is scrolled to its end to show them.

<img src="components/crops/nav-skeleton-default.png" alt="Task list loading skeleton, default" height="24"> <img src="components/crops/nav-skeleton-light.png" alt="Task list loading skeleton, light" height="24"> 

| State | Values |
|---|---|
| default | size 268 x 20; radius `radius.md` (6px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 268 x 20; radius `radius.md` (6px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`.

#### Share banner ("Share Manus with a friend")

<a id="share-banner"></a>`share-banner`, on home-dark. Radius 12, a 0.5px --border-dark hairline, --background-mask-white fill; serif title over a 12px grey line, a chevron at the end.

<img src="components/crops/share-banner-default.png" alt="Share banner ("Share Manus with a friend"), default" height="54"> <img src="components/crops/share-banner-hover.png" alt="Share banner ("Share Manus with a friend"), hover" height="54"> <img src="components/crops/share-banner-light.png" alt="Share banner ("Share Manus with a friend"), light" height="54"> <img src="components/crops/share-banner-light-hover.png" alt="Share banner ("Share Manus with a friend"), light-hover" height="54"> <img src="components/crops/share-banner-focus-visible.png" alt="Share banner ("Share Manus with a friend"), focus-visible" height="54"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 284 x 54; border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.mask-white` (rgba(63, 63, 63, 0.32)); text Libre Baskerville 14/20 400, `≈ text.primary` (#e6e6e6); transition box-shadow `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | shadow rgba(255, 255, 255, 0.04) 0px 0px 0px 100px inset |
| light (same: light-focus-visible) | size 284 x 54; border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.mask-white` (rgba(255, 255, 255, 0.65)); text Libre Baskerville 14/20 400, `≈ text.primary` (#1a1a1a); transition box-shadow `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | shadow rgba(55, 53, 47, 0.04) 0px 0px 0px 100px inset |

Tokens named in its classes: `--background-mask-white`, `--border-dark`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`, `--ui-density-menu-item-padding-y`, `--ui-density-section-row-gap`, `--ui-density-small-row-height`.

#### Sidebar footer account row

<a id="sidebar-footer"></a>`sidebar-footer`, on home-dark. Avatar, name, then the desktop and bell icon buttons.

<img src="components/crops/sidebar-footer-default.png" alt="Sidebar footer account row, default" height="32"> <img src="components/crops/sidebar-footer-light.png" alt="Sidebar footer account row, light" height="32"> 

| State | Values |
|---|---|
| default | size 284 x `size.row-small` (32px); padding 0px `space.0_5` (2px) 0px 0px; background transparent; text `typography.role.initial` (System 12/20 600), `≈ icon.primary` (#e6e6e6); icon `size.icon` (18 x 18), `icon.primary` (#e6e6e6) |
| light | size 284 x `size.row-small` (32px); padding 0px `space.0_5` (2px) 0px 0px; background transparent; text `typography.role.initial` (System 12/20 600), `≈ icon.primary` (#1a1a1a); icon `size.icon` (18 x 18), `icon.primary` (#1a1a1a) |

Child layers: div 28x28 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08))

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-primary`, `--text-primary`.

#### Account button (avatar and name)

<a id="sidebar-account"></a>`sidebar-account`, on home-dark.

<img src="components/crops/sidebar-account-default.png" alt="Account button (avatar and name), default" height="32"> <img src="components/crops/sidebar-account-hover.png" alt="Account button (avatar and name), hover" height="32"> <img src="components/crops/sidebar-account-light.png" alt="Account button (avatar and name), light" height="32"> <img src="components/crops/sidebar-account-light-hover.png" alt="Account button (avatar and name), light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 90.52 x `size.row-small` (32px); padding `space.0_5` (2px); background transparent; text `typography.role.initial` (System 12/20 600), `≈ text.primary` (#e6e6e6) |
| hover | opacity 0.7 |
| light | size 90.52 x `size.row-small` (32px); padding `space.0_5` (2px); background transparent; text `typography.role.initial` (System 12/20 600), `≈ text.primary` (#1a1a1a) |
| light-hover | opacity 0.7 |

Child layers: div 28x28 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08))

Tokens named in its classes: `--text-primary`.

#### Avatar (letter)

<a id="sidebar-avatar"></a>`sidebar-avatar`, on home-dark.

<img src="components/crops/sidebar-avatar-default.png" alt="Avatar (letter), default" height="28"> <img src="components/crops/sidebar-avatar-light.png" alt="Avatar (letter), light" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.full` (9999px); background transparent; text `typography.role.initial` (System 12/20 600), `≈ text.primary` (#e6e6e6) |
| light | size 28 x `size.control-small` (28px); radius `radius.full` (9999px); background transparent; text `typography.role.initial` (System 12/20 600), `≈ text.primary` (#1a1a1a) |

Child layers: div 28x28 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08))

#### Desktop app icon button

<a id="sidebar-desktop-button"></a>`sidebar-desktop-button`, on home-dark.

<img src="components/crops/sidebar-desktop-button-default.png" alt="Desktop app icon button, default" height="28"> <img src="components/crops/sidebar-desktop-button-hover.png" alt="Desktop app icon button, hover" height="28"> <img src="components/crops/sidebar-desktop-button-light.png" alt="Desktop app icon button, light" height="28"> <img src="components/crops/sidebar-desktop-button-light-hover.png" alt="Desktop app icon button, light-hover" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon` (18 x 18), `icon.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon` (18 x 18), `icon.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-primary`.

#### Notifications bell button

<a id="sidebar-bell-button"></a>`sidebar-bell-button`, on home-dark, home-dark-notifications.

<img src="components/crops/sidebar-bell-button-default.png" alt="Notifications bell button, default" height="28"> <img src="components/crops/sidebar-bell-button-hover.png" alt="Notifications bell button, hover" height="28"> <img src="components/crops/sidebar-bell-button-light.png" alt="Notifications bell button, light" height="28"> <img src="components/crops/sidebar-bell-button-light-hover.png" alt="Notifications bell button, light-hover" height="28"> <img src="components/crops/sidebar-bell-button-open.png" alt="Notifications bell button, open" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon` (18 x 18), `icon.primary` (#e6e6e6) |
| hover, open | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon` (18 x 18), `icon.primary` (#1a1a1a) |
| light-hover, light-open | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-primary`.

#### Sidebar collapsed to a rail

<a id="sidebar-collapsed"></a>`sidebar-collapsed`, on home-dark-sidebar-collapsed. 52 wide: icon-only nav tabs (36x36), a 28px divider in place of the sections, the footer buttons stacked.

<img src="components/crops/sidebar-collapsed-default.png" alt="Sidebar collapsed to a rail, default" height="120"> <img src="components/crops/sidebar-collapsed-light.png" alt="Sidebar collapsed to a rail, light" height="120"> 

| State | Values |
|---|---|
| default | size 52 x 900; background `background.nav` (#1f1f1f); text `typography.role.initial` (System 12/20 600), `≈ text.primary` (#e6e6e6); transition transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 28 x 28, `≈ text.primary` (#e6e6e6) |
| light | size 52 x 900; background `background.nav` (#f0f0f0); text `typography.role.initial` (System 12/20 600), `≈ text.primary` (#1a1a1a); transition transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 28 x 28, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-nav`, `--border-light`, `--border-main`, `--fill-tsp-white-light`, `--scroll-shadow-background`, `--scroll-shadow-block-end-offset`, `--scroll-shadow-block-start-offset`, `--scroll-shadow-height`, `--scroll-shadow-inline-end-offset`, `--scroll-shadow-inline-start-offset`, `--scroll-shadow-width`, `--scroll-shadow-z-index`, `--simplebar-scrollbar-width`, `--text-disable`, `--text-tertiary`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-outer-padding`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-density-section-gap`.

#### Collapsed rail nav tab

<a id="sidebar-collapsed-tab"></a>`sidebar-collapsed-tab`, on home-dark-sidebar-collapsed.

<img src="components/crops/sidebar-collapsed-tab-default.png" alt="Collapsed rail nav tab, default" height="36"> <img src="components/crops/sidebar-collapsed-tab-hover.png" alt="Collapsed rail nav tab, hover" height="36"> <img src="components/crops/sidebar-collapsed-tab-light.png" alt="Collapsed rail nav tab, light" height="36"> <img src="components/crops/sidebar-collapsed-tab-light-hover.png" alt="Collapsed rail nav tab, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 36 x `size.row` (36px); padding `space.2` (8px); radius `radius.row` (10px); background transparent; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 36 x `size.row` (36px); padding `space.2` (8px); radius `radius.row` (10px); background transparent; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-outer-padding`, `--ui-density-row-height`, `--ui-density-row-radius`.

### Top bar

The 48px row over the content: the model picker at the left, and at the right the plan chip with its Upgrade link and the credits pill on the home, or Upgrade, Share, more and the panel toggle on a task.

#### Model picker trigger

<a id="model-picker"></a>`model-picker`, on home-dark, home-dark-model-menu. Title-size 18/22 500 text and a 16px chevron that turns 180° when the menu is open.

<img src="components/crops/model-picker-default.png" alt="Model picker trigger, default" height="32"> <img src="components/crops/model-picker-hover.png" alt="Model picker trigger, hover" height="32"> <img src="components/crops/model-picker-light.png" alt="Model picker trigger, light" height="32"> <img src="components/crops/model-picker-light-hover.png" alt="Model picker trigger, light-hover" height="32"> <img src="components/crops/model-picker-open.png" alt="Model picker trigger, open" height="32"> 

| State | Values |
|---|---|
| default | size 154.09 x `size.row-small` (32px); padding 7px `space.1_5` (6px) 7px `space.2` (8px); radius `radius.small` (8px); background transparent; text System 18/22 500, `≈ text.primary` (#e6e6e6); transition background-color `duration.fast` (0.15s) cubic-bezier(0, 0, 0.2, 1); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| hover, open | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 154.09 x `size.row-small` (32px); padding 7px `space.1_5` (6px) 7px `space.2` (8px); radius `radius.small` (8px); background transparent; text System 18/22 500, `≈ text.primary` (#1a1a1a); transition background-color `duration.fast` (0.15s) cubic-bezier(0, 0, 0.2, 1); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |
| light-hover, light-open | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`.

#### Plan chip (Free plan | Upgrade)

<a id="plan-chip"></a>`plan-chip`, on home-dark.

<img src="components/crops/plan-chip-default.png" alt="Plan chip (Free plan | Upgrade), default" height="32"> <img src="components/crops/plan-chip-light.png" alt="Plan chip (Free plan | Upgrade), light" height="32"> 

| State | Values |
|---|---|
| default | size 166.7 x `size.row-small` (32px); padding `space.1` (4px) `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.small` (8px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.tertiary` (#8c8c8c) |
| light | size 166.7 x `size.row-small` (32px); padding `space.1` (4px) `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.small` (8px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--border-dark`, `--border-main`, `--text-blue`, `--text-tertiary`.

#### Upgrade link in the plan chip

<a id="upgrade-link"></a>`upgrade-link`, on home-dark. Blue text, hover drops opacity to 0.8.

<img src="components/crops/upgrade-link-default.png" alt="Upgrade link in the plan chip, default" height="24"> <img src="components/crops/upgrade-link-hover.png" alt="Upgrade link in the plan chip, hover" height="24"> <img src="components/crops/upgrade-link-light.png" alt="Upgrade link in the plan chip, light" height="24"> <img src="components/crops/upgrade-link-light-hover.png" alt="Upgrade link in the plan chip, light-hover" height="24"> <img src="components/crops/upgrade-link-focus-visible.png" alt="Upgrade link in the plan chip, focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 56 x 21; radius `radius.small` (8px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.blue` (#1a93fe); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover, pressed | opacity `opacity.pressed` (0.8) |
| light (same: light-focus-visible) | size 56 x 21; radius `radius.small` (8px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.blue` (#0081f2); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover, light-pressed | opacity `opacity.pressed` (0.8) |

Tokens named in its classes: `--text-blue`.

#### Credits pill

<a id="credits-pill"></a>`credits-pill`, on home-dark.

<img src="components/crops/credits-pill-default.png" alt="Credits pill, default" height="32"> <img src="components/crops/credits-pill-hover.png" alt="Credits pill, hover" height="32"> <img src="components/crops/credits-pill-light.png" alt="Credits pill, light" height="32"> <img src="components/crops/credits-pill-light-hover.png" alt="Credits pill, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 65.88 x `size.row-small` (32px); padding 0px `space.3` (12px) 0px `space.2` (8px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.small` (8px); background transparent; text System 14/20 500 tracking -0.15px, `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 65.88 x `size.row-small` (32px); padding 0px `space.3` (12px) 0px `space.2` (8px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.small` (8px); background transparent; text System 14/20 500 tracking -0.15px, `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--border-main`, `--fill-tsp-white-main`, `--text-primary`.

#### Upgrade button (task page)

<a id="upgrade-button-task"></a>`upgrade-button-task`, on task-dark-completed. On a task the plan chip collapses to one tinted Upgrade button.

<img src="components/crops/upgrade-button-task-default.png" alt="Upgrade button (task page), default" height="32"> <img src="components/crops/upgrade-button-task-hover.png" alt="Upgrade button (task page), hover" height="32"> <img src="components/crops/upgrade-button-task-light.png" alt="Upgrade button (task page), light" height="32"> <img src="components/crops/upgrade-button-task-light-hover.png" alt="Upgrade button (task page), light-hover" height="32"> <img src="components/crops/upgrade-button-task-focus-visible.png" alt="Upgrade button (task page), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 90.88 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.row` (10px); background rgba(0, 129, 242, 0.08); text System 13/18 500 tracking -0.091px, `≈ activity-indicator.running` (#0081f2); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background rgba(0, 129, 242, 0.12) |
| light (same: light-focus-visible) | size 90.88 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.row` (10px); background `≈ fill.blue` (rgba(0, 129, 242, 0.08)); text System 13/18 500 tracking -0.091px, `≈ text.blue` (#0081f2); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background rgba(0, 129, 242, 0.12) |

Tokens named in its classes: `--text-primary`.

#### Share button

<a id="share-button"></a>`share-button`, on task-dark-completed.

<img src="components/crops/share-button-default.png" alt="Share button, default" height="32"> <img src="components/crops/share-button-hover.png" alt="Share button, hover" height="32"> <img src="components/crops/share-button-light.png" alt="Share button, light" height="32"> <img src="components/crops/share-button-light-hover.png" alt="Share button, light-hover" height="32"> <img src="components/crops/share-button-focus-visible.png" alt="Share button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 74.22 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.label-compact` (System 14/18 500), `≈ text.secondary` (#b3b3b3); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light (same: light-focus-visible) | size 74.22 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.label-compact` (System 14/18 500), `≈ text.secondary` (#4d4d4d); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--text-secondary`.

#### More (…) button

<a id="topbar-more-button"></a>`topbar-more-button`, on task-dark-completed.

<img src="components/crops/topbar-more-button-default.png" alt="More (…) button, default" height="32"> <img src="components/crops/topbar-more-button-hover.png" alt="More (…) button, hover" height="32"> <img src="components/crops/topbar-more-button-light.png" alt="More (…) button, light" height="32"> <img src="components/crops/topbar-more-button-light-hover.png" alt="More (…) button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon-small` (16 x 16), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon-small` (16 x 16), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`.

#### Side panel toggle

<a id="panel-toggle"></a>`panel-toggle`, on task-dark-completed.

<img src="components/crops/panel-toggle-default.png" alt="Side panel toggle, default" height="32"> <img src="components/crops/panel-toggle-hover.png" alt="Side panel toggle, hover" height="32"> <img src="components/crops/panel-toggle-light.png" alt="Side panel toggle, light" height="32"> <img src="components/crops/panel-toggle-light-hover.png" alt="Side panel toggle, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`.

### Home

The new-task page: the logo with the promo carousel beside it, the Build and Create cards, the Start from a local file card, and the composer pinned at the bottom.

#### Home logo (mark and wordmark)

<a id="home-logo"></a>`home-logo`, on home-dark. An h1 holding two SVGs, 376x64, with "Manus Studio" as sr-only text.

<img src="components/crops/home-logo-default.png" alt="Home logo (mark and wordmark), default" height="64"> <img src="components/crops/home-logo-light.png" alt="Home logo (mark and wordmark), light" height="64"> 

| State | Values |
|---|---|
| default | size 376 x 64; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| light | size 376 x 64; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |

#### Promo carousel card

<a id="promo-card"></a>`promo-card`, on home-dark. Black (--background-game-promo) radius 12, 56 tall; a framed 38x30 preview, a serif 13/18 bold title and a 12/16 subtitle in white.

<img src="components/crops/promo-card-default.png" alt="Promo carousel card, default" height="56"> <img src="components/crops/promo-card-hover.png" alt="Promo carousel card, hover" height="56"> <img src="components/crops/promo-card-light.png" alt="Promo carousel card, light" height="56"> <img src="components/crops/promo-card-light-hover.png" alt="Promo carousel card, light-hover" height="56"> <img src="components/crops/promo-card-focus-visible.png" alt="Promo carousel card, focus-visible" height="56"> 

| State | Values |
|---|---|
| default (same: hover) | size 252 x 56; padding 1px `space.3_5` (14px) 1px `space.2_5` (10px); border `borderWidth.default` (1px) solid transparent; radius `radius.card` (12px); background `game.promo` (#000000); text Libre Baskerville 13/18 700, `≈ text.white` (#ffffff); transition transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| focus-visible | outline `focusRing.width` (2px) solid `≈ text.blue` (#1a93fe), offset `focusRing.width` (2px) |
| light (same: light-hover) | size 252 x 56; padding 1px `space.3_5` (14px) 1px `space.2_5` (10px); border `borderWidth.default` (1px) solid transparent; radius `radius.card` (12px); background `game.promo` (#1a1a19); text Libre Baskerville 13/18 700, `≈ text.white` (#ffffff); transition transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-focus-visible | outline `focusRing.width` (2px) solid `≈ text.blue` (#0081f2), offset `focusRing.width` (2px) |

Tokens named in its classes: `--background-game-promo`, `--background-game-promo-preview`, `--border-game-promo-preview`, `--text-blue`, `--text-white`, `--text-white-tsp`.

#### Promo carousel dot

<a id="promo-dot"></a>`promo-dot`, on home-dark. A 5px track in --fill-tsp-white-dark with an --icon-secondary fill that grows as the slide plays; the dots stack vertically at the card end.

<img src="components/crops/promo-dot-default.png" alt="Promo carousel dot, default" height="24"> <img src="components/crops/promo-dot-light.png" alt="Promo carousel dot, light" height="24"> <img src="components/crops/promo-dot-focus-visible.png" alt="Promo carousel dot, focus-visible" height="24"> 

| State | Values |
|---|---|
| default | size 14 x 18; radius `radius.full` (9999px); background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| focus-visible | outline `focusRing.width` (2px) solid `≈ icon.secondary` (#b3b3b3), offset 0px |
| inactive | size 14 x 12 |
| light | size 14 x 18; radius `radius.full` (9999px); background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |
| light-focus-visible | outline `focusRing.width` (2px) solid `≈ icon.secondary` (#4d4d4d), offset 0px |
| light-inactive | size 14 x 12 |

Child layers: span 5x18 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)) radius 9999px; span 5x3.6 background `≈ text.secondary` (#b3b3b3) radius 9999px

Tokens named in its classes: `--fill-tsp-white-dark`, `--icon-secondary`.

#### Build card

<a id="build-card"></a>`build-card`, on home-dark. 490x130, --fill-tsp-white-light, hover --fill-tsp-white-main; a 16/22 500 title with a chevron, a 14/20 grey line, an illustration bleeding off the end.

<img src="components/crops/build-card-default.png" alt="Build card, default" height="120"> <img src="components/crops/build-card-hover.png" alt="Build card, hover" height="120"> <img src="components/crops/build-card-light.png" alt="Build card, light" height="120"> <img src="components/crops/build-card-light-hover.png" alt="Build card, light-hover" height="120"> <img src="components/crops/build-card-focus-visible.png" alt="Build card, focus-visible" height="120"> 

| State | Values |
|---|---|
| default | size 490 x 130; padding 0px 0px 0px `space.5` (20px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.title-base` (System 16/22 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(255, 255, 255, 0.12) 0px 0px 0px 2px; outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px) |
| light | size 490 x 130; padding 0px 0px 0px `space.5` (20px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.title-base` (System 16/22 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |
| light-focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(0, 0, 0, 0.14) 0px 0px 0px 2px; outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px) |

Tokens named in its classes: `--border-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`, `--text-tertiary`.

#### Create card

<a id="create-card"></a>`create-card`, on home-dark.

<img src="components/crops/create-card-default.png" alt="Create card, default" height="120"> <img src="components/crops/create-card-hover.png" alt="Create card, hover" height="120"> <img src="components/crops/create-card-light.png" alt="Create card, light" height="120"> <img src="components/crops/create-card-light-hover.png" alt="Create card, light-hover" height="120"> 

| State | Values |
|---|---|
| default | size 490 x 130; padding 0px 0px 0px `space.5` (20px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.title-base` (System 16/22 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 490 x 130; padding 0px 0px 0px `space.5` (20px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.title-base` (System 16/22 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--illustration-studio-create-paper`, `--text-primary`, `--text-tertiary`.

#### Start from a local file card

<a id="local-file-card"></a>`local-file-card`, on home-dark.

<img src="components/crops/local-file-card-default.png" alt="Start from a local file card, default" height="120"> <img src="components/crops/local-file-card-hover.png" alt="Start from a local file card, hover" height="120"> <img src="components/crops/local-file-card-light.png" alt="Start from a local file card, light" height="120"> <img src="components/crops/local-file-card-light-hover.png" alt="Start from a local file card, light-hover" height="120"> 

| State | Values |
|---|---|
| default | size 270 x 270; padding `space.3` (12px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.caption` (System 12/16 400), `≈ text.secondary` (#b3b3b3); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 270 x 270; padding `space.3` (12px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.caption` (System 12/16 400), `≈ text.secondary` (#4d4d4d); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--border-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--fill-white-primary`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Studio only badge

<a id="studio-only-badge"></a>`studio-only-badge`, on home-dark.

<img src="components/crops/studio-only-badge-default.png" alt="Studio only badge, default" height="24"> <img src="components/crops/studio-only-badge-light.png" alt="Studio only badge, light" height="24"> 

| State | Values |
|---|---|
| default | size 75.45 x 20; padding 0px `space.1_5` (6px); radius `radius.full` (9999px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.role.caption` (System 12/16 400), `text.secondary` (#b3b3b3) |
| light | size 75.45 x 20; padding 0px `space.1_5` (6px); radius `radius.full` (9999px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.role.caption` (System 12/16 400), `text.secondary` (#4d4d4d) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-secondary`.

### Composer

The task composer, shared by the home, the task page, the project page and the phone: a 22px-radius card with a 50px editor, a + button, connector chips, the Manus Desktop chip, and the microphone and send buttons. The disclaimer sits under it on a task.

#### Composer

<a id="composer"></a>`composer`, on home-dark, home-dark-composer-typed, task-dark-completed. 768 wide, radius from --ui-density-composer-radius, --background-menu-white fill; a 50 tall editor above a 32px tool row.

<img src="components/crops/composer-default.png" alt="Composer, default" height="120"> <img src="components/crops/composer-light.png" alt="Composer, light" height="120"> <img src="components/crops/composer-typed.png" alt="Composer, typed" height="120"> <img src="components/crops/composer-focus-visible.png" alt="Composer, focus-visible" height="120"> 

| State | Values |
|---|---|
| default | size 768 x 120; padding `space.3` (12px) 0px; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.composer` (22px); background `background.menu-white` (#242424); shadow `elevation.composer` (rgba(0, 0, 0, 0.02) 0px 12px 32px 0px); text System 14/18 400, `≈ icon.secondary` (#b3b3b3); icon 17 x 17, `≈ icon.secondary` (#b3b3b3); placeholder `≈ text.tertiary` (#8c8c8c) |
| focus-visible | border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)) |
| typed | text `typography.role.body-long` (System 16/24 400), `≈ icon.primary` (#e6e6e6); placeholder none |
| task | text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c) |
| light | size 768 x 120; padding `space.3` (12px) 0px; border `borderWidth.default` (1px) solid #e5e7eb; radius `radius.composer` (22px); background `background.menu-white` (#ffffff); shadow `elevation.composer` (rgba(0, 0, 0, 0.02) 0px 12px 32px 0px); text System 14/18 400, `≈ icon.secondary` (#4d4d4d); icon 17 x 17, `≈ icon.secondary` (#4d4d4d); placeholder `≈ text.tertiary` (#737373) |
| light-focus-visible | border `borderWidth.default` (1px) solid `≈ gradient.dark-20` (rgba(0, 0, 0, 0.2)) |
| light-typed | text `typography.role.body-long` (System 16/24 400), `≈ icon.primary` (#1a1a1a); placeholder none |
| light-task | text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--accent-send-button`, `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-primary`, `--icon-secondary`, `--text-onblack`, `--text-primary`, `--text-secondary`, `--text-tertiary`, `--ui-density-composer-radius`, `--ui-density-content-padding`, `--ui-density-home-input-editor-min-height`, `--ui-density-outer-padding`, `--ui-density-row-gap`, `--ui-density-section-gap`, `--ui-density-small-row-height`.

#### Composer placeholder

<a id="composer-placeholder"></a>`composer-placeholder`, on home-dark. Tiptap draws it with p.is-editor-empty::before from data-placeholder.

<img src="components/crops/composer-placeholder-default.png" alt="Composer placeholder, default" height="24"> <img src="components/crops/composer-placeholder-light.png" alt="Composer placeholder, light" height="24"> 

| State | Values |
|---|---|
| default | size 742 x 24; background transparent; placeholder `≈ text.tertiary` (#8c8c8c) |
| light | size 742 x 24; background transparent; placeholder `≈ text.tertiary` (#737373) |

#### Composer typed text

<a id="composer-text"></a>`composer-text`, on home-dark-composer-typed.

<img src="components/crops/composer-text-default.png" alt="Composer typed text, default" height="24"> <img src="components/crops/composer-text-light.png" alt="Composer typed text, light" height="24"> 

| State | Values |
|---|---|
| default | size 742 x 24; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| light | size 742 x 24; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |

#### Composer + button

<a id="composer-plus"></a>`composer-plus`, on home-dark, home-dark-attach-menu. A 32px circle with a 1px --border-main ring.

<img src="components/crops/composer-plus-default.png" alt="Composer + button, default" height="32"> <img src="components/crops/composer-plus-hover.png" alt="Composer + button, hover" height="32"> <img src="components/crops/composer-plus-light.png" alt="Composer + button, light" height="32"> <img src="components/crops/composer-plus-light-hover.png" alt="Composer + button, light-hover" height="32"> <img src="components/crops/composer-plus-open.png" alt="Composer + button, open" height="32"> <img src="components/crops/composer-plus-focus-visible.png" alt="Composer + button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 32 x `size.row-small` (32px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.full` (9999px); background transparent; icon 17 x 17, `≈ text.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| open | border none; background `≈ fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-focus-visible) | size 32 x `size.row-small` (32px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.full` (9999px); background transparent; icon 17 x 17, `≈ text.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-open | border none; background `≈ fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-secondary`, `--ui-density-small-row-height`.

#### Connector chips button

<a id="composer-connectors"></a>`composer-connectors`, on home-dark. Overlapping 16px app icons in a pill.

<img src="components/crops/composer-connectors-default.png" alt="Connector chips button, default" height="32"> <img src="components/crops/composer-connectors-hover.png" alt="Connector chips button, hover" height="32"> <img src="components/crops/composer-connectors-light.png" alt="Connector chips button, light" height="32"> <img src="components/crops/composer-connectors-light-hover.png" alt="Connector chips button, light-hover" height="32"> <img src="components/crops/composer-connectors-focus-visible.png" alt="Connector chips button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 72 x `size.row-small` (32px); padding `space.2` (8px); radius 100px; background transparent; outline `focusRing.input-width` (1px) solid `≈ border.main` (rgba(255, 255, 255, 0.06)), offset -1px; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover, pressed | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 72 x `size.row-small` (32px); padding `space.2` (8px); radius 100px; background transparent; outline `focusRing.input-width` (1px) solid `≈ border.main` (rgba(0, 0, 0, 0.06)), offset -1px; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover, light-pressed | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 72x32 radius 100px

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-outer-padding`, `--ui-density-small-row-height`.

#### Manus Desktop chip

<a id="composer-desktop-chip"></a>`composer-desktop-chip`, on home-dark.

<img src="components/crops/composer-desktop-chip-default.png" alt="Manus Desktop chip, default" height="32"> <img src="components/crops/composer-desktop-chip-hover.png" alt="Manus Desktop chip, hover" height="32"> <img src="components/crops/composer-desktop-chip-light.png" alt="Manus Desktop chip, light" height="32"> <img src="components/crops/composer-desktop-chip-light-hover.png" alt="Manus Desktop chip, light-hover" height="32"> <img src="components/crops/composer-desktop-chip-focus-visible.png" alt="Manus Desktop chip, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 136.52 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.full` (9999px); background transparent; outline `focusRing.input-width` (1px) solid `≈ border.main` (rgba(255, 255, 255, 0.06)), offset -1px; text System 14/18 400, `≈ icon.secondary` (#b3b3b3); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| hover, pressed | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 136.52 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.full` (9999px); background transparent; outline `focusRing.input-width` (1px) solid `≈ border.main` (rgba(0, 0, 0, 0.06)), offset -1px; text System 14/18 400, `≈ icon.secondary` (#4d4d4d); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |
| light-hover, light-pressed | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 136.5x32 radius 9999px

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--icon-primary`, `--icon-secondary`, `--text-secondary`, `--ui-density-small-row-height`.

#### Composer agent-mode icon button

<a id="composer-skill-button"></a>`composer-skill-button`, on home-dark.

<img src="components/crops/composer-skill-button-default.png" alt="Composer agent-mode icon button, default" height="32"> <img src="components/crops/composer-skill-button-hover.png" alt="Composer agent-mode icon button, hover" height="32"> <img src="components/crops/composer-skill-button-light.png" alt="Composer agent-mode icon button, light" height="32"> <img src="components/crops/composer-skill-button-light-hover.png" alt="Composer agent-mode icon button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.full` (9999px); background transparent; icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.full` (9999px); background transparent; icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`.

#### Composer microphone button

<a id="composer-mic"></a>`composer-mic`, on home-dark.

<img src="components/crops/composer-mic-default.png" alt="Composer microphone button, default" height="32"> <img src="components/crops/composer-mic-hover.png" alt="Composer microphone button, hover" height="32"> <img src="components/crops/composer-mic-light.png" alt="Composer microphone button, light" height="32"> <img src="components/crops/composer-mic-light-hover.png" alt="Composer microphone button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.full` (9999px); background transparent; icon `size.icon-small` (16 x 16), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); radius `radius.full` (9999px); background transparent; icon `size.icon-small` (16 x 16), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`, `--ui-density-small-row-height`.

#### Composer send button

<a id="composer-send"></a>`composer-send`, on home-dark, home-dark-composer-typed. Disabled (opacity 0.5) while the composer is empty; `enabled` once text is typed.

<img src="components/crops/composer-send-default.png" alt="Composer send button, default" height="32"> <img src="components/crops/composer-send-light.png" alt="Composer send button, light" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.full` (9999px); background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 15 x 15, `≈ text.onblack` (rgba(0, 0, 0, 0.9)) |
| enabled | background `accent.send-button` (rgba(255, 255, 255, 0.95)) |
| enabled-hover | background `accent.send-button` (rgba(255, 255, 255, 0.95)); opacity `opacity.hover` (0.9) |
| enabled-focus-visible | background `accent.send-button` (rgba(255, 255, 255, 0.95)) |
| light | size 32 x `size.row-small` (32px); radius `radius.full` (9999px); background `≈ fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 15 x 15, `≈ text.onblack` (#ffffff) |
| light-enabled | background `accent.send-button` (#1a1a19) |
| light-enabled-hover | background `accent.send-button` (#1a1a19); opacity `opacity.hover` (0.9) |
| light-enabled-focus-visible | background `accent.send-button` (#1a1a19) |

Tokens named in its classes: `--accent-send-button`, `--fill-tsp-white-dark`, `--text-onblack`, `--ui-density-small-row-height`.

#### Footer disclaimer

<a id="disclaimer"></a>`disclaimer`, on task-dark-completed. Present but `invisible` on the home page; shown under the composer on a task.

<img src="components/crops/disclaimer-default.png" alt="Footer disclaimer, default" height="24"> <img src="components/crops/disclaimer-light.png" alt="Footer disclaimer, light" height="24"> 

| State | Values |
|---|---|
| default | size 768 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#8c8c8c) |
| light | size 768 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

### Menus and dialogs

The popovers and dialogs: the model menu, the + attach menu, the search dialog, the notifications panel, the account menu, the Library's row menu and view options, the sidebar's task menu and project context menu, the More menu, the files dialog, the previewer's and settings' dialogs. All share the 12px radius card on `--background-menu-white` with a hairline border.

#### Model menu

<a id="model-menu"></a>`model-menu`, on home-dark-model-menu. 366 wide, 4px padding, --background-menu-white, shadow-menu, a 40px backdrop blur.

<img src="components/crops/model-menu-default.png" alt="Model menu, default" height="120"> <img src="components/crops/model-menu-light.png" alt="Model menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 366 x 232; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); backdrop blur(40px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| light | size 366 x 232; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); backdrop blur(40px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--available-width`, `--background-menu-white`, `--border-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Model menu item

<a id="model-menu-item"></a>`model-menu-item`, on home-dark-model-menu. Title 14/20 with a serif Pro badge, a 12px description in --text-tertiary. The current model carries a check (`checked`).

<img src="components/crops/model-menu-item-default.png" alt="Model menu item, default" height="52"> <img src="components/crops/model-menu-item-hover.png" alt="Model menu item, hover" height="52"> <img src="components/crops/model-menu-item-light.png" alt="Model menu item, light" height="52"> <img src="components/crops/model-menu-item-light-hover.png" alt="Model menu item, light-hover" height="52"> <img src="components/crops/model-menu-item-checked.png" alt="Model menu item, checked" height="52"> 

| State | Values |
|---|---|
| default | size 358 x 52; padding `space.2` (8px) `space.2` (8px) `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); transition background-color `duration.fast` (0.15s) cubic-bezier(0, 0, 0.2, 1) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| checked | icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| checked-hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| light | size 358 x 52; padding `space.2` (8px) `space.2` (8px) `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); transition background-color `duration.fast` (0.15s) cubic-bezier(0, 0, 0.2, 1) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-checked | icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-checked-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |

Child layers: div 34.5x18 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 5px

Tokens named in its classes: `--border-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`, `--text-tertiary`.

#### Pro badge

<a id="model-menu-pro-badge"></a>`model-menu-pro-badge`, on home-dark-model-menu.

<img src="components/crops/model-menu-pro-badge-default.png" alt="Pro badge, default" height="24"> <img src="components/crops/model-menu-pro-badge-light.png" alt="Pro badge, light" height="24"> 

| State | Values |
|---|---|
| default | size 34.45 x 18; padding 1px `space.1_5` (6px); radius 5px; background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text Libre Baskerville 12/16 700, `text.primary` (#e6e6e6) |
| light | size 34.45 x 18; padding 1px `space.1_5` (6px); radius 5px; background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text Libre Baskerville 12/16 700, `text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`.

#### Beta badge

<a id="model-menu-beta-badge"></a>`model-menu-beta-badge`, on home-dark-model-menu.

<img src="components/crops/model-menu-beta-badge-default.png" alt="Beta badge, default" height="24"> <img src="components/crops/model-menu-beta-badge-light.png" alt="Beta badge, light" height="24"> 

| State | Values |
|---|---|
| default | size 40.34 x 18; padding 0px `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px) `radius.row` (10px) `radius.row` (10px) 0px; background transparent; text System 12/16 500, `text.tertiary` (#8c8c8c) |
| light | size 40.34 x 18; padding 0px `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.small` (8px) `radius.row` (10px) `radius.row` (10px) 0px; background transparent; text System 12/16 500, `text.tertiary` (#737373) |

Tokens named in its classes: `--border-dark`, `--text-tertiary`.

#### Attach (+) menu

<a id="attach-menu"></a>`attach-menu`, on home-dark-attach-menu.

<img src="components/crops/attach-menu-default.png" alt="Attach (+) menu, default" height="120"> <img src="components/crops/attach-menu-light.png" alt="Attach (+) menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 198.88 x 269; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 198.88 x 269; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Menu item (attach menu)

<a id="menu-item"></a>`menu-item`, on home-dark-attach-menu. The shared menu row: 36 tall, 8px horizontal padding, an icon then 14px text, radius 8, hover --fill-tsp-white-main.

<img src="components/crops/menu-item-default.png" alt="Menu item (attach menu), default" height="36"> <img src="components/crops/menu-item-hover.png" alt="Menu item (attach menu), hover" height="36"> <img src="components/crops/menu-item-light.png" alt="Menu item (attach menu), light" height="36"> <img src="components/crops/menu-item-light-hover.png" alt="Menu item (attach menu), light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 190.88 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 190.88 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Menu divider

<a id="menu-divider"></a>`menu-divider`, on home-dark-attach-menu.

<img src="components/crops/menu-divider-default.png" alt="Menu divider, default" height="24"> <img src="components/crops/menu-divider-light.png" alt="Menu divider, light" height="24"> 

| State | Values |
|---|---|
| default | size 166.88 x 1; background `border.main` (rgba(255, 255, 255, 0.06)) |
| light | size 166.88 x 1; background `border.main` (rgba(0, 0, 0, 0.06)) |

Tokens named in its classes: `--border-main`.

#### Search tasks dialog

<a id="search-dialog"></a>`search-dialog`, on home-dark-search. 680 wide, centred, over a transparent overlay (no dim).

| State | Values |
|---|---|
| default | size 680 x 440; radius 20px; background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6); placeholder `≈ icon.tertiary` (#8c8c8c) |
| light | size 680 x 440; radius 20px; background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a); placeholder `≈ icon.tertiary` (#737373) |

Tokens named in its classes: `--background-menu-white`, `--border-dark`, `--border-main`, `--dlg-enter-scale`, `--dlg-enter-y`, `--fill-tsp-white-light`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`.

#### Search dialog field row

<a id="search-input"></a>`search-input`, on home-dark-search.

<img src="components/crops/search-input-default.png" alt="Search dialog field row, default" height="67"> <img src="components/crops/search-input-light.png" alt="Search dialog field row, light" height="67"> <img src="components/crops/search-input-focus-visible.png" alt="Search dialog field row, focus-visible" height="67"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 680 x 67; padding `space.5` (20px) `space.3` (12px) 18px `space.5` (20px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); background transparent; icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6); placeholder `≈ icon.tertiary` (#8c8c8c) |
| light (same: light-focus-visible) | size 680 x 67; padding `space.5` (20px) `space.3` (12px) 18px `space.5` (20px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); background transparent; icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a); placeholder `≈ icon.tertiary` (#737373) |

Child layers: h3 680x67 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06))

Tokens named in its classes: `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`.

#### Search result row

<a id="search-result"></a>`search-result`, on home-dark-search.

| State | Values |
|---|---|
| default | size 664 x 52; padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| selected | size 664 x `size.row` (36px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| light | size 664 x 52; padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-selected | size 664 x `size.row` (36px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Search group label (Older)

<a id="search-group-label"></a>`search-group-label`, on home-dark-search.

<img src="components/crops/search-group-label-default.png" alt="Search group label (Older), default" height="40"> <img src="components/crops/search-group-label-light.png" alt="Search group label (Older), light" height="40"> 

| State | Values |
|---|---|
| default | size 680 x 39.5; padding `space.3` (12px) `space.5` (20px) `space.2` (8px) `space.5` (20px); background transparent; text System 13/19.5 500, `text.tertiary` (#8c8c8c) |
| light | size 680 x 39.5; padding `space.3` (12px) `space.5` (20px) `space.2` (8px) `space.5` (20px); background transparent; text System 13/19.5 500, `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

#### Notifications popover

<a id="notifications-panel"></a>`notifications-panel`, on home-dark-notifications. 400x600, radius 12, a 0.5px border, the All/Updates/Messages tabs, then entries split by rules.

<img src="components/crops/notifications-panel-default.png" alt="Notifications popover, default" height="120"> <img src="components/crops/notifications-panel-light.png" alt="Notifications popover, light" height="120"> 

| State | Values |
|---|---|
| default | size 400 x 600; border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.panel` (rgba(0, 0, 0, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 4px 32px 0px); backdrop blur(40px); text `typography.title-lg` (System 18/24 500), `≈ text.primary` (#e6e6e6); icon 60 x 60, `≈ text.primary` (#e6e6e6) |
| light | size 400 x 600; border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.panel` (rgba(0, 0, 0, 0.02) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 4px 32px 0px); backdrop blur(40px); text `typography.title-lg` (System 18/24 500), `≈ text.primary` (#1a1a1a); icon 60 x 60, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-mask-black`, `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-black`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--shadow-S`, `--shadow-XS`, `--simplebar-scrollbar-width`, `--text-disable`, `--text-primary`, `--text-tertiary`.

#### Notification entry

<a id="notification-item"></a>`notification-item`, on home-dark-notifications.

<img src="components/crops/notification-item-default.png" alt="Notification entry, default" height="120"> <img src="components/crops/notification-item-light.png" alt="Notification entry, light" height="120"> 

| State | Values |
|---|---|
| default | size 366 x 364.88; padding `space.4` (16px) 0px; border B: `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon 60 x 60, `≈ text.primary` (#e6e6e6) |
| light | size 366 x 364.88; padding `space.4` (16px) 0px; border B: `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon 60 x 60, `≈ text.primary` (#1a1a1a) |

Child layers: div 366x364.9 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)); svg 60x60 background `≈ fill.black` (rgba(40, 40, 41, 0.45)) radius 9999px

Tokens named in its classes: `--background-mask-black`, `--border-main`, `--fill-black`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Tooltip

<a id="tooltip"></a>`tooltip`, on home-dark-notifications.

<img src="components/crops/tooltip-default.png" alt="Tooltip, default" height="24"> <img src="components/crops/tooltip-light.png" alt="Tooltip, light" height="24"> 

| State | Values |
|---|---|
| default | size 87.67 x 24; padding `space.1` (4px) `space.2` (8px); radius `radius.small` (8px); background `background.menu-tooltips` (rgba(0, 0, 0, 0.9)); text `typography.role.caption` (System 12/16 400), `text.white` (#ffffff) |
| light | size 87.67 x 24; padding `space.1` (4px) `space.2` (8px); radius `radius.small` (8px); background `background.menu-tooltips` (rgba(0, 0, 0, 0.9)); text `typography.role.caption` (System 12/16 400), `text.white` (#ffffff) |

Tokens named in its classes: `--background-menu-tooltips`, `--text-white`.

#### View options menu

<a id="view-options-menu"></a>`view-options-menu`, on library-dark-images-grid-view-options. 192 wide; a 13px grey heading, then Group by task and Favorites only. No item carries a check in this capture.

<img src="components/crops/view-options-menu-default.png" alt="View options menu, default" height="112"> <img src="components/crops/view-options-menu-light.png" alt="View options menu, light" height="112"> 

| State | Values |
|---|---|
| default | size 192 x 111.5; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.shortcut` (System 13/19.5 400), `≈ text.tertiary` (#8c8c8c); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 192 x 111.5; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.shortcut` (System 13/19.5 400), `≈ text.tertiary` (#737373); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--fill-tsp-white-main`, `--text-primary`, `--text-tertiary`, `--ui-density-menu-item-padding-y`.

#### View options item

<a id="view-options-item"></a>`view-options-item`, on library-dark-images-grid-view-options.

<img src="components/crops/view-options-item-default.png" alt="View options item, default" height="36"> <img src="components/crops/view-options-item-hover.png" alt="View options item, hover" height="36"> <img src="components/crops/view-options-item-light.png" alt="View options item, light" height="36"> <img src="components/crops/view-options-item-light-hover.png" alt="View options item, light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: second) | size 184 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light (same: light-second) | size 184 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Library row menu

<a id="row-menu"></a>`row-menu`, on library-dark-row-menu. 280 min width; Download, Save to, Share, a divider, Locate in task, Add to favorites, Send to Manus.

<img src="components/crops/row-menu-default.png" alt="Library row menu, default" height="120"> <img src="components/crops/row-menu-light.png" alt="Library row menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 280 x 229; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 280 x 229; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Library row menu item

<a id="row-menu-item"></a>`row-menu-item`, on library-dark-row-menu.

<img src="components/crops/row-menu-item-default.png" alt="Library row menu item, default" height="36"> <img src="components/crops/row-menu-item-hover.png" alt="Library row menu item, hover" height="36"> <img src="components/crops/row-menu-item-light.png" alt="Library row menu item, light" height="36"> <img src="components/crops/row-menu-item-light-hover.png" alt="Library row menu item, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 272 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 272 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Account menu

<a id="user-menu"></a>`user-menu`, on library-dark-user-menu. 284 wide, opening above the account row.

<img src="components/crops/user-menu-default.png" alt="Account menu, default" height="120"> <img src="components/crops/user-menu-light.png" alt="Account menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 284 x 418; radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| light | size 284 x 418; radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--Button-black`, `--background-menu-white`, `--border-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-onblack`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Account menu header (avatar, name, workspace)

<a id="user-menu-header"></a>`user-menu-header`, on library-dark-user-menu.

<img src="components/crops/user-menu-header-default.png" alt="Account menu header (avatar, name, workspace), default" height="52"> <img src="components/crops/user-menu-header-hover.png" alt="Account menu header (avatar, name, workspace), hover" height="52"> <img src="components/crops/user-menu-header-light.png" alt="Account menu header (avatar, name, workspace), light" height="52"> <img src="components/crops/user-menu-header-light-hover.png" alt="Account menu header (avatar, name, workspace), light-hover" height="52"> 

| State | Values |
|---|---|
| default | size 276 x 52; padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 276 x 52; padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Child layers: div 28x28 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 9999px; div 26x26 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08))

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Account menu plan card

<a id="user-menu-plan"></a>`user-menu-plan`, on library-dark-user-menu.

<img src="components/crops/user-menu-plan-default.png" alt="Account menu plan card, default" height="80"> <img src="components/crops/user-menu-plan-light.png" alt="Account menu plan card, light" height="80"> 

| State | Values |
|---|---|
| default | size 276 x 80; radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text Libre Baskerville 14/20 700, `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 276 x 80; radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text Libre Baskerville 14/20 700, `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-black`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-onblack`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Account menu Upgrade button

<a id="user-menu-upgrade"></a>`user-menu-upgrade`, on library-dark-user-menu.

<img src="components/crops/user-menu-upgrade-default.png" alt="Account menu Upgrade button, default" height="28"> <img src="components/crops/user-menu-upgrade-hover.png" alt="Account menu Upgrade button, hover" height="28"> <img src="components/crops/user-menu-upgrade-light.png" alt="Account menu Upgrade button, light" height="28"> <img src="components/crops/user-menu-upgrade-light-hover.png" alt="Account menu Upgrade button, light-hover" height="28"> <img src="components/crops/user-menu-upgrade-focus-visible.png" alt="Account menu Upgrade button, focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 68.95 x `size.control-small` (28px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text System 13/18 500 tracking -0.08px, `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 68.95 x `size.control-small` (28px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (#1a1a19); text System 13/18 500 tracking -0.08px, `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`, `--ui-density-small-row-height`.

#### Account menu item

<a id="user-menu-item"></a>`user-menu-item`, on library-dark-user-menu. Hover also shows the shortcut hint (⌘⇧,).

<img src="components/crops/user-menu-item-default.png" alt="Account menu item, default" height="36"> <img src="components/crops/user-menu-item-hover.png" alt="Account menu item, hover" height="36"> <img src="components/crops/user-menu-item-light.png" alt="Account menu item, light" height="36"> <img src="components/crops/user-menu-item-light-hover.png" alt="Account menu item, light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: link, link-focus-visible) | size 276 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-link, light-link-focus-visible) | size 276 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Project context menu

<a id="context-menu"></a>`context-menu`, on plugins-dark-project-context-menu.

<img src="components/crops/context-menu-default.png" alt="Project context menu, default" height="116"> <img src="components/crops/context-menu-light.png" alt="Project context menu, light" height="116"> 

| State | Values |
|---|---|
| default | size 132.33 x 116; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 132.33 x 116; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--fill-tsp-white-main`, `--function-error`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Context menu Delete item

<a id="context-menu-item-danger"></a>`context-menu-item-danger`, on plugins-dark-project-context-menu.

<img src="components/crops/context-menu-item-danger-default.png" alt="Context menu Delete item, default" height="36"> <img src="components/crops/context-menu-item-danger-hover.png" alt="Context menu Delete item, hover" height="36"> <img src="components/crops/context-menu-item-danger-light.png" alt="Context menu Delete item, light" height="36"> <img src="components/crops/context-menu-item-danger-light-hover.png" alt="Context menu Delete item, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 124.33 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.error` (#eb4d4d); icon `size.icon-small` (16 x 16), `≈ function.error` (#eb4d4d) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 124.33 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.error` (#fb494f); icon `size.icon-small` (16 x 16), `≈ function.error` (#fb494f) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--function-error`, `--ui-density-menu-item-padding-y`.

#### Sidebar More menu

<a id="more-menu"></a>`more-menu`, on plugins-dark-more-menu. The one menu on --background-menu-gray rather than --background-menu-white.

<img src="components/crops/more-menu-default.png" alt="Sidebar More menu, default" height="116"> <img src="components/crops/more-menu-light.png" alt="Sidebar More menu, light" height="116"> 

| State | Values |
|---|---|
| default | size 190 x 116; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-gray` (#1a1a1a); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 190 x 116; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-gray` (#f8f8f7); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-gray`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Sidebar More menu item

<a id="more-menu-item"></a>`more-menu-item`, on plugins-dark-more-menu.

<img src="components/crops/more-menu-item-default.png" alt="Sidebar More menu item, default" height="36"> <img src="components/crops/more-menu-item-hover.png" alt="Sidebar More menu item, hover" height="36"> <img src="components/crops/more-menu-item-light.png" alt="Sidebar More menu item, light" height="36"> <img src="components/crops/more-menu-item-light-hover.png" alt="Sidebar More menu item, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 182 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 182 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Sidebar task menu

<a id="task-menu"></a>`task-menu`, on task-dark-sidebar-task-menu.

<img src="components/crops/task-menu-default.png" alt="Sidebar task menu, default" height="120"> <img src="components/crops/task-menu-light.png" alt="Sidebar task menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 200 x 424; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 200 x 424; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Sidebar task menu Delete item

<a id="task-menu-item-danger"></a>`task-menu-item-danger`, on task-dark-sidebar-task-menu.

<img src="components/crops/task-menu-item-danger-default.png" alt="Sidebar task menu Delete item, default" height="36"> <img src="components/crops/task-menu-item-danger-hover.png" alt="Sidebar task menu Delete item, hover" height="36"> <img src="components/crops/task-menu-item-danger-light.png" alt="Sidebar task menu Delete item, light" height="36"> <img src="components/crops/task-menu-item-danger-light-hover.png" alt="Sidebar task menu Delete item, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 192 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.error` (#eb4d4d); icon `size.icon-small` (16 x 16), `≈ function.error` (#eb4d4d) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 192 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.error` (#fb494f); icon `size.icon-small` (16 x 16), `≈ function.error` (#fb494f) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--function-error`, `--ui-density-menu-item-padding-y`.

#### Files in this task dialog

<a id="files-dialog"></a>`files-dialog`, on task-dark-files-dialog. 600x680, radius 16, --background-gray-main over --background-dialog-mask with a 4px blur.

| State | Values |
|---|---|
| default | size 600 x 680; radius `radius.dialog` (16px); background `background.gray-main` (#1a1a1a); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text System 18/28 600, `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `icon.secondary` (#b3b3b3) |
| light | size 600 x 680; radius `radius.dialog` (16px); background `background.gray-main` (#f8f8f7); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text System 18/28 600, `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `icon.secondary` (#4d4d4d) |

Tokens named in its classes: `--background-gray-main`, `--dlg-enter-scale`, `--dlg-enter-y`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-secondary`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Files dialog file row

<a id="files-dialog-row"></a>`files-dialog-row`, on task-dark-files-dialog.

| State | Values |
|---|---|
| default | size 576 x 56; padding `space.2_5` (10px) `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 32 x 32, `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 576 x 56; padding `space.2_5` (10px) `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 32 x 32, `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`.

#### Dialog backdrop

<a id="dialog-mask"></a>`dialog-mask`, on task-dark-files-dialog.

| State | Values |
|---|---|
| default | size 1440 x 900; background `background.dialog-mask` (rgba(0, 0, 0, 0.6)); backdrop blur(4px) |
| light | size 1440 x 900; background `background.dialog-mask` (rgba(0, 0, 0, 0.3)); backdrop blur(4px) |

Tokens named in its classes: `--background-dialog-mask`.

#### Dialog close button (files dialog)

<a id="dialog-close"></a>`dialog-close`, on task-dark-files-dialog.

<img src="components/crops/dialog-close-default.png" alt="Dialog close button (files dialog), default" height="32"> <img src="components/crops/dialog-close-hover.png" alt="Dialog close button (files dialog), hover" height="32"> <img src="components/crops/dialog-close-light.png" alt="Dialog close button (files dialog), light" height="32"> <img src="components/crops/dialog-close-light-hover.png" alt="Dialog close button (files dialog), light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 32 x `size.row-small` (32px); radius `radius.md` (6px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`, `--ui-density-small-row-height`.

### Library

The file library: the title bar with search, view options and the grid/list control, the strip of type tabs, then groups by day (or by task) of rows and grid cards.

#### Page title (h1)

<a id="page-title"></a>`page-title`, on library-dark. 18/24 500 in --text-primary, in a 112 tall header band.

<img src="components/crops/page-title-default.png" alt="Page title (h1), default" height="24"> <img src="components/crops/page-title-light.png" alt="Page title (h1), light" height="24"> 

| State | Values |
|---|---|
| default | size 57.63 x 24; background transparent; text `typography.title-lg` (System 18/24 500), `text.primary` (#e6e6e6) |
| light | size 57.63 x 24; background transparent; text `typography.title-lg` (System 18/24 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Search field

<a id="library-search"></a>`library-search`, on library-dark.

<img src="components/crops/library-search-default.png" alt="Search field, default" height="32"> <img src="components/crops/library-search-hover.png" alt="Search field, hover" height="32"> <img src="components/crops/library-search-light.png" alt="Search field, light" height="32"> <img src="components/crops/library-search-light-hover.png" alt="Search field, light-hover" height="32"> <img src="components/crops/library-search-focus-visible.png" alt="Search field, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 240 x `size.row-small` (32px); padding `space.1` (4px) `space.1_5` (6px) `space.1` (4px) `space.3` (12px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| light (same: light-hover, light-focus-visible) | size 240 x `size.row-small` (32px); padding `space.1` (4px) `space.1_5` (6px) `space.1` (4px) `space.3` (12px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--Button-border-secondary`, `--text-disable`, `--text-primary`, `--ui-density-input-gap`, `--ui-density-small-radius`.

#### View options button

<a id="view-options-button"></a>`view-options-button`, on library-dark.

<img src="components/crops/view-options-button-default.png" alt="View options button, default" height="32"> <img src="components/crops/view-options-button-hover.png" alt="View options button, hover" height="32"> <img src="components/crops/view-options-button-light.png" alt="View options button, light" height="32"> <img src="components/crops/view-options-button-light-hover.png" alt="View options button, light-hover" height="32"> <img src="components/crops/view-options-button-focus-visible.png" alt="View options button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 32 x `size.row-small` (32px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light (same: light-focus-visible) | size 32 x `size.row-small` (32px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-main`, `--icon-secondary`.

#### Grid/list segmented control

<a id="view-toggle"></a>`view-toggle`, on library-dark. 68x32, radius 8, 1px --border-main, --fill-tsp-gray-main; a white thumb (radius 6, a 0.5px-offset shadow) slides under the active option.

<img src="components/crops/view-toggle-default.png" alt="Grid/list segmented control, default" height="32"> <img src="components/crops/view-toggle-light.png" alt="Grid/list segmented control, light" height="32"> 

| State | Values |
|---|---|
| default | size 68 x `size.row-small` (32px); padding 1px; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.small` (8px); background `fill.tsp-gray-main` (rgba(0, 0, 0, 0.2)); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| light | size 68 x `size.row-small` (32px); padding 1px; border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.small` (8px); background `fill.tsp-gray-main` (rgba(55, 53, 47, 0.04)); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--border-main`, `--fill-tsp-gray-main`, `--fill-white`, `--shadow-S`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Segmented control option

<a id="view-toggle-option"></a>`view-toggle-option`, on library-dark.

<img src="components/crops/view-toggle-option-default.png" alt="Segmented control option, default" height="28"> <img src="components/crops/view-toggle-option-hover.png" alt="Segmented control option, hover" height="28"> <img src="components/crops/view-toggle-option-light.png" alt="Segmented control option, light" height="28"> <img src="components/crops/view-toggle-option-light-hover.png" alt="Segmented control option, light-hover" height="28"> <img src="components/crops/view-toggle-option-active.png" alt="Segmented control option, active" height="28"> <img src="components/crops/view-toggle-option-focus-visible.png" alt="Segmented control option, focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 32 x `size.control-small` (28px); padding 0px `space.2` (8px); background transparent; transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| hover | icon `size.icon-small` (16 x 16), `≈ text.secondary` (#b3b3b3) |
| active | icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 32 x `size.control-small` (28px); padding 0px `space.2` (8px); background transparent; transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |
| light-hover | icon `size.icon-small` (16 x 16), `≈ text.secondary` (#4d4d4d) |
| light-active | icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Segmented control thumb

<a id="view-toggle-thumb"></a>`view-toggle-thumb`, on library-dark.

<img src="components/crops/view-toggle-thumb-default.png" alt="Segmented control thumb, default" height="28"> <img src="components/crops/view-toggle-thumb-light.png" alt="Segmented control thumb, light" height="28"> 

| State | Values |
|---|---|
| default | size 32 x `size.control-small` (28px); radius `radius.md` (6px); background `fill.white` (#242424); shadow rgba(0, 0, 0, 0.16) 0px 0.5px 3px 0px |
| light | size 32 x `size.control-small` (28px); radius `radius.md` (6px); background `fill.white` (#ffffff); shadow rgba(0, 0, 0, 0.04) 0px 0.5px 3px 0px |

Tokens named in its classes: `--fill-white`, `--shadow-S`.

#### Type tab

<a id="type-tab"></a>`type-tab`, on library-dark. 32 tall, radius 8, 14px; the label is drawn twice (a hidden 500-weight copy reserves the width, so selecting does not shift the row).

<img src="components/crops/type-tab-default.png" alt="Type tab, default" height="32"> <img src="components/crops/type-tab-hover.png" alt="Type tab, hover" height="32"> <img src="components/crops/type-tab-light.png" alt="Type tab, light" height="32"> <img src="components/crops/type-tab-light-hover.png" alt="Type tab, light-hover" height="32"> <img src="components/crops/type-tab-selected.png" alt="Type tab, selected" height="32"> <img src="components/crops/type-tab-focus-visible.png" alt="Type tab, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 92.17 x `size.row-small` (32px); padding 0px `space.2_5` (10px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.tertiary` (#8c8c8c); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| selected, selected-hover | size 48 x `size.row-small` (32px); background `fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 92.17 x `size.row-small` (32px); padding 0px `space.2_5` (10px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.tertiary` (#737373); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-selected, light-selected-hover | size 48 x `size.row-small` (32px); background `fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-tertiary`.

#### Date group heading with count

<a id="date-heading"></a>`date-heading`, on library-dark.

<img src="components/crops/date-heading-default.png" alt="Date group heading with count, default" height="24"> <img src="components/crops/date-heading-light.png" alt="Date group heading with count, light" height="24"> 

| State | Values |
|---|---|
| default | size 59.67 x 20; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| light | size 59.67 x 20; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`, `--text-tertiary`.

#### File list row

<a id="file-row"></a>`file-row`, on library-dark. 67 tall; the hover fill extends 12px past the column on both sides (radius 8); a 1px --border-main rule under the inner row.

| State | Values |
|---|---|
| default | size 1024 x 67; padding 0px `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 1024 x 67; padding 0px `space.3` (12px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Child layers: div 1000x67 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06))

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### File row icon

<a id="file-row-icon"></a>`file-row-icon`, on library-dark.

<img src="components/crops/file-row-icon-default.png" alt="File row icon, default" height="24"> <img src="components/crops/file-row-icon-light.png" alt="File row icon, light" height="24"> 

| State | Values |
|---|---|
| default | size 24 x 24; background transparent; icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| light | size 24 x 24; background transparent; icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |

#### File row title

<a id="file-row-title"></a>`file-row-title`, on library-dark.

| State | Values |
|---|---|
| default | size 493.38 x 17; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| light | size 493.38 x 17; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |

#### File row source task

<a id="file-row-source"></a>`file-row-source`, on library-dark.

| State | Values |
|---|---|
| default | size 331.67 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#8c8c8c) |
| light | size 331.67 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

#### File row time

<a id="file-row-time"></a>`file-row-time`, on library-dark.

<img src="components/crops/file-row-time-default.png" alt="File row time, default" height="24"> <img src="components/crops/file-row-time-light.png" alt="File row time, light" height="24"> 

| State | Values |
|---|---|
| default | size 55.11 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#8c8c8c) |
| light | size 55.11 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

#### File row more button

<a id="file-row-menu"></a>`file-row-menu`, on library-dark, library-dark-row-menu.

<img src="components/crops/file-row-menu-default.png" alt="File row more button, default" height="32"> <img src="components/crops/file-row-menu-hover.png" alt="File row more button, hover" height="32"> <img src="components/crops/file-row-menu-light.png" alt="File row more button, light" height="32"> <img src="components/crops/file-row-menu-light-hover.png" alt="File row more button, light-hover" height="32"> <img src="components/crops/file-row-menu-open.png" alt="File row more button, open" height="32"> <img src="components/crops/file-row-menu-focus-visible.png" alt="File row more button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 32 x `size.row-small` (32px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| open | background `≈ fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-focus-visible) | size 32 x `size.row-small` (32px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-open | background `≈ fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`.

#### Grid card

<a id="grid-card"></a>`grid-card`, on library-dark-images-grid. 323x258, radius 12, a 0.5px --border-dark hairline on --background-menu-white; a title row (icon, name, extension, source, more) over the thumbnail.

| State | Values |
|---|---|
| default | size 322.66 x 258.41; border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| hover | shadow `elevation.layer` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px) |
| light | size 322.66 x 258.41; border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |
| light-hover | shadow `elevation.layer` (rgba(0, 0, 0, 0.06) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px) |

Tokens named in its classes: `--background-menu-white`, `--border-dark`, `--fill-tsp-gray-dark`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Grid card thumbnail area

<a id="grid-card-thumb"></a>`grid-card-thumb`, on library-dark-images-grid.

| State | Values |
|---|---|
| default | size 320.66 x 200.41; background transparent |
| light | size 320.66 x 200.41; background transparent |

Tokens named in its classes: `--fill-tsp-gray-dark`.

#### Grid card name and extension

<a id="grid-card-title"></a>`grid-card-title`, on library-dark-images-grid.

| State | Values |
|---|---|
| default | size 74.69 x 20; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| light | size 74.69 x 20; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |

#### Group-by-task heading

<a id="task-group-heading"></a>`task-group-heading`, on library-dark-images-grid-by-task. The task name as a 16/22 500 link (underline on hover) with its date at the end.

| State | Values |
|---|---|
| default | size 1000 x 34; padding `space.3` (12px) 0px 0px 0px; background transparent; text `typography.title-base` (System 16/22 500), `≈ text.primary` (#e6e6e6) |
| light | size 1000 x 34; padding `space.3` (12px) 0px 0px 0px; background transparent; text `typography.title-base` (System 16/22 500), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`, `--text-secondary`.

#### Group-by-task heading link

<a id="task-group-link"></a>`task-group-link`, on library-dark-images-grid-by-task.

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 96.56 x 22; background transparent; text `typography.title-base` (System 16/22 500), `text.primary` (#e6e6e6) |
| light (same: light-hover, light-focus-visible) | size 96.56 x 22; background transparent; text `typography.title-base` (System 16/22 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

### Document previewer

The full-screen previewer a Library row opens: a header with the title, Last modified and five tools, and the document body set in the serif.

#### Document previewer

<a id="previewer"></a>`previewer`, on library-dark-preview-doc. 1200x820 at 1440 (inset 120/40), --background-gray-main, over --background-dialog-mask with a 4px blur.

| State | Values |
|---|---|
| default | size 1200 x 820; background `background.gray-main` (#1a1a1a); shadow rgba(0, 0, 0, 0.02) 0px 0px 8px 0px; text System 16/22 500 tracking -0.31px, `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ text.tertiary` (#8c8c8c) |
| light | size 1200 x 820; background `background.gray-main` (#f8f8f7); shadow rgba(0, 0, 0, 0.02) 0px 0px 8px 0px; text System 16/22 500 tracking -0.31px, `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--background-gray-main`, `--border-dark`, `--border-main`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Previewer header

<a id="previewer-header"></a>`previewer-header`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 1200 x `size.header` (48px); padding `space.1_5` (6px) `space.3` (12px) `space.1_5` (6px) `space.5` (20px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); background `background.gray-main` (#1a1a1a); text System 16/22 500 tracking -0.31px, `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ text.tertiary` (#8c8c8c) |
| light | size 1200 x `size.header` (48px); padding `space.1_5` (6px) `space.3` (12px) `space.1_5` (6px) `space.5` (20px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); background `background.gray-main` (#f8f8f7); text System 16/22 500 tracking -0.31px, `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--background-gray-main`, `--border-dark`, `--border-main`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Previewer title

<a id="previewer-title"></a>`previewer-title`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 542.88 x 22; background transparent; text System 16/22 500 tracking -0.31px, `text.primary` (#e6e6e6) |
| light | size 542.88 x 22; background transparent; text System 16/22 500 tracking -0.31px, `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Previewer last-modified line

<a id="previewer-meta"></a>`previewer-meta`, on library-dark-preview-doc.

<img src="components/crops/previewer-meta-default.png" alt="Previewer last-modified line, default" height="24"> <img src="components/crops/previewer-meta-light.png" alt="Previewer last-modified line, light" height="24"> 

| State | Values |
|---|---|
| default | size 118.03 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c) |
| light | size 118.03 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373) |

#### Previewer toolbar icon button

<a id="previewer-tool"></a>`previewer-tool`, on library-dark-preview-doc.

<img src="components/crops/previewer-tool-default.png" alt="Previewer toolbar icon button, default" height="28"> <img src="components/crops/previewer-tool-hover.png" alt="Previewer toolbar icon button, hover" height="28"> <img src="components/crops/previewer-tool-light.png" alt="Previewer toolbar icon button, light" height="28"> <img src="components/crops/previewer-tool-light-hover.png" alt="Previewer toolbar icon button, light-hover" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon` (18 x 18), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--icon-secondary`.

#### Previewer document column

<a id="previewer-body"></a>`previewer-body`, on library-dark-preview-doc. 712 wide, centred in the scroll area.

| State | Values |
|---|---|
| default | size 712 x 3058.89; background transparent; text `typography.role.display` (Libre Baskerville 30/39 600), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| light | size 712 x 3058.89; background transparent; text `typography.role.display` (Libre Baskerville 30/39 600), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |

Child layers: div 712x1 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)); div 712x1 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)); div 712x1 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06))

Tokens named in its classes: `--border-main`.

#### Document h1

<a id="doc-h1"></a>`doc-h1`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 712 x 84; padding 3px 0px; background transparent; text `typography.role.display` (Libre Baskerville 30/39 600), `≈ text.primary` (#e6e6e6) |
| light | size 712 x 84; padding 3px 0px; background transparent; text `typography.role.display` (Libre Baskerville 30/39 600), `≈ text.primary` (#1a1a1a) |

#### Document h2

<a id="doc-h2"></a>`doc-h2`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 712 x 37.19; padding 3px 0px; background transparent; text System 24/31.2 600, `≈ text.primary` (#e6e6e6) |
| light | size 712 x 37.19; padding 3px 0px; background transparent; text System 24/31.2 600, `≈ text.primary` (#1a1a1a) |

#### Document h3

<a id="doc-h3"></a>`doc-h3`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 712 x `size.row-small` (32px); padding 3px 0px; background transparent; text System 20/26 600, `≈ text.primary` (#e6e6e6) |
| light | size 712 x `size.row-small` (32px); padding 3px 0px; background transparent; text System 20/26 600, `≈ text.primary` (#1a1a1a) |

#### Document paragraph

<a id="doc-paragraph"></a>`doc-paragraph`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 712 x 54; padding 3px 0px; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| light | size 712 x 54; padding 3px 0px; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |

#### Document bullet

<a id="doc-bullet"></a>`doc-bullet`, on library-dark-preview-doc.

| State | Values |
|---|---|
| default | size 24 x 30; background transparent; text System 24/36 400, `≈ text.primary` (#e6e6e6) |
| light | size 24 x 30; background transparent; text System 24/36 400, `≈ text.primary` (#1a1a1a) |

#### Document horizontal rule

<a id="doc-rule"></a>`doc-rule`, on library-dark-preview-doc.

<img src="components/crops/doc-rule-default.png" alt="Document horizontal rule, default" height="24"> <img src="components/crops/doc-rule-light.png" alt="Document horizontal rule, light" height="24"> 

| State | Values |
|---|---|
| default | size 712 x 1; background `border.main` (rgba(255, 255, 255, 0.06)) |
| light | size 712 x 1; background `border.main` (rgba(0, 0, 0, 0.06)) |

Tokens named in its classes: `--border-main`.

### Settings

The settings dialog: an account header and a left nav of sections, the General pane with Language, the three theme cards, selects and toggle rows, and the Keyboard shortcuts pane.

#### Settings dialog

<a id="settings-dialog"></a>`settings-dialog`, on settings-dark-general. 1152x810 at 1440, radius 16, shadow-menu; a 221 nav column with a right rule, the content column scrolls.

<img src="components/crops/settings-dialog-default.png" alt="Settings dialog, default" height="120"> <img src="components/crops/settings-dialog-light.png" alt="Settings dialog, light" height="120"> 

| State | Values |
|---|---|
| default | size 1152 x 810; radius `radius.dialog` (16px); background `background.gray-main` (#1a1a1a); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#8c8c8c); placeholder `≈ text.disable` (#595959) |
| light | size 1152 x 810; radius `radius.dialog` (16px); background `background.gray-main` (#f8f8f7); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#737373); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--Button-border-secondary`, `--background-gray-main`, `--border-input-active`, `--border-main`, `--dlg-enter-scale`, `--dlg-enter-y`, `--fill-tsp-gray-main`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-secondary`, `--icon-tertiary`, `--simplebar-scrollbar-width`, `--text-disable`, `--text-primary`, `--text-tertiary`, `--ui-density-row-gap`, `--ui-density-small-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Settings close button

<a id="settings-close"></a>`settings-close`, on settings-dark-general.

<img src="components/crops/settings-close-default.png" alt="Settings close button, default" height="28"> <img src="components/crops/settings-close-hover.png" alt="Settings close button, hover" height="28"> <img src="components/crops/settings-close-light.png" alt="Settings close button, light" height="28"> <img src="components/crops/settings-close-light-hover.png" alt="Settings close button, light-hover" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; icon `size.icon-medium` (20 x 20), `icon.tertiary` (#8c8c8c) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; icon `size.icon-medium` (20 x 20), `icon.tertiary` (#737373) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-tertiary`.

#### Settings account header

<a id="settings-account"></a>`settings-account`, on settings-dark-general.

<img src="components/crops/settings-account-default.png" alt="Settings account header, default" height="36"> <img src="components/crops/settings-account-hover.png" alt="Settings account header, hover" height="36"> <img src="components/crops/settings-account-light.png" alt="Settings account header, light" height="36"> <img src="components/crops/settings-account-light-hover.png" alt="Settings account header, light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 180 x `size.row` (36px); background transparent; text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#e6e6e6); transition opacity `duration.resize` (0.3s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#b3b3b3) |
| light (same: light-hover) | size 180 x `size.row` (36px); background transparent; text `typography.role.menu-header` (System 12/18 600), `≈ text.primary` (#1a1a1a); transition opacity `duration.resize` (0.3s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#4d4d4d) |

Child layers: div 32x32 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 9999px; div 30x30 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08))

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Settings search field

<a id="settings-search"></a>`settings-search`, on settings-dark-general.

<img src="components/crops/settings-search-default.png" alt="Settings search field, default" height="32"> <img src="components/crops/settings-search-hover.png" alt="Settings search field, hover" height="32"> <img src="components/crops/settings-search-light.png" alt="Settings search field, light" height="32"> <img src="components/crops/settings-search-light-hover.png" alt="Settings search field, light-hover" height="32"> <img src="components/crops/settings-search-focus-visible.png" alt="Settings search field, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 196 x `size.row-small` (32px); padding 0px `space.2` (8px) 0px 11px; border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| focus-visible | border `borderWidth.default` (1px) solid `border.input-active` (rgba(255, 255, 255, 0.32)) |
| light (same: light-hover) | size 196 x `size.row-small` (32px); padding 0px `space.2` (8px) 0px 11px; border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |
| light-focus-visible | border `borderWidth.default` (1px) solid `border.input-active` (rgba(0, 0, 0, 0.3)) |

Tokens named in its classes: `--Button-border-secondary`, `--border-input-active`, `--text-disable`, `--text-primary`.

#### Settings nav section label

<a id="settings-nav-label"></a>`settings-nav-label`, on settings-dark-general.

<img src="components/crops/settings-nav-label-default.png" alt="Settings nav section label, default" height="34"> <img src="components/crops/settings-nav-label-light.png" alt="Settings nav section label, light" height="34"> 

| State | Values |
|---|---|
| default | size 75.97 x 34; padding `space.3` (12px) `space.3` (12px) `space.1` (4px) `space.3_5` (14px); background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#8c8c8c) |
| light | size 75.97 x 34; padding `space.3` (12px) `space.3` (12px) `space.1` (4px) `space.3_5` (14px); background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

#### Settings nav item

<a id="settings-nav-item"></a>`settings-nav-item`, on settings-dark-general.

<img src="components/crops/settings-nav-item-default.png" alt="Settings nav item, default" height="32"> <img src="components/crops/settings-nav-item-hover.png" alt="Settings nav item, hover" height="32"> <img src="components/crops/settings-nav-item-light.png" alt="Settings nav item, light" height="32"> <img src="components/crops/settings-nav-item-light-hover.png" alt="Settings nav item, light-hover" height="32"> <img src="components/crops/settings-nav-item-active.png" alt="Settings nav item, active" height="32"> <img src="components/crops/settings-nav-item-focus-visible.png" alt="Settings nav item, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 196 x `size.row-small` (32px); padding `space.2` (8px) `space.4` (16px) `space.2` (8px) `space.3_5` (14px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| active, active-hover | background `≈ fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ icon.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 196 x `size.row-small` (32px); padding `space.2` (8px) `space.4` (16px) `space.2` (8px) `space.3_5` (14px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-active, light-active-hover | background `≈ fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ icon.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-secondary`, `--text-primary`, `--ui-density-row-gap`, `--ui-density-small-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Settings page title

<a id="settings-title"></a>`settings-title`, on settings-dark-general.

<img src="components/crops/settings-title-default.png" alt="Settings page title, default" height="30"> <img src="components/crops/settings-title-light.png" alt="Settings page title, light" height="30"> 

| State | Values |
|---|---|
| default | size 768 x 30; background transparent; text `typography.headline-base` (System 24/30 500), `text.primary` (#e6e6e6) |
| light | size 768 x 30; background transparent; text `typography.headline-base` (System 24/30 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Settings section title

<a id="settings-section-title"></a>`settings-section-title`, on settings-dark-general.

<img src="components/crops/settings-section-title-default.png" alt="Settings section title, default" height="24"> <img src="components/crops/settings-section-title-light.png" alt="Settings section title, light" height="24"> 

| State | Values |
|---|---|
| default | size 768 x 22; background transparent; text `typography.title-base` (System 16/22 500), `text.primary` (#e6e6e6) |
| light | size 768 x 22; background transparent; text `typography.title-base` (System 16/22 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`, `--ui-font-size-title-base`, `--ui-line-height-title-base`.

#### Settings field label

<a id="settings-field-label"></a>`settings-field-label`, on settings-dark-general.

<img src="components/crops/settings-field-label-default.png" alt="Settings field label, default" height="24"> <img src="components/crops/settings-field-label-light.png" alt="Settings field label, light" height="24"> 

| State | Values |
|---|---|
| default | size 768 x 24; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| light | size 768 x 24; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |

#### Language select

<a id="language-select"></a>`language-select`, on settings-dark-general.

<img src="components/crops/language-select-default.png" alt="Language select, default" height="36"> <img src="components/crops/language-select-hover.png" alt="Language select, hover" height="36"> <img src="components/crops/language-select-light.png" alt="Language select, light" height="36"> <img src="components/crops/language-select-light-hover.png" alt="Language select, light-hover" height="36"> <img src="components/crops/language-select-focus-visible.png" alt="Language select, focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 208 x `size.row` (36px); padding 0px `space.3` (12px); border `borderWidth.default` (1px) solid `border.white` (rgba(0, 0, 0, 0.08)); radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover, light-focus-visible) | size 208 x `size.row` (36px); padding 0px `space.3` (12px); border `borderWidth.default` (1px) solid `border.white` (rgba(255, 255, 255, 0.2)); radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--border-white`, `--fill-tsp-white-light`, `--text-primary`.

#### Theme option card

<a id="theme-card"></a>`theme-card`, on settings-dark-general. 110x62 with a small preview glyph over the label.

<img src="components/crops/theme-card-default.png" alt="Theme option card, default" height="62"> <img src="components/crops/theme-card-hover.png" alt="Theme option card, hover" height="62"> <img src="components/crops/theme-card-light.png" alt="Theme option card, light" height="62"> <img src="components/crops/theme-card-light-hover.png" alt="Theme option card, light-hover" height="62"> <img src="components/crops/theme-card-selected.png" alt="Theme option card, selected" height="62"> <img src="components/crops/theme-card-focus-visible.png" alt="Theme option card, focus-visible" height="62"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 110 x 62; padding `space.3` (12px) `space.2` (8px) `space.2` (8px) `space.2` (8px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.row` (10px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.secondary` (#b3b3b3); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| selected | border `borderWidth.default` (1px) solid `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 110 x 62; padding `space.3` (12px) `space.2` (8px) `space.2` (8px) `space.2` (8px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.row` (10px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.secondary` (#4d4d4d); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon` (18 x 18), `≈ text.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-selected | border `borderWidth.default` (1px) solid `button.black` (#1a1a19); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`, `--text-secondary`, `--ui-density-content-padding`, `--ui-density-outer-padding`, `--ui-density-row-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Settings inline select (Send without interrupting)

<a id="settings-select"></a>`settings-select`, on settings-dark-general.

<img src="components/crops/settings-select-default.png" alt="Settings inline select (Send without interrupting), default" height="36"> <img src="components/crops/settings-select-hover.png" alt="Settings inline select (Send without interrupting), hover" height="36"> <img src="components/crops/settings-select-light.png" alt="Settings inline select (Send without interrupting), light" height="36"> <img src="components/crops/settings-select-light-hover.png" alt="Settings inline select (Send without interrupting), light-hover" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 230 x `size.row` (36px); padding 0px 0px 0px `space.3` (12px); border `borderWidth.default` (1px) solid transparent; radius `radius.row` (10px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover) | size 230 x `size.row` (36px); padding 0px 0px 0px `space.3` (12px); border `borderWidth.default` (1px) solid transparent; radius `radius.row` (10px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`, `--ui-density-content-padding`, `--ui-density-row-gap`, `--ui-density-row-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Settings row title

<a id="settings-row-title"></a>`settings-row-title`, on settings-dark-general.

<img src="components/crops/settings-row-title-default.png" alt="Settings row title, default" height="24"> <img src="components/crops/settings-row-title-light.png" alt="Settings row title, light" height="24"> 

| State | Values |
|---|---|
| default | size 139.59 x 20; background transparent; text `typography.role.label` (System 14/20 500), `text.primary` (#e6e6e6) |
| light | size 139.59 x 20; background transparent; text `typography.role.label` (System 14/20 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Settings row description

<a id="settings-row-desc"></a>`settings-row-desc`, on settings-dark-general.

<img src="components/crops/settings-row-desc-default.png" alt="Settings row description, default" height="24"> <img src="components/crops/settings-row-desc-light.png" alt="Settings row description, light" height="24"> 

| State | Values |
|---|---|
| default | size 726 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#8c8c8c) |
| light | size 726 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`, `--ui-font-size-label`, `--ui-line-height-label`.

#### Toggle switch

<a id="toggle"></a>`toggle`, on settings-dark-general. 26x16 track, a 14px white knob that slides 10px; off --icon-disable, on --icon-blue.

<img src="components/crops/toggle-default.png" alt="Toggle switch, default" height="24"> <img src="components/crops/toggle-hover.png" alt="Toggle switch, hover" height="24"> <img src="components/crops/toggle-light.png" alt="Toggle switch, light" height="24"> <img src="components/crops/toggle-light-hover.png" alt="Toggle switch, light-hover" height="24"> <img src="components/crops/toggle-focus-visible.png" alt="Toggle switch, focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, on, disabled) | size 26 x 16; background transparent |
| light (same: light-hover, light-focus-visible, light-on, light-disabled) | size 26 x 16; background transparent |

Child layers: div 26x16 background `≈ text.disable` (#595959) radius 16px; span 14x14 background `≈ icon.white` (#ffffff) radius 9999px

Tokens named in its classes: `--icon-disable`, `--icon-white`.

#### Settings section rule

<a id="settings-rule"></a>`settings-rule`, on settings-dark-general.

<img src="components/crops/settings-rule-default.png" alt="Settings section rule, default" height="24"> <img src="components/crops/settings-rule-light.png" alt="Settings section rule, light" height="24"> 

| State | Values |
|---|---|
| default | size 768 x 1; background `border.main` (rgba(255, 255, 255, 0.06)) |
| light | size 768 x 1; background `border.main` (rgba(0, 0, 0, 0.06)) |

Tokens named in its classes: `--border-main`.

#### Shortcut row

<a id="shortcut-row"></a>`shortcut-row`, on settings-dark-shortcuts.

<img src="components/crops/shortcut-row-default.png" alt="Shortcut row, default" height="36"> <img src="components/crops/shortcut-row-light.png" alt="Shortcut row, light" height="36"> 

| State | Values |
|---|---|
| default | size 768 x `size.row` (36px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ icon.tertiary` (#8c8c8c) |
| light | size 768 x `size.row` (36px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ icon.tertiary` (#737373) |

Child layers: div 230x36 border 1px solid `≈ border.image-preview-toolbar` (rgba(255, 255, 255, 0.12)) radius 8px; span 26x26 background `≈ background.canvas-bg` (#1c1c1c) border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 6px; span 26x26 background `≈ background.canvas-bg` (#1c1c1c) border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 6px

Tokens named in its classes: `--background-card`, `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--icon-tertiary`, `--text-primary`, `--text-secondary`.

#### Shortcut key field

<a id="shortcut-field"></a>`shortcut-field`, on settings-dark-shortcuts.

<img src="components/crops/shortcut-field-default.png" alt="Shortcut key field, default" height="36"> <img src="components/crops/shortcut-field-hover.png" alt="Shortcut key field, hover" height="36"> <img src="components/crops/shortcut-field-light.png" alt="Shortcut key field, light" height="36"> <img src="components/crops/shortcut-field-light-hover.png" alt="Shortcut key field, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 230 x `size.row` (36px); padding 0px `space.1` (4px) 0px `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; text `typography.role.shortcut` (System 13/19.5 400), `≈ text.secondary` (#b3b3b3); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-xs` (14 x 14), `≈ icon.tertiary` (#8c8c8c) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 230 x `size.row` (36px); padding 0px `space.1` (4px) 0px `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.small` (8px); background transparent; text `typography.role.shortcut` (System 13/19.5 400), `≈ text.secondary` (#4d4d4d); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-xs` (14 x 14), `≈ icon.tertiary` (#737373) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--background-card`, `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--icon-tertiary`, `--text-primary`, `--text-secondary`.

#### Keycap

<a id="keycap"></a>`keycap`, on settings-dark-shortcuts.

<img src="components/crops/keycap-default.png" alt="Keycap, default" height="26"> <img src="components/crops/keycap-light.png" alt="Keycap, light" height="26"> 

| State | Values |
|---|---|
| default | size 26 x 26; padding 0px `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.md` (6px); background `background.card` (#1c1c1c); text `typography.role.shortcut` (System 13/19.5 400), `text.secondary` (#b3b3b3) |
| light | size 26 x 26; padding 0px `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.md` (6px); background `background.card` (#fafafa); text `typography.role.shortcut` (System 13/19.5 400), `text.secondary` (#4d4d4d) |

Tokens named in its classes: `--background-card`, `--border-main`, `--text-secondary`.

#### Shortcut clear button

<a id="shortcut-clear"></a>`shortcut-clear`, on settings-dark-shortcuts.

<img src="components/crops/shortcut-clear-default.png" alt="Shortcut clear button, default" height="24"> <img src="components/crops/shortcut-clear-hover.png" alt="Shortcut clear button, hover" height="24"> <img src="components/crops/shortcut-clear-light.png" alt="Shortcut clear button, light" height="24"> <img src="components/crops/shortcut-clear-light-hover.png" alt="Shortcut clear button, light-hover" height="24"> <img src="components/crops/shortcut-clear-focus-visible.png" alt="Shortcut clear button, focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 24 x 24; radius `radius.md` (6px); background transparent; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-xs` (14 x 14), `≈ icon.tertiary` (#8c8c8c) |
| hover | icon `size.icon-xs` (14 x 14), `≈ text.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 24 x 24; radius `radius.md` (6px); background transparent; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-xs` (14 x 14), `≈ icon.tertiary` (#737373) |
| light-hover | icon `size.icon-xs` (14 x 14), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--icon-tertiary`, `--text-primary`.

#### Reset to defaults button (outline)

<a id="reset-button"></a>`reset-button`, on settings-dark-shortcuts.

<img src="components/crops/reset-button-default.png" alt="Reset to defaults button (outline), default" height="32"> <img src="components/crops/reset-button-hover.png" alt="Reset to defaults button (outline), hover" height="32"> <img src="components/crops/reset-button-light.png" alt="Reset to defaults button (outline), light" height="32"> <img src="components/crops/reset-button-light-hover.png" alt="Reset to defaults button (outline), light-hover" height="32"> <img src="components/crops/reset-button-focus-visible.png" alt="Reset to defaults button (outline), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 127.7 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 127.7 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 127.7x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-small-row-height`.

### Creations

Published websites, games and apps: a tab strip and wide cards with a thumbnail, the task they came from, a URL chip and three actions.

#### Creations search field

<a id="creations-search"></a>`creations-search`, on creations-dark.

<img src="components/crops/creations-search-default.png" alt="Creations search field, default" height="32"> <img src="components/crops/creations-search-light.png" alt="Creations search field, light" height="32"> 

| State | Values |
|---|---|
| default | size 240 x `size.row-small` (32px); padding `space.1` (4px) `space.1_5` (6px) `space.1` (4px) `space.3` (12px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| light | size 240 x `size.row-small` (32px); padding `space.1` (4px) `space.1_5` (6px) `space.1` (4px) `space.3` (12px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--Button-border-secondary`, `--text-disable`, `--text-primary`, `--ui-density-input-gap`, `--ui-density-small-radius`.

#### Creation card

<a id="creation-card"></a>`creation-card`, on creations-dark. 1000 wide, radius 12, 0.5px --border-dark, --background-menu-white, 12 padding: a 232x131 thumbnail, the title, "Created in", the URL chip and three actions.

| State | Values |
|---|---|
| default (same: hover) | size 1000 x 156.5; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover) | size 1000 x 156.5; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-black`, `--Button-border-secondary`, `--background-menu-white`, `--border-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-onblack`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Creation thumbnail

<a id="creation-thumb"></a>`creation-thumb`, on creations-dark.

| State | Values |
|---|---|
| default (same: hover) | size 232 x 130.5; radius `radius.small` (8px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light (same: light-hover) | size 232 x 130.5; radius `radius.small` (8px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`.

#### Creation URL chip

<a id="creation-url"></a>`creation-url`, on creations-dark.

| State | Values |
|---|---|
| default (same: focus-visible) | size 208 x 20; padding `space.0_5` (2px) `space.1` (4px); radius 4px; background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c); icon `size.icon-xs` (14 x 14), `≈ text.tertiary` (#8c8c8c) |
| hover | text `typography.role.caption` (System 12/16 400), `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 208 x 20; padding `space.0_5` (2px) `space.1` (4px); radius 4px; background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373); icon `size.icon-xs` (14 x 14), `≈ text.tertiary` (#737373) |
| light-hover | text `typography.role.caption` (System 12/16 400), `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--text-tertiary`.

#### Locate in task (filled small button)

<a id="creation-action-primary"></a>`creation-action-primary`, on creations-dark.

<img src="components/crops/creation-action-primary-default.png" alt="Locate in task (filled small button), default" height="32"> <img src="components/crops/creation-action-primary-hover.png" alt="Locate in task (filled small button), hover" height="32"> <img src="components/crops/creation-action-primary-light.png" alt="Locate in task (filled small button), light" height="32"> <img src="components/crops/creation-action-primary-light-hover.png" alt="Locate in task (filled small button), light-hover" height="32"> <img src="components/crops/creation-action-primary-focus-visible.png" alt="Locate in task (filled small button), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 107.58 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label-compact` (System 14/18 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 107.58 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label-compact` (System 14/18 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`, `--ui-density-small-row-height`.

#### Edit in new task (ghost small button)

<a id="creation-action"></a>`creation-action`, on creations-dark.

<img src="components/crops/creation-action-default.png" alt="Edit in new task (ghost small button), default" height="32"> <img src="components/crops/creation-action-hover.png" alt="Edit in new task (ghost small button), hover" height="32"> <img src="components/crops/creation-action-light.png" alt="Edit in new task (ghost small button), light" height="32"> <img src="components/crops/creation-action-light-hover.png" alt="Edit in new task (ghost small button), light-hover" height="32"> <img src="components/crops/creation-action-focus-visible.png" alt="Edit in new task (ghost small button), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 121.56 x `size.row-small` (32px); padding 0px `space.2` (8px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light (same: light-focus-visible) | size 121.56 x `size.row-small` (32px); padding 0px `space.2` (8px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-small-row-height`.

#### Creation favourite (star) button

<a id="creation-star"></a>`creation-star`, on creations-dark.

<img src="components/crops/creation-star-default.png" alt="Creation favourite (star) button, default" height="28"> <img src="components/crops/creation-star-hover.png" alt="Creation favourite (star) button, hover" height="28"> <img src="components/crops/creation-star-light.png" alt="Creation favourite (star) button, light" height="28"> <img src="components/crops/creation-star-light-hover.png" alt="Creation favourite (star) button, light-hover" height="28"> <img src="components/crops/creation-star-focus-visible.png" alt="Creation favourite (star) button, focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-focus-visible) | size 28 x `size.control-small` (28px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`.

### Computers

Cloud computers: a heading, six setup cards with badges, and the Customize and Connect bands.

#### Create cloud computer button

<a id="computers-cta"></a>`computers-cta`, on computers-dark.

<img src="components/crops/computers-cta-default.png" alt="Create cloud computer button, default" height="32"> <img src="components/crops/computers-cta-hover.png" alt="Create cloud computer button, hover" height="32"> <img src="components/crops/computers-cta-light.png" alt="Create cloud computer button, light" height="32"> <img src="components/crops/computers-cta-light-hover.png" alt="Create cloud computer button, light-hover" height="32"> <img src="components/crops/computers-cta-focus-visible.png" alt="Create cloud computer button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 189.58 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 189.58 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 189.6x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-small-row-height`.

#### Computers section heading

<a id="computers-heading"></a>`computers-heading`, on computers-dark.

<img src="components/crops/computers-heading-default.png" alt="Computers section heading, default" height="32"> <img src="components/crops/computers-heading-light.png" alt="Computers section heading, light" height="32"> 

| State | Values |
|---|---|
| default | size 960 x `size.row-small` (32px); background transparent; text System 24/32 600, `text.primary` (#e6e6e6) |
| light | size 960 x `size.row-small` (32px); background transparent; text System 24/32 600, `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Setup card

<a id="setup-card"></a>`setup-card`, on computers-dark. 312x299, radius 12, 1px --border-main on --background-menu-white; a 173 tall illustration band on --fill-tsp-gray-main, title, two-line description and OS badges.

<img src="components/crops/setup-card-default.png" alt="Setup card, default" height="120"> <img src="components/crops/setup-card-hover.png" alt="Setup card, hover" height="120"> <img src="components/crops/setup-card-light.png" alt="Setup card, light" height="120"> <img src="components/crops/setup-card-light-hover.png" alt="Setup card, light-hover" height="120"> <img src="components/crops/setup-card-focus-visible.png" alt="Setup card, focus-visible" height="120"> 

| State | Values |
|---|---|
| default | size 312 x 299; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#242424); text System 16/22 600, `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); background `background.card` (#1c1c1c) |
| focus-visible | outline `focusRing.width` (2px) solid `≈ button.blue` (#1a93fe), offset `focusRing.width` (2px) |
| light | size 312 x 299; border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text System 16/22 600, `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); background `background.card` (#fafafa) |
| light-focus-visible | outline `focusRing.width` (2px) solid `≈ button.blue` (#0081f2), offset `focusRing.width` (2px) |

Tokens named in its classes: `--Button-blue`, `--background-card`, `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-gray-main`, `--fill-tsp-white-main`, `--text-primary`, `--text-secondary`.

#### OS badge

<a id="setup-badge"></a>`setup-badge`, on computers-dark.

<img src="components/crops/setup-badge-default.png" alt="OS badge, default" height="24"> <img src="components/crops/setup-badge-light.png" alt="OS badge, light" height="24"> 

| State | Values |
|---|---|
| default | size 66.08 x 24; padding `space.1` (4px) `space.2` (8px); radius `radius.md` (6px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.role.caption` (System 12/16 400), `≈ text.secondary` (#b3b3b3); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 66.08 x 24; padding `space.1` (4px) `space.2` (8px); radius `radius.md` (6px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.role.caption` (System 12/16 400), `≈ text.secondary` (#4d4d4d); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-main`.

#### Customize band (bottom CTA)

<a id="computers-customize"></a>`computers-customize`, on computers-dark.

<img src="components/crops/computers-customize-default.png" alt="Customize band (bottom CTA), default" height="86"> <img src="components/crops/computers-customize-hover.png" alt="Customize band (bottom CTA), hover" height="86"> <img src="components/crops/computers-customize-light.png" alt="Customize band (bottom CTA), light" height="86"> <img src="components/crops/computers-customize-light-hover.png" alt="Customize band (bottom CTA), light-hover" height="86"> <img src="components/crops/computers-customize-focus-visible.png" alt="Customize band (bottom CTA), focus-visible" height="86"> 

| State | Values |
|---|---|
| default | size 474 x 86; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.raised` (rgba(0, 0, 0, 0.16) 0px 3px 10px 0px); text System 14/20 500 tracking -0.15px, `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `background.menu-gray` (#1a1a1a) |
| focus-visible | outline `focusRing.width` (2px) solid `≈ button.blue` (#1a93fe), offset `focusRing.width` (2px) |
| light | size 474 x 86; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.raised` (rgba(0, 0, 0, 0.04) 0px 3px 10px 0px); text System 14/20 500 tracking -0.15px, `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `background.menu-gray` (#f8f8f7) |
| light-focus-visible | outline `focusRing.width` (2px) solid `≈ button.blue` (#0081f2), offset `focusRing.width` (2px) |

Tokens named in its classes: `--Button-blue`, `--background-menu-gray`, `--background-menu-white`, `--border-main`, `--shadow-S`, `--text-primary`, `--text-tertiary`.

#### Connect your devices band

<a id="computers-connect"></a>`computers-connect`, on computers-dark.

<img src="components/crops/computers-connect-default.png" alt="Connect your devices band, default" height="86"> <img src="components/crops/computers-connect-light.png" alt="Connect your devices band, light" height="86"> 

| State | Values |
|---|---|
| default | size 474 x 86; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.raised` (rgba(0, 0, 0, 0.16) 0px 3px 10px 0px); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ text.secondary` (#b3b3b3) |
| light | size 474 x 86; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.raised` (rgba(0, 0, 0, 0.04) 0px 3px 10px 0px); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ text.secondary` (#4d4d4d) |

Tokens named in its classes: `--Button-border-secondary`, `--background-menu-white`, `--border-main`, `--fill-tsp-white-light`, `--shadow-S`, `--text-primary`.

#### Connect new computer (outline small button)

<a id="computers-small-button"></a>`computers-small-button`, on computers-dark.

<img src="components/crops/computers-small-button-default.png" alt="Connect new computer (outline small button), default" height="28"> <img src="components/crops/computers-small-button-hover.png" alt="Connect new computer (outline small button), hover" height="28"> <img src="components/crops/computers-small-button-light.png" alt="Connect new computer (outline small button), light" height="28"> <img src="components/crops/computers-small-button-light-hover.png" alt="Connect new computer (outline small button), light-hover" height="28"> <img src="components/crops/computers-small-button-focus-visible.png" alt="Connect new computer (outline small button), focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 177.38 x `size.control-small` (28px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-xs` (14 x 14), `≈ text.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 177.38 x `size.control-small` (28px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-xs` (14 x 14), `≈ text.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 177.4x28 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`.

### Agents

The Meet Cue page: a title, a video with its play button, two download buttons, the waitlist banner and a footer link.

#### Meet Cue title

<a id="cue-title"></a>`cue-title`, on agents-dark.

<img src="components/crops/cue-title-default.png" alt="Meet Cue title, default" height="34"> <img src="components/crops/cue-title-light.png" alt="Meet Cue title, light" height="34"> 

| State | Values |
|---|---|
| default | size 562 x 34; background transparent; text System 34/34 500, `text.primary` (#e6e6e6) |
| light | size 562 x 34; background transparent; text System 34/34 500, `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Cue video frame

<a id="cue-video"></a>`cue-video`, on agents-dark.

<img src="components/crops/cue-video-default.png" alt="Cue video frame, default" height="120"> <img src="components/crops/cue-video-light.png" alt="Cue video frame, light" height="120"> 

| State | Values |
|---|---|
| default | size 562 x 316.13; radius 14px; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6); icon `size.icon-large` (24 x 24), `≈ icon.white` (#ffffff) |
| light | size 562 x 316.13; radius 14px; background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a); icon `size.icon-large` (24 x 24), `≈ icon.white` (#ffffff) |

Child layers: button 64x64 background `≈ background.dialog-mask` (rgba(0, 0, 0, 0.6)) radius 9999px

Tokens named in its classes: `--background-dialog-mask`, `--icon-white`.

#### Play video button

<a id="cue-play"></a>`cue-play`, on agents-dark.

<img src="components/crops/cue-play-default.png" alt="Play video button, default" height="64"> <img src="components/crops/cue-play-hover.png" alt="Play video button, hover" height="64"> <img src="components/crops/cue-play-light.png" alt="Play video button, light" height="64"> <img src="components/crops/cue-play-light-hover.png" alt="Play video button, light-hover" height="64"> <img src="components/crops/cue-play-focus-visible.png" alt="Play video button, focus-visible" height="64"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 64 x 64; radius `radius.full` (9999px); background `background.dialog-mask` (rgba(0, 0, 0, 0.6)); text `typography.role.body-long` (System 16/24 400), `icon.white` (#ffffff); icon `size.icon-large` (24 x 24), `≈ icon.white` (#ffffff) |
| light (same: light-hover, light-focus-visible) | size 64 x 64; radius `radius.full` (9999px); background `background.dialog-mask` (rgba(0, 0, 0, 0.3)); text `typography.role.body-long` (System 16/24 400), `icon.white` (#ffffff); icon `size.icon-large` (24 x 24), `≈ icon.white` (#ffffff) |

Tokens named in its classes: `--background-dialog-mask`, `--icon-white`.

#### Download for desktop (primary)

<a id="cue-download"></a>`cue-download`, on agents-dark.

<img src="components/crops/cue-download-default.png" alt="Download for desktop (primary), default" height="40"> <img src="components/crops/cue-download-hover.png" alt="Download for desktop (primary), hover" height="40"> <img src="components/crops/cue-download-light.png" alt="Download for desktop (primary), light" height="40"> <img src="components/crops/cue-download-light-hover.png" alt="Download for desktop (primary), light-hover" height="40"> <img src="components/crops/cue-download-focus-visible.png" alt="Download for desktop (primary), focus-visible" height="40"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 197.02 x `size.control-large` (40px); padding `space.2` (8px) `space.5` (20px) `space.2` (8px) `space.3` (12px); radius `radius.row` (10px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.meta` (System 13/18 400), `≈ text.onblack` (rgba(0, 0, 0, 0.9)) |
| light (same: light-hover, light-focus-visible) | size 197.02 x `size.control-large` (40px); padding `space.2` (8px) `space.5` (20px) `space.2` (8px) `space.3` (12px); radius `radius.row` (10px); background `button.black` (#1a1a19); text `typography.role.meta` (System 13/18 400), `≈ text.onblack` (#ffffff) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

#### Get the mobile app (black)

<a id="cue-mobile"></a>`cue-mobile`, on agents-dark.

<img src="components/crops/cue-mobile-default.png" alt="Get the mobile app (black), default" height="40"> <img src="components/crops/cue-mobile-hover.png" alt="Get the mobile app (black), hover" height="40"> <img src="components/crops/cue-mobile-light.png" alt="Get the mobile app (black), light" height="40"> <img src="components/crops/cue-mobile-light-hover.png" alt="Get the mobile app (black), light-hover" height="40"> <img src="components/crops/cue-mobile-focus-visible.png" alt="Get the mobile app (black), focus-visible" height="40"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 179.2 x `size.control-large` (40px); padding `space.2` (8px) `space.5` (20px) `space.2` (8px) `space.3` (12px); radius `radius.row` (10px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.meta` (System 13/18 400), `≈ text.onblack` (rgba(0, 0, 0, 0.9)) |
| light (same: light-hover, light-focus-visible) | size 179.2 x `size.control-large` (40px); padding `space.2` (8px) `space.5` (20px) `space.2` (8px) `space.3` (12px); radius `radius.row` (10px); background `button.black` (#1a1a19); text `typography.role.meta` (System 13/18 400), `≈ text.onblack` (#ffffff) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

#### Waitlist banner

<a id="waitlist-banner"></a>`waitlist-banner`, on agents-dark.

<img src="components/crops/waitlist-banner-default.png" alt="Waitlist banner, default" height="66"> <img src="components/crops/waitlist-banner-light.png" alt="Waitlist banner, light" height="66"> 

| State | Values |
|---|---|
| default | size 562 x 66; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#e6e6e6) |
| light | size 562 x 66; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-border-secondary`, `--background-menu-white`, `--border-dark`, `--fill-tsp-white-light`, `--icon-blue`, `--text-primary`.

#### Join waitlist button

<a id="waitlist-button"></a>`waitlist-button`, on agents-dark.

<img src="components/crops/waitlist-button-default.png" alt="Join waitlist button, default" height="36"> <img src="components/crops/waitlist-button-hover.png" alt="Join waitlist button, hover" height="36"> <img src="components/crops/waitlist-button-light.png" alt="Join waitlist button, light" height="36"> <img src="components/crops/waitlist-button-light-hover.png" alt="Join waitlist button, light-hover" height="36"> <img src="components/crops/waitlist-button-focus-visible.png" alt="Join waitlist button, focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 102.09 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 102.09 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 102.1x36 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`.

#### Visit our website link

<a id="cue-link"></a>`cue-link`, on agents-dark.

<img src="components/crops/cue-link-default.png" alt="Visit our website link, default" height="24"> <img src="components/crops/cue-link-hover.png" alt="Visit our website link, hover" height="24"> <img src="components/crops/cue-link-light.png" alt="Visit our website link, light" height="24"> <img src="components/crops/cue-link-light-hover.png" alt="Visit our website link, light-hover" height="24"> <img src="components/crops/cue-link-focus-visible.png" alt="Visit our website link, focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 116.25 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.secondary` (#b3b3b3); icon `size.icon-xs` (14 x 14), `≈ text.secondary` (#b3b3b3) |
| light (same: light-hover, light-focus-visible) | size 116.25 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.secondary` (#4d4d4d); icon `size.icon-xs` (14 x 14), `≈ text.secondary` (#4d4d4d) |

Tokens named in its classes: `--text-secondary`.

### Automations

The empty state: a heading and three example cards (Schedule, Trigger, Advanced) over a Get started button.

#### Create your first automation heading

<a id="automations-heading"></a>`automations-heading`, on automations-dark.

<img src="components/crops/automations-heading-default.png" alt="Create your first automation heading, default" height="34"> <img src="components/crops/automations-heading-light.png" alt="Create your first automation heading, light" height="34"> 

| State | Values |
|---|---|
| default | size 344.75 x 34; background transparent; text `typography.headline-lg` (System 28/34 500), `text.primary` (#e6e6e6) |
| light | size 344.75 x 34; background transparent; text `typography.headline-lg` (System 28/34 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Automation example card

<a id="automation-card"></a>`automation-card`, on automations-dark. 312x421, radius 12, 1px --border-main; an animated illustration band over a 16/22 title and a description.

<img src="components/crops/automation-card-default.png" alt="Automation example card, default" height="120"> <img src="components/crops/automation-card-hover.png" alt="Automation example card, hover" height="120"> <img src="components/crops/automation-card-light.png" alt="Automation example card, light" height="120"> <img src="components/crops/automation-card-light-hover.png" alt="Automation example card, light-hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 312 x 421; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#e6e6e6); icon 12 x 12, `≈ text.tertiary` (#8c8c8c) |
| light (same: light-hover) | size 312 x 421; border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#1a1a1a); icon 12 x 12, `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-white-dark`, `--fill-tsp-white-main`, `--icon-primary`, `--shadow-M`, `--text-onblack`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Automation card title

<a id="automation-card-title"></a>`automation-card-title`, on automations-dark.

<img src="components/crops/automation-card-title-default.png" alt="Automation card title, default" height="24"> <img src="components/crops/automation-card-title-light.png" alt="Automation card title, light" height="24"> 

| State | Values |
|---|---|
| default | size 69.11 x 22; background transparent; text `typography.title-base` (System 16/22 500), `text.primary` (#e6e6e6) |
| light | size 69.11 x 22; background transparent; text `typography.title-base` (System 16/22 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Get started button (black)

<a id="get-started"></a>`get-started`, on automations-dark.

<img src="components/crops/get-started-default.png" alt="Get started button (black), default" height="36"> <img src="components/crops/get-started-hover.png" alt="Get started button (black), hover" height="36"> <img src="components/crops/get-started-light.png" alt="Get started button (black), light" height="36"> <img src="components/crops/get-started-light-hover.png" alt="Get started button (black), light-hover" height="36"> <img src="components/crops/get-started-focus-visible.png" alt="Get started button (black), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 310 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 310 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

### Plugins

The connector gallery: header buttons, a carousel of promo cards, search, category tabs and a two-column grid of plugin rows.

#### Manage Connectors (outline)

<a id="plugins-header-button"></a>`plugins-header-button`, on plugins-dark.

<img src="components/crops/plugins-header-button-default.png" alt="Manage Connectors (outline), default" height="32"> <img src="components/crops/plugins-header-button-hover.png" alt="Manage Connectors (outline), hover" height="32"> <img src="components/crops/plugins-header-button-light.png" alt="Manage Connectors (outline), light" height="32"> <img src="components/crops/plugins-header-button-light-hover.png" alt="Manage Connectors (outline), light-hover" height="32"> <img src="components/crops/plugins-header-button-focus-visible.png" alt="Manage Connectors (outline), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 148.8 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 148.8 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 148.8x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-small-row-height`.

#### Header primary button

<a id="plugins-header-primary"></a>`plugins-header-primary`, on plugins-dark.

<img src="components/crops/plugins-header-primary-default.png" alt="Header primary button, default" height="32"> <img src="components/crops/plugins-header-primary-hover.png" alt="Header primary button, hover" height="32"> <img src="components/crops/plugins-header-primary-light.png" alt="Header primary button, light" height="32"> <img src="components/crops/plugins-header-primary-light-hover.png" alt="Header primary button, light-hover" height="32"> <img src="components/crops/plugins-header-primary-focus-visible.png" alt="Header primary button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 80.05 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 80.05 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 80x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-small-row-height`.

#### Plugin promo card

<a id="plugin-promo"></a>`plugin-promo`, on plugins-dark.

<img src="components/crops/plugin-promo-default.png" alt="Plugin promo card, default" height="114"> <img src="components/crops/plugin-promo-light.png" alt="Plugin promo card, light" height="114"> 

| State | Values |
|---|---|
| default | size 280 x 114; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.card-gray` (#1c1c1c); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6) |
| light | size 280 x 114; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.card-gray` (#fafafa); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-card-gray`, `--background-menu-white`, `--border-main`, `--fill-tsp-white-light`, `--text-primary`.

#### Carousel scroll-forward button

<a id="carousel-forward"></a>`carousel-forward`, on plugins-dark. Held at opacity 0 until the carousel is hovered; measured as found, then hovered.

<img src="components/crops/carousel-forward-default.png" alt="Carousel scroll-forward button, default" height="32"> <img src="components/crops/carousel-forward-hover.png" alt="Carousel scroll-forward button, hover" height="32"> <img src="components/crops/carousel-forward-light.png" alt="Carousel scroll-forward button, light" height="32"> <img src="components/crops/carousel-forward-light-hover.png" alt="Carousel scroll-forward button, light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 32 x `size.row-small` (32px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.full` (9999px); background `fill.white` (#242424); shadow rgba(0, 0, 0, 0.06) 0px 8px 16px 0px; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6); transition opacity `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); transform translate(0px, -16px); opacity 0; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.gray` (#1c1c1c); opacity none |
| light | size 32 x `size.row-small` (32px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.full` (9999px); background `fill.white` (#ffffff); shadow rgba(0, 0, 0, 0.06) 0px 8px 16px 0px; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a); transition opacity `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); transform translate(0px, -16px); opacity 0; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.gray` (#f8f8f7); opacity none |

Tokens named in its classes: `--border-main`, `--fill-gray`, `--fill-white`.

#### Plugins search field

<a id="plugins-search"></a>`plugins-search`, on plugins-dark.

<img src="components/crops/plugins-search-default.png" alt="Plugins search field, default" height="36"> <img src="components/crops/plugins-search-hover.png" alt="Plugins search field, hover" height="36"> <img src="components/crops/plugins-search-light.png" alt="Plugins search field, light" height="36"> <img src="components/crops/plugins-search-light-hover.png" alt="Plugins search field, light-hover" height="36"> <img src="components/crops/plugins-search-focus-visible.png" alt="Plugins search field, focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 768 x `size.row` (36px); padding 0px `space.2` (8px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| focus-visible | border `borderWidth.default` (1px) solid `border.input-active` (rgba(255, 255, 255, 0.32)) |
| light (same: light-hover) | size 768 x `size.row` (36px); padding 0px `space.2` (8px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |
| light-focus-visible | border `borderWidth.default` (1px) solid `border.input-active` (rgba(0, 0, 0, 0.3)) |

Tokens named in its classes: `--Button-border-secondary`, `--border-input-active`, `--text-disable`, `--text-primary`.

#### Category tab

<a id="category-tab"></a>`category-tab`, on plugins-dark.

<img src="components/crops/category-tab-default.png" alt="Category tab, default" height="32"> <img src="components/crops/category-tab-hover.png" alt="Category tab, hover" height="32"> <img src="components/crops/category-tab-light.png" alt="Category tab, light" height="32"> <img src="components/crops/category-tab-light-hover.png" alt="Category tab, light-hover" height="32"> <img src="components/crops/category-tab-selected.png" alt="Category tab, selected" height="32"> 

| State | Values |
|---|---|
| default | size 99.86 x `size.row-small` (32px); padding 0px `space.2_5` (10px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.tertiary` (#8c8c8c); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| selected | size 48 x `size.row-small` (32px); background `fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6) |
| light | size 99.86 x `size.row-small` (32px); padding 0px `space.2_5` (10px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.tertiary` (#737373); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-selected | size 48 x `size.row-small` (32px); background `fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-tertiary`.

#### Plugin row

<a id="plugin-row"></a>`plugin-row`, on plugins-dark. 378x76, radius 12, 1px --border-main, hover --fill-tsp-white-light; a 40px icon tile, name and two-line description, a 28px add button for plugins not yet added.

<img src="components/crops/plugin-row-default.png" alt="Plugin row, default" height="76"> <img src="components/crops/plugin-row-hover.png" alt="Plugin row, hover" height="76"> <img src="components/crops/plugin-row-light.png" alt="Plugin row, light" height="76"> <img src="components/crops/plugin-row-light-hover.png" alt="Plugin row, light-hover" height="76"> 

| State | Values |
|---|---|
| default | size 378 x 76; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background transparent; text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `icon.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 378 x 76; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background transparent; text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `icon.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-white-light`, `--icon-primary`, `--text-primary`, `--text-tertiary`.

#### Plugin icon tile

<a id="plugin-icon"></a>`plugin-icon`, on plugins-dark.

<img src="components/crops/plugin-icon-default.png" alt="Plugin icon tile, default" height="40"> <img src="components/crops/plugin-icon-light.png" alt="Plugin icon tile, light" height="40"> 

| State | Values |
|---|---|
| default | size 40 x `size.control-large` (40px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.small` (8px); background `background.menu-white` (#242424) |
| light | size 40 x `size.control-large` (40px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.small` (8px); background `background.menu-white` (#ffffff) |

Tokens named in its classes: `--background-menu-white`, `--border-main`.

#### Plugin name

<a id="plugin-name"></a>`plugin-name`, on plugins-dark.

<img src="components/crops/plugin-name-default.png" alt="Plugin name, default" height="24"> <img src="components/crops/plugin-name-light.png" alt="Plugin name, light" height="24"> 

| State | Values |
|---|---|
| default | size 66.31 x 17; background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6) |
| light | size 66.31 x 17; background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a) |

#### Plugin description

<a id="plugin-desc"></a>`plugin-desc`, on plugins-dark.

<img src="components/crops/plugin-desc-default.png" alt="Plugin description, default" height="31"> <img src="components/crops/plugin-desc-light.png" alt="Plugin description, light" height="31"> 

| State | Values |
|---|---|
| default | size 254.72 x 31; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c) |
| light | size 254.72 x 31; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373) |

#### Plugin add (+) button

<a id="plugin-add"></a>`plugin-add`, on plugins-dark.

<img src="components/crops/plugin-add-default.png" alt="Plugin add (+) button, default" height="28"> <img src="components/crops/plugin-add-hover.png" alt="Plugin add (+) button, hover" height="28"> <img src="components/crops/plugin-add-light.png" alt="Plugin add (+) button, light" height="28"> <img src="components/crops/plugin-add-light-hover.png" alt="Plugin add (+) button, light-hover" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.small` (8px); background transparent; icon `size.icon-xs` (14 x 14), `icon.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 28 x `size.control-small` (28px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.small` (8px); background transparent; icon `size.icon-xs` (14 x 14), `icon.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--icon-primary`.

### Project

A project page: icon, title and meta, the recent tasks, a composer, and the right rail of cards with Add buttons.

#### Project icon tile

<a id="project-icon"></a>`project-icon`, on project-dark.

<img src="components/crops/project-icon-default.png" alt="Project icon tile, default" height="48"> <img src="components/crops/project-icon-hover.png" alt="Project icon tile, hover" height="48"> <img src="components/crops/project-icon-light.png" alt="Project icon tile, light" height="48"> <img src="components/crops/project-icon-light-hover.png" alt="Project icon tile, light-hover" height="48"> 

| State | Values |
|---|---|
| default | size 48 x `size.header` (48px); padding `space.3` (12px); radius `radius.card` (12px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 48 x `size.header` (48px); padding `space.3` (12px); radius `radius.card` (12px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--fill-tsp-white-main`.

#### Project title

<a id="project-title"></a>`project-title`, on project-dark.

| State | Values |
|---|---|
| default (same: hover) | size 107.38 x `size.control-small` (28px); background transparent; text System 20/28 500, `text.primary` (#e6e6e6) |
| light (same: light-hover) | size 107.38 x `size.control-small` (28px); background transparent; text System 20/28 500, `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`, `--text-primary-hover`.

#### Project meta line

<a id="project-meta"></a>`project-meta`, on project-dark.

<img src="components/crops/project-meta-default.png" alt="Project meta line, default" height="24"> <img src="components/crops/project-meta-light.png" alt="Project meta line, light" height="24"> 

| State | Values |
|---|---|
| default | size 648 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c) |
| light | size 648 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373) |

Child layers: div 3x3 background `≈ text.disable` (#595959) radius 9999px

Tokens named in its classes: `--icon-disable`, `--text-tertiary`.

#### Recent label

<a id="project-recent-label"></a>`project-recent-label`, on project-dark.

<img src="components/crops/project-recent-label-default.png" alt="Recent label, default" height="24"> <img src="components/crops/project-recent-label-light.png" alt="Recent label, light" height="24"> 

| State | Values |
|---|---|
| default | size 43.23 x 18; background transparent; text `typography.role.section-label` (System 13/18 500), `text.tertiary` (#8c8c8c) |
| light | size 43.23 x 18; background transparent; text `typography.role.section-label` (System 13/18 500), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`, `--ui-font-size-label`, `--ui-line-height-label`.

#### Project task row

<a id="project-session"></a>`project-session`, on project-dark.

| State | Values |
|---|---|
| default | size 724 x 52; padding `space.3` (12px) `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 724 x 52; padding `space.3` (12px) `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Child layers: div 706x1 background `≈ border.light` (rgba(255, 255, 255, 0.03))

Tokens named in its classes: `--border-light`, `--fill-tsp-white-light`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`, `--ui-line-height-sm`, `--ui-line-height-xs`.

#### Right rail card (Instructions, Connectors)

<a id="project-rail-card"></a>`project-rail-card`, on project-dark. 320 wide, radius 12, 1px --border-main, clickable sections that fill on hover.

<img src="components/crops/project-rail-card-default.png" alt="Right rail card (Instructions, Connectors), default" height="120"> <img src="components/crops/project-rail-card-light.png" alt="Right rail card (Instructions, Connectors), light" height="120"> 

| State | Values |
|---|---|
| default | size 320 x 207; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 320 x 207; border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-border-secondary`, `--border-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`, `--text-secondary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Right rail card section

<a id="project-rail-section"></a>`project-rail-section`, on project-dark.

<img src="components/crops/project-rail-section-default.png" alt="Right rail card section, default" height="120"> <img src="components/crops/project-rail-section-hover.png" alt="Right rail card section, hover" height="120"> <img src="components/crops/project-rail-section-light.png" alt="Right rail card section, light" height="120"> <img src="components/crops/project-rail-section-light-hover.png" alt="Right rail card section, light-hover" height="120"> 

| State | Values |
|---|---|
| default | size 318 x 136; padding `space.4` (16px) `space.3` (12px) `space.4` (16px) `space.4` (16px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 318 x 136; padding `space.4` (16px) `space.3` (12px) `space.4` (16px) `space.4` (16px); background transparent; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Child layers: button 64.4x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Rail Add button (outline small)

<a id="project-add-button"></a>`project-add-button`, on project-dark.

<img src="components/crops/project-add-button-default.png" alt="Rail Add button (outline small), default" height="32"> <img src="components/crops/project-add-button-hover.png" alt="Rail Add button (outline small), hover" height="32"> <img src="components/crops/project-add-button-light.png" alt="Rail Add button (outline small), light" height="32"> <img src="components/crops/project-add-button-light-hover.png" alt="Rail Add button (outline small), light-hover" height="32"> <img src="components/crops/project-add-button-focus-visible.png" alt="Rail Add button (outline small), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 64.39 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 64.39 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 64.4x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-small-row-height`.

#### Connectors row

<a id="project-connectors"></a>`project-connectors`, on project-dark.

<img src="components/crops/project-connectors-default.png" alt="Connectors row, default" height="36"> <img src="components/crops/project-connectors-hover.png" alt="Connectors row, hover" height="36"> <img src="components/crops/project-connectors-light.png" alt="Connectors row, light" height="36"> <img src="components/crops/project-connectors-light-hover.png" alt="Connectors row, light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 290 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 290 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`, `--text-secondary`.

#### Project composer

<a id="project-composer"></a>`project-composer`, on project-dark.

<img src="components/crops/project-composer-default.png" alt="Project composer, default" height="120"> <img src="components/crops/project-composer-light.png" alt="Project composer, light" height="120"> 

| State | Values |
|---|---|
| default | size 740 x 120; padding `space.3` (12px) 0px; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.composer` (22px); background `background.menu-white` (#242424); shadow `elevation.composer` (rgba(0, 0, 0, 0.02) 0px 12px 32px 0px); text System 12/16 500, `≈ text.tertiary` (#8c8c8c); icon 17 x 17, `≈ icon.secondary` (#b3b3b3); placeholder `≈ text.tertiary` (#8c8c8c) |
| light | size 740 x 120; padding `space.3` (12px) 0px; border `borderWidth.default` (1px) solid #e5e7eb; radius `radius.composer` (22px); background `background.menu-white` (#ffffff); shadow `elevation.composer` (rgba(0, 0, 0, 0.02) 0px 12px 32px 0px); text System 12/16 500, `≈ text.tertiary` (#737373); icon 17 x 17, `≈ icon.secondary` (#4d4d4d); placeholder `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--accent-send-button`, `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-primary`, `--icon-secondary`, `--text-onblack`, `--text-primary`, `--text-secondary`, `--text-tertiary`, `--ui-density-composer-radius`, `--ui-density-content-padding`, `--ui-density-home-input-editor-min-height`, `--ui-density-outer-padding`, `--ui-density-row-gap`, `--ui-density-section-gap`, `--ui-density-small-row-height`.

### Task

A finished task's thread: the user bubble with an attachment, assistant turns with the logo header and Lite tag, step rows, message actions, the deliverable card, file chips, View all files, Task completed, rating stars, follow-up suggestions, the step footer, and the split view's tab bar, empty state tiles and files tree.

#### User message bubble

<a id="user-bubble"></a>`user-bubble`, on task-dark-thread-top. Right-aligned, at most 662 wide, radius from --ui-density-card-radius on --fill-tsp-white-main.

| State | Values |
|---|---|
| default | size 662.39 x 72; padding `space.3` (12px); radius `radius.card` (12px) `radius.card` (12px) 4px `radius.card` (12px); background `≈ background.live-events-end` (#242424); outline `focusRing.input-width` (1px) solid `≈ border.light` (rgba(255, 255, 255, 0.03)), offset 0px; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| light | size 662.39 x 72; padding `space.3` (12px); radius `radius.card` (12px) `radius.card` (12px) 4px `radius.card` (12px); background `≈ background.menu-white` (#ffffff); outline `focusRing.input-width` (1px) solid `≈ border.light` (rgba(0, 0, 0, 0.04)), offset 0px; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--border-light`, `--text-primary`, `--ui-density-bubble-padding-y`, `--ui-density-card-radius`, `--ui-density-content-padding`.

#### Attachment chip (in the thread)

<a id="user-attachment"></a>`user-attachment`, on task-dark-thread-top.

| State | Values |
|---|---|
| default | size 280 x 56; padding `space.2` (8px) `space.2_5` (10px) `space.2` (8px) `space.2` (8px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon 32 x 32, `≈ text.primary` (#e6e6e6) |
| hover | background `background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) |
| light | size 280 x 56; padding `space.2` (8px) `space.2_5` (10px) `space.2` (8px) `space.2` (8px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon 32 x 32, `≈ text.primary` (#1a1a1a) |
| light-hover | background `background.tsp-menu-white` (rgba(255, 255, 255, 0.08)) |

Tokens named in its classes: `--background-menu-white`, `--background-tsp-menu-white`, `--border-dark`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`, `--text-tertiary`.

#### Message time

<a id="message-time"></a>`message-time`, on task-dark-thread-top. Shown with the copy button only while the message is hovered.

<img src="components/crops/message-time-hover.png" alt="Message time, hover" height="24"> <img src="components/crops/message-time-light-hover.png" alt="Message time, light-hover" height="24"> 

| State | Values |
|---|---|
| hover | size 35.61 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#8c8c8c); transition color and 11 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | size 35.61 x 16; background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#737373); transition color and 11 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--text-tertiary`.

#### Assistant turn header (logo, wordmark, Lite tag)

<a id="assistant-header"></a>`assistant-header`, on task-dark-thread-top.

<img src="components/crops/assistant-header-default.png" alt="Assistant turn header (logo, wordmark, Lite tag), default" height="24"> <img src="components/crops/assistant-header-light.png" alt="Assistant turn header (logo, wordmark, Lite tag), light" height="24"> 

| State | Values |
|---|---|
| default | size 136.91 x 24; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c); icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| light | size 136.91 x 24; background transparent; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373); icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |

Child layers: span 34.9x20 border 1px solid `≈ border.image-preview-toolbar` (rgba(255, 255, 255, 0.12)) radius 6px

Tokens named in its classes: `--border-dark`, `--text-tertiary`.

#### Lite tag

<a id="lite-tag"></a>`lite-tag`, on task-dark-thread-top.

<img src="components/crops/lite-tag-default.png" alt="Lite tag, default" height="24"> <img src="components/crops/lite-tag-light.png" alt="Lite tag, light" height="24"> 

| State | Values |
|---|---|
| default | size 34.91 x 20; padding `space.0_5` (2px) `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.md` (6px); background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#8c8c8c) |
| light | size 34.91 x 20; padding `space.0_5` (2px) `space.1_5` (6px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.md` (6px); background transparent; text `typography.role.caption` (System 12/16 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--border-dark`, `--text-tertiary`.

#### Assistant message text

<a id="assistant-text"></a>`assistant-text`, on task-dark-thread-top.

| State | Values |
|---|---|
| default | size 736 x `size.header` (48px); background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#e6e6e6) |
| light | size 736 x `size.header` (48px); background transparent; text `typography.role.body-long` (System 16/24 400), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`.

#### Plan step row

<a id="step-row"></a>`step-row`, on task-dark-thread-top. 28 tall, 14px --text-secondary, a 17px round dot on --fill-tsp-white-dark holding a check; the time shows on hover.

| State | Values |
|---|---|
| default (same: focus-visible) | size 736 x `size.control-small` (28px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#b3b3b3); icon 9 x 9, `icon.tertiary` (#8c8c8c) |
| hover | text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| light (same: light-focus-visible) | size 736 x `size.control-small` (28px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#4d4d4d); icon 9 x 9, `icon.tertiary` (#737373) |
| light-hover | text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |

Child layers: div 17x17 background `≈ fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)) radius 9999px

Tokens named in its classes: `--fill-tsp-white-dark`, `--icon-tertiary`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Plan step dot

<a id="step-dot"></a>`step-dot`, on task-dark-thread-top.

<img src="components/crops/step-dot-default.png" alt="Plan step dot, default" height="24"> <img src="components/crops/step-dot-light.png" alt="Plan step dot, light" height="24"> 

| State | Values |
|---|---|
| default | size 17 x 17; radius `radius.full` (9999px); background `fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)); icon 9 x 9, `icon.tertiary` (#8c8c8c) |
| light | size 17 x 17; radius `radius.full` (9999px); background `fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)); icon 9 x 9, `icon.tertiary` (#737373) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--icon-tertiary`.

#### Message action icon button

<a id="message-action"></a>`message-action`, on task-dark-thread-top.

<img src="components/crops/message-action-default.png" alt="Message action icon button, default" height="28"> <img src="components/crops/message-action-hover.png" alt="Message action icon button, hover" height="28"> <img src="components/crops/message-action-light.png" alt="Message action icon button, light" height="28"> <img src="components/crops/message-action-light-hover.png" alt="Message action icon button, light-hover" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; icon `size.icon-small` (16 x 16), `icon.tertiary` (#8c8c8c) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; icon `size.icon-small` (16 x 16), `icon.tertiary` (#737373) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-tertiary`.

#### Deliverable card

<a id="deliverable-card"></a>`deliverable-card`, on task-dark-completed. 570 wide, radius 12, a 0.5px --border-dark hairline on --background-menu-white; a 61 tall header (icon, 14px 500 title, download and more) over a 16:9 preview.

| State | Values |
|---|---|
| default (same: hover) | size 570 x 382.5; border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text System 14/20 500 tracking -0.154px, `≈ text.primary` (#e6e6e6); icon 27 x 27, `≈ text.primary` (#e6e6e6) |
| light (same: light-hover) | size 570 x 382.5; border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text System 14/20 500 tracking -0.154px, `≈ text.primary` (#1a1a1a); icon 27 x 27, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`.

#### Deliverable card header

<a id="deliverable-header"></a>`deliverable-header`, on task-dark-completed.

| State | Values |
|---|---|
| default | size 568 x 61; padding `space.3_5` (14px) `space.3` (12px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); background transparent; text System 14/20 500 tracking -0.154px, `≈ text.primary` (#e6e6e6); icon 27 x 27, `≈ text.primary` (#e6e6e6) |
| light | size 568 x 61; padding `space.3_5` (14px) `space.3` (12px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); background transparent; text System 14/20 500 tracking -0.154px, `≈ text.primary` (#1a1a1a); icon 27 x 27, `≈ text.primary` (#1a1a1a) |

Child layers: div 568x61 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06))

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`.

#### Deliverable more button

<a id="deliverable-menu"></a>`deliverable-menu`, on task-dark-completed.

<img src="components/crops/deliverable-menu-default.png" alt="Deliverable more button, default" height="32"> <img src="components/crops/deliverable-menu-hover.png" alt="Deliverable more button, hover" height="32"> <img src="components/crops/deliverable-menu-light.png" alt="Deliverable more button, light" height="32"> <img src="components/crops/deliverable-menu-light-hover.png" alt="Deliverable more button, light-hover" height="32"> <img src="components/crops/deliverable-menu-focus-visible.png" alt="Deliverable more button, focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 32 x `size.row-small` (32px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-focus-visible) | size 32 x `size.row-small` (32px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`.

#### Deliverable card (document preview)

<a id="deliverable-doc"></a>`deliverable-doc`, on task-dark-thread-top.

| State | Values |
|---|---|
| default | size 570 x 382.5; border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| light | size 570 x 382.5; border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--text-primary`.

#### File chip

<a id="file-chip"></a>`file-chip`, on task-dark-completed. 280x56, radius 12, 0.5px border; a 32px file icon, name over type and size, a download button that appears on hover.

| State | Values |
|---|---|
| default | size 280 x 56; padding `space.2` (8px) `space.2_5` (10px) `space.2` (8px) `space.2` (8px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon 32 x 32, `≈ text.primary` (#e6e6e6) |
| hover | background `background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) |
| light | size 280 x 56; padding `space.2` (8px) `space.2_5` (10px) `space.2` (8px) `space.2` (8px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon 32 x 32, `≈ text.primary` (#1a1a1a) |
| light-hover | background `background.tsp-menu-white` (rgba(255, 255, 255, 0.08)) |

Tokens named in its classes: `--background-menu-white`, `--background-tsp-menu-white`, `--border-dark`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`, `--text-tertiary`.

#### View all files in this task button

<a id="view-all-files"></a>`view-all-files`, on task-dark-completed.

<img src="components/crops/view-all-files-default.png" alt="View all files in this task button, default" height="55"> <img src="components/crops/view-all-files-hover.png" alt="View all files in this task button, hover" height="55"> <img src="components/crops/view-all-files-light.png" alt="View all files in this task button, light" height="55"> <img src="components/crops/view-all-files-light-hover.png" alt="View all files in this task button, light-hover" height="55"> 

| State | Values |
|---|---|
| default | size 280 x 55; padding 0px `space.1_5` (6px) 0px `space.4` (16px); border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.body` (System 14/20 400), `≈ icon.secondary` (#b3b3b3); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover | background `background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) |
| light | size 280 x 55; padding 0px `space.1_5` (6px) 0px `space.4` (16px); border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.body` (System 14/20 400), `≈ icon.secondary` (#4d4d4d); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover | background `background.tsp-menu-white` (rgba(255, 255, 255, 0.08)) |

Tokens named in its classes: `--background-menu-white`, `--background-tsp-menu-white`, `--border-dark`, `--icon-secondary`.

#### Task completed status

<a id="task-completed"></a>`task-completed`, on task-dark-completed.

<img src="components/crops/task-completed-default.png" alt="Task completed status, default" height="24"> <img src="components/crops/task-completed-light.png" alt="Task completed status, light" height="24"> 

| State | Values |
|---|---|
| default | size 133.89 x 20; padding 0px `space.2` (8px) 0px 0px; radius `radius.full` (9999px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.success` (#5eb92d); icon `size.icon-small` (16 x 16), `≈ function.success` (#5eb92d) |
| light | size 133.89 x 20; padding 0px `space.2` (8px) 0px 0px; radius `radius.full` (9999px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.success` (#25ba3b); icon `size.icon-small` (16 x 16), `≈ function.success` (#25ba3b) |

Tokens named in its classes: `--function-success`.

#### Rating row (How was this result?)

<a id="rating"></a>`rating`, on task-dark-completed.

<img src="components/crops/rating-default.png" alt="Rating row (How was this result?), default" height="32"> <img src="components/crops/rating-light.png" alt="Rating row (How was this result?), light" height="32"> 

| State | Values |
|---|---|
| default | size 252.27 x `size.row-small` (32px); padding `space.1_5` (6px) 0px; radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#b3b3b3); icon `size.icon-small` (16 x 16), `≈ border.image-preview-toolbar` (rgba(255, 255, 255, 0.12)) |
| light | size 252.27 x `size.row-small` (32px); padding `space.1_5` (6px) 0px; radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#4d4d4d); icon `size.icon-small` (16 x 16), `≈ border.dark` (rgba(0, 0, 0, 0.14)) |

Tokens named in its classes: `--text-secondary`.

#### Rating star

<a id="rating-star"></a>`rating-star`, on task-dark-completed.

<img src="components/crops/rating-star-default.png" alt="Rating star, default" height="24"> <img src="components/crops/rating-star-hover.png" alt="Rating star, hover" height="24"> <img src="components/crops/rating-star-light.png" alt="Rating star, light" height="24"> <img src="components/crops/rating-star-light-hover.png" alt="Rating star, light-hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size 20 x 20; padding `space.0_5` (2px); background transparent; icon `size.icon-small` (16 x 16), `≈ border.image-preview-toolbar` (rgba(255, 255, 255, 0.12)) |
| light (same: light-hover) | size 20 x 20; padding `space.0_5` (2px); background transparent; icon `size.icon-small` (16 x 16), `≈ border.dark` (rgba(0, 0, 0, 0.14)) |

#### Follow-up suggestion row

<a id="suggestion-row"></a>`suggestion-row`, on task-dark-completed.

| State | Values |
|---|---|
| default | size 760 x 38; padding `density.suggestion-padding-y` (9px) `space.3` (12px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#b3b3b3); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| hover | radius `radius.row` (10px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 760 x 38; padding `density.suggestion-padding-y` (9px) `space.3` (12px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#4d4d4d); icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |
| light-hover | radius `radius.row` (10px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Child layers: div 736pxx1px background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06))

Tokens named in its classes: `--border-main`, `--fill-tsp-white-main`, `--text-secondary`, `--ui-density-suggestion-padding-y`.

#### Step footer above the composer

<a id="step-footer"></a>`step-footer`, on task-dark-completed. A rounded-top (22) card on --background-card-gray tucked 20px under the composer, with a thumbnail of the computer, the current step and "Step 4/4".

| State | Values |
|---|---|
| default | size 768 x 61; padding 0px 0px 19px 0px; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.composer` (22px) `radius.composer` (22px) 0px 0px; background `background.card-gray` (#1c1c1c); shadow rgba(0, 0, 0, 0.08) 0px 8px 16px 0px; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#8c8c8c); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 768 x 61; padding 0px 0px 19px 0px; border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.composer` (22px) `radius.composer` (22px) 0px 0px; background `background.card-gray` (#fafafa); shadow rgba(0, 0, 0, 0.02) 0px 8px 16px 0px; text `typography.role.caption` (System 12/16 400), `≈ text.tertiary` (#737373); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-card-gray`, `--background-gray-main`, `--border-dark`, `--border-main`, `--fill-white`, `--shadow-S`, `--shadow-XS`, `--shadows-drop-2`, `--tab-fill`, `--text-primary`, `--text-tertiary`.

#### Step footer row

<a id="step-footer-row"></a>`step-footer-row`, on task-dark-completed.

| State | Values |
|---|---|
| default (same: hover) | size 766 x `size.control-large` (40px); padding `space.2_5` (10px) `space.4` (16px); radius `radius.composer` (22px) `radius.composer` (22px) 0px 0px; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover) | size 766 x `size.control-large` (40px); padding `space.2_5` (10px) `space.4` (16px); radius `radius.composer` (22px) `radius.composer` (22px) 0px 0px; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--icon-tertiary`, `--text-tertiary`.

#### Step count

<a id="step-footer-count"></a>`step-footer-count`, on task-dark-completed.

<img src="components/crops/step-footer-count-default.png" alt="Step count, default" height="24"> <img src="components/crops/step-footer-count-light.png" alt="Step count, light" height="24"> 

| State | Values |
|---|---|
| default | size 51.77 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#8c8c8c) |
| light | size 51.77 x 18; background transparent; text `typography.role.meta` (System 13/18 400), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

#### Side panel

<a id="side-panel"></a>`side-panel`, on task-dark-side-panel. 570 wide at 1440, beside a 570 thread column, split by a 1px handle that widens to 5px blue on hover.

<img src="components/crops/side-panel-default.png" alt="Side panel, default" height="120"> <img src="components/crops/side-panel-light.png" alt="Side panel, light" height="120"> 

| State | Values |
|---|---|
| default | size 570 x 852; padding `space.8` (32px) `space.6` (24px); background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#e6e6e6); icon 22 x 22, `icon.secondary` (#b3b3b3) |
| light | size 570 x 852; padding `space.8` (32px) `space.6` (24px); background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#1a1a1a); icon 22 x 22, `icon.secondary` (#4d4d4d) |

Child layers: div 44x44 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px; div 216x72 background `≈ background.live-events-end` (#242424) border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px; div 216x72 background `≈ background.live-events-end` (#242424) border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-gray-main`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`, `--text-tertiary`.

#### Side panel tab bar

<a id="side-panel-tabbar"></a>`side-panel-tabbar`, on task-dark-side-panel.

<img src="components/crops/side-panel-tabbar-default.png" alt="Side panel tab bar, default" height="48"> <img src="components/crops/side-panel-tabbar-light.png" alt="Side panel tab bar, light" height="48"> 

| State | Values |
|---|---|
| default | size 570 x `size.header` (48px); padding 0px `space.3` (12px) 0px 0px; border B: `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); background `background.gray-main` (#1a1a1a); text `typography.role.shortcut` (System 13/19.5 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| light | size 570 x `size.header` (48px); padding 0px `space.3` (12px) 0px 0px; border B: `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); background `background.gray-main` (#f8f8f7); text `typography.role.shortcut` (System 13/19.5 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |

Tokens named in its classes: `--background-gray-main`, `--border-main`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--icon-secondary`, `--icon-tertiary`, `--tab-close-width`, `--tab-title-mask`, `--text-primary`, `--ui-density-small-row-height`.

#### Side panel tab

<a id="side-panel-tab"></a>`side-panel-tab`, on task-dark-side-panel.

<img src="components/crops/side-panel-tab-default.png" alt="Side panel tab, default" height="32"> <img src="components/crops/side-panel-tab-hover.png" alt="Side panel tab, hover" height="32"> <img src="components/crops/side-panel-tab-light.png" alt="Side panel tab, light" height="32"> <img src="components/crops/side-panel-tab-light-hover.png" alt="Side panel tab, light-hover" height="32"> 

| State | Values |
|---|---|
| default (same: hover) | size 160 x `size.row-small` (32px); padding 0px 5px; radius `radius.small` (8px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.role.shortcut` (System 13/19.5 400), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) cubic-bezier(0, 0, 0.2, 1); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| light (same: light-hover) | size 160 x `size.row-small` (32px); padding 0px 5px; radius `radius.small` (8px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.role.shortcut` (System 13/19.5 400), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) cubic-bezier(0, 0, 0.2, 1); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--fill-tsp-white-main`, `--icon-secondary`, `--icon-tertiary`, `--tab-close-width`, `--tab-title-mask`, `--text-primary`.

#### New tab launcher (+ and chevron)

<a id="side-panel-launcher"></a>`side-panel-launcher`, on task-dark-side-panel.

<img src="components/crops/side-panel-launcher-default.png" alt="New tab launcher (+ and chevron), default" height="32"> <img src="components/crops/side-panel-launcher-hover.png" alt="New tab launcher (+ and chevron), hover" height="32"> <img src="components/crops/side-panel-launcher-light.png" alt="New tab launcher (+ and chevron), light" height="32"> <img src="components/crops/side-panel-launcher-light-hover.png" alt="New tab launcher (+ and chevron), light-hover" height="32"> 

| State | Values |
|---|---|
| default | size 48 x `size.row-small` (32px); radius `radius.small` (8px); background transparent; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 48 x `size.row-small` (32px); radius `radius.small` (8px); background transparent; transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--icon-secondary`, `--ui-density-small-row-height`.

#### New tab empty state

<a id="new-tab-empty"></a>`new-tab-empty`, on task-dark-side-panel.

<img src="components/crops/new-tab-empty-default.png" alt="New tab empty state, default" height="120"> <img src="components/crops/new-tab-empty-light.png" alt="New tab empty state, light" height="120"> 

| State | Values |
|---|---|
| default | size 440 x 273; background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#e6e6e6); icon 22 x 22, `icon.secondary` (#b3b3b3) |
| light | size 440 x 273; background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#1a1a1a); icon 22 x 22, `icon.secondary` (#4d4d4d) |

Child layers: div 44x44 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px; div 216x72 background `≈ background.live-events-end` (#242424) border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px; div 216x72 background `≈ background.live-events-end` (#242424) border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-gray-main`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`, `--text-tertiary`.

#### Start from scratch tile

<a id="start-tile"></a>`start-tile`, on task-dark-side-panel.

<img src="components/crops/start-tile-default.png" alt="Start from scratch tile, default" height="72"> <img src="components/crops/start-tile-hover.png" alt="Start from scratch tile, hover" height="72"> <img src="components/crops/start-tile-light.png" alt="Start from scratch tile, light" height="72"> <img src="components/crops/start-tile-light-hover.png" alt="Start from scratch tile, light-hover" height="72"> 

| State | Values |
|---|---|
| default | size 216 x 72; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#242424); text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-gray-main` (rgba(0, 0, 0, 0.2)) |
| light | size 216 x 72; padding `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-gray-main` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--background-menu-white`, `--border-main`, `--fill-tsp-gray-main`, `--text-primary`.

#### Thread/panel resize handle

<a id="resize-handle"></a>`resize-handle`, on task-dark-side-panel.

| State | Values |
|---|---|
| default | size 1 x 900; radius `radius.full` (9999px); background `border.main` (rgba(255, 255, 255, 0.06)); transition width `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)), background-color `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | size 5 x 900; background `icon.blue` (#1a93fe) |
| light | size 1 x 900; radius `radius.full` (9999px); background `border.main` (rgba(0, 0, 0, 0.06)); transition width `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)), background-color `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | size 5 x 900; background `icon.blue` (#0081f2) |

Tokens named in its classes: `--border-main`, `--icon-blue`.

#### Files tab tree

<a id="file-tree"></a>`file-tree`, on task-dark-files-tab.

| State | Values |
|---|---|
| default | size 260 x 804; padding `space.1` (4px); background `background.gray-main` (#1a1a1a); text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `icon.tertiary` (#8c8c8c); placeholder `≈ text.disable` (#595959) |
| light | size 260 x 804; padding `space.1` (4px); background `background.gray-main` (#f8f8f7); text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `icon.tertiary` (#737373); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--background-gray-main`, `--background-menu-white`, `--border-input-active`, `--border-main`, `--fill-tsp-white-light`, `--icon-secondary`, `--icon-tertiary`, `--text-disable`, `--text-primary`, `--text-tertiary`, `--ui-density-input-gap`, `--ui-density-small-radius`, `--ui-density-small-row-height`.

#### Files tab tree header

<a id="file-tree-header"></a>`file-tree-header`, on task-dark-files-tab.

<img src="components/crops/file-tree-header-default.png" alt="Files tab tree header, default" height="30"> <img src="components/crops/file-tree-header-hover.png" alt="Files tab tree header, hover" height="30"> <img src="components/crops/file-tree-header-light.png" alt="Files tab tree header, light" height="30"> <img src="components/crops/file-tree-header-light-hover.png" alt="Files tab tree header, light-hover" height="30"> <img src="components/crops/file-tree-header-focus-visible.png" alt="Files tab tree header, focus-visible" height="30"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 252 x 30; padding 0px `space.1` (4px); radius `radius.md` (6px); background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#e6e6e6); icon 12 x 12, `icon.tertiary` (#8c8c8c) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-focus-visible) | size 252 x 30; padding 0px `space.1` (4px); radius `radius.md` (6px); background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#1a1a1a); icon 12 x 12, `icon.tertiary` (#737373) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-secondary`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`.

#### Files tab tree item

<a id="file-tree-item"></a>`file-tree-item`, on task-dark-files-tab.

| State | Values |
|---|---|
| default (same: focus-visible) | size 234 x `size.control-small` (28px); padding 0px 5px; radius 5px; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light (same: light-focus-visible) | size 234 x `size.control-small` (28px); padding 0px 5px; radius 5px; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-xs` (14 x 14), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`.

#### Select a file to preview

<a id="preview-empty"></a>`preview-empty`, on task-dark-files-tab.

<img src="components/crops/preview-empty-default.png" alt="Select a file to preview, default" height="77"> <img src="components/crops/preview-empty-light.png" alt="Select a file to preview, light" height="77"> 

| State | Values |
|---|---|
| default | size 197.34 x 77; padding 0px `space.6` (24px); background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#e6e6e6); icon 22 x 22, `icon.secondary` (#b3b3b3) |
| light | size 197.34 x 77; padding 0px `space.6` (24px); background transparent; text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#1a1a1a); icon 22 x 22, `icon.secondary` (#4d4d4d) |

Child layers: div 44x44 background `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)) radius 12px

Tokens named in its classes: `--fill-tsp-white-main`, `--icon-secondary`, `--text-primary`.

### Settings and forms

Added on the 2026-10-17 refresh: Settings' Developers pane (underline tabs, an info banner, the API key table with its row button and popover, the destructive confirmation), the Create API Key form (label, text field, select and its listbox, the primary button disabled and enabled), Personalization's fields, Usage & Billing loading, and the invite dialog (segmented control, black and blue buttons, the email field and Send), and the toast an invalid email raises. Pressed was read on every part here that has an `active:` style; the older parts' page copies were not kept, so their pressed rows are missing rather than measured.

#### Settings nav item, pressed and selected (Developers pane)

<a id="settings-nav-row"></a>`settings-nav-row`, on settings-dark-developers-table. A row in the Settings dialog's left nav: 16px icon, 14px label; the current pane is filled.

<img src="components/crops/settings-nav-row-default.png" alt="Settings nav item, pressed and selected (Developers pane), default" height="32"> <img src="components/crops/settings-nav-row-hover.png" alt="Settings nav item, pressed and selected (Developers pane), hover" height="32"> <img src="components/crops/settings-nav-row-light.png" alt="Settings nav item, pressed and selected (Developers pane), light" height="32"> <img src="components/crops/settings-nav-row-light-hover.png" alt="Settings nav item, pressed and selected (Developers pane), light-hover" height="32"> <img src="components/crops/settings-nav-row-selected.png" alt="Settings nav item, pressed and selected (Developers pane), selected" height="32"> 

| State | Values |
|---|---|
| default | size 196 x `size.row-small` (32px); padding `space.2` (8px) `space.4` (16px) `space.2` (8px) `space.3_5` (14px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#b3b3b3) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| pressed | background `fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)) |
| selected | background `≈ fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ icon.primary` (#e6e6e6) |
| light | size 196 x `size.row-small` (32px); padding `space.2` (8px) `space.4` (16px) `space.2` (8px) `space.3_5` (14px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ icon.secondary` (#4d4d4d) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |
| light-pressed | background `fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)) |
| light-selected | background `≈ fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.role.label` (System 14/20 500), `≈ icon.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ icon.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-secondary`, `--text-primary`, `--ui-density-row-gap`, `--ui-density-small-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Underline tab (API keys | Webhooks)

<a id="tabs-underline"></a>`tabs-underline`, on settings-dark-developers-table. Text tabs over a 1px rule; the active one is 500 weight in --text-primary with a 2px --Button-black underline that slides between tabs.

<img src="components/crops/tabs-underline-default.png" alt="Underline tab (API keys | Webhooks), default" height="40"> <img src="components/crops/tabs-underline-hover.png" alt="Underline tab (API keys | Webhooks), hover" height="40"> <img src="components/crops/tabs-underline-light.png" alt="Underline tab (API keys | Webhooks), light" height="40"> <img src="components/crops/tabs-underline-light-hover.png" alt="Underline tab (API keys | Webhooks), light-hover" height="40"> <img src="components/crops/tabs-underline-selected.png" alt="Underline tab (API keys | Webhooks), selected" height="40"> 

| State | Values |
|---|---|
| default | size 69.09 x `size.control-large` (40px); padding `space.2_5` (10px) 0px; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.tertiary` (#8c8c8c); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover | text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#b3b3b3) |
| selected | size 56.05 x `size.control-large` (40px); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6) |
| light | size 69.09 x `size.control-large` (40px); padding `space.2_5` (10px) 0px; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.tertiary` (#737373); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover | text `typography.role.body` (System 14/20 400), `≈ text.secondary` (#4d4d4d) |
| light-selected | size 56.05 x `size.control-large` (40px); text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Info banner (Manage API Keys …)

<a id="info-banner"></a>`info-banner`, on settings-dark-developers-table.

<img src="components/crops/info-banner-default.png" alt="Info banner (Manage API Keys …), default" height="42"> <img src="components/crops/info-banner-light.png" alt="Info banner (Manage API Keys …), light" height="42"> 

| State | Values |
|---|---|
| default | size 768 x 42; padding `space.3` (12px) `space.4` (16px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 768 x 42; padding `space.3` (12px) `space.4` (16px); radius `radius.card` (12px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Outline button (+ Create new)

<a id="button-outline"></a>`button-outline`, on settings-dark-developers-table.

<img src="components/crops/button-outline-default.png" alt="Outline button (+ Create new), default" height="32"> <img src="components/crops/button-outline-hover.png" alt="Outline button (+ Create new), hover" height="32"> <img src="components/crops/button-outline-light.png" alt="Outline button (+ Create new), light" height="32"> <img src="components/crops/button-outline-light-hover.png" alt="Outline button (+ Create new), light-hover" height="32"> <img src="components/crops/button-outline-focus-visible.png" alt="Outline button (+ Create new), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 112.91 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| hover, pressed | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 112.91 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label-compact` (System 14/18 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |
| light-hover, light-pressed | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 112.9x32 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`, `--ui-density-small-row-height`.

#### Table (API keys)

<a id="table"></a>`table`, on settings-dark-developers-table. A plain <table>: a 13px --text-tertiary header row and 14px body rows divided by 1px --border-main rules, no zebra, no outer border; the last column is a 28px more button.

<img src="components/crops/table-default.png" alt="Table (API keys), default" height="120"> <img src="components/crops/table-light.png" alt="Table (API keys), light" height="120"> 

| State | Values |
|---|---|
| default | size 768 x 183; background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.tertiary` (#8c8c8c); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#e6e6e6) |
| light | size 768 x 183; background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.tertiary` (#737373); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#1a1a1a) |

Child layers: thead 768x35 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06)); tr 768x49 border 1px solid `≈ border.light` (rgba(255, 255, 255, 0.03)); tr 768x49 border 1px solid `≈ border.light` (rgba(255, 255, 255, 0.03))

Tokens named in its classes: `--border-light`, `--border-main`, `--fill-tsp-white-main`, `--text-primary`, `--text-tertiary`.

#### Table header cell

<a id="table-header-cell"></a>`table-header-cell`, on settings-dark-developers-table.

<img src="components/crops/table-header-cell-default.png" alt="Table header cell, default" height="35"> <img src="components/crops/table-header-cell-light.png" alt="Table header cell, light" height="35"> 

| State | Values |
|---|---|
| default | size 140 x 35; padding `space.2` (8px) `space.6` (24px) `space.2` (8px) 1px; background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.tertiary` (#8c8c8c) |
| light | size 140 x 35; padding `space.2` (8px) `space.6` (24px) `space.2` (8px) 1px; background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.tertiary` (#737373) |

#### Table row

<a id="table-row"></a>`table-row`, on settings-dark-developers-table.

<img src="components/crops/table-row-default.png" alt="Table row, default" height="49"> <img src="components/crops/table-row-hover.png" alt="Table row, hover" height="49"> <img src="components/crops/table-row-light.png" alt="Table row, light" height="49"> <img src="components/crops/table-row-light-hover.png" alt="Table row, light-hover" height="49"> 

| State | Values |
|---|---|
| default (same: hover) | size 768 x 49; border B: `borderWidth.default` (1px) solid `border.light` (rgba(255, 255, 255, 0.03)); background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover) | size 768 x 49; border B: `borderWidth.default` (1px) solid `border.light` (rgba(0, 0, 0, 0.04)); background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#1a1a1a) |

Child layers: tr 768x49 border 1px solid `≈ border.light` (rgba(255, 255, 255, 0.03))

Tokens named in its classes: `--border-light`, `--fill-tsp-white-main`.

#### Table row more button

<a id="table-row-more"></a>`table-row-more`, on settings-dark-developers-table, settings-dark-key-menu. 28x28, radius 6; hover fills with --fill-tsp-white-main.

<img src="components/crops/table-row-more-default.png" alt="Table row more button, default" height="28"> <img src="components/crops/table-row-more-hover.png" alt="Table row more button, hover" height="28"> <img src="components/crops/table-row-more-light.png" alt="Table row more button, light" height="28"> <img src="components/crops/table-row-more-light-hover.png" alt="Table row more button, light-hover" height="28"> <img src="components/crops/table-row-more-open.png" alt="Table row more button, open" height="28"> <img src="components/crops/table-row-more-focus-visible.png" alt="Table row more button, focus-visible" height="28"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| open | background `≈ fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light (same: light-focus-visible) | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |
| light-open | background `≈ fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`.

#### Row popover menu

<a id="popover-menu"></a>`popover-menu`, on settings-dark-key-menu. A one-item popover under the more button.

<img src="components/crops/popover-menu-default.png" alt="Row popover menu, default" height="44"> <img src="components/crops/popover-menu-light.png" alt="Row popover menu, light" height="44"> 

| State | Values |
|---|---|
| default | size 110 x 44; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ function.error` (#eb4d4d); icon `size.icon-small` (16 x 16), `≈ function.error` (#eb4d4d) |
| light | size 110 x 44; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ function.error` (#fb494f); icon `size.icon-small` (16 x 16), `≈ function.error` (#fb494f) |

Tokens named in its classes: `--background-menu-white`, `--fill-tsp-white-main`, `--function-error`, `--ui-density-menu-item-padding-y`.

#### Menu item, destructive (Delete)

<a id="menu-item-danger"></a>`menu-item-danger`, on settings-dark-key-menu. Text and trash icon in --function-error; the hover fill is the neutral menu hover, not a red one.

<img src="components/crops/menu-item-danger-default.png" alt="Menu item, destructive (Delete), default" height="36"> <img src="components/crops/menu-item-danger-hover.png" alt="Menu item, destructive (Delete), hover" height="36"> <img src="components/crops/menu-item-danger-light.png" alt="Menu item, destructive (Delete), light" height="36"> <img src="components/crops/menu-item-danger-light-hover.png" alt="Menu item, destructive (Delete), light-hover" height="36"> 

| State | Values |
|---|---|
| default | size 102 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.error` (#eb4d4d); icon `size.icon-small` (16 x 16), `≈ function.error` (#eb4d4d) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 102 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ function.error` (#fb494f); icon `size.icon-small` (16 x 16), `≈ function.error` (#fb494f) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--fill-tsp-white-main`, `--function-error`, `--ui-density-menu-item-padding-y`.

#### Destructive confirmation dialog

<a id="confirm-dialog"></a>`confirm-dialog`, on settings-dark-delete-confirm. A small dialog over a scrim: a 16px 500 question, a 14px "This action cannot be undone." line, Cancel and a red Delete at the end, and a close button.

<img src="components/crops/confirm-dialog-default.png" alt="Destructive confirmation dialog, default" height="120"> <img src="components/crops/confirm-dialog-light.png" alt="Destructive confirmation dialog, light" height="120"> 

| State | Values |
|---|---|
| default | size 440 x 156; radius `radius.dialog` (16px); background `background.gray-main` (#1a1a1a); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.heading` (System 18/24 600), `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#8c8c8c) |
| light | size 440 x 156; radius `radius.dialog` (16px); background `background.gray-main` (#f8f8f7); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.heading` (System 18/24 600), `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#737373) |

Tokens named in its classes: `--Button-border-secondary`, `--background-gray-main`, `--dlg-enter-scale`, `--dlg-enter-y`, `--dp`, `--dp-header-end`, `--fill-tsp-white-light`, `--function-error`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`, `--text-white`.

#### Danger button (Delete)

<a id="button-danger"></a>`button-danger`, on settings-dark-delete-confirm.

<img src="components/crops/button-danger-default.png" alt="Danger button (Delete), default" height="36"> <img src="components/crops/button-danger-hover.png" alt="Danger button (Delete), hover" height="36"> <img src="components/crops/button-danger-light.png" alt="Danger button (Delete), light" height="36"> <img src="components/crops/button-danger-light-hover.png" alt="Danger button (Delete), light-hover" height="36"> <img src="components/crops/button-danger-focus-visible.png" alt="Danger button (Delete), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 72 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `function.error` (#eb4d4d); text `typography.role.label` (System 14/20 500), `≈ text.white` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover, pressed | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 72 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `function.error` (#fb494f); text `typography.role.label` (System 14/20 500), `≈ text.white` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover, light-pressed | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--function-error`, `--text-white`.

#### Secondary button (Cancel)

<a id="button-secondary"></a>`button-secondary`, on settings-dark-delete-confirm.

<img src="components/crops/button-secondary-default.png" alt="Secondary button (Cancel), default" height="36"> <img src="components/crops/button-secondary-hover.png" alt="Secondary button (Cancel), hover" height="36"> <img src="components/crops/button-secondary-light.png" alt="Secondary button (Cancel), light" height="36"> <img src="components/crops/button-secondary-light-hover.png" alt="Secondary button (Cancel), light-hover" height="36"> <img src="components/crops/button-secondary-focus-visible.png" alt="Secondary button (Cancel), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 72 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(255, 255, 255, 0.12)), offset -1px; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover, pressed | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 72 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background transparent; outline `focusRing.input-width` (1px) solid `≈ button.border-secondary` (rgba(0, 0, 0, 0.12)), offset -1px; text `typography.role.label` (System 14/20 500), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover, light-pressed | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); opacity `opacity.hover` (0.9) |

Child layers: button 72x36 radius 8px

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-light`, `--text-primary`.

#### Dialog close button

<a id="confirm-dialog-close"></a>`confirm-dialog-close`, on settings-dark-delete-confirm.

<img src="components/crops/confirm-dialog-close-default.png" alt="Dialog close button, default" height="28"> <img src="components/crops/confirm-dialog-close-hover.png" alt="Dialog close button, hover" height="28"> <img src="components/crops/confirm-dialog-close-light.png" alt="Dialog close button, light" height="28"> <img src="components/crops/confirm-dialog-close-light-hover.png" alt="Dialog close button, light-hover" height="28"> 

| State | Values |
|---|---|
| default | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; icon `size.icon-medium` (20 x 20), `icon.tertiary` (#8c8c8c) |
| hover | background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)) |
| light | size 28 x `size.control-small` (28px); radius `radius.md` (6px); background transparent; icon `size.icon-medium` (20 x 20), `icon.tertiary` (#737373) |
| light-hover | background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)) |

Tokens named in its classes: `--fill-tsp-white-light`, `--icon-tertiary`.

#### Form dialog (Create API Key)

<a id="form-dialog"></a>`form-dialog`, on settings-dark-create-key. Labelled fields stacked with 8px between label and field; Cancel and Create at the end. Create stays disabled until the name has text; there is no inline validation message.

<img src="components/crops/form-dialog-default.png" alt="Form dialog (Create API Key), default" height="120"> <img src="components/crops/form-dialog-light.png" alt="Form dialog (Create API Key), light" height="120"> 

| State | Values |
|---|---|
| default | size 400 x 280; radius `radius.dialog` (16px); background `background.gray-main` (#1a1a1a); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.heading` (System 18/24 600), `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#8c8c8c); placeholder `≈ text.disable` (#595959) |
| light | size 400 x 280; radius `radius.dialog` (16px); background `background.gray-main` (#f8f8f7); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text `typography.role.heading` (System 18/24 600), `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#737373); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--Button-black`, `--Button-border-secondary`, `--background-gray-main`, `--border-dark`, `--dlg-enter-scale`, `--dlg-enter-y`, `--dp`, `--dp-header-end`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--icon-tertiary`, `--text-disable`, `--text-onblack`, `--text-primary`, `--ui-density-content-padding`, `--ui-density-input-gap`, `--ui-density-large-control-height`, `--ui-density-row-gap`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-density-small-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Field label

<a id="field-label"></a>`field-label`, on settings-dark-create-key.

<img src="components/crops/field-label-default.png" alt="Field label, default" height="24"> <img src="components/crops/field-label-light.png" alt="Field label, light" height="24"> 

| State | Values |
|---|---|
| default | size 360 x 20; background transparent; text `typography.role.label` (System 14/20 500), `text.primary` (#e6e6e6) |
| light | size 360 x 20; background transparent; text `typography.role.label` (System 14/20 500), `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Text field

<a id="text-field"></a>`text-field`, on settings-dark-create-key, settings-dark-create-key-typed. Placeholder in --text-disable; the value in --text-primary; a clear (×) button appears inside once it has text.

<img src="components/crops/text-field-default.png" alt="Text field, default" height="24"> <img src="components/crops/text-field-hover.png" alt="Text field, hover" height="24"> <img src="components/crops/text-field-light.png" alt="Text field, light" height="24"> <img src="components/crops/text-field-light-hover.png" alt="Text field, light-hover" height="24"> <img src="components/crops/text-field-typed.png" alt="Text field, typed" height="24"> <img src="components/crops/text-field-focus-visible.png" alt="Text field, focus-visible" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible) | size 336 x 20; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| typed, typed-focus-visible | size 310 x 20 |
| light (same: light-hover, light-focus-visible) | size 336 x 20; background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |
| light-typed, light-typed-focus-visible | size 310 x 20 |

Tokens named in its classes: `--text-disable`.

#### Text field frame

<a id="text-field-wrapper"></a>`text-field-wrapper`, on settings-dark-create-key, settings-dark-create-key-typed. The painted frame around the input; focus-visible is read with keyboard focus on the input inside.

<img src="components/crops/text-field-wrapper-default.png" alt="Text field frame, default" height="36"> <img src="components/crops/text-field-wrapper-hover.png" alt="Text field frame, hover" height="36"> <img src="components/crops/text-field-wrapper-light.png" alt="Text field frame, light" height="36"> <img src="components/crops/text-field-wrapper-light-hover.png" alt="Text field frame, light-hover" height="36"> <img src="components/crops/text-field-wrapper-typed.png" alt="Text field frame, typed" height="36"> <img src="components/crops/text-field-wrapper-focus-visible.png" alt="Text field frame, focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 360 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); placeholder `≈ text.disable` (#595959) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset |
| typed | icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#8c8c8c) |
| light (same: light-hover) | size 360 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); placeholder `≈ text.disable` (#a6a6a6) |
| light-focus-visible | shadow #ffffff 0px 0px 0px 0px inset, rgba(0, 0, 0, 0.14) 0px 0px 0px 1px inset |
| light-typed | icon `size.icon-small` (16 x 16), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--border-dark`, `--fill-tsp-white-main`, `--text-disable`, `--text-primary`, `--ui-density-input-gap`, `--ui-density-row-height`, `--ui-density-small-radius`.

#### Select trigger (Expiration)

<a id="select-trigger"></a>`select-trigger`, on settings-dark-create-key, settings-dark-select-open.

<img src="components/crops/select-trigger-default.png" alt="Select trigger (Expiration), default" height="40"> <img src="components/crops/select-trigger-hover.png" alt="Select trigger (Expiration), hover" height="40"> <img src="components/crops/select-trigger-light.png" alt="Select trigger (Expiration), light" height="40"> <img src="components/crops/select-trigger-light-hover.png" alt="Select trigger (Expiration), light-hover" height="40"> <img src="components/crops/select-trigger-open.png" alt="Select trigger (Expiration), open" height="40"> 

| State | Values |
|---|---|
| default (same: hover, open) | size 360 x `size.control-large` (40px); padding 0px `space.3` (12px); border `borderWidth.default` (1px) solid transparent; radius `radius.row` (10px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light (same: light-hover, light-open) | size 360 x `size.control-large` (40px); padding 0px `space.3` (12px); border `borderWidth.default` (1px) solid transparent; radius `radius.row` (10px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-light`, `--text-primary`, `--ui-density-content-padding`, `--ui-density-large-control-height`, `--ui-density-row-gap`, `--ui-density-row-radius`, `--ui-density-small-row-height`, `--ui-font-size-sm`, `--ui-line-height-sm`.

#### Select listbox

<a id="select-listbox"></a>`select-listbox`, on settings-dark-select-open.

<img src="components/crops/select-listbox-default.png" alt="Select listbox, default" height="120"> <img src="components/crops/select-listbox-light.png" alt="Select listbox, light" height="120"> 

| State | Values |
|---|---|
| default | size 360 x 234; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 360 x 234; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--anchor-width`, `--background-menu-white`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`, `--ui-density-row-height`.

#### Select option

<a id="select-option"></a>`select-option`, on settings-dark-select-open.

<img src="components/crops/select-option-default.png" alt="Select option, default" height="36"> <img src="components/crops/select-option-hover.png" alt="Select option, hover" height="36"> <img src="components/crops/select-option-light.png" alt="Select option, light" height="36"> <img src="components/crops/select-option-light-hover.png" alt="Select option, light-hover" height="36"> <img src="components/crops/select-option-selected.png" alt="Select option, selected" height="36"> 

| State | Values |
|---|---|
| default | size 352 x `size.row` (36px); padding `space.2` (8px) `space.1_5` (6px) `space.2` (8px) `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| hover | background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| selected | icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 352 x `size.row` (36px); padding `space.2` (8px) `space.1_5` (6px) `space.2` (8px) `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |
| light-hover | background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |
| light-selected | icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`, `--ui-density-row-height`.

#### Primary button (Create)

<a id="button-primary"></a>`button-primary`, on settings-dark-create-key, settings-dark-create-key-typed. Black on light, white on dark (--Button-black / --text-onblack); hover opacity 0.9, pressed 0.8. Disabled while the form is incomplete (`default`), enabled once a name is typed.

<img src="components/crops/button-primary-default.png" alt="Primary button (Create), default" height="36"> <img src="components/crops/button-primary-light.png" alt="Primary button (Create), light" height="36"> 

| State | Values |
|---|---|
| default | size 72 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); opacity `opacity.disabled-strong` (0.5) |
| enabled | opacity none |
| enabled-hover | opacity `opacity.hover` (0.9) |
| enabled-focus-visible | opacity none |
| enabled-pressed | opacity `opacity.hover` (0.9) |
| light | size 72 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); opacity `opacity.disabled-strong` (0.5) |
| light-enabled | opacity none |
| light-enabled-hover | opacity `opacity.hover` (0.9) |
| light-enabled-focus-visible | opacity none |
| light-enabled-pressed | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

#### Text area (More about you)

<a id="text-area"></a>`text-area`, on settings-dark-personalization.

<img src="components/crops/text-area-default.png" alt="Text area (More about you), default" height="120"> <img src="components/crops/text-area-hover.png" alt="Text area (More about you), hover" height="120"> <img src="components/crops/text-area-light.png" alt="Text area (More about you), light" height="120"> <img src="components/crops/text-area-light-hover.png" alt="Text area (More about you), light-hover" height="120"> <img src="components/crops/text-area-focus-visible.png" alt="Text area (More about you), focus-visible" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 768 x 122; padding `space.3` (12px) `space.4` (16px) `space.5` (20px) `space.4` (16px); background transparent; text `typography.body-sm` (System 14/22 400), `text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(255, 255, 255, 0.12) 0px 0px 0px 0px |
| light (same: light-hover) | size 768 x 122; padding `space.3` (12px) `space.4` (16px) `space.5` (20px) `space.4` (16px); background transparent; text `typography.body-sm` (System 14/22 400), `text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |
| light-focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(0, 0, 0, 0.14) 0px 0px 0px 0px |

Tokens named in its classes: `--border-dark`, `--fill-tsp-white-light`, `--text-disable`, `--text-primary`, `--text-tertiary`.

#### Settings text field (Nickname)

<a id="text-field-settings"></a>`text-field-settings`, on settings-dark-personalization.

<img src="components/crops/text-field-settings-default.png" alt="Settings text field (Nickname), default" height="36"> <img src="components/crops/text-field-settings-hover.png" alt="Settings text field (Nickname), hover" height="36"> <img src="components/crops/text-field-settings-light.png" alt="Settings text field (Nickname), light" height="36"> <img src="components/crops/text-field-settings-light-hover.png" alt="Settings text field (Nickname), light-hover" height="36"> <img src="components/crops/text-field-settings-focus-visible.png" alt="Settings text field (Nickname), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover) | size 376 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(255, 255, 255, 0.04)); text `typography.role.body` (System 14/20 400), `text.primary` (#e6e6e6); placeholder `≈ text.disable` (#595959) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset |
| light (same: light-hover) | size 376 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px); radius `radius.small` (8px); background `fill.tsp-white-light` (rgba(55, 53, 47, 0.04)); text `typography.role.body` (System 14/20 400), `text.primary` (#1a1a1a); placeholder `≈ text.disable` (#a6a6a6) |
| light-focus-visible | shadow #ffffff 0px 0px 0px 0px inset, rgba(0, 0, 0, 0.14) 0px 0px 0px 1px inset |

Tokens named in its classes: `--border-dark`, `--fill-tsp-white-light`, `--text-disable`, `--text-primary`, `--ui-density-row-height`, `--ui-density-small-radius`.

#### Settings link card (Import memory)

<a id="settings-card-row"></a>`settings-card-row`, on settings-dark-personalization.

<img src="components/crops/settings-card-row-default.png" alt="Settings link card (Import memory), default" height="74"> <img src="components/crops/settings-card-row-hover.png" alt="Settings link card (Import memory), hover" height="74"> <img src="components/crops/settings-card-row-light.png" alt="Settings link card (Import memory), light" height="74"> <img src="components/crops/settings-card-row-light-hover.png" alt="Settings link card (Import memory), light-hover" height="74"> 

| State | Values |
|---|---|
| default | size 768 x 74.5; padding `space.4` (16px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.card` (12px); background `background.card-gray` (#1c1c1c); text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#e6e6e6); transition box-shadow `duration.sidebar` (0.2s) cubic-bezier(0, 0, 0.2, 1); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#e6e6e6) |
| hover | shadow rgba(0, 0, 0, 0.16) 0px 1px 2px 0px, rgba(0, 0, 0, 0.16) 0px 2px 4px 0px |
| light | size 768 x 74.5; padding `space.4` (16px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.card` (12px); background `background.card-gray` (#fafafa); text `typography.role.nav-strong` (System 14/21 500), `≈ text.primary` (#1a1a1a); transition box-shadow `duration.sidebar` (0.2s) cubic-bezier(0, 0, 0.2, 1); icon `size.icon-medium` (20 x 20), `≈ text.primary` (#1a1a1a) |
| light-hover | shadow rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px |

Tokens named in its classes: `--background-card-gray`, `--background-menu-white`, `--border-main`, `--shadow-S`, `--text-primary`, `--text-tertiary`.

#### Loading spinner

<a id="spinner"></a>`spinner`, on settings-dark-usage-loading. The only loading indicator in the Settings dialog: a ring under "Credits history" while the list loads.

<img src="components/crops/spinner-default.png" alt="Loading spinner, default" height="24"> <img src="components/crops/spinner-light.png" alt="Loading spinner, light" height="24"> 

| State | Values |
|---|---|
| default | size 16 x 16; border T: `borderWidth.strong` (2px) solid `≈ text.primary` (#e6e6e6); R: `borderWidth.strong` (2px) solid #e5e7eb; B: `borderWidth.strong` (2px) solid #e5e7eb; L: `borderWidth.strong` (2px) solid #e5e7eb; radius `radius.full` (9999px); background transparent |
| light | size 16 x 16; border T: `borderWidth.strong` (2px) solid `≈ text.primary` (#1a1a1a); R: `borderWidth.strong` (2px) solid #e5e7eb; B: `borderWidth.strong` (2px) solid #e5e7eb; L: `borderWidth.strong` (2px) solid #e5e7eb; radius `radius.full` (9999px); background transparent |

#### Upgrade button (Usage)

<a id="button-white"></a>`button-white`, on settings-dark-usage-loading.

<img src="components/crops/button-white-default.png" alt="Upgrade button (Usage), default" height="32"> <img src="components/crops/button-white-hover.png" alt="Upgrade button (Usage), hover" height="32"> <img src="components/crops/button-white-light.png" alt="Upgrade button (Usage), light" height="32"> <img src="components/crops/button-white-light-hover.png" alt="Upgrade button (Usage), light-hover" height="32"> <img src="components/crops/button-white-focus-visible.png" alt="Upgrade button (Usage), focus-visible" height="32"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 73.16 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label-compact` (System 14/18 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| hover, pressed | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 73.16 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label-compact` (System 14/18 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-hover, light-pressed | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`, `--ui-density-small-row-height`.

#### Plan card (Free)

<a id="plan-card"></a>`plan-card`, on settings-dark-usage-loading.

<img src="components/crops/plan-card-default.png" alt="Plan card (Free), default" height="57"> <img src="components/crops/plan-card-light.png" alt="Plan card (Free), light" height="57"> 

| State | Values |
|---|---|
| default | size 734 x 57; padding `space.3` (12px) 0px; border B: `borderWidth.default` (1px) dashed `border.dark` (rgba(255, 255, 255, 0.12)); background transparent; text Libre Baskerville 16/22 700, `≈ text.primary` (#e6e6e6) |
| light | size 734 x 57; padding `space.3` (12px) 0px; border B: `borderWidth.default` (1px) dashed `border.dark` (rgba(0, 0, 0, 0.14)); background transparent; text Libre Baskerville 16/22 700, `≈ text.primary` (#1a1a1a) |

Child layers: div 734x57 border 1px dashed `≈ border.image-preview-toolbar` (rgba(255, 255, 255, 0.12)); button 73.2x32 background `≈ button.black` (rgba(255, 255, 255, 0.95)) radius 8px

Tokens named in its classes: `--Button-black`, `--border-dark`, `--text-onblack`, `--text-primary`, `--ui-density-small-row-height`.

#### Invite dialog

<a id="invite-dialog"></a>`invite-dialog`, on invite-dark-dialog.

<img src="components/crops/invite-dialog-default.png" alt="Invite dialog, default" height="120"> <img src="components/crops/invite-dialog-light.png" alt="Invite dialog, light" height="120"> 

| State | Values |
|---|---|
| default | size 440 x 532.5; radius `radius.dialog` (16px); background `background.gray-main` (#1a1a1a); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text System 28/42 600, `≈ text.primary` (#e6e6e6); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#8c8c8c); placeholder `≈ text.disable` (#595959) |
| light | size 440 x 532.5; radius `radius.dialog` (16px); background `background.gray-main` (#f8f8f7); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); outline `focusRing.width` (2px) solid transparent, offset `focusRing.width` (2px); text System 28/42 600, `≈ text.primary` (#1a1a1a); icon `size.icon-medium` (20 x 20), `icon.tertiary` (#737373); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--background-gray-main`, `--border-main`, `--dlg-enter-scale`, `--dlg-enter-y`, `--dp`, `--dp-header-end`, `--fill-tsp-gray-main`, `--fill-tsp-white-light`, `--fill-white`, `--icon-tertiary`, `--shadow-S`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Segmented control (Share on web | mobile)

<a id="segmented"></a>`segmented`, on invite-dark-dialog.

<img src="components/crops/segmented-default.png" alt="Segmented control (Share on web | mobile), default" height="36"> <img src="components/crops/segmented-light.png" alt="Segmented control (Share on web | mobile), light" height="36"> <img src="components/crops/segmented-selected.png" alt="Segmented control (Share on web | mobile), selected" height="32"> 

| State | Values |
|---|---|
| default | size 276.25 x `size.row` (36px); padding 1px; border `borderWidth.default` (1px) solid transparent; radius `radius.small` (8px); background `fill.tsp-gray-main` (rgba(0, 0, 0, 0.2)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6) |
| item | size 136.13 x `size.row-small` (32px); padding 0px `space.4` (16px); border none; radius none; background transparent; text `typography.role.body` (System 14/20 400), `text.tertiary` (#8c8c8c); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| item-hover | size 136.13 x `size.row-small` (32px); padding 0px `space.4` (16px); border none; radius none; background transparent; text `typography.role.body` (System 14/20 400), `text.secondary` (#b3b3b3); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| item-focus-visible | size 136.13 x `size.row-small` (32px); padding 0px `space.4` (16px); border none; radius none; background transparent; text `typography.role.body` (System 14/20 400), `text.tertiary` (#8c8c8c); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| selected | size 136.13 x `size.row-small` (32px); padding none; border none; radius none; background transparent |
| light | size 276.25 x `size.row` (36px); padding 1px; border `borderWidth.default` (1px) solid transparent; radius `radius.small` (8px); background `fill.tsp-gray-main` (rgba(55, 53, 47, 0.04)); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a) |
| light-item | size 136.13 x `size.row-small` (32px); padding 0px `space.4` (16px); border none; radius none; background transparent; text `typography.role.body` (System 14/20 400), `text.tertiary` (#737373); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-item-hover | size 136.13 x `size.row-small` (32px); padding 0px `space.4` (16px); border none; radius none; background transparent; text `typography.role.body` (System 14/20 400), `text.secondary` (#4d4d4d); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-item-focus-visible | size 136.13 x `size.row-small` (32px); padding 0px `space.4` (16px); border none; radius none; background transparent; text `typography.role.body` (System 14/20 400), `text.tertiary` (#737373); transition color and 5 more `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-selected | size 136.13 x `size.row-small` (32px); padding none; border none; radius none; background transparent |

Tokens named in its classes: `--fill-tsp-gray-main`, `--fill-white`, `--shadow-S`, `--text-primary`, `--text-secondary`, `--text-tertiary`.

#### Full-width black button (Copy invitation link)

<a id="button-black-wide"></a>`button-black-wide`, on invite-dark-dialog.

<img src="components/crops/button-black-wide-default.png" alt="Full-width black button (Copy invitation link), default" height="36"> <img src="components/crops/button-black-wide-hover.png" alt="Full-width black button (Copy invitation link), hover" height="36"> <img src="components/crops/button-black-wide-light.png" alt="Full-width black button (Copy invitation link), light" height="36"> <img src="components/crops/button-black-wide-light-hover.png" alt="Full-width black button (Copy invitation link), light-hover" height="36"> <img src="components/crops/button-black-wide-focus-visible.png" alt="Full-width black button (Copy invitation link), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 392 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.onblack` (rgba(0, 0, 0, 0.9)) |
| hover, pressed | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 392 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.onblack` (#ffffff) |
| light-hover, light-pressed | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

#### Blue button (Invite Facebook friends)

<a id="button-blue"></a>`button-blue`, on invite-dark-dialog. Facebook's own blue as a literal (#2167e8 in both themes), not a Manus token; Manus's blue is button.blue. Kept for its states, which match the black buttons (hover and pressed at opacity 0.9).

<img src="components/crops/button-blue-default.png" alt="Blue button (Invite Facebook friends), default" height="36"> <img src="components/crops/button-blue-hover.png" alt="Blue button (Invite Facebook friends), hover" height="36"> <img src="components/crops/button-blue-light.png" alt="Blue button (Invite Facebook friends), light" height="36"> <img src="components/crops/button-blue-light-hover.png" alt="Blue button (Invite Facebook friends), light-hover" height="36"> <img src="components/crops/button-blue-focus-visible.png" alt="Blue button (Invite Facebook friends), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 392 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background #2167e8; text `typography.role.label` (System 14/20 500), `≈ text.white` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.white` (#ffffff) |
| hover, pressed | opacity `opacity.hover` (0.9) |
| light (same: light-focus-visible) | size 392 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background #2167e8; text `typography.role.label` (System 14/20 500), `≈ text.white` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.white` (#ffffff) |
| light-hover, light-pressed | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--text-white`.

#### Email field (typed, then rejected)

<a id="email-field"></a>`email-field`, on invite-dark-dialog, invite-dark-email-typed, invite-dark-email-error. Validated only on submit, and the field itself never changes: an invalid address is reported by a toast (`error` is the field with the toast showing).

<img src="components/crops/email-field-default.png" alt="Email field (typed, then rejected), default" height="36"> <img src="components/crops/email-field-hover.png" alt="Email field (typed, then rejected), hover" height="36"> <img src="components/crops/email-field-light.png" alt="Email field (typed, then rejected), light" height="36"> <img src="components/crops/email-field-light-hover.png" alt="Email field (typed, then rejected), light-hover" height="36"> <img src="components/crops/email-field-typed.png" alt="Email field (typed, then rejected), typed" height="36"> <img src="components/crops/email-field-focus-visible.png" alt="Email field (typed, then rejected), focus-visible" height="36"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, typed, error) | size 302.22 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px) `space.2` (8px) `space.4` (16px); border `borderWidth.default` (1px) solid transparent; background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#e6e6e6); transition color and 5 more `duration.resize` (0.3s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `≈ text.disable` (#595959) |
| light (same: light-hover, light-focus-visible, light-typed, light-error) | size 302.22 x `size.row` (36px); padding `space.2` (8px) `space.3` (12px) `space.2` (8px) `space.4` (16px); border `borderWidth.default` (1px) solid transparent; background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#1a1a1a); transition color and 5 more `duration.resize` (0.3s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--border-primary`, `--text-disable`.

#### Toast (error after an invalid email)

<a id="toast"></a>`toast`, on invite-dark-email-error. Centred against the top edge of the window (its fixed list sits 28px down, z-index 1050, newest first, and the toast is drawn translated up 44px, so it measures top 0); --background-menu-tooltips, radius 12, a 1px --border-white and shadow-M, 10/16 padding, a 20px icon and 14/22 500 text. It shows for about 6.3s and has no close button. Form validation errors use it too.

<img src="components/crops/toast-default.png" alt="Toast (error after an invalid email), default" height="44"> <img src="components/crops/toast-light.png" alt="Toast (error after an invalid email), light" height="44"> 

| State | Values |
|---|---|
| default | size 206.2 x 44; padding `space.2_5` (10px) `space.4` (16px); border `borderWidth.default` (1px) solid `border.white` (rgba(0, 0, 0, 0.08)); radius `radius.card` (12px); background `background.menu-tooltips` (rgba(0, 0, 0, 0.9)); shadow rgba(0, 0, 0, 0.28) 0px 4px 11px 0px; backdrop blur(40px); text System 14/22 500, `≈ text.white` (#ffffff); transform translate(0px, -44px); icon `size.icon-medium` (20 x 20), `≈ text.white` (#ffffff) |
| light | size 206.2 x 44; padding `space.2_5` (10px) `space.4` (16px); border `borderWidth.default` (1px) solid `border.white` (rgba(255, 255, 255, 0.2)); radius `radius.card` (12px); background `background.menu-tooltips` (rgba(0, 0, 0, 0.9)); shadow rgba(0, 0, 0, 0.06) 0px 4px 11px 0px; backdrop blur(40px); text System 14/22 500, `≈ text.white` (#ffffff); transform translate(0px, -44px); icon `size.icon-medium` (20 x 20), `≈ text.white` (#ffffff) |

Tokens named in its classes: `--background-menu-tooltips`, `--border-white`, `--shadow-M`, `--text-white`.

#### Send button (disabled, then enabled)

<a id="send-button"></a>`send-button`, on invite-dark-dialog, invite-dark-email-typed. Disabled while the field is empty; any text enables it (no format check before submit).

<img src="components/crops/send-button-default.png" alt="Send button (disabled, then enabled), default" height="36"> <img src="components/crops/send-button-light.png" alt="Send button (disabled, then enabled), light" height="36"> 

| State | Values |
|---|---|
| default | size 81.78 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); opacity `opacity.disabled-strong` (0.5); icon `size.icon-small` (16 x 16), `≈ text.onblack` (rgba(0, 0, 0, 0.9)) |
| enabled | opacity none |
| enabled-hover, enabled-pressed | opacity `opacity.hover` (0.9) |
| light | size 81.78 x `size.row` (36px); padding 0px `space.3` (12px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label` (System 14/20 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); opacity `opacity.disabled-strong` (0.5); icon `size.icon-small` (16 x 16), `≈ text.onblack` (#ffffff) |
| light-enabled | opacity none |
| light-enabled-hover, light-enabled-pressed | opacity `opacity.hover` (0.9) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

### Mobile

The same app at 390 wide: the app banner, the header with its menu button, the serif hero, the composer and suggestion chips, the carousel card, the drawer, the Library header with its type dropdown, and the task page.

#### App banner

<a id="m-app-banner"></a>`m-app-banner`, on mobile-home-dark.

<img src="components/crops/m-app-banner-default.png" alt="App banner, default" height="65"> <img src="components/crops/m-app-banner-light.png" alt="App banner, light" height="65"> 

| State | Values |
|---|---|
| default | size 390 x 65; padding `space.3` (12px) `space.4` (16px) `space.3` (12px) `space.1_5` (6px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); background `background.gray-main` (#1a1a1a); text System 16/22 600, `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 390 x 65; padding `space.3` (12px) `space.4` (16px) `space.3` (12px) `space.1_5` (6px); border B: `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); background `background.gray-main` (#f8f8f7); text System 16/22 600, `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-black`, `--background-gray-main`, `--border-main`, `--text-onblack`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Open app button

<a id="m-open-app"></a>`m-open-app`, on mobile-home-dark.

<img src="components/crops/m-open-app-default.png" alt="Open app button, default" height="32"> <img src="components/crops/m-open-app-light.png" alt="Open app button, light" height="32"> 

| State | Values |
|---|---|
| default | size 80.06 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (rgba(255, 255, 255, 0.95)); text `typography.role.label-compact` (System 14/18 500), `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size 80.06 x `size.row-small` (32px); padding 0px `space.2` (8px); radius `radius.small` (8px); background `button.black` (#1a1a19); text `typography.role.label-compact` (System 14/18 500), `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--Button-black`, `--text-onblack`, `--ui-density-small-row-height`.

#### Mobile header row

<a id="m-header"></a>`m-header`, on mobile-home-dark.

<img src="components/crops/m-header-default.png" alt="Mobile header row, default" height="48"> <img src="components/crops/m-header-light.png" alt="Mobile header row, light" height="48"> 

| State | Values |
|---|---|
| default | size 390 x `size.header` (48px); padding `space.2` (8px) `space.5` (20px) `space.2` (8px) `space.4` (16px); border B: `borderWidth.default` (1px) solid transparent; background `background.gray-main` (#1a1a1a); text System 16/20 500, `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `icon.secondary` (#b3b3b3) |
| light | size 390 x `size.header` (48px); padding `space.2` (8px) `space.5` (20px) `space.2` (8px) `space.4` (16px); border B: `borderWidth.default` (1px) solid transparent; background `background.gray-main` (#f8f8f7); text System 16/20 500, `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `icon.secondary` (#4d4d4d) |

Tokens named in its classes: `--background-gray-main`, `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--icon-secondary`, `--text-blue`, `--text-primary`, `--text-tertiary`.

#### Hero title (serif)

<a id="m-hero-title"></a>`m-hero-title`, on mobile-home-dark.

<img src="components/crops/m-hero-title-default.png" alt="Hero title (serif), default" height="42"> <img src="components/crops/m-hero-title-light.png" alt="Hero title (serif), light" height="42"> 

| State | Values |
|---|---|
| default | size 319.66 x 42; background transparent; text Libre Baskerville 28/42 400, `text.primary` (#e6e6e6) |
| light | size 319.66 x 42; background transparent; text Libre Baskerville 28/42 400, `text.primary` (#1a1a1a) |

Tokens named in its classes: `--text-primary`.

#### Mobile composer

<a id="m-composer"></a>`m-composer`, on mobile-home-dark.

<img src="components/crops/m-composer-default.png" alt="Mobile composer, default" height="120"> <img src="components/crops/m-composer-light.png" alt="Mobile composer, light" height="120"> 

| State | Values |
|---|---|
| default | size 358 x 120; padding `space.3` (12px) 0px; border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.composer` (22px); background `background.menu-white` (#242424); shadow `elevation.composer` (rgba(0, 0, 0, 0.02) 0px 12px 32px 0px); text System 12/16 500, `≈ text.tertiary` (#8c8c8c); icon 17 x 17, `≈ icon.secondary` (#b3b3b3); placeholder `≈ text.tertiary` (#8c8c8c) |
| light | size 358 x 120; padding `space.3` (12px) 0px; border `borderWidth.default` (1px) solid #e5e7eb; radius `radius.composer` (22px); background `background.menu-white` (#ffffff); shadow `elevation.composer` (rgba(0, 0, 0, 0.02) 0px 12px 32px 0px); text System 12/16 500, `≈ text.tertiary` (#737373); icon 17 x 17, `≈ icon.secondary` (#4d4d4d); placeholder `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--accent-send-button`, `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-white-dark`, `--fill-tsp-white-light`, `--icon-primary`, `--icon-secondary`, `--text-onblack`, `--text-primary`, `--text-secondary`, `--text-tertiary`, `--ui-density-composer-radius`, `--ui-density-content-padding`, `--ui-density-home-input-editor-min-height`, `--ui-density-outer-padding`, `--ui-density-row-gap`, `--ui-density-section-gap`, `--ui-density-small-row-height`.

#### Suggestion chip

<a id="m-chip"></a>`m-chip`, on mobile-home-dark.

<img src="components/crops/m-chip-default.png" alt="Suggestion chip, default" height="40"> <img src="components/crops/m-chip-light.png" alt="Suggestion chip, light" height="40"> 

| State | Values |
|---|---|
| default | size 136.09 x `size.control-large` (40px); padding 7px `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(255, 255, 255, 0.06)); radius `radius.full` (9999px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#e6e6e6); icon `size.icon` (18 x 18), `≈ text.tertiary` (#8c8c8c) |
| light | size 136.09 x `size.control-large` (40px); padding 7px `space.3` (12px); border `borderWidth.default` (1px) solid `border.main` (rgba(0, 0, 0, 0.06)); radius `radius.full` (9999px); background transparent; text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#1a1a1a); icon `size.icon` (18 x 18), `≈ text.tertiary` (#737373) |

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`.

#### Carousel card

<a id="m-carousel-card"></a>`m-carousel-card`, on mobile-home-dark.

<img src="components/crops/m-carousel-card-default.png" alt="Carousel card, default" height="98"> <img src="components/crops/m-carousel-card-light.png" alt="Carousel card, light" height="98"> 

| State | Values |
|---|---|
| default | size 350 x 98; radius `radius.card` (12px); background `fill.tsp-white-main` (rgba(255, 255, 255, 0.06)); text `typography.title-base` (System 16/22 500), `≈ text.primary` (#e6e6e6) |
| light | size 350 x 98; radius `radius.card` (12px); background `fill.tsp-white-main` (rgba(55, 53, 47, 0.06)); text `typography.title-base` (System 16/22 500), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--fill-tsp-white-main`, `--icon-tertiary`, `--text-primary`, `--text-tertiary`.

#### Carousel dot

<a id="m-carousel-dot"></a>`m-carousel-dot`, on mobile-home-dark.

<img src="components/crops/m-carousel-dot-default.png" alt="Carousel dot, default" height="24"> <img src="components/crops/m-carousel-dot-light.png" alt="Carousel dot, light" height="24"> <img src="components/crops/m-carousel-dot-active.png" alt="Carousel dot, active" height="24"> 

| State | Values |
|---|---|
| default | size 8 x 8; radius `radius.full` (9999px); background `fill.tsp-white-dark` (rgba(255, 255, 255, 0.08)); transition all `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| active | background `icon.disable` (#595959) |
| light | size 8 x 8; radius `radius.full` (9999px); background `fill.tsp-white-dark` (rgba(55, 53, 47, 0.08)); transition all `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light-active | background `icon.disable` (#a6a6a6) |

Tokens named in its classes: `--fill-tsp-white-dark`, `--fill-tsp-white-light`.

#### Drawer

<a id="m-drawer"></a>`m-drawer`, on mobile-home-dark-drawer.

<img src="components/crops/m-drawer-default.png" alt="Drawer, default" height="120"> <img src="components/crops/m-drawer-light.png" alt="Drawer, light" height="120"> 

| State | Values |
|---|---|
| default | size 300 x 844; background `background.nav` (#1f1f1f); text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#e6e6e6); transition width `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)), transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 28 x 28, `≈ text.primary` (#e6e6e6) |
| light | size 300 x 844; background `background.nav` (#f0f0f0); text `typography.role.nav` (System 14/21 400), `≈ text.primary` (#1a1a1a); transition width `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)), transform `duration.sidebar` (0.2s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon 28 x 28, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-nav`, `--border-light`, `--border-main`, `--fill-tsp-white-light`, `--icon-secondary`, `--text-primary`, `--text-tertiary`, `--ui-density-nav-icon-box-size`, `--ui-density-nav-item-gap`, `--ui-density-nav-item-padding-start`, `--ui-density-outer-padding`, `--ui-density-row-height`, `--ui-density-row-radius`, `--ui-font-size-sm`.

#### Drawer scrim

<a id="m-drawer-scrim"></a>`m-drawer-scrim`, on mobile-home-dark-drawer.

| State | Values |
|---|---|
| default | size 390 x 844; background `background.mask-black` (rgba(0, 0, 0, 0.45)); transition visibility 0.1s `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)), background-color 0.1s `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size 390 x 844; background `background.mask-black` (rgba(0, 0, 0, 0.65)); transition visibility 0.1s `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)), background-color 0.1s `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--background-mask-black`.

#### Mobile Library header

<a id="m-library-header"></a>`m-library-header`, on mobile-library-dark.

<img src="components/crops/m-library-header-default.png" alt="Mobile Library header, default" height="112"> <img src="components/crops/m-library-header-light.png" alt="Mobile Library header, light" height="112"> 

| State | Values |
|---|---|
| default | size 390 x 112; background `background.gray-main` (#1a1a1a); text `typography.title-lg` (System 18/24 500), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `icon.secondary` (#b3b3b3); placeholder `≈ text.disable` (#595959) |
| light | size 390 x 112; background `background.gray-main` (#f8f8f7); text `typography.title-lg` (System 18/24 500), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `icon.secondary` (#4d4d4d); placeholder `≈ text.disable` (#a6a6a6) |

Tokens named in its classes: `--Button-border-secondary`, `--background-gray-main`, `--border-main`, `--fill-tsp-gray-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--fill-white`, `--icon-secondary`, `--shadow-S`, `--text-disable`, `--text-primary`, `--text-secondary`, `--text-tertiary`, `--ui-density-input-gap`, `--ui-density-small-radius`.

#### Type dropdown button

<a id="m-type-dropdown"></a>`m-type-dropdown`, on mobile-library-dark, mobile-library-dark-type-menu.

<img src="components/crops/m-type-dropdown-default.png" alt="Type dropdown button, default" height="32"> <img src="components/crops/m-type-dropdown-light.png" alt="Type dropdown button, light" height="32"> <img src="components/crops/m-type-dropdown-open.png" alt="Type dropdown button, open" height="32"> 

| State | Values |
|---|---|
| default | size 81.11 x `size.row-small` (32px); padding 0px `space.2` (8px) 0px `space.3` (12px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(255, 255, 255, 0.12)); radius `radius.small` (8px); background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.secondary` (#b3b3b3); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#b3b3b3) |
| open | background `≈ fill.tsp-white-main` (rgba(255, 255, 255, 0.06)) |
| light | size 81.11 x `size.row-small` (32px); padding 0px `space.2` (8px) 0px `space.3` (12px); border `borderWidth.default` (1px) solid `button.border-secondary` (rgba(0, 0, 0, 0.12)); radius `radius.small` (8px); background transparent; text `typography.role.meta` (System 13/18 400), `≈ text.secondary` (#4d4d4d); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#4d4d4d) |
| light-open | background `≈ fill.tsp-white-main` (rgba(55, 53, 47, 0.06)) |

Tokens named in its classes: `--Button-border-secondary`, `--fill-tsp-white-main`, `--text-secondary`.

#### Type menu

<a id="m-type-menu"></a>`m-type-menu`, on mobile-library-dark-type-menu.

<img src="components/crops/m-type-menu-default.png" alt="Type menu, default" height="120"> <img src="components/crops/m-type-menu-light.png" alt="Type menu, light" height="120"> 

| State | Values |
|---|---|
| default | size 200 x 296; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#242424); shadow `elevation.menu` (rgba(255, 255, 255, 0.14) 0px 0px 0px 1px, rgba(0, 0, 0, 0.28) 0px 0px 0px 1px, rgba(0, 0, 0, 0.16) 0px 24px 24px -12px, rgba(0, 0, 0, 0.28) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.16) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 200 x 296; padding `space.1` (4px); radius `radius.card` (12px); background `background.menu-white` (#ffffff); shadow `elevation.menu` (rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) 0px 24px 24px -12px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px, rgba(0, 0, 0, 0.04) 0px 10px 20px 1px); text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Type menu item

<a id="m-type-menu-item"></a>`m-type-menu-item`, on mobile-library-dark-type-menu.

<img src="components/crops/m-type-menu-item-default.png" alt="Type menu item, default" height="36"> <img src="components/crops/m-type-menu-item-light.png" alt="Type menu item, light" height="36"> <img src="components/crops/m-type-menu-item-checked.png" alt="Type menu item, checked" height="36"> 

| State | Values |
|---|---|
| default | size 192 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#b3b3b3) |
| checked | icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 192 x `size.row` (36px); padding `space.2` (8px); radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.secondary` (#4d4d4d) |
| light-checked | icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--fill-tsp-white-main`, `--text-primary`, `--ui-density-menu-item-padding-y`.

#### Mobile file row

<a id="m-file-row"></a>`m-file-row`, on mobile-library-dark.

| State | Values |
|---|---|
| default | size 350 x 67; radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#e6e6e6); icon `size.icon-large` (24 x 24), `≈ text.primary` (#e6e6e6) |
| light | size 350 x 67; radius `radius.small` (8px); background transparent; text `typography.role.body` (System 14/20 400), `≈ text.primary` (#1a1a1a); icon `size.icon-large` (24 x 24), `≈ text.primary` (#1a1a1a) |

Child layers: div 350x67 border 1px solid `≈ background.tsp-menu-white` (rgba(255, 255, 255, 0.06))

Tokens named in its classes: `--border-main`, `--fill-tsp-white-light`, `--text-primary`, `--text-tertiary`.

#### Mobile deliverable card

<a id="m-task-deliverable"></a>`m-task-deliverable`, on mobile-task-dark. Scrolled to the middle of the viewport first: at the captured scroll it sits under the fixed app banner.

| State | Values |
|---|---|
| default | size 326 x 245.25; border `borderWidth.default` (1px) solid `border.dark` (rgba(255, 255, 255, 0.12)); radius `radius.card` (12px); background `background.menu-white` (#242424); text System 14/20 500 tracking -0.154px, `≈ text.primary` (#e6e6e6); icon 27 x 27, `≈ text.primary` (#e6e6e6) |
| light | size 326 x 245.25; border `borderWidth.default` (1px) solid `border.dark` (rgba(0, 0, 0, 0.14)); radius `radius.card` (12px); background `background.menu-white` (#ffffff); text System 14/20 500 tracking -0.154px, `≈ text.primary` (#1a1a1a); icon 27 x 27, `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--background-menu-white`, `--border-dark`, `--border-main`, `--fill-tsp-white-light`, `--fill-tsp-white-main`, `--text-primary`.

#### App gate screen

<a id="m-app-gate"></a>`m-app-gate`, on mobile-home-dark-app-gate.

<img src="components/crops/m-app-gate-default.png" alt="App gate screen, default" height="120"> <img src="components/crops/m-app-gate-light.png" alt="App gate screen, light" height="120"> 

| State | Values |
|---|---|
| default | size 390 x 844; background `background.gray-main` (#1a1a1a); text System 16/22 600, `≈ text.primary` (#e6e6e6); icon `size.icon-small` (16 x 16), `≈ text.primary` (#e6e6e6) |
| light | size 390 x 844; background `background.gray-main` (#f8f8f7); text System 16/22 600, `≈ text.primary` (#1a1a1a); icon `size.icon-small` (16 x 16), `≈ text.primary` (#1a1a1a) |

Tokens named in its classes: `--Button-black`, `--background-gray-main`, `--border-main`, `--text-onblack`, `--text-primary`, `--text-tertiary`, `--ui-density-small-row-height`.

#### Download app button (large black)

<a id="m-gate-download"></a>`m-gate-download`, on mobile-home-dark-app-gate.

<img src="components/crops/m-gate-download-default.png" alt="Download app button (large black), default" height="48"> <img src="components/crops/m-gate-download-light.png" alt="Download app button (large black), light" height="48"> 

| State | Values |
|---|---|
| default | size 298 x `size.header` (48px); padding 0px `space.6` (24px); radius `radius.card` (12px); background `button.black` (rgba(255, 255, 255, 0.95)); text System 16/24 500, `≈ text.onblack` (rgba(0, 0, 0, 0.9)); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |
| light | size 298 x `size.header` (48px); padding 0px `space.6` (24px); radius `radius.card` (12px); background `button.black` (#1a1a19); text System 16/24 500, `≈ text.onblack` (#ffffff); transition color and 5 more `duration.fast` (0.15s) `easing.standard` (cubic-bezier(0.4, 0, 0.2, 1)) |

Tokens named in its classes: `--Button-black`, `--text-onblack`.

#### Continue with web link

<a id="m-gate-continue"></a>`m-gate-continue`, on mobile-home-dark-app-gate.

<img src="components/crops/m-gate-continue-default.png" alt="Continue with web link, default" height="24"> <img src="components/crops/m-gate-continue-light.png" alt="Continue with web link, light" height="24"> 

| State | Values |
|---|---|
| default | size 122.27 x 20; background transparent; text `typography.role.label` (System 14/20 500), `text.tertiary` (#8c8c8c) |
| light | size 122.27 x 20; background transparent; text `typography.role.label` (System 14/20 500), `text.tertiary` (#737373) |

Tokens named in its classes: `--text-tertiary`.

## Icon index

161 distinct glyphs were lifted from the pages into [icons/](icons), every one named by its role or its Lucide name in [icons/INDEX.tsv](icons/INDEX.tsv) (the 67 icons.mjs had left as a hash were named on the 2026-10-17 refresh from the words beside them and by sight, through tools/capture/icon-names.tsv and name_icons.py). Glyphs named `brand-*` are other companies' marks (Gmail, Google Docs, Drive and Sheets, Instagram, Shopify, Windows, Apple) as Manus shows them in connectors and examples; they belong to those companies. Manus draws almost everything with Lucide (24-unit stroke icons at 2px, shown at 16 or 18) in `--icon-primary`, `--icon-secondary` or `--icon-tertiary`; the file-type icons in the Library are filled 32-unit glyphs in blue, red, orange and grey; the sidebar's task glyphs are images Manus serves from its CDN, kept under `icons/session/`.

| Icon | Where |
|---|---|
| `plus` | Projects [svg] [svg] / [svg] [svg] Hackathons // to the user / +1 Manus Desktop |
| `more-horizontal` | [svg] Plugins Plugins / More More Projects // More Projects [svg] / [svg] [svg] [svg] |
| `file-doc` | May 3 (2) / A report// 06:20 PM [svg] / Another task |
| `chevron-right` | [svg] [svg] [svg] / Hackathons Hackathons [svg] // 500 credits each / L Learner [svg] |
| `nav-new-task` | [svg] [svg] [svg] / New task New // Hackathons Hackathons [svg] / Tasks [svg] [svg] |
| `file-image` | 11:06 AM [svg] / an_image.png A project // 11:06 AM [svg] / another_image.png A project |
| `chevron-up` | More More Projects / [svg] [svg] [svg] // [svg] [svg] Tasks / [svg] [svg] [svg] |
| `check` | [svg] Task progress / Re-organize slide structure // for 5 presenters / Update slide conte |
| `logo-manus-mark` | [svg] Feb 11 / [svg] Lite Feb // 11 [svg] [svg] / [svg] Lite Feb |
| `sidebar-search` | Manus [svg] [svg] / [svg] [svg] New // [svg] [svg] Library / [svg] [svg] [svg] |
| `library-file-generic` | Jan 10 (2) / A task // 03:07 AM [svg] / A task |
| `project-folder` | [svg] [svg] [svg] / [svg] Hackathons Hackathons // [svg] [svg] [svg] / [svg] L [svg] |
| `close` | Manus Desktop [svg] / Manus Desktop [svg] // Manus Close banner / [svg] Manus app |
| `nav-computers` | New task ⌘⇧O / Computers Computers scrollable // New task Ctrl+⇧+O / Computers Computers s |
| `rating-star` | was this result? / [svg] [svg] [svg] // this result? [svg] / [svg] [svg] [svg] |
| `nav-library` | Agents Agents [svg] / Library Library [svg] // Recent tasks [svg] / Library [svg] [svg] |
| `nav-creations` | [svg] Library Library / Creations Creations [svg] // [svg] Library [svg] / Creations [svg] |
| `nav-automations` | [svg] Creations Creations / Automations Automations [svg] // [svg] [svg] [svg] / [svg] [sv |
| `nav-plugins` | [svg] Automations Automations / Plugins Plugins [svg] // [svg] [svg] [svg] / [svg] [svg] [ |
| `nav-agents` | Computers scrollable content / Agents Agents [svg] // [svg] scrollable content / [svg] [sv |
| `connect-devices` | [svg] L Learner / [svg] scrollable content // [svg] L Learner / [svg] Library [svg] |
| `bell` | L Learner [svg] / Library [svg] [svg] // L Learner [svg] / scrollable content Manus |
| `logo-manus-wordmark` | - Manus [svg] / [svg] [svg] [svg] // Manus [svg] / [svg] [svg] [svg] |
| `task-running` | Another task [svg] / A running task |
| `sidebar-collapse` | [svg] [svg] [svg] / [svg] New task |
| `share-with-friend` | a task [svg] / Share Manus with |
| `logo-cue-badge` | [svg] Agents Agents / [svg] Library Library |
| `copy` | [svg] Feb 11 / [svg] [svg][svg] Lite // for use later. / Feb 11 [svg][svg] |
| `list-filter` | Tasks [svg] [svg] / [svg] Another task |
| `chevron-down` | [svg] [svg] All / All All Text // user Step 4/4 / Task progress [svg] |
| `step-check` | for your reference. / Extract text from // [svg] Feb 11 / Deliver the Markdown |
| `logo-manus-wordmark-small` | Feb 11 [svg] / Lite Feb 11 // [svg] [svg] [svg] / Lite Feb 11 |
| `message-continue-in-new-task` | Feb 11 [svg] / [svg][svg] Lite Feb // more vibrant [svg] / How was this |
| `download` | · 104.13 KB / This is the // A file / [svg] A file |
| `composer-send` | Desktop [svg] [svg] / Manus is an // Manus Desktop [svg] / Manus is an |
| `desktop` | +1 Manus Desktop / [svg] Manus Desktop // [svg] Manus Desktop / [svg] Manus Desktop |
| `model-picker-chevron` | Manus 2.0 Lite / Free plan Upgrade // Manus 2.0 Lite / [svg] Upgrade [svg] |
| `mic` | Manus Desktop [svg] / [svg] Manus is // [svg] Manus Desktop / [svg] Manus is |
| `card-chevron` | your Video Build / Websites, apps, and // Manus Studio Create / Slides, images, and |
| `clear-filled` | [svg] Library [svg] / [svg] [svg] [svg] // [svg] Creations [svg] / [svg] [svg] All |
| `list-view` | [svg] [svg] [svg] / [svg] All [svg] // [svg] [svg] [svg] / [svg] Images [svg] |
| `share-button` | [svg] [svg] Upgrade / Share [svg] [svg] // Lite [svg] [svg] / [svg] scrollable content |
| `grid-view` | [svg] [svg] [svg] / [svg] [svg] All // [svg] [svg] [svg] / [svg] [svg] Images |
| `nav-tasks-filter` | Library [svg] [svg] / [svg] [svg] [svg] |
| `automation-expand` | 3 Sun 4 / [svg] Scheduled time // items · $128 / [svg] Checkout detected |
| `logo-manus-mark-filled` | Sun 4 [svg] / Scheduled time reached // · $128 [svg] / Checkout detected —Manus |
| `composer-chat-mode` | [svg] Manus Desktop / [svg] [svg] Manus // Desktop [svg] [svg] / [svg] [svg] Manus |
| `credits-sparkle` | Free plan Upgrade / 341 Manus Studio // Free plan Upgrade / What can I |
| `arrow-right` | skill with /skill-creator / [svg] Create a // the speaker notes. / [svg] Suggest additiona |
| `view-options-filter` | [svg] [svg] [svg] / All [svg] All // 03:02 AM [svg] / All [svg] [svg] |
| `panel-right` | [svg] Share [svg] / scrollable content [svg] // [svg] Share [svg] / scrollable content the |
| `notification-thumbnail-blank` | it with Manus. / Wed, 4:14 AM // new agent app. / Tue, 2:51 AM |
| `file-pdf` | [svg] scrollable content / Another file.pdf Another file.pdf PDF // Feb 11 [svg] / Another |
| `logo-manus-mark-outline` | Close banner [svg] / Manus app Leave // Continue with web / Get Manus on |
| `suggestion-create-slides` | double-check before use. / Create slides [svg] // [svg] Design More / Create slides [svg] |
| `upgrade-sparkle` | 2.0 Lite [svg] / Upgrade [svg] Share // 2.0 Lite [svg] / [svg] [svg] scrollable |
| `automation-back` | [svg] Detect changes / Update card [svg] // [svg] Update card / Compare plans [svg] |
| `settings-skills` | [svg] [svg] [svg] / Make the process // Personalization [svg] Connectors / Skills [svg] Ma |
| `star` | Creations [svg] [svg] / [svg] All [svg] // A project / https://example.manus.space/ [svg]  |
| `suggestion-build-website` | [svg] Create slides / Build website [svg] // [svg] Create slides / Build website More |
| `project-add` | in this project. / Add [svg] Connectors // Add [svg] Connectors / Add Files & |
| `arrow-up-right` | ⌘⇧, [svg] Homepage / [svg] Get help // [svg] Get help / [svg] Docs [svg] |
| `help` | Create a team / Get help [svg] // Upgrade [svg] Credits / 341 [svg] [svg] |
| `brand-google-docs` | your weekly report. / Weekly_report_Oct_04.md October[svg] Mon // highlighting emerging tr |
| `settings-personalization` | Beta features Capabilities / Personalization [svg] Connectors // [svg] [svg] Account / Per |
| `automation-arrow` | [svg] Monitor pricing / Detect changes [svg] // [svg] Collect feedback / Similar issues [s |
| `panel-tab-video` | Create games New / Video New [svg] // Slides [svg] Canvas / Video Close sidebar |
| `automation-condition` | when it happens. / Customized condition When // [svg] Compare plans / Customized condition |
| `calendar-previous` | own words. October / Mon 28 Tue // [svg] Weekly_report_Oct_04.md October / Mon 5 Tue |
| `filter-images` | [svg] [svg] [svg] / Images [svg] All // Slides [svg] Spreadsheets / Images [svg] Videos |
| `suggestion-design` | [svg] Video New / Design More [svg] // Files [svg] Slides / Canvas [svg] Video |
| `rename` | A task / Last active: Feb // per… [svg] Share / Rename [svg] Mark |
| `settings-connectors` | Capabilities [svg] Personalization / Connectors [svg] Skills // project. [svg] Add / Conne |
| `settings-phone` | Assets [svg] Email / Phone [svg] Wallet // Connect new computer / Control from your |
| `cloud` | PM Feb 11 / Temporary cloud computer // modified: May 3 / Last modified: May |
| `maximize` | [svg] [svg] [svg] / [svg] A report// [svg] [svg] [svg] / [svg] [svg] [svg] |
| `filter-text-pdf` | [svg] All [svg] / Text & PDF // 3 minutes per… / Files [svg] [svg] |
| `settings-general` | & Billing Settings / General [svg] Shortcuts // Account [svg] Personalization / Settings ⌘ |
| `account-switcher` | Learner Personal Personal / [svg] scrollable content // Learner Personal Personal / Free U |
| `file-doc-alt` | Feb 11 [svg] / A file.docx Feb 11 // A document / A file.docx Close |
| `settings-usage-billing` | Account [svg] Account / Usage & Billing // [svg] Free Upgrade / Credits [svg] 341 |
| `link` | [svg] [svg] [svg] /  // A document / Feb 11 [svg] |
| `settings-account` | scrollable content Account / Account [svg] Usage |
| `settings-team` | Integrations [svg] Developers / Create a team |
| `new-tab` | 3 minutes per… / New tab [svg] // [svg] [svg] [svg] / New tab Start |
| `brand-shopify` | Manus should run. / Checkout abandoned [svg] // Post improvement brief / Checkout abandone |
| `settings-email` | [svg] Computers Assets / Email [svg] Phone |
| `automation-checkout` | [svg] Checkout abandoned / 2 items · |
| `settings-data-controls` | Data & Integrations / Data controls [svg] |
| `brand-gmail` | personalized recovery email. / Recovery email draft |
| `settings-mail-manus` | Connectors [svg] Skills / Mail Manus [svg] |
| `settings-beta` | General [svg] Shortcuts / Beta features Capabilities |
| `settings-developers` | controls [svg] Integrations / Developers [svg] Create |
| `delete` | [svg] View project / Delete To pick // favorites [svg] Archive / Delete To pick |
| `settings-shortcuts` | Settings [svg] General / Shortcuts [svg] Beta |
| `settings-wallet` | Email [svg] Phone / Wallet Data & |
| `settings-integrations` | [svg] Data controls / Integrations [svg] Developers |
| `link-external` | Visit our website / To pick up |
| `sign-out` | [svg] Docs [svg] / Sign out To |
| `filter-audio` | Images [svg] Videos / Audio [svg] Others |
| `filter-slides` | scratch [svg] Files / Slides [svg] Canvas |
| `theme-dark` | Theme [svg] Light / Dark [svg] Auto |
| `mark-unread` | Share [svg] Rename / Mark as unread |
| `menu-share` | to[svg] [svg] Share / Locate in task |
| `brand-instagram` | Logged in Sheets / Post performance below |
| `menu-open-in-desktop` | in new tab / Open in desktop |
| `project-recent-tasks` | Use skills [svg] / Recent tasks [svg] |
| `attach-search-web` | tasks. [svg]Upload [svg] / Search web Skills |
| `computers-linux-server` | online. [svg]Linux Server / Have a setup |
| `computers-connect-device` | Connect your devices / Connect new computer |
| `filter-videos` | Spreadsheets [svg] Images / Videos [svg] Audio |
| `selection-quote` | escape to cancel. / Quote Cancel [svg] |
| `move-to-project` | app [svg] Pin / Move to project |
| `edit-project` | in Notion [svg] / Edit project [svg] |
| `view-options-group-by-task` | [svg] View options / Group by task |
| `settings-account-user` | [svg] 341 [svg] / Account [svg] Personalization |
| `attach-upload` | across all tasks. / Upload [svg] [svg] |
| `view-project` | [svg] Edit project / View project [svg] |
| `connector-computer-use` | in Notion [svg] / Computer Use [svg] |
| `theme-light` | English [svg] Theme / Light [svg] Dark |
| `attach-other-sources` | double-check before use. / Other sources [svg] |
| `brand-windows` | or other devices. / Windows Build & |
| `send-to-manus` | Add to favorites / Send to Manus |
| `brand-google-drive` | Other sources [svg] / Add from Google |
| `brand-instagram-small` | preparing improvement recommendations. / Post improvement brief |
| `attach` | [svg] Creations [svg] / Local files To |
| `file-pdf-small` | New invoice received / Invoice_1048.pdf [svg] [svg] |
| `archive` | Add to favorites / Archive [svg] Delete |
| `creation-url-globe` | This [svg] https://example.manus.space/ / https://example.manus.space/ Locate in |
| `theme-auto` | Light [svg] Dark / Auto Chat preferences |
| `automation-performance-drop` | performance below target / 24 hours · |
| `open-in-new-tab` | Mark as unread / Open in new |
| `brand-apple` | a cloud Mac. / macOS Xcode Host |
| `menu-pin` | in desktop app / Pin [svg] Move |
| `model-menu-check` | for everyday tasks. / Manus Flex Beta |
| `mobile-app-gate-dots` | the mobile app / You need an |
| `files-download-all` | in this task / [svg] All All |
| `library-tab-spreadsheets` | PDF [svg] Slides / Spreadsheets [svg] Images |
| `filter-others` | Videos [svg] Audio / Others To pick |
| `brand-gmail-large` | Recovery email draft / New invoice received |
| `video-play` | done for you. / Play video Download |
| `filter-files` | [svg] [svg] [svg] / Files in this |
| `brand-google-sheets` | the invoice tracker. / Saved to Drive |

## Gaps

- The thread of a running task (streaming text, the live computer view, tool cards as they appear, the Stop control) was not captured; every task capture is of a finished task. The `nav-task-running` entry is the sidebar's dashed ring for one that was still running.
- The deliverable card's slide preview is an iframe, kept as a same-size dark box in every copy; its header, menu and the file chips under it are real.
- Hover and focus on the 390-wide copies were not measured (a phone has neither), and the Library's checked view option does not exist in the mobile copy.
- The first grid-view copy (`library-dark-images-grid`) was taken before thumbnails were inlined, so its cards show the placeholder; the grouped-by-task and view-options copies have the real thumbnails.
- The Manus Flex promo dialog, the Create automation flow, a plugin's detail dialog, a creation's page, the Computers' create flow, the Account settings pane and the share sheet were not captured, since each either spends credits, changes the account or shows billing details.
- The light theme was read by removing the `dark` class from the copies, not by switching the account's theme. Everything Manus paints is a var() of the two palette blocks, so the readings match what the Light setting shows, but any image Manus swaps per theme through JavaScript rather than CSS would not have swapped.

