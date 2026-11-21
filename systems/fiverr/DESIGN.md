---
# Written for this blocked capture. catalog.json was not edited, so `make design-md` cannot generate this file.
# Source of truth: tokens.json. Unread roles are omitted rather than invented.
version: "alpha"
name: Fiverr
description: Partial public capture stopped at a human-check and the login wall. Four sampled fills only.
colors:
  primary: "#1dbf73"
  neutral: "#ffffff"
  surface: "#ffffff"
  on-surface: "#222325"
  panel: "#76293b"
typography:
  body:
    fontFamily: system-ui
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.45
rounded: {}
spacing: {}
components: {}
---

# Fiverr

This file is not the catalog generator's output. `make design-md` only writes packages that have a [catalog.json](../../catalog.json) entry, and this capture was told not to edit that file. Take values from [tokens.json](tokens.json).

It holds the light theme only. Muted text, borders, type roles, spacing, and radii were not read, so they are omitted here. They are Not captured in tokens.json.

## Overview

Good for: nothing yet. The signed-in app was not captured, and the public site tree stopped at a human-check.

Captured 2026-11-21, signed out. Themes: light.

## Colors

Sampled from [screenshots/login-light-default.png](screenshots/login-light-default.png):

- **primary (#1dbf73):** wordmark green
- **neutral / surface (#ffffff):** page and sign-in card
- **on-surface (#222325):** Join button fill, used as the text sample
- **panel (#76293b):** login left panel

Muted, outline, status, and focus colours are Not captured.

## Typography

The product font family is Not captured. The style guide falls back to system-ui. That fallback is not a measured Fiverr family.

## Layout

No spacing scale was captured.

## Elevation & Depth

No shadow tokens were captured.

## Shapes

No radius scale was captured.

## Components

No component tokens map onto DESIGN.md properties. The inventory is in [components.md](components.md).

## Do's and Don'ts

- Do treat unread roles as Not captured.
- Don't read a homepage layout from the login screenshot.
- Don't design a signed-in Fiverr from this package.
- Don't copy the wordmark or brand colours into something that ships.
