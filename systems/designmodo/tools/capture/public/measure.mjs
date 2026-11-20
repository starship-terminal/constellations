// Measures designmodo.com's public components in every state reachable without
// signing in or pressing a destructive control, and writes raw/components-computed.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs [OUT_JSON=/path/out.json] node measure.mjs [page ...]
//
// Pages (space-separated): home app pricing templates login postcards mobile.
// Writes raw/components-computed.json unless OUT_JSON names another file.
//
// designmodo.com is a single light theme signed out: the marketing home, the Postcards
// product/pricing pages, the email-templates gallery, the my-account sign-in form, and
// the signed-out Postcards app shell — which mounts a "Welcome back!" auth modal over
// the template gallery (Escape dismisses it; nothing is ever submitted). States:
// default, hover, focus-visible, pressed on controls; focused/filled on fields, which
// are typed into and cleared, never submitted. Add-to-cart links, Login/Signup, Create
// and Generate actions are measured, never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', app: '/postcards/app/folder/templates', pricing: '/postcards/pricing/', templates: '/email-templates/', login: '/my-account/sign-in/', postcards: '/postcards/', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
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
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it, pinned to the run
    // that actually read it (comp() has already restamped the component).
    const prev = c.states[state];
    if (prev && prev.style) {
      prev.rerunError = String(e.message || e).slice(0, 200);
      if (opts.earlierRun) { prev.read ??= opts.earlierRun; prev.rerunOn = run; } // a second failure keeps the first date
    }
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
  // Found this run: its states are re-read below, so an earlier miss no longer
  // describes them (the builder flags every token read from a component that
  // still carries recaptureMissed).
  delete out.components[key].recaptureMissed;
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
        // Modal calls skip reset() so the dialog stays open; the pointer then
        // still rests on the control and the reading picks up hover paint.
        // Move it away before the keyboard focus so this state stays
        // keyboard-only.
        await page.mouse.move((page.viewportSize()?.width ?? 1440) - 2, 2);
        await page.waitForTimeout(150);
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
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via, earlierRun: keep?.run });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) {
        prev.rerunError = String(e.message || e).slice(0, 200);
        // comp() already stamped this run's date on the component; pin the
        // retained reading to the run that actually captured it so an old
        // measurement is never republished as a new one.
        if (keep) { prev.read ??= keep.run; prev.rerunOn = run; } // a second failure keeps the first date
      }
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
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
  shell: 'Header and navigation', home: 'Home marketing', app: 'Postcards app (signed out)',
  modal: 'Welcome-back auth modal', pricing: 'Pricing', templates: 'Email-template gallery',
  login: 'Sign-in form', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// The signed-out Postcards app mounts a "Welcome back!" auth modal over the
