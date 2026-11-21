# Components

Public site only, foodnoms.com, 2026-11-21. The iOS app is not in this package. Values are token names where a token exists. Crops were not cut: the states are in [screenshots/](screenshots).

## Button

Get the App is the primary control. Fill `light.accent` (`#f8622e`), label `light.on-accent`, Aquawax Pro DemiBold 16px, height `core.size.control` (40px), padding 12px 18px, radius `core.radius.pill` (20px). Hover lightens the fill (computed `color(display-p3 0.984314 0.631373 0.509804)` in light, a darker oklab mix in dark). Focus draws the browser outline `#005fcc` 1px. Pressed was not held cleanly: the CDP press also focused the link, so the pressed fill is Not captured as its own value.

Shown in [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/home-dark-default.png](screenshots/home-dark-default.png).

Secondary pills on the press page (App Store, Mastodon, Threads, Instagram, Bluesky, Website) are one-off colours, not the brand accent. After a click the label becomes "Copied!". Shown in [screenshots/press-light-copied.png](screenshots/press-light-copied.png).

## Icon button

Phone header: "Open navigation menu" and "Close navigation menu". No separate icon file. Shown in [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Link

Nav links are Aquawax Pro Medium 15px, `light.muted` (`#666666`), `dark.muted` (`#999999`). Hover shifts the colour toward the accent over 0.4s `cubic-bezier(0.44, 0, 0.56, 1)`. Footer links on the orange band are white. Article links inside an open help row use the accent.

## Text field

Newsletter email on `/news`: height 42px, radius 40px, fill `light.surface` (`#f2f2f2`), placeholder `name@email.com`. Focused empty. Not typed into. Not submitted. Shown in [screenshots/news-light-newsletter-focus.png](screenshots/news-light-newsletter-focus.png).

Help search field sits in a dialog: white pill, placeholder `Search...`, over a scrim `rgba(46, 46, 46, 0.6)`. Shown in [screenshots/help-light-search.png](screenshots/help-light-search.png).

## Text area, select, checkbox, radio, switch

Not present on the public site.

## Tabs

Not present. The home carousel Previous and Next buttons step marketing images. They are not tabs.

## Menu

Phone navigation menu, opened by "Open navigation menu". Items: News, Foodnoms+, Help, Get the App. Shown in [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) and [screenshots/mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png).

## Tooltip, toast

Not present. Press "Copied!" is the button label changing, not a toast.

## Dialog

Help search opens a dialog with a scrim. Shown in [screenshots/help-light-search.png](screenshots/help-light-search.png) and [screenshots/help-dark-search.png](screenshots/help-dark-search.png).

## Card

Feature tiles on the home page: radius 25px, fill `#f2f2f2` in light and `#1a1a1a` in dark. News cards are image-plus-title links. Shown in [screenshots/home-light-full.png](screenshots/home-light-full.png) and [screenshots/news-light-default.png](screenshots/news-light-default.png).

## List row

Help categories are rows with a plus that becomes an x when open. Opening reveals article links. Shown in [screenshots/help-light-accordion.png](screenshots/help-light-accordion.png).

## Table, avatar, badge

Not present.

## Gaps

- No signed-in app components. The product UI in the home screenshots is a marketing composite.
- Disabled, loading, and error states of the newsletter form were not reached, because the form was not submitted.
- Pressed fill on Get the App is Not captured as a separate value.
- Icon SVGs were not extracted (`docs/RIGHTS.md`).
