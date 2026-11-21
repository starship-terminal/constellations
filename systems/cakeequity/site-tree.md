# Cake Equity public site tree

Mapped from https://www.cakeequity.com/ on 2026-11-21 in headless Chromium, signed out. The sitemap lists 1,012 URLs. This file records every control on the shared chrome, every in-page control on the homepage, and one page of each public template. Collection pages (blog posts, guides, stories, events, changelog notes, partner profiles) follow the same template as their index. A control that opens a login or signup wall is recorded and that branch stops.

`robots.txt` allows `/` and disallows `/partner/`.

## Header

Present on every marketing page. At 1440 the links are in the bar. At 390 they move into the menu button.

| Control | Opens |
|---|---|
| cake. wordmark | https://www.cakeequity.com/ |
| Product | Mega menu, stays on the page. See Product menu. |
| Solutions | Mega menu, stays on the page. See Solutions menu. |
| Resources | Mega menu, stays on the page. See Resources menu. |
| Customers | https://www.cakeequity.com/stories |
| Pricing | https://www.cakeequity.com/pricing |
| Login | https://app.cakeequity.com/login/ then https://authentication.cakeequity.com/auth/cx/ . Empty email wall. Branch stops. See [login-review.json](login-review.json). |
| Book a demo | https://www.cakeequity.com/book-sales-demo |
| Get started free | https://app.cakeequity.com/setup_company/ . Company setup. Branch stops. Not opened past the URL. |
| Menu button (390) | In-page overlay with Product, Solutions, Resources, Customers, Pricing, Login, Book a demo, Get started free. |

A "Sign up for Beta" link in the DOM points at https://webflow.com/. It was not visible in the header.

## Product menu

Opened from the Product control. The panel stays on the page.

| Label | Opens |
|---|---|
| Cap Table | https://www.cakeequity.com/features/cap-table |
| Scenario Modeling | https://www.cakeequity.com/features/scenario-modeling |
| Founder Vesting | https://www.cakeequity.com/features/founder-vesting |
| Warrants | https://www.cakeequity.com/features/warrants |
| Audit Log | https://www.cakeequity.com/features/audit-log |
| Cake MCP | https://www.cakeequity.com/features/mcp |
| Equity Incentives | https://www.cakeequity.com/features/equity-incentives |
| Stock Options (ISO, NSO) | https://www.cakeequity.com/features/stock-options |
| Restricted Stocks (RSU, RSA) | https://www.cakeequity.com/features/restricted-stocks |
| Equity Benchmarking | https://www.cakeequity.com/features/equity-benchmarking |
| Employee App | https://www.cakeequity.com/features/employee-motivation |
| AI Document scanner | https://www.cakeequity.com/features/ai-document-scanner |
| Capital Raise | https://www.cakeequity.com/features/capital-raise |
| SAFEs | https://www.cakeequity.com/features/safe |
| Convertible Notes | https://www.cakeequity.com/features/convertible-notes |
| Investor Relations | https://www.cakeequity.com/features/investor-relations |
| Data Room | https://www.cakeequity.com/features/data-room |
| Compliance | https://www.cakeequity.com/features/compliance |
| 409A Valuation | https://www.cakeequity.com/features/409a |
| QSBS | https://www.cakeequity.com/features/qsbs |
| ASC 718 | https://www.cakeequity.com/features/asc-718 |
| 83(b) Election | https://www.cakeequity.com/features/83b |
| Form 3921 | https://www.cakeequity.com/features/form-3921 |
| Rule 701 | https://www.cakeequity.com/features/rule-701 |
| Migrate from Pulley | https://www.cakeequity.com/migrate-from-pulley |
| Switch to Cake | https://www.cakeequity.com/switch |
| Product Tour | https://www.cakeequity.com/product-tour |
| Help Center | https://help.cakeequity.com/ |

## Solutions menu

