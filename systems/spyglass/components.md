# Spyglass components

Measured on the public pages on 2026-11-19. Values are token names. Raw numbers are in [raw/readings.json](raw/readings.json).

## Button

Primary link "Get 50% off": height `core.size.buttonMd` (36px), padding 8px 16px, radius `core.radius.sm` (6px), fill `light.color.primary`, text `light.color.onPrimary`, Geist 14px weight 500. Hover background `light.color.primaryHover`.

Outline link "Sign in": same height and padding, 1px `light.color.border`, fill `light.color.surface`. Hover fill `light.color.outlineHover`.

Disabled "Continue" on `/sign-in`: same primary colours at opacity 0.5 while the email is empty.

Pressed and loading were not captured.

Crops: [button-primary-default.png](components/crops/button-primary-default.png), [button-outline-default.png](components/crops/button-outline-default.png).

## Icon button

Phone "Open menu": 40px square, radius 8px, colour `#3b3b3b`, transparent fill. [home phone](screenshots/home-light-phone.png).

Carousel previous/next on `/sign-in`: 32px circle, fill `#212121`, icon white.

## Link

Footer "Pricing": Geist 16px, colour `light.color.footerLink` on `light.color.footer`.

## Text field

Home prompt: 14px Geist, placeholder `light.color.muted`, inside an 8px-radius card with 12px padding.

Sign-in email: wrapper height `core.size.field` (40px), 1px border `light.color.fieldBorder`, radius 6px, padding 0 13px. Label is Geist 14px weight 500, colour `#3b3b3b`. Not submitted.

Crops: [field-default.png](components/crops/field-default.png), [prompt-default.png](components/crops/prompt-default.png).

## Tabs

FAQ category chips: selected chip is `#212121` on white text, height 32px, radius 20px, padding 0 12px, 13px weight 500. Unselected chips were not separately measured.

## Menu

Product menu: 380 by 168, radius 24px, fill `light.color.scrim`, shadow `core.shadow.menu`. The trigger fills `light.color.navHover` while open. [menu-open.png](components/crops/menu-open.png).

## Card

Pricing card body was not a single bordered element in the measurement (the visible border sits on an inner node). Plan CTAs match the primary and outline buttons. Prices are Familjen Grotesk 40px weight 500.

## List row

FAQ question button: padding 20px, 16px weight 500, colour `#212121`. The open row wrapper is white, radius 8px. [faq open](screenshots/faq-light-open.png).

## Table

`/compare` table: header 13px weight 500 colour `#3b3b3b`, cell 16px colour `#212121`, padding 16px 20px. [compare](screenshots/compare-light-default.png).

## Gaps

Text area, select, checkbox, radio, switch, tooltip, dialog, toast, avatar: not on the public pages.

Badge "Most Popular" computed to a pill (padding 6px 12px, 12px, colour `#737373`) but its box height was 0 in the pass, so it is not cropped.

Focus ring: not painted on the header links.

Signed-in app, checkout, and Google OAuth: not entered.
