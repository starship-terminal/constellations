# Kinhive components

Measured from the public site on 2026-11-18 at 1440 and 390, plus the join and sign-in code step after those forms were submitted. Values are the declared custom properties in [tokens.json](tokens.json) where a computed colour matches one, and computed sizes where the site uses a Tailwind utility. Crops are in [components/crops/](components/crops).

## Promo bar

A chocolate strip (`light.color.chocolate` is not the strip; the strip is a dark brown photo-adjacent band, sampled as the page's top bar) sits above the nav and carries "Kinhive is free, forever." plus a Join today link. See [promo-bar-default](components/crops/promo-bar-default.png) and [home-light-default](screenshots/home-light-default.png).

## Navigation

The header is 65px, sticky, transparent over the page. The wordmark is an inline SVG, 97 by 15, labelled "Kinhive home". Links are Figtree 14px/500, ink at 85% opacity, 8px radius, 8px 12px padding. Join free is an ink fill, white label, 32px tall, 8px radius. See [nav-logo-default](components/crops/nav-logo-default.png), [nav-join-default](components/crops/nav-join-default.png), [nav-login-default](components/crops/nav-login-default.png).

Features and Use Cases are buttons with `aria-expanded`. Opening Features paints a mega-menu: chartreuse icon chips, a column of also-in-Kinhive rows, and a chocolate pricing card. See [nav-features-opened](components/crops/nav-features-opened.png) and [nav-menu-default](components/crops/nav-menu-default.png).

On a 390px viewport the same links collapse behind an "Open menu" button. The drawer is a full-screen sheet with Join free, Log in, and the feature list. See [m-menu-btn-default](components/crops/m-menu-btn-default.png) and [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png).

## Hero

The home h1 is Affairs, 44px at 1440, ink, line-height 1.05, inside a butter card. The email field is `#hero-email`, 44px tall, transparent, Figtree 15px. The submit control is a 44px ink square. See [hero-h1-default](components/crops/hero-h1-default.png), [hero-email-default](components/crops/hero-email-default.png), [hero-submit-default](components/crops/hero-submit-default.png).

## Pricing card

The free plan is a chartreuse card (`core.color.chartreuse` #d4e31f) with an Affairs $0, an ink Join free pill, and a check list. The coffee card beside it is a raised wash. See [price-card-default](components/crops/price-card-default.png) and [price-cta-default](components/crops/price-cta-default.png).

## Blog filters

Category chips are 8px-radius pills. "All posts" is the selected chip (raised fill). The rest are outlined. See [blog-tab-selected](components/crops/blog-tab-selected.png).

## Contact form

Name, email, a topic select, and a message textarea sit on a canvas panel. The select and textarea use the line border (`light.border.line` #e6e6e3) and 8px radius. Send message is a full-width ink button, 44px. The form was not submitted. See [contact-select-default](components/crops/contact-select-default.png), [contact-textarea-default](components/crops/contact-textarea-default.png), [contact-submit-default](components/crops/contact-submit-default.png).

## Join and sign-in

`/join` and `/sign-in` drop the marketing chrome for a split layout: a form column and a photograph. Fields are white, line-bordered, 8px radius. Continue and "Email me a sign-in code" are full-width ink buttons. LinkedIn is an outlined button. The 2026-11-21 walk photographed both walls empty and did not click Continue or LinkedIn. See [signin-light-empty](screenshots/signin-light-empty.png) and [join-light-empty](screenshots/join-light-empty.png).

## Cart

The shop cart is a right-hand drawer. Empty state copy and a "Browse the shop" link. Opened, not checked out. See [cart-drawer-default](components/crops/cart-drawer-default.png) and [shop-light-cart](screenshots/shop-light-cart.png).

## Gaps

- Checkbox, radio, switch, tooltip, toast, table, avatar, and badge do not appear on the public surface. The chartreuse icon chips in the mega-menu are the closest badge.
- Loading and success states do not appear. Contact, subscribe, and the hero email were not submitted. `--color-alert` (#f2a516) is still unused. `--color-destructive` (#d93a1f) paints as join and sign-in error text.
- Pressed and hover were not forced. The ink CTA declares `hover:bg-[#2a2a2c]`, recorded as `light.action.fill-hover`.
- The signed-in app (`/home`, `/matches`, `/chat`, `/cowork`, `/profile`, `/settings`, and the other robots.txt disallows) was not opened: the 6-digit code email never arrived.
- Focus rings are the browser outline plus `focus:ring-3 focus:ring-ink/10` on fields. A designed focus token beyond `light.border.focus` (ink) was not isolated.
