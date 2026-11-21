# Squarespace components

Public marketing site, measured on 2026-11-21. Crops were not cut. The states below are the whole-page shots in [screenshots/](screenshots/). Values are token names from [tokens.json](tokens.json). A state that was not read is Not captured.

## Button

Primary fill is `light.component.button.fill` (`core.palette.ink`) with `light.component.button.text`. Height `core.size.control` (60px), radius `core.radius.control` (4px), padding `core.space.23` by `core.space.28`, label `core.typography.label` in uppercase.

On the dark hero the same control inverts: `light.component.button.inverseFill` and `inverseText`. Seen in [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

Secondary (BUY NOW) has no fill. Its edge is an inset 2px shadow, `core.shadow.outline`.

| State | Where |
|---|---|
| Default | [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) |
| Inverse on dark header | [screenshots/home-light-products-menu.png](screenshots/home-light-products-menu.png) |
| Hover | [screenshots/home-light-cta-hover.png](screenshots/home-light-cta-hover.png). The shot exists. The computed hover colour was not read. |
| Focus-visible | Not captured |
| Pressed | Not captured |
| Disabled | Not present on the captured public pages |
| Loading | Not present |

## Link

Header LOG IN is a text link. Its computed colour on the hero was not isolated from the button wrapper (the wrapper reads `sans-serif` at 16px). Footer links sit on the black footer. The blue link role `light.text.link` is the discount badge colour, also used for the annual-savings line on pricing.

## Text field

The get-started page opens a search field, "Search for your site topic", with a topic list under it. Seen in [screenshots/get-started-light-default.png](screenshots/get-started-light-default.png). The field's computed styles were not read (the templates page input lookup returned no visible input). Nothing was typed. The field was not submitted.

## Menu

Desktop PRODUCTS, SOLUTIONS and RESOURCES open `global-navigation__menu`: 1082 by 534, fill `light.component.menu.fill`, radius `core.radius.menu`, shadow `core.shadow.menu`.

| State | Where |
|---|---|
| Products open | [screenshots/home-light-products-menu.png](screenshots/home-light-products-menu.png) |
| Solutions open | [screenshots/home-light-solutions-menu.png](screenshots/home-light-solutions-menu.png) |
| Phone drawer | [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |

## Badge

The 50% off badge is `light.component.badge.fill` and `light.component.badge.text`, radius `core.radius.badge`, padding 8px 16px. Seen on [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Card

Pricing plan cards (Basic, Core, Advanced) sit on the paper page. The card container's fill was not isolated from the button group, so card fill is Not captured as its own token. The cards are in the pricing screenshot.

Contact page cards (Contact Support, Security Escalations) are hairline boxes on paper. [screenshots/contact-light-default.png](screenshots/contact-light-default.png).

## Tabs

The billing control is a pill track, `light.background.track`, radius `core.radius.track`, padding 4px. Pay annually is selected (black). Pay monthly is `light.text.muted`. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) and [screenshots/pricing-light-billing-toggle.png](screenshots/pricing-light-billing-toggle.png).

## Icon button

The phone header uses a hamburger and a close mark. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Offer terms is a 32px icon button on the promo banner. Its tooltip was not captured: the open menu covered it.

## Gaps

| Checklist item | Status |
|---|---|
| Text area | Not present on the captured public pages |
| Select | Not present. The footer currency list was not opened |
| Checkbox | Not present |
| Radio | Not present. The billing toggle is a tab track, not a radio |
| Switch | Not present |
| Tooltip | Not captured. Offer terms opens one. The click was blocked by the open menu |
| Dialog | Not present as a modal on the captured pages. The get-started topic list is an inline panel |
| Toast | Not present |
| Table | Not present. The feature index is a long list, not a data table |
| Avatar | Not present |
| List row | The phone menu rows and the get-started topic rows are list rows. Phone menu: [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Focus ring | Not captured |
| Pressed | Not captured |
| Dark theme | Not present. Inversion is per surface, not a theme |
