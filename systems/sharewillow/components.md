# Sharewillow components

Public marketing site and the login wall, measured 2026-11-21. Crops are in [components/crops/](components/crops). Values are token names from [tokens.json](tokens.json). A state that was not reached is Not captured.

## Button

Primary action is a pill. Fill is `light.component.button.background` (espresso). Label is `light.component.button.text`. Height `core.size.buttonHeight` (56px). Radius is a full pill (`core.radius.button`).

| State | Evidence |
|---|---|
| default | [components/crops/button-primary-default.png](components/crops/button-primary-default.png) |
| hover | Fill shifts to `core.palette.buttonHover` (rgb 43, 26, 16). [components/crops/button-primary-hover.png](components/crops/button-primary-hover.png) |
| focus-visible | Keyboard focus landed. Computed border and outline did not change in this pass. Focus ring colour is Not captured. |
| pressed | CDP `:active:hover`. Same fill as hover. [components/crops/button-primary-pressed.png](components/crops/button-primary-pressed.png) |
| disabled | Not captured |
| loading | Not captured |

Login submit on the wall is a separate control: 44px tall, 8px radius, near-black fill. Not clicked. [components/crops/login-button-default.png](components/crops/login-button-default.png).

## Link

Quiet text link "See the app" uses `light.text.link` (espresso), 15px, weight 500, no fill. Hover did not change the computed colour in this pass.

Header nav link is 14px. Hover paints a 5% espresso wash. [components/crops/nav-link-hover.png](components/crops/nav-link-hover.png).

## Text field

Demo page field: paper fill, 48px tall, 16px radius, espresso text. Focus-visible and click-focus were measured. No error state was triggered, because no form was submitted. Sample text was not typed into an email or phone field.

| State | Evidence |
|---|---|
| default | [components/crops/text-field-default.png](components/crops/text-field-default.png) |
| hover | [components/crops/text-field-hover.png](components/crops/text-field-hover.png) |
| focused | [components/crops/text-field-focused.png](components/crops/text-field-focused.png) |
| error | Not captured. Validation was not triggered. |
| disabled | Not captured |

## Menu

Product disclosure opens a panel (about 860×391 in the crop) with product links and a dark "The tech app" card. [components/crops/menu-opened.png](components/crops/menu-opened.png). Full page: [screenshots/home-light-product-menu.png](screenshots/home-light-product-menu.png).

Industries disclosure: [screenshots/home-light-industries-menu.png](screenshots/home-light-industries-menu.png).

Phone menu: [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Badge

"Coming soon" sits on the Agents nav item in lemon. The measurement selector missed it (`missing` in raw/components-computed.json). Visible in [screenshots/home-light-default.png](screenshots/home-light-default.png). Colour is `light.accent.default` from the declared token, not from a crop.

## Card

Pricing and product pages use paper and surface-2 panels on ivory. The pricing measurement landed on a large section rather than one card. See [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Login wall

[screenshots/login-light-wall.png](screenshots/login-light-wall.png). Card on a warm off-white page. Email and password fields, Google and phone buttons, Login submit. Nothing was typed or submitted. Google and phone were not clicked.

## Not present on the public site

Checkbox, radio, switch, tabs, tooltip, toast, table, avatar, select, and text area were not found as product controls on the captured public pages. The login wall has one checkbox ("Remember me next time") that was not measured as its own component. Icon button: the phone header uses a hamburger (`Open menu`) and the desktop nav uses text buttons. No separate icon-button style was isolated.

## Gaps

- Focus ring colour: Not captured.
- Disabled, loading, and error states: Not captured.
- Scrim behind menus: Not captured.
- Signed-in app components (plans, payouts, people, settings): behind [https://app.sharewillow.com/login](https://app.sharewillow.com/login). Not captured.
- Dark theme: not present as a toggle. Hero dark colours are a section.
