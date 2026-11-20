# Variant patterns

Signed-out only. Layout numbers are from `getComputedStyle` and `getBoundingClientRect` on 2026-11-19. There is no screenshot to check them against.

## Homepage

At 1440×900 the page is two columns on `rgb(7, 7, 6)`.

| Region | Box |
|---|---|
| Left column | x 0, width 408, full viewport height |
| Right column | x 408, width 1032, overflow hidden |
| Headline | x 24, y 87, 360×72 |
| Composer bar | pinned to the bottom of the left column, height 84, padding `0 12px 12px` |
| Composer field | 384×72 inside that bar |

The right column is a squishy grid of widget cards. Cards are transparent 8px-radius frames around iframes. At 390×844 the left column still exists and the right column is not beside it. The grid container measured 366px wide, so the feed reflows under the fold rather than sitting in a second column. The composer stays at the bottom of the left column.

The only navigation out of `/` is the two chips. There is no header, no footer, and no link list.

## Authentication

`/authentication` replaces the homepage. The page background is `rgb(0, 0, 0)`, darker than the homepage body. A home mark sits at x 12, y 12, 28×28, radius 6px. The form is a 520px column (controls 400px) with 64px vertical and 48px horizontal padding on the left region, which at 1169px wide spanned the viewport.

Order: title, Google button, the word "or", email field, email button, fine print. The email button stays disabled until the field has text. Empty and filled share the same fill. Only the label opacity and the hover fill change.

## Legal

`/terms-and-privacy` is a 920px article on the same body colour as the homepage (`rgb(34, 34, 34)`). Two text buttons switch Terms of Service and Privacy Policy. The active tab is brighter text. There is no underline. Headings and body share 13px. The title matches the auth title: Inter 21/32 weight 500 at 50% white.

## What was not entered

Google sign-in, email submit, the composer Submit, Add image, and Select style. Those leave the signed-out measurement. Billing and the signed-in shell were not opened.
