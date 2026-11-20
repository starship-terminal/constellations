// Measures fourmula.ai's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home home-dark privacy start auth create-pdp mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fourmula.ai is a Webflow marketing site with a real two-theme switcher: the
// header pill's data-theme-toggle writes localStorage "isDarkMode" and toggles
// the `dark` class on <body>, but the names are inverted — `.body.dark` paints
// the LIGHT surface (white --mainbg) and plain `.body` paints the DARK one
// (#020108 --mainbg). A first visit stores isDarkMode=true, so the site opens
// light; the `home` page here is measured in that default paint and the
// `home-dark` page re-measures the same chrome under the site's own dark paint
// (driven through the isDarkMode key, the same write the toggle makes — never
// by editing CSS). app.fourmula.ai is a separate dark-only Next.js + Tailwind
// v4 app (sfProFont, --color-base-* ramp, --color-accent-500 orange) that
// shares no token layer with the Webflow site; its values are measured from
// the live DOM, never read from the marketing harvest. Specs select by role,
// aria-label, attribute or text. Nothing is sent, bought or signed into: the
// only presses are local UI toggles — the header "Menu" pill, the FAQ
// accordion rows, the app's "Open main menu", the "What's a PDP" and
// "Recommendations" dialog triggers, the password visibility eye and the auth
// card's Sign up switcher. "Forgot password?" is a validating submit, not a
// switch, so the reset view is recorded as uncaptured; the sign-in fields are typed
// into and cleared, never submitted; Get started, Create asset, Sign in,
// Start generation, Upload Main Image, Check connection and every submit
// button are measured, never followed or pressed. The finsweet
// cookie-consent modal (.cookies / fs-cc_*) shows on every first load: it is
// measured, then hidden — Accept all / Settings / Save changes are never
// pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, START_URL, AUTH_URL, PDP_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE, themeInit } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', 'home-dark': '/', privacy: '/privacy-policy', start: START_URL, auth: AUTH_URL, 'create-pdp': PDP_URL, mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, theme = null } = {}) {
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
  if (theme) await ctx.addInitScript(themeInit, theme);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', theme ? `(${theme} paint)` : '');
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message).slice(0, 200) };
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
  if (opts.open) {
    await reset();
    try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); }
    // The open step must produce the view the states are named for: a
    // switcher that submits or a target that never appears would otherwise
    // be measured and published under the wrong view's name.
    if (opts.openCheck && !(await opts.openCheck())) {
      const why = opts.openCheckWhy || 'the expected view did not appear after the open step';
      log('  ! open check failed', key, '-', why);
      for (const st of list) out.components[key].states[st] = { error: `open check failed: ${why}` };
      for (const st of list) if (opts.after?.[st]) await opts.after[st](target).catch(() => {});
      return;
    }
  }
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
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle, then left selected'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|generate|generate.*|sign up|connect|upload.*|cancel|close|back|start generation|check connection|create asset|create pdp|save changes|accept all|add your product)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

// Tags the closest ancestor of loc that paints a rounded card (an opaque fill
// and radius) and returns a locator for it — how the sign-in card on
// app.fourmula.ai/auth is found, since the Tailwind app gives it no semantic
// hook beyond a background + radius.
async function paintedCard(loc, { minR = 10, maxW = 900 } = {}) {
  const ok = await loc.filter({ visible: true }).first().evaluate((el, { minR, maxW }) => {
    document.querySelectorAll('[data-m-card]').forEach((n) => n.removeAttribute('data-m-card'));
    for (let n = el; n && n !== document.body; n = n.parentElement) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && parseFloat(cs.borderTopLeftRadius) >= minR && r.width > 200 && r.width <= maxW && r.height > 100) {
        n.setAttribute('data-m-card', '1');
        return true;
      }
    }
    return false;
  }, { minR, maxW }).catch(() => false);
  return ok ? page.locator('[data-m-card="1"]') : page.locator('[data-m-card="__none__"]');
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
  shell: 'Site chrome', menu: 'Nav overlay', home: 'Home', faq: 'FAQ accordion',
  cookies: 'Cookie consent', footer: 'Footer', legal: 'Legal pages',
  apphdr: 'App chrome', start: 'App start', auth: 'App sign-in',
  pdp: 'Create-PDP generator', mobile: 'Mobile (390 wide)',
};

