// Measures biosites.com's public components in every state reachable without
// signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home claim mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// biosites.com is a Next.js site (frontsitev2 CSS modules) in one light theme
// under a black hero collage; there are no design-token custom properties, so
// every value is a computed-style measurement. The nav is a fixed #navbar
// div, the FAQ a static <dl>, and /editor redirects to the signed-out
// claim-username screen. Nothing is sent, downloaded or signed into: the only
// presses are hover/focus/CDP :active on links and buttons; LOG IN, SIGN UP,
// "Create a free Bio Site", "Get started ↗", the claim submit and every legal
// link are measured, never followed or pressed for real. The claim field's
// filled state types a throwaway string and deletes it; nothing is submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', claim: APP };
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
  const url = URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key];
  await open(page, url, { wait });
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
        if (opts.forceHover) {
          undo = await forcePseudo((opts.hoverLoc || loc).filter({ visible: true }).first(), ['hover']);
          via = 'CDP forcePseudoState :hover';
        } else {
          await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
          await page.waitForTimeout(450);
          via = 'mouse hover';
        }
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
      } else if (st === 'expanded') {
        await toggle(loc); await page.waitForTimeout(900); via = 'own toggle';
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

// Clicks a UI toggle. Refuses a submit button and any control whose text
// names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign up|sign up for free|create|create a free bio site|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|start building|get started|get started ↗|claim|share|export|select|continue|continue with email|book|request)$/i;
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
  shell: 'Shell and navigation', home: 'Home', claim: 'Claim (signed-out editor)',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// The footer is a plain <div>: find the smallest ancestor that covers the
// whole band — the "BUILD YOUR FREE LINK IN BIO PAGE" CTA plus the
// ABOUT/SUPPORT/CONTACT/LEGAL/SOCIAL link columns — and mark it.
async function markFooter() {
  return page.evaluate(() => {
    const trigger = [...document.querySelectorAll('h1,h2,h3,h4,div,p,a')].find((x) => /BUILD YOUR FREE LINK/i.test(x.innerText || '') && (x.innerText || '').length < 100);
    if (!trigger) return false;
    let n = trigger;
    while (n.parentElement && !/SOCIAL/i.test(n.innerText || '')) n = n.parentElement;
    n.setAttribute('data-m-footer', '1');
    return true;
  });
}

// A persona card in the sliding carousel: the smallest ancestor of a "Get
// started ↗" link that also holds the persona label and paints a surface.
async function markCard() {
  return page.evaluate(() => {
    const gs = [...document.querySelectorAll('a')].find((a) => /^Get started/.test((a.innerText || '').trim()));
    if (!gs) return false;
    let n = gs;
    for (let i = 0; n.parentElement && i < 6; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      const c = getComputedStyle(n);
      if (r.width > 150 && r.width < 600 && r.height > 200 && (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || parseFloat(c.borderRadius) > 8)) break;
    }
    n.setAttribute('data-m-card', '1');
    return true;
  });
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  // The persona marquee is a sliding carousel: freeze it so a card does not
  // leave the viewport between centring and hover.
  await page.addStyleTag({ content: '[class*="carousel" i], [class*="carousel" i] * { animation-play-state: paused !important; }' });
  await page.evaluate(() => document.querySelectorAll('[class*="carousel" i]').forEach((el) => el.getAnimations({ subtree: true }).forEach((a) => a.pause()))).catch(() => {});
  const g = G.shell;
  // Note: hasText regexes are case-sensitive against textContent — the site's
  // caps styling is text-transform, so every text regex is /…/i here.
  await S('navbar', q('#navbar'), ['default'], { group: g, title: 'Navbar', desc: 'The fixed top bar (a #navbar div, not a header): the BIO.SITES mark left, BLOG / LOG IN / SIGN UP FOR FREE pills right.', sel: '#navbar' }, { noScroll: true });
  await S('logo', q('#navbar a').first(), ['default'], { group: g, title: 'Logo', desc: 'The BIO.SITES wordmark and Squarespace tagline (svg inside the first nav anchor).', sel: '#navbar a (first)' }, { noScroll: true });
  const navA = (t) => q('#navbar a').filter({ hasText: t }).filter({ visible: true }).first();
  await S('nav-link', navA(/^blog$/i), B4, { group: g, title: 'Nav link', desc: 'The BLOG pill, the only outbound item in the bar (text-transform renders "Blog" caps).', sel: '#navbar a:has-text("Blog")' }, { noScroll: true });
  await S('nav-login', navA(/^log in$/i), B4, { group: g, title: 'Log in pill', desc: 'The inverted pill linking to /editor?loginUser=true. Measured, never followed.', sel: '#navbar a:has-text("Log in")' }, { noScroll: true });
  await S('nav-signup', navA(/^sign up/i), B4, { group: g, title: 'Sign up pill', desc: 'The black "SIGN UP FOR FREE" pill linking to /editor. Measured, never followed.', sel: '#navbar a:has-text("Sign up")' }, { noScroll: true });
  await S('page-ground', q('body'), ['default'], { group: g, title: 'Page ground', desc: 'The body fill: black under the hero collage; the content sections paint their own surfaces.', sel: 'body' }, { noScroll: true, crop: false });

  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', desc: '"Your brand, your storefront, one link." under the dark collage band.', sel: 'first h1' }, { noScroll: true });
  await S('hero-sub', q('h1').first().locator('xpath=following::*[self::p or self::div][string-length(normalize-space())>40][1]'), ['default'], { group: h, title: 'Hero subcopy', sel: 'first long paragraph under h1' }, { noScroll: true });
  await S('cta', q('button').filter({ hasText: /Create a free Bio Site/ }).filter({ visible: true }).first(), B4, { group: h, title: 'CTA button', desc: 'The black "Create a free Bio Site" pill repeated down the page; a real <button>. Measured, never pressed for real.', sel: 'button:has-text("Create a free Bio Site")' }, { noScroll: true });
  await S('section-nav-link', q('a[href="#standout"]').first(), B4, { group: h, title: 'Section link', desc: 'One of the STAND OUT / SELL / CONNECT / ANALYZE anchor links under the hero.', sel: 'a[href="#standout"]' });
  await S('section-title', q('h2').filter({ hasText: /Stand out with engaging designs/ }).first(), ['default'], { group: h, title: 'Section title', sel: 'h2:has-text("Stand out")' });
  await S('eyebrow', q('h3').filter({ hasText: /trusted by/i }).first(), ['default'], { group: h, title: 'Eyebrow label', desc: 'The "TRUSTED BY MILLIONS OF" small-caps label over the carousel.', sel: 'h3:has-text("Trusted by")' });
  await markCard();
  await S('persona-card', q('[data-m-card="1"]'), ['default'], { group: h, title: 'Persona card', desc: 'A template card in the sliding carousel ("Health & Wellness", "Musician", …) with a "Get started ↗" link.', sel: 'marked ancestor of a Get started link' });
  // The marquee is JS-driven (the pause did not hold it): before every state,
  // mark whichever "Get started" instance is inside the viewport at that
  // moment — every card paints the same control — and aim the locator at the
  // marked copy first.
  const markInViewGs = async () => page.evaluate(() => {
    document.querySelectorAll('[data-m-gs]').forEach((x) => x.removeAttribute('data-m-gs'));
    const vh = innerHeight, vw = innerWidth;
    const hit = [...document.querySelectorAll('a')].find((a) => {
      if (!/^get started/i.test((a.innerText || '').trim())) return false;
      const r = a.getBoundingClientRect();
      return r.width > 0 && r.y > 0 && r.y + r.height < vh && r.x > 0 && r.x + r.width < vw;
    });
    if (!hit) return false;
    hit.setAttribute('data-m-gs', '1');
    return true;
  });
  const gsLoc = q('[data-m-gs="1"]').or(q('a').filter({ hasText: /^get started/i }).filter({ visible: true }).first());
  const markGs = async () => { await markInViewGs(); return 'marked the in-view instance'; };
  await S('card-cta', gsLoc, B4, { group: h, title: 'Card CTA', desc: 'The "Get started ↗" link inside a persona card, straight to /editor (each state reads whichever card the marquee had in view; hover is CDP-forced because the moving card never sits still for a pointer). Measured, never followed.', sel: 'a:has-text("Get started")' }, { forceHover: true, before: { default: markGs, hover: markGs, 'focus-visible': markGs, pressed: markGs } });
  // The FAQ is a static <dl>: question h3s with always-visible answers, no
  // accordion to press.
  await S('faq-item', q('h3').filter({ hasText: /Why should I use a link in bio tool/ }).first(), ['default'], { group: h, title: 'FAQ item', desc: 'A question row of the static FAQ <dl>; answers are always painted, nothing to expand.', sel: 'h3:has-text("Why should I use")' });

  // Footer on the same page.
  const f = G.footer;
  if (await markFooter()) {
    await S('footer', q('[data-m-footer="1"]'), ['default'], { group: f, title: 'Footer', desc: 'The bottom band: the "BUILD YOUR FREE LINK IN BIO PAGE" CTA, the BIO.SITE/YOURNAME marquee and the ABOUT/SUPPORT/CONTACT/LEGAL/SOCIAL columns.', sel: 'marked footer div' });
  }
  await S('footer-cta', q('h2').filter({ hasText: /bio\.site\/yourname/i }).first(), B4, { group: f, title: 'Footer marquee', desc: 'The giant "BIO.SITE/YOURNAME ↗" call; its ancestor links to /editor. Measured, never followed.', sel: 'h2:has-text("BIO.SITE/YOURNAME")' });
  await S('footer-link', q('a').filter({ hasText: /^Squarespace$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'An ABOUT column link (Squarespace).', sel: 'a:has-text("Squarespace")' });
  await S('footer-legal', q('a').filter({ hasText: /^Terms of service$/ }).filter({ visible: true }).first(), B4, { group: f, title: 'Legal link', sel: 'a:has-text("Terms of service")' });
  await S('footer-social', q('a').filter({ hasText: /^Instagram$/ }).filter({ visible: true }).last(), B4, { group: f, title: 'Social link', desc: 'A SOCIAL column link (Instagram; TikTok is the same control).', sel: 'a:has-text("Instagram")' });
  save();
}

async function claim() {
  if (!(await newPage('claim'))) return;
  const g = G.claim;
  // The title paints as text, not an h-tag with content: find the element
  // that holds "Claim your free username".
  const title = page.locator('text=Claim your free').first();
  await S('claim-title', title, ['default'], { group: g, title: 'Claim title', desc: '"Claim your free username" on the signed-out /editor screen.', sel: 'text "Claim your free"' }, { noScroll: true });
  // The field is a bare input inside a 50px-radius bordered wrap; measure both.
  await page.evaluate(() => {
    const i = document.querySelector('input[type="text"], input:not([type])');
    if (!i) return;
    i.setAttribute('data-m-field', '1');
    let n = i;
    for (let k = 0; n && k < 5; n = n.parentElement, k++) {
      const c = getComputedStyle(n);
      if (parseFloat(c.borderTopWidth) > 0 && c.borderTopStyle !== 'none' || c.backgroundColor !== 'rgba(0, 0, 0, 0)') { n.setAttribute('data-m-fieldwrap', '1'); break; }
    }
  });
  await S('claim-field-wrap', q('[data-m-fieldwrap="1"]'), ['default'], { group: g, title: 'Username field shell', desc: 'The 50px-radius bordered pill holding the bio.site/ prefix, the input and the circular submit.', sel: 'bordered ancestor of the username input (marked in-page)' });
  await S('claim-field', q('[data-m-field="1"]'), ['default', 'focused', 'filled'], { group: g, title: 'Username field', desc: 'The "bio.site/username" text input; a throwaway string was typed and deleted, nothing submitted.', sel: 'input[type=text]' }, { fillText: 'capturesample' });
  // The circular arrow button inside the field shell; pressing it would start
  // a claim, so only forced :active is captured.
  const submit = q('button[class*="UsernameSearch__submit"], button').filter({ hasText: /^$/ }).filter({ visible: true }).first();
  await S('claim-submit', submit, B4, { group: g, title: 'Claim submit', desc: 'The circular arrow button inside the field pill. Measured, never pressed for real — nothing was claimed.', sel: 'button.UsernameSearch__submit' });
  await S('claim-login', q('button').filter({ hasText: /^Log In$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in button', desc: 'The "Log In" pill top right of the claim screen. Measured, never pressed.', sel: 'button:has-text("Log In")' }, { noScroll: true });
  await S('claim-legal', q('a').filter({ hasText: /^Privacy Policy$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Legal link', desc: 'The Privacy Policy link in the claim footer (squarespace.com). Measured, never followed.', sel: 'a:has-text("Privacy Policy")' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-navbar', q('#navbar'), ['default'], { group: g, title: 'Mobile navbar', desc: 'The fixed bar at 390 wide: the circle-dot mark, BLOG and LOG IN text links, the black SIGN UP pill. No menu trigger exists.', sel: '#navbar' }, { noScroll: true });
  await S('m-signup', q('#navbar a').filter({ hasText: /sign up/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign up pill', desc: 'The black SIGN UP pill, the mobile bar\'s only button. Measured, never followed.', sel: '#navbar a:has-text("Sign up")' }, { noScroll: true });
  await S('m-cta', q('button').filter({ hasText: /Create a free Bio Site/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile CTA', desc: 'The "Create a free Bio Site" button at 390 wide.', sel: 'button:has-text("Create a free Bio Site")' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, claim, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
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
