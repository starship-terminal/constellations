# GitHub public surface

A token set and page captures for GitHub's public marketing site at **https://github.com**. First capture of this product into `systems/github/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 2 (PNG 2880 by 1800). Phone is **390 by 844** at devicePixelRatio 2 (PNG 780 by 1688). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/github/`. It has [systems/github-ios](../github-ios) (GitHub Mobile). That package was not edited. `catalog.json` and `webapps-manifest.json` were left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written. [DESIGN.md](DESIGN.md) was written from the measured tokens. It was not regenerated.

The marketing homepage paints a white page. Primer custom properties are on the page (`--fgColor-*`, `--bgColor-*`, `--button-primary-*`). The header Sign up pill is black. The hero Sign up for GitHub button is a sampled green (`#08792b`), not the Primer primary green (`#1f883d`). The login wall follows the OS colour scheme: dark in the preview, light in a headless page forced to light. There is no public theme toggle on the marketing header.

**Boundary.** The login wall was photographed empty and the branch stopped. Signup returned a captcha interstitial. The challenge was not solved. Nothing was typed. Nothing was submitted. Google, Apple, and passkey were not clicked. Star and Fork were not clicked. The signed-in dashboard was not opened.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login wall. Signup captcha discarded. login-extracted is not-started. |
| [icon.png](icon.png) | GitHub's fluidicon, scaled to 128px from `https://github.com/fluidicon.png`. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds type, radius, space, and control sizes. `light` and `dark` hold Primer roles plus the sampled hero button. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the light and dark chips and the hero controls. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/crops/](components/crops) | Element crops of the header Sign up pill, search, nav, hero buttons, email field, heading, and the empty login controls. |
| [icons/](icons/) | `mark.png` (64px) and `INDEX.tsv`. Do not ship. |
| [screenshots/](screenshots/) | Quantised page shots, menus, the search dialog, the phone drawer, and the empty login wall. Git LFS. |
| [raw/](raw/) | Computed styles and resolved Primer variables from the homepage, pricing, login, and the public docs repository. |
| [tools/](tools/) | `build_tokens.py` checks named roles against `raw/measured.json`. `build_style_guide.py` rebuilds the HTML. Neither rewrites `catalog.json`. |

## Brief

<!-- brief:start. Hand-written because catalog.json was left alone. make brief cannot attach a row. -->

Read this before designing in this style. Take every value from [tokens.json](tokens.json), never from the screenshots.

### Principles

1. Do paint the marketing page white with black ink on the display heading.
2. Do keep the header Sign up pill black, 32px tall, 6px radius.
3. Do keep the hero Sign up for GitHub button the sampled green `#08792b`, separate from Primer primary `#1f883d`.
4. Do use Mona Sans for display and Mona Sans VF for UI. The files are not in this package.
5. Don't style a signed-in dashboard from this package.
6. Don't treat hover and pressed Primer variables as photographed states.
7. Don't invent a signup form. The wall was a captcha and the shot was discarded.
8. Don't copy the octocat mark into a product you ship.

### Using tokens

| Role | light | dark |
|---|---|---|
| page | #ffffff `light.color.bg.default` | #0d1117 `dark.color.bg.default` |
| surface | #f6f8fa `light.color.bg.muted` | #151b23 `dark.color.bg.muted` |
| text | #1f2328 `light.color.fg.default` | #f0f6fc `dark.color.fg.default` |
| muted | #59636e `light.color.fg.muted` | #9198a1 `dark.color.fg.muted` |
| accent | #0969da `light.color.accent.emphasis` | #1f6feb `dark.color.accent.emphasis` |
| border | #d1d9e0 `light.color.border.default` | #3d444d `dark.color.border.default` |

Fonts: `core.font.family.display` is Mona Sans. `core.font.family.ui` is Mona Sans VF. The homepage h1 is 56px, weight 440, line-height 61.6px. Body is 14px / 400 / 21px.

### Using components

Read [components.md](components.md) for the inventory and [patterns.md](patterns.md) for how the pages combine. Crops are in [components/crops/](components/crops). [style-guide.html](style-guide.html) renders the chips and the hero controls.

### Accessibility

Light body text `#1f2328` on `#ffffff` is the painted pair. Muted `#59636e` on white is the secondary pair. Focus outline is `#0969da` (`light.color.border.focus`). Contrast was not graded by `make grade` because the catalog row was not added.

<!-- brief:end -->

## Health

<!-- health:start. Hand-written because catalog.json was left alone. make grade cannot attach a row. -->

