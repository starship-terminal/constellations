// Measures coinbase.com's public components in every state reachable
// without signing in, paying or submitting anything.
//
//   xvfb-run -a node measure.mjs [page ...]   (Cloudflare gates headless)
//
// Pages: home explore one prime signin mobile (the footer group also runs
// on home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is
// built by build-measurements.mjs.
//
// coinbase.com is a styled-components/CDS (Coinbase Design System) app behind
// Cloudflare — every launch is headed (xvfb). The full theme ships as ~830
// inline custom properties on div.coinbase.light plus a .coinbase.dark set;
// stable data-testid hooks (main-nav, *-button, prices-table-v2-*) carry the
// selectors. A promo banner row mounts inside the header — measured as real
// chrome. OneTrust cookie consent is hidden by closePromo, never answered.
// /signin redirects to login.coinbase.com — the product's sign-in boundary:
// its card is measured, never submitted — the email field gets a focus
// reading only (nothing typed, nothing sent). The only presses are local UI
// toggles — the mobile menu button opens its own overlay; the explore chips
// and price-table sort are read at rest, never switched.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', explore: '/explore', one: '/one', prime: '/prime', signin: 'https://www.coinbase.com/signin' };
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && (/^https?:/.test(URLS[current]) ? URLS[current] : BASE + URLS[current]) }, meta);
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
  shell: 'Shell and navigation', home: 'Home', explore: 'Explore (prices)',
  one: 'Coinbase One page', prime: 'Prime page', signin: 'App sign-in (boundary)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  // The fixed header (data-testid=main-nav): a promo banner row ("Sign up as
  // an Accredited Investor…") sits on top, then the 72px bar with the
  // Coinbase logo, mega-menu links (Crypto/Individuals/…), the search and
  // language icons, a ghost "Sign in" and the blue "Sign up" CDS pill.
  await S('promo-banner', q('header [class*="Banner"], header a[href*="ai-signup-offer"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The announcement row at the top of the header (Banner__StyledLink → /partner/ai-signup-offer) — real chrome, kept.', sel: 'header [class*=Banner] first' }, { noScroll: true });
  await S('header', q('[data-testid="main-nav"] [class*="StickyWrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The fixed site header (data-testid=main-nav): Coinbase logo, mega-menu links, search + language icons, Sign in ghost and the Sign up pill.', sel: '[data-testid=main-nav] [class*=StickyWrapper]' }, { noScroll: true });
  await S('logo', q('[data-testid="header-home-link"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Coinbase logo home anchor in the nav.', sel: '[data-testid=header-home-link]' }, { noScroll: true });
  await S('nav-item', q('[data-testid="main-nav-link-prices"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A mega-menu nav trigger ("Crypto", data-testid=main-nav-link-prices); its dropdown renders eager in the DOM.', sel: '[data-testid=main-nav-link-prices]' }, { noScroll: true });
  await S('nav-signin', q('header a[href*="/signin"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav sign-in', desc: 'The "Sign in" ghost button linking to login.coinbase.com; measured never followed.', sel: 'header a[href*=signin]' }, { noScroll: true });
  await S('nav-cta', q('header a[href*="/signup"].cds-Button, header a[href*="/signup"][data-testid="button"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The blue "Sign up" CDS pill (cds-Button, bgPrimary) in the nav; links to /signup, never followed.', sel: 'header a[href*=signup]' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"The most trusted crypto exchange" — the hero headline (CoinbaseDisplay scale).', sel: 'first visible h1' }, { noScroll: true });
  await S('hero-cta', q('main a[href*="signup"]').filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Sign up with Singpass" dark pill (cds-Button, bgInverse) under the hero copy; links to /signup, never followed.', sel: 'main a[href*=signup]' }, { noScroll: true });
  await S('carousel-card', q('[data-testid^="promo-carousel"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Promo card', desc: 'A promo-carousel card in the home flow (promo-carousel-item-*, autoplay rotating offers).', sel: '[data-testid^=promo-carousel] first' });
  await S('chip', q('main [data-testid="chip"]').filter({ visible: true }).first(), B4, { group: h, title: 'Filter chip', desc: 'A filter chip inside the dark asset panel on home ("Tradable"/"Top gainers"/"New on Coinbase", data-testid=chip, dark themed).', sel: '[data-testid=chip] first' });
  await S('dark-band', q('.coinbase.dark').filter({ visible: true }).first(), ['default'], { group: h, title: 'Dark panel', desc: 'The .coinbase.dark themed asset panel on home (the dark Tradable/Top-gainers card) — its paint lands on children; the theme element itself reads transparent.', sel: '.coinbase.dark' });
  await S('cta-dark', q('main a, main [data-testid="button"]').filter({ hasText: /See more assets/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Dark CTA', desc: 'The "See more assets" dark pill under the crypto band (fgInverse on bgInverse #0a0b0d, pill radius); links to /explore, never followed.', sel: 'main a:has-text("See more assets")' });
  await S('section-title', q('main h2, section h2').filter({ hasText: /Unlock|Explore crypto|Advanced|Built for/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section title', desc: 'A display section heading in page content ("Unlock zero trading fees…" style, CoinbaseDisplay scale).', sel: 'h2:has-text("Unlock|Explore crypto")' });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element painted fill — the page ground.', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function explore() {
  if (!(await newPage('explore'))) return;
  const g = G.explore;
  await S('explore-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Explore title', desc: '"Explore Crypto" — the prices page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('explore-search', q('[data-testid="input-interactable-area"], main input[type="search"], main input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Asset search field', desc: 'The asset search input on /explore (input-interactable-area) — a focus reading only; nothing typed.', sel: '[data-testid=input-interactable-area]' }, { noScroll: true });
  await S('price-table', q('[data-testid="prices-table-v2"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price table', desc: 'The live crypto price table (data-testid=prices-table-v2) with sortable columns.', sel: '[data-testid=prices-table-v2]' }, { noScroll: true });
  await S('price-row', q('[data-testid^="prices-table-v2-row-"]').filter({ visible: true }).first(), B4, { group: g, title: 'Price row', desc: 'An asset row in the price table (icon, name, price, sparkline, change).', sel: '[data-testid^=prices-table-v2-row-] first' });
  await S('price-figure', q('[data-testid^="prices-table-v2-row-"]').filter({ visible: true }).first().locator('xpath=./descendant-or-self::*[contains(text(),"S$")][1]'), ['default'], { group: g, title: 'Price figure', desc: 'A price figure cell in the price table (the "S$132,809.31"-style value).', sel: 'first S$ cell in first price row' });
  await S('sort-icon', q('[data-testid="table-sort-icon-up"], [data-testid="table-sort-icon-down"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sort icon', desc: 'A sort arrow on a sortable price-table column; measured at rest, never toggled.', sel: '[data-testid=table-sort-icon-*]' });
  save();
}

async function one() {
  if (!(await newPage('one'))) return;
  const g = G.one;
  await S('one-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Coinbase One title', desc: 'The Coinbase One subscription page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('one-cta', q('main a[href*="one"], main a[href*="signup"], main [data-testid="button"], main .cds-Button').filter({ visible: true }).first(), B4, { group: g, title: 'Coinbase One CTA', desc: 'The first CDS pill CTA on the Coinbase One page; links onward, never followed.', sel: 'main cds-Button first' }, { noScroll: true });
  save();
}

async function prime() {
  if (!(await newPage('prime'))) return;
  const g = G.prime;
  await S('prime-title', q('main h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Prime title', desc: 'The Coinbase Prime institutional page headline.', sel: 'first visible h1' }, { noScroll: true });
  await S('prime-cta', q('main a[href*="prime"], main a[href*="contact"], main [data-testid="button"], main .cds-Button').filter({ visible: true }).first(), B4, { group: g, title: 'Prime CTA', desc: 'The first CDS pill CTA on the Prime page; links onward, never followed.', sel: 'main cds-Button first' }, { noScroll: true });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 18000 }))) return;
  const g = G.signin;
  // /signin redirects to login.coinbase.com — the product's sign-in surface:
  // the card, OAuth/passkey rows and email field are measured at rest; the
  // field gets a focus reading only — nothing typed, nothing submitted.
  await S('signin-card', q('main [data-testid*="identity-multi-content-layout"]').filter({ visible: true }).last(), ['default'], { group: g, title: 'Sign-in card', desc: 'The login.coinbase.com sign-in surface the app paints. Measured at rest, never submitted.', sel: 'main/first visible sign-in container' }, { noScroll: true });
  await S('signin-field', q('[data-testid="email-input"], input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The sign-in email input (data-testid=email-input) — a focus reading only; nothing typed, nothing sent.', sel: '[data-testid=email-input]' }, { noScroll: true });
  await S('signin-submit', q('[data-testid="email-submit-button"], button').filter({ hasText: /Continue/ }).first(), B4, { group: g, title: 'Continue button', desc: 'The "Continue" submit on the sign-in card; measured never pressed — it would submit the form.', sel: '[data-testid=email-submit-button]' }, { noScroll: true });
  await S('signin-oauth', q('[data-testid="sign-in-with-google"], button').filter({ hasText: /Sign in with Google/i }).first(), B4, { group: g, title: 'OAuth button', desc: 'A "Sign in with Google" OAuth row on the sign-in card; measured never pressed.', sel: '[data-testid=sign-in-with-google]' }, { noScroll: true });
  await S('signin-passkey', q('[data-testid="sign-in-with-passkey"], button').filter({ hasText: /passkey/i }).first(), B4, { group: g, title: 'Passkey button', desc: 'The "Sign in with passkey" row on the sign-in card; measured never pressed.', sel: '[data-testid=sign-in-with-passkey]' }, { noScroll: true });
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
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The site footer: link columns (Company/Individuals/Businesses/Institutions/Developers/Support), social icons, region selector and the legal row.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] a').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A link in a footer link column.', sel: 'footer a first visible' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] a[href*="x.com"], [data-m-footer="1"] a[href*="twitter"], [data-m-footer="1"] a[href*="linkedin"], [data-m-footer="1"] a[href*="instagram"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon anchor (X/LinkedIn/Instagram).', sel: 'footer a[href*=x|linkedin|instagram]' }, { noScroll: true });
  const region = q('[data-m-footer="1"] button').filter({ hasText: /^Singapore$/ }).filter({ visible: true }).first();
  await S('footer-region', region.locator('xpath=..'), ['default'], { group: g, title: 'Region selector', desc: 'The "Language and region" pair in the footer (Singapore / English selectors) — the enclosing control cluster.', sel: 'parent of footer button:has-text("Singapore")' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  // At 390 the nav collapses to the mobile bar (data-testid=mobile-nav):
  // logo, search, language and the mobile-menu-toggle hamburger; the menu
  // opens on the button's own press.
  await S('m-header', q('[data-testid="mobile-nav"] [class*="StickyWrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile bar', desc: 'The 390 mobile nav bar (data-testid=mobile-nav): logo, search, language and menu toggle.', sel: '[data-testid=mobile-nav] inner bar' }, { noScroll: true });
  await S('m-menu-button', q('[data-testid="mobile-menu-toggle"], button[aria-label*="navigation menu" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (data-testid=mobile-menu-toggle, aria-label "open navigation menu"); its own press opens the menu.', sel: '[data-testid=mobile-menu-toggle]' }, { noScroll: true });
  const menuBtn = q('[data-testid="mobile-menu-toggle"], button[aria-label*="navigation menu" i]').filter({ visible: true }).first();
  if (await menuBtn.count()) {
    try { await menuBtn.click({ timeout: 5000 }); await page.waitForTimeout(1500); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  // The open menu is a fixed overlay holding the link list; tag whatever
  // fills the viewport and contains a nav link.
  await page.evaluate(() => {
    const p = [...document.querySelectorAll('body *')].find((e) => {
      const cs = getComputedStyle(e);
      const r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > 400 && r.width > 300 && (e.querySelector('a[href*="/explore"], a[href*="/signup"], [data-testid*="menu"] a'));
    });
    if (p) p.setAttribute('data-m-panel', '1');
  }).catch(() => {});
  await S('m-menu-open', q('[data-m-panel="1"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The menu overlay after the hamburger press.', sel: 'opened mobile menu overlay' }, { noScroll: true });
  await S('m-menu-link', q('[data-m-panel="1"] a, [data-m-panel="1"] button').filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link/accordion row inside the open mobile menu.', sel: 'first row inside the open menu' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero headline at 390.', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme (login.coinbase.com is the sign-in boundary)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, explore, one, prime, signin, mobile };
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
