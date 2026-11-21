---
version: "alpha"
name: "Digg"
description: "Public signed-out Digg: a news reader with a sidebar, topic feeds, story pages and a blue pill for the product's own actions. Written from tokens.json for this capture. The catalog entry is intentionally absent from this PR, so make design-md has not regenerated this file."
colors:
  primary: "#1c66eb"
  neutral: "#fdfdff"
  surface: "#ffffff"
  on-surface: "#161617"
  on-surface-variant: "rgba(21, 21, 23, 0.702)"
  outline: "rgba(0, 0, 0, 0.078)"
  page: "#fdfdff"
  text: "#161617"
  muted: "rgba(21, 21, 23, 0.702)"
  accent: "#1c66eb"
  border: "rgba(0, 0, 0, 0.078)"
  secondary: "#f0f0f5"
  destructive: "#cc434d"
  success: "#6aa15a"
  sidebar: "#f8f8fb"
typography:
  body:
    fontFamily: "roobert"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "roobert"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.25
  nav:
    fontFamily: "roobert"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.25
  story-title:
    fontFamily: "roobert"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: 1.3
rounded:
  sm: "0.375rem"
  md: "0.5rem"
  lg: "0.625rem"
  xl: "0.875rem"
  pill: "26px"
  control: "8px"
spacing:
  1: "4px"
  2: "8px"
  3: "12px"
  4: "16px"
  5: "14px"
components:
  button-primary:
    backgroundColor: "#1c66eb"
    textColor: "#ffffff"
    rounded: "26px"
    height: "40px"
  button-secondary:
    backgroundColor: "#f0f0f5"
    textColor: "#161617"
    rounded: "26px"
    height: "40px"
  field:
    backgroundColor: "rgba(0, 0, 0, 0)"
    textColor: "#161617"
    rounded: "8px"
    height: "36px"
---

## Overview

Digg's public web app is a news reader. The page is `#fdfdff` in light and `#161617` in dark. The product's own actions use `#1c66eb`. UI text is Roobert.

Take values from [tokens.json](tokens.json). This file is the light theme only and has no per-value provenance.

## Colors

Light page `#fdfdff`, surface `#ffffff`, text `#161617`, muted text at 70% opacity, accent `#1c66eb`, border black at 8% opacity. Dark page `#161617`, card `#1c1c1f`, text `#fdfdff`. The blue, red, yellow, and gray ramps are in `core.color`.

## Typography

Roobert at 16px for body and story titles, 14px for labels and nav. Weights 400, 500, 600, and 700 are declared. The story page display size was not measured.

## Layout

The desktop sidebar is 255px. Main content starts at 256px in a 1440px viewport. Corner radius starts at 0.625rem. Sidebar and feed controls are pills (26px, or fully round). Story cards use 18px.

## Elevation

One shadow is declared, `--shadow-md`. Cards on the captured pages sit on a hairline border more often than on that shadow.

## Shapes

Buttons at the large size are 40px tall with a 26px radius. Fields are 36px tall with an 8px radius. The digg control is a 44px pill.

## Components

Sign up is the primary pill. Log in is the secondary pill. Feed View and Feed display are select triggers. Login and signup are pages, not dialogs. The cookie preferences dialog holds two switches.

## Do's and Don'ts

Keep one blue for Digg's own actions. Set the UI in Roobert. Use pills for sidebar and feed controls. Keep cards flat. Do not treat the login wall as the product.
