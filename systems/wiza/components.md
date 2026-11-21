# Wiza components

Public signed-out surfaces, measured 2026-11-19. Values are token names. The computed reading is in [raw/components.json](raw/components.json).

Crops from the 2026-11-21 refresh are in [components/crops/](components/crops/). Page shots are in [screenshots/](screenshots/).

## Button

The marketing primary is `.button_main_wrap` with the filled variant. Background `light.component.buttonPrimary.background` (`#26114a`), text `light.component.buttonPrimary.text`, radius 8px, padding 8px 14px, height 36px, label 16px Inter. Seen on "Get started for free" and "Get Chrome extension".

The secondary is the same wrap on white, text `light.color.ink`, same radius and padding. Seen on "Log in", "Sign up", and "Get a demo".

Hover, focus-visible, pressed, disabled, and loading were not measured. Transition on the wrap is 0.45s for box-shadow, border-color, color, and background-color.

The login app uses a different button: `light.component.authSubmit` is `#7e43ff` on white text, 6px radius, 32px tall, 14px medium Inter var. "Log in via Google" is white with `#353849` text. Neither was clicked.

## Link

Nav links (`.nav_link1`) are 14px Inter, `light.color.ink`, 18px vertical padding, no radius. Footer links are 16px, `light.color.muted`. Prose links on the privacy page are `light.color.accent` and underlined.

## Text field

The home page has one email input, name `email`, placeholder "Work email". It is not inside a `form`. Background white, text `#3e0079`, radius 10px, height 40px, padding 0 14px, 1px border `rgba(47, 1, 151, 0.08)`. Nothing was typed.

The login field is a different control: 32px tall, 6px radius, black text, purple focus border. Nothing was typed. The signup field is the same empty control. Neither form was submitted.

## Text area, select, checkbox, radio, switch

Not present on the measured marketing pages. The pricing annual/monthly control is a custom pill toggle, not a switch. Annual is the default. Monthly was opened on 2026-11-21 and the prices repainted. Checkout was not entered.

## Tabs, menu, tooltip, dialog, toast

Solutions and Resources are hover menus. Both were opened on 2026-11-21 ([solutions crop](components/crops/menu-solutions-default.png), [resources crop](components/crops/menu-resources-default.png)). The phone menu button opens a full-screen drawer ([shot](screenshots/mobile-home-light-menu.png)). No tooltip, dialog, or toast was on the measured pages. Support in the Resources menu has href `#` and did not open a dialog.

## Card

Problem cards (`.tp_card_item`) are white at 80% opacity, 14px radius, padding 16px 20px, text `#312749`.

Pricing cards are 16px radius, 1px border, about 282 by 502. The default card is white at 60% opacity. The Email card (`.is-unique`) is solid white. Titles are 24px Britti Sans 500. Prices are 32px Britti Sans 500.

Customer story tiles on `/customers` are `#f6f8fa`, 8px radius, 384 by 202.

Feature tiles (`.col3_item`) are `#f6f7fa`, 40px radius.

Testimonials are white, 24px radius.

Section backgrounds use 56px radius. Their fills are gradients, so they are not a single colour token.

## List row, table, avatar, badge

No data table and no avatar component on the measured pages. The "Unlimited" pricing tag is a pill, 12px medium Inter, 1440px radius, padding 2px 6px. The G2 rating pill is `#ecedf3`, 14px, pill radius.

## Gaps

- Hover, focus-visible, pressed, disabled, loading, and error states were not fully computed. A primary hover crop exists. It does not establish a hover colour.
- Signup was photographed empty and not submitted. Book-a-demo and the opt-out form were not entered.
- The signed-in app was not captured. `login-extracted` stays not-started.
- Checkbox, radio, switch, textarea, select, toast, dialog, tooltip, table, and avatar were not on the measured pages.
