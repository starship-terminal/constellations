// Measures copy.ai's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// copy.ai is a Webflow marketing site with semantic class names (.mega--nav,
// .btn_nav, .request_input-field); specs select by class fragment, role,
// aria-label or text. The product itself sits behind app.copy.ai; the public
// auth card on login.copy.ai is measured as a surface — nothing is submitted.
// The only presses are local UI toggles — the Platform mega-menu, an FAQ
// accordion row, the contact form's own focus and the mobile menu. The HubSpot
// cookie banner and chat widget are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', pricing: '/prices', contact: '/contact-us', login: 'https://app.copy.ai/login' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const earlierRun = new WeakMap();  // component -> the run its states were measured in before this one
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
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current] || '') ? URLS[current] : BASE + (URLS[current] || '') }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

// A failed rerun keeps the state's earlier good reading and notes the error on
// it (recaptureError), as the kit does; only a state with no reading gets {error}.
function keepOrFail(c, state, e) {
  const msg = String(e.message || e).slice(0, 200);
  const prev = c.states[state];
  // a kept reading keeps the run it was measured in (comp() has already stamped this run on c),
  // and the failed retry is recorded beside it with its own date
  c.states[state] = prev && !prev.error
    ? { ...prev, run: prev.run || earlierRun.get(c) || c.run, recaptureError: msg, recaptureRun: run }
    : { error: msg, run };
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };  // each state names the run that measured it
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    keepOrFail(c, state, e);
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  if (prev) earlierRun.set(prev, prev.run);  // before comp() stamps this run
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
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
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      keepOrFail(out.components[key], st, e);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: lazy-mounted sections
// only enter the DOM once scrolled into view.
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
    await p.goto(URLS[key] ? (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]) : BASE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// The Platform mega-menu opens on hover (a Webflow dropdown); click is the
