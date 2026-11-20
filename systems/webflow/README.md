# Webflow design reference

A token set and component reference for Webflow's public marketing site (https://webflow.com/), the agentic web platform for modern businesses. Use it to build a marketing surface that borrows its look: a white page (`#ffffff`) in light and a near-black page (`#080808`) in dark, ink that swaps with the page, primary blue `#146ef5` on buttons and the campaign bar, 4px control radii, 8px card radii, and WF Visual Sans Variable with an Arial fallback. It was captured signed out, in headless Chromium, on 2026-11-21. Desktop is 1440×900 at devicePixelRatio 1. Phone is 390×844 at devicePixelRatio 2 (screenshots are 780 wide).

The designer, dashboard, site editor, and billing sit behind login and were not opened. Signup is a press-and-hold bot wall. Desktop login showed email and password; the password was not typed and Continue with Google was not clicked. Dark and phone login returned HTTP 403. This package contains no Webflow code, and none of its artwork has been redrawn. The screenshots and the visual system they show belong to Webflow ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions, not the logo, artwork, or brand assets.

| File | What it is |
|---|---|
| [icon.png](icon.png) | 128 px PNG from the public apple-touch webclip, scaled with `sips`. `tools/fetch_icon.py` was not used: it wants a catalog entry, and this capture does not add one |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (neutrals, brand hues, type, radius, spacing, motion), `light` and `dark` semantic colours. Every token has `$extensions.source` |
| [style-guide.html](style-guide.html) | One page that renders the semantic colours, type roles, radii, and a sample button in both themes. Open it from disk. It uses Arial, not the proprietary face |
| [components.md](components.md) | Component inventory from the public site, with crops where the measure pass resolved an element, and a Gaps section |
| [patterns.md](patterns.md) | How the marketing shell, menus, pricing grid, forms, and phone sheet combine |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or wall. Written before the screenshot pass |
| [components/crops/](components/crops) | 30 element crops, `{component}-{state}.png`, from `tools/capture/public/measure.mjs` |
| [screenshots/](screenshots) | 43 viewport captures, `{page}-{theme}-{state}.png`, quantised to 256 colours. Full-page sheets were not committed |
| [raw/](raw) | `css-vars.json` (custom properties and theme rules), `computed-colors.json` (resolved colour vars), `components-computed.json` (measured elements) |
| [tools/](tools) | The adapted kit: public capture, measure, vars, token builder, and the style-guide template |

## Brief

<!-- brief:start -->

Not generated. `make brief` reads a catalog entry, and this capture does not edit [catalog.json](../../catalog.json). Read [tokens.json](tokens.json) and the Do and don't list below.

<!-- brief:end -->

## Health

<!-- health:start -->

Not generated. `make grade` writes Health from a catalog entry and a scorecard snapshot. This capture does not edit [catalog.json](../../catalog.json), so Health, DESIGN.md, and `make check` cannot pass for this package. That is a policy gap, not a missing measurement.

Layout ([docs/PACKAGE.md](../../docs/PACKAGE.md)): no `DESIGN.md` (needs a catalog entry). No `icons/` (the public chrome uses the `webflow-icons` icon font; no standalone SVG set was extracted).

<!-- health:end -->

## How the values were read

Headless Playwright (`~/.design-systems/pw`) loaded https://webflow.com/ signed out. `tools/capture/vars.mjs` wrote [raw/css-vars.json](raw/css-vars.json) from the live stylesheets: 236 custom properties and 37 theme rules, 0 parse errors. `tools/capture/public/resolve-colors.mjs` computed each colour variable on `html` in light and in dark and wrote [raw/computed-colors.json](raw/computed-colors.json). Dark mode is a public control. A button labelled "Dark mode" sets `localStorage.darkMode` to `true` and adds `u-mode-dark` on `html`. After that, body background computed to `rgb(8, 8, 8)` and `colorScheme` became `dark`. Light has no `data-theme`, `colorScheme` `normal`, body `rgb(255, 255, 255)`.

`tools/capture/public/measure.mjs` read computed styles for nav, menu, hero, card, pricing switch, the contact-sales field, and the login fields. It did not type, submit, or follow a signup link. `tools/build_tokens.py` wrote [tokens.json](tokens.json) from those readings. Screenshots came from `tools/capture/public/public.mjs` at the two viewports above, then `tools/capture/quantize.py` reduced a curated set to 256-colour PNGs.

The cookie card was never accepted or rejected. A DOM hide that matched the smallest consent box did not remove it on every page. A later paint covered the card region on some raw shots before quantise. That paint is not a product colour.

