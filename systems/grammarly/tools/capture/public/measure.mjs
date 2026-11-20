// Measures grammarly.com's components on its public pages, in every state
// that can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home features plans grammar-check contact-sales signin mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// grammarly.com's marketing site is a Next.js app on the GDS token layer
// (--color-*/--button-*/--space-*/--radius-* plus the newer --origin-* set).
// Classes are CSS modules: base-module_basic__<hash> (the rounded buttons),
// header-global_*, tabs_tabLabel_*, form_input_*, card_card_*,
// tools-secondary-nav_*; the gds-* classes that ship with the token CSS do
// not appear in the public DOM.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   open/selected  a resting state reached by the page's own UI toggles — a
//                  nav menu button, a feature tab, the mobile sheet's Open
//                  button (the /plans page paints no billing switch, so that
//                  component records `missing` instead of a state)
//   anything else  a resting state reached by the page itself; nothing that
//                  submits a form, signs in or starts a trial is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, chromium, open, patch, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/', features: '/features', plans: '/plans',
  'grammar-check': '/grammar-check', 'contact-sales': '/contact/sales',
  signin: '/signin',
};

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, wait = 6000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  if (!(await open(page, BASE + URLS[key], { wait }))) {
    // a bot check that never cleared: the page runner fails and records nothing for it
    throw new Error('bot check never cleared: recorded as a boundary, not measured');
  }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(400);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

// Clicks a UI toggle (tab, segment, accordion summary, menu button). Refuses
// a submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|submit|sign in|log in|create|generate|upload|sign up|try|start|apply|get|talk|book|subscribe|request|resend|continue|accept|reject|insert|copy)/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= {});
  // A rerun replaces the component's evidence wholesale: old states from a list
  // the current run no longer measures would otherwise linger, and a `missing`
  // flag from an earlier failed run would survive a successful recapture.
  c.states = {};
  delete c.missing;
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  return c;
}

async function measure(key, state, target, opts = {}) {
  // opts.hidden targets an element that is in the DOM but unpainted (display:
  // none) — filtering it visible again would make its declared slot unreadable.
  const loc = opts.hidden ? target.first() : target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false && !opts.hidden) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

const FILL = 'A short note about the launch';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (opts.open) { await reset(); await opts.open(); }
  const loc = opts.hidden ? target.first() : target.filter({ visible: true }).first();
  if (!(await loc.count())) { log('  ! missing', key); out.components[key].missing = true; return; }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
      } else if (opts.stateOpen?.[st]) {
        await opts.stateOpen[st](loc);
        via = via || 'the page\'s own control';
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', buttons: 'Buttons', pricing: 'Pricing',
  features: 'Feature pages', tools: 'Writing tools', checker: 'Grammar checker',
  form: 'Forms', footer: 'Footer', overlay: 'Dialogs and overlays',
  content: 'Content and cards', mobile: 'Mobile (390 wide)',
};

// The site header's own menu button (Product): a UI toggle, no navigation.
async function openNavMenu() {
  const b = page.locator('header').locator('button, a').filter({ hasText: /^Product$/ }).first();
  await b.click();
  await page.waitForTimeout(900);
}
async function closeNavMenu() {
  await page.keyboard.press('Escape');
  await page.mouse.click(720, 500).catch(() => {});
  await page.waitForTimeout(500);
}

