# Components

Measured on raster.app, signed out, 2026-11-19, and checked again on 2026-11-21. Marketing values are from `html.dark`. Docs loads dark and can be switched to `html.light`.

## Button

Primary is Raster Red `#ff2f66`, white text, 14px / 500, height 37px, padding 7px 28px, radius 5.25px, border `oklab(white / 0.18)`, inset shadow `rgb(255, 83, 129) 0 0 10px -10px`. The nav copy is the same colour at 12.25px, height 27px, padding 3.5px 10.5px.

Secondary (Book demo, Onboard your agent) is `oklab(white / 0.08)` with a `oklab(white / 0.15)` border and no shadow.

Disabled on `/design` keeps the same fill at opacity 0.5. Hover did not change the computed background. Focus on Get started was the browser outline `rgb(153, 200, 255) auto 1px`, offset 1px.

Crops: [button-primary-default](components/crops/button-primary-default.png), [button-primary-hover](components/crops/button-primary-hover.png), [button-primary-focus](components/crops/button-primary-focus.png), [button-primary-disabled](components/crops/button-primary-disabled.png), [button-secondary-default](components/crops/button-secondary-default.png).

## Link

Nav links are Raster Neue, 14px / 500, white, padding 3.5px 17.5px, no radius. Sign in is 12.25px. Docs "On this page" current links are Raster Red.

Crop: [link-nav-default](components/crops/link-nav-default.png).

## Text field

`.input` on `/design` is height 37px, radius 5.25px, padding 7px 10.5px, background `rgb(39, 39, 42)`, border `oklab(white / 0.1)`, text white, weight 300. A disabled field uses the same chrome. On 2026-11-21 the sign-in email field was in the DOM, empty, and hidden until Email link to sign in. That button was not clicked. No email was typed.

Crop: [field-default](components/crops/field-default.png).

## Tabs

`.tabs` on `/design` is a 216 x 35 track, background `rgb(24, 24, 27)`, border `rgba(255, 255, 255, 0.08)`, radius 7px, padding 3.5px. The indicator is `rgb(63, 63, 70)`, radius 5.25px, shadow `rgba(0, 0, 0, 0.3) 0 1px 2px`. `.tabs.tabs-minimal` is an underline: the indicator is 2px Raster Red.

Crop: [tabs-default](components/crops/tabs-default.png).

## Tag

`.tag` is a pill (computed radius about 1.68e7 px), 10.5px / 300, padding 3.5px 10.5px, height 23px. Outline is gray-400 text on a `oklab(0.71 / 0.2)` border. Solid is `#d4d4d8` on `#3f3f46`.

Crops: [tag-outline-default](components/crops/tag-outline-default.png), [tag-solid-default](components/crops/tag-solid-default.png).

## Navbar

Fixed, 53px, background `rgba(0, 0, 0, 0.5)`. Wordmark is a 24px four-tile SVG plus "Raster" in Raster Neue 14px / 500. On the phone, Sign in and Book demo hide and a hamburger shows.

Crop: [navbar-default](components/crops/navbar-default.png).

## Hero heading

36px / 500 at 1440, line-height 39.6px, letter-spacing -0.9px. The first line clips `--raster-gradient-stops` (red, orange, yellow, pink, violet, rose) with `background-clip: text`. The next lines are `lab(98.26 0 0)`. The h1 itself computes to gray-500 because the clipped line's fill is transparent.

Crop: [hero-heading-default](components/crops/hero-heading-default.png).

## Pricing

Three columns: Personal ("Free, forever", a gray Get started), Team ("$20 per user", a red Get Started), Enterprise ("Custom pricing", a red Contact Sales). Plan titles are Raster Neue 26.25px / 600. Contact Sales was not followed.

## Docs card

On `/docs`, a guide card is 412 x 98, background `rgb(241, 241, 241)`, radius 12px, padding 16px, border `rgba(204, 204, 204, 0.5)`. The current sidebar row is Raster Red text on `oklab(0.654 / 0.1)`, radius 8px.

## Gaps

- Checkbox, radio, switch, textarea, toast: not on the signed-out pages.
- Tooltip and dialog: specimens exist on `/design` and were not cropped.
- Avatar: labelled 24, 48, 96, 144, 192 px on `/design`. The fill is generated per initial and was not sampled as a token.
- Reduced motion: custom properties were read. `prefers-reduced-motion` was not emulated.
- Pressed: the design page describes a fill that rises while pressed. A pressed computed style was not captured.
- Signed-in library, Google continue, email-link submit, and checkout: not entered.
