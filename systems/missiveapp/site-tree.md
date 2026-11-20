# Missive public site tree

Mapped from https://missiveapp.com/ on 2026-11-21 in headless Chromium before any screenshot pass. The homepage returned HTTP 200. The product app at https://mail.missiveapp.com/#login is a login wall and that branch stops there.

The marketing site is Webflow. English is the default. `/fr` and `/fr/...` are the French copies of the same templates. The published sitemap lists 1,234 URLs (630 English, 605 French). Versioned changelog posts, blog posts, customer stories, integration pages and partner pages share a handful of templates. This capture walks one of each template, plus the nav, menus and dialogs those templates open. It does not walk every blog post.

## Login wall (stop)

| Control | Opens | What it asks | Action |
|---|---|---|---|
| Nav "Log in" | https://mail.missiveapp.com/#login | Work email, password, Continue with Google, Continue with Apple, Single sign-on (SSO), Forgot your password, Create an account | Recorded. Not entered. |
| "Try for free", "Sign up", "Create an account" | https://mail.missiveapp.com/#signup | Same host, signup hash | Recorded. Not entered. |
| Download page Mac / Windows installers | https://mail.missiveapp.com/download/mac and `/download/win`, plus `downloads.missiveapp.com` binaries | App download, not a public page | Recorded. Not opened. |

Observed login copy, not submitted: "Log in to Missive", "Continue with Google", "Continue with Apple", "Single sign-on (SSO)", work email, password.

## Consent overlay (hidden, never submitted)

A Ketch banner (`#ketch-banner`) paints over the first view: "Your Privacy Choices" and an "I understand" button. The capture hides `#ketch-banner` and `#lanyard_root` with CSS. It does not click "I understand". The banner is not a product component.

## Desktop nav (1440)

The desktop bar is `.navbar.w-nav` (not `.mobile-only`).

| Control | Opens |
|---|---|
| Logo | `/` |
| Product (dropdown, `data-hover="true"`) | Mega menu, not a new page. Links below. |
| Pricing | `/pricing` |
| Customers | `/customers` |
| Resources (dropdown) | Menu, not a new page. Links below. |
| Log in | Login wall. Stop. |
| Book a demo | https://calendly.com/ali-eslami-missiveapp/missive-the-team-inbox-public-demo-and-q-a (external). Not captured. |
| Try for free | Login wall (`#signup`). Stop. |
| English (footer and some pages) | Language menu: English `/`, Français `/fr` |

Product menu:

| Label | Opens |
|---|---|
| Collaborate | `/collaborate` |
| Coordinate | `/coordinate` |
| Connect | `/connect` |
| All features | `/features` |
| Integrations | `/integrations` |
| AI assistant | `/ai-assistant` |
| Changelog | `/changelog` |
| Accounting | `/solutions/accounting` |
| Law | `/solutions/law` |
| Real estate | `/solutions/real-estate` |
| Logistics | `/solutions/transportation-logistics` |

The Product menu does not list E-commerce or Travel. Those two solution pages are in the footer.

Resources menu:

| Label | Opens |
|---|---|
| Help | `/docs` |
| Download | `/download` |
| Blog | `/blog` |
| Video card | https://youtu.be/CQM_p9k6eQ8 (external). Not captured. |

## Home interactions (same URL)

| Control | Opens |
|---|---|
| Watch demo | `.lightbox.is-demo` on `/`. Title "Missive Demo: What is a collaborative inbox?". A Try for Free link inside it goes to the signup wall and is not followed. |
| Read Story on the hero video | `#videoModalWrapper` (`.lightbox.is-dynamic`), a customer-story lightbox. The static "Read Story" links further down go to `/customers/morning`, `/customers/wulfsfish`, `/customers/the-academy-school`. |
| Three feature tabs | In-page panes `#w-tabs-0-data-w-pane-0` (automations), pane 1 (integrations), pane 2 (workflow). No navigation. |
| 4.8 reviews chip | A review popover on the same page. |

## Phone nav (390)

`.navbar.mobile-only` hamburger (`.menu-mobile-toggle`) opens `.menu-mobile-list` over the page. Links: Log in and Sign up (login wall, stop), Pricing, Features, Integrations, Book a demo (Calendly, external), Download, Collaborate, Coordinate, Connect, Customers, Help center (`/docs`), Blog, four use-case pages, six solution pages.

## Footer (every marketing page)

