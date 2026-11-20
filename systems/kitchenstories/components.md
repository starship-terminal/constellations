# Kitchen Stories components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from kitchenstories.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or bought. The search opener and the phone hamburger are local UI toggles. Checkout, profile, cart and rating submit were never followed. The consentmanager overlay was hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (44 components, 81 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (81 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://www.kitchenstories.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [search-open](screenshots/home-light-search-open.png) |
| Recipe index | `https://www.kitchenstories.com/rezepte` | [default](screenshots/recipes-light-default.png), [full](screenshots/recipes-light-full.png) |
| Category (Backen) | `https://www.kitchenstories.com/backen` | [default](screenshots/category-light-default.png), [full](screenshots/category-light-full.png) |
| Recipe | `https://www.kitchenstories.com/huhnersuppe-mit-zitrone-a-a/192140` | [default](screenshots/recipe-light-default.png), [full](screenshots/recipe-light-full.png) |
| Stories | `https://www.kitchenstories.com/stories` | [default](screenshots/stories-light-default.png), [full](screenshots/stories-light-full.png) |
| Search results | `https://www.kitchenstories.com/?s=pasta` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Partners | `https://www.kitchenstories.com/partners` | [default](screenshots/partners-light-default.png), [full](screenshots/partners-light-full.png) |
| Team | `https://www.kitchenstories.com/team` | [default](screenshots/team-light-default.png), [full](screenshots/team-light-full.png) |
| Author | `https://www.kitchenstories.com/author/johanna` | [default](screenshots/author-light-default.png), [full](screenshots/author-light-full.png) |
| Contact | `https://www.kitchenstories.com/kontakt` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Impressum | `https://www.kitchenstories.com/impressum` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| About | `https://pages.kitchenstories.com/de/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| App marketing | `https://pages.kitchenstories.com/de/app` | [default](screenshots/app-light-default.png), [full](screenshots/app-light-full.png) |
| Plus | `https://pages.kitchenstories.com/de/plus` | [default](screenshots/plus-light-default.png), [full](screenshots/plus-light-full.png) |
| Career | `https://pages.kitchenstories.com/de/career` | [default](screenshots/career-light-default.png), [full](screenshots/career-light-full.png) |
| English path (410) | `https://www.kitchenstories.com/en` | [default](screenshots/missing-light-default.png) |
| Home, phone | `https://www.kitchenstories.com/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Recipe, phone | `https://www.kitchenstories.com/huhnersuppe-mit-zitrone-a-a/192140` | [default](screenshots/mobile-recipe-light-default.png), [full](screenshots/mobile-recipe-light-full.png) |
| Recipe index, phone | `https://www.kitchenstories.com/rezepte` | [default](screenshots/mobile-recipes-light-default.png), [full](screenshots/mobile-recipes-light-full.png) |
| Plus, phone | `https://pages.kitchenstories.com/de/plus` | [default](screenshots/mobile-plus-light-default.png), [full](screenshots/mobile-plus-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search field open | home header | the Suche öffnen button, clicked locally, then Escape | [home-light-search-open](screenshots/home-light-search-open.png) |
| Phone menu | home at 390 | the visible hamburger, clicked locally | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Plus checkout link | Plus marketing | measured at rest, never followed | boundary; see Gaps |
| Recipe cart and rating submit | recipe page | measured at rest, never clicked | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus. 2 draw an outline ring: `plus-cta` (1px auto #005fcc, offset 1px), `plus-nav` (1px auto #005fcc, offset 1px). 1 change only their border: `search-submit`. The other 8 show no measured change: `nav-link`, `nav-plus`, `search-open`, `footer-link`, `page-link`, `app-cta`, `m-menu`, `m-menu-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.11s | `ease-in-out` | color, opacity | app-cta, author-link, card-title, footer-link, m-menu-link, nav-link, nav-plus, page-link and more |
| 0.15s | `ease-in-out` | background | m-menu, search-open, search-submit |
| 0.2s | `ease-in-out` | color | plus-cta, plus-nav |
| 0.25s | `ease` | transform | header, m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Recipe card](#recipe-card) | 970 x 357.75 | - | - | transparent | none | 0 |
| [Index card](#index-card) | 308.39 x 376.19 | - | - | transparent | none | 0 |
| [Story card](#story-card) | 308.39 x 376.19 | - | - | transparent | none | 0 |
| [Result card](#result-card) | 322 x 324.69 | - | - | transparent | none | 0 |
| [Recipe card block](#recipe-card-block) | 655 x 3789.75 | - | - | #ffffff `light.page` | none | 0 |

## Components

### Navigation and site chrome

The sticky magazine header: the Kitchen Stories wordmark, primary links (Rezepte, Artikel, App, Plus, Unsere Partner) and the search opener. At 1440 the links sit in the bar. At 390 they move into the hamburger panel.

#### Site header
The sticky magazine header: wordmark, primary links (Rezepte, Artikel, App, Plus, Partner) and the search and menu buttons. Read as `header` on the home page.

**Values (default).** size 1440 x 84.77; border B: 1px solid #e3e3e3; background #ffffff `light.page`; text Plus Jakarta Sans 15/18.75 600, #000000 `light.link`; transition transform 0.25s ease; icon 28 x 28, #000000 `light.link`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Site header default](components/crops/header-default.png)

#### Primary nav link
The "Rezepte" link in the header; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 60.36 x 19; background transparent; text Plus Jakarta Sans 15/18.75 600, #000000 `light.link`; transition color 0.11s ease-in-out; layers ::before rgb(0, 0, 0) 0px none 1; a::before 60.3594pxx1px rgb(0, 0, 0) |
| hover, pressed | opacity 0.75 |

Child layers that carry the look: a::before 60.3594pxx1px background #000000 `light.link`.

![Primary nav link default](components/crops/nav-link-default.png) ![Primary nav link hover](components/crops/nav-link-hover.png) ![Primary nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Primary nav link pressed](components/crops/nav-link-pressed.png)

#### Plus link
The "Plus" marketing link; measured, never followed. Checkout sits behind it. Read as `nav-plus` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 30.13 x 19; background transparent; text Plus Jakarta Sans 15/18.75 600, #000000 `light.link`; transition color 0.11s ease-in-out; layers ::before rgb(0, 0, 0) 0px none 1; a::before 30.125pxx1px rgb(0, 0, 0) |
| hover, pressed | opacity 0.75 |

Child layers that carry the look: a::before 30.125pxx1px background #000000 `light.link`.

![Plus link default](components/crops/nav-plus-default.png) ![Plus link hover](components/crops/nav-plus-hover.png) ![Plus link focus-visible](components/crops/nav-plus-focus-visible.png) ![Plus link pressed](components/crops/nav-plus-pressed.png)

#### Wordmark
The Kitchen Stories wordmark linking home. Read as `wordmark` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97 x 63.77; background transparent; text Plus Jakarta Sans 16/16 500, #515151 `light.muted`; transition color 0.11s ease-in-out |
| hover | text Plus Jakarta Sans 16/16 500, #111111 `light.ink` |

![Wordmark default](components/crops/wordmark-default.png) ![Wordmark hover](components/crops/wordmark-hover.png)

#### Open search
The "Suche öffnen" button. Measured at rest; the field itself is measured after it opens. Read as `search-open` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 28 x 36.34; padding 5px 0px 0px 0px; radius 5px; background transparent; text Plus Jakarta Sans 12.8/15.36 700, #000000 `light.link`; transition background 0.15s ease-in-out; icon 28 x 28, #000000 `light.link` |
| hover, pressed | opacity 0.7 |

![Open search default](components/crops/search-open-default.png) ![Open search hover](components/crops/search-open-hover.png) ![Open search focus-visible](components/crops/search-open-focus-visible.png) ![Open search pressed](components/crops/search-open-pressed.png)

#### Search field
The header search field (placeholder "Suche …"). Focused and typed into, then cleared. Enter is never pressed. Read as `search-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 298 x 41.97; padding 7.2px 50px 7.2px 13.2px; border 1px solid #cccccc `light.border`; background #ffffff `light.page`; text Plus Jakarta Sans 16/25.6 400, #111111 `light.ink`; placeholder #757575 |
| focused, filled | border 1px solid #111111 `light.ink` |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png) ![Search field filled](components/crops/search-field-filled.png)

#### Search submit
The search submit control. Measured, never pressed. Read as `search-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 37.97; padding 0px 10px; radius 5px; background transparent; text Plus Jakarta Sans 12.8/15.36 700, #111111 `light.ink`; transition background 0.15s ease-in-out; icon 28 x 28, #111111 `light.ink` |
| hover, focus-visible, pressed | text Plus Jakarta Sans 12.8/15.36 700, #212121 `light.ink-strong`; icon 28 x 28, #212121 `light.ink-strong` |

![Search submit default](components/crops/search-submit-default.png) ![Search submit hover](components/crops/search-submit-hover.png) ![Search submit focus-visible](components/crops/search-submit-focus-visible.png) ![Search submit pressed](components/crops/search-submit-pressed.png)

#### Menu toggle
The desktop menu button. Measured before search opens, because opening search slides the header. The opened state is a local toggle; its links are never followed. Read as `menu-toggle` on the home page.

Not on the page when it was captured.

### Home page

The German homepage: Rezept des Tages, a trending rail, and category bands. The visible page title is the site wordmark, not a separate headline.

#### Home title
The home page heading. Read as `home-h1` on the home page.

**Values (default).** size 97 x 46.06; background transparent; text Plus Jakarta Sans 19.2/23.04 700, #000000 `light.link`.

![Home title default](components/crops/home-h1-default.png)

#### Recipe card
A home recipe card: thumbnail, time, category, title and author. Read as `recipe-card` on the home page.

**Values (default).** size 970 x 357.75; background transparent; text Plus Jakarta Sans 12/19.2 500, #212121 `light.ink-strong`; layers figure.post-thumbnail 477.0x357.8 rgb(255, 255, 255) 5px; span.time-label 50.7x19.2 rgb(255, 245, 198) 10px.

Child layers that carry the look: figure 477x357.8 background #ffffff `light.page` radius 5px; span 50.7x19.2 background #fff5c6 radius 10px.

![Recipe card default](components/crops/recipe-card-default.png)

#### Card title
A recipe card title link. Measured, never followed. Read as `card-title` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 428.64 x 106; background transparent; text Spectral 38/48 600, #212121 `light.ink-strong`; transition color 0.11s ease-in-out |

![Card title default](components/crops/card-title-default.png) ![Card title hover](components/crops/card-title-hover.png)

#### Card meta
Category or time meta on a recipe card. Read as `card-meta` on the home page.

**Values (default).** size 477 x 50; background transparent; text Plus Jakarta Sans 12/19.2 500, #fc642d.

![Card meta default](components/crops/card-meta-default.png)

#### Author link
An author byline link. Measured, never followed. Read as `author-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 51.67 x 19.19; background transparent; text Plus Jakarta Sans 12/19.2 500, #fc642d; transition color 0.11s ease-in-out |
| hover | text Plus Jakarta Sans 12/19.2 500, #d4562a |

![Author link default](components/crops/author-link-default.png) ![Author link hover](components/crops/author-link-hover.png)

### Recipe index

The /rezepte archive: category chips, a card grid, and numbered pagination. The index has no page h1.

#### Index title
The recipes index heading. Read as `index-h1` on the recipe index page.

Not on the page when it was captured.

#### Index card
A recipe card on the /rezepte index. Read as `index-card` on the recipe index page.

**Values (default).** size 308.39 x 376.19; background transparent; text Plus Jakarta Sans 12/19.2 500, #212121 `light.ink-strong`; layers figure.post-thumbnail 308.4x250.0 rgb(255, 255, 255) 16px; span.time-label 50.7x19.2 rgb(255, 245, 198) 10px; span.cat-links 0.0x0.0 rgb(206, 236, 156) 12px.

Child layers that carry the look: figure 308.4x250 background #ffffff `light.page` radius 16px; span 50.7x19.2 background #fff5c6 radius 10px; span 0x0 background #ceec9c radius 12px.

![Index card default](components/crops/index-card-default.png)

#### Pagination
The archive pagination. Measured, never followed. Read as `pagination` on the recipe index page.

**Values (default).** size 980 x 40.34; background transparent; text Plus Jakarta Sans 12.8/15.36 700, #ffffff `light.page`; icon 22 x 22, #515151 `light.muted`; layers span.page-numbers.current 39.1x40.3 rgb(20, 95, 72) 50px.

Child layers that carry the look: span 39.1x40.3 background #145f48 radius 50px.

![Pagination default](components/crops/pagination-default.png)

#### Page link
A pagination page link. Measured, never followed. Read as `page-link` on the recipe index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 38.75 x 40.34; padding 10px 15px 5px 15px; background transparent; text Plus Jakarta Sans 14.08/16.89 400, #212121 `light.ink-strong`; transition color 0.11s ease-in-out |

![Page link default](components/crops/page-link-default.png) ![Page link hover](components/crops/page-link-hover.png) ![Page link focus-visible](components/crops/page-link-focus-visible.png) ![Page link pressed](components/crops/page-link-pressed.png)

### Recipe page

A public recipe (WP Recipe Maker): title, author, ingredients, instructions, rating at rest, and an app link. Cart and rating submit were not used.

#### Recipe title
The recipe headline. Read as `recipe-h1` on the recipe page.

**Values (default).** size 970 x 38.39; background transparent; text Spectral 32/38.4 600, #212121 `light.ink-strong`.

![Recipe title default](components/crops/recipe-h1-default.png)

#### Recipe card block
The WP Recipe Maker card: image, name, rating, ingredients, utensils, nutrition and steps. The cart and rating submit inside it were not pressed. Read as `recipe-card-block` on the recipe page.

**Values (default).** size 655 x 3789.75; background #ffffff `light.page`; text Plus Jakarta Sans 27/35.1 700, #212121 `light.ink-strong`.

![Recipe card block default](components/crops/recipe-card-block-default.png)

#### Recipe name
The recipe name inside the card. Read as `recipe-name` on the recipe page.

**Values (default).** size 655 x 35.09; background transparent; text Plus Jakarta Sans 27/35.1 700, #212121 `light.ink-strong`.

![Recipe name default](components/crops/recipe-name-default.png)

#### Rating
The star rating. Measured at rest. The rating form was not submitted. Read as `rating` on the recipe page.

**Values (default).** size 277.53 x 51; background transparent; text Plus Jakarta Sans 12/24 400, #212121 `light.ink-strong`; icon 24.75 x 24.75, #212121 `light.ink-strong`.

![Rating default](components/crops/rating-default.png)

#### Ingredients heading
The "Zutaten" heading inside the recipe card. Read as `ingredient-heading` on the recipe page.

**Values (default).** size 655 x 42.97; padding 8px 0px; radius 15px; background #ffffff `light.page`; text Plus Jakarta Sans 19.95/25.93 700, #212121 `light.ink-strong`.

![Ingredients heading default](components/crops/ingredient-heading-default.png)

#### Ingredient row
One ingredient row. Read as `ingredient` on the recipe page.

**Values (default).** size 585 x 30; padding 0px 0px 5px 0px; border B: 1px solid #eeeeee; background transparent; text Plus Jakarta Sans 15/24 400, #212121 `light.ink-strong`; layers li.wprm-recipe-ingredient 585.0x30.0 B:1px solid rgb(238, 238, 238); input.wprm-checkbox 16.0x20.0 rgb(255, 255, 255) T:1px solid rgb(204, 204, 204) / R:1px solid rgb(204, 204, 204) / B:1px solid rgb(204, 204, 204) / L:1px solid rgb(204, 204, 204) 2px; input::before.wprm-checkbox 24pxx24px; label::before.wprm-checkbox-label 16pxx16px rgb(255, 255, 255) T:1px double rgb(243, 243, 240) / R:1px doubl.

Child layers that carry the look: li 585x30 border 1px solid #eeeeee; input 16x20 background #ffffff `light.page` border 1px solid #cccccc `light.border` radius 2px; input::before 24pxx24px image url(data:…).

![Ingredient row default](components/crops/ingredient-default.png)

#### Steps heading
The "Zubereitung" heading inside the recipe card. Read as `instruction-heading` on the recipe page.

**Values (default).** size 655 x 64; padding 8px 0px; radius 15px; background #ffffff `light.page`; text Plus Jakarta Sans 19.95/25.93 700, #212121 `light.ink-strong`; icon 18.19 x 18.19, #000000 `light.link`.

![Steps heading default](components/crops/instruction-heading-default.png)

#### Step
One preparation step. Read as `instruction` on the recipe page.

**Values (default).** size 595 x 633.5; background transparent; text Plus Jakarta Sans 15/24 400, #212121 `light.ink-strong`.

![Step default](components/crops/instruction-default.png)

#### Next step
The "Weiter" step control if the template renders one. Measured, never used to submit. Read as `step-nav` on the recipe page.

Not on the page when it was captured.

#### Body paragraph
A paragraph of the recipe story. Read as `body` on the recipe page.

**Values (default).** size 655 x 84; background transparent; text Plus Jakarta Sans 15/28 500, #212121 `light.ink-strong`.

![Body paragraph default](components/crops/body-default.png)

#### App call to action
An app download call to action. Measured, never followed. Read as `app-cta` on the recipe page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 30.39 x 19; background transparent; text Plus Jakarta Sans 15/18.75 600, #000000 `light.link`; transition color 0.11s ease-in-out; layers ::before rgb(0, 0, 0) 0px none 1; a::before 30.3906pxx1px rgb(0, 0, 0) |
| hover, pressed | opacity 0.75 |

Child layers that carry the look: a::before 30.3906pxx1px background #000000 `light.link`.

![App call to action default](components/crops/app-cta-default.png) ![App call to action hover](components/crops/app-cta-hover.png) ![App call to action focus-visible](components/crops/app-cta-focus-visible.png) ![App call to action pressed](components/crops/app-cta-pressed.png)

### Stories

The /stories index of article cards.

#### Stories title
The stories index heading. Read as `stories-h1` on the stories page.

Not on the page when it was captured.

#### Story card
A story card on /stories. Read as `story-card` on the stories page.

**Values (default).** size 308.39 x 376.19; background transparent; text Plus Jakarta Sans 15/26 600, #212121 `light.ink-strong`; layers figure.post-thumbnail 308.4x250.0 rgb(255, 255, 255) 16px; span.cat-links 0.0x0.0 rgb(206, 236, 156) 12px.

Child layers that carry the look: figure 308.4x250 background #ffffff `light.page` radius 16px; span 0x0 background #ceec9c radius 12px.

![Story card default](components/crops/story-card-default.png)

#### Story title
A story title on the /stories index. The index has no page h1. Read as `stories-title` on the stories page.

**Values (default).** size 308.39 x 52; background transparent; text Plus Jakarta Sans 15/26 600, #212121 `light.ink-strong`.

![Story title default](components/crops/stories-title-default.png)

### Search

Public search results for the query pasta, loaded by URL. The field was typed into and cleared, never submitted.

#### Results heading
The search results heading ("SUCHERGEBNISSE") for the public query pasta. Read as `results-h1` on the search page.

**Values (default).** size 650 x 24; background transparent; text Plus Jakarta Sans 20/24 700, #212121 `light.ink-strong`.

![Results heading default](components/crops/results-h1-default.png)

#### Results field
The search field on the results page. Typed into and cleared. Never submitted from this pass. Read as `results-field` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 648 x 41.97; padding 7.2px 50px 7.2px 13.2px; border 1px solid #cccccc `light.border`; background #ffffff `light.page`; text Plus Jakarta Sans 16/25.6 400, #111111 `light.ink`; placeholder #757575 |
| focused, filled | border 1px solid #111111 `light.ink` |

![Results field default](components/crops/results-field-default.png) ![Results field focused](components/crops/results-field-focused.png) ![Results field filled](components/crops/results-field-filled.png)

#### Result card
A search result card. Read as `result-card` on the search page.

**Values (default).** size 322 x 324.69; background transparent; text Plus Jakarta Sans 12/19.2 500, #212121 `light.ink-strong`; layers figure.post-thumbnail 322.0x247.7 rgb(255, 255, 255) 5px; span.time-label 50.7x19.2 rgb(255, 245, 198) 10px.

Child layers that carry the look: figure 322x247.7 background #ffffff `light.page` radius 5px; span 50.7x19.2 background #fff5c6 radius 10px.

![Result card default](components/crops/result-card-default.png)

### Footer



#### Footer
The site footer: follow links, legal links and the published hello@kitchenstories.de contact. Read as `footer` on the home page.

**Values (default).** size 1440 x 500.97; background #fff5ea `light.footer`; text Plus Jakarta Sans 16/19.2 600, #000000 `light.link`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Footer default](components/crops/footer-default.png)

#### Footer link
A legal footer link. Measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 66.11 x 29; padding 2.5px 0px; background transparent; text Plus Jakarta Sans 12/24 500, #585450; transition opacity 0.11s ease-in-out |
| hover, pressed | opacity 0.7 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Plus marketing



#### Plus heading
The Plus marketing headline on pages.kitchenstories.com. Read as `plus-h1` on the Plus marketing page.

**Values (default).** size 655.55 x 212; padding 20px 0px 0px 0px; background transparent; text Fam-aime 64/64 600, #000000 `light.link`.

![Plus heading default](components/crops/plus-h1-default.png)

#### Start free link
The "Jetzt kostenlos starten" link to /de/checkout. Measured, never followed. Checkout is a gated surface. Read as `plus-cta` on the Plus marketing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 218.13 x 56.95; padding 16px 24px; radius 50px; background #621863; text Tt commons 19.2/24.96 400, #ffffff `light.page`; transition color 0.2s ease-in-out |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Start free link default](components/crops/plus-cta-default.png) ![Start free link hover](components/crops/plus-cta-hover.png) ![Start free link focus-visible](components/crops/plus-cta-focus-visible.png) ![Start free link pressed](components/crops/plus-cta-pressed.png)

#### Marketing nav link
A pages.kitchenstories.com nav link. Measured, never followed. Read as `plus-nav` on the Plus marketing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 178.67 x 29.39; background transparent; text Tt commons 19.6/29.4 600, #000000 `light.link`; transition color 0.2s ease-in-out |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.heading-433.no-underline 178.7x29.4 1px auto rgb(0, 95, 204) offset 1px |

![Marketing nav link default](components/crops/plus-nav-default.png) ![Marketing nav link hover](components/crops/plus-nav-hover.png) ![Marketing nav link focus-visible](components/crops/plus-nav-focus-visible.png) ![Marketing nav link pressed](components/crops/plus-nav-pressed.png)

### Mobile (390 wide)



#### Mobile header
The phone header. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64.77; border B: 1px solid #e3e3e3; background #ffffff `light.page`; text Plus Jakarta Sans 19.2/23.04 700, #000000 `light.link`; transition transform 0.25s ease; icon 28 x 28, #000000 `light.link`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu
The painted phone hamburger. The first .mobile-menu-toggle sits off-canvas in the header track. Opened as a local toggle; links not followed. Read as `m-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed, opened) | size 34.5 x 30; radius 5px; background transparent; text Plus Jakarta Sans 12.8/15.36 700, #000000 `light.link`; transition background 0.15s ease-in-out; icon 30 x 30, #000000 `light.link` |

![Mobile menu default](components/crops/m-menu-default.png) ![Mobile menu hover](components/crops/m-menu-hover.png) ![Mobile menu focus-visible](components/crops/m-menu-focus-visible.png) ![Mobile menu pressed](components/crops/m-menu-pressed.png) ![Mobile menu opened](components/crops/m-menu-opened.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 390 x 1366.83; background #fff5ea `light.footer`; text Plus Jakarta Sans 16/19.2 600, #000000 `light.link`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Mobile footer default](components/crops/m-footer-default.png)

### Menus and overlays



#### Mobile menu link
A link in the opened phone menu. Measured, never followed. Read as `m-menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 66.39 x 34.59; padding 4.5px 0px; background transparent; text Plus Jakarta Sans 16/25.6 500, #000000 `light.link`; transition color 0.11s ease-in-out |
| hover, pressed | opacity 0.75 |

![Mobile menu link default](components/crops/m-menu-link-default.png) ![Mobile menu link hover](components/crops/m-menu-link-hover.png) ![Mobile menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Mobile menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile menu panel
The phone nav panel opened by the hamburger. Links measured, never followed. Read as `m-menu-panel` on the home page.

**Values (default).** size 354 x 195.47; background transparent; text Plus Jakarta Sans 16/25.6 500, #000000 `light.link`; ancestors aside.mobile-sidebar bg #ffffff `light.page`.

![Mobile menu panel default](components/crops/m-menu-panel-default.png)

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark, search mark, hamburger and social glyphs are visible in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

Kitchen Stories has account, checkout and shop surfaces that this pass did not enter. Plus 'Jetzt kostenlos starten' links to https://www.kitchenstories.com/de/checkout. The account page at https://www.kitchenstories.com/profile says the account is moving and was not signed into. Recipe cart buttons and the rating submit control were left at rest.

### Pages

- **Checkout.** https://www.kitchenstories.com/de/checkout was not opened. The Plus CTA that points there was measured.
- **Account.** https://www.kitchenstories.com/profile was not signed into. /login and /anmelden return 404.
- **English magazine.** https://www.kitchenstories.com/en and /en/recipes return 410. The live public magazine is German.
- **Native app host.** https://app.kitchenstories.com does not resolve. App marketing is https://pages.kitchenstories.com/de/app.
- **Recipe shop.** Cart and 'Zum Warenkorb' on the recipe page were not clicked. Rating submit was not clicked.
- **Contact form.** https://www.kitchenstories.com/kontakt was captured as a page. No form was submitted.

### States

- **Pressed** was forced with DevTools on controls that were measured that way. Nothing a real press would submit was pressed.
- **The phone menu and search field** were opened by their own triggers. Search text was typed and deleted.
- **Desktop hamburger.** `button.desktop-menu-toggle` exists in the header track at about x 2775 with visibility hidden. It is not painted in the 1440 viewport. The desktop nav is the inline links.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One painted theme, no toggle: a white field, #111111 ink, a #fff5ea footer and a #dd3333 call-to-action, set in Plus Jakarta Sans. tokens.json emits light only.

### Fonts

- **Plus Jakarta Sans** is the face the magazine paints for body and headers. Barlow, Spectral, ttcommons, aime and Font Awesome are also served as @font-face. None of those files are shipped in this package. The style guide falls back to system faces.

### Screenshots

- Photography, cover art and author names shown in stories are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article text, headlines, captions and photography are the product's content; only frames and components were measured.
