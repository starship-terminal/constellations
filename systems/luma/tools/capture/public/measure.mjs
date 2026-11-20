// Measures luma.com's public components in every state reachable without
// signing in, registering, following or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing discover event signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// luma.com paints html.theme-root.light on marketing pages and
// html.theme-root.dark on a public event page. The only press is the pricing
// Monthly/Annual segment (a local toggle). The sign-in card is measured and
// never submitted. Consent overlays are hidden, never clicked.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', discover: '/discover', event: '/july4-brooklyn', signin: '/signin' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo })
    .catch((e) => { log('  open failed', key, String(e.message || e).slice(0, 120)); return false; });
  if (!cleared || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    const seen = [];
    for (const el of els) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 20);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
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
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (dropdown, menu, radio, day). Refuses a submit button and
// any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|create event|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|get luma plus|claim|share|export|continue|continue with email|sign in with google|sign in with passkey|follow|register|claim this offer|try again|next|confirm|i understand|decline|contact the host|report event)$/i;
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

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[key] = { selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home', pricing: 'Pricing',
  discover: 'Discover', event: 'Public event', auth: 'Sign in',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 8000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Landing header', desc: 'The marketing landing header: a spark mark and the Sign In pill. Inner pages add the wordmark and Discover Events.', sel: 'header.landing-topnav' }, { noScroll: true });
  await S('spark', q('header .logo, header svg').filter({ visible: true }).first(), ['default'], { group: g, title: 'Spark mark', desc: 'The four-point spark in the landing header. It is not a link.', sel: 'header .logo' }, { noScroll: true });
  await S('nav-signin', q('header a.lux-button').filter({ hasText: /^\s*Sign In\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign In pill', desc: 'The landing Sign In pill (light, round). It links to /signin; measured, never followed.', sel: 'header a.lux-button "Sign In"' }, { noScroll: true });
  const hg = G.hero;
  await S('hero-title', q('h1.landing-title').filter({ hasText: /Delightful/ }).filter({ visible: true }).first(), ['default'], { group: hg, title: 'Hero title', desc: 'The 80px landing title, "Delightful events start here". A second painted copy ("Stellar") sits in a dark island and is not this atom.', sel: 'h1.landing-title' });
  await S('hero-lede', q('main p, section p').filter({ hasText: /From run clubs/ }).filter({ visible: true }).first(), ['default'], { group: hg, title: 'Hero lede', desc: 'The sentence under the landing title.', sel: 'hero lede' });
  await S('cta-create', q('a.create-button, a[href="/create"]').filter({ hasText: /Create Your First Event/ }).filter({ visible: true }).first(), B4, { group: hg, title: 'Create event button', desc: 'The black Create Your First Event pill. It links to /create, which opens a sign-in dialog; measured, never followed.', sel: 'a.create-button' });
  await S('cta-discover', q('a.lux-button, a.btn').filter({ hasText: /^\s*Discover Events\s*$/ }).filter({ visible: true }).first(), B4, { group: hg, title: 'Discover Events button', desc: 'The secondary Discover Events action under the hero.', sel: 'a "Discover Events"' });
  await S('event-card', q('a[href^="/"]').filter({ hasText: /Today|Tomorrow|PM|AM/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: G.home, title: 'Event row', desc: 'A popular-events row on the home page. The row was measured, never opened.', sel: 'home event row' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 7000 }))) return;
  await sheetsFor('pricing');
  const g = G.pricing;
  await S('pricing-title', q('h1').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The 60px Pricing heading.', sel: 'h1 "Pricing"' });
  await S('billing-monthly', q('button.segment').filter({ hasText: /^\s*Monthly\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Monthly segment', desc: 'The Monthly half of the billing segment. Toggled as local UI; nothing was purchased.', sel: 'button.segment "Monthly"' });
  await S('billing-annual', q('button.segment').filter({ hasText: /^\s*Annual\s*$/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Annual segment', desc: 'The Annual half of the billing segment, selected at rest on this load.', sel: 'button.segment "Annual"' });
  await S('plan-card', q('.content-card').filter({ hasText: /Free, forever/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Free plan card', desc: 'The free plan card: 24px radius, white surface.', sel: '.content-card free plan' });
  await S('plan-card-plus', q('.content-card').filter({ hasText: /Luma Plus/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plus plan card', desc: 'The Luma Plus plan card. Get Luma Plus was measured, never followed (it is a sign-in checkout).', sel: '.content-card plus plan' });
  await S('plan-cta', q('a.lux-button').filter({ hasText: /^\s*Get Started\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Get Started button', desc: 'The primary plan button (near-black fill, 16px radius). It links to sign-in; measured, never followed.', sel: 'a.lux-button.primary "Get Started"' });
  await S('plan-cta-brand', q('a.lux-button').filter({ hasText: /Get Luma Plus/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Get Luma Plus button', desc: 'The brand button (#f31a7c, 16px radius). It links to calendar checkout; measured, never followed.', sel: 'a.lux-button.brand "Get Luma Plus"' });
  save();
}

async function discover() {
  if (!(await newPage('discover', { wait: 7000 }))) return;
  const g = G.discover;
  await S('discover-title', q('h1').filter({ hasText: /Discover/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Discover title', desc: 'The Discover Events heading.', sel: 'h1 Discover' });
  await S('category-card', q('a.content-card, a[class*="content-card"]').filter({ hasText: /Events/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Category card', desc: 'A browse-by-category card (Family, Books, …). Measured, never followed.', sel: 'a.content-card category' });
  await S('follow-button', q('button').filter({ hasText: /^\s*Follow\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Follow button', desc: 'A calendar Follow button. Measured, never pressed (pressing asks for sign-in).', sel: 'button "Follow"' });
  save();
}

async function event() {
  if (!(await newPage('event', { wait: 8000 }))) return;
  await sheetsFor('event');
  await chrome('event');
  const g = G.event;
  await S('event-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Event title', desc: 'The event page title. The page paints theme-root.dark on its own.', sel: 'event h1' });
  await S('wordmark', q('header a[aria-label="Luma Home"], a.logo-wrapper').filter({ visible: true }).first(), ['default'], { group: g, title: 'Wordmark', desc: 'The luma wordmark on an inner page. It links home; measured, never followed.', sel: 'a[aria-label="Luma Home"]' }, { noScroll: true });
  await S('nav-discover', q('header a[href="/discover"]').filter({ visible: true }).first(), B4, { group: g, title: 'Discover link', desc: 'The Discover Events link in the inner-page header. Measured, never followed.', sel: 'header a[href="/discover"]' }, { noScroll: true });
  await S('event-signin', q('header button.lux-button, header a.lux-button').filter({ hasText: /^\s*Sign In\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Event Sign In', desc: 'The header Sign In control on the dark event page. Measured, never pressed.', sel: 'event header Sign In' }, { noScroll: true });
  await S('host-card', q('.content-card').filter({ hasText: /Presented by/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Host card', desc: 'The presented-by host block beside the event title.', sel: '.content-card host' });
  await S('host-follow', q('button.lux-button').filter({ hasText: /^\s*Follow\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Host Follow', desc: 'The host Follow button. Measured, never pressed (it asks for sign-in).', sel: 'button "Follow"' });
  await S('event-meta', q('a.row-container, a').filter({ hasText: /Brooklyn Bridge Park/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Location row', desc: 'The place row. It links out to a map; measured, never followed.', sel: 'location row' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 5000 }))) return;
  await sheetsFor('signin');
  const g = G.auth;
  await S('signin-title', q('h3.title, h1, h2, h3').filter({ hasText: /Welcome to Luma/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in title', desc: 'The Welcome to Luma heading on the sign-in card. Nothing was submitted.', sel: 'h3 "Welcome to Luma"' });
  await S('email-field', q('input.lux-input, input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input (8px radius). Sample text was typed and deleted. Continue was never pressed.', sel: 'input.lux-input' });
  await S('phone-toggle', q('button.lux-button').filter({ hasText: /Use Phone Number/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Use Phone Number', desc: 'The link-styled toggle that swaps the email field for a phone field. Measured, never pressed.', sel: 'button "Use Phone Number"' });
  await S('continue-btn', q('button[type="submit"]').filter({ hasText: /Continue with Email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with Email', desc: 'The primary submit. Measured with CDP :active only, so the form was never submitted.', sel: 'button[type=submit] "Continue with Email"' });
  await S('google-btn', q('button.lux-button').filter({ hasText: /Sign in with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in with Google', desc: 'The Google button. Measured, never pressed.', sel: 'button "Sign in with Google"' });
  await S('passkey-btn', q('button.lux-button').filter({ hasText: /Sign in with Passkey/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in with Passkey', desc: 'The passkey button. Measured, never pressed.', sel: 'button "Sign in with Passkey"' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The page footer: Discover, Pricing, App, Help, Terms, Privacy.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer text link.', sel: 'footer a "Pricing"' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', wait: 7000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The 390px header: wordmark and Sign In. There is no hamburger.', sel: 'header at 390' }, { noScroll: true });
  await S('m-signin', q('header a.lux-button, header a').filter({ hasText: /^\s*Sign In\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile Sign In', desc: 'The header Sign In pill at 390. Measured, never followed.', sel: 'header Sign In at 390' }, { noScroll: true });
  await S('m-hero', q('h1.landing-title').filter({ hasText: /Delightful/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The landing title at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); marketing pages paint theme-root.light; the public event page paints theme-root.dark on its own';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, discover, event, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a.lux-button');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
