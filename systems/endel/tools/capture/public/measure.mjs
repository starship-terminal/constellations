// Measures endel.io's and app.endel.io's public components in every state
// reachable without signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home focus app-explore app-player app-login mobile (the footer group
// also runs on home). Writes raw/components-computed.json (merged) and one
// crop per component and state into components/crops/; raw/measurements.md is
// built by build-measurements.mjs.
//
// endel.io is a Next.js site in one dark theme; component classes are CSS
// modules (<Component>-module__<hash>__<slot>) so the stable part is the
// module prefix — selectors key off it, roles, landmarks and text. The
// signed-out web app (app.endel.io) ships the same system plus accent greens.
// Nothing is sent, downloaded or signed into: the only presses are local UI
// toggles — the More flyout, the FAQ accordion, the mobile menu and the
// player's Set Timer dialog — each closed again without submitting.
// "Try Today", "Sign In", "Subscribe", "Continue", "Unlock" and every
// outbound link are measured in all states except followed or pressed for
// real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: BASE + '/', focus: BASE + '/focus',
  'app-explore': APP + '/', 'app-player': APP + '/player/focus', 'app-login': APP + '/',
};
let page, cdp, current, view, context, run;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these — a blocked mobile visit
// must not erase evidence the desktop visit of the same route kept.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
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
  const cleared = await open(page, URLS[key], { wait });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  opened.add(key + '|' + view);
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
  // The page's own address at measure time (query and hash dropped): the
  // sign-in components are read on /login after an in-app navigation, not on
  // the app-login entry URL.
  const here = (page && page.url() && page.url() !== 'about:blank') ? page.url().split(/[?#]/)[0] : URLS[current];
  Object.assign(c, { page: current, view, run, url: here }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
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
        // A click at the centre of a range input sets its value (the volume
        // slider would jump to 50%): sliders take DOM focus only, text fields
        // still get the real click that puts a caret in them.
        const isRange = await fld.evaluate((el) => el.matches('input[type="range"], [role="slider"], [role="spinbutton"]')).catch(() => false);
        if (isRange) {
          await fld.evaluate((el) => el.focus());
          await page.waitForTimeout(400);
          via = 'DOM focus (no click: it would set the slider value)';
        } else {
          await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
          await page.waitForTimeout(400);
          via = 'clicked into the field';
        }
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

// Clicks a UI toggle (nav menu, mobile menu, accordion). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request|try today|try now|unlock|upgrade|gift|donate)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const mod = (name) => `[class*="${name}-module"]`;
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
  shell: 'Shell and navigation', marketing: 'Marketing sections',
  app: 'Web app (signed out)', player: 'Player', login: 'Sign-in card',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// Scrolls down in steps until fn() (run in-page) reports it found and marked
// its element, or the document ends.
async function scrollFind(fn) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y <= h; y += 550) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await page.waitForTimeout(320);
    if (await page.evaluate(fn)) return true;
  }
  await page.evaluate(() => scrollTo(0, 0));
  return false;
}

// The marketing header's own controls: the More flyout is a local toggle and
// its links never navigate anywhere but public pages — still never followed.
const openMore = async () => {
  const b = q(mod('MenuButton')).first();
  if (!(await b.count())) return false;
  await toggle(b);
  await page.waitForTimeout(1400);
  return true;
};

