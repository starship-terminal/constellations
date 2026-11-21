# FlutterFlow public site tree

Captured 2026-11-21 from [https://www.flutterflow.io/](https://www.flutterflow.io/) in headless Chromium. Desktop is 1440×900. Phone is 390×844. Signed out. No form was submitted. No OAuth button was clicked. Cookie banners, when present, were hidden and not accepted.

The walk stopped at the auth wall. Header Sign in and Start building both go to `https://build.flutterflow.io/signin`. Studio Open goes to `https://app.flutterflow.io/`, which redirects to the login canvas. Those walls are recorded in [login-review.json](login-review.json). The signed-in app was not captured.

Sitemap at `https://www.flutterflow.io/sitemap.xml` lists 209 URLs on `www.flutterflow.io` (111 blog posts, 22 customer stories, 18 showcase apps, changelog entries, author pages). This map covers the index pages, header, footer, and in-page controls. Individual blog posts, story pages, and showcase apps were not each photographed.

## Header (desktop)

Shot: [screenshots/flutterflow-io-desktop.png](screenshots/flutterflow-io-desktop.png).

| Control | Opens |
|---|---|
| Logo | [https://www.flutterflow.io/](https://www.flutterflow.io/) |
| Product (button) | Dropdown. See Product menu. |
| Studio (button) | Dropdown. See Studio menu. |
| Pricing | [https://www.flutterflow.io/pricing](https://www.flutterflow.io/pricing) |
| Enterprise | [https://www.flutterflow.io/enterprise](https://www.flutterflow.io/enterprise) |
| Resources (button) | Dropdown. See Resources menu. |
| Sign in | Auth wall [https://build.flutterflow.io/signin](https://build.flutterflow.io/signin). Branch stopped. |
| Start building | Auth wall [https://build.flutterflow.io/signin?returnTo=%2Fnew](https://build.flutterflow.io/signin?returnTo=%2Fnew). Not followed past the wall. |

### Product menu

Shot: [screenshots/flutterflow-io-desktop-menu-product.png](screenshots/flutterflow-io-desktop-menu-product.png).

| Item | Opens |
|---|---|
| Overview | [https://www.flutterflow.io/product](https://www.flutterflow.io/product) |
| AI | [https://www.flutterflow.io/ai](https://www.flutterflow.io/ai) |
| What's new | [https://www.flutterflow.io/changelog](https://www.flutterflow.io/changelog) |
| Docs | [https://docs.flutterflow.io/ffx](https://docs.flutterflow.io/ffx) (new tab) |
| FlutterFlow or Studio? | [https://www.flutterflow.io/flutterflow-vs-studio](https://www.flutterflow.io/flutterflow-vs-studio) |

### Studio menu

Shot: [screenshots/flutterflow-io-desktop-menu-studio.png](screenshots/flutterflow-io-desktop-menu-studio.png).

| Item | Opens |
|---|---|
| Sign in (panel CTA) | Auth wall [https://app.flutterflow.io/](https://app.flutterflow.io/). Branch stopped. |
| Overview | [https://www.flutterflow.io/studio](https://www.flutterflow.io/studio) |
| AI tools | [https://www.flutterflow.io/studio/ai](https://www.flutterflow.io/studio/ai) |
| Desktop app | [https://www.flutterflow.io/studio/desktop](https://www.flutterflow.io/studio/desktop) |
| Changelog | [https://www.flutterflow.io/studio/changelog](https://www.flutterflow.io/studio/changelog) |
| FAQ | [https://www.flutterflow.io/studio/faq](https://www.flutterflow.io/studio/faq) |
| Hire an expert | [https://www.flutterflow.io/studio/work-with-developers](https://www.flutterflow.io/studio/work-with-developers) |
| Apply to be an expert | [https://www.flutterflow.io/studio/apply-to-be-a-developer](https://www.flutterflow.io/studio/apply-to-be-a-developer) |

### Resources menu

Shot: [screenshots/flutterflow-io-desktop-menu-resources.png](screenshots/flutterflow-io-desktop-menu-resources.png).

| Item | Opens |
|---|---|
| Showcase | [https://www.flutterflow.io/studio/showcase](https://www.flutterflow.io/studio/showcase) |
| Customer stories | [https://www.flutterflow.io/customer-stories](https://www.flutterflow.io/customer-stories) |
| Blog | [https://www.flutterflow.io/blog](https://www.flutterflow.io/blog) |
| Docs | [https://docs.flutterflow.io/](https://docs.flutterflow.io/) (new tab) |
| Trainings | YouTube playlist (external, not followed) |
| Templates | [https://marketplace.flutterflow.io/home](https://marketplace.flutterflow.io/home) (new tab) |
| Community | [https://community.flutterflow.io/](https://community.flutterflow.io/) (new tab) |
| Developer groups | [https://www.flutterflow.io/flutterflow-developer-groups](https://www.flutterflow.io/flutterflow-developer-groups) |
| Student ambassadors | [https://www.flutterflow.io/student-ambassadors](https://www.flutterflow.io/student-ambassadors) |

## Header (phone)

Shot: [screenshots/flutterflow-io-phone.png](screenshots/flutterflow-io-phone.png). The hamburger control is labelled Open menu. The click that was meant to open it landed on the prompt's send control, so the sheet was not photographed. The same Product, Studio, and Resources destinations are in the desktop menus. Phone pages of the index routes were photographed.

| Control | Opens |
|---|---|
| Logo | Home |
| Start building | Auth wall `build.flutterflow.io/signin?returnTo=/new`. Not followed. |
| Open menu | Intended to open the mobile nav sheet. Not captured: the click missed the control. |

## Footer

Present on the marketing pages. Sign in in the footer goes to `https://build.flutterflow.io/signin?landing_page_version=v3` (auth wall, not followed).

| Control | Opens |
|---|---|
| Build, Refine, Launch, Scale | In-page anchors on home (`#build`, `#refine`, `#launch`, `#scale`) |
| Pricing | `/pricing` |
| Docs | `https://docs.flutterflow.io/ffx` and `https://docs.flutterflow.io/` |
| Open Studio | Auth wall `https://app.flutterflow.io/` |
| Templates | `https://marketplace.flutterflow.io/` |
| Community | `https://community.flutterflow.io/` |
| Status | `https://status.flutterflow.io/` (external, not followed) |
| About | `/about-us` |
| Careers | `https://jobs.ashbyhq.com/FlutterFlow` (external, not followed) |
| Blog | `/blog` |
| Contact | `/contact-us` |
| X, YouTube, LinkedIn, Reddit | External social profiles, not followed |
| Terms | `/tos` |
| Privacy | `/privacy` |
| Marketplace terms | `/tos-marketplace` |
| Your Privacy Choices | Button is in the footer DOM with `aria-haspopup=dialog`, and `display: none` at 1440×900, so it has no box and no dialog opened. Not accepted. Not photographed. |
| Match your system / Light / Dark | Theme radio group. Sets `data-theme` on the document. Dark paint photographed by setting the attribute: [screenshots/www-flutterflow-io-desktop-dark.png](screenshots/www-flutterflow-io-desktop-dark.png). |

## In-page controls on home

| Control | What it does |
|---|---|
| Prompt field | Types a description. Not submitted. Placeholder rotates. |
| Previous idea / Next idea | Cycles the sample prompt. Local only. |
| Tab / Use it | Inserts the sample prompt into the field. Local only. |
| Start building (send) | Would start a build. Not pressed. Same auth destination as the header CTA. |
| Talk to sales | `/enterprise` |
| Open FlutterFlow Studio / Open the builder | Auth wall `https://app.flutterflow.io/` |

## Index pages photographed

Desktop and phone unless noted. Auth links on these pages go to the same walls and were not followed.

| Page | URL | Notes |
|---|---|---|
| Home | `/` | Menus photographed on desktop. |
| Product | `/product` | |
| AI | `/ai` | |
| What's new | `/changelog` | Index only. Entry pages in the sitemap were not each opened. |
| FlutterFlow or Studio | `/flutterflow-vs-studio` | |
| Studio | `/studio` | |
| Studio AI | `/studio/ai` | |
| Studio desktop | `/studio/desktop` | |
| Studio FAQ | `/studio/faq` | |
| Studio showcase | `/studio/showcase` | Index. Individual apps not each opened. |
| Work with developers | `/studio/work-with-developers` | |
| Apply to be an expert | `/studio/apply-to-be-a-developer` | Form present. Not filled. Not submitted. |
| Pricing | `/pricing` | Monthly and Yearly buttons toggle the price display. Plan CTAs (Start free, Get Basic, Get Pro, Get Max) go to the sign-in wall with `returnTo=/account/usage`. Not followed. FAQ items are `<summary>` disclosures. Education Apply opens a Typeform (`flutterflow.typeform.com`). Not followed. |
| Enterprise | `/enterprise` | |
| Blog | `/blog` | Index. 111 posts in the sitemap, not each opened. |
| Customer stories | `/customer-stories` | Index. 22 stories in the sitemap, not each opened. |
| About | `/about-us` | |
| Contact | `/contact-us` | Four destination cards (docs, Typeform for schools, enterprise, partners). No fields filled. |
| Privacy | `/privacy` | |
| Terms | `/tos` | |
| Marketplace terms | `/tos-marketplace` | Desktop. |
| Sitemap | `/sitemap` | HTML index. |
| Student ambassadors | `/student-ambassadors` | |
| Developer groups | `/flutterflow-developer-groups` | |
| Designer | `/designer` | Desktop. |
| IXDC | `/ixdc`, `/ixdc-official-rules` | Desktop. |
| Wrapped | `/wrapped` | Desktop. |
| You ask we build | `/you-ask-we-build` | Desktop. |
| Fund | `/fund` | Desktop. Linked from a page, not the header. |
| Docs | `https://docs.flutterflow.io/` | Public docs. Search box present. Not submitted. Sidebar opens doc sections. |
| Docs FFX | `https://docs.flutterflow.io/ffx` | Product docs for the describing-it builder. |
| Marketplace | `https://marketplace.flutterflow.io/` | Public catalog. |
| Community | `https://community.flutterflow.io/` | Public forum index. |

## Auth wall (branch stopped)

| From | URL | What it asks | Shot |
|---|---|---|---|
| Sign in, Start building, plan CTAs | `https://build.flutterflow.io/signin` | Email, password, or Google, Apple, GitHub, Microsoft. Create an account and Forgot password are links. Not clicked. | [screenshots/build-flutterflow-io-signin-wall-desktop.png](screenshots/build-flutterflow-io-signin-wall-desktop.png) |
| Open Studio, Studio menu Sign in | `https://app.flutterflow.io/login` | Flutter canvas. After paint: email, password, or Google, Apple, GitHub, Microsoft. Not clicked. | [screenshots/app-flutterflow-io-login-wall-desktop.png](screenshots/app-flutterflow-io-login-wall-desktop.png) |

No human-check or captcha blocked a page before it painted.
