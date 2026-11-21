# Notion public site tree

Mapped 2026-11-21 from [https://www.notion.com/](https://www.notion.com/) while signed out, before the screenshot run. The page title on that load was "A shared brain for your team and agents. | Notion". A later load titled the same URL "The AI workspace that works for you. | Notion". The host is www.notion.com. Calendar (notion.calendar, formerly Cron) is a different product and is not this package.

Desktop shots are 1440 by 900 CSS pixels. Phone shots are 390 by 844. `html` carries a theme class (`QPCBRq_theme` on the first load). `color-scheme` stays `normal` when `prefers-color-scheme` is dark, and the page still paints white. There is no public theme switch.

A control that opens login, signup, or an identity provider stops that branch. Nothing was typed. No form was submitted. Google, Apple, Microsoft, ChatGPT, Passkey, and SSO were not clicked. Marketing links carry a `tid` query. That value is a browser cookie and is not written here.

The homepage mounts a marketing demo of the Notion app (a Ramp workspace mock). Those controls animate the demo. They are not the signed-in product. A report card, "The State of AI Transformation: Singapore Report", can cover the lower right. Its close control was not pressed while mapping.

## Header

Present on marketing pages. Product and Resources are buttons (`button.HWB10a_dropdownTrigger`), not links. A click sets `aria-expanded` to true and opens the panel. Hover alone did not open it in headless Chromium.

| Control | Kind | Opens |
|---|---|---|
| Wordmark | Link | https://www.notion.com/ |
| Product | Button | Dropdown. Shot: [desktop-menu-product.png](screenshots/site-tree/desktop-menu-product.png). |
| Resources | Button | Dropdown. Shot: [desktop-menu-resources.png](screenshots/site-tree/desktop-menu-resources.png). |
| Pricing | Link | https://www.notion.com/pricing |
| Request a demo | Link | https://www.notion.com/contact-sales (work-email step). Stopped. Not submitted. |
| Log in | Link | https://www.notion.com/login redirects to https://app.notion.com/login. **Wall. Stop.** |
| Get Notion free | Link | https://www.notion.com/signup redirects to https://app.notion.com/signup. **Wall. Stop.** |
| Open navigation | Button | Phone drawer. Shot: [phone-nav-drawer.png](screenshots/site-tree/phone-nav-drawer.png). |

## Product menu

Opened by clicking Product.

| Item | Opens |
|---|---|
| Capture | /product/features#capture |
| Find | /product/features#find |
| Automate | /product/features#automate |
| See all features | /product/features |
| See what's new | /releases |
| Download the Notion App | /download |

`/product/all-features` is a 404 ("Sorry, that page cannot be found."). The live destination is `/product/features`.

## Resources menu

Opened by clicking Resources. Blog was in an earlier DOM dump of a hidden menu and was not in the opened panel on the second pass.

| Group | Item | Opens |
|---|---|---|
| Notion for | Enterprise | /enterprise |
| Notion for | Small businesses | /teams |
| Notion for | Startups | /startups |
| Notion for | Developers | /product/dev |
| Discover | What's New | /releases |
| Discover | Customer stories | /customers |
| Discover | Webinars | /webinars |
| Discover | Templates | /templates |
| Discover | Consultants | /explore-consultants |
| Learn | Academy | https://academy.notion.com/ (leaves www.notion.com). Recorded, not walked. |
| Learn | Product tours | /product/demos |
| Learn | Help Center | /help |

## Homepage

| Control | Kind | Opens |
|---|---|---|
| Get Notion free | Link | /signup, then app.notion.com/signup. **Wall. Stop.** |
| Request a demo | Link | /contact-sales. Stopped. Not submitted. |
| Download report | Link | /resources/singapore-the-state-of-ai-transformation. Marketing article. |
| Close (report card) | Button | Dismisses the card. Not pressed while mapping. |
| Customer story cards | Link | /customers or /customers/<name>. Representative stories only. |
| Demo sidebar, Inbox, New page, Share | Buttons inside the homepage demo | Do not navigate. |

## Phone drawer

Opened by the header menu button at 390. Items: Product, How to, Enterprise, Resources, Pricing, Download. Footer of the drawer: Request a demo, Log in. Try Notion sits in the top bar and goes to signup. **Wall. Stop.**

How to and Enterprise appear as top-level rows on the phone. On desktop they are not header links. How to's desktop URL from the first DOM dump was `/a-new-shape-for-work`, which returned 404 on the later pass.

## Footer

Seen on the 404 page and linked from the homepage footer.

| Column | Items |
|---|---|
| Product | Features (/product/features), What's New (/releases), Notion AI (/product/ai), Pricing, Request a demo, Download |
| Resources | Customer stories, Connections (/connections), Marketplace (/templates), Help Center, Academy, Community (/community) |
| Company | About us (/about), Careers (/careers), Security (/security), Status (https://www.notion-status.com/, leaves the site), Terms & privacy (a published page on app.notion.com), Your privacy rights (/trust/privacy-policy) |
| Notion for | Enterprise, Small businesses, Startups, Developers (https://developers.notion.com/, leaves the site) |
| Locales | English (US) and other locales. English (US) only was captured. |
| Cookie settings | Cookie preferences. Not submitted. |

## Walls

| Control | Lands on | Stop |
|---|---|---|
| Log in | app.notion.com/login. Email field, Continue, then Google, ChatGPT, Apple, Microsoft, Passkey, SSO. | Photographed empty. Not typed. Providers not clicked. |
| Get Notion free, Try Notion | app.notion.com/signup. Work email field, Continue, then Google, Microsoft, ChatGPT. | Photographed empty. Not typed. Providers not clicked. |
| Request a demo, Contact Sales | www.notion.com/contact-sales. "What's your work email?" and Next. | Photographed empty. Not typed. Not submitted. |
