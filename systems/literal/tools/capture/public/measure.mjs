// Measures literal.club's public components without signing in or submitting.
//
//   PLAYWRIGHT=... CDP=http://127.0.0.1:9339 node measure.mjs [home,signin,book,profile,explore,mobile]
//
// Attaches over CDP to a Chrome started with a throwaway profile (see lib.mjs);
// every page opens in a fresh context. A Cloudflare challenge is a boundary:
// the page is skipped, never solved. Consent is hidden.
// Sign in, Join, Continue, Apple, Want to read, Follow, Like and Comment
// are measured, never activated. Email and password are not typed into.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, CROPS, RAW, centre, crop, hideConsent, launchBrowser, newPage, open, styleOf } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const arg = (process.argv[2] || '').split(',').filter(Boolean);
const want = (k) => !arg.length || arg.includes(k);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { _meta: {}, components: {} };
out._meta ??= {};
out.components ??= {};
const RUN = new Date().toLocaleDateString('en-CA');
// _meta.read keeps the earlier date until this run reads a state, so a rerun that
// fails throughout never redates old readings; _meta.lastAttempt is this run's
// date. Each state carries its own `run` date, and the component's `run` moves
// only when one of its states is read.
const PRIOR_READ = out._meta.read;
const BOOK = '/book/the-midnight-library-mrpx0';
const PROFILE = '/kikimeower';

const browser = await launchBrowser();
let page, cdp, current, theme = 'light';

