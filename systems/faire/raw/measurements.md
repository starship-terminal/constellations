# Faire measurements

Read on 2026-11-21 from https://www.faire.com/ in headed Chrome, signed out, viewport 1440 by 900. Cookie UI was hidden with CSS and was not accepted. Values are computed styles, not samples from screenshots.

## Page

| Role | Value | Where |
|---|---|---|
| Page wash | rgb(251, 248, 246) | Ancestor of the home h1, the painted page band |
| Header | rgb(255, 255, 255) | Header bar, 1440 by 108 |
| Footer band | rgb(255, 255, 255) | Parent of footer |
| Body text | rgb(0, 0, 0) | body |
| Body font | Graphik, system, -apple-system, system-ui, Helvetica Neue, Lucida Grande, sans-serif | body, 16px |
| Ink | rgb(51, 51, 51) | Sign in label, nav link, footer link |
| Near-black | rgb(22, 22, 22) | About us link, All categories, menu items |
| Hairline | rgb(218, 218, 218) | Field border, filter pill border, Google button border |
| Focus | rgb(39, 94, 197) solid 2px, offset 1px | Sign up to buy, keyboard focus |

theme-color meta: not present. color-scheme: normal. No dark theme switch on the public site.

## Type

| Role | Family | Size | Weight | Line height | Letter spacing |
|---|---|---|---|---|---|
| Display | Nantes_fix, serif | 52px | 400 | 64px | normal |
| Category title | Nantes_fix, serif | 38px | 400 | 50px | |
| UI | Graphik_fix, sans-serif | 14px | 400 | 20px | 0.15px |
| Body | Graphik | 16px | 400 | | |

## Controls

| Control | Fill | Text | Radius | Height | Padding |
|---|---|---|---|---|---|
| Sign up to buy, default | rgb(51, 51, 51) | rgb(255, 255, 255) | 4px | 40px | 0 16px |
| Sign up to buy, hover | rgb(0, 0, 0) | rgb(255, 255, 255) | 4px | 40px | |
| Sign up to buy, focus-visible | same fill, outline rgb(39, 94, 197) 2px offset 1px | | | | |
| Sign in | transparent | rgb(51, 51, 51) | 0 | 60px | 0 16px |
| All categories | transparent | rgb(22, 22, 22) | 32px | 40px | |
| Nav link | transparent | rgb(51, 51, 51) | 0 | 21px | |
| All filters pill | rgb(255, 255, 255) | rgb(0, 0, 0) | 999px | 40px | border 1px rgb(218, 218, 218) |
| Search field shell | rgb(255, 255, 255) | rgb(22, 22, 22) | 999px | 40px | width 631px, border 1px rgb(218, 218, 218), GT Standard 14px. Not submitted. |
| Sign-in dialog | rgb(255, 255, 255) | | 0 | 649px | width 420px, shadow none |
| Email field shell | rgb(255, 255, 255) | | 4px | 40px | border 1px rgb(218, 218, 218), width 340px |
| Sign in submit | rgb(51, 51, 51) | rgb(255, 255, 255) | 4px | 48px | width 340px |
| Sign in with Google | rgb(255, 255, 255) | rgb(51, 51, 51) | 4px | 48px | border 1px rgb(218, 218, 218). Not clicked. |
| Categories menu | rgb(255, 255, 255) | rgb(22, 22, 22) | 0 | 712px | full width 1440, shadow none |

Pressed, disabled, loading, and error states were not held. The sign-in form was not submitted, so validation error is not captured.

## Vendor colour variables

Toastify declares status colours in its stylesheet. They were not seen painted on a Faire toast during this capture. Recorded as vendor, not as Faire semantic tokens: info #3498db, success #07bc0c, warning #f1c40f, error hsl(6, 78%, 57%).
