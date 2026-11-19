# Patterns

How the signed-out pages are built. No page screenshot exists. The layout notes come from the live DOM on 2026-11-19. See [raw/viewport.json](raw/viewport.json).

## App shell

A 60px nav sits over the hero or as a solid `#131313` bar. The wordmark is `/dist/images/logoStocksy.svg`, 95 by 30. Links are 14px / 500. Cart is an injected stroke icon. At 390px the labelled links collapse and a hamburger is present. It was not opened.

The home hero is a full-bleed photo on a `#1f2424` plate, with a white headline at 44px on desktop and 32px at 390, a 20px pitch, and a white search bar with a green submit. Below that, a features panel, collection cards, a pullquote on `#1e1e1e`, category cards, artist rows, an FAQ, and a `#131313` footer.

## Search

`/search/photo?text=ocean` is a public results page. A masthead states the result count. Type chips and a left filter column (ORIENTATION, PEOPLE, AGE, ETHNICITY, LOCATION, COLOR, and others) sit beside a masonry of asset links. Pagination has a disabled Back and an active Next. The query was opened as a URL. Filters were not applied.

## Asset

The photo page shows the image, a row of dark pills (Like, Save, Share, Comp, Similar), a license size picker with one active row, a license use picker, a subtotal, and Add to Cart. Add to Cart was not pressed. The artist pill and keyword links sit under the image.

## Pricing

`/pricing` is a public three-step list: Standard license with image and video prices, extended Team and Enhanced add-ons, then an FAQ. There is no buy button on the page. Prices read on the page: image Medium $35, Large $85, X-Large $135. Video 720p $75, 1080p $175, 4k $300.

## Form

`/business` is a dark marketing page with a request form: first name, last name, email, phone, company, job title, message, and Submit a request. The phone field is why it was not submitted. `/user/login` is email, password, a disabled-looking Log in until the Turnstile completes, and Continue With Google / Facebook. It was not submitted.

## Empty, loading, error

A made-up path returns the product 404: a 44px "404", the line "We can't find that page, sorry.", and three dark pills (Visit Homepage, Browse Curated Collections, Contact Support). The body is the light shell. Loading and empty search states were not captured. Search for "ocean" returned results.

## Themes

Dark is the default on home, search, photo, pricing, category, business, resources and login (`body.dark-mode`). Light is the about page and the 404 shell. No theme toggle was found. `prefers-color-scheme` was not switched.

## Widths

Desktop was read at 1440 by 900 after resize, and once at the fill width 1169 by 731. Phone was read at 390 by 844 on the home. Other pages were not re-read at 390.
