// Measures classpass.com's public components in every state reachable
// without signing in, booking, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home search plans signin walk mobile (the footer group also runs on
// home). Writes raw/components-computed.json (merged) and one crop per
// component and state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// classpass.com is a React marketing + public-search app in one light theme;
// components are found by data-testid, role, CSS-module name prefix
// (AppHeader_*, Menu_*, Button_*, Login_*) or stable text — the hashed module
// suffixes are never selected. Cloudflare interstitials on sequential visits,
// so every route opens a fresh context and clearChallenge waits it out.
// Nothing is sent, booked or signed into: the only presses are local UI
// toggles — the header "How it works" dropdown, the search filter dropdowns,
// the FAQ accordion and the mobile menu trigger. The TrustArc consent
// overlay and the promo banner are hidden, never answered; every Log-in /
// Get-14-days-free / Book / Sign-in-with-* action is measured in all states
// except followed or pressed for real. /login's sign-in card and
// /walkthrough's trial-entry card are measured as documented boundaries.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', search: '/search', plans: '/plans', signin: '/login', walk: '/walkthrough' };
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

// A fixed, neutral place for every context: without it the site reads the capture machine's own location
// (the 2026-11 run recorded its country, prices in its currency and a distance-sorted nearby studio).
// The site can still place the run by its IP address; this pins what the browser itself reports.
const PLACE = { locale: 'en-US', timezoneId: 'America/New_York', geolocation: { latitude: 40.7128, longitude: -74.006 }, permissions: [] };

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, ...PLACE }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, ...PLACE });
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
  shell: 'Shell and navigation', home: 'Home', search: 'Public search',
  plans: 'Plans and pricing', signin: 'Sign-in page (boundary)',
  walk: 'Trial onboarding (boundary)', footer: 'Footer', mobile: 'Mobile (390 wide)',
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
  // The 64px top bar: the [data-testid=app-header] element itself.
  await S('header', q('[data-testid="app-header"], [class*="AppHeader_base"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The 64px top bar: wordmark, Search/Plans links, the "How it works" dropdown, Gifts/List-my-business/Corporate-wellness links, Log in and the promo CTA.', sel: 'div[data-testid=app-header]' }, { noScroll: true });
  await S('logo', q('a[aria-label="home"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The ClassPass wordmark anchor.', sel: 'a[aria-label=home]' }, { noScroll: true });
  await S('nav-item', q('a[href="/plans"]').filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain header link (Plans).', sel: 'header a[href=/plans]' }, { noScroll: true });
  // The "How it works" dropdown trigger (Headless UI menu button); its own
  // press opens the link menu — the opened state, then the menu panel and a
  // menu card are read while it stays up.
  const dropTrg = q('[class*="NavDesktopDropdown_Button"]').filter({ visible: true }).first();
  await S('nav-dropdown', dropTrg, [...B4, 'opened'], { group: g, title: 'Nav dropdown', desc: 'The "How it works" menu trigger (aria-haspopup=menu); its own press opens the link menu (opened state).', sel: 'button.NavDesktopDropdown_Button' }, { noScroll: true });
  const menuIsOpen = () => page.evaluate(() => {
    const m = document.querySelector('[id*="headlessui-menu-items"], [role="menu"]');
    const r = m && m.getBoundingClientRect();
    return !!(r && r.height > 0 && r.top >= 0 && r.top < 900);
  });
  const ensureMenuOpen = async () => {
    if (!(await menuIsOpen())) { await toggle(dropTrg); await page.waitForTimeout(900); }
  };
  const markMenu = () => page.evaluate(() => {
    const m = document.querySelector('[id*="headlessui-menu-items"], [role="menu"]');
    if (!m) return;
    m.setAttribute('data-m-panel', '1');
    const item = [...m.querySelectorAll('a,[role="menuitem"],li>div,li>button')].find((n) => n.getBoundingClientRect().height > 10);
    if (item) item.setAttribute('data-m-card', '1');
  });
  await S('menu-panel', q('[data-m-panel="1"]'), ['default'], { group: g, title: 'Nav menu', desc: 'The "How it works" dropdown panel (Walkthrough / How ClassPass works / Features links), held open by the trigger toggle.', sel: '[role=menu] under the open trigger' }, { noScroll: true, noReset: true, open: async () => { await ensureMenuOpen(); await markMenu(); } });
  await S('menu-card', q('[data-m-card="1"]'), ['default'], { group: g, title: 'Menu item', desc: 'A link row inside the open nav menu.', sel: 'first link inside [role=menu]' }, { noScroll: true, noReset: true, open: ensureMenuOpen });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('nav-login', q('a[href="/login"]').filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The header "Log in" link; measured never followed.', sel: 'header a[href=/login]' }, { noScroll: true });
  await S('nav-cta', q('[data-testid="NavCta"], [data-testid="NavCta"] a, [data-testid="NavCta"] button').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The "\u{1F4A5} Get 14 days free \u{1F4A5}" promo button; links to /walkthrough, measured never followed.', sel: '[data-testid=NavCta]' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('[class*="HomepageHeroC_heading"], h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: '"One app for <rotating word>" — the circuit display headline (the activity word cycles).', sel: 'h1.HomepageHeroC_heading' }, { noScroll: true });
  await S('hero-sub', q('[class*="HomepageHeroC_subtitle"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subcopy', desc: 'The norms lede under the display headline.', sel: '.HomepageHeroC_subtitle' }, { noScroll: true });
  // The animated activity card in the hero (photo card cycling venues).
  await S('hero-card', q('[class*="HeroAnimationBlock_card__"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero activity card', desc: 'One of the rotating activity photo cards beside the headline (the deck cycles).', sel: '.HeroAnimationBlock_card' }, { noScroll: true });
  // The page ground: body paints transparent; the html element carries the
  // white fill under every section. Read it directly.
  await S('page-ground', q('html'), ['default'], { group: h, title: 'Page ground', desc: "The html element's own painted fill — the white ground under every section (body itself is transparent).", sel: 'document.documentElement' }, { noScroll: true, crop: false });
  save();
}

