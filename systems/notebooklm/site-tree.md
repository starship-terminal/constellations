# NotebookLM public site tree

Mapped on 2026-11-22 from the public homepage, signed out, in the T3 preview browser (incognito). Desktop is 1440 by 900 CSS pixels. Phone is 390 by 844 CSS pixels. Both were photographed at device pixel ratio 2. `prefers-color-scheme` was light. The page painted white.

`https://notebooklm.google.com` returns 301 to `https://notebook.google.com/`, which then lands on `https://notebook.google.com/trynow`. The title is "Gemini Notebook". The page is the live marketing site, not a parked page and not a captcha wall. The product name on the page is Gemini Notebook. The public URL is still NotebookLM.

No email, password, phone, code, or address was typed. No identity provider was clicked. No form was submitted. No captcha was solved. Next was not clicked. Create account was not opened. No notebook was created. `login-extracted` stays not-started. `systems/google` was not touched. `catalog.json` was left alone.

## Header

At 1440 the header is the wordmark and Sign in. At 390 the header is the wordmark only. Sign in moves into the page.

| Control | Where | Destination |
|---|---|---|
| Gemini Notebook home | header, both widths | https://notebook.google.com/ which redirects to /trynow |
| Sign in | header, 1440 only | https://notebook.google.com/login which redirects to the Google Accounts identifier step |
| Get the app | in the DOM at 1440, `display: none` | https://notebook.google.com/download?from=trynow |

## Homepage body

The headline is "Understand anything". The supporting line is "Your research and thinking partner, grounded in the information you trust, built with the latest Gemini models."

The illustration labels are captions, not links: Slide decks, Mind Maps, Audio Overviews, Video Overviews.

| Control | Width | Destination |
|---|---|---|
| Sign in to Gemini Notebook | both | same login URL as header Sign in |
| Get the app | 390 only, visible | https://notebook.google.com/download?from=trynow |

Get the app does not open a store page. It redirects back to `/trynow` with `utm_source=nlm_web`, `utm_medium=google_oo`, and `utm_campaign=download_action`. That return is the same marketing page. It was not photographed again.

## Footer

Two links, both widths. No newsletter field. No social row.

| Control | Destination |
|---|---|
| Google | https://www.google.com/ (already captured as systems/google; not opened) |
| Privacy & Terms | https://policies.google.com/ (off this product; not opened) |

## Phone width

At 390 the header drops Sign in. Get the app is an outlined pill. Sign in to Gemini Notebook is the filled pill under it. The footer is the same two links. There is no menu.

## Login and signup

Sign in is the empty Google Accounts wall. The field was empty. Stopped there.

| Control | Where it goes | What was on screen |
|---|---|---|
| Sign in | accounts.google.com `/v3/signin/identifier`, flow WebLiteSignIn | Email or phone, Forgot email?, Create account, Next. Help, Privacy, Terms, language list. |
| Create account | accounts.google.com `/lifecycle/flows/signup` | Not opened. |
| Forgot email? | accounts.google.com `/signin/usernamerecovery` | Not opened. |
| Next | submits the identifier | Not clicked. |

No account chooser appeared. No identity provider was on the wall. A hidden password input exists in the DOM and was not shown. The photographed URL carries a continue parameter back to NotebookLM and a `dsh` value. The shots show the empty wall only.

Dark theme was not painted on the public page. The signed-in package already has dark and light app screenshots from 2026-10-17. Those were not recaptured.
