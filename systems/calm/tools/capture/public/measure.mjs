// Measures calm.com's public components in every state reachable without
// signing in, subscribing or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home sleep meditate login mobile health.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// calm.com is a Next.js marketing app (styled-components, styles__*-sc-*
// classes) behind PerimeterX; /app/sleep, /app/meditate and /app/music open a
// dark signed-out preview of the real app shell, and the B2B surface lives on
// the WordPress health.calm.com. Nothing is sent, bought or signed into: the
// only presses are local UI toggles — the Log In button (opens a card, never
// submitted), the Try Calm for Free button (opens a card), the nav dropdown
// triggers, the rail tab pills and the mobile menu. The cookie-consent bar is
// measured as a component, then hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, HEALTH, M, launch, patch, open, closePromo, clearChallenge, domFind, styleOf, crop, centre, RAW, UA, UA_DESKTOP, UA_MOBILE, isChallengeText } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: BASE + '/', sleep: BASE + '/app/sleep', meditate: BASE + '/app/meditate', login: BASE + '/', health: HEALTH + '/' };
let page, cdp, current, context, run;
// One live context per viewport width: a single liveCtx reused across the
// desktop and mobile passes would measure the mobile pages at 1440px.
const liveCtx = {};
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  // isChallengeText lives in Node — evaluate only the DOM reads; a function
  // referenced inside evaluate() does not serialize into the page.
  const s = await page.evaluate(() => ({
    title: document.title,
    body: (document.body && document.body.innerText) || '',
    url: location.href,
  })).catch(() => null);
  if (!s) return true;
  // A chrome-error document means the connection itself was dropped (PX reset
  // rather than a challenge page); it still counts as blocked.
  if (/^chrome-error:\/\//.test(s.url || '')) return true;
  return isChallengeText(s) || s.body.trim().length < 40;
}

// One context per width is shared across routes: PerimeterX clearance is a
// context cookie, so a fresh context restarts the scoring. A route that comes
// back blocked pauses and retries on the same context, then replaces it.
async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  const b = context.browser();
  // A bot check is a boundary: a few tries, then the page is recorded as failed (never a 20-try,
  // hour-long wait for PerimeterX to let the run through).
  for (let attempt = 0; attempt < 3; attempt++) {
    const mode = mobile ? 'mobile' : 'desktop';
    if (!liveCtx[mode]) {
      liveCtx[mode] = await b.newContext(mobile
        ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
        : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
      await patch(liveCtx[mode]);
    }
    page = await liveCtx[mode].newPage();
    cdp = await liveCtx[mode].newCDPSession(page);
    await cdp.send('DOM.enable');
    await cdp.send('CSS.enable');
    page.setDefaultTimeout(8000);
    log('open', key, mobile ? '(mobile)' : '', attempt ? `(attempt ${attempt})` : '');
    await open(page, url || URLS[key], { wait, promo });
    if (!(await blocked())) {
      await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
      return true;
    }
    log('  BLOCKED', key, attempt < 2 ? '- fresh context in 30s' : '- recorded as a boundary');
    await page.close().catch(() => {});
    if (attempt < 2) { await liveCtx[mode].close().catch(() => {}); liveCtx[mode] = null; await new Promise((r) => setTimeout(r, 30000)); }
  }
  failedPages.add(key);
  return false;
}

async function closePage() {
  await page?.close().catch(() => {});
  page = null;
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
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
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

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|sign up today|sign in with.*|try calm for free)$/i;
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
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA_DESKTOP, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  shell: 'Shell and navigation', home: 'Home', app: 'App shell (dark)', login: 'Login and signup',
  health: 'Calm Health (B2B)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// The consent bar: measured as a component BEFORE closePromo hides it for the
// rest of the pass. It is a styled-components Banner bottom sheet.
async function consentBar() {
  const bar = q('div[class*="Banner" i], aside[class*="Banner" i], section[class*="Banner" i]').filter({ hasText: /cookie|privacy/i }).filter({ visible: true }).first();
  await S('cookie-banner', bar, ['default'], { group: G.shell, title: 'Cookie bar', desc: 'The consent bottom sheet ("Cookie Preferences"), measured then hidden and never answered — no consent choice is ever made.', sel: 'div.Banner (cookie text)' }, { noScroll: true });
}

