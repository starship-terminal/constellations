# Ghost

Public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). That pass photographed the signed-out marketing pages and the empty sign-in and signup walls. `catalog.json` was left alone. `login-extracted` stays not-started.

Ghost is an open source publishing platform (ghost.org) for websites, newsletters, and paid memberships. This package captures the public marketing site and the empty account walls. No account was created. No site was created.

Surfaces: home, Ghost 6.0, audience pages, pricing, explore, docs home, resources, themes, marketplace, help, integrations, changelog, experts, about, news, tutorials, reviews, one comparison page, and the alternatives index. Theme: light. Widths: 1440 and 390 CSS pixels. Captured 22 November 2026.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px PNG from https://ghost.org/images/logos/ghost-logo-orb.png |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json. Not generated here: catalog.json was left alone |
| [tokens.json](tokens.json) | Declared colour roles from the public stylesheet |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Controls that painted on the public pages |
| [patterns.md](patterns.md) | The captured pages |
| [screenshots/](screenshots/) | Marketing pages and the empty walls |
| [site-tree.md](site-tree.md) | Header, footer, and the public pages those controls open. Mapped 2026-11-22 |
| [login-review.json](login-review.json) | Empty sign-in and signup walls. `login-extracted` is not-started |
| [raw/](raw/) | Declared custom properties from the public stylesheet |
| [tools/](tools/) | Note on how the shots were made |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

ghost.org is a Hugo marketing site. The linked stylesheet `main.min.*.css` declares `--color-*` and `--header-*`. Those names were parsed into [raw/css-vars.json](raw/css-vars.json) and copied into [tokens.json](tokens.json). Screenshots were not sampled for colour.

Sign-in and signup were opened and not filled. Continue was not clicked. No consent button was clicked.

Screenshots were taken with headless Chromium at 1440 by 900 and 390 by 844, device pixel ratio 2, then quantised to 256 colours. Sidecars record the measured viewport.

## What to distrust

- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- The home dashboard is a public demo inside an iframe. It is not the signed-in admin.
- Signup placeholders (Jamie Larson, jamie@example.com) are the product's own sample text. The fields were empty.
- Sign-in placeholder "site.ghost.io or myghostsite.com" is sample text. Nothing was typed.
- Contact prints a street address. That page was not photographed.
- No dark marketing theme was painted on the homepage. A transparent-header variant exists in CSS for other pages. It was not captured as a theme.
- Pricing plan buttons were not clicked. Checkout was not opened.

## Fonts

| Family | Used for |
|---|---|
| Inter Display | Headlines. Declared as `--font-heading` (`InterDisplay`). |
| Inter | Body. Declared as `--font-sans-serif`. The site preloads InterVariable.woff2. |
| Menlo | Declared as `--font-monospace`. |

No font file is committed. The style guide falls back to system-ui.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles | Captured from declared `--color-*` and `--header-*`. Light only. |
| Type roles | Declared families and weights. Sizes not measured. |
| Spacing, radii, elevation, motion | Not measured. Shadow is declared as `--header-dropdown-shadow`. |
| Button | Get Started is a black pill. See [screenshots/home-1440.png](screenshots/home-1440.png). |
| Text field | Empty on the signup wall. See [screenshots/signup-390.png](screenshots/signup-390.png). |
| Menu | Product and Resources, desktop and phone. |
| App shell | Marketing header and footer. The admin app was not entered. |
| Dark theme | Not present on the public homepage. |
| Desktop 1440 and phone 390 | Captured for the shell pages and both walls. |
| Form with validation error | Not captured. Forms were not submitted. |
| Checkout, subscribe, onboarding | Stopped at the walls. |

## Do and don't

- **Do use one black pill for the primary action.** Get Started is `#15171A` on white. See [screenshots/home-1440.png](screenshots/home-1440.png).
- **Do keep Sign in as text.** It sits beside the pill, not inside a second one. See [screenshots/home-1440.png](screenshots/home-1440.png).
- **Do set the launch chip in yellow.** Ghost 6.0 uses `#ffd400`. See [screenshots/home-1440.png](screenshots/home-1440.png).
- **Don't treat the hero dashboard as the product.** It is a public demo. The sign-in wall is [screenshots/signin-1440.png](screenshots/signin-1440.png).
- **Don't start a site from this package.** Signup stops at an empty form. See [screenshots/signup-1440.png](screenshots/signup-1440.png).
- **Don't invent a dark marketing theme.** The homepage painted light.

## Rebuild

```bash
# Shots were taken with headless Chromium at 1440x900 and 390x844, then
# quantised with tools/kit/capture/quantize.py. catalog.json was left alone,
# so make design-md was not run for this package.
```
