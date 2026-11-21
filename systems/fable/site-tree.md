# Fable public site tree

Mapped 2026-11-21 in headless Chromium, signed out, from https://fable.co/. The Osano consent banner was hidden with CSS. Accept All, Reject Non-Essential, and Save Preferences were not clicked. No email, name, password, or code was typed. Google, Apple, and store checkouts were not followed.

`/login` is a missing page. It renders the illustrated 404 ("Oops! The page you were looking for couldn't be found"). The real wall is `/signin`.

## Home (`https://fable.co/`)

| Control | Opens |
|---|---|
| Logo "Home" | `/` |
| Nav "Clubs" | `/clubs` |
| Nav "Books" | `/books` |
| Nav "Library" | `/library`, which redirects to `/signin?next=%2Flibrary`. Login wall. Branch stopped. |
| Nav "Blog" | `/blog` |
| Person icon "Sign up or log in" | Dialog on the same page: "Create your account". Fields: Display Name, Email Address, Password, Show. Checkbox: terms acceptance. Buttons: Sign up with Email, Continue with Google, Continue with Apple. Links: Terms of Use (`/terms`), Privacy Policy (`/privacy`), Log in (opens the login wall). Not submitted. Google and Apple not clicked. |
| Cart "Shopping cart" | Cart drawer. Empty when signed out. Not a checkout. |
| "Get the app" (hero and later repeats) | Dialog "Download the app" with App Store and Google Play badges and a QR code. Store links recorded, not followed into a store. |
| Cover carousel (about 28 covers) | Each cover is `/discover#b=<id>&src=home` (Discover, same page family). Example: "See books that look like The Song of Achilles, in Discover". |
| Club cards (about 10) | `/club/<slug>?club_type=free`. Example: `/club/romantasy-with-sophia-altman-599083839156`. |
| Footer "Join a club" | `/clubs` |
| Footer "Start a club" | `/blog/how-to-start-a-book-club` |
| Footer "Find a book" | `/books` |
| Footer "Company" | External: `https://www.scribdinc.com/about` |
| Footer "Community policy" | `/community-guidelines` |
| Footer "Blog" | `/blog` |
| Footer X / Twitter | External: `https://twitter.com/getfable` |
| Footer Instagram | External: `https://www.instagram.com/fable/` |
| Footer Facebook | External: `https://www.facebook.com/getfable` |
| Footer YouTube | External: `https://www.youtube.com/channel/UCqI3TsDOJOa9wgz1XJ8sc-A` |
| Footer TikTok | External: `https://www.tiktok.com/@getfable` |
| Footer "Help & Support" | `/support`, which links out to `https://help.fable.co/` |
| Footer "Privacy" | `/privacy` |
| Footer "Copyright Policy" | `/copyright-policy` |
| Footer "Terms of Service" | `/terms` |
| "Your Privacy Choices" | Osano preferences dialog (toggles for targeted advertising and personalization). Not accepted. Hidden for screenshots. |
| Phone menu (390) | Header collapses to a hamburger. Nav items are the same four destinations. |

## Clubs (`/clubs`)

| Control | Opens |
|---|---|
| "Search thousands of book and TV clubs" / "Search clubs" | Dialog "Find a club" with a search field. Empty state: "Clubs will appear here". Not submitted. |
| Genre chips (Fantasy, Romance, Thrillers, Young Adult, Literary Fiction, Dark Romance, Classics, Mystery, Horror, Sci-Fi, Historical Fiction, Cozy Fantasy, Personal Growth, LGBTQ+, Psychology, History, Religion & Spirituality, Biography, Poetry, Wellness, Short Stories, Politics, Education, Business, Manga, Graphic Novels, True Crime, Science & Technology, Nature & Environment, Art & Design, Humor, Sports, Music, Food, Travel) | `/club/<genre-slug>`. Sampled `/club/fantasy` ("Fantasy book clubs"). |
| "Scroll genres forward" | Same chip row, scrolled. |
| Carousel Previous / Next (Clubs starting soon, Engaging Book Clubs, Giveaway Clubs, Inspiring Clubs, Clubs Reading Free Books, and genre rows) | Same page, row scrolled. |
| Club cards | `/club/<slug>`. |
| "View more clubs" on a genre page | More club cards on the same page. |
| "Download the app to join" on a club page | `https://fable.sng.link/...` app deep link. Recorded. Not followed into a store. |
| "Start a club with this book" on a book page | `https://links.fable.co/create-a-club`. App link. Not followed. |
| Share (club or post) | Share menu, `aria-expanded=false` until opened. Not submitted. |
| FAQ rows | Accordion on the same page. |

