# Disney+ public site tree

Mapped on 2026-11-22 from [https://www.disneyplus.com/](https://www.disneyplus.com/), signed out. The homepage redirected to [https://www.disneyplus.com/en-sg](https://www.disneyplus.com/en-sg). No email, name, password, code, phone, or address was typed. No identity provider was clicked. No form was submitted. No captcha was solved. No subscription was started.

The public marketing site loaded. Title: Disney, Marvel, Pixar, Star Wars, Nat Geo and Hulu | Disney+ Singapore. Page background `rgb(4, 7, 20)`.

## Homepage controls

The header is a logo and one control. There is no product menu.

| Control | Opens |
|---|---|
| Logo | Painted in the hero. It is an image, not a link, on the Singapore homepage. |
| LOG IN | https://www.disneyplus.com/identity/login which landed on https://www.disneyplus.com/identity/login/enter-email. Login wall. Branch stopped. |
| DISNEY+ ANNUAL | https://www.disneyplus.com/commerce/plans?isLicensePlateUser=false&billingCadence=ANNUAL. Subscribe wall. Not followed past the plan chooser. |
| DISNEY+ MONTHLY | https://www.disneyplus.com/commerce/plans. Subscribe wall. Branch stopped. |
| View plan details | Same-page anchor `#apac-plan-comp`. |
| LEARN MORE (perks strip) | Same-page anchor `#apac-btf-perks`. |
| SIGN UP NOW | https://www.disneyplus.com/commerce/plans. Same subscribe wall. Not clicked. |
| Plan prices on the comparison | https://www.disneyplus.com/commerce/billing. Checkout. Not opened. |

## Footer

| Control | Opens |
|---|---|
| Subscriber Agreement | https://www.disneyplus.com/legal/subscriber-agreement landed on https://www.disneyplus.com/en-sg/legal/subscriber-agreement |
| Privacy Policy | https://www.disneyplus.com/en-sg/legal/privacy-policy |
| Supplemental Privacy Policy for Singapore | https://www.disneyplus.com/en-gb/legal/supplemental-privacy-policy-for-singapore. Listed. Not photographed as its own page. |
| Interest-Based Ads | https://privacy.thewaltdisneycompany.com/en/privacy-controls/online-tracking-and-advertising/. Leaves the product host. Not photographed. |
| Help Centre | https://help.disneyplus.com/ |
| Supported Devices | https://help.disneyplus.com/article/disneyplus-devices-supported/ |
| About Us | https://help.disneyplus.com/article/disneyplus-introduction |
| Explore Disney+ | https://www.disneyplus.com/en-sg/explore |
| Disney | https://www.disneyplus.com/en-sg/browse/page-4c4b78ed-4a17-43eb-8221-14a3959e4517 |
| Pixar | https://www.disneyplus.com/en-sg/browse/page-9143212f-5696-4ee3-a37a-f2fbcd14749a |
| Marvel | https://www.disneyplus.com/en-sg/browse/page-60f4707d-19bb-4c0c-9390-ab269137be50 |
| Star Wars | https://www.disneyplus.com/en-sg/browse/page-b4e74f38-aa35-4b12-965c-93f4a931f78a |
| National Geographic | https://www.disneyplus.com/en-sg/browse/page-a577ee5e-2f37-443f-bc13-594a20520492 |
| Hulu | https://www.disneyplus.com/en-sg/browse/hulu redirected to a Hulu browse page |
| All Collections | https://www.disneyplus.com/en-sg/browse/page-bceb41c9-cfa9-41e3-b6d7-d547362ea1cd |
| Bingeable Series, Action and Adventure, Asian Spotlight, Comedies, Drama, Horror, Shorts | Genre browse pages on disneyplus.com. Listed in the footer. Not photographed as separate pages. |
| X, Facebook, Instagram, TikTok, YouTube | Social accounts for Disney+ Singapore. Left the site. Not photographed. |

The homepage body also links title pages and more genre collections. Those are catalog rows, not header or footer controls. They were not photographed one by one.

Explore Disney+ has its own header: What to Watch, Explore More, How to Subscribe, Sign Up, About Explore Disney+. Sign Up points at the same subscribe wall and was not followed.

## Pages photographed

| Page | URL | Width |
|---|---|---|
| Home | https://www.disneyplus.com/en-sg | 1440 and 390 |
| Explore | https://www.disneyplus.com/en-sg/explore | 1440 |
| Subscriber agreement | https://www.disneyplus.com/en-sg/legal/subscriber-agreement | 1440 |
| Privacy policy | https://www.disneyplus.com/en-sg/legal/privacy-policy | 1440 |
| Help Centre | https://help.disneyplus.com/en-GB/ | 1440 |
| About Us | https://help.disneyplus.com/en-GB/article/disneyplus-introduction | 1440 |
| Supported devices | https://help.disneyplus.com/en-GB/article/disneyplus-devices-supported | 1440 |
| Disney | Disney browse page above | 1440 |
| Pixar | Pixar browse page above | 1440 |
| Marvel | Marvel browse page above | 1440 |
| Star Wars | Star Wars browse page above | 1440 |
| National Geographic | National Geographic browse page above | 1440 |
| Hulu | Hulu browse page | 1440 |
| All Collections | All Collections browse page | 1440 |
| Login wall | https://www.disneyplus.com/identity/login/enter-email | 1440 and 390 |
| Subscribe wall | https://www.disneyplus.com/en-gb/commerce/plans | 1440 |

Desktop viewport measured 1440 by 900, `devicePixelRatio` 1 in Playwright. The preview browser that opened the login and plan walls reported `devicePixelRatio` 2 at the same CSS size. Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2. The phone home shot measured `innerWidth` 390.

## Stopped branches

Login and the plan chooser are recorded in [login-review.json](login-review.json). The login wall asks for an email and shows Continue. The field was empty. Continue was not clicked. No password field appeared. No MyDisney, Google, Apple, or Facebook button was clicked. The plan chooser shows Disney+ Premium and Disney+ Standard with SELECT PLAN. Those buttons were not clicked. Billing, checkout, and subscribe forms were not opened. The Help Centre search field was photographed empty and was not submitted. The Help Centre Sign up and Log in controls were not followed past the walls already recorded.