async function go(key, url, { mobile = false, colorScheme = 'light' } = {}) {
  if (page) await page.close().catch(() => {});
  page = await newPage({ browser, width: mobile ? 390 : 1440, height: mobile ? 844 : 900, colorScheme });
  cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = key;
  theme = colorScheme;
  log('open', key, colorScheme, url);
  // open() throws when a bot check is still showing: recorded as a boundary, not bypassed.
  const ok = await open(page, url.startsWith('http') ? url : BASE + url, { wait: 1200 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return ok;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.mouse.move(8, 8);
  await page.waitForTimeout(180);
  await hideConsent(page);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  }
  await page.waitForTimeout(220);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(200);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function shot(loc, key, state) {
  const file = path.join(CROPS, `${key}-${state}.png`);
  await crop(loc, file, { pad: 6 });
  return `components/crops/${key}-${state}.png`;
}

async function S(key, loc, states, meta) {
  const c = out.components[key] ??= { states: {} };
  Object.assign(c, { page: current, theme, url: page.url().split('?')[0], ...meta });
  c.states ??= {};
  const target = loc.first();
  if (!(await target.count())) {
    log('  ! missing', key);
    c.missing = true;
    return;
  }
  const box = await target.boundingBox();
  if (!box || box.width < 2 || box.height < 2) {
    log('  ! offscreen', key);
    c.missing = true;
    return;
  }
  for (const st of states) {
    let undo;
    let via = 'at rest';
    try {
      await reset();
      await centre(target);
      if (st === 'hover') {
        await target.hover({ timeout: 4000 }).catch(() => target.hover({ force: true }));
        await page.waitForTimeout(250);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(target);
      } else if (st === 'pressed') {
        undo = await forcePseudo(target, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await target.click({ timeout: 4000 }).catch(() => target.evaluate((el) => el.focus()));
        await page.waitForTimeout(200);
        via = 'clicked into the field, nothing typed, nothing submitted';
      }
      const s = await styleOf(target);
      const cropPath = await shot(target, key, st);
      c.states[st] = { ...s, crop: cropPath, via, run: RUN };
      c.run = RUN;
      out._meta.read = RUN; // a reading succeeded in this run
      delete c.missing;
      log('  ', key, st, `${s.rect.w}x${s.rect.h}`, s.style?.backgroundColor, s.style?.color);
    } catch (e) {
      // Keep an earlier good reading and say the rerun failed, rather than
      // writing the error over it.
      const msg = String(e.message || e).slice(0, 180);
      const prev = c.states[st];
      c.states[st] = prev && !prev.error ? { ...prev, recaptureError: msg, recaptureRun: RUN } : { error: msg, run: RUN };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
  }
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
}

const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function home() {
  if (!want('home')) return;
  await go('home', '/');
  await S('logo', page.locator('header a[class*="LogoLink"]').first(), ['default'], {
    group: 'Site chrome', title: 'Wordmark', desc: 'Literal* wordmark in the header. Links home.',
  });
  await S('nav-explore', page.locator('header a[href="/explore"]').first(), B4, {
    group: 'Site chrome', title: 'Explore', desc: 'Header text link. Measured, never followed from this shot.',
  });
  await S('nav-signin', page.locator('header a[href^="/signin"]').first(), B4, {
    group: 'Site chrome', title: 'Sign in', desc: 'Header text link to the sign-in card. Measured, never activated.',
  });
  await S('nav-join', page.locator('header a[href="/register"]').first(), B4, {
    group: 'Site chrome', title: 'Join', desc: 'Green header action. Measured, never followed.',
  });
  await S('search', page.locator('input[name="query"]').first(), ['default', 'hover', 'focused'], {
    group: 'Site chrome', title: 'Search', desc: 'Header search field. Focused, nothing typed, nothing submitted.',
  });
  await S('hero-title', page.locator('h1').first(), ['default'], {
    group: 'Marketing', title: 'Hero title', desc: 'Libre Baskerville headline on the home page.',
  });
  await S('join-free', page.locator('a[href="/register"]').filter({ hasText: 'Join for free' }).first(), B4, {
    group: 'Marketing', title: 'Join for free', desc: 'Hero primary action. Measured, never followed.',
  });
  await S('app-store', page.locator('a[href*="apps.apple.com"]').first(), ['default', 'hover'], {
    group: 'Marketing', title: 'App Store badge', desc: 'Black App Store badge beside Join for free.',
  });
}

async function signin() {
  if (!want('signin')) return;
  await go('signin', '/signin');
  await S('signin-title', page.locator('h1').first(), ['default'], {
    group: 'Sign-in card', title: 'Sign in heading', desc: 'Libre Baskerville heading on the sign-in card. The form was not submitted.',
  });
  await S('email-field', page.getByPlaceholder('Email address').first(), ['default', 'hover', 'focused'], {
    group: 'Sign-in card', title: 'Email field', desc: 'Email address field. Focused, nothing typed, nothing submitted.',
  });
  await S('password-field', page.getByPlaceholder('Password').first(), ['default', 'focused'], {
    group: 'Sign-in card', title: 'Password field', desc: 'Password field. Focused, nothing typed, nothing submitted.',
  });
  await S('forgot', page.getByRole('link', { name: 'Forgot password?' }).first(), B4, {
    group: 'Sign-in card', title: 'Forgot password', desc: 'Text link. Not followed. Password reset was not started.',
  });
  await S('signin-submit', page.locator('form button, button').filter({ hasText: /^Sign in$/ }).first(), B4, {
    group: 'Sign-in card', title: 'Sign in button', desc: 'Primary submit. Measured in hover, focus and pressed. Never activated.',
  });
  await S('apple', page.getByRole('button', { name: /Apple/ }).first(), B4, {
    group: 'Sign-in card', title: 'Sign in with Apple', desc: 'OAuth button. Measured, never activated.',
  });
  await S('signup-link', page.getByRole('link', { name: 'Sign up' }).first(), ['default', 'hover', 'focus-visible'], {
    group: 'Sign-in card', title: 'Sign up link', desc: 'Inline link under the card. Not followed from this measurement.',
  });
}

async function book() {
  if (!want('book')) return;
  await go('book', BOOK);
  await S('book-title', page.locator('h1').first(), ['default'], {
    group: 'Book page', title: 'Book title', desc: 'Libre Baskerville title on a public book page.',
  });
  await S('want-to-read', page.getByRole('button', { name: 'Want to read' }).first(), B4, {
    group: 'Book page', title: 'Want to read', desc: 'Shelf action. Measured, never activated. Adding a book needs an account.',
  });
  await S('show-more', page.locator('[class*="Collapsable_button"]').first(), ['default', 'hover', 'focus-visible'], {
    group: 'Book page', title: 'Show more', desc: 'Expands the synopsis. A local toggle, not a submission.',
  });
  await S('review-like', page.getByRole('button', { name: 'Like' }).first(), ['default', 'hover'], {
    group: 'Book page', title: 'Like', desc: 'Review reaction. Measured, never activated. Liking needs an account.',
  });
  await S('review-comment', page.getByRole('button', { name: 'Comment' }).first(), ['default', 'hover'], {
    group: 'Book page', title: 'Comment', desc: 'Review comment control. Measured, never activated.',
  });
  await S('author-link', page.locator('a').filter({ hasText: 'Matt Haig' }).first(), ['default', 'hover'], {
    group: 'Book page', title: 'Author link', desc: 'Author name under the title.',
  });
}

async function profile() {
  if (!want('profile')) return;
  await go('profile', PROFILE);
  await S('follow', page.locator('button').filter({ hasText: /^Follow$/ }).first(), B4, {
    group: 'Profile', title: 'Follow', desc: 'Follow on a public profile. Measured, never activated. Following needs an account.',
  });
  await S('profile-tab', page.getByRole('link', { name: 'Books' }).or(page.getByRole('button', { name: 'Books' })).first(), ['default', 'hover'], {
    group: 'Profile', title: 'Books tab', desc: 'Shelf tab on a public profile.',
  });
  await S('avatar', page.locator('img').filter({ hasNot: page.locator('header img') }).first(), ['default'], {
    group: 'Profile', title: 'Avatar', desc: 'Public profile picture as the product shows it.',
  });
}

async function explore() {
  if (!want('explore')) return;
  await go('explore', '/explore');
  await S('book-card', page.locator('a[href^="/book/"]').first(), ['default', 'hover'], {
    group: 'Explore', title: 'Book card', desc: 'A trending book card. Hovered, not opened from this measurement.',
  });
}

async function mobile() {
  if (!want('mobile')) return;
  await go('mobile-home', '/', { mobile: true });
  await S('m-join', page.locator('header a[href="/register"]').first(), ['default'], {
    group: 'Mobile', title: 'Join', desc: 'Header Join at 390. Measured, never followed.',
  });
  await S('m-search', page.locator('input[name="query"]').first(), ['default'], {
    group: 'Mobile', title: 'Search', desc: 'Search icon field in the 390 header.',
  });
  await S('m-hero', page.locator('h1').first(), ['default'], {
    group: 'Mobile', title: 'Hero title', desc: 'Hero headline at 390.',
  });
}

async function dark() {
  if (!want('dark')) return;
  await go('home-dark', '/', { colorScheme: 'dark' });
  await S('nav-join-dark', page.locator('header a[href="/register"]').first(), ['default', 'hover'], {
    group: 'Dark theme', title: 'Join', desc: 'Same Join control with prefers-color-scheme dark. The public site has no theme toggle; dark is the system preference.',
  });
  await S('hero-title-dark', page.locator('h1').first(), ['default'], {
    group: 'Dark theme', title: 'Hero title', desc: 'Hero headline on the dark page.',
  });
  await go('signin-dark', '/signin', { colorScheme: 'dark' });
  await S('signin-submit-dark', page.locator('button').filter({ hasText: /^Sign in$/ }).first(), ['default', 'hover'], {
    group: 'Dark theme', title: 'Sign in button', desc: 'Primary submit in dark. Measured, never activated.',
  });
  await S('email-field-dark', page.getByPlaceholder('Email address').first(), ['default'], {
    group: 'Dark theme', title: 'Email field', desc: 'Email field in dark. Nothing typed.',
  });
}

out._meta = {
  read: PRIOR_READ || RUN,
  lastAttempt: RUN,
  product: 'Literal.club',
  route: 'public-web',
  viewport: '1440x900 desktop, 390x844 mobile',
  note: 'Signed out. Sign in, Join, Continue, Apple, Want to read, Follow, Like and Comment were measured and never activated. Email and password were not typed into. Dark is prefers-color-scheme, not a clicked toggle.',
};
// One page that fails (a bot check left showing, a missing control) is logged
// and skipped; the others still run and are saved.
const failedPages = [];
for (const run of [home, signin, book, profile, explore, mobile, dark]) {
  try { await run(); } catch (e) {
    const why = String(e.message || e).split('\n')[0].slice(0, 180);
    failedPages.push({ page: run.name, error: why });
    log('PAGE FAILED', run.name, why);
  }
}
// The file says which pages this run could not read; their earlier readings are kept.
if (failedPages.length) out._meta.failedPages = failedPages;
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, Object.keys(out.components).length, 'components');
if (page) await page.close().catch(() => {});
await browser.close();
if (failedPages.length) { console.error(`${failedPages.length} page(s) failed; their earlier readings were kept`); process.exit(1); }
