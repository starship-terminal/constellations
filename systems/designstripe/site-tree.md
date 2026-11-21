# Visual (designstripe) public site tree

Mapped on 2026-11-21 from the homepage, signed out, in headless Chromium. `https://designstripe.com/` returns 200 and lands on `https://visual.app/`. The product paints one light theme. A `.dark` class is declared in CSS and no control switches it.

Nothing was typed. No identity provider was clicked. No form was submitted.

## Homepage

The page is `https://visual.app/`. The hero heading is "Design Agents for Revenue Teams".

| Control | What it does |
|---|---|
| VISUAL (wordmark) | Goes to `/` |
| WHY VISUAL? | Goes to `/about` |
| ASSETS | Goes to `/assets` |
| TOOLS | Goes to `/tools` |
| BLOG | Goes to `/blog` |
| WAITLIST | Opens a dialog on the same URL. Stops here. |
| JOIN WAITLIST | Opens the same dialog |
| LEARN MORE | Goes to `/about` |
| LEARN MORE ABOUT WHAT WE'RE BUILDING | Goes to `/about` |
| Feature accordion rows | Stay on `/` and expand a panel. The first row is open at rest. |
| PRODUCT / OVERVIEW, DESIGN AGENTS, BRAND-LOCK, INTEGRATIONS, TEMPLATES, VISION | In-page labels. They are `span` elements with `role="link"` and no `href`. Clicking one does not change the URL or the scroll position. |
| Blog cards | Go to `/blog/<slug>` |
| Footer ASSET LIBRARY, DESIGN TOOLS, ABOUT, CONTACT | Go to `/assets`, `/tools`, `/about`, `/contact` |
| Footer LINKEDIN | Leaves the site for `https://www.linkedin.com/company/visualapp`. Not followed. |
| Footer PRIVACY | Goes to `/privacy`, which paints "Privacy page not found" |

On a 390px viewport the same links sit behind a header button. That button opens a menu: HOME, WHY VISUAL?, ASSETS, TOOLS, BLOG, and JOIN WAITLIST. JOIN WAITLIST in the menu opens the same dialog.

## Pages the homepage reaches

| Page | Opens from | What is on it |
|---|---|---|
| `/about` | WHY VISUAL?, LEARN MORE | "Why Visual?" copy. A Join waitlist button opens the same dialog. |
| `/assets` | ASSETS | Asset Library. Kind links and category tiles. |
| `/assets/avatars` | Avatars | Five set tiles: Replicants, Creatives, Classic, Corporate, Zoomers. |
| `/assets/avatars/replicants` | / REPLICANTS | A public avatar grid. Item links go to `/assets/avatars/<set>/<slug>`. Not followed into a download. |
| `/assets/illustrations` | Illustrations | Same tile pattern as avatars. |
| `/tools` | TOOLS | Design Tools index. |
| `/colors/color-wheel` | Color Wheel card | A public colour tool: wheel, hex field, Analogous select, Export. Export was not pressed. |
| `/colors/color-picker`, `/colors/image-color-picker`, `/colors/gradient-generator` | Tool cards | Same public tool family. Not each photographed. |
| `/images/image-resizer`, `/images/image-cropper`, `/images/image-mirror`, `/images/image-rotator` | Tool cards | Same public tool family. Not each photographed. |
| `/blog` | BLOG | Alpha Channel index. SHOW MORE reveals more posts and stays on the page. |
| `/blog/<slug>` | A post card | A public article. One article photographed: `/blog/branding-consistency`. |
| `/contact` | CONTACT | "Contact" copy. No form. |
| `/privacy` | PRIVACY | 404 chrome: "Privacy page not found". |

## Waitlist wall

WAITLIST, JOIN WAITLIST, and Join waitlist all open one dialog at `https://visual.app/`. It asks for:

- First name
- Work email
- Company name
- Company size (1-10, 11-50, 51-200, 201-500, 501-1000, 1001+)

A hidden `fullname` input sits in the dialog with autocomplete off. The submit button reads "Join waitlist". No Google, Apple, or other identity provider is offered. The branch stops at this dialog. Nothing was typed and the button was not pressed.

There is no separate login page. `/login`, `/signin`, `/signup`, `/sign-in`, `/dashboard`, `/waitlist`, and `/agents` return the site 404. `/app` redirects to `/designstripe`, a public "Designstripe is now Visual" page, and does not open an account.

## Not entered

Design agents, account downloads, and every screen after the waitlist stay behind that dialog. Dark theme has no switch on the public site.
