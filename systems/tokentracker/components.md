# TokenTracker components

What TokenTracker v1.3.5's dashboard is built from, read on 2026-10-11 from the local server the CLI runs (127.0.0.1:7680), no account signed in, in headless Chromium at 1440 x 900 and 2x. Every component was measured in dark (the default) and light. Each table shows the values that change across states; `=` repeats the first state. The full computed styles are in [raw/measurements.md](raw/measurements.md); the tokens in [tokens.json](tokens.json).

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`:active:hover`), so nothing was pressed; `focused` and `filled` are a field clicked into and typed into, then cleared; `open` is a menu or dialog the page opened itself. Private text (paths, session titles, skill names) was replaced in the page before any crop.

## Pages captured

| Page | Shots |
|---|---|
| achievements | [achievements-dark-default](screenshots/achievements-dark-default.png), [achievements-light-default](screenshots/achievements-light-default.png) |
| dashboard | [dashboard-dark-cost-hover](screenshots/dashboard-dark-cost-hover.png), [dashboard-dark-default](screenshots/dashboard-dark-default.png), [dashboard-dark-full](screenshots/dashboard-dark-full.png), [dashboard-dark-nav-hover](screenshots/dashboard-dark-nav-hover.png), [dashboard-dark-period-week](screenshots/dashboard-dark-period-week.png), [dashboard-dark-sidebar-collapsed](screenshots/dashboard-dark-sidebar-collapsed.png), [dashboard-light-cost-hover](screenshots/dashboard-light-cost-hover.png), [dashboard-light-default](screenshots/dashboard-light-default.png), [dashboard-light-full](screenshots/dashboard-light-full.png), [dashboard-light-nav-hover](screenshots/dashboard-light-nav-hover.png), [dashboard-light-period-week](screenshots/dashboard-light-period-week.png), [dashboard-light-sidebar-collapsed](screenshots/dashboard-light-sidebar-collapsed.png) |
| limits | [limits-dark-default](screenshots/limits-dark-default.png), [limits-dark-full](screenshots/limits-dark-full.png), [limits-light-default](screenshots/limits-light-default.png), [limits-light-full](screenshots/limits-light-full.png) |
| mobile-dashboard | [mobile-dashboard-dark-default](screenshots/mobile-dashboard-dark-default.png), [mobile-dashboard-dark-menu-open](screenshots/mobile-dashboard-dark-menu-open.png), [mobile-dashboard-light-default](screenshots/mobile-dashboard-light-default.png), [mobile-dashboard-light-menu-open](screenshots/mobile-dashboard-light-menu-open.png) |
| mobile-limits | [mobile-limits-dark-default](screenshots/mobile-limits-dark-default.png), [mobile-limits-light-default](screenshots/mobile-limits-light-default.png) |
| mobile-sessions | [mobile-sessions-dark-default](screenshots/mobile-sessions-dark-default.png), [mobile-sessions-light-default](screenshots/mobile-sessions-light-default.png) |
| mobile-settings | [mobile-settings-dark-default](screenshots/mobile-settings-dark-default.png), [mobile-settings-light-default](screenshots/mobile-settings-light-default.png) |
| pet | [pet-dark-default](screenshots/pet-dark-default.png), [pet-light-default](screenshots/pet-light-default.png) |
| service-status | [service-status-dark-default](screenshots/service-status-dark-default.png), [service-status-light-default](screenshots/service-status-light-default.png) |
| sessions | [sessions-dark-default](screenshots/sessions-dark-default.png), [sessions-dark-row-hover](screenshots/sessions-dark-row-hover.png), [sessions-dark-search-focused](screenshots/sessions-dark-search-focused.png), [sessions-dark-select-open](screenshots/sessions-dark-select-open.png), [sessions-light-default](screenshots/sessions-light-default.png), [sessions-light-row-hover](screenshots/sessions-light-row-hover.png), [sessions-light-search-focused](screenshots/sessions-light-search-focused.png), [sessions-light-select-open](screenshots/sessions-light-select-open.png) |
| settings | [settings-dark-account](screenshots/settings-dark-account.png), [settings-dark-default](screenshots/settings-dark-default.png), [settings-dark-labs](screenshots/settings-dark-labs.png), [settings-dark-segment-hover](screenshots/settings-dark-segment-hover.png), [settings-dark-usage-limits](screenshots/settings-dark-usage-limits.png), [settings-light-account](screenshots/settings-light-account.png), [settings-light-default](screenshots/settings-light-default.png), [settings-light-labs](screenshots/settings-light-labs.png), [settings-light-segment-hover](screenshots/settings-light-segment-hover.png), [settings-light-usage-limits](screenshots/settings-light-usage-limits.png) |
| skills | [skills-dark-browse](screenshots/skills-dark-browse.png), [skills-dark-default](screenshots/skills-dark-default.png), [skills-light-browse](screenshots/skills-light-browse.png), [skills-light-default](screenshots/skills-light-default.png) |
| widgets | [widgets-dark-default](screenshots/widgets-dark-default.png), [widgets-dark-full](screenshots/widgets-dark-full.png), [widgets-light-default](screenshots/widgets-light-default.png), [widgets-light-full](screenshots/widgets-light-full.png) |

## Shared values

- **Hover** changes colour: nav items and menu options take a translucent neutral wash (`bg.hover`), tabs a solid one, outlined controls a stronger border. Light-theme outlined buttons turn their text and border green on hover. Two things also grow: the primary button scales to 1.03 and a heatmap cell to 1.25.
- **Focus.** None. TokenTracker's stylesheet removes every Tailwind focus ring, so `focus-visible` reads the same as `default` in every table below.
- **Pressed** looks like hover: no scale, no darker fill.
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
| text | 10px/15px 400, tracking 0.5px, uppercase, #737373 |
| shadow | none |
| icon | 16px |
| transition | width 0.2s |

Crops: [sidebar-default](components/crops/sidebar-default.png).

| light | default |
|---|---|
| size | 220 x 900 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 13px/19.5px 500, #404040 |
| shadow | none |
| icon | 16px |
| transition | width 0.2s |

Crops: [sidebar.light-default](components/crops/sidebar.light-default.png).


#### Sidebar group label

`sidebar-group-label` on /dashboard, found by `leaf "Tools"`.

| dark | default |
|---|---|
| size | 204 x 35 |
| padding | 16px 12px 4px 12px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 10px/15px 400, tracking 0.5px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [sidebar-group-label-default](components/crops/sidebar-group-label-default.png).

| light | default |
|---|---|
| size | 204 x 35 |
| padding | 16px 12px 4px 12px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 10px/15px 400, tracking 0.5px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [sidebar-group-label.light-default](components/crops/sidebar-group-label.light-default.png).


