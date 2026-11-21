# Blue Apron public site tree

Mapped from https://blog.blueapron.com/ on 2026-11-21 in the T3 preview browser, signed out, before screenshots. The official product host is https://www.blueapron.com. That host returned Cloudflare "Sorry, you have been blocked" on the homepage in both the default and incognito preview profiles, and the same 403 from curl. The public surface that loaded is the Squarespace blog, Extra Helpings, at https://blog.blueapron.com/.

No email, password, phone, code, or location was typed. No form was submitted. No identity provider was clicked. No checkout was started.

Widths planned for every reachable public state: desktop 1440×900 and phone 390×844. One theme: light. No dark toggle on the blog.

The cookie banner is disabled sitewide. The announcement bar is visible chrome, not a consent dialog. It is not dismissed for the default shots.

## Shop host (blocked)

https://www.blueapron.com/

| Control | Opens |
|---|---|
| Homepage load | Cloudflare block page, title "Attention Required! \| Cloudflare", heading "Sorry, you have been blocked". Stop. No product UI. |

Header and footer links that leave the blog for this host are recorded below and not followed into the wall.

## Header (every blog page)

https://blog.blueapron.com/

| Control | Opens |
|---|---|
| Announcement bar "Get $25 off your first 2 orders + Free Shipping with code WELCOME25" | same page; the code is public promo copy |
| Terms Apply | https://www.blueapron.com/pages/terms/promo (shop host; blocked) |
| Close Announcement | hides the announcement bar on the same page |
| Skip to Content | https://blog.blueapron.com/#page |
| Wordmark | https://blog.blueapron.com/ |
| Blog | https://blog.blueapron.com/ |
| Blue Apron+ | https://blueapron.com/membership (shop host; blocked) |
| Subscribe & Save | https://www.blueapron.com/subscribe-and-save (shop host; blocked) |
| Shop Now | https://www.blueapron.com/menu (shop host; blocked) |
| Cart icon, "0 items in cart" | https://blog.blueapron.com/cart (empty public cart) |
| Search field, placeholder Search | local field on the same page. Typed sample text is deleted. Not submitted. |
| Open Menu (phone width; desktop button is hidden) | opens the header menu overlay on the same page. Close Menu closes it. |

## Home

https://blog.blueapron.com/

| Control | Opens |
|---|---|
| Learn more | https://blog.blueapron.com/guides/meet-the-new-blue-apron |
| Category tiles (Blue Apron+, Subscribe & Save, Shop Now images) | the same shop-host URLs as the header. Not followed. |
| Article card image, title, or Read More | that guide, for example https://blog.blueapron.com/guides/meal-delivery-for-two-people-how-to-choose |
| Category chip (How-To, FAQ, Recipes, From the Kitchen, About, Customer Favorite, Ingredients, New Blue Apron) | https://blog.blueapron.com/guides/category/{name} |
| Older Posts | https://blog.blueapron.com/?offset=1754668225787 (next page of the same list) |
| Pause Background / Play Background | pauses or plays a background video on the same page. No dialog. |

## Guide article

Example: https://blog.blueapron.com/guides/15-budget-friendly-quick-dinner-ideas-for-busy-weeknights

| Control | Opens |
|---|---|
| Comments header, when mounted | toggles the comments list on the same page. Not a post. |
| Body links and pager | another public guide, or a shop-host URL that is not followed |

## Category list

Example: https://blog.blueapron.com/guides/category/Recipes

| Control | Opens |
|---|---|
| A card | that guide |
| Pagination | the next offset of the same category |

## FAQ guide

https://blog.blueapron.com/guides/membership-autoship-faq

A long public article. No accordion dialog. In-page links that leave for the shop host are not followed.

## Cart

https://blog.blueapron.com/cart

Empty public cart. Checkout is not started.

## Footer

Present on every blog page. Logo links to https://www.blueapron.com/ (blocked).

| Column | Control | Opens |
|---|---|---|
| Blue Apron | Menu | https://www.blueapron.com/menu (blocked) |
| Blue Apron | Blue Apron+ | https://www.blueapron.com/membership (blocked) |
| Blue Apron | Autoship & Save | https://www.blueapron.com/autoship (blocked) |
| Blue Apron | About Us | https://www.blueapron.com/pages/vision (blocked) |
| Blue Apron | Gift Cards | https://www.blueapron.com/gifts (blocked) |
| Blue Apron | Recipes | https://www.blueapron.com/cookbook (blocked) |
| Blue Apron | Careers | https://wonder.wd1.myworkdayjobs.com/WG (other host; not captured) |
| Blue Apron | Affiliates | https://public.cj.com/signup/publisher (other host; signup wall; not opened) |
| Support | Help Center & FAQ | https://blueapronsupport.zendesk.com/hc/en-us (other host; not captured) |
| Support | Supply Chains Act | https://www.blueapron.com/pages/supply-chain-disclosure (blocked) |
| Support | Terms & Conditions | https://www.blueapron.com/pages/terms (blocked) |
| Support | Privacy Policy | https://www.blueapron.com/pages/privacy (blocked) |
| Support | Do Not Sell or Share My Info | https://www.blueapron.com/pages/privacy#ccpa (blocked) |
| Support | Notice to California Residents | https://www.blueapron.com/pages/privacy#california (blocked) |
| Social | Instagram, Facebook, TikTok | those public profiles (other hosts; not captured) |

## Not on this surface

No sign-in, sign-up, or identity-provider control is mounted on the blog. Account, settings, and create live on www.blueapron.com, which this client cannot load. No dark theme toggle. No cookie consent dialog.
