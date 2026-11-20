# Squarespace

Generated from [tokens.json](tokens.json) and [README.md](README.md) by the package builder, because this capture is not allowed to edit catalog.json. `make design-md` is the canonical generator and needs a catalog entry. Until that entry exists, this file is the readable export of the light theme. Take values from tokens.json. This file has no per-value provenance.

## Overview

Good for: marketing site with a paper page, a black inverted header and menu, Clarkson light display type, and 60px black primary bars.

Captured 2026-11-21, signed out. Themes: light.

## Colors

The roles are the measured semantic colours. Aliases are resolved.

- **primary (#000000):** `light.accent.default`
- **neutral (#ffffff):** `light.background.page`
- **surface (#ffffff):** `light.background.surface`
- **on-surface (#000000):** `light.text.primary`
- **on-surface-variant (#5a5a5a):** `light.text.muted`
- **outline (#000000):** `light.border.default`

Other measured colours: inverse background `#000000`, overlay `rgba(36, 36, 36, 0.9)`, track `rgba(0, 0, 0, 0.05)`, on-accent `#ffffff`, link and badge text `#0072f0`, badge fill `#e7f2ff`.

## Typography

Clarkson is proprietary and is not loaded. The stack is Clarkson, Helvetica, sans-serif.

- **display:** Clarkson, 64px, weight 300, line height 1.04, letter spacing -0.06em
- **title:** Clarkson, 56px, weight 300, line height 1.08, letter spacing -0.04em
- **subtitle:** Clarkson, 40px, weight 400, line height 1.08, letter spacing -0.04em
- **eyebrow:** Clarkson, 14px, weight 500, line height 1
- **label:** Clarkson, 14px, weight 500, line height 1
- **body:** sans-serif, 16px, weight 400, line height 1.2

## Rounded

- **none:** 0px
- **control:** 4px
- **menu:** 8px
- **badge:** 30px
- **pill:** 120px
- **track:** 1000px

## Spacing

Measured paddings, not a 4px scale: 4px, 8px, 16px, 23px, 28px, 40px.

## Components

Primary button: background `#000000`, text `#ffffff`, height 60px, radius 4px, padding 23px 28px. Inverse button on the dark header: background `#ffffff`, text `#000000`.

## Do's and Don'ts

See [README.md](README.md). Set display type in Clarkson light on paper. Invert the header when a menu opens. Make the primary action a 60px black bar. Keep the secondary action quiet. Mark a discount with the blue wash badge. The black menu is not a dark theme.
