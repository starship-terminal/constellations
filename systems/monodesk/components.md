# Components

Measured on www.monodesk.com and app.monodesk.com, signed out, 2026-11-19. Crops are at 2x from a 1440 CSS viewport.

## Button

Primary pill, marketing. Fill #d1ff6e, text #026232, radius 100px, height 40px, Geist 14px / 500.

![default](components/crops/cta-primary-default.png)

Hover inverts to fill #026232 and text #d1ff6e.

![hover](components/crops/cta-primary-hover.png)

Pricing "Get started" is the same pair at 13px / 500, padding 9px 18px. Hover matches the primary inversion.

![plan](components/crops/plan-cta-default.png)

Hero "Log in" is a ghost pill, background rgba(255, 255, 255, 0.15), white text, radius 100px, padding 8px 16px.

Login submit is #161616 fill, white text, radius 12px, height 40px. Google is white, 1px #e2e2e2 border, radius 7px, height 44px. Hover on Google goes to #f6f6f6. Login hover did not change the computed fill.

![google](components/crops/button-google-default.png)

![login](components/crops/button-login-default.png)

## Link

Header links are 14px / 500, rgba(255, 255, 255, 0.85), white on hover, color transition 0.2s ease.

Create account and Forgot password? are #1c64f5. Create account is 14px / 600. Forgot password is 12px / 500.

## Text field

Login email and password: background #f8f8f8, 1px #ebebeb border, radius 9px, height 44px, 16px Geist, padding 1px 12px (password adds 44px right for the visibility icon). Focus did not change the computed border color in this pass. The browser outline on the input went to a 2px transparent solid.

![field](components/crops/field-email-default.png)

## Search

Help centre search: white, radius 100px, height 54px, padding 15px 24px, shadow `0px 2px 10px rgba(0, 0, 0, 0.12)`. Focus adds a highlighter ring (`rgba(209, 255, 110, 0.996) 0px 0px` in the computed shadow string).

![search](components/crops/search-default.png)

## Card

Help category card: white, radius 16px, about 303×183 at 1440. Hover did not change the computed background.

![help card](components/crops/help-card-default.png)

Login card: white, radius 16px, padding 32px, width 450px, shadow `0px 8px 24px rgba(0, 0, 0, 0.15)`.

![login card](components/crops/login-card.png)

## Badge

MOST POPULAR: #026232 fill, white text, 10px / 500, padding 4px 10px, radius 100px.

ALWAYS FREE: rgba(2, 98, 50, 0.08) fill, #026232 text, same size and radius.

![badge](components/crops/badge-popular.png)

## Navigation

Header bar sits on the blue grid. Sampled bar fill from the 1440 screenshot is about rgb(30, 84, 192), darker than the page #1c64f5. The CSS custom property for that bar was not isolated (the header element itself was transparent). Treat the darker blue as observed in the screenshot, not as a named token.

![header](components/crops/site-header-bar.png)

## Heading

Home h1 at 1440: Geist 72px / 400, white, line-height about 1.05.

Pricing h1: about 40px / 600, white.

Login heading: Geist 22px / 500, #161616, line-height 30px, letter-spacing -0.015px.

## Gaps

Checkbox, radio, switch, select, textarea, tabs, toast, table, avatar, menu, tooltip, and dialog were not present as interactive controls on the captured signed-out pages. The home page has a video dialog and the phone width has an email sheet. Neither was submitted. The video dialog was not opened. FAQ rows on the home page open in place. Their button computed style did not change. The answer text is in the page, not a separate component crop with its own tokens.