| Label | Opens |
|---|---|
| Founders & CEOs | https://www.cakeequity.com/use-cases/founders |
| Finance & CFOs | https://www.cakeequity.com/use-cases/finance |
| People & HR | https://www.cakeequity.com/use-cases/hr |
| Law Firms | https://www.cakeequity.com/use-cases/law-firms |
| Investors | https://www.cakeequity.com/use-cases/investors |
| YC Founders | https://www.cakeequity.com/ycombinator |
| Startups | https://www.cakeequity.com/stage/startups |
| Growing Teams | https://www.cakeequity.com/stage/teams |
| Scaleups | https://www.cakeequity.com/stage/scaleups |
| Help Center | https://help.cakeequity.com/ |

The sitemap also has https://www.cakeequity.com/use-cases/ceo and https://www.cakeequity.com/use-cases/legal. They are not in this menu.

## Resources menu

| Label | Opens |
|---|---|
| Blog | https://www.cakeequity.com/blog |
| Guides | https://www.cakeequity.com/guides |
| Templates | https://www.cakeequity.com/templates |
| Tools | https://www.cakeequity.com/tools |
| Changelog | https://www.cakeequity.com/changelog |
| Cake love | https://www.cakeequity.com/customer-love |
| Customer stories | https://www.cakeequity.com/stories |
| Events | https://www.cakeequity.com/events |
| About Us | https://www.cakeequity.com/about |
| Legal Hub | https://www.cakeequity.com/legal |
| Cake vs. Carta | https://www.cakeequity.com/cake-vs-carta |
| Cake vs. Spreadsheet | https://www.cakeequity.com/cake-vs-spreadsheet |
| Migrate from Pulley | https://www.cakeequity.com/migrate-from-pulley |
| Help Center | https://help.cakeequity.com/ |

## Homepage controls

| Control | Opens |
|---|---|
| Pulley chip, How managed migration works | Same page, anchor `#managed-migrations` |
| Get started | https://app.cakeequity.com/setup_company . Branch stops. |
| Book a demo | https://www.cakeequity.com/book-sales-demo |
| G2 rating cluster | https://www.g2.com/products/cake-equity/reviews |
| Watch how it works (53s) | In-page video dialog. Play, Mute, CC, close. |
| Founder, Employee, Investor, Law firm tabs | In-page tab panes. They do not navigate. |
| Logo row | Decorative. Two story quotes link to https://www.cakeequity.com/stories/whimsical and https://www.cakeequity.com/stories/tracksuit. |
| Testimonial previous, next, dots | In-page slider. Six slides. |
| FAQ cards | In-page expand. |
| Cake AI Assistant | In-page Chatbase panel. See Chat overlay. |

## Chat overlay

Button label: Open Cake AI Assistant. Hosted at chatbase.co. No message was typed.

| Control | Opens |
|---|---|
| Close | Closes the panel |
| Open menu | Panel menu. Not followed past the open state. |
| Migrate from Pulley | Sends that prompt inside the panel. Not clicked. |
| Learn more about Cake | Sends that prompt inside the panel. Not clicked. |
| Investor or Employee logging in | Sends that prompt inside the panel. Not clicked. Login was not opened from here. |
| Pricing | Sends that prompt. A follow-up offers How much is a 409a?, What Cake plan do I need?, I have a quote from another provider. No message was typed. |
| Add attachments | File picker. Not used. |
| Start dictation | Microphone. Not used. |
| Start voice mode | Voice. Not used. |
| Powered by Chatbase | https://www.chatbase.co/ in a new tab. Not opened. |

## Footer

Shared on marketing pages.

