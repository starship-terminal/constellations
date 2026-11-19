# Patterns

## Homepage

Signed-in `https://coolors.co/` at 1169x731. A 60px white header holds the wordmark, a Tools menu, a pink Go Pro label, and an avatar. The h1 is Inter 800, about 94px, letter-spacing about -3.3px, ink `#0a0a0a`, wrapping to three lines: "The super fast / color palettes / generator!". A 20px lede sits under it. Two buttons follow: blue "Start the Generator" and gray "Explore 10M+ Palettes". The right side is a stack of palette thumbnails. Ads sit in the header and as a card; they are not part of the product chrome.

## Generator

`/generate` redirects to a five-color URL such as `/293f14-386c0b-38a700-31d843-3eff8b`. Under the same header, a 56px toolbar says "Press the spacebar to generate color palettes!" on the left (`#525252`, 15px weight 450) and puts View, Export and Save on the right. Five full-height columns fill the rest of the viewport. Each column is the color itself. The hex and the color name sit near the bottom. Hovering a column reveals a vertical stack of icon buttons. Spacebar replaces the palette. A first visit shows a terms dialog, then a Hello dialog, before the columns are usable.

See [screenshots/generate-light-desktop.png](screenshots/generate-light-desktop.png).

## Explore

`/palettes/popular`. Desktop h1 is 70px weight 800, letter-spacing -2.45px. At 390px the header collapses to a menu button and a centered wordmark, the h1 drops to 50px, and palette cards stack with a 30px side inset. A search field accepts colors, topics, styles or hex values. Cards show a row of swatches, a title and a like count.

A clean mobile screenshot was not saved. The 390px numbers are computed styles.
