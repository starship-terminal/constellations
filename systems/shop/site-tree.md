# Shop public site tree

Mapped on 2026-11-22 from the public homepage, https://shop.app/, which redirects to https://shop.com/. Title: "Shop - Shopping designed around you". Incognito preview tab. Desktop shots are 1440 by 900 CSS pixels at 2x (PNG 2880 by 1800). Phone shots are 390 by 844 CSS pixels at 2x (PNG 780 by 1688). The page is a live shopping surface, not a parked domain and not a captcha wall.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider, wallet, or passkey was used. No captcha was solved. Nothing was added to cart, bought, or followed. `login-extracted` stays not-started. catalog.json was left alone.

The same empty form is the login wall and the signup wall. Its heading is "Sign in to Shop" and the line under it is "Or create an account". There is no separate signup URL on the public controls. Orders and saved items redirect into an OAuth login URL. Those URLs were not photographed.

## Header

Desktop is a fixed left rail, 96px wide. Phone replaces that rail with a bottom bar and a wordmark.

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Home wordmark | link | https://shop.com/?_m_home=1 | home |
| Home | link | https://shop.com/?_m_home=1 | photographed |
| Explore | link | https://shop.com/categories | photographed |
| View Cart | link | https://shop.com/cart | empty cart, photographed |
| Deals | link | https://shop.com/deals | photographed |
| Orders | link | https://shop.com/orders | OAuth login redirect. Stop. Not photographed. |
| Sign in to view saved items | button | same OAuth login path as Orders | not clicked |
| Sign in | button | https://shop.app/accounts/login | empty wall, photographed |
| Search | searchbox | suggested searches, not typed | left empty |
| Attach image | button | image picker | not used |
| Download the Shop app | card | https://shop.com/download | photographed. Store badges not clicked. |
| Dismiss app download prompt | button | hides the card | not clicked |

Phone bottom bar, left to right: Home, Explore, View Cart, Orders, Sign in. Orders and Sign in are the same walls as the desktop rail.

## Homepage chips and hero

| Control | Destination | This pass |
|---|---|---|
| Holiday Sale | https://shop.com/deals | same page as the Deals rail |
| Gifts | https://shop.com/events/bfcm-26 | not opened as its own shot. Deals is the photographed sale page. |
| Beauty | https://shop.com/categories/5/beauty | photographed as the category sample |
| Women | https://shop.com/categories/1/women | same category pattern. Not a second shot. |
| Men | https://shop.com/categories/2/men | same category pattern |
| Baby & toddler | https://shop.com/categories/209/baby-toddler | same category pattern |
| Sporting goods | https://shop.com/categories/267/sporting-goods | same category pattern |
| Explore chip | https://shop.com/categories | same page as the Explore rail |
| Hero, slide 2 | https://shop.com/edits/korean-beauty | photographed |
| Hero, slide 1 | https://shop.com/offers | redirects to https://shop.com/deals |
| Explore Korean beauty | https://shop.com/edits/korean-beauty | same edit page |
| A trending store | https://shop.com/m/mykitsch | photographed as the store sample. Follow not clicked. |
| A product tile | https://shop.com/products/8143720153269/smoothing-air-dry-cream | photographed. Add to cart and Buy now not clicked. |
| Add to saved items | login wall | not clicked |
| Categories heading | https://shop.com/categories | same Explore page |

Other category tiles on the homepage (Home, Fitness & nutrition, Food & drinks, Toys & games, Pet supplies) use the same `/categories/<id>/<slug>` pattern as Beauty.

## Footer

Photographed on the What is Shop page: [public-footer-desktop.png](screenshots/public-footer-desktop.png). Columns: Learn more, Get started, Social, Legal. The copyright line reads "© Shopify Inc. 2026". Language was left on English.

| Control | Destination | This pass |
|---|---|---|
| What is Shop? | https://shop.com/what-is-shop | photographed |
| Why trust Shop? | https://shop.com/trust | photographed |
| Why use Shop Pay? | https://shop.com/buy-with-shop | photographed. A marketing page, not checkout. |
| Help center | https://help.shop.app/shop | off the shopping host. Not opened. |
| For brands | https://www.shopify.com/shop | Shopify, not Shop. Not opened. |
| For creators | https://www.shopify.com/collabs/creators | Shopify. Not opened. |
| For agents | https://shop.md/ | another host. Not opened. |
| Build your store | https://www.shopify.com/free-trial | Shopify trial. Not opened. |
| Instagram | https://instagram.com/shopapp | another product. Not opened. |
| Terms of Service | https://shop.com/terms-of-service | photographed |
| Privacy Policy | https://www.shopify.com/legal/privacy/app-users | Shopify legal. Not opened. |
| Your Privacy Choices | https://privacy.shopify.com/ | Shopify privacy. Not opened. |
| Download on the App Store | https://open.shop.app/... | store deep link. Not clicked. |
| Download on Google Play | https://open.shop.app/... | store deep link. Not clicked. |
| Language | https://shop.com/language-settings | photographed. Update not clicked. |

## Login and signup wall

https://shop.app/accounts/login is the wall Sign in opens. Title: "Log in to your Shop account | Shop". The email field was empty (`value` length 0). Continue was not clicked. Use a passkey was not clicked. English was not changed. Terms and Privacy Policy on this wall were not followed.

| Control | What it would do | This pass |
|---|---|---|
| Email field | stays on the form | left empty |
| Continue | submits the email | not clicked |
| Use a passkey | passkey prompt | not clicked |
| Terms | https://shop.app/terms-of-service | same terms page as the footer |
| Privacy Policy | Shopify legal | not opened |
| English | language menu | not opened |

## Stopped

| Control | Why |
|---|---|
| Orders | Redirects to an OAuth login URL with `auth_state` and `next=OAuthContinue`. Not photographed. |
| Saved items | Same OAuth path. Not clicked. |
| Continue, passkey, identity providers, wallets | Auth wall. |
| Add to cart, Buy now | Checkout path. |
| Follow a store, Add to saved items | Account action. |
| App Store and Google Play badges | Store deep links. |
| Help center, For brands, For creators, For agents, Build your store, Instagram, Privacy Policy, Your Privacy Choices | Leave the Shop shopping host. |
