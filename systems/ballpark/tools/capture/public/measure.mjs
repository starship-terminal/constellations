// Measures ballparkhq.com's public components in every state reachable without
// signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// ballparkhq.com is a Framer site in one light theme; components are found by
// role, landmark, cursor:pointer structure or stable text — the framer-*
// classes are build hashes, never selected. Nothing is sent, downloaded or
// signed into: the only presses are local UI toggles — the Solutions nav menu
// and the mobile menu. "Book a demo", "Sign in", the plan CTAs, the sign-in
// OAuth links, the Coach widget's submit and the contact form's "Submit
// request" are measured in all states except followed or pressed for real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', contact: '/contact/sales', signin: '/sign-in' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
// Pages that actually loaded this run (not blocked): readings may only be
// pruned for components on one of these — a blocked route must not erase
// evidence captured earlier.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
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
  await open(page, BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key);
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
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
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
  contact: 'Contact sales', signin: 'Sign in', footer: 'Footer', mobile: 'Mobile (390 wide)',
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

// Marks the Coach demo widget's submit, its box and its ask field.
const markCoachFn = () => {
  const btn = [...document.querySelectorAll('button')].find((n) => /submit/i.test((n.innerText || '') + (n.getAttribute('aria-label') || '') + (n.getAttribute('name') || '') + (n.getAttribute('data-framer-name') || '')));
  if (!btn) return false;
  btn.setAttribute('data-m-coach-submit', '1');
  let box = btn;
  for (let i = 0; i < 6 && box; i++, box = box.parentElement) if (box.querySelector('input, textarea')) break;
  if (box && box !== btn) box.setAttribute('data-m-coach', '1');
  const inp = box && box.querySelector('input, textarea');
  if (inp) inp.setAttribute('data-m-coach-field', '1');
  return !!(inp);
};

