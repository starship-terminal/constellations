// Measures headspace.com's components on its public pages, in every state
// that can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [group ...]
//
// Groups: home app subscriptions content redeem auth checkout org mobile.
// Writes raw/components-computed.json (merged, so a subset of groups can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 600ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   opened         a resting state reached by the component's own toggle: the
//                  header's hover mega-menu, the phone's nav sheet
//   focused        a text field clicked into — nothing is typed
// Nothing is typed, sent, bought, redeemed or signed into. The only presses
// are local UI toggles the page's own chrome provides.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, ORG, CHECKOUT, M, open, closePromo, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  app: BASE + '/app',
  meditation: BASE + '/meditation',
  sleep: BASE + '/sleep',
  therapy: BASE + '/online-therapy',
  coaching: BASE + '/coaching',
  ebb: BASE + '/ai-mental-health-companion',
  'mental-health': BASE + '/mental-health',
  anxiety: BASE + '/mental-health/anxiety',
  science: BASE + '/science',
  about: BASE + '/about-us',
  articles: BASE + '/articles',
  article: BASE + '/articles/can-you-use-hsa-or-fsa-for-mental-health',
  content: BASE + '/content',
  topic: BASE + '/content/topics/100',
  subscriptions: BASE + '/subscriptions',
  family: BASE + '/family-plan',
  gift: BASE + '/buy/gift',
  share: BASE + '/share-headspace',
  redeem: BASE + '/code',
  'mindful-families': BASE + '/app/mindful-families',
  login: BASE + '/login',
  signup: BASE + '/signup',
  'org-home': ORG + '/',
  'org-employers': ORG + '/employers',
  checkout: CHECKOUT + '/checkout',
};

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  // Force :active:hover on the component element itself, never the topmost
  // node at its centre (a text span or an svg), so the component's own
  // :active rule applies (2026-11 audit, finding 12-6; not run since).
  await cdp.send('DOM.getDocument').catch(() => {});
  await loc.evaluate((el) => el.setAttribute('data-press-target', '1'));
  try {
    const { result } = await cdp.send('Runtime.evaluate', { expression: `document.querySelector('[data-press-target]')`, returnByValue: false });
    // an unresolved target throws, so the state records an error instead of
    // a resting reading labelled pressed
    if (!result || !result.objectId) throw new Error('press target not resolvable');
    const { nodeId } = await cdp.send('DOM.requestNode', { objectId: result.objectId });
    if (!nodeId) throw new Error('press target has no DOM node');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(400);
    return nodeId;
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-press-target')).catch(() => {});
  }
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'focused' | { name, via, fn }.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'opened': 'the component\'s own UI toggle' };

// A real pointer hover opens the header's hover mega-menu; the pane's links
// are never followed.
const menuHover = async () => {
  const cat = page.locator('header a[data-testid="navbar-category-link"]').filter({ visible: true }).first();
  const b = await cat.boundingBox();
  if (!b) throw new Error('no category link to hover');
  await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2);
  await page.waitForTimeout(1400);
};

