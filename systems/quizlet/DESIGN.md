---
version: "alpha"
name: "Quizlet"
description: "Public signed-out marketing site: gray page #F6F7FB, gray-800 text #282E3E, twilight-500 pills #4255FF, sunset-400 trial pill #FFCD1F, Hurme Geometric Sans 2. The upgrade page paints twilight-900 #0A092D. Signed-in extraction was not started."
colors:
  primary: "#4255FF"
  neutral: "#F6F7FB"
  surface: "#F6F7FB"
  on-surface: "#282E3E"
  on-surface-variant: "#586380"
  outline: "#D9DDE8"
  twilight-500: "#4255FF"
  twilight-600: "#423ED8"
  twilight-900: "#0A092D"
  gray-200: "#F6F7FB"
  gray-800: "#282E3E"
  sunset-400: "#FFCD1F"
rounded:
  field: "8px"
  pill: "200px"
spacing:
  login-y: "10px"
  login-x: "16px"
  signup-y: "12px"
  signup-x: "24px"
typography:
  body:
    fontFamily: hurme_no2-webfont
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "26px"
  heading:
    fontFamily: hurme_no2-webfont
    fontSize: "44px"
    fontWeight: 700
    lineHeight: "56px"
  label:
    fontFamily: hurme_no2-webfont
    fontSize: "14px"
    fontWeight: 600
    lineHeight: "20px"
---

# Quizlet

Hand-written from the public readings. `make design-md` was not run, and catalog.json was left alone. The source of truth is [tokens.json](tokens.json).

## Overview

Public light marketing site. Page `#F6F7FB`, text `#282E3E`, accent `#4255FF`, accent hover `#423ED8`, trial `#FFCD1F`. The public upgrade page background is `#0A092D`.

## Colors

Ramps live in `core.color` of [tokens.json](tokens.json): gray, error, lemon, lilac, mint, sherbert, sky, sunset, and twilight. Semantic roles are the `light` set. The `night` set keeps the prior signed-in role aliases. This pass did not re-open that shell.

The homepage h1 computed as `rgb(0, 0, 0)`. That value is not a ramp step. `light.text-strong` aliases gray-900 and records the gap.

## Typography

Hurme Geometric Sans 2 (`hurme_no2-webfont`), then `-apple-system`, `system-ui`, `sans-serif`. Body 16/26 weight 400. Homepage h1 44/56 weight 700. Log in pill 14px weight 600. Sign up pill 16px weight 600.

## Layout

Desktop measured 1440 by 900. Phone measured 390 by 844. Header with Study tools, Subjects, Create, Search, Log in, and Sign up. Footer columns sit below the marketing page.

## Elevation

Sampled controls reported `box-shadow: none`. No elevation token was measured. The login and signup dialogs are overlays. Their scrim colour was not sampled.

## Components

Log in pill, Sign up pill, search field, trial pill, teacher link. See [components.md](components.md).

## Do's and Don'ts

Do use the gray marketing page and the twilight pills. Do keep the trial pill sunset. Don't treat the night set as a capture from this pass. Don't read colours from the quantized screenshots.