| Column | Control | Opens |
|---|---|---|
| Brand | LinkedIn | https://www.linkedin.com/company/cake-equity/ |
| Brand | X | https://twitter.com/CakeEquity |
| Brand | Instagram | https://www.instagram.com/cakeequity/ |
| Brand | Reddit | https://www.reddit.com/r/CakeEquity/ |
| About | About Cake | https://www.cakeequity.com/about |
| About | Customer Stories | https://www.cakeequity.com/stories |
| About | Become a Partner | https://www.cakeequity.com/partners |
| About | Legal & Privacy Hub | https://www.cakeequity.com/legal |
| About | Trust Center | https://trust.cakeequity.com/ |
| About | Help Center | https://help.cakeequity.com/ |
| Product | Cap table | https://www.cakeequity.com/features/cap-table |
| Product | Equity incentives | https://www.cakeequity.com/features/equity-incentives |
| Product | Stock options | https://www.cakeequity.com/features/stock-options |
| Product | Capital raise | https://www.cakeequity.com/features/capital-raise |
| Product | 409A valuation | https://www.cakeequity.com/features/409a |
| Product | Employee motivation | https://www.cakeequity.com/features/employee-motivation |
| Product | Equity benchmarking | https://www.cakeequity.com/features/equity-benchmarking |
| Product | Cake Intelligence | https://www.cakeequity.com/cake-intelligence |
| Product | Cake MCP | https://www.cakeequity.com/features/mcp |
| Learn | Blog | https://www.cakeequity.com/blog |
| Learn | Guides | https://www.cakeequity.com/guides |
| Learn | Events | https://www.cakeequity.com/events |
| Learn | Changelog | https://www.cakeequity.com/changelog |
| Learn | Cake Momentum | https://www.cakeequity.com/cake-momentum |
| Learn | Cake vs Carta | https://www.cakeequity.com/cake-vs-carta |
| Learn | Cake vs Pulley | https://www.cakeequity.com/cake-vs-pulley |
| Learn | Migrate from Pulley | https://www.cakeequity.com/migrate-from-pulley |
| Resources | Employee stock options | https://www.cakeequity.com/guides/employee-stock-options |
| Resources | Equity grants for startups | https://www.cakeequity.com/guides/equity-grant |
| Resources | Startup stock options | https://www.cakeequity.com/guides/startup-stock-options |
| Resources | 409A valuation | https://www.cakeequity.com/guides/409a-valuation |
| Resources | QSBS | https://www.cakeequity.com/guides/qsbs |
| Legal row | Privacy Policy | https://www.cakeequity.com/privacy |
| Legal row | Security | https://www.cakeequity.com/security |
| Legal row | Legal Hub | https://www.cakeequity.com/legal |
| Badges | BSI, NASPP, Open Cap Table Coalition | External badge links in the footer art. Not followed. |

The footer prints a street address. It is public marketing copy. It is not copied into this file.

## Page templates

Each row is one template. Collection items use the same chrome and the same kind of controls as the index.

