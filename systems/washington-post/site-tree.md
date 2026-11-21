# Washington Post public site tree

Mapped from the signed-out homepage on 2026-11-21, before any package screenshot. Driver: Playwright, headed Chrome (headless Chromium and HTTP/2 both failed to load the site). Desktop map at 1440×900. Phone chrome checked at 390×844. No form was submitted. No Google, Apple, Amazon, Facebook, or SSO control was clicked. No password, code, profile, plan, survey, newsletter, or onboarding field was filled.

Theme observed: `color-scheme: normal`. No public dark-mode toggle on the homepage, section fronts, or section drawer.

## Homepage chrome

| Control | Opens | Then |
|---|---|---|
| Accessibility statement | https://www.washingtonpost.com/accessibility/ | Public page. Captured. |
| Skip to main content | `#main-content` on the current page | In-page jump. |
| Search and browse sections | `#sc-sections-nav-drawer` (dialog, "Sections Navigation") | Public menu. Captured. Escape closes it. |
| News alerts | Radix dialog "NEWS ALERTS" | Public list of published alerts, plus "Create a free account" which goes to the sign-in wall. The dialog was opened. Its screenshot was not kept: one headline named a street sale. Account branch stopped. |
| Save and subscribe | https://subscribe.washingtonpost.com/acquisition/ | Public offer page. Captured. No plan field filled. |
| Sign in | https://www.washingtonpost.com/subscribe/signin/ | Login wall. URL recorded. Page captured as the wall. Branch stopped. |
| Logo ("Democracy Dies in Darkness" / "Logo of The Washington Post") | https://www.washingtonpost.com/ | Homepage. |
| Breaking banner close | Dismisses the breaking-news strip on the homepage | UI dismiss, not a form. |
| Black Friday softwall (`#softwall-…`, "Collapse notification") | Marketing dialog: Subscribe, Sign In | Subscribe goes to checkout. Sign In goes to the sign-in wall. Dialog captured. Neither control followed into a filled form. |

## Sign-in wall

https://www.washingtonpost.com/subscribe/signin/?next_url=https%3A%2F%2Fwww.washingtonpost.com%2F&itid=nav_sign_in

Visible controls, none followed past the wall: email field, Next, Continue with Amazon, Continue with Facebook, Continue with Google, Continue with Apple, Continue with SSO. Google and Apple were not clicked. The email field was not filled. The same wall is the destination of header Sign in, the softwall Sign In link, and News alerts "Create a free account".

## Section drawer

The drawer search form posts to https://www.washingtonpost.com/search (`name=query`). The field was focused and typed into. The form was not submitted, so no results page was opened.

Primary row (each name is a link to that front):

| Label | URL |
|---|---|
| Home Page | https://www.washingtonpost.com/ |
| Politics | https://www.washingtonpost.com/politics/ |
| Opinions | https://www.washingtonpost.com/opinions/ |
| U.S. News | https://www.washingtonpost.com/national/ |
| Style | https://www.washingtonpost.com/style/ |
| Investigations | https://www.washingtonpost.com/national/investigations/ |
| Recipes | https://www.washingtonpost.com/recipes/ |
| Well+Being | https://www.washingtonpost.com/wellbeing/ |
| Business | https://www.washingtonpost.com/business/ |
| Tech | https://www.washingtonpost.com/business/technology/ |
| World | https://www.washingtonpost.com/world/ |
| D.C., Md. & Va. | https://www.washingtonpost.com/local/ |
| Sports | https://www.washingtonpost.com/sports/ |
| Games | https://www.washingtonpost.com/games/ |

A second list in the same drawer repeats many of those and adds: Abortion, Advice, Arts & Entertainment, Books, Carolyn Hax, Chats & Community, Classifieds, Climate, Climate Solutions, Comics, Education, Food, Gender & Identity, Health, History, Home & Design, Horoscopes, Immigration, Jobs, National Security, Newsletters & Alerts, Obituaries, The Optimist, Parenting, Photography, Podcasts, Religion, Science, Transportation, Travel, Video, Washington Post Live, Weather. Product links at the bottom: WP Intelligence, Ask The Post AI, Ripple, WP Creative Group, WP Creator.

