---
# Written for this capture because catalog.json was not edited, so make design-md cannot see the package.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "Epidemic Sound"
description: "Public music licensing site: off-white page, black pill buttons, Sebenta display, Inter UI."
omitted:
  - section: "components"
    reason: "tokens.json has no component group"
colors:
  primary: "#000000"
  neutral: "#f1f0eb"
  surface: "#ffffff"
  on-surface: "#000000"
  on-surface-variant: "rgba(0, 0, 0, 0.6)"
  outline: "#000000"
typography:
  display:
    fontFamily: "Sebenta"
    fontSize: "80px"
    fontWeight: 500
    lineHeight: "80px"
  heading:
    fontFamily: "Sebenta"
    fontSize: "64px"
    fontWeight: 500
    lineHeight: "64px"
  body:
    fontFamily: "Inter"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "16px"
  button-s:
    fontFamily: "Inter"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: "24px"
  button-m:
    fontFamily: "Inter"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: "24px"
rounded:
  none: "0px"
  medium: "4px"
  large: "8px"
  pill: "10000px"
spacing:
  button-s-x: "16px"
  button-s-y: "4px"
  button-m-x: "24px"
  nav-x: "16px"
---

# Epidemic Sound

Public signed-out marketing site. Values are in [tokens.json](tokens.json).

## Overview

Off-white page, black text, black pill buttons, Sebenta for display, Inter for UI.

## Colors

Page `#f1f0eb`, surface `#ffffff`, text `#000000`, muted `rgba(0, 0, 0, 0.6)`, primary action `#000000`.

## Typography

Display is Sebenta 80/500. Body is Inter 16/400. Buttons are Inter 14/600 and 16/600.

## Layout

Desktop header is 100px at 1440. Phone width captured at 390. Content uses a centered hero and a card row.

## Elevation

Public controls have no shadow. The nav panel is a white surface on the page.

## Shapes

Public buttons are pills (`10000px`). The product token `--es-radius-button` is 0 until `.radii-override`.

## Components

Primary and secondary buttons, nav menu, pricing segment, billing switch, search field, plan card. See [components.md](components.md).

## Do's and Don'ts

Use the light marketing values. Do not treat the declared dark `--es-color-*` set as the page theme. Do not follow login or checkout.
