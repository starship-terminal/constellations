# Hulu public site tree

Mapped on 2026-11-22 from [https://www.hulu.com](https://www.hulu.com), signed out, from Singapore. No email, name, password, code, phone, or address was typed. No identity provider was clicked. No form was submitted. No captcha was solved. No subscription was started.

`https://www.hulu.com/` and `https://www.hulu.com/welcome` returned HTTP 302 to `https://www.disneyplus.com/` (`x-aka-user-geo: SG`). The same redirect hit `/guides`, `/subscriber_agreement`, `/your-us-state-privacy-rights`, `/live-tv`, `/about`, `/originals`, and the other www paths that were requested. Those redirects were not photographed as Hulu pages. The Disney+ page they land on is already in [systems/disneyplus](../disneyplus/site-tree.md).

The pages that stayed on a Hulu host are the plan chooser, the login wall, the Help Center, and the press site.

## Plan chooser

Opened from [https://signup.hulu.com/plans](https://signup.hulu.com/plans). It landed on [https://secure.hulu.com/commerce/plans?hitsFlowName=suf_web_default](https://secure.hulu.com/commerce/plans?hitsFlowName=suf_web_default). Title: Hulu. Heading: Choose Your Plan. Page background `rgb(247, 247, 249)`.

The header is the Hulu wordmark and LOG IN. There is no product menu.

| Control | Opens |
|---|---|
| Wordmark | https://www.hulu.com/welcome. From this region that 302s to Disney+. Not followed again. |
| LOG IN | https://secure.hulu.com/login, which landed on https://auth.hulu.com/web/login/enter-email. Login wall. Branch stopped. |
| Bundle/Save | Same page. Shows bundle cards. Photographed. |
| Base Plans | Same page. Shows Hulu and Hulu Premium. Photographed. SELECT was not clicked. |
| Details | Same-page disclosure. Not opened into a new page. |
| SELECT | Subscribe wall. Not clicked. |
| Terms apply | Same-page disclosure. Not opened. |
| Learn about our plans and pricing in our Help Center | Help article. The Help Center article that was opened is Plans and pricing. |

## Footer on the plan chooser and the login wall

| Control | Opens |
|---|---|
| Privacy Policy | https://privacy.thewaltdisneycompany.com/en/current-privacy-policy/. Leaves the product host. Not photographed. |
| Children's Online Privacy Policy | https://privacy.thewaltdisneycompany.com/en/for-parents/childrens-online-privacy-policy/. Leaves the product host. Not photographed. |
| Subscriber Agreement | https://www.hulu.com/subscriber_agreement. From this region that 302s to Disney+. Not photographed as a Hulu page. |
| Your US State Privacy Rights | https://www.hulu.com/your-us-state-privacy-rights. Same geo redirect. Not photographed as a Hulu page. |
| Terms of Use | https://disneytermsofuse.com/. Leaves the product host. Not photographed. |
| Your Privacy Choices | Same-page preference control. Not submitted. |
| Help | https://help.hulu.com/ |
| Interest-Based Ads | https://privacy.thewaltdisneycompany.com/en/privacy-controls/online-tracking-and-advertising/. Leaves the product host. Not photographed. |

## Help Center

[https://help.hulu.com/](https://help.hulu.com/). Title: Hulu Help Center.

| Control | Opens |
|---|---|
| Sign up | Same signup path as the plan chooser. Not followed a second time. |
| Log in | Same login wall. Not followed a second time. |
| Search | Empty field, placeholder "Enter a question or topic". Not submitted. |
| Plans and pricing | https://help.hulu.com/article/hulu-how-much-does-hulu-cost |
| Login issues, Update payment, Live TV Home network, Manage activated devices, Watch Live Sports on Hulu | Help articles. Listed. Not each photographed. |
| Getting Started, Account & Billing, Plans & Add-ons, Fix a Problem, Using Hulu, TV, Channels & Movies | Topic cards. Listed. Not each photographed. |
| Get in Touch | Live support. Not opened. |

## Press site

[https://press.hulu.com/](https://press.hulu.com/). Title: Hulu Press. This is the public press room, not the streaming app.

| Control | Opens |
|---|---|
| NEWS | https://press.hulu.com/news/ |
| GUIDES | https://www.hulu.com/guides. Geo redirect to Disney+. Not photographed as a Hulu page. |
| SCHEDULE | https://press.hulu.com/schedule/ |
| ORIGINALS | https://press.hulu.com/originals/ |
| FX | https://press.hulu.com/fx/. Points at https://www.fxnetworkspressroom.com/. The FX press room was not opened. |
| ASSETS, Branding | https://press.hulu.com/branding/. It links to thisishulu.com for brand files. That site was not opened. |
| ABOUT, Corporate | https://press.hulu.com/corporate/ |
| Sign In | https://press.hulu.com/login/?redirect_to=https%3A%2F%2Fpress.hulu.com%2F&site_id=34. Empty username and password. Stopped. |
| Sign Up | https://www.detpress.com/members/register/?site_id=34. Press registration wall. Stopped. No form was filled. |
| About, Careers, Help, Advertising, About Ads, Terms of Use, Your California Privacy Rights | Footer links. Terms of Use on the press host was photographed. Careers (careers.hulu.com) and Advertising (advertising.hulu.com) did not resolve. Not photographed. |

Show pages and individual press releases are catalog rows under Latest Releases. They were not photographed one by one.

## Pages photographed

| Page | URL | Width |
|---|---|---|
| Plan chooser, bundles | https://secure.hulu.com/commerce/plans | 1440 and 390 |
| Plan chooser, base plans | same URL, Base Plans tab | 1440 |
| Login wall | https://auth.hulu.com/web/login/enter-email | 1440 and 390 |
| Help Center | https://help.hulu.com/ | 1440 and 390 |
| Help, plans and prices | https://help.hulu.com/article/hulu-how-much-does-hulu-cost | 1440 |
| Press home | https://press.hulu.com/ | 1440 and 390 |
| Press news | https://press.hulu.com/news/ | 1440 |
| Press originals | https://press.hulu.com/originals/ | 1440 |
| Press schedule | https://press.hulu.com/schedule/ | 1440 |
| Press about | https://press.hulu.com/corporate/ | 1440 |
| Press branding | https://press.hulu.com/branding/ | 1440 |
| Press FX | https://press.hulu.com/fx/ | 1440 |
| Press terms | https://press.hulu.com/terms-of-use/ | 1440 |
| Press login wall | https://press.hulu.com/login/ | 1440 |
| Press signup wall | https://www.detpress.com/members/register/?site_id=34 | 1440 |

Desktop viewport was 1440 by 900, `deviceScaleFactor` 1. Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2.

## Stopped branches

Login, plan SELECT, and press registration are recorded in [login-review.json](login-review.json). The consumer login wall asks for an email and shows Continue. The field was empty. Continue was not clicked. No password field appeared. No MyDisney, Google, Apple, or Facebook button was clicked. SELECT on a plan was not clicked. No card or address was typed. The press login fields were empty and Log In was not clicked. The press registration form was not filled.
