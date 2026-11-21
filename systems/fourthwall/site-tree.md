# Fourthwall public site tree

Captured 2026-11-21 from [https://fourthwall.com/](https://fourthwall.com/), signed out. `signed_in` is false. Desktop shots are 1440x900. Phone shots are 390x844. Cookie banners were hidden and never accepted. No email, password, code, or SSO control was used.

The sitemap at [https://fourthwall.com/sitemap.xml](https://fourthwall.com/sitemap.xml) listed 1,566 URLs. Unique marketing, feature, legal, and audience pages were opened. Generated templates (`/make-your-own/*` 783, `/blog/*` 482, `/design-and-sell/*` 87, `/compare/*` 63, `/apps/*` 28, `/creator-examples/*` 28, `/seasons/*` 9, `/categoryx/*` 7) were sampled at the first, middle, and last URL. The signed-in app was not captured.

## Header (desktop)

The bar is `nav.nav-bar`. Wordmark links to `/`.

| Control | Opens |
|---|---|
| Wordmark | `/` |
| Features (hover) | Mega menu, below. The trigger href is `#features`. |
| Product catalog | [https://products.fourthwall.com/](https://products.fourthwall.com/) |
| Pricing | `/pricing` |
| Learn (hover) | Mega menu, below. The trigger href is `#learn`. |
| Log in | `https://my-shop.fourthwall.com/admin/dashboard?redirect`, which redirects to the Keycloak wall at `auth.fourthwall.com`. Branch stopped. See [login-review.json](login-review.json). |
| Start now | `/get-started`, which redirects to the Keycloak registration wall. Branch stopped. |

### Features menu

Shot: [screenshots/home-menu-features.png](screenshots/home-menu-features.png).

| Label | Opens |
|---|---|
| Product catalog | [https://products.fourthwall.com/](https://products.fourthwall.com/) |
| Product designer | `/design-and-sell` |
| Source custom products | `/bespoke` |
| Digital products | `/features/digital-products` |
| Curated artists | `/designers` |
| Shop builder | `/shops` |
| Themes | `/features/custom-themes` |
| Fulfillment & shipping | `/print-on-demand` |
| Sales channels | `/features` |
| Discounts | `/features/promo-codes` |
| Homepages | `/websites` |
| Memberships | `/memberships` |
| Apps & integrations | `/features` |
| Launch your mobile app | `/features/custom-mobile-apps` |
| Introducing Eli (What's new card) | `/ai-assistant-eli` |
| Build your own app | [https://docs.fourthwall.com/](https://docs.fourthwall.com/) |
| Fourthwall MCP | [https://docs.fourthwall.com/ai/mcp](https://docs.fourthwall.com/ai/mcp) |

### Learn menu

| Label | Opens |
|---|---|
| Get inspired | `/get-inspired` |
| Designers | `/designers` |
| Help center | [https://help.fourthwall.com/](https://help.fourthwall.com/) |
| Blog | `/blog` |
| Join our Discord community | [https://discord.com/invite/t5Vm6Q2425](https://discord.com/invite/t5Vm6Q2425) |
| App Store badge | [https://apps.apple.com/us/app/fourthwall-for-creators/id1479668990](https://apps.apple.com/us/app/fourthwall-for-creators/id1479668990) |
| Google Play badge | [https://play.google.com/store/apps/details?id=com.fourthwall.android](https://play.google.com/store/apps/details?id=com.fourthwall.android) |

## Header (phone)

The burger (`.nav-burger`, aria "Open menu") opens a full-screen ink menu. Shot: [screenshots/mobile-home-menu.png](screenshots/mobile-home-menu.png). Close is the X.

| Control | Opens |
|---|---|
| Features | Accordion. Shot: [screenshots/mobile-home-menu-features.png](screenshots/mobile-home-menu-features.png). Same destinations as the desktop Features menu. |
| Product catalog | [https://products.fourthwall.com/](https://products.fourthwall.com/) |
| Pricing | `/pricing` |
| Learn | Accordion. Same destinations as the desktop Learn menu, including Discord and the two app badges. |
| Log in | Same Keycloak wall. Phone shot: [screenshots/auth-login-mobile.png](screenshots/auth-login-mobile.png). |
| Start now | Same registration wall. |

## Search

`/search` is a page, not a dialog. Empty query shows "No matching results." The field was not filled and Search was not submitted. Shot: [screenshots/home-search.png](screenshots/home-search.png).

## Home page controls

| Control | Opens |
|---|---|
| Start now (hero, repeated) | `/get-started` (auth wall) |
| Browse all | [https://products.fourthwall.com/](https://products.fourthwall.com/) |
| Product cards (Comfort Colors tee, LA Apparel crop, Cotton Heritage hoodie, Yupoong hat, Black Glossy Mug, Kiss Cut Sticker Sheet) | `products.fourthwall.com/<slug>` |
| Color swatches on the product rail | In-page color change. Does not navigate. |
| Previous / Next | In-page carousel. |
| Scroll filters left / right | In-page filter rail. |
| FAQ questions (cost, payments, taxes, design support, profit, shipping, AI, support, domain) | In-page accordion. |
| Chat bubble | Third-party chat widget. Not opened past the bubble. No message was sent. |

## Footer

| Column | Links |
|---|---|
| Product | Product catalog (`products.fourthwall.com`), Shops (`/shops`), Homepages (`/websites`), Memberships (`/memberships`), Pricing (`/pricing`), Features (`/features`) |
| Learn | Get inspired (`/get-inspired`), Designers (`/designers`), Blog (`/blog`), Careers (`jobs.fourthwall.com`), Help center (`help.fourthwall.com`), Contact (`/contact`), System status (`status.fourthwall.com`), FAQs (`/faq`), Security (`trust.fourthwall.com`) |
| Compare | Shopify, Spring, Redbubble, Streamlabs, Patreon (`/compare/fourthwall-vs-*`), Compare all (`/compare`) |
| Social | Instagram, X, Discord, YouTube, TikTok |
| Apps | App Store, Google Play |
| Legal | Privacy Policy (`/legal/privacy-policy`), Terms of Service (`/legal/terms-of-service`), Acceptable Use Policy (`/legal/acceptable-use-policy`), Your Privacy Choices (`/privacy-choices`), AI transparency (`/ai-transparency`) |

## Pages opened

Each row was requested at 1440 and 390 unless noted. Shots live in [screenshots/](screenshots/) as `{slug}-default.png` and `mobile-{slug}-default.png`.

| Path | Title seen | Note |
|---|---|---|
| `/` | One platform for custom products and branded shops | Home |
| `/pricing` | Plans & pricing | |
| `/features` | Features | |
| `/features/digital-products` | Digital Products | |
| `/features/custom-themes` | Custom Themes | |
| `/features/custom-mobile-apps` | Custom Mobile Apps | |
| `/features/promo-codes` | Promo Codes | |
| `/features/payment-methods` | Payment Methods | |
| `/features/donations` | Donations | |
| `/features/direct-messages` | Direct Messages | Desktop shot timed out once. Phone shot landed. |
| `/features/sell-your-own-products` | Sell your own products | |
| `/features/video-memberships` | Video Memberships | |
| `/features/apps-and-integrations/*` | Partner pages (beehiiv, Klaviyo, Spotify, TikTok Shop, and the rest of the 16 sitemap URLs) | Integration template. Desktop shots of stream-alerts and twitch-gifting timed out. Phone shots landed. |
| `/shops` | Create an Online Store | |
| `/websites` | Website Builder | |
| `/memberships` | Memberships | |
| `/design-and-sell` | Design & Sell Your Own Products | |
| `/design-and-sell/custom-mugs` | Custom Mugs | Category template sample |
| `/design-and-sell/custom-yoga-pants` | Custom Yoga Pants | Category template sample |
| `/bespoke` | Source & Sell Bespoke Products | |
| `/bespoke/mixam` | Create Custom Printed Products | |
| `/print-on-demand` | Print On Demand | |
| `/designers` | Hire a designer | |
| `/ai-assistant-eli` | AI Assistant Eli | |
| `/ai-transparency` | AI Transparency | |
| `/ai-assistant-eli-transparency-old` | Transparency | Older page, still public |
| `/get-inspired` | Get inspired | |
| `/blog` | Blog | |
| `/blog/how-to-make-money-as-a-designer-10-proven-strategies` | How to Make Money as a Designer | Post template sample |
| `/blog/zazzle-alternatives` | Zazzle Alternatives | Post template sample |
| `/faq` | Frequently asked questions | |
| `/contact` | Contact us | Form photographed empty. Not submitted. |
| `/contact-sales` | Talk to Sales | Form photographed empty. Not submitted. |
| `/contact-support` | Contact support | |
| `/compare` | Compare Fourthwall | |
| `/compare/fourthwall-vs-patreon` | Fourthwall vs Patreon | Comparison template sample |
| `/compare/merchology` | Fourthwall vs Merchology | Comparison template sample |
| `/search` | Search results | Empty. Not submitted. |
| `/glossary` | Glossary | |
| `/style-guide` | Style Guide 2026 | Public brand page, not this package's guide |
| `/privacy-choices` | Your Privacy Choices | |
| `/legal/privacy-policy` | Privacy Policy | |
| `/legal/terms-of-service` | Terms of Service | |
| `/legal/acceptable-use-policy` | Acceptable Use Policy | |
| `/legal/merchandise-privacy-policy` | Merchandise Privacy Policy | |
| `/legal/merchandise-terms-of-service` | Merchandise Terms of Service | |
| `/legal/creator-dpa` | Data Processing Agreement | |
| `/legal/responsible-disclosure-policy` | Responsible Disclosure Policy | |
| `/legal/annex-technical-organisational-measures` | Annex II | |
| `/make-your-own` | Make Your Own Custom Products | Index of 783 generated landings |
| `/creator-examples/all-examples` | Get Inspired | Category index |
| `/creator-examples/hobby` | Get Inspired | Category template |
| `/creator-examples/zodiac-astrology` | Get Inspired | Category template |
| `/seasons/autumn` | Autumn | |
| `/seasons/summer` | Summer | |
| `/seasons/holidays-apparel` | Apparel | |
| `/categoryx/business-branding` | Blog | Blog category |
| `/categoryx/marketing-audience-growth` | Blog | Blog category |
| `/categoryx/tools-platforms` | Blog | Blog category |
| `/artists` | For Artists | |
| `/creators` | Creators | |
| `/companies` | Custom Products for Companies | |
| `/comedians` | Comedians | |
| `/musicians` | Musicians | |
| `/podcasts` | Podcasts | |
| `/podcasts-rss` | RSS.com x Fourthwall | |
| `/youtubers` | YouTube | |
| `/youtube` | YouTube | |
| `/twitch` | Twitch | |
| `/twitch-merch` | Twitch Merch | |
| `/tiktok` | TikTok | |
| `/spotify` | Spotify | |
| `/asmr-creators` | ASMR Creators | |
| `/non-profits` | Non-Profits | |
| `/vidcon` | VidCon | |
| `/what-is-fourthwall` | What is Fourthwall? | |
| `/reviews` | Reviews | |
| `/affiliate-plus-program` | Affiliate Plus Program | |
| `/referral-program` | Referral Program | |
| `/launch-your-own-brand` | Launch your own brand | |
| `/merch-made-easy` | Merch Made Easy | |
| `/merch-maker` | Merch Maker | |
| `/signature` | Fourthwall Signature | |
| `/apps/beehiiv`, `/apps/packiyo`, `/apps/zapier` | Page not found | Sitemap lists 28 `/apps/*` URLs. The three sampled returned 404. |

## Stopped branches

| URL | Why |
|---|---|
| Log in, and `https://my-shop.fourthwall.com/admin/dashboard?redirect` | Keycloak login at `auth.fourthwall.com`. Empty email and password fields, plus Google and Apple. Photographed. Not filled. Not submitted. |
| `/get-started` and every Start now | Keycloak registration. Google, Apple, or email. Photographed. Email step not opened. |
| `https://fourthwall.com/login` | Download started. Page did not paint. |
| `/admin/products/*` | Storefront product pages on `products.fourthwall.com`. Public product pages, not the admin app. Not a login wall. Sampled, not enumerated (the homepage alone links dozens). |
| Signed-in dashboard, onboarding, checkout, newsletter, plan, survey | Not entered. |

## Off-site, not walked

`docs.fourthwall.com`, `help.fourthwall.com`, `jobs.fourthwall.com`, `status.fourthwall.com`, `trust.fourthwall.com`, Discord, Instagram, X, YouTube, TikTok, App Store, Google Play, and creator shop domains linked as examples (for example `mkbhd.com`, `sandiskmerch.com`).
