# Luma AI design reference

A token set and component reference for Luma AI's public marketing site, lumalabs.ai. Captured 2026-11-21, signed out, in headless Playwright at 1440×900 and 390×844. The site loaded. The signed-in app did not: Sign In and Try for free redirect to `https://auth.lumalabs.ai/sign-up`. That URL was recorded and the branch stopped. No password, email code, Google, Apple, or form was submitted.

The marketing pages paint a white page and black type, with black hero bands and white pill buttons. The stylesheet also declares a `.dark` set. No public control applied it, so the dark tokens are from CSS and the screenshots are the light pages.

The control map is [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site favicon, 128 px PNG, from `/favicons/favicon-black.ico` |
| [tokens.json](tokens.json) | DTCG tokens: `core`, `light`, `dark`. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated export. One theme, no provenance. Take values from tokens.json |
| [style-guide.html](style-guide.html) | Renders the colour roles, the shell, and the hero button |
| [components.md](components.md) | Checklist inventory and gaps |
| [patterns.md](patterns.md) | Shell, hero, pricing, FAQ, form, list |
| [screenshots/](screenshots) | 105 captures, `{page}-light-{state}.png` and `mobile-*`, plus `.capture.json` sidecars |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall |
| [raw/](raw) | Resolved CSS colours and measured component styles |
| [icons/](icons) | Index only. Icons were not extracted as assets |
| [tools/](tools) | Builders and the adapted capture kit |

## Brief

<!-- brief:start -->
Brief is not generated. This capture does not edit catalog.json, and `make brief` reads the catalog. Swatches below are the token paths a catalog preview would use.

| Role | light | dark |
|---|---|---|
| page | #ffffff `light.page` | #000000 `dark.page` |
| surface | #f2f2f2 `light.surface` | #1f1f1f `dark.surface` |
| text | #000000 `light.text` | #ffffff `dark.text` |
| muted | #737373 `light.muted` | #8c8c8c `dark.muted` |
| accent | #000000 `light.accent` | #ffffff `dark.accent` |
| border | #e5e5e5 `light.border` | rgba(245, 255, 255, 0.102) `dark.border` |

<!-- brief:end -->

## Health

<!-- health:start -->
Not graded. `make grade` rewrites Health from the catalog, and this capture does not edit catalog.json.

<!-- health:end -->

## How the values were read

`public.mjs` loaded each public route in headless Chromium. Desktop viewport 1440×900 at 1x. Phone viewport 390×844 at 2x. Sidecars record `innerWidth` and `devicePixelRatio`.

Colour roles come from the Next.js stylesheet `https://lumalabs.ai/_next/static/css/b45ed3abd985d8e0.css`. Semantic names on `.light,:root` and `.dark` are HSL triplets. Shadcn roles (`--border`, `--destructive`, `--muted`) are oklch. Both were resolved by painting the computed value onto a 1×1 canvas in Chromium, then reading sRGB. The dump is [raw/css-vars.json](raw/css-vars.json).

Control sizes come from `getComputedStyle` on the home Sign In link, the Try for free link, and the h1. Hover and focus-visible were forced with the Chrome DevTools protocol. Those readings are [raw/component-tokens.json](raw/component-tokens.json).

`build_tokens.py` writes [tokens.json](tokens.json). `build_style_guide.py` writes [style-guide.html](style-guide.html).

## What to distrust

- Dark screenshots were not taken on a live `.dark` page. The dark tokens are the declared CSS set, resolved in a probe. The public pages paint light.
- `--border` in dark resolved to `rgba(245, 255, 255, 0.102)`. The green channel is what the canvas returned from `oklch(100% 0 0 / 0.1)`. Treat the alpha as the measured part.
- Graphik and PP Editorial are commercial faces. The package names them and does not ship the files. The measured h1 used Graphik, not PP Editorial. PP Editorial was declared and unloaded.
- Pill radius is stored as `9999px`. The computed value was a very large pixel radius, which is how the site paints a full pill.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- The news index is taller than the tile cap on the phone capture. [mobile-news-light-full.png](screenshots/mobile-news-light-full.png) is the first 56000px.
- Career rows name published job locations. Those are the product's own listings. No email, phone, or street address was written into the package.

## Fonts

- Graphik (400, 500, 600) is the UI face, loaded as `__graphik_7126cf`. Commercial. The guide falls back to the system sans stack.
- PP Editorial is declared as `--font-pp-editorial` and did not load on the home capture. Not used for measured headings.
- Mono is the stylesheet's `--font-mono` system stack.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.*` from `--surface-*`, `--primary`, `--secondary`, `--border` |
| Dark theme | captured as CSS, not as a live page | `dark.*`. No public control applied `.dark` |
| Type | captured | Graphik. Display 52/500/62.4. Body 16/400/24 |
| Spacing, radii | captured | `--spacing` .25rem, `--radius-*`, pill from the Sign In control |
| Elevation | not present | Computed shadows on the measured controls were `none` |
| Motion | captured | `--default-transition-duration` .15s, accordion .2s |
| Button | captured | Sign In and Try for free. Hover and focus measured |
| Icon button | captured | Submit prompt, social icons, in screenshots |
| Link | captured | Nav links |
| Text field | captured | Home prompt. Not submitted |
| Text area | captured | Sales forms. Not filled |
| Select | not captured open | Enterprise selects exist. The listbox did not open from the hero |
| Checkbox, radio, switch | not present | |
| Tabs | captured | Monthly/Yearly, Ray3.2/Uni-1.1 |
| Menu | captured | Phone nav sheet |
| Tooltip, toast, dialog, avatar | not present | FAQ expands in place |
| Card | captured | Pricing plans |
| List row | captured | Careers |
| Table | captured | Subprocessors page |
| Badge | captured | Top banner |
| App shell | captured | Desktop nav and phone sheet |
| Form with validation | not captured | Forms are public and were not submitted |
| Empty, loading, error | not captured | Behind the account wall |
| Destructive confirmation | not present | |
| Search and filter | captured | Careers department filter, case-study Agency chip, learning-center search field (not filled) |
| Onboarding | not captured | Signup wall |
| Desktop 1440 and phone 390 | captured | Sidecars record the measured viewport |
| Signed-in app | not captured | `https://auth.lumalabs.ai/sign-up` |

## Do and don't

- **Do invert the pill.** On a black hero the button is white. On a white page it is black. [home-light-default.png](screenshots/home-light-default.png), [pricing-light-default.png](screenshots/pricing-light-default.png).
- **Do set display type in Graphik at 52px, weight 500, tight tracking.** The home headline is that recipe.
- **Do keep the nav to one row of uppercase links.** No desktop menu. [home-light-default.png](screenshots/home-light-default.png).
- **Don't invent a second accent hue.** The brand accent on these pages is black or white.
- **Don't treat the dark tokens as a live theme.** They are the stylesheet's `.dark` block. The captures are light.
- **Don't follow Sign In.** It is an account wall. [site-tree.md](site-tree.md).

## Rebuild

```bash
cd systems/lumalabs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Screenshots were captured with:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/lumalabs/raw-shots
```
