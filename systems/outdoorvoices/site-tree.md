# Outdoor Voices public site tree

Mapped signed out on 2026-11-22 from [https://www.outdoorvoices.com/](https://www.outdoorvoices.com/) in an incognito preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. Title: Outdoor Voices | Activewear & Athletic Apparel for Recreation. The page is a live Shopify store, not a parked domain and not a captcha wall.

A gender popup ("First, who are we shopping for?") covered the first paint. Its close control was used so the public page could be photographed. Women, Men, and Both on that popup were not clicked. A later "Get 30% Off" chip was hidden in the preview the same way. Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. Nothing was added to bag. Checkout was not opened. `login-extracted` stays `not-started`.

`catalog.json` and `webapps-manifest.json` were left alone. origin/main had no `systems/outdoorvoices/` and no `systems/outdoor-voices/`.

Tracking query strings are not recorded. The account redirect drops the OAuth query. Menus were read from the homepage DOM. Each submenu was not hovered open.

## Promo bar

Photographed: [home-light-1440.png](screenshots/home-light-1440.png). Height 42px. Background `#2b54ab`. Two slides.

| Control | Opens | This pass |
|---|---|---|
| Enjoy 30% off sitewide. | `/collections/shop-women` | not opened |
| Free Shipping on orders $100+ | no link of its own | read on the homepage |
| Previous slide / Next slide | the other slide | listed |

## Header

White bar, 75px, under the promo. Women and Men are menu summaries. OV Extra Sale and Gift Guide are links. Search, Account, and Cart sit at the right. The wordmark is 200 by 23, ink `#202020`.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Women | summary | women's mega menu | read from the DOM, not hovered open |
| Men | summary | men's mega menu | read from the DOM, not hovered open |
| OV Extra Sale | link | `/collections/ov-extra` | not opened |
| Gift Guide | link | `/pages/gift-guide-2026` | not opened |
| Outdoor Voices | link | `/` | home |
| Search | button | search overlay | not opened, not submitted |
| Account | link | `/account` | empty wall photographed, then stopped |
| Cart | button | cart drawer | not opened. Checkout was not started |

The mobile menu is in the DOM at this width and is not the photographed chrome. It also lists Log In at `/customer_authentication/redirect`. That is the same wall. It was not opened from the mobile menu.

## Women's menu

| Column | Control | Opens |
|---|---|---|
| Featured | New Arrivals | `/collections/w-new-arrivals` |
| Featured | All Women's | `/collections/shop-women` |
| Featured | OV Outdoors | `/collections/ov-hike` |
| Featured | Best Sellers | `/collections/w-bestsellers` |
| Featured | CloudKnit | `/collections/w-cloudknit` |
| Featured | OV Extra Sale | `/collections/ov-extra?filter.p.m.filter.gender=Women&filter.p.m.filter.gender=Unisex&sort_by=manual` |
| Apparel + More | Dresses | `/collections/dresses` |
| Apparel + More | Tops & Tanks | `/collections/womens-tops` |
| Apparel + More | Pants | `/collections/w-pants` |
| Apparel + More | Sweatshirts & Jackets | `/collections/w-jackets` |
| Apparel + More | Shorts & Skorts | `/collections/w-shorts-skorts` |
| Apparel + More | Bras | `/collections/sports-bras` |
| Apparel + More | Leggings | `/collections/leggings` |
| Apparel + More | Accessories | `/collections/shoes?genderFilter=woman` |
| Activity | Studio | `/collections/studio` |
| Activity | Sweat | `/collections/sweat` |
| Activity | Rest Day | `/collections/rest-day` |
| Activity | Hike | `/collections/ov-hike` |
| Activity | Court Sports | `/collections/court-sports` |
| Activity | Everyday | `/collections/everyday` |
| Card | Shop Sale | `/collections/shop-women` |

## Men's menu

| Column | Control | Opens |
|---|---|---|
| Featured | New Arrivals | `/collections/m-new-arrivals` |
| Featured | All Men's | `/collections/shop-men` |
| Featured | Best Sellers | `/collections/m-bestsellers` |
| Featured | OV Extra Sale | `/collections/ov-extra?filter.p.m.filter.gender=Men&filter.p.m.filter.gender=Unisex&sort_by=manual` |
| Apparel + More | Shorts | `/collections/m-shorts` |
| Apparel + More | Tops | `/collections/mens-tops` |
| Apparel + More | Pants | `/collections/m-pants` |
| Apparel + More | Sweatshirts & Jackets | `/collections/m-jackets` |
| Apparel + More | Accessories | `/collections/shoes?filter.p.m.filter.gender=Unisex&sort_by=manual` |
| Shop by | OV Hike | `/collections/ov-hike?filter.p.m.filter.gender=Men&sort_by=manual` |
| Shop by | CloudKnit | `/collections/cloudknit?filter.p.m.filter.gender=Men&filter.p.m.filter.gender=Unisex&sort_by=manual` |
| Shop by | Fleeces | `/collections/find-your-fleece?filter.p.m.filter.gender=Men&sort_by=manual` |
| Shop by | The Cozy Shop | `/collections/the-cozy-shop-2026?filter.p.m.filter.gender=Men&filter.p.m.filter.gender=Unisex&sort_by=manual` |
| Card | Shop Sale | `/collections/shop-men` |

## Homepage tiles

One product tile was opened.

| Control | Opens | This pass |
|---|---|---|
| Shop — Women | `/collections/shop-women` | not opened |
| Shop — Men | `/collections/shop-men` | not opened |
| Doing Things Bra | `/products/w-doing-things-bra-darkbay-polka-dot` | photographed |
| TechSweat Core 7/8 Legging | `/products/w-techsweat-core-7-8-legging-darkbay-polka-dot` | not opened |
| The Exercise Dress | `/products/w-the-exercise-dress-navy` | not opened |

## Footer

Join the Team is the subscribe wall. The email field was empty. Sign Up Now was not clicked. Preference radios (Women, Men, Both) were not selected.

| Control | Opens | Stop? |
|---|---|---|
| My Account | `/account` | same empty login wall |
| Returns | `/pages/help-center-returns-exchanges` | not opened |
| Help Center | `/pages/help-center` | not opened |
| About Us | `/pages/about-us` | not opened |
| Accessibility | `/pages/accessibility` | not opened |
| Accessibility Widget | `/#open-accessibility-widget` | not opened |
| California Residents | `/pages/prop-65` | not opened |
| Privacy | `/pages/privacy-policy` | not opened |
| Your Privacy Choices | `/pages/your-privacy-choices` | not opened |
| Terms | `/pages/terms-of-use` | not opened |
| Instagram | `https://www.instagram.com/outdoorvoices/` | not opened |
| Facebook | `https://www.facebook.com/OutdoorVoices/` | not opened |
| TYB | `https://app.tyb.xyz/brand/outdoorvoices` | not opened |
| TikTok | `https://www.tiktok.com/@outdoorvoices` | not opened |
| Email / Sign Up Now | newsletter form | subscribe wall, not submitted |

The copyright line reads ©2026 Outdoor Voices.

## Where this pass stopped

Login, signup, checkout, and subscribe. Account and My Account land on one empty email wall at `shopify.com`. Continue with Shop was visible and was not clicked. The cart button was not opened. The footer email was left empty. Add to Bag on the product page was not clicked.
