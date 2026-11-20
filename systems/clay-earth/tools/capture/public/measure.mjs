// Measures me.sh's public components in every state reachable without
// signing in, paying or submitting anything. clay.earth 301s to me.sh —
// the Clay product rebranded to Mesh — so every route below is read on
// me.sh, and the catalog records the redirect as provenance.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing signin library mobile (the footer group also runs on
// home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is built
// by build-measurements.mjs.
//
// me.sh is a React marketing app in one DARK theme (the html element paints
// #000; body is transparent); components are found by CSS-module class
// prefix (*_navigationLink, *_signInBtn, *_ctaInner, *_card, *_planPrice —
// the hashed prefixes are stable across loads, the random part is never
// selected). Nothing is sent, bought or signed into: the only presses are
// local UI toggles — the nav dropdowns and the mobile menu. app.me.sh's
// sign-in card is a LIGHT sibling surface measured as a documented
// boundary: the e-mail field is filled with the documented test address
// then cleared, and no Sign-in / Create-account / Get-started / Try-it-free
// action is ever followed or pressed for real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', signin: 'https://app.me.sh/login?signin', library: 'https://library.me.sh/' };
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, /^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
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

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, view, run, url: URLS[current] && new URL(URLS[current], BASE).href }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed state capture must not erase a previous reading: keep it under
    // its own provenance and record the error beside it.
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
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
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'menu held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      out.components[key].states[st] = prev && !prev.error
        ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (nav menu, mobile menu). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Marks the shallowest ancestor of a text leaf whose subtree paints a fill of
// colour `want` (Framer draws a button's fill on a sibling layer, so the
// anchor alone reads transparent). `minY` skips same-text copies in the
// header. Falls back to the leaf. Returns whether anything was marked.
const markFillParent = async (textRe, want, attr, { minY = 0 } = {}) => page.evaluate(([src, flags, a, w, miny]) => {
  const re = new RegExp(src, flags);
  const texts = [...document.querySelectorAll('a,button,div,p,span')].filter((n) => {
    const t = (n.innerText || '').trim();
    const r = n.getBoundingClientRect();
    return re.test(t) && t.length < 60 && r.width > 0 && r.y >= miny;
  });
  const leaf = texts.find((n) => !texts.some((o) => o !== n && n.contains(o))) || texts[0];
  if (!leaf) return false;
  const paints = (n) => getComputedStyle(n).backgroundColor === w;
  for (let n = leaf, i = 0; n && i < 8; i++, n = n.parentElement) {
    if (n.getBoundingClientRect().width > 700) break;
    if (paints(n) || [...n.children].some((k) => paints(k) && k.getBoundingClientRect().width >= 80)) {
      n.setAttribute(a, '1');
      return true;
    }
  }
  leaf.setAttribute(a, '1');
  return true;
}, [textRe.source, textRe.flags, attr, want, minY]);

async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  signin: 'Sign-in page (boundary)', library: 'Library (boundary)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// Scrolls down in steps until fn() (run in-page) reports it found and marked
// its element, or the document ends. Framer mounts a section only while its
// band is near the viewport and unmounts it again when it leaves, so the mark
// has to happen where the element lives, not after a full sweep.
async function scrollFind(fn) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y <= h; y += 550) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await page.waitForTimeout(320);
    if (await page.evaluate(fn)) return true;
  }
  return false;
}

