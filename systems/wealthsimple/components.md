# Wealthsimple components

Public marketing site, measured 2026-11-21 at https://www.wealthsimple.com/en-ca. Signed out. One light scheme. Desktop 1440 and phone 390.

Crops are in [components/crops/](components/crops). Values are token names from [tokens.json](tokens.json). A state that was not reached is listed under Gaps.

## Button

Primary is a pill (`core.radius.pill`) with an ink fill (`light.accent.default`) and off-white label (`light.text.onAccent`) at 14px / 500 (`core.typography.label`). Height on the header is about 44px, padding 12px 16px.

| State | Crop | Notes |
|---|---|---|
| default | [button-primary-default.png](components/crops/button-primary-default.png) | Get started |
| hover | [button-primary-hover.png](components/crops/button-primary-hover.png) | Fill mixes the ink to about 80% (`--ws-color-hover-button-solid`) |
| focus-visible | [button-primary-focus-visible.png](components/crops/button-primary-focus-visible.png) | Focus landed. The element outline computed to none. The ring is a separate pseudo-element (`core.size.focusRing` 0.25rem) and was not a visible colour change in the crop |
| pressed | not captured | Space on the link did not hold a distinct pressed colour |
| disabled | not present | No disabled primary on the public header |
| loading | not present | |

Secondary is an outline pill: transparent fill, ink border and ink label. [button-secondary-default.png](components/crops/button-secondary-default.png), hover [button-secondary-hover.png](components/crops/button-secondary-hover.png).

## Icon button

Search is a circle with an ink keyline. [icon-button-search-default.png](components/crops/icon-button-search-default.png), hover [icon-button-search-hover.png](components/crops/icon-button-search-hover.png). Phone menu is the same circle with a two-line glyph. [icon-button-menu-default.png](components/crops/icon-button-menu-default.png).

## Link

Nav items are 14px / 500 ink text with a chevron when the item opens a menu. [nav-button-default.png](components/crops/nav-button-default.png), hover [nav-button-hover.png](components/crops/nav-button-hover.png). Footer links are 18px ink, not a separate accent hue (`light.text.link`).

## Text field

Search field is a pill, 2px slate-90 border (`light.border.default`), 18px The Future, placeholder "I'm looking for...". [search-field-default.png](components/crops/search-field-default.png), filled [search-field-filled.png](components/crops/search-field-filled.png). The query "TFSA" was typed. Suggested public results painted in [screenshots/home-light-search-typed.png](../screenshots/home-light-search-typed.png). The query was not submitted. Minimum input height token is 4rem (`core.size.inputMin`).

The Monthly Millionaire email field is the same pill on the midnight hero. It was not filled. The form was not submitted.

Contact and get-in-touch fields were not focused. The focus step timed out on scroll. No personal data was typed. Login fields on the wall were focused empty and not filled. [login-email-default.png](components/crops/login-email-default.png), [login-email-focused.png](components/crops/login-email-focused.png), [login-password-default.png](components/crops/login-password-default.png), [login-submit-default.png](components/crops/login-submit-default.png).

## Text area

Not captured as a distinct control. Contact may use a textarea; a dedicated error state was not produced because no form was submitted.

## Select, checkbox, radio, switch

Not present on the captured public marketing pages. Pricing uses links and headings, not a select. Segmented controls exist in the CSS (`--ws-min-input-height` on a grid of options) but were not shown on the pages walked.

## Tabs

Not present as a tab widget on the pages captured. Pricing plan names are a comparison layout, not a tablist that changed the page in the first probe.

## Menu

Header buttons open a floating panel (`core.elevation.floating`, `light.background.surface`) with two columns of product links. [menu-trade-default.png](components/crops/menu-trade-default.png). Phone uses a full-screen drawer opened by the button labelled Open navigation. [menu-mobile-default.png](components/crops/menu-mobile-default.png). Trade inside that drawer is a second list. [menu-mobile-trade.png](components/crops/menu-mobile-trade.png).

## Tooltip

Not present on the public pages walked.

## Dialog

Search opens a panel under the header, not a modal with a scrim. Chat ("Open chat") is a third-party widget (Decagon). It was not submitted. No destructive confirmation dialog exists on the public site.

## Toast

Not present. No action was submitted, so no success toast was shown.

## Card

Product sections are full-bleed bands, not a raised card grid. The floating menu panel is the closest card. See the menu crop.

## List row

Menu links are text rows without dividers. Footer columns are the same pattern.

## Table

Pricing comparison is a set of plan columns. A data table with row selection was not present.

## Avatar

Not present on the signed-out marketing site.

## Badge

Not captured as a separate component. Promo callout styles exist in CSS (`--ws-color-promo-callout-background`) and were not isolated as a crop.

## Header

[header-default.png](components/crops/header-default.png). Wordmark in Tiempos, nav in The Future 14/500, search circle, Log in outline pill, Get started ink pill. Height token `core.size.header` is 5.75rem including the floating bar.

## Banner

A dismissible promo sits above the header. [banner-default.png](components/crops/banner-default.png). Close banner hides it. The consent banner was hidden in CSS and never clicked.

## Gaps

- Pressed, disabled, and loading were not shown on public controls.
- Form error, toast, tooltip, select, checkbox, radio, switch, avatar, and table selection were not present, or sit behind the login wall.
- Focus ring colour was declared (`light.focus.ring`, width 0.25rem) but the captured Get started crop did not show a painted ring.
- Signed-in app components are behind https://my.wealthsimple.com/app/login. The branch stopped there.
