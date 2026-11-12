# Buy Me a Coffee patterns

How the measured components combine on buymeacoffee.com's public surface, read
from the screenshots and the component entries in
[components.md](components.md). The site paints two light frontends: the Nuxt
marketing pages (home, faq, reviews, blog, brand, about, stream-alerts, terms)
on a `#faf8f0` cream field, and the Vite-built creator page and login card
(/cara.app, /login, /signup) on white, themed per creator by inline
`--theme-color*` vars.

## The marketing header

Every marketing page carries the same white bar
([header](components/crops/header-default.png), 76px high): the coffee-cup
wordmark ([logo](components/crops/logo-default.png), 175 x 30), the `FAQ` and
`Wall of ♥` links and the `Apps`/`Resources` dropdown triggers
([nav-link](components/crops/nav-link-default.png),
[nav-trigger](components/crops/nav-trigger-default.png), Circular Medium
16/24), a fake `Search creators` pill on a 3%-black field
([nav-search](components/crops/nav-search-default.png), 24px radius), `Log in`
([nav-login](components/crops/nav-login-default.png)) and the yellow `Sign up`
pill ([nav-cta](components/crops/nav-cta-default.png), 48px). Links and
triggers hover to a 5%-black pill drawn by a `::before` layer at a 40px
radius; the yellow pill keeps the same `#ffdd00` paint in every state — the
`::before` just grows ~2%/4% on hover. The `Apps` trigger opens a white
drop-down panel at a 12px radius under a three-layer shadow
([nav-dropdown](components/crops/nav-dropdown-default.png),
[menu-link](components/crops/menu-link-default.png), Circular Bold rows at a
10px radius with a dark-5% hover fill,
[home-light-menu](screenshots/home-light-menu.png)); the search pill opens a
Trending overlay ([home-light-search](screenshots/home-light-search.png)).
Keyboard focus keeps Chromium's 1px `#005fcc` auto outline — no custom ring is
declared on the marketing pages.

## The home hero and sections

The home page opens over the cream field
([home-light-default](screenshots/home-light-default.png)): the five-star
`Loved by 2,000,000+ creators` rating row
([rating](components/crops/rating-default.png)), the 96px `Fund your creative
work` display in Circular Bold at -2.4px tracking
([hero-title](components/crops/hero-title-default.png)), the 22px tagline
([hero-sub](components/crops/hero-sub-default.png)) and the yellow `Start my
page` pill ([hero-cta](components/crops/hero-cta-default.png), 74px high on a
9999px painted pill). Floating creator tiles drift over the hero
([creator-card](components/crops/creator-card-default.png), white at a 16px
radius under the three-layer menu shadow). Sections repeat a grammar: a 16px
uppercase `#717171` eyebrow in Circular Bold at +2px tracking
([section-eyebrow](components/crops/section-eyebrow-default.png)), a 64px
Circular Bold heading at -2px tracking
([section-h2](components/crops/section-h2-default.png)) and a 24px Circular
Regular lede ([section-lede](components/crops/section-lede-default.png)),
revealing on an 0.8s scroll animation
([home-light-full](screenshots/home-light-full.png)).

## The creator page

`/cara.app` paints the real product surface signed out
([creator-light-default](screenshots/creator-light-default.png),
[creator-light-full](screenshots/creator-light-full.png)). A sticky 64px
white bar ([c-header](components/crops/c-header-default.png), 1px 6% shadow)
carries the avatar and name, the `Home`/`Membership`/`Wishlist` tabs
([c-tab](components/crops/c-tab-default.png), Circular Medium 15px, the
active one accent-orange), the more-options ellipsis
([c-more](components/crops/c-more-default.png)) and `Login`
([c-login](components/crops/c-login-default.png)). The ellipsis opens a small
menu — `Follow`, `Share`, `Report` at 186 x 36 rows
([c-context](components/crops/c-context-default.png),
[c-follow](components/crops/c-follow-default.png),
[c-share](components/crops/c-share-default.png),
[creator-light-menu](screenshots/creator-light-menu.png)).

