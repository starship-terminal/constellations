// Measures dona.ai's public components in every state reachable without
// signing in, paying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home about privacy mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// dona.ai is a Gatsby + styled-components site: classes are stable
// `Component__Element-sc-<id>-<n>` names, so specs select by class fragment,
// role or text. Login and Try for free open https://app.dona.ai in a new tab
// — measured, never pressed. The newsletter form is measured and sample-filled
// (deleted again), never submitted: the Join button is never really pressed.
// The "This website uses cookies" banner is measured, then hidden — its
// Accept button is never clicked. Watch video opens the YouTube-embed modal,
// a local UI toggle: measured open, then hidden.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', about: '/about', privacy: '/privacy-policy' };
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
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
          // close it again with the same control so it cannot hold focus or cover the next reading
          undo = async () => { await page.keyboard.press('Escape'); if ((await loc.getAttribute('aria-expanded').catch(() => null)) === 'true' || (await loc.evaluate((el) => !!el.closest('details[open]')).catch(() => false))) await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(400); };
        }
      } else via = via || 'at rest';
      // A focus attempt that never landed is not a focus-visible reading:
      // record the failure instead of publishing a default-state style under
      // the focus-visible name. Builders treat via 'focus failed' as uncaptured.
      if (st === 'focus-visible' && via === 'focus failed') {
        out.components[key].states[st] = { via, error: 'the element did not take keyboard focus — no focus-visible style was measured' };
        log('  !', key, st, 'focus failed — recorded, not measured');
        continue;
      }
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|try for free|join our newsletter|watch video)$/i;
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

const G = {
  shell: 'Shell and navigation', home: 'Home', about: 'About',
  legal: 'Legal pages', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// Marks the cookie-consent banner: the smallest fixed element whose text reads
// "This website uses cookies." (Accept is never clicked — measured only.)
async function markCookies() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div,section,aside')].filter((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return cs.position === 'fixed' && /this website uses cookies/i.test(t) && t.length < 3000 && r.width > 100;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'cookies');
  });
}

// Marks the opened video modal: the fixed pages__Modal overlay the Watch video
// button mounts (a YouTube iframe on a dimmed backdrop).
async function markModal() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('[class*="Modal"]')].filter((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return cs.position === 'fixed' && r.width > 400 && r.height > 300;
    }).sort((a, b) => b.getBoundingClientRect().width - a.getBoundingClientRect().width);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'vmodal');
  });
}

async function hideModal() {
  await page.evaluate(() => {
    document.querySelectorAll('[class*="Modal"]').forEach((x) => {
      if (getComputedStyle(x).position === 'fixed') x.style.setProperty('display', 'none', 'important');
    });
  });
  await page.waitForTimeout(400);
}

