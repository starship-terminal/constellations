# Components

Public signed-out Slab, measured on 2026-11-19. Computed styles are from a 1169 by 731 CSS viewport. Crops are cut from the 1440 marketing screenshots.

## Button

Marketing buttons use Whitney, 6px radius, and 18px / 600 / 24px. The short size pads 16px 24px and computes to 56px tall.

| State | Where | Values |
|---|---|---|
| Primary, default | Home "Get Started" | background `#ff4143`, text `#ffffff`, radius 6px, padding 16px 24px, height 56px. [button-primary-default.png](components/crops/button-primary-default.png) |
| Primary, hover | Stylesheet `.Button-module--primary:hover` | background `#ff5052`. Not shown |
| Primary, active | Stylesheet `:active` | background `#ff4143`. Not shown |
| Gray | Pricing Free "Get Started" | background `#2f4050`, text `#ffffff`, height 56px. [button-gray-default.png](components/crops/button-gray-default.png) |
| Yellow | Pricing Startup | background `#fcb415`. [button-yellow-default.png](components/crops/button-yellow-default.png) |
| Cyan | Pricing Business | background `#50c5dc`. [button-cyan-default.png](components/crops/button-cyan-default.png) |
| Maroon | Pricing "Contact Sales" | background `#741448`, text `#ffffff`. [button-maroon-default.png](components/crops/button-maroon-default.png) |
| Google, marketing | Home "Sign up with Google" | background `#4285f4`, radius 2px, height 40px, width 460px at 1169. Not clicked. [button-google-default.png](components/crops/button-google-default.png) |
| Account primary | Login "Continue" and register "Create my account" | background `#7e0048`, text `#ffffff`, radius 2px, height 35px, padding 8px 12px, Untitled Sans 14px / 500 |
| Account primary, hover | Stylesheet | background `#6b003d`. Not shown |
| Account primary, active | Stylesheet | background `#560031`. Not shown |
| Account secondary | Register "Sign up with Google" | background `#ffffff`, border `1px solid #e3e3e3`, text `#333333`, height 35px. Not clicked |
| Disabled | Stylesheet `.Button-module--disabled` | opacity 0.4. Not shown |
| Unstyled | Footer "Contact Support" | transparent, inherited colour, padding 0 |

## Link

Home "Log In" is Whitney 20px / 600, white, on the plum nav. Pricing "Log In" is the body colour `#455360`. The login "Sign up for Slab" link is `#a21a68` at 14px. Footer Terms and Privacy are `#939598` at 16px / 500. Focused links draw `outline: rgb(229, 151, 0) auto 1px` with offset 1px.

## Text field

Home "Work Email" is a text input: background `#ffffff`, height 56px, radius 6px, padding 0 12px, Whitney 18px, placeholder "Work Email". It was not filled and the form was not submitted. [field-email-default.png](components/crops/field-email-default.png).

Login subdomain input: background `#ffffff`, height 33px, radius 2px, padding 8px 12px, Untitled Sans 14px, shadow `rgb(144, 144, 144) 0px 0px 0px 1px`, placeholder "subdomain". Not submitted.

Register shows email, full name and password fields at the same 33px account size. The password field means this is not an email-only form. Nothing was typed.

The stylesheet gives `.form-field` inputs a focus ring `rgb(80, 197, 220) 0px 0px 0px 2px`. A programmatic focus on the home field did not paint that ring, so it stays a rule.

## Text area, select, checkbox, radio, switch

Form stylesheets declare them: select height 56px, radius 6px, checkbox fake control radius 6px, radio circle `border-radius: 50%`, toggle knob transition 0.15s. None of these controls were on the pages opened.

## Tabs

Pricing Annually / Monthly is a 36px pill. Track `#ebecec`, radius 18px. Selected "Annually" sits on `#7e0048` with white text. Idle "Monthly" is `#2f4050`. [tabs-billing-default.png](components/crops/tabs-billing-default.png).

## Menu, tooltip, dialog, toast

Nav menus exist in the DOM and were not opened. Toastify rules are in the home stylesheet, including a Slab override for success (`#ffffff` face, 2px `#50c5dc` border, text `#455360`). No toast was shown. No dialog was shown.

## Card

Login card: background `#ffffff`, border `1px solid rgba(125, 106, 104, 0.2)`, radius 4px, shadow `rgba(106, 52, 33, 0.06) 0px 0px 23px`, padding 48px, width 430px. No screenshot of this card: the login page was not opened in the headless browser.

Pricing columns are in [pricing-light-default.png](screenshots/pricing-light-default.png).

## Table

The pricing comparison is a table. Plan names are Whitney 16px / 500. Rows cover usage, essentials, advanced, AI, security, integrations and support. No cell border colour was measured as a separate token. The Enterprise column uses the plum fill.

## Avatar, badge

Not present as components on the public pages. The home hero shows a product demo with names inside an illustration. That illustration is not the app.

## Gaps

- Register asks for email, full name and password. It was not filled or submitted.
- Google signup was not clicked. Company SSO, Okta and SAML were not opened.
- No card, phone, government ID or KYC step was entered.
- Hover, pressed, disabled, error and loading were not shown.
- Checkbox, radio, switch, select, text area, menu, tooltip, dialog and toast were not shown.
- Login and register have computed styles and no screenshots.
- Signed-in wiki was not opened.
