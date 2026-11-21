# DESIGN.md

This file is a stand-in. `make design-md` writes the real DESIGN.md from catalog.json and tokens.json. This capture was told not to edit catalog.json, so the generator was not run. Values below are copied from tokens.json. If they disagree, tokens.json wins.

## Colors

| Name | Value | Token |
|---|---|---|
| surface | #faf6f0 | core.color.paper |
| on-surface | #000000 | core.color.ink |
| primary | #000000 | core.color.ink |
| on-primary | #ffffff | core.color.white |
| outline | #c4c4c4 | core.color.field-border |

Light only. No dark palette was captured.

## Typography

| Style | Family | Size | Weight | Line height |
|---|---|---|---|---|
| display | Unbounded | 82px | 500 | 90.2px |
| body | Inter | 27px | 400 | 40.5px |
| nav | Inter | 16px | 600 | 19.2px |
| button | Inter | 16px | 600 | 19.2px |

## Rounded

| Step | Value |
|---|---|
| pill | 9999px |
| control | 10px |
| none | 0px |

## Spacing

6px, 10px, 12px, 15px, 16px, 20px, 30px, 48px. These are measured paddings and insets, not a published scale.

## Components

Button background #000000, text #ffffff, radius 9999px, height 56px. Field background #fcfcfc, text #222222, radius 10px, height 48.5px.

## Omitted

Elevation, motion, focus, dark theme, and signed-in components. Not captured. See [README.md](README.md).
