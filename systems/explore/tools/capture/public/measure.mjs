// Measures explore.family's public components in every state reachable
// without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home discover login register forgot about legal mobile ssr.
//
// Every route is replayed from the local Internet Archive mirror (lib.mjs
// wireMirror): the live host is gone, so the February 2023 build runs against
// archived files, archived API JSON and archived uploads. What the archive
// lacks is recorded, not invented: profile and single-post APIs were never
// crawled, so the SPA's /{username} and /p/{id} render the shell only; the
// mirror's routes/*.html SSR copies are what the server sent crawlers.
//
// Explore ships one fixed theme (no custom properties, no
// prefers-color-scheme); every value is hardcoded in app.4ef09b07.css.
// Classes are stable BEM names (.header, .post__gallery, .btn--yellow).
// Nothing is sent, created or signed into: the only presses are local UI
// toggles — the password visibility eye, the carousel arrows; the auth
// fields are typed into and cleared, never submitted; every link, Log in,
// Sign up and Reset Password is measured, never followed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, wireMirror, open, closePromo, domFind, styleOf, crop, centre, RAW, REF, CROPS, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', discover: '/discover', login: '/login', register: '/register', forgot: '/forgot-password', about: '/about', legal: '/conduct', mobile: '/discover', ssr: '/malikafavre' };
// ^ ssr has its entry so comp() records the profile URL its components were read on (it was undefined).
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
const keepMeta = new Map();
const failedPages = new Set();

async function newPage(key, { mobile = false, wait = 9000, url = null, ssr = null } = {}) {
  current = key;
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  await wireMirror(ctx, { era: 'feb', ssr });
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', ssr ? '(ssr)' : '');
  await open(page, url || BASE + URLS[key], { wait, promo: 'close' });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return true;
}

// Fixed/sticky chrome with paint order, recorded per page into _meta.chrome.
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
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'focus() (keyboard ring via :focus)';
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
    // A reading of a hidden element (the marketing chrome sits display:none
    // in the DOM of the auth pages) is not a measurement of the component —
    // keep the earlier visible state and mark the recapture as missed.
    const hidden = s.style.display === 'none' || s.style.visibility === 'hidden' || (!s.rect.w && !s.rect.h);
    if (hidden) {
      const prev = c.states[state];
      if (prev && prev.style) {
        // Restore the earlier page's page/run/url alongside its readings.
        const keep = keepMeta.get(key);
        if (keep) Object.assign(c, keep);
        c.recaptureMissed = run;
        log('  ! hidden', key, state, '(earlier visible state kept)');
        return;
      }
      s.hidden = true;
    }
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  keepMeta.set(key, keep);
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
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
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        await toggle(loc, { allowLink: opts.allowLink });
        await page.waitForTimeout(900);
        via = 'own toggle';
      } else via = via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead (the builders list it as "focus could not be
        // captured"); an earlier run's real focus reading is kept, with the failed retry noted beside it.
        const prevSt = out.components[key].states[st];
        if (prevSt?.style && prevSt.via !== 'focus failed') {
          prevSt.rerunError = 'focus failed: keyboard focus did not reach the element';
          log('  !', key, st, 'focus failed; earlier reading kept');
        } else {
          const old = prevSt?.crop && path.resolve(REF, prevSt.crop);
          if (old && old.startsWith(CROPS + path.sep)) fs.rmSync(old, { force: true });
          out.components[key].states[st] = { skipped: 'focus failed: keyboard focus did not reach the element', via, run };
          log('  -', key, st, 'skipped: focus failed');
        }
      } else await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle only. Refuses submits and named actions.
const NEVER = /^(send|submit|sign in|sign up|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|try again|reset password)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

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
  shell: 'Site chrome', home: 'Home (marketing + feed)', discover: 'Discover feed',
  auth: 'Auth forms', about: 'About / legal', ssr: 'Server-rendered profile', mobile: 'Mobile (390 wide)',
};

