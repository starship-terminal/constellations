# SeatGeek components

Public signed-out pages only, measured 19 November 2026. Values are computed styles. A colour is followed by the token in [tokens.json](tokens.json) when one matches.

Screenshots and crops are absent. `preview_snapshot` returned "The browser is not producing screenshot frames" twice, and those images were not invented.

## Button

Sign in, on the dark hero: background `rgba(255, 255, 255, 0.12)`, text `#ffffff`, radius `100px`, height `40px`, border `0.5px` `rgba(255, 255, 255, 0.08)`, padding `0 16px`, weight `400`. Token `light.component.button-glass`.

Get updates, in the email modal before it was dismissed: background `#000000`, text `#ffffff`, radius `8px`, height `56px`, padding `16px 24px`, size `17px`, weight `650`. Token `light.component.button-primary`.

Chat with us, on `/help`: background `#ff5b49`, text `#ffffff`, radius `12px`, height `44px`, padding `0 24px`, weight `650`, shadow `rgba(255, 91, 73, 0.3) 0px 6px 16px 0px`. Token `light.component.button-brand`.

Connect, Spotify banner: background `#1ed760`, text `#000000`, radius `9999px`, height `40px`, weight `700`. That green is Spotify's, not a SeatGeek semantic token.

Hover, pressed, disabled and loading were not held. The stylesheet declares primary hover `#000000cf`, success `#055d48` / hover `#024031`, critical `#b61d2f` / hover `#9d0c1d`.

## Icon button

Main menu is a `40px` glass circle, radius `100px`, padding `0 4px`. Close Modal was a `36px` circle with a `2px` white ring and a `4px` black outer ring. Not extracted as an SVG.

## Link

Sports nav link: text `#181818`, size `16px`, weight `400`, padding `12px`, radius `8px`. Logo link computed color `#ff5b49`. Legal-link token `--sg-color-semantic-action-legal-link` is `#1c71ef` and was not confirmed on a painted link.

## Text field

Home search wrap: background `rgba(255, 255, 255, 0.12)`, border `0.5px rgba(255, 255, 255, 0.08)`, radius `100px`, height `46px`. The input itself is transparent, size `14px`, padding `0 32px 0 44px`, placeholder "Search or ask anything".

Help textarea wrap: background `#ffffff`, border `2px #dedddb`, radius `20px`, padding `20px 16px 16px`, shadow `rgba(15, 23, 42, 0.06) 0px 12px 32px 0px`. The textarea is `18px` / `27px`.

## Text area

The help composer is the only textarea measured. See Text field. It was not submitted.

## Select

Not present as a native `<select>` on the pages visited. Location and date are pill buttons that open panels. Those panels were not opened.

## Checkbox, radio, switch

Not on the pages visited. The stylesheet paints them (`.if39jt8` radius `4px`, `.iov00p0` radius `100px`, `.toj2eu3` pill switch, transition `.12s` and `.2s`). Recorded as not present on the public surfaces, not as measured components.

## Tabs

Concert genres (All genres, Pop, Rock) are text links, height `52px`, padding `16px 0`, no filled selected state was the visible one. Not a tab widget.

## Menu

The Sports mega-menu was in the DOM (rows `36px`, padding `8px 12px`, radius `8px`, one row background `#f5f5f4`). It was not opened by a click in this capture, so treat the open state as observed in the DOM, not as an interaction.

## Tooltip

Not observed. Stylesheet keyframes `uniformTooltipFadeIn` and slide variants exist. Not captured as a painted state.

## Dialog

An email dialog ("Become a SeatGeek member!") was open on first load, then dismissed with its Close Modal control. It was not submitted. Its Get updates button is measured above. The dialog container itself reported a transparent background, so the panel fill was not isolated. Gap.

## Toast

Not observed.

## Card

Team row on `/nfl-tickets`: radius `12px`, padding `8px`, height `52px`. Trust card: border `0.5px #dedddb`, radius `12px`, padding `20px 24px`. Event row: padding `16px 0`, title `17px` / `24px` weight `700`, time `#767575` `15px`.

## List row

Event list row as above. City guide links on `/cities` are plain `16px` / `24px` text, color `#181818`, no card chrome.

## Table

A table component exists in the stylesheet (`.e3dx8k0`, semantic surface background, `12px` radius, `16px` cell padding). Not painted on the pages visited.

## Avatar

Not observed on the public pages.

## Badge

Price pill "From $42": background `#181818`, text `#ffffff`, radius `6px`, height `36px`, padding `0 16px`, size `14px`, weight `650`.

## Gaps

- No screenshots and no crops. The preview browser did not produce frames.
- Hover, focus-visible, pressed, disabled, loading and error were not held.
- Checkbox, radio, switch, tooltip, toast, avatar, table and select were not on the public pages.
- Dialog panel fill was not isolated.
- `/login` was a DataDome interstitial and was not passed.
- Checkout, payment and account creation were not entered.
- Phone field "Enter your phone number" was not filled.