## What to distrust

- **The product is absent.** The designer, dashboard, CMS, and billing are behind https://webflow.com/login. Desktop light login showed the form. The password was not submitted. Continue with Google was not clicked. Dark login and phone login returned HTTP 403. Signup is a press-and-hold bot wall at https://webflow.com/signup. Nothing here describes the app.
- **Screenshots are 256-colour PNGs.** Read exact colours from [tokens.json](tokens.json) or [raw/computed-colors.json](raw/computed-colors.json), never from a screenshot pixel.
- **Homepage and login shots have a paint bite.** [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/home-dark-default.png](screenshots/home-dark-default.png), and [screenshots/login-light-wall.png](screenshots/login-light-wall.png) lost a rectangle where the cookie card sat. The white notch on the login livestream panel is that cover, not a product shape. The platform menu shot is cleaner: [screenshots/home-light-platform-menu.png](screenshots/home-light-platform-menu.png).
- **Fluid sizes are Derived.** Spacing steps in `core.spacing` are the desktop end of `clamp()`, labelled Derived in `$extensions.source`. Type sizes that came from a clamp are labelled the same way.
- **Primary button and badge crops missed.** The measure pass did not find a visible "Get started" button or a "NEW" badge element. The blue fill `#146ef5` and white on-accent are from CSS variables, not from a crop. See [screenshots/home-light-default.png](screenshots/home-light-default.png) for the painted button.
- **Phone menu measure said hidden.** [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) shows the sheet open. The measure JSON did not record an open overlay. Trust the screenshot for layout, not a missing crop.
- **CTA copy swaps.** The captured homepage paints "Start for free" as the blue header button. An earlier load painted "Contact Sales" there. Do not treat one label as the only header CTA.
- **Vendor CSS is in the raw dump.** Swiper and Marketo embed variables sit in [raw/css-vars.json](raw/css-vars.json). They are not Webflow semantic colours. Signed CDN query strings were not copied into the package prose.
- **Login marketing names are public.** The login wall shows published livestream hosts. They are not account data. Do not copy a signup Reference ID out of a bot-wall screenshot into new prose.

## Fonts

