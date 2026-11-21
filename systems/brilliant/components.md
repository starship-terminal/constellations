# Components

Public controls measured on 2026-11-21, signed out. The earlier signed-in inventory is in [components.signed-in-2026-10.md](components.signed-in-2026-10.md).

## Button, learner

The homepage "I'm a learner" control is a transparent button. The painted face is an inner span: `rgb(41, 204, 87)`, white label, 60px radius, 47px tall, and a 4px lip `rgb(21, 180, 65)`. Desktop width 218px. Phone width 350px. See [home-light-default](screenshots/public-2026-11/home-light-default.png).

## Button, parent or teacher

Same structure. Face `rgb(255, 255, 255)`, label `rgba(0, 0, 0, 0.4)`, lip `rgb(220, 218, 216)`.

## Button, Sign in

Outline button on the homepage nav. 1px `rgb(228, 228, 228)`, 54px radius, 36px tall, 14px CoFo Brilliant. On the login page the submit face is `rgb(229, 229, 229)` on a `#141414` page, 56px radius, 48px tall, 448px wide.

## Text field

Login fields are 52px tall, 448px wide, 8px radius. Email border `2px solid rgb(229, 229, 229)`. Password border `2px solid rgba(255, 255, 255, 0.2)`. Placeholders were "Email or username" and "Password". Both values were empty. See [login-dark-empty](screenshots/public-2026-11/login-dark-empty.png).

The signup wall shows one empty Email field. Password, name, and age fields exist in the DOM and stay hidden until later steps. Those steps were not taken.

## Link

Footer and body links use `--panda-colors-text-link` (`#456DFF`) where they are blue. Homepage body links on the oat surface are dark.

## Tabs

The homepage "Level" tablist has Foundations, Algebra, Calculus, Probability and Statistics, and Mind-Bending Math. Algebra was selected. The courses page has a subject strip: Math, Basic Algebra, Algebra, and the rest. Phone width turns that strip into a horizontal scroller. See [courses-dark-phone](screenshots/public-2026-11/courses-dark-phone.png).

## Card

Course rows on `/courses/` sit on `#141414` with a title, a gray description, and a green NEW badge on some rows. Pricing plan cards use an iridescent frame from `--panda-gradients-hue-shift-upgrade-iridescent-primary`.

## Badge

NEW is a small green pill on course titles. MOST POPULAR is a purple pill on the Annual pricing tab.

## Not measured this pass

Select, checkbox, radio, switch, toast, dialog (other than the cookie host, which was hidden), tooltip, avatar, menu, and icon button. The homepage nav has no hamburger. Sign in and Get started are the only nav controls.
