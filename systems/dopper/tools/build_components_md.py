#!/usr/bin/env python3
"""Write components.md from the capture notes. Deterministic, no network."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
text = """# Dopper components

Captured signed out from www.dopper.com and shop.dopper.com on 2026-11-21.
Values are token names from [tokens.json](tokens.json). Crops were not cut;
the states below are the ones measured or photographed.

## Button

Shop add to cart: fill `color.blue`, text `color.cream-deep`, radius `radius.button` (20px), height `size.button-height` (54px), padding 13px 25px, Gilroy 600 / 20px. Focus-visible: 2px `color.ink` outline and a 4px `color.paper` gap. Hover did not change the fill on the measured click. See [pdp-light-default](screenshots/pdp-light-default.png).

Marketing primary: near-black pill, cream label. Secondary: cream outline on the blue hero. See [home-light-default](screenshots/home-light-default.png).

Shop Filters: green pill `color.green`, cream label. See [shop-bottles-light-filters](screenshots/shop-bottles-light-filters.png).

## Link

Shop category links: Gilroy 600 / 20px, `color.blue` when current, `color.ink` otherwise. Marketing nav links sit in the `dopper-navigation` shadow root, Gilroy 700 / 16px, cream on a blue hero and ink on a light page.

## Menu

Desktop marketing menus open from Bottle, Travel Mug, Tap, Mission, Get Involved and For Businesses. The Bottle panel is a blue card of links plus a cream promo card. See [home-light-nav](screenshots/home-light-nav.png).

Phone: the menu toggle opens a blue drawer. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

Shop submenus (Mugs, Bottles, Spare parts) exist in the DOM as `.level0.submenu` and stay `display: none` on hover in this capture. They are listed in [site-tree.md](site-tree.md).

## Language menu

EN opens a cream list: English, Nederlands, Deutsch, Français. See [home-light-language](screenshots/home-light-language.png).

## Text field

Present on the login wall (email, password). Not filled. Not measured past the screenshot. See [login-wall-light-default](screenshots/login-wall-light-default.png).

## Checkbox

Show password and Remember Me on the login wall. Not toggled.

## Filter

Collection, Size and Colour on bottle grids. Colour is a set of swatch dots. See [shop-bottles-light-filters](screenshots/shop-bottles-light-filters.png).

## Card

Product tiles on the shop grid. A New badge sits above some bottles. Radius was 0 on the measured `.product-item`.

## Not present on the captured surface

Text area, select (except the shop sorter), radio outside filters, switch, tabs, tooltip, toast, table, avatar, badge as a system component. Dark theme: not present.

## Not captured

Pressed and loading states of add to cart. A filled cart. Checkout past the empty basket. Signed-in account. Newsletter submit. Hover of the marketing burst buttons (the wrapper is transparent; the visible pill is a child that was not separately measured).
"""
(HERE / "components.md").write_text(text)
print("wrote components.md")