#### Nav item, current

`nav-item-active` on /dashboard, found by `a[href="/dashboard"] (Tokens)`.

| dark | default | focus-visible |
|---|---|---|
| size | 204 x 32 | = |
| padding | 6px 8px | = |
| fill | #262626 | = |
| border | none | = |
| radius | 8px | = |
| text | 13px/19.5px 500, #ffffff | = |
| shadow | none | = |
| icon | 15px | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [nav-item-active-default](components/crops/nav-item-active-default.png), [nav-item-active-focus-visible](components/crops/nav-item-active-focus-visible.png).

| light | default | focus-visible |
|---|---|---|
| size | 204 x 32 | = |
| padding | 6px 8px | = |
| fill | #e5e5e5 @ 0.7 | = |
| border | none | = |
| radius | 8px | = |
| text | 13px/19.5px 500, #0a0a0a | = |
| shadow | none | = |
| icon | 15px | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [nav-item-active.light-default](components/crops/nav-item-active.light-default.png), [nav-item-active.light-focus-visible](components/crops/nav-item-active.light-focus-visible.png).


#### Nav item

`nav-item` on /dashboard, found by `a[href="/sessions"]`.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 204 x 32 | = | = | = |
| padding | 6px 8px | = | = | = |
| fill | transparent | #262626 @ 0.6 | = | #262626 @ 0.6 |
| border | none | = | = | = |
| radius | 8px | = | = | = |
| text | 13px/19.5px 400, #a3a3a3 | 13px/19.5px 400, #ffffff | = | 13px/19.5px 400, #ffffff |
| shadow | none | = | = | = |
| icon | 15px | = | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = | = |

Crops: [nav-item-default](components/crops/nav-item-default.png), [nav-item-hover](components/crops/nav-item-hover.png), [nav-item-focus-visible](components/crops/nav-item-focus-visible.png), [nav-item-pressed](components/crops/nav-item-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 204 x 32 | = | = | = |
| padding | 6px 8px | = | = | = |
| fill | transparent | #e5e5e5 @ 0.5 | = | #e5e5e5 @ 0.5 |
| border | none | = | = | = |
| radius | 8px | = | = | = |
| text | 13px/19.5px 400, #525252 | 13px/19.5px 400, #0a0a0a | = | 13px/19.5px 400, #0a0a0a |
| shadow | none | = | = | = |
| icon | 15px | = | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = | = |

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
| text | 13px/19.5px 400, #a3a3a3 |
| shadow | none |
| icon | 15px |
| transition | none |

Crops: [nav-icon-default](components/crops/nav-icon-default.png).

| light | default |
|---|---|
| size | 15 x 15 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 13px/19.5px 400, #525252 |
| shadow | none |
| icon | 15px |
| transition | none |

Crops: [nav-icon.light-default](components/crops/nav-icon.light-default.png).


#### Content panel

`content-panel` on /dashboard, found by `first rounded, filled ancestor of main`. The rounded panel the pages sit in, inset from the window edge on the page wash.

| dark | default |
|---|---|
| size | 1208 x 880 |
| padding | 0px |
| fill | #171717 |
| border | 1px #262626 |
| radius | 16px |
| text | 9px/13.5px 600, tracking -0.225px, #ffffff @ 0.9 |
| shadow | yes |
| icon | 0px |
| transition | none |

| light | default |
|---|---|
| size | 1208 x 880 |
| padding | 0px |
| fill | #fafafa |
| border | 1px #e5e5e5 |
| radius | 16px |
| text | 9px/13.5px 600, tracking -0.225px, #ffffff @ 0.9 |
| shadow | yes |
| icon | 0px |
| transition | none |


#### Theme toggle

`theme-toggle` on /dashboard, found by `button[aria-label*=theme]`.

| dark | default | hover |
|---|---|---|
| size | 44 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 9999px | = |
| text | 16px/24px 400, #fafafa | = |
| shadow | none | = |
| icon | 14px | = |
| transition | none | = |

Crops: [theme-toggle-default](components/crops/theme-toggle-default.png), [theme-toggle-hover](components/crops/theme-toggle-hover.png).

| light | default | hover |
|---|---|---|
| size | 44 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 9999px | = |
| text | 16px/24px 400, #0a0a0a | = |
| shadow | none | = |
| icon | 14px | = |
| transition | none | = |

Crops: [theme-toggle.light-default](components/crops/theme-toggle.light-default.png), [theme-toggle.light-hover](components/crops/theme-toggle.light-hover.png).


#### GitHub star pill

`star-pill` on /dashboard, found by `a[href*=github]`.

| dark | default | hover |
|---|---|---|
| size | 63.92 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 9999px | = |
| text | 12px/12px 500, #a3a3a3 | 12px/12px 500, #ffffff |
| shadow | none | = |
| icon | 12px | = |
| transition | none | = |

Crops: [star-pill-default](components/crops/star-pill-default.png), [star-pill-hover](components/crops/star-pill-hover.png).

| light | default | hover |
|---|---|---|
| size | 63.92 x 44 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 9999px | = |
| text | 12px/12px 500, #525252 | 12px/12px 500, #0a0a0a |
| shadow | none | = |
| icon | 12px | = |
| transition | none | = |

Crops: [star-pill.light-default](components/crops/star-pill.light-default.png), [star-pill.light-hover](components/crops/star-pill.light-hover.png).


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
| text | 12px/16px 500, #d4d4d4 |
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
| text | 12px/16px 500, #737373 |
| shadow | none |
| transition | none |

Crops: [period-tabs.light-default](components/crops/period-tabs.light-default.png).


#### Period tab, selected

`period-tab-selected` on /dashboard, found by `[role=tab][aria-selected=true]`.

| dark | default | focus-visible |
|---|---|---|
| size | 60.8 x 28 | = |
| padding | 6px 12px | = |
| fill | #262626 | = |
| border | none | = |
| radius | 8px | = |
| text | 12px/16px 500, #fafafa | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [period-tab-selected-default](components/crops/period-tab-selected-default.png), [period-tab-selected-focus-visible](components/crops/period-tab-selected-focus-visible.png).

| light | default | focus-visible |
|---|---|---|
| size | 60.8 x 28 | = |
| padding | 6px 12px | = |
| fill | #f5f5f5 | = |
| border | none | = |
| radius | 8px | = |
| text | 12px/16px 500, #0a0a0a | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [period-tab-selected.light-default](components/crops/period-tab-selected.light-default.png), [period-tab-selected.light-focus-visible](components/crops/period-tab-selected.light-focus-visible.png).


#### Period tab

`period-tab` on /dashboard, found by `[role=tab][aria-selected=false]`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 46.08 x 28 | = | = |
| padding | 6px 12px | = | = |
| fill | transparent | #262626 | = |
| border | none | = | = |
| radius | 8px | = | = |
| text | 12px/16px 500, #d4d4d4 | 12px/16px 500, #fafafa | = |
| shadow | none | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [period-tab-default](components/crops/period-tab-default.png), [period-tab-hover](components/crops/period-tab-hover.png), [period-tab-focus-visible](components/crops/period-tab-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 46.08 x 28 | = | = |
| padding | 6px 12px | = | = |
| fill | transparent | #fafafa | = |
| border | none | = | = |
| radius | 8px | = | = |
| text | 12px/16px 500, #737373 | 12px/16px 500, #0a0a0a | = |
| shadow | none | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [period-tab.light-default](components/crops/period-tab.light-default.png), [period-tab.light-hover](components/crops/period-tab.light-hover.png), [period-tab.light-focus-visible](components/crops/period-tab.light-focus-visible.png).


#### Secondary button

`share-button` on /dashboard, found by `button "Share"`. Outlined, as on Share. Measured, never pressed.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 79.41 x 32 | = | = | = |
| padding | 0px 12px | = | = | = |
| fill | #171717 | = | = | = |
| border | 1px #404040 | = | = | = |
| radius | 8px | = | = | = |
| text | 12px/16px 500, #fafafa | = | = | = |
| shadow | none | = | = | = |
| icon | 14px | = | = | = |
| transition | color, background-color, border-color, text-deco 0.2s | = | = | = |

Crops: [share-button-default](components/crops/share-button-default.png), [share-button-hover](components/crops/share-button-hover.png), [share-button-focus-visible](components/crops/share-button-focus-visible.png), [share-button-pressed](components/crops/share-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 79.41 x 32 | = | = | = |
| padding | 0px 12px | = | = | = |
| fill | #fafafa | = | = | = |
| border | 1px #d4d4d4 | 1px #059669 | = | 1px #059669 |
| radius | 8px | = | = | = |
| text | 12px/16px 500, #0a0a0a | 12px/16px 500, #059669 | = | 12px/16px 500, #059669 |
| shadow | none | = | = | = |
| icon | 14px | = | = | = |
| transition | color, background-color, border-color, text-deco 0.2s | = | = | = |

Crops: [share-button.light-default](components/crops/share-button.light-default.png), [share-button.light-hover](components/crops/share-button.light-hover.png), [share-button.light-focus-visible](components/crops/share-button.light-focus-visible.png), [share-button.light-pressed](components/crops/share-button.light-pressed.png).


#### Primary button

`primary-button` on /dashboard, found by `button "Open in Mac app"`. Solid near-black in light, near-white in dark. Measured, never pressed.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 121.02 x 28 | 124.65 x 28.84, scale 1.03 | = | = |
| padding | 6px 12px | = | = | = |
| fill | #fafafa | = | = | = |
| border | none | = | = | = |
| radius | 8px | = | = | = |
| text | 12px/16px 500, #171717 | = | = | = |
| shadow | none | = | = | = |
| transition | opacity 0.15s | = | = | = |

Crops: [primary-button-default](components/crops/primary-button-default.png), [primary-button-hover](components/crops/primary-button-hover.png), [primary-button-focus-visible](components/crops/primary-button-focus-visible.png), [primary-button-pressed](components/crops/primary-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 121.02 x 28 | 124.65 x 28.84, scale 1.03 | = | = |
| padding | 6px 12px | = | = | = |
| fill | #171717 | = | = | = |
| border | none | = | = | = |
| radius | 8px | = | = | = |
| text | 12px/16px 500, #ffffff | = | = | = |
| shadow | none | = | = | = |
| transition | opacity 0.15s | = | = | = |

Crops: [primary-button.light-default](components/crops/primary-button.light-default.png), [primary-button.light-hover](components/crops/primary-button.light-hover.png), [primary-button.light-focus-visible](components/crops/primary-button.light-focus-visible.png), [primary-button.light-pressed](components/crops/primary-button.light-pressed.png).


#### Small segmented control

`segmented-2d` on /dashboard, found by `parent of button "2D"`. 2D / 3D switch on the heatmap.

| dark | default |
|---|---|
| size | 65.53 x 25 |
| padding | 2px |
| fill | transparent |
| border | 1px #262626 |
| radius | 8px |
| text | 10px/15px 500, #fafafa |
| shadow | none |
| transition | none |

Crops: [segmented-2d-default](components/crops/segmented-2d-default.png).

| light | default |
|---|---|
| size | 65.53 x 25 |
| padding | 2px |
| fill | transparent |
| border | 1px #e5e5e5 |
| radius | 8px |
| text | 10px/15px 500, #0a0a0a |
| shadow | none |
| transition | none |

Crops: [segmented-2d.light-default](components/crops/segmented-2d.light-default.png).


#### Icon button

`icon-button` on /sessions, found by `main button[aria-label]`. Refresh at the top right. Measured, never pressed.

| dark | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 36 x 36 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | #262626 | = | #262626 |
| border | 1px #262626 | = | = | = |
| radius | 12px | = | = | = |
| text | 16px/24px 400, #a3a3a3 | 16px/24px 400, #ffffff | = | 16px/24px 400, #ffffff |
| shadow | none | = | = | = |
| icon | 16px | = | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = | = |

Crops: [icon-button-default](components/crops/icon-button-default.png), [icon-button-hover](components/crops/icon-button-hover.png), [icon-button-focus-visible](components/crops/icon-button-focus-visible.png), [icon-button-pressed](components/crops/icon-button-pressed.png).

| light | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| size | 36 x 36 | = | = | = |
| padding | 0px | = | = | = |
| fill | transparent | #f5f5f5 | = | #f5f5f5 |
| border | 1px #e5e5e5 | = | = | = |
| radius | 12px | = | = | = |
| text | 16px/24px 400, #525252 | 16px/24px 400, #0a0a0a | = | 16px/24px 400, #0a0a0a |
| shadow | none | = | = | = |
| icon | 16px | = | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = | = |

Crops: [icon-button.light-default](components/crops/icon-button.light-default.png), [icon-button.light-hover](components/crops/icon-button.light-hover.png), [icon-button.light-focus-visible](components/crops/icon-button.light-focus-visible.png), [icon-button.light-pressed](components/crops/icon-button.light-pressed.png).


#### Segmented control

`segmented` on /settings, found by `parent of button "Compact"`.

| dark | default |
|---|---|
| size | 126.88 x 34 |
| padding | 2px |
| fill | #171717 |
| border | 1px #262626 |
| radius | 12px |
| text | 12px/16px 500, #ffffff |
| shadow | none |
| transition | none |

Crops: [segmented-default](components/crops/segmented-default.png).

| light | default |
|---|---|
| size | 126.88 x 34 |
| padding | 2px |
| fill | #fafafa |
| border | 1px #e5e5e5 |
| radius | 12px |
| text | 12px/16px 500, #0a0a0a |
| shadow | none |
| transition | none |

Crops: [segmented.light-default](components/crops/segmented.light-default.png).


#### Segment, selected

`segment-selected` on /settings, found by `button "Compact"`.

| dark | default | focus-visible |
|---|---|---|
| size | 76.31 x 28 | = |
| padding | 6px 12px | = |
| fill | #262626 | = |
| border | none | = |
| radius | 8px | = |
| text | 12px/16px 500, #ffffff | = |
| shadow | yes | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [segment-selected-default](components/crops/segment-selected-default.png), [segment-selected-focus-visible](components/crops/segment-selected-focus-visible.png).

| light | default | focus-visible |
|---|---|---|
| size | 76.31 x 28 | = |
| padding | 6px 12px | = |
| fill | #ffffff | = |
| border | none | = |
| radius | 8px | = |
| text | 12px/16px 500, #0a0a0a | = |
| shadow | yes | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [segment-selected.light-default](components/crops/segment-selected.light-default.png), [segment-selected.light-focus-visible](components/crops/segment-selected.light-focus-visible.png).


#### Segment

`segment` on /settings, found by `button "Full"`. Hovered and focused only; never pressed, so the setting is unchanged.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 44.56 x 28 | = | = |
| padding | 6px 12px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 8px | = | = |
| text | 12px/16px 500, #a3a3a3 | 12px/16px 500, #ffffff | = |
| shadow | none | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [segment-default](components/crops/segment-default.png), [segment-hover](components/crops/segment-hover.png), [segment-focus-visible](components/crops/segment-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 44.56 x 28 | = | = |
| padding | 6px 12px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 8px | = | = |
| text | 12px/16px 500, #737373 | 12px/16px 500, #0a0a0a | = |
| shadow | none | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [segment.light-default](components/crops/segment.light-default.png), [segment.light-hover](components/crops/segment.light-hover.png), [segment.light-focus-visible](components/crops/segment.light-focus-visible.png).


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
| text | 12px/16px 400, tracking 0.6px, uppercase, #d4d4d4 |
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
| text | 12px/16px 400, tracking 0.6px, uppercase, #737373 |
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
| text | 72px/72px 700, tracking -1.8px, #fafafa |
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
| text | 72px/72px 700, tracking -1.8px, #0a0a0a |
| shadow | none |
| transition | none |

Crops: [hero-metric.light-default](components/crops/hero-metric.light-default.png).


#### Hero cost

`hero-cost` on /dashboard, found by `text matching $n.nn`. Cost under the hero number, in the brand green.

| dark | default |
|---|---|
| size | 133.09 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 20px/28px 700, #059669 |
| shadow | none |
| icon | 16px |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [hero-cost-default](components/crops/hero-cost-default.png).

| light | default |
|---|---|
| size | 133.98 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 20px/28px 700, #059669 |
| shadow | none |
| icon | 16px |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [hero-cost.light-default](components/crops/hero-cost.light-default.png).


#### Provider share tile

`provider-tile` on /dashboard, found by `tile holding "CLAUDE"`.

| dark | default | hover |
|---|---|---|
| size | 172.17 x 96.5 | = |
| padding | 12px | = |
| fill | transparent | = |
| border | 1px #404040 | 1px #525252 |
| radius | 12px | = |
| text | 14px/20px 500, #fafafa | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.2s | = |

Crops: [provider-tile-default](components/crops/provider-tile-default.png), [provider-tile-hover](components/crops/provider-tile-hover.png).

| light | default | hover |
|---|---|---|
| size | 172.17 x 96.5 | = |
| padding | 12px | = |
| fill | transparent | = |
| border | 1px #e5e5e5 | 1px #d4d4d4 |
| radius | 12px | = |
| text | 14px/20px 500, #0a0a0a | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.2s | = |

Crops: [provider-tile.light-default](components/crops/provider-tile.light-default.png), [provider-tile.light-hover](components/crops/provider-tile.light-hover.png).


#### Provider share tile, all

`provider-tile-all` on /dashboard, found by `tile holding "All"`.

| dark | default |
|---|---|
| size | 172.16 x 96.5 |
| padding | 12px |
| fill | transparent |
| border | 1px #404040 |
| radius | 12px |
| text | 14px/20px 500, #fafafa |
| shadow | none |
| icon | 15px |
| transition | color, background-color, border-color, text-deco 0.2s |

Crops: [provider-tile-all-default](components/crops/provider-tile-all-default.png).

| light | default |
|---|---|
| size | 172.16 x 96.5 |
| padding | 12px |
| fill | transparent |
| border | 1px #e5e5e5 |
| radius | 12px |
| text | 14px/20px 500, #0a0a0a |
| shadow | none |
| icon | 15px |
| transition | color, background-color, border-color, text-deco 0.2s |

Crops: [provider-tile-all.light-default](components/crops/provider-tile-all.light-default.png).


#### Stat chip

`stat-chip` on /dashboard, found by `parent of "7d"`. A small filled tile: value over a caption (7d, 30d, avg, convs).

| dark | default |
|---|---|
| size | 77.33 x 53 |
| padding | 8px |
| fill | #262626 |
| border | none |
| radius | 12px |
| text | 14px/20px 600, #fafafa |
| shadow | none |
| transition | none |

Crops: [stat-chip-default](components/crops/stat-chip-default.png).

| light | default |
|---|---|
| size | 77.33 x 53 |
| padding | 8px |
| fill | #fafafa |
| border | none |
| radius | 12px |
| text | 14px/20px 600, #0a0a0a |
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
| text | 14px/20px 500, tracking 0.35px, uppercase, #d4d4d4 |
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
| text | 14px/20px 500, tracking 0.35px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [card-title.light-default](components/crops/card-title.light-default.png).


#### Heatmap cell, busiest

`heatmap-cell` on /dashboard, found by `span.rounded-[2px] whose fill is farthest from the empty fill`.

| dark | default | hover |
|---|---|---|
| size | 12 x 12 | 15 x 15, scale 1.25 |
| padding | 0px | = |
| fill | #34d399 | = |
| border | none | = |
| radius | 2px | = |
| text | 16px/24px 400, #fafafa | = |
| shadow | none | = |
| transition | transform 0.15s | = |

Crops: [heatmap-cell-default](components/crops/heatmap-cell-default.png), [heatmap-cell-hover](components/crops/heatmap-cell-hover.png).

| light | default | hover |
|---|---|---|
| size | 12 x 12 | 15 x 15, scale 1.25 |
| padding | 0px | = |
| fill | #10b981 | = |
| border | none | = |
| radius | 2px | = |
| text | 16px/24px 400, #0a0a0a | = |
| shadow | none | = |
| transition | transform 0.15s | = |

Crops: [heatmap-cell.light-default](components/crops/heatmap-cell.light-default.png), [heatmap-cell.light-hover](components/crops/heatmap-cell.light-hover.png).


#### Heatmap cell, empty

`heatmap-cell-empty` on /dashboard, found by `span.rounded-[2px] with the least saturated fill`.

| dark | default |
|---|---|
| size | 12 x 12 |
| padding | 0px |
| fill | #121212 |
| border | none |
| radius | 2px |
| text | 16px/24px 400, #fafafa |
| shadow | none |
| transition | transform 0.15s |

Crops: [heatmap-cell-empty-default](components/crops/heatmap-cell-empty-default.png).

| light | default |
|---|---|
| size | 12 x 12 |
| padding | 0px |
| fill | #ebedf0 |
| border | none |
| radius | 2px |
| text | 16px/24px 400, #0a0a0a |
| shadow | none |
| transition | transform 0.15s |

Crops: [heatmap-cell-empty.light-default](components/crops/heatmap-cell-empty.light-default.png).


#### Hero cost button

`cost-button` on /dashboard, found by `button[aria-label="View cost breakdown"]`. The cost under the hero number is a button that opens the cost breakdown.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 133.09 x 28 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 0px | = | = |
| text | 20px/28px 700, #059669 | 20px/28px 700, #10b981 | = |
| shadow | none | = | = |
| icon | 16px | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [cost-button-default](components/crops/cost-button-default.png), [cost-button-hover](components/crops/cost-button-hover.png), [cost-button-focus-visible](components/crops/cost-button-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 133.98 x 28 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 0px | = | = |
| text | 20px/28px 700, #059669 | 20px/28px 700, #047857 | = |
| shadow | none | = | = |
| icon | 16px | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [cost-button.light-default](components/crops/cost-button.light-default.png), [cost-button.light-hover](components/crops/cost-button.light-hover.png), [cost-button.light-focus-visible](components/crops/cost-button.light-focus-visible.png).


#### Card

`card` on /dashboard, found by `card around "Activity heatmap"`. The Activity heatmap card: the shared card surface.

| dark | default |
|---|---|
| size | 375.33 x 231 |
| padding | 20px |
| fill | #171717 |
| border | 1px #262626 |
| radius | 16px |
| text | 14px/20px 500, tracking 0.35px, uppercase, #d4d4d4 |
| shadow | none |
| transition | none |

Crops: [card-default](components/crops/card-default.png).

| light | default |
|---|---|
| size | 375.33 x 231 |
| padding | 20px |
| fill | #ffffff |
| border | 1px #e5e5e5 |
| radius | 16px |
| text | 14px/20px 500, tracking 0.35px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [card.light-default](components/crops/card.light-default.png).


### Badges, tooltips and status

#### Badge

`beta-badge` on /dashboard, found by `leaf "BETA"`.

| dark | default |
|---|---|
| size | 31.57 x 14.4, scale 0.9 |
| padding | 2px 6px |
| fill | #262626 @ 0.8 |
| border | none |
| radius | 4px |
| text | 8px/12px 600, tracking 0.4px, uppercase, #a3a3a3 |
| shadow | none |
| transition | none |

Crops: [beta-badge-default](components/crops/beta-badge-default.png).

| light | default |
|---|---|
| size | 31.57 x 14.4, scale 0.9 |
| padding | 2px 6px |
| fill | #f5f5f5 |
| border | none |
| radius | 4px |
| text | 8px/12px 600, tracking 0.4px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [beta-badge.light-default](components/crops/beta-badge.light-default.png).


#### Dialog (cost breakdown)

`dialog` on /dashboard, found by `[role=dialog]`. Opened by the hero cost button, closed with Escape.

| dark | open |
|---|---|
| size | 460 x 868 |
| padding | 0px |
| fill | #0a0a0a |
| border | none |
| radius | 16px |
| text | 11px/14.3px 600, tracking 1.32px, uppercase, #a3a3a3 |
| shadow | yes |
| icon | 16px |
| transition | opacity, transform 0.22s, 0.26s |

Crops: [dialog-open](components/crops/dialog-open.png).

| light | open |
|---|---|
| size | 460 x 868 |
| padding | 0px |
| fill | #ffffff |
| border | none |
| radius | 16px |
| text | 11px/14.3px 600, tracking 1.32px, uppercase, #737373 |
| shadow | yes |
| icon | 16px |
| transition | opacity, transform 0.22s, 0.26s |

Crops: [dialog.light-open](components/crops/dialog.light-open.png).


#### Status badge

`status-badge` on /limits, found by `pill reading STALE`. STALE / RE-AUTH pill with a coloured dot.

| dark | default |
|---|---|
| size | 101.11 x 19.5 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 9px/13.5px 600, tracking 0.45px, uppercase, #a3a3a3 |
| shadow | none |
| transition | none |

Crops: [status-badge-default](components/crops/status-badge-default.png).

| light | default |
|---|---|
| size | 101.11 x 19.5 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 9px/13.5px 600, tracking 0.45px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [status-badge.light-default](components/crops/status-badge.light-default.png).


#### Service status row

`status-row` on /status, found by `row around "Claude"`.

| dark | default | hover |
|---|---|---|
| size | 544 x 130 | = |
| padding | 20px | = |
| fill | #171717 | #262626 @ 0.6 |
| border | 1px #262626 | 1px #404040 |
| radius | 16px | = |
| text | 16px/24px 500, #fafafa | = |
| shadow | none | = |
| icon | 16px | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [status-row-default](components/crops/status-row-default.png), [status-row-hover](components/crops/status-row-hover.png).

| light | default | hover |
|---|---|---|
| size | 544 x 130 | = |
| padding | 20px | = |
| fill | #ffffff | #fafafa |
| border | 1px #e5e5e5 | 1px #d4d4d4 |
| radius | 16px | = |
| text | 16px/24px 500, #0a0a0a | = |
| shadow | none | = |
| icon | 16px | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [status-row.light-default](components/crops/status-row.light-default.png), [status-row.light-hover](components/crops/status-row.light-hover.png).


### Tables and lists

#### Table tab, selected

`table-tab-selected` on /dashboard, found by `button "Daily Breakdown"`.

| dark | default |
|---|---|
| size | 119.97 x 28 |
| padding | 6px 12px |
| fill | #262626 |
| border | none |
| radius | 4px |
| text | 12px/16px 500, #fafafa |
| shadow | none |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [table-tab-selected-default](components/crops/table-tab-selected-default.png).

| light | default |
|---|---|
| size | 119.97 x 28 |
| padding | 6px 12px |
| fill | #f5f5f5 |
| border | none |
| radius | 4px |
| text | 12px/16px 500, #0a0a0a |
| shadow | none |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [table-tab-selected.light-default](components/crops/table-tab-selected.light-default.png).


#### Table tab

`table-tab` on /dashboard, found by `button "Project Usage"`.

| dark | default | hover |
|---|---|---|
| size | 105.06 x 28 | = |
| padding | 6px 12px | = |
| fill | transparent | #262626 @ 0.5 |
| border | none | = |
| radius | 4px | = |
| text | 12px/16px 500, #d4d4d4 | 12px/16px 500, #fafafa |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [table-tab-default](components/crops/table-tab-default.png), [table-tab-hover](components/crops/table-tab-hover.png).

| light | default | hover |
|---|---|---|
| size | 105.06 x 28 | = |
| padding | 6px 12px | = |
| fill | transparent | #fafafa |
| border | none | = |
| radius | 4px | = |
| text | 12px/16px 500, #737373 | 12px/16px 500, #0a0a0a |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [table-tab.light-default](components/crops/table-tab.light-default.png), [table-tab.light-hover](components/crops/table-tab.light-hover.png).


#### Table header cell

`table-header` on /dashboard, found by `thead th:nth(1)`.

| dark | default |
|---|---|
| size | 102.94 x 33.3 |
| padding | 0px |
| fill | #171717 |
| border | none |
| radius | 0px |
| text | 12px/16.8px 500, tracking 0.12px, #d4d4d4 |
| shadow | none |
| transition | none |

Crops: [table-header-default](components/crops/table-header-default.png).

| light | default |
|---|---|
| size | 102.94 x 33.3 |
| padding | 0px |
| fill | #ffffff |
| border | none |
| radius | 0px |
| text | 12px/16.8px 500, tracking 0.12px, #525252 |
| shadow | none |
| transition | none |

Crops: [table-header.light-default](components/crops/table-header.light-default.png).


#### Table cell (numeric)

`table-cell` on /dashboard, found by `tbody td:nth(1)`.

| dark | default |
|---|---|
| size | 102.94 x 38 |
| padding | 8px 16px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 14px/21px 400, #fafafa |
| shadow | none |
| transition | none |

Crops: [table-cell-default](components/crops/table-cell-default.png).

| light | default |
|---|---|
| size | 102.94 x 38 |
| padding | 8px 16px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 14px/21px 400, #0a0a0a |
| shadow | none |
| transition | none |

Crops: [table-cell.light-default](components/crops/table-cell.light-default.png).


#### Table row

`table-row` on /dashboard, found by `tbody tr:nth(1)`.

| dark | default | hover |
|---|---|---|
| size | 756.67 x 38 | = |
| padding | 0px | = |
| fill | transparent | #262626 @ 0.5 |
| border | bottom 1px #262626 | = |
| radius | 0px | = |
| text | 14px/21px 400, #d4d4d4 | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [table-row-default](components/crops/table-row-default.png), [table-row-hover](components/crops/table-row-hover.png).

| light | default | hover |
|---|---|---|
| size | 756.67 x 38 | = |
| padding | 0px | = |
| fill | transparent | #fafafa @ 0.5 |
| border | bottom 1px #f5f5f5 | = |
| radius | 0px | = |
| text | 14px/21px 400, #737373 | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

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
| text | 12px/16px 400, #a3a3a3 |
| shadow | none |
| icon | 14px |
| transition | none |

Crops: [summary-strip-default](components/crops/summary-strip-default.png).

| light | default |
|---|---|
| size | 1070 x 48 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 12px/16px 400, #737373 |
| shadow | none |
| icon | 14px |
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
| text | 12px/16px 400, #a3a3a3 |
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
| text | 12px/16px 400, #737373 |
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
| text | 12px/16px 400, #a3a3a3 |
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
| text | 12px/16px 400, #737373 |
| shadow | none |
| transition | none |

Crops: [list-header.light-default](components/crops/list-header.light-default.png).


#### Session row

`list-row` on /sessions, found by `.sessions-row`.

| dark | default | hover |
|---|---|---|
| size | 1104 x 63 | = |
| padding | 12px 0px | = |
| fill | transparent | = |
| border | 1px #262626 | = |
| radius | 0px | = |
| text | 14px/20px 500, #ffffff | = |
| shadow | none | = |
| icon | 16px | = |
| transition | none | = |

Crops: [list-row-default](components/crops/list-row-default.png), [list-row-hover](components/crops/list-row-hover.png).

| light | default | hover |
|---|---|---|
| size | 1104 x 63 | = |
| padding | 12px 0px | = |
| fill | transparent | = |
| border | 1px #e5e5e5 | = |
| radius | 0px | = |
| text | 14px/20px 500, #0a0a0a | = |
| shadow | none | = |
| icon | 16px | = |
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
| radius | 4px | = | = |
| text | 14px/20px 500, #ffffff | = | = |
| shadow | none | = | = |
| transition | none | = | = |

Crops: [list-row-title-default](components/crops/list-row-title-default.png), [list-row-title-hover](components/crops/list-row-title-hover.png), [list-row-title-focus-visible](components/crops/list-row-title-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 61.42 x 20 | = | = |
| padding | 0px | = | = |
| fill | transparent | = | = |
| border | none | = | = |
| radius | 4px | = | = |
| text | 14px/20px 500, #0a0a0a | = | = |
| shadow | none | = | = |
| transition | none | = | = |

Crops: [list-row-title.light-default](components/crops/list-row-title.light-default.png), [list-row-title.light-hover](components/crops/list-row-title.light-hover.png), [list-row-title.light-focus-visible](components/crops/list-row-title.light-focus-visible.png).


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
| text | 36px/40px 600, tracking -0.9px, #ffffff |
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
| text | 36px/40px 600, tracking -0.9px, #0a0a0a |
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
| text | 16px/24px 400, #a3a3a3 |
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
| text | 16px/24px 400, #737373 |
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
| text | 16px/24px 400, #fafafa | = |
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
| text | 16px/24px 400, #0a0a0a | = |
| shadow | none | = |
| transition | none | = |

Crops: [search-field.light-default](components/crops/search-field.light-default.png), [search-field.light-hover](components/crops/search-field.light-hover.png).


#### Search input

`search-input` on /sessions, found by `input[placeholder^=Search]`. A model name was typed and deleted; nothing was sent.

| dark | default | focused | filled |
|---|---|---|---|
| size | 400 x 36 | = | = |
| padding | 0px 48px 0px 40px | = | = |
| fill | #171717 | = | = |
| border | 1px #262626 | = | = |
| radius | 8px | = | = |
| text | 14px/20px 400, #fafafa | = | = |
| shadow | none | = | = |
| transition | all 0.2s | = | = |

Crops: [search-input-default](components/crops/search-input-default.png), [search-input-focused](components/crops/search-input-focused.png), [search-input-filled](components/crops/search-input-filled.png).

| light | default | focused | filled |
|---|---|---|---|
| size | 400 x 36 | = | = |
| padding | 0px 48px 0px 40px | = | = |
| fill | #ffffff | = | = |
| border | 1px #e5e5e5 | = | = |
| radius | 8px | = | = |
| text | 14px/20px 400, #0a0a0a | = | = |
| shadow | none | = | = |
| transition | all 0.2s | = | = |

Crops: [search-input.light-default](components/crops/search-input.light-default.png), [search-input.light-focused](components/crops/search-input.light-focused.png), [search-input.light-filled](components/crops/search-input.light-filled.png).


#### Select button

`select` on /sessions, found by `button holding "All tools"`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 168 x 36 | = | = |
| padding | 0px 12px | = | = |
| fill | #171717 | = | = |
| border | 1px #262626 | 1px #404040 | = |
| radius | 6px | = | = |
| text | 14px/20px 400, #ffffff | = | = |
| shadow | none | = | = |
| icon | 14px | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [select-default](components/crops/select-default.png), [select-hover](components/crops/select-hover.png), [select-focus-visible](components/crops/select-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 168 x 36 | = | = |
| padding | 0px 12px | = | = |
| fill | #ffffff | = | = |
| border | 1px #e5e5e5 | 1px #d4d4d4 | = |
| radius | 6px | = | = |
| text | 14px/20px 400, #0a0a0a | = | = |
| shadow | none | = | = |
| icon | 14px | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [select.light-default](components/crops/select.light-default.png), [select.light-hover](components/crops/select.light-hover.png), [select.light-focus-visible](components/crops/select.light-focus-visible.png).


#### Select menu

`select-menu` on /sessions, found by `[role=listbox]`.

| dark | open |
|---|---|
| size | 158 x 112 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 12px/16px 400, #ffffff |
| shadow | none |
| icon | 12px |
| transition | none |

Crops: [select-menu-open](components/crops/select-menu-open.png).

| light | open |
|---|---|
| size | 158 x 112 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 12px/16px 400, #0a0a0a |
| shadow | none |
| icon | 12px |
| transition | none |

Crops: [select-menu.light-open](components/crops/select-menu.light-open.png).


#### Select option, selected

`select-option-selected` on /sessions, found by `first option`.

| dark | open |
|---|---|
| size | 158 x 28 |
| padding | 6px 24px 6px 6px |
| fill | #262626 @ 0.7 |
| border | none |
| radius | 12px |
| text | 12px/16px 400, #ffffff |
| shadow | none |
| icon | 12px |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [select-option-selected-open](components/crops/select-option-selected-open.png).

| light | open |
|---|---|
| size | 158 x 28 |
| padding | 6px 24px 6px 6px |
| fill | #f5f5f5 |
| border | none |
| radius | 12px |
| text | 12px/16px 400, #0a0a0a |
| shadow | none |
| icon | 12px |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [select-option-selected.light-open](components/crops/select-option-selected.light-open.png).


#### Select option

`select-option` on /sessions, found by `second option`.

| dark | open | hover |
|---|---|---|
| size | 158 x 28 | = |
| padding | 6px 24px 6px 6px | = |
| fill | transparent | #262626 @ 0.6 |
| border | none | = |
| radius | 12px | = |
| text | 12px/16px 400, #d4d4d4 | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [select-option-open](components/crops/select-option-open.png), [select-option-hover](components/crops/select-option-hover.png).

| light | open | hover |
|---|---|---|
| size | 158 x 28 | = |
| padding | 6px 24px 6px 6px | = |
| fill | transparent | #fafafa |
| border | none | = |
| radius | 12px | = |
| text | 12px/16px 400, #525252 | = |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [select-option.light-open](components/crops/select-option.light-open.png), [select-option.light-hover](components/crops/select-option.light-hover.png).


### Limits

#### Limits card

`limits-card` on /limits, found by `card around the "Usage limits" title`.

| dark | default |
|---|---|
| size | 1104 x 2340.81 |
| padding | 0px |
| fill | #171717 |
| border | 1px #262626 |
| radius | 16px |
| text | 14px/20px 500, tracking 0.35px, uppercase, #d4d4d4 |
| shadow | none |
| icon | 14px |
| transition | color, background-color, border-color, text-deco 0.2s |

| light | default |
|---|---|
| size | 1104 x 2340.81 |
| padding | 0px |
| fill | #ffffff |
| border | 1px #e5e5e5 |
| radius | 16px |
| text | 14px/20px 500, tracking 0.35px, uppercase, #737373 |
| shadow | none |
| icon | 14px |
| transition | color, background-color, border-color, text-deco 0.2s |


#### Limits card title

`limits-title` on /limits, found by `leaf "Usage limits"`.

| dark | default |
|---|---|
| size | 1062 x 20 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 14px/20px 500, tracking 0.35px, uppercase, #d4d4d4 |
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
| text | 14px/20px 500, tracking 0.35px, uppercase, #737373 |
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
| text | 10.5px/14.4375px 400, #e5e5e5 |
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
| text | 10.5px/14.4375px 400, #404040 |
| shadow | none |
| transition | none |

Crops: [usage-row.light-default](components/crops/usage-row.light-default.png).


#### Usage track

`usage-track` on /limits, found by `first track`.

| dark | default |
|---|---|
| size | 931 x 6 |
| padding | 0px |
| fill | #404040 @ 0.5 |
| border | none |
| radius | 9999px |
| text | 16px/24px 400, #fafafa |
| shadow | none |
| transition | none |

Crops: [usage-track-default](components/crops/usage-track-default.png).

| light | default |
|---|---|
| size | 931 x 6 |
| padding | 0px |
| fill | #f5f5f5 |
| border | none |
| radius | 9999px |
| text | 16px/24px 400, #0a0a0a |
| shadow | none |
| transition | none |

Crops: [usage-track.light-default](components/crops/usage-track.light-default.png).


#### Usage fill

`usage-fill` on /limits, found by `its fill`.

| dark | default |
|---|---|
| size | 269.98 x 6 |
| padding | 0px |
| fill | #10b981 |
| border | none |
| radius | 9999px |
| text | 16px/24px 400, #fafafa |
| shadow | none |
| transition | width 0.5s |

Crops: [usage-fill-default](components/crops/usage-fill-default.png).

| light | default |
|---|---|
| size | 269.98 x 6 |
| padding | 0px |
| fill | #10b981 |
| border | none |
| radius | 9999px |
| text | 16px/24px 400, #0a0a0a |
| shadow | none |
| transition | width 0.5s |

Crops: [usage-fill.light-default](components/crops/usage-fill.light-default.png).


#### Code block

`code-block` on /limits, found by `main pre`.

| dark | default |
|---|---|
| size | 1040 x 51.38 |
| padding | 6px 8px |
| fill | #171717 @ 0.6 |
| border | none |
| radius | 4px |
| text | 10.5px/13.125px 400, #d4d4d4 |
| shadow | none |
| transition | none |

Crops: [code-block-default](components/crops/code-block-default.png).

| light | default |
|---|---|
| size | 1040 x 51.38 |
| padding | 6px 8px |
| fill | #f5f5f5 |
| border | none |
| radius | 4px |
| text | 10.5px/13.125px 400, #525252 |
| shadow | none |
| transition | none |

Crops: [code-block.light-default](components/crops/code-block.light-default.png).


### Settings

#### Settings nav item, current

`subnav-item-active` on /settings, found by `button "Appearance"`.

| dark | default |
|---|---|
| size | 176 x 40 |
| padding | 8px 12px |
| fill | #262626 |
| border | none |
| radius | 8px |
| text | 14px/20px 500, #ffffff |
| shadow | none |
| icon | 16px |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [subnav-item-active-default](components/crops/subnav-item-active-default.png).

| light | default |
|---|---|
| size | 176 x 40 |
| padding | 8px 12px |
| fill | #f5f5f5 |
| border | none |
| radius | 8px |
| text | 14px/20px 500, #0a0a0a |
| shadow | none |
| icon | 16px |
| transition | color, background-color, border-color, text-deco 0.15s |

Crops: [subnav-item-active.light-default](components/crops/subnav-item-active.light-default.png).


#### Settings nav item

`subnav-item` on /settings, found by `button "Account"`.

| dark | default | hover | focus-visible |
|---|---|---|---|
| size | 176 x 40 | = | = |
| padding | 8px 12px | = | = |
| fill | transparent | #171717 | = |
| border | none | = | = |
| radius | 8px | = | = |
| text | 14px/20px 500, #a3a3a3 | 14px/20px 500, #e5e5e5 | = |
| shadow | none | = | = |
| icon | 16px | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [subnav-item-default](components/crops/subnav-item-default.png), [subnav-item-hover](components/crops/subnav-item-hover.png), [subnav-item-focus-visible](components/crops/subnav-item-focus-visible.png).

| light | default | hover | focus-visible |
|---|---|---|---|
| size | 176 x 40 | = | = |
| padding | 8px 12px | = | = |
| fill | transparent | #fafafa | = |
| border | none | = | = |
| radius | 8px | = | = |
| text | 14px/20px 500, #737373 | 14px/20px 500, #171717 | = |
| shadow | none | = | = |
| icon | 16px | = | = |
| transition | color, background-color, border-color, text-deco 0.15s | = | = |

Crops: [subnav-item.light-default](components/crops/subnav-item.light-default.png), [subnav-item.light-hover](components/crops/subnav-item.light-hover.png), [subnav-item.light-focus-visible](components/crops/subnav-item.light-focus-visible.png).


#### Settings nav group label

`subnav-group-label` on /settings, found by `leaf "App"`.

| dark | default |
|---|---|
| size | 176 x 19 |
| padding | 0px 12px 4px 12px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 10px/15px 600, tracking 1.6px, uppercase, #737373 |
| shadow | none |
| transition | none |

Crops: [subnav-group-label-default](components/crops/subnav-group-label-default.png).

| light | default |
|---|---|
| size | 176 x 19 |
| padding | 0px 12px 4px 12px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 10px/15px 600, tracking 1.6px, uppercase, #a3a3a3 |
| shadow | none |
| transition | none |

Crops: [subnav-group-label.light-default](components/crops/subnav-group-label.light-default.png).


#### Section title

`section-title` on /settings, found by `main h2`.

| dark | default |
|---|---|
| size | 768 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 20px/28px 600, tracking -0.5px, #ffffff |
| shadow | none |
| transition | none |

Crops: [section-title-default](components/crops/section-title-default.png).

| light | default |
|---|---|
| size | 768 x 28 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 20px/28px 600, tracking -0.5px, #0a0a0a |
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
| text | 14px/20px 400, #e5e5e5 |
| shadow | none |
| icon | 14px |
| transition | none |

| light | default |
|---|---|
| size | 726 x 377 |
| padding | 0px |
| fill | transparent |
| border | none |
| radius | 0px |
| text | 14px/20px 400, #171717 |
| shadow | none |
| icon | 14px |
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
| text | 14px/20px 400, #e5e5e5 |
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
| text | 14px/20px 400, #171717 |
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
| text | 12px/16px 400, #a3a3a3 |
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
| text | 12px/16px 400, #737373 |
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
| text | 12px/16px 400, #737373 | 12px/16px 400, #d4d4d4 |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [footer-link-default](components/crops/footer-link-default.png), [footer-link-hover](components/crops/footer-link-hover.png).

| light | default | hover |
|---|---|---|
| size | 103.95 x 16 | = |
| padding | 0px | = |
| fill | transparent | = |
| border | none | = |
| radius | 0px | = |
| text | 12px/16px 400, #737373 | 12px/16px 400, #404040 |
| shadow | none | = |
| transition | color, background-color, border-color, text-deco 0.15s | = |

Crops: [footer-link.light-default](components/crops/footer-link.light-default.png), [footer-link.light-hover](components/crops/footer-link.light-hover.png).


## Icons

37 Lucide icons (lucide-react, stroke 2, `currentColor`), named by their Lucide class, in [icons/](icons) with [icons/INDEX.tsv](icons/INDEX.tsv). Nav icons render at 15px, control icons at 14 to 16px. Provider logos, the pet and the menu bar art are brand material and were not collected.

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
| [arrow-up-right](icons/arrow-up-right.svg) | 12x12 | tokens |
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

- **Not captured: signed-in pages.** Cloud, Leaderboard and the account half of Settings need a TokenTracker account; none was signed in. Leaderboard would also show other people's handles.
- **Not captured: toasts and validation errors.** No action that raises a toast or a form error was taken (nothing was saved, copied or submitted).
- **Not captured: destructive confirmation.** The dashboard has no delete flow reachable without changing data.
- **Not captured: phone-width components.** The 390-wide layouts are in the `mobile-*` screenshots only; no component was measured at that width.
- **Not tokenised: provider colours.** The per-tool colours in the share bar, tiles and charts come from `getProviderColor()` in the dashboard source.
- **Status badge** (`STALE`, `RE-AUTH`) was found by text and its reading is the badge's wrapper; read its dot and pill from the crops and screenshots.
