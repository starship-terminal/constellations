# Lemni patterns

How the pages combine the controls in [components.md](components.md). Public marketing and the signed-in free product, 2026-11-18, 1440 and 390.

## Marketing shell

A 50 px bar (64 px on the phone) sits over the page. Home paints it as a 40% wash of `#0d0d12`. Every other marketing page paints the bar the same `#f6f6f8` as the page. Links are Docs, Blog, Company, Community, Pricing, then Continue. Continue leaves the marketing host for `https://lemni.com/signup`, which redirects to the sign-in shell.

![Home](screenshots/home-dark-default.png)

On the phone the same links open as a full-screen dark list with a close control. The list was opened. Continue was not followed.

![Phone menu](screenshots/mobile-home-dark-menu-open.png)

The bottom of each marketing page is a link band, not a `<footer>` element: Home, Docs, Changelog, Pricing, Company, Blog, Community, Support, Brand, Privacy, Terms, and the social links.

![Home full](screenshots/home-dark-full.png)

## Dark hero

Home is the only dark page. The headline is `core.typography.display` in `#e3e8ff`. Under it, a glass black Continue pill and a glass Watch video pill. A violet decorative chip (`core.color.accent.violet`) appears in the art. It is not the button colour. Twelve elements run a 1 s `dots` transform loop. The loop does not stop under reduced motion.

![Home hero](screenshots/home-dark-default.png)

## Light inner page

Pricing, docs, blog, company, brand, changelog, support and privacy share one light ground (`light.background.page`). Headlines use TWK Lausanne 250 in black. Body and nav use the muted greys. There is no theme toggle. `prefers-color-scheme` does not flip these pages.

![Pricing](screenshots/pricing-light-default.png)

![Company](screenshots/company-light-default.png)

## Pricing

One plan column: a white card, a 46 px figure, a struck comparison in `#cacacd`, and a 340 × 40 black pill labelled Try For Free. The pill goes to sign-up. There is no public checkout form. Phone pricing stacks the same card.

![Pricing phone](screenshots/mobile-pricing-light-default.png)

## Docs

Public documentation, not the signed-in product. A horizontal section row (Basics, Knowledge, Agents, Actions, Inbox) and a left list of page names (Overview, Workplace, Members, Connections, Usage, Plans). The current section is black with a hairline. Side links are 13 px muted until hover.

![Docs](screenshots/docs-light-default.png)

![Docs phone](screenshots/mobile-docs-light-default.png)

`/docs/agents`, `/docs/knowledge`, `/docs/actions` and `/docs/inbox` are the same template. Only `/docs` was screenshotted.

## Sign-in boundary

`https://lemni.com/signin` (reached from `/signup`, `/login`, nav Continue and Try For Free) is a separate React shell on the apex host. Light ground, system-ui, a 32 px title, a Google button, an email field, and a black Continue bar at 12 px radius. Continue with Google was not used. Email Continue sends a magic link.

![Sign-in](screenshots/signin-light-default.png)

![Sign-in phone](screenshots/mobile-signin-light-default.png)

## Onboarding

After the magic link, `/welcome` asks for first and last name, `/welcome/space` creates a workplace, `/welcome/subscribe` is a paid plan, `/welcome/tutorial` is a video with Skip Tutorial. The plan page was captured. Upgrade was not pressed. Skip Tutorial opens the free workplace.

![Subscribe](screenshots/app-subscribe-light-default.png)

![Tutorial](screenshots/app-tutorial-light-default.png)

## Workplace shell

A 260 px `#f1f3f4` sidebar (Inbox, Assigned, Agents, Knowledge, Behavior, Actions, Settings), a free-trial Upgrade card, Tutorials and Docs tiles. The product is light-only. Phone inbox shows the thread list; the hamburger opens the same nav. Agents on a 390-wide viewport shows "Please use Lemni on desktop."

![Inbox](screenshots/app-inbox-light-default.png)

![Phone nav](screenshots/mobile-app-inbox-light-nav-open.png)

![Phone desktop gate](screenshots/mobile-app-agents-light-default.png)

## Agent builder

Stock agents (Webshop Support and four others) sit Disabled. The right column lists Enabled and Suggested actions. Enable Agent was not pressed. The centre pane can sit on a spinner while the agent body loads.

![Agents](screenshots/app-agents-light-default.png)

## Knowledge

Datasets (General, Gmail, Shopify, Stripe, Hubspot) and an empty drop zone. Add Webpage and Upload File were not used.

![Knowledge](screenshots/app-knowledge-light-default.png)

## Actions store

A searchable grid of action cards plus a Code actions Create control. Create and Install were not pressed.

![Actions](screenshots/app-actions-light-default.png)

## Empty inbox

No threads todo, Filter and Sort at rest, and a four-step setup list. Invite and Add Webpages And Files were not pressed. A Reconnecting toast can sit over the page on this client.

## Workplace settings

`?workspaceSettings=members` opens a dialog on a white 80% overlay: Members, Details, Connections, Usage, Plan, About. The members list shows the owner. Invite was not sent. `?settings=profile` opens Account (name, email, avatar). Fields were not edited.

![Members](screenshots/app-workspace-settings-light-default.png)

![Account](screenshots/app-profile-light-default.png)

## What is not a pattern here

Error and destructive confirm were not shown. The application form at `/company/apply` was not submitted. `community.lemni.com` returned an empty body. Checkout behind Upgrade was not opened.
