// Measures chargetrip.com's public components in every state reachable
// without signing in, booking, submitting or buying anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing sales signin mobile (the footer group also runs on home).
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// chargetrip.com is a Framer marketing site in one light theme; components
// are found by role, data-framer-name, cursor:pointer structure or stable
// text — the hashed framer-* classes are never selected. Nothing is sent,
// booked or signed into: the only presses are local UI toggles — the header
// "Products" trigger that opens the mega menu and the mobile menu trigger.
// The "Cookie Settings" card is hidden, never answered; every Book-a-demo /
// Plan-a-route / Contact-sales / Sign-in / Get-started / Submit / Sign-up
// action is measured in all states except followed or pressed for real.
// account.chargetrip.io's sign-in card (a different app on the same public
// surface) is measured as a documented boundary — its own Light/Dark theme
// select did not respond to synthetic input, so it is captured light-only.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/api', sales: '/contact/sales', signin: 'https://account.chargetrip.io/sign-in' };
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
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
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
        // A click moves a range thumb and opens a native select's popup; those two only take focus().
        const noClick = await fld.evaluate((el) => el.tagName === 'SELECT' || (el.tagName === 'INPUT' && el.type === 'range'));
        if (noClick) await fld.evaluate((el) => el.focus());
        else await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = noClick ? 'focus() (no click)' : 'clicked into the field';
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
  sales: 'Contact sales form', signin: 'Sign-in page (boundary)',
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

