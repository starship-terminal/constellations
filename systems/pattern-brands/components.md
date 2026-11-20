# Components

Public signed-out pages on patternbrands.com, measured 2026-11-19. Values are token names. The numbers are the computed styles in [raw/readings.json](raw/readings.json).

There are no crops. The preview browser returned `The browser is not producing screenshot frames`.

## Button

Home Contact Us is an anchor with class `btn`. The fill is the child `.btn__bg`, not the anchor.

| Part | Value |
|---|---|
| Fill | `light.component.button.background` (#084935) |
| Label | `light.component.button.text` (#ffffff) |
| Radius | `light.component.button.radius` (24px on a 44px fill) |
| Padding | 12px 20px |
| Type | `core.typography.body` |
| Height | 44px |

A second circle, `.btn__circle`, is #1d9671 and 50% radius. It measured 0 by 0 at rest. The hover rule scales it to full size over 700ms. Hover was not held.

The 404 Go Home control is `.button.w-button`: same green, white label, padding 8px 24px, radius 1600px, height 37px, width 320px (it stretched to the utility column).

## Link

Product card links ("Visit Onsen") use `light.text.secondary` (#084935) at 16px, with an 18 by 8 arrow in `icons/arrow.svg`. Hover shifts the arrow 4px on the x axis. Hover was not held.

Footer links are Cadiz 14px, white on the green footer. Contact Us in the footer is `mailto:help@patternbrands.com`. No mail was sent.

Legal body links are the ink colour with an underline. Hover drops opacity to 0.5 over 300ms. Hover was not held.

## Text

| Role | Token | Where |
|---|---|---|
| Page title | `core.typography.page-title` | Legal h1, 48px / 52.8px |
| Home heading | `core.typography.home-heading` | h2.heading-style-h4, 28.8px / 31.68px |
| Section | `core.typography.section` | Legal h3, 24px |
| Subsection | `core.typography.subsection` | Legal h4, 20px |
| Body | `core.typography.body` | 16px / 20.8px, weight 400 |
| Footer | `core.typography.footer` | Cadiz 14px |
| Not found | `core.typography.not-found` | 404 h3, 32px |

Weight is 400 everywhere that was measured. The h6 class rule sets weight 700. No h6 was on the pages.

## Card

A brand card is a grid: image, wordmark, one sentence, a green link. Gap 16px. Card width 240px. List gap 8px. Image radius 0. No border, no shadow.

## Footer

Green band, Cadiz, white links, 24px vertical padding on the link row, 50px column gap. Logo is an inline SVG, 70 by 28 in the footer and 301 by 98 in the home lockup.

## Gaps

| Component | Status |
|---|---|
| Button hover and pressed | Not held. Hover rules are in the stylesheet. |
| Focus | Authored outline is 2px solid #4d65ff, offset 2px, on `[tabindex]:focus-visible`. Not held. Webflow input focus border is rgb(56, 152, 236). No input was on these pages. |
| Text field, text area, select, checkbox, radio, switch | Not present |
| Tabs, menu, tooltip, dialog, toast | Not present |
| Table, avatar, badge | Not present |
| Disabled, loading, error field | Token colours exist on `:root` (success, warning, error). None was painted. |
| Icon button | Not present |
| Dark theme | `color-scheme` was `normal`. No theme switch. |
