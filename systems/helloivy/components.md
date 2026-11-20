# Hello Ivy components

Public surface only, read on 2026-11-21. Values are computed styles. A state that was not opened is Not captured. Crops were not cut. The screenshots are the evidence.

## Button

Header "Get Started" and "Try it for free" are black pills.

| Property | Value | Source |
|---|---|---|
| Height | 56px | `core.layout.header-cta-height` |
| Padding | 15px 30px | `core.space.15`, `core.space.30` |
| Radius | 9999px | `core.radius.pill` |
| Background | #000000 | `light.component.button.background` |
| Label | Inter 16px / 19.2px, weight 600, #ffffff | `core.typography.button` |

Pricing "Try for Free" anchors computed radius 0px and a cream label (`#faf6f0`) in Unbounded 16px weight 500. That is a second button shape, not a variant that was named in the product. See [pricing-light-full](screenshots/pricing-light-full.png).

Login "Continue" is Inter 17px weight 500, background `#222222`, white text, radius 10px, height 53.25px, width 500px at 1440. "Login with Google" is a 2px black outline, transparent fill, label `#707b8b`. It was not clicked.

Hover, focus-visible, pressed, disabled, and loading were not captured.

## Link

Header "Features" is Inter 16px weight 600, line-height 19.2px, colour `#000000`. It navigates. It does not open a dropdown. See [home-light-default](screenshots/home-light-default.png).

## Text field

Login email and password, measured empty.

| Property | Email | Password |
|---|---|---|
| Font | Inter 15px / 22.5px, weight 400 | same family |
| Text | #222222 | not separately tokenised |
| Background | #fcfcfc | same reading family |
| Border | 1px #777777 | 1px #c4c4c4 |
| Radius | 10px | 10px |
| Height | 48.5px | similar |
| Width | 500px at 1440 | 500px at 1440 |

Nothing was typed. No error state exists in this package. Docs search is visible on [docs-light-default](screenshots/docs-light-default.png) and was not measured.

## Menu

The header menu icon opens a full cream overlay. Desktop items "01" through "05" were read while open: Inter 24px, weight 500, line-height 33.6px, colour `#000000`. That reading is not a token. The overlay trial pill matches the header pill (56px, radius 9999px, black, white Inter 14px weight 600 label). Close is an X control. Phone overlay also shows social glyphs and a "Change theme" control that did not change `toggle-theme`.

See [home-light-menu](screenshots/home-light-menu.png) and [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Wordmark

An SVG named `Group_1794_1_`, about 124 by 60 at x 48, y 52 on the desktop home header. Computed font on the SVG is the browser default. Face: Not captured.

## Card

Feature and docs indexes are grids of linked cards. No separate card chrome was measured. See [features-light-default](screenshots/features-light-default.png) and [docs-light-default](screenshots/docs-light-default.png).

## Not present

Text area, select, checkbox, radio, switch, tabs, tooltip, toast, dialog, table, avatar, badge. No public page opened these.

## Gaps

- No component crops.
- No hover, focus, pressed, disabled, loading, or error state.
- Menu type size is recorded here and not in tokens.json.
- Pricing square CTA and header pill are both real. They are not one radius.
