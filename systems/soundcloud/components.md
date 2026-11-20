# SoundCloud components

Public pages only, captured 2026-11-21. Crops are cut from the screenshots. Values are token names. A state that was not on screen is Not captured.

## Button

Desktop header. Create account is a white pill, 32px tall, radius 9999px, label 14px weight 600. Sign in is the same size with no fill.

| State | Crop | Tokens |
|---|---|---|
| Default | [button-create-default.png](components/crops/button-create-default.png) | `dark.component.button.bg`, `dark.component.button.text`, `core.radius.pill`, `core.size.button` |
| Hover | [button-create-hover.png](components/crops/button-create-hover.png) | Label fades to 40%. Fill does not change. Not a separate colour token. |
| Focus | [button-create-focus.png](components/crops/button-create-focus.png) | `dark.color.focus` as a 2px inset ring |
| Sign in | [button-signin-default.png](components/crops/button-signin-default.png) | Text `dark.color.text` on `dark.color.page` |
| Sign in hover | [button-signin-hover.png](components/crops/button-signin-hover.png) | Label fades to 40% white |
| Follow | [button-follow-default.png](components/crops/button-follow-default.png) | White pill on the profile. Same family as Create account. |
| Phone | [button-listen-in-app.png](components/crops/button-listen-in-app.png) | `light.component.button.*`, radius 4px, height 40px |

Pressed, disabled, and loading were not captured.

## Icon button

The header more control is three dots. [icon-button-more-default.png](components/crops/icon-button-more-default.png). Size was not measured as its own token.

## Link

Player links are `dark.color.link` (#699fff). Learn More in the banner is one. Help Center uses orange for the inline "here" link. Checkout uses `light.color.link` (#044dd2).

## Text field

Desktop search: [text-field-search-default.png](components/crops/text-field-search-default.png), focused [text-field-search-focus.png](components/crops/text-field-search-focus.png). 440 by 36, radius 3px, fill `dark.color.surface`, caret `core.color.orange`. Focus border is a translucent grey, not tokenised.

Phone search: [text-field-search-mobile.png](components/crops/text-field-search-mobile.png). The fill in `light.component.field.bg` is Sampled.

## Text area, select, checkbox, radio, switch

Not present on the public pages opened.

## Tabs

Search filters: [tabs-search-default.png](components/crops/tabs-search-default.png) and [tabs-search-tracks-filters.png](components/crops/tabs-search-tracks-filters.png). The selected tab is a white pill. Profile uses a text tab with an underline (All, Popular tracks, Tracks, Albums, Playlists, Reposts) in [profile-dark-default.png](screenshots/profile-dark-default.png).

Phone tabs are a text row with an underline, in [mobile-search-light-results.png](screenshots/mobile-search-light-results.png).

## Menu

Settings and more: [menu-settings-open.png](components/crops/menu-settings-open.png). Track more: [menu-track-more.png](components/crops/menu-track-more.png). Items are Add to Next up, Add to Playlist, Station. A share menu is in [share-menu-dark-open.png](screenshots/share-menu-dark-open.png).

## Tooltip

Not captured. No tooltip was held.

## Dialog

Keyboard shortcuts: [dialog-shortcuts-open.png](components/crops/dialog-shortcuts-open.png). Language: [dialog-language-open.png](components/crops/dialog-language-open.png). Sign-in wall: [dialog-signin-wall.png](components/crops/dialog-signin-wall.png). The wall is an iframe. Its inner colours were not read. Facebook, Google, and Apple were not clicked.

## Toast

Not present.

## Card

Playlist tile: [card-playlist.png](components/crops/card-playlist.png). Help topic: [card-help-topic.png](components/crops/card-help-topic.png). Plan card: [card-plan.png](components/crops/card-plan.png).

## List row

A playing search row: [list-row-playing.png](components/crops/list-row-playing.png). Artwork, title, waveform, counts.

## Table

Not present.

## Avatar

Profile avatar sits on the banner in [profile-dark-default.png](screenshots/profile-dark-default.png). A verified mark is a blue check. The blue was not read as its own token.

## Badge

Genre tags such as # Dance & EDM are small grey pills on search rows. Their fill was not measured separately.

## Gaps

- Pressed, disabled, loading, error, toast, table, checkbox, radio, switch, text area, select, tooltip: not captured or not present.
- Sign-in iframe colours: Not captured. The iframe is cross-origin.
- Phone search fill: Sampled.
- Icons are not extracted. The logo and waveform are SoundCloud artwork ([docs/RIGHTS.md](../../docs/RIGHTS.md)).
