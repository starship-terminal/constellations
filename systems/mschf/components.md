# Components

MSCHF's public site is one index. The pieces below are the ones that paint on https://mschf.com. Values are the computed styles at 1440x900 unless the row says 390. Crops are 2x.

## Link

The shop link in the header, and every drop title.

| State | What changes | Crop |
|---|---|---|
| default | colour `#84898e`, no underline, uppercase | [link-default.png](components/crops/link-default.png) |
| hover | colour `#ffffff`. A title that is not `.latest` also appends `↗` | [link-hover.png](components/crops/link-hover.png) |
| focus-visible | UA outline `rgb(0, 95, 204) auto 1px`, offset 1px. Colour stays `#84898e` | [link-focus.png](components/crops/link-focus.png) |
| active | no rule. Colour stays `#84898e` | not captured as a separate crop; forced `:active` matched default |

Below 500px the shop link is `display: none`. Drop titles stay.

## Icon button

The header mark. It is a `<button>` with no accessible name.

| State | What changes | Crop |
|---|---|---|
| default | 65px square, padding 10px 12px, background `#ffc700`, radius 0, red mark `#f00007` | [icon-button-default.png](components/crops/icon-button-default.png) |
| hover | background becomes transparent. The mark stays `#f00007` | [icon-button-hover.png](components/crops/icon-button-hover.png) |
| focus-visible | UA outline `#005fcc`. Background stays gold | [icon-button-focus.png](components/crops/icon-button-focus.png) |
| active | no rule | not captured as a separate crop |

At 390 the button is 62px, padding 10.4px 12.48px (declared `16vw` tall under `max-width: 500px`; the computed box was 62px at 390). A click does not open a menu, a search field, or a subscribe form.

## List row

One drop. A flex row, 56px tall at 1440, nowrap.

| Part | Value |
|---|---|
| index (`.left`) | 26px / 28px, width `4ch`, letter-spacing 0 |
| title (`.right`) | 65px / 56px, width `33ch`, overflow hidden |
| colour | `#84898e`. A `.links` row is gold `#ffc700`, blue `#40aaff`, or red `#f00007`, one row each. `.project-tbd` is declared red and was not in the DOM |
| hover | title colour `#ffffff` |

Crops: [list-row-default.png](components/crops/list-row-default.png), [list-row-hover.png](components/crops/list-row-hover.png).

A title wider than the column runs as a `steps()` marquee (`marquee-667400b0`, 50s on the one running row). The overlay on a linked tile is a 45-degree black hatch, `0.416666vw` tiles, and it hides on hover of `.has-link`.

## Text field, text area, select, checkbox, radio, switch

Not in the DOM. The stylesheet declares `input` (transparent, `3.88889vw` tall, `13.5417vw` wide, uppercase) and a Tailwind placeholder colour `rgb(156, 163, 175)`. The only textarea is a hidden `g-recaptcha-response`.

## Tabs, menu, tooltip, dialog, toast, card, table, avatar, badge

Not present on the public index.

## Gaps

- No form, so no error, disabled, or loading field.
- No pressed style beyond the forced `:active`, which matches rest.
- The logo button has no accessible name and its click does nothing visible.
- `section.subscription` (`#40aaff`) is declared and not mounted.
- store.mschf.com is a separate Shopify theme (white page, Courier, Nunito Sans, Assistant) and is not this system.
