# Components

Public marketing controls and the signed-out login form. Values are computed styles. The 21 November walk re-read the same button, page, and field colours. Crops are from the Playwright captures. The control map is [site-tree.md](site-tree.md).

## Button

Primary. `a.btn--primary`. Fill `#222222`, text `#f7f7f7`, 1px border of the same fill, radius 8px, padding 6px 16px, 14px Inter, height 35px.

[components/crops/button-primary-default.png](components/crops/button-primary-default.png)

Outline. `a.btn--outline`. White fill, text `#252525`, 1px border `#949494`, radius 8px, padding 8px 20px.

[components/crops/button-outline-default.png](components/crops/button-outline-default.png)

Nav Login. Fill `#313131`, text `#f7f7f7`, 1px border `#252525`, radius 8px, padding 6px 16px.

[components/crops/button-login-default.png](components/crops/button-login-default.png)

Nav Sign up. White fill, text `#252525`, 1px border `#949494`, radius 8px.

[components/crops/button-signup-default.png](components/crops/button-signup-default.png)

Login submit. Fill `#2e2e2e`, white text, radius 12px, padding 8px 16px, height 40px, weight 500. With empty fields the computed opacity is 0.5.

[components/crops/button-login-submit-disabled.png](components/crops/button-login-submit-disabled.png)

Hover is declared, not cropped. `.btn--outline.btn--outline--black--stroke:hover` and `.btn--primary.btn--pricing:hover` set `box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 5px 1px`.

## Link

Nav label. 16px Inter, `#252525`, letter-spacing -0.54px. Hover sets the colour to `--blue` (`#222`).

[components/crops/link-nav-default.png](components/crops/link-nav-default.png)

Text link. `.signupin-link`. 14px, colour `oklch(0.556 0 0)` (`#737373`), underlined.

[components/crops/link-text-default.png](components/crops/link-text-default.png)

Footer link. 14px, `#949494`, transition `color 0.2s`.

## Text field

Email and password on the login form. Fill `#f1f1f1`, radius 12px, padding 4px 12px, height 44px, 14px Inter. Focus sets the border colour to `oklch(0.708 0 0)`.

[components/crops/field-email-default.png](components/crops/field-email-default.png)

## Select

Occupation on the signup form, which was not submitted. Fill `#f1f1f1`, radius 12px, height 44px, padding 0 12px. The menu was not opened.

## Checkbox

`input.signupin-checkbox`. 16px square, radius 4px, 1px border `#a4a4a4`, white fill. The checked state was not clicked.

## Badge

BETA pill. Fill `#fbd302`, black text, radius 999px, padding 4px 8px, 9px Inter weight 700.

[components/crops/badge-beta-default.png](components/crops/badge-beta-default.png)

Offer pill. Same yellow, black text, radius 999px, padding 6px 12px, 12px Inter weight 500.

[components/crops/badge-offer-default.png](components/crops/badge-offer-default.png)

## Card

Pricing plan. 1px border `#d0d0d0`, radius 20px, padding 24px. The price is 36px Inter weight 600.

[components/crops/card-plan-default.png](components/crops/card-plan-default.png)

Login card. `.signupin-card` is white, padding 24px, width 420px, radius 0.

## Logo

The nav wordmark is an image at `/web-assets/media/vectary-logo-full.svg`. The crop is the rendered image, not a redraw.

[components/crops/logo-nav-default.png](components/crops/logo-nav-default.png)

## Gaps

- Icon button, text area, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table, and avatar were not on the pages that were measured.
- Hover, pressed, and loading crops were not taken. Hover shadow is a declared rule.
- The checkbox was not checked. The select was not opened.
- The hero 3D player failed in headless Playwright and showed "Player error". That frame is in the home, Canvas, and Studio screenshots. It is not a Vectary empty state.
- The phone menu was opened. Hover and pressed crops were still not taken.
- Signed-in editor controls were not reached. `/dashboard/` redirected to the login wall.