const CHROME = [
  { key: 'nav-promo-strip', group: 'Marketing chrome', title: 'Promo strip',
    desc: 'The banner over the header ("Feel your best for 50% off →").',
    sel: 'header + div / [data-testid*="promo" i]', find: (p) => p.locator('header').first().locator('xpath=preceding::*[self::div or self::section or self::aside][1]').first(), states: ['default'] },
  { key: 'nav-header', group: 'Marketing chrome', title: 'Header bar',
    desc: 'The top bar: logo, the For You / For Business / For Providers / Our Plans / Resources / About categories, Log in, Help and the Get-50%-off CTA.',
    sel: 'header', find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'nav-logo', group: 'Marketing chrome', title: 'Logo link',
    desc: 'The headspace wordmark image in the header.',
    sel: 'header a[data-testid="logo-link"]', find: (p) => p.locator('header a[data-testid="logo-link"]').first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-category', group: 'Marketing chrome', title: 'Nav category link',
    desc: 'A top-level header link ("For You"): hovering it opens the mega-menu.',
    sel: 'header a[data-testid="navbar-category-link"]', find: (p) => p.locator('header a[data-testid="navbar-category-link"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-mega-menu', group: 'Marketing chrome', title: 'Mega-menu pane (open)',
    desc: 'The dropdown pane of subcategory links under a hovered category. "opened" is a real pointer hover on the category link; the pane is read while the pointer rests inside it.',
    sel: 'header a[data-testid="navbar-subcategory-link"] pane', find: async (p) => {
      await menuHover();
      const sub = p.locator('header a[data-testid="navbar-subcategory-link"]').filter({ visible: true }).first();
      return sub.locator('xpath=ancestor::*[self::div or self::nav or self::ul][position()<=6]').last();
    }, states: [{ name: 'opened', via: 'a real pointer hover on the header category link — the pane\'s links were never followed', fn: menuHover }] },
  { key: 'nav-subcategory', group: 'Marketing chrome', title: 'Mega-menu link',
    desc: 'One link inside the open mega-menu ("Meditation" under For You).',
    sel: 'header a[data-testid="navbar-subcategory-link"]', find: async (p) => {
      await menuHover();
      return p.locator('header a[data-testid="navbar-subcategory-link"]').filter({ visible: true }).first();
    }, states: [{ name: 'opened', via: 'the category link\'s own hover state, menu open', fn: async () => {} }, 'hover'] },
  { key: 'nav-cta', group: 'Marketing chrome', title: 'Header CTA ("Get 50% off")',
    desc: 'The pill call-to-action in the header, measured, never followed.',
    sel: 'header a (text Get 50% off|Get started)', find: async (p) => await domFind(p, /get 50% off|get started|try (headspace|free)/i, { sel: 'header a, header button', tag: 'ncta', minW: 60, minH: 24, notInside: 'dialog, [role="dialog"]' }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'nav-login', group: 'Marketing chrome', title: '"Log in" link',
    desc: 'The sign-in link in the header, measured, never followed.',
    sel: 'header a (text Log in)', find: async (p) => await domFind(p, /^\s*log in\s*$/i, { sel: 'header a', tag: 'nli', minW: 20 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'footer', group: 'Marketing chrome', title: 'Footer',
    desc: 'The page footer: link columns, app-store badges, the language selector and legal links.',
    sel: 'footer', find: (p) => p.locator('footer').first(), states: ['default'] },
  { key: 'footer-link', group: 'Marketing chrome', title: 'Footer link',
    desc: 'A link in a footer column.',
    sel: 'footer a', find: (p) => p.locator('footer a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'footer-language', group: 'Marketing chrome', title: 'Language selector',
    desc: 'The footer\'s locale button ("English"). Measured at rest — its option list was never opened.',
    sel: 'footer button|a (text English)', find: async (p) => await domFind(p, /^\s*(english|deutsch|español|français|português)\s*$/i, { sel: 'footer button, footer a, footer [role="button"]', tag: 'lang', minW: 30 }), states: ['default', 'hover'] },
  { key: 'footer-app-badge', group: 'Marketing chrome', title: 'App-store badge',
    desc: 'The App Store / Google Play badge links in the footer.',
    sel: 'footer a[href*="apple"], footer a[href*="play.google"], footer img[alt*="app" i]', find: (p) => p.locator('footer a[href*="apple"], footer a[href*="play.google"], footer img[alt*="app store" i]').first(), states: ['default'] },
];

const HERO = [
  { key: 'hero-h1', group: 'Hero and type', title: 'Hero headline (h1)',
    desc: 'The page\'s display headline in Headspace Apercu.',
    sel: 'main h1, h1', find: (p) => p.locator('main h1, h1').filter({ visible: true }).first(), states: ['default'] },
  { key: 'hero-lede', group: 'Hero and type', title: 'Hero lede',
    desc: 'The paragraph under the hero headline.',
    sel: 'main h1 + p / first main p', find: async (p) => {
      const h1 = p.locator('main h1, h1').filter({ visible: true }).first();
      return h1.locator('xpath=following::p[1]').first();
    }, states: ['default'] },
  { key: 'hero-cta', group: 'Hero and type', title: 'Hero primary CTA',
    desc: 'The pill call-to-action inside the hero ("Get 50% off" / "Get started"), measured, never followed.',
    sel: 'main a|button (text Get 50% off|Get started|Try)', find: async (p) => await domFind(p, /get 50% off|get started|try headspace|try free|start free/i, { sel: 'main a, main button', tag: 'hcta', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'prose-h2', group: 'Hero and type', title: 'Section heading (h2)',
    desc: 'A mid-page section headline.',
    sel: 'main h2', find: (p) => p.locator('main h2').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-h3', group: 'Hero and type', title: 'Card heading (h3)',
    desc: 'A card or feature heading.',
    sel: 'main h3', find: (p) => p.locator('main h3').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-body', group: 'Hero and type', title: 'Body copy',
    desc: 'A body paragraph.',
    sel: 'main p', find: (p) => p.locator('main p').filter({ visible: true }).first(), states: ['default'] },
  { key: 'prose-link', group: 'Hero and type', title: 'Inline text link',
    desc: 'A link inside body copy.',
    sel: 'main p a, main li a', find: (p) => p.locator('main :is(p,li) a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
];

const WIDGETS = [
  { key: 'feature-card', page: 'home', group: 'Marketing widgets', title: 'Feature/benefit card',
    desc: 'A rounded card on the home page (benefit or content tile).',
    sel: 'main [class*="card" i], main article', find: (p) => p.locator('main [class*="card" i], main article').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'testimonial', page: 'home', group: 'Marketing widgets', title: 'Testimonial/press quote',
    desc: 'A quote or press-mention block on the home page.',
    sel: 'main blockquote, [class*="testimonial" i], [class*="quote" i]', find: (p) => p.locator('main blockquote, main [class*="testimonial" i], main [class*="quote" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'app-tab', page: 'app', group: 'Marketing widgets', title: 'Feature tab',
    desc: 'A numbered feature tab on /app ("1 Guided meditations", "2 AI guidance", ...). Its own activation is a local UI toggle.',
    sel: 'main button (text Guided meditations|AI guidance)', find: async (p) => await domFind(p, /guided meditations|ai guidance|sleep resources|expert-led/i, { sel: 'main button, main [role="tab"]', tag: 'atab', minW: 40 }), states: ['default', 'hover'] },
  { key: 'plan-card', page: 'subscriptions', group: 'Marketing widgets', title: 'Plan card',
    desc: 'A subscription plan card on /subscriptions (radius 12, cream fill).',
    sel: 'main [class*="card" i], main li', find: (p) => p.locator('main [class*="card" i], main article').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'plan-switch', page: 'subscriptions', group: 'Marketing widgets', title: 'Billing switch',
    desc: 'The monthly/annual switch control on /subscriptions (role switch or checkbox name="switch"), measured at rest — never toggled.',
    sel: 'input[name="switch"], [role="switch"]', find: (p) => p.locator('input[name="switch"], [role="switch"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'plan-slider', page: 'subscriptions', group: 'Marketing widgets', title: 'Seat slider',
    desc: 'A range input on the plans page (member-count slider), measured at rest — never dragged.',
    sel: 'input[type="range"]', find: (p) => p.locator('input[type="range"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'subscribe-button', page: 'content', group: 'Marketing widgets', title: '"Subscribe" button',
    desc: 'The subscribe action on a plan/upsell card, measured, never pressed.',
    sel: 'button|a (text Subscribe)', find: async (p) => await domFind(p, /^\s*subscribe\s*$/i, { sel: 'main button, main a', tag: 'sub', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'content-tile', page: 'content', group: 'Marketing widgets', title: 'Content preview tile',
    desc: 'A meditation/music/sleep preview tile on /content. Never played.',
    sel: 'main [class*="card" i], main article, main [class*="tile" i]', find: (p) => p.locator('main [class*="card" i], main article, main [class*="tile" i]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'play-button', page: 'content', group: 'Marketing widgets', title: 'Preview play button',
    desc: 'A play control on a preview tile or audio row. Never pressed — previews were not played.',
    sel: 'button[aria-label*="play" i], [class*="play" i] button', find: (p) => p.locator('button[aria-label*="play" i], main [class*="play" i] button, main button[class*="play" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'faq-item', page: 'meditation', group: 'Marketing widgets', title: 'FAQ accordion row',
    desc: 'A frequently-asked-questions row near the foot of a topic page (a details/summary or button accordion). Measured at rest and opened by its own toggle.',
    sel: 'details, [class*="accordion" i] button, [class*="faq" i] button', find: (p) => p.locator('main details summary, main [class*="accordion" i] button, main [class*="faq" i] button, main [class*="question" i]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'redeem-field', page: 'redeem', group: 'Forms', title: 'Redeem-code field',
    desc: 'The "Enter your code" text input on /code, clicked into — nothing typed.',
    sel: 'input[name="Redeem Field"], input[placeholder*="code" i]', find: (p) => p.locator('input[name="Redeem Field"], input[placeholder*="code" i]').filter({ visible: true }).first(), states: ['default', 'focused', 'focus-visible'] },
  { key: 'redeem-button', page: 'redeem', group: 'Forms', title: '"Redeem code" button',
    desc: 'The submit on /code, measured, never pressed.',
    sel: 'button (text Redeem)', find: async (p) => await domFind(p, /redeem/i, { sel: 'main button', tag: 'rdm', minW: 60 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'newsletter-field', page: 'home', group: 'Forms', title: 'Newsletter email field',
    desc: 'The footer\'s email input, clicked into — nothing typed.',
    sel: 'input[type="email"]', find: (p) => p.locator('input[type="email"]').filter({ visible: true }).first(), states: ['default', 'focused'] },
];

const AUTH = [
  { key: 'auth-card', group: 'Auth surface', title: 'Auth card',
    desc: 'The centred card on auth.headspace.com (the universal login).',
    sel: 'main, [class*="widget" i], form', find: (p) => p.locator('main, [class*="widget" i], form').filter({ visible: true }).first(), states: ['default'] },
  { key: 'auth-email', group: 'Auth surface', title: 'Email field',
    desc: 'The email input on the universal login, clicked into — nothing typed.',
    sel: 'input[type="email"], input[name="username"]', find: (p) => p.locator('input[type="email"], input[name="username"]').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'auth-continue', group: 'Auth surface', title: '"Continue" button',
    desc: 'The primary submit on the universal login, measured, never pressed.',
    sel: 'button (text Continue)', find: async (p) => await domFind(p, /^continue$/i, { sel: 'button, [role="button"]', tag: 'ac', minW: 60 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'auth-sso', group: 'Auth surface', title: '"Continue with SSO" button',
    desc: 'The secondary SSO submit, measured, never pressed.',
    sel: 'button (text SSO)', find: async (p) => await domFind(p, /sso|google|apple/i, { sel: 'button, [role="button"], a', tag: 'asso', minW: 60 }), states: ['default', 'hover'] },
];

const CHECKOUT_SPECS = [
  { key: 'checkout-form', group: 'Checkout', title: 'Checkout panel',
    desc: 'The self-serve checkout surface (plan picker or payment form) as it paints without a voucher — viewed only, nothing filled or submitted.',
    sel: 'main, form', find: (p) => p.locator('main, form').filter({ visible: true }).first(), states: ['default'] },
  { key: 'checkout-field', group: 'Checkout', title: 'Checkout field',
    desc: 'An input on the checkout surface (email or plan option), measured at rest.',
    sel: 'main input', find: (p) => p.locator('main input').filter({ visible: true }).first(), states: ['default'] },
  { key: 'checkout-button', group: 'Checkout', title: 'Checkout button',
    desc: 'The primary action on the checkout surface, measured, never pressed.',
    sel: 'main button', find: (p) => p.locator('main button, main [role="button"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
];

const ORG_SPECS = [
  { key: 'org-h1', group: 'B2B surface', title: 'B2B hero headline',
    desc: 'The organizations.headspace.com hero h1.',
    sel: 'main h1, h1', find: (p) => p.locator('main h1, h1').filter({ visible: true }).first(), states: ['default'] },
  { key: 'org-cta', group: 'B2B surface', title: 'B2B CTA',
    desc: 'The business-surface call-to-action ("Request a demo" / "Get started"), measured, never followed.',
    sel: 'a|button (text demo|Get started|Contact)', find: async (p) => await domFind(p, /demo|get started|contact|learn more/i, { sel: 'header a, main a, header button, main button', tag: 'octa', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'org-card', group: 'B2B surface', title: 'B2B card',
    desc: 'A card on the B2B surface (stat, benefit or customer logo tile).',
    sel: 'main [class*="card" i], main article', find: (p) => p.locator('main [class*="card" i], main article').filter({ visible: true }).first(), states: ['default'] },
];

const MOBILE = [
  { key: 'm-nav-header', group: 'Marketing chrome (mobile)', title: 'Mobile header',
    desc: 'The bar at 390px: logo and the nav button.', sel: 'header',
    find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'm-nav-button', group: 'Marketing chrome (mobile)', title: 'Nav button',
    desc: 'The button that opens the nav sheet.', sel: 'header button',
    find: (p) => p.locator('header button, header [role="button"]').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'm-nav-sheet', group: 'Marketing chrome (mobile)', title: 'Nav sheet (open)',
    desc: 'The opened navigation sheet. The nav button\'s own press happens in find(); the state itself is a no-op.',
    sel: 'header nav sheet', find: async (p) => {
      const ham = p.locator('header button, header [role="button"]').filter({ visible: true }).first();
      await ham.tap({ timeout: 5000 }).catch(() => ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click())));
      await p.waitForTimeout(1600);
      return p.locator('header nav, header [class*="menu" i], [class*="drawer" i], [role="dialog"]').filter({ visible: true }).first();
    }, states: [{ name: 'opened', via: 'the nav button\'s own press — the sheet\'s links were never followed', fn: async () => {} }] },
  { key: 'm-hero-cta', group: 'Marketing widgets (mobile)', title: 'Mobile hero CTA',
    desc: 'The hero call-to-action at 390px, measured, never followed.',
    sel: 'main a|button (text Get 50% off|Get started)', find: async (p) => await domFind(p, /get 50% off|get started|try headspace/i, { sel: 'main a, main button', tag: 'mhcta', minW: 60, minH: 24 }), states: ['default'] },
];

const GROUPS = {
  home: { page: 'home', specs: [...CHROME, ...HERO, ...WIDGETS.filter((w) => w.page === 'home')] },
  app: { page: 'app', specs: WIDGETS.filter((w) => w.page === 'app') },
  meditation: { page: 'meditation', specs: [...HERO.slice(0, 1), ...WIDGETS.filter((w) => w.page === 'meditation')] },
  sleep: { page: 'sleep', specs: HERO.slice(0, 1) },
  therapy: { page: 'therapy', specs: HERO.slice(0, 1) },
  coaching: { page: 'coaching', specs: HERO.slice(0, 1) },
  ebb: { page: 'ebb', specs: HERO.slice(0, 1) },
  'mental-health': { page: 'mental-health', specs: HERO.slice(0, 1) },
  anxiety: { page: 'anxiety', specs: HERO.slice(0, 1) },
  science: { page: 'science', specs: HERO.slice(0, 1) },
  about: { page: 'about', specs: HERO.slice(0, 1) },
  articles: { page: 'articles', specs: HERO.slice(0, 1) },
  article: { page: 'article', specs: HERO },
  topic: { page: 'topic', specs: HERO.slice(0, 1) },
  content: { page: 'content', specs: WIDGETS.filter((w) => w.page === 'content') },
  subscriptions: { page: 'subscriptions', specs: WIDGETS.filter((w) => w.page === 'subscriptions') },
  family: { page: 'family', specs: HERO.slice(0, 1) },
  gift: { page: 'gift', specs: HERO.slice(0, 1) },
  share: { page: 'share', specs: HERO.slice(0, 1) },
  redeem: { page: 'redeem', specs: WIDGETS.filter((w) => w.page === 'redeem') },
  'mindful-families': { page: 'mindful-families', specs: HERO.slice(0, 1) },
  auth: { page: 'login', specs: AUTH },
  'auth-signup': { page: 'signup', specs: AUTH.slice(0, 2) },
  checkout: { page: 'checkout', specs: CHECKOUT_SPECS },
  org: { page: 'org-home', specs: ORG_SPECS },
  'org-employers': { page: 'org-employers', specs: ORG_SPECS.slice(0, 2) },
  mobile: { page: 'home', mobile: true, specs: MOBILE },
};

// The group that owns each spec key's bare name: the first group listing it.
const KEY_OWNER = {};
for (const [gk, gg] of Object.entries(GROUPS)) for (const sp of gg.specs) KEY_OWNER[sp.key] ??= gk;

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); headspace.com paints light only — there is no theme control anywhere signed out';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const url = URLS[g.page];
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 8000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[g.page] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (let spec of g.specs) {
    // One key per page, fixed by GROUPS order: a spec key listed by several
    // groups belongs to the FIRST group that lists it (home's hero-h1, the
    // /login auth-card) and every other group writes it under its own prefix
    // (meditation-hero-h1), whatever an earlier run saved. (2026-11 audit;
    // not run since.)
    if (KEY_OWNER[spec.key] !== key) spec = { ...spec, key: `${key}-${spec.key}` };
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    // Page attribution only lands when the element was actually found on this
    // page: a failed rerun keeps the page/url of the run that measured the
    // saved states instead of renaming another page's readings.
    comp.page = g.page;
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      let pressed = null;
      try {
        await reset();
        let viaText = 'resting state';
        if (st === 'hover') { await hover(loc); viaText = via.hover; }
        else if (st === 'focus-visible') { await kbFocus(loc); viaText = via['focus-visible']; }
        else if (st === 'focused') { await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into — nothing typed'; }
        else if (st === 'pressed') { pressed = await pressOn(loc); viaText = via.pressed; }
        else if (st && typeof st === 'object' && st.fn) { await st.fn(loc); viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(loc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(loc).catch(() => {});
        const v = await styleOf(loc);
        v.via = viaText;
        v.page = g.page;
        v.url = safeUrl(url);
        v.crop = await crop(page, loc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
      }
    }
    save();
  }
  await page.close();
}
await b.close();
log('done ->', OUT);
