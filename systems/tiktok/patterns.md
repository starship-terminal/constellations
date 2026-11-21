# Patterns

Public signed-out surfaces. The map of controls is [site-tree.md](site-tree.md). Shots are from the 2026-11-21 Playwright pass.

## Signed-out Explore

https://www.tiktok.com/ redirected to https://www.tiktok.com/explore. English. `data-tux-color-scheme="light"`. Title "Explore - Find your favorite videos on TikTok". See [screenshots/explore-light-default.png](screenshots/explore-light-default.png).

At innerWidth 1440 the left rail is 240px. `--side-nav-width` computed to 15rem. Nav buttons are 208 by 40, starting at x 16. Log in is 200 by 40 at x 20, y 436, fill `#fe2c55`. Footer headings (Company, Program, Terms & Policies) sit under the button. Get Coins and Get App sit at the bottom of the rail. The grid continues to the right of the rail. Creator names and captions are feed content, not chrome tokens.

At innerWidth 390 the rail collapses to icons. Explore is a 40 by 40 button at x 16. The filled Log in label is not painted. A round red control sits in the rail. See [screenshots/explore-light-phone.png](screenshots/explore-light-phone.png).

## Login wall

Opened by clicking Log in. No field was filled. No provider was continued. See [screenshots/login-light-dialog.png](screenshots/login-light-dialog.png).

The dialog stays on https://www.tiktok.com/explore. The measured dialog box is 428 by 562. Channel rows are 300 by 48, radius 24px, fill black at 5%, type `#161823` weight 600. Sign up is 11px weight 600, `#fe2c55`.

The 2026-11-19 dark sheet (`#1e1e1e`, channels at white 13%) is in [raw/computed.json](raw/computed.json). This pass did not paint that sheet.

Upload and TikTok Studio redirect to https://www.tiktok.com/login. See [screenshots/login-light-page.png](screenshots/login-light-page.png). That page asks for QR, phone / email / username, and the same identity providers. The branch stopped there.

## What these pages do not show

No account shell, no upload form, no comments composer, no payment. QR, phone, email, and identity providers were not opened. Dark mode was visible in More and did not switch the scheme. See [login-review.json](login-review.json).
