# Leonardo.Ai components

Public marketing site only, captured 2026-11-21, signed out. Crops are the real controls. Values are computed styles or flat fills sampled before quantise. A state that was not reached is listed under Gaps.

## Button

White pill, black label, full radius. Header Log in is 87 by 35 px, 16 px Canva Sans, weight 500, fill `#ffffff`, text `#000000`. Hero Start now is a white pill at 48 px tall. Subscribe on pricing is the same pill in violet `#6e60ee` with white text, 118 by 48 px.

Crops: [button-login-default.png](components/crops/button-login-default.png), [button-login-hover.png](components/crops/button-login-hover.png), [button-subscribe-default.png](components/crops/button-subscribe-default.png).

Hover on Log in did not change the computed fill. Focus-visible on the hero link did not paint a separate ring in the reading. Pressed was not held.

## Icon button

Phone header uses a two-line menu mark. The open drawer uses an X. Desktop video controls (Previous, Unmute, Next) sit on the hero. Crops were not cut for the phone mark. See [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png).

## Link

Pricing and Contact in the header are white text, 14 px, no fill. Developer API on the phone hero is an underlined white link. Menu rows are links with a title and a muted description.

Crops: [nav-link-default.png](components/crops/nav-link-default.png), [menu-link-default.png](components/crops/menu-link-default.png).

## Text field

Contact page fields are outlined, dark fill, placeholder text. The form was not filled and not submitted. A Turnstile widget is present, so the field reading from a later pass was blocked. The visible fields are in [contact-dark-default.png](screenshots/contact-dark-default.png). Computed field metrics: Not captured.

## Text area

"Describe your issue" on the contact form. Same gap as the text field. Visible in the contact screenshot. Not submitted.

## Select

Enterprise sales form includes country and company-size selects. That tab was not opened after the first map. Select metrics: Not captured.

## Checkbox, radio, switch

Not present on the captured public pages.

## Tabs

Pricing audience control is `role=tab`. Selected SOLO is violet `#6e60ee` (rgb 110, 96, 238), 205 by 61 px, pill radius, 12 px Canva Sans, weight 500. Idle TEAM is a 10% white fill with muted text. Billing is a second pill: Pay Monthly is white with black text, Pay Yearly is transparent with 70% white text and a green "Up to 20% off" badge.

Crops: [tab-selected.png](components/crops/tab-selected.png), [tab-default.png](components/crops/tab-default.png), [billing-toggle-selected.png](components/crops/billing-toggle-selected.png).

## Menu

Create, Industry, Business and Learn open a dark panel (`#111111` sampled) with columns and a featured card. Phone uses a full-screen drawer. See [home-dark-create-menu.png](screenshots/home-dark-create-menu.png) and [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png).

## Tooltip, dialog, toast

Not present on the captured public pages. Cookie consent, if it mounts, was hidden and not answered.

## Card

Pricing plans are dark cards with a hairline border. Names are colour-coded: FREE white, ESSENTIAL yellow `#f8c030`, PREMIUM green, ULTIMATE red `#f85848`. A green Best Offer ribbon sits on Premium. Prices are `#ededed` at 40.5 px.

## List row

Phone drawer rows are full-width labels with a hairline and a trailing chevron. See the phone menu screenshot.

## Table

Not present.

## Avatar

Not present on the marketing header. Artist story cards use photos. Those photos are published marketing, not an account avatar.

## Badge

Green "Up to 20% off" and "Best Offer" on pricing. Support and billing on contact is a green pill `#03e65b`. Computed badge metrics: Not captured (the text node was not isolated). Visible in [pricing-dark-default.png](screenshots/pricing-dark-default.png) and [contact-dark-default.png](screenshots/contact-dark-default.png).

## Gaps

- Signed-in app controls (generate, canvas, library, settings): not captured. Log in opens https://app.leonardo.ai/auth/login, which asks for email and password or Canva, Apple, Google, Microsoft. That branch was stopped.
- Text field, text area and select computed styles: Not captured. Contact later sat behind a Turnstile widget.
- Checkbox, radio, switch, tooltip, dialog, toast, table: not present on the public pages that were shot.
- Hover and pressed often paint the same fill. Where the computed style did not change, no separate hover token was invented.
- Light theme: not present on the public marketing site.
