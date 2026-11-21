# Components

Public signed-out Prime Video, captured 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops are from the full-colour captures, then quantised.

## Button

Join Prime in the header is the only blue control on the public pages. Height 42px, radius 8px, label 16px medium, letter-spacing 0.64px. Fill is `dark.color.accent.default` (rgba(26, 152, 255, 0.8)) with `dark.shadow.accent`. Hover and pressed both resolve to `dark.color.accent.hover` (`#1A98FF`); the hover glow is `dark.shadow.accentHover`. Focus-visible is a 2px `dark.color.border.focus` outline.

The hero buttons (Prime Member? Sign in, Start your 30-day free trial) are white on the page colour: `dark.color.bg.buttonInverse`, `dark.color.text.onInverse`, height 62px, label 20px medium.

Crops: [button-join-default.png](components/crops/button-join-default.png), [button-join-hover.png](components/crops/button-join-hover.png), [button-join-focus.png](components/crops/button-join-focus.png), [button-signin-default.png](components/crops/button-signin-default.png), [button-trial-default.png](components/crops/button-trial-default.png), [button-join-mobile.png](components/crops/button-join-mobile.png).

Disabled, loading and error were not on these pages.

## Icon button

Title-page actions (Watch trailer, Add to Watchlist, Like, Not for me, Share) are 48px circles. Fill `dark.color.bg.iconButton`, 3px border `dark.color.border.iconButton`.

Crop: [icon-button-default.png](components/crops/icon-button-default.png).

Hover, focus and pressed were not measured. Like opens Amazon Sign-In. That branch stopped.

## Link

Nav links are 16px medium, white, padding 0 14px, radius 8px. Inline links on the title page (genre names, cast names) are white with an underline. See more is 20px regular, white, no underline treatment beyond the chevron.

No separate link colour was measured. `dark.color.text.primary` is the only text colour those links used.

## Text field

Search opens a panel. The field is 966x74 on desktop, fill `dark.color.bg.search` (`#33373D`), radius 8px, 20px Amazon Ember, padding 5px 11px 5px 16px. Empty. Nothing was typed.

Crop: [search-field-default.png](components/crops/search-field-default.png).

Focus, filled, error and disabled were not captured. The field was not submitted.

## Tabs

Genre pages use pill chips. Selected All is white fill `dark.color.bg.chipSelected` with `dark.color.text.chipSelected`, height 39px, radius 180px, padding 8px 16px, 20px medium. Unselected Movies and TV shows are transparent with white text.

Title pages use Related and Details. Selected Details shows a white underline. Text stays white.

Crops: [chip-selected-default.png](components/crops/chip-selected-default.png), [tabs-details-default.png](components/crops/tabs-details-default.png).

## Menu

Language menu opens from EN. Account menu opens from the profile icon: a small panel labelled YOUR ACCOUNT, with Sign In, Help and Watch Anywhere. Phone width uses a Menu button that drops Home, Movies, TV shows, Sports, Categories and Join Prime.

Crops: [menu-language-default.png](components/crops/menu-language-default.png), [menu-account-default.png](components/crops/menu-account-default.png), [menu-mobile-default.png](components/crops/menu-mobile-default.png).

The language panel's own fill was not isolated (the measured wrapper was transparent). Treat the crop as Observed.

## Dialog

Share is a dialog, fill `dark.color.bg.dialog` (the page colour), radius 24px, which matches the declared `--fable-dialog-border-top-radius`. Title Share, four share targets, a Copy link bar. Email was not clicked.

Crop: [dialog-share-default.png](components/crops/dialog-share-default.png).

Watch trailer opens a full-screen player. On this capture it showed Video Unavailable with an OK button. See [detail-dark-trailer-unavailable.png](../screenshots/detail-dark-trailer-unavailable.png).

## Card

Poster cards on genre and browse pages are 251x141 with radius 8px (`dark` has no separate poster fill; the artwork is the card). A small lock badge sits on the corner. Detail metadata sits in raised cards: fill `dark.color.bg.card`, 1px `dark.color.border.card`, radius 12px.

Crops: [card-poster-default.png](components/crops/card-poster-default.png), and the cards inside [tabs-details-default.png](components/crops/tabs-details-default.png).

## Badge

Maturity rating NC16 is a small filled label on the title page. The declared Fable heights are 22px, 30px and 34px (`core.fable.badge`). The NC16 node's own fill was not isolated (the measured wrapper was larger than the paint), so the colour is Not captured. The crop shows the label.

Crop: [badge-rating-default.png](components/crops/badge-rating-default.png).

## List row

Help articles and the language list are rows of text. No separate row fill was measured. Observed in [help-dark-default.png](../screenshots/help-dark-default.png) and the language crop.

## Avatar

The signed-out header shows a generic person glyph, not a photo. No avatar component with a name or image was on the public pages.

## Not present on the public pages

Text area, select, checkbox, radio, switch, tooltip, toast, table. A destructive confirmation was not shown. Sign-in is a wall, not a form on primevideo.com.

## Gaps

- Hover, focus and pressed were measured only on Join Prime.
- Search was left empty. No suggestion list, no results page.
- Language items were not selected, so no second locale was captured.
- Like, watchlist, Sign In, Join Prime and Contact Us end at Amazon Sign-In. Password was not submitted.
- No light theme. No status colours (success, warning, danger, info) were painted as roles. The lock mark on posters is artwork, not a token.
- Motion durations: Not captured.