| Template | URL | Controls beyond the chrome |
|---|---|---|
| Home | https://www.cakeequity.com/ | See Homepage controls. |
| Feature | https://www.cakeequity.com/features/cap-table and 25 sibling feature URLs | Get started and Book a demo, same walls as the header. FAQ expand. |
| Use case | https://www.cakeequity.com/use-cases/founders and finance, hr, law-firms, investors, ceo, legal | Same CTA pair. |
| Stage | https://www.cakeequity.com/stage/startups, /stage/teams, /stage/scaleups | Same CTA pair. |
| Pricing | https://www.cakeequity.com/pricing | Country select. Stakeholder number. Plan checkboxes. Quote carousel (Quote 1 to Quote 5), in-page. Start free and Begin managed migration open https://app.cakeequity.com/setup_company . Branch stops. |
| Find your plan | https://www.cakeequity.com/find-your-plan | Shareholders and Employees number fields. Start over. Not submitted. |
| Get a quote | https://www.cakeequity.com/get-a-quote | Name and email fields, submit. Not filled. Not submitted. |
| Book a demo | https://www.cakeequity.com/book-sales-demo | HubSpot meetings iframe. Not filled. |
| Demo request | https://www.cakeequity.com/demo-request | HubSpot form iframe. A sales mailto is on the page. Not filled. |
| Checkout | https://www.cakeequity.com/checkout | Address fields, country select, shipping radio, Pay with browser, Place Order. Not filled. Not submitted. Branch stops at the purchase control. |
| Search | https://www.cakeequity.com/search | Search field, placeholder Search Cake. Not submitted. |
| Blog index | https://www.cakeequity.com/blog | Cards open `/blog/<slug>`. 45 posts in the sitemap. |
| Guides index | https://www.cakeequity.com/guides | Cards open `/guides/<slug>`. 115 guides in the sitemap. |
| Stories index | https://www.cakeequity.com/stories | Read story opens `/stories/<slug>`. 14 stories in the sitemap. |
| Templates | https://www.cakeequity.com/templates | Cards open template pages such as `/templates/safe-note-agreement`. |
| Tools | https://www.cakeequity.com/tools | Cards open calculators and checklists under `/tools/`. Not submitted. |
| Changelog | https://www.cakeequity.com/changelog | Cards open `/changelog/<slug>`. 53 notes in the sitemap. |
| Events | https://www.cakeequity.com/events | Cards open `/events/<slug>`. 83 events in the sitemap. |
| Product tour | https://www.cakeequity.com/product-tour | Six Loom embeds. Play stays in the embed. |
| Compare | https://www.cakeequity.com/cake-vs-carta, cake-vs-pulley, cake-vs-spreadsheet, cake-vs-carta-vs-pulley | Same CTA pair. |
| Switch / migrate | https://www.cakeequity.com/switch, /migrate-from-pulley, /pulley-migration, /ycombinator | Get started opens company setup. Branch stops. |
| About | https://www.cakeequity.com/about | Staff links such as `/jason-atkins` and `/kim-hansen`. |
| Partners | https://www.cakeequity.com/partners | Become a partner. `/partner/<slug>` is disallowed in robots.txt and was not opened. Marketplace cards live under `/partner-marketplace/`. |
| Legal hub | https://www.cakeequity.com/legal | Links to privacy, terms, security, platform terms. |
| Privacy | https://www.cakeequity.com/privacy | Long text. No form. |
| Terms | https://www.cakeequity.com/terms | Long text. |
| Security | https://www.cakeequity.com/security | Trust copy. Trust Center is a separate host. |
| Glossary | https://www.cakeequity.com/glossary | In-page term list. |
| Equity toolkit | https://www.cakeequity.com/equity-toolkit | Cards open toolkit pages. |
| Podcasts | https://www.cakeequity.com/podcasts | Episode cards under `/podcasts/`. |
| Customer love | https://www.cakeequity.com/customer-love | Quote cards. |
| Cake Intelligence | https://www.cakeequity.com/cake-intelligence | Same CTA pair. |
| Cake Momentum | https://www.cakeequity.com/cake-momentum | Same CTA pair. |
| Office hours | https://www.cakeequity.com/office-hours | Booking. Not filled. |
| Resources | https://www.cakeequity.com/resources | Same layout as Guides. |
| Learn | https://www.cakeequity.com/learn | 404. |
| Careers | https://www.cakeequity.com/careers | No heading was painted. |
| Success pages | `/book-demo-success`, `/quote-request-success`, `/409a-request-success`, `/order-confirmation` | Confirmation templates. Not reached, because no form was submitted. |

## Walls, not opened past the URL

| Control | URL | Stop |
|---|---|---|
| Login | https://app.cakeequity.com/login | Empty email wall. See [login-review.json](login-review.json). |
| Get started, Get started free, Start free, Begin managed migration | https://app.cakeequity.com/setup_company | Company setup. Not opened. |
| Create one | Register step on the auth host | Not clicked. |
| Continue with Google | Identity provider | Not clicked. |
| Continue with LinkedIn | Identity provider | Not clicked. |
| Place Order, Pay with browser | https://www.cakeequity.com/checkout | Not clicked. |
