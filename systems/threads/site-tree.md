# Threads public site tree

Mapped from https://www.threads.com/ in headless Chromium on 2026-11-21, before screenshots. Desktop viewport 1440×900. Phone viewport 390×844 with an iPhone user agent. Escape dismisses the join dialog. No form was submitted. No username, email, password, or code was typed. Instagram, Google, Apple, and Facebook buttons were not clicked.

The signed-out home page is the public feed. `html` starts in `__fb-light-mode`. A dark colour-scheme context paints `__fb-dark-mode` (`rgb(16, 16, 16)` page, `rgb(243, 245, 247)` text). More > Appearance shows Auto. The Dark and Light rows did not mount in this pass, so those menu rows are not captured as separate controls.

## Desktop chrome (left rail)

| Control | Opens | Stop |
|---|---|---|
| Logo | https://www.threads.com/ | |
| Home | https://www.threads.com/ | |
| New thread | Dialog: "Sign up to post. Join Threads to share ideas, ask questions, post random thoughts…" Continue with Instagram | Login wall. Stop. |
| Search | https://www.threads.com/search | |
| Messages | Dialog: "Say more with Threads… Continue with Instagram" | Login wall. Stop. |
| Activity | Same join dialog | Login wall. Stop. |
| Profile | Same join dialog | Login wall. Stop. |
| Insights | Same join dialog | Login wall. Stop. |
| Log in | https://www.threads.com/login | Login wall. Stop. Do not type. |
| More | Menu: Appearance, Sounds, Report a problem | |
| More > Appearance | Submenu: Back, Appearance, Auto | Auto is the only option that mounted. |
| More > Sounds | Panel: "Sounds. Play a sound on this device when you receive new notifications. Activity. Messages." | Public. No account setting was changed. |
| More > Report a problem | Menu stayed on the same three items in this pass. No form opened. | Not submitted. |

## Home feed

| Control | Opens | Stop |
|---|---|---|
| Join dialog on first paint | "Say more with Threads… Continue with Instagram" | Escape closes it. Do not click Continue with Instagram. |
| Username | https://www.threads.com/@{handle} | Public profile. |
| Topic chip | https://www.threads.com/search?q=…&serp_type=tags | Public search. |
| Timestamp | https://www.threads.com/@{handle}/post/{id} | Public post. |
| Media | https://www.threads.com/@{handle}/post/{id}/media | Public. |
| More (post) | Menu: Copy link | Public. Copy was not used. |
| Like, Comment, Repost, Share | Action row on the post. Counts are visible. | Not pressed. A press can write or open a login wall. |
| Footer: Threads Terms | https://help.instagram.com/769983657850450 | Off-site help page. |
| Privacy Policy | https://help.instagram.com/515230437301944 | Off-site help page. |
| Cookies Policy | https://help.instagram.com/1896641480634370/ | Off-site help page. |
| Report a problem (footer) | Same control as More > Report a problem | Not submitted. |
| "Learn more" on a video error | https://l.threads.com/?u=https://www.facebook.com/help/… | Signed redirect. Not followed. |

## Search

https://www.threads.com/search loads signed out. It shows a search field (placeholder "Search") and a bottom sheet: "Log in or sign up for Threads… Continue with Instagram" plus "Log in with username instead" (https://www.threads.com/login?show_choice_screen=false). Focusing the field does not open a new page. No query was typed.

## Profile (public)

https://www.threads.com/@threads loads signed out. Header: avatar, name, bio, topic chips, follower count, Follow, Mention, an Instagram link (https://www.instagram.com/threads/, not clicked), and an external podcast link (open.spotify.com, not followed).

| Control | Opens | Stop |
|---|---|---|
| Threads, Replies, Media, Reposts | In-page tabs. URL stays on /@threads | Public. |
| Follow | Dialog: "Sign up to follow… Continue with Instagram" | Login wall. Stop. |
| 6.9M followers | https://www.threads.com/login | Login wall. Stop. |
| Mention | Not opened. | Likely a composer wall. |

A post permalink such as https://www.threads.com/@{handle}/post/{id} loads signed out with no dialog.

## Login (boundary only)

https://www.threads.com/login and https://www.threads.com/login?show_choice_screen=false both land on https://www.threads.com/login (title "Threads • Log in"). Visible, not used: "Scan to get the app", username field ("Username, phone or email"), password field, Log in, Forgot password? (https://www.threads.com/reset_password, not opened), Continue with Instagram. No Google, Apple, or Facebook button. Nothing was typed. Nothing was submitted.

These paths redirect to login and were not entered:

- https://www.threads.com/about
- https://www.threads.com/privacy
- https://www.threads.com/terms

## Phone (390×844)

The iPhone user agent paints a splash (`#barcelona-splash-screen`) that hides the page until it fades. After it hides:

| Control | Opens | Stop |
|---|---|---|
| Logo | https://www.threads.com/ | |
| Log in | Button in the header | Login wall. Stop. |
| Open app | https://applink.threads.com/… | App link. Not followed. |
| Tab bar: Home | https://www.threads.com/ | |
| Tab bar: Search | https://www.threads.com/search | |
| Tab bar: Create | Icon button. A click in this pass left the feed and opened no dialog. | Treated as the composer wall. Not retried. |
| Tab bar: Notifications | Icon button | Login wall if it opens the join dialog. Stop. |
| Tab bar: Profile | Icon button | Login wall if it opens the join dialog. Stop. |
| Post row | Same as desktop: profile, topic, post, media, more, like, comment, repost, share | Like, comment, repost, and share not pressed. |

A 390-wide window with a desktop user agent shows the feed and a Log in link, without the phone tab bar. Captures use the phone user agent so the phone chrome is the one recorded.
