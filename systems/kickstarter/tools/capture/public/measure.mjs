// Measures kickstarter.com's public components without signing in, pledging or submitting.
//
//   PLAYWRIGHT=... node measure.mjs [home,discover,project,login,start,mobile]
//
// Headed Chrome. Consent is hidden, never clicked. Writes raw/components-computed.json
// and one crop per component and state into components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, CROPS, RAW, centre, crop, hideConsent, launchBrowser, newContext, open, styleOf } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const arg = (process.argv[2] || '').split(',').filter(Boolean);
const want = (k) => !arg.length || arg.includes(k);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { _meta: {}, components: {} };
out._meta ??= {};
out.components ??= {};
const RUN = new Date().toLocaleDateString('en-CA');   // the local run date

const browser = await launchBrowser();
let page, cdp, context, current;

async function go(key, url, { mobile = false } = {}) {
  if (context) await context.close().catch(() => {});
  context = await newContext(browser, { mobile, dpr: mobile ? 2 : 1 });
  page = await context.newPage();
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = key;
  log('open', key, url);
  const ok = await open(page, url.startsWith('http') ? url : BASE + url, { wait: 1600 });
  if (!ok) log('  CHALLENGE', key);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return ok;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.mouse.move(8, 8);
  await page.waitForTimeout(200);
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
  await page.waitForTimeout(250);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function shot(loc, key, state) {
  const file = path.join(CROPS, `${key}-${state}.png`);
  await crop(loc, file, { pad: 6 });
  return `components/crops/${key}-${state}.png`;
}

async function S(key, loc, states, meta) {
  // fillText is an option for the filled state, not part of the component record.
  const { fillText = 'name@example.com', ...record } = meta || {};
  const c = out.components[key] ??= { states: {} };
  Object.assign(c, { page: current, run: RUN, url: page.url().split('?')[0], ...record });
  delete c.fillText;
  c.states ??= {};
  const target = loc.first();
  if (!(await target.count())) {
    log('  ! missing', key);
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
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(target);
      } else if (st === 'pressed') {
        undo = await forcePseudo(target, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await target.click({ timeout: 4000 }).catch(() => target.evaluate((el) => el.focus()));
        await page.waitForTimeout(250);
        via = 'clicked into the field, nothing submitted';
      } else if (st === 'filled') {
        await target.click({ timeout: 4000 }).catch(() => target.evaluate((el) => el.focus()));
        await page.keyboard.type(fillText, { delay: 8 });
        await page.waitForTimeout(200);
        undo = async () => {
          await target.focus();
          await page.keyboard.press('Meta+a').catch(() => {});
          await page.keyboard.press('Backspace');
        };
        via = `typed ${fillText}, then deleted; nothing sent`;
      }
      const s = await styleOf(target);
      const cropPath = await shot(target, key, st);
      c.states[st] = { ...s, crop: cropPath, via, run: RUN };
      delete c.missing;
      log('  ', key, st, `${s.rect.w}x${s.rect.h}`, s.style?.backgroundColor, s.style?.color);
    } catch (e) {
      // A failed re-measure keeps the earlier reading and notes the error, so a rerun never
      // replaces a good state with an error.
      const err = String(e.message || e).slice(0, 180);
      const prev = c.states[st];
      c.states[st] = prev && !prev.error ? { ...prev, recaptureError: err, recaptureRun: RUN } : { error: err };
      log('  !', key, st, String(e.message).slice(0, 100));
    }
    if (undo) await undo().catch(() => {});
  }
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
}

const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function projectPath() {
  const file = path.join(process.env.HOME, '.design-systems', 'kickstarter', 'raw-shots', 'project-path.txt');
  if (fs.existsSync(file)) return fs.readFileSync(file, 'utf8').trim();
  return '/projects/shirtaloon/hwfwm';
}

