// Measures endlesstools.io's and app.endlesstools.io's public components in
// every state reachable without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home login legal mobile (`legal` measures /legal/privacy_policy and
// records its components under page `privacy`; `privacy` is accepted as an alias).
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// Two surfaces paint signed out: the Next.js/Tailwind-v4 marketing one-pager
// on endlesstools.io (declared --color-*/--text-* layer, dark only) and the
// app host's public shell (the /login card and /legal/* document pages,
// Tailwind v3, dark). Nothing is sent, submitted or signed into: the only
// presses are local UI toggles — the Yearly/Monthly billing toggle, the login
// card's "Log in with password" switch and the newsletter consent checkbox.
// The newsletter and login forms were never submitted; no consent overlay was
// seen (any would be hidden, never answered).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: BASE + '/', login: APP + '/login', privacy: APP + '/legal/privacy_policy', mobile: BASE + '/' };
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
  const cleared = await open(page, url || URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
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

// Clicks a UI toggle (a billing option, a form-mode switch, a checkbox label).
// Refuses a submit button and any control whose text names an action this kit
// must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|continue|claim this offer|try again|next|confirm|schedule event|i understand|decline|send code|stay updated|go pro)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const SEC = 'section[data-analytics-section';

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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (a plan card's #121212 fill sits several wrappers up),
// or falls back to marking a painted descendant.
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

const G = {
  shell: 'Shell and navigation', hero: 'Home hero', assets: 'Asset inputs',
  sections: 'Statement sections', pricing: 'Pricing', team: 'Team and education',
  social: 'Testimonials', news: 'Newsletter', footer: 'Footer',
  auth: 'Log in (app host)', legal: 'Legal documents (app host)',
  mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('div.nav-gradient, div.sticky').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky top bar over a fade gradient: the logomark, the Log-in outline pill and the white Start-for-free pill.', sel: 'div.nav-gradient' }, { noScroll: true });
  await S('logo', q('div.nav-gradient img[alt*="Endless" i], .nav-gradient img').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Endless Tools dot-grid logomark anchor.', sel: '.nav-gradient img' }, { noScroll: true });
  await S('nav-login', q('.nav-gradient a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The Log-in header action (secondary pill on a blurred #1e1e1e fill); measured never followed.', sel: '.nav-gradient a "Log in"' }, { noScroll: true });
  await S('nav-cta', q('.nav-gradient a, .nav-gradient button').filter({ hasText: /Start for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Start-for-free white pill; measured never followed (it opens the app host).', sel: '"Start for free" pill' }, { noScroll: true });
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The 42px title-primary headline; "exploration" and "graphic designers" carry hand-drawn circle/underline marks painted by masked white spans.', sel: 'hero h1' }, { noScroll: true });
  await S('hero-mark', q('h1 span[aria-hidden="true"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Annotation mark', desc: 'One of the aria-hidden white spans behind the headline words, masked (via CSS mask-image) into the hand-drawn circle and underline — the signature annotation style repeated on every section heading.', sel: 'h1 span[aria-hidden]' }, { noScroll: true, crop: false });
  await S('hero-lede', q('p').filter({ hasText: /Bring your assets/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero copy', desc: 'The 14px grey-4 lede under the headline.', sel: 'hero lede' });
  await S('hero-cta', q('a, button').filter({ hasText: /Start exploring/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The Start-exploring pill — the only pink (#FF13B1) action on the site; measured never followed.', sel: '"Start exploring"' });
  const a = G.assets;
  await S('asset-title', q(`${SEC}="hero_inputs"] h2`).filter({ hasText: /Use a library/i }).filter({ visible: true }).first(), ['default'], { group: a, title: 'Asset input title', desc: 'An input-source heading (Use a library) inside a hand-drawn circle mark.', sel: 'hero_inputs h2 "Use a library"' });
  await S('asset-thumb', q(`${SEC}="hero_inputs"] div.rounded-\\[16px\\], ${SEC}="hero_inputs"] video`).filter({ visible: true }).first(), ['default'], { group: a, title: 'Asset thumbnail', desc: 'A floating asset tile: a looping muted video in a 16px-radius rounded box.', sel: 'hero_inputs video tile' });
  const s = G.sections;
  await S('section-title', q('h1, h2').filter({ hasText: /The hard part/i }).filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A statement heading ("The hard part isn\'t making it.") — title-primary inside an underline mark.', sel: '"The hard part" heading' });
  // The workspace stage is the rounded wrapper holding the section's one big
  // video; a bare section-media selector drifts onto the floating orbit tiles.
  await S('editor-shot', q(`${SEC}="hero_workspace"] div:has(> video), ${SEC}="hero_workspace"] video`).filter({ visible: true }).first(), ['default'], { group: s, title: 'Product shot', desc: 'The embedded product-workspace image/video in the "One workspace" band (marketing content, not the app).', sel: 'workspace section media' });
  const pr = G.pricing;
  await S('billing-yearly', q('button').filter({ hasText: /Yearly/i }).filter({ visible: true }).first(), B4, { group: pr, title: 'Billing toggle, yearly', desc: 'The Yearly option of the billing toggle (selected by default — the chosen option renders disabled).', sel: 'button "Yearly"' });
  await S('billing-monthly', q('button').filter({ hasText: /^\s*Monthly\s*$/i }).filter({ visible: true }).first(), B4, { group: pr, title: 'Billing toggle, monthly', desc: 'The Monthly option, read as the page left it (public.mjs pressed it only for the home-dark-monthly screenshot); never checked out.', sel: 'button "Monthly"' });
  await S('save-pill', q('button span, span').filter({ hasText: /Save 17%/i }).filter({ visible: true }).first(), ['default'], { group: pr, title: 'Save badge', desc: 'The pink "Save 17%" pill inside the Yearly option.', sel: '"Save 17%" badge' });
  await S('plan-card', q('div.rounded-\\[33px\\]').filter({ visible: true }).first(), ['default', 'hover'], { group: pr, title: 'Plan card', desc: 'A pricing plan card: 33px radius, #121212 fill, 1px #222 ring, hover lifts to #1D1D1D.', sel: 'div.rounded-[33px]' });
  await S('plan-chip', q('div').filter({ hasText: /^\s*FREE\s*$/ }).filter({ visible: true }).first(), ['default'], { group: pr, title: 'Plan chip', desc: 'The FREE plan chip — a dark pill on the card header.', sel: '"FREE" chip' });
  await S('plan-chip-pro', q('div').filter({ hasText: /^\s*PRO\s*$/ }).filter({ visible: true }).first(), ['default'], { group: pr, title: 'Plan chip, PRO', desc: 'The PRO chip — the inverted white pill.', sel: '"PRO" chip' });
  await S('plan-chip-edu', q('div').filter({ hasText: /^\s*EDUCATION\s*$/ }).filter({ visible: true }).first(), ['default'], { group: pr, title: 'Plan chip, EDUCATION', desc: 'The EDUCATION chip — the one blue element on the surface.', sel: '"EDUCATION" chip' });
  await S('plan-price', q('div').filter({ hasText: /^\$\d+(\.\d+)?$/ }).filter({ visible: true }).first(), ['default'], { group: pr, title: 'Plan price', desc: 'A plan price figure at title-primary size.', sel: 'plan price' });
  await S('plan-feature', q('div').filter({ hasText: /AI Generation|Export|Visual Effects/i }).filter({ visible: true }).last(), ['default'], { group: pr, title: 'Plan feature row', desc: 'A feature row on the PRO card: a 15px SVG glyph plus a bold white key and grey detail text.', sel: 'plan feature row' });
  await S('plan-cta', q('a, button').filter({ hasText: /Try for free|Go PRO|Get Education/i }).filter({ visible: true }).first(), B4, { group: pr, title: 'Plan CTA', desc: 'A plan card action (white pill); measured never followed.', sel: '"Try for free"' });
  const t = G.team;
  await S('team-cta', q('a, button').filter({ hasText: /Create team/i }).filter({ visible: true }).first(), B4, { group: t, title: 'Team CTA', desc: 'The Create-team action under the shared-workspace section; measured never followed.', sel: '"Create team"' });
  await S('edu-cta', q('a').filter({ hasText: /Request Education access/i }).filter({ visible: true }).first(), B4, { group: t, title: 'Education CTA', desc: 'The Request-Education-access mailto link; measured never followed.', sel: '"Request Education access"' });
  const so = G.social;
  // The card is the painted wrapper that holds the .et-tweet-content text; a
  // hasText filter on bare divs climbs to the whole tweets section.
  await S('social-card', q(`${SEC}="tweets"] div:has(> div.et-tweet-content)`).filter({ visible: true }).first(), ['default'], { group: so, title: 'Testimonial card', desc: 'A "Created with Endless Tools" social post card in the carousel.', sel: 'testimonial card' });
  await S('carousel-prev', q('button[aria-label="Previous"]').filter({ visible: true }).first(), B4, { group: so, title: 'Carousel prev', desc: 'The round 40px Previous arrow of the testimonial carousel.', sel: 'button[aria-label=Previous]' });
  await S('promo-card', q('div.fixed').filter({ hasText: /Endless Tools|Art Director|designer/i }).filter({ visible: true }).first(), ['default'], { group: so, title: 'Floating promo card', desc: 'The fixed bottom-centre testimonial pill ("Endless Tools great tool for designers by designers.").', sel: 'fixed bottom card' }, { noScroll: true });
  const n = G.news;
  await S('news-title', q('h2, h1').filter({ hasText: /Stay in the loop/i }).filter({ visible: true }).first(), ['default'], { group: n, title: 'Newsletter heading', desc: 'The "Stay in the loop" heading.', sel: '"Stay in the loop"' });
  await S('news-field', q('input[type="text"], input[placeholder*="email" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: n, title: 'Newsletter field', desc: 'The "Your email" input; sample text was typed and deleted, nothing sent.', sel: 'newsletter email field' });
  await S('news-consent', q('label[aria-invalid]').filter({ visible: true }).first(), ['default', 'selected'], { group: n, title: 'Consent checkbox', desc: 'The "I agree to the Privacy Policy" checkbox (peer-checked swaps its fill white); checked as a local toggle — the form was never submitted.', sel: 'label[aria-invalid] consent box' });
  await S('news-submit', q('button[type="submit"], button').filter({ hasText: /Stay updated/i }).filter({ visible: true }).first(), B4, { group: n, title: 'Newsletter submit', desc: 'The "Stay updated" submit; measured, never pressed (a press would subscribe).', sel: '"Stay updated"' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: f, title: 'Footer', desc: 'The page footer: social links, legal links, contact mailto and the ©EndlessTools line.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /Privacy policy|Terms of use/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A legal link in the footer.', sel: 'footer a' });
  await S('social-link', q('footer a').filter({ hasText: /Instagram|Linked In|TikTok/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Social link', desc: 'A social link in the footer Get-in-touch block; measured never followed.', sel: 'footer social a' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.auth;
  // markPainted returns the __none__ locator on a miss (S records it missing), never null.
  const card = await markPainted('input, h1', 'm-login', { minW: 250, minH: 200 });
  await S('login-card', card, ['default'], { group: g, title: 'Login card', desc: 'The centred 450px login card: a 5%-white fill at a 20px radius on the #0a0a0a field; never filled or submitted.', sel: 'login card' });
  await S('login-logo', q('svg').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login logo', desc: 'The dot-grid Endless Tools mark above the card title (inline SVG, currentColor).', sel: 'login svg mark' });
  await S('login-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login title', desc: '"Welcome to Endless Tools!" plus the sign-in-or-create lede.', sel: 'login h1' });
  await S('login-field', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input (secondary fill, grey-2 border); sample text was typed and deleted, nothing sent.', sel: 'input[type=email]' });
  await S('send-code', q('button').filter({ hasText: /Send Code/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Send Code button', desc: 'The Send-Code submit (white fill); measured, never pressed (a press would send a login code).', sel: '"Send Code"' });
  await S('login-switch', q('button').filter({ hasText: /Log in with password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Password switch', desc: 'The "Log in with password" ghost button that swaps the OTP form for the password form; toggled for the password-field reading.', sel: '"Log in with password"' });
  try {
    const sw = q('button').filter({ hasText: /Log in with password/i }).filter({ visible: true }).first();
    if (await sw.count()) { await sw.click({ timeout: 5000 }).catch(() => sw.evaluate((el) => el.click())); await page.waitForTimeout(1200); }
  } catch (e) { log('  ! password switch failed', String(e.message).split('\n')[0]); }
  await S('login-password-field', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input on the password form (after the local switch); focused only, never filled or submitted.', sel: 'input[type=password]' });
  await S('login-submit', q('button').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in button', desc: 'The password form\'s Log-in submit; measured, never pressed.', sel: '"Log in" submit' });
  await S('login-forgot', q('a, button').filter({ hasText: /Forgot your password/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot password link', desc: 'The "Forgot your password?" link; measured never followed.', sel: '"Forgot your password?"' });
  // domFind's leaf match lands on the line itself; a hasText filter on bare
  // divs climbs to the page root.
  await S('login-legal', await domFind(page, /By creating an account you agree/i, { sel: 'p, div, span, small' }), ['default'], { group: g, title: 'Legal line', desc: 'The agree-to-terms line with its underlined Terms and Privacy links.', sel: 'login legal line' });
  save();
}

async function legal() {
  if (!(await newPage('privacy', { wait: 8000 }))) return;
  const g = G.legal;
  await S('legal-header', q('div.fixed, header, div.sticky').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal header', desc: 'The fixed top bar on the legal pages: logomark left, Sign-in pill right, over a nav gradient.', sel: 'legal top bar' }, { noScroll: true });
  await S('legal-signin', q('a, button').filter({ hasText: /^\s*Sign in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign in link', desc: 'The Sign-in pill in the legal header; measured never followed.', sel: '"Sign in"' }, { noScroll: true });
  await S('legal-title', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal title', desc: 'The document title ("Privacy Policy").', sel: 'legal h1' });
  await S('legal-content', q('div.et-content, .et-content, main div').filter({ hasText: /privacy notice|Last updated/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal content', desc: 'The document body (the .et-content column): 14px grey-4 text with white emphasis spans.', sel: '.et-content' });
  await S('legal-link', q('a').filter({ hasText: /endlesstools\.io|privacy notice/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Legal link', desc: 'An inline document link (underlined); measured never followed.', sel: 'legal doc a' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('div.nav-gradient, div.sticky').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The sticky bar at 390: logomark plus the white Start-for-free pill (the Log-in link hides at this width).', sel: 'header at 390' }, { noScroll: true });
  await S('m-cta', q('.nav-gradient button, .nav-gradient a').filter({ hasText: /Start for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav CTA', desc: 'The Start-for-free button at 390 (a button, not an anchor, at this width).', sel: '"Start for free" at 390' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The hero at 390: title-secondary size with the same circle/underline marks.', sel: 'h1 at 390' });
  await S('m-asset-card', q(`${SEC}="hero_inputs"] h2`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile asset title', desc: 'An input-source heading in the stacked mobile layout.', sel: 'asset h2 at 390' });
  await S('m-plan-card', q('div.rounded-\\[33px\\]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile plan card', desc: 'A plan card in the horizontally scrolling pricing row at 390.', sel: 'plan card at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
{
  // A page argument that matches no page fails before anything is rewritten:
  // a misspelt one used to run nothing yet stamp _meta.read with today's date.
  const known = ['home', 'login', 'legal', 'privacy', 'mobile'];
  const unknown = process.argv.slice(2).filter((p) => !known.includes(p));
  if (unknown.length) {
    console.error(`unknown page argument(s): ${unknown.join(', ')} — known pages: ${known.join(', ')}`);
    process.exit(1);
  }
}
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every captured surface paints dark only';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const plan = { home, login, legal, mobile };
const pages = process.argv.slice(2).map((p) => (p === 'privacy' ? 'legal' : p));
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) await plan[k]();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'div.nav-gradient');
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