| Group | Opens |
|---|---|
| Product | `/features`, `/pricing`, `/integrations`, `/templates/rules`, `/download` |
| Learn | `/docs`, `/changelog`, `/docs/developers`, `/blog`, `/about`, a mailto support link (address not recorded), https://status.missiveapp.com/ (other host, not captured) |
| Company | `/customers`, `/referral-program`, `/partners` |
| Pillars | `/collaborate`, `/coordinate`, `/connect` |
| Use cases | `/usecases/contracted-services`, `/professional-services`, `/sales`, `/support` |
| Solutions | `/solutions/accounting`, `/e-commerce`, `/law`, `/real-estate`, `/transportation-logistics`, `/travel` |
| Compare | `/compare/frontapp-vs-missive`, `/missive-vs-gmelius-alternative`, `/help-scout-vs-missive`, `/missive-helpwise-alternative`, `/missive-vs-hiver-alternative`, `/office-365-shared-mailbox`, `/shortwave-email-vs-missive`, `/slack-vs-email`, `/spark-mail-vs-missive`, `/best-superhuman-alternative` |
| Legal | `/privacy`, `/security`, `/terms` |
| Language | `/` and `/fr` |

A second Book a demo in the footer goes to https://calendly.com/luis-missive/missive-the-team-inbox (external).

## Page templates and what they open

| Template | Representative URL | Extra controls |
|---|---|---|
| Home | `/` | Demo lightbox, story lightbox, three tabs, review chip, nav menus |
| Pillar | `/collaborate`, `/coordinate`, `/connect` | Same nav. Marketing sections only. |
| Features index | `/features` | Nav, review chip |
| Feature detail | `/features/sms`, `/live-chat`, `/whatsapp`, `/messenger`, `/instagram`, `/custom-channels` | Same template. SMS is the representative. |
| Integrations index | `/integrations` | Cards open `/integrations/<slug>` |
| Integration detail | `/integrations/asana` (representative of ~40) | Same nav |
| AI | `/ai-assistant` | Same nav |
| Pricing | `/pricing` | Plan columns (Starter, Productive, Business), "View all plan features", FAQ accordions. Plan CTAs go to the signup wall and are not followed. |
| Customers index | `/customers` | Cards open `/customers/<slug>` |
| Customer story | `/customers/morning` (representative of ~50) | Same nav |
| Docs / help | `/docs` | A search field and an AI chat field. Neither is submitted. Article links under `/help/...` and `/docs/developers` share the docs chrome. |
| Download | `/download` | Store and installer links. Installer hosts are the login/download wall. |
| Blog index | `/blog` | Cards open `/blog/<slug>`. Categories are `/blog-category/<slug>`. |
| Blog post | `/blog/team-inbox-vs-shared-inbox` (representative of ~122) | Same nav |
| Changelog index | `/changelog` | Rows open `/changelog/<version>` (~341 posts) |
| Changelog post | `/changelog/10-64-1` (the version named on the download host) | Same nav |
| About | `/about` | Same nav |
| Referral | `/referral-program` | FAQ accordions. No form on the public page. |
| Partners index | `/partners` | Language filter ("All languages"), cards to `/partners/<slug>` |
| Partner detail | `/partners/blackgallina` (representative of 16) | Same nav |
| Rule templates | `/templates/rules` | Template cards, same nav |
| Use case | `/usecases/support` (representative of 4) | Same nav |
| Solution | `/solutions/travel` (the one missing from the Product menu) | Same nav |
| Compare | `/compare/frontapp-vs-missive` (representative of 10) | Same nav |
| Legal | `/privacy`, `/security`, `/terms`, `/gdpr` | Long text. Privacy is the representative. |
| Subprocessors | `/subprocessors/stripe` (representative of 13) | Legal-adjacent text page |
| French home | `/fr` | Same controls, French labels. One width only, to show the locale switch works. |

## Not present on the public site

No theme toggle. `color-scheme` is `normal` and `html` has no `data-theme`. Dark is not a painted theme.

No public checkbox, radio, switch, toast, table, or destructive confirmation. The docs search is a text field that is not submitted. Pricing FAQ and the referral FAQ are accordions. The mobile menu and the two nav dropdowns are the menus. The demo lightbox and the story lightbox are the dialogs.

## Theme and widths

One painted theme: light. Widths: desktop 1440×900 and phone 390×844.