async function home() {
  if (!want('home')) return;
  await go('home', '/');
  await S('logo', page.locator('a[aria-label="Kickstarter"], a.global-nav-ksr-logo, header a').first(), ['default'], {
    group: 'Site chrome', title: 'Wordmark', desc: 'Green KICKSTARTER wordmark in the header.',
  });
  await S('nav-login', page.getByRole('button', { name: 'Log in' }).first(), B4, {
    group: 'Site chrome', title: 'Log in', desc: 'Header text button. Measured, never activated.',
  });
  await S('nav-creators', page.getByRole('link', { name: 'For creators' }).first(), B4, {
    group: 'Site chrome', title: 'For creators', desc: 'Outlined header link to the creator resources page.',
  });
  await S('nav-category', page.locator('a').filter({ hasText: /^Games$/ }).first(), B4, {
    group: 'Site chrome', title: 'Category link', desc: 'A category in the horizontal nav.',
  });
  await S('search', page.locator('input[aria-label*="Search"], input[placeholder*="Search"]').first(), ['default', 'hover', 'focused', 'filled'], {
    group: 'Site chrome', title: 'Search field', desc: 'Header search. Typed into and cleared; never submitted.',
    fillText: 'camera',
  });
  // search fill uses the generic filled text; override via a second pass is fine
  await S('hero-h1', page.locator('h1').first(), ['default'], {
    group: 'Home', title: 'Hero heading', desc: 'The home page headline.',
  });
  await S('banner-cta', page.getByRole('link', { name: /Explore the app/i }).first(), B4, {
    group: 'Home', title: 'Banner button', desc: 'White pill on the editorial banner. Not followed.',
  });
  await S('project-card', page.locator('a[href*="/projects/"]').filter({ has: page.locator('img') }).first(), ['default', 'hover'], {
    group: 'Home', title: 'Project card', desc: 'A project card on the home rail. The link was not followed from this control.',
  });
  await S('save-btn', page.getByRole('button', { name: /Save this project/i }).first(), B4, {
    group: 'Home', title: 'Save', desc: 'Bookmark control on a card. Measured, never activated (save requires an account).',
  });
  await S('footer-link', page.locator('footer a, #global-footer a').first(), ['default', 'hover', 'focus-visible'], {
    group: 'Footer', title: 'Footer link', desc: 'A link in the global footer.',
  });
}

async function discover() {
  if (!want('discover')) return;
  await go('discover', '/discover?ref=nav');
  await S('filter-show-more', page.getByRole('button', { name: 'Show more' }).first(), B4, {
    group: 'Discover', title: 'Show more', desc: 'Expands a filter group. A local toggle, not a submission.',
  });
  await S('discover-card', page.locator('a[href*="/projects/"]').first(), ['default', 'hover'], {
    group: 'Discover', title: 'Discover card', desc: 'A project result on Discover.',
  });
  await S('filter-toggle', page.getByRole('button', { name: 'Toggle options' }).first(), B4, {
    group: 'Discover', title: 'Filter toggle', desc: 'Opens a filter control. Not a form submit.',
  });
}

async function project() {
  if (!want('project')) return;
  const pth = await projectPath();
  await go('project', pth);
  await S('project-h1', page.locator('h1').first(), ['default'], {
    group: 'Project', title: 'Project title', desc: 'The public campaign title.',
  });
  await S('pledge-btn', page.getByRole('link', { name: /Back this project|Pledge/i }).or(page.getByRole('button', { name: /Back this project|Pledge/i })).first(), B4, {
    group: 'Project', title: 'Back this project', desc: 'Primary pledge control. Measured, never followed. Checkout is gated.',
  });
  await S('reward-card', page.locator('[class*="reward"], [data-testid*="reward"]').filter({ hasText: /\$|pledge|Reward/i }).first(), ['default'], {
    group: 'Project', title: 'Reward', desc: 'A public reward tier. Not selected.',
  });
  await S('tab-campaign', page.getByRole('link', { name: /^Campaign$/ }).or(page.getByRole('tab', { name: /Campaign/i })).first(), ['default', 'hover', 'focus-visible'], {
    group: 'Project', title: 'Campaign tab', desc: 'A section tab on the project page.',
  });
  await S('progress', page.locator('[class*="progress"], [role="progressbar"]').first(), ['default'], {
    group: 'Project', title: 'Funding meter', desc: 'The green funding bar.',
  });
  await S('creator-avatar', page.locator('a[href*="/profile/"] img, img[alt*="avatar" i], [class*="avatar"] img').first(), ['default'], {
    group: 'Project', title: 'Creator avatar', desc: 'The creator portrait on the public campaign.',
  });
}

