# Kitchen Stories patterns

How the public magazine is put together. Screenshots are in [screenshots/](screenshots). Component values are in [components.md](components.md).

## Header

At 1440 the header is a white bar: the stacked "kitchen stories" wordmark, then Rezepte, Artikel, App, Plus and Unsere Partner, then a search icon. Opening search replaces the icon with a field and a close control. There is no painted hamburger at this width.

At 390 the same bar keeps the wordmark centred, a search icon on the left and a hamburger on the right. The hamburger opens a white panel of the same five links, a rule, and a row of social icons.

See [home-light-default](screenshots/home-light-default.png), [home-light-search-open](screenshots/home-light-search-open.png) and [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Home feed

The home page opens with "REZEPT DES TAGES": a large photo, a time chip, a serif-scale title and an author. Below that, "Rezepte im Trend" is a horizontal card rail with round previous and next controls. Further bands repeat the same card: photo, time chip, title.

See [home-light-default](screenshots/home-light-default.png) and [home-light-full](screenshots/home-light-full.png).

## Recipe index

`/rezepte` is a card grid with category links and numbered pagination. The index has no page h1. A category such as `/backen` reuses the same grid.

See [recipes-light-default](screenshots/recipes-light-default.png) and [category-light-default](screenshots/category-light-default.png).

## Recipe

A recipe page is a title, an author with a round portrait and a date, a short intro, a hero photo, then the WP Recipe Maker block: ingredients, equipment, nutrition, instructions and a rating control at rest. An app link sits near the card. Cart and rating submit were not used.

See [recipe-light-default](screenshots/recipe-light-default.png).

## Search

Public search is a GET on `/?s=`. Results use the heading "SUCHERGEBNISSE" and the same card shape as the index. The field on the results page was typed into and cleared.

See [search-light-default](screenshots/search-light-default.png).

## Plus

The Plus page on pages.kitchenstories.com is a marketing layout with a large headline and a red "Jetzt kostenlos starten" link. That link points at checkout, which was not opened.

See [plus-light-default](screenshots/plus-light-default.png).

## Footer

The footer is a warm `#fff5ea` band of link columns: follow, about, legal, and brand contact. It is the only large cream surface.

See [footer](components/crops/footer-default.png).
