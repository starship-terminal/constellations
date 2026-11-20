// Measures descript.com's public components in every state reachable without
// signing up, starting a trial or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing video templates story underlord auth mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// descript.com is a single light theme signed out: the marketing pages, the
// /templates gallery and the public auth card on web.descript.com. Nothing is
// sent or signed into: the only presses are local UI toggles — the home
// workflow tabs and the pricing Monthly/Annual switch; the auth email field
// is typed into and cleared, never submitted; Sign in, Sign up, Get started
// and every plan/auth action are measured, never followed. No consent overlay
// was seen.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', video: '/video-editing', templates: '/templates', story: '/customers/saastr', underlord: '/underlord', auth: 'https://web.descript.com/authenticate', mobile: '/', 'mobile-pricing': '/pricing' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// page keys newPage() opened during the current plan
const opened = new Set();
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
  opened.add(key);
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
  const loc = target.and(page.locator(':visible')).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).and(page.locator(':visible')).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, run };
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
  const loc = target.and(page.locator(':visible')).first();
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
        await (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).and(page.locator(':visible')).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).and(page.locator(':visible')).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          undo = () => closeOpened(key, loc, opts);
        }
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

// Closes what an `opened` state opened. An open dropdown or menu keeps focus
// and covers the page, so every later focus-visible reading would come back
// 'focus failed'. Escape first, then the trigger again; if the trigger still
// reports aria-expanded="true" the miss is recorded on the opened state so
// the later readings on this page can be checked.
async function closeOpened(key, loc, opts) {
  const expanded = () => loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(400);
  if ((await expanded()) === 'true') { await toggle(loc, { allowLink: opts.allowLink }).catch(() => {}); await page.waitForTimeout(600); }
  if ((await expanded()) === 'true') {
    const st = out.components[key].states.opened;
    if (st) st.closeFailed = 'aria-expanded still "true" after Escape and a second toggle';
    log('  ! opened state did not close', key);
  }
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.and(page.locator(':visible')).first();
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
  shell: 'Header and navigation', home: 'Home', pricing: 'Pricing',
  video: 'Video editing page', templates: 'Templates gallery',
  story: 'Customer story', underlord: 'Underlord', auth: 'Auth card',
  mobile: 'Mobile (390 wide)', footer: 'Footer',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header, nav').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Site header', desc: 'The top bar: Descript wordmark, nav (Features / Pricing / Contact sales), Sign in and the Sign up button.', sel: 'nav' }, { noScroll: true });
  await S('mkt-logo', q('header a, nav a').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Logo', desc: 'The Descript wordmark at the left of the header.', sel: 'header logo' }, { noScroll: true });
  await S('nav-link', q('header a, nav a').filter({ hasText: /^\s*Pricing\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Nav link', desc: 'A header nav link ("Pricing"); measured, never followed.', sel: 'nav Pricing' }, { noScroll: true });
  await S('signin-link', q('header a, nav a, a').filter({ hasText: /^\s*Sign in\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sign in', desc: 'The header "Sign in" link; measured, never followed (it leads to the auth card measured on the auth page).', sel: 'Sign in' }, { noScroll: true });
  await S('signup-cta', q('header a, header button, a').filter({ hasText: /^\s*Sign up\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sign up button', desc: 'The maroon "Sign up" button in the header; measured, never followed.', sel: 'Sign up' }, { noScroll: true });
  const h = G.home;
  await S('hero-eyebrow', q('h1').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Eyebrow', desc: 'The small uppercase red eyebrow above the display headline ("AI VIDEO EDITOR").', sel: 'h1 eyebrow' }, { noScroll: true });
  await S('hero-display', q('h2').filter({ hasText: /AI-editing|every kind of video/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Display headline', desc: 'The gamuthDisplay display headline on the home hero.', sel: 'hero h2' }, { noScroll: true });
  const t = G.home;
  await S('flow-tabs', q('button').filter({ hasText: /^\s*Record\s*$/ }).and(page.locator(':visible')).first().locator('xpath=..'), ['default'], { group: t, title: 'Workflow tabs', desc: 'The Record / Edit / Refine / Share / Multiply workflow tab strip in "The whole workflow, right here".', sel: 'workflow tab strip' });
  await S('flow-tab', q('button').filter({ hasText: /^\s*Edit\s*$/ }).and(page.locator(':visible')).first(), [...B4, 'opened'], { group: t, title: 'Workflow tab', desc: 'A workflow tab ("Edit"); its opened state is a local tab selection, never a navigation.', sel: 'workflow tab' });
  await S('flow-tab-rest', q('button').filter({ hasText: /^\s*Multiply\s*$/ }).and(page.locator(':visible')).first(), B4, { group: t, title: 'Workflow tab (rest)', desc: 'A second workflow tab measured at rest for the unselected style.', sel: 'workflow tab' });
  await S('section-h2', q('h2').filter({ hasText: /whole workflow|change what/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Section heading', desc: 'A home section heading ("The whole workflow, right here").', sel: 'section h2' });
  const f = G.footer;
  await S('site-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: f, title: 'Site footer', desc: 'The sitemap footer (product links, resources, company).', sel: 'footer' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pr-eyebrow', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Page eyebrow', desc: 'The uppercase "PRICING" eyebrow heading.', sel: 'pricing h1' }, { noScroll: true });
  await S('pr-display', q('h2').filter({ hasText: /plan for whatever/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Pricing headline', desc: 'The display heading "A plan for whatever you create".', sel: 'pricing h2' }, { noScroll: true });
  await S('pr-toggle', q('button').filter({ hasText: /^\s*Monthly\s*$/ }).and(page.locator(':visible')).first().locator('xpath=..'), ['default'], { group: g, title: 'Billing toggle', desc: 'The Monthly / Annual billing switch above the plan cards.', sel: 'billing toggle' }, { noScroll: true });
  await S('pr-toggle-month', q('button').filter({ hasText: /^\s*Monthly\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Monthly option', desc: 'The "Monthly" toggle option; measured, the Annual side is toggled below.', sel: 'Monthly' }, { noScroll: true });
  await S('pr-toggle-annual', q('button').filter({ hasText: /^\s*Annual\s*$/ }).and(page.locator(':visible')).first(), [...B4, 'opened'], { group: g, title: 'Annual option', desc: 'The "Annual" toggle option — a local billing switch; its opened state is the selected-annual style, never a purchase.', sel: 'Annual' }, { noScroll: true, before: { opened: async () => { const m = q('button').filter({ hasText: /^\s*Monthly\s*$/ }).and(page.locator(':visible')).first(); await m.click({ timeout: 4000 }).catch(() => m.evaluate((el) => el.click())); await page.waitForTimeout(600); return 'Monthly selected first'; } } });
  await S('pr-card', q('a, button').filter({ hasText: /Get started|Try free|Choose/i }).and(page.locator(':visible')).first().locator('xpath=ancestor::*[contains(@class,"card") or contains(@class,"plan") or self::li or self::div][1]'), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (name, price, feature list, CTA).', sel: 'plan card' });
  await S('pr-cta', q('a, button').filter({ hasText: /^\s*(Get started|Try free|Choose)/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\u2019s CTA; measured, never followed (it starts signup/checkout).', sel: 'plan CTA' });
  await S('pr-compare-h2', q('h2').filter({ hasText: /difference/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Comparison heading', desc: 'The "What\u2019s the difference?" heading over the plan comparison table.', sel: 'compare h2' });
  await S('pr-faq', q('h2').filter({ hasText: /Frequently asked/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'FAQ heading', desc: 'The "Frequently asked questions" section heading.', sel: 'faq h2' });
  save();
}

async function video() {
  if (!(await newPage('video', { wait: 10000 }))) return;
  await sheetsFor('video');
  await chrome('video');
  const g = G.video;
  await S('vid-h1', q('h1, h2').filter({ hasText: /All-in-one video editing|video editing/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Page headline', desc: 'The "All-in-one video editing" display heading.', sel: 'video h1' }, { noScroll: true });
  await S('vid-cta', q('a, button').filter({ hasText: /Get started|Try free/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Page CTA', desc: 'The video page hero CTA; measured, never followed.', sel: 'video CTA' });
  await S('vid-h2', q('h2').and(page.locator(':visible')).nth(1), ['default'], { group: g, title: 'Section heading', desc: 'A feature section heading on the video page.', sel: 'video h2' });
  save();
}

async function templates() {
  if (!(await newPage('templates', { wait: 10000 }))) return;
  await sheetsFor('templates');
  await chrome('templates');
  const g = G.templates;
  await S('tpl-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Gallery heading', desc: 'The templates gallery heading.', sel: 'templates h1' }, { noScroll: true });
  await S('tpl-card', q('a.absolute.inset-0').and(page.locator(':visible')).first().locator('xpath=..'), ['default'], { group: g, title: 'Template card', desc: 'A template card in the gallery grid (thumbnail, name, category); the overlay link was measured, never followed.', sel: 'template card' });
  await S('tpl-link', q('a.absolute.inset-0').and(page.locator(':visible')).first(), B4, { group: g, title: 'Template link', desc: 'A template card\u2019s overlay link; measured, never followed.', sel: 'template overlay link' });
  save();
}

async function story() {
  if (!(await newPage('story', { wait: 10000 }))) return;
  await sheetsFor('story');
  await chrome('story');
  const g = G.story;
  await S('st-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Story headline', desc: 'The SaaStr customer story headline.', sel: 'story h1' }, { noScroll: true });
  await S('st-prose', q('main p, article p').filter({ hasText: /[\s\S]{60}/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Story prose', desc: 'Body copy in the customer story.', sel: 'story p' });
  await S('st-cta', q('a, button').filter({ hasText: /Request a demo|Get started|Try free/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Story CTA', desc: 'The "Request a demo" CTA in the customer story; measured, never followed.', sel: 'Request a demo' });
  save();
}

async function underlord() {
  if (!(await newPage('underlord', { wait: 10000 }))) return;
  await sheetsFor('underlord');
  await chrome('underlord');
  const g = G.underlord;
  await S('ul-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Underlord headline', desc: 'The Underlord AI co-editor page headline.', sel: 'underlord h1' }, { noScroll: true });
  await S('ul-cta', q('a, button').filter({ hasText: /Get started|Try free|Try Underlord/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Underlord CTA', desc: 'The Underlord page CTA; measured, never followed.', sel: 'underlord CTA' });
  save();
}

async function auth() {
  if (!(await newPage('auth', { wait: 10000 }))) return;
  await sheetsFor('auth');
  await chrome('auth');
  const g = G.auth;
  await S('au-card', q('main, [class*="Auth"], form').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Auth card', desc: 'The sign-in card on web.descript.com/authenticate (SSO buttons, email field, terms links).', sel: 'auth card' }, { noScroll: true });
  await S('au-google', q('button').filter({ hasText: /Continue with Google/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Google SSO', desc: '"Continue with Google" — the outline SSO button; measured, never pressed.', sel: 'Continue with Google' }, { noScroll: true });
  await S('au-sso', q('button').filter({ hasText: /single sign-on/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'SSO button', desc: '"Use single sign-on" — the second outline auth option; measured, never pressed.', sel: 'Use single sign-on' }, { noScroll: true });
  await S('au-email', q('input[type="email"], input').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Email field', desc: 'The auth email input; focused and typed into then cleared, never submitted.', sel: 'auth email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('au-email-btn', q('button').filter({ hasText: /Continue with email/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Email button', desc: '"Continue with email" — the primary auth button; measured, never pressed.', sel: 'Continue with email' }, { noScroll: true });
  await S('au-password', q('button').filter({ hasText: /password instead/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Password link', desc: '"Use a password instead" — the ghost fallback; measured, never pressed.', sel: 'Use a password instead' }, { noScroll: true });
  await S('au-terms', q('a').filter({ hasText: /Terms of Service/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Terms link', desc: 'The "Terms of Service" link under the auth card; measured, never followed.', sel: 'Terms of Service' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header, nav').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar: wordmark and sign-in/sign-up actions.', sel: 'mobile nav' }, { noScroll: true });
  await S('m-eyebrow', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile eyebrow', desc: 'The phone hero eyebrow heading.', sel: 'mobile h1' });
  await S('m-display', q('h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile display', desc: 'The phone display headline.', sel: 'mobile h2' });
  await S('m-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'mobile footer' });
  save();
  if (!(await newPage('mobile-pricing', { mobile: true, url: BASE + '/pricing', wait: 10000 }))) return;
  await chrome('mobile-pricing');
  await S('mp-toggle', q('button').filter({ hasText: /^\s*Annual\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile billing toggle', desc: 'The Annual option of the billing toggle on the phone.', sel: 'mobile Annual' }, { noScroll: true });
  await S('mp-cta', q('a, button').filter({ hasText: /Get started|Try free|Choose/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile plan CTA', desc: 'A plan CTA on the phone pricing page; measured, never followed.', sel: 'mobile plan CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); descript.com paints a single light theme signed out';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, video, templates, story, underlord, auth, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
// A plan can open more than one page key (mobile() opens 'mobile' and
// 'mobile-pricing'): every key the plan opened counts as finished with it, so
// a component that vanished from either page is pruned.
const finishedPages = new Set();
const finish = () => { for (const k of opened) finishedPages.add(k); opened.clear(); };
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finish(); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finish(); }
  // Reduced-motion check on an element that transitions (the Create CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a, nav a');
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
