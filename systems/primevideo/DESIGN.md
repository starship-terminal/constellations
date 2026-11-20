---
# Written by systems/primevideo/tools/write_design_md.py because this capture
# must not edit catalog.json, and make design-md only emits packages that are
# already registered. Regenerate with: python3 tools/write_design_md.py
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "Prime Video"
description: "Signed-out Prime Video. Near-black page, white Amazon Ember, one blue on Join Prime."
colors:
  primary: "#1A98FF"
  neutral: "#00050D"
  surface: "rgba(23, 25, 28, 0.8)"
  on-surface: "#FFFFFF"
  on-surface-variant: "#999999"
  outline: "#66696E"
  page: "#00050D"
  text: "#FFFFFF"
  muted: "#999999"
  accent: "#1A98FF"
  border: "#66696E"
typography:
  display:
    fontFamily: "Amazon Ember"
    fontSize: "50px"
    fontWeight: 700
    lineHeight: 1.12
  heading:
    fontFamily: "Amazon Ember"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: 1.125
  synopsis:
    fontFamily: "Amazon Ember"
    fontSize: "18px"
    fontWeight: 500
    lineHeight: 1.389
  body:
    fontFamily: "Amazon Ember"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.429
  nav:
    fontFamily: "Amazon Ember"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: 1.25
  button:
    fontFamily: "Amazon Ember"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: 1.25
  button-large:
    fontFamily: "Amazon Ember"
    fontSize: "20px"
    fontWeight: 500
    lineHeight: 1.15
  label:
    fontFamily: "Amazon Ember"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.2
rounded:
  control: "8px"
  chip: "180px"
  card: "12px"
  poster: "8px"
  dialog: "24px"
  icon-button: "10000px"
spacing:
  button-pad-y: "8px"
  chip-pad-x: "16px"
  nav-pad-x: "51px"
  search-pad-left: "16px"
---

# Prime Video

Generated from [tokens.json](tokens.json) and [README.md](README.md). This file is not the catalog's `make design-md` output. That command only writes packages registered in catalog.json, and this capture does not edit catalog.json. Take values from [tokens.json](tokens.json). This file holds the dark theme only, with aliases resolved, and no per-value provenance.

## Overview

Captured 2026-11-21, signed out, public web. Themes: dark.

Prime Video's public site is a near-black page, white Amazon Ember, and one blue on Join Prime.

## Colors

Roles are the measured dark set. `primary` is the hover blue `#1A98FF`. The rest-state Join Prime fill is rgba(26, 152, 255, 0.8), which DESIGN.md's primary field does not hold. Read `dark.color.accent.default` in tokens.json for that.

- **primary:** `#1A98FF` from `dark.color.accent.hover`
- **neutral:** `#00050D` from `dark.color.bg.page`
- **surface:** `rgba(23, 25, 28, 0.8)` from `dark.color.bg.card`
- **on-surface:** `#FFFFFF` from `dark.color.text.primary`
- **on-surface-variant:** `#999999` from `dark.color.text.muted`
- **outline:** `#66696E` from `dark.color.border.card`

## Typography

Eight styles from `core.typography`. `fontFamily` is the first family of the stack. The full stack is Amazon Ember, Amazon Arabic Ember, Arial, sans-serif.

## Layout

Spacing from `core.space`: `buttonPadY` 8px, `chipPadX` 16px, `navPadX` 51px, `searchPadLeft` 16px. This is not a full scale.

## Elevation & Depth

Join Prime carries a blue glow. See `dark.shadow.accent` and `dark.shadow.accentHover` in tokens.json. Other measured surfaces had no shadow.

## Shapes

Corner radii from `core.radius`: control 8px, chip 180px, card 12px, poster 8px, dialog 24px, icon button 10000px.

## Components

No `component` token group maps onto DESIGN.md component properties. Measured states and crops are in [components.md](components.md) and [style-guide.html](style-guide.html).

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json).
- Do read [README.md](README.md) before relying on a value.
- Don't read colours off the screenshots. They are 256-colour PNGs.
- Don't copy the logo, posters or the blue into something that ships.
- Don't treat this file as `make design-md` output. It was written because catalog.json was left unchanged.
