# Components

Measured on tripadvisor.com, signed out, 2026-11-19. Values are computed styles. There are no crops: the preview browser did not produce screenshot frames, and headless Playwright was stopped by a captcha.

## Button

Sign in is a pine pill: background `#002B11`, text `#F7F7F7`, radius `1000px`, padding `9px 15px`, height 40px. The label computed 700 16px/20px.

Search and See tickets are the brand pill: background `#00EB5B`, border `1px solid #00AB42`, text `#002B11`, radius `1000px`. Search height was 48px. See tickets height was 40px.

Book now is pine with radius 28px, padding `18px 24px`, height 52px.

Continue with Google is white, `2px solid #002B11`, radius 28px, height 48px, label 700 14px/18px.

The login Sign in submit is pine, radius 28px, height 56px, padding `18px 24px`, label 700 16px/18px, text `#FFFFFF`.

Tokens: `light.color.action.primary.background`, `light.color.action.brand.background`, `core.radius.full`.

## Search field

The home shell at rest is white, `1px solid #768A79`, radius `1000px`, shadow `0 2px 4px #00000029`, height 58px. The input is 16px/24px, colour `#38443A`, placeholder "Places to go, things to do, hotels...".

Focused, with the suggestion list open, the shell computed `2px solid #F7F7F7`, radius 12px, shadow `0 2px 12px #00000029`.

At 390px the shell was 342px wide and stayed a full pill.

## Text field

Login email and password, and the join name fields, are `#F7F7F7`, `2px solid #768A79`, radius 4px, height 48px, padding `4px 4px 4px 8px`, font 14px. The label computed 600 14px/18px. Weight 600 is not a `--trip-sans-*` token (those are 400, 700, 800, 900).

Hotel destination, dates, and guests are white, height 48px, radius 12px, border `1px solid #768A79`. Check-in, while it opened the calendar, computed `2px solid #002B11` and radius `12px 0 0 12px`.

## Card

Home experience images sit in an 8px radius wrapper, overflow hidden, fill `#F7F7F7`. The title is 700 16px/20px `#002B11`. The rating number is 14px/18px `#38443A`. "from $3 per adult" is 700 14px/18px. Hotel prices computed 700 18px/22px.

## Tabs

On the Kyoto page, Things to Do, Hotels, Restaurants, Cruises, and Forums are text links, 700 16px/20px `#002B11`, with no measured underline.

## Dialog

The hotel date dialog is `role="dialog"`, about 700 by 483, radius 12px, on a white parent. Title text is "Select dates". A selected day cell computed background `#EAEAEA`. The day button colour computed `#F7F7F7`. The dialog was closed with Escape. No date was chosen.

The cookie preference center opened from the footer. Allow All computed black fill, white text, radius 24px. It was not pressed.

## Menu

At 390px the header Menu button opened a white drawer, 326px wide, listing Write a review, Post photos, Add a place, Travelers' Choice, Travel Stories, Hotels, Things to Do, Restaurants, Cruises, and Forums. It was closed without following a link.

## Link

Header pills are white, radius `1000px`, text `#002B11`. Forum topic titles computed `#006699`, 700 14.4px (`light.color.link.forum`).

## Badge

Best Seller text computed 700 12px/16px, colour `#FFFFFF`. The chip behind it was not separated from the photo.

## Gaps

- No hover, pressed, or focus-visible ring was forced. `--focus-ring` is `0 0 0 2px #00f, 0 0 0 4px #fff`.
- No checkbox, radio, switch, text area, or toast was on the pages read.
- Currency and region selects were not opened.
- Avatar boxes on the home traveler row were not measured.
- Icon glyphs are not in this package.
