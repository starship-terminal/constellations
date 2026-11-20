// Measures dropbox.com's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home plans business features sign login register mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// dropbox.com's marketing pages are server-rendered "warp" pages on the
// dwg-component library — real BEM classes (nav.dwg-nav, a.dwg-button2--
// button-style-primary, .dwg-theme--graphite sections) plus hashed CSS-module
// classes — so specs select by role, aria-label, text, the stable dwg-*
// classes or structure. The product sits behind /login and /register; those
// pages' cards and fields are public surfaces and are measured as such —
// the email field is focused and given sample text that is deleted again,
// and the Continue/Get started actions are never pressed. Nothing is sent,
// bought or signed into: the only presses are local UI toggles — the
// Products nav mega-menu, the /plans billing radio and the mobile hamburger.
// The privacy consent banner and Google One Tap are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, blockConsent, unlockScroll, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', plans: '/plans', business: '/business', features: '/features', sign: '/sign', login: '/login', register: '/register' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
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
  await blockConsent(page);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  await unlockScroll(page);
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
    log('  !', key, state, String(e.message || e).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message || e).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  // A briefly unmounted element gets up to 6s to come back before declaring a
  // miss (sections hydrate lazily as the page scrolls them in).
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
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
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          // Close it again after the reading: a menu left open holds focus, so every later
          // focus-visible on the page records 'focus failed'. Escape closes a menu; an
          // accordion still reporting aria-expanded=true is toggled back.
          undo = async () => {
            await page.keyboard.press('Escape'); await page.waitForTimeout(300);
            const l = loc.filter({ visible: true }).first();
            if ((await l.getAttribute('aria-expanded').catch(() => null)) === 'true') { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(600); }
          };
        }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message || e).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|buy now|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|try for free|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|contact sales|get basic|contact us)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: cards and comparison
// rows hydrate lazily, so a cold page only has the heading region in the DOM
// when the run reaches it.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
}

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

// The Products nav item opens the mega-menu panel on hover (a click toggles
// it closed again — measured behaviour: hover sets aria-expanded and the
// 480px dwg-nav-dropdown fades in).
async function openFlyout() {
  const t = q('nav.dwg-nav button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  const box = await t.boundingBox();
  if (box) await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
  else await t.hover({ timeout: 5000 });
  await page.waitForTimeout(1200);
  return page.evaluate(() => {
    const dd = [...document.querySelectorAll('nav .dwg-nav-item__dropdown')].some((e) => getComputedStyle(e).visibility === 'visible' && getComputedStyle(e).opacity === '1');
    return dd;
  }).catch(() => false);
}

// Marks the smallest visible ancestor of a plan CTA that holds a plan name
// and a price — one pricing card, not the comparison grid around it.
async function markPlanCard() {
  await page.evaluate(() => {
    const cta = [...document.querySelectorAll('button, a')].find((b) => /Try for free|Buy now|Get started/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0 && !b.closest('nav'));
    if (!cta) return;
    let n = cta;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/\$\d|\d+\s*\/\s*(month|year|mo)|per (month|year)|\/month/i.test(t) && t.length < 2200 && r.width < 640 && r.height > 200) {
        n.setAttribute('data-m-mark', 'plancard');
        return;
      }
    }
  });
}

// Marks the opened Products mega-menu panel: the visible .dwg-nav-dropdown
// holding the product links (the dwg-nav-item__dropdown wrappers are
// zero-height anchors; the panel is the absolute-positioned dropdown child).
async function markFlyout() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('nav .dwg-nav-item__dropdown, nav [class*="dwg-nav-dropdown--"]')].filter((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return cs.visibility === 'visible' && cs.opacity !== '0' && r.height > 150 && r.width > 300;
    }).sort((a, b) => (b.getBoundingClientRect().height * b.getBoundingClientRect().width) - (a.getBoundingClientRect().height * a.getBoundingClientRect().width));
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'flyout');
  });
}

