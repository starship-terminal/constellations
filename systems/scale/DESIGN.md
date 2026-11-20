---
# Hand-written for this capture because catalog.json must not be edited.
# make design-md would overwrite this once a catalog entry exists. Do not treat it as generated.
version: "alpha"
name: "Scale"
description: "Public marketing site for Scale AI: white page, black ink, Aeonik, 8px controls, a black Get Started pill."
colors:
  primary: "#000000"
  neutral: "#ffffff"
  surface: "#f5f5f5"
  on-surface: "#000000"
  on-surface-variant: "#929292"
  outline: "#c7c7c7"
  page: "#ffffff"
  text: "#000000"
  muted: "#929292"
  accent: "#000000"
  link: "#006cff"
  border: "#c7c7c7"
typography:
  body:
    fontFamily: aeonik
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  display:
    fontFamily: aeonik
    fontSize: 40px
    fontWeight: 400
    lineHeight: 50px
    letterSpacing: -0.4px
  nav:
    fontFamily: aeonik
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
rounded:
  xs: 0.125rem
  sm: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  2xl: 1rem
  control: 8px
  field: 8px
spacing:
  base: 4px
  "2": 8px
  "3": 12px
  "4": 16px
  "6": 24px
  "8": 32px
components:
  button-primary:
    backgroundColor: "#000000"
    textColor: "#ffffff"
    height: 40px
    rounded: 8px
  field:
    backgroundColor: "#ffffff"
    textColor: "#171717"
    rounded: 8px
---

# Scale

Light marketing tokens from [tokens.json](tokens.json), read on 2026-11-21. The dark set is declared and is not in this file. Aeonik is not loaded here.

## Colors

Page is #ffffff. Text is #000000. The primary action is #000000 with #ffffff text. Muted text on the login control is #929292. The login border is #c7c7c7. Docs links use #006cff, derived from `:root --primary` 0 108 255.

## Typography

Body is Aeonik 16px / 24px, weight 400. The demo headline is 40px / 50px, weight 400, letter-spacing -0.4px. Nav labels are 14px.

## Rounded

The Tailwind radius scale runs from 0.125rem to 1rem. Controls and fields measured 8px.

## Spacing

`--spacing` is 0.25rem. The steps here are that unit times 1, 2, 3, 4, 6, and 8 at a 16px root, so they are derived.

## Components

The primary button is 40px tall, 8px radius, black fill, white text. Fields are white, 8px radius, #171717 text.
