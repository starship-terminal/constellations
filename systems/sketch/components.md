# Components

Public marketing pages and the signed-out account shell, measured on 19 November 2026. Crops are 2x.

## Button

Primary. `a.button-new.button-new--primary` on the home page.

![Primary button](components/crops/button-primary-default.png)

| State | Value |
|---|---|
| Default | Background `#151515`, text `#ffffff`, 16px/600, radius 24px, padding `11px 16px 12px 24px`, height 47px |
| Hover | Declared only. Shadow grows to `0 2px 8px` and the control translates -1px. Not captured as a crop. |
| Active | Declared `transform: scale(.97)` over 100ms. Not captured. |
| Disabled | Declared `opacity: .4`. Not on the marketing pages that were open. |
| Focus-visible | Declared `outline: 2px solid #000` with offset 2px. Not captured. |

Secondary (`.button-new--secondary`) is declared: transparent fill, 1.5px black border. It is on the pricing page ("Get in touch", "Contact for pricing"). A crop of that state was not saved. Tertiary is a white fill with a 1px `rgba(0,0,0,0.1)` border.

The account shell uses a different button: 40px tall, radius 6px, Inter 14px/600. The Sign In submit was disabled, so only the disabled fill `rgba(87, 95, 255, 0.3)` was measured.

## Link

Sign In in the marketing nav. Weight 600, colour `#000` on the refreshed nav, no underline.

![Sign in link](components/crops/link-default.png)

The account shell's "Create an account" link is `#575fff`, 12px, weight 600, underlined.

## Text field

Home newsletter field: background `#f9f9f9`, radius 16px, padding `12px 14px`, height 48px, ring `#e6e6e6`.

Sign-in email field: height 40px, radius 6px, padding 10px, 2px transparent border. Password field fill is `rgba(255,255,255,0.16)`.

Focus on the refreshed marketing field is a `#555dff` 2px ring (stylesheet). Focus on the sign-in email field at rest was the browser outline `rgb(229, 151, 0)`, not a designed ring. Invalid is `#cc0000`. Success is `#13bf3e`.

## Search

Help Center search, public. The field itself was not given a computed-style reading because the visible input was a custom control with a 0-size native input. The crop shows the pill, the placeholder, and the shortcut chip.

![Search](components/crops/search-default.png)

## Checkbox

Marketing newsletter checkbox: 16px, radius 3px, white fill, `1px solid rgba(0,0,0,0.1)`. Checked state was not opened.

The signup page has a marketing-consent checkbox. It was not toggled, and the form was not submitted.

## Card

Pricing plan card. Radius 28px, padding `36px 36px 52px`, fill `rgba(255,255,255,0.9)`, shadow `rgba(74, 21, 39, 0.2) 0 0 1px, rgba(74, 21, 39, 0.1) 0 12px 24px`.

![Plan cards](components/crops/card-plan-default.png)

Home promo card:

![Promo card](components/crops/card-promo-default.png)

Help Center category cards:

![Help cards](components/crops/card-help-default.png)

## Billing toggle

Yearly / Monthly on the pricing page. The selected pill is `#212123`, radius 16px, 31px tall. The selected label is `#ffffff` at 13px/500.

## Logo

Diamond mark from `.main-nav__logo__shape`. The SVG is in [icons/logo.svg](icons/logo.svg).

![Logo](components/crops/logo-default.png)

## Gaps

| Component | Status |
|---|---|
| Text area | Not present on the pages that were open. |
| Select | Declared as `.form-select`. Not rendered on the captured pages. The pricing currency control was not measured. |
| Radio | Not present. |
| Switch | Not present on the captured pages. A layout toggle exists in an "extra surprises" stylesheet block and was not on screen. |
| Tabs | The billing toggle is the only segmented control that was measured. |
| Menu | Nav submenus are declared. They were not opened. |
| Tooltip | Declared. Not opened. |
| Dialog | A "Thinking of switching tools?" popover sat over the pricing cards in the headless capture. It was not dismissed and its styles were not read. |
| Toast | `.snackbar` is declared. None was shown. |
| Table | Not present. |
| Avatar | Not present on signed-out pages. |
| Badge | `.pill` is declared (uppercase, radius 6px, refreshed radius 9999px). The "New" chip in the nav was not measured separately. |
| Icon button | The password reveal button on sign-in was present and not measured. |
| Hover, pressed, loading, error | Declared in CSS. Not captured as crops. |
