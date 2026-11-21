# Makersite public site tree

Mapped 2026-11-21 from [https://makersite.io/](https://makersite.io/) while signed out, before the refresh screenshots. [https://makersite.com](https://makersite.com) returns HTTP 302 to that host. Desktop readings are 1440 CSS pixels wide. The page title is "Makersite | AI-Powered Product Lifecycle Intelligence". The marketing site paints light: `html` has no theme class, no `data-theme`, and `color-scheme` is `normal`. There is no theme switch on the homepage.

A control that opens a login, signup, demo form, or identity-provider wall stops that branch. Nothing was typed. No form was submitted. Google, Apple, and other identity providers were not clicked. Cookie Accept all, Accept only essential cookies, and Individual Privacy Preferences were not pressed while mapping this tree.

The Borlabs Cookie "Privacy Preference" dialog covers the homepage on a fresh visit in a headed browser. A later headless run left `#BorlabsCookieBox` at height 0, so the cookie shot is the first headed frame, saved as [screenshots/site-tree/desktop-cookie-dialog.png](screenshots/site-tree/desktop-cookie-dialog.png). Shots of opened states live in [screenshots/site-tree/](screenshots/site-tree/).

## Announcement bar

A lime bar (`rgb(222, 255, 0)`) appears after a menu opens, and on the phone before the drawer opens. It is not in the first hero frame.

| Control | Kind | Opens |
|---|---|---|
| SiGREEN Becomes Mattermaps | Text | Not a link |
| Read more | Link | https://makersite.io/press/sigreen-becomes-mattermaps-as-makersite-completes-ownership-transition/ |
| Close | Control | Dismisses the bar. Not pressed. |

## Utility bar

Present above the primary menu. The wordmark link has no visible text. Its accessible name comes from the logo image.

| Control | Kind | Opens |
|---|---|---|
| Wordmark | Link | https://makersite.io/ |
| Get a job | Link | https://makersitegmbh.recruitee.com/ (leaves the site) |
| Contact | Link | https://makersite.io/contact/ |
| Mattermaps | Link | http://www.mattermaps.com/ (leaves the site) |
| Book a Demo | Link | https://makersite.io/book-a-demo/ (demo form). Stopped. Not submitted. |

## Primary menu

Present on the homepage. Parent labels with children are links with `href` empty. Hover does not open the submenu (`display: none` stays). A click on the parent opens the submenu. Escape does not close it. A click elsewhere does. At 390 the same items sit in a drawer opened by "Primary Menu" (`button.menu-toggle`).

| Control | Kind | Opens |
|---|---|---|
| What is Makersite? | Link, parent | Submenu. Shot: [desktop-menu-what-is.png](screenshots/site-tree/desktop-menu-what-is.png). |
| What can I do with it? | Link, parent | Submenu. Shot: [desktop-menu-what-can-i-do.png](screenshots/site-tree/desktop-menu-what-can-i-do.png). |
| Who is it for? | Link, parent | Submenu. Shot: [desktop-menu-who.png](screenshots/site-tree/desktop-menu-who.png). |
| Customer stories | Link | https://makersite.io/customer-story/ |
| Resources | Link, parent | Submenu. Shot: [desktop-menu-resources.png](screenshots/site-tree/desktop-menu-resources.png). |
| Company | Link, parent | Submenu. Shot: [desktop-menu-company.png](screenshots/site-tree/desktop-menu-company.png). |
| Primary Menu | Button | Hidden at 1440 (`button.menu-toggle` has no box). At 390 the visible control is `a#open-mobile-menu`. A tap opens a full-screen drawer. Shot: [phone-nav-drawer.png](screenshots/site-tree/phone-nav-drawer.png). |

## What is Makersite? menu

| Label | Opens |
|---|---|
| AI, Data and Apps | https://makersite.io/makersite-ai-data-apps/ |
| Features and Benefits | https://makersite.io/features-and-benefits/ |
| Pricing | https://makersite.io/pricing/ |
| Data Foundation | https://makersite.io/makersite-data-foundation/ |

## What can I do with it? menu

The submenu has two groups. "Product declarations" and "Accelerate Product Design" are group labels, not links.

| Label | Opens |
|---|---|
| Automated LCA & PCF | https://makersite.io/get-to-net-zero/automated-lcas/ |
| EPD Automation & Scale | https://makersite.io/get-to-net-zero/epd-automation-and-scale/ |
| Scope 3 Supply Chain Emissions | https://makersite.io/get-to-net-zero/scope-3-supply-chain-emissions-software/ |
| Product Material Compliance | https://makersite.io/features-and-benefits/product-compliance/ |
| AI-Enabled Ecodesign | https://makersite.io/accelerate-product-design/ai-enabled-ecodesign-using-lcas/ |
| Chemical Data Enrichment | https://makersite.io/accelerate-product-design/chemical-data-enrichment/ |
| Sustainability Data With PTC Windchill | https://makersite.io/ptc-makersite-real-time-sustainability-in-product-design/ |
| Teamcenter Sustainability Lifecycle Assessment | https://makersite.io/siemens-makersite-real-time-sustainability-in-product-development/ |
| Build Resilient Supply Chains | https://makersite.io/resilient-supply-chain/ |

## Who is it for? menu

| Label | Opens |
|---|---|
| For Engineers | https://makersite.io/for-engineers/ |
| For Procurement | https://makersite.io/for-procurement/ |
| For Sustainability Experts | https://makersite.io/for-sustainability-experts/ |
| For Experts | https://makersite.io/for-experts/ |

## Resources menu

| Label | Opens |
|---|---|
| Sustainability data playbooks | https://makersite.io/playbooks/ |
| How to purchase sustainability software | https://makersite.io/insights/how-to-write-an-rfp-for-sustainability-solutions/ |
| What good independent analysis for LCA software looks like | https://makersite.io/what-independent-analysts-look-for-in-lca-software/ |
| Insights | https://makersite.io/insights/ |
| Makersite x Forrester study | https://makersite.io/makersite-x-forrester-study-transform-product-sustainability-into-performance-initiatives-with-product-lifecycle-intelligence/ |

## Company menu

| Label | Opens |
|---|---|
| We are Makersite | https://makersite.io/we-are-makersite/ |
| Our Partners | https://makersite.io/our-partners/ |
| Careers | https://makersitegmbh.recruitee.com/ (leaves the site) |
| Press | https://makersite.io/press/ |

## Homepage body

Controls that are not the header or the footer. "Watch a demo" and "Book a Demo" stop at a demo wall. The Articulate placeholder is a third-party embed gate. Unblock and Accept required service were not clicked.

| Control | Kind | Opens |
|---|---|---|
| What is Makersite? | Link | https://makersite.io/makersite-ai-data-apps/ |
| Watch a demo | Link | https://makersite.io/makersite-platform-demo/ (demo). Stopped. |
| How Makersite helped 3M | Link | https://makersite.io/customer-story/how-3m-accelerated-to-portfolio-scale-sustainability-data/ |
| See how Makersite helped Lenovo | Link | https://makersite.io/customer-story/lenovo-strengthens-enterprise-competitiveness-sustainability-with-configuration-level-pcfs/ |
| Learn how Barco connect their products to supply chain data | Link | https://makersite.io/customer-story/barco-create-multiple-lcas-and-pefs-on-the-fly/ |
| Learn how Makersite is used for ecodesign | Link | https://makersite.io/customer-story/microsofts-lca-methodology/ |
| See how Cummins standardize product & supply chain data | Link | https://makersite.io/customer-story/cummins-inc-s-journey-with-product-level-lcas-supply-chain-insights/ |
| Unblock content | Link | Stays on the homepage. Third-party embed gate. Not clicked. |
| Accept required service and unblock content | Link | Stays on the homepage. Third-party consent. Not clicked. |
| More Information | Link | Stays on the homepage. Not clicked. |
| Find out more | Link | https://makersite.io/guide-pfas/ |
| Explore Features & Benefits | Link | https://makersite.io/features-and-benefits/ |
| More about Makersite's data | Link | https://makersite.io/makersite-data-foundation/ |
| Automate your way to Net Zero | Link | https://makersite.io/get-to-net-zero/ |
| Learn about Multi-Criteria Ecodesign | Link | https://makersite.io/accelerate-product-design/ |
| Learn about Deep-Tier Transparency | Link | https://makersite.io/resilient-supply-chain/ |
| For Engineers | Card link | https://makersite.io/for-engineers/ |
| For Procurement | Card link | https://makersite.io/for-procurement/ |
| For Experts | Card link | https://makersite.io/for-experts/ |
| View all articles | Link | https://makersite.io/insights/ |
| Read more | Link | Insight articles, including the Construction Products Regulation guide and the AI lifecycle analysis guide |
| Get in touch | Link | https://makersite.io/contact/ |

## Cookie dialog

Opened by the site on first visit. Dialog id `BorlabsCookieBox`. Title "Privacy Preference". Essential is checked and disabled. Statistics and Marketing are unchecked. External Media says content from video and social platforms is blocked by default. None of the buttons were pressed.

| Control | Kind | Opens |
|---|---|---|
| Accept all | Button | Consent POST. Not pressed. |
| Accept only essential cookies | Button | Consent POST. Not pressed. |
| Individual Privacy Preferences | Button | Preference panel. Not pressed. |
| Preferences | Link | Preference panel. Not pressed. |
| Privacy Policy | Link | https://makersite.io/privacy-policy/ |
| Imprint | Link | https://makersite.io/impressum/ |
| Borlabs Cookie | Link | Leaves the site. Not clicked. |

Shot: [desktop-cookie-dialog.png](screenshots/site-tree/desktop-cookie-dialog.png).

## Footer

The footer repeats the product, audience, and company links. Imprint, Responsible disclosure, Privacy policy, and Social policy are extra. LinkedIn and Twitter leave the site. ISO 27001, TISAX, and GDPR marks are images, not links.

## Walls

No login, signup, or identity-provider control appears on the homepage. "Book a Demo", "Watch a demo", and "Get in touch" are the walls. They were opened only to photograph the form, then left unsubmitted.
