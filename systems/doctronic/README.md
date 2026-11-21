# Doctronic AI design reference

A token set and component reference for Doctronic's public site. It was read from **doctronic.ai** on **2026-11-21**, signed out, in headless Chromium at 1440×900 and 390×844. Captured: the home composer, the marketing sidebar, the empty login and signup dialogs, the public chat shell, and representative marketing, legal, and catalog pages.

Doctronic paints a warm paper canvas (`#fdfdf7`) with Fraunces display type and Geist for UI text. The primary action is a blue pill (`#2463eb`). Sign up and the solid controls are near-black (`#0b0b0a`) on that paper. The site declares the roles itself: `--color-surface-canvas`, `--color-accent-bg`, `--color-fg-default`, status backgrounds, and a `--text-*` type ramp. One light theme. No dark theme was offered.

**Boundary:** the signed-in app was not entered. Health record and Appointments redirect to a login wall. That wall asks for an email code or Google, Apple, or Facebook. None of those were used. See [site-tree.md](site-tree.md) and [login-review.json](login-review.json).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from apple-touch-icon.png |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared ramps, type styles, shadows, and measured control sizes. `light` holds the role aliases. No dark set. |
| [DESIGN.md](DESIGN.md) | Short token export. Hand-written because this PR does not edit catalog.json, so `make design-md` was not run. |
| [style-guide.html](style-guide.html) | Renders the roles and a home-composer specimen |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the home, sidebar, chat, and auth dialog combine |
| [site-tree.md](site-tree.md) | Public controls and what each opens |
| [login-review.json](login-review.json) | Empty login and signup walls. Probe is no-form. login-extracted is not-started. |
| [components/crops/](components/crops) | Element crops of the public controls |
| [screenshots/](screenshots) | Page captures, 256-colour PNGs |
| [raw/](raw) | CSS variable dump and computed-style readings |
| [tools/](tools) | Capture scripts and builders |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

[tools/capture/vars.mjs](tools/capture/vars.mjs) opened https://www.doctronic.ai/ and walked every readable stylesheet. It wrote [raw/css-vars.json](raw/css-vars.json): 238 resolved custom properties, including the `--color-*` roles and ramps, `--text-*` shorthands, `--font-*` stacks, and `--shadow-*`. [tools/build_tokens.py](tools/build_tokens.py) copies those declarations into `tokens.json`. A rem in a type shorthand is converted at 16px and labelled Derived.

[tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) read computed styles on the visible controls. Button wrappers are transparent. The painted fill sits on an inner layer: Start chat and Log in with email sample as `#2463eb`, which matches `--color-accent-bg`. Sign up samples as `#0b0b0a`, which matches `--color-solid-bg`. Those fills are tokenised from the declared variables, not from the screenshot.

Screenshots were taken by [tools/capture/public/public.mjs](tools/capture/public/public.mjs) and quantised with [tools/capture/quantize.py](tools/capture/quantize.py).

Nothing was signed into, bought, or submitted. The login and signup dialogs were opened empty. Get Login Code and Get Sign up Code were not clicked. Google, Apple, and Facebook were not clicked. No email was typed.

## What to distrust

- This is the public site. The signed-in chat, health record, appointments, and settings were not reached.
- Button wrappers compute `backgroundColor: transparent`. Read the accent and solid tokens, or the inner painted layer.
- `--color-fg-muted` and several borders are `hsl(from …)` and are stored as declared. They are not flattened to sRGB.
- `--shadow-focus-ring` is `0 0 0 2px #2463eb`. The builder records offset, blur, and spread from the length list. The focus colour is the declared `#2463eb`.
- Screenshots are 256-colour PNGs. Read colours from `tokens.json`.
- A chat suggestion chip navigated to a URL that carries a query token. The token value was not copied into this package.
- No cookie banner appeared, so none was hidden.

## Fonts

Four stacks, all declared:

- **Fraunces** (`--font-display`): the "Hi, I'm Doctronic" display and `--text-display-*` / `--text-italic-*`.
- **Geist** (`--font-sans`): headings, labels, and body.
- **System stack** (`--font-body`): `-apple-system`, SF Pro Text, Segoe UI, Roboto.
- **Geist Mono** (`--font-mono`).

The faces are served by the site as woff2. They are not in this package. The style guide falls back to Georgia and system sans.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured. [tokens.json](tokens.json) `light.*` from declared `--color-*` |
| Type roles | Captured. `core.typography` from `--text-*` |
| Spacing | Not captured as a scale. The site does not declare a spacing ramp. Header height and tap target are in `core.size`. |
| Radii | Partly. Measured pill 32px and CTA 52px in `core.measured`. No declared radius ramp. |
| Borders | Captured. `light.border`, `light.borderStrong` |
| Elevation | Captured. `core.shadow` from `--shadow-xs` through `--shadow-xl` |
| Motion | Not captured. No duration tokens were declared. Pause animations is a control, not a token. |
| Sizing | Partly. Header 72px, tap target 44px, focus ring 2px, measured control heights |
| Layout | Captured at 1440 and 390. [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png) |
| Button | Captured. Login, Sign up, Start chat, Log in with email |
| Icon button | Captured. Sidebar toggle, send |
| Link | Observed in the footer and sidebar. [site-tree.md](site-tree.md) |
| Text field | Captured empty. Hero and chat composers. Not filled. |
| Text area | Same composers. The hero control is a textarea. |
| Select, checkbox, radio, switch | Not present on the captured public pages |
| Tabs | Not present |
| Menu | Captured. Marketing sidebar and its two sections |
| Tooltip | Not captured. The headline trigger did not yield readable tooltip text. |
| Dialog | Captured. Login, signup, anonymous info |
| Toast | Not present |
| Card | Observed. Home composer card in [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| List row | Observed. Sidebar rows |
| Table | Not present |
| Avatar | Observed inside the login dialog artwork. Not a user avatar. |
| Badge | Captured. Anonymous chip and suggestion chips |
| App shell | Captured public shell only. Signed-in shell not captured: login wall |
| Form validation | Not captured. No form was submitted, so no error state was shown. |
| Empty state | Captured. Public chat empty composer |
| Loading, error | Not present, except the 404 at `/for-partners/` |
| Destructive confirmation | Not present |
| Feedback after an action | Not captured. No action was submitted. |
| Search and filtering | Not present on the captured pages |
| List or table | Blog and treatment indexes are link lists, not data tables |
| Onboarding | Not captured. Behind sign-in. |
| Dark theme | Not present |
| Phone width | Captured for home, chat, and the login dialog |

## Do and don't

- **Do set the page on warm paper.** The canvas is `#fdfdf7`, not pure white. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do use one blue for the primary action.** Start chat and Log in with email are `#2463eb`. [components/crops/button-start-chat-default.png](components/crops/button-start-chat-default.png)
- **Do keep Sign up near-black.** The solid control is `#0b0b0a` on the paper. [components/crops/button-signup-default.png](components/crops/button-signup-default.png)
- **Do set the greeting in Fraunces.** The hero is 48px Fraunces. UI labels are Geist. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Don't style the signed-in app from this package.** Health record and appointments stop at the login wall. [screenshots/home-light-login.png](screenshots/home-light-login.png)
- **Don't invent a dark theme.** None was offered.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/doctronic/tools/capture/vars.mjs
python3 systems/doctronic/tools/build_tokens.py
python3 systems/doctronic/tools/build_style_guide.py
```
