# Components

Public signed-out surfaces of Stable Audio, measured on 19 November 2026 from computed styles in the T3 preview browser. The browser did not produce screenshot frames, so this inventory has no crops. A value with no crop is still a measured value when the capture column names the element.

## Button

| State | Fill | Text | Border | Radius | Size | Where |
|---|---|---|---|---|---|---|
| Primary, home | #BC6C25 | #000000, 600 | 1px solid #BC6C25 | 0 | 13px / 36px nav, 15px / 44px hero | Start free, Make my mix |
| Primary, pricing and plugin | #ABA185 | #000000, 600 | 1px solid #ABA185 | 0 | 15px / 44px, padding 0 20px | Get Session, Download for Mac, 404 Go home |
| Secondary | transparent | #E8E8E8, 500 | 1px solid rgba(255,255,255,0.22) | 0 | 13px / 36px or 15px / 44px | Sign in, Roll the dice |
| Ghost | transparent | #E8E8E8, 500 | 1px solid transparent | 0 | 15px / 44px, padding 0 20px | Download, Save |
| Outline | transparent | #FFFFFF, 500 | 1px solid #FFFFFF | 0 | 13px / 32px, padding 0 14px | Contact us |
| Focus-visible | unchanged | unchanged | unchanged | 0 | outline 2px solid #FFB703 | Start free and a nav link after focus() |
| Hover, declared | not a fill change | var(--sx-primary-hover-ink, var(--sx-p-100)) | declared on .sx-btn-primary:hover | 0 | stylesheet rule, not a hovered element | .sx-btn-primary:hover |
| Disabled, declared | unchanged | var(--sx-ink-500) | stylesheet | 0 | opacity 0.5, cursor not-allowed | .sx-btn:disabled. No disabled control was on the pages |

## Icon button

Help and the phone menu button are 36 by 36, transparent, 1px solid rgba(255,255,255,0.22), radius 0. The menu icon is an inline SVG, viewBox 0 0 12 12, painted at 16px. The API link icon is 11px. The help icon is 14px.

## Link

Nav links are 13px, weight 500, colour #CFCDC6, padding 0 10px, height 32, radius 0. Ecosystem links are 14px, weight 500, colour #D27929. The word "here" in body copy is 12.5px, colour #8E8E8E. Terms links inside the legal page are white and underlined.

## Text field

The footer newsletter field is 30px tall, padding 0 10px, radius 0, fill #0B0B0B, border 1px solid color(srgb 1 1 1 / 0.16), text 13px white, placeholder "Email address". It was not filled and Subscribe was not pressed.

The AuthKit email field is 38px tall, 342px wide, radius 3.5px, transparent fill, colour #EEEEEE, placeholder "Your email address". Focusing it produced no extra outline on the input itself. Nothing was typed.

## Text area, select, checkbox, radio, switch

Not present on the captured public pages.

## Tabs

Not present. Pricing has no monthly or yearly switch.

## Menu

At 390 the hamburger opens a drawer. The drawer computed display block, fill #0B0B0B, width 390, height 333, padding 8px 16px 20px. Links are 16px, weight 400, white, row height 48. Sign in and Start free sit in a grid under the links. A second header in the DOM (the signed-in shell, height 0) was not the painted bar.

## Tooltip

Not present.

## Dialog

No product dialog was opened. OneTrust cookie UI was dismissed with Reject All before measuring. AuthKit is a full page, not a dialog: a 440px card, padding 48px, radius 4px, inset shadow rgba(255,255,255,0.16).

## Toast

Not present.

## Card

Pricing cards are fill #0B0B0B, padding 24px, radius 4px, border 1px solid rgba(255,255,255,0.1). The Session card uses rgba(255,255,255,0.22). The enterprise card uses padding 40px. Home teaser cards match the pricing fill and use padding 28px.

## List row

FAQ summaries are 17px, weight 600, white, padding 16px 0, row height 64. The open chevron is #FFB703. The open answer is 16px, line-height 24px, colour #CFCDC6.

## Table

Not present.

## Avatar

Not present. Signed out, so no account avatar.

## Badge

RECOMMENDED is a chip: font SX Plex Mono 10px, weight 500, letter-spacing 0.2px, colour and border #ABA185, padding 0 6px, height 18, radius 0.

## Gaps

- No crops. The preview browser returned "The browser is not producing screenshot frames."
- Hover, pressed and loading were not computed on a live element. Hover is a stylesheet rule only.
- Disabled, error, empty and loading states were not on the public pages.
- Checkbox, radio, switch, select, textarea, tabs, tooltip, toast, table and avatar were not on the public pages.
- The signed-in studio, sampler, Sessions and the plugin download were not entered.
- AuthKit error and verification states were not opened. The email form was not submitted.
- Google continue was not followed.
