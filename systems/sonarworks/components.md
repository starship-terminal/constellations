# Components

Measured on the live Sonarworks pages on 19 November 2026. The preview browser returned "The browser is not producing screenshot frames", so this inventory has no crops. Each value is a computed style, or a stylesheet rule marked as declared when the state was not on screen.

## Button

Learn More, Buy now, Get Free Trial and the social continue buttons.

| State | Where | Values |
|---|---|---|
| Dark pill | Buy now on /black-friday | background `#000000`, text `#ffffff`, radius `9999px`, padding `12px 20px`, height 48px, Inter 16/24 weight 400 |
| Light pill | Learn More on a dark photo | background `#ffffff`, text `#000000`, radius `9999px`, padding `12px 16px`, height 48px |
| Outlined pill | Continue with Google on /account/login | background `#ffffff`, text `#000000`, border `1px solid #000000`, radius `9999px`, padding `12px 24px`, height 50px |
| Trial | 7-day Free Trial class `.bg-highlight-blue` | background `#68befd`, text `#000000`, radius `9999px`, padding `4px 16px` |
| Disabled | Log in and Sign up submits before the form is valid | background `#d8d9da`, text `#636669`, border `1px solid #d8d9da`, radius `9999px`, padding `12px 20px`, height 50px, cursor default |
| Hover | not measured | Links underline on hover (`a:hover { text-decoration-line: underline }`). A filled pill's hover fill was not read, because hover cannot be forced without a pointer screenshot. |
| Focus | email field focused | outline `none 0px`. No focus ring colour was painted. |
| Pressed | not captured | |
| Loading | `.animate-spin` is declared at 1s linear. No spinner was on screen. | |

## Link

Top-bar links are Inter 16/24, `#96999c`, padding `8px 16px`, no underline at rest. Footer primary links are `#ffffff`. Legal links on signup are 11/16, `#000000`. Forgot your password is 11px and underlined.

## Text field

Email on /account/login: width 318px, height 48px, padding 12px, border `1px solid #000000`, radius 0, background `#ffffff`, text `#000000`, placeholder "Email address". Password at rest: border `1px solid #dfe0e1`. Focus keeps the black border and sets outline to 0. Error border `#fc5b41` is declared on `.field.has-errors .control input` and was not shown.

The newsletter field on /soundid-reference is a pill: height 64px, padding 20px, radius `9999px`, border 0 at this width, placeholder colour class `text-base-60`.

## Text area

Not present on the pages visited.

## Select

Not present.

## Checkbox

Not present. Signup has no checkbox. The legal line is 11px `#636669`: "By continuing you agree to SoundID Privacy Policy and Terms of Service."

## Radio

Not present.

## Switch

Not present.

## Tabs

Not present. Product navigation is a list of links.

## Menu

The company disclosure uses a 16px chevron, stroke `#96999c`. The mobile menu (`#mobile-navigation`) was off screen at 1169px. Its open transition is 0.3s ease. Not opened.

## Tooltip

Not present.

## Dialog

CookieScript banner was on the home page before it was dismissed: white bar, text `#2d2d2d`, Open Sans 14/21, "Got it" pill radius 999px, border `1px solid #2d2d2d`, padding `12px 16px`. That banner is a third-party widget, not the product type system.

## Toast

`.alert[data-type=success]` is `#6fe362` and `.alert[data-type=danger]` is `#fc5b41`. Neither was on screen.

## Card

Home product tiles are 389 by 365px photo grids. Type sits in a 16px pad over the image. No card radius, no shadow. Pricing cells on /black-friday have a 1px `#dfe0e1` border and padding `16px 16px 32px`.

## List row

FAQ `details` on /soundid-reference: summary 24/32, weight 400, padding `16px 16px 48px`, bottom border `1px solid #d8d9da`. Closed when measured.

## Table

System-requirements rows sit inside those details. Not expanded.

## Avatar

The account icon is a 16px stroke glyph, `#96999c`. No user avatar was shown.

## Badge

"You save €29.00" on /black-friday: background `#ffe701`, text `#000000`, 16/24. The struck price is `#636669`.

## Gaps

- No component crops. The preview browser did not produce screenshot frames.
- Hover, pressed, loading, error, success, open menu, open FAQ and the phone width were not captured.
- Checkbox, radio, switch, select, text area, tabs and tooltip were not on these pages.