Below the cover, an `About Cara` box
([c-about](components/crops/c-about-default.png)) sits beside the support
widget ([c-widget](components/crops/c-widget-default.png), 500px wide, white
at a 24px radius): a `Buy Cara a coffee` title in Circular Bold 24px, the
coffee-count pills ([c-qty-on](components/crops/c-qty-on-default.png),
[c-qty-off](components/crops/c-qty-off-default.png) — 48px circles at 9999px,
selected fills accent, unchecked is white with the accent count and a 25%
accent hairline), a custom-amount field
([c-amount](components/crops/c-amount-default.png), 12px radius), the `Name
or @yoursocial` field ([c-name](components/crops/c-name-default.png), 52px on
a `#f0f0f0` fill at 12px — focus turns it white with a 2px accent border and
a 4px `#2563eb` ring), the `Say something nice…` textarea
([c-message](components/crops/c-message-default.png)), the `Make this
monthly` and `Make this message private` checkboxes
([c-monthly](components/crops/c-monthly-default.png),
[c-private](components/crops/c-private-default.png), 6px-radius boxes —
[creator-light-three](screenshots/creator-light-three.png) and
[creator-light-monthly](screenshots/creator-light-monthly.png) show them
toggled) and the accent `Support $5` pill
([c-support](components/crops/c-support-default.png), 48px, 9999px, white
label, `#ff6b1c` on hover — a submit, never pressed). A `Recent supporters`
list rows names and coffee counts
([c-supporter](components/crops/c-supporter-default.png)), and `Become a
member` groups tier cards ([c-tier](components/crops/c-tier-default.png))
with their own accent Join pills
([c-join](components/crops/c-join-default.png), never followed).

## The login card

`/login` centres a Welcome-back card on white
([login-light-default](screenshots/login-light-default.png)): the title
([l-title](components/crops/l-title-default.png)), the Email field
([l-email](components/crops/l-email-default.png), 48px on `#f0f0f0` at 12px —
focus turns it white with a 2px `#151515` border; it was filled once with a
throwaway address and cleared), the yellow `Continue with email` pill
([l-cta](components/crops/l-cta-default.png), 48px 9999px, `#ffc800` on
hover — a submit, never pressed), an `or login with` divider
([l-divider](components/crops/l-divider-default.png)) and the bordered white
social buttons ([l-social](components/crops/l-social-default.png), 1px
`#e5e5e5`, never pressed). The Password input lives in a second step behind
the submit and was never reached.

## Wall of love, FAQ, footer

`/reviews` tiles tweet-style testimonial cards
([r-tweet](components/crops/r-tweet-default.png), white 24px radius under a
4px card shadow, ~3% lift on hover,
[reviews-light-full](screenshots/reviews-light-full.png)) behind a Borel
title ([r-title](components/crops/r-title-default.png)) and 40px square
bordered slide buttons ([r-slide](components/crops/r-slide-default.png),
black fill on hover). `/faq` pairs a 48px Borel title
([f-h1](components/crops/f-h1-default.png)) with static 20px Circular Medium
questions ([f-q](components/crops/f-q-default.png)) and 18px Circular Regular
answers ([f-a](components/crops/f-a-default.png)) plus bordered
Contact-support pills ([f-cta](components/crops/f-cta-default.png), 40px
paint radius). The footer is a white bar of `Apps`/`Resources`/`Legal`
drop-up triggers ([footer-trigger](components/crops/footer-trigger-default.png))
that open small link panels ([footer-menu](components/crops/footer-menu-default.png),
[footer-link](components/crops/footer-link-default.png)) beside the socials
([footer-social](components/crops/footer-social-default.png), ~10% scale on
hover).

## Mobile

At 390 wide the header slims to 65px
([m-header](components/crops/m-header-default.png)) and the burger
([m-menu-button](components/crops/m-menu-button-default.png)) slides a
full-screen white panel in over 0.3s
([m-menu-open](components.md#mobile-menu-open),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) with 20px
Circular Medium rows ([m-nav-item](components/crops/m-nav-item-default.png)).
The display falls to 48px at -1.2px tracking
([m-hero](components/crops/m-hero-default.png),
[mobile-home-light-full](screenshots/mobile-home-light-full.png)); the
creator page stacks the widget under the profile
([mobile-creator-light-full](screenshots/mobile-creator-light-full.png)).
