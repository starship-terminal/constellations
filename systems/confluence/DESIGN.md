# Confluence design notes

Public marketing site and empty account walls, 2026-11-22. Values are computed styles, except the wordmark blue, which was sampled from the homepage screenshot before quantising. catalog.json was left alone, so `make design-md` was not run.

## Colour

| Role | Value | Where |
|---|---|---|
| Page | #ffffff | Homepage and footer |
| Text | #292a2e | Body |
| Heading | #101214 | h1 |
| Primary | #1868db | Get it free, Sign up, Continue, wordmark mark |
| On primary | #ffffff | Those labels |
| Banner | #e9f2fe | Gartner announcement |
| Hero field | #f8f8f8 | Work-email wrapper |
| Login canvas | #fafbfc | Login screenshot sample |

No dark theme on the public pages.

## Type

| Role | Face | Size | Weight |
|---|---|---|---|
| Display | Charlie Display | 64px | 500 |
| Body | Charlie Text | 16px | 400 |
| Header button | Charlie Text | 16px | 500 |
| Login field and Continue | Atlassian Sans | 14px | 400 and 500 |
| Signup heading | Charlie Display | 32px | 700 |

Display letter-spacing on the homepage h1 was -1.28px. Line height was 66.56px.

## Controls

| Control | Height | Radius | Fill |
|---|---|---|---|
| Header Get it free | 40px | 10000px | #1868db |
| Hero Sign up | 48px | 10000px | #1868db |
| Hero email wrapper | 44px | 25px | #f8f8f8 |
| Login email field | 36px | 0px on the input | transparent input |
| Login Continue | 40px | 3px | #1868db |
| Signup Sign up | 45px | 6px | #1868db |

Header bar height is 68px. Sign in in the header is text, #101214, weight 500, no fill.
