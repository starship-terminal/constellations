# WordPress.com

Public site tree, dated 2026-11-22, is [site-tree.md](site-tree.md). That pass photographed the signed-out marketing pages and the empty log-in and signup walls. `catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` stays not-started.

WordPress.com is Automattic's hosted WordPress product (https://wordpress.com). This package captures that public site. wordpress.org was not captured.

Surfaces: homepage, product pages from the Products and Resources menus, pricing, support, guides, courses, forums, contact, about, accessibility, sitemap, compare, press, themes, plugins, patterns, features, blog, and discover. Theme: light. Widths: 1440 and 390 CSS pixels. Captured 22 November 2026.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 512 px web clip from https://s1.wp.com/i/webclip.png |
| [DESIGN.md](DESIGN.md) | Hand-written from tokens.json. Not generated: catalog.json was left alone |
| [tokens.json](tokens.json) | Studio colours and the type and size readings |
| [style-guide.html](style-guide.html) | Swatches from those tokens |
| [components.md](components.md) | Controls that painted on the public pages |
| [patterns.md](patterns.md) | The captured pages |
| [screenshots/](screenshots/) | Marketing pages and the empty walls |
| [site-tree.md](site-tree.md) | Header, footer, and the public pages those controls open. Mapped 2026-11-22 |
| [login-review.json](login-review.json) | Empty log-in and signup walls. `login-extracted` is not-started |
| [raw/](raw/) | Declared custom properties from the public homepage |
| [tools/](tools/) | Note on how the shots were made |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

wordpress.com declares Automattic Studio colours as `--studio-*` custom properties, and marketing type as `--lp-font-stack-*` and `--lp-font-size-*`. Those names were read from the homepage stylesheets into [raw/css-vars.json](raw/css-vars.json). Button height, radius, and the headline size were also read with `getComputedStyle`. Screenshots were not sampled for colour.

Log in and signup were opened and not filled. Continue was not clicked. Identity providers were not clicked. No captcha was solved.

Screenshots were taken with headless Chromium at 1440 by 900 and 390 by 844, device pixel ratio 2, then quantised to 256 colours. The empty login wall was photographed in a signed-out preview tab because headless Chromium received a captcha interstitial. Sidecars record the measured viewport and the PNG pixel size.

## What to distrust

- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- The homepage hero swaps copy after a few seconds. The saved home shots are the later blue hosting hero, not the first restaurant frame.
- Pricing shows Singapore dollars (S$). That is the locale the capture host resolved. The amounts are not a token.
- Login controls use a 2px radius. Marketing buttons use the declared 4px `--lp-radius`.
- Green, red, yellow, and pink are declared. Only green was seen, on the pricing savings line.
- Motion durations were not read.
- The homepage footer is a section, not a `footer` element.

## Coverage

| Checklist item | Status | Evidence |
|---|---|---|
| Colour roles | Captured, partial | Blue, ink, paper, gray, white in [tokens.json](tokens.json). Scrim not isolated. |
| Type | Captured, partial | Recoleta display, Inter UI, 80px headline, 13px nav. |
| Spacing | Not captured | Pad tokens exist in the stylesheet and were not mapped to a scale. |
| Radii | Captured | 4px marketing, 2px on the login wall, 999px pill token. |
| Borders | Captured, partial | Login field 1px blue when focused. |
| Elevation | Not captured | Plan cards sit on a dark band. Shadow not tokenised. |
| Motion | Not captured | Hero copy swaps. No duration was read. |
| Sizing | Captured, partial | Nav 64, hero button 48, login field 40. |
| Layout | Captured, partial | 1440 and 390. |
| Button | Captured, partial | Blue Get started, quiet Log in, disabled signup Continue. Hover and pressed not isolated. |
| Icon button | Captured | Promo close and phone menu. Not cropped. |
| Link | Captured | Pricing and support text links. |
| Text field | Captured | Empty login and signup fields. Not typed. |
| Text area | Not present | |
| Select | Observed | Pricing yearly toggle. Not opened. |
| Checkbox | Not present | |
| Radio | Not present | |
| Switch | Not present | |
| Tabs | Observed | Discover tabs. Not switched. |
| Menu | Captured | Products, Resources, phone drawer. |
| Tooltip | Not present | |
| Dialog | Not captured | Help "?" was not opened. |
| Toast | Not present | |
| Card | Captured | Pricing plans, contact cards, discover posts. |
| List row | Captured | Phone drawer rows. |
| Table | Not present | |
| Avatar | Observed | Discover comment avatars. Public readers. |
| Badge | Captured | Most popular, Save 58%. |
| App shell | Captured | Header, footer, phone drawer. |
| Form validation | Not captured | No submit. |
| Empty, loading, error | Captured, partial | Signup Continue disabled. Login captcha in headless was discarded. |
| Destructive confirmation | Not captured | Behind login. |
| Feedback after an action | Not captured | Nothing submitted. |
| Search and filtering | Not captured | Support search was not typed. |
| Onboarding | Not captured | Signup is an auth wall. The editor was not started. |
| Themes | Captured, partial | Light only. No public theme toggle. |
| Widths | Captured | Desktop 1440 by 900. Phone 390 by 844. |
| Principles and voice | Not captured | No public design-system voice page was found. |
| Per-component behaviour | Not captured | No published component guide for this marketing site. |

## Do and don't

- **Use one blue for WordPress.com's own actions.** Get started and login Continue are `#3858e9`. [screenshots/home-1440.png](screenshots/home-1440.png)
- **Keep Log in quiet.** It is text beside the blue button. [screenshots/menu-phone-390.png](screenshots/menu-phone-390.png)
- **Set headlines in Recoleta and controls in Inter.** [screenshots/pricing-1440.png](screenshots/pricing-1440.png)
- **Leave signup Continue disabled until an email is present.** [screenshots/signup-1440.png](screenshots/signup-1440.png)
- **Stop at the login wall.** Identity buttons are visible and were not used. [screenshots/login-1440.png](screenshots/login-1440.png)

## Rebuild

There is no builder. Tokens were copied from the declared custom properties in [raw/css-vars.json](raw/css-vars.json). `make design-md` was not run, because it rewrites from catalog.json and this capture leaves the catalog alone.