async function home() {
  // promo:'none' keeps the cookie banner up for its own readings; it is
  // hidden right after, never answered.
  if (!(await newPage('home', { wait: 10000, promo: 'none' }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await markCookies();
  await S('cookie-banner', q('[data-m-mark="cookies"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Cookie banner', desc: 'The "This website uses cookies." consent notice (Learn more / Accept); measured, then hidden — Accept was never clicked.', sel: 'fixed cookie banner' }, { noScroll: true });
  await S('cookie-learn', q('[data-m-mark="cookies"] a').filter({ hasText: /Learn more/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Cookie "Learn more"', desc: 'The Learn more link inside the cookie banner (to /privacy-policy); measured, never followed.', sel: 'cookie banner a' }, { noScroll: true });
  await S('cookie-accept', q('[data-m-mark="cookies"] button').filter({ hasText: /^\s*Accept\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Cookie accept', desc: 'The banner\'s Accept action; measured, never clicked — no consent was ever posted.', sel: 'cookie banner Accept' }, { noScroll: true });
  await closePromo(page);
  await S('header', q('div[class*="Header__Wrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The top bar: the About button, the centred dona wordmark and the Login action.', sel: 'Header__Wrapper' }, { noScroll: true });
  // The logo anchor is display:block with width 0 — the SVG inside overflows
  // it — so the mark is measured on the SVG itself.
  // The SVG itself is not keyboard-focusable — focus its enclosing anchor so
  // the focus-visible reading is real (the crop stays on the SVG).
  await S('logo', q('a[class*="Header__LogoLink"] svg').filter({ visible: true }).first(), B4, { group: g, title: 'Logo', desc: 'The centred dona logo (ring mark + wordmark), inside an anchor to / whose own box is 0 wide.', sel: 'Header__LogoLink svg' }, { noScroll: true, focusLoc: q('a[class*="Header__LogoLink"]').first() });
  await S('nav-about', q('div[class*="Header__Wrapper"] button').filter({ hasText: /^\s*About\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'About button', desc: 'The header About action (routes to /about).', sel: 'header button About' }, { noScroll: true });
  await S('nav-login', q('div[class*="Header__Wrapper"] button').filter({ hasText: /^\s*Login\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Login button', desc: 'The header Login action — opens https://app.dona.ai in a new tab; measured, never pressed.', sel: 'header button Login' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "A more humane / to-do list" display — the first line paints muted, the second ink.', sel: 'h1' }, { noScroll: true });
  await S('hero-lede', q('p[class*="Hero__Text"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero lede', desc: 'The "back to basic to-do list" paragraph under the headline.', sel: 'Hero__Text' });
  await S('watch-video', q('button').filter({ hasText: /^\s*Watch video\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Watch video button', desc: 'The secondary pill with the play-triangle icon; opens the video modal.', sel: 'button Watch video' });
  await S('try-cta', q('button').filter({ hasText: /Try for free/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Try for free button', desc: 'The blue primary pill — opens https://app.dona.ai in a new tab; measured, never pressed.', sel: 'button Try for free' });
  await S('hero-video', q('div[class*="pages__Screen"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero app frame', desc: 'The autoplay product video under the CTAs (the Dona task UI in a rounded frame).', sel: 'pages__Screen' });
  await S('section-h2', q('h2').filter({ hasText: /Fast & delightful/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'The "Fast & delightful user experience" section title.', sel: 'h2 Fast & delightful' });
  await S('section-h3', q('h3').filter({ hasText: /Light, dark & black|Details matter/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature heading', desc: 'A feature tile\'s h3 ("Light, dark & black UI theme" / "Details matter").', sel: 'h3' });
  await S('section-para', q('p[class*="pages__Paragraph"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature paragraph', desc: 'A feature tile\'s body copy.', sel: 'pages__Paragraph' });
  await S('feature-tile', q('div[class*="pages__GridHalf"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature tile', desc: 'A half-width feature tile (headline + autoplay video).', sel: 'pages__GridHalf' });
  await S('newsletter', q('form[class*="Newsletter__Wrapper"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Newsletter form', desc: 'The email capture: the "Enter your email" field plus the "Join our newsletter" submit with the arrow-circle icon; measured, never submitted.', sel: 'Newsletter__Wrapper form' });
  await S('email-input', q('input[placeholder="Enter your email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Email field', desc: 'The newsletter email input; focused and given sample text that was deleted again — the form was never submitted.', sel: 'input[placeholder="Enter your email"]' });
  await S('join-btn', q('button[type="submit"]').filter({ hasText: /Join our newsletter/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Newsletter submit', desc: 'The "Join our newsletter" submit button; measured — pressed state forced via DevTools, the button itself was never really pressed.', sel: 'button Join our newsletter' });
  // The video modal: open it with the Watch video toggle, measure it and its
  // close button, then hide it for the rest of the run.
  try {
    const t = q('button').filter({ hasText: /^\s*Watch video\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await page.waitForTimeout(2500); }
  } catch (e) { log('  ! video modal open failed', String(e.message).split('\n')[0]); }
  await markModal();
  await S('video-modal', q('[data-m-mark="vmodal"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Video modal', desc: 'The fixed overlay the Watch video button mounts: a YouTube iframe ("Say hello to Dona") on a dimmed page with a close button.', sel: 'pages__Modal' }, { noScroll: true, noReset: true });
  // Reset between states: without it the pointer stays on the button after the
  // hover reading and the focus state is measured with the hover fill. The
  // reset only blurs and parks the pointer in the corner — it cannot close the
  // modal.
  await S('modal-close', q('[data-m-mark="vmodal"] button, [data-m-mark="vmodal"] [role="button"], [class*="Modal"] svg').filter({ visible: true }).first(), B4, { group: h, title: 'Modal close', desc: 'The close (x) control on the video modal.', sel: 'modal close' }, { noScroll: true });
  await hideModal();
  save();
}

async function about() {
  if (!(await newPage('about', { wait: 9000 }))) return;
  await sheetsFor('about');
  await chrome('about');
  const g = G.about;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About headline', desc: 'The "We’re building / to-do list you’ll enjoy using" display — muted first line, ink continuation.', sel: 'h1' }, { noScroll: true });
  await S('mission-text', q('p[class*="Hero__Text"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mission text', desc: 'The mission paragraph; its second sentence paints muted (a span inside the paragraph).', sel: 'Hero__Text' });
  await S('team-h2', q('h2').filter({ hasText: /^\s*Team\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Team heading', desc: 'The "Team" section title.', sel: 'h2 Team' });
  await S('team-card', q('div[class*="about__Box"]').filter({ visible: true }).first(), B4, { group: g, title: 'Team card', desc: 'A team-member card: photo, name, one-line bio and social links (Jakub Antalik / Aaron Iker / Nisarg Patel).', sel: 'about__Box' });
  await S('team-avatar', q('img[class*="about__Avatar"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Team avatar', desc: 'A member photo inside the team card.', sel: 'about__Avatar img' });
  await S('social-link', q('a[class*="about__Social"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link inside a team card (twitter / dribbble glyphs); measured, never followed.', sel: 'about__Social a' });
  save();
}

async function privacy() {
  if (!(await newPage('privacy', { wait: 8000 }))) return;
  const g = G.legal;
  await S('legal-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal heading', desc: 'The "Privacy / policy" display on /privacy-policy; /terms-of-service is the same layout.', sel: 'h1' }, { noScroll: true });
  await S('legal-text', q('p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal paragraph', desc: 'A body paragraph of the legal copy.', sel: 'p' });
  await S('legal-h4', q('h4, h3').filter({ hasText: /Cookies|Terms|Disclaimer/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal subheading', desc: 'A section subheading inside the legal copy ("Cookies", "Terms").', sel: 'legal h3/h4' });
  // The legal link must come from the legal copy itself: a bare `div a`
  // reaches past the article and lands on the footer's "Privacy policy" link.
  // Mark the first qualifying in-copy anchor (paragraphs and list items, never
  // inside the footer wrapper); when the copy holds no link the selector below
  // matches nothing and the miss is recorded instead of a footer reading.
  await page.evaluate(() => {
    const footer = document.querySelector('[class*="Footer__Wrapper"]');
    const a = [...document.querySelectorAll('p a, li a')].find((el) =>
      /dona\.ai|contact|privacy/i.test(el.innerText || '') && !(footer && footer.contains(el)));
    if (a) a.setAttribute('data-m-mark', 'legal-link');
  });
  await S('legal-link', q('[data-m-mark="legal-link"]').filter({ visible: true }).first(), B4, { group: g, title: 'Legal link', desc: 'A link inside the legal copy.', sel: 'legal copy a (never the footer)' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('div[class*="Footer__Wrapper"]').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: the copyright line, Terms of Service / Privacy policy links and the @getdona twitter link.', sel: 'Footer__Wrapper' }, { noScroll: true });
  await S('footer-link', q('a[href="/terms-of-service"], a[href="/privacy-policy"]').filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A legal link in the footer.', sel: 'footer a' }, { noScroll: true });
  await S('footer-twitter', q('a[href*="twitter.com/getdona"]').filter({ visible: true }).first(), B4, { group: g, title: 'Twitter link', desc: 'The @getdona icon link in the footer; measured, never followed.', sel: 'footer twitter a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', promo: 'none' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await markCookies();
  // A marked node outside the 390 x 844 viewport is not the banner as painted (the 2026-11-12 run
  // read a 555x64 bar at top:1138px and its crop caught body text): record it missing instead.
  const cookieMark = q('[data-m-mark="cookies"]').filter({ visible: true }).first();
  const cookieInView = await cookieMark.evaluate((el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.top >= 0 && r.bottom <= innerHeight && r.right <= innerWidth; }).catch(() => false);
  if (!cookieInView) { log('  ! m-cookie-banner: the marked node is outside the viewport; recorded missing'); delete out.components['m-cookie-banner']; }
  await S('m-cookie-banner', cookieInView ? cookieMark : q('[data-m-none="m-cookie-banner"]'), ['default'], { group: g, title: 'Cookie banner (mobile)', desc: 'The consent notice at 390 wide; hidden after its own reading, never answered. Recorded missing when the marked node lies outside the viewport.', sel: 'fixed cookie banner at 390' }, { noScroll: true });
  await closePromo(page);
  await S('m-header', q('div[class*="Header__Wrapper"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'Header__Wrapper at 390' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  await S('m-watch', q('button').filter({ hasText: /^\s*Watch video\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile Watch video', sel: 'Watch video at 390' });
  await S('m-try', q('button').filter({ hasText: /Try for free/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile Try for free', sel: 'Try for free at 390' });
  await S('m-email-input', q('input[placeholder="Enter your email"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile email field', sel: 'newsletter input at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints one light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, about, privacy, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a header
  // button), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'div[class*="Header__Wrapper"] button');
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
