# Capy public tokens

Hand-written from tokens.json on 2026-11-22. `make design-md` was not run, so catalog.json was not rewritten. Take values from tokens.json.

## Color

| Role | Light | Dark |
|---|---|---|
| page | #ffffff | #121214 |
| text | #000000 | #efefef |
| header | #000000 | |
| accent | #7699fb | #4d6fe8 |
| link | #2a44af | |
| on accent | #ffffff | #ffffff |
| muted | #6d6d6d | |
| focus | #e59700 | |

The dark column is the sign-in wall under `prefers-color-scheme: dark`. The marketing site did not paint a dark theme.

## Typography

| Role | Family | Size | Weight |
|---|---|---|---|
| Homepage hero | bebasNeue Inline | 64px | 400 |
| Pricing title and price | bebasNeue Inline | 56px | 400 |
| Hero paragraph | abcSocialMono | 18px | 400 |
| Buttons and nav chrome | abcSocialMono | 16px | 400 |
| Product menu item | DM Mono | 18px | 400 |
| Sign-in heading | Inter | 22px | 500 |
| Sign-in control | Inter | 13px | 500 |

## Radius

8px on marketing buttons. 6px on sign-in fields and Continue. The billing toggle is a pill.

## Size

Header 65px. Header Download 36px. Hero Download 35px. Start free 40px. Sign-in controls 32px.

## Shadow

Marketing buttons use a hard offset, no blur: `-2px 2px 0 #888` on the filled Download, `-2px 2px 0 #000` on Continue in web.
