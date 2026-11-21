# Typeform components

Public marketing controls, measured signed out on 2026-11-21. Crops are in [components/crops/](components/crops). Values name tokens in [tokens.json](tokens.json).

The product behind login (the form builder, results, contacts) was not reached. See Gaps.

## Button

Primary action on the dark header is a light pill. Secondary action is a dark pill.

| State | Crop | Values |
|---|---|---|
| Primary default | [button-primary-default.png](components/crops/button-primary-default.png) | Fill `light.button.secondary-bg`, text `light.text.primary`, radius `core.measured.button-radius` (12px), height 40px |
| Primary hover | [button-primary-hover.png](components/crops/button-primary-hover.png) | Fill `light.button.secondary-hover` |
| Primary focus | [button-primary-focus-visible.png](components/crops/button-primary-focus-visible.png) | Keyboard focus landed. Outline computed to none. |
| Secondary default | [button-secondary-default.png](components/crops/button-secondary-default.png) | Fill `light.accent.default`, text `light.text.on-accent` |
| Secondary hover | [button-secondary-hover.png](components/crops/button-secondary-hover.png) | Fill `light.accent.pressed` (#3e3040, measured) |
| Secondary focus | [button-secondary-focus-visible.png](components/crops/button-secondary-focus-visible.png) | Focus landed. No painted ring. |

## Link

| State | Crop | Values |
|---|---|---|
| Log in default | [link-login-default.png](components/crops/link-login-default.png) | Text `light.text.invert` on the dark header, 16px Twklausanne |
| Log in hover | [link-login-hover.png](components/crops/link-login-hover.png) | No fill change |
| Log in focus | [link-login-focus-visible.png](components/crops/link-login-focus-visible.png) | Focus landed. No painted ring. |

## Navigation

| State | Crop | Values |
|---|---|---|
| Platform trigger | [nav-platform-default.png](components/crops/nav-platform-default.png) | 16px, transparent, height 88px on the dark header |
| Platform hover | [nav-platform-hover.png](components/crops/nav-platform-hover.png) | Opens the menu. See [home-light-platform-menu.png](screenshots/home-light-platform-menu.png) |
| Menu panel | [nav-menu-default.png](components/crops/nav-menu-default.png) | Fill `light.invert`, shadow `core.measured.menu-shadow` |
| Menu item | [nav-menu-item-default.png](components/crops/nav-menu-item-default.png) | 16px, transparent row |

Phone menu: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Billing toggle

| State | Crop | Values |
|---|---|---|
| Yearly selected | [billing-yearly-default.png](components/crops/billing-yearly-default.png) | Fill `light.border.default` (#e5e1e5), text `light.text.primary`, 14px, radius 12px |
| Monthly unselected | [billing-monthly-default.png](components/crops/billing-monthly-default.png) | Transparent, text `light.text.secondary` |

## Type

| Role | Crop | Values |
|---|---|---|
| Hero | [hero-heading-default.png](components/crops/hero-heading-default.png) | Tobias, 80px measured on the homepage (`core.measured.hero-size`). Declared display is 5rem. |

## Dialog

Template preview is a public dialog: [template-light-preview.png](screenshots/template-light-preview.png). It was opened and closed. It was not submitted.

## Shared values

Page ground is `light.page` (#faf9fb). The header and the open menus invert to `light.invert` (#2a222b) with `light.text.invert`. The purple highlight (`light.text.highlight`, #9454ab) is used for eyebrows and NEW badges, not for the main button.

## Gaps

- Text field, text area, select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, badge: not present as product controls on the captured public pages, or not measured. The login email field is visible in [login-light-default.png](screenshots/login-light-default.png) and was not filled.
- Disabled, loading, error, pressed: not held. Pressed is Not captured.
- Focus ring colour: Not captured. Focus landed and the outline computed to none.
- Signed-in builder, results, and settings: behind [https://admin.typeform.com/login](https://admin.typeform.com/login). Not captured.
- OneTrust cookie dialog: present, hidden, never answered.