No scorecard row. The catalog was left alone on purpose.

| Open | Grade | Evidence |
|---|---|---|
| Colour roles | Captured | Primer light roles on the homepage. Dark roles on the login wall and a dark-forced public repository. |
| Type | Captured | Homepage h1, body, nav link, hero button. |
| Button states | Partly | Default measured. Hover and active exist as Primer variables, not as photographed pointer states. |
| Auth | Stopped | Empty login wall. Signup captcha discarded. `login_extracted` is not-started. |
| Signed-in app | Missing | Not entered. |

<!-- health:end -->

## How the values were read

Computed style and Primer custom properties were read in headless Chromium on `https://github.com/` at 1440, on `https://github.com/login` with `colorScheme` dark, and on `https://github.com/github/docs` with a dark colour scheme. Those readings are in [raw/measured.json](raw/measured.json). Colour tokens are the resolved custom properties, written as hex. The hero button `#08792b` and the quiet download fill `rgba(0, 0, 0, 0.06)` are computed styles, labelled Sampled, because they are not the Primer primary token.

Menus, the search dialog, the phone drawer, and the dark login wall were also opened in the T3 preview and photographed at 2x. Page shots are headless Chromium at devicePixelRatio 2, then quantised to 256 colours.

## What to distrust

- **Screenshots are 256-colour.** Read colours from [tokens.json](tokens.json) and [raw/measured.json](raw/measured.json), not from a PNG pixel.
- **The hero green is sampled.** `#08792b` is the painted hero button. Primer's primary rest colour is `#1f883d`.
- **Hover and pressed were not photographed.** `--button-primary-bgColor-hover` and `--button-primary-bgColor-active` are stylesheet variables. Do not treat them as pointer-state evidence.
- **Marketing pages were not forced dark.** Dark tokens come from the login wall and a dark-forced public repository, not from a marketing theme toggle.
- **Pricing full shot is capped.** The page is 15997 CSS px tall. [screenshots/pricing-light-full.png](screenshots/pricing-light-full.png) keeps the first 12000.
- **The businesses menu crop is the left columns.** The right-hand promo card was not fully in frame.
- **Signup was a captcha.** The empty form was never reached. The shot was discarded because it printed a network address.
- **Mona Sans is not shipped.** The tokens name the family.
- **Public names on the homepage ticker and on github/docs are other people's public activity.** They are not this capture's account.

## Fonts

- **Mona Sans** for the display heading and the Pricing nav link. The site serves it. It is licensed and not included.
- **Mona Sans VF** for UI text, body, and the header Sign up pill. Not included.
- **ui-monospace** is the declared mono stack. It was not the painted body.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured. Light from the homepage. Dark from the login wall. |
| Type roles | Captured. Desktop computed size for the home h1, body, nav, and hero button. |
| Spacing | Header pill padding measured (0 12px). Primer base sizes derived at 16px. |
| Radii | Primer 3 / 6 / 12px. Nav link paints 24px. |
| Borders | Primer default, muted, emphasis, and focus. |
| Elevation | Overlay backdrop token captured. Shadow stacks were not tokenised. |
| Motion | Not measured. Reduced motion was not emulated. |
| Button | Header pill, hero signup, and quiet download measured at rest. |
| Link | Nav, menu, and footer links observed. Hover not measured. |
| Text field | Hero email and login username/password measured empty. Search dialog empty. Nothing typed. |
| Text area, checkbox, radio, switch | Not measured. |
| Menu | Products, Developers, Businesses, Resources, and the phone drawer captured. |
| Dialog | Search dialog captured empty. |
| Card | Pricing plan cards captured in the page shots. |
| 404 | Captured. |
| Empty search | Captured. |
| Public repository | `github/docs` captured signed out. Star and Fork not clicked. |
| Themes | Marketing light. Login light and dark. No marketing toggle. |
| Widths | Desktop 1440 and phone 390. Home and pricing at both widths. Phone drawer on the homepage. |
| Login wall | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signup wall | Captcha. Not solved. Shot discarded. |
| Signed-in app | Not captured. |

## Do and don't

- Do use the black header pill and the sampled hero green as two different buttons.
- Do leave login fields empty when you restage this wall.
- Don't click through to signup, Google, Apple, or a passkey from these shots.
- Don't read a colour off a quantised PNG.

## Rebuild

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`build_tokens.py` checks named roles against [raw/measured.json](raw/measured.json). It does not rewrite [tokens.json](tokens.json). `build_style_guide.py` rewrites [style-guide.html](style-guide.html). Neither script touches `catalog.json`.
