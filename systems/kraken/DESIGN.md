---
# Generated for this capture from tokens.json and README.md. catalog.json was not edited, so tools/catalog.py did not write this file.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "Kraken"
description: "Public Kraken marketing site: cool grey page, white cards, one purple primary action, brand face for the hero and product face for controls"
colors:
  primary: "#7132f5"
  neutral: "#f6f5f9"
  surface: "#fff"
  on-surface: "#101114"
  on-surface-variant: "#686b82"
  outline: "#686b8229"
  page: "#f6f5f9"
  canvas: "#fff"
  overlay: "#fff"
  sunken: "#9497a914"
  hover: "#686b821f"
  selected: "#855bfb14"
  scrim: "#0006"
  text: "#101114"
  muted: "#686b82"
  dimmed: "#9497a9"
  disabled: "#fff6"
  inverse: "#fff"
  link: "#7132f5"
  accent: "#7132f5"
  accentHover: "#5b1ecf"
  onAccent: "#fff"
  border: "#686b8229"
  borderStrong: "#686b82"
  focus: "#7132f5"
  success: "#08844f"
  successFill: "#149e61"
  successSubtle: "#149e6129"
  warning: "#89640c"
  warningFill: "#ffcd60"
  warningSubtle: "#c396213d"
  danger: "#d11d45"
  dangerFill: "#d11d45"
  dangerSubtle: "#f5395e29"
  info: "#0079b4"
  infoFill: "#0079b4"
  infoSubtle: "#0092d829"
  secondary: "#686b8214"
  secondaryHover: "#686b821f"
  secondaryText: "#484b5e"
typography:
  display1:
    fontFamily: "Kraken-Brand"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: "3.5rem"
  display2:
    fontFamily: "Kraken-Brand"
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: "3rem"
  display3:
    fontFamily: "Kraken-Brand"
    fontSize: "2.25rem"
    fontWeight: 700
    lineHeight: "2.75rem"
  display4:
    fontFamily: "Kraken-Brand"
    fontSize: "2rem"
    fontWeight: 700
    lineHeight: "2.5rem"
  heading1:
    fontFamily: "Kraken-Brand"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: "2rem"
  heading2:
    fontFamily: "Kraken-Brand"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: "1.75rem"
  heading3:
    fontFamily: "Kraken-Brand"
    fontSize: "1.125rem"
    fontWeight: 700
    lineHeight: "1.625rem"
  heading4:
    fontFamily: "Kraken-Brand"
    fontSize: "1rem"
    fontWeight: 700
    lineHeight: "1.375rem"
  heading5:
    fontFamily: "Kraken-Brand"
    fontSize: "1rem"
    fontWeight: 500
    lineHeight: "1.375rem"
  heading6:
    fontFamily: "Kraken-Brand"
    fontSize: "1rem"
    fontWeight: 500
    lineHeight: "1.375rem"
  body1:
    fontFamily: "Kraken-Product"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: "1.375rem"
  body2:
    fontFamily: "Kraken-Product"
    fontSize: ".875rem"
    fontWeight: 400
    lineHeight: "1.25rem"
  body3:
    fontFamily: "Kraken-Product"
    fontSize: ".75rem"
    fontWeight: 400
    lineHeight: "1rem"
  caption1:
    fontFamily: "Kraken-Product"
    fontSize: ".75rem"
    fontWeight: 600
    lineHeight: "1rem"
  caption2:
    fontFamily: "Kraken-Product"
    fontSize: ".625rem"
    fontWeight: 600
    lineHeight: ".875rem"
  label1:
    fontFamily: "Kraken-Product"
    fontSize: "1rem"
    fontWeight: 500
    lineHeight: "1.375rem"
  label2:
    fontFamily: "Kraken-Product"
    fontSize: ".875rem"
    fontWeight: 500
    lineHeight: "1.25rem"
  label3:
    fontFamily: "Kraken-Product"
    fontSize: ".75rem"
    fontWeight: 500
    lineHeight: "1rem"
rounded:
  0: "0px"
  1: "2px"
  2: "4px"
  3: "6px"
  4: "8px"
  5: "12px"
  6: "16px"
  7: "20px"
  8: "32px"
  round: "9999px"
spacing:
  1: "4px"
  2: "8px"
  3: "12px"
  4: "16px"
  5: "24px"
  6: "32px"
---

# Kraken

Generated from tokens.json and README.md for this capture. The catalog generator was not run, because this PR does not edit catalog.json. tokens.json remains the source of truth.

## Overview

Good for: a public marketing site with a cool grey page, white cards, and one purple primary action.

Captured 2026-11-21, public site, signed out. Themes: light (live), dark (declared in CSS, not applied on the public site).

## Colors

- **primary (#7132f5):** `light.accent`
- **neutral (#f6f5f9):** `light.page`
- **surface (#fff):** `light.surface`
- **on-surface (#101114):** `light.text`
- **on-surface-variant (#686b82):** `light.muted`
- **outline (#686b8229):** `light.border`

## Typography

18 styles from `core.typography`. Families: Kraken-Brand, Kraken-Product. Proprietary files are not in this package.

## Layout

Spacing from `core.space`: `1` 4px, `2` 8px, `3` 12px, `4` 16px, `5` 24px, `6` 32px.

## Elevation & Depth

No shadow tokens were captured. Depth comes from the page colour against white cards.

## Shapes

Corner radii from `core.radius`: `0` 0px, `1` 2px, `2` 4px, `3` 6px, `4` 8px, `5` 12px, `6` 16px, `7` 20px, `8` 32px, `round` 9999px.

## Components

No component tokens map onto DESIGN.md's component properties. See components.md and style-guide.html.

## Do's and Don'ts

- Do take values from tokens.json.
- Do read README.md before relying on a dark value. The dark set was declared, not seen live.
- Don't read colours off the screenshots. They are 256-colour PNGs.
- Don't copy the logo or brand purple into something that ships.