// ---------- home: shell, buttons, cards ----------
async function home() {
  await newPage('home');
  const g = G.shell;
  await S('header', q('header, ' + M('header-global_headerStickyWrapper')).first(), ['default'], { group: g, title: 'Top nav', desc: 'The fixed bar over every page: the Grammarly lockup, the Product/Work/Education/Resources menu buttons, the Pricing link, then Request a demo, Log in and the Sign Up pill.', sel: 'header-global_headerStickyWrapper' }, { noScroll: true });
  await S('brand', q('a' + M('headerItemLogo_') + ', header a'), ['default'], { group: g, title: 'Brand lockup', desc: 'The Grammarly mark + wordmark link in the nav start.', sel: 'a.headerItemLogo_*' }, { noScroll: true });
  const menuBtn = q('header').locator('button, a').filter({ hasText: /^Product$/ }).first();
  await S('nav-menu-button', menuBtn, B4, { group: g, title: 'Nav menu button', desc: 'A top-level menu trigger (Product): nav text with a chevron; opens the flyout panel.', sel: 'header button:has-text("Product")' }, { noScroll: true });
  await S('nav-panel', q(M('flyout')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown panel', desc: 'The Product flyout: a floating panel with Learn and Use Grammarly columns of item rows.', sel: 'flyout*' }, { noScroll: true, open: openNavMenu, after: { default: closeNavMenu } });
  // The flyout is hover-driven: the per-state reset moves the mouse away and
  // the panel closes, so re-open it before every state when the item is gone.
  const ensureFlyout = async (loc) => {
    if (!(await loc.isVisible().catch(() => false))) { await openNavMenu().catch(() => {}); }
    return 'Product flyout held open for the state';
  };
  await S('nav-panel-item', q(M('flyout')).filter({ visible: true }).locator('a').filter({ visible: true }).first(), B4, { group: g, title: 'Nav dropdown item', sel: 'flyout* a' }, { noScroll: true, open: openNavMenu, before: { default: ensureFlyout, hover: ensureFlyout, 'focus-visible': ensureFlyout, pressed: ensureFlyout }, after: { default: closeNavMenu, hover: closeNavMenu, 'focus-visible': closeNavMenu, pressed: closeNavMenu } });
  await S('nav-link', q('header').locator('a').filter({ hasText: /^Pricing$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain text link in the bar (Pricing).', sel: 'header a:has-text("Pricing")' }, { noScroll: true });
  await S('nav-demo', q('header').locator('a, button').filter({ hasText: /Request a demo/ }).first(), B4, { group: g, title: 'Request a demo link', desc: 'The secondary text link in the nav end. Measured, never followed.', sel: 'header :text("Request a demo")' }, { noScroll: true });
  await S('nav-login', q('header').locator('a').filter({ hasText: /^Log in$/ }).first(), B4, { group: g, title: 'Log in link', desc: 'The plain sign-in link in the nav end. Measured, never followed.', sel: 'header a:has-text("Log in")' }, { noScroll: true });
  await S('nav-signup', q('header').locator('a, button').filter({ hasText: /Sign Up/ }).first(), B4, { group: g, title: 'Sign Up (nav)', desc: 'The green pill in the nav end. Measured, never followed.', sel: 'header :text("Sign Up")' }, { noScroll: true });

  const b = G.buttons;
  await S('btn-hero', q('main, [role="main"], body').locator('a, button').filter({ hasText: /Sign up.*free/ }).filter({ visible: true }).first(), B4, { group: b, title: 'Primary button (hero)', desc: 'The large green button under the hero ("Sign up It\'s free"): the brand fill, radius 6-ish, trailing arrow. Measured, never followed.', sel: 'a:has-text("Sign up")' });
  await S('btn-google', q('a, button').filter({ hasText: /Sign up with Google/ }).filter({ visible: true }).first(), B4, { group: b, title: 'Secondary button (Google)', desc: 'The bordered white button beside the primary CTA ("Sign up with Google"): hairline border, the G mark, same radius. Measured, never followed.', sel: ':text("Sign up with Google")' });
  await S('btn-carousel', q('button' + M('carousel_navButton') + '[aria-label="Next"]'), B4, { group: b, title: 'Carousel arrow button', desc: 'The round Next arrow on the feature carousel (the Previous arrow sits collapsed at the start of the strip).', sel: 'button.carousel_navButton*[aria-label="Next"]' });

  const c = G.content;
  await S('hero', q('h1').first(), ['default'], { group: c, title: 'Hero title', desc: 'The page\'s display line ("Think big. We\'ll take care of the details."): Matter, large size, tight tracking.', sel: 'h1' });
  await S('hero-lede', q('h1').first().locator('xpath=following::*[self::p or self::div][normalize-space()][1]'), ['default'], { group: c, title: 'Hero lede', desc: 'The supporting line under the hero title.', sel: 'h1 + *' });
  await S('feature-card', q(M('card_card__')).filter({ visible: true }).first(), B4, { group: c, title: 'Feature card', desc: 'A card in the capability carousel ("Paragraph rewrites", "Tone suggestions"): a screenshot tile over a title and a lede, on the page ground.', sel: 'card_card__*' });
  await S('stat-card', q(M('scrollable-content_cardLinkWrapper')).filter({ visible: true }).first(), B4, { group: c, title: 'Customer stat card', desc: 'A linked card in the dark enterprise strip ("20 days saved annually per user"): dark fill, a stat, a name. Measured, never followed.', sel: 'scrollable-content_cardLinkWrapper*' });
  await S('banner', q(M('banner-component_banner')).filter({ visible: true }).first(), ['default'], { group: c, title: 'Promo banner', desc: 'The dark banner aside ("Try Grammarly Pro for free"): dark fill, white text and a pale CTA.', sel: 'banner-component_banner*' });
  // The dark enterprise strip carries bg-colors_darkThemeTextColor_* on the
  // page-section element itself (not on a descendant), and mounts lazily —
  // scroll it in before the presence check.
  await S('section-dark', q(M('page-section_') + M('bg-colors_darkThemeTextColor')).first(), ['default'], { group: c, title: 'Dark section', desc: 'A marketing section painted dark (bg-colors_darkThemeTextColor_*): ink ground with light text, reached without a theme switch.', sel: 'page-section_*.bg-colors_darkThemeTextColor_*' }, { open: async () => { await q(M('bg-colors_darkThemeTextColor')).first().scrollIntoViewIfNeeded().catch(() => {}); await page.waitForTimeout(800); } });
  await S('link-legal', q('a').filter({ hasText: /Terms and Conditions/ }).filter({ visible: true }).first(), B4, { group: c, title: 'Inline link', desc: 'A text link inside body copy ("Terms and Conditions" under the hero buttons).', sel: 'a:has-text("Terms")' });

  const f = G.footer;
  await S('footer', q('footer, ' + M('footerContainer_')).first(), ['default'], { group: f, title: 'Footer', desc: 'The site foot: link columns, the legal bar and the social icons.', sel: 'footerContainer_*' });
  await S('footer-link', q('footer a, ' + M('footerContainer_') + ' a').filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', sel: 'footer a' });
}

// ---------- plans: plan cards, CTAs, compare table ----------
async function plans() {
  await newPage('plans');
  const g = G.pricing;
  // As captured, /plans paints three plan columns with no Monthly/Yearly
  // billing switch (the toggle classes that appeared in older markup are
  // absent). billing-switch is kept in the spec and records `missing` so the
  // gap is explicit rather than silently dropped.
  const tog = q(M('toggleInput_')).first();
  await S('billing-switch', tog, ['default'], { group: g, title: 'Billing period switch', desc: 'The Monthly/Yearly toggle that used to sit above the plan cards. Not present in the captured /plans markup — recorded as a gap.', sel: 'toggleInput_*' });
  // The plan columns mount as [class*="planBoxContainer_"] inside
  // [class*="boxItemsContainer_"]; all three report "Most popular" in hidden
  // copy, so the featured card is picked by its price instead.
  await S('plan-grid', q(M('boxItemsContainer_')).first(), ['default'], { group: g, title: 'Plan grid', desc: 'The three-column plans list: Free, Pro (marked Most popular), Enterprise.', sel: 'boxItemsContainer_*' });
  const boxes = q(M('planBoxContainer_'));
  await S('plan-card', boxes.filter({ hasText: '$12' }).first(), ['default'], { group: g, title: 'Plan card (featured)', desc: 'The Pro column ($12 USD/month as captured): the "Most popular" green header bar, the price, the Try-for-free tag and its CTAs.', sel: 'planBoxContainer_* with $12' });
  await S('plan-card-plain', boxes.filter({ hasText: 'Free' }).first(), ['default'], { group: g, title: 'Plan card (plain)', desc: 'The Free column: quiet card next to the featured one.', sel: 'planBoxContainer_* first' });
  await S('sticker-tag', q(M('freeTagText_')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Try-for-free tag', desc: 'The small tag beside the Pro price ("Try for free"): a pill tag with its own fill.', sel: 'freeTagText_*' });
  const inPlans = async () => { await boxes.first().scrollIntoViewIfNeeded().catch(() => {}); await page.waitForTimeout(400); };
  await S('plan-cta-primary', boxes.locator('a, button').filter({ hasText: /Try for \$0|Try Grammarly Pro|Try for free/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA (primary)', desc: 'The green CTA inside the Pro card. Measured, never followed.', sel: 'planBoxContainer_* :text("Try for $0.00")' }, { before: { default: inPlans, hover: inPlans, 'focus-visible': inPlans, pressed: inPlans } });
  await S('plan-cta-secondary', boxes.locator('a, button').filter({ hasText: /Create account|Contact Sales/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA (secondary)', desc: 'The bordered CTA in a plan card (Create account / Contact Sales). Measured, never followed.', sel: 'planBoxContainer_* :text("Create account"), :text("Contact Sales")' }, { before: { default: inPlans, hover: inPlans, 'focus-visible': inPlans, pressed: inPlans } });
  // The Compare Plans table mounts lazily below the fold; scroll it in first.
  const scrollBottom = async () => { await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.7)); await page.waitForTimeout(1500); };
  await S('info-icon-button', q('button.gds-icon-button-medium, button[aria-label="More information"]').filter({ visible: true }).first(), B4, { group: g, title: 'Info icon button', desc: 'The round "More information" icon button beside a row in the Compare Plans table.', sel: 'button.gds-icon-button-medium' }, { before: { default: scrollBottom, hover: scrollBottom, 'focus-visible': scrollBottom, pressed: scrollBottom } });
  // The FAQ block mounts as [class*="questions_"] with one div row per
  // question, below the compare table — scroll it in via `open` (which runs
  // before the presence check).
  const scrollFaq = async () => { await page.getByText('Frequently Asked Questions').first().scrollIntoViewIfNeeded().catch(() => scrollBottom()); await page.waitForTimeout(1500); };
  const acc = q('[class$="-questions"]').locator('> div').filter({ visible: true }).first();
  await S('faq-item', acc, ['default'], { group: g, title: 'FAQ accordion item', desc: 'A question row in the plans FAQ ("What will happen to my Premium subscription if I switch to Pro?"): a labelled row with a chevron that opens the answer. Never opened.', sel: '[class$="-questions"] > div' }, { open: scrollFaq });
}

// ---------- features: tabs ----------
async function features() {
  await newPage('features');
  const g = G.features;
  await S('tab-list', q('[role="tablist"], ' + M('tabs_tabLabels') + ', ' + M('tabList_')).first(), ['default'], { group: g, title: 'Feature tab list', desc: 'The pill tabs over the feature demos (Paragraph rewrites, Proofreading, ...): a row of labelled tabs.', sel: '[role=tablist] / tabs_tabLabels_*' });
  const tab = q('button[role="tab"]').filter({ hasText: /^Proofreading$/ }).filter({ visible: true }).first();
  await S('tab', q('button[role="tab"]').filter({ hasText: /^Paragraph rewrites$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature tab', desc: 'One tab in the feature list. Measured and selected only through the tab itself.', sel: 'button[role=tab].tabs_tabLabel_*' });
  await S('tab-selected', tab, ['default'], { group: g, title: 'Feature tab, selected', desc: 'The same tab measured after the page\'s own tab was pressed: the selected pill.', sel: 'tabs_tabLabel*' }, { before: { default: async (loc) => { await loc.click({ timeout: 4000 }); await page.waitForTimeout(800); return 'the page\'s own tab pressed (a UI toggle)'; } } });
}

// ---------- grammar-check: tools nav, editor, suggestions ----------
async function grammarCheck() {
  await newPage('grammar-check');
  const g = G.tools;
  await S('tools-nav', q(M('tools-secondary-nav_banner')).first(), ['default'], { group: g, title: 'Tools secondary nav', desc: 'The sticky strip under the header on the free tools (Grammar Check, Plagiarism Checker, Paraphrasing Tool, ...): icon + label links, the current tool underlined.', sel: 'tools-secondary-nav_*' });
  await S('tools-nav-item', q(M('tools-secondary-nav_banner')).locator('a').filter({ visible: true }).first(), B4, { group: g, title: 'Tools nav item', desc: 'One item in the tools strip; the first is the current page.', sel: 'tools-secondary-nav_* a' });

  const c = G.checker;
  const ed = q('[contenteditable="true"], textarea').filter({ visible: true }).first();
  await S('checker', q(M('checker')).filter({ visible: true }).first(), ['default'], { group: c, title: 'Checker frame', desc: 'The free grammar checker: a two-column panel — the editor on the left, the Suggestions rail on the right.', sel: 'checker frame' });
  await S('checker-editor', ed, ['default', 'focused'], { group: c, title: 'Editor area', desc: 'The writing area with the "Start writing here" placeholder: a large bordered field.', sel: '[contenteditable]' }, { fieldLoc: ed });
  // The right rail: for a fresh signed-out visit it paints a "Let's get
  // started" onboarding card (contentContainer_*); live suggestion cards are
  // rendered by the product overlay (shadow DOM) and never enter the light DOM,
  // so suggestion-card stays a recorded gap.
  await S('suggestions-panel', q(M('contentContainer_')).filter({ hasText: /get started/i }).filter({ visible: true }).first(), ['default'], { group: c, title: 'Suggestions rail (onboarding)', desc: 'The right rail of the free checker: the Suggestions header and the three-step "Let\'s get started" card shown to signed-out visitors.', sel: 'contentContainer_* (get started)' });
  await S('getting-started', q(M('getStartedList_')).filter({ visible: true }).first(), ['default'], { group: c, title: 'Get-started steps', desc: 'The numbered steps inside the rail\'s onboarding card ("Add your text...", "Hover over the underlines...", "Click a suggestion...").', sel: 'getStartedList_*' });
  // checker-filled: recorded as a boundary, not measured. Typed text is sent to
  // Grammarly's server checker, so the editor is read at rest only (checker-editor).
  // Deliberately strict: `suggestion*` alone matches the rail's header label
  // (a false positive). The real card classes don't mount for a signed-out
  // visitor, so this records `missing` — an honest gap.
  await S('suggestion-card', q(M('suggestionCard_') + ', ' + M('suggestion-card')).filter({ visible: true }).first(), ['default'], { group: c, title: 'Suggestion card', desc: 'A suggestion card in the rail (issue type, fix, Accept/Dismiss). The checker\'s issue underlines and cards are painted by a product overlay outside the page\'s light DOM; nothing matched in the signed-out run — recorded as a gap.', sel: 'suggestionCard_*' });
  await S('checker-cta', q('a, button').filter({ hasText: /Get Grammarly/ }).filter({ visible: true }).first(), B4, { group: c, title: 'Get Grammarly CTA', desc: 'The green CTA in the Suggestions rail. Measured, never followed.', sel: ':text("Get Grammarly")' });
  await S('copy-button', q('button, a').filter({ hasText: /^Copy text$/ }).filter({ visible: true }).first(), B4, { group: c, title: 'Copy text button', desc: 'The quiet button over the editor that copies the field\'s text (present in the DOM but collapsed when the editor\'s helper footer is hidden). Measured, never pressed.', sel: ':text("Copy text")' });
}

// ---------- contact-sales: the form ----------
async function contactSales() {
  await newPage('contact-sales');
  const g = G.form;
  await S('form', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact sales form', desc: 'The lead form ("Contact our Sales team"): labelled required fields, selects and the Submit button.', sel: 'form' });
  await S('form-label', q('label, ' + M('form_label')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Field label', desc: 'A field caption ("Work email*"): small text over the input.', sel: 'label' });
  const inp = q(M('form_input_')).filter({ visible: true }).first();
  await S('form-input', inp, ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'A single-line input in the sales form: hairline border, placeholder only via the label. Text was typed and deleted; nothing sent.', sel: 'form_input_*' }, { fieldLoc: inp });
  await S('form-select', q(M('form_select_')).filter({ visible: true }).first(), B4, { group: g, title: 'Select', desc: 'A dropdown in the sales form (institution type, product, country): same field skin with a chevron. Never opened.', sel: 'form_select_*' });
  await S('form-submit', q('button[type="submit"], button').filter({ hasText: /^Submit$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The form\'s green Submit. Measured, never pressed.', sel: 'button:has-text("Submit")' });
}

// ---------- signin: the dialog ----------
async function signin() {
  await newPage('signin');
  const g = G.overlay;
  // The sign-in card mounts as `main form` (form-module_formContainer_*);
  // `[class*="signin"]` classes name inner rows, not the card itself.
  await S('signin-dialog', q('main form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The account card on /signin ("Sign in" with the email field and the provider buttons). Shot and measured, never submitted.', sel: 'main form' });
  const inp = q('input[type="email"], input[name*="email" i], ' + M('base-module_input')).filter({ visible: true }).first();
  await S('signin-email', inp, ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The sign-in email input: hairline border with the Email label inside. Text was typed and deleted; nothing sent.', sel: 'input[type=email] or base-module_input*' }, { fieldLoc: inp, fillText: 'name@example.com' });
  await S('signin-continue', q('button').filter({ hasText: /^Continue$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The dialog\'s green primary. Measured, never pressed.', sel: 'button:has-text("Continue")' });
  await S('signin-provider', q('button, a').filter({ hasText: /Sign in with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Provider button', desc: 'A social sign-in row (Google, Facebook, Apple, SSO): bordered, icon left, chevron right. Measured, never followed.', sel: ':text("Sign in with Google")' });
  await S('signin-help-link', q('button, a').filter({ hasText: /Can't sign in|don't have an account/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Troubleshoot link', desc: 'The quiet link under the primary ("Can\'t sign in?") and the "I don\'t have an account" link. Measured, never followed.', sel: ':text("Can\'t sign in")' });
}

// ---------- mobile (390) ----------
async function mobile() {
  await newPage('home', { mobile: true });
  const g = G.mobile;
  await S('m-header', q('header, ' + M('header-global_headerStickyWrapper')).first(), ['default'], { group: g, title: 'Top nav (mobile)', desc: 'The 390-wide header: lockup and the menu button.', sel: 'header' }, { noScroll: true });
  await S('m-menu-button', q('button[aria-label*="navigation menu" i], ' + M('openButton_')).first(), B4, { group: g, title: 'Menu button', desc: 'The icon button that opens the mobile navigation sheet.', sel: 'openButton_*' }, { noScroll: true });
  await S('m-menu', q(M('headerMobileMenu_')).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu', desc: 'The open navigation sheet at 390: the link list and the sign-in row.', sel: 'headerMobileMenu_*' }, { noScroll: true, open: async () => { await q('button[aria-label*="navigation menu" i], ' + M('openButton_')).first().click(); await page.waitForTimeout(1200); }, after: { default: async () => { await q(M('closeButton_')).first().click().catch(() => {}); await page.waitForTimeout(600); } } });
  await S('m-hero-btn', q('a, button').filter({ hasText: /Sign up.*free/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Primary button (mobile)', desc: 'The hero CTA at 390.', sel: ':text("Sign up")' });
}

const RUNNERS = { home, plans, features, 'grammar-check': grammarCheck, 'contact-sales': contactSales, signin };
const wanted = process.argv.slice(2);
const browser = await chromium.launch();
context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
run = new Date().toISOString();
out._meta.captured = run;
out._meta.url = BASE;
out._meta.read = run.slice(0, 10);
out._meta.via = 'tools/capture/public/measure.mjs: computed styles + element crops from live pages, signed out';
for (const key of Object.keys(RUNNERS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  try { await RUNNERS[key](); } catch (e) { log('!! page failed', key, String(e.message).split('\n')[0]); }
  save();
  await page.close().catch(() => {});
}
// The mobile group runs in its own context at 390 with the phone UA and touch.
if (!wanted.length || wanted.includes('mobile')) {
  await context.close();
  context = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
  await patch(context);
  try { await mobile(); } catch (e) { log('!! page failed mobile', String(e.message).split('\n')[0]); }
  save();
}
save();
await browser.close();
const n = Object.values(out.components).reduce((a, c) => a + Object.keys(c.states || {}).length, 0);
console.log('done:', Object.keys(out.components).length, 'components,', n, 'states ->', OUT);