// Marks the first stories-carousel page dot.
const markDotFn = () => {
  const b = [...document.querySelectorAll('button')].find((n) => /scroll to page/i.test((n.innerText || '') + (n.getAttribute('aria-label') || '') + (n.getAttribute('data-framer-name') || '')));
  if (!b) return false;
  b.setAttribute('data-m-dot', '1');
  return true;
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The two-row bar under the announcement strip: logo, the nav (Platform, Solutions, Templates, Pricing), Sign in and the black Book a demo pill.', sel: 'header' }, { noScroll: true });
  await S('announcement-bar', q('a[href*="claude"]').first(), B4, { group: g, title: 'Announcement bar', desc: 'The "NEW · Ballpark is now available in Claude" banner over the header: a centred pill link with a coral NEW chip. Measured, never followed.', sel: 'a[href*="claude"]' }, { noScroll: true });
  await S('logo', q('header a').filter({ hasText: /^Ballpark$/ }).first(), ['default'], { group: g, title: 'Logo', sel: 'header a:has-text("Ballpark")' }, { noScroll: true });
  const navA = (t) => q('header a, nav a').filter({ hasText: t }).first();
  await S('nav-link', navA(/^Platform$/), B4, { group: g, title: 'Nav link', sel: 'a:has-text("Platform")' }, { noScroll: true });
  const sol = navA(/^Solutions$/);
  await S('nav-solutions', sol, B4, { group: g, title: 'Solutions menu link', desc: 'The nav item that opens the mega menu of solutions pages on hover.', sel: 'a:has-text("Solutions")' }, { noScroll: true });
  await S('nav-solutions-open', sol, ['opened'], { group: g, title: 'Solutions menu, open', desc: 'The link after its own hover opens the menu; the crop holds the opened panel region.', sel: 'a:has-text("Solutions")' }, { noScroll: true, noToggle: true, before: { opened: async (l) => { await l.hover(); await page.waitForTimeout(1400); return 'own hover opens the mega menu'; } }, cropLoc: q('header') });
  await page.keyboard.press('Escape'); await page.mouse.move(700, 500); await page.waitForTimeout(500);
  await S('nav-signin', navA(/^Sign in$/), B4, { group: g, title: 'Sign in link', desc: 'The secondary action on the right of the nav. Measured, never followed.', sel: 'a:has-text("Sign in")' }, { noScroll: true });
  await S('nav-cta', navA(/^Book a demo$/), B4, { group: g, title: 'Book a demo button', desc: 'The black pill on the right of the nav. Measured, never followed.', sel: 'a:has-text("Book a demo")' }, { noScroll: true });
  await S('intercom-launcher', q('div[role="button"][aria-label*="Intercom" i]'), B4, { group: g, title: 'Intercom launcher', desc: 'The round chat bubble Intercom mounts at the bottom-right of every page (third-party widget).', sel: 'div[role="button"][aria-label*="Intercom"]' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: '"Research without the complexity" in the site\'s display face (Inter Display).', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1').first().locator('xpath=following::*[self::p or self::div][string-length(normalize-space())>40][1]'), ['default'], { group: h, title: 'Hero subcopy', sel: 'first long paragraph under h1' }, { noScroll: true });
  await S('section-title', q('h2').first(), ['default'], { group: h, title: 'Section title', sel: 'first h2' });
  // The scroll sweep marks the Coach demo's parts when they mount; when the
  // widget is absent the S() calls record an explicit missing entry rather
  // than silently claiming coverage.
  await scrollFind(markCoachFn);
  await S('coach-widget', q('[data-m-coach]'), ['default', 'hover'], { group: h, title: 'Coach demo widget', desc: 'The working "Ask Coach" demo box on the home page: the product\'s chat UI with an "Ask me anything…" field and a round submit.', sel: 'Coach box (marked in-page)' }, { noScroll: true });
  await S('coach-field', q('[data-m-coach-field]'), ['default', 'focused', 'filled'], { group: h, title: 'Coach ask field', desc: 'The demo\'s ask field. The box paints a fake field (a Framer div, not an input or textarea), so the entry is recorded missing when the sweep finds no real input.', sel: 'input inside the Coach box' });
  await S('coach-submit', q('[data-m-coach-submit]'), B4, { group: h, title: 'Coach send button', desc: 'The round send button inside the demo. Measured, never pressed.', sel: 'button:has-text("Submit")' });
  if (await scrollFind(markDotFn)) {
    await S('carousel-dot', q('[data-m-dot="1"]'), B4, { group: h, title: 'Carousel page dot', desc: 'The pagination dots of the stories carousel ("Scroll to page 1"…).', sel: 'button:has-text("Scroll to page")' }, { noScroll: true });
  } else {
    await S('carousel-dot', q('button').filter({ hasText: /scroll to page/i }), B4, { group: h, title: 'Carousel page dot', desc: 'The pagination dots of the stories carousel ("Scroll to page 1"…).', sel: 'button:has-text("Scroll to page")' }, { noScroll: true });
  }
  await page.evaluate(() => scrollTo(0, 0)); await page.waitForTimeout(600);
  const card = q('a[href*="/features/"], a[href*="./features/"]').filter({ visible: true }).first();
  await S('feature-card', card, B4, { group: h, title: 'Feature card', desc: 'A tall image card linking a feature page (live interviews, creative testing, …). Measured, never followed.', sel: 'a[href*="features/"]' });
  await S('cta-request', q('a').filter({ hasText: /^Request a demo$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Request a demo button', desc: 'The closing CTA over the footer ("Try Ballpark with your team"). Measured, never followed.', sel: 'a:has-text("Request a demo")' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  const planBtn = q('main a, section a').filter({ hasText: /demo|trial|started|sales|contact/i }).filter({ visible: true }).first();
  await S('plan-cta', planBtn, B4, { group: g, title: 'Plan CTA', desc: 'The action inside an enterprise plan card. Measured, never followed.', sel: 'a:has-text("demo|trial") inside a plan card' });
  // The card is the smallest ancestor that actually paints its own surface —
  // a background, a ring shadow or a border. A wider transparent container
  // (the two-card row is ~768px) would measure empty air around the card.
  await page.evaluate(() => {
    const a = [...document.querySelectorAll('main a, section a')].find((n) => /demo|trial|started|sales|contact/i.test(n.innerText || '') && n.getBoundingClientRect().width > 0);
    if (!a) return;
    // The card is the outermost ancestor that still paints its own surface —
    // a background, a ring shadow or a border — within card bounds. A wider
    // transparent container (the two-card row is ~768px) or an inner painted
    // band would measure the wrong box.
    let card = null;
    for (let n = a, i = 0; n && i < 8; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 700 || r.height > 1000) break;
      if (r.width >= 300 && r.height >= 140) {
        const c = getComputedStyle(n);
        if (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || c.boxShadow !== 'none' || parseFloat(c.borderTopWidth) > 0) card = n;
      }
    }
    (card || a.parentElement || a).setAttribute('data-m-plan-card', '1');
  });
  await S('plan-card', q('[data-m-plan-card="1"]'), ['default'], { group: g, title: 'Plan card', sel: 'card ancestor of a plan CTA (marked in-page)' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('contact-title', q('h1, h2').first(), ['default'], { group: g, title: 'Contact title', sel: 'h1/h2' }, { noScroll: true });
  const flds = q('main input, form input, input').filter({ visible: true });
  await S('contact-field', flds.first(), ['default', 'focused', 'filled'], { group: g, title: 'Contact field', desc: 'A short text field of the sales form (first/last name pair); sample text was typed and deleted, nothing sent.', sel: 'input[type=text]' });
  const wide = flds.nth(2);
  await S('contact-email', wide, ['default', 'focused'], { group: g, title: 'Contact email field', desc: 'The wider field under the name pair (work email); focused only, nothing typed.', sel: 'wide input' });
  await S('contact-message', q('textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Message textarea', desc: 'The form\'s message box; focused only, nothing typed.', sel: 'textarea' });
  await S('contact-submit', q('button').filter({ hasText: /submit request/i }).first(), B4, { group: g, title: 'Submit request button', desc: 'The form\'s black submit. Measured, never pressed.', sel: 'button:has-text("Submit request")' });
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-title', q('h1, h2').first(), ['default'], { group: g, title: 'Sign-in title', sel: 'h1/h2' }, { noScroll: true });
  await S('signin-google', q('a').filter({ hasText: /continue with google/i }).first(), B4, { group: g, title: 'Continue with Google', desc: 'The OAuth link. Measured, never followed — no sign-in was attempted.', sel: 'a:has-text("Continue with Google")' });
  await S('signin-sso', q('a').filter({ hasText: /continue with sso/i }).first(), B4, { group: g, title: 'Continue with SSO', desc: 'The SSO link. Measured, never followed.', sel: 'a:has-text("Continue with SSO")' });
  const flds = q('input').filter({ visible: true });
  await S('signin-field', flds.first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The sign-in email field; sample text was typed and deleted, nothing sent.', sel: 'input' });
  await S('signin-password', flds.nth(1), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password field; focused only — nothing was typed into it.', sel: 'input' });
  await S('signin-submit', q('button').filter({ hasText: /continue with email/i }).first(), B4, { group: g, title: 'Continue with email button', desc: 'The email sign-in submit. Measured, never pressed.', sel: 'button:has-text("Continue with email")' });
  await S('signin-forgot', q('a').filter({ hasText: /forgot password/i }).first(), B4, { group: g, title: 'Forgot password link', sel: 'a:has-text("Forgot password")' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep another page's
  // readings under the wrong url.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q('footer a[href*="linkedin" i], footer a[href*="twitter" i], footer a[href*="x.com" i], footer a[href*="youtube" i]').first(), B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
    await S('footer-rating', q('footer a[href*="g2.com" i]').first(), B4, { group: g, title: 'G2 rating badge', desc: 'The "4.6 Star Rating" badge linking the G2 review page. Measured, never followed.', sel: 'footer a[href*="g2.com"]' });
    await S('footer-legal', q('footer a').filter({ hasText: /privacy|terms|dpa|security/i }).first(), B4, { group: g, title: 'Legal link', sel: 'footer a:has-text("Privacy")' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header' }, { noScroll: true });
  const marked = await page.evaluate(() => {
    const h = document.querySelector('header');
    if (!h) return false;
    const cand = [...h.querySelectorAll('div,button')].filter((n) => {
      const r = n.getBoundingClientRect(); const c = getComputedStyle(n);
      return r.width >= 28 && r.width <= 48 && r.height >= 28 && r.height <= 48 && r.x > 280 && c.cursor === 'pointer';
    });
    if (!cand[0]) return false;
    cand[0].setAttribute('data-m-menu', '1');
    return true;
  });
  const menuBtn = q('[data-m-menu="1"]');
  if (marked) {
    await S('m-menu-button', menuBtn, ['default', 'pressed'], { group: g, title: 'Mobile menu button', desc: 'The 36px trigger at the right of the mobile bar; its own press opens the menu overlay.', sel: 'header div[cursor=pointer] at right' }, { noScroll: true });
    await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The trigger after its own toggle; the open overlay shows in the crop.', sel: 'header menu trigger' }, { noScroll: true, cropLoc: q('body') });
    await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  }
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, contact, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components on a page that actually opened this run: a blocked
    // or unvisited route keeps its earlier readings (write new captures first,
    // prune old outputs only after a complete run).
    if (!touched.has(key) && !pages.length) { if (opened.has(c.page)) delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