async function search() {
  if (!(await newPage('search'))) return;
  const g = G.search;
  await S('search-box', q('[data-testid="SearchBox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Search box', desc: 'The activity + location combobox pair on the public results page.', sel: '[data-testid=SearchBox]' }, { noScroll: true });
  // The activity field (empty placeholder — a fill can be typed and cleared
  // without losing a prefilled value).
  await S('search-field', q('[data-testid="SearchBoxField"] input, input[placeholder*="pilates" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Activity field', desc: 'The "Yoga, pilates, massage\u2026" combobox field; filled with sample text then deleted, never searched.', sel: 'SearchBoxField input[placeholder~=pilates]' }, { fillText: 'yoga' });
  // The location field comes prefilled with the geo-detected area — typing
  // and clearing would lose it, so it is focused only.
  await S('search-loc', q('input[placeholder*="neighborhood" i]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Location field', desc: 'The "City, neighborhood" combobox, prefilled with the detected area — focused only so the prefilled value survives.', sel: 'input[placeholder~=neighborhood]' });
  // Filter row: the vertical pill and a multi-select dropdown (its own press
  // opens the option panel — a local toggle).
  await S('filter-pill', q('[data-testid="VerticalsFilter"] button, [data-testid="VerticalsFilter"]').filter({ visible: true }).first(), B4, { group: g, title: 'Vertical pill', desc: 'The "Fitness" vertical pill in the filter bar; its press opens the verticals switcher.', sel: '[data-testid=VerticalsFilter] button' });
  const multi = q('[data-testid="MultiSelectFilter"] button, [data-testid="MultiSelectFilter"]').filter({ hasText: /activities/i }).filter({ visible: true }).first();
  await S('filter-multi', multi, [...B4, 'opened'], { group: g, title: 'Filter dropdown', desc: 'The "Activities" multi-select trigger; its own press opens the option panel (opened state).', sel: '[data-testid=MultiSelectFilter] button:has-text("Activities")' });
  // The options panel is a styled-component div (fully hashed class): mark
  // the positioned div holding the activity list plus the Clear/Done actions.
  const fp = await page.evaluate(() => {
    const m = [...document.querySelectorAll('div')].find((n) => {
      const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
      if (r.width < 200 || r.width > 600 || r.height < 150 || r.height > 700 || r.top < 20 || r.top > 700) return false;
      if (cs.position !== 'absolute' && cs.position !== 'fixed') return false;
      const tt = n.innerText || '';
      return /\bClear\b/.test(tt) && /\bDone\b/.test(tt) && /Yoga|Barre|HIIT|Pilates/.test(tt) && tt.length < 500;
    });
    if (!m) return false;
    m.setAttribute('data-m-fpanel', '1');
    return true;
  });
  await S('filter-panel', fp ? q('[data-m-fpanel="1"]') : q('[data-m-fpanel="__none__"]'), ['default'], { group: g, title: 'Filter panel', desc: 'The opened Activities option panel.', sel: 'opened dropdown under Activities' });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  await S('venue-card', q('[data-testid="VenueItem"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Venue card', desc: 'A studio result card (photo, name, rating, distance); links to the public venue page, hovered never followed.' });
  await S('venue-rating', q('[data-testid="StarRating"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Star rating', desc: 'The "4.8 (27500+)" star-rating row inside a venue card.' });
  await S('universal-cta', q('[data-testid="UniversalCta"], a[class*="bt--primary"], a[class*=" bt--"]').filter({ visible: true }).first(), B4, { group: g, title: 'Universal CTA', desc: 'The "Get 14 days free" pill rendered with the bt--primary classes; links to /walkthrough, never followed.', sel: '[data-testid=UniversalCta] / a.bt--primary' });
  save();
}

