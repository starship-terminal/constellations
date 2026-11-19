# Components

Public marketing components measured on tesla.com on 19 November 2026. Values are computed styles. Token names point at [tokens.json](tokens.json). Crops were not taken: the preview browser returned no screenshot frames, and headless Playwright received HTTP 403.

## Button

The marketing call to action is `a.tcl-button.tds-btn`.

| State | What was measured |
|---|---|
| Primary, default | Order Now. Background `light.color.color-primary` (#3e6ae1), text #ffffff, height 40px, radius `core.radius.border-radius` (4px), weight 500, 14px. Border is 3px transparent. |
| High contrast, on a photo | Learn More. Background #ffffff, text #393c41, same height and radius. |
| High contrast, on a light band | Schedule Demo. Background #171a20, text #eeeeee. |
| Tertiary | Schedule a Drive Today. Background #f4f4f4, 1px border #d0d1d2, padding 4px 24px, height 40px. |
| Hover, pressed, disabled, loading | Not captured. No state was forced. The live page did not show a disabled or loading button. |

## Link

The promo line "2.49% APR Available" is `a.tds-link` in Universal Sans Display, 20px / 28px, white, with a 2px underline drawn as a box-shadow. Footer links are 12px / 20px, weight 500, colour #5c5e62.

Hover and focus-visible were not captured.

## Icon button

`button.tds-icon-btn--medium` is 32 by 32, radius 4px, padding 4px. The locale close control is 40 by 40.

## Text field

`/support` has one search field. The input itself is unstyled. The wrap `.tds-form-input--default` is 40px tall, background #f4f4f4, radius 4px, padding 0 12px. Placeholder "Search Support" is 14px, weight 500, colour #5c5e62. Focus left the outline at `none`.

Text area, select, checkbox, radio, switch: not present on the pages that were opened.

## Tabs

Homepage carousel dots use `[role=tab].tds-tab`, 12 by 12, radius 8px. They are dots, not text tabs.

## Menu

The header Menu button opens `dialog.tds-site-header-panel`. The panel is white and full window. Rows (Vehicles, Energy, Charging, Robotaxi, Semi, Discover, Shop, Support) are 56px tall, 17px, weight 500, colour #171a20, padding 16px 6px 16px 12px.

## Dialog and banner

The location confirm card and the cookie banner share one chrome: background `rgba(244, 244, 244, 0.85)`, radius 8px, padding 24px, backdrop blur 4px. The location card shadow is `0 8px 16px rgba(0,0,0,0.16)`. The cookie banner shadow is `0 8px 8px rgba(0,0,0,0.16)`. Heading 17px / 500 / #171a20. Body 12px / #5c5e62.

Accept and Reject are tertiary buttons. The banner was dismissed with Reject. No account was created.

## Card

Support's "Get Personalized Support" heading is 24px display, weight 500, #171a20. The product card chrome in TDS is `--tds-card--border-radius` 4px and `--tds-card--padding` 24px.

## Header and footer

The header is 56px (`core.size.site-header-height`). Over a hero its background is transparent. The footer is 12px, padding `0 24px 60px`, link colour #5c5e62.

## Gaps

| Component | Status |
|---|---|
| Button hover, focus-visible, pressed, disabled, loading | Not captured. States were not forced. |
| Text area, select, checkbox, radio, switch | Not present on the public pages opened. |
| Toast | The toast tokens exist (`--tds-toast--background` #222222). No toast was shown. |
| Table, avatar, badge, tooltip | Not present on the public pages opened. |
| Form validation error | Not captured. No form was submitted. |
| Destructive confirmation | Not present. |
| Dark theme, live | The marketing site has no theme toggle. Dark values are the `.tds-colorscheme--dark` probe. |
| Screenshots and crops | Not captured. Preview frames failed. Headless Playwright was denied. |
