# beehiiv

beehiiv is a newsletter, podcast, and community platform. This package covers the public marketing site at https://www.beehiiv.com/ and the signed-out login at https://app.beehiiv.com/login, measured on 2026-11-22. No account was created. Themes seen: dark marketing, light login. Widths photographed: 1440 and 390 CSS px.

A 2026-11-22 pass mapped the public website into [site-tree.md](site-tree.md) and photographed the marketing pages plus the empty login wall. Signup stopped on a press-and-hold captcha. Google was not clicked. The email field was not typed. `login-extracted` stays not-started. catalog.json was left alone.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the marketing favicon |
| [DESIGN.md](DESIGN.md) | Colour, type, and control sizes from the readings |
| [tokens.json](tokens.json) | Measured colours, type, radii, and control sizes |
| [style-guide.html](style-guide.html) | Dark marketing and light login swatches |
| [components.md](components.md) | Controls seen on the public pages and the login wall |
| [patterns.md](patterns.md) | Marketing shell, pricing, login, signup stop, help center |
| [site-tree.md](site-tree.md) | Which header and footer controls open which public page or wall |
| [login-review.json](login-review.json) | Empty login wall. `login-extracted` is not-started |
| [raw/](raw/) | Computed-style readings |
| [screenshots/](screenshots/) | Marketing pages, the empty login wall, and the signup captcha stop |
| [tools/](tools/) | Kit helpers and the site-tree check |

## Brief

<!-- brief:start -->

Not generated. catalog.json was left alone, so `make brief` was not run for this package.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This pass maps the public site and does not register the package.

<!-- health:end -->

## How the values were read

The T3 preview browser opened https://www.beehiiv.com/ in an incognito tab and read `getComputedStyle` at 1440 CSS px. Custom properties were read from the marketing stylesheets. The same tab opened https://app.beehiiv.com/login and read the empty email field and the disabled Sign in button. Pricing colours were read on https://www.beehiiv.com/pricing. Headless Chromium photographed the public pages at 1440 by 900 and the homepage and pricing at 390 by 844.

## What to distrust

Hover and pressed fills are declared custom properties. They were not held on a live control. The homepage body computed background is transparent. The token uses the nav and footer fill, #060419, which matches `--surface-page`. The login heading computed as #000000 while the app token `--color-text-primary` is #171717. Both are recorded. The demo form prefilled a name and an email. That screenshot was deleted and the form was not submitted. Creator Spotlight, social profiles, and the sitemap's child pages were not opened.

## Fonts

Marketing body is SatoshiFont. Display headings are ClashGroteskFont. The login field uses ui-sans-serif. Satoshi and Clash Grotesk are licensed to the product. The tokens name them. The style guide falls back to Helvetica.

## Coverage

| Item | Status |
|---|---|
| Colour roles, dark | Captured in [tokens.json](tokens.json) from the marketing site |
| Colour roles, light | Captured from the login page tokens and the empty email field |
| Type roles | Captured. Clash Grotesk display, Satoshi body, system face on login |
| Spacing | Captured from computed padding and control heights |
| Radii | Captured. 6px on controls. 12px is declared `--radius-xl`, not computed on a captured control |
| Borders | Captured. Nav demo 1px white at 20%, plan outline #3843d0, field #e5e7eb |
| Elevation | Not captured. Nav shadow is none. Login card shadow was none on the measured parent |
| Motion | Not captured. No duration was read |
| Sizing | Captured. Nav 36px, plan buttons 46px, login field 38px |
| Layout | Captured as screenshots at 1440 and 390 |
| Button | Captured, default and disabled. Hover and pressed declared only |
| Icon button | Phone menu present. Not measured |
| Link | Captured |
| Text field | Captured, empty, on the login wall |
| Text area, select, checkbox, radio, switch | Not present on the photographed pages |
| Tabs | Not present. The yearly and monthly control is a toggle |
| Menu | Product, Solutions, and Resources open as pages. The open menu was not screenshotted |
| Tooltip, toast, dialog, table, avatar | Not present on these pages |
| Card | Captured, pricing plan cards |
| Badge | Captured, Most Popular on the Pro card |
| App shell | Marketing shell captured. Signed-in shell not captured |
| Form validation | Not captured. No form was submitted |
| Empty login | Captured |
| Signup | Stopped at a press-and-hold captcha |
| Desktop 1440 and phone 390 | Homepage and pricing at both widths. Other pages at 1440 |

## Do and don't

**Pink is the accent, and blue is the action.** "ONE PLATFORM." and the subscriber count use #ff5ec4. Try for free and Sign up with Google use #2f39ba. Do not paint the main button pink.

**The nav signup is a white pill.** Sign up for free in the bar is #ffffff with #060419 text. The page-body signup buttons are blue or outlined blue.

**The login Sign in button stays grey until an email is present.** The empty state is #d1d5db with #6b7280 text. Do not draw it as the marketing primary.

**The marketing page is navy, not black.** The bar and footer are #060419. The hero illustration sits on that same ground.

## Rebuild

Readings are in [raw/readings.json](raw/readings.json). [tokens.json](tokens.json) was written from those readings. There is no builder to regenerate them. catalog.json was left alone, so `make brief` and `make grade` were not run.
