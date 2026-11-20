# Programa components

Public marketing site only, read on 2026-11-21 from [programa.design](https://programa.design/). Crops are cut from the full-colour captures and saved at 2x. Values are token names from [tokens.json](tokens.json).

## Button

The header **Start free** control is a mint pill, not the yellow accent.

| State | Crop | Values |
|---|---|---|
| default | [button-primary-default.png](components/crops/button-primary-default.png) | background `light.component.buttonPrimary.background`, text `light.component.buttonPrimary.text`, radius `light.component.buttonPrimary.radius`, height 28px |
| hover | not a colour change on this control | computed hover matched default |
| focus-visible | recorded in [raw/components-computed.json](raw/components-computed.json) | focus via `focus()`. Ring is the browser default, not a designed token |
| pressed | CDP forcePseudoState, not a click | login and register were not opened |

The hero **Get started** control is the dark button: `light.component.buttonDark`. Hover paints `light.component.buttonDark.hover`.

The hero **Watch a demo** control is the white button: `light.component.buttonSecondary`. Hover paints `light.raised`.

The pricing **Start 7 day trial** control is the yellow accent. It was not clicked. Its fill is `light.accent`.

## Link

Nav links (Features, Solutions, Pricing, Learn) are Inter 14px, colour `light.text`, radius 6px. Hover paints `light.raised`. Crop: [nav-link-default.png](components/crops/nav-link-default.png).

Footer links are Inter 12px, colour `light.link`. Hover adds an underline. Crop was not cut because the link sits far down the page.

Log in is a quiet text button. Crop: [button-quiet-default.png](components/crops/button-quiet-default.png). It opens the login wall. Not followed.

## Text field

Blog search (`input[name="query"]`, placeholder Explore the blog) and the contact email field were focused and not typed into. The measured box is the inner input, 14px Inter, transparent background, 20px tall. The painted field chrome is Not captured.

## Switch

Pricing has a Monthly / Annual toggle. The annual state is in [pricing-light-default.png](screenshots/pricing-light-default.png). The control was clicked locally and not submitted. No computed switch metrics were kept, because the first selector missed the thumb.

## Accordion

FAQ questions are buttons. Open state: [faq-light-accordion.png](screenshots/faq-light-accordion.png). Question text is Inter 16px, colour black.

## Badge

The Features menu marks Schedules with a New chip. Crop: [badge-default.png](components/crops/badge-default.png). Background `light.component.badge.background` (green pale), text `light.component.badge.text` (green dark), radius 6px.

## Menu

Desktop Features, Solutions and Learn menus open on hover. Shots: [home-light-features-menu.png](screenshots/home-light-features-menu.png), [home-light-solutions-menu.png](screenshots/home-light-solutions-menu.png), [home-light-learn-menu.png](screenshots/home-light-learn-menu.png).

Phone menu opens from the button labelled Open menu. Shots: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png), [mobile-home-light-menu-features.png](screenshots/mobile-home-light-menu-features.png).

## Card

The pricing Pro card is visible in [pricing-light-default.png](screenshots/pricing-light-default.png). Its metrics were not tokenised. The selector matched the page, not the card.

## Display type

H1 uses Rhymes Display, 80px, weight 300, line-height 64px, colour `light.text`. Crop: [display-default.png](components/crops/display-default.png).

## Not present on the public site

Text area, select, checkbox, radio, tooltip, toast, table, and a designed avatar component. Contact shows staff photos. Those are published portraits, not a component with states.

Dialog: no public dialog mounted. Login is a separate page, not a dialog.

## Gaps

- Signed-in app components are behind `https://app.programa.design/login`. Not captured.
- Disabled, loading, and error states were not shown on the public pages.
- Text field chrome, plan card metrics, and the billing switch thumb are Not captured.
- Icon extraction was not run. Icons are visible in the menu screenshots.
