---
version: "alpha"
name: "Leonardo.Ai"
description: "Public marketing site for Leonardo.Ai: black page, violet #6e60ee poster type and subscribe pill, white Log in pill, Canva Sans UI, Ufficio Display headlines. Signed-in app not captured."
colors:
  primary: "#6e60ee"
  neutral: "#000000"
  surface: "#111111"
  on-surface: "#ffffff"
  on-surface-variant: "#ededed"
  outline: "rgba(255, 255, 255, 0.16)"
  color-violet: "#6e60ee"
  color-white: "#ffffff"
  color-ink: "#000000"
  color-muted: "#ededed"
  color-menu: "#111111"
  color-green: "#03e65b"
  color-yellow: "#f8c030"
  color-red: "#f85848"
typography:
  hero:
    fontFamily: ufficioDisplay
    fontSize: 34.425px
    fontWeight: 500
    lineHeight: 0.925
    letterSpacing: -0.02em
  button:
    fontFamily: canvaSans
    fontSize: 16px
    fontWeight: 500
  poster:
    fontFamily: leoSans
    fontSize: 76px
    fontWeight: 900
rounded:
  pill: 9999px
  none: 0px
spacing:
  login-height: 35px
  hero-button-height: 48px
  tab-height: 61px
components:
  button-login:
    backgroundColor: "#ffffff"
    textColor: "#000000"
    rounded: "{rounded.pill}"
    height: "{spacing.login-height}"
  button-subscribe:
    backgroundColor: "#6e60ee"
    textColor: "#ffffff"
    rounded: "{rounded.pill}"
    height: "{spacing.hero-button-height}"
---

# Leonardo.Ai

Written for this capture because the package is not registered in catalog.json, so `make design-md` cannot emit this file. Tokens in [tokens.json](tokens.json) are the source of truth. This file holds the dark theme only and drops provenance.

## Overview

Leonardo.Ai's public site is a black marketing surface. Violet `#6e60ee` is the poster colour and the subscribe pill. White pills are the account action. The signed-in generator was not captured.

## Colors

Page `#000000`, menu surface `#111111`, text `#ffffff`, muted `#ededed`, accent `#6e60ee`. Plan labels add yellow `#f8c030`, green `#03e65b` and red `#f85848`. The shadcn `:root` variables are not this palette.

## Typography

Canva Sans for UI. Ufficio Display for the headline, 34.425 px, weight 500, uppercase. Leo Sans for the 76 px poster, weight 900. All three are proprietary and are not shipped here.

## Layout

Desktop 1440 and phone 390. Header menus collapse into a drawer. Content width was not tokenised.

## Elevation

Flat. The menu is a fill, not a shadow.

## Shapes

Pills use a full radius, recorded as 9999 px from a computed value the browser expanded.

## Components

Log in is a white pill. Subscribe is a violet pill. Pricing uses a selected violet tab and idle tabs at 10% white.

## Do's and Don'ts

Paint the page black. Spend violet on poster type and subscribe. Do not copy the shadcn `:root` accent as the brand. Do not style the signed-in app from this package.