// template gallery. Escape is a local UI dismissal — it reveals the gallery,
// which is then browsable signed out. Nothing is ever submitted.
async function closeWelcome() {
  const open = () => page.locator('.dialog-container').isVisible().catch(() => false);
  if (!(await open())) return 'no welcome modal was mounted';
  for (let i = 0; i < 3; i++) {
    await page.keyboard.press('Escape');
    await page.waitForTimeout(900);
    if (!(await open())) return 'Escape dismissed the welcome modal';
  }
  const x = page.locator('.dialog-container svg').first();
  await x.click({ timeout: 3000 }).catch(() => x.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  return (await open()) ? 'the welcome modal stayed open' : 'the modal close control dismissed it';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header nav.main-menu, nav.main-menu, header nav').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Site header', desc: 'The top bar: Designmodo wordmark, Apps/Articles menus, Log In and Sign Up.', sel: 'header' }, { noScroll: true });
  await S('nav-apps', q('header a, header button, nav a').filter({ hasText: /^\s*Apps\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Apps menu', desc: 'The "Apps" product menu in the header; measured, never opened beyond hover.', sel: 'Apps' }, { noScroll: true });
  await S('nav-login', q('header a, a, button').filter({ hasText: /^\s*Log In\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Log In', desc: 'The header Log-In action; measured, never followed.', sel: 'Log In' }, { noScroll: true });
  await S('nav-signup', q('header a, a, button').filter({ hasText: /^\s*Sign Up\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sign Up', desc: 'The header Sign-Up action; measured, never followed.', sel: 'Sign Up' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Level up email & web designs faster" — the 56px display heading over the dark hero.', sel: 'h1' }, { noScroll: true });
  await S('openapp-cta', q('a').filter({ hasText: /^\s*Open App/ }).and(page.locator(':visible')).first(), B4, { group: h, title: 'Open App CTA', desc: 'The green "Open App \u2192" product CTA (164x53, #27ae60); measured, never followed.', sel: 'Open App' }, { noScroll: true });
  await S('seemore-link', q('a.see_more, a').filter({ hasText: /See more/ }).and(page.locator(':visible')).first(), B4, { group: h, title: 'See more link', desc: 'A "See more \u2192" link on a product strip.', sel: 'a.see_more' });
  // The home pricing-strip plan links (a[href*=add-to-cart]) live in an off-viewport
  // slide panel (y~-41000) — unreachable in the default flow; plan CTAs are
  // measured on the pricing page instead.
  await S('article-card', q('a').filter({ hasText: /Read more/ }).and(page.locator(':visible')).first(), B4, { group: h, title: 'Article card', desc: 'A "Read more \u2192" article card in the home articles strip.', sel: 'Read more' });
  const f = G.footer;
  await S('site-footer', q('section.footer, .footer, footer').and(page.locator(':visible')).last(), ['default'], { group: f, title: 'Site footer', desc: 'The sitemap footer (products, resources, legal links).', sel: 'footer' });
  save();
}

async function app() {
  if (!(await newPage('app'))) return;
  await sheetsFor('app');
  await chrome('app');
  const m = G.modal;
  // The welcome-back modal is the default signed-out state; its controls are
  // measured, never pressed, then Escape reveals the gallery behind it.
  await S('welcome-modal', q('.dialog-container').and(page.locator(':visible')).first(), ['default'], { group: m, title: 'Welcome modal', desc: 'The "Welcome back!" auth modal over the app shell (418x615, white card on a dimmed gallery).', sel: '.dialog-container' }, { noScroll: true });
  await S('modal-google', q('.dialog-container a, .dialog-container button, .dialog-container [role="button"]').filter({ hasText: /Continue with Google/i }).and(page.locator(':visible')).first(), B4, { group: m, title: 'Google button', desc: '"Continue with Google" in the welcome modal; measured, never pressed.', sel: 'Continue with Google' }, { noScroll: true, noReset: true });
  await S('modal-sso', q('.dialog-container a, .dialog-container button').filter({ hasText: /Sign-in with SSO/i }).and(page.locator(':visible')).first(), B4, { group: m, title: 'SSO button', desc: 'The dark "Sign-in with SSO" button; measured, never pressed.', sel: 'Sign-in with SSO' }, { noScroll: true, noReset: true });
  await S('modal-email', q('.dialog-container input[type="email"], .dialog-container input[placeholder*="email" i]').and(page.locator(':visible')).first(), FIELD, { group: m, title: 'Email field', desc: 'The your@email.com field in the welcome modal; focused and typed then cleared, never submitted.', sel: 'modal email field' }, { noScroll: true, fillText: 'probe@example.com' });
  await S('modal-login', q('.dialog-container button, .dialog-container a').filter({ hasText: /^\s*Login\s*$/ }).and(page.locator(':visible')).first(), B4, { group: m, title: 'Modal Login', desc: 'The green modal Login button; measured, never pressed.', sel: 'modal Login' }, { noScroll: true, noReset: true });
  await S('modal-create', q('.dialog-container button, .dialog-container a').filter({ hasText: /Create Account/i }).and(page.locator(':visible')).first(), B4, { group: m, title: 'Create Account', desc: 'The secondary "Create Account" button; measured, never pressed.', sel: 'Create Account' }, { noScroll: true, noReset: true });
  await page.evaluate(() => new Promise(r => setTimeout(r, 300)));
  const note = await closeWelcome();
  const g = G.app;
  await S('app-header', q('header, [class*="header" i], [class*="topbar" i]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'App header', desc: 'The dark navy app header: postcards mark, Login/Signup, the "+ Create" split button.', sel: 'app header' }, { noScroll: true });
  await S('app-login', q('a, button').filter({ hasText: /^\s*Login\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'App Login', desc: 'The blue Login pill in the app header; measured, never pressed.', sel: 'app Login' }, { noScroll: true });
  await S('app-signup', q('a, button').filter({ hasText: /^\s*Signup\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'App Signup', desc: 'The dark Signup pill in the app header; measured, never pressed.', sel: 'app Signup' }, { noScroll: true });
  await S('create-split', q('button, a, [class*="sc-"]').filter({ hasText: /^\s*\+?\s*Create\s*$/ }).and(page.locator(':visible')).last(), B4, { group: g, title: 'Create split button', desc: 'The green "+ Create" split button top-right of the gallery; measured, never pressed.', sel: '+ Create' }, { noScroll: true });
  await S('sidebar', q('div').filter({ hasText: /Chat with Us/ }).filter({ hasText: /Drafts/ }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'App sidebar', desc: 'The 240px workspace sidebar: Drafts, Templates (+233 NEW), Workspace Settings, Chat with Us.', sel: 'aside' });
  await S('side-templates', q('div').filter({ hasText: /^\s*Templates\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Templates nav', desc: 'The "Templates" sidebar item with the +233 NEW badge.', sel: 'Templates nav' });
  await S('new-badge', q('span, [class*="sc-"]').filter({ hasText: /^\s*\+?\d*\s*NEW\s*$/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'NEW badge', desc: 'The green "+233 NEW" counter badge on the Templates item.', sel: 'NEW badge' });
  await S('filter-industry', q('button, [class*="sc-"], div').filter({ hasText: /^\s*Industry\s*$/ }).and(page.locator(':visible')).last(), B4, { group: g, title: 'Industry filter', desc: 'The "Industry" gallery filter dropdown; measured, never opened.', sel: 'Industry filter' }, { noScroll: true });
  await S('create-blank', q('div').filter({ hasText: /^\s*Create Blank Template\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Create Blank card', desc: 'The dashed "Create Blank Template" gallery card (266x532); measured, never pressed.', sel: 'Create Blank Template' });
  await S('genai-card', q('div').filter({ hasText: /^\s*Generate with AI\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Generate AI card', desc: 'The lavender "Generate with AI" gallery card; measured, never pressed.', sel: 'Generate with AI' });
  await S('tpl-card', q('span:has-text("FREE")').and(page.locator(':visible')).first().locator('xpath=ancestor::*[contains(@class,"sc-")][2]'), ['default'], { group: g, title: 'Template card', desc: 'A named template card (Kindred, Nortflow...) with the FREE badge and category tags.', sel: 'template card' });
  await S('free-badge', q('span:has-text("FREE")').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'FREE badge', desc: 'The blue FREE corner badge on template cards.', sel: 'FREE badge' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Pricing headline', desc: 'The 91.5px "Pricing" display heading.', sel: 'h1' }, { noScroll: true });
  await S('billing-toggle', q('button, [role="switch"], [class*="switch" i], [class*="toggle" i], label').filter({ hasText: /Yearly|Monthly/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Billing toggle', desc: 'The Yearly/Monthly billing switch; measured, never toggled.', sel: 'Yearly Monthly' }, { noScroll: true });
  await S('plan-card', q('.PriceBlock').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (Start FREE FOREVER / Plus / Pro) — white-box 313px wide.', sel: '.PriceBlock' });
  await S('plan-cta', q('a[href*="add-to-cart"], a, button').filter({ hasText: /Get Started|\$\d+\/month|\/year/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan action (Get Started / $19/month) — it adds to the cart; measured, never pressed.', sel: 'plan CTA' });
  await S('plan-feature', q('.planFeatures li, .planFeatures *').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Plan feature', desc: 'A plan feature row ("10 template projects") with the ? hint icon.', sel: 'planFeatures row' });
  save();
}

async function templates() {
  if (!(await newPage('templates'))) return;
  await sheetsFor('templates');
  await chrome('templates');
  const g = G.templates;
  await S('tpl-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Gallery headline', desc: 'The email-templates gallery heading.', sel: 'h1' }, { noScroll: true });
  await S('tpl-filter', q('li.fill').and(page.locator(':visible')).first(), B4, { group: g, title: 'Gallery filter', desc: 'The Industry / Usage / Season / Brand / Free-only filter bar over the email-template grid (714x43); measured, never activated.', sel: 'li.fill' });
  await S('tpl-card-m', q('.template-box').and(page.locator(':visible')).first(), B4, { group: g, title: 'Template tile', desc: 'An email-template tile in the marketing gallery grid (210x420, thumbnail + name + tags); measured, never followed.', sel: '.template-box' });
  save();
}

async function login() {
  if (!(await newPage('login'))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('login-form', q('form.woocommerce-form-login, form').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Sign-in form', desc: 'The my-account sign-in card (380px, Google/SSO buttons over email+password).', sel: 'form.woocommerce-form-login' });
  await S('login-h1', q('h1, h2').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Sign-in heading', desc: '"Login to Designmodo" — the 24px form heading.', sel: 'login h1' }, { noScroll: true });
  await S('login-google', q('a, button').filter({ hasText: /Login with Google|Continue with Google/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Google login', desc: '"Login with Google" — measured, never pressed.', sel: 'Login with Google' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name*="email" i], input.input-text').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Email field', desc: 'The 380x50 email input; focused and typed then cleared, never submitted.', sel: 'email input' }, { fillText: 'probe@example.com' });
  await S('login-pass', q('input[type="password"]').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Password field', desc: 'The password input; focused and typed then cleared, never submitted.', sel: 'password input' }, { fillText: 'probe-not-real' });
  await S('login-submit', q('button[type="submit"], button').filter({ hasText: /^\s*Login/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Login button', desc: 'The blue Login submit (186x38.5, #2f80ed); measured, never pressed.', sel: 'Login button' }, { noScroll: true });
  await S('login-create', q('a, button').filter({ hasText: /Create Account/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Create Account', desc: 'The green "Create Account" pair button; measured, never followed.', sel: 'Create Account' }, { noScroll: true });
  save();
}

async function postcards() {
  if (!(await newPage('postcards'))) return;
  await sheetsFor('postcards');
  await chrome('postcards');
  const g = G.home;
  await S('pc-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Product headline', desc: 'The Postcards product page heading.', sel: 'postcards h1' }, { noScroll: true });
  await S('pc-cta', q('a, button').filter({ hasText: /Open App|Try it|Get Started|Start/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Product CTA', desc: 'The product page primary CTA; measured, never followed.', sel: 'product CTA' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header nav.main-menu, nav.main-menu, header nav, header').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar with the wordmark and menu.', sel: 'mobile header' }, { noScroll: true });
  await S('m-h1', q('h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The phone hero heading.', sel: 'mobile h1' });
  await S('m-cta', q('a').filter({ hasText: /Open App/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile CTA', desc: 'The green Open App CTA on the phone; measured, never followed.', sel: 'mobile Open App' });
  await S('m-footer', q('section.footer, .footer, footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'mobile footer' });
  save();
}

const pages = process.argv.slice(2);
const plan = { home, app, pricing, templates, login, postcards, mobile };
// Refuse an unknown page name (a comma-separated list is one unknown name)
// before anything is stamped: a run that matches no page must not write
// today's date into _meta.read.
const unknown = pages.filter((k) => !(k in plan));
if (unknown.length) { console.error(`unknown page(s): ${unknown.join(', ')}; pages are: ${Object.keys(plan).join(' ')}`); process.exit(2); }
run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); designmodo.com paints a single light theme signed out';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the Create CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a');
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