Chevron rows open a second dialog (Radix) of child sections. Children that opened on this pass:

| Parent | Children |
|---|---|
| Style | Fashion, Power, Trends |
| Sports | NFL, MLB, NBA, WNBA, NHL, Auto Racing, Boxing & MMA, College Sports, Golf, Olympics, Soccer, Tennis |
| World | Africa, Americas, Asia, Europe, Middle East |
| Weather | Extreme Weather |
| Food | Recipes |
| Science | Animals |
| Education | Higher Education |
| D.C., Md. & Va. | The District, Maryland, Virginia, Local Weather, Going Out Guide |

Politics, Opinions, Business, Games, Climate, Health, Travel, and Arts & Entertainment showed a chevron and did not open a child list on this click. Their section fronts still have their own subnav (below).

## Section-front subnavs

| Front | Subnav links |
|---|---|
| Politics | Donald Trump, White House, Democracy in America, Courts & Law, National Security, Elections |
| Opinions | Editorials, Columns, Guest Opinions, Cartoons, Letters to the Editor, Submit a Guest Opinion (Google Form, not opened), Submit a Letter |
| Games | Daily Crossword, Daily Mini Meta Crossword, Sudoku, On the Record, Keyword, Wridges, Half Chance, Untangled, More Games (games.washingtonpost.com) |
| Election 2026 | Senate, House, Governor, States |

Crossword, Sudoku, and the other puzzle players were not opened. They sit behind the games index.

## Homepage story links

Story cards, author names, and the breaking-news story link go to article or `/people/` pages. Those URLs were recorded in the map and left out of screenshots: article pages on this site carry bylines and correction furniture that can show an email, and author pages are account-like profiles. No article or author page was screenshotted.

## Phone (390×844)

Same header actions: Search and browse sections, News alerts, Save and subscribe, Sign in, logo. Extra tabs on the homepage: Top Stories, Latest, For You, Ask The Post AI. For You is a personalization tab on the public homepage. It was opened as a tab state and not treated as an account. Ask The Post AI goes to https://www.washingtonpost.com/ask-the-post-ai/.

## Footer (public)

About The Post, Newsroom Policies & Standards, WP Creative Group, Workforce Demographics, Careers (careers.washingtonpost.com), Media & Community Relations, Accessibility Statement, section fronts already listed, Obituaries, Weather, Arts & Entertainment, Recipes, WP Intelligence, Enterprise Subscriptions, Manage Your Subscription (account, not opened), Become a Subscriber, Gift Subscriptions, Mobile & Apps, Newsletters & Alerts, Washington Post Live, Reprints & Permissions, Post Store (store.washingtonpost.com), Books & E-Books, Print Archives (ProQuest, subscribers only, not opened), Today's Paper, Public Notices, Crosswords & Games, app-store links (not opened), Contact the Newsroom / Customer Care / Opinions team (helpcenter.washingtonpost.com), Advertise, Licensing & Syndication, Request a Correction, Send a News Tip, Report a Vulnerability, terms and privacy pages, Cookie Settings, Sitemap, Ad Choices.

Cookie Settings was opened as a dialog and not submitted. Manage Your Subscription, Print Archives, help-center contact articles, and app-store links were mapped and not followed. Newsletters was not filled.

## Stopped branches

| URL | Why |
|---|---|
| https://www.washingtonpost.com/subscribe/signin/ | Login wall. Email, Google, Apple, Amazon, Facebook, SSO. |
| Subscribe checkout from the softwall | Payment. Not opened past the offer page. |
| Manage Your Subscription | Account. |
| Create a free account inside News alerts | Same sign-in wall. |
| Google Form "Submit a Guest Opinion" | Form. Not opened. |
| Any article or `/people/` URL | Mapped. Left out of screenshots. |
