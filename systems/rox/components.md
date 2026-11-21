# Rox components

Public site only, measured on 2026-11-21 from www.rox.com, signed out. Crops from the first measure pass landed on Framer wrapper links and are not used as evidence. The states below were read again from the painted control. Screenshots show the layout.

## Button

Header "Start now" is the primary button. 90 by 30, fill `#1c1917`, label Geist 14/500 `#fafafa`, radius 0, padding 8px 13px. Hover fill `#0c0a09` with an inset shadow. Keyboard focus adds a 1px `#005fcc` auto outline. "Contact Sales" is the quiet button: fill `#fafafa`, label `#403f3e`, shadow `0 1px 2px rgba(0,0,0,.04)`. Plan "Start for free" is wider (308 by 41), fill `#403f3e`, label 16/500. Hover and pressed both go to `#000000`.

Shown in [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png) and [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Link and nav

Header links are Geist 14/500 `#403f3e` on a 64px hit row. Hover opens a menu for Platform, Resources, and Company. It does not recolour the link. Footer links repeat the same labels.

Shown in [screenshots/home-light-platform-menu.png](screenshots/home-light-platform-menu.png).

## Text field, text area, select

The contact form is the only public form that was opened. The email field's painted wrapper is 560 by 49, fill `#f4f4f3`, radius 4px. The input itself is borderless. Text area padding is 16px. The "How did you hear about us?" control is a select. Nothing was typed. Nothing was submitted. Focus was moved onto the email field for [screenshots/contact-light-focus.png](screenshots/contact-light-focus.png). Disabled, error, and loading states were not present.

## Menu

Desktop menus are hover panels. The phone menu is a full-screen black drawer opened by a 33px icon button, with Contact Sales and Start now pinned at the bottom.

Shown in [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Dialog

Docs search opens a white dialog ("Search the docs…", Escape). No query was typed.

Shown in [screenshots/docs-light-search.png](screenshots/docs-light-search.png).

## Card

Pricing cards sit on `#faf9f7` with a hairline. Three plans: Individual, Teams, Enterprise. No billing toggle.

## Badge

A Gartner toast sits over the home hero. It is a promo, not a status badge.

## Gaps

| Component | Status |
|---|---|
| Icon button | Observed on phone (menu close). Values not isolated from the 33px hit target. |
| Checkbox, radio, switch | Not present on the public pages opened. |
| Tabs | Docs has a section nav. Not a tab widget. |
| Tooltip, toast, table, avatar | Not present as product components. The Gartner toast is a marketing widget. |
| List row | Customer logo row and story cards are marketing, not an app list. |
| Destructive confirmation, empty, loading, error | Not present on the public surface. |
| Signed-in app | Behind `run.rox.com` and Auth0. Not captured. |
