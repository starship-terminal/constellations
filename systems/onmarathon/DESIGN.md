---
# Written by hand for this capture. catalog.json was not edited, so make design-md was not run.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "On Marathon"
description: "Public archive of a former Figma comment tool: a white page, one lime banner, graphik display type, and black pill actions."
colors:
  primary: "#d7fd51"
  neutral: "#ffffff"
  surface: "#ffffff"
  on-surface: "#0b0b0b"
  on-surface-variant: "#717171"
  outline: "#e1e1e1"
  lime: "#d7fd51"
  lime-hover: "#c8ee3a"
  ink: "#0b0b0b"
  ink-muted: "#717171"
  page: "#ffffff"
  muted: "#f2f2f2"
  border: "#e1e1e1"
  destructive: "#d40924"
  on-accent: "#21240c"
  white: "#ffffff"
  button-hover: "#404040"
  focus: "#005fcc"
  accent: "#d7fd51"
  accent-text: "#21240c"
  text: "#0b0b0b"
  link: "#717171"
  button: "#0b0b0b"
typography:
  display:
    fontFamily: "graphik"
    fontSize: "81.4px"
    fontWeight: 500
    lineHeight: 1
  body:
    fontFamily: "Inter"
    fontSize: "17.6px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Inter"
    fontSize: "15.4px"
    fontWeight: 500
    lineHeight: 1.43
  caption:
    fontFamily: "Inter"
    fontSize: "13.2px"
    fontWeight: 500
    lineHeight: 1.33
rounded:
  md: "17.6px"
  pill: "9999px"
spacing:
  "2": "8.8px"
  "3": "13.2px"
  "4": "17.6px"
  "5": "22px"
  "6": "26.4px"
  "10": "44px"
components:
  button:
    height: "39.594px"
    rounded: "9999px"
  banner:
    height: "43.969px"
  header:
    height: "56px"
  plan:
    rounded: "17.6px"
    padding: "44px"
  menu-button:
    size: "39.594px"
  focus:
    width: "1px"
---

# On Marathon

Written by hand from [tokens.json](tokens.json) and [README.md](README.md). catalog.json was not edited, so `make design-md` was not run and this file is not a catalog generation. A later registration should replace this file with the generator's output.

It follows the DESIGN.md spec, version alpha. That format has no themes, no per-value provenance and only px, em and rem units, so this file holds the `light` theme alone with every alias resolved. [tokens.json](tokens.json) is the source of truth: it records where each value was read, and keeps the motion tokens this format cannot hold.

## Overview

Good for: a quiet marketing archive with one lime band, graphik display type, and black pill actions.

Captured 2026-11-21, signed out. Themes: light.

A token set and component reference for the public archive at onmarathon.com. The live site paints one light theme. Sign In and Get Started redirect to the homepage and show no form. The control map is [site-tree.md](site-tree.md).

## Colors

The roles below are the light swatches. The front matter then lists the colour tokens, named by path with dots turned into hyphens.

- **primary (#d7fd51):** `light.accent`, alias of `core.color.lime`. CSS name `--primary`.
- **neutral (#ffffff):** `light.page`
- **surface (#ffffff):** `light.surface`
- **on-surface (#0b0b0b):** `light.text`
- **on-surface-variant (#717171):** `light.muted`
- **outline (#e1e1e1):** `light.border`

The lime paints the archive banner and the Pro plan card. The primary button is ink `#0b0b0b`, and its hover is `#404040`. `--destructive` is declared and not painted on a captured control.

## Typography

4 styles from `core.typography`. `fontFamily` is the first family of each stack. Families: graphik, Inter.

### Fonts (from README.md)

Inter, weights 100 to 900, from the Next font files, with an "Inter Fallback" that maps to Arial. graphik, weights 400 and 500, also from Next font files, used on the display heading. The webfonts are not committed. The guide falls back to system-ui.

## Layout

Spacing from `core.space`: `2` 8.8px, `3` 13.2px, `4` 17.6px, `5` 22px, `6` 26.4px, `10` 44px.

These are measured paddings, not a published scale. The root font size is 110%, so 1rem is 17.6px.

## Elevation & Depth

No shadow tokens were captured. Plan cards and the header have no box-shadow. See [style-guide.html](style-guide.html).

## Shapes

Corner radii from `core.radius`: `md` 17.6px, `pill` 9999px.

## Components

6 component groups from `light.component`, keeping height, radius, padding, width and size. Horizontal padding on the button is in tokens.json and is not a DESIGN.md property name.

Measured states, crops and the full inventory: [components.md](components.md), [style-guide.html](style-guide.html).

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json) when you need a value's source, or a token this file leaves out.
- Do read [README.md](README.md) before relying on a value; it says what is known to be wrong.
- Don't read colours off the screenshots; they are 256-colour PNGs.
- Don't copy the product's logo or brand colours into something that ships. Borrow structure and proportions.
- Don't treat this file as a `make design-md` generation. It was written by hand because catalog.json was left unchanged.

### What to distrust (from README.md)

- **One painted theme.** Screenshots are light. `darkProbe` on a colour token is a forced class, not a page anyone can open from the nav.
- **oklch to hex.** The builder converts oklch the same way the canvas probe did. A later browser can round a chroma colour differently. `#d7fd51`, `#ffffff` and `#404040` were read as sRGB and do not depend on that conversion.
- **Focus ring.** Desktop keyboard focus is Chromium's `#005fcc` auto outline. The phone menu button drew `rgb(229, 151, 0)` in the same browser's mobile context. Neither is a site token.
- **`--destructive` is unused** on the captured pages. It is a declared variable, not a painted state.
- **The demo iframe** was still a spinner in the viewport shot. Do not treat that white card as the scheduler's design.
- **Quantised screenshots.** Read colours from tokens.json, not from `screenshots/`.
- **Wordmark states.** Only the resting wordmark was measured. The first locator matched the banner.

### Do and don't (from README.md)

- **Do keep the page quiet.** The homepage is a letter on a grey-white ground. One black pill is the action. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do use the lime once per band.** The banner and the Pro card share `#d7fd51`. Body sections stay white or grey. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png)
- **Do set display type in graphik at a tight line height.** The h1 is 81.4px on 81.4px. [components/crops/heading-default.png](components/crops/heading-default.png)
- **Don't invent a theme switch.** The live pages are `html.light`. The `.dark` rule is not a screen. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Don't follow Sign In or Get Started into a form.** Both URLs redirect to the archive homepage. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Don't fill the demo embed.** It is a booking form. [screenshots/demo-light-default.png](screenshots/demo-light-default.png)
