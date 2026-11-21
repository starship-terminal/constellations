---
version: "alpha"
name: "Douze"
description: "Spritz storefront: dusk ink on white, sable surfaces, Boogy display, Robin labels, square buttons, pill filters."
colors:
  primary: "#301816"
  neutral: "#ffffff"
  surface: "#f6f2e9"
  on-surface: "#301816"
  on-surface-variant: "#5b5b5b"
  outline: "#321a18"
typography:
  display:
    fontFamily: "Boogy"
    fontSize: "72px"
    fontWeight: 300
    lineHeight: "64.8px"
    letterSpacing: "-0.72px"
  heading2:
    fontFamily: "Boogy"
    fontSize: "52px"
    fontWeight: 300
    lineHeight: "52px"
    letterSpacing: "-0.52px"
  body:
    fontFamily: "Robin Regular"
    fontSize: "16px"
    fontWeight: 500
    lineHeight: "19.2px"
    letterSpacing: "0px"
rounded:
  none: "0px"
  pill: "999px"
  block: "45px"
  blockReduced: "16px"
spacing:
  gutter: "73px"
  buttonX: "15px"
  buttonXWide: "20px"
components:
  button:
    backgroundColor: "#301816"
    textColor: "#ffffff"
    rounded: "0px"
    height: "44px"
  field:
    backgroundColor: "#ffffff"
    textColor: "#301816"
    rounded: "16px"
---

# Douze

Hand-written stand-in. The catalog generator (`make design-md`) needs a catalog.json entry, and this capture must not add one. [tokens.json](tokens.json) is the source of truth. This file has no provenance and no second theme.

When the package is registered, replace this file by running `make design-md`. Do not treat this copy as generated.

## Overview

Good for a warm storefront with one dusk ink, a sable surface, square buttons, and pill filters.

Captured 2026-11-21, signed out. Themes: light.

## Colors

Roles match the light semantic set: accent and text `#301816`, page `#ffffff`, surface `#f6f2e9`, muted `#5b5b5b`, border `#321a18`.

## Typography

Boogy for display. Robin Regular for body. Robin Semibold for nav and buttons (12px, uppercase). Full stacks are in [tokens.json](tokens.json).

## Layout

Spacing tokens are the container gutter and the two button paddings, not a 4px scale.

## Elevation & Depth

No shadow tokens. Add-to-cart focus computed a 4px 8px shadow. That reading is in [raw/measurements.json](raw/measurements.json), not in this file.

## Shapes

Buttons 0px. Filter tabs 999px. Cards and the footer 45px. Reduced block radius 16px.

## Components

Button and field only. Field radius is the computed 16px on the login fields. See [README.md](README.md).

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json).
- Do read [README.md](README.md) before relying on a value.
- Don't read colours off the screenshots. They are 256-colour PNGs.
- Don't edit catalog.json in the capture PR that added this package.
