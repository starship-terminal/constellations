# Wiza components

Public signed-out surfaces, measured 2026-11-19. Values are token names. The computed reading is in [raw/components.json](raw/components.json).

Crops were not saved. The preview browser returned "The browser is not producing screenshot frames", so no element screenshot exists to crop.

## Button

The marketing primary is `.button_main_wrap` with the filled variant. Background `light.component.buttonPrimary.background` (`#26114a`), text `light.component.buttonPrimary.text`, radius 8px, padding 8px 14px, height 36px, label 16px Inter. Seen on "Get started for free" and "Get Chrome extension".

The secondary is the same wrap on white, text `light.color.ink`, same radius and padding. Seen on "Log in", "Sign up", and "Get a demo".

Hover, focus-visible, pressed, disabled, and loading were not measured. Transition on the wrap is 0.45s for box-shadow, border-color, color, and background-color.

The login app uses a different button: `light.component.authSubmit` is `#7e43ff` on white text, 6px radius, 32px tall, 14px medium Inter var. "Log in via Google" is white with `#353849` text. Neither was clicked.

## Link

Nav links (`.nav_link1`) are 14px Inter, `light.color.ink`, 18px vertical padding, no radius. Footer links are 16px, `light.color.muted`. Prose links on the privacy page are `light.color.accent` and underlined.

## Text field

The home page has one email input, name `email`, placeholder "Work email". It is not inside a `form`. Background white, text `#3e0079`, radius 10px, height 40px, padding 0 14px, 1px border `rgba(47, 1, 151, 0.08)`. Nothing was typed.

The login field is a different control: 32px tall, 6px radius, black text, purple focus border. Nothing was typed. Signup was a Cloudflare challenge and was not measured.

## Text area, select, checkbox, radio, switch

Not present on the measured marketing pages. The pricing annual/monthly control is a custom pill toggle, not a switch. Track `rgba(56, 5, 116, 0.04)`, white thumb, pill radius, 46px tall. Annual is the selected state. It was not clicked, so the monthly repaint is a gap.

## Tabs, menu, tooltip, dialog, toast

Not opened. The nav has Solutions and Resources dropdown toggles. They were not opened, so menu panel styles are a gap. No tooltip, dialog, or toast was on screen. The phone nav shows a 40 by 37 menu button (`.nav_hb_wrap`). It was not opened.

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

- No crops. Screenshot frames were not produced.
- Hover, focus-visible, pressed, disabled, loading, and error states were not computed.
- Dropdown menus, the phone menu, and the pricing monthly state were not opened.
- Signup, book-a-demo, and contact-sales forms were not entered.
- Checkbox, radio, switch, textarea, select, toast, dialog, tooltip, table, and avatar were not on the measured pages.
