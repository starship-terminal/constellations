# Craft Docs public surface

A token set and page captures for Craft's public marketing site at **https://www.craft.do/**. Refreshed **2026-11-22**, signed out, into the existing slug `systems/craft/`. origin/main already had this package for craft.do. `systems/craft-docs` was not created. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 2 (PNG width 780). The site tree is [site-tree.md](site-tree.md).

`catalog.json` was left alone, so `login-extracted` stays `not-started`. This README's Brief and Health are hand-written. [DESIGN.md](DESIGN.md) was hand-written from the measured tokens and was not regenerated.

The marketing site paints **one theme**. `prefers-color-scheme: dark` did not change the body. The login and signup wall is a separate app at docs.craft.do (blue Continue button, Inter, empty email field). There is no separate signup URL.

**Boundary.** The empty wall was photographed and the branch stopped. Nothing was typed. Nothing was submitted. Google, Apple, and Microsoft were not clicked. Continue and continue with SSO were not pressed. The reCAPTCHA was not solved. No document was opened. No installer was started. Monthly pricing was not switched.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup wall. Probe stopped there. login-extracted is not-started. |
| [icon.png](icon.png) | The site icon, 128px, from `/images/favicon-large.png`. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds declared swatches, radii, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches, the nav pill, and the auth Continue button. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | Element crops of the nav, hero, product menu, pricing cards, and the empty auth card. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | The stylesheet readings and the login probe. |
| [tools/](tools/) | `test_tokens.py`. |

## How the values were read

Computed style and the custom properties were read in headless Chromium on the live homepage, then written to [raw/css-vars.json](raw/css-vars.json). 191 custom properties resolved on `:root`. Colour tokens are the declared hex. The homepage h1 size, the nav height, the pill padding, and the auth Continue colour are computed values from the same session. The auth button `#2e6de9` is `rgb(46, 109, 233)` on `https://docs.craft.do/`.

Menus and the phone drawer were opened in the T3 preview browser and again in headless Chromium. Page shots are headless Chromium. They were quantised to 256 colours after the readings were saved.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The sky collage does not. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **Yearly pricing is the painted state.** Monthly was not switched. Prices rendered in SGD for the capture region.
- **Login is a different system.** Continue is `#2e6de9` and the type is Inter. It is not the marketing ink pill.
- **The hero collage is marketing art.** The notes in "Joe's Space" are the site's illustration, not an account.
- **Untitled Sans and Untitled Serif are not shipped.** The tokens name the families.
- **The footer English button did not open a locale dialog** in this capture. Locales were not followed.
- **Full sheets were kept only for home and pricing.** Other pages keep the first viewport.

## Fonts

- **Untitled Sans** for marketing UI, links, and body. The site serves it. It is licensed and not included.
- **Untitled Serif** for display headings and prices. Licensed and not included.
- **Inter** on the docs login wall. Not included.
- **SFMono-Regular** is the declared mono stack. It was not the painted body.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured. Page, card, ink, muted, border, ring, accent, destructive. One theme. Auth button recorded separately. |
| Type roles | Captured. Homepage h1 and body computed. Auth field and button computed. |
| Spacing | CTA padding measured. Declared unit is 0.25rem. |
| Radii | Declared scale plus painted nav, footer, pill, and auth button. |
| Borders | Declared `--border` `#03030217`. Width not isolated beyond the computed 0px on body. |
| Elevation | Nav shadow measured. Declared drop-shadow-2xl recorded. |
| Motion | Declared ping and pulse. Reduced motion was not emulated. |
| Button | Header pill, hero pill, and auth Continue measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Empty email field on the login wall. Nothing typed. |
| Text area, select, checkbox, radio, switch | Not present as public form controls. A hidden captcha checkbox exists and was not used. |
| Tabs | Not present. Billing is a two-pill toggle. Monthly was not selected. |
| Menu | Product and Community menus photographed. Phone drawer photographed. |
| Tooltip, toast | Not present on the measured pages. |
| Dialog | Footer English did not open a dialog. No other dialog was opened. |
| Card | Pricing cards and download cards photographed. |
| List row, table, avatar, badge | Not present as product UI. Testimonial portraits are marketing art. |
| App shell | Public nav and footer captured. Signed-in shell not entered. |
| Empty state | 404 page captured. Login wall is an empty form. |
| Loading, error, destructive confirm | Not present on the public pages. |
| Themes | Light only. Dark preference did not restyle the page. |
| Widths | 1440 and 390 for home, plus 390 for pricing and the login wall. |

## Do and don't

1. **Use ink for the marketing CTA.** The header pill is `#030302` with white type. The teal `--accent` is declared and is not the CTA.
2. **Keep the nav a white pill.** 52px, 26px radius, floating over the collage.
3. **Set display in Untitled Serif and UI in Untitled Sans.** The login wall is Inter. Do not mix them onto the marketing pages.
4. **Leave the auth wall blue.** Continue is `#2e6de9` at 10px radius. It is not an ink pill.
5. **Don't enter the docs app from this package.** The wall was photographed empty and the branch stopped.
6. **Don't ship the typefaces or the wordmark.** The tokens name the families. The font files and the logo stay on the site.

## Health

<!-- health:start -->

Not regraded. This PR does not edit `catalog.json`, so `make grade` cannot attach a new scorecard row. Coverage gaps are in the table above.

Layout: `icons/` holds an index only. No SVG set was lifted. The wordmark and platform glyphs stay in the screenshots.

<!-- health:end -->

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. The catalog entry was not updated, so this Brief is hand-written and `make brief` has not rewritten it.

Home is a warm beige page with a 66px serif headline on a sky collage. The nav is a white pill. The marketing CTA is an ink pill. Pricing cards sit on the same beige. The auth wall is a separate blue Continue button.

<!-- brief:end -->

## Rebuild

```bash
cd systems/craft
python3 tools/test_tokens.py
```

`test_tokens.py` checks the named swatches against [raw/css-vars.json](raw/css-vars.json). It does not rewrite tokens.json.
