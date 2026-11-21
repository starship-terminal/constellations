# Stocksy public site tree

Mapped on 2026-11-22 from the public homepage, https://www.stocksy.com/. Title: "Artist-Owned Stock Images, Videos & Illustrations | Stocksy". Headed Chrome via Playwright. Desktop shots are 2880 by 1800 pixels, from a 1440 by 900 CSS viewport at devicePixelRatio 2. The phone shot is 780 by 1688 pixels, from a 390 by 844 CSS viewport at devicePixelRatio 2. The homepage paints a black hero with a green search button.

The site is a live marketing and browse site, not a parked domain and not a captcha wall. The T3 preview tools were not registered in this session. `search_tool` stayed partial, and `t3-code__preview_status` returned `Tool not found: t3-code__preview_status`. No email, password, name, phone, code, or address was typed. No form was submitted. No identity provider was clicked. No captcha was solved. No image was licensed. No checkout was started. `login-extracted` stays not-started. catalog.json was left alone. webapps-manifest.json was left alone.

The existing package in this folder (tokens, icons, and the 2026-11-19 readings) was not overwritten. This pass adds the site tree and the screenshots the earlier pass could not save.

## Header, desktop (1440)

On the hero, the wordmark sits left and the controls sit right. After scroll, a search field joins the bar. Photographed on [home-light-desktop.png](screenshots/home-light-desktop.png).

| Control | Destination |
|---|---|
| Wordmark | https://www.stocksy.com/ |
| Insights & Trends | flyout. The panel did not paint. A toast said "There was a problem loading insights and trends. Please try again." A Cloudflare Turnstile appeared and was not solved. Footer column of the same name is mapped below. |
| Pricing | /pricing |
| For Business | /business |
| For Artists | /cta/welcome. That URL stopped on a Cloudflare "Verify you are human" page. Not solved. Footer "Artist Application" uses the same path. |
| Cart | empty popover. Tooltip reads "Cart". Checkout was not opened. |
| Log In | /user/login |
| Menu | button, aria-label "Open Navigation Menu". On desktop it showed a "Menu" tooltip and did not open a panel. |

## Header, phone (390)

The wordmark, a cart icon, Log In, and a menu icon. The menu was not expanded. Photographed in [home-light-phone.png](screenshots/home-light-phone.png).

## Homepage

`/` returned the marketing page. Heading: "100% Artist-Owned, 100% Human-Made Stock Images, Videos and Illustrations". The search field placeholder is "Search all" and its value length was 0. Search was not submitted. Search By Image was not opened.

| Control | Opens |
|---|---|
| Hero credit, Trevor Wentt | /photo/7746947/young-man-lays-in-bed-binge-watching-shows-on-his-laptop |
| View Pricing | /pricing |
| Featured categories | /category/healthcare, /category/business, /category/ugc, /category/technology, /category/fitness-and-sports, /category/lifestyle |
| Featured artists | artist profile paths such as /sashadove. Follow was not clicked. |
| Apply Now | /cta/welcome. Stop at the captcha wall. |
| Asset tiles | public photo, video, and illustration pages. One photo page was opened. |

## Footer

Photographed on the homepage in [footer-light-desktop.png](screenshots/footer-light-desktop.png). Columns: Services, Insights & Trends, Our Cooperative, Support, Collections, Legal, Language. Social icons leave the site and were not opened. Cookie Preferences was not opened. Language switches were not clicked. The phone number and support email were not used.

| Column | Destinations |
|---|---|
| Services | /pricing, /business, /cta/welcome, https://share.stocksy.com/curation-services |
| Insights & Trends | /resources, /ideas, https://share.stocksy.com/newsletter |
| Our Cooperative | /service/about/, /service/hiring |
| Support | /service/support#support, /service/support, https://support.stocksy.com/hc/en-us, https://developers.stocksy.com/ |
| Collections | /photo, /video, /illustration |
| Legal | /legal/terms, /legal/privacy, Cookie Preferences (not opened) |
| Language | /user/languageselect?code=en, /user/languageselect?code=es. Not opened. |
| Social | Pinterest, Instagram, LinkedIn, YouTube, identity.coop. Off-site. Not opened. |

## Pages opened from header or footer

| Path | Result |
|---|---|
| /pricing | Public. "Simple pricing for standout visuals". Standard License prices are on the page. No license was bought. [pricing-light-desktop.png](screenshots/pricing-light-desktop.png) |
| /business | Public marketing page. "Business solutions for using Stocksy at scale". The request form (name, email, phone, company) was empty and was not filled. [business-light-desktop.png](screenshots/business-light-desktop.png) |
| /service/about/ | Public. "About Us". [about-light-desktop.png](screenshots/about-light-desktop.png) |
| /service/hiring | Public. "Come work with us". [careers-light-desktop.png](screenshots/careers-light-desktop.png) |
| /resources | Public. "Resources". [resources-light-desktop.png](screenshots/resources-light-desktop.png) |
| /ideas/ | Public editorial index. Stocksy Ideas, with its own header (Home, Categories, Stocksy.com, Search). One featured story is on screen. The story was not opened. [ideas-light-desktop.png](screenshots/ideas-light-desktop.png) |
| /service/support | Public. "Contact Support". Name and email fields were empty and were not filled. [support-light-desktop.png](screenshots/support-light-desktop.png) |
| /photo | Public collection. "Premium Stock Photos". [photos-light-desktop.png](screenshots/photos-light-desktop.png) |
| /category/healthcare | Public collection. "Healthcare Stock Images". [category-light-desktop.png](screenshots/category-light-desktop.png) |
| /photo/7746947/... | Public asset page. "Young Man Lays In Bed Binge-Watching Shows On His Laptop". License and cart were not used. [asset-light-desktop.png](screenshots/asset-light-desktop.png) |
| /legal/terms | Public. "Terms and Conditions". [terms-light-desktop.png](screenshots/terms-light-desktop.png) |
| /legal/privacy | Public. "Privacy Policy". [privacy-light-desktop.png](screenshots/privacy-light-desktop.png) |
| /cta/welcome | Cloudflare "Performing security verification" / "Verify you are human". Not solved. Not photographed. |
| https://share.stocksy.com/newsletter | Not opened. Subscribe wall. |
| https://share.stocksy.com/curation-services | Off the main host. Not opened. |
| https://support.stocksy.com/hc/en-us | Off the main host. Not opened. |
| https://developers.stocksy.com/ | Off the main host. Not opened. |

Videos and Illustrations use the same collection template as Photos. They were mapped and not photographed a second time. The other featured categories use the same template as Healthcare.

## Login wall

Log In opens https://www.stocksy.com/user/login. Title: "Sign in | Stocksy". Heading: "Log in to your account". The email field value length was 0. The password field value length was 0. Log in was not clicked. Forgot password was not clicked. Continue With Google and Continue With Facebook were not clicked. A Turnstile checkbox was visible and was not solved. Photographed empty in [login-light-desktop.png](screenshots/login-light-desktop.png). The URL has no OAuth or session query.

## Signup wall

Sign up is a panel on the same URL, https://www.stocksy.com/user/login. Heading: "Create an account". The email field placeholder is "Enter an email address" and its value length was 0. CONTINUE was not clicked. Continue With Google and Continue With Facebook were not clicked. The Turnstile checkbox was not solved. Photographed empty in [signup-light-empty.png](screenshots/signup-light-empty.png).

/user/register, /user/join, /user/create, and /signup returned the product's own 404. Those are not the signup wall.
