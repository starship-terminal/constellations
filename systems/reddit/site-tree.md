# Reddit site tree

Mapped on 2026-11-22 from the public homepage, https://www.reddit.com/, signed out, in the T3 preview browser at 1440 by 900. The page title was "Reddit - The heart of the internet". A first load carried a `js_challenge` query. The feed still rendered. That query is not a page. No login, signup, or identity-provider wall was crossed while mapping. No form was submitted. No vote, comment, join, or subscribe control was used.

The homepage header is a search field, Sign Up, and Log In. At 390 the wordmark is replaced by a menu button and Log In. Best, Everywhere, and the view control open menus. They were not opened. Footer links sit under the feed. Popular communities sit in the right rail.

| Control | Page | Destination or state |
|---|---|---|
| Home | https://www.reddit.com/ | / |
| Sign Up | https://www.reddit.com/ | /register/ (empty wall, not submitted) |
| Log In | https://www.reddit.com/ | /login/ (empty wall, not submitted) |
| Search Reddit | https://www.reddit.com/ | search field, not typed |
| Best | https://www.reddit.com/ | /r/popular/best/ (menu, not opened) |
| Hot | https://www.reddit.com/ | /r/popular/hot/ (menu, not opened) |
| New | https://www.reddit.com/ | /r/popular/new/ (menu, not opened) |
| Top | https://www.reddit.com/ | /r/popular/top/ (menu, not opened) |
| Rising | https://www.reddit.com/ | /r/popular/rising/ (menu, not opened) |
| Everywhere | https://www.reddit.com/ | /r/popular/best/?geo_filter=global (menu, not opened) |
| Card | https://www.reddit.com/ | /?feedViewType=cardView (menu, not opened) |
| Compact | https://www.reddit.com/ | /?feedViewType=compactView (menu, not opened) |
| Open menu | phone homepage | left nav, not opened |
| Expand user menu | header | not opened |
| Post title | feed | a public comments page, logged out |
| Community name | feed | a public community, logged out |
| Join | feed and community | not clicked |
| Create Post | community header | not clicked |
| Upvote, Downvote, Reply, Share | post and feed | not clicked |
| Popular | footer | /r/popular/ |
| News | footer | /news/ |
| Explore | footer | /explore/ |
| Best of Reddit | footer | /posts/2026/global/ |
| Best of Reddit in Portuguese | footer | /posts/2026/tl-pt-BR/ |
| Best of Reddit in German | footer | /posts/2026/tl-de/ |
| Reddit Rules | footer | https://www.redditinc.com/policies/content-policy |
| Privacy Policy | footer and auth walls | https://www.reddit.com/policies/privacy-policy and https://www.redditinc.com/policies/privacy-policy |
| User Agreement | footer and auth walls | https://www.redditinc.com/policies/user-agreement |
| Accessibility | footer | https://support.reddithelp.com/hc/sections/38303584022676-Accessibility |
| Forgot password? | login wall | /password/ (not opened) |
| Continue with Phone Number | login and signup | same login path, not clicked |
| Continue with Google | login and signup | identity provider, not clicked |
| Continue with Apple | login and signup | identity provider, not clicked |
| Email me a one-time link | login | not clicked |
| Continue with SSO | login, hidden step | not opened |
| Use a backup code | login, hidden step | not opened |

A public post from the homepage feed loaded without an account: https://www.reddit.com/r/AskReddit/comments/1y1kdmq/what_sport_has_the_smallest_skill_gap_between_an/. Comments were visible. The left rail was a join card. The comment box said "Join the conversation" and was not typed into.

A public community from that post loaded without an account: https://www.reddit.com/r/AskReddit/. The official community https://www.reddit.com/r/reddit/ also loaded, with Create Post and Join. Neither was clicked.

An unknown community path, https://www.reddit.com/r/thiscommunitydoesnotexistxyz123/, opened a dialog titled "We couldn't find that community" and a second dialog titled "Mature Content". Neither button was used. Escape did not dismiss the community dialog.

`prefers-color-scheme: light` switched the page background from `#0E1113` to `#FFFFFF`. The brand button stayed `#D93900`. Dark was the first paint. The homepage, the phone homepage, and r/reddit were shot after the switch. The public post, r/AskReddit, the missing-community dialog, and the login and signup walls were shot on the dark first paint.
