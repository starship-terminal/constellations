// Measures Lemni's public components in every state reachable without
// signing in, submitting a form, or following an OAuth flow.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
//
// Writes raw/components-computed.json and one crop per component and state
// into components/crops/.
//
// www.lemni.com is Framer. Classes are build hashes, so every target is
// marked with data-m-mark from a constrained evaluate (role, data-framer-name,
// or exact published label). Nothing is submitted: Continue, Try For Free
// and Continue with Google are measured at rest, hover, focus and a forced
// :active, and are never clicked through.
import fs from 'node:fs';
import path from 'node:path';
import { safeUrl } from '../safe-url.mjs';
import { APP, BASE, launch, open, closePromo, clearChallenge, styleOf, crop, centre, mark, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const ONLY = (process.argv[2] || '').split(',').filter(Boolean);
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { _meta: {}, components: {} };
const TODAY = new Date().toLocaleDateString('en-CA');
// _meta.read keeps the earlier date until this run reads a state, so a rerun that
// fails throughout never redates old readings; _meta.lastAttempt is this run's date.
// Each component and state also carries its own `read` date.
out._meta = { ...out._meta, read: (out._meta && out._meta.read) || TODAY, lastAttempt: TODAY, product: 'Lemni', route: 'public-web' };
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, cdp, current, context, browser;
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function newPage(key, url, { mobile = false, wait = 4500 } = {}) {
  current = key;
  if (context) await context.close().catch(() => {});
  context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  // automation is not hidden: the webdriver flag stays as Chromium sets it (bot check: recorded as a boundary, not bypassed)
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, url);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) throw new Error('blocked ' + url);
  await page.waitForTimeout(wait);
  await closePromo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(200);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  }
  await page.waitForTimeout(300);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(300);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  // Each component carries the date it was read, so a partial run that leaves
  // other components untouched does not pass their readings off as today's.
  out.components[key] = { page: current, url: meta.url, read: TODAY, states: {}, ...meta };
  return out.components[key];
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 10); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via, read: TODAY };
    out._meta.read = TODAY; // a reading succeeded in this run
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.textStyle && s.textStyle.color);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, getLoc, list, meta, opts = {}) {
  comp(key, meta);
  const loc0 = await getLoc();
  if (!loc0) { out.components[key].missing = true; log('  ! missing', key); return; }
  for (const st of list) {
    let undo, via = 'at rest';
    try {
      await reset();
      const loc = (await getLoc()) || loc0;
      if (!opts.noScroll) await centre(loc);
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => loc.hover({ force: true, timeout: 4000 }));
        await page.waitForTimeout(400);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(loc);
      } else if (st === 'pressed') {
        undo = await forcePseudo(loc, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover; not clicked';
      } else if (st === 'focused') {
        await loc.click({ timeout: 4000 });
        await page.waitForTimeout(300);
        via = 'clicked into the field; nothing submitted';
      } else if (st === 'filled') {
        throw new Error('filled is not captured: the public pass does not type into fields');
      }
      const loc2 = (await getLoc()) || loc;
      await measure(key, st, loc2, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 140));
    }
    if (undo) await undo().catch(() => {});
  }
  await reset();
}

const byName = (name) => () => mark(page, { name, tags: 'a,button,nav,div,section,h1,h2,p,span' });
const byText = (text, tags, extra = {}) => () => mark(page, { text, tags, exact: true, ...extra });

async function sheetsFor(key) {
  out._meta.sheets ??= {};
  out._meta.sheets[key] = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if ((t && t !== 'all 0s ease 0s') || a) transitions.push({ selector: (r.selectorText || '').slice(0, 140), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions.slice(0, 40);
  });
}