## Books (`/books`)

| Control | Opens |
|---|---|
| "Shop 1M+ ebooks…" | Dialog "Search 1M+ books to organize & read". Empty until a query. Not submitted. |
| Book cards | `/book/<slug>`. Sampled `/book/fourth-wing-by-rebecca-yarros-9781649374080`. |
| Carousel Previous / Next | Same page, row scrolled. |
| `/store` | Redirects to `/books`. |

## Book page (`/book/<slug>`)

| Control | Opens |
|---|---|
| Author name / "View author profile" | `/author/<slug>` |
| "Want to read" | Menu of shelf actions. Signed-out press does not save. Not submitted. |
| "Read or listen free today" | App or Everand handoff. Not followed into a purchase. |
| App Store / Google Play badges in the green banner | `https://apps.apple.com/us/app/fable-stories-for-everyone/id1488170618` and `https://play.google.com/store/apps/details?id=co.fable.fable`. Recorded. Not followed. |
| "Other books by…" and "Books Similar to…" | Other `/book/<slug>` pages. |
| "Discussed by the community" club cards | `/club/<slug>` |
| FAQ rows | Accordion on the same page. |
| "May contain spoilers!" | Spoiler gate on the same page. Not opened past the gate. |

## Discover (`/discover`)

| Control | Opens |
|---|---|
| Search "Search for a book you love..." | Same page filter. Not submitted. |
| "Random" | Reloads the cover wall. |
| "What is this?" | Dialog explaining cover browsing. Closed with Escape. |
| "×" on the shelf | Removes a shelf item. Not used (shelf was empty). |
| "Sign up to save this shelf" | Signup wall. Branch stopped. |
| "Already have an account? Log in" | Login wall. Branch stopped. |
| "Copy link to this shelf" | Copies a link. Not pressed. |

## Blog (`/blog`)

| Control | Opens |
|---|---|
| Post cards | `/blog/<slug>`. Sampled `/blog/how-to-start-a-book-club`. |
| "View more posts" | More posts on the same page. |
| In-post "Fable Bookstore" | `/store`, which redirects to `/books`. |
| In-post "Fable Community Guidelines" | `/blog/fable-community-guidelines` |
| External citations | Left as external (for example a New Yorker essay). Not followed. |

## Legal and company

| Path | What it is |
|---|---|
| `/privacy` | Privacy policy. External opt-out links (Google, NAI, DAA) recorded, not followed. |
| `/terms` | Terms of use. |
| `/community-guidelines` | Community guidelines. |
| `/copyright-policy` | Copyright dispute policy. A published contact link is on the page. It was not opened and is not copied here. |
| `/company` | Redirects to `https://www.scribdinc.com/about`. Scribd Inc. nav: careers, newsroom, commitments, contact, Scribd, SlideShare, Everand. External. Not walked past the landing. |
| `/support` | Short page that points at `https://help.fable.co/`. |
| `https://help.fable.co/` | Help center collections: Getting Started, Fable Plus, Fable & Everand, Stats, Features, Clubs, Account, Authors, plus articles. Contact anchors stay on the help home. Not submitted. |
| `/login` | 404. "Go back" returns to the previous page. |

## Stopped at a login or signup wall

| From | Lands on | Stopped because |
|---|---|---|
| Nav Library, and any `/library` link | `https://fable.co/signin?next=%2Flibrary` | Email, password, Login with email, Reset it, Continue with Google, Continue with Apple, Sign up. Photographed. Nothing typed or clicked. |
| Person icon | Create-account dialog on the current page | Display Name, Email, Password, Sign up with Email, Google, Apple. Photographed. Not submitted. |
| Discover "Sign up to save this shelf" / "Log in" | Same signup or login wall | Not followed past the wall. |
| Club "Download the app to join" | Singular app link | App-store / app open. Not followed. |