// Clicks the nav "Resources"-style dropdown trigger (a local nav toggle;
// opens the link menu, never navigates). The triggers are BUTTONs sharing
// navigationLink's class, so the first one is marked for the menu read.
const markNavDrop = async () => page.evaluate(() => {
  const el = [...document.querySelectorAll('button[class*="navigationLink"]')].find((n) => n.getBoundingClientRect().y < 80);
  if (!el) return false;
  el.setAttribute('data-m-navdrop', '1');
  return true;
});

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The floating top pill: wordmark left, link list, Sign In right.
  await S('header', q('[class$="_nav"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav pill', desc: 'The floating top nav: wordmark, the Releases/Resources/Company dropdowns, Pricing link and Sign In.', sel: 'div.y0DxmG_nav' }, { noScroll: true });
  await S('logo', q('a[href="https://me.sh/"], a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Mesh wordmark anchor.', sel: 'a[href=me.sh/]' }, { noScroll: true });
  await S('nav-item', q('a[href="/pricing"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain nav link (Pricing).', sel: 'nav a[href=/pricing]' }, { noScroll: true });
  // A dropdown trigger ("Releases"-type button); its own press opens the
  // link menu — the opened state, the panel and a menu item are read while
  // it stays up.
  if (!(await markNavDrop())) log('  ! nav dropdown trigger not found');
  const dropTrg = q('[data-m-navdrop="1"]');
  await S('nav-dropdown', dropTrg, [...B4, 'opened'], { group: g, title: 'Nav dropdown', desc: 'A nav dropdown trigger (the Releases/Resources/Company buttons); its own press opens the link menu (opened state).', sel: 'button.y0DxmG_navigationLink' }, { noScroll: true });
  const menuIsOpen = () => page.evaluate(() => {
    const m = document.querySelector('[role="menu"], [class*="dropdown"], [class*="Dropdown"], [class*="popover"], [class*="Popover"], [class*="menuContent"], [class*="Menu_content"]');
    const r = m && m.getBoundingClientRect();
    return !!(r && r.height > 40 && r.top >= 0 && r.top < 900 && getComputedStyle(m).visibility !== 'hidden' && r.bottom > 0);
  });
  const ensureMenuOpen = async () => {
    if (!(await menuIsOpen())) { await toggle(dropTrg); await page.waitForTimeout(900); }
  };
  const markMenu = () => page.evaluate(() => {
    const cand = [...document.querySelectorAll('[role="menu"], [role="listbox"], [class*="dropdown"], [class*="Dropdown"], [class*="popover"], [class*="Popover"], [class*="menuContent"], [class*="Menu_content"], ul')]
      .filter((n) => { const r = n.getBoundingClientRect(); const cs = getComputedStyle(n); return r.height > 40 && r.width > 100 && r.top > 20 && r.top < 700 && (cs.position === 'absolute' || cs.position === 'fixed') && cs.visibility !== 'hidden' && parseFloat(cs.opacity) > 0; })
      .sort((a, b) => a.querySelectorAll('a').length ? -1 : 1)[0];
    if (!cand) return;
    cand.setAttribute('data-m-panel', '1');
    const item = [...cand.querySelectorAll('a,li,button')].find((n) => n.getBoundingClientRect().height > 10 && (n.innerText || '').trim().length > 1);
    if (item) item.setAttribute('data-m-card', '1');
  });
  await S('menu-panel', q('[data-m-panel="1"]'), ['default'], { group: g, title: 'Nav menu', desc: 'The opened nav dropdown panel, held open by the trigger toggle.', sel: 'dropdown panel under the open trigger' }, { noScroll: true, noReset: true, open: async () => { await ensureMenuOpen(); await markMenu(); } });
  await S('menu-card', q('[data-m-card="1"]'), ['default'], { group: g, title: 'Menu item', desc: 'A link row inside the open nav menu.', sel: 'first link inside the open dropdown' }, { noScroll: true, noReset: true, open: ensureMenuOpen });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('nav-cta', q('[class*="_ctaWrapper"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The "Get Started" action inside the nav pill; links to /start, measured never followed.', sel: '.y0DxmG_ctaWrapper' }, { noScroll: true });
  await S('nav-signin', q('[class*="signInBtn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The "Sign In" action in the nav pill; links to app.me.sh/login, measured never followed.', sel: '.y0DxmG_signInBtn' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Every relationship, organized." — the VerlagCondensed display headline.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1').locator('xpath=following-sibling::p[1]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subcopy', desc: '"Mesh brings together everyone you\'ve ever met…" — the serif lede under the display headline.', sel: 'first p after h1' }, { noScroll: true });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: '"Never miss what matters." — the first section heading (Verlag, 480x48); the hero carries no lede, only the display h1 and an animated stat counter.', sel: 'first h2' }, { noScroll: true });
  await S('stat-counter', q('[class*="animatedDigit"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Stat counter', desc: 'One digit of the animated relationship-count ticker beside the hero (the digits cycle).', sel: '.IQmOHa_animatedDigit' }, { noScroll: true });
  // The white "Get Mesh Free" pill — the inverted CTA on the dark page.
  await S('cta', q('[class*="mainCTA"] [class*="ctaInner"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Get Mesh Free" pill — the painted 205x54 off-white inner of the hero CTA; the anchor links to /start, never followed.', sel: '.IQmOHa_mainCTA .eoWgla_ctaInner' }, { noScroll: true });
  // The bottom-CTA twin at the page foot paints its fill on the outer div
  // (white, 185x52) — the painted ancestor, not the transparent inner.
  await S('cta-bottom', q('[class*="ctaButton"]').filter({ visible: true }).first(), B4, { group: h, title: 'Bottom CTA', desc: 'The "Get Mesh Free" pill closing the page — a white 185x52 button on the #0f0f10 bottom band; never followed.', sel: '.JzsFla_ctaButton' }, { noScroll: true });
  // The feature filter pills (Birthdays/Events/News/…): 480px buttons.
  await S('filter-button', q('[class*="filterButton"]').filter({ visible: true }).first(), B4, { group: h, title: 'Feature pill', desc: 'A feature filter pill (Birthdays/Events/News/…); its press swaps the demo panel — a local toggle.', sel: '._9nEsHa_filterButton_*' });
  // The page ground: body paints transparent; html carries the black fill.
  await S('page-ground', q('html'), ['default'], { group: h, title: 'Page ground', desc: "The html element's own painted fill — the black ground under every section (body itself is transparent).", sel: 'document.documentElement' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-ground', q('main').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing ground', desc: "The pricing page's warm-cream main surface (#f9f8f6) — pricing is a light route on the otherwise-dark site.", sel: 'main' }, { noScroll: true, crop: false });
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: '"Invest in better relationships" — the pricing page display heading.', sel: 'h1' }, { noScroll: true });
  // The 288px plan cards: translucent gray fills on the black page.
  await S('plan-card', q('[class*="_card"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Plan card', desc: 'A plan card (the Personal column); translucent gray fill on black.', sel: '._3K18mq_card' });
  await S('plan-card-popular', q('[class*="_card"][class*="popular"], [class*="popular"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Popular plan card', desc: 'The Team plan card with the Popular tag.', sel: '._3K18mq_card._3K18mq_popular' });
  await S('plan-price', q('[class*="planPrice"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The "Free"/"$10/ month" price line inside a plan card.', sel: '.tnESpa_planPrice' });
  await S('plan-cta', q('[class*="_plan"] [class*="button"], [class*="_card"] [class*="button"]').filter({ hasText: /get started|try it free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The "Get Started" outline action inside the Personal plan card (a button-styled div, 238x44); measured in all non-submitting states, never followed.', sel: '.htJ5kW_button inside a plan card' });
  await S('plan-cta-filled', q('[class*="_popular"] [class*="button"]').filter({ hasText: /try it free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA, filled', desc: 'The filled orange "Try it free" action inside the popular Team card; never pressed for real.', sel: '.htJ5kW_button inside _3K18mq_popular' });
  await S('billing-toggle', q('[class*="toggle"], [class*="Toggle"]').filter({ hasText: /annually|monthly/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Billing toggle', desc: 'The "Pay monthly / Pay annually" switcher above the plan cards (226x40, gray-chip fill); a local toggle, never flipped.', sel: '.iVr8Iq_toggle' });
  await S('plan-name', q('[class*="planLabel"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan label', desc: 'The PERSONAL/PRO/TEAM eyebrow label on a plan card.', sel: '._3K18mq_planLabel' });
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-title', q('[class*="_headline_"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in title', desc: '"Sign in to Mesh" — the 32px headline on the app.me.sh sign-in card, a LIGHT sibling surface (#fcfcfc), a different stack from the dark marketing site.', sel: 'span._headline_*' }, { noScroll: true });
  await S('signin-input', q('input[type="text"], input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'E-mail field', desc: 'The "Enter your email" field; filled with the documented test address then deleted, Sign in with email never pressed.', sel: 'input[type=text]', fillText: 'name@example.com' });
  await S('signin-email-btn', q('[class*="emailLoginBtn"]').filter({ visible: true }).first(), B4, { group: g, title: 'E-mail sign-in', desc: 'The orange "Sign in with email" button — the brand accent on this light surface; never pressed.', sel: '._emailLoginBtn_*' });
  await S('signin-apple', q('[class*="appleBtn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Apple sign-in', desc: 'The "Sign in with Apple" OAuth button; never followed.', sel: '._appleBtn_*' });
  await S('signin-google', q('[class*="googleBtn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Google sign-in', desc: 'The "Sign in with Google" OAuth button (Google blue); never followed.', sel: '._googleBtn_*' });
  await S('signin-toggle', q('[class*="toggleBtn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Create-account toggle', desc: 'The "Create account" switcher on the sign-in card; a local toggle measured never pressed.', sel: '._toggleBtn_*' });
  save();
}

async function library() {
  if (!(await newPage('library'))) return;
  const g = G.library;
  await S('library-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Library title', desc: 'The knowledge-base index heading on library.me.sh — the docs subdomain the Terms/Privacy links land on.', sel: 'h1' }, { noScroll: true });
  await S('library-link', q('a').filter({ visible: true, hasText: /\w{4,}/ }).first(), B4, { group: g, title: 'Library link', desc: 'A link row on the library index (a WordPress stack — wp-block classes); never followed.', sel: 'first link with text' }, { noScroll: true });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document
  // that is actually open.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  await page.evaluate(() => {
    const f = document.querySelector('footer, [role="contentinfo"]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The #0f0f10 footer band: link columns, app links, the legal subfooter.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] a[href="/about"], footer a[href="/about"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a[href=/about]' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] a[href*="x.com" i], [data-m-footer="1"] a[href*="twitter" i], footer a[aria-label*="x" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon link (X).', sel: 'footer a[href*=x.com]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the nav collapses to three fixed pieces — logo, a GET STARTED
  // pill and the hamburger (y0DxmG_toggle) — with no shared bar element, so
  // each is measured on its own. The mobileNav drawer stays transparent
  // and translated off-canvas until the toggle's own press slides it in.
  await S('m-menu-button', q('[class*="_toggle"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The 44x32 hamburger at the bar edge (an icon div, no label); its own press slides the nav drawer in.', sel: '.y0DxmG_toggle' }, { noScroll: true });
  await S('m-cta', q('[class*="_btns"], [class*="mobileNav"] ~ [class*="cta"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The fixed "Get Started" pill in the mobile bar; links to /start, never followed.', sel: '.y0DxmG_btns' }, { noScroll: true });
  const menuBtn = q('[class*="_toggle"]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await toggle(menuBtn); await page.waitForTimeout(1200); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  await S('m-menu-open', q('[class*="mobileNav"]').first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The nav drawer after the hamburger press (fixed, 374x762; it is transparent and translated -187px off-canvas while closed).', sel: '.y0DxmG_mobileNav after toggle press' }, { noScroll: true });
  await S('m-menu-link', q('[class*="mobileNav"] a').filter({ visible: true, hasText: /\w{3,}/ }).first(), B4, { group: g, title: 'Menu link', desc: 'A link row inside the open mobile drawer.', sel: 'first link inside .y0DxmG_mobileNav' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  // The h1 cycles a rotating word — organized / searchable / up to date.
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390 — the final word rotates (organized / searchable / up to date).', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), dark theme (sign-in card is a light sibling)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, signin, library, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components whose page+viewport visit actually opened this
    // run: a blocked route (or a blocked mobile pass of a route the desktop
    // pass captured) keeps its earlier readings. Components saved before the
    // view field existed fall back to the m- prefix for their variant.
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has(c.page + '|' + cview)) delete out.components[key];
      continue;
    }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
