// Measures DoorDash's public signed-out components in every state reachable
// without signing in, ordering, entering an address or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home food-delivery business dashpass restaurants store hsa promos
// careers mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// BOUNDARY: live *.doordash.com Cloudflare-blocks this client; every reading
// comes from the product's own SSR pages rendered from Internet Archive
// snapshots (URLS, "<timestamp>/<original url>"). doordash.com is a Next.js
// app (consumer-web-next): styled-components over the prism token system
// (:where(.prism-theme) --base/--usage/--comp vars); stable hooks are
// data-testid attributes and kind="BUTTON/<VARIANT>". careersatdoordash.com
// is a separate WordPress/Tailwind stack, measured only for context.
// Nothing is sent, ordered, address-gated or signed into: the only presses
// are local UI toggles — tabs, Show-more reveals, the mobile hamburger and
// focus/blur on the address field (never typed into with a real address,
// never submitted). The cookie banner is un-hidden for one measurement then
// re-hidden; it is never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';
import { prefer } from './prefer.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '20261112001404/https://www.doordash.com/',
  'food-delivery': '20261004033917/https://www.doordash.com/food-delivery/',
  business: '20261012092322/https://www.doordash.com/en-US/business/',
  dashpass: '20261012183135/https://www.doordash.com/en-US/dashpass/student',
  restaurants: '20261005002021/https://www.doordash.com/en-US/restaurants-near-me/',
  store: '20261024031734/https://www.doordash.com/en-US/store/the-sweet-tooth-north-miami-beach-33434247/',
  hsa: '20260930222321/https://www.doordash.com/en-US/p/hsa-fsa-store',
  promos: '20261008212700/https://www.doordash.com/en-US/promos/',
  careers: '20261009000533/https://careersatdoordash.com/',
  mobile: '20261112001404/https://www.doordash.com/',
};
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
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|wayback machine doesn't have that page archived/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 9000, promo = 'close', url = null } = {}) {
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
  page.setDefaultTimeout(9000);
  log('open', key, mobile ? '(mobile)' : '');
  // open() returns false when the bot check did not clear: that page is a boundary, never measured
  // as the product (finding 20-4), whatever blocked() reads off the page afterwards.
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });
  if (!cleared || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
  // A Wayback replay can serve the HTML without the product's stylesheets: then every reading is the
  // browser's default (Times 16px, link blue; a native button would read the UA sans). Require the
  // site's own face on some text before measuring: DD Norms on the prism pages, TT Norms Pro on the
  // careers WordPress theme.
  const face = /^car/.test(key) ? 'tt norms pro' : 'dd norms';
  const styled = await page.evaluate((f) => [...document.querySelectorAll('h1, h2, p, span, a, button')].slice(0, 600)
    .some((el) => getComputedStyle(el).fontFamily.toLowerCase().includes(f)), face).catch(() => false);
  if (!styled) { log('  UNSTYLED', key, '(the archived stylesheets did not apply; recorded as a failed page)'); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline|order|search)$/i;
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
    await p.goto(BASE + URLS[key], { waitUntil: 'commit', timeout: 120000 }).catch(() => {});
    for (let i = 0; i < 30; i++) {
      const len = await p.evaluate(() => (document.body && document.body.innerText || '').length).catch(() => 0);
      if (len > 200) break;
      await p.waitForTimeout(2000);
    }
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
// or a background image (a CTA band's red field), or falls back to marking a
// painted descendant.
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

// markPainted() and domFind() return a locator that matches nothing on a miss (never null), and so
// does NONE() when either throws. Locator.or() is a union resolved in DOM order, so neither
// `x || fallback` nor `.or()` prefers x: prefer() (prefer.mjs) takes the first candidate with a visible
// match, in the order given.
const NONE = () => q('[data-m-mark="__none__"]');

const G = {
  shell: 'App shell and navigation', hero: 'Marketing hero', bands: 'CTA bands and cards',
  dir: 'Directory lists and tabs', store: 'Storefront (menu page)', food: 'Restaurant directory',
  field: 'Fields, search and gates', footer: 'Footer', careers: 'Careers site (WordPress stack)',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The marketing home's top bar carries the wordmark, language select and
  // the Sign in / Sign Up buttons (anchors to identity.doordash.com —
  // measured, never followed).
  const bar = await markPainted('[data-testid="signInButton"]', 'm-topbar', { minW: 600, minH: 40 }).catch(NONE);
  // The painted ancestor this climbs to is the campaign hero field itself
  // (the top bar floats on it — the marketing page has no separate bar
  // background), so this component IS the hero band.
  await S('hero-band', await prefer(bar, q('[data-testid="signInButton"]').locator('xpath=ancestor::div[4]')), ['default'], { group: g, title: 'Hero band', desc: 'The marketing hero region the top bar floats on: wordmark, Sign in and Sign Up over the campaign field (the bar has no separate paint).', sel: 'painted ancestor of [data-testid=signInButton] (the hero)' }, { noScroll: true });
  await S('logo', await prefer(q('a[href="/"], a[href*="doordash.com/"], svg').filter({ hasText: /^\s*DoorDash\s*$/i }).first(), q('a').filter({ has: q('span[class*="VisuallyHiddenText"]') }).first()), ['default'], { group: g, title: 'Wordmark', desc: 'The DoorDash wordmark anchor (svg + visually-hidden label).', sel: 'wordmark anchor' }, { noScroll: true });
  await S('signin-btn', q('[data-testid="signInButton"]'), B4, { group: g, title: 'Sign-in button', desc: 'kind="BUTTON/PRIMARY" anchor to identity.doordash.com; measured, never followed.', sel: '[data-testid=signInButton]' }, { noScroll: true });
  await S('signup-btn', q('[data-testid="signUpButton"]'), B4, { group: g, title: 'Sign-up button', desc: 'kind="BUTTON/PLAIN" red pill to the signup URL; measured, never followed.', sel: '[data-testid=signUpButton]' }, { noScroll: true });
  await S('language-select', q('[data-testid="LanguageDropdown"]'), ['default', 'focused'], { group: g, title: 'Language select', desc: 'The footer/top-bar native <select> of locales (data-size="small").', sel: '[data-testid=LanguageDropdown]' }, { noScroll: true });
  const h = G.hero;
  await S('hero-title', q('[data-testid="HomePageHeroHeader"]'), ['default'], { group: h, title: 'Hero headline', desc: 'The campaign h1 — TTNormsProCond-Blk 900, uppercase.', sel: '[data-testid=HomePageHeroHeader]' });
  await S('hero-sub', q('[data-testid="HomePageHeroHeader"]').locator('xpath=following::span[1]'), ['default'], { group: h, title: 'Hero subcopy', desc: 'The line under the hero headline ("Other fees apply").', sel: 'span under HomePageHeroHeader' });
  // The two address pills under the hero copy — "Sign in for saved address"
  // and "Use current Location" — are the product's address gate. Measured,
  // never pressed (a press either opens sign-in or prompts geolocation).
  const pill = await domFind(page, /Sign in for saved address/i, { sel: 'a,button,[role="button"]', tag: 'm-pill', minW: 100 }).catch(NONE);
  await S('address-pill', await prefer(pill, q('a,button').filter({ hasText: /saved address/i }).first()), B4, { group: h, title: 'Address pill (sign-in gate)', desc: 'The "Sign in for saved address" hero pill — an authentication gate, never pressed.', sel: 'hero pill "Sign in for saved address"' });
  const pill2 = await domFind(page, /Use current Location/i, { sel: 'a,button,[role="button"]', tag: 'm-pill2', minW: 80 }).catch(NONE);
  await S('location-pill', await prefer(pill2, q('a,button').filter({ hasText: /current Location/i }).first()), B4, { group: h, title: 'Location pill', desc: 'The "Use current Location" hero pill — a geolocation prompt, never pressed.', sel: 'hero pill "Use current Location"' });
  const b = G.bands;
  await S('cta-band', q('[data-testid="splash-cta-background"], [data-testid="CTASplash"]').first(), ['default'], { group: b, title: 'CTA band', desc: 'A mid-page CTA section (CTASplash) — tinted band with headline, copy and a primary action.', sel: '[data-testid=CTASplash]' });
  await S('cta-band-title', q('[data-testid="CTAContentHeader"]').first(), ['default'], { group: b, title: 'CTA band headline', sel: '[data-testid=CTAContentHeader]' });
  await S('cta-band-copy', q('[data-testid="CTAContentDescription"]').first(), ['default'], { group: b, title: 'CTA band copy', sel: '[data-testid=CTAContentDescription]' });
  await S('cta-btn', q('[data-testid="CTAContentCTAButton"]').first(), B4, { group: b, title: 'CTA button', desc: 'kind="BUTTON/PRIMARY" red pill in the CTA band; measured, never followed.', sel: '[data-testid=CTAContentCTAButton]' });
  await S('value-prop-card', q('[data-testid="value-prop-card-wrapper"]').first(), B4, { group: b, title: 'Value-prop card', desc: 'A "Become a Dasher"-style card: illustration, heading, copy and a link.', sel: '[data-testid=value-prop-card-wrapper]' });
  await S('card-cta', q('[data-testid="card-cta-button"], [data-testid="cta-text"]').first(), B4, { group: b, title: 'Card CTA', desc: 'The arrow/action inside a value-prop card.', sel: '[data-testid=card-cta-button]' });
  const d = G.dir;
  await S('section-title', q('h2').filter({ hasText: /neighborhood|popular|cities/i }).first(), ['default'], { group: d, title: 'Section title', desc: 'A "Get more from your neighborhood" h2.', sel: 'h2 section title' });
  await S('tab-selected', q('[role="tab"][data-testid$="-selected"], [data-testid="tab-topcities-selected"]').first(), B4, { group: d, title: 'Directory tab, selected', desc: 'The selected tab (Top Cities) — 3px bottom border in the selected colour.', sel: '[role=tab][data-testid$=-selected]' });
  await S('tab-idle', q('[role="tab"][data-testid$="-not-selected"]').first(), B4, { group: d, title: 'Directory tab, idle', desc: 'An idle tab (Top Cuisines / Top Chains).', sel: '[role=tab][data-testid$=-not-selected]' });
  await S('dir-link', await prefer(await domFind(page, /^(Atlanta|Austin|Boston|Chicago|Denver|Pizza|Chinese Food|Sushi)$/i, { sel: 'a', tag: 'm-dirlink', minW: 40 }).catch(NONE), q('a').filter({ hasText: /^\s*(Atlanta|Chicago|Pizza)\s*$/ }).first()), B4, { group: d, title: 'Directory link', desc: 'A city/cuisine/chain link in the tabbed directory lists.', sel: 'directory a' });
  await S('show-more', q('[data-testid="rest-items-toggle"], [data-testid="rest-items-toggle-icon-button"]').first(), B4, { group: d, title: 'Show-more toggle', desc: 'The expand/collapse control on a directory list; measured, not pressed here (toggled in the shot pass).', sel: '[data-testid=rest-items-toggle]' });
  await S('cross-link', q('[data-testid="cross-link-anchor"]').first(), B4, { group: d, title: 'Cross link', desc: 'A cross-category link tile (e.g. grocery → convenience).', sel: '[data-testid=cross-link-anchor]' });
  save();
}

async function foodDelivery() {
  if (!(await newPage('food-delivery'))) return;
  await sheetsFor('food-delivery');
  await chrome('food-delivery');
  const g = G.dir;
  await S('fd-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: 'The food-delivery page headline.', sel: 'h1 on /food-delivery/' }, { noScroll: true });
  const city = await domFind(page, /^(Atlanta|Austin|Boston|Chicago|Dallas|Denver|Houston|Las Vegas|Los Angeles|Miami|New York)$/i, { sel: 'a,button,[role="button"],[data-testid]', tag: 'm-city', minW: 30 }).catch(NONE);
  await S('city-link', await prefer(city, q('[data-testid="Atlanta"], a').filter({ hasText: /^\s*Atlanta\s*$/ }).first()), B4, { group: g, title: 'City link', desc: 'A city directory entry (per-city data-testid); measured, never followed.', sel: 'city link' });
  await S('fd-faq', q('[data-testid="seo-faq-block"], details, [class*="faq" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ block', desc: 'The SEO FAQ accordion block, if published on this route.', sel: 'seo-faq-block' });
  save();
}

async function business() {
  if (!(await newPage('business'))) return;
  await sheetsFor('business');
  await chrome('business');
  const g = G.bands;
  await S('biz-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Business hero', desc: 'The DoorDash for Business headline.', sel: 'h1 on /en-US/business/' }, { noScroll: true });
  await S('biz-cta', q('a,button').filter({ hasText: /Get started|Learn more|Sign up|Contact/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Business CTA', desc: 'The business page primary action; measured, never followed.', sel: 'business page CTA' });
  const merchant = await domFind(page, /^(7-Eleven|Safeway|ALDI|CVS|Walgreens)$/i, { sel: 'a,div,li,[data-testid]', tag: 'm-merch', minW: 30 }).catch(NONE);
  await S('biz-merchant', await prefer(merchant, q('[data-testid="7-Eleven"]').first()), ['default'], { group: g, title: 'Merchant link', desc: 'A merchant-name entry in the business directory lists.', sel: 'merchant entry' });
  save();
}

async function dashpass() {
  if (!(await newPage('dashpass'))) return;
  await sheetsFor('dashpass');
  await chrome('dashpass');
  const g = G.shell;
  // The app shell header: logo, address button, side-nav, cart, bell.
  await S('app-header', q('[data-testid="Header"]'), ['default'], { group: g, title: 'App header', desc: 'The consumer app shell header — HomeLogo, address button, side-nav toggle, cart and bell.', sel: '[data-testid=Header]' }, { noScroll: true });
  await S('app-logo', q('[data-testid="HomeLogo"]'), ['default'], { group: g, title: 'App wordmark', sel: '[data-testid=HomeLogo]' }, { noScroll: true });
  await S('address-btn', q('[data-testid="addressTextButton"]'), B4, { group: g, title: 'Address button', desc: 'The header address/destination control — an address gate, never pressed.', sel: '[data-testid=addressTextButton]' }, { noScroll: true });
  await S('sidenav-toggle', q('[data-testid="side-nav"], [data-testid="hamburger"]').first(), ['default'], { group: g, title: 'Side-nav toggle', desc: 'The hamburger that opens the side navigation; toggled on mobile only.', sel: '[data-testid=side-nav] / hamburger' }, { noScroll: true });
  await S('cart-btn', q('[data-testid="OrderCartIconButton"], [data-testid="OrderCartButton"]').first(), B4, { group: g, title: 'Cart button', desc: 'The header cart (icon button with badge); measured, never pressed.', sel: '[data-testid=OrderCartIconButton]' }, { noScroll: true });
  await S('bell-btn', q('[data-testid="NotificationBell"], [data-testid="HeaderNotificationBellIcon"]').first(), B4, { group: g, title: 'Bell button', desc: 'The header notifications bell; measured, never pressed.', sel: '[data-testid=NotificationBell]' }, { noScroll: true });
  const g2 = G.bands;
  await S('dp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g2, title: 'DashPass headline', desc: 'The DashPass student page headline.', sel: 'h1 on /en-US/dashpass/student' });
  await S('dp-cta', q('a,button').filter({ hasText: /DashPass|Get started|Try|Sign up|Start/i }).filter({ visible: true }).first(), B4, { group: g2, title: 'DashPass CTA', desc: 'A DashPass signup action; measured, never followed (signup gated).', sel: 'dashpass CTA' });
  save();
}

async function restaurants() {
  if (!(await newPage('restaurants'))) return;
  await sheetsFor('restaurants');
  await chrome('restaurants');
  const g = G.food;
  // The CompactCard* testids exist in the DOM but paint 0x0 (ghost SSR
  // duplicates); the cards a visitor sees are /store/… anchors. The card is
  // the anchor's nearest ancestor that also holds the tile image.
  await S('rest-card', q('a[href*="/store/"]').filter({ hasText: /\S/ }).first().locator('xpath=ancestor::div[.//img][1]'), ['default'], { group: g, title: 'Restaurant card', desc: 'A restaurant tile: image, name, rating/ETA and an offer badge.', sel: 'a[href*=/store/] ancestor with img' });
  await S('rest-card-title', q('a[href*="/store/"]').filter({ hasText: /\S/ }).first(), ['default'], { group: g, title: 'Card title', sel: 'a[href*=/store/] with text' });
  const sub = await domFind(page, /^\d+(\.\d+)?\s*(mi|km)$|^\d+(\.\d+)?\s*min$/i, { sel: 'span,div,p', tag: 'm-rsub', minW: 30 }).catch(NONE);
  await S('rest-card-sub', await prefer(sub, q('a[href*="/store/"]').first().locator('xpath=following::div[1]')), ['default'], { group: g, title: 'Card subtitle', desc: 'The rating · ETA · fee line under the restaurant name (a single styled leaf of the row).', sel: 'rating/ETA leaf under a card' });
  await S('offer-badge', q('[data-testid^="offer:"]').first(), ['default'], { group: g, title: 'Offer badge', desc: 'A promo chip on a restaurant card ("20% off on $40+").', sel: '[data-testid^=offer:]' });
  await S('leaderboard-badge', q('[data-testid^="top_rated_leaderboard"], [data-testid^="farther_away"]').first(), ['default'], { group: g, title: 'Leaderboard badge', desc: 'A "Top 10%"-style tag on a restaurant card.', sel: '[data-testid^=top_rated_leaderboard]' });
  await S('popular-btn', q('[data-testid="PopularItemsButton"]').first(), B4, { group: g, title: 'Popular-items button', sel: '[data-testid=PopularItemsButton]' });
  await S('nearby-cta', q('[data-testid="LocationPageSearchNearByCTA"], [data-testid="LocationPageSignInCTA"]').first(), B4, { group: g, title: 'Location CTA', desc: 'The "search nearby"/sign-in call at the end of the directory; measured, never pressed (address/sign-in gate).', sel: 'LocationPage*CTA' });
  await S('pagination', q('[data-testid="lego-pagination-loader"]').first(), B4, { group: g, title: 'Pagination loader', sel: '[data-testid=lego-pagination-loader]' });
  await S('faq-block', q('[data-testid="seo-faq-block"]').first(), ['default'], { group: g, title: 'FAQ block', desc: 'The SEO FAQ accordion under the listings.', sel: '[data-testid=seo-faq-block]' });
  await S('internal-link', q('[data-testid="internal-links-section-list-item"] a, [data-testid="seo-internal-links"] a').first(), B4, { group: g, title: 'Internal link', desc: 'A related-cuisine link in the footer SEO block.', sel: 'internal-links-section a' });
  save();
}

async function store() {
  if (!(await newPage('store'))) return;
  await sheetsFor('store');
  await chrome('store');
  const g = G.store;
  // The cookie banner is hidden by open(); un-hide it for one measurement of
  // the published component, then re-hide. Never answered.
  await page.evaluate(() => { const b = document.querySelector('[data-testid="cookie-banner"]'); if (b) b.style.removeProperty('display'); }).catch(() => {});
  await S('cookie-banner', q('[data-testid="cookie-banner"]'), ['default'], { group: G.field, title: 'Cookie banner', desc: 'The consent strip, measured then re-hidden — never answered.', sel: '[data-testid=cookie-banner]' }, { noScroll: true });
  await page.evaluate(() => { const b = document.querySelector('[data-testid="cookie-banner"]'); if (b) b.style.setProperty('display', 'none', 'important'); }).catch(() => {});
  await S('store-head', q('[data-testid="storeInfo"], [data-testid="HeroImageContainer"]').first(), ['default'], { group: g, title: 'Store header', desc: 'The storefront header: hero image, name, rating and delivery info.', sel: '[data-testid=storeInfo] / HeroImageContainer' }, { noScroll: true });
  await S('store-name', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Store name', sel: 'h1 on store page' }, { noScroll: true });
  await S('store-meta', q('[data-testid="infoBoxDetail"], [data-testid="MenuHeaderDeliveryFee"]').first(), ['default'], { group: g, title: 'Store meta', desc: 'The rating/distance/delivery-fee detail line under the store name.', sel: 'infoBoxDetail / MenuHeaderDeliveryFee' }, { noScroll: true });
  await S('fulfil-toggle', q('[data-testid="MenuOrderMethodToggleDelivery"], [data-testid="OrderMethodToggle"]').first(), B4, { group: g, title: 'Fulfilment toggle', desc: 'The Delivery/Pickup segmented toggle in the menu header; measured, not pressed (a press re-queries the menu).', sel: 'MenuOrderMethodToggle*' }, { noScroll: true });
  await S('group-order', q('[data-testid="CreateGroupCartModalButton"], [data-testid="GroupOrderButtonIconWithLabel"]').first(), B4, { group: g, title: 'Group-order button', desc: 'The group-cart action; measured, never pressed.', sel: 'CreateGroupCartModalButton' }, { noScroll: true });
  await S('search-input', q('[data-testid="SearchInput"], [data-testid="search-icon"]').first(), ['default', 'focused'], { group: g, title: 'Store search field', desc: 'The in-store menu search input; focused only, never submitted.', sel: '[data-testid=SearchInput]' }, { noScroll: true });
  await S('menu-item', q('[data-testid="VirtualGridContainer"] > *').first(), ['default'], { group: g, title: 'Menu item card', desc: 'A menu item in the virtualised grid: image, name, price.', sel: 'VirtualGridContainer > item' });
  await S('quick-add', q('[data-testid="quick-add-button"]').first(), B4, { group: g, title: 'Quick-add button', desc: 'The + quick-add circle on a menu item; measured, NEVER pressed — a press starts a cart.', sel: '[data-testid=quick-add-button]' });
  await S('rec-section', q('[data-testid="recommended_items_for_you"], [data-testid="carousel-slider"]').first(), ['default'], { group: g, title: 'Recommended carousel', desc: 'The "Recommended items for you" carousel rail.', sel: 'recommended_items_for_you' });
  await S('breadcrumb', q('[data-testid="seo-breadcrumb"]').first(), ['default'], { group: g, title: 'Breadcrumb', desc: 'The SEO breadcrumb trail at the foot of the store page.', sel: '[data-testid=seo-breadcrumb]' });
  await S('address-nux', q('[data-testid="nuxStoreMissingAddress"]').first(), ['default'], { group: g, title: 'Missing-address nux', desc: 'The new-user "add an address" prompt shown without a saved address — the documented address gate, never answered.', sel: '[data-testid=nuxStoreMissingAddress]' });
  save();
}

async function hsa() {
  if (!(await newPage('hsa'))) return;
  await sheetsFor('hsa');
  await chrome('hsa');
  const g = G.field;
  await S('hsa-search', q('[data-testid="SearchInput"]').first(), ['default', 'focused'], { group: g, title: 'Search input', desc: 'The catalog search field on the HSA/FSA store; focused only, nothing submitted.', sel: '[data-testid=SearchInput]' });
  await S('hsa-toggle', q('[data-testid="OrderMethodToggle"]').first(), B4, { group: g, title: 'Delivery/Pickup toggle', sel: '[data-testid=OrderMethodToggle]' });
  await S('hsa-h1', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo page title', desc: 'The HSA/FSA store headline.', sel: 'h1 on /en-US/p/hsa-fsa-store' });
  save();
}

async function promos() {
  if (!(await newPage('promos'))) return;
  await sheetsFor('promos');
  await chrome('promos');
  const g = G.field;
  // The address gate itself: measured and focused, never typed into with a
  // real address and never submitted. The documented gate stays closed.
  await S('address-field', q('[data-testid="LandingPageAddressSearch"] input, [data-testid="LandingPageAddressSearch"]').first(), ['default', 'focused'], { group: g, title: 'Address field (gate)', desc: 'The landing-page address search — the entry point the whole consumer flow is gated behind. Focused only; nothing typed or submitted.', sel: '[data-testid=LandingPageAddressSearch]' });
  await S('identity-btn', q('[data-testid="identityButton"]').first(), B4, { group: g, title: 'Identity button', desc: 'The header Sign-in/sign-up identity control; measured, never followed.', sel: '[data-testid=identityButton]' });
  await S('landing-link', q('[data-testid="LandingLinks"] a, [data-testid="LandingLinks"]').first(), B4, { group: g, title: 'Landing link', sel: '[data-testid=LandingLinks]' });
  save();
}

async function careers() {
  if (!(await newPage('careers'))) return;
  await sheetsFor('careers');
  await chrome('careers');
  const g = G.careers;
  await S('car-header', q('header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Careers header', desc: 'The careersatdoordash.com header — a separate WordPress/Tailwind stack (bg-pinot-noir, .btn), not the prism consumer system.', sel: 'careers header' }, { noScroll: true });
  await S('car-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Careers headline', sel: 'careers h1' });
  await S('car-btn', q('a.btn, a[class*="btn"]').filter({ visible: true }).first(), B4, { group: g, title: 'Careers button', desc: 'A .btn pill on the WordPress careers theme.', sel: 'a.btn' });
  await S('car-nav-link', q('nav a, header a').filter({ hasText: /Teams|Jobs|Life|Students/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Careers nav link', sel: 'careers nav a' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 7000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('[data-testid="Footer"], footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: link columns, store badges, language select, socials, legal.', sel: '[data-testid=Footer]' }, { noScroll: true });
  await S('footer-link', q('[data-testid="Footer"] a, footer a').filter({ hasText: /About|Careers|Help|Terms/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('appstore-badge', q('[data-testid="AppStoreButton"], [data-testid="GoogleStoreButton"]').first(), B4, { group: g, title: 'Store badge', desc: 'The App Store / Google Play badge links.', sel: '[data-testid=AppStoreButton]' }, { noScroll: true });
  await S('social-btn', q('[data-testid="FacebookSocialMediaButton"], [data-testid="InstagramSocialMediaButton"], [data-testid="TwitterSocialMediaButton"]').first(), B4, { group: g, title: 'Social button', desc: 'A social-media icon link in the footer.', sel: '[data-testid$=SocialMediaButton]' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true }))) return;
  await chrome('mobile');
  const g = G.mobile;
  const bar = await markPainted('[data-testid="signInButton"], [data-testid="signinSignupButton"]', 'm-mtopbar', { minW: 200, minH: 40 }).catch(NONE);
  await S('m-topbar', await prefer(bar, q('header').filter({ visible: true }).first()), ['default'], { group: g, title: 'Mobile top bar', sel: 'top bar at 390' }, { noScroll: true });
  await S('m-identity-btn', q('[data-testid="signinSignupButton"], [data-testid="signInButton"]').first(), B4, { group: g, title: 'Mobile identity button', desc: 'The combined sign-in/sign-up control at 390 wide.', sel: 'identity button at 390' }, { noScroll: true });
  await S('m-hero', q('[data-testid="HomePageHeroHeader"], h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the prism consumer system paints light only — no dark theme is published; careers is a separate WordPress/Tailwind stack';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.source = 'Internet Archive Wayback Machine snapshots of the product’s own SSR pages (live *.doordash.com Cloudflare-blocks this client); see raw/archive-urls.json';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, 'food-delivery': foodDelivery, business, dashpass, restaurants, store, hsa, promos, careers, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a button's press
  // transition), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '[data-testid="signUpButton"]');
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
