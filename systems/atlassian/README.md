# Atlassian

Public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). That pass photographed the signed-out marketing pages and the empty sign-in and signup walls. `catalog.json` was left alone. `login-extracted` stays not-started.

Atlassian (atlassian.com) publishes collaboration software for software, IT, and business teams. This package captures the public marketing site and the empty account walls. No account was created. No site was created. No trial was started.

Surfaces: home, products index, product and collection pages from the header, solutions and industry pages, why-Atlassian pages, resources pages, company pages, and both walls. Theme: light. Widths: 1440 and 390 CSS pixels. Captured 22 November 2026.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px PNG from https://www.atlassian.com/favicon.ico |
| [DESIGN.md](DESIGN.md) | Written by hand from declared tokens. catalog.json was left alone, so make design-md was not run |
| [tokens.json](tokens.json) | Declared colour, type, and spacing roles from the public stylesheets |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Controls that painted on the public pages |
| [patterns.md](patterns.md) | The captured pages |
| [screenshots/](screenshots/) | Marketing pages and the empty walls |
| [site-tree.md](site-tree.md) | Header, footer, and the public pages those controls open. Mapped 2026-11-22 |
| [login-review.json](login-review.json) | Empty sign-in and signup walls. `login-extracted` is not-started |
| [raw/](raw/) | Declared custom properties from the public stylesheets |
| [tools/](tools/) | Note on how the shots were made |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

www.atlassian.com links three public stylesheets: `atlaskit-tokens_light.css`, `atlaskit-tokens_spacing.css`, and `atlaskit-tokens_typography.css`. Named `--ds-*` roles were parsed into [raw/css-vars.json](raw/css-vars.json) and copied into [tokens.json](tokens.json). Screenshots were not sampled for colour.

Sign-in and signup were opened and not filled. Continue and Sign up were not clicked. No identity provider was clicked. No consent button was accepted. Reject all cookies was clicked so the banner would not cover the header.

Screenshots were taken with headless Chromium at 1440 by 900 and 390 by 844, device pixel ratio 2, then quantised to 256 colours. Sidecars record the measured viewport.

## What to distrust

- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- The home board is a public demo. It is not a signed-in Jira site.
- Signup placeholder "you@company.com" is the product's own sample text. The field was empty.
- Sign-in placeholder "Enter your email" is sample text. Nothing was typed.
- Contact prints street addresses and a phone number. That page was not photographed.
- The public stylesheet captured here is the light theme. A dark token sheet was not linked from the homepage.
- Get Jira free was not submitted. No checkout was opened.

## Fonts

| Family | Used for |
|---|---|
| Atlassian Sans | Headings and body. Declared on `--ds-font-heading-*` and `--ds-font-body`. |
| Charlie Display, Charlie Text | Declared on the marketing page as `--bxp-charlie-display-font-family` and `--bxp-charlie-text-font-family`. Not measured as a role. |

No font file is committed. The style guide falls back to system-ui.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles | Captured from declared `--ds-*` in the light stylesheet. |
| Type roles | Declared heading and body shorthand. Sizes are in the token values. |
| Spacing | Declared `--ds-space-*` scale. |
| Radii, elevation, motion | Elevation is declared as `--ds-shadow-raised` and `--ds-shadow-overlay`. Radii and motion were not measured. |
| Button | Get Jira free is a blue pill. See [screenshots/home-1440.png](screenshots/home-1440.png). |
| Text field | Empty on both walls. See [screenshots/signin-1440.png](screenshots/signin-1440.png). |
| Menu | Products, AI, Solutions, Why Atlassian, Resources, and the phone drawer. |
| App shell | Marketing header and footer. The product apps were not entered. |
| Dark theme | Not linked from the public homepage. |
| Desktop 1440 and phone 390 | Captured for the shell pages and both walls. |
| Form with validation error | Not captured. Forms were not submitted. |
| Checkout, subscribe, onboarding | Stopped at the walls. |

## Do and don't

- **Do use one blue pill for the primary action.** Get Jira free is `#1868DB` on white. See [screenshots/home-1440.png](screenshots/home-1440.png).
- **Do keep Sign in as text.** It sits beside the pill, not inside a second one. See [screenshots/home-1440.png](screenshots/home-1440.png).
- **Do open the nav as a panel of cards.** Products is a menuitem, not a page. See [screenshots/menu-products-1440.png](screenshots/menu-products-1440.png).
- **Don't treat the hero board as the product.** It is a public demo. The sign-in wall is [screenshots/signin-1440.png](screenshots/signin-1440.png).
- **Don't start a trial from this package.** Signup stops at an empty email field. See [screenshots/signup-1440.png](screenshots/signup-1440.png).
- **Don't invent a dark marketing theme.** The homepage painted light.

## Rebuild

```bash
# Shots were taken with headless Chromium at 1440x900 and 390x844, then
# quantised with tools/kit/capture/quantize.py. catalog.json was left alone,
# so make design-md was not run for this package.
```
