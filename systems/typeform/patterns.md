# Typeform patterns

How the public site combines the controls. Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Marketing shell

The homepage opens with a purple announcement strip, then a dark inverted header: logo, Platform, Solutions, Resources, Pricing, Log in, Contact sales, Sign up. The hero is a large Tobias line on a dark band, then a light page.

[home-light-default.png](screenshots/home-light-default.png) shows the shell after the announcement close. [home-light-banner.png](screenshots/home-light-banner.png) shows the strip still up.

Platform, Solutions, and Resources open on hover as full-width dark menus.

| Menu | Screenshot |
|---|---|
| Platform | [home-light-platform-menu.png](screenshots/home-light-platform-menu.png) |
| Solutions | [home-light-solutions-menu.png](screenshots/home-light-solutions-menu.png) |
| Resources | [home-light-resources-menu.png](screenshots/home-light-resources-menu.png) |

On a phone the same links sit behind a menu button: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Pricing

[pricing-light-default.png](screenshots/pricing-light-default.png) is the plan page. Monthly and Yearly are a local toggle: [pricing-light-yearly.png](screenshots/pricing-light-yearly.png) and [pricing-light-monthly.png](screenshots/pricing-light-monthly.png). The Growth Flow card keeps a struck-through trial price over the current figure for a moment after the toggle, so those two frames show overlapping digits. Plan CTAs go to signup and were not followed.

## Template preview

A template page opens a preview dialog without an account: [template-light-preview.png](screenshots/template-light-preview.png). "Start with this template" goes to signup and was not clicked.

## Login wall

[login-light-default.png](screenshots/login-light-default.png) is the signed-out wall at [https://admin.typeform.com/login](https://admin.typeform.com/login). Continue with Google, Continue with Microsoft, Continue with email, and Log in with SSO are on the page. None was clicked. The email field was not submitted. [signup-light-default.png](screenshots/signup-light-default.png) is the signup wall, also not filled.

## What this package does not show

The form builder, results, automations, and account settings sit behind that wall. Empty, loading, error, and destructive confirmation inside the product were not captured. Public FAQ accordions and the billing toggle are the only local state changes that were exercised beyond menus and the preview dialog.