// Clicks the header "Products" trigger (a local nav toggle; opens the mega
// menu, never navigates). Returns whether it marked the trigger.
const openProducts = async () => page.evaluate(() => {
  const el = [...document.querySelectorAll('[class*="-container"]')].find((n) => (n.innerText || '').trim() === 'Products' && n.getBoundingClientRect().y < 64 && n.getBoundingClientRect().y >= 0);
  if (!el) return false;
  el.setAttribute('data-m-nav', '1');
  return true;
});

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The white 64px top bar: the div[data-framer-name="Content"] that is the
  // nav's own bar (the page wrapper shares the name at 8200px tall).
  await page.evaluate(() => {
    const bar = [...document.querySelectorAll('div[data-framer-name="Content"]')].find((n) => { const r = n.getBoundingClientRect(); return r.y === 0 && r.height >= 56 && r.height <= 72; });
    if (bar) bar.setAttribute('data-m-header', '1');
  });
  await S('header', q('[data-m-header="1"]'), ['default'], { group: g, title: 'Header', desc: 'The white 64px top bar: wordmark, the Products/Use-cases/Developers/Pricing/Company menu triggers, and the Contact-sales + Sign-in buttons.', sel: 'div[data-framer-name="Content"] at y=0' }, { noScroll: true });
  // The wordmark: the first in-bar link (home) holding an svg/img.
  await page.evaluate(() => {
    const bar = document.querySelector('[data-m-header="1"]');
    const el = bar && [...bar.querySelectorAll('a')].find((a) => a.querySelector('svg,img'));
    if (el) el.setAttribute('data-m-logo', '1');
  });
  await S('logo', q('[data-m-logo="1"]'), ['default'], { group: g, title: 'Logo', desc: 'The chargetrip wordmark anchor.', sel: 'first header a holding an svg/img' }, { noScroll: true });
  const navItem = q('[class*="-container"]').filter({ hasText: /^Products$/ }).filter({ visible: true }).first();
  await S('nav-item', navItem, [...B4, 'opened'], { group: g, title: 'Nav item', desc: 'The "Products" menu trigger; its own press opens the mega menu (opened state, then the menu stays up for the next two entries).', sel: 'div[text=Products] inside the bar' }, { noScroll: true });
  // The mega menu, held open by the Products toggle above: the card row under
  // the bar. The footer repeats ./no-code in its own nav column far below the
  // viewport, so only the link inside the open menu counts — the candidate
  // with its top edge inside the menu band right under the header. The menu
  // closes when the pointer leaves the nav region (reset() parks the cursor
  // in the corner after every entry), so each entry re-opens it idempotently.
  const menuIsOpen = () => page.evaluate(() =>
    [...document.querySelectorAll('a[href="./no-code"]')].some((a) => { const r = a.getBoundingClientRect(); return r.height > 0 && r.top >= 0 && r.top < 800; }));
  const ensureMenuOpen = async () => {
    if (!(await menuIsOpen())) { await toggle(navItem); await page.waitForTimeout(1200); }
  };
  const markMenu = () => page.evaluate(() => {
    const link = [...document.querySelectorAll('a[href="./no-code"]')]
      .map((a) => ({ a, r: a.getBoundingClientRect() }))
      .filter(({ r }) => r.height > 0 && r.top >= 0 && r.top < 800)
      .sort((x, y) => x.r.top - y.r.top)[0];
    if (!link) return;
    link.a.setAttribute('data-m-nocode', '1');
    for (let n = link.a, i = 0; n && i < 8; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 900 && r.height > 300 && r.height <= 900) { n.setAttribute('data-m-panel', '1'); break; }
    }
    for (let n = link.a, i = 0; n && i < 6; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 250 && r.width < 700 && r.height > 90 && r.height <= 800) { n.setAttribute('data-m-card', '1'); break; }
    }
  });
  await S('menu-panel', q('[data-m-panel="1"]'), ['default'], { group: g, title: 'Mega menu', desc: 'The Products mega-menu card row (No-code / API / Integration Partners photo cards), held open by the nav-item toggle.', sel: 'card-row ancestor of the in-menu a[href="./no-code"] (top < 800, not the footer copy)' }, { noScroll: true, noReset: true, open: async () => { await ensureMenuOpen(); await markMenu(); } });
  await S('menu-card', q('[data-m-card="1"]'), ['default'], { group: g, title: 'Menu card', desc: 'The No-code photo card inside the open mega menu.', sel: 'card ancestor of the in-menu a[href="./no-code"]' }, { noScroll: true, noReset: true, open: ensureMenuOpen });
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  await S('nav-cta', q('a[data-framer-name="Background Dark Primary / Fill"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The dark "Contact sales" button; links to /contact/sales, measured never followed.', sel: 'a.Background Dark Primary / Fill' }, { noScroll: true });
  await S('nav-signin', q('a[data-framer-name="Background Dark Primary / Outline"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in button', desc: 'The outlined "Sign in" button; links to account.chargetrip.com, measured never followed.', sel: 'a.Background Dark Primary / Outline' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: 'The 88px Cirka display headline on the dark hero card.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p, div').filter({ hasText: /Every charge decision/ }).filter({ visible: true }).last(), ['default'], { group: h, title: 'Hero subcopy', desc: 'The muted lede under the display headline.', sel: 'the lede paragraph under h1' }, { noScroll: true });
  // The dark hero band: the nearest ancestor of the h1 that paints — a dark
  // fill or a non-none background image (the band is drawn with a gradient,
  // so a colour-only check falls through to the transparent content wrapper).
  // No wrapper fallback: if nothing paints, the entry records a miss.
  await page.evaluate(() => {
    const h = document.querySelector('h1');
    for (let n = h, i = 0; h && n && i < 12; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      const m = cs.backgroundColor.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
      const dark = m && (m[4] === undefined || +m[4] > 0.5) && +m[1] < 100 && +m[2] < 100 && +m[3] < 100;
      const painted = dark || cs.backgroundImage !== 'none';
      if (r.width > 900 && r.height < 1400 && painted) { n.setAttribute('data-m-hero', '1'); return; }
    }
  });
  await S('hero-card', q('[data-m-hero="1"]'), ['default'], { group: h, title: 'Hero band', desc: 'The dark rounded hero card the headline sits on.', sel: 'dark ancestor of h1 (marked in-page)' }, { noScroll: true });
  await S('cta-accent', q('a[data-framer-name="Large / Accent"]').filter({ visible: true }).first(), B4, { group: h, title: 'Accent CTA', desc: 'The orange "Book a demo" button (links to a HubSpot meeting page, never followed).', sel: 'a.Large / Accent' }, { noScroll: true });
  await S('cta-dark', q('a[data-framer-name="Large / Dark"]').filter({ visible: true }).first(), B4, { group: h, title: 'Dark CTA', desc: 'The dark "Plan a route" button with its map thumbnail (links to go.chargetrip.com, never followed).', sel: 'a.Large / Dark' }, { noScroll: true });
  const h2ok = await scrollFind(() => {
    const h = [...document.querySelectorAll('h2')].find((n) => (n.innerText || '').trim().length > 3 && n.getBoundingClientRect().height > 0);
    if (!h) return false;
    h.setAttribute('data-m-h2', '1');
    return true;
  });
  await S('section-title', h2ok ? q('[data-m-h2="1"]') : q('[data-m-h2="__none__"]'), ['default'], { group: h, title: 'Section title', sel: 'first visible h2, marked where it mounts' });
  // The page ground: the body element's own painted fill (the warm cream
  // under every section). Read directly — no visible element carries it.
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: "The body element's own painted fill — the warm-cream ground under every section.", sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: '"Build for free and go live with the best plan for you." in 88px Cirka.', sel: 'h1' }, { noScroll: true });
  await S('logo-chip', q('a').filter({ hasText: /Plugsurfing|Hertz|Motability/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Customer chip', desc: 'A dark customer-logo chip under the headline (Plugsurfing).', sel: 'a:has-text("Plugsurfing")' }, { noScroll: true });
  const card = (re) => q('[data-framer-name="Card"]').filter({ hasText: re }).filter({ visible: true }).first();
  await S('plan-card', card(/^Lite/), ['default'], { group: g, title: 'Plan card (light)', desc: 'The white Lite plan card.', sel: 'div.Card:has-text("Lite")' });
  await S('plan-card-dark', card(/Standard/), ['default'], { group: g, title: 'Plan card (dark)', desc: 'The dark Standard card under the "Most popular" banner.', sel: 'div.Card:has-text("Standard")' });
  await S('plan-cta', q('a[data-framer-name="Default / Accent"]').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA (accent)', desc: 'The orange "Get started" inside the Standard card; links to the sign-up, never followed.', sel: 'a.Default / Accent' });
  await S('plan-cta-dark', q('a[data-framer-name="Default / Dark"]').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA (dark)', desc: 'A dark "Get started"/"Get a quote" plan action; never followed.', sel: 'a.Default / Dark' });
  // "Most popular" tag above the Standard card.
  const pop = await domFind(page, /most popular/i, { sel: 'div, p, span', tag: 'pop', up: 'div' });
  await S('popular-tag', pop, ['default'], { group: g, title: 'Popular tag', desc: 'The "Most popular" label above the Standard card.', sel: 'leaf text "Most popular"' });
  // A feature row with its orange check (the Includes lists inside plan cards).
  const chk = await domFind(page, /^All API services$/i, { sel: 'div, p, li', tag: 'chk' });
  await S('check-item', chk, ['default'], { group: g, title: 'Feature row', desc: 'An Includes list row with its orange check glyph.', sel: 'leaf "All API services"' });
  // The usage-calculator slider (min 0 max 3, steps).
  await S('range-slider', q('input[type="range"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Range slider', desc: 'The price calculator\'s usage slider (0-3 steps); focused only, never dragged.', sel: 'input[type=range]' });
  save();
}

async function sales() {
  if (!(await newPage('sales'))) return;
  const g = G.sales;
  await S('contact-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', desc: '"Grow your business with routing." in 64px Cirka.', sel: 'h1' }, { noScroll: true });
  await S('form-input', q('form input[name="firstname"], input[name="firstname"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'The First-name text field; filled with sample text then deleted, never submitted.', sel: 'input[name=firstname]' }, { fillText: 'Ada' });
  await S('form-email', q('form input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'E-mail field', desc: 'The required E-mail field.', sel: 'form input[type=email]' });
  await S('form-tel', q('form input[type="tel"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Phone field', desc: 'The optional Phone-number field.', sel: 'form input[type=tel]' });
  await S('form-select', q('form select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Select', desc: 'The Job-function native select; focused only, its dropdown never opened.', sel: 'form select' });
  await S('form-textarea', q('form textarea').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Textarea', desc: 'The Message textarea.', sel: 'form textarea' });
  await S('form-submit', q('form button[type="submit"], form [type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Submit button', desc: 'The dark "Submit" button; measured in all non-submitting states, never pressed for real.', sel: 'form [type=submit]' });
  await S('demo-card', q('a').filter({ hasText: /Book a demo\s*30 minutes/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Book-a-demo card', desc: 'The white "Book a demo · 30 minutes" card beside the form; never followed.', sel: 'a:has-text("Book a demo 30 minutes")' });
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in title', desc: '"Sign in to your account." in 48px Cirka.', sel: 'h1' }, { noScroll: true });
  await S('signin-input', q('input[type="text"], input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'E-mail field', desc: 'The E-mail-address field on the sign-in card; filled with sample text then deleted, Continue never pressed.', sel: 'sign-in input', fillText: 'name@example.com' });
  await S('signin-continue', q('button').filter({ hasText: /continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The dark Continue button; measured in all non-submitting states, never pressed for real.', sel: 'button:has-text("Continue")' });
  await S('signin-create', q('a, button').filter({ hasText: /create account/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Create-account button', desc: 'The secondary Create-account action; never followed.', sel: ':has-text("Create account")' });
  await S('signin-trust', q('div, p, li').filter({ hasText: /^No credit card needed$/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Trust row', desc: 'A check-marked reassurance row under the hero panel.', sel: 'leaf "No credit card needed"' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep another page's
  // readings under the wrong url.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  // The footer band: the widest tall ancestor of the footer status link.
  await page.evaluate(() => {
    const tag = document.querySelector('a[href*="status.chargetrip.com"]') || [...document.querySelectorAll('a')].find((n) => /linkedin/i.test(n.href || ''));
    if (!tag) return;
    for (let n = tag, i = 0; n && i < 12; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 900 && r.height > 350 && r.height < 1600) { n.setAttribute('data-m-footer', '1'); return; }
    }
    tag.parentElement.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The footer band: link columns, the "chargetrip presents" newsletter block, badges, the legal subfooter.', sel: 'ancestor of "chargetrip presents"' }, { noScroll: true });
  await S('footer-link', q('a').filter({ hasText: /^No-code$/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Footer link', sel: 'footer a:has-text("No-code")' }, { noScroll: true });
  await S('footer-social', q('a[href*="linkedin" i], a[href*="x.com" i], a[href*="youtube" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', sel: 'footer social a' }, { noScroll: true });
  await S('newsletter-cta', q('a, button').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Newsletter CTA', desc: 'The footer newsletter "Sign up" button; never followed.', sel: 'footer a:has-text("Sign up")' }, { noScroll: true });
  // The link itself: a text filter on 'a, div' caught the outermost footer column whose text ends in "Stable".
  await S('status-pill', q('a[href*="status.chargetrip.com"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Status pill', desc: 'The "● Stable" status link in the footer (green dot; links to status.chargetrip.com, never followed).', sel: 'a[href*="status.chargetrip.com"]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await page.evaluate(() => {
    // The top bar: the outermost ancestor of the hamburger still inside the
    // header zone (top <= 100). Walking without a top bound previously let a
    // chart container pass the size check and publish 100/75/50/25/0 as the
    // header.
    const btn = document.querySelector('[data-framer-name="Button Icon"]');
    let cand = null;
    for (let n = btn, i = 0; btn && n && i < 8; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.top > 140 || r.width > 480 || r.height > 200) break;
      if (r.top <= 100 && r.width >= 300 && r.height >= 40 && r.height <= 140) cand = n;
    }
    if (cand) cand.setAttribute('data-m-mheader', '1');
  });
  await S('m-header', q('[data-m-mheader="1"]'), ['default'], { group: g, title: 'Mobile header', sel: 'the mobile top bar at y=0' }, { noScroll: true });
  const menuBtn = q('[data-framer-name="Button Icon"]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, ['default'], { group: g, title: 'Menu button', desc: 'The dark-teal hamburger at the bar\'s right edge; its own press opens the menu overlay.', sel: 'div[data-framer-name="Button Icon"]' }, { noScroll: true });
  if (await menuBtn.count()) {
    try { await toggle(menuBtn); await page.waitForTimeout(1500); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  // The open overlay: the menu container, not body — the outermost fixed
  // ancestor of the in-viewport no-code link (the page's own copy sits behind
  // the overlay), falling back to the link's top-level ancestor.
  await page.evaluate(() => {
    const links = [...document.querySelectorAll('a[href="./no-code"]')].filter((n) => { const r = n.getBoundingClientRect(); return r.height > 0 && r.top > -50 && r.top < innerHeight; });
    const inMenu = links.find((n) => { for (let m = n; m && m !== document.body; m = m.parentElement) if (getComputedStyle(m).position === 'fixed') return true; return false; });
    const link = inMenu || links[links.length - 1];
    if (!link) return;
    let mark = null;
    for (let n = link, i = 0; n && n !== document.body && i < 12; i++, n = n.parentElement) {
      if (getComputedStyle(n).position === 'fixed' && n.getBoundingClientRect().width <= 420) mark = n;
    }
    if (!mark) { mark = link; while (mark.parentElement && mark.parentElement !== document.body) mark = mark.parentElement; }
    if (mark && mark !== document.body) mark.setAttribute('data-m-mopen', '1');
  });
  await S('m-menu-open', q('[data-m-mopen="1"]'), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The full-screen menu overlay after the trigger\'s own toggle: orange No-code card, dark API card, Integration Partners, the Use-cases list.', sel: 'fixed menu overlay ancestor of the in-menu a[href="./no-code"]' }, { noScroll: true, crop: true });
  await page.evaluate(() => {
    const links = [...document.querySelectorAll('a[href="./no-code"]')].filter((n) => { const r = n.getBoundingClientRect(); return r.height > 0 && r.top > -50 && r.top < innerHeight; });
    const a = links.find((n) => { for (let m = n; m && m !== document.body; m = m.parentElement) if (getComputedStyle(m).position === 'fixed') return true; return false; }) || links[links.length - 1];
    for (let n = a, i = 0; a && n && i < 6; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 250 && r.width < 700 && r.height > 80 && r.height < 700) { n.setAttribute('data-m-mcard', '1'); return; }
    }
  });
  await S('m-menu-card', q('[data-m-mcard="1"]'), ['default'], { group: g, title: 'Mobile menu card', desc: 'The orange No-code card in the open mobile menu.', sel: 'card ancestor of a[href="./no-code"]' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, sales, signin, mobile };
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
