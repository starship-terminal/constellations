# Mural patterns

Public marketing pages and the signed-out login. Light only. Captured 2026-11-19 at 1440 CSS px and at a 390 CSS px phone width (the phone PNGs are 780 x 1688, device pixel ratio 2).

## Marketing home

[home-light-default.png](screenshots/home-light-default.png) is the top of https://www.mural.co/.

A white pill nav floats over a black hero. The pill is 1360 x 64, radius 16px, with the elevated shadow. Inside it: the wordmark, text links at 16px weight 300, a Login link, an outlined Book a demo, and a dark Sign up free. The phone nav is the wordmark plus a hamburger, in [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

The hero headline is STK Bureau 80px. The first lines are #8c8c8c and "Stand out." is white. The lede is ABC Social 18px white. Under that, a black email field with a grey border and a jade Get started control. A short legal line sits under the field. The rest of the hero is a product demo on a dotted canvas. That demo is a marketing illustration, not the signed-in app.

## Pricing

[pricing-light-default.png](screenshots/pricing-light-default.png) is https://www.mural.co/pricing.

The same pill nav. A small PRICING eyebrow, then an STK Bureau title at 64px. Four plan cards in a row: Free, Team+, Business, Enterprise. Each card content block is white, radius 20px, padding 32px 24px. Business carries a MOST POPULAR mark and a green price. A chat widget from the site sat over the right edge of this capture. It was not opened.

Phone: [mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png).

## Product, templates, enterprise, integrations

These are the same marketing shell with a different hero.

| Page | Desktop | Phone |
|---|---|---|
| Product | [product-light-default.png](screenshots/product-light-default.png) | [mobile-product-light-default.png](screenshots/mobile-product-light-default.png) |
| Templates | [templates-light-default.png](screenshots/templates-light-default.png) | [mobile-templates-light-default.png](screenshots/mobile-templates-light-default.png) |
| Enterprise | [enterprise-light-default.png](screenshots/enterprise-light-default.png) | [mobile-enterprise-light-default.png](screenshots/mobile-enterprise-light-default.png) |
| Integrations | [integrations-light-default.png](screenshots/integrations-light-default.png) | [mobile-integrations-light-default.png](screenshots/mobile-integrations-light-default.png) |

The public templates page is a catalog of published templates. Opening one inside the app needs an account, which was not created.

## Signed-out login and signup

[signin-light-default.png](screenshots/signin-light-default.png) is https://app.mural.co/signin. [signup-light-default.png](screenshots/signup-light-default.png) is https://app.mural.co/signup.

The page background is #f9fafa. A white header holds the wordmark and the other auth action. The form is a 416px column: a display heading, a Work email label, a 40px field, a legal line on signup, a red primary button, an Or divider, and a Google button. Login also has Remember me and a Terms of Service link. Neither form was submitted. No password field appeared, because the email was not sent.

Phone shots of both auth pages were saved. Their PNG height is the full page at 2x, not a 390 x 844 viewport crop, so the desktop shots are the ones to trust for the form.

## What these pages do not show

The signed-in mural, the canvas, comments, sharing, and workspace settings sit behind the login. The public site does not show a destructive confirm, an empty workspace, a loading state, or a validation error. Those are listed as gaps in [components.md](components.md).