async function login() {
  if (!want('login')) return;
  await go('login', '/login');
  await S('login-h1', page.locator('h1').first(), ['default'], {
    group: 'Auth boundary', title: 'Log in heading', desc: 'The signed-out auth shell. Nothing was submitted.',
  });
  await S('login-email', page.locator('input[name="passwordless-email"], input[type="email"]').first(), ['default', 'hover', 'focused', 'filled'], {
    group: 'Auth boundary', title: 'Email field', desc: 'Passwordless email. Typed into and cleared; Continue was never pressed.',
  });
  await S('login-continue', page.getByRole('button', { name: 'Continue' }).first(), B4, {
    group: 'Auth boundary', title: 'Continue', desc: 'Submits the email step. Measured in every state, never pressed.',
  });
  await S('login-apple', page.getByRole('button', { name: /Apple/i }).first(), B4, {
    group: 'Auth boundary', title: 'Sign in with Apple', desc: 'OAuth button. Never followed.',
  });
  await S('login-checkbox', page.locator('input[type="checkbox"]').first(), ['default', 'focus-visible'], {
    group: 'Auth boundary', title: 'Remember checkbox', desc: 'The remember-me checkbox. Not toggled into a submit.',
  });
  await S('login-link', page.getByRole('link', { name: /Facebook account recovery/i }).first(), ['default', 'hover', 'focus-visible'], {
    group: 'Auth boundary', title: 'Recovery link', desc: 'A text link on the auth shell. Not followed.',
  });
}

async function start() {
  if (!want('start')) return;
  await go('start', '/start');
  await S('start-h1', page.locator('h1').first(), ['default'], {
    group: 'Start a project', title: 'Setup heading', desc: 'The public first step of project creation. Next was never pressed.',
  });
  await S('start-select', page.locator('select').first(), ['default', 'hover', 'focus-visible'], {
    group: 'Start a project', title: 'Category select', desc: 'Primary category select. Not changed into a submission.',
  });
  await S('start-next', page.getByRole('button', { name: /Next/i }).first(), B4, {
    group: 'Start a project', title: 'Next', desc: 'Advances the wizard. Measured, never pressed.',
  });
}

async function mobile() {
  if (!want('mobile')) return;
  await go('mobile', '/', { mobile: true });
  await S('m-login', page.getByRole('button', { name: 'Log in' }).or(page.getByRole('link', { name: 'Log in' })).first(), ['default'], {
    group: 'Mobile', title: 'Log in (phone)', desc: 'Header login at 390. Not activated.',
  });
  await S('m-search', page.locator('input[aria-label*="Search"], input[placeholder*="Search"]').first(), ['default'], {
    group: 'Mobile', title: 'Search (phone)', desc: 'Search field at 390.',
  });
  const menu = page.locator('[aria-label="Open menu"], [aria-label="Menu"], button[aria-label*="menu" i]').first();
  if (await menu.count()) {
    await menu.click().catch(() => {});
    await page.waitForTimeout(600);
    await hideConsent(page);
    await S('m-menu', menu, ['default'], {
      group: 'Mobile', title: 'Menu button', desc: 'Opens the phone navigation. A local toggle.',
    });
  }
}

out._meta.read = RUN;
out._meta.source = 'headed Chrome, signed out, consent hidden never clicked';
await home();
await discover();
await project();
await login();
await start();
await mobile();
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const n = Object.keys(out.components).length;
const states = Object.values(out.components).reduce((a, c) => a + Object.keys(c.states || {}).length, 0);
log('done', n, 'components', states, 'states');
await browser.close();