async function home() {
  await newPage('home', BASE + '/');
  await sheetsFor('home');
  const url = BASE + '/';
  const g = 'Shell';
  await S('nav-dark', async () => page.locator('nav').first(), ['default'], {
    group: g, title: 'Top bar, dark (home)', url,
    desc: 'The 50px fixed bar on the dark home page. Logo at the left, Docs Blog Company Community Pricing in TWK Lausanne 400 15px muted ink, Continue as a glass pill at the right.',
    selector: 'nav',
  }, { noScroll: true });
  await S('nav-link', byText('Docs', 'a'), B4, {
    group: g, title: 'Nav link', url,
    desc: 'A destination in the top bar. Resting ink is rgb(99, 100, 117) on the dark home page. Measured, never followed.',
    selector: 'nav a (Docs)',
  }, { noScroll: true });
  await S('nav-continue', byText('Continue', 'a'), B4, {
    group: g, title: 'Continue pill (nav)', url,
    desc: 'The glass pill at the right of the bar: rgba(0, 0, 0, 0.8) fill, 140px radius, white TWK Lausanne 500 15px label, an inset white hairline. It links to lemni.com/signup. Measured, never followed.',
    selector: 'nav a (Continue)',
  }, { noScroll: true });
  await S('logo', async () => {
    const ok = await page.evaluate(() => {
      const nav = document.querySelector('nav');
      if (!nav) return false;
      const el = nav.querySelector('[data-framer-name="Logo and Name"], [data-framer-name="Logo"], [data-framer-name="Logotype"]')
        || [...nav.querySelectorAll('a')].find((n) => {
          const r = n.getBoundingClientRect();
          return r.x < 280 && r.width > 16 && r.width < 160 && r.height > 12 && r.height < 48 && !(n.innerText || '').trim();
        });
      if (!el) return false;
      el.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, ['default'], {
    group: g, title: 'Wordmark', url,
    desc: 'The Lemni wordmark in the top bar.',
    selector: 'nav a (logo)',
  }, { noScroll: true });

  const h = 'Home';
  await S('hero-title', async () => page.locator('h1').first(), ['default'], {
    group: h, title: 'Hero title', url,
    desc: 'TWK Lausanne 250 at 94px, line-height 81.78px, letter-spacing -4.7px, colour rgb(227, 232, 255) on the dark ground.',
    selector: 'h1',
  });
  await S('hero-continue', async () => {
    const ok = await page.evaluate(() => {
      document.querySelectorAll('[data-m-mark]').forEach((n) => n.removeAttribute('data-m-mark'));
      const hits = [...document.querySelectorAll('a')].filter((a) => /Continue/.test(a.innerText || '') && a.getBoundingClientRect().y > 200 && a.getBoundingClientRect().width > 80);
      const el = hits[0];
      if (!el) return false;
      el.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, B4, {
    group: h, title: 'Hero Continue button', url,
    desc: 'The primary glass pill under the hero: black at 80% opacity, 140px radius, 40px tall, white label. Links to the sign-in shell. Measured, never followed.',
    selector: 'a (Continue, below the fold of the nav)',
  });
  await S('watch-video', byText('Watch Video', 'a'), B4, {
    group: h, title: 'Watch Video button', url,
    desc: 'The secondary pill beside Continue: rgba(28, 28, 38, 0.4), 40px radius, white label. A local control. Measured, not played.',
    selector: 'a (Watch Video)',
  });
  await S('feature-card', async () => {
    const ok = await page.evaluate(() => {
      document.querySelectorAll('[data-m-mark]').forEach((n) => n.removeAttribute('data-m-mark'));
      const el = [...document.querySelectorAll('[data-framer-name]')].find((n) => /Shadow$/.test(n.getAttribute('data-framer-name') || '') && n.getBoundingClientRect().width > 180 && n.getBoundingClientRect().height > 80);
      if (!el) return false;
      el.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, ['default'], {
    group: h, title: 'Product card', url,
    desc: 'A named product tile (Actions, Agents, Knowledge, Inbox) on the home page.',
    selector: '[data-framer-name$="Shadow"]',
  });
  await S('footer-link', async () => {
    await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
    await page.waitForTimeout(500);
    return mark(page, { text: 'Privacy', tags: 'a', exact: true });
  }, ['default', 'hover'], {
    group: h, title: 'Footer link', url,
    desc: 'A link in the bottom band (Privacy, Terms, Support, Brand). The page has no footer element; the band is a row of links.',
    selector: 'a (Privacy)',
  }, { noScroll: true });
  await page.close();
}

async function pricing() {
  await newPage('pricing', BASE + '/pricing');
  await sheetsFor('pricing');
  const url = BASE + '/pricing';
  await S('nav-light', async () => page.locator('nav').first(), ['default'], {
    group: 'Shell', title: 'Top bar, light (pricing)', url,
    desc: 'The same bar on a light page: ground rgb(246, 246, 248), resting links rgb(155, 155, 156), the current item black.',
    selector: 'nav',
  }, { noScroll: true });
  await S('pricing-title', async () => page.locator('h1, h2').first(), ['default'], {
    group: 'Pricing', title: 'Pricing headline', url,
    desc: 'TWK Lausanne 250 at 76px, black, letter-spacing -0.04em.',
    selector: 'h1, h2',
  });
  await S('price', byText('$98', 'span,p,div,h2,h3'), ['default'], {
    group: 'Pricing', title: 'Price figure', url,
    desc: 'The struck $196 sits in rgb(202, 202, 205); the current $98 is black, TWK Lausanne 400 at 46px.',
    selector: 'text $98',
  });
  await S('plan-cta', byText('Try For Free', 'a'), B4, {
    group: 'Pricing', title: 'Plan button', url,
    desc: 'A black pill, 40px radius, 40px tall, white TWK Lausanne 500 15px. Links to the sign-in shell. Measured, never followed.',
    selector: 'a (Try For Free)',
  });
  await page.close();
}

async function docs() {
  await newPage('docs', BASE + '/docs');
  await sheetsFor('docs');
  const url = BASE + '/docs';
  await S('docs-tabs', async () => {
    const ok = await page.evaluate(() => {
      document.querySelectorAll('[data-m-mark]').forEach((n) => n.removeAttribute('data-m-mark'));
      const el = [...document.querySelectorAll('a, div, button')].find((n) => (n.innerText || '').trim() === 'Basics' && n.getBoundingClientRect().y > 200 && n.getBoundingClientRect().y < 700);
      const box = el && (el.parentElement || el);
      if (!box) return false;
      box.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, ['default'], {
    group: 'Docs', title: 'Docs section tabs', url,
    desc: 'The horizontal section row under the Documentation title: Basics, Knowledge, Agents, Actions, Inbox. Basics is the current section, marked with a black underline.',
    selector: 'docs section row',
  });
  await S('docs-link', async () => mark(page, { text: 'Agents', tags: 'a', exact: false }), ['default', 'hover'], {
    group: 'Docs', title: 'Docs section link', url,
    desc: 'A public docs section. Measured at rest and hover. The agents page is also captured as docs-light-agents.png.',
    selector: 'a (Agents)',
  });
  await S('docs-side-link', async () => mark(page, { text: 'Overview', tags: 'a', exact: true }), ['default', 'hover'], {
    group: 'Docs', title: 'Docs page link', url,
    desc: 'A link in the left page list (Overview, Workplace, Members). Measured, never used to submit anything.',
    selector: 'a (Overview)',
  });
  await page.close();
}

async function signin() {
  await newPage('signin', APP + '/signup', { wait: 3500 });
  await sheetsFor('signin');
  const url = safeUrl(page.url()); // /signup redirects to /signin: record where the page landed
  await S('auth-title', async () => {
    const ok = await page.evaluate(() => {
      const el = [...document.querySelectorAll('h1, h2, div, p')].find((n) => (n.innerText || '').trim() === 'Welcome to Lemni');
      if (!el) return false;
      el.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, ['default'], {
    group: 'Auth shell', title: 'Sign-in title', url,
    desc: 'system-ui 32px / 500, black, on the light ground. The shell is the boundary: submitting the email or Continue with Google starts an account.',
    selector: 'Welcome to Lemni',
  }, { noScroll: true });
  await S('google-button', byText('Continue with Google', 'button, a, div'), B4, {
    group: 'Auth shell', title: 'Continue with Google', url,
    desc: 'The OAuth entry. Measured at rest, hover, focus and a forced press. Never clicked.',
    selector: 'Continue with Google',
  }, { noScroll: true });
  await S('email-field', async () => page.locator('input[type="email"], input').first(), ['default', 'hover', 'focus-visible', 'focused'], {
    group: 'Auth shell', title: 'Email field', url,
    desc: '360 by 44, 12px radius, white at 50% opacity, placeholder "Email…". Photographed empty. Nothing was typed. Nothing was submitted.',
    selector: 'input',
  }, { noScroll: true });
  await S('auth-continue', async () => {
    const ok = await page.evaluate(() => {
      document.querySelectorAll('[data-m-mark]').forEach((n) => n.removeAttribute('data-m-mark'));
      const el = [...document.querySelectorAll('button, a, div')].find((n) => {
        const t = (n.innerText || '').replace(/\s+/g, ' ').trim();
        const r = n.getBoundingClientRect();
        return t === 'Continue' && r.width > 200 && r.height > 30 && r.y > 400;
      });
      if (!el) return false;
      el.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, ['default', 'hover', 'focus-visible', 'pressed'], {
    group: 'Auth shell', title: 'Continue (auth)', url,
    desc: 'The black submit control under the email field. Measured, never clicked, so no account was created.',
    selector: 'Continue (auth card)',
  }, { noScroll: true });
  await page.close();
}

async function mobile() {
  await newPage('mobile-home', BASE + '/', { mobile: true });
  const url = BASE + '/';
  await S('nav-mobile', async () => page.locator('nav').first(), ['default'], {
    group: 'Mobile', title: 'Phone top bar', url,
    desc: 'The dark home bar at 390 wide: wordmark and a menu control, 64px tall.',
    selector: 'nav',
  }, { noScroll: true });
  await S('menu-button', async () => {
    const ok = await page.evaluate(() => {
      const nav = document.querySelector('nav');
      if (!nav) return false;
      const cand = [...nav.querySelectorAll('a, button, div')].filter((n) => {
        const r = n.getBoundingClientRect();
        return r.width >= 16 && r.width <= 64 && r.height >= 16 && r.height <= 64 && r.x > 250 && !(n.innerText || '').trim();
      });
      const el = cand[cand.length - 1];
      if (!el) return false;
      el.setAttribute('data-m-mark', '1');
      return true;
    });
    return ok ? page.locator('[data-m-mark="1"]') : null;
  }, ['default'], {
    group: 'Mobile', title: 'Phone menu button', url,
    desc: 'The icon control at the right of the phone bar. Opening it is a local toggle, captured as mobile-home-dark-menu-open.png.',
    selector: 'nav icon control',
  }, { noScroll: true });
  await page.close();
}

browser = await launch().then((x) => x.browser);
const jobs = { home, pricing, docs, signin, mobile };
try {
  for (const [name, fn] of Object.entries(jobs)) {
    if (ONLY.length && !ONLY.includes(name)) continue;
    await fn();
  }
} finally {
  save();
  if (context) await context.close().catch(() => {});
  await browser.close();
}
log('wrote', OUT, Object.keys(out.components).length, 'components');