// fallback. Marks the opened panel with data-m-mark="flyout".
async function openFlyout() {
  const t = q('.mega--nav_dd_toggle').filter({ hasText: /Platform/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.hover({ timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(1200);
  const list = q('.w-dropdown-list.w--open, .mega--nav_dd_list').filter({ visible: true }).first();
  if (!(await list.count())) { await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(1200); }
  return page.evaluate(() => {
    const l = [...document.querySelectorAll('.w-dropdown-list, .mega--nav_dd_list')].find((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 200 && getComputedStyle(e).visibility !== 'hidden' && (e.classList.contains('w--open') || r.height > 0);
    });
    if (!l) return false;
    l.setAttribute('data-m-mark', 'flyout');
    return true;
  });
}

// Marks the opened mobile navigation panel: the container holding the
// accordion rows (Platform/Use cases/Resources/GTM AI) and the Login /
// Contact Sales actions.
async function markMobileMenu() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div,nav,aside,section')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return r.height > innerHeight * 0.5 && r.width > innerWidth * 0.6
        && /Login|Contact Sales/i.test(t) && /Platform|Pricing|Resources/i.test(t) && t.length < 9000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks the smallest visible ancestor of a "Get started" plan CTA that holds
// a plan name and a price — one plan card, not the whole layout.
async function markPlanCard() {
  await page.evaluate(() => {
    const cta = [...document.querySelectorAll('a.btn--price, button, a')].find((b) => /Get started/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0);
    if (!cta) return;
    let n = cta;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Chat|Enterprise|Self.?Serve/i.test(t) && /\$\d|\d+\s*\/\s*mo|per (month|year)/i.test(t) && t.length < 3000 && r.width < 800 && r.height > 300) {
        n.setAttribute('data-m-mark', 'plancard');
        return;
      }
    }
    // no ancestor fits a plan card: leave it unmarked so the spec records a miss
    // (never the CTA's parent or the layout standing in for the card)
  });
}

// Marks the sign-in card on login.copy.ai: the smallest visible ancestor of
// the email field that also holds the OAuth buttons.
async function markAuthCard() {
  await page.evaluate(() => {
    const fld = [...document.querySelectorAll('input[type="email"]')].find((e) => e.getBoundingClientRect().width > 0);
    if (!fld) return;
    let n = fld;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Continue with Google|Continue with email/i.test(t) && t.length < 3000 && r.height > 250 && r.width < 800) {
        n.setAttribute('data-m-mark', 'authcard');
        return;
      }
    }
    // no ancestor holds the OAuth buttons: leave it unmarked so the spec records a miss
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  contact: 'Contact', login: 'Login', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('top-banner', q('.top-banner_component').filter({ visible: true }).first(), ['default'], { group: g, title: 'Top banner', desc: 'The dark promo strip above the nav ("The 2026 Benchmarks Report is Finally Here!" with its arrow action); static, scrolls with the page.', sel: '.top-banner_component' }, { noScroll: true });
  await S('header', q('nav.mega--nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky nav.mega--nav (z 1000): wordmark, the Platform/Use cases/Resources/Pricing/GTM AI triggers, Login and the Get a Demo action.', sel: 'nav.mega--nav' }, { noScroll: true });
  await S('logo', q('a.navbar_brand').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The copy.ai wordmark anchor.', sel: 'a.navbar_brand' }, { noScroll: true });
  await S('nav-dd-toggle', q('.mega--nav_dd_toggle').filter({ hasText: /Platform/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav dropdown trigger', desc: 'The Platform trigger that opens the mega-menu; toggled for the menu screenshot, never followed.', sel: '.mega--nav_dd_toggle' }, { noScroll: true });
  await S('btn-nav', q('a.btn_nav').filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The purple "Get a Demo" button in the header; measured, never followed.', sel: 'a.btn_nav' }, { noScroll: true });
  await S('login-link', q('a.mega--nav_login-link').filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The header Login action (app.copy.ai); measured, never followed.', sel: 'a.mega--nav_login-link' }, { noScroll: true });
  try { await openFlyout(); } catch (e) { log('  ! flyout open failed', String(e.message).split('\n')[0]); }
  await S('nav-dd-panel', q('[data-m-mark="flyout"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-menu panel', desc: 'The opened Platform mega-menu (OVERVIEW / WORKFLOWS / INTELLIGENCE LAYER / TECHNICAL RESOURCES columns).', sel: 'opened Platform dropdown' }, { noScroll: true, noReset: true });
  const ensureFlyout = async () => {
    if (!(await q('[data-m-mark="flyout"]').filter({ visible: true }).count())) { await openFlyout(); await page.waitForTimeout(400); }
  };
  await S('dd-link', q('[data-m-mark="flyout"] a.dd-link').filter({ visible: true }).first(), B4, { group: g, title: 'Dropdown link', desc: 'A link inside the opened Platform mega-menu (How it Works et al.); measured, never followed.', sel: 'mega-menu a.dd-link' }, { noScroll: true, noReset: true, before: { default: ensureFlyout, hover: ensureFlyout, 'focus-visible': ensureFlyout, pressed: ensureFlyout } });
  await page.keyboard.press('Escape'); await page.mouse.move(700, 500); await page.waitForTimeout(600);
  const h = G.home;
  await lazyLoad();
  await S('hero-title', q('h1.home--hero_h1, h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "The First AI-Native GTM Platform" display.', sel: 'h1.home--hero_h1' });
  await S('hero-sub', q('p.home--hero_small-text').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline (Infuse AI across your go-to-market engine…).', sel: 'p.home--hero_small-text' });
  await S('hero-email', q('input#Email.form--input, input.form--input').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Email field', desc: 'The hero "What\'s your email?" field; focused and given sample text that was deleted again — the form was never submitted.', sel: 'input#Email.form--input' });
  await S('hero-submit', q('input#submit.button.is-submit, input.is-submit').filter({ visible: true }).first(), B4, { group: h, title: 'Hero submit', desc: 'The black "Get a demo" submit of the hero email form; measured, never pressed.', sel: 'input.is-submit' });
  await S('playbook-card', q('a.btn--playbook').filter({ visible: true }).first(), B4, { group: h, title: 'Playbook card', desc: 'A "Get Demo" playbook card (the purple GTM-AI-Playbook rail); measured, never followed.', sel: 'a.btn--playbook' });
  await S('invert-cta', q('a.btn--primary-invert').filter({ visible: true }).first(), B4, { group: h, title: 'Inverted CTA', desc: 'A "Get a demo" action on a dark band (the inverted variant); measured, never followed.', sel: 'a.btn--primary-invert' });
  await S('platform-card', q('a.platfrom_right-card').filter({ visible: true }).first(), B4, { group: h, title: 'Platform card', desc: 'A platform-feature card (Agents Automate…); measured, never followed.', sel: 'a.platfrom_right-card' });
  await S('section-h2', q('h2.heading--h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A 56px section heading (Design Your GTM AI Playbook).', sel: 'h2.heading--h2' });
  await S('blog-card', q('a.blog-slider_card').filter({ visible: true }).first(), B4, { group: h, title: 'Blog card', desc: 'A blog/article card in the home slider; measured, never followed.', sel: 'a.blog-slider_card' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 9000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  await lazyLoad();
  const g = G.pricing;
  await S('pricing-h1', q('h1.heading--h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Copy.ai pricing" display heading.', sel: 'h1.heading--h1' }, { noScroll: true });
  await S('plan-toggle', q('button.price_menu-toggle').filter({ visible: true }).first(), B4, { group: g, title: 'Plan toggle', desc: 'The Self-Serve / Enterprise segmented control; measured at rest — toggling it swaps the pricing view, so the pressed state is the CDP-forced one.', sel: 'button.price_menu-toggle' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'The Chat plan card (name, checklist, Monthly|Annually control, the 20% SAVING badge, $29/mo and Get started).', sel: 'plan card (.price_layout-new)' });
  await S('plan-price', await domFind(page, /\$\s*\d+/, { sel: 'div, span, p, h3', tag: 'price' }), ['default'], { group: g, title: 'Plan price', desc: 'The $29/mo price figure in the plan card.', sel: 'plan $ figure' });
  await S('plan-cta', q('a.btn--price').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The plan card\'s "Get started" action; measured, never followed.', sel: 'a.btn--price' });
  await S('saving-badge', await domFind(page, /SAVING/i, { sel: 'div, span, p', tag: 'saving', leaf: true }), ['default'], { group: g, title: 'Saving badge', desc: 'The "20% SAVING" outlined badge inside the plan card.', sel: 'SAVING badge' });
  await S('faq-item', q('.faq_trigger').filter({ visible: true }).first(), B4, { group: g, title: 'FAQ row', desc: 'An FAQ accordion row (question + the open chevron); measured closed, the opened state is the screenshot toggle.', sel: '.faq_trigger' });
  save();
}

async function contact() {
  if (!(await newPage('contact', { wait: 9000 }))) return;
  await sheetsFor('contact');
  await chrome('contact');
  const g = G.contact;
  await S('contact-h1', q('h1.heading-01-hero, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Contact title', desc: 'The "Got Questions?" display heading.', sel: 'h1.heading-01-hero' }, { noScroll: true });
  await S('name-input', q('input#Name.request_input-field').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Name field', desc: 'The "Your Name" field of the contact form; focused and given sample text that was deleted again — never submitted.', sel: 'input#Name' }, { fillText: 'Ada Example' });
  await S('email-input', q('input#Email.request_input-field').filter({ visible: true }).first(), ['default'], { group: g, title: 'Email field', desc: 'The "Your Email" field of the contact form.', sel: 'input#Email.request_input-field' });
  await S('message-field', q('textarea.ms-text-area, textarea.request_input-field').filter({ visible: true }).first(), ['default'], { group: g, title: 'Message field', desc: 'The "What would you like to learn?" textarea.', sel: 'textarea.request_input-field' });
  await S('send-button', q('form a.btn--primary').filter({ visible: true }).first(), B4, { group: g, title: 'Send button', desc: 'The "Send message" action of the contact form (the input[type=submit] twin is hidden); measured, never pressed.', sel: 'form a.btn--primary' });
  await S('contact-faq', q('.faq_trigger').filter({ visible: true }).first(), B4, { group: g, title: 'Contact FAQ row', desc: 'An FAQ accordion row beside the form; measured closed, never expanded.', sel: '.faq_trigger' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  const g = G.login;
  await markAuthCard();
  await S('auth-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Auth card', desc: 'The login.copy.ai sign-in card (email field, Continue with email, the OAuth buttons, the Sign up link); captured, never used.', sel: 'auth card' }, { noScroll: true });
  await S('auth-email', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Auth email field', desc: 'The "Your email address" input; focused and given sample text that was deleted again — nothing sent.', sel: 'input[type=email]' }, { noScroll: true });
  await S('auth-continue', q('button').filter({ hasText: /Continue with email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The "Continue with email" submit; measured, never pressed.', sel: 'Continue with email' }, { noScroll: true });
  await S('auth-oauth', q('a, button').filter({ hasText: /Continue with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'OAuth button', desc: 'The "Continue with Google" action (an anchor); measured, never followed — it would leave for the OAuth flow.', sel: 'Continue with Google' }, { noScroll: true });
  await S('auth-signup', q('a, button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The "Sign up" link on the auth card; measured, never followed.', sel: 'Sign up link' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: the link columns, social icons and legal.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('a.footer_link').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer column link (Blog / Contact Support / Changelog); measured, never followed.', sel: 'a.footer_link' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="linkedin"], footer a[href*="twitter"], footer a[href*="x.com"], footer a[href*="youtube"], footer a[aria-label*="LinkedIn" i], footer a[aria-label*="Twitter" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('nav.mega--nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'nav.mega--nav at 390' }, { noScroll: true });
  const menu = q('a.mega--nav_burger_trigger').filter({ visible: true }).first();
  await S('m-menu-button', menu, B4, { group: g, title: 'Menu button', desc: 'The circled burger toggle (a.mega--nav_burger_trigger).', sel: '.mega--nav_burger_trigger' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await markMobileMenu();
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile menu: the accordion rows (Platform / Use cases / Resources / Pricing / GTM AI) over the page with Login and Contact Sales at the foot.', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] .mega--nav_dd_toggle, [data-m-mark="mmenu"] [role="button"]').filter({ hasText: /^\s*(Platform|Pricing|Use cases|Resources|GTM AI)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu row', desc: 'A row inside the opened mobile menu.', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-login', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /^\s*Login\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile login', desc: 'The Login action inside the mobile menu; measured, never followed.', sel: 'mobile menu Login' }, { noScroll: true });
  await S('m-sales', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /Contact Sales/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sales CTA', desc: 'The purple Contact Sales action inside the mobile menu; measured, never followed.', sel: 'mobile menu Contact Sales' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  try { await menu.click({ timeout: 3000 }).catch(() => {}); await page.waitForTimeout(600); } catch { /* still open is fine */ }
  await S('m-hero', q('h1.home--hero_h1, h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); copy.ai paints a single light theme with ink-dark bands inside the light pages';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, contact, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // dropdown trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.mega--nav_dd_toggle');
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