- **WF Visual Sans Variable** is the painted UI face (`--_typography---fonts--primary-font`). It is proprietary. It is not committed. The style guide falls back to Arial.
- **Arial, sans-serif** is the declared fallback in the same stack.
- **Inconsolata** is the code face loaded by `@font-face`. The token stack adds `ui-monospace, monospace` as a Derived generic fallback.
- **webflow-icons** is an icon font used by the chrome. Individual glyphs were not extracted as SVG.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.page` `#ffffff`, `dark.page` `#080808`, `light.surface` `#f0f0f0`, `dark.surface` `#171717`, `light.text` `#080808`, `dark.text` `#ffffff`, `light.muted` `#5a5a5a`, `dark.muted` `#ababab`, accent `#146ef5` both themes, `light.border` `#d8d8d8`, `dark.border` `#363636` |
| Accent states | partly | Default fill measured from `--colors--primary-accent`. Hover of the header CTA is a screenshot ([screenshots/home-light-cta-hover.png](screenshots/home-light-cta-hover.png)), not a computed crop. Pressed, disabled, and loading were not shown |
| Theme parity | captured | Dark is a live public control, painted on home, pricing, enterprise, and the platform menu |
| Type | captured | `core.fontFamily.ui` and `core.typography` from CSS variables. Clamp sizes are Derived |
| Shape | captured | Button and input `0.25rem`, card `0.5rem` |
| Spacing | Derived | Desktop ends of `clamp()` in `core.spacing` |
| Motion | captured | `--transition-duration-1` through `-4` are 150, 300, 450, and 750 ms, with `--transition-timing-inoutcubic`. Reduced motion was not separately measured |
| Button | partly | Painted on the homepage. Crop missed. Quiet "Talk to Sales" is in the same screenshot |
| Icon button | captured | Phone `.w-nav-button`, crops `icon-button-default` and `icon-button-pressed` |
| Link | captured | Nav link default, hover, and focus-visible, both themes |
| Text field | captured | Login email and password (not typed). Contact-sales email default and focus. Form not submitted |
| Text area | not captured | Contact-sales was opened and not filled. Measure did not resolve a textarea |
| Select | not captured | Pricing bandwidth and locale selects were present and not opened or submitted |
| Checkbox, radio | not present | Not on the captured public pages. Billing is a switch |
| Switch | captured | Pricing Monthly / Yearly, default Yearly. Crops `switch-default` and `switch-dark-default` |
| Tabs | not present | The role switcher is a menu, not a tablist |
| Menu | captured | Platform, Solutions, Resources, role menu, phone sheet. See [site-tree.md](site-tree.md) |
| Tooltip | not captured | None held open |
| Dialog | captured | Homepage story dialog. Cookie card seen and not answered. Two-factor dialog mounted and not opened |
| Toast | not present | No form was submitted |
| Card | captured | Homepage story card and pricing plan cards |
| List row | captured | Phone menu rows in [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Table | not present | Pricing is a card grid |
| Avatar | not captured | Story portraits are marketing photos. No account avatar |
| Badge | partly | "NEW" is visible in the platform menu and on pricing. No crop |
| App shell, pricing, search focus, contact form, auth walls, phone | captured | [screenshots/](screenshots), [patterns.md](patterns.md) |
| Form validation, empty, loading, error, destructive confirm, onboarding | not captured | Forms were not submitted. Signup stops at the bot wall |
| Signed-in product | not captured | Login and signup walls stop the branch |
| Language pages `/fr`, `/de`, `/es` | not captured | Listed in the site tree. Not screenshotted |
| Footer feature, customer, and legal pages beyond the shot list | not captured | Mapped in [site-tree.md](site-tree.md). Individually screenshotted: about, legal, accessibility, vs not included, most `/feature/*` and `/customers/*` not included |
| Icons as SVG | not captured | Icon font only |
| Full-page screenshots | not committed | Viewport shots only. Pricing full page was about 7900 to 8300 px on different loads |

## Do and don't

- **Do keep light pages white and dark pages `#080808`.** Light text is `#080808`. Dark text is white. The campaign bar and the primary button stay `#146ef5` in both. ([home light](screenshots/home-light-default.png), [home dark](screenshots/home-dark-default.png))
- **Do use `#146ef5` with white text for the primary action.** Radius is `0.25rem`. "Get started" and "Start for free" use that fill. "Talk to Sales" is a quiet gray button. ([home](screenshots/home-light-default.png), [CTA hover](screenshots/home-light-cta-hover.png))
- **Do open Platform, Solutions, and Resources as menus, not as page loads.** The panel is a light gray surface, four columns, and two blue promo cards. Appearance sits in that chrome. ([platform menu](screenshots/home-light-platform-menu.png))
- **Do radius cards at `0.5rem` and inputs at `0.25rem`.** Plan cards use the secondary surface `#f0f0f0` in light. ([pricing](screenshots/pricing-light-default.png), [login field crop](components/crops/login-email-default.png))
- **Do name WF Visual Sans Variable and fall back to Arial.** Do not commit the webfont. ([hero crop](components/crops/hero-title-default.png))
- **Don't treat this package as the designer.** Login, signup, and the hidden two-factor dialog stop the branch. A screen of the editor built from these tokens would be invented. ([login wall](screenshots/login-light-wall.png), [signup wall](screenshots/signup-light-wall.png))
- **Don't read a colour off a screenshot pixel.** The homepage and login shots have a paint bite. Quantising also collapses gradients. ([login wall](screenshots/login-light-wall.png))
- **Don't submit the contact form or click Accept all.** Those controls were recorded and left alone. ([contact sales](screenshots/contact-sales-light-default.png))

## Rebuild

```bash
cd systems/webflow
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/resolve-colors.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
python3 tools/build_tokens.py
python3 tools/capture/quantize.py
```

`make design-md`, `make brief`, `make grade`, and `make check` need a catalog entry. This capture does not add one. Do not edit [catalog.json](../../catalog.json) or [webapps-manifest.json](../../webapps-manifest.json) to make those commands pass.

## Site tree

The full map is [site-tree.md](site-tree.md). From the homepage header: Platform opens `dropdown_content_0` (Design, CMS, Analyze, Apps, and the rest of the feature list, plus Platform Overview and Webflow AI). Source opens `/source`. Solutions opens `dropdown_content_1` (Brand, Performance, Agencies, Enterprise, and the other solution links). Resources opens `dropdown_content_2` (Templates, Blog, Customers, and external University, Developers, Help, and Community hosts). Enterprise opens `/enterprise`. Pricing opens `/pricing`. Log in opens `/login` and stops. Start for free opens `/signup` and stops at the bot wall. Contact Sales opens `/enterprise/contact-sales` and was not submitted. Dark mode is a button inside the menu chrome, not a separate route. Phone uses one `.w-nav-button` (`aria-label="menu"`) to open the same links.