// Marks the opened mobile navigation panel: the .dwg-nav-mobile-dropdown
// layer (its _backdrop sibling is the dim; the panel holds the nav items and
// the auth actions).
async function markMobileMenu() {
  await page.evaluate(() => {
    // The opened mobile menu is .dwg-nav-mobile-dropdown (its __backdrop
    // sibling is the dim); fall back to the nav itself if the menu is painted
    // inside it.
    const cand = [...document.querySelectorAll('[class*="dwg-nav-mobile-dropdown"]:not([class*="backdrop"]), nav.dwg-nav')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return r.height > 200 && r.height < innerHeight * 1.5 && /Products|Solutions|Business|Pricing/.test(t);
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks the smallest visible ancestor of the first SSO button that holds the
// whole auth card (the SSO actions + the email form + the terms line).
async function markAuthCard() {
  await page.evaluate(() => {
    const g = [...document.querySelectorAll('button, a')].find((b) => /Continue with (Apple|Google|Microsoft)/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0);
    if (!g) return;
    let n = g;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Continue with (Apple|Google|Microsoft)/i.test(t) && /Continue/i.test(t) && t.length < 3000 && r.height > 250 && r.width < 800 && r.width > 260) {
        n.setAttribute('data-m-mark', 'authcard');
        return;
      }
    }
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', plans: 'Plans and pricing',
  features: 'Features and products', login: 'Login and signup', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('nav.dwg-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky dwg-nav bar (dwg-theme--coconut, z 120): the Dropbox mark, the Products / Solutions flyout triggers, the Business / Pricing / Contact sales links, the Get app trigger and Sign up / Log in / Get started.', sel: 'nav.dwg-nav' }, { noScroll: true });
  await S('logo', q('nav.dwg-nav a.dwg-nav-logo-button, nav.dwg-nav a[class*="logo"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Dropbox mark anchor in the nav.', sel: 'nav a.dwg-nav-logo-button' }, { noScroll: true });
  await S('nav-trigger', q('nav.dwg-nav button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Products button that opens the mega-menu; toggled, never followed.', sel: 'nav button Products' }, { noScroll: true });
  await S('nav-link', q('nav.dwg-nav a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The Pricing link in the nav; measured, never followed.', sel: 'nav a Pricing' }, { noScroll: true });
  await S('nav-contact', q('nav.dwg-nav a').filter({ hasText: /Contact sales/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav contact link', desc: 'The Contact sales link in the nav; measured, never followed.', sel: 'nav a Contact sales' }, { noScroll: true });
  await S('nav-signup', q('nav.dwg-nav a').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The header Sign up link; measured, never followed.', sel: 'nav a Sign up' }, { noScroll: true });
  await S('nav-login', q('nav.dwg-nav a').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The header Log in link; measured, never followed.', sel: 'nav a Log in' }, { noScroll: true });
  await S('nav-cta', q('nav.dwg-nav a').filter({ hasText: /^\s*Get started\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Get-started action', desc: 'The header Get started action (the blue pill); measured, never followed.', sel: 'nav a Get started' }, { noScroll: true });
  try { await openFlyout(); } catch (e) { log('  ! flyout open failed', String(e.message || e).split('\n')[0]); }
  await markFlyout();
  await S('nav-dropdown', q('[data-m-mark="flyout"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav mega-menu', desc: 'The Products mega-menu panel (Dropbox / Replay / Sign / Reclaim.ai / Dash / DocSend / Early access), opened by its own trigger.', sel: 'opened Products panel' }, { noScroll: true, noReset: true });
  // The panel closes when the pointer leaves; re-hover Products before every
  // flyout-child state so hover/focus land on a live element.
  const ensureFlyout = async () => {
    for (let i = 0; i < 4; i++) {
      await openFlyout();
      await markFlyout();
      if (await q('[data-m-mark="flyout"] a').filter({ visible: true }).first().count()) return;
      await page.waitForTimeout(700);
    }
  };
  // The mega-menu is pointer-driven: it opens on hover and closes when
  // keyboard focus moves, so a menu link's rest and hover states are what the
  // menu really paints (focus-visible/pressed are not reachable while it is
  // held open — a documented state gap).
  await S('menu-link', q('[data-m-mark="flyout"] a, [data-m-mark="flyout"] [role="link"]').filter({ hasText: /Replay|DocSend|Sign|Dash/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mega-menu link', desc: 'A product link inside the opened Products mega-menu (pointer-driven; the menu closes on keyboard focus).', sel: 'flyout link' }, { noScroll: true, noReset: true, open: ensureFlyout, before: { default: ensureFlyout, hover: ensureFlyout } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "One place to store, share, and collaborate" display heading.', sel: 'h1' });
  await S('hero-sub', await domFind(page, /brings your files and AI tools together|keeps your workflow moving/i, { sel: 'p, span, div, h2', tag: 'herosub' }), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline.', sel: 'hero lede' });
  await S('hero-cta', q('a, button').filter({ hasText: /^\s*Try Dropbox free\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Try Dropbox free" primary action on the hero; measured, never followed.', sel: 'hero primary CTA' });
  await S('transparent-btn', q('a.dwg-button2--button-style-transparent, button.dwg-button2--button-style-transparent').filter({ visible: true }).first(), B4, { group: h, title: 'Transparent button', desc: 'A dwg-button2 transparent-variant action (See all integrations / Connect now / Learn more); measured, never followed.', sel: 'a.dwg-button2--button-style-transparent' });
  await S('text-link', q('a.dwg-text-link').filter({ visible: true }).first(), B4, { group: h, title: 'Text link', desc: 'A dwg-text-link inline link (the AI-integration names); measured, never followed.', sel: 'a.dwg-text-link' });
  await S('icon-button', q('button.dwg-icon-button').filter({ visible: true }).first(), B4, { group: h, title: 'Icon button', desc: 'A dwg-icon-button glyph action on the page (a carousel arrow).', sel: 'button.dwg-icon-button' });
  await S('section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section heading below the hero.', sel: 'section h2' });
  await S('graphite-band', q('section[class*="dwg-theme--graphite"], div[class*="dwg-theme--graphite"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Graphite band', desc: 'A dark dwg-theme--graphite section painted inside the light page.', sel: '.dwg-theme--graphite section' });
  await S('coconut-band', q('section[class*="dwg-theme--coconut"], div[class*="dwg-theme--coconut"]').filter({ visible: true }).last(), ['default'], { group: h, title: 'Coconut band', desc: 'A cream dwg-theme--coconut section.', sel: '.dwg-theme--coconut section' });
  save();
}

async function plans() {
  if (!(await newPage('plans', { wait: 10000 }))) return;
  await sheetsFor('plans');
  await chrome('plans');
  await lazyLoad();
  const g = G.plans;
  await S('plans-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plans title', desc: 'The plans-page heading (the markup carries no h1; the first heading element is read).', sel: 'first h1/h2 on /plans' }, { noScroll: true });
  await S('billing-radio', q('label').filter({ hasText: /monthly|yearly|annual/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing radio', desc: 'A Monthly/Yearly billing-period radio label (the input is a real radio — dwg-input-radio__input); the Yearly side was toggled for the screenshot, never checked out.', sel: 'billing radio label' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (plan name, price and its action).', sel: 'plan card' });
  await S('plan-name', await domFind(page, /^\s*(Plus|Essentials|Professional|Business|Business Plus|Enterprise|Basic)\s*$/i, { sel: 'h2, h3, h4, p, span, div', tag: 'planname' }), ['default'], { group: g, title: 'Plan name', desc: "A plan card's plan name.", sel: 'plan name text' });
  await S('plan-price', await domFind(page, /\$\s*\d+(\.\d+)?/, { sel: 'span, div, p', tag: 'price' }), ['default'], { group: g, title: 'Plan price', desc: "A plan card's price figure (US$ in the region the capture was served).", sel: 'plan $ figure' });
  await S('plan-cta', q('[data-m-mark="plancard"] button, [data-m-mark="plancard"] a').filter({ hasText: /Try for free|Buy now|Get started/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: "A plan card's primary action (Try for free / Buy now); measured, never followed.", sel: 'plan card primary CTA' });
  await S('plan-cta-alt', q('button.dwg-button2--button-style-transparent, a.dwg-button2--button-style-transparent').filter({ hasText: /or buy now/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan secondary CTA', desc: 'The "or buy now" transparent action under a plan CTA; measured, never followed.', sel: 'plan transparent CTA' });
  await S('plan-outline', q('a.dwg-button2--button-style-outline, button.dwg-button2--button-style-outline').filter({ visible: true }).first(), B4, { group: g, title: 'Outline button', desc: 'A dwg-button2 outline-variant action (Get Basic / Contact us); measured, never followed.', sel: 'dwg-button2--button-style-outline' });
  await S('diff-toggle', q('button').filter({ hasText: /Show only differences/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Difference toggle', desc: 'The "Show only differences" comparison-table toggle; measured, never toggled.', sel: 'cf-diff-toggle' });
  await S('help-choose', q('button').filter({ hasText: /Help me choose/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Help-me-choose', desc: 'The "? Help me choose" assistant trigger; measured, never pressed.', sel: 'cf-help-choose-trigger' });
  save();
}

async function business() {
  if (!(await newPage('business', { wait: 9000 }))) return;
  await sheetsFor('business');
  const g = G.features;
  await S('biz-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Business headline', desc: 'The /business display heading ("Everything your business needs to work efficiently, all in one place").', sel: 'h1 on /business' });
  await S('biz-cta', q('a.dwg-button2--button-style-primary, button.dwg-button2--button-style-primary').filter({ visible: true }).first(), B4, { group: g, title: 'Business CTA', desc: 'A primary dwg-button2 action on /business; measured, never followed.', sel: 'dwg-button2--button-style-primary' });
  await S('navy-band', q('section[class*="dwg-theme--navy"], div[class*="dwg-theme--navy"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Navy band', desc: 'A dwg-theme--navy coloured section.', sel: '.dwg-theme--navy section' });
  save();
}

async function features() {
  if (!(await newPage('features', { wait: 9000 }))) return;
  const g = G.features;
  await S('feat-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Features headline', desc: 'The /features display heading ("What is Dropbox?").', sel: 'h1 on /features' });
  await S('feat-card', q('a[class*="dwg-nav-card"], [class*="dwg-card"]').filter({ visible: true }).first(), B4, { group: g, title: 'Feature card', desc: 'A dwg-card / dwg-nav-card feature tile on /features; the link was measured, never followed.', sel: 'dwg-card/dwg-nav-card tile' });
  save();
}

async function sign() {
  if (!(await newPage('sign', { wait: 9000 }))) return;
  const g = G.features;
  await S('sign-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign headline', desc: 'The /sign product-page heading ("Sign paperwork without all the paperwork").', sel: 'h1 on /sign' });
  await S('sign-cta', q('a.dwg-button2--button-style-primary, button.dwg-button2--button-style-primary').filter({ visible: true }).first(), B4, { group: g, title: 'Sign CTA', desc: 'A primary dwg-button2 action on /sign; measured, never followed.', sel: 'dwg-button2--button-style-primary' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  const g = G.login;
  await markAuthCard();
  await S('auth-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Auth card', desc: 'The log-in card (Continue with Apple / Google / Microsoft + the email field and terms); captured, never used.', sel: 'auth card' }, { noScroll: true });
  await S('sso-button', q('button, a').filter({ hasText: /Continue with Apple/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button', desc: 'The "Continue with Apple" SSO action; measured, never pressed — it would leave for the provider flow.', sel: 'Continue with Apple' }, { noScroll: true });
  await S('sso-button-alt', q('button, a').filter({ hasText: /Continue with (Google|Microsoft)/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button (alt)', desc: 'A second SSO action (Google or Microsoft); measured, never pressed.', sel: 'Continue with Google/Microsoft' }, { noScroll: true });
  await S('email-field', q('input[type="email"], input[name*="email" i], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input on the auth card; focused and given sample text that was deleted again — nothing sent.', sel: 'input[type=email]' }, { noScroll: true });
  await S('continue-button', q('button').filter({ hasText: /^\s*Continue\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: "The auth card's Continue action; measured, never pressed.", sel: 'form Continue' }, { noScroll: true });
  save();
}

async function register() {
  if (!(await newPage('register', { wait: 9000 }))) return;
  const g = G.login;
  await markAuthCard();
  await S('register-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Register card', desc: 'The "Get started with Dropbox" sign-up card; captured, never used.', sel: 'register card' }, { noScroll: true });
  await S('register-email', q('input[type="email"], input[name="susi_email"], input[name*="email" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Register email field', desc: 'The name@company.com email input on the sign-up card; focused and given sample text that was deleted again — nothing sent.', sel: 'input[name=susi_email]' }, { noScroll: true });
  await S('register-cta', q('button, a').filter({ hasText: /^\s*Continue\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Register CTA', desc: "The sign-up card's Continue action; measured, never pressed.", sel: 'register Continue' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: the product/company link columns, app links, the language and legal links.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /Help center|Plans|Desktop app|Cookie policy/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  // href*="x.com" matched dropbox.com links ("Dropbox Sign"): match the x.com host only.
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="facebook"], footer a[href^="https://x.com"], footer a[href^="https://twitter.com"], footer a[href*="linkedin"], footer a[href*="youtube"], footer a[aria-label*="Instagram" i], footer a[aria-label*="Facebook" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('nav.dwg-nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'nav at 390' }, { noScroll: true });
  const menu = q('nav.dwg-nav button[class*="hamburger"], nav.dwg-nav button[aria-label*="menu" i], nav.dwg-nav button[aria-label*="navigation" i]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The hamburger toggle in the mobile nav.', sel: 'dwg-nav hamburger button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message || e).split('\n')[0]); }
  await markMobileMenu();
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile navigation panel (the overlay holding the menu items and the auth actions).', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button, [data-m-mark="mmenu"] [role="link"], [data-m-mark="mmenu"] [role="button"]').filter({ hasText: /^\s*(Products|Solutions|Business|Pricing|Get app)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A row inside the opened mobile menu (Products / Solutions / Business / Pricing / Get app).', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-signup', q('nav.dwg-nav a, nav.dwg-nav button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign-up', desc: 'The Sign up action in the mobile top bar, visible above the opened menu; measured, never followed.', sel: 'mobile Sign up' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints the dig-Theme-vis2023--bright scope on dig-Mode--bright — coconut/white sections with dark dwg-theme--graphite bands inside the light pages';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, plans, business, features, sign, login, register, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav.dwg-nav button');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
