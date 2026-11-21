# Wikipedia public site tree

Mapped on 2026-11-22 from [https://en.wikipedia.org/wiki/Main_Page](https://en.wikipedia.org/wiki/Main_Page), signed out. Desktop shots are 1440 × 900 CSS pixels at 2× (PNG 2880 × 1800). Phone shots are 390 × 844 CSS pixels at 2× (PNG 780 × 1688). The page title is "Wikipedia, the free encyclopedia". The first visible heading is "Welcome to Wikipedia". This is the live English Wikipedia, Vector 2022 skin, not a parked domain.

Nothing was typed. No username, password, email, or search query was entered in a field. No form was submitted. No identity provider was clicked. No captcha was solved. No page was edited. `login-extracted` stays `not-started`.

origin/main did not have `systems/wikipedia/` when this branch was cut from `991cb07a0`, and it still did not have `systems/wikipedia/site-tree.md` when this package was written. This is a first capture. The slug is `wikipedia`.

The featured photograph of Carly Rae Jepsen, the garbage-bin photograph, and the Voyager rendering are public article illustrations. They are not a signed-in account.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Main menu (hamburger) | click | Unpinned dropdown. Navigation and Contribute. A "move to sidebar" control is in the menu. It was not clicked. |
| Wordmark | link | [/wiki/Main_Page](https://en.wikipedia.org/wiki/Main_Page) |
| Search box, empty, then Search | navigation by URL | [Special:Search](https://en.wikipedia.org/wiki/Special:Search). The header field was not typed in. |
| Create account | link | Central auth on auth.wikimedia.org, Special:CreateAccount. Photographed empty. |
| Log in | link | Central auth on auth.wikimedia.org, Special:UserLogin. Photographed empty. |
| Donate | link | donate.wikimedia.org. Not followed. |
| Tools (page toolbar) | click | Unpinned dropdown: General, Print/export, In other projects. |
| Appearance | already open | Pinned panel on the right. hide was not clicked. |
| 349 languages | click | Universal Language Selector panel (`.uls-rewrite`). Search languages was not typed. No language was clicked. |
| Phone menu | click | Same Navigation and Contribute list, full width. |

## Header

Photographed: [home-light-desktop.png](screenshots/home-light-desktop.png), [site-tree/main-menu.png](screenshots/site-tree/main-menu.png), [home-light-phone.png](screenshots/home-light-phone.png), [site-tree/phone-menu.png](screenshots/site-tree/phone-menu.png).

The tagline under the wordmark is "25 years of the free encyclopedia". Personal tools, signed out: Donate, Create account, Log in.

### Main menu

Opened by click. Not pinned. Two sections.

| Section | Label | Destination | This pass |
|---|---|---|---|
| Navigation | Main page | [/wiki/Main_Page](https://en.wikipedia.org/wiki/Main_Page) | home |
| Navigation | Contents | [/wiki/Wikipedia:Contents](https://en.wikipedia.org/wiki/Wikipedia:Contents) | not opened |
| Navigation | Current events | [/wiki/Portal:Current_events](https://en.wikipedia.org/wiki/Portal:Current_events) | not opened |
| Navigation | Random article | [/wiki/Special:Random](https://en.wikipedia.org/wiki/Special:Random) | not followed |
| Navigation | About Wikipedia | [/wiki/Wikipedia:About](https://en.wikipedia.org/wiki/Wikipedia:About) | not opened |
| Navigation | Contact us | [/wiki/Wikipedia:Contact_us](https://en.wikipedia.org/wiki/Wikipedia:Contact_us) | not opened |
| Contribute | Help | [/wiki/Help:Contents](https://en.wikipedia.org/wiki/Help:Contents) | not opened |
| Contribute | Learn to edit | [/wiki/Help:Introduction](https://en.wikipedia.org/wiki/Help:Introduction) | not opened |
| Contribute | Community portal | [/wiki/Wikipedia:Community_portal](https://en.wikipedia.org/wiki/Wikipedia:Community_portal) | not opened |
| Contribute | Recent changes | [/wiki/Special:RecentChanges](https://en.wikipedia.org/wiki/Special:RecentChanges) | not opened |
| Contribute | Upload file | [/wiki/Wikipedia:File_upload_wizard](https://en.wikipedia.org/wiki/Wikipedia:File_upload_wizard) | not opened |
| Contribute | Special pages | [/wiki/Special:SpecialPages](https://en.wikipedia.org/wiki/Special:SpecialPages) | not opened |

The phone menu at 390 CSS pixels shows the same labels. Shot: [site-tree/phone-menu.png](screenshots/site-tree/phone-menu.png).

## Page toolbar

Namespaces on the main page: Main Page (current), Talk ([/wiki/Talk:Main_Page](https://en.wikipedia.org/wiki/Talk:Main_Page), not opened).

Views: Read (current), View source (`action=edit` on Main_Page, not opened), View history (not opened). The watch star was not clicked.

### Tools

Opened by click. Shot: [site-tree/tools-menu.png](screenshots/site-tree/tools-menu.png). None of these destinations were followed.

| Section | Label |
|---|---|
| General | What links here, Related changes, Permanent link, Page information, Get shortened URL, Switch to legacy parser, Edit interlanguage links |
| Print/export | Download as PDF, Printable version (`javascript:print`, not clicked) |
| In other projects | Abstract Wikipedia, Wikimedia Commons, Wikimedia Foundation, MediaWiki, Meta-Wiki, Wikimedia Outreach, Multilingual Wikisource, Wikispecies, Wikibooks, Wikidata, Wikifunctions, Wikimania, Wikinews, Wikiquote, Wikisource, Wikiversity, Wikivoyage, Wiktionary, Wikidata item |

The permanent link on this visit pointed at oldid 1383522990. That revision was not opened.

## Appearance

Pinned on the right of the main page and of the article. hide was not clicked. Default public selection: Text Standard, Width Standard, Color Light. HTML classes included `skin-vector-2022`, `skin-theme-clientpref-day`, `appearance-pinned-clientpref-1`, `limited-width-clientpref-1`.

| Group | Options | This pass |
|---|---|---|
| Text | Small, Standard (checked), Large | Standard left checked in the preview session |
| Width | Standard (checked), Wide | Standard left checked |
| Color | Automatic, Light (checked), Dark | Light is the documented default. Dark was selected only in a separate headless context to read night tokens and shoot [home-dark-desktop.png](screenshots/home-dark-desktop.png). |

On the login and signup walls, the Text radios are disabled. The note says "This page always uses small font size". Width Standard and Color Light stay checked.

## Language

The main-page footer has a "349 languages" button. A click opened the Universal Language Selector (`.uls-rewrite`), with a "Search languages" field, Suggested languages, and All languages. The field was not typed in. No language link was clicked. Shot: [site-tree/language-menu.png](screenshots/site-tree/language-menu.png).

## Search

The header search field was not typed in. Empty search and a no-match query were opened by URL.

| URL | What it shows | Shot |
|---|---|---|
| [Special:Search](https://en.wikipedia.org/wiki/Special:Search) | Empty search form. Search box, Search button, and the search-results chrome with no query. | [search-empty-light-desktop.png](screenshots/search-empty-light-desktop.png), [site-tree/search-empty-preview.png](screenshots/site-tree/search-empty-preview.png) |
| Special:Search?search=zzzz-constellations-no-match-9f3a | "There were no results matching the query." The query string is a made-up token in the URL, not text typed into the field. | [search-no-results-light-desktop.png](screenshots/search-no-results-light-desktop.png) |

## Pages opened

| URL | Title | Shot |
|---|---|---|
| [/wiki/Main_Page](https://en.wikipedia.org/wiki/Main_Page) | Wikipedia, the free encyclopedia | [home-light-desktop.png](screenshots/home-light-desktop.png) |
| same, Color Dark, headless only | same | [home-dark-desktop.png](screenshots/home-dark-desktop.png) |
| same at 390 | same | [home-light-phone.png](screenshots/home-light-phone.png) |
| [/wiki/Talking_to_Yourself](https://en.wikipedia.org/wiki/Talking_to_Yourself) | Talking to Yourself - Wikipedia | [article-light-desktop.png](screenshots/article-light-desktop.png) |
| same at 390 | same | [article-light-phone.png](screenshots/article-light-phone.png) |
| [Special:Search](https://en.wikipedia.org/wiki/Special:Search) | Search - Wikipedia | [search-empty-light-desktop.png](screenshots/search-empty-light-desktop.png) |
| Special:UserLogin, no returnto | Log in - Wikipedia, on auth.wikimedia.org | [login-wall-light-desktop.png](screenshots/login-wall-light-desktop.png) |
| Special:CreateAccount | Create account - Wikipedia, on auth.wikimedia.org | [signup-wall-light-desktop.png](screenshots/signup-wall-light-desktop.png) |

The article is the featured article linked from the main page on this visit. Its contents list: (Top), Background and release, Composition, Critical reception, Credits and personnel, Charts, Notes, References. Edit and View source on the article were not opened.

Main-page counts painted on this visit: 263,142 active editors, 7,267,554 articles in English.

## Footer

Shot: [site-tree/footer.png](screenshots/site-tree/footer.png). Sister projects listed: Wikibooks, Wikiquote, Wikiversity, Wikidata, Wikisource, Wikivoyage, Wikifunctions, Wikispecies, Wiktionary. None were followed.

Footer links: Privacy policy (foundation.wikimedia.org), About Wikipedia, Disclaimers, Contact Wikipedia, Legal & safety contacts, Code of Conduct, Developers, Statistics, Cookie statement, Mobile view. None were followed. The footer says the page was rendered with Parsoid, and names CC BY-SA 4.0, Terms of Use, and the Wikimedia Foundation, Inc.

## Auth walls

Create account and Log in leave en.wikipedia.org for Wikimedia central auth (SUL3) on auth.wikimedia.org. Query tokens from those redirects are omitted here.

| Wall | How it was opened | What was painted | Stopped |
|---|---|---|---|
| Log in | [Special:UserLogin](https://en.wikipedia.org/w/index.php?title=Special:UserLogin) with no returnto. A URL that added `returnto=Main+Page` returned "invalid returnUrlToken" (400) and was abandoned. | Username and Password empty. "Keep me logged in" unchecked. Log in not clicked. Help with logging in, Forgot your password?, and Join Wikipedia not followed. No identity provider. No captcha widget. | Yes. [login-wall-light-desktop.png](screenshots/login-wall-light-desktop.png) |
| Create account | [Special:CreateAccount](https://en.wikipedia.org/w/index.php?title=Special:CreateAccount) | Username, Password, Confirm password, and Email address empty. "Create your account" not clicked. Username-policy help not clicked. hCaptcha privacy and terms links not clicked. No identity provider. The page shows the notice "This site is protected by hCaptcha and its Privacy Policy and Terms of Service apply." No challenge widget was painted. | Yes. [signup-wall-light-desktop.png](screenshots/signup-wall-light-desktop.png) |

`login-extracted` stays `not-started`.
