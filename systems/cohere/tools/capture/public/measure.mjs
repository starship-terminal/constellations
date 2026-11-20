// Measures cohere.com's public components in every state reachable
// without signing in, paying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing north signin mobile (the footer group also runs
// on home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is
// built by build-measurements.mjs.
//
// cohere.com is a Next.js (App Router)/Tailwind v3 + Sanity CMS build in one
// LIGHT theme: a custom config palette baked into utilities (pureBlack/
// pureWhite, surface-*, volcanic/coral/mushroom/marble/quartz/onyx, neutral-*,
// the web3-* type scale), group/*-named classes, ease-button-gradient CTA
// pills and aria-labels carry the selectors. A dismissible fixed promo banner
// (bg-pureBlack, "Close banner") mounts over the header — measured as real
// chrome. CookieYes mounts a "Manage Cookies" revisit button
// (.cky-banner-element) — hidden by closePromo, never answered.
// dashboard.cohere.com/welcome/login is the product's sign-in boundary: its
// card is measured, never submitted — the email field gets a focus reading
// only (nothing typed, nothing sent). The only presses are local UI toggles —
// the pricing model-category tabs are read at rest, never switched; the
// mobile menu button opens its own overlay.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', north: '/north', command: '/command', signin: 'https://dashboard.cohere.com/welcome/login' };
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

