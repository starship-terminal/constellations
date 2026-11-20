# Patterns

Signed-out Twitch, dark, 2026-11-19.

## App shell

The home is a 50px top bar, a left rail of live channels, a featured player, and a grid under "Live on Twitch". The top bar paints transparent. `--color-background-top-nav` (`#451093`) is declared and was not the painted bar. A purple banner sits on the bottom edge: "Join the Twitch community!" with a white Sign Up pill.

![Home](screenshots/home-dark-default.png)

At 390 CSS pixels the rail collapses to an icon strip and the top bar keeps Log In and Sign Up.

![Phone](screenshots/home-dark-phone.png)

## Browse

`/directory` leads with a Browse title, five illustrated category chips (Games, IRL, Music & DJs, Creative, Esports), then Categories and Live Channels. Category tiles are square art with a title and a viewer count. Channel tiles are 16:9 thumbs with a LIVE badge, a title, a name, and pill tags.

![Directory](screenshots/directory-dark-default.png)

![Channels](screenshots/channels-dark-default.png)

![Just Chatting](screenshots/category-dark-default.png)

## Signup wall

`/signup` is one column: email, a phone link, a disabled Continue, then Google, Amazon, and Apple. The form is 488px wide in the 1169px preview. No account was created.

![Signup](screenshots/signup-dark-default.png)

![Signup phone](screenshots/signup-dark-phone.png)

## Search

The top-bar search is a split control: an 8px-radius field joined to a square icon button. Submitting a query was not part of the capture.

## Empty, loading, error

The featured player on the home showed a player error ("This video is either unavailable or not supported in this browser"). That is the player, not an app empty state. The signup page ships an "Email is invalid" paragraph in the idle DOM. It computed the body text colour, not `--color-text-error`. A submitted validation error was not produced, because the form was not filled.

## Not captured

Signed-in chat, a followed channel, settings, and a theme toggle. The player itself does not play in this browser.
