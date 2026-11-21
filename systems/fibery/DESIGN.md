---
version: "alpha"
name: Fibery
description: "Public marketing site for a work platform: soup page, ink text, Suisse Intl, 6px controls."
colors:
  primary: "#3b758c"
  neutral: "#faebd6"
  surface: "#fdf7ef"
  on-surface: "#251d1a"
  on-surface-variant: "#9f8b7f"
  outline: "#251d1a"
typography:
  display:
    fontFamily: Suisse Intl
    fontSize: 64px
    fontWeight: 800
    lineHeight: 64px
  heading:
    fontFamily: Suisse Intl
    fontSize: 48px
    fontWeight: 800
    lineHeight: 48px
  title:
    fontFamily: Suisse Intl
    fontSize: 36px
    fontWeight: 700
    lineHeight: 36px
  body:
    fontFamily: Suisse Intl
    fontSize: 16px
    fontWeight: 400
    lineHeight: 19.2px
rounded:
  control: 6px
  pill: 48px
spacing:
  control-x: 16px
  header: 12px
---

# Fibery

Written from [tokens.json](tokens.json) for this package-only capture. `make design-md` was not run, because that command needs a catalog.json entry and this change does not add one. Take values from [tokens.json](tokens.json).

## Overview

Public marketing site, captured 2026-11-21, signed out. One theme: light. The walk stopped at the login wall.

## Colors

Page `#faebd6`, surface `#fdf7ef`, text `#251d1a`, muted `#9f8b7f`, accent `#3b758c`, border `#251d1a`.

## Typography

Suisse Intl. Display 64/64 weight 800. Heading 48/48 weight 800. Title 36/36 weight 700. Body 16/19.2 weight 400.

## Layout

Control padding 16px horizontal. Header padding 12px. Button height 40px.

## Elevation & Depth

One shadow: `0 10px 16px -3px rgba(20,21,26,.08), 0 1px 2px 0 rgba(20,21,26,.05)`.

## Shapes

Controls 6px. Pills 48px. Chat composer 20px.

## Components

Filled signup button, cream login button, peach pills, hover menus. See [components.md](components.md).

## Do's and Don'ts

- Do take values from [tokens.json](tokens.json).
- Don't invent a dark theme or a signed-in screen. Neither was captured.
