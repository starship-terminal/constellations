# Urban Outfitters measurements

Read from the live signed-out site on 2026-11-19 in the T3 preview browser. CSS viewport 1440 by 900, devicePixelRatio 2. The preview browser returned "The browser is not producing screenshot frames", so this file is the evidence. No screenshot was invented.

Nothing was added to bag, checked out, or typed into a phone, email, or card field.

## Pages

| Page | URL | What was read |
|---|---|---|
| Home | https://www.urbanoutfitters.com/ | Promo strip, utility bar, search, primary nav, editorial CTAs, product tray prices, `:root` custom properties |
| Product | https://www.urbanoutfitters.com/shop/bdg-kayla-low-rise-jean22?color=107 | Title, sale price, cart button, colour swatch, size chip, accordions, sign-in dialog opened and closed |
| Women's grid | https://www.urbanoutfitters.com/womens-clothing | Heading, filter control, product tile and promo price colour |

## Computed components

| Element | Colour | Background | Type | Box |
|---|---|---|---|---|
| Promo strip, first slide | white text | rgb(235, 64, 52) | Helvetica 12px / 0.2px, pad 10px 158px | 45px tall, full width |
| Later promo slides | white text | rgb(34, 34, 34) | same | 45px |
| Promo link | rgb(255, 255, 255), underline | transparent | 12px / 0.5px | |
| Utility links | rgb(34, 34, 34) | transparent | Helvetica 12px / 16.8px / 0.5px | Sign In 124 by 20 |
| Search input | rgb(34, 34, 34) | transparent | Helvetica 12px / 0.5px, pad 0 0 0 15px, radius 0 | 43px tall |
| Primary nav link | rgb(34, 34, 34) | transparent | Helvetica 12px / 0.5px, pad 10px 12px, radius 0 | 60px tall |
| Section heading | rgb(34, 34, 34) | transparent | Helvetica 16px / 22.4px / 0.5px | |
| Product tile title and price | rgb(34, 34, 34) | transparent | Helvetica 12px / 0.2px | tile link 248 by 398 on home |
| PDP title | rgb(34, 34, 34) | transparent | Helvetica 22px / 30.8px / 0.5px, weight 100 | |
| PDP sale price | rgb(216, 54, 4) | transparent | Helvetica 22px / 0.5px, weight 100 | |
| PDP original price | rgb(34, 34, 34), line-through | transparent | Helvetica 12px / 0.2px | |
| PDP promo line | rgb(58, 135, 0) | transparent | Helvetica 22px / 0.5px, weight 100 | |
| Cart button | rgb(255, 255, 255) | rgb(34, 34, 34) | Helvetica 16px / 22.4px / 0.5px, weight 700, pad 10px 20px, border 1px solid rgb(34, 34, 34), radius 0 | 520 by 45 |
| Size chip | rgb(112, 112, 112) | rgb(255, 255, 255) | Helvetica 12px / 0.5px, border 1px solid rgb(221, 221, 221), radius 0 | 38 by 38 |
| Colour swatch label | | | border 1px solid rgb(34, 34, 34), radius 50% | 36 by 36 |
| Accordion toggle | rgb(34, 34, 34) | transparent | Helvetica 14px / 19.6px / 0.2px, pad 20px 0 | 520 by 60 |
| Sign-in dialog | | rgb(255, 255, 255) | inner pad 80px 40px, radius 0 | 475 by 620 |
| Sign-in heading | rgb(34, 34, 34) | transparent | Helvetica 18px / 25.2px / 0.5px | |
| Sign-in subcopy | rgb(112, 112, 112) | transparent | Helvetica 12px / 16.8px / 0.5px | |
| Selected tab | rgb(34, 34, 34), border-bottom 2px solid rgb(34, 34, 34) | transparent | Helvetica 12px / 0.2px | |
| Resting tab | rgb(112, 112, 112), border-bottom 1px solid rgb(221, 221, 221) | transparent | Helvetica 12px / 0.2px | |
| Phone field | rgb(34, 34, 34) | rgb(255, 255, 255) | Helvetica 16px / 0.2px, border 1px solid rgb(34, 34, 34), radius 0, pad 10px 10px 10px 44px | 296 by 45 |
| Country select | rgb(34, 34, 34) | rgb(255, 255, 255) | Helvetica 16px, border 1px solid rgb(112, 112, 112), radius 5px | 94 by 45 |
| Primary submit (Next) | rgb(255, 255, 255) | rgb(34, 34, 34) | Helvetica 16px / 0.5px, weight 700, pad 10px 20px, radius 0 | 395 by 45 |
| Close button | rgb(34, 34, 34) | transparent | radius 50% | 44 by 44 |
| Women's heading | rgb(34, 34, 34) | transparent | Helvetica 18px / 25.2px / 0.5px | |
| Grid promo price | rgb(58, 135, 0) | transparent | Helvetica 12px / 0.2px | |
| Filter button | rgb(34, 34, 34) | transparent | Helvetica 14px / 0.2px | |

## Authored rules read from accessible stylesheets

- `:focus-visible` outline is `1.5px solid var(--focus-ring)`. `--focus-ring` resolves to rgb(112, 112, 112).
- `.c-pwa-header-navigation__link:hover` sets colour to `--link-navigation-text-hover` (rgb(112, 112, 112)) and underline, with a 1px bottom border of `--link-navigation-border-hover` (rgb(170, 170, 170)).
- `.c-pwa-site-account-menu__link:hover` sets colour to `--link-navigation-utility-text-hover` (rgb(112, 112, 112)).
- `.o-pwa-button-primary` uses `--button-primary-*`. Hover and focus (not `.is-rested`) use the hover tokens. Disabled uses `--button-primary-background-disabled` (rgb(170, 170, 170)). Padding 10px 20px, font-size 1.6rem, weight `--font-body-bold` (700).
- `.o-pwa-button-cart` uses `--button-cart-*`. Hover background is rgb(112, 112, 112). Confirmation background is rgb(58, 135, 0). Disabled background is rgb(170, 170, 170).
- Header transition is `top 0.35s linear`. Banner arrow colour transitions `0.15s cubic-bezier(0.645, 0.045, 0.355, 1)`. Search submit background transitions `0.05s ease-in`.
- Two `prefers-reduced-motion` rules were present in accessible stylesheets. The live page was not re-read under reduced motion.

## Not entered

The sign-in dialog asks for a mobile number and a verification code. The email tab was not submitted. No phone number, email, card, or bag action was entered.
