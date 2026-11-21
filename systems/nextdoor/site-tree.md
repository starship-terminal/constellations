# Nextdoor public site tree

Mapped from the homepage at https://nextdoor.com/ in headless Playwright on 2026-11-21, before screenshots, at 1440 x 900. A control that opens a login or signup wall is recorded and that branch stops. Nothing was typed or submitted. Google, Facebook and Apple were not clicked. Tracking query strings are stripped from this file.

## Homepage

https://nextdoor.com/ loads as a public marketing page (HTTP 200, title Nextdoor). The hero is a signup card. The rest of the page (header menus, feature copy, footer) is public and is the root of this tree.

| Control | Opens | What happens |
|---|---|---|
| Partners | menu | Publishers, Public agencies |
| Businesses | menu | Small-business and industry marketing pages |
| Log in | https://nextdoor.com/login/ | Wall. Email or mobile number, password, or Google, Facebook, Apple. Stop. |
| Sign up | signup card on the same page | Wall. Email, password, Continue, Google, Apple. Stop. |
| Continue with Google | Google OAuth | Not clicked. |
| Continue with Apple | Apple OAuth | Not clicked. |
| Email address / Create a password / Continue | signup submit | Not typed, not submitted. |
| toggle password visibility | shows the password field | Not used. |
| Have a business? Get started | https://nextdoor.com/create-business | Wall. Stop. |
| Have an invite code? | https://nextdoor.com/join | Wall. Stop. |
| Join Nextdoor | signup card | Wall. Stop. |
| Create Business / Your business name | signup card | Not filled. |
| Privacy Policy | https://help.nextdoor.com/s/article/Privacy-Policy-2026 | Public legal page. |
| Cookie Policy | https://help.nextdoor.com/s/article/Cookie-Policy-2026 | Public legal page. |
| Member Agreement | https://help.nextdoor.com/s/article/Member-Agreement-US-2026 | Public legal page. |
| About | https://about.nextdoor.com/ | Public. |
| News | https://about.nextdoor.com/press-releases | Public. |
| Media Assets | https://about.nextdoor.com/us-media | Public. |
| Investor Relations | https://investors.nextdoor.com/ | Public. |
| Blog | https://blog.nextdoor.com/ | Public. |
| Careers | https://about.nextdoor.com/careers | Public. |
| Help | https://help.nextdoor.com/s/topic-page?topicName=Neighbor | Public help center. |
| Get Started (Neighbors) | https://nextdoor.com/choose_address/ | Wall. Address join. Stop. |
| Events | https://nextdoor.com/events/calendar/ | Redirects to https://nextdoor.com/login/?next=/events/calendar/. Stop. |
| Neighborhoods | https://nextdoor.com/find-neighborhood/ | Public index. Search not submitted. |
| Guidelines | https://help.nextdoor.com/s/article/community-guidelines | Public. |
| Small Business | https://business.nextdoor.com/en-us/small-business | Public. |
| Brands and Media Agencies | https://business.nextdoor.com/en/en-us/enterprise | Public. |
| Public Agencies | https://about.nextdoor.com/public-agency | Public. |
| Publishers | https://about.nextdoor.com/publishers | Public. |
| Businesses on Nextdoor | https://nextdoor.com/directories/ | Public directory index. |
| For Developers | https://developer.nextdoor.com/ | Public. |
| Agencies on Nextdoor | https://nextdoor.com/agencies/ | Public. |
| Home & Garden | https://business.nextdoor.com/en-us/small-business/industry/home-garden | Public. Redirects to the resources industry page. |
| Real Estate | https://business.nextdoor.com/en-us/resources/industry/real-estate | Public. |
| Professional Services | https://business.nextdoor.com/en-us/resources/industry/professional-services | Public. |
| Food & Entertainment | https://business.nextdoor.com/en-us/resources/industry/food-and-beverage | Public. |
| Shopping & Retail | https://business.nextdoor.com/en-us/resources/industry/retail | Public. |
| Medical & Dental | https://business.nextdoor.com/en-us/small-business/industry/medical-dental | Public industry page. |
| Privacy | https://nextdoor.com/privacy_policy/ | Redirects to the help-center privacy article. |
| Legal & Terms | https://help.nextdoor.com/s/topic-page?topicName=Legal | Public. |
| Cookies | https://nextdoor.com/cookie_policy/ | Redirects to the help-center cookie article. |
| Self-Service Ad Terms | https://nextdoor.com/self-service-advertising-terms-of-service/ | Public legal page. |
| Get the app | App Store | Off-site. Not followed. |

## Walls (branch stops)