async function home() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header').first(), ['default'], { group: g, title: 'Header', desc: 'The fixed dark bar: the Endel mark, the nav links (ADHD, Sleep, Focus, Relax, Activity), the More flyout, Try Today and Sign In.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a').first(), ['default'], { group: g, title: 'Logo', desc: 'The 40x40 Endel mark, a link home.', sel: 'header a:first' }, { noScroll: true });
  const navA = (t) => q('header a').filter({ hasText: t }).first();
  await S('nav-link', navA(/^Focus$/), B4, { group: g, title: 'Nav link', sel: 'header a:has-text("Focus")' }, { noScroll: true });
  await S('nav-more', q(mod('MenuButton')).first(), B4, { group: g, title: 'More button', desc: 'The nav overflow toggle; its press opens the flyout inside the header.', sel: 'MenuButton-module button' }, { noScroll: true });
  const btnB = () => q(`header ${mod('Button')}`);
  await S('btn-try', btnB().filter({ hasText: /Try Today/ }).first(), B4, { group: g, title: 'Try Today button', desc: 'The primary header CTA. Measured, never followed.', sel: 'header Button-module button:has-text("Try Today")' }, { noScroll: true });
  await S('btn-signin', btnB().filter({ hasText: /Sign In/ }).first(), B4, { group: g, title: 'Sign In button', desc: 'The header auth link. Measured, never followed.', sel: 'header Button-module button:has-text("Sign In")' }, { noScroll: true });
  // The flyout: press More, then read a link that only exists while it is open.
  const flyout = await openMore();
  if (flyout) {
    const fly = q('header a').filter({ hasText: /^Manifesto$/ }).first();
    // count() is a Promise (always truthy): await it, or the fallback never runs.
    await S('menu-flyout', (await fly.count()) ? fly : q('header').first(), ['default'], { group: g, title: 'More flyout', desc: 'The expanded nav groups inside the header after More is pressed (Company, Technology, the store links). Read while held open.', sel: 'header a:has-text("Manifesto") while the flyout is open' }, { noScroll: true });
    await S('nav-more-open', q(mod('MenuButton')).first(), ['opened'], { group: g, title: 'More button, open', desc: 'The trigger after its own toggle; the open flyout shows in the crop.', sel: 'MenuButton-module button, open' }, { noScroll: true, cropLoc: q('header'), noToggle: true });
    await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  }
  const m = G.marketing;
  await S('hero-title', q('h1').first(), ['default'], { group: m, title: 'Hero title', desc: 'The "Endel" display wordmark at the top of the home page.', sel: 'h1' }, { noScroll: true });
  await S('page-ground', q('body'), ['default'], { group: m, title: 'Page ground', desc: 'The near-black every page paints on.', sel: 'body' }, { noScroll: true, crop: false });
  const h2ok = await scrollFind(() => {
    const h = [...document.querySelectorAll('h2')].find((n) => (n.innerText || '').trim().length > 3 && n.getBoundingClientRect().height > 0);
    if (!h) return false;
    h.setAttribute('data-m-h2', '1');
    return true;
  });
  await S('section-title', h2ok ? q('[data-m-h2="1"]') : q('[data-m-h2="__none__"]'), ['default'], { group: m, title: 'Section title', sel: 'first visible h2, marked where it mounts' });
  // Both alternatives must be scoped to `main`: an unscoped Text-module
  // fallback matches the header's nav links (they share the module) and the
  // "paragraph" reading lands on navigation instead of body copy.
  await S('body-text', await domFind(page, /\S/, { sel: 'main p, main [class*="Text-module"]', tag: 'btxt', minW: 60, minH: 14 }), ['default'], { group: m, title: 'Body text', sel: 'first visible marketing paragraph' });
  await S('learn-more', q('main a').filter({ hasText: /Learn More/ }).first(), B4, { group: m, title: 'Learn More link', sel: 'main a:has-text("Learn More")' });
  await S('try-now', q('main a').filter({ hasText: /Try Now/ }).first(), B4, { group: m, title: 'Try Now link', sel: 'main a:has-text("Try Now")' });
  // The 72px round button in the device sections is a media play control:
  // measured, never pressed for real (audio).
  const play = q(`main ${mod('Button')}[class*="border-radius-full"]`).filter({ hasText: /^$/ }).first();
  await S('play-button', play, B4, { group: m, title: 'Round media button', desc: 'The 72x72 circular play control over the product imagery. Measured, never pressed.', sel: 'Button-module button[class*="border-radius-full"] (72px, icon only)' });
  await S('show-more', q('main button').filter({ hasText: /^Show More$/ }).first(), B4, { group: m, title: 'Show More button', desc: 'Loads more press quotes into the reviews waterfall; a local toggle, never pressed for real beyond states.', sel: 'main button:has-text("Show More")' });
  const acc = q(mod('AccordionTitle')).first();
  await S('accordion-title', acc, [...B4, 'opened'], { group: m, title: 'FAQ accordion item', desc: 'A question row in the FAQ; its own press expands the answer. Opened once for the reading.', sel: 'AccordionTitle-module button' });
  await S('accordion-content', q(mod('AccordionContent')).first(), ['opened'], { group: m, title: 'FAQ answer', desc: 'The answer panel under the open question.', sel: 'AccordionContent-module wrap' }, { noToggle: true });
  const mail = q('main input[type="email"], main input').first();
  await S('input-email', mail, ['default', 'focused', 'filled'], { group: m, title: 'Newsletter email field', desc: 'The newsletter signup input. Text was typed and deleted again; nothing was submitted.', sel: 'main input' });
  await S('btn-subscribe', q('main button').filter({ hasText: /^Subscribe$/ }).first(), B4, { group: m, title: 'Subscribe button', desc: 'Submits the newsletter form. Measured in all states, never pressed for real.', sel: 'main button:has-text("Subscribe")' });
  await S('press-logo', q(`${mod('PressWall')} a, main a:has(img)`).first(), B4, { group: m, title: 'Press logo', desc: 'An outlet logo tile in the press wall. Measured, never followed.', sel: 'PressWall-module a' });
  save();
}

