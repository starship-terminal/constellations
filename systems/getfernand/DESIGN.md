---
# Hand-written because catalog.json was not edited, so `make design-md` cannot emit this file.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
# A later registration can regenerate this file. Until then, do not treat it as a catalog export.
version: "alpha"
name: "Fernand"
description: "Public light marketing site for a SaaS helpdesk. Accent #00a0ff, white page, Inter, 6px controls. Signed-in app not captured."
omitted:
  - section: "typography"
    reason: "tokens.json has no typography tokens under `core.typography`. Faces and sizes are in README.md and raw/components-computed.json."
  - section: "components"
    reason: "tokens.json light.component tokens are named button-height and hero-size. DESIGN.md only maps a last word of bg, text, radius, padding, height, width, or size, so these names do not fill a component entry. The measured values stay in tokens.json."
colors:
  primary: "#00a0ff"
  neutral: "#ffffff"
  surface: "#f4f5f7"
  on-surface: "#1a2035"
  on-surface-variant: "#6f7b96"
  outline: "#eaecf8"
  page: "#ffffff"
  text: "#1a2035"
  muted: "#6f7b96"
  accent: "#00a0ff"
  accentText: "#ffffff"
  ink: "#131e40"
  border: "#eaecf8"
  focus: "#3b84d8"
  grey: "#9fa3b5"
  grey-medium: "#717583"
  grey-strong: "#3d4259"
  blue-pale: "#e8f5ff"
  orange: "#fb8c3b"
  red: "#dc2626"
  red-pale: "#fee2e2"
  green: "#2dbd33"
  green-dark: "#33c27f"
  border-strong: "#e4e6eb"
rounded:
  control: "6px"
spacing:
  control-pad-y: "8px"
  control-pad-x: "12px"
---

# Fernand

This file was written by hand from [tokens.json](tokens.json) and [README.md](README.md). `make design-md` did not run, because catalog.json was not edited and the generator needs a catalog entry. Tokens stay the source of truth. After registration, regenerate this file and discard the hand-written copy if the generator disagrees.

It follows the DESIGN.md spec, version alpha. That format has no themes, no per-value provenance, and only px, em, and rem units, so this file holds the light theme alone with every alias resolved. There is no dark token set. The marketing page stays light.

## Overview

Good for: a public light SaaS marketing page with one blue accent, a white ground, and quiet secondary controls.

Captured 2026-11-21, signed out. Themes: light.

Public marketing capture of Fernand, the customer support platform at [https://getfernand.com/](https://getfernand.com/). Read on 2026-11-21, signed out, in headless Chromium. Desktop measured 1440x900. Phone measured 390x844 at device pixel ratio 2. One painted theme: light.

The signed-in app was not captured. Log in opens [https://app.getfernand.com/auth/login](https://app.getfernand.com/auth/login) and asks for a work email and a password. No code was sent. The walk stopped there. [https://getfernand.com/login](https://getfernand.com/login) is a 404.

## Colors

The roles below match the catalog swatch names for a light theme. Values are the resolved light tokens. `primary` is `light.accent`. `neutral` is `light.page`. `surface` is `light.surface`. `on-surface` is `light.text`. `on-surface-variant` is `light.muted`. `outline` is `light.border`.

- **primary (#00a0ff):** `light.accent`, alias of `core.color.blue`
- **neutral (#ffffff):** `light.page`
- **surface (#f4f5f7):** `light.surface`, alias of `core.color.grey-light`
- **on-surface (#1a2035):** `light.text`, measured on the homepage h1
- **on-surface-variant (#6f7b96):** `light.muted`, measured on nav links
- **outline (#eaecf8):** `light.border`, alias of `core.color.border`

`light.focus` is `#3b84d8`. That is Chromium's focus outline on Start for free, not a designed ring. Status colours (`green`, `orange`, `red`) are declared CSS variables. They were not seen as status chips on the captured homepage.

### What to distrust (from README.md)

- One theme. The marketing page stays light. The widget preview has Light and Dark buttons. Those restyle the illustration, not the page.
- WordPress preset colours are not Fernand's palette.
- Focus colour `#3b84d8` is Chromium's outline on the primary link, not a designed ring.
- Hover on "Start for free" did not change the computed background.
- The signed-in inbox, settings, and onboarding were not opened. Those token values are Not captured.
- Screenshots are 256-colour PNGs.

## Typography

No composite type styles in tokens.json. The face is Inter, then system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial. Read from `getComputedStyle(body)`. The webfont file is not in the package.

Measured sizes, from [raw/components-computed.json](raw/components-computed.json): Start for free is 14px, weight 500, line-height 14px. The homepage h1 is 38px with a 48px line-height, weight 400, colour `#1a2035`.

## Layout

Spacing from `core.space`: `control-pad-y` 8px, `control-pad-x` 12px. Those are the Start for free padding. There is no spacing scale token on the site.

The header is a single row. On a 390px phone the header shows the wordmark, About us, Pricing, Log in, and Start for free. There is no menu button. Book a demo sits in the hero at that width.

## Elevation & Depth

No shadow tokens were captured. Start for free has `box-shadow: none`. Book a demo paints this computed shadow, recorded in [raw/components-computed.json](raw/components-computed.json), not as a token:

`rgba(18, 55, 105, 0.08) 0px 2px 4px 0px, rgba(18, 55, 105, 0.04) 0px 1px 1px 0px, rgba(18, 55, 105, 0.08) 0px 0px 0px 1px`

See [style-guide.html](style-guide.html).

## Shapes

Corner radii from `core.radius`: `control` 6px. That is the Start for free and Book a demo radius.

## Components

No component tokens map onto DESIGN.md's component properties. The measured control is still in tokens.json as `light.component.button-height` 30px, `button-radius` 6px, and `button-font-size` 14px.

Measured states, crops, and the inventory: [components.md](components.md), [components/crops/](components/crops/), [style-guide.html](style-guide.html).

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json) when you need a value's source, or a token this file leaves out.
- Do read [README.md](README.md) before relying on a value. It says what is known to be wrong.
- Don't read colours off the screenshots. They are 256-colour PNGs.
- Don't copy the product's logo, icons, illustrations, or brand colours into something that ships. Borrow structure and proportions.
- Don't invent a dark marketing theme from the widget preview's Dark button.
- Don't treat this file as the output of `make design-md`. catalog.json was excluded from this capture.

### Do and don't (from README.md)

1. **Use one blue accent.** Start for free is `#00a0ff` on white. See [screenshots/desk-home-default.png](screenshots/desk-home-default.png).
2. **Keep secondary actions quiet.** Book a demo is a white control with a hairline shadow, not a second blue. See [screenshots/desk-home-default.png](screenshots/desk-home-default.png).
3. **Stay on one light page.** Do not invent a dark marketing theme from the widget preview's Dark button. See [screenshots/desk-home-default.png](screenshots/desk-home-default.png).