| From | Control | URL | Why it stops |
|---|---|---|---|
| https://nextdoor.com/ | Log in | https://nextdoor.com/login/ | Asks for email or mobile number and password, or Google, Facebook, or Apple. Branch stops. |
| https://nextdoor.com/ | Sign up | https://nextdoor.com/ | Scrolls to the homepage signup card (email, password, Continue, Google, Apple). Not submitted. |
| https://nextdoor.com/ | Continue with Google | https://accounts.google.com/ | OAuth. Not clicked. |
| https://nextdoor.com/ | Continue with Apple | https://appleid.apple.com/ | OAuth. Not clicked. |
| https://nextdoor.com/ | Continue | https://nextdoor.com/ | Submits the signup card. Not clicked. |
| https://nextdoor.com/ | Join Nextdoor | https://nextdoor.com/ | Signup card. Not clicked. |
| https://nextdoor.com/ | Create Business | https://nextdoor.com/ | Business-name field on the signup card. Not filled. |
| https://nextdoor.com/ | Get started (business) | https://nextdoor.com/create-business | Business page claim. Signup wall. Not opened. |
| https://nextdoor.com/ | Have an invite code? | https://nextdoor.com/join | Invite-code join. Signup wall. Not opened. |
| https://nextdoor.com/ | Get Started (neighbors) | https://nextdoor.com/choose_address/ | Address join. Signup wall. Not opened. |
| https://nextdoor.com/login/ | Continue with Facebook | https://www.facebook.com/ | OAuth. Not clicked. |
| marketing pages | Create Your Business Page | https://nextdoor.com/create-business | Signup wall. Not opened. |
| marketing pages | Advertise Now | https://ads.nextdoor.com/v2/signup | Ads signup wall. Not opened. |
| about.nextdoor.com | Log in | https://nextdoor.com/login/ | Header login. Branch stops. |

## Public pages the homepage reaches

| URL | Role | Note |
|---|---|---|
| https://nextdoor.com/ | Homepage | Public marketing page with an embedded signup card. Card not used. |
| https://about.nextdoor.com/ | About | Footer About. Public. |
| https://about.nextdoor.com/press-releases | News / press | Footer News. Public. |
| https://about.nextdoor.com/us-media | Media assets | Footer Media Assets. Public. |
| https://about.nextdoor.com/careers | Careers | Footer Careers. Public. |
| https://about.nextdoor.com/public-agency | Public agencies | Footer and Partners menu. Public. |
| https://about.nextdoor.com/publishers | Publishers | Partners menu. Public. |
| https://blog.nextdoor.com/ | Blog | Footer Blog. Public. |
| https://investors.nextdoor.com/ | Investor relations | Footer Investor Relations. Public. |
| https://help.nextdoor.com/s/topic-page | Help | Footer Help. Public help center. |
| https://help.nextdoor.com/s/article/Privacy-Policy-2026 | Privacy | Footer Privacy. Public. |
| https://help.nextdoor.com/s/article/Cookie-Policy-2026 | Cookies | Footer Cookies. Public. |
| https://help.nextdoor.com/s/article/Member-Agreement-US-2026 | Member agreement | Signup-card link. Public legal page. |
| https://help.nextdoor.com/s/article/community-guidelines | Guidelines | Footer Guidelines. Public. |
| https://nextdoor.com/directories/ | Businesses on Nextdoor | Footer directory index. Public. |
| https://nextdoor.com/agencies/ | Agencies on Nextdoor | Footer. Public. |
| https://nextdoor.com/find-neighborhood/ | Neighborhoods | Footer Neighborhoods. Public search page. Query not submitted. |
| https://business.nextdoor.com/en-us/small-business | Small business | Footer and Businesses menu. Public. |
| https://business.nextdoor.com/en/en-us/enterprise | Brands and agencies | Footer and Businesses menu. Public. |
| https://business.nextdoor.com/en-us/resources/industry/home-garden | Home and garden | Footer industry. Public. |
| https://developer.nextdoor.com/ | Developers | Footer For Developers. Public. |
| https://nextdoor.com/events/calendar/ | Events | Footer Events. Redirects to login. Wall. |

## Capture set

Screenshots cover the homepage and the distinct public surfaces a signed-out visitor can open without a form: about, press, careers, help, one legal page, small business, enterprise, public agency, developers, directories, agencies, neighborhoods, and one industry page. Industry pages share one template, so one stands for the set. Blog, investor relations and the help center are the same public family. Login, join, choose-address, create-business, ads signup and the homepage signup card are walls and are not captured as filled forms.

## Interactions that stay on the page

| Page | Control | Result |
|---|---|---|
| Homepage | Partners | Menu: Publishers, Public agencies. |
| Homepage | Businesses | Menu of business marketing links. |
| About and business pages | Newsroom, Partners, Resources | Header menus (javascript:;). Opened in the capture pass where the control is a real menu. |
| Help center | Search | Public search field. Not submitted. |
| Neighborhoods | Search | Public field. Not submitted. |
| Any page | Cookie or consent banner | Hidden, never clicked. |

