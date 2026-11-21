---
# Written by hand because this capture must not edit catalog.json, which is what generates DESIGN.md.
# Source of truth: tokens.json. Spec version alpha. One theme, no provenance.
version: "alpha"
name: "Starbucks"
description: "Public Starbucks site: green bands on white, pill account buttons, SoDo Sans, a green order button."
colors:
  primary: "#00754a"
  neutral: "#ffffff"
  surface: "#f5f1eb"
  on-surface: "#000000"
  on-surface-variant: "rgba(0, 0, 0, 0.87)"
  outline: "rgba(0, 0, 0, 0.87)"
  background-page: "#ffffff"
  background-brand: "#006242"
  background-surface: "#f5f1eb"
  text-primary: "#000000"
  text-accent: "#00754a"
  text-heading: "#006242"
  action-primary: "#000000"
  action-brand: "#00754a"
typography:
  body:
    fontFamily: SoDoSans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: -0.16px
  nav:
    fontFamily: SoDoSans
    fontSize: 14px
    fontWeight: 700
    lineHeight: 21px
    letterSpacing: 1.4px
  heading:
    fontFamily: SoDoSans
    fontSize: 24px
    fontWeight: 600
    lineHeight: 33.6px
  display:
    fontFamily: SoDoSans
    fontSize: 36px
    fontWeight: 700
    lineHeight: 44px
rounded:
  none: 0px
  field: 8px
  pill: 50px
spacing:
  button-x: 16px
  button-y: 7px
  field-x: 16px
  order-x: 24px
components:
  button:
    backgroundColor: "{action.primary}"
    textColor: "{text.onBrand}"
    height: 33px
    radius: 50px
---

# Starbucks

Public site tokens. Take values from tokens.json. This file is a stand-in until `make design-md` can run against a catalog entry.

## Overview

Green (#006242) bands, white page, black Join now pill, green (#00754a) links and order button. SoDo Sans. One light theme.

## Colors

Page is white. The order strip and the sign-in ground are #006242. Links and Add to Order are #00754a. Join now is black.

## Typography

SoDo Sans, with Helvetica Neue as the fallback. Nav is 14px bold, uppercase, 1.4px tracking. Body is 16/24.

## Layout

Desktop captures are 1440 wide. Phone captures are 390 wide. The header is 100px tall on desktop.

## Elevation

The order button has a two-layer shadow. Chrome pills do not.

## Components

Header pills, outline links, text fields at 56px with 8px radius, size radios, a check-balance dialog, and a mobile menu drawer. See components.md.

## Do's and Don'ts

See the README. Do not fill sign-in fields. Do not screenshot the store locator.
