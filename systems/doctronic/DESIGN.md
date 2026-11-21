---
name: Doctronic AI
description: Public medical-AI marketing and chat shell. Warm paper canvas, Fraunces display, Geist UI, one blue primary pill.
colors:
  page: "#fdfdf7"
  surface: "#ffffff"
  text: "#1b1b18"
  muted: "hsl(from #1b1b18 h s l / .73)"
  accent: "#2463eb"
  border: "hsl(from #1b1b18 h s l / .08)"
typography:
  display-48:
    fontFamily: fraunces
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.17
  body-16:
    fontFamily: geist
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
  heading-20:
    fontFamily: geist
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
---

# Doctronic AI

This file is a short export of [tokens.json](tokens.json). The catalog generator was not run, because this capture does not edit catalog.json. [tokens.json](tokens.json) is the source of truth.

## Overview

Captured 2026-11-21, signed out, light theme only, at 1440 and 390.

The public site is a paper canvas, a serif greeting, and one blue action. The signed-in app was not captured.

## Colors

- **page:** `#fdfdf7` (`light.page`, declared `--color-surface-canvas`)
- **surface:** `#ffffff` (`light.surface`)
- **text:** `#1b1b18` (`light.text`)
- **accent:** `#2463eb` (`light.accent`)
- **solid:** `#0b0b0a` (`light.solid`)
- **success / warning / danger / info:** declared foreground and background pairs in `light`

Ramps for blue, neutral, sage, lime, error, success, and warning live under `core.color`.

## Typography

Fraunces for display. Geist for sans, headings, and labels. Geist Mono for code. Stacks are in `core.font`. The `--text-*` ramp is in `core.typography`.

## Elevation

`core.shadow` holds xs through xl, plus a brand glow and a 2px focus ring in the accent blue.
