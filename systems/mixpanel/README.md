# Mixpanel

Mixpanel is a product analytics platform. This package covers the public marketing site at https://mixpanel.com/ and the empty login and signup walls at https://mixpanel.com/login/ and https://mixpanel.com/register/, photographed on 2026-11-22. No account was created. No email was typed. Themes seen: light marketing, light login wall. Widths photographed: 1440 and 390 CSS px.

A 2026-11-22 pass mapped the public website into [site-tree.md](site-tree.md) and photographed the marketing pages the header and footer open, plus the empty login and signup walls. Google was not clicked. `login-extracted` stays not-started. catalog.json was left alone.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the 180 px apple-touch icon |
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

Headless Chromium opened https://mixpanel.com/home/ at 1440×900 and read `getComputedStyle` on the hero, the header labels, and the header pills. The same browser opened https://mixpanel.com/login/ and read the empty email field and the Continue button. Nothing was typed. Cookie banners were left in place. They were not accepted through a consent POST.

## What to distrust

The homepage hero demo is a marketing illustration. It is not a signed-in Mixpanel workspace. The icon is the 180 px apple-touch image, scaled to 128 px. Header menus were opened to read their links. Their open state was not a separate screenshot. Integrations and Partner Directory returned 403. Community showed member names and was discarded. Events listed venue names and was discarded. The 390 homepage paints a different hero from the 1440 page.

## Fonts

Garnett Medium is the marketing display and nav face. Garnett Regular is the marketing body. Garnett is the login wall. None of those files are in this package.

## Coverage

Marketing pages the header and footer open are listed in [site-tree.md](site-tree.md). Login and signup are the empty wall. The product app, checkout, and subscribe were not entered.

## Do and don't

- **Spend the black pill on the one primary action.** Get Started Free is black with a white label. Contact Sales is a quiet grey pill.
- **Set the marketing hero in Garnett Medium at 48px, weight 400.** The homepage h1 was that size on 57.6px line-height.
- **Keep the login field empty.** The wall asks for an email and leaves Continue unclicked. This package stops there.
- **Use purple only on the login wall.** Continue is #7856ff. The marketing primary action is black.
- **Do not treat the hero demo as the app.** The panel under the fold is a public illustration.

## Rebuild

```bash
python3 -m pytest systems/mixpanel/tools/test_site_tree.py
```

There is no `build_tokens.py`. [tokens.json](tokens.json) was written from [raw/readings.json](raw/readings.json). catalog.json was left alone, so `make design-md` was not run.
