# Unsplash patterns

Public signed-out pages, measured 2026-11-19. No page screenshots: the preview browser did not produce frames.

## Shell

At 1440 the shell is a 64px sticky sidebar and a 64px sticky top bar inset by that sidebar. The top bar padding is `12px 24px`, gap 16px, white. The sidebar padding is 12px. The logo is a 32px viewBox path, painted at 24px, fill `#111111`.

At 390 the sidebar collapses. The nav is 56px tall, padding `8px 12px`, full width. A 40px Menu button sits at x 346. Search remains a 40px pill, 366px wide.

## Search

The home, topic, and search pages share one search form: placeholder "Search photos and illustrations", pill radius 24px, fill `#eeeeee`. A query was not typed. `/s/photos/lighthouse` and `/s/photos/nature` were opened by URL. Results show a Photos tab with a count, an Illustrations count, and filter chips for License, Orientation, and Sort by Relevance. Load more is a full-width outline button, 1296px at 1440, 64px tall.

## Pricing

`/plus` is public. The plan card shows Yearly selected, a struck `$12`, a `$4` price, and "Limited Launch Special". The Get Unsplash+ button is the 44px primary. It was not clicked. Monthly was not selected.

## Photo page

A photo page shows the contributor, Edit image (outline), Download (primary, 32px), Share (outline), a 32px avatar, and tag pills. Both photo URLs opened from search were Unsplash+ photos, licensed under the Unsplash+ License. Download was not clicked.

## License and about

`/license` is a running-text page. The h1 is 28px / 700. The content column measured 966px. `/about` uses a 42px / 700 title, "Unsplash is the internet’s source for visuals.", and 40px section headings.

## Missing page

`/this-page-does-not-exist-capture` rewrote to `/@this-page-does-not-exist-capture` and rendered "Page not found". The title is 72px / 700, white, over a photo. Back to Unsplash is a 44px primary button with `#111111` type on white, the dark-surface primary.

## Login boundary

`/login` shows Email, Password, a 44px Login button, and a Join link to `/join`. The fields were focused for the outline and left empty. Nothing was submitted.

## Coverage

| Pattern | State |
|---|---|
| App shell | Measured at 1440 and 390 |
| Search | Results opened by URL. The field was not submitted from the home page |
| Pricing | Card measured. Checkout not entered |
| Photo | Plus photos only. Download not clicked |
| License and about | Measured |
| 404 | Measured |
| Login | Measured, not submitted |
| Empty, loading, error, destructive confirm | Not on the public pages |
