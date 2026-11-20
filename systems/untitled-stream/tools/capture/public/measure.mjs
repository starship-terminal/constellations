// Measures untitled.stream's public marketing components in every state
// reachable without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing trust login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// States: hover, focus-visible, pressed (CDP forcePseudoState), open (a
// resting state via a UI toggle).
// Nothing is sent, bought or signed into: the consent card is HIDDEN, never
// clicked — its buttons POST a Remix action to /settings/cookies, which
// Cloudflare 403s headless and the router's error boundary then replaces the
// whole page with "Something went wrong". The Yearly/Monthly toggle is a
// client-side state switch; the sign-in buttons are measured at rest only.
// /terms, /privacy and /cookie-policy stay inside Cloudflare's waiting room
// headless and are documented as blocked, not measured.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, closePromo, killGeo, domClick, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  pricing: '/pricing',
  trust: '/trust',
  login: '/login',
};
let page, cdp, current, browser, context, contextMobile, ctx, run;
const touched = new Set();

// The Cloudflare waiting room and the Remix error boundary both render a
// minimal page: detect either so a blocked load is skipped, not measured.
async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /something went wrong|performing security verification|verifying you are human|just a moment/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

// ---------- helpers ----------

// Closes the per-page context: a bare page.close() leaves the context (and so
// the command) alive.
async function closeCtx() {
  if (ctx) await ctx.close().catch(() => {});
  ctx = null;
  page = null;
  cdp = null;
}

async function newPage(key, { mobile = false, promo = 'close', wait = 6000 } = {}) {
  current = key;
  // A fresh context per page: Cloudflare is measurably more willing to clear
  // a first-party path on a clean session than after several navigations.
  const b = context.browser();
  ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  // bot check: Cloudflare's challenge is recorded as a boundary, not bypassed (no navigator.webdriver mask).
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  page.setDefaultTimeout(8000);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  // Retry transient Cloudflare stalls / Remix error cards.
  let cleared = false;
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      cleared = await open(page, URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { wait, promo });
    } catch (e) {
      cleared = false;
      log('  open failed', String(e.message).split('\n')[0]);
    }
    if (cleared && !(await blocked())) break;
    log('  blocked pass', attempt + 1, '- reloading');
  }
  if (!cleared || await blocked()) { log('  BLOCKED', key); return false; }
  if (promo === 'close') await killGeo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return true;
}

// Tags the first element matching `sel` whose text matches reText AND that a
// reader can actually see: Playwright's `visible` ignores opacity, so an
// opacity:0 duplicate (the hidden Learn more copy) or an element under a
// transparent parent wins the first match otherwise. Multiplies opacity up
// the ancestor chain. Retries a few times: the pill bar reveals itself through
// an opacity transition, so a match read mid-reveal is retried until settled.
async function opaqueText(reText, { sel = 'button, a', tag = 'op', tries = 4 } = {}) {
  for (let i = 0; i < tries; i++) {
    const ok = await page.evaluate(
      ([src, flags, s, t]) => {
        const re = new RegExp(src, flags);
        document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
        const els = [...document.querySelectorAll(s)].filter((n) => {
          const r = n.getBoundingClientRect();
          if (!(r.width > 0 && r.height > 0)) return false;
          if (getComputedStyle(n).visibility === 'hidden') return false;
          for (let m = n; m; m = m.parentElement) if (parseFloat(getComputedStyle(m).opacity) < 0.5) return false;
          return re.test((n.innerText || n.getAttribute('aria-label') || '').trim());
        });
        if (!els[0]) return false;
        els[0].setAttribute('data-m-mark', t);
        return true;
      },
      [reText.source, reText.flags, sel, tag],
    );
    if (ok) return page.locator(`[data-m-mark="${tag}"]`);
    await page.waitForTimeout(900);
  }
  return page.locator('[data-m-mark="__none__"]');
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

// Clicks a UI toggle (accordion, menu, drawer). Refuses a submit button and any
// control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign in|log in|create|buy|checkout|pay|purchase|subscribe|share|start free trial|upgrade|open|continue with|accept all|reject all|customize)$/i;
async function toggle(loc) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || t.tag === 'A') throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// Records the listed states of one component. meta: title, group, desc, sel.
// When the selector misses but earlier states exist, those states stay — and
// the entry keeps the run timestamp they were measured under, with the miss
// recorded as recaptureMissed instead of re-dating stale readings.
async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
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

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FILL = 'name@example.com';

// Transitions and animations declared in every readable sheet, by selector.
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
// ---------- page runs ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  trust: 'Trust and security', overlay: 'Dialogs and overlays',
  signin: 'Sign-in boundary', mobile: 'Mobile (390 wide)',
};

