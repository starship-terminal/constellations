# Patterns

Public signed-out surfaces only. No screenshots: the preview browser did not paint frames.

## App shell

At 1440 by 900 CSS pixels the navigation aside is 240px wide and full height, black, on the left. The top bar is 48px (`--desktop-navbar-height`). Log in sits at y 14, height 32. Create a free account is the white pill to its right. Download TIDAL is the same secondary pill to the left of Log in.

At 390 by 844 the aside width computed 0. A fixed bar at the bottom is 56px tall (`bottom: 0`). Its tabs are Home, Feed, Search, My Collection and Upload, 40px targets. Search was the selected tab on Explore, at `rgba(255, 255, 255, 0.1)`. The top action collapses to one white pill, "Log in / Create a free account", 32px, at x 160.

## Marketing page

`https://tidal.com/download` redirects to `https://offer.tidal.com/download`. The h1 "Download TIDAL" is 32px bold Nationale, line-height 38.4px, white, on a black page. The Download and Install links are 50px white buttons, radius 12px, text `rgb(25, 25, 25)`, 16px weight 600. About and Support in the header are 16px weight 600, radius 6px, transparent. Footer links (Privacy Notice, Terms and Conditions) are 12px regular white.

## Login

Log in on the player navigates to the OAuth authorize page. The h1 is "Sign up or log in", 20px bold Nationale. Below it is one email field, a disabled Continue button, the word "or" in `#888F98`, then Continue with Passkey, Continue with Google and Continue with Apple. Those last three are OAuth. They were not clicked.

## Not captured

Search and filtering, empty, loading and error states, a form validation error, a destructive confirmation, and feedback after an action all sit behind an account or behind a control that was not opened. Onboarding that asks for a plan or a card was not started.
