# Klarna components

Public marketing components, read on 2026-11-18 from www.klarna.com/us/ while signed out. Specs use token names from [tokens.json](tokens.json). Computed geometry that has no token is labelled Measured and points at [raw/components-computed.json](raw/components-computed.json).

## Shared values

| Role | Token | Light value |
|---|---|---|
| Page | `light.page` | `#ffffff` |
| Surface | `light.surface` | `#f8f7fa` |
| Text | `light.text` | `#0b051d` |
| Muted | `light.muted` | `#504f5f` |
| Brand pink | `light.accent` | `#ffa8cd` |
| Border | `light.border` | `#e2e2e7` |
| Pill radius | `core.radiuses.radius.round` | `99999px` |
| Button type | Klarna Text | 16px / 500 |
| Nav type | Klarna Text | 14px / 500, line-height 16px |

Focus on Sign in and the hero buttons is a 2px solid outline in `light.text` (`#0b051d`). Keyboard focus never landed on the nav link or the icon button (`via: focus failed`), so their focus look was not captured; it was not measured as absent. Transitions on background, border, colour and opacity run 200ms `ease` (`core.motion.duration.200ms`). Under `prefers-reduced-motion: reduce` the probe recorded partial removal: some 200ms transitions stayed, some dropped. See [raw/motion.json](raw/motion.json).

## Nav link

A text link in the sticky header. Height 32px, padding 8px 12px, radius `core.radiuses.radius.round`, Klarna Text 14/500, colour `light.text`. Resting background is transparent.

| State | What changes | Crop |
|---|---|---|
| default | Transparent fill | [nav-link-default](components/crops/nav-link-default.png) |
| hover | Fill `#e5e3f5` (Measured, lavender wash) | [nav-link-hover](components/crops/nav-link-hover.png) |
| pressed | Overlay `rgba(0, 0, 0, 0.08)`, matches `--colors-overlay-press-default` | [nav-link-pressed](components/crops/nav-link-pressed.png) |
| focus-visible | Not captured: keyboard focus did not land (`focus failed`); the reading and crop show the link at rest | - |

## Sign in button

Header pill. Fill `light.color.btn.primary` (`#0b051d`), text inverse, height 42px, padding 11px 20px, radius `core.radiuses.radius.round`, Klarna Text 16/500, leading person icon.

| State | What changes | Crop |
|---|---|---|
| default | Ink fill | [sign-in-button-default](components/crops/sign-in-button-default.png) |
| hover | Eggplant `rgb(44, 34, 66)` (Measured) | [sign-in-button-hover](components/crops/sign-in-button-hover.png) |
| pressed | Not captured: the forced `:active` landed on the nav link, so the reading equals default. Recapture needed | - |
| focus-visible | 2px solid `light.text` outline | [sign-in-button-focus-visible](components/crops/sign-in-button-focus-visible.png) |

## Brand button

The pink "Get the app" pill. Fill `light.accent` (`#ffa8cd`), text `light.text`, height 52px, padding 15px 20px, radius `core.radiuses.radius.round`, Klarna Text 16/500. Hover fill measured `rgb(245, 161, 197)`. Focus outline 2px solid `light.text`. Pressed was not captured: the forced `:active` landed on the nav link, so the reading equals default (recapture needed).

The painted pill sits in a horizontal scroller. The element crop named `primary-button-default.png` is the pink QR card, not this pill. Use [home-light-search](screenshots/home-light-search.png) and the computed JSON. [primary-button-hover](components/crops/primary-button-hover.png) is the hover fill sample from the first measure run.

## Ink button

Secondary hero action ("Learn more"). Fill `light.color.btn.primary`, text inverse, height 52px, same pill radius and type as the brand button. Hover measured `rgb(31, 25, 47)`. The default crop is a blank off-screen frame. Do not cite it. The focus crop exists from the measure run. Pressed was not captured: the forced `:active` landed on the nav link, so the reading equals default (recapture needed). Confirm crops against [raw/components-computed.json](raw/components-computed.json) before treating a file as the painted button.

## Icon button

Round header controls (search, language). About 28 to 56px, radius `core.radiuses.radius.round`. Crops: [icon-button-default](components/crops/icon-button-default.png), [hover](components/crops/icon-button-hover.png). Pressed was not captured: the forced `:active` landed on the nav link, so the reading equals default (recapture needed). Keyboard focus did not land (`focus failed`), so focus-visible was not captured either.

## Search field

The header search control is an unlabelled round button. Clicking it opens a white popover with an input whose placeholder is "Search for any product or brand", plus suggestion rows (Clothing, Nike, Shoes, Apple) and a scrim. The field itself is 14px Klarna Text on a transparent ground. Focus outline computed to 0. A query was not submitted.

Crops: [search-field-default](components/crops/search-field-default.png), [focused](components/crops/search-field-focused.png), [filled](components/crops/search-field-filled.png). The filled crop may still show the placeholder. The overlay is [home-light-search](screenshots/home-light-search.png).

## Menu item

Language and region rows inside the header dialog. Crops: [menu-item-default](components/crops/menu-item-default.png), [menu-item-hover](components/crops/menu-item-hover.png). Confirm was not submitted.

## Help tabs

Pill tabs on `/us/help/klarna-card/`. Selected "All" is an ink pill: fill `light.text`, white text, height 32px, radius `core.radiuses.radius.round`. Unselected tabs have a `light.border` stroke and ink text. Crops: [tab-selected](components/crops/tab-selected.png), [tab-default](components/crops/tab-default.png).

## FAQ row

Help topics list questions as links, about 824 x 72, with a trailing chevron. They are not `<details>` accordions. See [help-topic-light-default](screenshots/help-topic-light-default.png). A dedicated row crop was not written (the crop locator matched both a tab and a row).

## Card

Marketing cards on the home and shopping pages. The pink QR card uses `light.accent` as its ground, ink text, and a Close control. See [card-default](components/crops/card-default.png) and [home-light-search](screenshots/home-light-search.png). Elevation uses the declared shadow scale (`core.shadows.shadow.s`, `.m`, `.l`) where a card lifts. Many marketing cards are flat fills, not shadows.

## Hero title

Display heading. Klarna Title, 84px / 700, line-height 80px on the measured home h1, colour `light.text`. Token role: `core.typography.display-xl`. The larger declared step is `core.typography.display-3xl` (130px / 124px). Crop: [hero-title-default](components/crops/hero-title-default.png).

## Sign-in continue

The QR interstitial primary action on app.klarna.com ("Continue securely in the Klarna app" / "Continue on web?"). Measured at rest. Not followed. Crops: [signin-continue-default](components/crops/signin-continue-default.png), [signin-continue-hover](components/crops/signin-continue-hover.png). Page: [signin-boundary-light-default](screenshots/signin-boundary-light-default.png).

## Gaps

Not present on the public marketing surface: checkbox, radio, switch, textarea, select, table, toast, avatar, painted badge chip, accordion, disabled, loading, and error form states.

Declared but not painted here: dark theme, status fills (`--colors-bg-negative` `#ae1d1d`, warning `#fbc64d`, positive `#046234`) as a fill plus text plus border set.

Not captured because they sit behind sign-in, checkout, or a submit: the web sign-in form after "Continue on web?", payments, purchases, portfolio, savings, the signed-in account, checkout, and search results. Cookie preference center was not opened.
