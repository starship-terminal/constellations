---
version: alpha
name: Buy Me a Coffee
description: Public marketing site. Floral white page, ink text, one yellow pill. One light theme.
colors:
  primary: "#ffdd00"
  neutral: "#faf8f0"
  surface: "#ffffff"
  on-surface: "#222222"
  on-surface-variant: "#777777"
  outline: "rgba(34, 34, 34, 0.1)"
typography:
  display:
    fontFamily: Circular Bold
    fontSize: 96px
    fontWeight: 400
    lineHeight: 95px
    letterSpacing: -2.4px
  body:
    fontFamily: Circular Regular
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  label:
    fontFamily: Circular Medium
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
rounded:
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  card: 36px
  pill: 9999px
spacing:
  "1": 4px
  "2": 8px
  "3": 12px
  "4": 16px
  "5": 24px
  "6": 32px
components:
  button:
    backgroundColor: "#ffdd00"
    textColor: "#222222"
    rounded: 9999px
    height: 48px
---

# Buy Me a Coffee

Written from [tokens.json](tokens.json) for this capture. The catalog exporter was not run, because this pull request does not edit catalog.json. `make design-md` will replace this file once the package is registered.

## Overview

Public site only. Floral white page, white header, ink text, one yellow pill. Circular is the type family and is not included.

## Colors

Yellow `#ffdd00` is the accent. Page is `#faf8f0`. Text is `#222222`. Muted is `#777777`. Surface is `#ffffff`.

## Typography

Display is Circular Bold at 96px on 95px. Body and labels are 16px. Circular is proprietary and not shipped.

## Layout

Header is 76px at 1440. Buttons are pills. Cards use 36px radius. Spacing steps are 4, 8, 12, 16, 24 and 32.

## Components

The yellow button, the nav link, the header, and the search field. States and gaps are in [components.md](components.md).

## Do's and Don'ts

See [README.md](README.md). Do not invent a dark theme. Do not style the dashboard from this package.
