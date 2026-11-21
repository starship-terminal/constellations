---
version: "alpha"
name: "Curater"
description: "Public signed-out curation app: white page, near-black type, a white Google pill, a filled search pill, and an icon rail."
colors:
  primary: "oklch(0.21 0.006 285.885)"
  neutral: "oklch(1 0 0)"
  surface: "oklch(1 0 0)"
  on-surface: "oklch(0.141 0.005 285.823)"
  on-surface-variant: "oklch(0.552 0.016 285.938)"
  outline: "oklch(0.95 0.004 286.32)"
---

# Curater

Written from [tokens.json](tokens.json) for this capture. `make design-md` was not run, because this capture was asked not to edit catalog.json. [tokens.json](tokens.json) is the source of truth.

## Overview

Captured 2026-11-21 from https://curater.org/, signed out. One light theme. Desktop 1440 x 900 and phone 390 x 844.

## Colors

- **primary:** `light.accent.default`, the filled search pill
- **neutral:** `light.page`
- **surface:** `light.surface`
- **on-surface:** `light.text.primary`
- **on-surface-variant:** `light.text.secondary`
- **outline:** `light.border.default`

Brand colours live under `core.color` as the `--Curater-*` palette, including gray, green, red, yellow, pink, and the selection set.

## Typography

Painted UI is ABCDiatype, 16px on buttons, 14px on the search field. The declared scale is `core.fontSize` from `--text-xs` through `--text-5xl`.

## Layout

Spacing is a 0.25rem base, `core.spacing`. The sidebar token is 5rem. Content width is 35rem.

## Elevation

Shadows are the four `--shadow-*` values in `core.shadow`. The sign-in dialog also uses a `rgba(0, 0, 0, 0.5)` scrim.

## Shapes

Pills use `9999px`. The settings menu uses 12px. The token scale runs from `--radius-sm` to `--radius-full`.

## Components

The Google action is a white 58px pill. The phone search submit is a filled pill. Menus are white, 12px radius. See [components.md](components.md).

## Do's and Don'ts

Keep the page white. Use the white pill for Google sign-in. Use the filled pill for search submit. Do not invent a signed-in screen or a dark theme. See [README.md](README.md).
