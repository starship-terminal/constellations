# Cosmos site tree

Mapped 2026-11-21 in headless Chromium from [https://www.cosmos.so/](https://www.cosmos.so/). Desktop viewport 1440 x 900. Phone viewport 390 x 844. Nothing was typed, submitted, or downloaded. A login wall stops that branch.

Theme: no public theme control. `data-theme` stays `light` and `color-scheme` stays `light` when the browser prefers dark. Dark values in the package are declared CSS, not a painted theme.

## Shell

The same header sits on the marketing and discovery pages.

| Control | Opens |
|---|---|
| Mark (header, left) | [https://www.cosmos.so/](https://www.cosmos.so/) |
| Explore | [https://www.cosmos.so/explore](https://www.cosmos.so/explore) |
| Sequence | [https://www.cosmos.so/sequence](https://www.cosmos.so/sequence) |
| Shop | [https://www.cosmos.so/explore/shop](https://www.cosmos.so/explore/shop) |
| Wordmark COSMOS | [https://www.cosmos.so/](https://www.cosmos.so/) |
| Search combobox (`input[name="search"]`, role combobox) | Focus sets `aria-expanded="true"` and clears the placeholder. No suggestion list opened with an empty field. Nothing was typed, so no results page was submitted from here. |
| Visual search (explore, shop, search, brand, profile, product) | In-page drop zone: "Upload an image to find visually similar results". The "upload file" control is a file picker. No file was chosen. [explore-light-visual-search.png](screenshots/explore-light-visual-search.png) |
| Color search (palette icon, also labelled Color search) | Dialog: colour canvas, hue strip, hex field `color-search-input` (placeholder `#`), a plus button, and Add. Add was not pressed. Nothing was typed. [home-light-color-search.png](screenshots/home-light-color-search.png) |
| Log in | Login wall. See below. |
| Sign up | [https://www.cosmos.so/start](https://www.cosmos.so/start). Email field present. Nothing typed. Next not pressed. |

Phone header (390): wordmark, a Download pill, and a Menu button (aria-label Menu). Download points at the App Store (`apps.apple.com`, id 1577975475). It was not pressed. Menu opens a full-screen dialog. Close (X) dismisses it. [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png)

| Menu item | Opens |
|---|---|
| Home | [https://www.cosmos.so/](https://www.cosmos.so/) |
| Explore | [https://www.cosmos.so/explore](https://www.cosmos.so/explore) |
| Sequence | [https://www.cosmos.so/sequence](https://www.cosmos.so/sequence) |
| Careers | [https://www.cosmos.so/careers](https://www.cosmos.so/careers) |
| Sign up | [https://www.cosmos.so/start](https://www.cosmos.so/start) |
| Close | Dismisses the dialog. Stays on the current page. |

Shop is not in the phone menu. Phone `/login` does not show the password card. It shows "Download Cosmos" and a Download app button. That button was not pressed. [mobile-login-light-default.png](screenshots/mobile-login-light-default.png)

## Home `/`

| Control | Opens |
|---|---|
| Rotating hero phrase (a link, for example "lamp with character") | A public search path such as [https://www.cosmos.so/search/elements/lamps](https://www.cosmos.so/search/elements/lamps). The phrase cycles. The shot caught "forever chair" and "go-to outfit" as well. |
| Search field | Same combobox as the shell. Focus only. [home-light-search-focus.png](screenshots/home-light-search-focus.png) |
| Color search | The colour dialog, over the home hero. |
| Join Cosmos for free | [https://www.cosmos.so/start](https://www.cosmos.so/start) |
| Get the app (QR card, bottom right) | A painted card with an Apple mark and a QR code. It is not a link that was followed. The phone Download pill is the control that points at the App Store. Neither was used to download. |
| Down chevron under the hero | In-page scroll. Stays on `/`. |
| Feature carousel Next | In-page. Advances the "Build your world, your way" cards. Stays on `/`. |
| Show, Blur, Hide (role tab, inside the Hide AI card) | In-page. Show is selected on load. Blur and Hide change `aria-selected` and the demo tiles in the card. [home-light-ai-blur.png](screenshots/home-light-ai-blur.png), [home-light-ai-hide.png](screenshots/home-light-ai-hide.png) |
| Brand names under "Shop from brands like" | One public brand page each. Studio Ford, Christopher Esber, St. Agni, Khaite, Róhe, NILI LOTAN, Gimaguas. Example: [https://www.cosmos.so/brand/studio-ford](https://www.cosmos.so/brand/studio-ford) |
| Explore Cosmos | [https://www.cosmos.so/explore](https://www.cosmos.so/explore) |
| A profile name or avatar in "Find what others are saving" | [https://www.cosmos.so/{handle}](https://www.cosmos.so/) (public profile). Example captured: [https://www.cosmos.so/laurentdelrey](https://www.cosmos.so/laurentdelrey) |
| Follow (on each profile row) | No dialog opened and the URL did not change. Not pressed again. Treated as a signed-in action that does nothing useful while signed out. |

Footer, on the home page and repeated on discovery pages:

| Control | Opens |
|---|---|
| Sign up | [https://www.cosmos.so/start](https://www.cosmos.so/start) |
| Log in | Login wall |
| Sequence | [https://www.cosmos.so/sequence](https://www.cosmos.so/sequence) |
| Instagram | [https://www.instagram.com/cosmos/](https://www.instagram.com/cosmos/). External. Not opened. |
| TikTok | [https://www.tiktok.com/@cosmos](https://www.tiktok.com/@cosmos). External. Not opened. |
| X | [https://x.com/thecosmos](https://x.com/thecosmos). External. Not opened. |
| Careers | [https://www.cosmos.so/careers](https://www.cosmos.so/careers) |
| Terms | [https://www.cosmos.so/legal/terms-conditions](https://www.cosmos.so/legal/terms-conditions) |
| Privacy | [https://www.cosmos.so/legal/privacy-policy](https://www.cosmos.so/legal/privacy-policy) |
| Copyright | [https://www.cosmos.so/legal/copyright-policy](https://www.cosmos.so/legal/copyright-policy) |
| Contact | A mailto link. Not opened. The address is not recorded here. |

## Explore `/explore`

| Control | Opens |
|---|---|
| Search, Visual search, Color search | Same as the shell. |
| Featured (tab, selected) | [https://www.cosmos.so/explore](https://www.cosmos.so/explore) |
| Fashion | [https://www.cosmos.so/explore/fashion](https://www.cosmos.so/explore/fashion) |
| Interiors | [https://www.cosmos.so/explore/interior-design](https://www.cosmos.so/explore/interior-design) |
| Graphic Design | [https://www.cosmos.so/explore/graphic-design](https://www.cosmos.so/explore/graphic-design) |
| Art | [https://www.cosmos.so/explore/art](https://www.cosmos.so/explore/art) |
| Branding | [https://www.cosmos.so/explore/branding](https://www.cosmos.so/explore/branding) |
| Typography | [https://www.cosmos.so/explore/typography](https://www.cosmos.so/explore/typography) |
| Architecture | [https://www.cosmos.so/explore/architecture](https://www.cosmos.so/explore/architecture) |
| Weddings | [https://www.cosmos.so/explore/weddings](https://www.cosmos.so/explore/weddings) |
| Interfaces | [https://www.cosmos.so/explore/interfaces](https://www.cosmos.so/explore/interfaces) |
| Nature | [https://www.cosmos.so/explore/nature](https://www.cosmos.so/explore/nature) |
| Cinema | [https://www.cosmos.so/explore/cinema](https://www.cosmos.so/explore/cinema) |
| Motion | [https://www.cosmos.so/explore/motion](https://www.cosmos.so/explore/motion) |
| Technology | [https://www.cosmos.so/explore/technology](https://www.cosmos.so/explore/technology) |
| Portraiture | [https://www.cosmos.so/explore/portraiture](https://www.cosmos.so/explore/portraiture) |
| Quotes | [https://www.cosmos.so/explore/quotes](https://www.cosmos.so/explore/quotes) |
| Emotion | [https://www.cosmos.so/explore/emotion](https://www.cosmos.so/explore/emotion) |
| Symbol & Myth | [https://www.cosmos.so/explore/symbol-myth](https://www.cosmos.so/explore/symbol-myth) |
| Go to next slide | In-page. Advances the "Selected by Cosmos" carousel. |
| A selected card (Giving thanks, window shopping, Dressed in icy blue, and the rest) | A public collection or cluster path: `/shop/{slug}`, `/design/{slug}`, `/style/{slug}`, `/ideas/{slug}`, `/spaces/{slug}`, `/art/{slug}`. Examples opened: `/shop/giving-thanks`, `/design/gift-guide-pages`, `/ideas/the-sun-had-a-face`, `/style/dressed-in-icy-blue1`, `/art/gatherings-in-paintings`, `/spaces/rooms-with-a-fireplace`. |
| @handle under a card | That public profile, for example `/shop` redirects to [https://www.cosmos.so/shop/collections](https://www.cosmos.so/shop/collections) and `/ideas` is [https://www.cosmos.so/ideas](https://www.cosmos.so/ideas). |
| Save (on a tile) | No dialog. URL unchanged. Not used as a save. |
| Suggestive (on a grey tile) | No dialog. URL unchanged. |
| An element tile | A public element or product path. One product opened from shop, below. |

Phone explore keeps the same category tabs in a horizontal scroller, plus Cancel in the search field. [mobile-explore-light-default.png](screenshots/mobile-explore-light-default.png)

## Shop `/explore/shop`

| Control | Opens |
|---|---|
| All | [https://www.cosmos.so/explore/shop](https://www.cosmos.so/explore/shop) |
| Womenswear | [https://www.cosmos.so/explore/shop/womenswear](https://www.cosmos.so/explore/shop/womenswear) |
| Menswear | [https://www.cosmos.so/explore/shop/menswear](https://www.cosmos.so/explore/shop/menswear) |
| Interiors | [https://www.cosmos.so/explore/shop/interiors](https://www.cosmos.so/explore/shop/interiors) |
| Gifts | [https://www.cosmos.so/explore/shop/gifts](https://www.cosmos.so/explore/shop/gifts) |
| Brands | [https://www.cosmos.so/explore/shop/brands](https://www.cosmos.so/explore/shop/brands) |
| Sale | [https://www.cosmos.so/explore/shop/sale](https://www.cosmos.so/explore/shop/sale) |
| View all (a mood row) | A public shop cluster, for example `/shop/a-softer-place-to-land` |
| A product tile (name and price, rendered as a button) | A public product page. Example: Artemide Tizio Floor Lamp opened [https://www.cosmos.so/product/artemide/534905610](https://www.cosmos.so/product/artemide/534905610) |
| A featured brand | `/brand/{slug}` |

Phone shop uses the same shell. [mobile-shop-light-default.png](screenshots/mobile-shop-light-default.png)

## Product `/product/{brand}/{id}`

Captured: Tizio Floor Lamp.

| Control | Opens |
|---|---|
| Brand name (Artemide) | [https://www.cosmos.so/brand/artemide](https://www.cosmos.so/brand/artemide) |
| More (in the description) | In-page. Expands the product copy. A shorter label replaces it. |
| Shop (the grey pill on the product, with an external-arrow) | Leaves cosmos.so for `https://buy.trychannel3.com/{id}`. Not followed. No purchase. |
| Saved by N others | Dialog: "0 Profiles 0 Collections" on this signed-out session. Escape closes it. |
| Save | No dialog while signed out. Not used as a save. |
| You may also like / See more like this | In-page section of related tiles. Each tile is another public element. |
| Sign up / Log in in the related-items prompt | `/start` and the login wall. |

## Search `/search/elements/{query}`

Reached from the home hero link, not by typing. Example query: lamps.

| Control | Opens |
|---|---|
| Elements (tab, selected) | [https://www.cosmos.so/search/elements/lamps](https://www.cosmos.so/search/elements/lamps) |
| Products | [https://www.cosmos.so/search/products/lamps](https://www.cosmos.so/search/products/lamps). In-page tab. [search-light-products.png](screenshots/search-light-products.png) |
| Collections | [https://www.cosmos.so/search/collections/lamps](https://www.cosmos.so/search/collections/lamps) |
| A result tile | A public element, product, or collection. |

The feed is long. The full shot stops at the 8-chunk bound (19949 px).

## Brand `/brand/{slug}`

Captured: Studio Ford.

| Control | Opens |
|---|---|
| Follow | No navigation while signed out. Not used as a follow. |
| Sort (aria-haspopup listbox) | Listbox on the same page: Latest, Price: Low to high, Price: High to low. Escape closes it. No option was chosen. |
| Price (aria-haspopup dialog) | Dialog: "Price range", Reset, a low field and a high field ($50 to $6.8K on this brand). Nothing typed. Reset not pressed. |
| In stock | Toggles the query on the same page (`?inStock=false` on the first click from the default). |
| On sale | Toggles `onSale=true` on the same page. |
| A product tile | `/product/{brand}/{id}` |

## Profile `/{handle}`

Captured: `/laurentdelrey`. `/shop` redirects to `/shop/collections`. `/ideas` is the Ideas profile.

| Control | Opens |
|---|---|
| Share | Dialog: "Share Copy link Download X". Copy link, Download, and X were not pressed. Escape closes it. |
| View avatar | No dialog on this pass. |
| Followers / Following counts | Dialog listing public profiles, each with a Follow button. Follow was not pressed. Escape closes it. |
| Follow (profile) | No navigation while signed out. |
| Profile (tab) | [https://www.cosmos.so/{handle}](https://www.cosmos.so/laurentdelrey) |
| Collections (tab) | [https://www.cosmos.so/{handle}/collections](https://www.cosmos.so/laurentdelrey/collections) |
| Explicit (on a tile) | No dialog. URL unchanged. |
| Save | No dialog while signed out. |

## Sequence `/sequence`

| Control | Opens |
|---|---|
| Subscribe | No dialog and no navigation. The button is enabled. It was clicked once and nothing opened, so it is recorded as not captured as a form. Not treated as a newsletter submit. |
| See all (This week in Sequence) | [https://www.cosmos.so/sequence/editions](https://www.cosmos.so/sequence/editions) |
| See all (Interviews) | [https://www.cosmos.so/sequence/interviews](https://www.cosmos.so/sequence/interviews) |
| See all (Aesthetic Study) | [https://www.cosmos.so/sequence/aesthetic-studies](https://www.cosmos.so/sequence/aesthetic-studies) |
| See all (Object Love) | [https://www.cosmos.so/sequence/object-love](https://www.cosmos.so/sequence/object-love) |
| An article card | [https://www.cosmos.so/sequence/{slug}](https://www.cosmos.so/sequence/earbud-leash). Example: Earbud Leash. |
| Get the app (lower on the page) | Same App Store URL as the phone Download pill. Not pressed. |
| A source link inside an article | External (press, museums, social). Not opened. Instagram, X, TikTok, and Substack links in articles were not clicked. |

Phone sequence uses the same article list. [mobile-sequence-light-default.png](screenshots/mobile-sequence-light-default.png)

## Careers `/careers`

| Control | Opens |
|---|---|
| Join us | A mailto link. Not opened. The address is not recorded here. |
| Header and footer | Same as the shell. |

No job board, no application form.

## Legal

| Page | Controls beyond the shell |
|---|---|
| [Terms](https://www.cosmos.so/legal/terms-conditions) | In-page prose. Privacy Policy link goes to `/legal/privacy-policy`. |
| [Privacy](https://www.cosmos.so/legal/privacy-policy) | In-page prose. |
| [Copyright](https://www.cosmos.so/legal/copyright-policy) | A DMCA link to copyright.gov (external, not opened). A mailto link (not opened, address not recorded). Help Center link to the help host. |

## Help `https://help.cosmos.so/en/`

Linked from the copyright page. A different host, still public. [help-light-default.png](screenshots/help-light-default.png)

| Control | Opens |
|---|---|
| Mark | [https://help.cosmos.so/en/](https://help.cosmos.so/en/) |
| Contact Support | A mailto link. Not opened. The address is not recorded here. |
| Search for articles | A search field. Nothing typed. |
| Getting Started | [https://help.cosmos.so/en/collections/19779442-getting-started](https://help.cosmos.so/en/collections/19779442-getting-started) |
| Collections & Elements | [https://help.cosmos.so/en/collections/19779445-collections-elements](https://help.cosmos.so/en/collections/19779445-collections-elements) |
| Shop | [https://help.cosmos.so/en/collections/19779446-shop](https://help.cosmos.so/en/collections/19779446-shop) |
| Account & Premium | [https://help.cosmos.so/en/collections/19779448-account-premium](https://help.cosmos.so/en/collections/19779448-account-premium) |
| Safety & Content | [https://help.cosmos.so/en/collections/19779450-safety-content](https://help.cosmos.so/en/collections/19779450-safety-content) |
| Login & Access | [https://help.cosmos.so/en/collections/19779452-login-access](https://help.cosmos.so/en/collections/19779452-login-access) |
| Legal & Policies | [https://help.cosmos.so/en/collections/19801407-legal-policies](https://help.cosmos.so/en/collections/19801407-legal-policies) |
| Launcher button (bottom right) | Not pressed. It sits on a third-party help widget. |

## Other public paths

| Path | How it was reached | What it is |
|---|---|---|
| `/public-work` | Listed in `sitemaps/marketing.xml` | A public search-like page titled Public Work by Cosmos. Same shell, Save tiles. |
| `/shop` | Footer-less cluster links and `/shop` | Redirects to `/shop/collections` (the Shop profile). |
| `/ideas` | Cluster byline | Public profile Ideas. |
| `/design`, `/style`, `/art`, `/spaces` | Cluster bylines | Public cluster or profile indexes. |
| `sitemaps/marketing.xml` | [https://www.cosmos.so/sitemap.xml](https://www.cosmos.so/sitemap.xml) | Lists `/`, `/explore`, `/explore/shop`, `/careers`, `/public-work`, `/sequence`, and the sequence section and article URLs. |
| `sitemaps/brands.xml` | Same sitemap index | Brand URLs. One brand was captured. |

## Login wall (branch stopped)

Desktop [https://www.cosmos.so/login](https://www.cosmos.so/login) asks for username or email (`emailOrUsername`) and a password. No code was sent. Nothing was typed. Next was not pressed. No Google, Apple, or other identity button is on the card. [login-light-default.png](screenshots/login-light-default.png)

| Control on the card | Where it would go | What was done |
|---|---|---|
| Show password | In-page toggle | Not pressed. |
| Next | Would submit credentials | Not pressed. |
| sign up | `/start` | Link recorded. The start page was opened separately and not submitted. |
| Forgot password? | [https://www.cosmos.so/forgot-password](https://www.cosmos.so/forgot-password) | Opened. See below. |
| Mark / Go to homepage | `/` | Link recorded. |
| Go back (on the reset page) | Previous page | Not pressed. |

[https://www.cosmos.so/forgot-password](https://www.cosmos.so/forgot-password) asks for username or email and shows Send reset link. Nothing was typed. Send reset link was not pressed. Contact support is a mailto link and was not opened. The address is not recorded here. [forgot-light-default.png](screenshots/forgot-light-default.png)

[https://www.cosmos.so/start](https://www.cosmos.so/start) asks for an email and shows Next. Nothing was typed. Next was not pressed. Terms of Service and Privacy Policy are the legal pages above. "log in" returns to the login wall.

`robots.txt` disallows `/signup`, `/settings/`, `/account/`, `/studio/`, `/api/`, and `/external/`. Those were not opened. Signed-in feed, boards, clusters, and settings stay behind the login card.
