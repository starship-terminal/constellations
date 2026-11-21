# Rivian

Written from [tokens.json](tokens.json) for this capture. `make design-md` was not run, because that command reads catalog.json and this capture was told not to edit the catalog. Take values from tokens.json. This file holds the light theme only.

## Overview

Good for: electric-vehicle marketing pages, a white header with one amber action, and long product stories.

Captured 2026-11-21, public, signed out. Themes: light.

## Colors

Roles from the light set.

- **primary (#ffaa00):** `light.color.accent`
- **surface (#ffffff):** `light.color.page`
- **on-surface (#000000):** `light.text.primary`
- **on-surface-variant (#494949):** `light.text.secondary`
- **outline (#cbcbcb):** `light.border.default`

Status: success `#4a8231`, warning `#d58103`, danger `#dc3127`, info `#005e7d`.

## Typography

Adventure, then Helvetica Neue, Helvetica, Arial, sans-serif. Display 96px weight 600, headline 36px weight 600, body 16px, label 14px weight 600. Full roles are in `core.typography`.

## Layout

Navbar height 56px. Content widths were not tokenised beyond the consumer-ui max of 1920px.

## Elevation

`core.shadow.nav` is `0 2px 8px rgba(0,0,0,.15)`. `core.shadow.base` and `core.shadow.hero` are the softer card shadows. First layer only.

## Shapes

Pills on header controls (`9999px`). Cards use 20px (`core.radius.macro`). The scale also has 4, 12, 32 and 40px steps, some of them Derived from fallbacks.

## Components

Primary button: `#ffaa00` fill, black text, 32px height, 9999px radius, 8px 16px padding. Hover `#ffbd2e`. Inverse button: white fill, 40px radius.

## Do's and Don'ts

- Do take values from tokens.json.
- Don't read colours off the screenshots. They are 256-colour PNGs.
- Don't invent a dark theme.
- Don't copy the logo or vehicle art into something that ships.
