# Exactly site tree

Mapped 2026-11-21 from a signed-in T3 preview tab on the default profile, starting at `https://threads.exactly.ai/onboarding`. The public marketing tree below is the one the existing package already captured (2026-11-14). The signed-in tree is only what this pass could see without filling onboarding.

## Public site (exactly.ai)

Already captured. Not re-walked in this pass.

| Control | Opens |
|---|---|
| Logo | `/` |
| Nav: Showcase, Case studies, Industries, Pricing, Help | `/showcase`, `/case-studies`, `/industries`, `/pricing`, `/help-center` |
| Log in | `threads.exactly.ai` (not followed in the public capture) |
| Start for free | `threads.exactly.ai` signup (not followed) |
| Book a demo | `/book-a-demo` (scheduler measured at rest) |
| Footer columns | the same public routes, plus legal pages linked from the footer |
| Mobile hamburger | the drawer with the same nav links |

## Signed-in app (threads.exactly.ai)

The session was already signed in. The only painted shell is the first onboarding step. No sidebar, settings, or create control is in the DOM.

| Control | What it does | This pass |
|---|---|---|
| Progress bar (`aria-valuenow` 14, accent fill) | Shows step progress across the top | Seen. Not a navigation control |
| Log out | Ends the session | Seen. Not clicked |
| The company I work for | Advances onboarding for a company the person works for | Seen. Not clicked. Filling onboarding was refused |
| My client's company | Advances onboarding for a client's company | Seen. Not clicked |
| My own business | Advances onboarding for a personal business | Seen. Not clicked |
| My personal project | Advances onboarding for a personal project | Seen. Not clicked |
| Help (`https://exactly.ai/help-center`) | Opens the public help center in a new navigation | Desktop only, bottom-right cluster. Not followed |
| Chat bubble (no label) | Opens the support widget | Desktop only. Not opened |
| Notifications region (`Alt+T`) | Toast region, empty | Present, nothing in it |

Phone width (390 x 844) hides the help cluster. Log out and the four choices stay. The card docks to the bottom of the viewport and clips the last choice.

## Not in this shell

| Area | Why it is missing |
|---|---|
| Studio, generator, models, credits, billing | Behind the unanswered onboarding step |
| Settings, account, profile | No settings control is rendered |
| Create, prompt bar, empty project | No create control is rendered |
| Later onboarding steps | Choosing an option would submit the profile field |
