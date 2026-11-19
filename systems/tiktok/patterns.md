# Patterns

Public signed-out surfaces only. No screenshots: the preview browser returned no frames. Layout numbers are from `getBoundingClientRect`.

## Signed-out home

https://www.tiktok.com/ stayed on that URL. English. `data-theme="dark"`. Title "TikTok - Make Your Day", then "Log in | TikTok" while the dialog was open.

At innerWidth 1169 the left rail is 240px of content (nav buttons are 208px wide, starting at x 16). The wordmark is 105 by 28 at x 24, y 20. Search is a 208 by 40 capsule at y 64. Nav rows are 40px tall at y 116, 160, 204, 248, 292, 336, and 380. Log in is 200 by 40 at x 20, y 436. Footer headings (Company, Program, Terms & Policies) start at y 516. Get Coins and Get App sit at y 687. The feed continues to the right of the rail. Creator names and captions are feed content, not chrome tokens.

`--side-nav-width` computed to 15rem at this width.

At innerWidth 390 the same rail collapses. `--side-nav-width` computed to 4.5rem. The wordmark link is 26 by 28. Search is 39 by 40. Each nav button is 40 by 40 and its label box has width 0. Log in is a 40 by 40 icon button, transparent, not the filled primary. The player measured 404 by 718, starting at x 80. visualViewport width was 382, scale 1.

## Login wall

Opened by clicking Log in. No field was filled. No provider was continued.

The sheet is `#1e1e1e`, radius 24px, no shadow. Desktop: 428 by 562. Phone: 390 by 562, flush to the left, y 125. The mask is black at 68%. The title is 33px TikTokDisplayFont bold. Seven channel rows are 300 by 48, radius 24px, fill white at 13%. A 0.5px divider at white 12% sits above the legal line. Sign up is 11px `#ff3b5c`.

The dialog names QR code and phone or email as the first two channels. Neither was opened. That is the signup wall.

## What these pages do not show

No account shell, no upload form, no settings, no comments composer, no payment, no light theme, no 1440 CSS-pixel width. A 1440 width was not requested; the fill viewport was 1169.
