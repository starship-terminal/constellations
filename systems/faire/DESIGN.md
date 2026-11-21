---
# Written to the DESIGN.md alpha shape from tokens.json because catalog.json was not edited in this capture. Regenerate with make design-md after the catalog entry exists.
version: "alpha"
name: "Faire"
description: "Wholesale marketplace, public signed-out site: paper page, ink buttons, Nantes display, Graphik UI, 4px control radius, blue focus ring"
colors:
  primary: "#333333"
  neutral: "#fbf8f6"
  surface: "#ffffff"
  on-surface: "#333333"
  on-surface-variant: "#161616"
  outline: "#dadada"
  page: "#fbf8f6"
  ink: "#333333"
  focus: "#275ec5"
typography:
  display:
    fontFamily: "Nantes_fix"
    fontSize: "52px"
    fontWeight: 400
    lineHeight: 1.23
  heading:
    fontFamily: "Nantes_fix"
    fontSize: "38px"
    fontWeight: 400
    lineHeight: 1.32
  ui:
    fontFamily: "Graphik_fix"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: "0.01em"
  body:
    fontFamily: "Graphik"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.25
rounded:
  none: "0px"
  control: "4px"
  pill: "32px"
  full: "999px"
spacing:
  "4": "4px"
  "8": "8px"
  "16": "16px"
  "20": "20px"
  "24": "24px"
components:
  button:
    backgroundColor: "#333333"
    textColor: "#ffffff"
    rounded: "4px"
    height: "40px"
    padding: "16px"
---

## Overview

Faire's public site, signed out, captured 2026-11-21. Values are in [tokens.json](tokens.json). This file is a flat export.

## Colors

Page is #fbf8f6. Surfaces, the header, the menu, and the sign-in dialog are #ffffff. Ink is #333333. The primary button darkens to #000000 on hover. Focus is #275ec5.

## Typography

Display is Nantes at 52px. UI is Graphik at 14px with 0.15px tracking. Both families are proprietary. The style guide uses fallbacks.

## Layout

Desktop captures are 1440 wide. Phone captures are 390 wide. The header is 108px tall at 1440. The sign-in dialog is 420px wide.

## Elevation

The categories menu and the sign-in dialog computed to no box-shadow. Elevation is not a token on this surface.

## Motion

Not captured. Durations were not read from a running transition.

## Do's and Don'ts

Use one ink for the primary button. Keep the display in the serif and the UI in Graphik. Do not invent a dark theme. The public site did not show one.
