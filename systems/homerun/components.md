# Homerun components

Public marketing components from www.homerun.co, measured signed out on 2026-11-21 in headless Chromium at 1440 x 900 (crops at 2x) and 390 x 844. The login wall at app.homerun.co/login was loaded and photographed. Nothing was typed into it.

Readings live in [raw/components-computed.json](raw/components-computed.json). Crops are in [components/crops/](components/crops).

## Discovery list

| Surface | URL | Screenshot |
|---|---|---|
| Home | https://www.homerun.co/ | [home-light-default](screenshots/home-light-default.png) |
| Resources menu | home, Resources dropdown | [home-light-resources-menu](screenshots/home-light-resources-menu.png) |
| Log in menu | home, Log in dropdown | [home-light-login-menu](screenshots/home-light-login-menu.png) |
| Feature disclosure | home | [home-light-feature-open](screenshots/home-light-feature-open.png) |
| ATS | /ats | [ats-light-default](screenshots/ats-light-default.png) |
| HR | /hr | [hr-light-default](screenshots/hr-light-default.png) |
| Pricing | /pricing | [pricing-light-default](screenshots/pricing-light-default.png) |
| Pricing FAQ | /pricing | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png) |
| Customers | /customers | [customers-light-default](screenshots/customers-light-default.png) |
| Blog | /blog | [blog-light-default](screenshots/blog-light-default.png) |
| Integrations | /integrations | [integrations-light-default](screenshots/integrations-light-default.png) |
| Contact | /contact | [contact-light-default](screenshots/contact-light-default.png) |
| Help | https://help.homerun.co/en/ | [help-light-default](screenshots/help-light-default.png) |
| Careers board | https://jobs.homerun.co/ | [careers-light-default](screenshots/careers-light-default.png) |
| Login wall | https://app.homerun.co/login | [login-light-wall](screenshots/login-light-wall.png) |
| Phone home | / at 390 | [mobile-home-light-default](screenshots/mobile-home-light-default.png) |
| Phone menu | / at 390 | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

## Button

Primary trial link. Fill `#4f75fe` (`light.accent.default`), text white, radius 12px, height 40px, padding 4px 16px, GT America 16/32. Hover fill `#264ddb` (`light.accent.hover`). Focus paints the browser ring `rgb(0, 95, 204) auto 1px`. Pressed was not captured: the control is a link.

Crops: [default](components/crops/button-primary-default.png), [hover](components/crops/button-primary-hover.png), [focus-visible](components/crops/button-primary-focus-visible.png).

The hero trial link is the same blue at 52px tall, 20/28, padding 12px 20px. [button-trial-default](components/crops/button-trial-default.png).

## Secondary button

Book a demo. Fill `#2d2323` (`light.button.secondary`), white text, radius 12px, height 40px. Hover fill `#4a3e3e`. [default](components/crops/button-secondary-default.png), [hover](components/crops/button-secondary-hover.png).

## Nav link

Organise your hiring. Transparent, text `#4a3e3e`, radius 10px, padding 12px, 16/22. Hover wash `rgba(245, 243, 239, 0.984)`. [nav-link-default](components/crops/nav-link-default.png), [nav-link-hover](components/crops/nav-link-hover.png).

## Login trigger

Outlined pill, 1px border, radius 12px, text `#4a3e3e`. Opens the login menu. It does not submit. [login-trigger-default](components/crops/login-trigger-default.png).

## Menu item

Resources menu row. Text `#4f75fe`, padding 8px, height 40px. [menu-item-default](components/crops/menu-item-default.png).

## Feature row and FAQ

In-page disclosure. Feature row is 14/20, padding 14px 24px. FAQ row on pricing is 25/37.5. Selected crops: [feature-row-selected](components/crops/feature-row-selected.png), [faq-row-selected](components/crops/faq-row-selected.png).

## Text field

Newsletter and contact email fields were measured empty. Height 50px, font 18px, fill `rgba(45, 35, 35, 0.1)`, radius `30px 0px 0px 30px` (the field shares a pill with its submit). Not filled, not submitted. [newsletter-field-default](components/crops/newsletter-field-default.png), [text-field-default](components/crops/text-field-default.png).

The login email field is a separate control on the wall: height 44px, radius 10px, fill `#f5f3ef`. Empty. [login-email-default](components/crops/login-email-default.png).

## Checkbox

Integrations category label, 18/20 weight 700. The native box was not isolated from the label. [checkbox-default](components/crops/checkbox-default.png).

## Card

Blog title link. Text `#131313`. The card art is a published illustration, not a measured surface token. [card-default](components/crops/card-default.png).

## Login wall controls

Google and Microsoft buttons were not clicked. The Google button is 382 x 44, radius 10px, 1px border, shadow `rgb(227, 225, 221) 0px 2px 0px 0px`, hover fill `#f5f3ef`. [sso-button-default](components/crops/sso-button-default.png).

The Log in submit is the same blue `#4f75fe`, 382 x 44, radius 10px. Not clicked. Hover fill `#274edc`. [login-submit-default](components/crops/login-submit-default.png).

## Gaps

| Component | Status |
|---|---|
| Button pressed | Not captured. Public CTAs are links. |
| Text area | Not present on the public pages measured. |
| Select | Not present. |
| Radio | Present as blog category filters. Not isolated as a crop. |
| Switch | Not present. |
| Tabs | Login wall shows ATS and HR tabs. Not clicked, so the HR tab state is Not captured. |
| Tooltip | Not present. |
| Dialog | Not present on marketing. Login is a page, not a dialog. |
| Toast | Newsletter success and error nodes exist in the DOM at zero size. Not triggered. |
| Table | Not present. |
| Avatar | Not present as a product control. Demo art in the hero is illustration. |
| Badge | ATS and HR pills in the nav are links, measured as nav links. |
| Dark theme | Not present. |
| Signed-in app | Not captured. Login wall only. |