async function focus() {
  if (!(await newPage('focus', { wait: 8000 }))) return;
  const m = G.marketing;
  await S('page-title', q('h1').first(), ['default'], { group: m, title: 'Page title', desc: 'The product page h1 ("Find your focus with Endel").', sel: 'h1' }, { noScroll: true });
  await S('soundscape-card', q('a[class*="Card-module"]').first(), B4, { group: m, title: 'Soundscape card', desc: 'A 270x270 soundscape tile linking its page (cover art, title, Try Now). Measured, never followed.', sel: 'a[class*="Card-module"]' });
  await S('scenario-card', q('a[class*="Card-module"]').nth(4), ['default'], { group: m, title: 'Scenario card', desc: 'A scenario tile from the Timed Scenarios band (same Card module, second row).', sel: 'a[class*="Card-module"] (timed scenarios row)' });
  save();
}

async function appExplore() {
  if (!(await newPage('app-explore', { wait: 9000 }))) return;
  await sheetsFor('app-explore');
  const g = G.app;
  await S('app-header', q('header').first(), ['default'], { group: g, title: 'App header', desc: 'The signed-out web app bar: the FREEMIUM account chip and Sign In.', sel: 'app header' }, { noScroll: true });
  await S('user-button', q(mod('UserButton')).first(), B4, { group: g, title: 'FREEMIUM chip', desc: 'The account state button; opens the account sheet. Measured, never opened (it gates on sign-in).', sel: 'UserButton-module button' }, { noScroll: true });
  await S('app-btn-signin', q(`header ${mod('Button')}`).filter({ hasText: /Sign In/ }).first(), B4, { group: g, title: 'Sign In button (app)', sel: 'app header button:has-text("Sign In")' }, { noScroll: true });
  await S('banner', q('a[class*="Banner-module"]').first(), B4, { group: g, title: 'Carousel banner', desc: 'A promo card in the explore carousel (SPECIAL OFFER, product updates). Measured, never followed.', sel: 'a[class*="Banner-module"]' });
  await S('banner-dot', q(mod('BannerCarousel') + ' button').first(), ['default'], { group: g, title: 'Carousel dot', desc: 'The selected pager dot under the banner carousel.', sel: 'BannerCarousel-module dot button' });
  await S('scenario-pill', q(mod('Button')).filter({ hasText: /^Focus Timer$/ }).first(), B4, { group: g, title: 'Scenario pill', desc: 'A rounded-full scenario tag in the explore grid (Focus Timer, ASMR, Meditate…). Selecting one gates on premium; never pressed for real.', sel: 'app Button-module pill:has-text("Focus Timer")' });
  await S('soundscape-row', q(mod('SoundscapeItem')).first(), B4, { group: g, title: 'Soundscape row', desc: 'A list row that opens a soundscape in the player (Focus, Colored Noises…). Measured; its destination is the public player.', sel: 'SoundscapeItem-module button' });
  await S('mini-player', q(mod('MiniPlayer')).first(), ['default'], { group: g, title: 'Mini player', desc: 'The fixed bottom bar with the paused soundscape and transport. Audio was never started.', sel: 'MiniPlayer-module wrap' });
  save();
}