async function plans() {
  if (!(await newPage('plans'))) return;
  const g = G.plans;
  await S('plans-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plans title', desc: '"Pick a plan that works for you" in 60px circuit.', sel: 'h1' }, { noScroll: true });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section title', desc: 'The first section heading on the plans page (norms 24px).', sel: 'first h2' }, { noScroll: true });
  // The credit-plan carousel: the slide carrying the DEFAULT pill is the
  // recommended plan; slides are ~267px cards.
  await S('plan-slide', q('[class*="AvailablePlansCarousel_slide__"]').filter({ hasText: /default/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Plan slide (default)', desc: 'The recommended "45 credits" plan slide (the DEFAULT pill); prices render in the detected locale (SGD here).', sel: '.AvailablePlansCarousel_slide:has-text(DEFAULT)' });
  await S('plan-price', q('[data-testid="AvailablePlanSlide-price"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The "SGD 99 /mo" price row inside a slide.' });
  await S('plan-pill', q('[data-testid="Pill"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan pill', desc: 'The DEFAULT tag on the recommended slide.' });
  await S('loc-selector', q('[data-testid="LocationSelector"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Location selector', desc: 'The detected-market pill pricing is quoted in; a locale control, never toggled.' });
  // The FAQ accordion: the trigger's own press opens the answer.
  await S('faq-question', q('[data-testid="faq-question"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'FAQ question', desc: 'An FAQ accordion trigger; its own press opens the answer (opened state).' });
  await page.keyboard.press('Escape');
  // A page-level CTA in the CMS body ("Get started"-type link).
  await S('cms-cta', q('[data-testid="CmsBaseCta"] a, [data-testid="CmsBaseCta"] button, [data-testid="CmsBaseCta"]').filter({ visible: true }).first(), B4, { group: g, title: 'Page CTA', desc: 'A CMS call-to-action in the plans body; never followed.' });
  save();
}

async function signin() {
  if (!(await newPage('signin'))) return;
  const g = G.signin;
  await S('signin-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in title', desc: '"Welcome back" on the public sign-in card.', sel: 'h1' }, { noScroll: true });
  await S('signin-email', q('input[name="email"], [data-testid="LoginEmailInput"] input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'E-mail field', desc: 'The e-mail input; filled with the documented test address then deleted, Log in never pressed.', sel: 'input[name=email]', fillText: 'name@example.com' });
  await S('signin-pass', q('input[name="password"], [data-testid="LoginPasswordInput"] input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input; focused only, never filled.', sel: 'input[name=password]' });
  await S('signin-submit', q('[data-testid="LoginSubmitButton"] button, [data-testid="LoginSubmitButton"], button[class*="buttonColor-primary"]').filter({ visible: true }).first(), B4, { group: g, title: 'Log-in button', desc: 'The primary "Log in" submit; measured in all non-submitting states, never pressed for real.', sel: '[data-testid=LoginSubmitButton]' });
  await S('signin-apple', q('[data-testid="SignInWithApple"] button, [data-testid="SignInWithApple"], button').filter({ hasText: /sign in with apple/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Apple sign-in', desc: 'The "Sign in with Apple" OAuth button; never followed.', sel: '[data-testid=SignInWithApple]' });
  await S('signin-google', q('[data-testid="SignInWithGoogle"] button, [data-testid="SignInWithGoogle"], button').filter({ hasText: /sign in with google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google sign-in', desc: 'The "Sign in with Google" OAuth button; never followed.', sel: '[data-testid=SignInWithGoogle]' });
  await S('signin-forgot', q('a[class*="forgotPassword"], a').filter({ hasText: /forgot your password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot-password link', desc: 'The "Forgot your password?" link; never followed.', sel: 'a.Login_forgotPassword' });
  save();
}

async function walk() {
  if (!(await newPage('walk'))) return;
  const g = G.walk;
  await S('walk-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Trial title', desc: '"What your trial includes" — the first onboarding card, the entry the promo CTAs link to.', sel: 'h1' }, { noScroll: true });
  // The primary step action (Continue/Get started): measured, never pressed.
  await S('walk-cta', q('button[class*="buttonColor-mkt-black"]').filter({ visible: true }).first(), B4, { group: g, title: 'Step CTA', desc: 'The black "Next" step button; measured in all non-submitting states, never pressed — pressing advances account creation.', sel: 'button.Button_buttonColor-mkt-black' });
  await S('walk-slide', q('[class*="WalkThrough_slide"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Benefit slide', desc: 'A "What your trial includes" benefit slide (icon + heading + body).', sel: '.WalkThrough_slide' });
  await S('walk-dots', q('[class*="WalkThrough_dots"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Step dots', desc: 'The onboarding progress dots (the first is active).', sel: '.WalkThrough_dots' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document
  // that is actually open.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1600);
  // The footer band: the widest tall ancestor of a social link, else the
  // footer landmark itself.
  // The footer landmark itself (footer.Footer_footer), not an inner column.
  await page.evaluate(() => {
    const f = document.querySelector('footer, [role="contentinfo"], [class*="Footer_footer"]');
    if (f) f.setAttribute('data-m-footer', '1');
  });
  await S('footer', q('[data-m-footer="1"]'), ['default'], { group: g, title: 'Footer', desc: 'The footer band: link columns, the app-store badges, social icons, the legal subfooter.', sel: 'footer.Footer_footer' }, { noScroll: true });
  await S('footer-link', q('[data-m-footer="1"] a[href="/about"], [class*="Footer"] a[href="/about"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a[href=/about]' }, { noScroll: true });
  await S('footer-social', q('[data-m-footer="1"] a[href*="facebook" i], [class*="Footer"] a[href*="facebook" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A footer social icon link (Facebook).', sel: 'footer a[href*=facebook]' }, { noScroll: true });
  // An app-store badge link in the AppDownloadIcons row.
  await S('app-badge', q('[class*="AppDownloadIcons"] a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'App-store badge', desc: 'An app-store badge link in the footer; never followed. The anchor hugs the text line — the badge art is an oversized inline child (see the crop).', sel: 'footer .AppDownloadIcons a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('[data-testid="app-header"], [class*="AppHeader_base"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'div[data-testid=app-header] at 390' }, { noScroll: true });
  // The yellow promo banner under the bar (visible at this width).
  await S('m-banner', q('[class*="Banner_"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The yellow "Get 14 days free" promo bar at this width; captured as UI, its Close never pressed.', sel: 'div.Banner_*' }, { noScroll: true });
  const menuBtn = q('[class*="Menu_toggler"]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, ['default'], { group: g, title: 'Menu button', desc: 'The hamburger at the bar\'s right edge; its own press opens the menu overlay.', sel: 'button.Menu_toggler' }, { noScroll: true });
  if (await menuBtn.count()) {
    try { await toggle(menuBtn); await page.waitForTimeout(1200); } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  }
  // The open overlay: the menu container, not body.
  await page.evaluate(() => {
    const cands = [...document.querySelectorAll('[class*="Menu_"], nav, [role="dialog"], [class*="Drawer"], [class*="menu"]')]
      .filter((n) => { const r = n.getBoundingClientRect(); const cs = getComputedStyle(n); return r.height > 300 && r.width > 300 && (cs.position === 'fixed' || cs.position === 'absolute') && r.top <= 140; })
      .sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height);
    if (cands[0]) cands[0].setAttribute('data-m-mopen', '1');
    const link = cands[0] && [...cands[0].querySelectorAll('a')].find((n) => (n.innerText || '').trim().length > 2 && n.getBoundingClientRect().height > 10);
    if (link) link.setAttribute('data-m-mlink', '1');
  });
  await S('m-menu-open', q('[data-m-mopen="1"]'), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The menu overlay after the toggler\'s own press.', sel: 'fixed/absolute menu container after Menu_toggler press' }, { noScroll: true });
  await S('m-menu-link', q('[data-m-mlink="1"]'), B4, { group: g, title: 'Menu link', desc: 'A link row inside the open mobile menu.', sel: 'first link in the open menu' }, { noScroll: true });
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
const plan = { home, search, plans, signin, walk, mobile };
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
