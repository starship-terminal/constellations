# Components

Public controls on lottiefiles.com, measured 2026-11-21 from computed styles. Crops are 2x screenshots of the element. A missing state is listed under Gaps.

## button-primary

- default: [button-primary-default.png](components/crops/button-primary-default.png). bg `oklch(0.626 0.11 185.333)`, text `oklch(0.985 0 0)`, 16px/500, radius `12px`, height `48px`. Via home hero.
- hover: [button-primary-hover.png](components/crops/button-primary-hover.png). bg `oklab(0.626 -0.109524 -0.0102239 / 0.9)`, text `oklch(0.985 0 0)`, 16px/500, radius `12px`, height `48px`. Via pointer hover.
- focus-visible: [button-primary-focus-visible.png](components/crops/button-primary-focus-visible.png). bg `oklab(0.626 -0.109524 -0.0102239 / 0.9)`, text `oklch(0.985 0 0)`, 16px/500, radius `12px`, height `48px`. Via focus().

## button-secondary

- default: [button-secondary-default.png](components/crops/button-secondary-default.png). bg `rgba(0, 0, 0, 0)`, text `oklch(0.141 0.005 285.823)`, 16px/500, radius `0px`, height `24px`. Via home hero.
- hover: [button-secondary-hover.png](components/crops/button-secondary-hover.png). bg `rgba(0, 0, 0, 0)`, text `oklch(0.21 0.006 285.885)`, 16px/500, radius `0px`, height `24px`. Via pointer hover.

## button-signup

- default: [button-signup-default.png](components/crops/button-signup-default.png). bg `oklch(0.626 0.11 185.333)`, text `oklch(0.985 0 0)`, 14px/500, radius `6px`, height `36px`. Via header.
- hover: [button-signup-hover.png](components/crops/button-signup-hover.png). bg `oklab(0.626 -0.109524 -0.0102239 / 0.9)`, text `oklch(0.985 0 0)`, 14px/500, radius `6px`, height `36px`. Via pointer hover.

## button-login

- default: [button-login-default.png](components/crops/button-login-default.png). bg `oklch(1 0 0)`, text `oklch(0.141 0.005 285.823)`, 14px/500, radius `6px`, height `36px`. Via header.

## nav-link

- default: [nav-link-default.png](components/crops/nav-link-default.png). bg `oklch(1 0 0)`, text `oklch(0.141 0.005 285.823)`, 14px/500, radius `6px`, height `36px`. Via header.
- hover: [nav-link-hover.png](components/crops/nav-link-hover.png). bg `oklch(0.967 0.001 286.375)`, text `oklch(0.21 0.006 285.885)`, 14px/500, radius `6px`, height `36px`. Via pointer hover.

## heading

- default: [heading-default.png](components/crops/heading-default.png). bg `rgba(0, 0, 0, 0)`, text `oklch(0.141 0.005 285.823)`, 96px/500, radius `0px`, height `299.531px`. Via home h1.

## search-button

- default: [search-button-default.png](components/crops/search-button-default.png). bg `oklch(0.985 0 0)`, text `oklch(0.552 0.016 285.938)`, 14px/400, radius `6px`, height `36px`. Via header search.

## menu

- opened: [menu-opened.png](components/crops/menu-opened.png). bg `oklch(1 0 0)`, text `oklch(0.141 0.005 285.823)`, 16px/400, radius `6px`, height `616px`. Via products menu.

## text-field

- default: [text-field-default.png](components/crops/text-field-default.png). bg `rgba(0, 0, 0, 0)`, text `oklch(0.141 0.005 285.823)`, 16px/400, radius `6px`, height `36px`. Via search dialog.
- focus-visible: [text-field-focus-visible.png](components/crops/text-field-focus-visible.png). bg `rgba(0, 0, 0, 0)`, text `oklch(0.141 0.005 285.823)`, 16px/400, radius `6px`, height `36px`. Via focus search.
- filled: [text-field-filled.png](components/crops/text-field-filled.png). bg `rgba(0, 0, 0, 0)`, text `oklch(0.141 0.005 285.823)`, 16px/400, radius `6px`, height `36px`. Via typed loader, not submitted.

## badge

- default: [badge-default.png](components/crops/badge-default.png). bg `rgba(0, 0, 0, 0)`, text `rgb(32, 39, 44)`, 20px/400, radius `0px`, height `auto`. Via pricing plan name.

## price

- default: [price-default.png](components/crops/price-default.png). bg `rgba(0, 0, 0, 0)`, text `rgb(32, 39, 44)`, 36px/400, radius `0px`, height `46.7969px`. Via pricing.

## Gaps

- Checkbox, radio, switch, tabs, tooltip, toast, table, avatar, select: not present as product controls on the captured public pages. Pricing has a hire-status switch that is an account control, not a theme switch.
- Disabled, loading, error, pressed: not shown on the public pages. Pressed was not forced.
- Focus ring: keyboard Tab did not land on the hero CTA in the probe. The search button carries a 1px border-coloured outline. Focus ring token is not captured as a measured focus-visible ring.
- Dark theme: not present. `--color-*-inverse` tokens exist and paint inverse sections, not a second theme.
- Signed-in app components: behind login.lottiefiles.com. Not captured.
