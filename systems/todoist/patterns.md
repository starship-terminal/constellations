# Patterns

Public pages only. Desktop viewport 1440 by 900. Phone viewport 390 by 844. Screenshots are in [screenshots/](screenshots/). The control map is [site-tree.md](site-tree.md).

## Marketing home

https://www.todoist.com/

[screenshots/home-light-default.png](screenshots/home-light-default.png)

A 72px nav, padding 0 24px, transparent over the page. Links are quiet 39px pills. The page background is `light.background.page`. The visible heading is Graphik 55px weight 600. The lede is Inter 20.5px at 66% ink. One red xl button, "Start for free". The Resources menu is [screenshots/home-light-resources-menu.png](screenshots/home-light-resources-menu.png). Phone width is [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

A cookie dialog from Osano covered the corner on first load. "Reject Non-Essential" was clicked so the page underneath could be measured. Osano colours are not in the tokens.

## Pricing

https://www.todoist.com/pricing

Heading "Plans and pricing", same 55px Graphik. Three articles side by side: Beginner (US $0, quiet "Get started"), Pro (US $5 per month on the yearly view), Business (US $8). Cards are white, 10px radius, 1px quiet border, 24px 32px padding. No plan was started. No card was entered.

## Signed-out login

https://app.todoist.com/auth/login

[screenshots/login-light-empty.png](screenshots/login-light-empty.png)

The marketing host redirects here. Page background rgb(252, 250, 248). Column width 376px. Heading "Welcome back!" at 32px weight 700, system font. Three identity-provider rows (Google, Facebook, Apple), each 48px with a 1px #e5e5e5 border and 6px radius. Email and password fields, then a red "Log in" button at rgb(211, 51, 34). Links underneath are the same red at 13px.

Nothing was submitted. No identity provider was clicked. The branch stops here. See [login-review.json](login-review.json).

## Signup boundary

https://app.todoist.com/auth/signup?locale=en

Same chrome as login. Fields are email and password. Google, Facebook and Apple are offered. A Cloudflare Turnstile input is in the form. Signup was not submitted. No phone field was on the page.
