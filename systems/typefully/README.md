# Typefully design reference

A token set and component reference for Typefully's public marketing site. It was read from **typefully.com** on **2026-11-21**, signed out, in headless Playwright at 1440 x 900 and 390 x 844. No account was used. Light is the only theme that was captured. The product app (Write, Plan, Analyze, queue, settings) sits behind a login dialog and was not entered.

Typefully paints a white page, Inter, black headlines, and one blue accent (`#199af5`). Plan cards and tools stay quiet: hairline borders, 9.6px and 12px radii, and a pill for the header CTA. The homepage is a marketing dialog over a product-shell illustration that does not receive clicks.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, from `https://typefully.com/icon/apple-icon.png` |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the neutral ramp, accent, type, radius, space, and motion. `light` holds semantic roles and the primary button. No dark set. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Local stand-in in Google's DESIGN.md shape. `make design-md` was not run, because that command needs a catalog entry and this capture was told not to edit `catalog.json`. |
| [style-guide.html](style-guide.html) | One page that renders the light tokens and the main controls. No theme toggle: the site has none that changes resolved variables. |
| [components.md](components.md) | Public controls with measured values as token names, and a Gaps section |
| [patterns.md](patterns.md) | How those controls combine on the marketing pages, the homepage modal, pricing, docs, and phone |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog. Mapped before screenshots. |
| [screenshots/](screenshots) | 60 quantised `{page}-{theme}-{state}.png` captures. Desktop 1440 x 900 at 1x. Phone shots are 390 CSS px at 2x (780 px wide files). |
| [raw/](raw) | [css-vars.json](raw/css-vars.json), [components-computed.json](raw/components-computed.json), [root-computed.json](raw/root-computed.json) |
| [tools/](tools) | Capture kit copied from `tools/kit`, plus Typefully's `shoot.mjs`, `measure.mjs`, `vars.mjs`, and `build_tokens.py` |

## Brief

<!-- brief:start -->

Not generated. `make brief` reads `catalog.json`. This capture was told not to edit that file, so the Brief markers are empty on purpose. Read [Do and don't](#do-and-dont) and [tokens.json](tokens.json) directly.

<!-- brief:end -->

## Health

<!-- health:start -->

Not generated. `make grade` reads `catalog.json` and writes a scorecard snapshot. Neither was run. The package has no catalog entry, so `make check` will report that `systems/typefully` has no catalog entry.

<!-- health:end -->

## How the values were read

CSS custom properties were harvested from the live stylesheets on `https://typefully.com/pricing` with `tools/capture/vars.mjs`. Computed control styles were read in Playwright from the pricing buttons, the header links, and the login dialog's email field, and saved to `raw/components-computed.json`. `tools/build_tokens.py` turns those two files into `tokens.json`. Screenshots were taken with Playwright (`tools/capture/public/shoot.mjs`) and quantised to sRGB 256-colour PNGs. Token colours were not sampled from the PNGs.

A dark class was applied on a probe. It changed 0 resolved custom properties, so no dark set was written. `prefers-color-scheme: dark` painted a dark page background on pricing while `color-scheme` stayed `normal`. That preference check is noted in [site-tree.md](site-tree.md). It is not a second token set.

## What to distrust

The screenshots are quantised. Flat UI colours survive, but do not read a token from a PNG. The homepage shell looks interactive and is not: ancestors have `pointer-events: none`. Accent hover is the same hex as the default, because the measured hover did not change the fill. `light.color.text.disabled` is the `--color-typ-c4` ramp name, not a disabled control. Warning is the declared orange, not an on-screen warning. The pill radius is derived from a computed radius of `3.35544e+07px`. The xs radius is a subpixel computed value at 1440. Jobs screenshots have the contact address painted out. The paint is page white and shortens that sentence. [DESIGN.md](DESIGN.md) is not the catalog generator's output.

## Fonts

Inter is loaded from Google Fonts and used for headlines, buttons, and fields. The token stack falls back to system UI, Helvetica Neue, and Helvetica. Nav links computed to the system stack, not Inter. A Fira Code stack is declared as `--font-code` and was not measured on a public control. Inter's licence is the SIL Open Font License. The package does not vendor the font files.

## Coverage

Captured, light, desktop 1440 and the phone rows marked below.

| Surface | Desktop | Phone |
|---|---|---|
| Home, including login, signup, and the email field | yes | yes, default and full |
| Pricing, social-set menu, one comparison row | yes | default and full. Plan tabs not a separate shot. |
| AI, AI agents, X, LinkedIn, Threads, Bluesky, content ideas, analytics, scheduling, profile | yes, some full-page | AI only |
| Blog index and one post, changelog index and one entry, announcements, academy, shortcuts | yes | blog index |
| Jobs | yes, address painted out | yes, address painted out. Menu icon not opened. |
| Tools index, AI tools index, fake tweet (default, advanced, focused), counter, LinkedIn preview | yes | tools index |
| Glossary index, search focused, one term | yes | index |
| API docs | yes | yes. Search overlay not a separate shot. |
| Not-found (`/login`) | yes | no |

Not captured: the signed-in app, SSO, submitted forms, support.typefully.com articles, Zapier, Notion brand assets, the Chrome Web Store page, changelog pages 3 to 6, and most blog and glossary slugs. Those slugs share the captured templates. The sitemap listed 231 URLs.

## Do and don't

- **Do use one blue accent.** The header pill and the primary plan button are `#199af5` on white. See [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).
- **Do keep plan cards quiet.** The secondary button is white, a 1px `#e6e8ea` border, and a soft shadow. See the Free plan in the same shot.
- **Do treat the homepage shell as illustration.** Write, Plan, and Analyze do not navigate. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Don't invent a dark theme.** The neutral ramp exists. A dark class changed no resolved variable. See [How the values were read](#how-the-values-were-read).
- **Don't style the signed-in app from this package.** Queue, calendar, and settings were behind the login dialog. See [screenshots/home-light-login-dialog.png](screenshots/home-light-login-dialog.png).
- **Don't read colours from the screenshots.** They are 256-colour PNGs. Use [tokens.json](tokens.json).
- **Don't put a contact address back into the jobs shots.** Those pixels were covered. The address is not in this package.

## Rebuild

From the repo root, with `PLAYWRIGHT` pointing at a Playwright `index.mjs`:

```bash
cd systems/typefully
node tools/capture/vars.mjs
node tools/capture/public/measure.mjs
python3 tools/build_tokens.py
```

Screenshots:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/shoot.mjs
python3 tools/capture/quantize.py ~/.design-systems/typefully/raw-shots screenshots
```

`make design-md`, `make brief`, `make grade`, and `make check` need a catalog entry. This package does not add one.

## Registration gap

`catalog.json` and `webapps-manifest.json` were not edited. A later change can register the package. Until then the root catalog table will not list Typefully, and `make check` will fail on the missing entry.
