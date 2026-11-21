---
version: alpha
name: Cofounder
description: Public marketing site of cofounder.co, measured 2026-11-21. One light theme. Not a generated catalog export.
colors:
  primary: "#171717"
  neutral: "#f5f5f2"
  surface: "#ffffff"
  on-surface: "#171717"
  on-surface-variant: "#171717"
  outline: "#005fcc"
typography:
  hero:
    fontFamily: neoris
    fontSize: 46px
    fontWeight: 400
    lineHeight: 1.08
  body:
    fontFamily: neoris
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  nav:
    fontFamily: neoris
    fontSize: 15px
    fontWeight: 400
    lineHeight: 22.5px
rounded:
  control: 8px
  capability: 10px
  dialog: 16px
spacing:
  header: 91px
  control: 41px
  capability: 47px
components:
  button:
    backgroundColor: "#ffffff"
    textColor: "#171717"
    rounded: 8px
    height: 41px
---

# Cofounder

Values come from [tokens.json](tokens.json). This file is a short export for readers that expect DESIGN.md. It was written by hand because the package is not in catalog.json, so `make design-md` cannot generate it.

Muted text is not a separate reading. `on-surface-variant` repeats the primary text for that reason.

## Colour

Page `#f5f5f2`, text `#171717`, raised surface `#ffffff`, focus `#005fcc`.

## Type

Neoris at 46px for the hero and 16px for body. The webfont is not in this package.

## Controls

The header action is a white pill, 41px tall, 8px radius.
