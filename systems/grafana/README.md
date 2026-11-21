# Grafana

Grafana is an observability platform from Grafana Labs. This package is a public Playwright capture of [grafana.com](https://grafana.com/) on 2026-11-22, signed out. Marketing pages are light, on a gray page (`#f4f4f6`) with a peach-to-blue hero. Desktop width measured 1440 by 900. Phone width measured 390 by 844 on the home page and the pricing page. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the published schema icon |
| [DESIGN.md](DESIGN.md) | Light-theme copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, radius, and motion tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of Sign up, Sign in, and Pricing |
| [icons/](icons/) | Header wordmark SVG and INDEX.tsv |
| [screenshots/](screenshots/) | Public pages, open menus, and the login and signup walls |
| [raw/](raw/) | Computed styles and custom properties that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | Token check and the style-guide writer |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the public site at 1440 by 900, `devicePixelRatio` 1. A preview browser at the same CSS width, `devicePixelRatio` 2, read `getComputedStyle` on the body, the h1, Sign up, Sign in, and Pricing, and read the `--gmui-*` custom properties from the stylesheets. Hover on Sign up was a real pointer move. Focus on Sign up was `element.focus()`. Cookie banners were hidden, not answered.

Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2. The home phone shot measured `innerWidth` 390.

## What to distrust

This is the marketing site, not the signed-in Grafana product. Do not treat the hero gradient or the pricing cards as the app chrome.

Sign up hover was measured as `#1440e1`. The default fill is `#1b55f5`. The style guide button uses the default fill.

`--gmui-color-red-500` and `--gmui-color-amber-600` are published tokens. They were not seen as live error or warning states.

The signup screenshot has the Cloudflare Turnstile widget painted over with the card white. The widget was not solved. The contact screenshots have the published mailbox painted over. The downloads email field had a placeholder address painted over. The field border is still the live page.

Spacing is a 4px unit, not a named scale. Control height is on the Sign up measurement, not a separate size token.

## Fonts

Inter is the UI face. Poppins is the display face. These are commercial faces. The tokens name them. The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Colour, accent | Captured | Sign up fill `#1b55f5` |
| Colour, status | Captured as tokens | Green, red, and amber custom properties. Live error and warning states were not shown |
| Type, display and UI | Captured | Home h1 and body |
| Type, code | Not captured | Mono family is a custom property. No code sample was measured |
| Spacing scale | Captured as a unit | `--gmui-spacing` is 4px. No named scale |
| Radius | Captured | 8px control, 4px nav item, 16px panel token |
| Elevation | Not captured | Sign up computed box-shadow none. Menu shadow was not stored |
| Motion | Captured | 150ms, `cubic-bezier(0, 0, 0.2, 1)` |
| Button | Captured | [components/crops/button-signup-default.png](components/crops/button-signup-default.png) |
| Button hover | Captured | [components/crops/button-signup-hover.png](components/crops/button-signup-hover.png) |
| Button focus | Captured | [screenshots/home-light-signup-focus.png](screenshots/home-light-signup-focus.png) |
| Link | Captured | [components/crops/link-pricing-default.png](components/crops/link-pricing-default.png) |
| Text field | Captured, empty | [screenshots/contact-light-default.png](screenshots/contact-light-default.png) |
| Text area | Captured, empty | Same contact page |
| Select | Observed, not opened | Contact menus |
| Checkbox | Captured, unchecked | [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |
| Radio, switch | Not present | Not on the public pages that were opened |
| Tabs | Observed | Downloads Cloud and OSS. OSS was not activated |
| Menu | Captured | [screenshots/home-light-menu-grafana-cloud.png](screenshots/home-light-menu-grafana-cloud.png) |
| Tooltip, toast, dialog | Not present | Not shown on the public pages |
| Card | Captured | [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) |
| Table, list row, avatar | Not present | Not on the public pages that were opened |
| Icon button | Not captured | Phone menu button was visible and not opened |
| App shell | Captured | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Form validation | Not captured | Contact form was not submitted |
| Empty, loading, error | Not captured | Signed-in app was not entered |
| Destructive confirmation | Not present | Not on the public site |
| Search | Captured, empty | Docs search and homepage Ask AI. Neither was submitted |
| Onboarding | Not captured | Would require an account |
| Dark theme | Not present | Public marketing site is light |
| Light theme | Captured | Marketing site, login, and signup |
| Desktop 1440 | Captured | Playwright innerWidth 1440 |
| Phone 390 | Captured | Home and pricing |
| Signed-in app | Not captured | Login wall. Session absent |

## Do and don't

- **Use blue for the primary action.** Sign up is `#1b55f5` on white, 8px radius, 36px tall, Inter 14/500. Hover is `#1440e1`. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Keep the page on gray.** Body background is `#f4f4f6`. Cards and the header are white. Display type is Poppins. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Use orange for the mark, not for buttons.** `--gmui-color-orange-600` is `#f04306`. The logo mark is that orange. Buttons stay blue. See [icon.png](icon.png).
- **Do not submit the signup form from this capture.** Signup offers Google, GitHub, Microsoft, and Amazon as well as email. A captcha was on the page and was not solved. No account was created. See [screenshots/signup-light-default.png](screenshots/signup-light-default.png).
- **Do not follow Sign in and keep capturing.** That URL is a login wall. Record it and stop. See [login-review.json](login-review.json).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run those from this folder. `tools/build_tokens.py` checks sources. It does not regenerate tokens.json. The tokens were written from the readings at capture time. `make design-md` cannot write this package's DESIGN.md until catalog.json has a `grafana` entry. This pass does not edit catalog.json.