// The header's centre pill: the "Menu" text half toggles the fixed .menu nav
// overlay — a local UI toggle; the overlay's links are never followed.
const MENUBTN = '.header__menu';
async function openMenu() {
  const isOpen = () => page.evaluate(() => {
    const el = document.querySelector('.menu');
    if (!el) return false;
    const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    return (r.height > 200 || el.className.includes('open') || el.className.includes('active')) && cs.visibility !== 'hidden' && cs.opacity !== '0';
  }).catch(() => false);
  const btn = page.locator(MENUBTN).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no menu trigger';
  if (await isOpen()) return 'the nav overlay was already open';
  for (let i = 0; i < 3; i++) {
    await toggle(btn, { allowLink: true }).catch(() => btn.evaluate((el) => el.click()));
    await page.waitForTimeout(1200);
    if (await isOpen()) return 'clicked the "Menu" pill to open the nav overlay';
  }
  return 'activated the "Menu" pill; the overlay did not report open';
}
async function closeMenu() {
  await page.keyboard.press('Escape').catch(() => {});
  await page.locator(MENUBTN).filter({ visible: true }).first().click({ timeout: 2000 }).catch(() => {});
  await page.waitForTimeout(500);
}

// The finsweet cookie-consent layer (.cookies) mounts on every first load as
// a full-screen modal. It is measured, then hidden — its Accept all / Save
// changes controls are never pressed. The "Settings" button opens the
// preference manager in place (a local UI toggle that accepts nothing), so it
// is clicked once to reach the manager's controls, which are then measured
// and hidden unanswered.
async function cookieBits() {
  const g = G.cookies;
  await S('cookie-modal', q('.cookies').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cookie consent modal', desc: 'The @finsweet consent modal shown on first load ("By clicking Accept all…"): the banner plus the cookie-preference manager. Measured, then hidden — never answered.', sel: '.cookies' }, { noScroll: true, crop: false });
  await S('cookie-accept', q('.cookies a.btn-primary, .cookies [class*="btn-primary"]').filter({ hasText: /accept all/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Accept all button', desc: 'The filled "Accept all" in the consent modal; measured, never pressed.', sel: '.cookies .btn-primary "Accept all"' }, { noScroll: true });
  await S('cookie-settings', q('.cookies a.btn-outline, .cookies [class*="btn-outline"]').filter({ hasText: /^settings$/i }).filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'Settings button', desc: 'The outline "Settings" that opens the cookie-preference manager in place — a local UI toggle accepting nothing; the opened state was measured after clicking it, and the manager was left open to measure its controls.', sel: '.cookies .btn-outline "Settings"' }, { noScroll: true, allowLink: true });
  // The manager is now open behind the banner; its Save changes and the
  // category checkboxes are measurable. Nothing is toggled or saved.
  await S('cookie-save', q('.cookies a.btn-outline, .cookies [class*="btn-outline"]').filter({ hasText: /save changes/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Save changes button', desc: 'The outline "Save changes" inside the opened preference manager; measured, never pressed.', sel: '.cookies .btn-outline "Save changes"' }, { noScroll: true });
  await S('cookie-check', q('.cookies .fs-cc_checkbox, .cookies [class*="checkbox"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Consent checkbox row', desc: 'A category checkbox row in the opened preference manager (Strictly necessary is forced active); measured, never toggled.', sel: '.cookies .fs-cc_checkbox row' }, { noScroll: true });
}

// The shell measured under the site's own dark paint: same components,
// re-read with isDarkMode=false so plain .body paints #020108.
async function shellDark() {
  const g = G.shell;
  await S('mkt-header-dark', q('.header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header (dark paint)', desc: 'The 91px header under the site\'s dark paint (plain .body, isDarkMode=false): the Menu pill, the theme toggle, the scroll-percentage counter, the account icon-link and the Get started pill.', sel: '.header @ dark paint' }, { noScroll: true });
  await S('menu-pill-dark', q(MENUBTN).filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu pill (dark paint)', desc: 'The header\'s centre "Menu" pill under the dark paint.', sel: '.header__menu @ dark paint' }, { noScroll: true });
  await S('header-cta-dark', q('a.btn-primary.is-header-btn').filter({ visible: true }).first(), ['default'], { group: g, title: 'Get started button (dark paint)', desc: 'The header\'s primary "Get started" pill under the dark paint; measured, never followed.', sel: 'a.btn-primary.is-header-btn @ dark paint' }, { noScroll: true });
  await S('hero-h1-dark', q('.hero__title').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Hero headline (dark paint)', desc: '"Your catalog, instantly re-shot." under the dark paint — the second line picks up --fonts-50.', sel: '.hero__title @ dark paint' }, { noScroll: true });
  await S('step-cta-dark', q('a.btn-primary-stb').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Step CTA (dark paint)', desc: 'A "Get started" button in the four-steps section under the dark paint; measured, never followed.', sel: 'a.btn-primary-stb @ dark paint' });
  await S('faq-item-dark', q('.faq__item').filter({ visible: true }).first(), ['default'], { group: G.faq, title: 'FAQ row (dark paint)', desc: 'A closed FAQ accordion row under the dark paint.', sel: '.faq__item @ dark paint' });
  await S('footer-dark', q('.footer').filter({ visible: true }).first(), ['default'], { group: G.footer, title: 'Footer (dark paint)', desc: 'The page footer under the dark paint.', sel: '.footer @ dark paint' }, { noScroll: true });
}

async function home() {
  // promo: 'show' keeps the first-load consent modal up long enough to
  // measure it; it is hidden before any other component is read.
  if (!(await newPage('home', { promo: 'show', wait: 9000 }))) return;
  await cookieBits();
  await closePromo(page);
  await sheetsFor('home');
  await chrome('home');
  let g = G.shell;
  await S('mkt-header', q('.header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The 91px header: the logo-and-wordmark, the centre Menu pill with the theme toggle and scroll-percentage counter, the Fourmula-app account icon-link and the Get started pill.', sel: '.header' }, { noScroll: true });
  await S('mkt-logo', q('.header__left').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The header\'s fourmula.ai logo-and-wordmark.', sel: '.header__left' }, { noScroll: true });
  await S('menu-pill', q(MENUBTN).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Menu pill', desc: 'The header\'s centre "Menu" pill (lines icon + label) — a local UI toggle that opens the fixed .menu overlay; the opened state was measured after clicking it, then closed.', sel: '.header__menu' }, { noScroll: true, allowLink: true, after: { opened: closeMenu } });
  await S('theme-toggle', q('[data-theme-toggle]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Theme toggle', desc: 'The sun/moon half of the header pill — writes localStorage isDarkMode and flips body.dark (note .body.dark paints the LIGHT surface). Never pressed here; both paints are captured as separate pages instead.', sel: '[data-theme-toggle]' }, { noScroll: true });
  await S('prc-counter', q('.header__prc').filter({ visible: true }).first(), ['default'], { group: g, title: 'Scroll-percentage counter', desc: 'The "0%" readout inside the header pill that counts down scroll progress through the page.', sel: '.header__prc' }, { noScroll: true });
  await S('account-link', q('a.header_signin.is-header-btn').filter({ visible: true }).first(), B4, { group: g, title: 'App account link', desc: 'The icon-only "Fourmula app account" link to app.fourmula.ai/auth; measured, never followed.', sel: 'a.header_signin.is-header-btn' }, { noScroll: true });
  await S('header-cta', q('a.btn-primary.is-header-btn').filter({ visible: true }).first(), B4, { group: g, title: 'Get started button', desc: 'The primary "Get started" pill in the header linking to app.fourmula.ai/start; measured, never followed.', sel: 'a.btn-primary.is-header-btn' }, { noScroll: true });
  g = G.menu;
  await S('nav-overlay', q('.menu').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Nav overlay', desc: 'The fixed .menu overlay opened by the Menu pill: PDP\'s / Products / Videos / Our features anchors, Privacy/Terms/Cookie links, Instagram and the app account link. Its links were never followed.', sel: '.menu (opened)' }, { open: openMenu, noToggle: true, noScroll: true, noReset: true, after: { opened: closeMenu } });
  await S('nav-overlay-link', q('.menu a[href^="#"], .menu .menu__link').filter({ hasText: /PDP/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Nav overlay link', desc: 'An anchor link inside the opened .menu overlay ("PDP\'s"); measured, never followed.', sel: '.menu .menu__link "PDP\'s"' }, { open: openMenu, noScroll: true, noReset: true, after: { hover: closeMenu } });
  g = G.home;
  await S('hero-h1', q('.hero__title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline', desc: '"Your catalog, instantly re-shot." — the display h1; the second line paints --fonts-50 (u-fonts-50).', sel: '.hero__title' }, { noScroll: true });
  await S('hero-word', q('.hero__slider__item').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero keyword chip', desc: 'A chip in the hero\'s right-edge rotating word column (PDPs / UGC / Lifestyle shots / Ads / Stories / Street style).', sel: '.hero__slider__item' }, { noScroll: true });
  await S('hero-scroll', q('.hero__scroll').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Scroll-down cue', desc: 'The "SCROLL DOWN" micro-label at the hero\'s bottom right, an in-page anchor to #what-is-fourmula; measured, never followed.', sel: '.hero__scroll' }, { noScroll: true });
  await S('section-h2', q('.what__title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section heading', desc: '"On-brand visuals. Made by AI." — the u-h2 section heading style.', sel: '.what__title' });
  await S('ai-btn', q('a.ai__btn').filter({ visible: true }).first(), B4, { group: g, title: 'Round app link', desc: 'The 53px round icon-link ("fourmula.ai") into app.fourmula.ai/start, repeated beside the AI feature copy; measured, never followed.', sel: 'a.ai__btn' });
  await S('how-cta', q('a.btn-primary.is-how').filter({ visible: true }).first(), B4, { group: g, title: 'How-it-works CTA', desc: 'The "Get started" pill in the How It Works section; measured, never followed.', sel: 'a.btn-primary.is-how' });
  await S('step-h3', q('.list__main__h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Step heading', desc: 'A u-h2-5 step heading in the "From idea to assets in four steps" section.', sel: '.list__main__h2' });
  await S('step-cta', q('a.btn-primary-stb').filter({ visible: true }).first(), B4, { group: g, title: 'Step CTA', desc: 'The "Get started" button repeated beside each of the four steps, linking to app.fourmula.ai/start; measured, never followed.', sel: 'a.btn-primary-stb' });
  g = G.faq;
  await S('faq-item', q('.faq__item').filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'FAQ row', desc: 'A FAQ accordion row ("What can AI FOURMULA create for my brand?") — a local UI toggle whose + icon flips and the answer expands; the opened state was measured after clicking, then re-closed by toggling again.', sel: '.faq__item' }, { after: { opened: async () => { await q('.faq__item').filter({ visible: true }).first().click({ timeout: 3000 }).catch(() => {}); await page.waitForTimeout(600); } } });
  g = G.footer;
  await S('footer', q('.footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The 811px page footer: the fourmula.ai mark, section anchors (PDP\'s / Videos / Products / Our features), legal links, Instagram.', sel: '.footer' }, { noScroll: true });
  await S('footer-link', q('.footer__main__link-small').filter({ hasText: /privacy policy/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'The "Privacy Policy" footer link; measured, never followed.', sel: '.footer__main__link-small "Privacy Policy"' }, { noScroll: true });
  save();
}

async function homeDark() {
  if (!(await newPage('home-dark', { theme: 'dark', wait: 9000 }))) return;
  await chrome('home-dark');
  await shellDark();
  save();
}

async function privacy() {
  if (!(await newPage('privacy'))) return;
  await chrome('privacy');
  const g = G.legal;
  // The legal pages paint a .tech section: an h1 + last-updated line, then
  // long unclassed <p> prose — the same template for /privacy-policy and
  // /terms-of-service.
  await S('legal-section', q('.tech').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal section', desc: 'The .tech section the legal pages paint their prose in.', sel: '.tech' }, { noScroll: true });
  await S('legal-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal page title', desc: '"PRIVACY & COOKIES POLICY" — the legal page heading.', sel: '.tech h1' }, { noScroll: true });
  await S('legal-body', q('.tech p, .page p').filter({ hasText: /.{40,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal body copy', desc: 'A body paragraph in the privacy policy — the legal prose text style.', sel: '.tech p' });
  await S('legal-link', q('.tech a').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Legal inline link', desc: 'A link inside the privacy-policy prose; measured, never followed.', sel: '.tech a' });
  save();
}

// The app chrome every app.fourmula.ai page paints: a fixed rounded-full
// header bar holding the Open-main-menu button, the header Create asset
// submit, and the Sign in button.
async function appChrome(g) {
  await S('app-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'App header', desc: 'The app\'s floating header — a fixed rounded-full bar (1392x56 at 24,24) holding the menu button, the Create asset submit and the Sign in button.', sel: 'header' }, { noScroll: true });
  await S('app-menu-btn', q('button[aria-label="Open main menu"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'App menu button', desc: 'The 32px icon button (aria "Open main menu") in the app header — a local UI toggle that opens the nav drawer; the opened state was measured after clicking it, then the drawer was closed with Escape.', sel: 'button[aria-label="Open main menu"]' }, { noScroll: true, after: { opened: async () => { await page.keyboard.press('Escape'); await page.waitForTimeout(400); } } });
  await S('app-create-btn', q('button').filter({ hasText: /^Create asset$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Create asset button', desc: 'The header\'s "Create asset" submit — its states were measured but it was never pressed (it would start an authenticated action).', sel: 'header "Create asset" button' }, { noScroll: true });
  await S('app-signin-btn', q('button[aria-label="Sign in to your account"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign in button', desc: 'The header\'s "Sign in" button (aria "Sign in to your account"); measured, never pressed.', sel: 'button[aria-label="Sign in to your account"]' }, { noScroll: true });
}

async function start() {
  if (!(await newPage('start', { wait: 12000 }))) return;
  await sheetsFor('start');
  await chrome('start');
  await appChrome(G.apphdr);
  const g = G.start;
  await S('start-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Start headline', desc: '"Create studio-quality product photos" — the signed-out start-page masthead (the page titles itself "Formula AI | Start").', sel: 'start h1' });
  await S('start-cta', q('button').filter({ hasText: /^Create asset$/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Start CTA', desc: 'The large "Create asset" button in the start-page body; its states were measured but it was never pressed.', sel: 'start "Create asset" button' });
  save();
}

async function auth() {
  if (!(await newPage('auth', { wait: 12000 }))) return;
  await sheetsFor('auth');
  await chrome('auth');
  await appChrome(G.apphdr);
  const g = G.auth;
  let card = await paintedCard(q('input[type="email"]').filter({ visible: true }).first());
  await S('auth-card', card, ['default'], { group: g, title: 'Sign-in card', desc: 'The sign-in card over the dark field: "Sign in" heading, Continue with Google, Email + Password fields, Sign in submit, the Forgot password? and Sign up switchers.', sel: 'auth card (painted ancestor of email input)' }, { noScroll: true });
  await S('auth-back', q('button').filter({ hasText: /^Back$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Back button', desc: 'The "Back" button over the auth card; measured, never pressed (it navigates to the start page).', sel: 'auth "Back" button' }, { noScroll: true });
  await S('auth-google', q('button').filter({ hasText: /continue with google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google sign-in', desc: 'The "Continue with Google" button; measured, never pressed — it would start the OAuth flow.', sel: 'auth "Continue with Google"' }, { noScroll: true });
  await S('auth-field-email', q('input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The "Email address" field on the sign-in card; focused and typed into then cleared — never submitted.', sel: 'auth input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('auth-field-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field', desc: 'The "Password" field on the sign-in card; focused and typed into then cleared — never submitted.', sel: 'auth input[type=password]' }, { noScroll: true, fillText: 'not-a-real-password' });
  await S('auth-eye', q('button[aria-label="Toggle password visibility"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Password visibility eye', desc: 'The eye button inside the password field — a local UI toggle; measured at rest, never needed to reveal anything.', sel: 'button[aria-label="Toggle password visibility"]' }, { noScroll: true });
  await S('auth-submit', card.filter({ visible: true }).first().locator('button').filter({ hasText: /^\s*Sign in\s*$/ }).last(), B4, { group: g, title: 'Sign-in submit', desc: 'The card\'s "Sign in" submit; its states were measured but the button was never pressed — nothing was submitted.', sel: 'auth card "Sign in" submit' }, { noScroll: true });
  await S('auth-forgot', q('button').filter({ hasText: /forgot password\??/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Forgot password submit', desc: 'The "Forgot password?" button on the sign-in card — a form action, not a view switch: pressing it validates the email field in place (the card shows "Please enter a valid email address" and stays on sign-in), and completing it submits. Measured at rest, never pressed.', sel: 'auth "Forgot password?"' }, { noScroll: true });
  // The card's "Sign up" switcher flips the card in place to the create-
  // account view — a local UI toggle; the submit inside is never pressed.
  await S('auth-switch', q('button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Sign-up switcher', desc: 'The "Sign up" text button at the card\'s foot that switches it to the create-account view — a local UI switch; measured at rest.', sel: 'auth card "Sign up" switcher' }, { noScroll: true });
  // The "Forgot password?" control is a form action, not a view switch:
  // pressed on the live card it only paints the email validation ("Please
  // enter a valid email address") and the card stays on sign-in — a valid
  // email submits the reset, which this kit never runs. The reset view is
  // uncaptured: it is recorded as such rather than republishing the sign-in
  // card's validation view under the reset view's name.
  const fc = comp('auth-forgot-card', { group: g, title: 'Forgot-password view (uncaptured)', desc: 'The auth card\'s reset view. "Forgot password?" is a form action, not a local UI switch: pressing it validates the email field in place and the card stays on sign-in, while a valid email would submit — so the reset view is uncaptured.', sel: 'auth card @ forgot view' });
  fc.uncaptured = 'the forgot-password control validates and submits rather than switching views; the reset view needs a submission this kit never runs';
  fc.states = { opened: { uncaptured: true, via: 'never pressed — the control submits' } };
  await S('auth-signup-card', card, ['opened'], { group: g, title: 'Create-account view', desc: 'The auth card switched to its create-account view by pressing the "Sign up" switcher; fields were measured, the create submit was never pressed. Returned to the sign-in view afterwards.', sel: 'auth card @ signup view' }, { noScroll: true, noToggle: true, open: async () => { await q('button').filter({ hasText: /^\s*Sign up\s*$/ }).first().click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); card = await paintedCard(q('input').filter({ visible: true }).first()); }, openCheck: async () => { const t = await card.evaluate((el) => (el.innerText || '').split('\n')[0].trim()).catch(() => ''); return t !== '' && !/^sign in$/i.test(t); }, openCheckWhy: 'the card stayed on the sign-in view after the "Sign up" switcher' });
  save();
}

// A dialog opened by an in-page trigger on the create-pdp page; closed again
// afterwards with Escape.
const openDialog = (name) => async () => {
  await q('button').filter({ hasText: new RegExp(name, 'i') }).filter({ visible: true }).first().click({ timeout: 4000 }).catch((e) => { throw e; });
  await page.waitForTimeout(1200);
};
// Dismisses the open dialog without touching any page control: Escape, then
// a click on the backdrop (the headless-ui overlay) if the dialog is still
// up. It deliberately never presses a button — "Cancel and close" would
// leave the generator, and any dialog close control is decoration for this
// purpose.
const closeDialog = async () => {
  for (let i = 0; i < 3; i++) {
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(500);
    const open = await q('[role="dialog"][data-state="open"], [role="dialog"]').filter({ visible: true }).count().catch(() => 0);
    if (!open) return;
    await page.mouse.click(12, 12).catch(() => {});
    await page.waitForTimeout(500);
  }
};

async function createPdp() {
  if (!(await newPage('create-pdp', { wait: 14000 }))) return;
  await sheetsFor('create-pdp');
  await chrome('create-pdp');
  const g = G.pdp;
  await S('app-menu-btn-pdp', q('button[aria-label="Open main menu"]').filter({ visible: true }).first(), [...B4, 'opened'], { group: G.apphdr, title: 'App menu button', desc: 'The 32px icon button (aria "Open main menu") in the app header — a local UI toggle that opens the nav drawer; the opened state was measured after clicking it, then the drawer was closed with Escape.', sel: 'button[aria-label="Open main menu"]' }, { noScroll: true, after: { opened: async () => { await page.keyboard.press('Escape'); await page.waitForTimeout(400); } } });
  await S('pdp-cancel', q('button[aria-label="Cancel and close PDP creation"]').filter({ visible: true }).first(), B4, { group: g, title: 'Cancel button', desc: 'The header\'s "Cancel and close" (aria "Cancel and close PDP creation"); measured, never pressed — it would leave the generator.', sel: 'button[aria-label="Cancel and close PDP creation"]' }, { noScroll: true });
  await S('pdp-start-header', q('button[aria-label="Start PDP generation"]').filter({ visible: true }).first(), B4, { group: g, title: 'Start generation (header)', desc: 'The header\'s compact "Start generation" submit; measured, never pressed — it would queue a generation.', sel: 'header "Start generation" button' }, { noScroll: true });
  await S('pdp-dash-link', q('a[href="/"]').filter({ hasText: /dashboard/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Dashboard link', desc: 'The faded "Dashboard" nav link beside the menu button; measured, never followed (the dashboard needs an account).', sel: 'a[href="/"] "Dashboard"' }, { noScroll: true });
  await S('pdp-visuals-h', q('h2').filter({ hasText: /your visuals/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Your visuals heading', desc: 'The left rail\'s "Your visuals" section heading.', sel: 'create-pdp h2 "Your visuals"' });
  await S('pdp-reco', q('button').filter({ hasText: /^Recommendations$/ }).filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'Recommendations button', desc: 'The small "Recommendations" trigger under Your visuals — a local UI toggle that opens the recommendations dialog; the opened state was measured after clicking it, then the dialog was closed with Escape.', sel: '"Recommendations" button' }, { after: { opened: closeDialog } });
  // The dialog's [role=dialog] wrapper is a zero-height anchor; the painted
  // panel is the rounded-4xl bg-base-750 card inside it.
  const DLG_PANEL = '[role="dialog"] div[class*="rounded-4xl"], [role="dialog"] div[class*="bg-base-7"]';
  await S('pdp-reco-dialog', q(DLG_PANEL).filter({ visible: true }).first(), ['default'], { group: g, title: 'Recommendations dialog', desc: 'The "What can I upload?" dialog opened by the Recommendations trigger — a rounded-4xl bg-base-750 panel over a blurred backdrop; measured, never submitted.', sel: 'recommendations dialog panel' }, { open: openDialog('Recommendations'), noReset: true, after: { default: closeDialog } });
  await S('pdp-upload', q('button').filter({ hasText: /upload main image/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Upload button', desc: 'The "Upload Main Image" button in the Your visuals rail; measured, never pressed (it would open the file picker).', sel: '"Upload Main Image" button' });
  await S('pdp-add-product', q('button').filter({ hasText: /add your product/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Add product button', desc: 'The "Add your product" button under the upload slot; measured, never pressed.', sel: '"Add your product" button' });
  // The Shopify banner mounts twice in the DOM (a hidden copy beside the
  // painted one): domFind picks the painted element.
  await S('pdp-shopify-h', await domFind(page, /connect your shopify store/i, { sel: 'h2', minW: 100, minH: 10 }), ['default'], { group: g, title: 'Shopify banner heading', desc: 'The "Connect your Shopify store" banner heading.', sel: 'create-pdp h2 "Connect your Shopify store" (painted copy)' });
  await S('pdp-shopify-cta', await domFind(page, /check connection/i, { sel: 'a', minW: 50, minH: 10 }), B4, { group: g, title: 'Check connection pill', desc: 'The accent "Check connection" pill linking to /shopify-integration — the only painted accent surface on the signed-out page; measured, never followed.', sel: 'a[href="/shopify-integration"] "Check connection" (painted copy)' });
  await S('pdp-adjust-h', q('h2').filter({ hasText: /adjust look/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Adjust-look heading', desc: 'The "Adjust look" section heading that carries the "What\'s a PDP" trigger.', sel: 'create-pdp h2 "Adjust look"' });
  await S('pdp-what', q('button').filter({ hasText: /what's a pdp/i }).filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'What\'s-a-PDP button', desc: 'The pill-shaped "What\'s a PDP" explainer trigger — a local UI toggle that opens the PDP explainer dialog; the opened state was measured after clicking it, then the dialog was closed with Escape.', sel: '"What\'s a PDP" button' }, { after: { opened: closeDialog } });
  await S('pdp-what-dialog', q(DLG_PANEL).filter({ visible: true }).first(), ['default'], { group: g, title: 'PDP explainer dialog', desc: 'The dialog opened by the "What\'s a PDP" trigger; measured, never submitted.', sel: 'PDP explainer dialog panel' }, { open: openDialog("What's a PDP"), noReset: true, after: { default: closeDialog } });
  await S('pdp-signedin-chip', q('button').filter({ hasText: /^Signed in$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Requirement chip', desc: 'A small "Signed in" status chip in the requirements area; measured, never pressed.', sel: '"Signed in" chip' });
  // The format radiogroup (Static content / Video content) is a local UI
  // toggle — Video content paints disabled at 0.5 opacity signed out; nothing
  // is submitted by selecting a radio.
  await S('pdp-format-group', q('[role="radiogroup"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Format radiogroup', desc: 'The "Static content / Video content" radio pair under Adjust look — a local UI toggle; Video paints disabled signed out.', sel: '[role=radiogroup]' });
  await S('pdp-format-static', q('[role="radio"]').filter({ hasText: /static content/i }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Format radio (Static)', desc: 'The "Static content" radio — the checked default; measured, never changed.', sel: '[role=radio] "Static content"' });
  await S('pdp-format-video', q('[role="radio"]').filter({ hasText: /video content/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Format radio (Video, disabled)', desc: 'The "Video content" radio — painted disabled (data-disabled, 0.5 opacity) for signed-out visitors; measured, never pressed.', sel: '[role=radio] "Video content"' });
  await S('pdp-start-bottom', await domFind(page, /start generation/i, { sel: 'button', minW: 400, minH: 10 }), B4, { group: g, title: 'Start generation (footer)', desc: 'The full-width "Start generation" submit at the foot of the form; measured, never pressed — it would queue a generation.', sel: 'footer "Start generation" button (painted copy)' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', wait: 9000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('.header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone header at 390 wide: logo, the Menu pill with the theme toggle and the Get started pill.', sel: 'mobile .header' }, { noScroll: true });
  await S('m-menu-pill', q(MENUBTN).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile menu pill', desc: 'The "Menu" pill at 390 wide — a local UI toggle that opens the nav overlay; the opened state was measured after clicking it, then closed.', sel: 'mobile .header__menu' }, { noScroll: true, allowLink: true, after: { opened: closeMenu } });
  await S('m-nav-overlay', q('.menu').filter({ visible: true }).first(), ['opened'], { group: g, title: 'Mobile nav overlay', desc: 'The nav overlay opened by the menu pill at 390 wide; its links were never followed.', sel: 'mobile .menu (opened)' }, { open: openMenu, noToggle: true, noScroll: true, noReset: true, after: { opened: closeMenu } });
  await S('m-hero-h1', q('.hero__title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide (u-h1 resolves to the mobile size).', sel: 'mobile .hero__title' });
  await S('m-step-cta', q('a.btn-primary-stb').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile step CTA', desc: 'A "Get started" button in the steps section at 390 wide; measured, never followed.', sel: 'mobile a.btn-primary-stb' });
  await S('m-faq-item', q('.faq__item').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'Mobile FAQ row', desc: 'A FAQ accordion row at 390 wide; the opened state was measured after clicking, then re-closed.', sel: 'mobile .faq__item' }, { after: { opened: async () => { await q('.faq__item').filter({ visible: true }).first().click({ timeout: 3000 }).catch(() => {}); await page.waitForTimeout(600); } } });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the marketing site paints light on first visit (isDarkMode=true → .body.dark) and dark on a plain .body — `home` is the default light paint, `home-dark` the site\'s own dark paint; app.fourmula.ai is a separate dark-only Tailwind app';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, 'home-dark': homeDark, privacy, start, auth, 'create-pdp': createPdp, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the header pill's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a.btn-primary.is-header-btn');
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
