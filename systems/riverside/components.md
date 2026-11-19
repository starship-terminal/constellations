# Components

Measured on the public marketing site and the signed-out studio login on 19 November 2026. Values are computed styles. There are no crops: the preview browser returned no screenshot frames.

## Button

Marketing primary (`a.main-button`, `a.rs-button`): background `#9671ff`, text `#ffffff`, radius 100px (rs-button 300px), padding 20px 40px (rs-button 17px 46px), weight 500 or 600. Visible hero instance was 58px tall.

Nav action (`a.c-updated-nav-button`): background `#1d1d1d`, text `#ffffff`, 1px solid `#1d1d1d`, radius 300px, padding 11px, height 40px, 14px Instrument Sans weight 500. Transition 275ms ease.

Pricing action (`.ra-pricing-button`): transparent fill, 1px solid `#1b2127`, text `#1b2127`, radius 999px, padding 16px 5px, height 50px, 16px weight 500.

Studio submit (`button.button--primary-40`): background `#7848ff`, text `#fafafa`, radius 8px, height 40px, padding 0 16px, weight 600. Focus-visible rule declares a 3px `#ffffff` ring.

Studio social (`button.button-CguhK3` on login, `.buttonHighlighted` on register): background `#222222`, text `#fafafa`, radius 8px on login and 10px on register, height 40px.

## Link

Nav link (`a.c-nav-link--login`): `#1d1d1d`, 14px Instrument Sans weight 500, padding 0 9px, no underline read.

Studio link (`a.link` Sign up): `#b196ff`, 12px Inter, line-height 20px.

## Text field

Studio email (`input.input-q6h84o`): background `#222222`, text `#fafafa`, 14px Inter, radius 8px, padding 8px 12px, height 40px, no border. Focus paints an inset 1px `#b196ff` shadow.

Password sits in a row of the same 40px height and 8px radius. Placeholder text was "Email" and "Password".

No marketing page that was opened painted a text field.

## Badge

`.pricing__plan-badge`: background `#9671ff`, text `#ffffff`, 12px weight 500, padding 4px 9px 8px, radius 0 0 8px 8px. Text read "Best Value".

## Billing pill

`.plan-test-navigator-round`: background `rgba(150, 113, 255, 0.3)`, radius 6px, 40 by 129px, sitting in a 274 by 52px white track with 10px radius (`.c-price-abtest-price-inner`).

## Plan card

`.pricing__plan`: white, radius 12px, padding 32px 20px. Featured `.is--pro_v2` adds a 4px solid `#9671ff` border and padding 28px 16px 24px.

## Gaps

Icon button, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table and avatar were not on the signed-out pages opened. The studio stylesheets declare rules for several of them under `.button`, `.tabs`, `.segmented-control` and menu surfaces. Those rules were not painted, so they are not tokens.

Hover, pressed, disabled, loading and error states were not forced. The focus state of the email field was read. A disabled button colour is declared as `--color-secondary-c300` under the light theme selector and was not on screen.
