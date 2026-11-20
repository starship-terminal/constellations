# Wiza design reference

A token set for Wiza's public marketing site, read from **wiza.co** on **2026-11-19**, signed out, in the T3 preview browser. Desktop CSS viewport was **1440 x 900** and the phone pass was **390 x 844**, both at devicePixelRatio 2 and visualViewport scale 1. Captured surfaces: the home, `/pricing`, `/enterprise`, `/customers`, `/privacy`, `/blog/`, `/auth/login` (measured, not submitted), and a made-up route that renders the product 404. The marketing site is Webflow and paints **one theme**. There is no theme control.

The marketing stylesheet declares **154 custom properties** on `:root`: a brand and light swatch scale, a radius scale, a fluid type scale, and a fluid spacing scale. Those declarations are the token layer. Painted buttons, cards, and fields were read from computed style and stored beside them. The login app is a separate PrimeVue and Tailwind surface (Inter var, 6px controls, `#7e43ff` submit). Its values are recorded as measured auth components, not as a second marketing theme.

**Boundaries.** Log in was opened and measured. Nothing was typed and the form was not submitted. "Log in via Google" was not clicked. `/auth/signup` returned a Cloudflare "Just a moment..." page and was not driven. Book-a-demo, contact sales, and checkout were not opened. No phone number, card, or company SSO was entered. The home "Work email" field was not filled.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | The apple-touch icon from the marketing site, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared swatches, radii, spacing ends, and type. `light` holds the resolved theme roles and the painted components. |
| [DESIGN.md](DESIGN.md) | Generated from the tokens and this README. |
| [style-guide.html](style-guide.html) | A page that renders the swatches and a drawn hero, pricing row, and login card from the tokens. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | `crops/` is empty. No element screenshot was saved. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Empty. The preview browser did not produce screenshot frames. |
| [raw/](raw/) | `css-vars.json` and `components.json`, the readings the tokens were built from. |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, the style-guide template, and `test_tokens.py`. |

## How the values were read

Computed style and the `:root` custom properties were read with `preview_evaluate` on the live page. The Webflow sheet is `wiza-dev.webflow.shared.5a7165800.min.css`. Colour tokens are the declared hex, or the computed `rgb()` converted to hex. Radius, type, and spacing tokens are the declared rem values, or the computed pixel size when that is what the page paints (the home h1 is 64px at 1440). Fluid clamps are stored as the desktop end of the clamp. The full clamp text is in [raw/css-vars.json](raw/css-vars.json).

At 390px the h1 token computed to 49.2727px and `--site--margin` computed to 18.5391px. The menu button is 40 by 37.

## What to distrust

- **No screenshots.** The preview browser returned "The browser is not producing screenshot frames". Coverage is computed style, not a picture of the page.
- **Hover, focus, and pressed states were not read.** Do not invent them from the 0.45s transition declaration.
- **The h1 computed color is transparent.** The visible purple is on the animation wrap (`#231645` plus a gradient). Use `light.color.ink` for body text and `light.color.heroGround` for that wrap.
- **`--_theme---button-primary--background` is `#7e43ff`.** The painted home primary button is `#26114a`. Both are recorded. The painted button is `light.component.buttonPrimary`.
- **The blog is a different theme.** Work Sans and a `#ffacac` chip. It does not use the marketing swatches.
- **Login is a different system.** Inter var and 6px radius. It is not the marketing button.
- **Signup was a Cloudflare challenge.** It was not measured.
- **Britti Sans and Inter files are not shipped.** The tokens name the families.
- **Type line heights are hand entries.** raw/ holds the declared font-size clamps and line-height steps, not each style's computed line height or tracking. Each `core.typography` step's line height applies the declared steps by hand (headings at 1, text at 1.3 or 1.5); `display` is 80px/80px. `textXsmall` is the exception: its 16px line height is the computed value on the pricing tag and price note, not a declared step, and raw/ does not hold that reading either. No step carries a letterSpacing. The `-0.03em` tracking token is under `core.$extensions.notTokenised`. `light.color.heroGround`, `core.layout.contentMax` and `core.font.family.auth` were read but not saved, and are labelled Reconstruction.

## Fonts

