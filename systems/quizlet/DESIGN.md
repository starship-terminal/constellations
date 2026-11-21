---
version: "alpha"
name: "Quizlet"
description: "Signed-in night web app: twilight page #0A092D, gray text #F6F7FB, twilight-500 pill #4255FF, sunset-400 trial pill #FFCD1F, Hurme Geometric Sans 2. Light mode was not captured."
colors:
  primary: "#4255FF"
  neutral: "#0A092D"
  surface: "#2E3856"
  on-surface: "#F6F7FB"
  on-surface-variant: "#D9DDE8"
  outline: "#586380"
  twilight-500: "#4255FF"
  twilight-900: "#0A092D"
  gray-200: "#F6F7FB"
  gray-700: "#2E3856"
  sunset-400: "#FFCD1F"
rounded:
  field: "8px"
  pill: "200px"
spacing:
  button-y: "10px"
  button-x: "16px"
typography:
  body:
    fontFamily: hurme_no2-webfont
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "26px"
  heading:
    fontFamily: hurme_no2-webfont
    fontSize: "20px"
    fontWeight: 600
    lineHeight: "28px"
---

# Quizlet

Hand-written because `make design-md` needs a catalog.json entry, and that entry is deferred. The source of truth is [tokens.json](tokens.json).

## Overview

Night theme only. Page `#0A092D`, text `#F6F7FB`, accent `#4255FF`, trial `#FFCD1F`.

## Colors

Ramps live in `core.color` of [tokens.json](tokens.json): gray, error, lemon, lilac, mint, sherbert, sky, sunset, twilight. Semantic roles are the `night` set.

## Typography

Hurme Geometric Sans 2 (`hurme_no2-webfont`), then `-apple-system`, `system-ui`, `sans-serif`. Body 16/26 weight 400. Section heading 20/28 weight 600. Phone page title 32/40 weight 700.

## Layout

Desktop measured 1440 by 900. Phone measured 430 by 932. Sidebar plus a header with Search, Create, and a trial pill.

## Elevation

Menus sit on the twilight page. No elevation token was measured. Shadows on the sampled controls were `none`.

## Components

Primary pill, trial pill, search field, account menu, create menu. See [components.md](components.md).

## Do's and Don'ts

Do use the night page and the two pills. Don't invent a light theme. Don't read colours from the quantized screenshots.