async function appPlayer() {
  if (!(await newPage('app-player', { wait: 9000 }))) return;
  const g = G.player;
  await S('player-header', q('header').first(), ['default'], { group: g, title: 'Player header', desc: 'The soundscape title bar over the visualizer (name + live energy state).', sel: 'player header' }, { noScroll: true });
  await S('player-title', q('header h1').first(), ['default'], { group: g, title: 'Soundscape title', sel: 'player header h1' }, { noScroll: true });
  await S('btn-close-player', q(`header ${mod('Button')}`).first(), B4, { group: g, title: 'Close button', desc: 'The icon button that leaves the player for Explore. Measured, never pressed.', sel: 'player header Button-module icon button' }, { noScroll: true });
  await S('btn-set-timer', q('footer button').filter({ hasText: /Set Timer/ }).first(), B4, { group: g, title: 'Set Timer button', desc: 'Opens the shut-off timer dialog. Pressed once to read the dialog, closed again.', sel: 'player footer button:has-text("Set Timer")' });
  await S('button-mode', q(`${mod('ButtonMode')}:not([class*="is-active"])`).first(), B4, { group: g, title: 'Mode button', desc: 'One of the energy-mode icon buttons under the visualizer.', sel: 'ButtonMode-module button' });
  await S('button-mode-active', q(`${mod('ButtonMode')}[class*="is-active"]`).first(), ['default'], { group: g, title: 'Mode button, active', desc: 'The engaged mode icon.', sel: 'ButtonMode-module button.is-active' });
  // Transport row: the round 56px buttons left of the volume control.
  await S('player-control', q(`footer ${mod('Button')}[class*="border-radius-full"]`).filter({ hasText: /^$/ }).nth(1), B4, { group: g, title: 'Transport button', desc: 'A round transport control (play/skip). Audio was never started.', sel: 'player footer round icon button' });
  await S('volume', q('input[class*="InputRange-module"], input[type="range"]').first(), ['default', 'focused'], { group: g, title: 'Volume slider', desc: 'The range control at the transport row\'s right end. Never dragged.', sel: 'input[class*="InputRange-module"], input[type="range"]' });
  await S('btn-explore', q(mod('ExploreButton')).first(), B4, { group: g, title: 'Explore button', desc: 'The back-to-explore pill in the player footer. Measured, never followed.', sel: 'ExploreButton-module button' });
  // The timer dialog: press Set Timer, read the sheet, close it again.
  const st = q('footer button').filter({ hasText: /Set Timer/ }).first();
  if (await st.count()) {
    await toggle(st);
    await page.waitForTimeout(1400);
    const form = q(mod('TimerForm'));
    await S('timer-dialog', form, ['opened'], { group: g, title: 'Shut-off timer dialog', desc: 'The bottom sheet Set Timer opens: duration chips, the premium Unlock and Done rows. Unlock was measured, never pressed.', sel: 'TimerForm-module wrap' }, { noToggle: true });
    await S('btn-unlock', q(`${mod('TimerForm')} button`).filter({ hasText: /Unlock/ }).first(), ['opened'], { group: g, title: 'Unlock button', desc: 'The premium upsell inside the timer dialog. Measured, never pressed (it starts checkout).', sel: 'TimerForm-module button:has-text("Unlock")' }, { noToggle: true });
    await page.keyboard.press('Escape'); await page.waitForTimeout(700);
    const open = await page.evaluate(() => !!document.querySelector('[class*="TimerForm-module"]'));
    if (open) { const d = q('button').filter({ hasText: /^Done$/ }).first(); if (await d.count()) await toggle(d); await page.waitForTimeout(700); }
  }
  save();
}

