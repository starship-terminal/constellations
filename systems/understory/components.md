# Understory components

Public marketing UI on understory.io, measured 2026-11-21. Crops were not cut. The states below are the full screenshots. Values are token names from [tokens.json](tokens.json).

## Button

Primary is `a.button-n`. Fill `light.action.primary` (moss), label `light.action.primaryText`, radius `core.radius.button` (9px), type `core.typography.label`. Header instance is 29px tall (`core.size.button`). Pricing "Start your free trial" is 40px tall with 12px 15px padding. Hover did not change the computed background.

Secondary is `a.button-n.is-lightgreen`. Fill `light.action.secondary` (moss at 10%). Ghost Login is `a.button-n.is-transparent`.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Link

Nav labels are `.dropdown-toggle_nav` and `.nav_menu_link`, Inter 13.5px weight 450, colour `light.text.nav` on the toggle (`#222222`) and moss elsewhere. Dropdown items inside the open menu are white on moss.

## Text field

`input.field-form_link.w-input`. Height 38px, transparent fill, no border, padding-left 15px, placeholder "Enter your website" or "Enter your email". Not submitted. Focus shot: [screenshots/home-light-field-focus.png](screenshots/home-light-field-focus.png). A focus ring was not measured.

Help center search is a separate field on help.understory.io: [screenshots/help-light-default.png](screenshots/help-light-default.png). Not submitted.

## Tabs

Homepage tabs: Less admin, More bookings, Better booking experience. Current tab is underlined. Shown in [screenshots/home-light-tab.png](screenshots/home-light-tab.png).

Pricing feature tabs (Sell more, Save time, Get paid faster, Get insights) exist below the plan cards. The selected pricing tab measured a `rgb(223, 221, 210)` fill and 9px radius. That fill is not a declared custom property. Not tokenised.

Blog filters (All Stories, Industry Insights, News, Host Story) are radios styled as tabs. [screenshots/blog-light-filter.png](screenshots/blog-light-filter.png).

## Menu

Booking system and Marketing are hover dropdowns. The open panel is moss, white text, 12px radius, 327px tall. [screenshots/home-light-menu-booking.png](screenshots/home-light-menu-booking.png), [screenshots/home-light-menu-marketing.png](screenshots/home-light-menu-marketing.png).

Phone drawer: [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Nested sections were not expanded.

## Dialog

No marketing dialog was opened. The cookie banner (`#coiOverlay`) was hidden, not accepted. Login is a separate page, not a dialog, and was not screenshotted.

## Card

Plan cards (`.plan-card`) use `light.background.surface` (`#eae8dd`), radius 15px, no shadow. Recommended badge is moss fill, 6px top radius. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Switch

Pricing Monthly / Yearly is `.billing-toggle` / `.toggle-track`, 27px tall. Clicking Yearly (no form submit) changed Starter from €29 to €35. [screenshots/pricing-light-yearly.png](screenshots/pricing-light-yearly.png). Track colours were not isolated as tokens.

## Accordion

FAQ rows (`.faq-item_heading`) open on the page. The first home FAQ is active on load. [screenshots/home-light-faq.png](screenshots/home-light-faq.png), [screenshots/support-light-faq.png](screenshots/support-light-faq.png).

## Badge

"Recommended" on the Starter plan. "For workshops, classes, tours, & events" is a small pill on the homepage. Pill fill was not isolated.

## Icon button

Phone close control in the nav drawer. Chat launcher (dark circle, bottom right) is a third-party widget. Not measured.

## Not present on the captured public pages

Text area, select, checkbox (the try-for-free page has checkboxes; that form was not filled), radio as a control style beyond the blog filter, toast, table, avatar, tooltip.

## Gaps

- Hover and pressed colours for the primary button: computed background stayed moss. Not captured as a distinct step.
- Focus ring: not painted on the measured controls. Not captured.
- Disabled, loading, and error states: not shown without submitting a form.
- Motion durations and easings: not read.
- Elevation: plan cards have `box-shadow: none`.
- Dark theme: not on understory.io. developer.understory.io ships a theme button; the dark frame in [screenshots/docs-dark-default.png](screenshots/docs-dark-default.png) is that site's own theme, not tokenised.
- Signed-in backoffice, signup, preview URL submit, newsletter, demo booking, guest checkout: not captured. Login URL recorded in [site-tree.md](site-tree.md).
