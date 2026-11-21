# ChatGPT public site tree

Mapped 2026-11-22 from [https://chatgpt.com](https://chatgpt.com) while signed out, in an incognito preview tab. The page title is "ChatGPT: Chat, Work, Create & Code with AI". Desktop shots are 1440×900 CSS pixels at 2x (2880×1800 PNG). Phone shots are 390×844 CSS pixels at 2x (780×1688 PNG).

Nothing was typed. No chat was sent. No form was submitted. Google, Apple, and phone were not clicked. `login-extracted` stays not-started. The signed-in package already in this folder was left in place. `systems/chatgpt-ios` was not touched.

The app shell and the marketing site are different public surfaces. The homepage, Images, Plugins, and the auth wall are the app. Pricing, About, Codex, Business, and Download are the marketing site, reached from the sidebar's pricing link and from the marketing header.

## Homepage

| Control | Opens |
|---|---|
| Wordmark "ChatGPT" (desktop sidebar) | https://chatgpt.com/ |
| New chat | Homepage again. The href seen in the phone drawer was `/?noauth_recent_chat_failed=1`. Clicking it can open a "Clear current chat?" dialog ("To start a new chat, your current conversation will be discarded. Sign up or log in to save chats.") That dialog was not photographed. |
| Images | https://chatgpt.com/images. Public empty state. Photographed desktop and phone. |
| Plugins | https://chatgpt.com/plugins. Public catalog. Photographed desktop. The phone drawer link was `/plugins?plugins_landing=1`. |
| See plans and pricing | https://openai.com/chatgpt/pricing/ redirects to https://chatgpt.com/pricing/. Public. Photographed desktop. |
| Help | https://help.openai.com. External. Not opened. |
| Deep research (button) | Popover on the homepage: "Turn questions into research" / "Log in to run multi-step research, compare sources, and save cited reports to revisit later." Log in and Sign up for free. Photographed. Neither button was clicked. |
| Settings | https://chatgpt.com/settings. Not opened. Expected to be the same auth wall or a signed-in shell. Stop. |
| Search chats (phone drawer) | Button. Not clicked. |
| Sidebar promo "Get responses tailored to you" + Log in | Same auth wall. Not clicked from the promo. |
| Header Log in | https://chatgpt.com/auth/login. Empty wall. Photographed. Stop. |
| Header Sign up for free | Same wall. The plugins page links both Log in and Sign up to `/auth/login`. Photographed as the same image. Stop. |
| Close sidebar / Open sidebar | Collapses the 260px desktop column, or opens the phone drawer (dialog "Sidebar", about 310px). Photographed phone. |
| Add files and more | Menu: Add photos, Web search, then "Log in to use..." Create image, Deep research, Add files. Photographed. No file picked. Login-gated items not clicked. |
| Start dictation | Not clicked. May request a microphone. |
| Start Voice | https://chatgpt.com/?mode=voice. Not opened. |
| Send message | Disabled while the composer is empty. Not clicked. |
| What can I do here? | Suggestion chip under the composer. Not clicked. |
| Footer Terms | https://openai.com/terms. Not opened. |
| Footer Privacy Policy | https://openai.com/privacy. Not opened. |
| Footer Learn more | https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance. Not opened. |

Desktop headline is "Where should we begin?". Phone headline is "What are you working on?". There is no public theme switch on the logged-out shell (`data-theme` is null). The page paints black with white text.

## Auth wall

Log in and Sign up for free open one page: https://chatgpt.com/auth/login, title "Log in or sign up". Photographed empty. Email field empty. Continue not pressed.

| Control | Opens |
|---|---|
| Continue with Google | Identity provider. Not clicked. |
| Continue with Apple | Identity provider. Not clicked. |
| Continue with phone | Identity provider. Not clicked. |
| Email address | Empty text field, name `username`, type email. Not typed. |
| Continue | Not pressed. |
| Terms of use | https://openai.com/policies/terms-of-use/. Not opened. |
| Privacy policy | https://openai.com/policies/privacy-policy/. Not opened. |
| Cookie preferences | Not pressed. |

## Images

https://chatgpt.com/images. Title "AI Image Generator - ChatGPT Images". Heading "Images". Composer placeholder "Describe a new image". Send disabled. The suggestion request (`image-suggestions`) returned 502, so no chips rendered. Photographed desktop and phone as that empty state.

## Plugins

https://chatgpt.com/plugins. Heading "Plugins". Subhead "Work with ChatGPT across your favorite tools." Search box. Categories seen: Popular, New & Noteworthy, Small Business, Real Estate, Productivity, Creativity, Developer Tools. Install buttons are links to `/auth/login?next=/plugins/...`. Not clicked.

## Pricing

https://chatgpt.com/pricing/. Title "Plans and Pricing | ChatGPT". Heading "Pricing". Subhead "See pricing for our individual, business, and enterprise plans." Currency on this locale was SGD. Individual was selected. Business & Enterprise was not switched. Paid plan buttons were not clicked. Get Plus and Get Pro hrefs carried a query (`ifpazk`, `default_tab`, `highlight_plan`). Those links were not followed, and the query is not treated as a public path.

| Control | Opens |
|---|---|
| ChatGPT blossom logo | https://chatgpt.com/ |
| About | https://chatgpt.com/overview/. Mapped, not opened. |
| Features | Menu. Items seen in the link list include ChatGPT Work `/work/`, Deep Research `/features/deep-research/`, Dots, Finances, Images, Plugins, Remote, Shopping, Sites, Slack and Teams, Slides, Space, Study Mode, Voice, and use-case pages. Menu not expanded for a shot. |
| Learn | Menu. Not expanded. |
| Codex | https://chatgpt.com/codex/. Mapped, not opened. |
| Business | https://chatgpt.com/business/. Mapped, not opened. |
| Pricing | https://chatgpt.com/pricing/. This page. |
| Download | https://chatgpt.com/download/. Mapped, not opened. |
| Log in / Sign up for free | Same auth wall already photographed. Not clicked again. |
| Individual / Business & Enterprise | Radiogroup on this page. Individual stayed selected. |
| Get Free | https://chatgpt.com/. Not clicked. |
| Get Go | https://chatgpt.com/explore/go. Not clicked. |
| Get Plus / Get Pro | Query links back to the app with a plan highlight. Not clicked. |
| Rosalind Academic Plan, Learn more | https://openai.com/index/introducing-the-rosalind-academic-plan/. Not opened. Dismiss not pressed. |
| billing help | https://help.openai.com/en/collections/3943089-billing. Not opened. |

Prices read on the page: Free SGD 0 / month, Go SGD 11 / month, Plus SGD 30 / month, Pro from SGD 138 / month.

## Phone

The phone homepage collapses the sidebar into a drawer. Open sidebar opens dialog "Sidebar". Destinations match the desktop sidebar, plus Search chats. New chat and the drawer wordmark used `/?noauth_recent_chat_failed=1`. Settings is `/settings`. The drawer was photographed and closed. No username was on screen.