async function newPage(key, { mobile = false, wait = 8000, dsf } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: dsf ?? 2, userAgent: UA, locale: 'en-US' });
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
        else { await toggle(opts.toggleLoc || loc); await page.waitForTimeout(900); via = 'own toggle'; }
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
  north: 'North product page', command: 'Command model page', signin: 'App sign-in (boundary)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The fixed top nav (z-nav): the h-[60px] inner bar holds the Cohere mark,
  // the group/nav-link roll-hover links, a transparent "Sign in" and the
  // dark "Request a demo" ease-button-gradient pill. The fixed promo banner
  // (bg-pureBlack) sits above it and carries its own close button.
  await S('promo-banner', q('div.bg-pureBlack.text-pureWhite').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The dismissible announcement strip above the nav ("Rerank 5 is here…"), bg-pureBlack, with its Learn-more link and close control.', sel: 'div.bg-pureBlack first' }, { noScroll: true });
  await S('banner-close', q('button[aria-label="Close banner"]').filter({ visible: true }).first(), B4, { group: g, title: 'Banner close', desc: 'The promo banner close button (icon-close, hover rotate-90). A local dismiss toggle — pressing it only hides the banner.', sel: 'button[aria-label="Close banner"]' }, { noScroll: true });
  await S('header', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The fixed site nav (nav.z-nav, h-[60px] inner bar): Cohere mark, roll-hover nav links, Sign in + Request-a-demo CTAs.', sel: 'nav first visible' }, { noScroll: true });
  await S('logo', q('nav a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Cohere mark home anchor in the nav (h-5 w-[118px] svg).', sel: 'nav a[href="/"]' }, { noScroll: true });
  await S('nav-item', q('nav a.group\\/nav-link').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A flat nav link with the roll-hover duplicate text (group/nav-link, hover translates the label -100%).', sel: 'nav a.group/nav-link' }, { noScroll: true });
  await S('nav-signin', q('nav a[class*="ease-button-gradient"]').filter({ hasText: /^Sign in$/ }).first(), B4, { group: g, title: 'Nav sign-in', desc: 'The transparent "Sign in" ghost control linking to dashboard.cohere.com; measured never followed.', sel: 'nav a:has-text("Sign in")' }, { noScroll: true });
  await S('nav-cta', q('nav a[class*="ease-button-gradient"]').filter({ hasText: /Request a demo/ }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The dark "Request a demo" ease-button-gradient pill in the nav; links to the contact form, never followed.', sel: 'nav a:has-text("Request a demo")' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"Your AI. Your rules." — the hero headline (web3 display scale).', sel: 'first visible h1' }, { noScroll: true });
  await S('hero-cta', q('main a[class*="ease-button-gradient"], section a[class*="ease-button-gradient"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The first ease-button-gradient CTA in page content ("Explore now"-style pill); links onward, never followed.', sel: 'main a.ease-button-gradient' }, { noScroll: true });
  await S('cta-dark', q('main a[class*="ease-button-gradient"].bg-neutral-15, section a[class*="ease-button-gradient"].bg-neutral-15').filter({ visible: true }).first(), B4, { group: h, title: 'Dark CTA', desc: 'A dark ease-button-gradient pill (bg-neutral-15 text-pureWhite, gradient hover sweep) in page content.', sel: 'main a.ease-button-gradient.bg-neutral-15' });
  await S('cta-light', q('main a[class*="ease-button-gradient"].bg-pureWhite, section a[class*="ease-button-gradient"].bg-pureWhite').filter({ visible: true }).first(), B4, { group: h, title: 'Light CTA', desc: 'A light ease-button-gradient pill (bg-pureWhite text-neutral-15) in page content.', sel: 'main a.ease-button-gradient.bg-pureWhite' });
  await S('callout-card', q('a.group\\/calloutCard').filter({ visible: true }).first(), B4, { group: h, title: 'Callout card', desc: 'A callout-module card anchor (group/calloutCard, rounded-lg/xl).', sel: 'a.group/calloutCard' });
  await S('marquee-logo', q('img[alt$=" Logo"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Customer logo', desc: 'A logo in the customer marquee (Oracle/Dell/RBC row, rendered twice for the loop).', sel: 'img[alt$=" Logo"]' });
  await S('section-title', q('main h2, section h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'A section heading under the hero (web3 display scale).', sel: 'first visible h2' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element painted fill — the page ground.', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('price-tab', q('[role="tablist"] button[role="tab"][aria-selected="true"]').filter({ visible: true }).first(), B4, { group: g, title: 'Category tab (selected)', desc: 'The selected model-category tab (role=tab aria-selected=true — "Workplace systems") switching the rate table. Measured at rest, never switched.', sel: '[role=tab][aria-selected=true]' }, { noScroll: true });
  await S('price-tab-off', q('[role="tablist"] button[role="tab"][aria-selected="false"]').filter({ visible: true }).first(), B4, { group: g, title: 'Category tab (unselected)', desc: 'An unselected model-category tab (aria-selected=false); never pressed — it would swap the rate table.', sel: '[role=tab][aria-selected=false]' }, { noScroll: true });
  await S('price-rate', q('text=/\\$\\d+(\\.\\d+)?/').filter({ visible: true }).first(), ['default'], { group: g, title: 'Rate figure', desc: 'A per-model rate figure in the pricing table (the "$3.00"-style cells).', sel: 'text=/\\$\\d+/' });
  await S('faq-item', q('button').filter({ hasText: /How do I|What’s the|When do I/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ row', desc: 'A pricing-FAQ accordion row (closed state; its own press opens the answer — a local toggle).', sel: 'button:has-text("How do I")' });
  const faqBtn = q('button').filter({ hasText: /How do I|What’s the|When do I/ }).filter({ visible: true }).first();
  await S('faq-item-open', faqBtn.locator('xpath=..'), ['opened'], { group: g, title: 'FAQ row, open', desc: 'The FAQ item after its question button\'s own press (a local UI toggle) — the enclosing row is measured so the expanded answer lands in the state, not just the toggle.', sel: 'parent of button:has-text("How do I")', toggleLoc: faqBtn });
  save();
}

async function north() {
  if (!(await newPage('north'))) return;
  const g = G.north;
  await S('north-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'North title', desc: '"North 2: Enterprise AI without compromises" — the product page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('north-cta', q('main a[class*="ease-button-gradient"], section a[class*="ease-button-gradient"]').filter({ visible: true }).first(), B4, { group: g, title: 'North CTA', desc: 'The first ease-button-gradient CTA on the North page; links onward, never followed.', sel: 'main a.ease-button-gradient' }, { noScroll: true });
  save();
}

async function command() {
  if (!(await newPage('command'))) return;
  const g = G.command;
  await S('command-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Command title', desc: '"Secure, production-ready efficiency for agentic intelligence" — the model page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('command-cta', q('main a[class*="ease-button-gradient"], section a[class*="ease-button-gradient"]').filter({ visible: true }).first(), B4, { group: g, title: 'Command CTA', desc: 'The first ease-button-gradient CTA on the Command page; links onward, never followed.', sel: 'main a.ease-button-gradient' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 18000 }))) return;
  const g = G.signin;
  // dashboard.cohere.com/welcome/login is the product's sign-in surface: the
  // card, OAuth buttons and email field are measured at rest; the field gets
  // a focus reading only — nothing typed, nothing submitted.
  await S('signin-card', q('main, [class*="login" i], [class*="auth" i], form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The dashboard.cohere.com/welcome/login surface: the sign-in card the app paints. Measured at rest, never submitted.', sel: 'main/first visible login container' }, { noScroll: true });
  await S('signin-oauth', q('button').filter({ hasText: /Continue with Google/i }).first(), B4, { group: g, title: 'OAuth button', desc: 'A "Continue with" OAuth button on the sign-in card; measured never pressed.', sel: 'button:has-text("Continue with Google")' }, { noScroll: true });
  await S('signin-field', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The sign-in email input — a focus reading only; nothing typed, nothing sent.', sel: 'input[type=email]' }, { noScroll: true });
  await S('signin-submit', q('button[type="submit"], button').filter({ hasText: /^(Log in|Continue)$/i }).first(), B4, { group: g, title: 'Log-in button', desc: 'The "Log in" submit on the sign-in card; measured never pressed — it would submit the form.', sel: 'button:has-text("Log in")' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  await page.evaluate(() => {
    const f = document.querySelector('footer, [role="contentinfo"]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The dark footer band (bg near-black): link columns (Platforms/Models/…), social icons and the legal row; the certification strip sits just above it on the home page.', sel: 'footer' }, { noScroll: true });
  // The footer ships three DOM copies of its link list; only the
  // div.hidden.lg:flex desktop columns paint — the accordion copies stay 0x0.
  await S('footer-link', q('[data-m-footer="1"] div.hidden.lg\\:flex a.group\\/footer-link').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A link in a footer link column (group/footer-link text-white, inside the lg:flex desktop block; the md:hidden accordion copies measure 0x0).', sel: 'footer .lg\\:flex a.group/footer-link' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] img[alt="LinkedIn"], [data-m-footer="1"] img[alt="X"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon (LinkedIn/X) — the img inside the social anchor.', sel: 'footer img[alt=LinkedIn|X]' }, { noScroll: true });
  await S('footer-cta', q('[data-m-footer="1"] a[class*="ease-button-gradient"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer CTA', desc: 'The footer "Request a demo" ease-button-gradient pill; links to the contact form, never followed.', sel: 'footer a.ease-button-gradient' }, { noScroll: true });
  // The SOC2/GDPR/ISO certification strip sits on the home page above the
  // footer's contentinfo block, not inside it.
  await S('footer-badge', q('a[aria-label="SOC2"], a[aria-label="GDPR"], a[aria-label="ISO"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Trust badge', desc: 'A certification badge anchor in the compliance strip on the home page (SOC2/GDPR/ISO/CCPA, w-[120px]).', sel: 'a[aria-label=SOC2|GDPR|ISO]' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the nav collapses to the bar plus the "Open navigation menu"
  // toggle; the menu opens on the button's own press.
  await S('m-header', q('nav[aria-label="Mobile navigation"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390 mobile nav bar (aria-label="Mobile navigation"): logo + menu toggle; the desktop nav unmounts to 0x0 at this width.', sel: 'nav[aria-label="Mobile navigation"]' }, { noScroll: true });
  await S('m-menu-button', q('button[aria-label="Open navigation menu"], [aria-label="Mobile navigation"] button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (aria-label="Open navigation menu"); its own press opens the drawer.', sel: 'button[aria-label="Open navigation menu"]' }, { noScroll: true });
  const menuBtn = q('button[aria-label="Open navigation menu"]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await menuBtn.click({ timeout: 5000 }); await page.waitForTimeout(1500); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  // The open menu is a fixed overlay holding the accordion link list; tag
  // whatever fills the viewport and contains a nav link.
  await page.evaluate(() => {
    const p = [...document.querySelectorAll('body *')].find((e) => {
      const cs = getComputedStyle(e);
      const r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > 500 && r.width > 300 && e.querySelector('a[href="/pricing"], a.group\\/nav-link');
    });
    if (p) p.setAttribute('data-m-panel', '1');
  }).catch(() => {});
  await S('m-menu-open', q('[data-m-panel="1"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The menu overlay after the hamburger press (min-h-[100vh] bg-black/20 backdrop-blur scrim + panel).', sel: 'opened mobile menu overlay' }, { noScroll: true });
  await S('m-menu-link', q('[data-m-panel="1"] a, [data-m-panel="1"] button').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link/accordion row inside the open mobile menu (min-h-[44px] rows).', sel: 'first row inside the open menu' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (dashboard.cohere.com/welcome/login is the sign-in boundary)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, north, command, signin, mobile };
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