// The visitor chrome is identical on every page: grey fixed .header with the
// logo, "Sign in" link and yellow "Sign up free" pill.
async function shell(g) {
  await S('mkt-header', q('header.header').first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed grey top bar: logo left, "Sign in" link and yellow "Sign up free" pill right.', sel: 'header.header' }, { noScroll: true });
  await S('mkt-logo', q('header .header__logo, header a.header__logo').first(), ['default'], { group: g, title: 'Logo', desc: 'The Explore wordmark (inline svg) in the header, linking home.', sel: '.header__logo' }, { noScroll: true });
  await S('nav-signin', q('.header__auth-links a').filter({ hasText: /^Sign in$/ }).first(), B4, { group: g, title: 'Sign in link', desc: 'The "Sign in" header link; measured, never followed.', sel: '.header__auth-links a "Sign in"' }, { noScroll: true });
  await S('nav-signup', q('.header__auth-links a.btn, header a.btn--yellow').filter({ hasText: /Sign up free/ }).first(), B4, { group: g, title: 'Sign up pill', desc: 'The yellow "Sign up free" pill (btn--yellow btn--rounded btn--small); measured, never followed.', sel: '.header__auth-links a.btn--yellow' }, { noScroll: true });
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  await shell(G.home);
  const g = G.home;
  await S('hero', q('section.section--hero, .hero').first(), ['default'], { group: g, title: 'Hero section', desc: 'The home hero: "Welcome" greeting, the positioning sentence and the feature tags, over the testimonial imagery.', sel: 'section.section--hero .hero' }, { noScroll: true });
  await S('hero-welcome', q('.hero__welcome').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero greeting', desc: 'The "Welcome" greeting at the top of the hero.', sel: '.hero__welcome' }, { noScroll: true });
  await S('hero-title', q('.hero__title:not(.hero__title--mobile)').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline', desc: '"Explore is an emotionally intelligent ad-free social media platform…" — the display sentence.', sel: '.hero__title' }, { noScroll: true });
  await S('hero-tag', q('.hero__tag').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero tag', desc: 'A feature tag in the hero tag list (Free / For creatives / No ads…).', sel: '.hero__tag' }, { noScroll: true });
  await S('hero-tag-cta', q('a.hero__tag').filter({ visible: true }).first(), B4, { group: g, title: 'Hero tag CTA', desc: 'The "All features" tag link; measured, never followed.', sel: 'a.hero__tag' }, { noScroll: true });
  await S('feed-section', q('.content--posts').first(), ['default'], { group: g, title: 'Feed section', desc: 'The post feed below the hero (the same card grid as /discover).', sel: 'home .content--posts' });
  save();
}

async function discover() {
  if (!(await newPage('discover', { wait: 12000 }))) return;
  await sheetsFor('discover');
  await chrome('discover');
  await shell(G.discover);
  const g = G.discover;
  await S('discover-title', q('.discover__title').filter({ visible: true }).first(), ['default'], { group: g, title: 'Discover heading', desc: '"Browse inspiring work on Explore curated by our team" — the page heading above the feed.', sel: '.discover__title' }, { noScroll: true });
  await S('pill-row', q('.discover__categories, .pills').filter({ visible: true }).first(), ['default'], { group: g, title: 'Category pill row', desc: 'The scrollable category pills row (All / 3D Design / Animation / Art…).', sel: '.discover__categories .pills' }, { noScroll: true });
  await S('pill', q('a.pill').first(), B4, { group: g, title: 'Category pill (active)', desc: 'The selected "All" category pill; measured, never followed.', sel: 'a.pill "All"' }, { noScroll: true });
  await S('pill-idle', q('a.pill').nth(1), B4, { group: g, title: 'Category pill', desc: 'An unselected category pill; measured, never followed.', sel: 'a.pill "Animation"' }, { noScroll: true });
  await S('post-card', q('.post--with-author, .post').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post card', desc: 'A feed post card: gallery tile on top, author row and title below.', sel: '.post' });
  await S('post-gallery', q('.post__gallery').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post gallery', desc: 'The media tile of a feed card (post__gallery--rounded); images or a video poster.', sel: '.post__gallery' });
  await S('post-author', q('.post__author').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post author row', desc: 'The author line under a card: avatar, name, age ("4yr").', sel: '.post__author' });
  await S('post-avatar', q('.post__author-image').filter({ visible: true }).first(), ['default'], { group: g, title: 'Author avatar', desc: 'The round author avatar on a feed card (post__author-image--blank when empty).', sel: '.post__author-image' });
  await S('post-title', q('.post__content').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post title', desc: 'The work title under a card.', sel: '.post__content' });
  await S('post-actions', q('.post__actions').filter({ visible: true }).first(), ['default'], { group: g, title: 'Post actions', desc: 'The action icon row on a card (appreciate/save/comment affordances).', sel: '.post__actions' });
  await S('carousel-next', q('button.VueCarousel-navigation-next').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Carousel next arrow', desc: 'The next-arrow on a multi-image post carousel.', sel: 'button.VueCarousel-navigation-next' });
  save();
}

async function login() {
  if (!(await newPage('login'))) return;
  await sheetsFor('login');
  await chrome('login');
  await shell(G.auth);
  const g = G.auth;
  await S('auth-panel', q('.auth').first(), ['default'], { group: g, title: 'Auth layout', desc: 'The split auth screen: community welcome on the left, the form panel on the right.', sel: '.auth' }, { noScroll: true });
  await S('auth-quote', q('.auth__left .auth__quote, .auth__left').first(), ['default'], { group: g, title: 'Welcome quote', desc: 'The left welcome panel: "Remember we are a community…" over the looping animation.', sel: '.auth__left' }, { noScroll: true });
  await S('auth-logo', q('.auth__logo').first(), ['default'], { group: g, title: 'Auth logo', desc: 'The Explore logo above the form.', sel: '.auth__logo' }, { noScroll: true });
  await S('auth-heading', q('.auth__text').first(), ['default'], { group: g, title: 'Auth heading', desc: '"Welcome back to Explore! / Log in to your account" — the form intro.', sel: '.auth__text' }, { noScroll: true });
  await S('field-email', q('input.input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The Email input; focused and typed into then cleared — never submitted.', sel: 'input.input (Email)' }, { noScroll: true, fillText: 'name@example.com' });
  await S('field-password', q('.input-password input, input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field', desc: 'The Password input with the visibility eye; typed into and cleared, never submitted.', sel: 'input[type=password]' }, { noScroll: true, fillText: 'hunter2example', cropLoc: q('.input-password').first() });
  await S('password-eye', q('.input-password .svg-eye, .input-password svg').filter({ visible: true }).first(), ['default'], { group: g, title: 'Password visibility eye', desc: 'The eye icon that toggles password visibility — a local UI toggle, pressed for nothing else.', sel: '.input-password .svg-eye' }, { noScroll: true });
  await S('login-submit', q('button.btn').filter({ hasText: /^\s*Log in\s*$/ }).first(), B4, { group: g, title: 'Log in button', desc: 'The full-width "Log in" submit (btn--full); states measured, never clicked — nothing was submitted.', sel: 'button.btn "Log in"' }, { noScroll: true });
  await S('forgot-link', q('a.forgot-password').first(), B4, { group: g, title: 'Forgot password link', desc: 'The "Forgot your password?" link under the submit; measured, never followed.', sel: 'a.forgot-password' }, { noScroll: true });
  await S('signup-link', q('.auth__right a, .text-center a').filter({ hasText: /Sign up free/ }).first(), B4, { group: g, title: 'Sign up link', desc: 'The "Sign up free" link under the submit; measured, never followed.', sel: '.text-center a "Sign up free"' }, { noScroll: true });
  save();
}

async function register() {
  if (!(await newPage('register'))) return;
  await sheetsFor('register');
  await shell(G.auth);
  const g = G.auth;
  await S('reg-heading', q('.auth__text, .auth__right').first(), ['default'], { group: g, title: 'Register heading', desc: 'The sign-up form intro.', sel: '.auth__right .auth__text' }, { noScroll: true });
  await S('reg-field-email', q('input.input, input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (register)', desc: 'The Email input; typed into and cleared, never submitted.', sel: 'register input.input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('reg-field-password', q('input[type="password"], .input-password input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (register)', desc: 'The Password input; typed into and cleared, never submitted.', sel: 'register input[type=password]' }, { noScroll: true, fillText: 'hunter2example' });
  await S('newsletter-check', q('.input-checkbox').filter({ visible: true }).first(), ['default'], { group: g, title: 'Newsletter checkbox', desc: 'The "Subscribe to newsletter (no spam…)" checkbox; measured, never toggled.', sel: '.input-checkbox' }, { noScroll: true });
  await S('terms-line', q('.auth__right *').filter({ hasText: /By clicking Sign up/ }).last(), ['default'], { group: g, title: 'Terms agreement line', desc: '"By clicking Sign up, I agree to Terms of Service and Privacy Policy."', sel: 'register agreement line' }, { noScroll: true });
  await S('reg-submit', q('button.btn, .btn-submit').filter({ hasText: /^\s*Sign up\s*$/ }).first(), B4, { group: g, title: 'Sign up button', desc: 'The "Sign up" submit; states measured, never clicked — nothing was submitted.', sel: 'register "Sign up"' }, { noScroll: true });
  save();
}

async function forgot() {
  if (!(await newPage('forgot'))) return;
  await sheetsFor('forgot');
  await shell(G.auth);
  const g = G.auth;
  await S('forgot-intro', q('.auth__right, .auth__text').first(), ['default'], { group: g, title: 'Reset intro', desc: '"Please enter your email address and you will receive a link…"', sel: 'forgot intro' }, { noScroll: true });
  await S('forgot-field', q('input.input, input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (reset)', desc: 'The Email input on the reset form; typed into and cleared, never submitted.', sel: 'forgot input.input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('forgot-submit', q('button.btn, .btn-submit').filter({ hasText: /Reset Password/i }).first(), B4, { group: g, title: 'Reset button', desc: 'The "Reset Password" submit; states measured, never clicked.', sel: 'forgot "Reset Password"' }, { noScroll: true });
  save();
}

async function about() {
  if (!(await newPage('about'))) return;
  await sheetsFor('about');
  const g = G.about;
  await S('about-title', q('.title').filter({ visible: true }).first(), ['default'], { group: g, title: 'About headline', desc: 'The about page masthead sentence.', sel: '.title' }, { noScroll: true });
  await S('feature', q('.feature').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature card', desc: 'A feature block ("Perfectly simple", "Community not numbers"…).', sel: '.feature' });
  await S('about-copy', q('.about').filter({ visible: true }).first(), ['default'], { group: g, title: 'About statement', desc: '"We are building Explore as it should be built…" — the statement copy.', sel: '.about' });
  await S('about-cta', q('a.btn-submit').filter({ hasText: /Sign up/ }).first(), B4, { group: g, title: 'About CTA', desc: '"Sign up — No bank card required" in the closing section; measured, never followed.', sel: '.section--cta a.btn-submit' });
  await S('footer', q('.footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The grey closing footer: typeface credits and site links.', sel: '.footer' }, { noScroll: true });
  await S('footer-column', q('.footer__column').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer column', desc: 'One footer column (Typefaces credits: Labil Grotesk / Untitled Sans…).', sel: '.footer__column' }, { noScroll: true });
  save();
}

async function legal() {
  if (!(await newPage('legal'))) return;
  const g = G.about;
  await S('legal-title', q('h1, h2, .page-title, .title, div').filter({ hasText: /^Code of Conduct$/ }).first(), ['default'], { group: g, title: 'Legal heading', desc: 'The page heading on the code of conduct.', sel: 'legal h1' }, { noScroll: true });
  await S('legal-body', q('div, p, section').filter({ hasText: /commitment to uphold/i }).last(), ['default'], { group: g, title: 'Legal body', desc: 'Body copy on a legal page (the same type treatment as /terms and /privacy).', sel: 'legal body' }, { noScroll: true });
  save();
}

// The archived server-rendered profile page (what crawlers and no-JS visitors
// received): replayed verbatim from mirror/routes/malikafavre.html with
// JavaScript disabled. Media URLs point at uploads the archive never kept, so
// tiles read as their empty placeholders — that is the evidence, not a bug.
async function ssr() {
  if (!(await newPage('ssr', { url: BASE + '/malikafavre', ssr: '/malikafavre', wait: 6000 }))) return;
  const g = G.ssr;
  await S('ssr-profile', q('.profile').first(), ['default'], { group: g, title: 'SSR profile', desc: 'The server-rendered profile page (Malika Favre): name, avatar placeholder and the post grid the crawler received.', sel: 'SSR .profile' }, { noScroll: true });
  await S('ssr-avatar', q('.profile__image').first(), ['default'], { group: g, title: 'SSR profile avatar', desc: 'The profile image slot; the avatar file itself was never archived, so it reads as its placeholder.', sel: 'SSR .profile__image' }, { noScroll: true });
  await S('ssr-name', q('.profile__name').first(), ['default'], { group: g, title: 'SSR profile name', desc: 'The display name on the server-rendered profile.', sel: 'SSR .profile__name' }, { noScroll: true });
  await S('ssr-post', q('.post').filter({ visible: true }).first(), ['default'], { group: g, title: 'SSR post tile', desc: 'A post tile in the server-rendered feed; its video/poster media was never archived, so it paints the empty placeholder.', sel: 'SSR .post' });
  await S('ssr-gallery', q('.post__gallery').filter({ visible: true }).first(), ['default'], { group: g, title: 'SSR post gallery', desc: 'The media tile of a server-rendered post.', sel: 'SSR .post__gallery' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/discover', wait: 12000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header.header').first(), ['default'], { group: g, title: 'Mobile header', desc: 'The fixed top bar at 390 wide.', sel: 'mobile .header' }, { noScroll: true });
  await S('m-signup', q('.header__auth-links a.btn, header a.btn--yellow').filter({ hasText: /Sign up/ }).first(), B4, { group: g, title: 'Mobile sign up pill', desc: 'The header "Sign up free" pill at 390 wide.', sel: 'mobile .btn--yellow' }, { noScroll: true });
  await S('m-pill', q('a.pill').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile category pill', desc: 'A category pill in the horizontally scrolling row at 390 wide.', sel: 'mobile a.pill' }, { noScroll: true });
  await S('m-post', q('.post').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile post card', desc: 'A feed card at 390 wide.', sel: 'mobile .post' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every page replays the 2023-02-23 explore.family build from the Internet Archive mirror — the live domain lapsed after the 2023-04-19 shutdown; one fixed light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, discover, login, register, forgot, about, legal, ssr, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { await plan[k](); finishedPages.add(k); }
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
