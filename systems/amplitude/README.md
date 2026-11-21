# Amplitude

Amplitude is a product analytics platform. This package covers the public marketing site at https://amplitude.com/ and the empty login and signup walls at https://app.amplitude.com/login and https://app.amplitude.com/signup, photographed on 2026-11-22. No account was created. No email was typed. Themes seen: light marketing, light login wall. Widths photographed: 1440 and 390 CSS px.

A 2026-11-22 pass mapped the public website into [site-tree.md](site-tree.md) and photographed the marketing pages the header and footer open, plus the empty login and signup walls. Google, Slack, and GitHub were not clicked. `login-extracted` stays not-started. catalog.json was left alone.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the 48 px marketing favicon |
| [DESIGN.md](DESIGN.md) | Colour, type, and control sizes from the readings |
| [tokens.json](tokens.json) | Measured colours, type, radii, and control sizes |
| [style-guide.html](style-guide.html) | Marketing and login swatches |
| [components.md](components.md) | Controls seen on the public pages and the login wall |
| [patterns.md](patterns.md) | Marketing shell, pricing, login and signup stop |
| [site-tree.md](site-tree.md) | Which header and footer controls open which public page or wall |
| [login-review.json](login-review.json) | Empty login and signup walls. `login-extracted` is not-started |
| [raw/](raw/) | Computed-style readings and the shoot log |
| [screenshots/](screenshots/) | Marketing pages and the empty walls. Git LFS |
| [tools/](tools/) | Site-tree check |

## Brief

<!-- brief:start -->

Not generated. catalog.json was left alone, so `make brief` was not run for this package.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This pass maps the public site and does not register the package.

<!-- health:end -->

## How the values were read

Headless Chromium opened https://amplitude.com/ at 1440×900 and read `getComputedStyle` on the hero, the header pills, and the body. The same browser opened https://app.amplitude.com/login and read the empty email field and the disabled Continue button. Nothing was typed. The cookie banner was hidden after the page loaded. It was not accepted through a consent POST.

## What to distrust

The homepage hero demo is a marketing illustration. It is not a signed-in Amplitude workspace. The favicon is 48 px, scaled to 128 px, so [icon.png](icon.png) is soft. Header menus were read from the DOM. Their open state was not a separate screenshot. Help Center, Academy, and Investor Relations blocked the signed-out browser and were not photographed.

## Fonts

Gellix is the marketing display and nav face. IBM Plex Sans is the marketing body. Inter is the login wall. None of those files are in this package.

## Coverage

Marketing pages the header and footer open are listed in [site-tree.md](site-tree.md). Login and signup are the empty wall. The product app, checkout, and subscribe were not entered.

## Do and don't

- **Spend the black pill on the one primary action.** Get started is black with a white label. Contact sales is an outline.
- **Set the marketing hero in Gellix at 72px, weight 600.** The homepage h1 was that size on 72px line-height.
- **Keep the login field empty.** The wall asks for a work email and leaves Continue disabled until one is present. This package stops there.
- **Do not treat the hero demo as the app.** The sessions panel under the fold is a public illustration.

## Rebuild

```bash
python3 -m pytest systems/amplitude/tools/test_site_tree.py
```

There is no `build_tokens.py`. [tokens.json](tokens.json) was written from [raw/readings.json](raw/readings.json). catalog.json was left alone, so `make design-md` was not run.
