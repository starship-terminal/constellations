#!/usr/bin/env python3
"""Write components.md from the measured inventory. No crops."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TEXT = """# Zara Home components

Public signed-out surfaces, measured on zarahome.com on 2026-11-19 from computed styles. No element crops: `preview_snapshot` returned "The browser is not producing screenshot frames", and headless Playwright was answered HTTP 403 Access Denied. This inventory names the element and the token.

## Button

Filled square. The market gate GO and the product CHOOSE A SIZE use `light.action.primary` (#1e1e1e), text `light.text.inverse`, height `core.size.button` (36px), horizontal padding `core.space.buttonPad` (16px), 12px weight 600, tracking `core.letterSpacing.body` (0.2px), uppercase, radius `core.radius.none`.

The market dialog's primary button is the same fill at `core.size.dialogButton` (40px), 462px wide. Its secondary is white with a 1px #1e1e1e border, same height.

ADD on a product card is not that button. It is `rgba(255, 255, 255, 0.8)` text `light.text.body`, 36px, no border, radius 0. It opens a size selector. It was not used to add an item.

`button.mdc-button:hover` in the stylesheet is #3a3a3c. That hover was not triggered live.

## Icon button

Header account, help and basket are icon links, about 19px to 29px, white on the homepage hero and ink on the white category header. The product page has a 36px round white control with Material elevation `core.shadow.fab`. No separate icon set was extracted beyond the wordmark SVG.

## Link

Footer links are 12px, weight 300, uppercase, tracking 0.2px, ink, no underline, 8px apart. Category subnav links (SEE ALL, DUVET COVERS) are 14px, weight 400, tracking 0.2px, not uppercase. FILTERS and SORT are 11px uppercase. Product meta links (PRODUCT DETAILS) are 11px uppercase. More info is 14px, sentence case, ink.

## Text field

Search (`input.search-input`) is 30px, weight 500, uppercase, tracking 0.2px, height 35px, padding `0 45px 0 0`, no border, radius 0. Placeholder: "What are you searching for?". Nothing was typed into it.

The market gate `mat-form-field` is 75px tall, 14px weight 500, 15px below the next field. Its open menu was not measured.

## Text area

Not present on the captured public pages.

## Select

CHOOSE A SIZE is a button, not a native select. 36px, ink fill, 1px `rgba(0, 0, 0, 0.12)` border, uppercase 12px weight 600. The size menu was not opened.

Market and language on the worldwide gate are Material selects. The closed fields were measured. The option list was not.

## Checkbox

OneTrust category switches exist in the cookie panel. They were not opened as a storefront control. No product checkbox was on the captured pages.

## Radio

Not present on the captured public pages.

## Switch

Not present as a storefront control. OneTrust uses checkbox switches inside the cookie panel.

## Tabs

Category subnav is a row of links, not a tab widget. The current item has class `active`. Its computed colour, size and weight matched the idle links. No underline was read from the element.

Grid view is three 20 by 24px buttons labelled 1, 2 and 3, 10px weight 500. The selected one adds `grid-view__option--selected`. No fill change was measured.

## Tooltip

Colour chips expose `mat-mdc-tooltip-trigger` and an accessible name (SAND, PINK). The tooltip popup was not opened.

## Toast

Not present.

## Table

Not present.

## Avatar

Not present.

## Card

A category card is `article.product-item`, about 544 by 430px in this 1169px pane, radius 0, no border, no shadow. Name is 14px uppercase weight 400. Price is 14px weight 500, ink. Colour chips are 20px squares with a 1px white image border.

## Dialog

The market dialog surface is white, radius 0, shadow none, pane 512 by 288px. HELLO is 18px weight 300. The subtext is 14px weight 300. The footer line is 10px weight 300. Primary and secondary buttons are 40px, 462px wide.

## Badge

Not present. Prices were not struck through on the captured products. The declared sale colour `--accent-lighter-color` (#cf0a2c) was not used by a measured price.

## Gaps

- Dark theme: not shown.
- Phone width and 1440: the pane was 1169 by 731.
- Screenshots of the site: preview frames unavailable. Headless Playwright returned 403.
- Hover, focus and disabled: stylesheet only (`:focus-visible` outline #2684ff, button hover #3a3a3c).
- Size menu, filter drawer, sort menu, mega menu: not opened.
- Bag, checkout, payment, address, phone, account creation, newsletter submit: not entered.
- Text area, radio, switch, toast, table, avatar: not on these pages.
- Sale price colour: declared, not used by a measured price.
- OneTrust Allow All is 2px radius, black fill. It was collapsed (height 0) on the storefront.
- Chat control radius is 100%. A percentage is not stored as a dimension token.
"""
(HERE / "components.md").write_text(TEXT)
print("wrote components.md")
