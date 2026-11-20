# Super design reference

A token set and component reference for Super's public marketing site, for building a light Notion-to-website marketing surface in the style of the real thing. It was read from **https://super.so/** on **2026-11-21**, signed out, in headless Chromium at 1440 x 900 (device pixel ratio 1) and 390 x 844 (device pixel ratio 2). The signed-in app at app.super.so was not entered. The login wall was photographed once and left empty.

Super publishes Notion pages as websites. The marketing site is itself a Super site: Notion content, a custom navbar (`.super-navbar`), and a yellow call to action that is a computed fill, not a `--color-*` token. The page ground is `#fdfdfc`. Body text is `#262a2e`. The footer is near-black. Visible headings are `h1.notion-heading` in Beausite at 56px on the home hero and 57.6px on pricing and feature pages.

No account was used. No email was typed. Google, Apple and the passkey control were not clicked. No form was submitted.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Super's site icon, 128 px PNG, from the homepage favicon on assets.super.so |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the `--color-*` palette, two font stacks, six type styles, two radii and three control paddings. `light` holds page, surface, text, muted, accent, accent hover, border, navbar, footer and footer text. No dark set. Every token has `$extensions.source` |
| [style-guide.html](style-guide.html) | One page that renders the tokens and a redraw of the navbar, the yellow button and the footer. Beausite is not loaded |
| [components.md](components.md) | Measured controls, crops, and the selector misses |
| [patterns.md](patterns.md) | How the shell, home, pricing, templates, feature pages and the login wall combine |
| [site-tree.md](site-tree.md) | Which control opens which page, menu or wall, mapped before the screenshots |
| [components/crops/](components/crops) | 74 element screenshots, `{component}-{state}.png` |
| [screenshots/](screenshots) | 53 page captures, `{page}-light-{state}.png`. Desktop 1440 wide at 1x. `mobile-*` is 390 CSS px at 2x, so the PNG is 780 px wide |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) from the CSSOM, [components-computed.json](raw/components-computed.json) from `getComputedStyle` |
| [tools/](tools) | The capture kit and the builders. See [Rebuild](#rebuild) |

## Brief

<!-- brief:start -->
Not generated. This package has no catalog.json entry, by the capture rule that a capture PR must not edit catalog.json. `make brief` reads the catalog and was not run.
<!-- brief:end -->

## Health

<!-- health:start -->
Not generated. `make grade` writes Health from the catalog and a scorecard snapshot. Neither was run. `make check` will report that `systems/super-so` has no catalog.json entry. That is the capture rule, not a missing file in this folder.
<!-- health:end -->

## How the values were read

Every value came off the running signed-out site in headless Chromium, through Playwright at `~/.design-systems/pw`. The T3 preview browser was not used.

- **Tokens.** [tools/capture/vars.mjs](tools/capture/vars.mjs) read the CSSOM on https://super.so/. It found 26 rules and 12 font faces. Custom properties were resolved on the live root. `--color-*` names went into `core.color`. Vendor names (`--cc-*` cookie consent, `--rdp-*` date picker) were left out of the token file. [tools/build_tokens.py](tools/build_tokens.py) writes [tokens.json](tokens.json).
- **Components.** [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) opened each route in a fresh context and read `getComputedStyle` for default, hover, focus-visible and pressed, plus focused and filled on the template search field. Results are in [raw/components-computed.json](raw/components-computed.json). Crops are in [components/crops/](components/crops).
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) took viewport and full-page shots. They were posterised to 256 colours. Measured viewport: desktop `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1. Phone `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2.
- **Icon.** The homepage `<link rel="icon">` points at a PNG on assets.super.so. `tools/fetch_icon.py` failed on this machine because Python's certificate store rejected the host. The same URL was fetched with curl and resized with `sips -Z 128` to [icon.png](icon.png).
- **Site tree.** [site-tree.md](site-tree.md) was written from the live header, footer and in-page controls before the package screenshots.

Nothing was signed into. The template search field was filled with the word portfolio and cleared. Login fields were focused empty. Password was not submitted.

## What to distrust

- **One painted theme.** The public site paints light. `html.theme-dark` declares a dark rule set and was not switched, so those values are Not captured. There is no dark token set.
- **The yellow CTA is not `--color-yellow`.** `light.accent` is the computed background of `.super-navbar__cta`, `#ffbe3c`. `core.color.yellow` is `#ffaa00`. Do not alias them.
- **Login yellow is a third value.** The login submit computed to `rgb(255, 190, 61)`, and its hover to `rgb(255, 174, 0)`. Those are in the component entry, not in `light.accent`.
- **Wrong nodes.** [components.md](components.md) names them: announcement matched the whole page, template-card and pricing-cta matched a Free badge, page-title and blog-title matched grey eyebrows, category-row was 0 x 0, the navbar dropdown panel clip failed. Do not read those crops as the named component.
- **Derived line heights.** `core.typography.body` line-height 24px and `label` line-height 20px were derived because computed line-height was `normal`. The source string says so.
- **Spacing is not a scale.** `core.spacing` is three control paddings.
- **Focus.** Captured focus-visible states painted no ring. No focus colour token.
- **Quantised screenshots.** `screenshots/` are 256-colour PNGs. Read exact colours from tokens or the raw JSON.
- **8-chunk cap.** [home-light-full.png](screenshots/home-light-full.png) is 1440 x 20020 and stops before the page ends. [mobile-home-light-full.png](screenshots/mobile-home-light-full.png) is 780 x 73988 and is also capped.
- **Cookie banner.** `--cc-*` exists in CSS. No banner mounted. Those names are not tokens.
- **No catalog entry.** [DESIGN.md](DESIGN.md) is not in this package. `tools/catalog.py design-md` requires a catalog entry, and this capture must not edit catalog.json.