- **Britti Sans** (weight 500) for marketing headings. The site serves a woff2. It is licensed and not included. Fallback in the token is Arial, sans-serif.
- **Inter** (400 and 500) for marketing UI and body. woff2, not shipped. Fallback Arial, sans-serif.
- **Inter var** on `/auth/login` only, with the system UI stack.
- **Work Sans** on `/blog/` only.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from `:root` swatches and computed text, button, card, and field colours. One theme. |
| Type roles | Captured. Desktop computed sizes for h1, h2, pricing titles, and body. Phone h1 size recorded. |
| Spacing | Declared fluid scale, desktop ends tokenised. Phone margin computed. |
| Radii | Declared scale plus painted 8, 10, 14, 16, 24, 28, 40, and 56px. |
| Borders | `--border-width--main` is 0.094rem. Painted fields use 1px. |
| Elevation | Button and field box-shadows were read and are described in the raw component notes. They are not a separate elevation scale. |
| Motion | Button and field transitions declare 0.45s. Reduced motion was not emulated. |
| Button | Default primary and secondary measured. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav, footer, and prose links measured at rest. |
| Text field | Home work-email field and login email field measured at rest. Nothing typed. |
| Text area, select, checkbox, radio, switch | Not present on the measured pages. |
| Tabs, menu, tooltip, dialog, toast | Nav dropdowns and the phone menu were not opened. |
| Card | Problem, pricing, customer, feature, and testimonial cards measured. |
| Badge | Pricing "Unlimited" tag and the rating pill measured. |
| Avatar, list row, table | Not present. |
| Pricing pattern | Annual state measured. Monthly state not opened. Checkout not entered. |
| 404 | Measured. |
| Themes | Light only. No dark theme on the public site. |
| Widths | 1440 and 390 measured for type and the menu button. Screenshots of neither were saved. |

## Do and don't

1. **Do paint marketing text in brand ink.** Body, headings, and nav use `#26114a` (`light.color.ink`).
2. **Do use the filled primary for the main action.** "Get started for free" is `#26114a` with white text, 8px radius, 36px tall.
3. **Do keep secondary actions white.** "Log in" and "Get a demo" are white buttons with the same radius and the brand ink.
4. **Do set headings in Britti Sans 500.** The home h1 is 64px at 1440 with a 1 line height. Body is Inter.
5. **Do use the declared radius scale.** Section bands are 56px (`--radius--section`). Cards sit between 14px and 16px. Pills use a full radius.
6. **Do treat the hero as a gradient, not a flat page colour.** The page background is transparent over the lavender hero gradient.
7. **Don't style the app from the marketing buttons.** Login uses `#7e43ff`, 6px radius, and Inter var.
8. **Don't invent a dark theme.** None was on the public site.
9. **Don't follow signup, demo, or checkout from this package.** Those flows were not entered.
10. **Don't ship Britti Sans or the wordmark.** The tokens name the family. The font file and the logo SVG stay on the site.

## Health

<!-- health:start. Generated by tools/health.py from the newest scorecard snapshot; `make grade` rewrites it. Do not edit. -->

Not graded yet: no scorecard snapshot reviews this package. Review it against [scorecard/criteria.json](../../scorecard/criteria.json) in the wording for its platform (`python3 tools/grade.py --criteria wiza` prints it) and merge the grades with `python3 tools/grade.py --write --review wiza=<grades.json>`.

Layout: every standard part is here and in the file table ([docs/PACKAGE.md](../../docs/PACKAGE.md)).

<!-- health:end -->

## Rebuild

```bash
cd systems/wiza
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/test_tokens.py
```

## Brief

<!-- brief:start. Generated by tools/brief.py from catalog.json, the tokens file and this README; `make brief` rewrites it. Do not edit. -->

Read this before designing in this style. Take every value from [tokens.json](tokens.json), never from the screenshots; `python3 tools/catalog.py export wiza` prints them all with aliases resolved.

### Principles

1. Do paint marketing text in brand ink.
2. Do use the filled primary for the main action.
3. Do keep secondary actions white.
4. Do set headings in Britti Sans 500.
5. Do use the declared radius scale.
6. Do treat the hero as a gradient, not a flat page colour.
7. Don't style the app from the marketing buttons.
8. Don't invent a dark theme.
9. Don't follow signup, demo, or checkout from this package.
10. Don't ship Britti Sans or the wordmark.

Each rule links the screenshot or crop that shows it, under [Do and don't](#do-and-dont).

### Using tokens

| Role | light |
|---|---|
| page | #ffffff `light.color.page` |
| surface | #ffffff `light.component.pricingCardFeatured.background` |
| text | #26114a `light.color.ink` |
| muted | #615e6e `light.color.muted` |
| accent | #7e43ff `light.color.accent` |
| border | #26114a `light.color.ink` |

Fonts: `core.font.family.display` is Britti Sans, then 2 fallbacks; `core.font.family.body` is Inter, then 2 fallbacks. Scales, counted as [DESIGN.md](DESIGN.md) holds them: 12 type styles (`core.typography`), 11 radius steps (`core.radius`), 14 spacing steps (`core.spacing`).

### Using components

Read [components.md](components.md) for the component inventory; [patterns.md](patterns.md) for how components combine into screens; 0 element crops in [components/crops/](components/crops); [style-guide.html](style-guide.html), which renders every token and the main components.

### Accessibility

| Theme | text on page | text on surface | muted on page | muted on surface |
|---|---|---|---|---|
| light | 16.64:1 pass | 16.64:1 pass | 6.29:1 pass | 6.29:1 pass |

4 of 4 pairs pass 4.5:1 (WCAG AA for body text), the pairs the scorecard's F15 check grades. Focus tokens: `core.focus.width` 0.125rem; `core.focus.offsetInner` -0.125rem; `core.focus.offsetOuter` 0.1875rem.

<!-- brief:end -->
