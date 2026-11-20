// Measures deezer.com's public components in every state reachable without
// signing in, subscribing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home offers artist album login signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// deezer.com is a light/dark marketing site plus a dark Chakra-UI web app that
// is public signed-out on the catalog pages (/en/artist/*, /en/album/*,
// /en/playlist/*), with the dark login/signup forms on account.deezer.com.
// The css-* classes are hashed, so specs select by role, aria-label, structure
// or text. Nothing is sent, bought or signed into: the only presses are local
// UI toggles — the "View menu" track overflow (a Chakra popover), the
// Monthly/Annual billing toggle and the mobile hamburger; the search field is
// typed into and cleared, never submitted; Log in, Sign up, Try for free and
// every payment/go.php link are measured, never followed. The "A note about
// our cookies" GDPR modal is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/en/', offers: '/en/offers', artist: '/en/artist/27', album: '/en/album/302127', login: 'https://account.deezer.com/en/login/', signup: 'https://account.deezer.com/en/signup/', mobile: '/en/artist/27' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
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
  const cleared = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

// A failed re-read must not erase an earlier successful one: keep the saved
// style and record the failed attempt beside it. comp() has already stamped
// this run's date on the component, so the kept state is pinned to the run
// that actually read it (its own run stamp, else the component's earlier run)
// and an old reading is never republished as a new one.
function keepEarlier(c, state, e, earlierRun) {
  const err = String(e.message || e).slice(0, 200);
  const prev = c.states[state];
  if (prev && prev.style) {
    prev.rerunError = err;
    prev.read ??= prev.run || earlierRun; // a second failed re-read keeps the first date
    prev.rerunOn = run;
  } else c.states[state] = { error: err };
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
    keepEarlier(c, state, e, opts.earlierRun);
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
  // Found this run: its states are re-read below, so an earlier miss no longer
  // describes them (the builders flag every token read from a component that
  // still carries recaptureMissed).
  delete out.components[key].recaptureMissed;
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
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via, earlierRun: keep?.run });
    } catch (e) {
      keepEarlier(out.components[key], st, e, keep?.run);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
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
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

const G = {
  shell: 'App shell and navigation', home: 'Home (light)', offers: 'Offers (dark marketing)',
  artist: 'Artist page (dark app)', player: 'Player bar', banner: 'Signup banner',
  login: 'Login and signup', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the track overflow menu: the "..." (aria-label "View menu") button is a
// Chakra popover trigger — a local UI toggle, never a link. The panel stays open
// so the popover and one item can be measured; Escape closes it afterwards.
async function openTrackMenu() {
  // "Open" means a populated content section with a real height: the popper
  // wrappers report visible while the panel still animates from 0px, and a
  // zero-height panel reads as not-visible to the measurer.
  const populated = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('.chakra-popover__content')].some((el) => el.getBoundingClientRect().height > 10 && /\S/.test(el.textContent || '') && getComputedStyle(el).visibility !== 'hidden'),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await populated(400)) return 'the overflow popover was already open';
  const item = page.locator('button[aria-label="View menu"]').filter({ visible: true }).first();
  if (!(await item.count())) return 'no View-menu trigger';
  for (let i = 0; i < 3; i++) {
    await item.click({ timeout: 4000 }).catch(() => item.evaluate((el) => el.click()));
    if (await populated(5000)) return 'clicked "View menu" to open the track overflow popover';
    await page.waitForTimeout(600);
  }
  return 'clicked "View menu"; the popover did not report open';
}

// Opens the mobile nav overlay: the .burger-menu div toggles a full-viewport
// ul.burger-menu-content. A local UI toggle; its links are never followed.
async function openBurgerMenu() {
  const ok = () => page.waitForFunction(() => { const el = document.querySelector('ul.burger-menu-content'); return el && el.getBoundingClientRect().height > 100; }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await ok()) return 'the nav overlay was already open';
  const b = page.locator('.burger-menu').filter({ visible: true }).first();
  if (!(await b.count())) return 'no burger toggle';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok()) return 'clicked the burger to open the nav overlay';
    await page.waitForTimeout(500);
  }
  return 'clicked the burger; the overlay did not report open';
}

