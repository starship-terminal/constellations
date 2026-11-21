# Wrike components

Public marketing controls measured on www.wrike.com on 2026-11-21, signed out, in headless Chromium. Values are computed styles. Crops are in [components/crops/](components/crops/). The signed-in product was not opened.

## Button

Primary action is `button.website-btn.bg-color--accent`. Green fill `#00e05c`, ink `#162136`, 8px radius, 2px transparent border.

| State | Fill | Ink | Where |
|---|---|---|---|
| default | #00e05c | #162136 | [hero-cta-default.png](components/crops/hero-cta-default.png) |
| hover | #14ff75 | #162136 | [hero-cta-hover.png](components/crops/hero-cta-hover.png) |
| focus-visible | #14ff75 | #162136 | [hero-cta-focus-visible.png](components/crops/hero-cta-focus-visible.png) |
| pressed | #00c752 | #162136 | [hero-cta-pressed.png](components/crops/hero-cta-pressed.png) |

Header size is 40px tall, 16px type, padding 8px 14px. Hero size is 60px tall, 20px type. Disabled, loading and error were not on the public pages.

## Outline button

`button.website-btn.outline--invert` in the open Products menu. Transparent fill, 2px border, 8px radius, 40px tall. Hover fills it with the accent green `#14ff75`. Crops: [outline-cta-default.png](components/crops/outline-cta-default.png), [outline-cta-hover.png](components/crops/outline-cta-hover.png).

## Link

Text links paint `#0073d3` and lift to `#078eff` on hover. Measured on the top-banner "Read the report" link and the hero "Wrike in 3 minutes" control. Crops: [banner-link-default.png](components/crops/banner-link-default.png), [banner-link-hover.png](components/crops/banner-link-hover.png), [hero-video-default.png](components/crops/hero-video-default.png).

## Text field

The contact-sales form shows a 56px field, fill `#f2f5fa`, ink `#162136`, 16px type. Focus was clicked, not typed, not submitted. Crops: [sales-field-default.png](components/crops/sales-field-default.png), [sales-field-focused.png](components/crops/sales-field-focused.png). The phone menu has a separate "Enter your business email" field that was not filled.

## Menu

Products, Solutions and Resources open a full-width panel under the header. A menu link is 68px tall and fills `#f2f5fa` on hover. Crops: [menu-panel-opened.png](components/crops/menu-panel-opened.png), [menu-link-default.png](components/crops/menu-link-default.png), [menu-link-hover.png](components/crops/menu-link-hover.png). The phone control is `button.header-nav-button` titled "Toggle mobile navigation": [m-menu-button-default.png](components/crops/m-menu-button-default.png).

## Tabs

The home workflow row has Ideate, Plan, Deliver, Report, Evolve. Plan was selected. Crops: [workflow-tab-default.png](components/crops/workflow-tab-default.png), [workflow-tab-selected.png](components/crops/workflow-tab-selected.png).

## Nav text buttons

Log in and Contact Sales in the header are text buttons, 16px, ink `#162136`, transparent fill. Hover did not change the computed fill. Crops: [nav-login-default.png](components/crops/nav-login-default.png), [nav-sales-default.png](components/crops/nav-sales-default.png), [nav-products-default.png](components/crops/nav-products-default.png).

## Gaps

Not present on the public marketing surface: checkbox, radio, switch, tooltip, dialog, toast, table, avatar, badge, textarea as a distinct control (the sales form was not fully inventoried), destructive confirmation, empty, loading and error states.

Not captured: the signed-in app, the password step after an email on login.wrike.com, identity-provider buttons (seen, not clicked), disabled and loading buttons, focus ring width (focus-visible changed the fill, not a measured ring), icon sizes.
