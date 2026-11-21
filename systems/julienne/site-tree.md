# Julienne site tree

Mapped 2026-11-21 from the public home page in headless Chromium, before screenshots. Origin: `https://withjulienne.com`. Signed out. Light is the default (`html.js.light`). A header control labelled "Toggle theme" switches `html` to `js dark`.

No control was typed into. No form was submitted. The cookie line ("This website uses cookies. Accept") was recorded and not clicked.

## Shell

The app shell (home, Discover, search, legal, recipe) shares one header.

| Control | Opens |
|---|---|
| Wordmark "Julienne" | `/` |
| Discover | `/discover` |
| Cookbook | `/cookbook` (signed-out empty state: "Come back soon.") |
| Search all recipes (desktop: header field; phone: icon button, `aria-label` "Search all recipes") | Focuses the search field. Submitting a query navigates to `/search?q=…`. Not submitted in this map. |
| Log in (header glass button, header text button, and the hero "Already have an account? Log in") | Auth dialog on the same URL. Email and Password fields, a checkbox for Terms of Service and Privacy Policy, "Create account or sign in with", Google, Apple, and "Already have an account? Sign in". Stop. Nothing typed. |
| Toggle theme | Stays on the page. Adds or removes `dark` on `html`. |
| `/login` | Redirects to `/` (HTTP 200, final URL `/`). Does not open the dialog by itself. |

Phone (390) header: wordmark, Search all recipes, Toggle theme, Log in. Discover and Cookbook are not in that header; they are reached by URL. No hamburger was found.

## Home `/`

| Control | Opens |
|---|---|
| Get the app | `https://apps.apple.com/us/app/julienne-a-smarter-cookbook/id6451086935` (leaves the site) |
| See more recipes (phone: "See more recipes for free") | Stays on `/`. No dialog observed. |
| Recipe card | `/days/<M_D_YYYY>/recipes/<id>` |
| Save (on a card) | Same auth dialog as Log in. Stop. |
| Ingredient chip (Brussel sprouts, Apple, …) | `/search?ingredients=<name>` |
| Collection title ("November breakfast specials") | Link target `/collections/carousel/…` redirected to `/` on this visit |
| Scroll left / Scroll right | Moves a carousel on the same page |
| Cookbook cover | Not followed as a separate page in this map |
| Buy | New tab, Amazon product URL with an affiliate tag. Not a Julienne page. Not purchased. |
| Footer Team | `/team` |
| Footer Roadmap | `/roadmap` |
| Footer Shop | `/shop` |
| Footer Terms of Service, Privacy Policy, Legal | All three hrefs are `/privacy-policy` |
| Twitter, Instagram, Tiktok | Off-site profiles. Not captured. |
| Email | `mailto:` contact. Not opened. Address is not written here. |

## Discover `/discover`

Same shell as home, plus a filter row and an import composer.

| Control | Opens |
|---|---|
| Browse all | `/discover` |
| Breakfast, Lunch, Dinner, Dessert, Quick 30, Under 500 cal, Soup, Pasta, Chicken, Steak, Fish, Salad, Sandwich, Beans, Potatoes, Salmon, Vegetarian, Vegan | `/discover/<slug>` (Breakfast click landed on `/discover/breakfast`) |
| Import field ("Import a recipe using a link, photo, video, text or chat…") | Focus only. Not typed. Submitting would create a recipe. |
| Attach file, Import links, Import photos | File or import UI. Not used (would upload or create). |
| Create a recipe (on an empty-ish search) | Not followed. Creation is behind an account. |

Sitemap pages, same shell, captured as the filter family rather than 17 full duplicates: `/discover/breakfast`, `/discover/lunch`, `/discover/dinner`, `/discover/dessert`, `/discover/quick-30-min`, `/discover/under-500-calories`, `/discover/soup`, `/discover/pasta`, `/discover/chicken`, `/discover/steak`, `/discover/fish`, `/discover/salmon`, `/discover/salad`, `/discover/sandwich`, `/discover/beans`, `/discover/potatoes`, `/discover/vegetarian`, `/discover/vegan`.

## Search `/search`

| Control | Opens |
|---|---|
| Meal-idea chips (Vegetable frittata, Chocolate overnight oats, …) | A search query page. One chip family is enough; chips are the same control. |
| Ingredient result page `/search?ingredients=<name>` | Result list, "Create a recipe", social handles as buttons. Create a recipe stops at the auth wall if it asks for an account. |

## Recipe `/days/<date>/recipes/<id>`

One public recipe that loaded (title "5 Minute Punch Mocktail") and one that did not ("This recipe doesn't exist").

| Control | Opens |
|---|---|
| Create an account | Auth dialog. Stop. |
| Decrease portions / Increase portions | Same recipe, portion count changes. No submit. |
| Save | Auth dialog. Stop. |
| Watch | Off-site or embedded video. Recorded if it stays on the page. |
| Cook | Not followed if it starts a signed-in cook mode. |
| Scan to get the recipe on mobile | QR / app handoff. Recorded as a state, not scanned. |

Hundreds of recipe URLs live in dated `sitemap-recipes-*.xml` files. They share this template. The capture keeps one working recipe and one missing-recipe state, not every date.

## Marketing pages (no app shell)

| Page | Notes |
|---|---|
| `/team` | Editorial page. Nav: home, Instagram, Twitter / X, Shop. |
| `/roadmap` | Q2 2025 roadmap. Same marketing nav, plus Tiktok. |
| `/shop` | Marketing shop shell. On this visit the body was the footer ("Need Cooking Inspiration?") with no product grid. |
| `/privacy-policy` | App shell. Heading is "Terms of Service" even though the path says privacy. Effective date April 9th, 2025. |

## Stopped branches

| Control or URL | What happened |
|---|---|
| `/login` | Redirects to `/`. |
| Log in, Save, Create an account | Auth dialog: email, password, Google, Apple. Not typed. Google and Apple not clicked. |
| Newsletter "Your email" on the home page | Not typed. Not submitted. |
| Cookbook contents, saved recipes, profile, plan, onboarding | Not reachable signed out. |
