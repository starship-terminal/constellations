# TokenTracker components

What TokenTracker v1.4.3's dashboard is built from, read on 2026-10-17 from the local server the CLI runs (127.0.0.1:7680), no account signed in, in headless Chromium at 1440 x 900 and 2x. Every component was measured in dark (the default) and light. Each table shows the values that change across states; `=` repeats the first state.

Every value is written as the token in [tokens.json](tokens.json) that holds it: semantic names (`bg.card`, `text.secondary`) come from the table's theme set, `color.*`, `space.scale.*`, `radius.*`, `typography.*`, `shadow.*` and `motion.*` from `core`. `@ 0.7` is a token at that opacity. A value no token holds is shown raw and marked untokenised; those are one-off sizes and paddings, not part of the system. `size` is the rendered box of that instance (it follows its content). `python3 tools/catalog.py export tokentracker` resolves every name; the raw computed styles are in [raw/measurements.md](raw/measurements.md).

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`:active:hover`), so nothing was pressed; `focused` and `filled` are a field clicked into and typed into, then cleared; `open` is a menu, tooltip, toast or dialog on screen; `disabled` is a control the page itself disables; `loading` and `error` are Sessions with its request held back or aborted in the capture browser; `checked` is a Skills row ticked and then cleared. Every request that is not a read was blocked, so no state saved, synced or removed anything. Private text (paths, session titles, skill names) was replaced in the page before any crop.

## Pages captured

| Page | Shots |
|---|---|
| achievements | [achievements-dark-default](screenshots/achievements-dark-default.png), [achievements-light-default](screenshots/achievements-light-default.png) |
| dashboard | [dashboard-dark-cost-hover](screenshots/dashboard-dark-cost-hover.png), [dashboard-dark-default](screenshots/dashboard-dark-default.png), [dashboard-dark-full](screenshots/dashboard-dark-full.png), [dashboard-dark-nav-hover](screenshots/dashboard-dark-nav-hover.png), [dashboard-dark-period-week](screenshots/dashboard-dark-period-week.png), [dashboard-dark-share-open](screenshots/dashboard-dark-share-open.png), [dashboard-dark-sidebar-collapsed](screenshots/dashboard-dark-sidebar-collapsed.png), [dashboard-dark-toast](screenshots/dashboard-dark-toast.png), [dashboard-light-cost-hover](screenshots/dashboard-light-cost-hover.png), [dashboard-light-default](screenshots/dashboard-light-default.png), [dashboard-light-full](screenshots/dashboard-light-full.png), [dashboard-light-nav-hover](screenshots/dashboard-light-nav-hover.png), [dashboard-light-period-week](screenshots/dashboard-light-period-week.png), [dashboard-light-share-open](screenshots/dashboard-light-share-open.png), [dashboard-light-sidebar-collapsed](screenshots/dashboard-light-sidebar-collapsed.png), [dashboard-light-toast](screenshots/dashboard-light-toast.png) |
| limits | [limits-dark-default](screenshots/limits-dark-default.png), [limits-dark-full](screenshots/limits-dark-full.png), [limits-light-default](screenshots/limits-light-default.png), [limits-light-full](screenshots/limits-light-full.png) |
| mobile-dashboard | [mobile-dashboard-dark-default](screenshots/mobile-dashboard-dark-default.png), [mobile-dashboard-dark-menu-open](screenshots/mobile-dashboard-dark-menu-open.png), [mobile-dashboard-light-default](screenshots/mobile-dashboard-light-default.png), [mobile-dashboard-light-menu-open](screenshots/mobile-dashboard-light-menu-open.png) |
| mobile-limits | [mobile-limits-dark-default](screenshots/mobile-limits-dark-default.png), [mobile-limits-light-default](screenshots/mobile-limits-light-default.png) |
| mobile-sessions | [mobile-sessions-dark-default](screenshots/mobile-sessions-dark-default.png), [mobile-sessions-light-default](screenshots/mobile-sessions-light-default.png) |
| mobile-settings | [mobile-settings-dark-default](screenshots/mobile-settings-dark-default.png), [mobile-settings-light-default](screenshots/mobile-settings-light-default.png) |
| onboarding | [onboarding-dark-default](screenshots/onboarding-dark-default.png), [onboarding-dark-full](screenshots/onboarding-dark-full.png), [onboarding-light-default](screenshots/onboarding-light-default.png), [onboarding-light-full](screenshots/onboarding-light-full.png) |
| pet | [pet-dark-default](screenshots/pet-dark-default.png), [pet-light-default](screenshots/pet-light-default.png) |
| service-status | [service-status-dark-default](screenshots/service-status-dark-default.png), [service-status-light-default](screenshots/service-status-light-default.png) |
| sessions | [sessions-dark-default](screenshots/sessions-dark-default.png), [sessions-dark-empty](screenshots/sessions-dark-empty.png), [sessions-dark-row-hover](screenshots/sessions-dark-row-hover.png), [sessions-dark-search-focused](screenshots/sessions-dark-search-focused.png), [sessions-dark-select-open](screenshots/sessions-dark-select-open.png), [sessions-light-default](screenshots/sessions-light-default.png), [sessions-light-empty](screenshots/sessions-light-empty.png), [sessions-light-row-hover](screenshots/sessions-light-row-hover.png), [sessions-light-search-focused](screenshots/sessions-light-search-focused.png), [sessions-light-select-open](screenshots/sessions-light-select-open.png) |
| sessions-error | [sessions-error-dark-default](screenshots/sessions-error-dark-default.png), [sessions-error-light-default](screenshots/sessions-error-light-default.png) |
| sessions-loading | [sessions-loading-dark-default](screenshots/sessions-loading-dark-default.png), [sessions-loading-light-default](screenshots/sessions-loading-light-default.png) |
| settings | [settings-dark-account](screenshots/settings-dark-account.png), [settings-dark-default](screenshots/settings-dark-default.png), [settings-dark-labs](screenshots/settings-dark-labs.png), [settings-dark-network-error](screenshots/settings-dark-network-error.png), [settings-dark-network](screenshots/settings-dark-network.png), [settings-dark-segment-hover](screenshots/settings-dark-segment-hover.png), [settings-dark-usage-limits](screenshots/settings-dark-usage-limits.png), [settings-light-account](screenshots/settings-light-account.png), [settings-light-default](screenshots/settings-light-default.png), [settings-light-labs](screenshots/settings-light-labs.png), [settings-light-network-error](screenshots/settings-light-network-error.png), [settings-light-network](screenshots/settings-light-network.png), [settings-light-segment-hover](screenshots/settings-light-segment-hover.png), [settings-light-usage-limits](screenshots/settings-light-usage-limits.png) |
| skills | [skills-dark-browse](screenshots/skills-dark-browse.png), [skills-dark-confirm](screenshots/skills-dark-confirm.png), [skills-dark-default](screenshots/skills-dark-default.png), [skills-dark-selected](screenshots/skills-dark-selected.png), [skills-light-browse](screenshots/skills-light-browse.png), [skills-light-confirm](screenshots/skills-light-confirm.png), [skills-light-default](screenshots/skills-light-default.png), [skills-light-selected](screenshots/skills-light-selected.png) |
| widgets | [widgets-dark-default](screenshots/widgets-dark-default.png), [widgets-dark-full](screenshots/widgets-dark-full.png), [widgets-light-default](screenshots/widgets-light-default.png), [widgets-light-full](screenshots/widgets-light-full.png) |

## Shared values

- **Hover** changes colour: nav items and menu options take a translucent neutral wash (`bg.hover`), tabs a solid one, outlined controls a stronger border. Light-theme outlined buttons turn their text and border green on hover. Two things also grow: the primary button scales to 1.03 and a heatmap cell to 1.25.
- **Focus.** Mostly none: the stylesheet removes outlines and Tailwind rings on every element. A few controls override that with a 2px solid outline 2px out in the ink colour (`focusRing.*`, `focus.ring`): the sidebar's theme toggle, star pill and collapse chevron, and the Cloud page's buttons. Light text fields turn their border emerald on focus (`border.focus`). Everything else reads the same at `focus-visible` as at `default`.
- **Pressed** looks like hover: no scale, no darker fill. The primary button is the exception: pressed takes one more neutral step.
- **Disabled** controls are drawn, not faded: a filled neutral with muted text (`button.disabled.bg`, `text.disabled`). Switches are the exception: the whole control drops to 50% opacity.
- **Motion.** Colour transitions run 150ms (nav, tabs, selects) or 200ms (buttons, tiles, fields) on cubic-bezier(0.4, 0, 0.2, 1). The dialog eases in over 260ms on cubic-bezier(0.16, 1, 0.3, 1).
- **Radii** step 2, 4, 6, 8, 12, 16 and full; cards, the content panel and dialogs are 16, controls 8, tiles 12.

## Components

### Shell and navigation

#### Sidebar

`sidebar` on /dashboard, found by `aside`. The 220px rail on the page wash: no fill of its own, three groups, footer pills.

| dark | default |
|---|---|
| size | 220 x 900 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.text13w500`, `text.linkHover` |
| shadow | none |
| icon | `size.icon.control` |
| transition | width `motion.duration.base` |

Crops: [sidebar-default](components/crops/sidebar-default.png).

| light | default |
|---|---|
| size | 220 x 900 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.text13w500`, `text.linkHover` |
| shadow | none |
| icon | `size.icon.control` |
| transition | width `motion.duration.base` |

Crops: [sidebar.light-default](components/crops/sidebar.light-default.png).


#### Sidebar group label

`sidebar-group-label` on /dashboard, found by `leaf "Tools"`.

| dark | default |
|---|---|
| size | 204 x 35 |
| padding | `space.scale.4` `space.scale.3` `space.scale.1` `space.scale.3` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.groupLabel`, uppercase, `text.muted` |
| shadow | none |
| transition | none |

Crops: [sidebar-group-label-default](components/crops/sidebar-group-label-default.png).

| light | default |
|---|---|
| size | 204 x 35 |
| padding | `space.scale.4` `space.scale.3` `space.scale.1` `space.scale.3` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.groupLabel`, uppercase, `text.muted` |
| shadow | none |
| transition | none |

Crops: [sidebar-group-label.light-default](components/crops/sidebar-group-label.light-default.png).


#### Nav item, current

`nav-item-active` on /dashboard, found by `a[href="/dashboard"] (Tokens)`.

| dark | default | focus-visible |
|---|---|---|
| size | 204 x 32 | = |
| padding | `space.scale.1_5` `space.scale.2` | = |
| fill | `bg.navActive` | = |
| border | none | = |
| radius | `radius.lg` | = |
| text | `typography.text13w500`, `text.strong` | = |
| shadow | none | = |
| icon | `size.icon.nav` | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [nav-item-active-default](components/crops/nav-item-active-default.png), [nav-item-active-focus-visible](components/crops/nav-item-active-focus-visible.png).

| light | default | focus-visible |
|---|---|---|
| size | 204 x 32 | = |
| padding | `space.scale.1_5` `space.scale.2` | = |
| fill | `bg.navActive` | = |
| border | none | = |
| radius | `radius.lg` | = |
| text | `typography.text13w500`, `text.primary` | = |
| shadow | none | = |
| icon | `size.icon.nav` | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [nav-item-active.light-default](components/crops/nav-item-active.light-default.png), [nav-item-active.light-focus-visible](components/crops/nav-item-active.light-focus-visible.png).


