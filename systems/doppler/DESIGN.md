---
# Written for this package because catalog.json was not edited. make design-md would replace this after a catalog entry exists.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "Doppler"
description: "Public secrets-management marketing site on warm black with one fluorescent-green primary action, plus a separate light docs chrome."
colors:
  primary: "#00f575"
  neutral: "#1c1624"
  surface: "#1c1624"
  on-surface: "#f1f0ec"
  on-surface-variant: "#d0c9c4"
  outline: "#f1f0ec"
  page: "#1c1624"
  text: "#f1f0ec"
  accent: "#00f575"
  accent-hover: "#00c05b"
  on-accent: "#1c1624"
  border: "#f1f0ec"
  focus: "#005fcc"
typography:
  display:
    fontFamily: "__DopplerRepro_a18e76"
    fontSize: "48px"
    fontWeight: 450
    lineHeight: 1.2
  body:
    fontFamily: "__DopplerRepro_a18e76"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
  button:
    fontFamily: "__DopplerRepro_a18e76"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  button: "12px"
  header-bottom: "16px"
spacing:
  header-x: "20px"
  button-y: "8px"
  button-x: "12px"
  demo-y: "10px"
  demo-x: "16px"
components:
  button-primary:
    backgroundColor: "#00f575"
    textColor: "#1c1624"
    rounded: "12px"
    height: "32px"
---

# Doppler

Generated from [tokens.json](tokens.json) and [README.md](README.md). This copy was written by hand because the capture was not allowed to edit catalog.json, which is what `make design-md` reads. Do not treat this file as the source of truth.

It follows the DESIGN.md spec, version alpha. That format has no themes and no per-value provenance. This file holds the marketing dark theme. The docs light theme is in tokens.json.

## Overview

Good for: dark marketing pages with one bright primary action, and a separate light documentation chrome.

Captured 2026-11-21, signed out. Themes: dark (marketing), light (docs).

## Colors

Roles are the marketing site. Page and header are warm black `#1c1624`. Primary text is warm white `#f1f0ec`. The primary action is fluorescent green `#00f575`, hover `#00c05b`, label `#1c1624`. Focus outline is `#005fcc`.

## Typography

Display is 48px at weight 450. Body and buttons are 16px at weight 400. The family name in CSS is a Next.js local font. The real family name was not captured.

## Layout

Header is 72px tall with 20px horizontal padding. Desktop captures are 1440 wide. Phone captures are 390 wide. The display size drops to 36px at 768.

## Elevation & Depth

No shadow tokens. The header computed box-shadow is none.

## Shapes

Buttons are 12px radius. The header's bottom corners are 16px.

## Components

Primary button: green fill, warm-black label, 12px radius, 32px tall in the header. Secondary button: transparent fill, 1px warm-white border.

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json).
- Do read [README.md](README.md) before relying on a value.
- Don't read colours off the screenshots. They are 256-colour PNGs.
- Don't copy the logo or brand colours into something that ships.
- Don't invent a light theme for the marketing site.
