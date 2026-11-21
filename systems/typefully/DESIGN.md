---
# Local stand-in. tools/catalog.py design-md needs a catalog.json entry.
# This capture was told not to edit catalog.json, so make design-md was not run.
# Source of truth: tokens.json. Do not treat this file as the generated export.
version: "alpha"
name: "Typefully"
description: "Public marketing site for a social scheduling product. Light only. Signed-in app not captured."
colors:
  primary: "#199af5"
  neutral: "#ffffff"
  surface: "#fcfcfd"
  on-surface: "#000000"
  on-surface-variant: "#5c6d7a"
  outline: "#e6e8ea"
  background-page: "#ffffff"
  background-surface: "#fcfcfd"
  background-raised: "#ffffff"
  background-muted: "#f5f5f5"
  text-primary: "#000000"
  text-secondary: "#354450"
  text-muted: "#5c6d7a"
  text-disabled: "#8d9aa5"
  text-on-accent: "#ffffff"
  text-link: "#199af5"
  border-default: "#e6e8ea"
  border-subtle: "#eef0f1"
  border-focus: "#199af5"
  accent-default: "#199af5"
  accent-hover: "#199af5"
  status-success: "#32ae47"
  status-danger: "#f53d3d"
  status-warning: "#ff9029"
  status-info: "#199af5"
  component-button-background: "#199af5"
  component-button-text: "#ffffff"
typography:
  display:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: 700
    lineHeight: 40px
  body:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  label:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 600
    lineHeight: 18.2px
  nav:
    fontFamily: system-ui
    fontSize: 14.5px
    fontWeight: 400
    lineHeight: 21.75px
rounded:
  xs: 1.59375px
  sm: 3.1875px
  md: 6.39062px
  lg: 9.59375px
  xl: 12px
  button: 9.6px
  card: 12px
  pill: 9999px
spacing:
  1: 4px
  2: 8px
  3: 12px
  4: 16px
  5: 18px
components:
  button:
    backgroundColor: "#199af5"
    textColor: "#ffffff"
    rounded: 9.6px
    height: 32px
---

# Typefully

Public marketing capture, light only. The signed-in app was not reached.

## Overview

Typefully's public site is a white Inter marketing system with one blue accent, `#199af5`. The product app is behind a login dialog. This file is a local stand-in: `make design-md` was not run, because that command reads `catalog.json` and this capture was told not to edit it.

## Colors

Primary is `light.color.accent.default` (`#199af5`). Page is white. Text is black. Muted text is `#5c6d7a`. The outline is `#e6e8ea`. Status colours are declared CSS variables. Warning is the declared orange, not a warning component on screen. Accent hover is the same blue, because hover did not change the primary button.

## Typography

Inter for display, body, and buttons. The nav link uses the system stack at 14.5px. A code stack (Fira Code) is declared and was not measured on a public control, so it is not a type style here.

## Layout

Desktop captures are 1440px wide. Phone captures are 390px CSS wide at 2x. Spacing steps are the paddings that were measured: 4, 8, 12, 16, and 18px. No full spacing scale was declared.

## Elevation & Depth

The secondary plan button carries a soft 1px shadow. Dropdowns declare `--shadow-dropdowns`. Those shadow strings are in `raw/css-vars.json` and are not colour tokens. The homepage dialog is a full-viewport overlay at z-index 1000.

## Shapes

Buttons use 9.6px. The quiet plan button uses 12px. The header CTA and auth buttons are pills. The xs radius is the computed `--radius-xs` at 1440, 1.59375px, not a guessed 2px.

## Components

The primary button is 32px tall, accent fill, white text, 9.6px radius. See [components.md](components.md).

## Do's and Don'ts

Use the accent for one action on a page. Do not invent a dark theme from the neutral ramp. Do not style the signed-in app from the homepage shell illustration. Read values from tokens.json, not from the quantised screenshots.
