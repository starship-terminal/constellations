# Hashnode signed-in site tree

Mapped on 2026-11-21 from the signed-in shell at `https://hashnode.com/onboard`, in the T3 in-app preview, default profile. The session was signed in. Setup is incomplete, so the app forces Step 1 of 2. Nothing was typed, submitted, published, bought, invited, or deleted. The profile fields were left as they arrived.

The public package already covers the signed-out marketing and blog surfaces. This map is the signed-in shell only.

## Shell

The desktop shell is a 268px sidebar plus a main column. Phone width (measured 390x844) collapses that sidebar into an Open menu button, a wordmark, Search, and Write.

| Control | Opens | What happened |
|---|---|---|
| Wordmark | `/` | Same-origin navigation 307s to `/onboard`. |
| Notifications | `/notifications` | Prefetch 307s to `/onboard?callbackUrl=/notifications`. Not opened as a page. |
| Toggle Sidebar | Collapses the rail | Not pressed. |
| Write | Write sheet, and sets `callbackUrl=/dashboards` | The sheet closed before a frame was saved. Not opened into the editor. |
| Search | Search dialog, "Search posts, people, tags and pages" | Opened. Nothing typed. |
| Home | `/` | Redirects to `/onboard`. |
| Feed | `/feed` | Redirects to `/onboard?callbackUrl=/feed`. |
| Drafts | `/drafts` | Prefetch 307s to onboard. Not opened as a page. |
| Hashnode Pro | `/pro` | Not navigated from this session. Public `/pro` is already in the package. |
| Hashnode for Agents | `/agents` | Not navigated from this session. Public `/agents` is already in the package. |
| What's new card | `/changelog/2026-10-07-aeo-suggested-queries` | Prefetch 307s to onboard. Not opened. Dismiss was not pressed. |
| Theme | Light / Dark / System | Opened. System was checked on arrival. Light was selected for one reading, then Dark was restored and verified (`html` class contains `dark`, `colorScheme` dark). |
| More | Resource menu | Opened earlier in the session. Items listed below. Not re-shot in the committed set because that frame matched the closed shell. |
| Account button | Account menu | Opened. Profile, Bookmarks, Settings, Sign out. Sign out was not pressed. |

## Account menu

| Item | Target | What happened |
|---|---|---|
| Header | Account profile URL | Prefetch 307s to onboard. Not opened. |
| Profile | Same profile URL | Prefetch 307s to onboard. Not opened. |
| Bookmarks | `/bookmarks` | Prefetch 307s to `/onboard?callbackUrl=/bookmarks`. Not opened. |
| Settings | `/settings` | Prefetch 307s to `/onboard?callbackUrl=/settings`. Not opened. |
| Sign out | No href | Not pressed. |

## Search dialog (resting, no query)

Pages: Home feed, Write a post, Bookmarks, Drafts, Profile, Settings.

Settings: General settings, Account, Email, Developer.

Other: Brand, Support (published product contact), Terms, Privacy Policy, Code of Conduct.

Shortcuts footer: Move, Open, All shortcuts. All shortcuts was not opened. No result row was opened.

## More menu

Buildful and Bug0 (external), The foreword (`/blog`), Hashnode gql skill (GitHub), Changelog, Brand, Hackathons, X, LinkedIn, Support (mailto, not opened), Code of Conduct, Terms, Privacy, Sitemap. Same-origin items prefetch to onboard while setup is incomplete. External and mailto links were not followed.

## Onboard form (visible shell)

Step 1 of 2. Upload photo, Change photo, and Remove were not pressed. Name and email arrived filled and were left alone. Username, location, and tagline were left empty. Next was not pressed, so Step 2 never loaded.

## Gate

Every app destination tried from this session (`/`, `/feed`, `/notifications`, `/drafts`, `/settings`, `/bookmarks`, the account profile, the changelog card) returns 307 to `/onboard` with that path as `callbackUrl`. The signed-in product behind setup is not reachable without submitting the form, which this pass did not do.
