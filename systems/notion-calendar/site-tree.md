# Notion Calendar public site tree

Mapped on 2026-11-22 from the live public site, signed out. Requested URL `https://notion.com/product/calendar` redirected to `https://www.notion.com/product/calendar`. Page title: "Notion Calendar". Hero: "It's time."

The host is `www.notion.com`. The signed-in calendar app at `calendar.notion.so` and the desktop app in [systems/notion-calendar-desktop](../notion-calendar-desktop) are different surfaces and were not entered. [systems/notion](../notion) is the Notion workspace marketing site and was not edited.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. `login-extracted` stays `not-started`.

The marketing page paints one light theme. `color-scheme` on the root was `normal`. There is no public theme switch. Desktop shots are 1440 by 900 CSS pixels. The phone homepage is 390 by 844.

## Auth walls

Photographed empty. Stopped there.

| Control | Opens | Action |
|---|---|---|
| Header "Log in" | `https://www.notion.com/login/calendar` redirects to `https://app.notion.com/login/calendar` | Empty email field. "Welcome to Notion Calendar". Continue, then Google, Apple, Microsoft, Passkey, SSO. Not typed. Providers not clicked. Continue not clicked. |
| Header "Get Notion Calendar free" | `https://www.notion.com/product/calendar/signup` redirects to `https://calendar.notion.so/` and then to a login wall with `error=true` | Same empty login wall. Not typed. Providers not clicked. |
| Hero "Get Notion Calendar free" | `https://www.notion.com/calendar/signup` redirects the same way, to the login wall | Not typed. Providers not clicked. |
| Direct signup URL | `https://www.notion.com/signup/calendar` redirects to `https://app.notion.com/signup/calendar` | Empty work-email field. "Sign up with your work email". Continue, then Google and Microsoft. Not typed. Providers not clicked. Continue not clicked. |
| Login "Sign up" | `/signup/calendar` | Not followed from the login card. |
| Signup "Log in" | `/login/calendar` | Not followed from the signup card. |
| Request a demo | `https://www.notion.com/contact-sales` | Empty work-email field and Next. Not typed. Next not clicked. |

## Homepage header (`https://www.notion.com/product/calendar`)

Desktop, left to right: Product (link), How to (link), Enterprise (link), Resources (button), wordmark, Pricing, Request a demo, Log in, Get Notion Calendar free.

In the T3 preview at 1440 CSS, Product, How to, and Enterprise are links, not dropdowns. Resources is the only button, and a click sets `aria-expanded` to true.

Headless Chromium painted Product and Resources as dropdowns on the same URL. That is a client variant, not the preview tree. The shot of the Resources panel matches the preview. The Product dropdown was not photographed as the public tree.

| Control | Opens |
|---|---|
| Wordmark | `https://www.notion.com/` |
| Product | `https://www.notion.com/product/all-features` |
| How to | `https://www.notion.com/a-new-shape-for-work` |
| Enterprise | `https://www.notion.com/enterprise` |
| Resources | Dropdown. Shot: [desktop-menu-resources.png](screenshots/site-tree/desktop-menu-resources.png). |
| Pricing | `https://www.notion.com/pricing` |
| Request a demo | `https://www.notion.com/contact-sales` (work-email step). Stopped. Not submitted. |
| Log in | `https://app.notion.com/login/calendar`. **Wall. Stop.** |
| Get Notion Calendar free | Signup URL that landed on a login wall in the preview. The empty signup wall is `https://app.notion.com/signup/calendar`. **Wall. Stop.** |

### Resources menu

Opened by clicking Resources. Three columns, then a promo row.

| Group | Item | Opens |
|---|---|---|
| Notion for | Enterprise | `/enterprise` |
| Notion for | Small businesses | `/teams` |
| Notion for | Startups | `/startups` |
| Notion for | Developers | `/product/dev` |
| Discover | What's New | `/releases` |
| Discover | Customer stories | `/customers` |
| Discover | Webinars | `/webinars` |
| Discover | Templates | `/templates` |
| Discover | Consultants | `/explore-consultants` |
| Discover | Blog | `/blog` |
| Learn | Academy | `https://academy.notion.com/` (leaves www.notion.com). Recorded, not walked. |
| Learn | Product tours | `/product/demos` |
| Learn | Help Center | `/help` |
| Promo | See what's new | `/releases` |
| Promo | Notion app | `/download` |

## Homepage body

| Control | Opens |
|---|---|
| Get Notion Calendar free | `/calendar/signup`. Preview landed on a login wall. **Wall. Stop.** |
| Download for macOS | `/calendar/desktop/mac-universal/download`. A file download, not a page. Not saved. |
| Play | In-page product video. Not played. |
| macOS, Windows (lower on the page) | `/calendar/desktop/mac/download`, `/calendar/desktop/windows/download`. File downloads. Not saved. |
| Apple App Store | `https://apps.apple.com/app/notion-calendar/id1607562761`. External. Not opened. |
| Google Play | `https://play.google.com/store/apps/details`. External. Not opened. |
| Get Notion Calendar free (lower CTA) | `/calendar/signup`. **Wall. Stop.** |

The laptop and phone in the hero are marketing art of a January 2024 calendar. They are not a signed-in account.

## Phone (390)

Logo, Get Notion Calendar free, and Open navigation. The drawer lists Product, How to, Enterprise, Resources (chevron), Pricing, Download. Footer of the drawer: Request a demo, Log in. Shot: [phone-nav-drawer.png](screenshots/site-tree/phone-nav-drawer.png). No row was followed.

## Footer

Shared Notion footer on the calendar page.

| Column | Items |
|---|---|
| Product | Features (`/product/features`), What's New (`/releases`), Notion AI (`/product/ai`), Pricing, Request a demo, Download, Explore more (`/explore`) |
| Resources | Customer stories, Connections (`/connections`), Marketplace (`/templates`), Help Center, Academy, Community (`/community`) |
| Company | About us (`/about`), Careers (`/careers`), Security (`/security`), Status (`https://www.notion-status.com/`), Terms & privacy (a published page on app.notion.com), Your privacy rights (`/trust/privacy-policy`) |
| Notion for | Enterprise, Small businesses, Startups, Developers (`https://developers.notion.com/`) |
| Locales | English (US) and other locales of `/product/calendar`. English (US) only was captured. |
| Cookie settings | Cookie preferences. Not opened. Not submitted. |

## Pages opened

| Page | What it is |
|---|---|
| `https://www.notion.com/product/calendar` | Calendar marketing home. Desktop and phone. |
| `https://www.notion.com/product/calendar/download` | Calendar desktop download page. macOS Universal selector. Download button starts a file. Not saved. |
| `https://www.notion.com/download` | Notion Desktop download page. Includes a Notion Calendar card whose Download for macOS is a file. |
| `https://www.notion.com/pricing` | Notion plans (Free, Plus, Business, Enterprise). Free includes "Notion Calendar". Pay yearly was the painted state. Pay monthly was not switched. Sign up, Get started, and Contact Sales were not clicked. |
| `https://www.notion.com/help/category/notion-calendar` | Help category. Search was not used. Articles were not opened. |
| `https://www.notion.com/contact-sales` | Empty work-email step. Not submitted. |
| `https://app.notion.com/login/calendar` | Empty login wall. |
| `https://app.notion.com/signup/calendar` | Empty signup wall. |

Shared Notion marketing pages (Product, How to, Enterprise, blog, customers, careers) belong to [systems/notion](../notion). They were recorded in the tree and not recaptured here.
