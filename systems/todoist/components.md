# Components

Measured on the public marketing site and the empty login page. The 2026-11-19 readings are in [raw/readings.json](raw/readings.json). Crops from the 2026-11-21 Playwright pass are in [components/crops/](components/crops/).

## Button

Home hero "Start for free" (`_primary_` `_xl_`).

| State | Fill | Text | Radius | Padding | Height |
|---|---|---|---|---|---|
| default | `light.background.action` oklch(61.47% .1986 30.12) | white | 15px | 12px 16px | 64px |
| focus | same fill | white | 15px | same | same |

Focus painted `box-shadow: oklch(0.9451 0.0168 215.46) 0px 0px 0px 4px, oklch(0.6772 0.1122 245.18) 0px 0px 0px 1px`. That matches `--shadow-focusvisible-default`. Outline was none.

A real hover on 2026-11-21 did not change the computed fill. The declared hover fill is `--actionable-primary-background-onhover`, oklch(56.45% .1938 31.13), stored as `light.background.action-hover`. The crop is [components/crops/hero-cta-hover.png](components/crops/hero-cta-hover.png). Focus is [components/crops/hero-cta-focus-visible.png](components/crops/hero-cta-focus-visible.png).

Nav "Log in" and pricing "Get started" are the quiet button: fill rgba(37, 34, 30, 0.07), text rgb(37, 34, 30), radius 8px, padding 9px 14px, height 39px. Font Inter 15.5px weight 600 on the pricing link, weight 500 on the nav link.

Login "Log in" is a different control. Fill rgb(211, 51, 34), text white, radius 6px, height 48px, width 376px, font -apple-system 18px weight 700. It was not clicked. A real hover on 2026-11-21 painted rgb(199, 56, 42). See [components/crops/login-submit-default.png](components/crops/login-submit-default.png) and [components/crops/login-submit-hover.png](components/crops/login-submit-hover.png).

## Link

Login "Forgot your password?" and "Sign up" are rgb(211, 51, 34), 13px, weight 400. Marketing nav links are the quiet button above, not underlined.

## Text field

Login email and password. The wrapper is 65px tall, radius 6px, padding 8px 8px 4px. Rest border is 1px solid rgb(229, 229, 229). After `input.focus()` the border became 1px solid rgb(184, 184, 184). No box-shadow and no outline. The input itself is 16px weight 600, color rgb(32, 32, 32). The label is 12px.

Placeholder text was "Enter your email..." and "Enter your password...". Nothing was typed.

## Icon button

A 24px round close control sat on the cookie dialog (radius 50%, 2px border). It belongs to Osano, not to Todoist's button system. No product icon button was measured.

## Card

Pricing articles: background rgb(255, 255, 255), border 1px solid oklch(0.2538 0.0086 75.21 / 0.12), radius 10px, padding 24px 32px, width 363px, shadow none. Plan names (Beginner, Pro, Business) are Graphik 31px weight 600.

## Badge, tabs, menu, select, checkbox, radio, switch, text area, tooltip, dialog, toast, list row, table, avatar

Not present on the pages that were measured, or present only inside the Osano cookie dialog (its toggle and buttons). Those Osano colours were not tokenised.

Signup shows email and password plus Google, Facebook and Apple. A Cloudflare Turnstile field is in the form. The form was not submitted.

## Gaps

- Hover and pressed were not forced. Declared hover tokens are labelled as declared.
- No dark theme on these pages. Login `colorScheme` was `light`.
- No screenshots or crops.
- Signed-in app, validation errors, empty states, and paid checkout were not entered.
