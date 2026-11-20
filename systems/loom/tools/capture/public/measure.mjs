// Measures Loom public components. Nothing is submitted, signed into, or purchased.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, SHARE, launch, open, styleOf, crop, centre, RAW, hideConsent } from './lib.mjs';
import { datePrior } from '../merge-dates.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Start from the committed readings: a run that fails part-way keeps every
// component it did not reach, and a state that errors keeps its prior reading.
// _meta.captured is this run's date; every state carries its own `read` date, so
// a reading kept from an earlier run keeps the date it was taken (merge-dates.mjs).
const prior = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : null;
const RUN = new Date().toLocaleDateString('en-CA');
const out = {
  _meta: {
    product: 'Loom',
    captured: RUN, // the local date of the latest run; per-state dates are under states.*.read
    route: 'public-web',
    theme: 'light',
    note: 'Signed-out marketing, pricing, login wall, and one public share page. SSO, signup Continue, checkout and recording were not pressed.',
  },
  components: datePrior((prior && prior.components) || {}, prior && prior._meta && prior._meta.captured),
};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, context, browser, cdp, current;

async function newPage(url) {
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  current = url;
  log('open', url);
  await open(page, url, { wait: 2000 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await hideConsent(page);
}

async function reset() {
  await page.mouse.move(8, 8).catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.waitForTimeout(120);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  const ok = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement));
  await page.waitForTimeout(180);
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(200);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(key, state, loc, meta, via) {
  const c = (out.components[key] ??= { states: {}, ...meta, url: current });
  c.states ??= {};
  try {
    await centre(loc);
    const s = await styleOf(loc);
    let file;
    try { file = await crop(page, loc, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
    c.states[state] = { ...s, crop: file, via, read: RUN };
    // A state read now supersedes an earlier run's "not captured" marker for it.
    if (c.notCaptured && c.notCaptured[state]) {
      delete c.notCaptured[state];
      if (!Object.keys(c.notCaptured).length) delete c.notCaptured;
    }
    log(' ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.style?.backgroundColor, s.style?.color);
  } catch (e) {
    const msg = String(e.message).slice(0, 180);
    const old = c.states[state];
    // A kept reading keeps its own read date; the failed attempt is dated apart.
    c.states[state] = old && !old.error ? { ...old, recaptureError: msg, recaptureRun: RUN } : { error: msg, via, read: RUN };
    log(' !', key, state, String(e.message).slice(0, 120));
  }
}

async function states(key, loc, list, meta) {
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    log(' ! missing', key);
    if (out.components[key] && !out.components[key].missing) out.components[key].recaptureMissed = RUN;
    else out.components[key] = { missing: true, ...meta, url: current, states: {} };
    return;
  }
  for (const st of list) {
    await reset();
    let undo, via = 'at rest';
    if (st === 'hover') { await target.hover({ timeout: 4000 }).catch(() => {}); via = 'mouse hover'; await page.waitForTimeout(250); }
    else if (st === 'focus-visible') {
      via = await kbFocus(target);
      if (String(via).includes('failed')) {
        // Recorded as not captured, never as a reading of the element at rest.
        log(' !', key, 'focus-visible not captured:', via);
        const c = (out.components[key] ??= { states: {}, ...meta, url: current });
        delete c.states[st];
        c.notCaptured = { ...(c.notCaptured || {}), [st]: { via, note: 'Keyboard focus did not land. The crop is the unfocused control and is not a focus sample.' } };
        continue;
      }
    }
    else if (st === 'pressed') { undo = await forcePseudo(target, ['active', 'hover']); via = 'CDP forcePseudoState :active:hover; no click'; }
    else if (st === 'focused') { await target.click({ timeout: 4000 }); via = 'clicked into the field; nothing submitted'; await page.waitForTimeout(180); }
    await record(key, st, target, meta, via);
    if (undo) await undo();
    await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((el) => el.removeAttribute('data-m-force'))).catch(() => {});
  }
}

async function mark(selector, attr) {
  return page.evaluate(({ selector, attr }) => {
    const el = document.querySelector(selector);
    if (!el) return false;
    el.setAttribute(attr, '1');
    return true;
  }, { selector, attr });
}

({ browser, context } = await launch({ width: 1440, height: 900, dpr: 2 }));

try {
  await newPage(BASE + '/');
  await states('primary-cta', page.locator('header a, nav a').filter({ hasText: 'Get Loom for free' }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { role: 'button', where: 'home nav' });
  await states('nav-link', page.getByRole('link', { name: 'Pricing', exact: true }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { role: 'link', where: 'home nav' });
  await states('nav-menu', page.locator('header button, nav button').filter({ hasText: /^Solutions$/ }).first(), ['default', 'hover', 'focus-visible'], { role: 'button', where: 'home nav' });
  const apps = page.locator('header button, nav button').filter({ hasText: /^Apps$/ }).first();
  await apps.hover().catch(() => {});
  await page.waitForTimeout(400);
  await states('menu-panel', page.locator('[class*="NewSubnav_menu"]').first(), ['default'], { role: 'menu', where: 'Apps menu' });
  await states('menu-item', page.locator('[class*="NewSubnav_menu"] a').filter({ hasText: 'Screen Recorder' }).first(), ['default', 'hover'], { role: 'link', where: 'Apps menu row' });
  await states('quiet-cta', page.getByRole('link', { name: 'Install Chrome Extension' }).first(), ['default', 'hover', 'focus-visible'], { role: 'link', where: 'home hero' });
  await page.keyboard.press('Escape').catch(() => {});
  await states('text-link', page.getByRole('link', { name: 'Chrome extension' }).first(), ['default', 'hover', 'focus-visible'], { role: 'link', where: 'home hero' });
  await states('hero-title', page.locator('h1').first(), ['default'], { role: 'display', where: 'home' });
  await states('body-copy', page.locator('main p, section p').filter({ hasText: /.{40,}/ }).first(), ['default'], { role: 'body', where: 'home' });
  save();

  await page.close();
  await newPage(BASE + '/pricing');
  await states('plan-card', page.locator('h2, h3').filter({ hasText: /^Starter$/ }).locator('xpath=ancestor::*[self::article or self::div][1]'), ['default'], { role: 'card', where: 'pricing Starter' });
  await states('plan-cta', page.locator('a').filter({ hasText: /^Sign up$/ }).first(), ['default', 'hover', 'focus-visible'], { role: 'link', where: 'pricing Starter; not followed' });
  await states('popular-cta', page.locator('a').filter({ hasText: /^Try for free$/ }).last(), ['default', 'hover'], { role: 'link', where: 'pricing Business + AI filled action; not followed' });
  await states('badge', page.getByText('MOST POPULAR', { exact: true }).first(), ['default'], { role: 'badge', where: 'pricing Business + AI' });
  const team = page.locator('input[type="number"], input[inputmode="numeric"], input[aria-label*="team" i], input[name*="team" i], input[name*="seat" i]').first();
  if (await team.count()) await states('team-size', team, ['default', 'focused'], { role: 'text field', where: 'pricing team size; value not changed and not submitted' });
  else log(' ! no team-size input');
  const annual = page.getByRole('radio', { name: /Annually/i }).first();
  if (await annual.count()) {
    await states('billing-monthly', page.getByRole('radio', { name: /Monthly/i }).first(), ['default'], { role: 'radio', where: 'pricing; selected' });
    await states('billing-annual', annual, ['default', 'hover'], { role: 'radio', where: 'pricing; not selected' });
  } else log(' ! no billing radios');
  const faq = page.locator('button, summary').filter({ hasText: /\?$/ }).first();
  if (await faq.count()) {
    await states('faq', faq, ['default', 'hover'], { role: 'disclosure', where: 'pricing' });
    await faq.click().catch(() => {});
    await page.waitForTimeout(300);
    await record('faq', 'opened', faq, { role: 'disclosure', where: 'pricing' }, 'clicked the question; no form submitted');
  }
  save();

  await page.close();
  await newPage(BASE + '/login');
  await states('email-field', page.locator('#email'), ['default', 'focused'], { role: 'text field', where: 'login wall' });
  await page.locator('#email').fill('capture@example.com');
  await page.waitForTimeout(150);
  await record('email-field', 'filled', page.locator('#email'), { role: 'text field', where: 'login wall' }, 'typed a placeholder address; Continue was not pressed');
  await page.locator('#email').fill('');
  await states('sso-google', page.getByRole('button', { name: 'Log in with Google' }).first(), ['default', 'hover', 'focus-visible'], { role: 'button', where: 'login wall; not pressed' });
  await states('continue-button', page.getByRole('button', { name: 'Continue', exact: true }).first(), ['default', 'hover', 'focus-visible', 'pressed'], { role: 'button', where: 'login wall; pressed is forced :active, not a click' });
  save();

  await page.close();
  await newPage(SHARE);
  await states('reaction', page.getByRole('button', { name: '👍' }).first(), ['default', 'hover'], { role: 'icon button', where: 'public share; not pressed so no reaction is sent' });
  await states('copy-link', page.getByRole('button', { name: 'Copy link' }).first(), ['default', 'hover', 'focus-visible'], { role: 'button', where: 'public share; not clicked' });
  await states('share-tab', page.getByRole('button', { name: 'Transcript' }).first(), ['default', 'hover'], { role: 'tab', where: 'public share' });
  const play = page.getByRole('button', { name: /play/i }).first();
  if (await play.count()) await states('play-button', play, ['default', 'hover'], { role: 'icon button', where: 'public share player' });
  save();

  await page.close();
  await newPage(BASE + '/ai');
  await states('secondary-cta', page.getByRole('link', { name: /Get Loom|Try/i }).first(), ['default', 'hover'], { role: 'link', where: 'ai page' });
  save();
} finally {
  save();
  await browser.close();
}
log('wrote', OUT);
