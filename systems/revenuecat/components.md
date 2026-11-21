# RevenueCat components

Public marketing site and public docs, captured 2026-11-21, signed out. Crops are 2x element screenshots. Values are token names. A state that was not on the page is listed under Gaps.

## Button

The primary action is a blue pill. Nav Sign up is 36px tall, Object Sans 14/500, fill `light.component.button-primary-bg` (`#576cdb`), label `light.component.button-primary-text`. Hover darkens to `light.component.button-primary-bg-hover` (`#3e52b9`). The hero and sales submit buttons are the same fill at 48px (`light.component.button-lg-height`).

| State | Crop |
|---|---|
| default | [nav-signup-default](components/crops/nav-signup-default.png) |
| hover | [nav-signup-hover](components/crops/nav-signup-hover.png) |
| focus | [nav-signup-focus](components/crops/nav-signup-focus.png) |
| pressed | [nav-signup-pressed](components/crops/nav-signup-pressed.png) (forced `:active` failed; the crop matches focus, not a held press) |
| large default | [hero-cta-default](components/crops/hero-cta-default.png) |
| large hover | [hero-cta-hover](components/crops/hero-cta-hover.png) |
| form submit | [sales-submit-default](components/crops/sales-submit-default.png), hover [sales-submit-hover](components/crops/sales-submit-hover.png) |

Disabled and loading were not on any public page.

## Icon button

Docs theme toggle is a 32px round icon button. [docs-theme-toggle-default](components/crops/docs-theme-toggle-default.png). Mobile menu close is the X in [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png). No separate icon-button hover crop.

## Link

Log in is text, not a pill: 14/500, `light.muted`, darkening on hover. [nav-login-default](components/crops/nav-login-default.png), [nav-login-hover](components/crops/nav-login-hover.png).

Contact sales is an outline pill: text `light.component.button-outline-text`, 1px border. [nav-contact-default](components/crops/nav-contact-default.png), [nav-contact-hover](components/crops/nav-contact-hover.png).

## Text field

Hero email is a white pill, 64px, border `light.component.field-border`, focus border `light.component.field-border-focus`. Nothing was typed. [hero-email-default](components/crops/hero-email-default.png), [hero-email-focus](components/crops/hero-email-focus.png).

Sales first-name field is a 56px rounded-4 rectangle on `light.surface`, focus border the accent blue. [sales-field-default](components/crops/sales-field-default.png), [sales-field-focus](components/crops/sales-field-focus.png). The form was not submitted.

## Text area

Present on `/talk-to-sales` and `/contact` ("Tell us more", "How can we help?"). Not cropped. Not filled.

## Select

`/talk-to-sales` has "What would you like to discuss?". The page runner looked for a button of that name and did not find one, so the open menu was not captured. The closed form is [talk-to-sales-light-default](screenshots/talk-to-sales-light-default.png). No value was chosen.

## Checkbox, radio, switch

Not present on the marketing pages that were captured. Signup has a marketing checkbox behind the signup wall, which was not filled.

## Tabs

Pricing in-page tabs (Growth Tools, All features, Testimonials, Certifications, FAQs) are text buttons, Helvetica Neue 18/500, accent blue. [pricing-tab-default](components/crops/pricing-tab-default.png), [pricing-tab-hover](components/crops/pricing-tab-hover.png), [pricing-tab-selected](components/crops/pricing-tab-selected.png). Page shots: [pricing-light-tab-all-features](screenshots/pricing-light-tab-all-features.png), [pricing-light-tab-testimonials](screenshots/pricing-light-tab-testimonials.png), [pricing-light-tab-faqs](screenshots/pricing-light-tab-faqs.png).

Changelog filters (All, Integration, SDK, and the rest) are text chips. Selected state did not change the computed colour. [changelog-chip-default](components/crops/changelog-chip-default.png), [changelog-chip-hover](components/crops/changelog-chip-hover.png), [changelog-chip-selected](components/crops/changelog-chip-selected.png).

## Menu

Header mega-menus, opened by click:

- [home-light-menu-why-revenuecat](screenshots/home-light-menu-why-revenuecat.png)
- [home-light-menu-solutions](screenshots/home-light-menu-solutions.png)
- [home-light-menu-developers](screenshots/home-light-menu-developers.png)
- [home-light-menu-resources](screenshots/home-light-menu-resources.png)

Phone sheet: [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png). The Eng locale control sits in that sheet. The desktop locale button did not receive a click (timeout); the phone sheet is the evidence.

Nav trigger hover turns the label the brand red. [nav-trigger-default](components/crops/nav-trigger-default.png), [nav-trigger-hover](components/crops/nav-trigger-hover.png).

## Tooltip

Not present.

## Dialog

Docs search opens a dialog with an empty field, filter chips, and a scrim. Nothing was typed and no AI prompt was sent. [docs-light-search-open](screenshots/docs-light-search-open.png). The cookie banner is a third-party dialog and was hidden, not accepted.

## Toast

Not present.

## Card

Pricing plan card and docs SDK cards. The pricing card is in [pricing-light-default](screenshots/pricing-light-default.png). Docs SDK cards are in [docs-light-default](screenshots/docs-light-default.png) and, dark, [docs-light-dark](screenshots/docs-light-dark.png). No separate crop.

## List row

FAQ row click opened the nav trigger of the same name rather than an FAQ answer, so [faq-row-open](components/crops/faq-row-open.png) is the nav label in the red hover colour, not an expanded answer. The FAQ tab page is [pricing-light-tab-faqs](screenshots/pricing-light-tab-faqs.png). Glossary letter P is [glossary-light-letter-p](screenshots/glossary-light-letter-p.png).

## Table

Not measured. Pricing comparison, if present below the fold, is in [pricing-light-full](screenshots/pricing-light-full.png). No table token.

## Avatar

Not present on the marketing chrome. Customer logos in the homepage strip are brand marks, not avatars.

## Badge

Changelog filter chips above. Docs "Popular articles" chips are in [docs-light-default](screenshots/docs-light-default.png). No separate badge crop.

## Shared values

| Role | Token |
|---|---|
| Page | `light.page` #ffffff |
| Text | `light.text` #1f1f47 |
| Accent | `light.accent` #576cdb |
| Brand red | `light.brand` #f2545b |
| Focus border | `light.focus` #576ddc |
| Header height | `core.space.header` 64px |
| Motion | `core.motion.duration` 0.15s, `core.motion.easing` cubic-bezier(0.4, 0, 0.2, 1) |

## Gaps

- Pressed was not captured. CSS.forcePseudoState failed because the DOM agent was not enabled. The pressed crop matches focus.
- Disabled, loading, error, toast, tooltip, checkbox, radio and switch were not on the public pages.
- Docs dark has a heading colour and a screenshot. Page, surface, border and button fills in dark were not re-read after the toggle.
- The sales select did not open. The runner found no button named "What would you like to discuss?".
- Login and signup walls were photographed and not filled. They are boundaries, not components of the marketing system.
