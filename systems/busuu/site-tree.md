# Busuu public site tree

Mapped on 2026-11-21 from [https://www.busuu.com/](https://www.busuu.com/) in headless Chromium, signed out. Desktop viewport measured 1440×900. Phone viewport measured 390×844, except the blog, which painted at 393×851 and was not kept. No email, password, phone number, or code was typed. No form was submitted. Google, Apple, Facebook, Microsoft, and SSO were not clicked. Cookie banners were hidden, never answered.

The signed-in product on `app.busuu.com` was not opened. A control that points at login, register, or an SSO host is listed and that branch stops.

## How the home page opens things

| Control | Where | Opens |
|---|---|---|
| Wordmark | Header, every marketing page | [https://www.busuu.com/](https://www.busuu.com/) |
| Learn for free | Header pill and hero pill | [https://www.busuu.com/en/choose-your-language](https://www.busuu.com/en/choose-your-language) |
| Log in | Header outline button | [https://www.busuu.com/en/login](https://www.busuu.com/en/login). Wall. Stop. |
| Kebab `#js-menu-toggle` | Header, desktop and phone | Local dropdown. Log in, For Educators, For Businesses. See [tree-desktop-home-light-menu.png](screenshots/tree-desktop-home-light-menu.png) and [tree-phone-home-light-menu.png](screenshots/tree-phone-home-light-menu.png). |
| Kebab: Log in | Dropdown | Same login wall. Stop. |
| Kebab: For Educators | Dropdown | [https://business.busuu.com/education](https://business.busuu.com/education) |
| Kebab: For Businesses | Dropdown | [https://business.busuu.com/](https://business.busuu.com/) |
| Language flag (English, Spanish, and the rest) | "I want to learn" | [https://www.busuu.com/en/register?learning=…](https://www.busuu.com/en/register). Wall. Stop. A flag is not chosen. |
| Get started | Sticky band | Language picker, same as Learn for free |
| Display Language | Footer `<select>` | Native list of 16 interface languages. Focusing it does not navigate. The painted list did not open in headless Chromium. See [tree-desktop-home-light-footer.png](screenshots/tree-desktop-home-light-footer.png). Changing it was not done. |

## Marketing pages reached from the footer

Each row is a public page. The same control exists on desktop and phone. Screenshots are viewport shots, light theme only. The site does not offer a dark theme.

| Footer control | URL | Desktop | Phone |
|---|---|---|---|
| (home, not a footer link) | [https://www.busuu.com/](https://www.busuu.com/) | [tree-desktop-home-light-default.png](screenshots/tree-desktop-home-light-default.png) | [tree-phone-home-light-default.png](screenshots/tree-phone-home-light-default.png) |
| Learn Spanish online (and 13 sibling course links) | `/en/course/learn-<language>-online` | Spanish: [tree-desktop-course-spanish-light-default.png](screenshots/tree-desktop-course-spanish-light-default.png). Japanese, a second template: [tree-desktop-course-japanese-light-default.png](screenshots/tree-desktop-course-japanese-light-default.png) | [tree-phone-course-spanish-light-default.png](screenshots/tree-phone-course-spanish-light-default.png), [tree-phone-course-japanese-light-default.png](screenshots/tree-phone-course-japanese-light-default.png) |
| How Busuu works | [https://www.busuu.com/en/it-works/courses](https://www.busuu.com/en/it-works/courses) | [tree-desktop-it-works-light-default.png](screenshots/tree-desktop-it-works-light-default.png) | [tree-phone-it-works-light-default.png](screenshots/tree-phone-it-works-light-default.png) |
| Busuu Premium plans | [https://www.busuu.com/en/premium](https://www.busuu.com/en/premium) redirects to `/products/en` | [tree-desktop-premium-light-default.png](screenshots/tree-desktop-premium-light-default.png) | [tree-phone-premium-light-default.png](screenshots/tree-phone-premium-light-default.png) |
| Busuu for Business | [https://business.busuu.com/](https://business.busuu.com/) | [tree-desktop-business-light-default.png](screenshots/tree-desktop-business-light-default.png) | [tree-phone-business-light-default.png](screenshots/tree-phone-business-light-default.png) |
| Download Busuu | [https://www.busuu.com/en/mobile](https://www.busuu.com/en/mobile) | [tree-desktop-mobile-app-light-default.png](screenshots/tree-desktop-mobile-app-light-default.png) | [tree-phone-mobile-app-light-default.png](screenshots/tree-phone-mobile-app-light-default.png) |
| Redeem a voucher | [https://www.busuu.com/en/voucher](https://www.busuu.com/en/voucher) | [tree-desktop-voucher-light-default.png](screenshots/tree-desktop-voucher-light-default.png) | [tree-phone-voucher-light-default.png](screenshots/tree-phone-voucher-light-default.png) |
| Busuu Blog | [https://blog.busuu.com/](https://blog.busuu.com/) | [tree-desktop-blog-light-default.png](screenshots/tree-desktop-blog-light-default.png) | Not captured. Phone viewport measured 393×851, not 390. |
| Contact us | [https://help.busuu.com/hc/requests/new](https://help.busuu.com/hc/requests/new) | Not photographed. A request form. Not filled. | Same. |
| FAQs | [https://help.busuu.com/hc/en-us](https://help.busuu.com/hc/en-us) | [tree-desktop-help-light-default.png](screenshots/tree-desktop-help-light-default.png) | [tree-phone-help-light-default.png](screenshots/tree-phone-help-light-default.png) |
| About Busuu | [https://www.busuu.com/en/about](https://www.busuu.com/en/about) | [tree-desktop-about-light-default.png](screenshots/tree-desktop-about-light-default.png) | [tree-phone-about-light-default.png](screenshots/tree-phone-about-light-default.png) |
| Careers | [https://www.busuu.com/en/careers](https://www.busuu.com/en/careers) | [tree-desktop-careers-light-default.png](screenshots/tree-desktop-careers-light-default.png) | [tree-phone-careers-light-default.png](screenshots/tree-phone-careers-light-default.png) |
| Press | [https://www.busuu.com/en/press](https://www.busuu.com/en/press) | [tree-desktop-press-light-default.png](screenshots/tree-desktop-press-light-default.png) | [tree-phone-press-light-default.png](screenshots/tree-phone-press-light-default.png) |
| Partner with Busuu | [https://www.busuu.com/en/partners](https://www.busuu.com/en/partners) | [tree-desktop-partners-light-default.png](screenshots/tree-desktop-partners-light-default.png) | [tree-phone-partners-light-default.png](screenshots/tree-phone-partners-light-default.png) |
| COVID-19 | [https://www.busuu.com/en/covid-19](https://www.busuu.com/en/covid-19) | [tree-desktop-covid-light-default.png](screenshots/tree-desktop-covid-light-default.png) | [tree-phone-covid-light-default.png](screenshots/tree-phone-covid-light-default.png) |
| Modern Slavery Statement | [https://www.busuu.com/en/modern-slavery-statement](https://www.busuu.com/en/modern-slavery-statement) | [tree-desktop-slavery-light-default.png](screenshots/tree-desktop-slavery-light-default.png) | [tree-phone-slavery-light-default.png](screenshots/tree-phone-slavery-light-default.png) |
| Terms | [https://www.busuu.com/en/terms](https://www.busuu.com/en/terms) | [tree-desktop-terms-light-default.png](screenshots/tree-desktop-terms-light-default.png) | [tree-phone-terms-light-default.png](screenshots/tree-phone-terms-light-default.png) |
| Privacy | [https://www.busuu.com/en/privacy](https://www.busuu.com/en/privacy) | [tree-desktop-privacy-light-default.png](screenshots/tree-desktop-privacy-light-default.png) | [tree-phone-privacy-light-default.png](screenshots/tree-phone-privacy-light-default.png) |

App Store and Google Play badges in the footer leave the site. Social icons (X, Facebook, TikTok, YouTube) leave the site. Those hosts were not captured.

## Pages one click from home that are not the footer

| Control | URL | What it is | Shots |
|---|---|---|---|
| Locale home | [https://www.busuu.com/en](https://www.busuu.com/en) | English marketing home, a different hero from `/` | [tree-desktop-en-light-default.png](screenshots/tree-desktop-en-light-default.png), [tree-phone-en-light-default.png](screenshots/tree-phone-en-light-default.png) |
| Language picker | [https://www.busuu.com/en/choose-your-language](https://www.busuu.com/en/choose-your-language) | 14 language cards. Each card's href is empty in the DOM. Choosing one starts register. Not chosen. | [tree-desktop-languages-light-default.png](screenshots/tree-desktop-languages-light-default.png), [tree-phone-languages-light-default.png](screenshots/tree-phone-languages-light-default.png) |
| Sign up (app shell header) | Same picker, or `/en/register` | Wall. Stop. | Not followed past the picker. |
| Grammar article (sample) | [https://www.busuu.com/en/spanish/spanish-numbers](https://www.busuu.com/en/spanish/spanish-numbers) | One article template. Dozens of siblings exist under `/en/<language>/<topic>`. | [tree-desktop-grammar-light-default.png](screenshots/tree-desktop-grammar-light-default.png), [tree-phone-grammar-light-default.png](screenshots/tree-phone-grammar-light-default.png) |
| Study guide (sample) | [https://www.busuu.com/en/languages/how-to-speak-spanish](https://www.busuu.com/en/languages/how-to-speak-spanish) | One guide template. | [tree-desktop-guide-light-default.png](screenshots/tree-desktop-guide-light-default.png), [tree-phone-guide-light-default.png](screenshots/tree-phone-guide-light-default.png) |

Course landings share one template. Spanish stands for English, French, German, Dutch, Italian, Portuguese, Chinese, Polish, Turkish, Russian, Arabic, and Korean. Japanese was shot as the second look. Article pages share one template. Spanish numbers stands for the rest of that family.

## Overlays that do not need sign-in

| Overlay | How it opens | What it contains | Shot |
|---|---|---|---|
| Home kebab | `#js-menu-toggle` | Log in (wall), For Educators, For Businesses | Desktop and phone menu shots above |
| Premium billing period | `role="radio"` inside a `role="radiogroup"` on `/products/en`. "12 months" is selected on load. "1 month" is a local toggle. | Prices change. Get Premium still leaves for checkout and was not clicked. | [tree-desktop-premium-light-monthly.png](screenshots/tree-desktop-premium-light-monthly.png) |
| Premium close | X, `aria-label="Close page."` | Leaves the paywall. Not pressed, so the underlying page is not invented. | Visible on the premium shots |
| Business "Our offer" | `button.menu__child-toggle` labelled "Show submenu for Our offer" | Our product, Our method, four corporate training links | [tree-desktop-business-light-submenu.png](screenshots/tree-desktop-business-light-submenu.png) |
| Business Industries, Resources | Same toggle pattern | Industry anchors and resource anchors. Same menu component. Not each opened. | Same control as Our offer |
| Business phone drawer | `.mobile-trigger` | Full-screen nav: About, Our offer, Industries, Clients, Resources | [tree-phone-business-light-menu.png](screenshots/tree-phone-business-light-menu.png) |
| Business announcement bar | Present on load | Dismiss X is a local close. Not pressed. | Visible on the business shots |
| Help language menu | "English (United States)" in the help header | Zendesk locale list. Not opened. Changing locale was not done. | Help shots |
| Help search | Search field on the help home | Not typed. | Help shots |
| Footer Display Language | Footer `<select>` | 16 options, listed in the probe, not changed | Footer shot |

## Walls: recorded, then stopped

| Control | URL | What the page asks for |
|---|---|---|
| Log in, kebab Log in, voucher Log in, help Sign in | [https://www.busuu.com/en/login](https://www.busuu.com/en/login) | Email and password. Optional "Use your mobile number". Continue with Google, Apple, or Facebook. "Log in with SSO". Forgot password. A stale-session reset banner was already on the page. Nothing was typed. Nothing was clicked. Shots: [tree-desktop-login-light-default.png](screenshots/tree-desktop-login-light-default.png), [tree-phone-login-light-default.png](screenshots/tree-phone-login-light-default.png). |
| Learn-for-free flags, course CTAs, article CTAs, Sign up | [https://www.busuu.com/en/register](https://www.busuu.com/en/register) and `?learning=` variants, plus `/en-us/register` | Account creation. Not opened. |
| Business LOG IN | [https://org.busuu.com/app#/en/login](https://org.busuu.com/app#/en/login) | Organisation SSO. Not opened. |
| Get Premium, Get Premium Plus | Checkout on the products host | Purchase. Not opened. |
| Book a demo, Get in touch | [https://business.busuu.com/demo](https://business.busuu.com/demo) and the contact form | A lead form. Not filled. |
| Help Submit a request | [https://help.busuu.com/hc/requests/new](https://help.busuu.com/hc/requests/new) | A request form. Not filled. |
| Blog Log in, Start Learning | Login and register walls | Not followed. |
| Careers job links | `busuu.teamtailor.com`, Workday | External applications. Not opened. |

## Hosts the home page names and this capture did not enter

`app.busuu.com` (the product), `org.busuu.com` (business SSO), Apple App Store, Google Play, social hosts, press outlets linked from the press page, and job-board hosts. External links are recorded as leaves.

## What was not captured, and why

- Signed-in lessons, review, profile, and settings. They sit behind login.
- Register step 1 onward, checkout, voucher redemption, demo booking, and the help request form. Each is a form or a purchase.
- A dark theme. The public site does not offer one.
- The native footer language list and the help locale list. Headless Chromium did not paint the native popup. The option labels were read from the `<select>` and are in the probe, not guessed into a screenshot.
- Phone blog. The measured viewport was 393×851, so it is not a 390 capture.
- Every grammar article and every course language. One of each template was photographed. The map above names the family.
