# Kickstarter public site tree

Walked signed out on 2026-11-21 from [https://www.kickstarter.com/](https://www.kickstarter.com/) (HTTP 200, title Kickstarter). Desktop viewport 1440 by 900. Phone viewport 390 by 844. The product is live. It is not parked, sunset, or a captcha wall.

The Transcend card ("We use personal data") was hidden with CSS. Confirm and Accept all were not clicked. Query strings on project links are stripped in this file. No page-level theme switch was found. The public site paints light. `theme-color` is `#05CE78`.

Opened means the control was used and the destination loaded or the panel was photographed. Linked means the href was read and the page was not opened in this pass. Stop means the control opens a login, signup, checkout, pledge, or identity-provider wall and the branch stopped.

## Header, desktop

The wordmark links to `/?ref=nav`. Search is an input (`#global-nav-search-input`, placeholder "Search projects, creators, and categories"). Focusing it stays on `/`. Photographed in [home-light-search-focused.png](screenshots/home-light-search-focused.png). Nothing was typed and nothing was submitted.

For creators links to `/creators?ref=nav` and was opened. Log in is a button with no href. Clicking it keeps the URL on `/` and opens a dialog titled "Log in". See the login wall below. Not photographed into the package.

| Control | Opens |
|---|---|
| Wordmark | `/` |
| Search (focus) | in-page. URL stays `/`. |
| For creators | `/creators` |
| Log in | dialog on `/`. Wall. Branch stopped. |

## Category row, desktop

Each name is an anchor with `aria-haspopup` and `aria-expanded`. Hovering one keeps the URL on `/` and opens a drawer. Art was hovered. Photographed in [home-light-category-menu.png](screenshots/home-light-category-menu.png).

| Control | Opens |
|---|---|
| Art | `/discover/categories/art`. Drawer subcategories: Ceramics, Conceptual Art, Digital Art, Illustration, Installations, Mixed Media, Painting, Performance Art, Public Art, Sculpture, Social Practice, Textiles, Video Art. Filters in the same drawer: Projects We Love, Trending, Nearly Funded, Just Launched, Projects Near You, Upcoming Projects. |
| Comics | `/discover/categories/comics`. Linked. |
| Crafts | `/discover/categories/crafts`. Linked. |
| Dance | `/discover/categories/dance`. Linked. |
| Design | `/discover/categories/design`. Linked. |
| Fashion | `/discover/categories/fashion`. Linked. |
| Film | `/discover/categories/film%20&%20video`. Linked. |
| Food | `/discover/categories/food`. Linked. |
| Games | `/discover/categories/games`. Opened. |
| Journalism | `/discover/categories/journalism`. Linked. |
| Music | `/discover/categories/music`. Linked. |
| Photography | `/discover/categories/photography`. Linked. |
| Publishing | `/discover/categories/publishing`. Linked. |
| Technology | `/discover/categories/technology`. Linked. |
| Theater | `/discover/categories/theater`. Linked. |
| Discover | `/discover`. Drawer tags read from the open panel: Collectibles, Forward Fund: Next Wave, Genre Fiction, Imaginative Worlds, Kickstarter Culture Fund, LGBTQIA+, Magic & Divination, PNW RPG Fest, Robots, Romance, RPGs, Sci-Fi and Fantasy, STEM, Superbacker Launches, Make 100, Zine Quest, Long Story Short, Micro May, Kiss & Tell, Witchstarter, Join an Open Call (`/open-calls`), AANHPI Creators, Black Creators, Hispanic and Latin Creators, LGBTQIA+ Creators, Women Creators. The Discover page itself was opened. |

## Header, phone (390)

The island is the wordmark, For creators, Log in, and a hamburger. Photographed in [mobile-home-light-default.png](screenshots/mobile-home-light-default.png). The category row collapses to a horizontal scroller. Log in is the same dialog wall. The hamburger was visible and not opened.

## Homepage body

URL stays `/` unless noted. Photographed in [home-light-default.png](screenshots/home-light-default.png) and [home-light-full.png](screenshots/home-light-full.png).

| Control | Result |
|---|---|
| Explore the app | `https://launch.kickstarter.com/shopify`. Linked. Not a pledge. |
| Featured project card | `/projects/arex/arex-ar-dive-computer-mask-and-marine-life-identification`. Opened as the public project page. Back this project was not clicked. |
| Project We Love badge | `/discover/pwl`. Linked. |
| Creator name on a card | `/profile/<slug>`. Linked. A public profile may show a name, so it was not photographed. |
| Save this project | button, no href. Not clicked. Save is an account action. |
| Category and place chips on a card | `/discover/categories/...` and `/discover/places/...`. Linked. |
| Discover more (recommendations) | `/discover/advanced?state=live&backed=-1&created=-1&recommended=1`. Linked. |
| Collection pager (1, 2, 3) | buttons. URL stays `/`. Not used as navigation. |
| Discover more (collection) | `/discover/advanced` with a tag id. Linked. |

## Footer

Read from the homepage. Social and store links were not followed.

| Control | Opens |
|---|---|
| Arts | `/arts` |
| Comics & Illustration | `/comics-illustration` |
| Design & Tech | `/design-tech` |
| Film | `/film` |
| Food & Craft | `/food-craft` |
| Games | `/games` |
| Music | `/music` |
| Publishing | `/publishing` |
| About us | `/about`. Opened. |
| Our charter | `/charter`. Linked. |
| Press | `/press`. Opened. |
| Jobs | `/jobs`. Linked. |
| Status | `/status`. Linked. |
| Help Center | `/help`. Linked. |
| Our Rules | `/rules`. Opened. |
| Creator Resources | `/learn`. Linked. |
| Forward Funds | `/forward-funds`. Linked. |
| Brand assets | `/help/brand_assets`. Linked. |
| Newsletters | `/newsletters`. Linked. Not submitted. |
| Kickstarter Project Updates | `https://updates.kickstarter.com`. Linked. |
| The Creative Independent | `https://thecreativeindependent.com`. Linked. |
| Mobile apps | `/mobile`. Linked. |
| Research | `/research`. Linked. |
| Trust & Safety | `/trust`. Opened. |
| Terms of Use | `/terms-of-use`. Linked. |
| Privacy Policy | `/privacy`. Linked. |
| Cookie Policy | `/cookies`. Linked. |
| Accessibility Statement | `/accessibility`. Linked. |
| CA Notice of Consent | `/privacy#privacy-information-for-california-residents`. Linked. |

## Login wall

Log in opens a dialog on the current URL, labelled "Log in". Copy read and not submitted: "Log in or sign up". Field seen and left empty: email (`passwordless-email`, placeholder "name@email.com"). Checkbox seen and not used: "Remember this device for 30 days". Actions seen and not used: Continue, Sign in with Apple, Dismiss dialog. A link to `/facebook_account_recovery` was not followed. Google was not offered in this dialog. No identity provider was clicked. Nothing was typed. The dialog was closed with Escape.

`/login` loaded as its own URL and stayed a public form with no account chrome. Photographed in [login-light-default.png](screenshots/login-light-default.png) and [mobile-login-light-default.png](screenshots/mobile-login-light-default.png). Continue was not clicked. Apple was not clicked. A Cloudflare "Verify you are human" box was visible on the phone card and was not solved.

## Create

`/start` is the public start page. It was opened. Next was not clicked. No project was created. No form was submitted.

## Pledge

A public project page shows Back this project. That control was not clicked. Checkout and pledge were not opened.
