# Digg public site tree

Mapped signed out from [https://digg.com/](https://digg.com/) on 2026-11-21 with Playwright. The cookie notice (`section.cookie-notice`) was hidden with CSS. Its buttons were not clicked, except **Cookie preferences** on `/about`, which opens the preferences dialog and does not submit a choice.

A control that opens a login or signup wall stops that branch. Google and X were not clicked.

## Shell

| Control | Opens |
|---|---|
| Wordmark (`aria-label` digg home) | [https://digg.com/](https://digg.com/) |
| Sidebar **Home** | [https://digg.com/](https://digg.com/) |
| Sidebar **Technology** | [https://digg.com/tech](https://digg.com/tech) |
| Sidebar **Gaming** | [https://digg.com/gaming](https://digg.com/gaming) |
| Sidebar **Entertainment** | [https://digg.com/entertainment](https://digg.com/entertainment) |
| Sidebar **World & Business** | [https://digg.com/world-business](https://digg.com/world-business) |
| Sidebar **Science** | [https://digg.com/science](https://digg.com/science) |
| Sidebar **Sports** | [https://digg.com/sports](https://digg.com/sports) |
| Sidebar **AI** | [https://digg.com/ai](https://digg.com/ai) |
| **System** / **Light** / **Dark** (`aria-label` ends in Switch theme) | Cycles the theme on `<html>`: Light, Dark, System. It is a button, not a menu. |
| **Log in** | [https://digg.com/login?redirect_url=%2F](https://digg.com/login?redirect_url=%2F). Wall. Stop. |
| **Sign up** | [https://digg.com/sign-up?redirect_url=%2F](https://digg.com/sign-up?redirect_url=%2F). Wall. Stop. |
| **Toggle Sidebar** | Folds and expands the desktop sidebar. No new URL. |
| **Trending** (`aria-label` Feed View) | Listbox: Trending, Best, Hot, Newest, Top. Same page, different sort. |
| **Compact** (`aria-label` Feed display: Compact) | Listbox: Comfy, Compact. Same page, different card density. |
| Phone **Open navigation menu** | Sheet with the same sidebar links, the theme cycle, Log in and Sign up. |
| Footer **About** | [https://digg.com/about](https://digg.com/about) |
| Footer **Contact** | [https://digg.com/contact](https://digg.com/contact). Address links are hidden in the screenshots and are not written in this package. |
| Footer **Privacy Policy** | [https://digg.com/privacy](https://digg.com/privacy) |
| Footer **Terms of Service** | [https://digg.com/tos](https://digg.com/tos) |
| Footer **Community Guidelines** | [https://digg.com/community-guidelines](https://digg.com/community-guidelines) |
| Footer **Cookie preferences** | Cookie preferences dialog. Switches and Save preferences were not used. |

## Feed

Each topic feed uses the same shell. A story title opens `/<topic>/<id>`. A source avatar opens `/u/<handle>`. **N Sources** jumps to `#source-posts` on that story. A comment count links to `#comments` or `#add-comment`. A sponsored card links to `/api/internal/sponsor-delivery/<id>/click`, an outbound ad click, and was not followed.

| Page | URL |
|---|---|
| Home | [https://digg.com/](https://digg.com/) |
| Technology | [https://digg.com/tech](https://digg.com/tech) |
| Gaming | [https://digg.com/gaming](https://digg.com/gaming) |
| Entertainment | [https://digg.com/entertainment](https://digg.com/entertainment) |
| World & Business | [https://digg.com/world-business](https://digg.com/world-business) |
| Science | [https://digg.com/science](https://digg.com/science) |
| Sports | [https://digg.com/sports](https://digg.com/sports) |
| AI | [https://digg.com/ai](https://digg.com/ai) |

Story ids change with the feed. One public story was opened: [https://digg.com/ai/f7vysbah](https://digg.com/ai/f7vysbah). One public profile was opened: [https://digg.com/u/justinmezzell](https://digg.com/u/justinmezzell).

## Story

| Control | Opens |
|---|---|
| **Back to feed** | The topic feed (`/ai` on the captured story) |
| Topic chip | The topic feed |
| **digg it** | Not followed. Treating a vote as an action that needs an account. |
| Source avatars | `/u/<handle>` |
| **N Sources** | `#source-posts` on the same story |
| Related story links | Other public story URLs |
| External source posts | `https://x.com/...` on the captured story. Not opened. |

`#comments` on the captured story stayed on the story URL and did not open a dialog.

## Profile

| Control | Opens |
|---|---|
| **Follow** | [https://digg.com/login?redirect_url=%2Fu%2Fjustinmezzell](https://digg.com/login?redirect_url=%2Fu%2Fjustinmezzell). Wall. Stop. |
| Follower and following counts | Buttons on the profile. Not opened, because they sit next to account actions. |
| **Show more** | Expands the public bio. Not photographed as its own state. |

## Login and signup walls

[https://digg.com/login](https://digg.com/login) asks for an email (`name=identifier`) and, on the first paint of this capture, showed email only until the password field is in the form. The probe of the same URL listed email and password together, plus **Continue with Google** and **Continue with X / Twitter**. The photographed login page showed email and Continue, with the password field not in that paint. Signup at [https://digg.com/sign-up](https://digg.com/sign-up) shows email, password, Google and X. No field was filled. Google and X were not clicked. Continue was not clicked. No code was sent.

## Other public URLs

| URL | What it is |
|---|---|
| [https://digg.com/llms.txt](https://digg.com/llms.txt) | `text/plain`, linked from About and Contact. Not a visual page. |
| [https://digg.com/this-page-does-not-exist-capture](https://digg.com/this-page-does-not-exist-capture) | 404 page: "404 · PAGE NOT FOUND". |
| `https://x.com/basic_in_` | External link on About and Contact. Not opened. |

## Not present on the public surface

No search field. No tooltip, toast, table, checkbox, radio, text area, or tabs in the checklist sense. The cookie dialog has two switches. Select is the feed view and feed display listboxes.