## Fonts

`--primary-font` and `--secondary-font` both resolve to Beausite, then Inter, then Helvetica and the system sans. Twelve `@font-face` rules point at woff2 files on assets.super.so. Beausite and Inter files are not committed. [style-guide.html](style-guide.html) uses Helvetica, then the system sans.

## Coverage

| Checklist | Status | Where |
|---|---|---|
| Colour roles, light | Captured | [tokens.json](tokens.json) `light`, [home-light-default.png](screenshots/home-light-default.png) |
| Colour roles, dark | Not captured | `html.theme-dark` declared, not switched. No public toggle |
| Type roles | Captured | `core.typography` from hero, pricing, feature, body, search, CTA |
| Spacing scale | Not present | Three control paddings only |
| Radii | Captured | 8px on the CTA. 14px is `--floating-toc-panel-radius`, declared, not cropped |
| Borders | Captured | `light.border` from `--color-border-default` |
| Elevation | Partly | Hero CTA shadow recorded in [components.md](components.md). No elevation scale |
| Motion | Not captured | No duration tokens read |
| Button | Captured | Navbar CTA, hero CTA, login submit |
| Icon button | Captured | Phone hamburger [m-menu-button-default.png](components/crops/m-menu-button-default.png) |
| Link | Captured | Nav link, footer link |
| Text field | Partly | Template search measured. Login field chrome not the measured node |
| Text area, select, checkbox, radio, switch | Not present on the public pages opened | |
| Tabs | Partly | Pricing Monthly / Yearly / Multi-pack is on [pricing-light-default.png](screenshots/pricing-light-default.png). Not measured as a component |
| Menu | Partly | Use cases and Features open in screenshots. Panel crop failed |
| Tooltip, dialog, toast | Not present on the pages opened | |
| Card | Partly | Blog card wrapper measured. Template card selector missed. Cards are visible on [templates-light-default.png](screenshots/templates-light-default.png) |
| List row | Partly | Phone drawer item measured. Template category row was 0 x 0 |
| Table, avatar | Not captured | Not measured |
| Badge | Not captured | Free pill is visible. The crop that hit it was filed under the wrong name |
| Hover, pressed | Captured where the control changed | Hero CTA, Sign in, Load more, login submit, dropdown item |
| Focus-visible | Captured as no visible change | On the controls that were focused |
| Disabled, loading, error | Not present on the public pages | Behind the login wall if they exist |
| App shell | Captured | Marketing navbar and phone drawer |
| Form validation, empty, loading, destructive, onboarding | Not captured | Login or signup wall. Branch stopped |
| Search and filtering | Captured | [templates-light-search-filled.png](screenshots/templates-light-search-filled.png), [templates-light-category.png](screenshots/templates-light-category.png) |
| Desktop 1440 and phone 390 | Captured | Sidecars recorded those `innerWidth` values. Phone PNGs are 780 px wide at 2x |
| Login wall | Captured, not crossed | [login-light-wall.png](screenshots/login-light-wall.png). No email, no password, no Google, no Apple, no passkey |
| Signed-in app | Not captured | Wall at https://app.super.so/login and https://app.super.so/signup |
| Customer sites | Not captured | `*.super.site` is customer content |
| Docs, changelog, status, feedback | One viewport each | Separate hosts, not the marketing shell |
| Sibling use-case and feature pages | Listed, not each shot | [site-tree.md](site-tree.md). One use case and one feature page stand in |
| Dead hash links | One 404 shell | [notfound-light-default.png](screenshots/notfound-light-default.png) |

## Do and don't

- **Do** paint the page `#fdfdfc` and the body text `#262a2e`. [home-light-default.png](screenshots/home-light-default.png).
- **Do** use `#ffbe3c` for the marketing call to action, with `#111111` text and an 8px radius. [nav-cta-default.png](components/crops/nav-cta-default.png).
- **Do** keep the navbar 80px and `rgba(255, 255, 255, 0.85)`. [navbar-default.png](components/crops/navbar-default.png).
- **Do** set visible headings in Beausite at 56px on the hero and 57.6px on pricing and feature pages. Fall back to Helvetica when the webfont is absent. [hero-title-default.png](components/crops/hero-title-default.png).
- **Do** paint the footer `#090909` with white text. [footer-default.png](components/crops/footer-default.png).
- **Don't** alias the yellow button to `core.color.yellow` (`#ffaa00`). The button is a computed fill.
- **Don't** invent a dark theme from `html.theme-dark`. It was not switched.
- **Don't** treat the Free-badge crops as a template card or a pricing button.
- **Don't** follow Sign in or Get started free past the wall. [login-light-wall.png](screenshots/login-light-wall.png).
- **Don't** read colours off the 256-colour screenshots.

## Rebuild

From the package folder, with the readings already in `raw/`:

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`tools/build_components_md.py` is the shared kit and still expects another product's `raw/component-tokens.json`. [components.md](components.md) was written from [raw/components-computed.json](raw/components-computed.json). Do not run that kit script against this package.

Recapture needs Playwright at `~/.design-systems/pw` and network access to super.so. The public runner does not click Sign in, Get started, Google, Apple or a passkey, and it does not submit forms.

```bash
node tools/capture/vars.mjs
node tools/capture/public/public.mjs
node tools/capture/public/measure.mjs
```

## Catalog

This folder is not in catalog.json. A capture PR that edits catalog.json is rejected. DESIGN.md, Brief and Health stay ungenerated until a later change adds the entry.