async function home() {
  // promo 'keep': the consent card is measured first, then hidden (never
  // clicked — the buttons POST a Remix action that 403s into an error page).
  if (!(await newPage('home', { promo: 'keep' }))) { await closeCtx(); return; }
  await sheetsFor('home');
  const g = G.shell;

  // Consent card first — it covers the bottom-left corner until hidden.
  const card = await domFind(page, /we value privacy/i, { sel: 'div, section, aside, [role="dialog"]', tag: 'cc', leaf: false, minW: 250, minH: 100 });
  await S('consent-card', card, ['default'], { group: G.overlay, title: 'Cookie consent card', desc: 'The "We value privacy" card, fixed bottom-left on first load (frosted surface). Its Customize / Reject all / Accept all buttons were measured but never pressed: the consent form posts a Remix action to /settings/cookies, which Cloudflare 403s headless, replacing the page with the router error boundary.', sel: 'consent card' });
  await S('consent-accept', q('button:has-text("Accept all")').filter({ visible: true }).first(), ['default', 'hover'], { group: G.overlay, title: 'Accept all button', desc: 'The solid white pill in the consent card. Not pressed.', sel: 'button Accept all' });
  await S('consent-reject', q('button:has-text("Reject all")').filter({ visible: true }).first(), ['default', 'hover'], { group: G.overlay, title: 'Reject all button', desc: 'The bg-white/5 ghost pill beside Accept all. Not pressed.', sel: 'button Reject all' });
  await S('consent-customize', q('button:has-text("Customize")').filter({ visible: true }).first(), ['default', 'hover'], { group: G.overlay, title: 'Customize link', desc: 'The text-only option in the consent card. Not pressed.', sel: 'button Customize' });
  await closePromo(page);
  await page.waitForTimeout(400);

  const hdr = q('div.flex.w-full.flex-col').filter({ visible: true }).first();
  await S('header', hdr, ['default'], { group: g, title: 'Header', desc: 'The transparent top band: [untitled] wordmark and the super-title tagline on the left, [membership] text link and the black Enter App pill on the right.', sel: 'header column' }, { noScroll: true });
  // Home's header has no visible wordmark — the h1 is sr-only and the mark
  // only renders on the sub-pages, so `logo` is measured on pricing.
  await S('nav-membership', q('a:has-text("[membership]")').filter({ visible: true }).first(), B4, { group: g, title: 'Membership nav link', desc: 'The [membership] text link in the header; scrolls to the membership pitch.', sel: 'a [membership]' }, { noScroll: true });
  await S('cta-enter-app', q('a.clean-btn:has-text("Enter App"), a:has-text("Enter App")').filter({ visible: true }).first(), B4, { group: g, title: 'Enter App CTA', desc: 'The black pill at the header\'s far right; links to /login.', sel: 'a.clean-btn Enter App' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', q('p.super-title').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero title', desc: 'The visible display copy "A sacred place for your work-in-progress music" (p.super-title); the actual h1 is sr-only.', sel: 'p.super-title' }, { noScroll: true });
  const disc = q('div.rounded-full').filter({ visible: true }).first();
  const discRow = disc.locator('xpath=ancestor::*[contains(@class,"flex") or contains(@class,"grid") or self::section or self::div][1]');
  await S('disc-carousel', discRow, ['default'], { group: h, title: 'Disc carousel', desc: 'The signature element: a strip of oversized iridescent CD renders (div.rounded-full with webp background-image art) filling the hero.', sel: 'disc strip' });
  await S('disc', disc, ['default'], { group: h, title: 'Disc', desc: 'One iridescent CD render: a rounded-full div whose background-image is a webp disc artwork.', sel: 'div.rounded-full disc' });

  // The floating pill bar pinned to the viewport bottom.
  const bar = q('a.bg-shading:has-text("iOS")').filter({ visible: true }).first()
    .locator('xpath=ancestor::*[contains(@class,"pointer-events") or contains(@class,"fixed") or contains(@class,"absolute")][1]');
  await S('pill-bar', (await bar.count()) ? bar : q('a.bg-shading:has-text("iOS")').filter({ visible: true }).first(), ['default'], { group: h, title: 'Bottom pill bar', desc: 'The floating bar pinned to the viewport bottom: social pills (Texting Interviews, IG, X), the black We\'re hiring pill, Learn more, and the iOS / Android / MacOS platform pills.', sel: 'floating pill bar' });
  // The social pill's copy changes with campaigns (it read "Texting
  // Interviews" in the 2026-11-08 capture, "[untitled broadcast network]" a
  // day later) — match either, and the IG/X links beside it stay out.
  await S('pill-social', await opaqueText(/interviews|broadcast/i, { sel: 'a.body-semibold', tag: 'ps' }), B4, { group: h, title: 'Social pill', desc: 'A frosted pill in the bottom bar holding the social links (a campaign link — "[untitled broadcast network]", earlier "Texting Interviews" — then IG, X).', sel: 'social pill' });
  await S('cta-hiring', q('a:has-text("We\'re hiring"), a.bg-primary-label').filter({ visible: true }).first(), B4, { group: h, title: 'Hiring pill', desc: 'The inverted (black) "We\'re hiring" pill in the bottom bar; links to jobs.untitled.stream.', sel: 'a We\'re hiring' });
  // Learn more fades to opacity 0 the moment the page leaves the top (its job
  // is to scroll you to the product sections) and fades back at scrollY 0 —
  // real behaviour, verified live. Scroll to top before tagging, and don't
  // centre() it back down during the states.
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(1200);
  await S('pill-learn-more', await opaqueText(/learn more/i, { tag: 'plm' }), B4, { group: h, title: 'Learn more pill', desc: 'The frosted pill that scrolls the page to the product sections. It fades to opacity 0 as soon as the page scrolls and back at the top — these states are measured at scrollY 0.', sel: 'button Learn more' }, { noScroll: true });
  await S('pill-platform', q('a.bg-shading:has-text("iOS")').filter({ visible: true }).first(), B4, { group: h, title: 'Platform pill', desc: 'One of the iOS / Android / MacOS download pills in the bottom bar, each with a platform icon.', sel: 'a.bg-shading platform' });

  // Down-page product sections (the full page is ~4800px).
  const feat = await domFind(page, /organize your music/i, { sel: 'h3, h2', tag: 'ft' });
  await S('feature-title', feat, ['default'], { group: h, title: 'Feature title', desc: 'An h3.body-semibold heading a product section down the page ("Organize your music the way you want").', sel: 'h3 feature' });
  const featSec = feat.filter({ visible: true }).first().locator('xpath=ancestor::*[self::section or self::li or contains(@class,"grid") or contains(@class,"flex")][1]');
  await S('feature-section', featSec, ['default'], { group: h, title: 'Feature section', desc: 'A product-feature block down the landing page: heading, copy and media.', sel: 'feature block' });
  await S('feature-video', q('video').filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature video', desc: 'A product-demo video embedded in a feature section; measured as the element, its stream is not introspected.', sel: 'video' });
  await S('read-more', q('a:has-text("Read more")').filter({ visible: true }).first(), B4, { group: h, title: 'Read more link', desc: 'A text link expanding a product story section.', sel: 'a Read more' });

  await S('footer', q('a:has-text("Cookie Policy")').filter({ visible: true }).first().locator('xpath=ancestor::*[self::footer or self::div][1]'), ['default'], { group: g, title: 'Footer', desc: 'The legal row at the foot: Terms, Privacy, Cookie Policy, Contact Us and a Cookie Settings button, plus the Made in Brooklyn, NY mark.', sel: 'footer row' });
  await S('footer-link', q('a.subhead:has-text("Terms")').filter({ visible: true }).first(), B4, { group: g, title: 'Footer legal link', sel: 'a.subhead Terms' });
  await S('cookie-settings', q('button:has-text("Cookie Settings")').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Cookie settings button', desc: 'The footer control that re-opens the consent card. Focused and hovered only — pressing it reposts the gated consent flow.', sel: 'button Cookie Settings' });
  await closeCtx();
}

async function pricing() {
  if (!(await newPage('pricing'))) { await closeCtx(); return; }
  await sheetsFor('pricing');
  const g = G.pricing;
  const hdr = q('div.flex.w-full.flex-col, header').filter({ visible: true }).first();
  await S('pricing-header', hdr, ['default'], { group: G.shell, title: 'Pricing header', desc: 'Same top band as home, here with the [untitled] wordmark link at the left and Enter app (ghost) + Subscribe (black) pills on the right.', sel: 'header column' }, { noScroll: true });
  await S('logo', q('a:has-text("ntitled"), a[href="/"]').filter({ visible: true }).first(), B4, { group: G.shell, title: 'Wordmark', desc: 'The [untitled] mark, a text link rendered with bracket styling; only rendered on the sub-pages, not on home.', sel: 'wordmark link' }, { noScroll: true });
  await S('cta-subscribe', q('a.clean-btn:has-text("Subscribe"), a:has-text("Subscribe")').filter({ visible: true }).first(), B4, { group: G.shell, title: 'Subscribe CTA', desc: 'The black Subscribe pill in the header.', sel: 'a.clean-btn Subscribe' }, { noScroll: true });
  await S('pricing-title', q('div.super-title, p.super-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: '"Take your creative process to the next level" — a .super-title block, same display style as the home hero.', sel: '.super-title' });
  const yearly = q('button:has-text("Yearly")').filter({ visible: true }).first();
  // The toggle group is the smallest ancestor that also holds Monthly.
  const toggleWrap = yearly.locator('xpath=ancestor::*[.//button[contains(.,"Monthly")]][1]');
  await S('billing-toggle', toggleWrap, ['default'], { group: g, title: 'Billing toggle', desc: 'The Yearly / Monthly segment rail at the left of the plan grid: the buttons are its direct children, and the column stretches to the plan cards\' full height.', sel: 'billing segment' });
  await S('billing-yearly', yearly, ['default', 'hover', 'pressed'], { group: g, title: 'Yearly option', desc: 'The selected segment (default plan is yearly).', sel: 'button Yearly' });
  const monthly = q('button:has-text("Monthly")').filter({ visible: true }).first();
  // The toggle is client-side state: press Monthly, measure, switch back if it worked.
  await S('billing-monthly', monthly, ['default', 'hover'], { group: g, title: 'Monthly option', sel: 'button Monthly' });
  if (await monthly.count()) {
    await monthly.click().catch(() => monthly.evaluate((el) => el.click()));
    await page.waitForTimeout(1200);
    if (!(await blocked())) {
      await S('billing-monthly-on', monthly, ['open'], { group: g, title: 'Monthly option (selected)', desc: 'The Monthly segment after pressing it: client-side state switch, no data posted.', sel: 'button Monthly on' }, { noScroll: true });
      await S('plan-price-monthly', q('text=/\\$[0-9]/').filter({ visible: true }).first(), ['open'], { group: g, title: 'Monthly price', desc: 'The membership price after switching to Monthly.', sel: 'price monthly' }, { noScroll: true });
      await yearly.click().catch(() => {});
      await page.waitForTimeout(800);
    }
  }
  const starter = await domFind(page, /\[starter\]/i, { sel: 'h2, h3, p, div, span', tag: 'st' });
  const starterCard = starter.filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"rounded") or contains(@class,"bg-") or self::li or self::section][1]');
  await S('plan-card', starterCard, ['default'], { group: g, title: 'Plan card (starter)', desc: 'The [starter] free tier card: plan name, price, feature list with icons.', sel: 'starter card' });
  const member = await domFind(page, /\$49\.99/, { sel: 'p, div, span, h2, h3', tag: 'mb' });
  const memberCard = member.filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"rounded") or contains(@class,"bg-") or self::li or self::section][1]');
  await S('plan-card-paid', memberCard, ['default'], { group: g, title: 'Plan card (membership)', desc: 'The [membership] card: $49.99 / year, feature list with icons.', sel: 'membership card' });
  await S('plan-name', starter.filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'A bracketed plan name ([starter], [membership]).', sel: 'plan name' });
  await S('plan-price', q('text=/^Free$|\\$49\\.99|\\$[0-9]+\\.[0-9]+/').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', sel: 'price text' });
  await S('feature-row', q('li:has(h3), h3.body-semibold').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature row', desc: 'A plan feature line: icon + h3.body-semibold name + sub copy ("Unlimited listening").', sel: 'feature li' });
  await closeCtx();
}

async function trust() {
  if (!(await newPage('trust'))) { await closeCtx(); return; }
  await sheetsFor('trust');
  const g = G.trust;
  await S('trust-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Trust title', desc: '"Trust & Security" — the page is a single long-text column.', sel: 'trust h1' });
  const sec = await domFind(page, /\[\d\]|Passwordless|Encryption|Face ID/i, { sel: 'h2, h3, h4, p, strong', tag: 'ts' });
  await S('trust-section-title', sec, ['default'], { group: g, title: 'Trust section title', desc: 'A numbered practice heading ("[1] Passwordless sign-in").', sel: 'trust heading' });
  await S('trust-list', q('ul, ol').filter({ visible: true }).first(), ['default'], { group: g, title: 'Trust bullet list', desc: 'The encryption-standards bullet list (TLS in transit, AES-256 at rest).', sel: 'trust ul' });
  // The first <a> on the page is the [untitled] header wordmark; the described
  // element is the outbound link inside the practices column (the Latacora link).
  await S('trust-link', await opaqueText(/latacora|cloudflare|security@|https?:\/\//i, { sel: 'a[href^="http"], a[href^="mailto:"]', tag: 'tl' }), B4, { group: g, title: 'Trust link', desc: 'The untitled-blue outbound link inside the practices column (the Latacora link).', sel: 'trust outbound a' });
  await closeCtx();
}

async function login() {
  if (!(await newPage('login', { wait: 9000 }))) { await closeCtx(); return; }
  await sheetsFor('login');
  const g = G.signin;
  const card = await domFind(page, /sacred place|continue with/i, { sel: 'main, section, div', tag: 'lc', leaf: false, minW: 280, minH: 300 });
  await S('login-card', card, ['default'], { group: g, title: 'Sign-in card', desc: 'The centred sign-in column: app icon, the tagline, and three choices — Continue with Google, Continue with Apple, Sign in with phone. OAuth and phone sign-in were measured at rest only; nothing was pressed or sent.', sel: 'login column' });
  // The mark is the 220px .amulet-clip-mask disc; a first-match rounded-full
  // is its 189px inset-[7%] inner circle, not the icon.
  await S('login-icon', q('div.amulet-clip-mask, div.bg-amulet').filter({ visible: true }).first(), ['default'], { group: g, title: 'App icon', desc: 'The iridescent-disc app icon at the top of the sign-in card (the 220 px amulet mask, not its inner ring).', sel: '.amulet-clip-mask' });
  await S('login-title', q('h1, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in title', sel: 'login h1' });
  // Rest states only: these leave the site (OAuth) or start a flow.
  await S('oauth-google', q('a:has-text("Continue with Google"), button:has-text("Continue with Google")').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Continue with Google', desc: 'The frosted OAuth pill. Hovered and focused only — pressing it leaves for accounts.google.com.', sel: 'Google oauth pill' });
  await S('oauth-apple', q('a:has-text("Continue with Apple"), button:has-text("Continue with Apple")').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Continue with Apple', desc: 'The matching Apple OAuth pill. Hovered and focused only.', sel: 'Apple oauth pill' });
  await S('phone-signin', q('a:has-text("Sign in with phone"), button:has-text("Sign in with phone")').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Phone sign-in link', desc: 'The text option under the OAuth pills; leads to the passwordless SMS flow.', sel: 'phone sign-in' });
  await S('legal-link', q('a:has-text("Terms"), a:has-text("Privacy Policy")').filter({ visible: true }).first(), B4, { group: g, title: 'Legal link', desc: 'The Terms / Privacy Policy links under the sign-in choices.', sel: 'login legal a' });
  await closeCtx();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) { await closeCtx(); return; }
  const g = G.mobile;
  await closePromo(page);
  await S('m-hero-title', q('p.super-title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero title', sel: 'mobile super-title' }, { noScroll: true });
  await S('m-appstore', q('a:has-text("App Store"), img[alt*="App Store" i], a[href*="apple" i]').filter({ visible: true }).first(), ['default', 'pressed'], { group: g, title: 'App Store badge', desc: 'The Download on the App Store badge under the mobile hero title.', sel: 'app store badge' }, { noScroll: true });
  await S('m-disc', q('div.rounded-full').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile disc', desc: 'The oversized iridescent disc filling the lower half of the mobile hero.', sel: 'mobile disc div' });
  await S('m-membership', q('a:has-text("[membership]"), a:has-text("Enter App")').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav link', sel: 'mobile header link' }, { noScroll: true });
  await closeCtx();
}

const RUNNERS = { home, pricing, trust, login, mobile };
run = new Date().toISOString();
out._meta.run = run;
out._meta.product = 'untitled.stream';
const wanted = process.argv.slice(2).join(',').split(',').map((s) => s.trim()).filter(Boolean);
({ browser, context } = await launch());
for (const [k, fn] of Object.entries(RUNNERS)) {
  if (wanted.length && !wanted.includes(k)) continue;
  for (let attempt = 0; attempt < 3; attempt++) {
    try { await fn(); break; } catch (e) {
      log('PAGE FAILED', k, String(e.message).split('\n')[0]);
      // A renderer crash ("Target page/context/browser has been closed") is
      // retried with a fresh browser; anything else fails the page once.
      if (!/closed|crash|Terminated|target/i.test(e.message) || attempt === 2) break;
      try { await browser.close(); } catch {}
      ({ browser, context } = await launch());
      log('  relaunched browser, retrying', k);
    }
  }
  save();
}
// mark components from this run whose selectors matched nothing; a component
// with recorded states (from an earlier merged run) is covered, not missing
for (const [k, c] of Object.entries(out.components)) {
  if (!touched.has(k)) continue;
  if (Object.keys(c.states || {}).length) delete c.missing;
  else c.missing = true;
}
save();
await browser.close();
log('done ->', OUT);
