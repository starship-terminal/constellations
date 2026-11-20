# Navia patterns

How the measured components compose on www.thenavia.com. Values are in [components.md](components.md) and [tokens.json](tokens.json). The control map is [site-tree.md](site-tree.md).

## The shell

A 72px transparent header on the cream page: wordmark, Platform, Pricing, Resources, and a chartreuse Get started pill. The pill's fill is an inner `.button-base`, not the anchor. At 390 the links collapse behind a menu button of three 24 by 2 bars. Opening it shows the same links plus Get started for free. [home-light-default](screenshots/home-light-default.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## The hero and features

A left-aligned Lora hero at 56px, a chartreuse primary pill, and a secondary Book a demo link. Four feature rows act as buttons. Clicking one adds `is-active` and removes it from the others. The row itself stays transparent. [home-light-feature](screenshots/home-light-feature.png).

## Plans

Three static cards: Basic, Business, Growth. Each Sign up link goes to the app wall. There is no billing toggle. [home-light-default](screenshots/home-light-default.png).

## Blog

An 80px Lora title, article cards, and a Next control that walks `?55a1b861_page=`. Page 2 was captured. Pages 3 and 4 were mapped and not shot. A post is one column of article type with related cards and a Get started link to the wall. [blog-light-default](screenshots/blog-light-default.png), [post-light-default](screenshots/post-light-default.png).

## Contact

A cream form: 44px fields at 4px radius, a 44px topic select, a 180px message area, and a 48px orange pill. Focus turns a field white. The select was focused and no option was chosen. The form was not submitted, so validation, loading, and success are absent. A published mailbox line on the page was hidden before the shot. [contact-light-default](screenshots/contact-light-default.png), [contact-light-select-focused](screenshots/contact-light-select-focused.png).

## Overlays

CookieYes mounts on first paint: Customise, Reject All, Accept All. Customise opens a preference center. Reject All was used. Accept All was not. A Flodesk newsletter popup mounts on its own. It was closed and not filled. [home-light-cookies](screenshots/home-light-cookies.png), [home-light-cookie-preferences](screenshots/home-light-cookie-preferences.png).

## Walls

Get started, plan Sign up, and the app host open https://app.thenavia.com/, which asks the visitor to sign in. That page was recorded. Sign In was not followed past the Cloudflare check on accounts.thenavia.com. [app-wall-light-default](screenshots/app-wall-light-default.png).
