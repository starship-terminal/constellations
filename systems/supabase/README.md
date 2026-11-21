# Supabase

Public marketing site, captured again on 2026-11-21, signed out. This refreshes the existing `systems/supabase` package. The earlier signed-in dashboard shots stay in the package history. This pass did not enter the dashboard.

`https://supabase.com/` returned 200. Product, Developers, and Solutions open menus. Pricing, docs, product pages, the blog, customers, company, security, and status are public. Sign in and Start your project stop at empty walls. Nothing was typed. GitHub, ChatGPT, and SSO were not clicked. `login-extracted` stays not-started. `catalog.json` was not edited.

| File | Contents |
|---|---|
| [README.md](README.md) | This note |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [tokens.json](tokens.json) | Measured public tokens, light and dark |
| [DESIGN.md](DESIGN.md) | Hand-written one-theme export. Not regenerated, so the catalog stays as it was. |
| [screenshots/](screenshots/) | Public pages from this pass, plus the earlier dashboard set |
| [raw/public-2026-11-21.json](raw/public-2026-11-21.json) | Readings for this pass |

## What was captured

Headless Chromium, Playwright, signed out, 2026-11-21.

Desktop shots request 1440×900 at 1x. Phone shots request 390×844 at 2x. Sidecars record `innerWidth` 1440 and 390. The homepage viewport file is cropped to 1440×430 so a marketing demo of sample emails is not in the committed image. The tall homepage stitch was discarded for the same reason.

| Shot | What it shows |
|---|---|
| [screenshots/home-dark-default.png](screenshots/home-dark-default.png) | Homepage hero, dark |
| [screenshots/home-dark-menu-product.png](screenshots/home-dark-menu-product.png) | Product menu |
| [screenshots/home-dark-menu-developers.png](screenshots/home-dark-menu-developers.png) | Developers menu |
| [screenshots/home-dark-menu-solutions.png](screenshots/home-dark-menu-solutions.png) | Solutions menu |
| [screenshots/home-dark-theme-menu.png](screenshots/home-dark-theme-menu.png) | System, Dark, Light |
| [screenshots/home-dark-theme-light.png](screenshots/home-dark-theme-light.png) | Same page in Light |
| [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png) | Pricing cards |
| [screenshots/docs-dark-default.png](screenshots/docs-dark-default.png) | Docs landing |
| [screenshots/docs-dark-search.png](screenshots/docs-dark-search.png) | Docs search, empty |
| [screenshots/login-dark-default.png](screenshots/login-dark-default.png) | Empty sign-in wall |
| [screenshots/signup-dark-default.png](screenshots/signup-dark-default.png) | Empty sign-up wall |
| [screenshots/mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png) | Homepage at 390 |
| [screenshots/mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png) | Phone menu |
| [screenshots/mobile-pricing-dark-default.png](screenshots/mobile-pricing-dark-default.png) | Pricing at 390 |
| [screenshots/mobile-login-dark-default.png](screenshots/mobile-login-dark-default.png) | Empty sign-in wall at 390 |
| [screenshots/mobile-signup-dark-default.png](screenshots/mobile-signup-dark-default.png) | Empty sign-up wall at 390 |

Also shot, dark, desktop: database, auth product page, features, blog, customers, company, security, enterprise, brand, changelog, support, contact sales, status.

## Where this stopped

The sign-in wall is Welcome back. The sign-up wall is Get started. Email and password were empty. The password dots are the placeholder. Continue with GitHub, Continue with ChatGPT, and Continue with SSO were not clicked. Sign in and Sign up were not clicked. The dashboard was not opened.

## How the values were read

Computed styles on `supabase.com`, then converted to sRGB in the page. Dark page `#131413`, dark text `#edefee`, dark CTA fill `#006338`, dark accent type `#4acd8b`. Light page `#fdfdfd`, light text `#030303`, light accent `#0e7e4e`. Hero is Manrope 46px, weight 500. Body is Inter 16/24. Header CTA is 26px tall, 8px radius. Pricing CTA is 42px tall. Declared weights include a 450 "normal".

## What to distrust

The earlier dashboard tokens and crops in this package are from 2026-10-31. This pass did not remeasure them. The homepage hero crop is not a full 900px viewport. Quantised screenshots are for layout. Read colours from [tokens.json](tokens.json).

## Coverage

| Item | Status |
|---|---|
| Colour roles, dark | Captured on the public homepage. [tokens.json](tokens.json) |
| Colour roles, light | Captured. [screenshots/home-dark-theme-light.png](screenshots/home-dark-theme-light.png) |
| Type | Captured. Hero 46/46 Manrope, nav 14, header button 12 |
| Spacing | Header CTA padding 4px 10px. No full spacing scale was declared on the measured controls. |
| Radii | Captured. 8px header, about 10px on pricing and auth buttons |
| Button | Captured. Header CTA and pricing Get Started |
| Link | Captured. Nav Pricing |
| Menu | Captured. Product, Developers, Solutions, phone sheet, theme menu |
| Dialog | Captured. Docs search |
| Text field | Seen empty on the auth wall and the sales contact page. Not filled. |
| App shell of the signed-in product | Not captured in this pass. Login wall. Earlier dashboard shots remain from 2026-10-31. |
| Destructive confirmation, toast, onboarding | Not captured. Behind the login wall. |

## Do and don't

- Do put the action in a green pill. Start your project is `#006338` in dark and `#0e7e4e` in light. [screenshots/home-dark-default.png](screenshots/home-dark-default.png)
- Do open product, developer, and solution links from a menu that stays on the page. [screenshots/home-dark-menu-product.png](screenshots/home-dark-menu-product.png)
- Do set the accent line of the hero in the brand green and the first line in the text colour. [screenshots/home-dark-default.png](screenshots/home-dark-default.png)
- Don't treat the public site as the dashboard. Sign in stops at an empty wall. [screenshots/login-dark-default.png](screenshots/login-dark-default.png)
