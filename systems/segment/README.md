# Segment

Segment is Twilio's customer data platform. This package covers the public marketing site at https://segment.com/ and the empty login and signup walls at https://app.segment.com/login and https://app.segment.com/signup, photographed on 2026-11-22. No account was created. No email was typed. Themes seen: ink marketing hero, light login wall. Widths photographed: 1440 and 390 CSS px.

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

Headless Chromium opened https://segment.com/ at 1440×900. It redirected to https://www.twilio.com/en-us/segment. The same browser read `getComputedStyle` on the hero, the header labels, and the header pills. It opened https://app.segment.com/login and read the empty email field and the Next button. Nothing was typed. Cookie banners were left in place. They were not accepted through a consent POST.

## What to distrust

The homepage puzzle graphic is a marketing illustration. It is not a signed-in Segment workspace. The icon is the 180 px apple-touch image, scaled to 128 px. The Support menu was read from the header. Its open state was not a separate screenshot. Investor relations returned 403. Impressum printed a street address and a phone number and was discarded. Careers printed a location and was discarded. Signup hops to a Twilio login URL that carries a state parameter. That URL was not stored. The screenshot is the empty form.

## Fonts

Whitney SSm is the marketing display, section, and nav face. SF UI Text is the login wall. None of those files are in this package.

## Coverage

Marketing pages the header and footer open are listed in [site-tree.md](site-tree.md). Login and signup are the empty wall. The product app, checkout, and subscribe were not entered.

## Do and don't

- **Spend the blue pill on the one primary action.** Start for free is #1866ee with a white label. Contact sales is a quiet blue outline.
- **Set the marketing hero in Whitney SSm at 48px, weight 700.** The homepage h1 was that size on 60px line-height, white on #000d25.
- **Keep the login field empty.** The wall asks for an email and leaves Next unclicked. This package stops there.
- **Use #3366ff only on the login wall.** Next is that blue. The marketing primary action is #1866ee.
- **Do not treat the puzzle graphic as the app.** The panel beside the hero is a public illustration.

## Rebuild

```bash
python3 -m pytest systems/segment/tools/test_site_tree.py
```

There is no `build_tokens.py`. [tokens.json](tokens.json) was written from [raw/readings.json](raw/readings.json). catalog.json was left alone, so `make design-md` was not run.