async function home() {
  if (!(await newPage('home', { wait: 12000, promo: 'keep' }))) return;
  await consentBar();
  await closePromo(page);
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The navy-scrim-gradient marketing header over the hero photograph: app-icon logo, the Sleep/Stress & Anxiety/Mindfulness links, Screening, the Calm Health dropdown, Log In and the Try-Calm-for-Free pill.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a[aria-label*="Calm Logo"], header a[href="/"]:has(svg)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The rounded-square app icon anchor (the #60B4E7->#6461E0 gradient tile with the white wordmark inside).', sel: 'header a[aria-label*="Calm Logo"]' }, { noScroll: true });
  await S('nav-link', q('header button').filter({ hasText: /^\s*(Sleep|Mindfulness|Screening)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav item', desc: 'A plain header item (Sleep, Mindfulness or Screening) — a styled-components button that opens a section panel, not an anchor.', sel: 'header button (Sleep)' }, { noScroll: true });
  await S('nav-trigger', q('header button[class*="Trigger" i], header button').filter({ hasText: /^\s*Calm Health\s*/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Calm Health chevron that opens the dropdown panel; toggled, never followed.', sel: 'header button.Trigger (Calm Health)' }, { noScroll: true });
  await S('nav-login', q('button[data-testid="desktopnav-login-button"], header button').filter({ hasText: /^\s*Log ?In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav login', desc: 'The header Log In button; pressing it opens the login card, measured under login-dialog, never submitted.', sel: 'button[data-testid=desktopnav-login-button]' }, { noScroll: true });
  await S('nav-cta', q('header a, header button').filter({ hasText: /Try\s*Calm/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The white Try-Calm-for-Free header pill; pressing it opens the signup flow (the page measured under signup-), never submitted.', sel: 'header a/button (Try Calm)' }, { noScroll: true });
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The navy "Calm your mind. Change your life." headline.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1 + p, main p, h2').filter({ hasText: /#1 app|sleep, meditation/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline.', sel: 'hero lede' });
  await S('hero-cta', q('main a, main button, section a, section button').filter({ hasText: /Try\s*Calm\s*for\s*Free/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The navy hero action; measured never followed.', sel: 'hero Try Calm for Free' });
  await S('learn-more', q('main button, section button, main a, section a').filter({ hasText: /in-the-moment relief|stay asleep|ups and downs/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Section card link', desc: 'A marketing section card (Stress less. / Sleep more. / Live mindfully.) — a button carrying the heading, copy and Learn-more label; measured never followed.', sel: 'section card button' });
  await S('section-h2', q('main h2, section h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading (Stress less. / Sleep more. / Live mindfully.).', sel: 'h2' });
  save();
  await closePage();
}

async function login() {
  if (!(await newPage('login', { wait: 12000 }))) return;
  const g = G.login;
  // The Log In button opens the card in place; it is a local UI toggle, never
  // a submission. Escape dismisses it afterwards.
  try {
    const t = q('button[data-testid="desktopnav-login-button"], header button').filter({ hasText: /^\s*Log ?In\s*$/i }).filter({ visible: true }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1800); }
  } catch (e) { log('  ! login open failed', String(e.message).split('\n')[0]); }
  const dlg = q('[role="dialog"], [class*="Modal" i], [class*="Dialog" i]').filter({ visible: true }).last();
  await S('login-dialog', dlg, ['default'], { group: g, title: 'Login card', desc: 'The white "Log into your account" modal card over a dimmed blur backdrop; opened by its own Log In button, never submitted.', sel: '[role=dialog]' }, { noScroll: true, pad: 24 });
  await S('login-email-btn', q('[role="dialog"] button, [role="dialog"] a').filter({ hasText: /Sign in with Email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in primary', desc: 'The navy Sign-in-with-Email pill inside the login card; never pressed for real.', sel: 'dialog Sign in with Email' }, { noScroll: true });
  await S('login-social-btn', q('[role="dialog"] button, [role="dialog"] a').filter({ hasText: /Sign in with (Facebook|Apple|Google)/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in social', desc: 'A white outline social sign-in pill; never pressed for real.', sel: 'dialog social button' }, { noScroll: true });
  await S('dialog-close', q('button[data-testid="modal-close"], [role="dialog"] button[aria-label*="close" i], [class*="Modal" i] button[aria-label*="close" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Dialog close', desc: 'The X close control of the login card.', sel: 'button[data-testid=modal-close]' }, { noScroll: true });
  await page.keyboard.press('Escape');
  await page.waitForTimeout(800);
  // Try Calm for Free either navigates to the signup flow's first page or
  // opens the same card in signup mode: whichever appears is measured, then
  // left (back or Escape); the flow itself is never submitted.
  try {
    const t = q('header a, header button').filter({ hasText: /Try\s*Calm/i }).filter({ visible: true }).first();
    const before = page.url();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(2500); }
    if (page.url() !== before) {
      // The landing route gets its own PerimeterX challenge — wait it out on
      // this context before declaring the step uncaptured.
      // Path only (safeUrl drops the query and masks id-like segments): a signup
      // redirect can carry a token or an email in its query, and this lands in a
      // committed desc.
      const dest = safeUrl(page.url()).replace(BASE, '');
      // Bot check: recorded as a boundary, not waited out in a loop and not measured. The 2026-11-16 run
      // read the PerimeterX "Press & Hold" container here and published it as the signup page.
      const cleared = await clearChallenge(page, { tries: 3, step: 4000 }).catch(() => false);
      await page.waitForTimeout(1500);
      if (!cleared || (await blocked())) {
        comp('signup-page', { title: 'Signup page', group: g, desc: `The page the Try-Calm-for-Free button navigates to (${dest}): a PerimeterX bot check served instead of the signup flow, recorded as a boundary.` });
        out.components['signup-page'].blocked = true;
        log('  ! signup landing is a bot check: recorded as a boundary');
        await page.goBack({ waitUntil: 'domcontentloaded' }).catch(() => {});
        await page.waitForTimeout(4000);
      } else {
      // a fresh reading replaces an earlier run's bot-check boundary
      if (out.components['signup-page']) delete out.components['signup-page'].blocked;
      await S('signup-page', q('main, [role="main"], form, body > div').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup page', desc: `The page the Try-Calm-for-Free button navigates to (${dest}) — the signup flow's first step, reached by its own button and never submitted${cleared ? '' : '; its landing stayed PerimeterX-blocked this run'}.`, sel: 'signup landing main' }, { noScroll: true, pad: 24 });
      await S('signup-field', q('input, main button, main a, form button, form a, button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup control', desc: 'The first interactive control on the signup landing page; never pressed for real.', sel: 'signup page control' }, { noScroll: true });
      await page.goBack({ waitUntil: 'domcontentloaded' }).catch(() => {});
      await page.waitForTimeout(4000);
      log('  signup navigated to a page; measured it and went back');
      }
    } else {
      // Older behaviour: a card opens in place (the same ModalBody in signup
      // mode). The consent banner also carries role=dialog, so it is excluded.
      await S('signup-dialog', q('[class*="ModalBody" i], [role="dialog"]:not(:has-text("Cookie"))').filter({ visible: true }).last(), ['default'], { group: g, title: 'Signup card', desc: 'The card the Try-Calm-for-Free button opens (sign-up choices or a plan step); never submitted.', sel: 'ModalBody dialog' }, { noScroll: true, pad: 24 });
      await S('signup-field', q('[class*="ModalBody" i] input, [class*="ModalBody" i] button, [class*="ModalBody" i] a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup control', desc: 'The first interactive control inside the signup card; never pressed for real.', sel: 'dialog control' }, { noScroll: true });
      await page.keyboard.press('Escape');
    }
  } catch (e) { log('  ! signup open failed', String(e.message).split('\n')[0]); }
  save();
  await closePage();
}

async function sleep() {
  if (!(await newPage('sleep', { wait: 12000 }))) return;
  await sheetsFor('sleep');
  await chrome('sleep');
  const g = G.app;
  await S('scene', q('[class*="SceneGradient" i], [class*="Scene" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Scene canvas', desc: 'The full-viewport scene gradient the sleep shell paints behind everything.', sel: 'scene gradient' }, { noScroll: true });
  await S('rail', q('aside').filter({ visible: true }).first(), ['default'], { group: g, title: 'App rail', desc: 'The dark left rail: wordmark, Home/Meditate/Sleep/Music/For Work/Wisdom/Calm Kids/Movement/Profile icon items.', sel: 'aside' }, { noScroll: true });
  await S('rail-item', q('nav[aria-label="main app"] a, aside nav a').filter({ hasText: /^\s*(Meditate|Music|Wisdom|Movement)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Rail item', desc: 'An icon-plus-label rail link.', sel: 'nav[aria-label="main app"] a' }, { noScroll: true });
  await S('rail-item-active', q('nav[aria-label="main app"] a[aria-current], nav[aria-label="main app"] a, aside nav a').filter({ hasText: /^\s*Sleep\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Rail item, selected', desc: 'The selected Sleep rail item (its icon tile filled).', sel: 'rail a Sleep' }, { noScroll: true });
  await S('topbar-search', q('a[href="/app/search"], a[aria-label="Search" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Search link', desc: 'The top-bar search icon link to /app/search (the wide search field only paints inside the search page); never followed.', sel: 'a[href=/app/search]' }, { noScroll: true });
  await S('d-login', await domFind(page, /^\s*Log ?In\s*$/i, { sel: 'button', tag: 'dl' }), B4, { group: g, title: 'Dark login', desc: 'The dark shell\'s translucent Log In pill (the shell paints no header element); opens the same login card, never submitted.', sel: 'button (Log In)' }, { noScroll: true });
  await S('d-cta', await domFind(page, /^\s*Try\s+Calm\s+for\s+Free\s*$/i, { sel: 'button', tag: 'dc' }), B4, { group: g, title: 'Dark CTA', desc: 'The white Try-Calm-for-Free pill on the dark top bar; opens the signup flow, never submitted.', sel: 'button (Try Calm)' }, { noScroll: true });
  await S('tab-active', q('button, a, [role="tab"]').filter({ hasText: /^\s*(Sleep Stories|All)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Tab, selected', desc: 'The selected white category pill (Sleep Stories/All).', sel: 'category tab' });
  await S('tab', q('button, a, [role="tab"]').filter({ hasText: /^\s*(Meditations|Soundscapes|Downloads)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Tab', desc: 'An unselected dark category pill.', sel: 'category tab' });
  await S('upsell', q('a[class*="Upsell" i], [class*="Upsell" i]').filter({ hasText: /missing out on the full Calm experience|Subscribe with/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Upsell banner', desc: 'The subscribe upsell bar ("You\'re missing out on the full Calm experience. Subscribe with 40% off ...") — the whole banner is one anchor.', sel: 'a.UpsellBanner' }, { noScroll: true });
  await S('content-card', q('a, article, [class*="Card" i]').filter({ hasText: /narrator|Cozy|Ballad|Friends|Glacier/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Content card', desc: 'A featured-story card: artwork tile, "New" badge, title and narrator.', sel: 'featured card' });
  await S('card-badge', q('[data-testid="new-icon"], [class*="NewTag" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'New badge', desc: 'The white "New" chip on a card\'s artwork.', sel: '[data-testid=new-icon]' });
  await S('see-all', q('a, button').filter({ hasText: /^\s*See All\s*/ }).filter({ visible: true }).first(), B4, { group: g, title: 'See All', desc: 'A section "See All" link with its chevron.', sel: 'See All' });
  await S('carousel-arrow', q('button[aria-label*="carousel" i][aria-label*="next" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Carousel arrow', desc: 'A rail carousel arrow (the "Scroll carousel towards next items" chevron).', sel: 'button[aria-label*=carousel][aria-label*=next]' });
  await S('signup-bar', q('a[class*="Upsell" i], [class*="Upsell" i]').filter({ hasText: /Get notified of new Calm content/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Signup bar', desc: 'The bottom notification bar ("Get notified of new Calm content ...") — a full-width anchor carrying the Sign-up-today gradient pill; never submitted.', sel: 'a.UpsellFooter' }, { noScroll: true });
  await S('signup-button', q('button, a').filter({ hasText: /^\s*Sign up today\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Signup button', desc: 'The gradient Sign-up-today button (pill-shaped) in the bottom bar; never pressed for real.', sel: 'Sign up today' }, { noScroll: true });
  save();
  await closePage();
}

async function meditate() {
  if (!(await newPage('meditate', { wait: 12000 }))) return;
  const g = G.app;
  await S('med-title', q('h1, main h2, [class*="Title" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Section title', desc: 'The page title of an app-shell section (Meditate).', sel: 'section h1' }, { noScroll: true });
  await S('med-card', q('a[class*="CardContainer" i]').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Meditate card', desc: 'A featured content card on the Meditate surface (the shared CardContainer: artwork, title, narrator).', sel: 'a.CardContainer' });
  save();
  await closePage();
}

async function health() {
  if (!(await newPage('health', { wait: 10000 }))) return;
  await sheetsFor('health');
  await chrome('health');
  const g = G.health;
  await S('h-nav', q('nav.main-menu, .main-menu, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Health nav', desc: 'The WordPress B2B header menu (Solutions/Resources megamenus, Log In, contact CTA).', sel: 'nav.main-menu' }, { noScroll: true });
  await S('h-nav-link', q('a.main-menu__link').filter({ hasText: /Support|Solutions|Resources|About Us/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Health nav link', desc: 'A top-level B2B nav link.', sel: '.main-menu a' }, { noScroll: true });
  await S('h-mega-trigger', q('nav.main-menu button, .main-menu button, nav.main-menu a, .main-menu a').filter({ hasText: /Solutions|Resources|About/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Megamenu trigger', desc: 'A menu item that opens a megamenu panel; toggled, never followed.', sel: '.main-menu trigger' }, { noScroll: true });
  await S('h-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Health hero', desc: 'The B2B hero headline.', sel: 'health h1' }, { noScroll: true });
  await S('h-cta', q('a.btn--primary, button.btn--primary').filter({ hasText: /request a demo|contact us|get started/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Health CTA', desc: 'The B2B contact/action button; measured never followed.', sel: 'health CTA' });
  await S('h-card', q('.custom-cards__card').filter({ visible: true }).first(), B4, { group: g, title: 'Health card', desc: 'A card on the B2B surface (customer story, benefit or resource card).', sel: 'health card' });
  await S('h-footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Health footer', desc: 'The B2B footer.', sel: 'health footer' }, { noScroll: true });
  save();
  await closePage();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The marketing footer: link columns, social icons, legal.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="facebook"], footer a[href*="instagram"], footer a[href*="twitter"], footer a[href*="x.com"], footer a:has(svg)').filter({ visible: true }).first(), B4, { group: g, title: 'Social icon', desc: 'A social icon link in the footer (Facebook/Instagram/Twitter); the footer carries no app-store badges.', sel: 'footer social a' }, { noScroll: true });
  save();
  await closePage();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('button[aria-label*="menu" i], button[data-testid*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The hamburger menu toggle (aria-label "Open Mobile menu").', sel: 'button[aria-label*=menu]' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1500); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  const mp = q('nav[aria-label="Mobile navigation menu" i], nav[aria-label*="Mobile" i]').filter({ visible: true }).first();
  const mpick = (await mp.count()) ? mp : q('header nav').filter({ visible: true }).first();
  await S('m-menu-open', mpick, ['default'], { group: g, title: 'Mobile menu, open', desc: 'The full-screen nav panel (aria-label "Mobile navigation menu", fixed z:999) opened by the hamburger toggle.', sel: 'nav[aria-label=Mobile navigation menu]' }, { noScroll: true });
  await S('m-nav-item', await domFind(page, /^\s*(Sleep|Mindfulness|Screening)\s*$/, { sel: 'nav[aria-label*="Mobile" i] button, nav[aria-label*="Mobile" i] a', tag: 'mn', inView: true }), B4, { group: g, title: 'Mobile nav item', desc: 'A button inside the opened mobile menu (Sleep, Mindfulness or Screening — the same styled-components nav items as desktop).', sel: 'mobile nav button' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  // only a run that re-measured the mobile group may describe it as a phone capture
  out._meta.viewport = VIEWPORT_PHONE;
  save();
  await closePage();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
// The viewport note describes the readings on file: a run that does not re-measure the mobile group
// keeps the earlier note (whose mobile readings were taken at 390 x 844 without phone emulation).
const VIEWPORT_PHONE = '1440 x 900 (mobile group 390 x 844 as a phone: mobile UA, isMobile, touch); the marketing pages paint light, the /app/* preview shell paints dark';
out._meta.viewport ??= '1440 x 900 (mobile group 390 x 844); the marketing pages paint light, the /app/* preview shell paints dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, sleep, meditate, login, health, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile' && k !== 'login') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('login')) await plan.login();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a, header button');
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
  for (const c of Object.values(liveCtx)) await c?.close().catch(() => {});
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
