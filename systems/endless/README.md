# Endless design reference

A token set and component reference for Endless, the team AI workspace, captured from the public signed-out site. [https://endless.io](https://endless.io) redirects to [https://endless.app/](https://endless.app/). Captured 2026-11-21 in headless Chromium at 1440 and 390, light and dark.

The site is a near-white page (`#fcfcfc`) with near-black ink (`#0a0a0a`), 8px filled buttons, and a sky accent (`#11a8ff` declared, `#01bcff` computed from `--accent`). TikTok Sans sets the UI. Dark is a real theme: the footer control cycles system, light, and dark, and dark paints a black page with a white filled button.

Signed-in app paths were not entered. The sign-in page was photographed and left unsubmitted.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | W3C DTCG tokens: `core`, `light`, `dark`. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Not generated. `make design-md` reads [catalog.json](../../catalog.json), and this capture was told not to edit that file. |
| [style-guide.html](style-guide.html) | Renders the token roles and the main controls. Theme toggle switches `data-mode`. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the marketing shell, composer, pricing, docs, and sign-in page are built. |
| [site-tree.md](site-tree.md) | Public page and control map. |
| [components/crops/](components/crops) | Element crops from the full-colour captures. |
| [screenshots/](screenshots) | 256-colour page captures, `{page}-{theme}-{state}.png`. Phone shots are prefixed `mobile-`. |
| [raw/](raw) | CSS variables, computed styles, and [raw/site-tree.json](raw/site-tree.json). |
| [tools/](tools) | Builders and the capture kit copy. |

## Brief

Not generated. `make brief` reads the catalog entry, which this capture does not add.

## Health

Not generated. `make grade` writes Health from the scorecard and the catalog.

## How the values were read

Custom properties were read from `:root` after the footer theme control was set to light, then to dark. Computed styles were read on the header Sign up button, the home heading, the prompt chip, the composer, and the sign-in email field. CSS `lab()` values were converted with the CSS Color 4 Lab to sRGB path and checked against flat pixels in the full-colour captures: page `#fcfcfc`, ink `#0a0a0a`.

## What to distrust

- `--accent` converts to `#01bcff`. The declared landing action is `#11a8ff`. Hero artwork pixels nearby read about `#21aeed`. The token keeps the computed accent and the declared landing colour as two values.
- Dark border is `lab(100% 0 0 / 0.1)`, stored as `rgba(255, 255, 255, 0.1)`.
- Spacing steps of 4px and 8px are derived from the measured 8px radius and 32px control, not from a published space scale.
- Screenshots are 256-colour. Read colours from tokens.json.
- The home composer is a marketing demo, not the signed-in app.
- Sign-in shows published testimonial names. Those are product content. No account email was typed.

## Fonts

TikTok Sans is the UI face (`--font-sans`). Geist Mono is the mono face. Both are named from computed styles. Neither file is in this package. The guide falls back to system-ui and ui-monospace.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light` and `dark` semantic sets |
| Dark theme | captured | Footer theme control, `home-dark-default.png` |
| Type | captured | `core.typography` display, body, label, caption |
| Radius | captured | `core.radius` from `--radius-*` and the Sign up button |
| Buttons, links, fields, text area, tabs, menu, dialog, card | captured | [components.md](components.md) |
| Checkbox, radio, switch, tooltip, toast, table, avatar | not present | not on the public pages opened |
| Hover and focus | captured | Sign up hover and focus, email focus |
| Disabled, loading, error, validation | not captured | forms were not submitted |
| Signed-in app, checkout, paywall | not captured | stopped at [https://endless.app/sign-in](https://endless.app/sign-in) |
| Phone 390 | captured | `mobile-home-light-menu.png` and the other `mobile-*` shots |
| Docs principles or voice guide | not present | docs are product guides, not a design-system site |

## Do and don't

- Do set text in near-black on the near-white page. [screenshots/home-light-default.png](screenshots/home-light-default.png).
- Do use one filled button for the primary action and leave Sign in quiet. [screenshots/home-light-default.png](screenshots/home-light-default.png).
- Do keep corners at 8px on header buttons and 12px on chips. [components.md](components.md).
- Do switch the whole page when the theme control moves to dark. [screenshots/home-dark-default.png](screenshots/home-dark-default.png).
- Don't treat the home composer as the signed-in product. The model chip opens a sign-up gate. [screenshots/home-light-model-gate.png](screenshots/home-light-model-gate.png).
- Don't submit the sign-in form to capture more states. [screenshots/signin-light-default.png](screenshots/signin-light-default.png).

## Rebuild

```bash
cd systems/endless
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`build_components_md.py` is the public kit copy and was not adapted to this site's measurements. components.md was written from the capture notes.

Full-colour captures stay outside the repo at `~/.design-systems/endless/raw-shots/`.