#### Nav item

`nav-item` on /dashboard, found by `a[href="/sessions"]`.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 204 x 32 | = | = | = |
| padding | `space.scale.1_5` `space.scale.2` | = | = | = |
| fill | transparent | `bg.hover` | = | `bg.hover` |
| border | none | = | = | = |
| radius | `radius.lg` | = | = | = |
| text | `typography.nav`, `text.nav` | `typography.nav`, `text.strong` | = | `typography.nav`, `text.strong` |
| shadow | none | = | = | = |
| icon | `size.icon.nav` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [nav-item-default](components/crops/nav-item-default.png), [nav-item-hover](components/crops/nav-item-hover.png), [nav-item-focus-visible](components/crops/nav-item-focus-visible.png), [nav-item-pressed](components/crops/nav-item-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 204 x 32 | = | = | = |
| padding | `space.scale.1_5` `space.scale.2` | = | = | = |
| fill | transparent | `bg.hover` | = | `bg.hover` |
| border | none | = | = | = |
| radius | `radius.lg` | = | = | = |
| text | `typography.nav`, `text.nav` | `typography.nav`, `text.primary` | = | `typography.nav`, `text.primary` |
| shadow | none | = | = | = |
| icon | `size.icon.nav` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [nav-item.light-default](components/crops/nav-item.light-default.png), [nav-item.light-hover](components/crops/nav-item.light-hover.png), [nav-item.light-focus-visible](components/crops/nav-item.light-focus-visible.png), [nav-item.light-pressed](components/crops/nav-item.light-pressed.png).


#### Nav icon

`nav-icon` on /dashboard, found by `a[href="/sessions"] svg`. Lucide History at the nav size.

| dark | default |
|---|---|
| size | 15 x 15 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.nav`, `text.secondary` |
| shadow | none |
| icon | `size.icon.nav` |
| transition | none |

Crops: [nav-icon-default](components/crops/nav-icon-default.png).

| light | default |
|---|---|
| size | 15 x 15 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.nav`, `text.nav` |
| shadow | none |
| icon | `size.icon.nav` |
| transition | none |

Crops: [nav-icon.light-default](components/crops/nav-icon.light-default.png).


#### Content panel

`content-panel` on /dashboard, found by `first rounded, filled ancestor of main`. The rounded panel the pages sit in, inset from the window edge on the page wash.

| dark | default |
|---|---|
| size | 1208 x 880 |
| padding | 0px |
| fill | `bg.panel` |
| border | `border.width.default` `bg.subtle` |
| radius | `radius.2xl` |
| text | `typography.text14w600`, `text.primary` |
| shadow | `shadow.sm` |
| icon | 0px |
| transition | none |

| light | default |
|---|---|
| size | 1208 x 880 |
| padding | 0px |
| fill | `bg.panel` |
| border | `border.width.default` `border.default` |
| radius | `radius.2xl` |
| text | `typography.text14w600`, `text.primary` |
| shadow | `shadow.sm` |
| icon | 0px |
| transition | none |


#### Theme toggle

`theme-toggle` on /dashboard, found by `button[aria-label*=theme]`. One of the few controls that keeps a focus outline (.tt-sidebar-theme:focus-visible).

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 44 x 44 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.full` | = | = |
| text | `typography.body`, `focus.ring` | = | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `focus.ring`, offset `focusRing.width` |
| icon | `size.icon.small` | = | = |
| transition | none | = | = |

Crops: [theme-toggle-default](components/crops/theme-toggle-default.png), [theme-toggle-hover](components/crops/theme-toggle-hover.png), [theme-toggle-focus-visible](components/crops/theme-toggle-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 44 x 44 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.full` | = | = |
| text | `typography.body`, `focus.ring` | = | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `focus.ring`, offset `focusRing.width` |
| icon | `size.icon.small` | = | = |
| transition | none | = | = |

Crops: [theme-toggle.light-default](components/crops/theme-toggle.light-default.png), [theme-toggle.light-hover](components/crops/theme-toggle.light-hover.png), [theme-toggle.light-focus-visible](components/crops/theme-toggle.light-focus-visible.png).


#### GitHub star pill

`star-pill` on /dashboard, found by `a[href*=github]`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 63.92 x 44 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.full` | = | = |
| text | `typography.text12w500lh12`, `text.secondary` | `typography.text12w500lh12`, `text.strong` | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `text.primary`, offset `focusRing.width` |
| icon | 12px (untokenised) | = | = |
| transition | none | = | = |

Crops: [star-pill-default](components/crops/star-pill-default.png), [star-pill-hover](components/crops/star-pill-hover.png), [star-pill-focus-visible](components/crops/star-pill-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 63.92 x 44 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.full` | = | = |
| text | `typography.text12w500lh12`, `text.nav` | `typography.text12w500lh12`, `text.primary` | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `text.primary`, offset `focusRing.width` |
| icon | 12px (untokenised) | = | = |
| transition | none | = | = |

Crops: [star-pill.light-default](components/crops/star-pill.light-default.png), [star-pill.light-hover](components/crops/star-pill.light-hover.png), [star-pill.light-focus-visible](components/crops/star-pill.light-focus-visible.png).


#### Sidebar collapse button

`sidebar-toggle` on /dashboard, found by `button.tt-sidebar-toggle`. Chevron in the sidebar header; keeps a focus outline.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 44 x 44 | = | = |
| padding | 0px | = | = |
| fill | transparent | `bg.subtle` | = |
| border | none | = | = |
| radius | `radius.xl` | = | = |
| text | `typography.body`, `text.muted` | `typography.body`, `text.label` | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `text.muted`, offset `focusRing.width` |
| icon | `size.icon.control` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [sidebar-toggle-default](components/crops/sidebar-toggle-default.png), [sidebar-toggle-hover](components/crops/sidebar-toggle-hover.png), [sidebar-toggle-focus-visible](components/crops/sidebar-toggle-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 44 x 44 | = | = |
| padding | 0px | = | = |
| fill | transparent | `border.default` @ 0.6 | = |
| border | none | = | = |
| radius | `radius.xl` | = | = |
| text | `typography.body`, `text.secondary` | `typography.body`, `text.label` | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `text.secondary`, offset `focusRing.width` |
| icon | `size.icon.control` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [sidebar-toggle.light-default](components/crops/sidebar-toggle.light-default.png), [sidebar-toggle.light-hover](components/crops/sidebar-toggle.light-hover.png), [sidebar-toggle.light-focus-visible](components/crops/sidebar-toggle.light-focus-visible.png).


#### Account control (signed out)

`account-control` on /dashboard, found by `.tt-sidebar-account-control`. Top of the sidebar: the app mark and "Sign in", where a signed-in account shows its avatar. Measured only; never pressed.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 156 x 32 | = | = |
| padding | `space.scale.1_5` `space.scale.2` | = | = |
| fill | transparent | `bg.subtle` | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.text13w500`, `text.linkHover` | `typography.text13w500`, `text.strong` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [account-control-default](components/crops/account-control-default.png), [account-control-hover](components/crops/account-control-hover.png), [account-control-focus-visible](components/crops/account-control-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 156 x 32 | = | = |
| padding | `space.scale.1_5` `space.scale.2` | = | = |
| fill | transparent | `border.default` @ 0.6 | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.text13w500`, `text.linkHover` | `typography.text13w500`, `text.primary` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [account-control.light-default](components/crops/account-control.light-default.png), [account-control.light-hover](components/crops/account-control.light-hover.png), [account-control.light-focus-visible](components/crops/account-control.light-focus-visible.png).


### Buttons and segmented controls

#### Period tabs

`period-tabs` on /dashboard, found by `[role=tablist][aria-label="Time period"]`.

| dark | default |
|---|---|
| size | 599.27 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.control`, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [period-tabs-default](components/crops/period-tabs-default.png).

| light | default |
|---|---|
| size | 599.27 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.control`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [period-tabs.light-default](components/crops/period-tabs.light-default.png).


#### Period tab, selected

`period-tab-selected` on /dashboard, found by `[role=tab][aria-selected=true]`.

| dark | default | focus-visible |
|---|---|---|
| size | 60.8 x 28 | = |
| padding | `space.scale.1_5` `space.scale.3` | = |
| fill | `bg.selected` | = |
| border | none | = |
| radius | `radius.lg` | = |
| text | `typography.control`, `text.primary` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [period-tab-selected-default](components/crops/period-tab-selected-default.png), [period-tab-selected-focus-visible](components/crops/period-tab-selected-focus-visible.png).

| light | default | focus-visible |
|---|---|---|
| size | 60.8 x 28 | = |
| padding | `space.scale.1_5` `space.scale.3` | = |
| fill | `bg.selected` | = |
| border | none | = |
| radius | `radius.lg` | = |
| text | `typography.control`, `text.primary` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [period-tab-selected.light-default](components/crops/period-tab-selected.light-default.png), [period-tab-selected.light-focus-visible](components/crops/period-tab-selected.light-focus-visible.png).


#### Period tab

`period-tab` on /dashboard, found by `[role=tab][aria-selected=false]`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 46.08 x 28 | = | = |
| padding | `space.scale.1_5` `space.scale.3` | = | = |
| fill | transparent | `bg.subtle` | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.control`, `text.linkHover` | `typography.control`, `text.primary` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [period-tab-default](components/crops/period-tab-default.png), [period-tab-hover](components/crops/period-tab-hover.png), [period-tab-focus-visible](components/crops/period-tab-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 46.08 x 28 | = | = |
| padding | `space.scale.1_5` `space.scale.3` | = | = |
| fill | transparent | `bg.panel` | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.control`, `text.secondary` | `typography.control`, `text.primary` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [period-tab.light-default](components/crops/period-tab.light-default.png), [period-tab.light-hover](components/crops/period-tab.light-hover.png), [period-tab.light-focus-visible](components/crops/period-tab.light-focus-visible.png).


#### Secondary button

`share-button` on /dashboard, found by `button "Share"`. Outlined, as on Share. Measured, never pressed.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 79.41 x 32 | = | = | = |
| padding | 0px `space.scale.3` | = | = | = |
| fill | `button.secondary.bg` | = | = | = |
| border | `border.width.default` `border.strong` | = | = | = |
| radius | `radius.lg` | = | = | = |
| text | `typography.control`, `button.secondary.hoverFg` | = | = | = |
| shadow | none | = | = | = |
| icon | `size.icon.small` | = | = | = |
| transition | color, background-color +4 `motion.duration.base` | = | = | = |

Crops: [share-button-default](components/crops/share-button-default.png), [share-button-hover](components/crops/share-button-hover.png), [share-button-focus-visible](components/crops/share-button-focus-visible.png), [share-button-pressed](components/crops/share-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 79.41 x 32 | = | = | = |
| padding | 0px `space.scale.3` | = | = | = |
| fill | `button.secondary.bg` | = | = | = |
| border | `border.width.default` `border.strong` | `border.width.default` `button.secondary.hoverFg` | = | `border.width.default` `button.secondary.hoverFg` |
| radius | `radius.lg` | = | = | = |
| text | `typography.control`, `text.primary` | `typography.control`, `button.secondary.hoverFg` | = | `typography.control`, `button.secondary.hoverFg` |
| shadow | none | = | = | = |
| icon | `size.icon.small` | = | = | = |
| transition | color, background-color +4 `motion.duration.base` | = | = | = |

Crops: [share-button.light-default](components/crops/share-button.light-default.png), [share-button.light-hover](components/crops/share-button.light-hover.png), [share-button.light-focus-visible](components/crops/share-button.light-focus-visible.png), [share-button.light-pressed](components/crops/share-button.light-pressed.png).


#### Primary button

`primary-button` on /widgets, found by `a "Download Mac App"`. "Download Mac App": solid near-black in light, near-white in dark. Measured, never pressed.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 183.42 x 40 | = | = | = |
| padding | 0px `space.scale.4` | = | = | = |
| fill | `button.primary.bg` | `button.primary.hover` | = | `button.primary.pressed` |
| border | none | = | = | = |
| radius | `radius.xl` | = | = | = |
| text | `typography.rowTitle`, `text.onPrimary` | = | = | = |
| shadow | none | = | = | = |
| icon | `size.icon.control` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [primary-button-default](components/crops/primary-button-default.png), [primary-button-hover](components/crops/primary-button-hover.png), [primary-button-focus-visible](components/crops/primary-button-focus-visible.png), [primary-button-pressed](components/crops/primary-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 183.42 x 40 | = | = | = |
| padding | 0px `space.scale.4` | = | = | = |
| fill | `button.primary.bg` | `button.primary.hover` | = | `button.primary.pressed` |
| border | none | = | = | = |
| radius | `radius.xl` | = | = | = |
| text | `typography.rowTitle`, `text.onPrimary` | = | = | = |
| shadow | none | = | = | = |
| icon | `size.icon.control` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [primary-button.light-default](components/crops/primary-button.light-default.png), [primary-button.light-hover](components/crops/primary-button.light-hover.png), [primary-button.light-focus-visible](components/crops/primary-button.light-focus-visible.png), [primary-button.light-pressed](components/crops/primary-button.light-pressed.png).


#### Small segmented control

`segmented-2d` on /dashboard, found by `parent of button "2D"`. 2D / 3D switch on the heatmap.

| dark | default |
|---|---|
| size | 65.53 x 25 |
| padding | `space.scale.0_5` |
| fill | transparent |
| border | `border.width.default` `bg.subtle` |
| radius | `radius.lg` |
| text | 10px/15px 500 (untokenised), `text.primary` |
| shadow | none |
| transition | none |

Crops: [segmented-2d-default](components/crops/segmented-2d-default.png).

| light | default |
|---|---|
| size | 65.53 x 25 |
| padding | `space.scale.0_5` |
| fill | transparent |
| border | `border.width.default` `border.default` |
| radius | `radius.lg` |
| text | 10px/15px 500 (untokenised), `text.primary` |
| shadow | none |
| transition | none |

Crops: [segmented-2d.light-default](components/crops/segmented-2d.light-default.png).


#### Icon button

`icon-button` on /sessions, found by `main button[aria-label]`. Refresh at the top right. Measured, never pressed.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 36 x 36 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | `bg.subtle` | = | `bg.subtle` |
| border | `border.width.default` `bg.subtle` | = | = | = |
| radius | `radius.xl` | = | = | = |
| text | `typography.body`, `text.secondary` | `typography.body`, `text.strong` | = | `typography.body`, `text.strong` |
| shadow | none | = | = | = |
| icon | `size.icon.control` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [icon-button-default](components/crops/icon-button-default.png), [icon-button-hover](components/crops/icon-button-hover.png), [icon-button-focus-visible](components/crops/icon-button-focus-visible.png), [icon-button-pressed](components/crops/icon-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 36 x 36 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | `bg.wash` | = | `bg.wash` |
| border | `border.width.default` `border.default` | = | = | = |
| radius | `radius.xl` | = | = | = |
| text | `typography.body`, `text.nav` | `typography.body`, `text.primary` | = | `typography.body`, `text.primary` |
| shadow | none | = | = | = |
| icon | `size.icon.control` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [icon-button.light-default](components/crops/icon-button.light-default.png), [icon-button.light-hover](components/crops/icon-button.light-hover.png), [icon-button.light-focus-visible](components/crops/icon-button.light-focus-visible.png), [icon-button.light-pressed](components/crops/icon-button.light-pressed.png).


#### Segmented control

`segmented` on /settings, found by `parent of button "Compact"`.

| dark | default |
|---|---|
| size | 126.88 x 34 |
| padding | `space.scale.0_5` |
| fill | `bg.segmentTrack` |
| border | `border.width.default` `bg.subtle` |
| radius | `radius.xl` |
| text | `typography.control`, `text.strong` |
| shadow | none |
| transition | none |

Crops: [segmented-default](components/crops/segmented-default.png).

| light | default |
|---|---|
| size | 126.88 x 34 |
| padding | `space.scale.0_5` |
| fill | `bg.segmentTrack` |
| border | `border.width.default` `border.default` |
| radius | `radius.xl` |
| text | `typography.control`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [segmented.light-default](components/crops/segmented.light-default.png).


#### Segment, selected

`segment-selected` on /settings, found by `button "Compact"`.

| dark | default | focus-visible |
|---|---|---|
| size | 76.31 x 28 | = |
| padding | `space.scale.1_5` `space.scale.3` | = |
| fill | `bg.segmentSelected` | = |
| border | none | = |
| radius | `radius.lg` | = |
| text | `typography.control`, `text.strong` | = |
| shadow | `shadow.sm` | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [segment-selected-default](components/crops/segment-selected-default.png), [segment-selected-focus-visible](components/crops/segment-selected-focus-visible.png).

| light | default | focus-visible |
|---|---|---|
| size | 76.31 x 28 | = |
| padding | `space.scale.1_5` `space.scale.3` | = |
| fill | `bg.segmentSelected` | = |
| border | none | = |
| radius | `radius.lg` | = |
| text | `typography.control`, `text.primary` | = |
| shadow | `shadow.sm` | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [segment-selected.light-default](components/crops/segment-selected.light-default.png), [segment-selected.light-focus-visible](components/crops/segment-selected.light-focus-visible.png).


#### Segment

`segment` on /settings, found by `button "Full"`. Hovered and focused only; never pressed, so the setting is unchanged.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 44.56 x 28 | = | = |
| padding | `space.scale.1_5` `space.scale.3` | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.control`, `text.secondary` | `typography.control`, `text.strong` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [segment-default](components/crops/segment-default.png), [segment-hover](components/crops/segment-hover.png), [segment-focus-visible](components/crops/segment-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 44.56 x 28 | = | = |
| padding | `space.scale.1_5` `space.scale.3` | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.control`, `text.secondary` | `typography.control`, `text.primary` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [segment.light-default](components/crops/segment.light-default.png), [segment.light-hover](components/crops/segment.light-hover.png), [segment.light-focus-visible](components/crops/segment.light-focus-visible.png).


#### Retry button

`retry-button` on /sessionsError, found by `button "Try again"`. Measured, never pressed.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 79.09 x 44 | = | = |
| padding | 0px `space.scale.3` | = | = |
| fill | transparent | `bg.subtle` | = |
| border | `border.width.default` `bg.subtle` | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.control`, `text.label` | `typography.control`, `text.strong` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [retry-button-default](components/crops/retry-button-default.png), [retry-button-hover](components/crops/retry-button-hover.png), [retry-button-focus-visible](components/crops/retry-button-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 79.09 x 44 | = | = |
| padding | 0px `space.scale.3` | = | = |
| fill | transparent | `bg.wash` | = |
| border | `border.width.default` `border.default` | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.control`, `text.linkHover` | `typography.control`, `text.primary` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [retry-button.light-default](components/crops/retry-button.light-default.png), [retry-button.light-hover](components/crops/retry-button.light-hover.png), [retry-button.light-focus-visible](components/crops/retry-button.light-focus-visible.png).


#### Text link

`link` on /achievements, found by `a "Suggest it on GitHub"`. "Suggest it on GitHub" under the badges: secondary text with a light underline. Never followed.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 117.83 x 15 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 0px | = | = |
| text | `typography.caption`, `text.link` | `typography.caption`, `text.linkHover` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [link-default](components/crops/link-default.png), [link-hover](components/crops/link-hover.png), [link-focus-visible](components/crops/link-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 117.83 x 15 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 0px | = | = |
| text | `typography.caption`, `text.link` | `typography.caption`, `text.linkHover` | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [link.light-default](components/crops/link.light-default.png), [link.light-hover](components/crops/link.light-hover.png), [link.light-focus-visible](components/crops/link.light-focus-visible.png).


#### Danger button

`danger-button` on /skills, found by `last "Remove" button in the dialog`. The confirm action in the remove dialog. Hovered and focused only, never pressed.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 78.14 x 32 | = | = |
| padding | 0px `space.scale.3` | = | = |
| fill | `button.danger.bg` | `button.danger.hover` | = |
| border | `border.width.default` transparent | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.rowTitle`, `button.danger.fg` | = | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.base` | = | = |

Crops: [danger-button-default](components/crops/danger-button-default.png), [danger-button-hover](components/crops/danger-button-hover.png), [danger-button-focus-visible](components/crops/danger-button-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 78.14 x 32 | = | = |
| padding | 0px `space.scale.3` | = | = |
| fill | `button.danger.bg` | `button.danger.hover` | = |
| border | `border.width.default` transparent | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.rowTitle`, `button.danger.fg` | = | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.base` | = | = |

Crops: [danger-button.light-default](components/crops/danger-button.light-default.png), [danger-button.light-hover](components/crops/danger-button.light-hover.png), [danger-button.light-focus-visible](components/crops/danger-button.light-focus-visible.png).


#### Cancel button

`cancel-button` on /skills, found by `"Cancel" in the dialog`.

| dark | default | hover |
|---|---|---|
| size | 69.59 x 32 | = |
| padding | 0px `space.scale.3` | = |
| fill | `bg.panel` | = |
| border | `border.width.default` `border.strong` | = |
| radius | `radius.lg` | = |
| text | `typography.rowTitle`, `text.primary` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.base` | = |

Crops: [cancel-button-default](components/crops/cancel-button-default.png), [cancel-button-hover](components/crops/cancel-button-hover.png).

| light | default | hover |
|---|---|---|
| size | 69.59 x 32 | = |
| padding | 0px `space.scale.3` | = |
| fill | `bg.panel` | = |
| border | `border.width.default` `link.underline` | `border.width.default` `accent.default` |
| radius | `radius.lg` | = |
| text | `typography.rowTitle`, `text.primary` | `typography.rowTitle`, `accent.default` |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.base` | = |

Crops: [cancel-button.light-default](components/crops/cancel-button.light-default.png), [cancel-button.light-hover](components/crops/cancel-button.light-hover.png).


#### Switch, on

`switch-on` on /widgets, found by `[role=switch][aria-checked=true]`. Disabled here: the switches only work with the Mac app connected.

| dark | disabled | hover |
|---|---|---|
| size | 44 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | `radius.full` | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | none | = |

Crops: [switch-on-disabled](components/crops/switch-on-disabled.png), [switch-on-hover](components/crops/switch-on-hover.png).

| light | disabled | hover |
|---|---|---|
| size | 44 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | `radius.full` | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | none | = |

Crops: [switch-on.light-disabled](components/crops/switch-on.light-disabled.png), [switch-on.light-hover](components/crops/switch-on.light-hover.png).


#### Switch, off

`switch-off` on /pet, found by `[role=switch][aria-checked=false]`.

| dark | disabled | hover |
|---|---|---|
| size | 44 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | `radius.full` | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | none | = |

Crops: [switch-off-disabled](components/crops/switch-off-disabled.png), [switch-off-hover](components/crops/switch-off-hover.png).

| light | disabled | hover |
|---|---|---|
| size | 44 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | `radius.full` | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | none | = |

Crops: [switch-off.light-disabled](components/crops/switch-off.light-disabled.png), [switch-off.light-hover](components/crops/switch-off.light-hover.png).


#### Button, disabled

`button-disabled` on /pet, found by `button[type=submit][disabled]`. "Add" before a pet URL is typed.

| dark | disabled |
|---|---|
| size | 51.55 x 36 |
| padding | 0px `space.scale.3_5` |
| fill | `button.disabled.bg` |
| border | none |
| radius | `radius.xl` |
| text | 12px/16px 600 (untokenised), `text.disabled` |
| shadow | none |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [button-disabled-disabled](components/crops/button-disabled-disabled.png).

| light | disabled |
|---|---|
| size | 51.55 x 36 |
| padding | 0px `space.scale.3_5` |
| fill | `button.disabled.bg` |
| border | none |
| radius | `radius.xl` |
| text | 12px/16px 600 (untokenised), `text.disabled` |
| shadow | none |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [button-disabled.light-disabled](components/crops/button-disabled.light-disabled.png).


#### Cloud page button

`cloud-button` on /cloud, found by `first button in .tt-cloud-theme`. First button on the signed-out Cloud page; the Cloud page draws focus outlines. Never pressed.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 418 x 44 | = | = |
| padding | 0px `space.scale.4` | = | = |
| fill | `bg.panel` | = | = |
| border | `border.width.default` `border.strong` | `border.width.default` `text.linkHover` | = |
| radius | `radius.lg` | = | = |
| text | `typography.rowTitle`, `text.primary` | `typography.rowTitle`, `color.neutral.100` | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `color.neutral.100`, offset `focusRing.width` |
| transition | color, background-color +4 `motion.duration.base` | = | = |

Crops: [cloud-button-default](components/crops/cloud-button-default.png), [cloud-button-hover](components/crops/cloud-button-hover.png), [cloud-button-focus-visible](components/crops/cloud-button-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 418 x 44 | = | = |
| padding | 0px `space.scale.4` | = | = |
| fill | `bg.panel` | = | = |
| border | `border.width.default` `link.underline` | `border.width.default` `text.nav` | = |
| radius | `radius.lg` | = | = |
| text | `typography.rowTitle`, `text.primary` | `typography.rowTitle`, `text.label` | = |
| shadow | none | = | = |
| focus ring | - | = | `focusRing.width` `text.label`, offset `focusRing.width` |
| transition | color, background-color +4 `motion.duration.base` | = | = |

Crops: [cloud-button.light-default](components/crops/cloud-button.light-default.png), [cloud-button.light-hover](components/crops/cloud-button.light-hover.png), [cloud-button.light-focus-visible](components/crops/cloud-button.light-focus-visible.png).


#### Icon link

`icon-link` on /limits, found by `main a[href^=/settings]`. The gear on Limits ("Display settings" is its accessible label): an icon-only link to Settings.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 36 x 36 | = | = |
| padding | 0px | = | = |
| fill | transparent | `bg.subtle` | = |
| border | `border.width.default` `bg.subtle` | = | = |
| radius | `radius.xl` | = | = |
| text | `typography.body`, `text.secondary` | `typography.body`, `text.strong` | = |
| shadow | none | = | = |
| icon | `size.icon.control` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [icon-link-default](components/crops/icon-link-default.png), [icon-link-hover](components/crops/icon-link-hover.png), [icon-link-focus-visible](components/crops/icon-link-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 36 x 36 | = | = |
| padding | 0px | = | = |
| fill | transparent | `bg.wash` | = |
| border | `border.width.default` `border.default` | = | = |
| radius | `radius.xl` | = | = |
| text | `typography.body`, `text.nav` | `typography.body`, `text.primary` | = |
| shadow | none | = | = |
| icon | `size.icon.control` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [icon-link.light-default](components/crops/icon-link.light-default.png), [icon-link.light-hover](components/crops/icon-link.light-hover.png), [icon-link.light-focus-visible](components/crops/icon-link.light-focus-visible.png).


### Tokens page

#### Hero metric label

`hero-label` on /dashboard, found by `leaf "Total tokens"`. Set in uppercase by CSS (the text is "Total tokens").

| dark | default |
|---|---|
| size | 724.67 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.eyebrow`, uppercase, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [hero-label-default](components/crops/hero-label-default.png).

| light | default |
|---|---|
| size | 724.67 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.eyebrow`, uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [hero-label.light-default](components/crops/hero-label.light-default.png).


#### Hero metric

`hero-metric` on /dashboard, found by `largest text in main`. The one giant number: total tokens for the period.

| dark | default |
|---|---|
| size | 724.67 x 87 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.display`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [hero-metric-default](components/crops/hero-metric-default.png).

| light | default |
|---|---|
| size | 724.67 x 87 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.display`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [hero-metric.light-default](components/crops/hero-metric.light-default.png).


#### Hero cost

`hero-cost` on /dashboard, found by `text matching $n.nn`. Cost under the hero number, in the brand green.

| dark | default |
|---|---|
| size | 131.17 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.figure`, `accent.default` |
| shadow | none |
| icon | `size.icon.control` |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [hero-cost-default](components/crops/hero-cost-default.png).

| light | default |
|---|---|
| size | 131.17 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.figure`, `accent.default` |
| shadow | none |
| icon | `size.icon.control` |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [hero-cost.light-default](components/crops/hero-cost.light-default.png).


#### Provider share tile

`provider-tile` on /dashboard, found by `tile holding "CLAUDE"`.

| dark | default | hover |
|---|---|---|
| size | 172.17 x 96.5 | = |
| padding | `space.scale.3` | = |
| fill | transparent | = |
| border | `border.width.default` `color.neutral.700` | `border.width.default` `link.underline` |
| radius | `radius.xl` | = |
| text | `typography.rowTitle`, `text.primary` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.base` | = |

Crops: [provider-tile-default](components/crops/provider-tile-default.png), [provider-tile-hover](components/crops/provider-tile-hover.png).

| light | default | hover |
|---|---|---|
| size | 172.17 x 96.5 | = |
| padding | `space.scale.3` | = |
| fill | transparent | = |
| border | `border.width.default` `border.default` | `border.width.default` `link.underline` |
| radius | `radius.xl` | = |
| text | `typography.rowTitle`, `text.primary` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.base` | = |

Crops: [provider-tile.light-default](components/crops/provider-tile.light-default.png), [provider-tile.light-hover](components/crops/provider-tile.light-hover.png).


#### Provider share tile, all

`provider-tile-all` on /dashboard, found by `tile holding "All"`.

| dark | default |
|---|---|
| size | 172.16 x 96.5 |
| padding | `space.scale.3` |
| fill | transparent |
| border | `border.width.default` `border.strong` |
| radius | `radius.xl` |
| text | `typography.rowTitle`, `text.primary` |
| shadow | none |
| icon | `size.icon.nav` |
| transition | color, background-color +4 `motion.duration.base` |

Crops: [provider-tile-all-default](components/crops/provider-tile-all-default.png).

| light | default |
|---|---|
| size | 172.16 x 96.5 |
| padding | `space.scale.3` |
| fill | transparent |
| border | `border.width.default` `border.default` |
| radius | `radius.xl` |
| text | `typography.rowTitle`, `text.primary` |
| shadow | none |
| icon | `size.icon.nav` |
| transition | color, background-color +4 `motion.duration.base` |

Crops: [provider-tile-all.light-default](components/crops/provider-tile-all.light-default.png).


#### Stat chip

`stat-chip` on /dashboard, found by `parent of "7d"`. A small filled tile: value over a caption (7d, 30d, avg, convs).

| dark | default |
|---|---|
| size | 77.33 x 53 |
| padding | `space.scale.2` |
| fill | `bg.subtle` |
| border | none |
| radius | `radius.xl` |
| text | `typography.text14w600`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [stat-chip-default](components/crops/stat-chip-default.png).

| light | default |
|---|---|
| size | 77.33 x 53 |
| padding | `space.scale.2` |
| fill | `bg.subtle` |
| border | none |
| radius | `radius.xl` |
| text | `typography.text14w600`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [stat-chip.light-default](components/crops/stat-chip.light-default.png).


#### Card title (legacy, uppercase)

`card-title` on /dashboard, found by `leaf "Activity heatmap"`. Older cards title themselves in small tracked uppercase.

| dark | default |
|---|---|
| size | 138.94 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.sectionTitle`, uppercase, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [card-title-default](components/crops/card-title-default.png).

| light | default |
|---|---|
| size | 138.94 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.sectionTitle`, uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [card-title.light-default](components/crops/card-title.light-default.png).


#### Heatmap cell, busiest

`heatmap-cell` on /dashboard, found by `span.rounded-[2px] whose fill is farthest from the empty fill`.

| dark | default | hover |
|---|---|---|
| size | 12 x 12 | 15 x 15, scale 1.25 |
| padding | 0px | = |
| fill | `status.success` | = |
| border | none | = |
| radius | `radius.xs` | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | transform `motion.duration.fast` | = |

Crops: [heatmap-cell-default](components/crops/heatmap-cell-default.png), [heatmap-cell-hover](components/crops/heatmap-cell-hover.png).

| light | default | hover |
|---|---|---|
| size | 12 x 12 | 15 x 15, scale 1.25 |
| padding | 0px | = |
| fill | `border.focus` | = |
| border | none | = |
| radius | `radius.xs` | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | transform `motion.duration.fast` | = |

Crops: [heatmap-cell.light-default](components/crops/heatmap-cell.light-default.png), [heatmap-cell.light-hover](components/crops/heatmap-cell.light-hover.png).


#### Heatmap cell, empty

`heatmap-cell-empty` on /dashboard, found by `span.rounded-[2px] with the least saturated fill`.

| dark | default |
|---|---|
| size | 12 x 12 |
| padding | 0px |
| fill | `heatmap.0` |
| border | none |
| radius | `radius.xs` |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | transform `motion.duration.fast` |

Crops: [heatmap-cell-empty-default](components/crops/heatmap-cell-empty-default.png).

| light | default |
|---|---|
| size | 12 x 12 |
| padding | 0px |
| fill | `heatmap.0` |
| border | none |
| radius | `radius.xs` |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | transform `motion.duration.fast` |

Crops: [heatmap-cell-empty.light-default](components/crops/heatmap-cell-empty.light-default.png).


#### Hero cost button

`cost-button` on /dashboard, found by `button[aria-label="View cost breakdown"]`. The cost under the hero number is a button that opens the cost breakdown.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 131.17 x 28 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | = | = | = |
| border | none | = | = | = |
| radius | 0px | = | = | = |
| text | `typography.figure`, `accent.default` | `typography.figure`, `accent.hover` | = | `typography.figure`, `accent.pressed` |
| shadow | none | = | = | = |
| icon | `size.icon.control` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [cost-button-default](components/crops/cost-button-default.png), [cost-button-hover](components/crops/cost-button-hover.png), [cost-button-focus-visible](components/crops/cost-button-focus-visible.png), [cost-button-pressed](components/crops/cost-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 131.17 x 28 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | = | = | = |
| border | none | = | = | = |
| radius | 0px | = | = | = |
| text | `typography.figure`, `accent.default` | `typography.figure`, `accent.hover` | = | `typography.figure`, `accent.pressed` |
| shadow | none | = | = | = |
| icon | `size.icon.control` | = | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = | = |

Crops: [cost-button.light-default](components/crops/cost-button.light-default.png), [cost-button.light-hover](components/crops/cost-button.light-hover.png), [cost-button.light-focus-visible](components/crops/cost-button.light-focus-visible.png), [cost-button.light-pressed](components/crops/cost-button.light-pressed.png).


#### Card

`card` on /dashboard, found by `card around "Activity heatmap"`. The Activity heatmap card: the shared card surface.

| dark | default |
|---|---|
| size | 375.33 x 231 |
| padding | `space.scale.5` |
| fill | `bg.card` |
| border | `border.width.default` `border.default` |
| radius | `radius.2xl` |
| text | `typography.sectionTitle`, uppercase, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [card-default](components/crops/card-default.png).

| light | default |
|---|---|
| size | 375.33 x 231 |
| padding | `space.scale.5` |
| fill | `bg.card` |
| border | `border.width.default` `border.default` |
| radius | `radius.2xl` |
| text | `typography.sectionTitle`, uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [card.light-default](components/crops/card.light-default.png).


### Tables and lists

#### Table tab, selected

`table-tab-selected` on /dashboard, found by `button "Daily Breakdown"`.

| dark | default |
|---|---|
| size | 119.97 x 28 |
| padding | `space.scale.1_5` `space.scale.3` |
| fill | `bg.subtle` |
| border | none |
| radius | `radius.sm` |
| text | `typography.control`, `text.primary` |
| shadow | none |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [table-tab-selected-default](components/crops/table-tab-selected-default.png).

| light | default |
|---|---|
| size | 119.97 x 28 |
| padding | `space.scale.1_5` `space.scale.3` |
| fill | `bg.wash` |
| border | none |
| radius | `radius.sm` |
| text | `typography.control`, `text.primary` |
| shadow | none |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [table-tab-selected.light-default](components/crops/table-tab-selected.light-default.png).


#### Table tab

`table-tab` on /dashboard, found by `button "Project Usage"`.

| dark | default | hover |
|---|---|---|
| size | 105.06 x 28 | = |
| padding | `space.scale.1_5` `space.scale.3` | = |
| fill | transparent | `bg.rowHover` |
| border | none | = |
| radius | `radius.sm` | = |
| text | `typography.control`, `text.linkHover` | `typography.control`, `text.primary` |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [table-tab-default](components/crops/table-tab-default.png), [table-tab-hover](components/crops/table-tab-hover.png).

| light | default | hover |
|---|---|---|
| size | 105.06 x 28 | = |
| padding | `space.scale.1_5` `space.scale.3` | = |
| fill | transparent | `bg.panel` |
| border | none | = |
| radius | `radius.sm` | = |
| text | `typography.control`, `text.secondary` | `typography.control`, `text.primary` |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [table-tab.light-default](components/crops/table-tab.light-default.png), [table-tab.light-hover](components/crops/table-tab.light-hover.png).


#### Table header cell

`table-header` on /dashboard, found by `thead th:nth(1)`.

| dark | default |
|---|---|
| size | 102.94 x 33.3 |
| padding | 0px |
| fill | `bg.panel` |
| border | none |
| radius | 0px |
| text | `typography.tableHeader`, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [table-header-default](components/crops/table-header-default.png).

| light | default |
|---|---|
| size | 102.94 x 33.3 |
| padding | 0px |
| fill | `bg.card` |
| border | none |
| radius | 0px |
| text | `typography.tableHeader`, `text.nav` |
| shadow | none |
| transition | none |

Crops: [table-header.light-default](components/crops/table-header.light-default.png).


#### Table cell (numeric)

`table-cell` on /dashboard, found by `tbody td:nth(1)`.

| dark | default |
|---|---|
| size | 102.94 x 38 |
| padding | `space.scale.2` `space.scale.4` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.text14w400`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [table-cell-default](components/crops/table-cell-default.png).

| light | default |
|---|---|
| size | 102.94 x 38 |
| padding | `space.scale.2` `space.scale.4` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.text14w400`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [table-cell.light-default](components/crops/table-cell.light-default.png).


#### Table row

`table-row` on /dashboard, found by `tbody tr:nth(1)`.

| dark | default | hover |
|---|---|---|
| size | 756.67 x 38 | = |
| padding | 0px | = |
| fill | transparent | `bg.rowHover` |
| border | bottom `border.width.default` `bg.subtle` | = |
| radius | 0px | = |
| text | `typography.text14w400`, `text.linkHover` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [table-row-default](components/crops/table-row-default.png), [table-row-hover](components/crops/table-row-hover.png).

| light | default | hover |
|---|---|---|
| size | 756.67 x 38 | = |
| padding | 0px | = |
| fill | transparent | `bg.rowHover` |
| border | bottom `border.width.default` `bg.wash` | = |
| radius | 0px | = |
| text | `typography.text14w400`, `text.secondary` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [table-row.light-default](components/crops/table-row.light-default.png), [table-row.light-hover](components/crops/table-row.light-hover.png).


#### Summary strip

`summary-strip` on /sessions, found by `box around "Matching sessions"`. Four figures in one bordered box, split by rules.

| dark | default |
|---|---|
| size | 1070 x 48 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| icon | `size.icon.small` |
| transition | none |

Crops: [summary-strip-default](components/crops/summary-strip-default.png).

| light | default |
|---|---|
| size | 1070 x 48 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| icon | `size.icon.small` |
| transition | none |

Crops: [summary-strip.light-default](components/crops/summary-strip.light-default.png).


#### Summary label

`summary-label` on /sessions, found by `leaf "Matching sessions"`.

| dark | default |
|---|---|
| size | 267.5 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [summary-label-default](components/crops/summary-label-default.png).

| light | default |
|---|---|
| size | 267.5 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [summary-label.light-default](components/crops/summary-label.light-default.png).


#### List column header

`list-header` on /sessions, found by `leaf "Session / project"`.

| dark | default |
|---|---|
| size | 760 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [list-header-default](components/crops/list-header-default.png).

| light | default |
|---|---|
| size | 760 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [list-header.light-default](components/crops/list-header.light-default.png).


#### Session row

`list-row` on /sessions, found by `.sessions-row`.

| dark | default | hover |
|---|---|---|
| size | 1104 x 63 | = |
| padding | `space.scale.3` 0px | = |
| fill | transparent | = |
| border | `border.width.default` `bg.subtle` | = |
| radius | 0px | = |
| text | `typography.rowTitle`, `text.strong` | = |
| shadow | none | = |
| icon | `size.icon.control` | = |
| transition | none | = |

Crops: [list-row-default](components/crops/list-row-default.png), [list-row-hover](components/crops/list-row-hover.png).

| light | default | hover |
|---|---|---|
| size | 1104 x 63 | = |
| padding | `space.scale.3` 0px | = |
| fill | transparent | = |
| border | `border.width.default` `border.default` | = |
| radius | 0px | = |
| text | `typography.rowTitle`, `text.primary` | = |
| shadow | none | = |
| icon | `size.icon.control` | = |
| transition | none | = |

Crops: [list-row.light-default](components/crops/list-row.light-default.png), [list-row.light-hover](components/crops/list-row.light-hover.png).


#### Session row title

`list-row-title` on /sessions, found by `.sessions-row-title`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 61.42 x 20 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.sm` | = | = |
| text | `typography.rowTitle`, `text.strong` | = | = |
| shadow | none | = | = |
| transition | none | = | = |

Crops: [list-row-title-default](components/crops/list-row-title-default.png), [list-row-title-hover](components/crops/list-row-title-hover.png), [list-row-title-focus-visible](components/crops/list-row-title-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 61.42 x 20 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | `radius.sm` | = | = |
| text | `typography.rowTitle`, `text.primary` | = | = |
| shadow | none | = | = |
| transition | none | = | = |

Crops: [list-row-title.light-default](components/crops/list-row-title.light-default.png), [list-row-title.light-hover](components/crops/list-row-title.light-hover.png), [list-row-title.light-focus-visible](components/crops/list-row-title.light-focus-visible.png).


#### Empty state (no match)

`empty-state` on /sessions, found by `block around "No matching sessions"`. Sessions searched for text nothing matches: a title and a hint, no illustration.

| dark | default |
|---|---|
| size | 1104 x 174 |
| padding | `space.scale.16` 0px |
| fill | transparent |
| border | `border.width.default` `bg.subtle` |
| radius | `radius.2xl` |
| text | `typography.rowTitle`, `text.strong` |
| shadow | none |
| transition | none |

Crops: [empty-state-default](components/crops/empty-state-default.png).

| light | default |
|---|---|
| size | 1104 x 174 |
| padding | `space.scale.16` 0px |
| fill | transparent |
| border | `border.width.default` `border.default` |
| radius | `radius.2xl` |
| text | `typography.rowTitle`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [empty-state.light-default](components/crops/empty-state.light-default.png).


#### Loading state

`loading-state` on /sessionsLoading, found by `block around "Loading sessions…"`. Sessions with its request held back: one quiet line where the list goes.

| dark | loading |
|---|---|
| size | 1152 x 408 |
| padding | 0px `space.scale.6` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.pageTitle`, `text.strong` |
| shadow | none |
| icon | `size.icon.control` |
| transition | none |

Crops: [loading-state-loading](components/crops/loading-state-loading.png).

| light | loading |
|---|---|
| size | 1152 x 408 |
| padding | 0px `space.scale.6` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.pageTitle`, `text.primary` |
| shadow | none |
| icon | `size.icon.control` |
| transition | none |

Crops: [loading-state.light-loading](components/crops/loading-state.light-loading.png).


#### Error state

`error-state` on /sessionsError, found by `block around "Could not load sessions"`. Sessions with its request aborted: a title, the reason and Try again.

| dark | error |
|---|---|
| size | 1104 x 234 |
| padding | `space.scale.16` 0px |
| fill | transparent |
| border | `border.width.default` `button.danger.hover` @ 0.4 |
| radius | `radius.2xl` |
| text | `typography.rowTitle`, `text.strong` |
| shadow | none |
| transition | none |

Crops: [error-state-error](components/crops/error-state-error.png).

| light | error |
|---|---|
| size | 1104 x 234 |
| padding | `space.scale.16` 0px |
| fill | transparent |
| border | `border.width.default` `color.red.300` |
| radius | `radius.2xl` |
| text | `typography.rowTitle`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [error-state.light-error](components/crops/error-state.light-error.png).


### Badges, tooltips and status

#### Dialog (cost breakdown)

`dialog` on /dashboard, found by `[role=dialog]`. Opened by the hero cost button, closed with Escape.

| dark | open |
|---|---|
| size | 460 x 868 |
| padding | 0px |
| fill | `bg.dialog` |
| border | none |
| radius | `radius.2xl` |
| text | 11px/14.3px 600, letter-spacing 1.32px (untokenised), uppercase, `text.secondary` |
| shadow | `shadow.dialog.dark` |
| icon | `size.icon.control` |
| transition | opacity `motion.duration.fade`; transform `motion.duration.dialog` |

Crops: [dialog-open](components/crops/dialog-open.png).

| light | open |
|---|---|
| size | 460 x 868 |
| padding | 0px |
| fill | `bg.dialog` |
| border | none |
| radius | `radius.2xl` |
| text | 11px/14.3px 600, letter-spacing 1.32px (untokenised), uppercase, `text.secondary` |
| shadow | `shadow.dialog.light` |
| icon | `size.icon.control` |
| transition | opacity `motion.duration.fade`; transform `motion.duration.dialog` |

Crops: [dialog.light-open](components/crops/dialog.light-open.png).


#### Status badge

`status-badge` on /limits, found by `pill reading CACHED, STALE or RE-AUTH`. CACHED / STALE / RE-AUTH pill beside a limit.

| dark | default |
|---|---|
| size | 46.33 x 19.5 |
| padding | `space.scale.0_5` `space.scale.1_5` |
| fill | `bg.subtle` |
| border | `border.width.default` `border.strong` @ 0.6 |
| radius | `radius.full` |
| text | 9px/13.5px 600, letter-spacing 0.45px (untokenised), uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [status-badge-default](components/crops/status-badge-default.png).

| light | default |
|---|---|
| size | 46.33 x 19.5 |
| padding | `space.scale.0_5` `space.scale.1_5` |
| fill | `bg.panel` |
| border | `border.width.default` `border.default` @ 0.6 |
| radius | `radius.full` |
| text | 9px/13.5px 600, letter-spacing 0.45px (untokenised), uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [status-badge.light-default](components/crops/status-badge.light-default.png).


#### Service status row

`status-row` on /status, found by `row around "Claude"`.

| dark | default | hover |
|---|---|---|
| size | 544 x 106 | = |
| padding | `space.scale.5` | = |
| fill | `bg.panel` | `bg.hover` |
| border | `border.width.default` `bg.subtle` | `border.width.default` `border.strong` |
| radius | `radius.2xl` | = |
| text | 16px/24px 500 (untokenised), `text.primary` | = |
| shadow | none | = |
| icon | `size.icon.control` | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [status-row-default](components/crops/status-row-default.png), [status-row-hover](components/crops/status-row-hover.png).

| light | default | hover |
|---|---|---|
| size | 544 x 106 | = |
| padding | `space.scale.5` | = |
| fill | `bg.card` | `bg.panel` |
| border | `border.width.default` `border.default` | `border.width.default` `link.underline` |
| radius | `radius.2xl` | = |
| text | 16px/24px 500 (untokenised), `text.primary` | = |
| shadow | none | = |
| icon | `size.icon.control` | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [status-row.light-default](components/crops/status-row.light-default.png), [status-row.light-hover](components/crops/status-row.light-hover.png).


#### Tooltip

`tooltip` on /dashboard, found by `node that appears on hovering the busiest heatmap cell`. Hovering a heatmap cell: the day, its tokens and the timezone.

| dark | open |
|---|---|
| size | 235.13 x 218.5 |
| padding | `space.scale.3_5` |
| fill | `bg.panel` @ 0.95 |
| border | `border.width.default` `bg.rowHover` |
| radius | `radius.2xl` |
| text | 11px/16.5px 600 (untokenised), `text.secondary` |
| shadow | `shadow.xl` |
| transition | all 100ms (untokenised) |

Crops: [tooltip-open](components/crops/tooltip-open.png).

| light | open |
|---|---|
| size | 235.13 x 218.5 |
| padding | `space.scale.3_5` |
| fill | `bg.card` @ 0.95 |
| border | `border.width.default` `bg.hover` |
| radius | `radius.2xl` |
| text | 11px/16.5px 600 (untokenised), `text.secondary` |
| shadow | `shadow.xl` |
| transition | all 100ms (untokenised) |

Crops: [tooltip.light-open](components/crops/tooltip.light-open.png).


#### Dialog scrim

`dialog-scrim` on /dashboard, found by `fixed full-window layer behind [role=dialog]`. The full-window layer behind the open dialog.

| dark | open |
|---|---|
| size | 1440 x 900 |
| padding | 0px |
| fill | `bg.scrim` |
| border | none |
| radius | 0px |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | opacity `motion.duration.base` |

| light | open |
|---|---|
| size | 1440 x 900 |
| padding | 0px |
| fill | `bg.scrim` |
| border | none |
| radius | 0px |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | opacity `motion.duration.base` |


#### Dialog (share card)

`share-dialog` on /dashboard, found by `[role=dialog] after Share`. Opened by Share; the image is drawn in the browser.

| dark | open |
|---|---|
| size | 1440 x 900 |
| padding | `space.scale.6` |
| fill | `bg.wash` @ 0.72 |
| border | none |
| radius | 0px |
| text | 20px/24px 500 (untokenised), `text.strong` @ 0.45 |
| shadow | none |
| icon | 22px (untokenised) |
| transition | none |

Crops: [share-dialog-open](components/crops/share-dialog-open.png).

| light | open |
|---|---|
| size | 1440 x 900 |
| padding | `space.scale.6` |
| fill | `text.primary` @ 0.72 |
| border | none |
| radius | 0px |
| text | 20px/24px 500 (untokenised), `bg.card` @ 0.45 |
| shadow | none |
| icon | 22px (untokenised) |
| transition | none |

Crops: [share-dialog.light-open](components/crops/share-dialog.light-open.png).


#### Toast

`toast` on /dashboard, found by `node that appears after Copy`. Feedback after Copy on the share card.

| dark | open |
|---|---|
| size | 174.45 x 32 |
| padding | `space.scale.2` `space.scale.4` |
| fill | `status.danger.fill` |
| border | none |
| radius | `radius.full` |
| text | `typography.control`, `status.danger.text` |
| shadow | `shadow.md` |
| transition | none |

Crops: [toast-open](components/crops/toast-open.png).

| light | open |
|---|---|
| size | 174.45 x 32 |
| padding | `space.scale.2` `space.scale.4` |
| fill | `status.danger.fill` |
| border | none |
| radius | `radius.full` |
| text | `typography.control`, `status.danger.text` |
| shadow | `shadow.md` |
| transition | none |

Crops: [toast.light-open](components/crops/toast.light-open.png).


#### Confirmation dialog (destructive)

`confirm-dialog` on /skills, found by `[role=dialog] after bulk Remove`. Bulk Remove on Skills asks first. Cancelled with Escape.

| dark | open |
|---|---|
| size | 448 x 180 |
| padding | `space.scale.6` |
| fill | `bg.overlay` |
| border | none |
| radius | `radius.2xl` |
| text | 16px/24px 600 (untokenised), `text.strong` |
| shadow | `shadow.dialog.dark` |
| transition | opacity, transform `motion.duration.fade` |

Crops: [confirm-dialog-open](components/crops/confirm-dialog-open.png).

| light | open |
|---|---|
| size | 448 x 180 |
| padding | `space.scale.6` |
| fill | `bg.overlay` |
| border | none |
| radius | `radius.2xl` |
| text | 16px/24px 600 (untokenised), `text.primary` |
| shadow | `shadow.dialog.light` |
| transition | opacity, transform `motion.duration.fade` |

Crops: [confirm-dialog.light-open](components/crops/confirm-dialog.light-open.png).


#### Confirmation scrim

`confirm-scrim` on /skills, found by `fixed full-window layer behind the dialog`.

| dark | open |
|---|---|
| size | 1440 x 900 |
| padding | 0px |
| fill | #00000066 (untokenised) |
| border | none |
| radius | 0px |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | opacity `motion.duration.base` |

| light | open |
|---|---|
| size | 1440 x 900 |
| padding | 0px |
| fill | `bg.scrim` |
| border | none |
| radius | 0px |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | opacity `motion.duration.base` |


#### Tooltip (hint)

`hint-tooltip` on /limits, found by `absolute span that appears on hovering the pill`. Hovering the CACHED pill on Limits.

| dark | open |
|---|---|
| size | 192 x 44 |
| padding | `space.scale.1_5` `space.scale.2_5` |
| fill | `bg.subtle` |
| border | `border.width.default` `border.strong` |
| radius | `radius.lg` |
| text | `typography.groupLabel` with letter-spacing 0px, `text.strong` |
| shadow | `shadow.lgBare` |
| transition | all `motion.duration.base` |

Crops: [hint-tooltip-open](components/crops/hint-tooltip-open.png).

| light | open |
|---|---|
| size | 192 x 44 |
| padding | `space.scale.1_5` `space.scale.2_5` |
| fill | `text.label` |
| border | `border.width.default` `button.primary.hover` |
| radius | `radius.lg` |
| text | `typography.groupLabel` with letter-spacing 0px, `bg.card` |
| shadow | `shadow.lgBare` |
| transition | all `motion.duration.base` |

Crops: [hint-tooltip.light-open](components/crops/hint-tooltip.light-open.png).


#### Badge

`badge` on /skills, found by `leaf "Plugin"`. The neutral pill on a skill row ("Plugin").

| dark | default |
|---|---|
| size | 43.45 x 19 |
| padding | `space.scale.0_5` `space.scale.1_5` |
| fill | `bg.subtle` |
| border | none |
| radius | `radius.full` |
| text | `typography.badge`, `text.linkHover` |
| shadow | `shadow.ring.dark` |
| transition | none |

Crops: [badge-default](components/crops/badge-default.png).

| light | default |
|---|---|
| size | 43.45 x 19 |
| padding | `space.scale.0_5` `space.scale.1_5` |
| fill | `bg.wash` |
| border | none |
| radius | `radius.full` |
| text | `typography.badge`, `text.nav` |
| shadow | `shadow.ring.light` |
| transition | none |

Crops: [badge.light-default](components/crops/badge.light-default.png).


### Page header

#### Page title

`page-title` on /sessions, found by `main h1`.

| dark | default |
|---|---|
| size | 304.95 x 40 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.pageTitle`, `text.strong` |
| shadow | none |
| transition | none |

Crops: [page-title-default](components/crops/page-title-default.png).

| light | default |
|---|---|
| size | 304.95 x 40 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.pageTitle`, `text.strong` |
| shadow | none |
| transition | none |

Crops: [page-title.light-default](components/crops/page-title.light-default.png).


#### Page subtitle

`page-subtitle` on /sessions, found by `main h1 + p`.

| dark | default |
|---|---|
| size | 304.95 x 24 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.body`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [page-subtitle-default](components/crops/page-subtitle-default.png).

| light | default |
|---|---|
| size | 304.95 x 24 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.body`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [page-subtitle.light-default](components/crops/page-subtitle.light-default.png).


### Fields and selects

#### Search field

`search-field` on /sessions, found by `input[placeholder^=Search] parent`.

| dark | default | hover |
|---|---|---|
| size | 400 x 36 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 0px | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | none | = |

Crops: [search-field-default](components/crops/search-field-default.png), [search-field-hover](components/crops/search-field-hover.png).

| light | default | hover |
|---|---|---|
| size | 400 x 36 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 0px | = |
| text | `typography.body`, `text.primary` | = |
| shadow | none | = |
| transition | none | = |

Crops: [search-field.light-default](components/crops/search-field.light-default.png), [search-field.light-hover](components/crops/search-field.light-hover.png).


#### Search input

`search-input` on /sessions, found by `input[placeholder^=Search]`. A model name was typed and deleted; nothing was sent.

| dark | default | focused | filled |
|---|---|---|---|
| size | 400 x 36 | = | = |
| padding | 0px 48px (untokenised) 0px `space.scale.10` | = | = |
| fill | `bg.field` | = | = |
| border | `border.width.default` `bg.subtle` | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.bodySmall`, `text.primary` | = | = |
| shadow | none | = | = |
| transition | all `motion.duration.base` | = | = |

Crops: [search-input-default](components/crops/search-input-default.png), [search-input-focused](components/crops/search-input-focused.png), [search-input-filled](components/crops/search-input-filled.png).

| light | default | focused | filled |
|---|---|---|---|
| size | 400 x 36 | = | = |
| padding | 0px 48px (untokenised) 0px `space.scale.10` | = | = |
| fill | `bg.field` | = | = |
| border | `border.width.default` `border.default` | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.bodySmall`, `text.primary` | = | = |
| shadow | none | = | = |
| transition | all `motion.duration.base` | = | = |

Crops: [search-input.light-default](components/crops/search-input.light-default.png), [search-input.light-focused](components/crops/search-input.light-focused.png), [search-input.light-filled](components/crops/search-input.light-filled.png).


#### Select button

`select` on /sessions, found by `button holding "All tools"`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 168 x 36 | = | = |
| padding | 0px `space.scale.3` | = | = |
| fill | `bg.raised` | = | = |
| border | `border.width.default` `bg.subtle` | `border.width.default` `border.hover` | = |
| radius | `radius.md` | = | = |
| text | `typography.bodySmall`, `text.strong` | = | = |
| shadow | none | = | = |
| icon | `size.icon.small` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [select-default](components/crops/select-default.png), [select-hover](components/crops/select-hover.png), [select-focus-visible](components/crops/select-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 168 x 36 | = | = |
| padding | 0px `space.scale.3` | = | = |
| fill | `bg.card` | = | = |
| border | `border.width.default` `border.default` | `border.width.default` `border.hover` | = |
| radius | `radius.md` | = | = |
| text | `typography.bodySmall`, `text.primary` | = | = |
| shadow | none | = | = |
| icon | `size.icon.small` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [select.light-default](components/crops/select.light-default.png), [select.light-hover](components/crops/select.light-hover.png), [select.light-focus-visible](components/crops/select.light-focus-visible.png).


#### Select menu

`select-menu` on /sessions, found by `[role=listbox]`.

| dark | open |
|---|---|
| size | 158 x 196 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.strong` |
| shadow | none |
| icon | 12px (untokenised) |
| transition | none |

Crops: [select-menu-open](components/crops/select-menu-open.png).

| light | open |
|---|---|
| size | 158 x 196 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.primary` |
| shadow | none |
| icon | 12px (untokenised) |
| transition | none |

Crops: [select-menu.light-open](components/crops/select-menu.light-open.png).


#### Select option, selected

`select-option-selected` on /sessions, found by `first option`.

| dark | open |
|---|---|
| size | 158 x 28 |
| padding | `space.scale.1_5` `space.scale.6` `space.scale.1_5` `space.scale.1_5` |
| fill | `bg.subtle` @ 0.7 |
| border | none |
| radius | `radius.xl` |
| text | `typography.caption`, `text.strong` |
| shadow | none |
| icon | 12px (untokenised) |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [select-option-selected-open](components/crops/select-option-selected-open.png).

| light | open |
|---|---|
| size | 158 x 28 |
| padding | `space.scale.1_5` `space.scale.6` `space.scale.1_5` `space.scale.1_5` |
| fill | `bg.wash` |
| border | none |
| radius | `radius.xl` |
| text | `typography.caption`, `text.primary` |
| shadow | none |
| icon | 12px (untokenised) |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [select-option-selected.light-open](components/crops/select-option-selected.light-open.png).


#### Select option

`select-option` on /sessions, found by `second option`.

| dark | open | hover |
|---|---|---|
| size | 158 x 28 | = |
| padding | `space.scale.1_5` `space.scale.6` `space.scale.1_5` `space.scale.1_5` | = |
| fill | transparent | `bg.hover` |
| border | none | = |
| radius | `radius.xl` | = |
| text | `typography.caption`, `text.linkHover` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [select-option-open](components/crops/select-option-open.png), [select-option-hover](components/crops/select-option-hover.png).

| light | open | hover |
|---|---|---|
| size | 158 x 28 | = |
| padding | `space.scale.1_5` `space.scale.6` `space.scale.1_5` `space.scale.1_5` | = |
| fill | transparent | `bg.panel` |
| border | none | = |
| radius | `radius.xl` | = |
| text | `typography.caption`, `text.nav` | = |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [select-option.light-open](components/crops/select-option.light-open.png), [select-option.light-hover](components/crops/select-option.light-hover.png).


#### Checkbox

`checkbox` on /skills, found by `first input[type=checkbox] on Skills`.

| dark | default | hover | focus-visible | checked |
|---|---|---|---|---|
| size | 16 x 16 | = | = | = |
| padding | 0px | = | = | = |
| fill | `bg.panel` | = | = | = |
| border | none | = | = | = |
| radius | 0px | = | = | = |
| text | `typography.body`, `text.strong` | = | = | = |
| shadow | none | = | = | = |
| transition | none | = | = | = |

Crops: [checkbox-default](components/crops/checkbox-default.png), [checkbox-hover](components/crops/checkbox-hover.png), [checkbox-focus-visible](components/crops/checkbox-focus-visible.png), [checkbox-checked](components/crops/checkbox-checked.png).

| light | default | hover | focus-visible | checked |
|---|---|---|---|---|
| size | 16 x 16 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | = | = | = |
| border | none | = | = | = |
| radius | 0px | = | = | = |
| text | `typography.body`, `text.primary` | = | = | = |
| shadow | none | = | = | = |
| transition | none | = | = | = |

Crops: [checkbox.light-default](components/crops/checkbox.light-default.png), [checkbox.light-hover](components/crops/checkbox.light-hover.png), [checkbox.light-focus-visible](components/crops/checkbox.light-focus-visible.png), [checkbox.light-checked](components/crops/checkbox.light-checked.png).


#### Select, disabled

`select-disabled` on /widgets, found by `button[role=combobox][disabled]`.

| dark | disabled |
|---|---|
| size | 455 x 38 |
| padding | `space.scale.2` `space.scale.3` |
| fill | `bg.panel` |
| border | `border.width.default` `bg.subtle` |
| radius | `radius.xl` |
| text | `typography.rowTitle`, `text.strong` |
| shadow | none |
| icon | `size.icon.small` |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [select-disabled-disabled](components/crops/select-disabled-disabled.png).

| light | disabled |
|---|---|
| size | 455 x 38 |
| padding | `space.scale.2` `space.scale.3` |
| fill | `bg.card` |
| border | `border.width.default` `border.default` |
| radius | `radius.xl` |
| text | `typography.rowTitle`, `text.primary` |
| shadow | none |
| icon | `size.icon.small` |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [select-disabled.light-disabled](components/crops/select-disabled.light-disabled.png).


#### Text field

`text-field` on /settings, found by `first text input in Network settings`. Settings, Network: proxy host. Focus changes the border only.

| dark | default | hover | focused |
|---|---|---|---|
| size | 176 x 34 | = | = |
| padding | `space.scale.1_5` `space.scale.2_5` | = | = |
| fill | transparent | = | = |
| border | `border.width.default` `border.focus` | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.bodySmall`, `text.strong` | = | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [text-field-default](components/crops/text-field-default.png), [text-field-hover](components/crops/text-field-hover.png), [text-field-focused](components/crops/text-field-focused.png).

| light | default | hover | focused |
|---|---|---|---|
| size | 176 x 34 | = | = |
| padding | `space.scale.1_5` `space.scale.2_5` | = | = |
| fill | transparent | = | = |
| border | `border.width.default` `link.underline` | = | `border.width.default` `border.focus` |
| radius | `radius.lg` | = | = |
| text | `typography.bodySmall`, `text.primary` | = | = |
| shadow | none | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [text-field.light-default](components/crops/text-field.light-default.png), [text-field.light-hover](components/crops/text-field.light-hover.png), [text-field.light-focused](components/crops/text-field.light-focused.png).


#### Field error message

`field-error` on /settings, found by `leaf "Enter a host ..."`. Replaces the field hint when Test connection finds an invalid host.

| dark | default |
|---|---|
| size | 534 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [field-error-default](components/crops/field-error-default.png).

| light | default |
|---|---|
| size | 534 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [field-error.light-default](components/crops/field-error.light-default.png).


#### Text field, invalid

`text-field-error` on /settings, found by `the same input holding an invalid host`.

| dark | error |
|---|---|
| size | 176 x 34 |
| padding | `space.scale.1_5` `space.scale.2_5` |
| fill | transparent |
| border | `border.width.default` `border.strong` |
| radius | `radius.lg` |
| text | `typography.bodySmall`, `text.strong` |
| shadow | none |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [text-field-error-error](components/crops/text-field-error-error.png).

| light | error |
|---|---|
| size | 176 x 34 |
| padding | `space.scale.1_5` `space.scale.2_5` |
| fill | transparent |
| border | `border.width.default` `link.underline` |
| radius | `radius.lg` |
| text | `typography.bodySmall`, `text.primary` |
| shadow | none |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [text-field-error.light-error](components/crops/text-field-error.light-error.png).


### Limits

#### Limits card

`limits-card` on /limits, found by `card around the "Usage limits" title`.

| dark | default |
|---|---|
| size | 1104 x 2417.69 |
| padding | 0px |
| fill | `bg.panel` |
| border | `border.width.default` `bg.subtle` |
| radius | `radius.2xl` |
| text | `typography.sectionTitle`, uppercase, `text.linkHover` |
| shadow | none |
| icon | `size.icon.small` |
| transition | color, background-color +4 `motion.duration.base` |

| light | default |
|---|---|
| size | 1104 x 2417.69 |
| padding | 0px |
| fill | `bg.card` |
| border | `border.width.default` `border.default` |
| radius | `radius.2xl` |
| text | `typography.sectionTitle`, uppercase, `text.secondary` |
| shadow | none |
| icon | `size.icon.small` |
| transition | color, background-color +4 `motion.duration.base` |


#### Limits card title

`limits-title` on /limits, found by `leaf "Usage limits"`.

| dark | default |
|---|---|
| size | 1062 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.sectionTitle`, uppercase, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [limits-title-default](components/crops/limits-title-default.png).

| light | default |
|---|---|
| size | 1062 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.sectionTitle`, uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [limits-title.light-default](components/crops/limits-title.light-default.png).


#### Usage row

`usage-row` on /limits, found by `row around the first track`. Window label, a thin track with a pace tick, percent and time left.

| dark | default |
|---|---|
| size | 1062 x 16.5 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 10.5px/14.4375px 400 (untokenised), `text.label` |
| shadow | none |
| transition | none |

Crops: [usage-row-default](components/crops/usage-row-default.png).

| light | default |
|---|---|
| size | 1062 x 16.5 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 10.5px/14.4375px 400 (untokenised), `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [usage-row.light-default](components/crops/usage-row.light-default.png).


#### Usage track

`usage-track` on /limits, found by `first track`.

| dark | default |
|---|---|
| size | 931 x 6 |
| padding | 0px |
| fill | `usage.track` |
| border | none |
| radius | `radius.full` |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [usage-track-default](components/crops/usage-track-default.png).

| light | default |
|---|---|
| size | 931 x 6 |
| padding | 0px |
| fill | `usage.track` |
| border | none |
| radius | `radius.full` |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | none |

Crops: [usage-track.light-default](components/crops/usage-track.light-default.png).


#### Usage fill

`usage-fill` on /limits, found by `its fill`.

| dark | default |
|---|---|
| size | 335.16 x 6 |
| padding | 0px |
| fill | `accent.fill` |
| border | none |
| radius | `radius.full` |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | width 500ms (untokenised) |

Crops: [usage-fill-default](components/crops/usage-fill-default.png).

| light | default |
|---|---|
| size | 335.16 x 6 |
| padding | 0px |
| fill | `accent.fill` |
| border | none |
| radius | `radius.full` |
| text | `typography.body`, `text.primary` |
| shadow | none |
| transition | width 500ms (untokenised) |

Crops: [usage-fill.light-default](components/crops/usage-fill.light-default.png).


#### Code block

`code-block` on /limits, found by `main pre`.

| dark | default |
|---|---|
| size | 1040 x 51.38 |
| padding | `space.scale.1_5` `space.scale.2` |
| fill | `bg.code` |
| border | none |
| radius | `radius.sm` |
| text | `typography.code`, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [code-block-default](components/crops/code-block-default.png).

| light | default |
|---|---|
| size | 1040 x 51.38 |
| padding | `space.scale.1_5` `space.scale.2` |
| fill | `bg.code` |
| border | none |
| radius | `radius.sm` |
| text | `typography.code`, `text.nav` |
| shadow | none |
| transition | none |

Crops: [code-block.light-default](components/crops/code-block.light-default.png).


### Settings

#### Settings nav item, current

`subnav-item-active` on /settings, found by `button "Appearance"`.

| dark | default |
|---|---|
| size | 176 x 40 |
| padding | `space.scale.2` `space.scale.3` |
| fill | `bg.subtle` |
| border | none |
| radius | `radius.lg` |
| text | `typography.rowTitle`, `text.strong` |
| shadow | none |
| icon | `size.icon.control` |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [subnav-item-active-default](components/crops/subnav-item-active-default.png).

| light | default |
|---|---|
| size | 176 x 40 |
| padding | `space.scale.2` `space.scale.3` |
| fill | `bg.wash` |
| border | none |
| radius | `radius.lg` |
| text | `typography.rowTitle`, `text.primary` |
| shadow | none |
| icon | `size.icon.control` |
| transition | color, background-color +4 `motion.duration.fast` |

Crops: [subnav-item-active.light-default](components/crops/subnav-item-active.light-default.png).


#### Settings nav item

`subnav-item` on /settings, found by `button "Account"`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 176 x 40 | = | = |
| padding | `space.scale.2` `space.scale.3` | = | = |
| fill | transparent | `bg.panel` | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.rowTitle`, `text.secondary` | `typography.rowTitle`, `text.label` | = |
| shadow | none | = | = |
| icon | `size.icon.control` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [subnav-item-default](components/crops/subnav-item-default.png), [subnav-item-hover](components/crops/subnav-item-hover.png), [subnav-item-focus-visible](components/crops/subnav-item-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 176 x 40 | = | = |
| padding | `space.scale.2` `space.scale.3` | = | = |
| fill | transparent | `bg.panel` | = |
| border | none | = | = |
| radius | `radius.lg` | = | = |
| text | `typography.rowTitle`, `text.secondary` | `typography.rowTitle`, `text.label` | = |
| shadow | none | = | = |
| icon | `size.icon.control` | = | = |
| transition | color, background-color +4 `motion.duration.fast` | = | = |

Crops: [subnav-item.light-default](components/crops/subnav-item.light-default.png), [subnav-item.light-hover](components/crops/subnav-item.light-hover.png), [subnav-item.light-focus-visible](components/crops/subnav-item.light-focus-visible.png).


#### Settings nav group label

`subnav-group-label` on /settings, found by `leaf "App"`.

| dark | default |
|---|---|
| size | 176 x 19 |
| padding | 0px `space.scale.3` `space.scale.1` `space.scale.3` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.badge` with letter-spacing 1.6px, uppercase, `text.muted` |
| shadow | none |
| transition | none |

Crops: [subnav-group-label-default](components/crops/subnav-group-label-default.png).

| light | default |
|---|---|
| size | 176 x 19 |
| padding | 0px `space.scale.3` `space.scale.1` `space.scale.3` |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.badge` with letter-spacing 1.6px, uppercase, `text.disabled` |
| shadow | none |
| transition | none |

Crops: [subnav-group-label.light-default](components/crops/subnav-group-label.light-default.png).


#### Section title

`section-title` on /settings, found by `main h2`.

| dark | default |
|---|---|
| size | 726 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.sectionTitle`, uppercase, `text.linkHover` |
| shadow | none |
| transition | none |

Crops: [section-title-default](components/crops/section-title-default.png).

| light | default |
|---|---|
| size | 726 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.sectionTitle`, uppercase, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [section-title.light-default](components/crops/section-title.light-default.png).


#### Settings card

`settings-card` on /settings, found by `card around "Theme"`.

| dark | default |
|---|---|
| size | 726 x 377 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.bodySmall`, `text.label` |
| shadow | none |
| icon | `size.icon.small` |
| transition | none |

| light | default |
|---|---|
| size | 726 x 377 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.bodySmall`, `text.label` |
| shadow | none |
| icon | `size.icon.small` |
| transition | none |


#### Setting label

`setting-label` on /settings, found by `leaf "Theme"`.

| dark | default |
|---|---|
| size | 472.7 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.bodySmall`, `text.label` |
| shadow | none |
| transition | none |

Crops: [setting-label-default](components/crops/setting-label-default.png).

| light | default |
|---|---|
| size | 472.7 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.bodySmall`, `text.label` |
| shadow | none |
| transition | none |

Crops: [setting-label.light-default](components/crops/setting-label.light-default.png).


#### Setting description

`setting-description` on /settings, found by `leaf description`.

| dark | default |
|---|---|
| size | 472.7 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [setting-description-default](components/crops/setting-description-default.png).

| light | default |
|---|---|
| size | 472.7 x 16 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | `typography.caption`, `text.secondary` |
| shadow | none |
| transition | none |

Crops: [setting-description.light-default](components/crops/setting-description.light-default.png).


#### Footer link

`footer-link` on /settings, found by `button "Check for updates"`.

| dark | default | hover |
|---|---|---|
| size | 103.95 x 16 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 0px | = |
| text | `typography.caption`, `text.muted` | `typography.caption`, `text.linkHover` |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [footer-link-default](components/crops/footer-link-default.png), [footer-link-hover](components/crops/footer-link-hover.png).

| light | default | hover |
|---|---|---|
| size | 103.95 x 16 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 0px | = |
| text | `typography.caption`, `text.secondary` | `typography.caption`, `text.linkHover` |
| shadow | none | = |
| transition | color, background-color +4 `motion.duration.fast` | = |

Crops: [footer-link.light-default](components/crops/footer-link.light-default.png), [footer-link.light-hover](components/crops/footer-link.light-hover.png).


## Icons

36 Lucide icons (lucide-react, stroke 2, `currentColor`), named by their Lucide class, in [icons/](icons) with [icons/INDEX.tsv](icons/INDEX.tsv). Nav icons render at 15px, control icons at 14 to 16px. Provider logos, the pet and the menu bar art are brand material and were not collected.

| Icon | Sizes | Where |
|---|---|---|
| [gauge](icons/gauge.svg) | 15x15 16x16 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [activity](icons/activity.svg) | 14x14 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [moon](icons/moon.svg) | 14x14 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [trophy](icons/trophy.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [puzzle](icons/puzzle.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [chevron-left](icons/chevron-left.svg) | 16x16 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [layout-grid](icons/layout-grid.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [globe](icons/globe.svg) | 15x15 16x16 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [settings](icons/settings.svg) | 15x15 16x16 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [rotate-ccw-clock](icons/rotate-ccw-clock.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [cloud](icons/cloud.svg) | 15x15 16x16 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [chart-column](icons/chart-column.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [award](icons/award.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [paw-print](icons/paw-print.svg) | 15x15 | tokens; sessions; limits; skills; settings; widgets; service-status; achievements |
| [refresh-cw](icons/refresh-cw.svg) | 14x14 16x16 | tokens; sessions; limits; skills; service-status |
| [chevron-down](icons/chevron-down.svg) | 14x14 | sessions; skills; settings; widgets |
| [chevron-right](icons/chevron-right.svg) | 14x14 16x16 | sessions; skills |
| [search](icons/search.svg) | 16x16 | sessions; skills |
| [info](icons/info.svg) | 14x14 16x16 | tokens; sessions |
| [folder](icons/folder.svg) | 14x14 | sessions |
| [copy](icons/copy.svg) | 16x16 | sessions |
| [calendar-clock](icons/calendar-clock.svg) | 16x16 | limits |
| [maximize-2](icons/maximize-2.svg) | 14x14 | tokens |
| [square-arrow-out-up-right](icons/square-arrow-out-up-right.svg) | 14x14 | tokens |
| [bell-off](icons/bell-off.svg) | 16x16 | limits |
| [download](icons/download.svg) | 16x16 | widgets |
| [external-link](icons/external-link.svg) | 16x16 | service-status |
| [sun](icons/sun.svg) | 14x14 | settings |
| [palette](icons/palette.svg) | 16x16 | settings |
| [languages](icons/languages.svg) | 14x14 | settings |
| [hard-drive](icons/hard-drive.svg) | 11x11 | achievements |
| [calendar](icons/calendar.svg) | 14x14 | sessions |
| [user-round](icons/user-round.svg) | 16x16 | settings |
| [flask-conical](icons/flask-conical.svg) | 16x16 | settings |
| [x](icons/x.svg) | 13x13 | skills |
| [monitor](icons/monitor.svg) | 14x14 | settings |

## Gaps

- **Not captured: signed-in pages.** The signed-in Cloud page, Leaderboard and the account half of Settings need a TokenTracker account; none was signed in. Leaderboard shows other people's handles and avatars, so it was not captured; the signed-out account control stands in for an avatar.
- **Not present: text area and radio.** No page in v1.4.3 renders either.
- **The toast** is the share card's failure toast: Copy image cannot reach a clipboard in a headless browser, so the product reports "Couldn't generate image". The success toast ("Image copied to clipboard") was not reached.
- **Switches are disabled** on every page reached: they work only with the Mac app connected. Their hover and focus states are not available.
- **The field error** appears only after Test connection (or Save): the host was typed, Test connection was pressed, the check failed before any request, and the field was cleared. Save was never pressed.
- **Not captured: phone-width components.** The 390-wide layouts are in the `mobile-*` screenshots only; no component was measured at that width.
- **Not tokenised: provider colours.** The per-tool colours in the share bar, tiles and charts come from `getProviderColor()` in the dashboard source.
- **Status badge** reads the `CACHED` pill on Limits; `STALE` and `RE-AUTH` did not appear on this machine.