async function appLogin() {
  if (!(await newPage('app-login', { wait: 8000 }))) return;
  const g = G.login;
  // app.endel.io/login redirects to the explore page on a fresh load: the
  // sign-in card only mounts through the app's own Sign In button — in-app
  // navigation to a public auth page; nothing is entered or sent.
  await q('header button').filter({ hasText: /Sign In/ }).first().click({ timeout: 8000 }).catch(() => {});
  await page.waitForURL('**/login**', { timeout: 15000 }).catch(() => {});
  await page.waitForTimeout(2200);
  // The sign-in card: climb from the heading to the first ancestor that paints
  // a fill or border at card size. `innerText` matches containers too (a div
  // whose descendants hold the heading text), so the match pool is reduced to
  // leaves — an element that contains another match is a wrapper, not the
  // heading; without it the climb starts at `main` and the "card" reading is
  // the whole page.
  const marked = await page.evaluate(() => {
    const els = [...document.querySelectorAll('h1,h2,h3,div,p')].filter((n) => /sign in or register/i.test((n.innerText || '').trim()));
    const h = els.find((n) => !els.some((o) => o !== n && n.contains(o)));
    if (!h) return false;
    let card = null;
    let fit = null;
    for (let n = h, i = 0; n && i < 10; i++, n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 1000 || r.height > 820) break;
      fit = n;
      const c = getComputedStyle(n);
      if (r.width >= 280 && r.height >= 200 && (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || c.boxShadow !== 'none' || parseFloat(c.borderTopWidth) > 0)) card = n;
    }
    // The card paints nothing itself (a transparent column on the black
    // page), so the fallback is the widest ancestor still at card size, not
    // the heading's own wrapper.
    (card || fit || h.parentElement || h).setAttribute('data-m-card', '1');
    return true;
  });
  // The field's placeholder is the product's example address. Hide it so the
  // crop does not look filled. Nothing is typed.
  await page.addStyleTag({ content: 'input::placeholder{color:transparent!important}' }).catch(() => {});
  await S('login-card', marked ? q('[data-m-card="1"]') : q('[data-m-card="__none__"]'), ['default'], { group: g, title: 'Sign-in card', desc: 'The "Sign In or Register" panel: an empty email field, Continue, and three icon-only identity-provider buttons (Google, Apple, Facebook). Nothing was typed or submitted. The provider buttons were not clicked.', sel: 'card ancestor of the sign-in heading (marked in-page)' });
  await S('input-email-login', q('input[type="email"], input[name="email"], input').first(), ['default', 'focused'], { group: g, title: 'Email field (sign-in)', desc: 'Read default and focused; no address was ever typed on this page.', sel: 'login input' });
  await S('btn-continue', q('button').filter({ hasText: /^Continue$/ }).first(), B4, { group: g, title: 'Continue button', desc: 'Submits the sign-in form. Measured in all states, never pressed for real.', sel: 'login button:has-text("Continue")' });
  await S('btn-oauth', q('button').filter({ has: q('svg') }).filter({ hasText: /^$/ }).first(), B4, { group: g, title: 'Identity-provider button', desc: 'The Google icon button on the sign-in card. Apple and Facebook sit beside it. Measured, never pressed.', sel: 'login icon button' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep another page's
  // readings under the wrong url.
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer', q('footer').first(), ['default'], { group: g, title: 'Footer', desc: 'The big footer: Explore and product link columns, stores, legal and socials.', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q('footer a[href*="instagram" i], footer a[href*="twitter" i], footer a[href*="x.com" i], footer a[href*="discord" i], footer a[href*="facebook" i]').first(), B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
    await S('footer-legal', q('footer a').filter({ hasText: /privacy|terms|impressum|imprint/i }).first(), B4, { group: g, title: 'Legal link', sel: 'footer a:has-text("Privacy")' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 9000 }))) return;
  const g = G.mobile;
  await S('m-header', q('header').first(), ['default'], { group: g, title: 'Mobile header', desc: 'The 56px bar: mark, Try Today and the Menu trigger.', sel: 'header' }, { noScroll: true });
  const menuBtn = q('header button').filter({ hasText: /^Menu$/ }).first();
  await S('m-menu-button', menuBtn, [...B4, 'opened'], { group: g, title: 'Menu button', desc: 'Opens the full-screen nav inside the header; pressed once for the open reading, closed again.', sel: 'header button:has-text("Menu")' }, { noScroll: true });
  const openLink = q('header a').filter({ hasText: /Endel for Students/ }).first();
  if (await openLink.count()) {
    await S('m-menu-flyout', openLink, ['default'], { group: g, title: 'Mobile menu, open', desc: 'A promo row in the open menu (students / teams / gift cards). Read while held open.', sel: 'header a while menu is open' }, { noScroll: true });
  }
  await page.keyboard.press('Escape'); await page.waitForTimeout(600);
  await S('m-hero-title', q('h1').first(), ['default'], { group: g, title: 'Hero title (mobile)', sel: 'h1' }, { noScroll: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), dark theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, focus, 'app-explore': appExplore, 'app-player': appPlayer, 'app-login': appLogin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune only components whose page+viewport visit actually opened this
    // run: a blocked route (or a blocked mobile pass of a route the desktop
    // pass captured) keeps its earlier readings. Components saved before the
    // view field existed fall back to the m- prefix for their variant.
    if (!touched.has(key) && !pages.length) {
      const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
      if (opened.has(c.page + '|' + cview)) delete out.components[key];
      continue;
    }
    if (!touched.has(key)) continue;
    // States a spec no longer lists are pruned on every run once the
    // component's page visit finished (the old `&& pages.length` pruned them
    // only on subset runs, so full runs kept stale states forever).
    const want = listed.get(key);
    const cview = c.view || (key.startsWith('m-') ? 'mobile' : 'desktop');
    if (want && opened.has(c.page + '|' + cview)) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
