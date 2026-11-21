# Boords public site tree

Mapped from https://boords.com/ on 2026-11-21, signed out, in headless Chromium. The product host is https://app.boords.com. Login and signup on www return the public 404. The app login page asks for email and password, or Google. No email was typed. No password was typed. No form was submitted. No SSO button was clicked. A control that opens that wall is recorded and that branch stops.

Sitemap: https://boords.com/sitemap.xml (286 URLs). `robots.txt` also names https://boords.com/image-sitemap.xml and disallows `/soundbites/*`, `/offer`, `/for/*`, and `/api/og`. PDF downloads on `downloads.boords.com` are files, not pages, so they are listed and not photographed.

## Shell

| Control | Opens | Stop? |
|---|---|---|
| Wordmark | `/` | |
| Features (desktop hover, `aria-haspopup`) | Features menu | |
| Resources (desktop hover, `aria-haspopup`) | Resources menu | |
| Success Stories | `/customers` | |
| Pricing | `/pricing` | |
| Book a demo | `/demo?from=header` | |
| Log in | `https://app.boords.com/login` | yes, login wall |
| Try Boords Free | `https://app.boords.com/signup` | yes, signup wall |
| Open menu (phone, `aria-label`) | Mobile drawer | |
| Accept & Close | Cookie card | hidden, never clicked |

## Features menu

Hover opens it. Click toggles it closed. Escape closes it. Phone: Open menu, then Features, opens a nested list with Back.

| Item | Opens | Stop? |
|---|---|---|
| Scripts | `/script-editor` | |
| Storyboards | `/storyboard-software` | |
| Animatics | `/animatic-software` | |
| Feedback & Approvals | `/collaborate` | |
| Shot Lists | `/shot-list-software` | |
| Boords Agent | `/agent` | |
| Claude | `/integrations/claude` | |
| ChatGPT | `/integrations/chatgpt` | |
| Slack | `/integrations/slack` | |
| API and webhooks | `/integrations/api` | |
| Exports | `/integrations/exports` | |
| All integrations & exports | `/integrations` | |
| Phone only: Storyboard Generator | `/ai-storyboard-generator` | |
| Phone only: Back | Closes the nested list | |

Phone Resources (opened from the drawer, photographed) lists Changelog, Storyboard Templates, Filmmaking Templates, Storyboarding 101, Animatics 101, Blog. That list is shorter than the desktop Resources menu.

## Resources menu

| Item | Opens |
|---|---|
| Learn Boords | `/learn` |
| Documentation | `/docs` |
| Changelog | `/changelog` |
| Blog | `/blog` |
| Storyboard Templates | `/storyboard-template` |
| Video Script Template | `/video-script-template` |

## Mobile drawer

Open menu opens the drawer. Close menu closes it. Features and Resources are nested lists.

| Item | Opens | Stop? |
|---|---|---|
| Try Boords Free | `https://app.boords.com/signup` | yes |
| Log in | `https://app.boords.com/login` | yes |
| Book a demo | `/demo?from=header_mobile` | |
| Success Stories | `/customers` | |
| Pricing | `/pricing` | |

## Home interactions

These stay on `/`. None submits a form.

| Control | Opens |
|---|---|
| Connect your AI | In-page section toward `/mcp` |
| Watch the 34s overview | Video overlay on the home demo |
| Script / Storyboard / Review | Demo stage tabs |
| Client view / Team view | Review demo panes |
| Cast / Refine | Frame demo panes |
| Animatic / Edit | Export demo panes |
| Pause demo | Pauses the running demo |
| Ask ChatGPT / Ask Perplexity / Ask Claude | External chat sites. Not followed |
| Customer story cards | `/customers/mobula`, `/customers/the-3rd-eye`, `/customers/silver` |

## Pricing

| Control | Opens |
|---|---|
| Monthly / Yearly tabs | Local price toggle. Yearly reads "Save 33%" |
| Comparison rows (Custom frame fields, and the rows under it) | Expand a row in place |
| Plan CTAs | `https://app.boords.com/signup` or `/demo` or `/enterprise` |

## Demo

`/demo` is a public booking page. Date radios, time radios, and a timezone combobox are visible. The booking form was not filled and not submitted. Accordions: "Who will I talk to?", "Do I need to prepare anything?".

## Docs

`/docs` and `/docs/<slug>` share a sidebar. Theme radios Light and Dark set `html.dark`. That is the only dark theme on the public site. Sidebar groups (Getting Started, Images, Storyboards, Scripts, Comments & sharing, Exports, Team & workspace, Account, Developers) expand in place. Contact support is a sidebar control, not followed into a form submit. Article pages link the Learn videos.

Photographed: index, one article (`/docs/quick-start`) in light and dark, phone index, phone article drawer.

## Script timer

`/script-timer` is a public calculator. Textarea, Slow / Normal / Fast pace buttons, three checkboxes, FAQ accordions. Sample text was typed and not submitted.

## Customers

`/customers` filter buttons: Everyone, Founders, Producers, Creatives. They filter the story cards in place. Story pages: `/customers/mobula`, `/customers/the-3rd-eye`, `/customers/silver`, `/customers/demoflick`, `/customers/lemonly`.

## Other public pages photographed

Product: `/script-editor`, `/storyboard-software`, `/animatic-software`, `/shot-list-software`, `/collaborate`, `/agent`, `/ai-storyboard-generator`, `/ai-script-generator`, `/mcp`, `/integrations`, `/enterprise`.

Tools and templates: `/script-timer`, `/video-script-template`, `/storyboard-template`, `/shot-list-template`, `/call-sheet-template`.

Company and legal: `/about`, `/security`, `/privacy`, `/terms`, `/page/terms-of-service`, `/changelog`, `/newsletter`, `/blog`, `/learn`, `/compare`, `/pre-production-software`.

Index pages for long content trees: `/blog`, `/learn`, `/docs`, `/how-to-storyboard`, `/storytelling`, `/filmmaking-templates`, `/storyboard-examples`, `/best-storyboard-software`, `/best-scriptwriting-software`. One sample child of each long tree is photographed. The rest of the sitemap children are the same template.

www `/login` and www `/signup` are the public 404. Photographed once as the dead branch.

## Login wall (branch stop)

| Control | URL | What it asks | Action |
|---|---|---|---|
| Log in | `https://app.boords.com/login` | Email, password, Keep me signed in, or Google. Also Sign up here and Forgot password? | Recorded. Not typed. Not submitted. Google not clicked |
| Try Boords Free | `https://app.boords.com/signup` | Signup wall | Not opened past the URL. Not filled |
| Newsletter Subscribe | `/newsletter`, `/blog` | Email field | Not filled. Not submitted |
| Enterprise Send | `/enterprise` | Name, email, company, team size | Not filled. Not submitted |

## Not a page

| Thing | Why |
|---|---|
| `downloads.boords.com/templates/*.pdf` | File downloads linked from the sitemap |
| `/soundbites/*`, `/offer`, `/for/*` | Disallowed in robots.txt. Not linked from the home tree |
| Signed-in app (boards, scripts, billing, team) | Behind the login wall |
