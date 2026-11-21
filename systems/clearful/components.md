# Components

Public Clearful, signed out, 2026-11-21. Values are token names. Crops were not cut: the states below are the live readings, and the screenshots show the layout.

## Button

Nav pill `a.button.is-small.w-button`. Fill `{light.accent}` (`#1953ff`), label `{light.on-accent}`, radius `{core.radius.pill}` (999px), height 50px, padding 12px 20px, Manrope 16/600. Hover paints `#1b1bbc` (`{light.accent-hover}`), a deleted Webflow variable, not a declared token. Screenshot: [home-get-app](screenshots/home-get-app.png) shows the same blue family on the store chips. Default is in [home-light-default](screenshots/home-default.png).

Hero button `a.button.is-large`. Same fill, 20px type, 82px tall, with a 6px `{core.color.brand.blue-200}` border as a halo.

## Link

Nav link `a.navbar1_link`. Manrope 16/600, `{light.text}`, padding 8px 20px, no underline. Guided Journals and Log In share this recipe. Log In leaves for the sign-in wall.

## Text field and text area

Contact page. Name field is 60px tall, 8px radius, 1px `{light.border}` (`#e1e1e1`), white fill. Message area is 180px tall, same border. Neither was filled or submitted. Screenshot: [contact-default](screenshots/contact-default.png).

## Tabs

Home timeline: Weekly, Monthly, Quarterly, Bi-Yearly, Yearly. What's New: All, New Features, Product Improvements, New Guided Journals, Bug Fixes. Both are Webflow `a.w-tab-link` panes. Screenshot: [home-timeline-monthly](screenshots/home-timeline-monthly.png), [whats-new-tab-features](screenshots/whats-new-tab-features.png).

## Menu

Phone nav drawer, opened from `.w-nav-button`. White sheet, Guided Journals, Log In, and the blue pill. Screenshot: [mobile-home-menu-open](screenshots/mobile-home-menu-open.png). Desktop has no dropdown.

## Dialog

Get-app overlay `.modal_get-app`. Scrim `{light.scrim}` (`rgba(0, 0, 0, 0.25)` measured on `.modal_get-app_background-overlay`; the painted panel reads as a blue wash in the screenshot). Close control top right. Store chips are outlined pills. Screenshot: [home-get-app](screenshots/home-get-app.png), [mobile-home-get-app](screenshots/mobile-home-get-app.png).

## Card

Library journal cards and What's New update cards. Surface and type follow the page tokens. Screenshot: [library-default](screenshots/library-default.png).

## Badge

App Store laurels and the 4.8 rating on the home hero and the get-app overlay. Not a separate component token.

## Search

Help center search field on [support-default](screenshots/support-default.png). Nothing was typed.

## Not present on the public surface

Icon button as its own recipe (the menu and close marks are the exceptions), select, checkbox, radio, switch, tooltip, toast, list row, table, avatar.

## Gaps

- Focus ring: keyboard focus on the nav pill did not paint a distinct ring in the live reading. Not captured.
- Pressed, disabled, loading, and error states do not appear on the public pages.
- Signed-in components (editor, entries, settings) sit behind [the sign-in wall](screenshots/sign-in-wall.png). Not captured.
- No `components/crops/` directory. States are whole-page screenshots, not element crops.
