# Fingerprint design reference

Public site of Fingerprint (fingerprint.com), captured 2026-11-21, signed out. Desktop 1440 by 900 and phone 390 by 844. One light theme on the marketing site. The dashboard login was reached and not entered.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px |
| [tokens.json](tokens.json) | Measured color ramps and the light roles |
| [DESIGN.md](DESIGN.md) | Generated export |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [components.md](components.md) | Controls that were seen |
| [patterns.md](patterns.md) | Header, menus, search, pricing, auth wall |
| [site-tree.md](site-tree.md) | Public page and control map |
| [login-review.json](login-review.json) | Auth wall. signed_in is false |
| [screenshots/](screenshots/) | 125 viewport shots, menus, docs search, login wall |
| [raw/](raw/) | Computed styles and declared fpds color channels |
| [tools/](tools/) | Capture kit copy and builders |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Playwright loaded https://fingerprint.com/ and read computed styles plus the `--fpds-color-*` custom properties. Those properties store HSL channels (`16 90% 54%`). They were resolved to hex. The Get Started button's computed fill is `#f35820`, which matches `--fpds-color-orange-7` and `--primary`. Hover is `#bd400f`. Focus draws a 2px white ring and a 4px orange ring. No value was sampled from a screenshot.

## What to distrust

The marketing site is light only. Docs has a dark-mode toggle that was not captured as a token set. Homepage frames that paint a live visitor identifier are not in screenshots/. The signed-in app, onboarding, and form validation were not captured. Sitemap leaves (599 blog posts, 150 bot pages, 101 explorer entries, 27 case studies) share hub chrome and were not each photographed.

## Fonts

Inter (hashed family name, Arial fallback) for UI. Petrona for serif. JetBrains Mono for code. None are bundled.

## Coverage

| Checklist item | Status | Evidence |
|---|---|---|
| Colour | captured | tokens.json light roles and core.color ramps |
| Type | captured | core.typography display, body, label |
| Spacing | not captured | No spacing scale read as a token set |
| Radius | captured | core.radius xs through 3xl |
| Button | captured | raw/cta-states.json default, hover, focus |
| Link | captured | Header and footer |
| Text field | captured | Search and newsletter, unfilled |
| Switch | captured | I'm a developer, toggled and restored |
| Menu | captured | screenshots/desktop-menu-product.png |
| Search | captured | screenshots/desktop-docs-search-open.png |
| Dialog | captured | screenshots/desktop-login-wall.png |
| Dark theme | not present | Marketing site is light. Docs toggle not measured |
| Signed-in app | not captured | Auth wall. login-review.json |
| Onboarding | not captured | Signup wall, not filled |
| Form validation | not captured | No form submitted |

## Do and don't

- **Keep the orange for the one primary action.** Get Started is `#f35820` on a warm gray page. See [pricing](screenshots/desktop-pricing.png).
- **Open Product, Use Cases, and Resources as panels, not pages.** See [Product menu](screenshots/desktop-menu-product.png).
- **Stop at the login dialog.** Google, GitHub, and Microsoft sit above email. See [login wall](screenshots/desktop-login-wall.png).
- **Do not invent a dark marketing theme.** The public site paints one light surface.
- **Do not submit the newsletter or contact form** as part of using this reference.

## Rebuild

```sh
python3 systems/fingerprint/tools/build_tokens.py
python3 systems/fingerprint/tools/build_style_guide.py
```

Values come from the readings already committed under raw/. The builders pass those through.
