# Components

Measured on the public marketing site and the signed-out login. Crops are 2x from the 1440 captures.

## Button

Primary on a light header is a 12px radius fill of `#2A222B` with `#FAF9FB` type, 40px tall in the nav (`padding: 12px 20px`) and 48px on plan cards (`padding: 8px 24px`). On the dark hero the same control flips: Sign up is `#FAF9FB` with `#2A222B` type, and Contact sales is a 1px `#FAF9FB` outline on the hero fill.

[components/crops/button-primary.png](components/crops/button-primary.png)
[components/crops/button-secondary.png](components/crops/button-secondary.png)
[components/crops/button-hero.png](components/crops/button-hero.png)
[components/crops/button-plan.png](components/crops/button-plan.png)

Hover, pressed, disabled and loading were not forced. The computed transition is background-colour 200ms ease and radius 300ms ease-out. Declared hover fill is `#564B58` (`--tokens--button--primary-bg-hover`).

Focus on the home Sign up link, after `element.focus()`, is `rgb(229, 151, 0)` outline, 1px, offset 1px.

## Link

Log in is a text button, Twklausanne 500 at computed weight 400, 16px, no fill, no radius. Colour follows the header: `#FAF9FB` on the hero, `#2A222B` on pricing.

[components/crops/link-login.png](components/crops/link-login.png)

## Card

Hero cards are 439 by 199, radius 12px, padding 24px, fill `#2A222B`, with an inset shadow `rgb(37, 28, 39) 10px 10px 20px -9px`. Plan cards are white, 324px wide, 1px border `#E5E1E5`, radius 12px, padding `48px 24px 24px`.

[components/crops/card-hero.png](components/crops/card-hero.png)
[components/crops/card-plan.png](components/crops/card-plan.png)

## Billing switch

Yearly is selected by default. The selected pill is `#E5E1E5` with `#2A222B` type, 14px, padding `5px 12px`, radius 12px, 31px tall. Monthly is transparent with `#655D67` type. The switch track itself was not a separate measured box.

## Text field

Login email wrap, focused: 400 by 44, radius 12px, fill `#FAFAFA`, border `1px solid #3C323E`, outline `2px solid #3C323E`, padding `0 2px 0 12px`. The input itself has no border. Signup email and password fields use the same 44px, 12px radius. The password field was empty. Neither form was submitted.

## Badge

NEW on the hero cards is a pill (`border-radius: 16000px`) with a purple glow `rgb(182, 109, 213) 0 0 15px`. The crop of the card shows it. A separate badge crop was not cut.

## Logo

Header mark is 43 by 24 inside a 152 by 24 link. [components/crops/logo.png](components/crops/logo.png) and [icons/mark.svg](icons/mark.svg).

## Gaps

Text area, select, checkbox, radio, switch (other than the billing pills), tabs, menu (the dropdown list stayed `display: none`), tooltip (the 32px button was on the pricing table, the panel was not opened), dialog, toast, list row, table, avatar, icon button as its own measured control. The phone menu button is in the 390 screenshot and was not opened.