// The Monthly/Annual offers segmented control toggles prices locally.
async function annualToggle() {
  const t = page.locator('button, [role="tab"], a, label').filter({ hasText: /^\s*Annual\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return 'no Annual toggle';
  await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return 'clicked Annual on the billing toggle';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header, [class*="topbar" i], [class*="header" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing header', desc: 'The dark top bar over the light hero: wordmark, Plans/Features/Music, Log in and the purple Sign up pill.', sel: 'header / .topbar' }, { noScroll: true });
  await S('mkt-logo', q('a.tempo-topbar-deezer-logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Deezer heart-and-wordmark in the header.', sel: 'a.tempo-topbar-deezer-logo' }, { noScroll: true });
  await S('mkt-nav-link', q('a.tempo-link').filter({ hasText: /^\s*(Plans|Features|Music)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header link (Plans/Features/Music); measured, never followed.', sel: 'a.tempo-link' }, { noScroll: true });
  await S('mkt-login', q('header a, header button, [class*="topbar" i] a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in button', desc: 'The dark-outline Log-in pill; links to account.deezer.com, measured never followed.', sel: 'header Log in' }, { noScroll: true });
  await S('mkt-signup', q('header a, header button, [class*="topbar" i] a, a.topbar-action').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button', desc: 'The purple Sign-up pill in the header; measured never followed.', sel: 'a.topbar-action Sign up' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1, [class*="hero" i] h1, [class*="title" i]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"WHERE MUSIC COMES TO LIFE" — the condensed display headline on the light hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h2, p, [class*="subtitle" i]').filter({ hasText: /music streaming/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero sub', desc: '"Music streaming by Deezer" under the headline.', sel: 'hero sub' }, { noScroll: true });
  await S('hero-cta', q('a.tempo-btn-primary, a.tempo-btn-m').filter({ hasText: /^\s*Try for free\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The purple "Try for free" pill under the hero copy; measured never followed.', sel: 'hero Try for free' });
  await S('rating', q('p').filter({ hasText: /5-star ratings/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Rating line', desc: 'The five-star "Over 3 million 5-star ratings" strip under the hero.', sel: 'rating block' });
  await S('section-h2', q('h2.heading-2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  save();
}

async function offers() {
  if (!(await newPage('offers'))) return;
  await sheetsFor('offers');
  await chrome('offers');
  const g = G.offers;
  await S('offers-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Offers headline', desc: '"Get 1 month of Premium free" — the display heading on the dark offers page.', sel: 'h1 on /en/offers' }, { noScroll: true });
  await S('billing-toggle', q('ul.toggle-premiumtab, .toggle-container').filter({ visible: true }).first(), B4, { group: g, title: 'Billing toggle', desc: 'The Monthly/Annual segmented control over the plan cards; toggled, never checked out.', sel: 'ul.toggle-premiumtab' }, { noScroll: true });
  await S('toggle-option', q('ul.toggle-premiumtab li, .toggle-container li').filter({ hasText: /^\s*Annual\s*$/ }).filter({ visible: true }).first(), ['default', 'focus-visible'], { group: g, title: 'Toggle option', desc: 'The "Annual" option inside the billing toggle; clicked open for the annual shot, never checked out.', sel: 'ul.toggle-premiumtab li Annual' }, { noScroll: true });
  await S('plan-card', q('li.card-container, [class*="card-container" i], .unlogged-card').filter({ hasText: /PREMIUM/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A white plan card (PREMIUM) on the purple band: title chip, account count, free month, price, Try-for-free CTA and Learn more.', sel: 'li.card-container' });
  await S('plan-title', q('.unlogged-card-title, [class*="card-title" i], h2').filter({ hasText: /PREMIUM/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name chip', desc: 'The purple "PREMIUM" chip on the plan card.', sel: '.unlogged-card-title' });
  await S('plan-price', q('.unlogged-card-description, [class*="card-description" i], [class*="price" i]').filter({ hasText: /month|free/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price line', desc: '"1 month free / then US$11.99/month" on the card.', sel: '.unlogged-card-description' });
  await S('plan-cta', q('a.tempo-btn, [class*="card-container" i] a, .unlogged-card a').filter({ hasText: /try for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The black "Try for free" action on the plan card — links to payment/go.php; measured never followed.', sel: 'a.tempo-btn Try for free' });
  await S('learn-more', q('a.unlogged-card-caption, [class*="card-container" i] a').filter({ hasText: /learn more|1 month free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Learn more link', desc: 'The underlined caption link inside the plan card; measured never followed.', sel: 'a.unlogged-card-caption' });
  save();
}

async function artist() {
  if (!(await newPage('artist'))) return;
  await sheetsFor('artist');
  await chrome('artist');
  const g = G.shell;
  const side = q('a.chakra-link[href="/en/"]').filter({ hasText: /^\s*Home\s*$/ }).filter({ visible: true }).first().locator('xpath=ancestor::div[3]');
  await S('a-sidebar', side, ['default'], { group: g, title: 'App sidebar', desc: 'The left rail: DEEZER wordmark, Home/Explore, the Playlists promo card with Create-a-playlist.', sel: 'sidebar rail (Home-link ancestor)' }, { noScroll: true });
  await S('a-logo', side.locator('a').first(), ['default'], { group: g, title: 'Sidebar logo', desc: 'The DEEZER wordmark at the top of the rail.', sel: 'sidebar logo' }, { noScroll: true });
  await S('a-nav-home', q('a.chakra-link[href="/en/"]').filter({ hasText: /^\s*Home\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar link', desc: 'The "Home" nav item (icon + label); measured, never followed.', sel: 'a.chakra-link Home' }, { noScroll: true });
  await S('a-nav-explore', q('a.chakra-link[href*="/channels/"]').filter({ hasText: /^\s*Explore\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar link 2', desc: 'The "Explore" nav item; measured, never followed.', sel: 'a.chakra-link Explore' }, { noScroll: true });
  await S('a-playlist-promo', q('div, aside, section').filter({ hasText: /create your first playlist/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Playlist promo card', desc: 'The sidebar "Create your first playlist" card — an upsell/empty-state nudge.', sel: 'sidebar promo card' }, { noScroll: true });
  await S('a-create-playlist', q('button, a').filter({ hasText: /^\s*Create a playlist\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Create playlist button', desc: "The promo card's white \"Create a playlist\" action; measured, never clicked (it would need an account).", sel: 'Create a playlist' }, { noScroll: true });
  await S('a-plans-link', q('a.chakra-link').filter({ hasText: /^\s*Plans\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plans link', desc: 'The header "Plans" link to /en/offers; measured, never followed.', sel: 'header Plans' }, { noScroll: true });
  await S('a-login', q('a.chakra-button').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in button (app)', desc: 'The dark-outline Log-in pill in the app header; links to account.deezer.com, measured never followed.', sel: 'a.chakra-button Log in' }, { noScroll: true });
  await S('a-signup', q('a.chakra-button').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up button (app)', desc: 'The purple Sign-up pill in the app header; measured never followed.', sel: 'a.chakra-button Sign up' }, { noScroll: true });
  const a = G.artist;
  await page.locator('button[aria-label="Mix"]').first().waitFor({ state: 'visible', timeout: 20000 }).catch(() => {});
  await page.locator('a[role="tab"].navbar-link').first().waitFor({ state: 'visible', timeout: 10000 }).catch(() => {});
  await S('artist-avatar', q('img.chakra-image').filter({ visible: true }).first(), ['default'], { group: a, title: 'Artist image', desc: "The artist's round photo in the page header (the first large chakra-image on the page).", sel: 'img.chakra-image' }, { noScroll: true });
  await S('artist-name', q('h1, h2').filter({ hasText: /^Daft Punk$/ }).filter({ visible: true }).first(), ['default'], { group: a, title: 'Artist name', desc: "The artist's display name heading.", sel: 'artist h1' }, { noScroll: true });
  await S('artist-fans', q('p, span, div').filter({ hasText: /fans$/ }).filter({ visible: true }).last(), ['default'], { group: a, title: 'Fan count', desc: 'The "5,237,122 fans" muted count under the name.', sel: 'fans text' }, { noScroll: true });
  await S('mix-btn', q('button[aria-label="Mix"]').filter({ visible: true }).first(), B4, { group: a, title: 'Mix button', desc: 'The purple "▶ Mix" primary action; measured, never pressed (it would start playback and, signed out, a paywall).', sel: 'button[aria-label=Mix]' });
  await S('fav-btn', q('button[aria-label="Add"]').filter({ visible: true }).first(), B4, { group: a, title: 'Favourite icon button', desc: 'The heart "Add" icon button beside Mix; measured, never toggled (it needs an account).', sel: 'button[aria-label=Add]' });
  await S('menu-btn', q('button[aria-label="View menu"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: a, title: 'Track overflow button', desc: 'The "..." ("View menu") icon button — a Chakra popover trigger; the opened state was measured after clicking it, its items never followed.', sel: 'button[aria-label="View menu"]' });
  await S('menu-popover', q('.chakra-popover__content').filter({ hasText: /\S/ }).filter({ visible: true }).last(), ['default'], { group: a, title: 'Overflow popover', desc: 'The track overflow menu opened by its own trigger (a Chakra popper panel); its items were never followed.', sel: 'popper panel' }, { open: openTrackMenu, noScroll: true, noReset: true });
  await S('menu-item', q('.chakra-popover__content li, .chakra-popover__content button, .chakra-popover__content a, [role="menuitem"]').filter({ hasText: /\S/ }).filter({ visible: true }).first(), ['default'], { group: a, title: 'Overflow menu item', desc: 'An item inside the opened overflow popover; measured, never followed.', sel: 'popper item' }, { open: openTrackMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('tabs-nav', q('nav.navbar, [role="tablist"]').filter({ visible: true }).first(), ['default'], { group: a, title: 'Tab strip', desc: 'The Discography/Top-tracks/Similar-artists/Playlists/Bio tab bar under the artist header.', sel: 'nav.navbar' });
  await S('tab-item', q('a[role="tab"].navbar-link, a[role="tab"]').filter({ hasText: /^\s*Discography\s*$/ }).filter({ visible: true }).first(), B4, { group: a, title: 'Tab item', desc: 'The selected "Discography" tab (a real link with an underline indicator); measured, never followed.', sel: 'a[role=tab].navbar-link' });
  await S('track-list', q('div[role="row"].JR0qJ').filter({ visible: true }).first().locator('xpath=ancestor::*[self::ol or self::ul or contains(@class,"track") or @role="table" or @role="grid"][1]'), ['default'], { group: a, title: 'Track list', desc: 'The "Top tracks" numbered list under the tab bar.', sel: 'tracklist (row ancestor)' });
  await S('track-row', q('div[role="row"].JR0qJ').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: a, title: 'Track row', desc: 'A numbered track row (play button, title, heart, "...") in Top tracks.', sel: 'div[role=row].JR0qJ' });
  await S('track-play', q('button[aria-label^="Play "]').filter({ visible: true }).first(), B4, { group: a, title: 'Track play button', desc: "A row's purple circular play button (\"Play Instant Crush ...\"); measured, never pressed.", sel: 'button[aria-label^=Play]' });
  await S('track-fav', q('button[aria-label="Add to Favourite tracks"]').filter({ visible: true }).first(), B4, { group: a, title: 'Track favourite button', desc: "A row's heart icon button; measured, never toggled.", sel: 'button[aria-label="Add to Favourite tracks"]' });
  await S('view-all', q('button, a').filter({ hasText: /^\s*View all\s*$/i }).filter({ visible: true }).first(), B4, { group: a, title: 'View all button', desc: "The section's \"View all\" ghost action; measured, never followed.", sel: 'View all' });
  await S('a-section-h2', q('h2').filter({ hasText: /top tracks|playlists|similar artists/i }).filter({ visible: true }).first(), ['default'], { group: a, title: 'Section heading (app)', desc: 'A catalog section heading ("Top tracks"/"Playlists").', sel: 'section h2' });
  await S('playlist-card', q('a').filter({ hasText: /100% Daft Punk|80s Electronic/i }).filter({ visible: true }).first().locator('xpath=ancestor::*[@role="group"][1]'), B4, { group: a, title: 'Playlist card', desc: 'A "Playlists" aside card (cover, title, fan count, heart); measured, never followed.', sel: 'aside playlist card' });
  const bn = G.banner;
  await S('signup-banner', q('a, button').filter({ hasText: /^\s*Sign up for free\s*$/i }).filter({ visible: true }).first().locator('xpath=ancestor::div[1]'), ['default'], { group: bn, title: 'Signup banner', desc: 'The light-purple "Live the music with Deezer" upsell strip pinned above the player bar.', sel: 'signup banner (CTA ancestor)' }, { noScroll: true });
  await S('banner-cta', q('a, button').filter({ hasText: /^\s*Sign up for free\s*$/i }).filter({ visible: true }).first(), B4, { group: bn, title: 'Banner CTA', desc: "The banner's purple \"Sign up for free\" pill; measured never followed.", sel: 'Sign up for free' }, { noScroll: true });
  const pl = G.player;
  const bar = q('div:has(button[aria-label="volume button"]):has(a.chakra-link)').last();
  await S('player-bar', bar, ['default'], { group: pl, title: 'Player bar', desc: 'The bottom playback bar: track title/artists, heart and add, transport controls, queue and volume.', sel: 'fixed bar holding the transport buttons' }, { noScroll: true });
  await S('player-track', bar.locator('a.chakra-link').filter({ hasText: /Instant Crush/i }).filter({ visible: true }).first(), ['default'], { group: pl, title: 'Player track', desc: "The playing track's title in the player bar.", sel: 'player track title' }, { noScroll: true });
  await S('player-play', bar.locator('button[aria-label="Play"]').filter({ visible: true }).first(), B4, { group: pl, title: 'Play button (player)', desc: "The player's round purple play toggle; measured, never pressed.", sel: 'player Play' }, { noScroll: true });
  await S('player-prev', bar.locator('button[aria-label="Back"]').filter({ visible: true }).first(), B4, { group: pl, title: 'Previous button', desc: 'The player\u2019s back-track icon button (aria-label "Back"); measured, never pressed.', sel: 'player Back' }, { noScroll: true });
  await S('player-next', bar.locator('button[aria-label="Next"]').filter({ visible: true }).first(), B4, { group: pl, title: 'Next button', desc: "The player's next-track icon button; measured, never pressed.", sel: 'player Next' }, { noScroll: true });
  await S('player-shuffle', bar.locator('button[aria-label="Turn on Shuffle"]').filter({ visible: true }).first(), B4, { group: pl, title: 'Shuffle button', desc: "The player's shuffle icon button; measured, never toggled.", sel: 'player Shuffle' }, { noScroll: true });
  await S('player-more', bar.locator('button[aria-label="Open context menu"]').filter({ visible: true }).first(), B4, { group: pl, title: 'Player overflow', desc: "The player's context-menu icon button; measured, never opened.", sel: 'player Open context menu' }, { noScroll: true });
  // The header search navigates to /search/<q> as it is typed, so it is
  // measured last on this page.
  await S('a-search', q('input.chakra-input[aria-label="Search"], input[aria-label="Search"], input[placeholder*="Artists" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The "Artists, tracks, podcasts..." header search; focused and typed into then cleared — never submitted. Typing into it navigates to a search-results page, which is why it is measured last here.', sel: 'input.chakra-input[aria-label=Search]' }, { noScroll: true, fillText: 'daft punk' });
  save();
}

async function album() {
  if (!(await newPage('album'))) return;
  await sheetsFor('album');
  await chrome('album');
  const g = G.artist;
  await S('album-cover', q('img.chakra-image').filter({ visible: true }).first(), ['default'], { group: g, title: 'Album cover', desc: "The album's square cover art in the page header (the first large chakra-image).", sel: 'img.chakra-image' }, { noScroll: true });
  await S('album-title', q('h2.chakra-heading, h1').filter({ hasText: /^Discovery$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Album title', desc: "The album's title heading.", sel: 'album title h2' }, { noScroll: true });
  await S('album-play', q('button[aria-label^="Play "]').filter({ visible: true }).first(), B4, { group: g, title: 'Track play button', desc: 'The first track row\'s purple circular play button; measured, never pressed.', sel: 'button[aria-label^=Play]' });
  await S('album-track-row', q('div[role="row"]').filter({ hasText: /One More Time/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Album track row', desc: 'A numbered track row on the album page.', sel: 'div[role=row]' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-logo', q('a[href*="deezer.com"], a:has(svg), [class*="logo" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login logo', desc: 'The Deezer wordmark over the form; links back to deezer.com, measured never followed.', sel: 'login logo' }, { noScroll: true });
  await S('login-field-email', q('input.chakra-input, input[type="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The login e-mail input; focused and typed into then cleared — never submitted.', sel: 'input.chakra-input (1st)' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-field-password', q('input.chakra-input[type="password"], input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field', desc: 'The login password input; focused and typed into then cleared — never submitted.', sel: 'input[type=password]' }, { noScroll: true, fillText: 'not-a-real-password' });
  await S('login-show-password', q('button[aria-label*="password" i], button[aria-label="show-password"]').filter({ visible: true }).first(), B4, { group: g, title: 'Show-password button', desc: 'The eye icon button inside the password field (a local reveal toggle); measured, never clicked.', sel: 'button[aria-label=show-password]' }, { noScroll: true });
  await S('login-submit', q('button.chakra-button').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in submit', desc: 'The login submit button; its states were measured but the button was never clicked — nothing was submitted.', sel: 'login Log in' }, { noScroll: true });
  await S('login-forgot', q('a.chakra-form__helper-text, a').filter({ hasText: /forgotten password|forgot password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgotten-password link', desc: 'The "Forgotten password?" helper link; measured, never followed.', sel: 'a.chakra-form__helper-text' }, { noScroll: true });
  await S('login-signup', q('a.chakra-button, a').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup link (login)', desc: 'The "Sign up" action beside the form; measured, never followed.', sel: 'login Sign up' }, { noScroll: true });
  await S('social-btn', q('button[aria-label="google"], button[aria-label="facebook"], button[aria-label="apple"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social login button', desc: 'A Google/Facebook/Apple round social sign-in button; measured, never followed.', sel: 'button[aria-label=google]' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 9000 }))) return;
  await sheetsFor('signup');
  const g = G.login;
  await S('signup-field', q('input.chakra-input, input[type="email"], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Signup field', desc: 'A signup form input; focused and typed into then cleared — never submitted.', sel: 'signup input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('signup-cta', q('button.chakra-button, a.chakra-button').filter({ hasText: /sign up|create|continue/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup action', desc: "The signup form's submit action; its states were measured but it was never clicked — nothing was submitted.", sel: 'signup submit' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/en/artist/27' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('header, [class*="header" i], [class*="topbar" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone top bar: purple heart + DEEZER wordmark, Sign-up pill, hamburger.', sel: 'mobile header' }, { noScroll: true });
  await S('m-signup', q('header a, header button, [class*="header" i] a, [class*="header" i] button, a, button').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile Sign up', desc: 'The purple Sign-up pill in the phone top bar; measured never followed.', sel: 'mobile Sign up' }, { noScroll: true });
  const ham = q('.burger-menu').filter({ visible: true }).first();
  await S('m-hamburger', ham, [...B4, 'opened'], { group: g, title: 'Mobile hamburger', desc: 'The burger icon that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.', sel: '.burger-menu' }, { noScroll: true, allowLink: true });
  await S('m-drawer', q('ul.burger-menu-content').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile drawer', desc: 'The nav overlay opened by the burger toggle; its links were never followed.', sel: 'ul.burger-menu-content' }, { open: openBurgerMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-name', q('h1, h2').filter({ hasText: /Daft Punk/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile artist name', desc: 'The artist name over the phone hero image.', sel: 'mobile h1' });
  await S('m-signup-card', q('div, section, aside').filter({ hasText: /start listening on deezer|sign up to listen/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Mobile signup card', desc: 'The "Start listening on Deezer / Sign up to listen to this artist" card — the signed-out gate for playback.', sel: 'mobile signup card' });
  await S('m-track-row', q('div.stack-sm-horizontal').filter({ hasText: /Instant Crush|Get Lucky/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile track row', desc: 'A track row in the phone list (thumb, title, artists, duration).', sel: 'div.stack-sm-horizontal' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the home hero paints light, the offers/features/download marketing pages, the signed-out catalog app, the account forms and the mobile surface all paint dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, offers, artist, album, login, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the Mix button's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('artist')) await reducedMotion('artist', 'button[aria-label="Mix"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
