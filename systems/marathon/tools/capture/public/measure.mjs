// Measures Marathon's public components. Nothing is submitted. Sign-in and
// register redirect to / and are recorded as redirects, not as forms.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, RAW, CROPS, PROPS } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const out = { _meta: { product: 'Marathon', base: BASE, captured: new Date().toISOString() }, components: {} };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

// One DevTools session per page, reused by every press on it (a new one per call was never detached).
const sessions = new WeakMap();
async function session(page) {
  if (!sessions.has(page)) {
    const cdp = await page.context().newCDPSession(page);
    await cdp.send('DOM.enable');
    await cdp.send('CSS.enable');
    sessions.set(page, cdp);
  }
  return sessions.get(page);
}

async function forcePseudo(page, loc, classes) {
  const cdp = await session(page);
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(250);
  return async () => {
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
    await loc.evaluate((el) => el.removeAttribute('data-m-force')).catch(() => {});
  };
}

async function record(page, name, state, loc, extra = {}) {
  const n = await loc.count();
  if (!n) {
    log('  miss', name, state);
    out.components[name] ??= {};
    out.components[name][state] = { missing: true, ...extra };
    return;
  }
  const target = loc.first();
  await target.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const reading = await styleOf(target);
  reading.via = extra.via || 'rest';
  reading.url = safeUrl(page.url());
  reading.width = page.viewportSize()?.width;
  out.components[name] ??= {};
  out.components[name][state] = reading;
  const box = await target.boundingBox();
  if (box && box.width > 2 && box.height > 2) {
    const pad = 8;
    const clip = {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(box.width + pad * 2, 1440),
      height: Math.min(box.height + pad * 2, 700),
    };
    const file = path.join(CROPS, `${name}-${state}.png`);
    await page.screenshot({ path: file, clip }).catch((e) => log('  crop fail', name, state, e.message.split('\n')[0]));
  }
  log('  ', name, state, reading.rect.w + 'x' + reading.rect.h, reading.style.backgroundColor, reading.style.color);
}

// Pointer to a corner and focus dropped before every state, as the kit's S() does. Before, the
// pointer stayed on the element from the hover reading through pressed and focus-visible, so the
// focus-visible readings were hover and focus mixed.
async function rest(page, loc) {
  // Park the pointer outside the control being measured: (2, 2) sits inside the full-width banner
  // link, so it would hover that control. Below the control's box, or off the viewport's right edge.
  const vp = page.viewportSize() || { width: 1440, height: 900 };
  const box = loc ? await loc.first().boundingBox().catch(() => null) : null;
  const y = box ? Math.min(vp.height - 2, Math.round(box.y + box.height + 40)) : vp.height - 2;
  await page.mouse.move(vp.width - 2, y).catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.waitForTimeout(150);
}

async function states(page, name, loc) {
  await rest(page, loc);
  if (!(await loc.count())) {
    await record(page, name, 'default', loc, { via: 'rest' });
    return;
  }
  await record(page, name, 'default', loc, { via: 'rest' });
  await loc.first().hover().catch(() => {});
  await page.waitForTimeout(350);
  await record(page, name, 'hover', loc, { via: 'mouse hover' });
  await rest(page, loc);
  const release = await forcePseudo(page, loc.first(), ['hover', 'active']);
  await record(page, name, 'pressed', loc, { via: 'CDP forcePseudoState active+hover; no click' });
  await release();
  await rest(page, loc);
  await loc.first().focus().catch(() => {});
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  await page.waitForTimeout(200);
  const focused = await loc.first().evaluate((el) => document.activeElement === el || el.contains(document.activeElement)).catch(() => false);
  if (focused) await record(page, name, 'focus-visible', loc, { via: 'Shift+Tab, Tab' });
  else {
    // Keyboard focus never reached the element, so a reading now would be the element at rest
    // saved as its focus. Record the miss instead, as the kit does.
    out.components[name] ??= {};
    out.components[name]['focus-visible'] = { skipped: 'focus failed: keyboard focus did not reach the element', via: 'focus failed' };
    // A crop from an earlier run would still show a focus state the reading now says was not captured.
    fs.rmSync(path.join(CROPS, `${name}-focus-visible.png`), { force: true });
    log('  -', name, 'focus-visible skipped: focus failed');
  }
  await rest(page, loc);
}

async function run() {
  const { browser, context } = await launch();
  const page = await context.newPage();
  page.setDefaultTimeout(4000);

  await open(page, BASE + '/');
  await states(page, 'banner-link', page.locator('a.bg-primary').first());
  await states(page, 'nav-link', page.getByRole('link', { name: 'Pricing', exact: true }).first());
  await states(page, 'wordmark', page.locator('header a').filter({ hasText: 'Marathon' }).first());
  await states(page, 'primary-button', page.getByRole('link', { name: 'Get Started' }).first());
  await record(page, 'display', 'default', page.locator('h1').first());
  await record(page, 'section-heading', 'default', page.locator('h2').first());
  await record(page, 'body', 'default', page.locator('main p, section p').first());
  await record(page, 'text-link', 'default', page.locator('a.underline-offset-4, a[class*="underline"]').first());
  await states(page, 'text-link', page.locator('a.underline-offset-4, a[class*="underline"]').first());

  await open(page, BASE + '/pricing');
  await states(page, 'segment-selected', page.getByRole('button', { name: 'Pay Annually' }));
  await states(page, 'segment', page.getByRole('button', { name: 'Pay Monthly' }));
  await page.getByRole('button', { name: 'Pay Monthly' }).click();
  await page.waitForTimeout(300);
  await record(page, 'segment', 'selected', page.getByRole('button', { name: 'Pay Monthly' }), { via: 'click toggles billing period; no checkout' });
  await record(page, 'segment-selected', 'unselected', page.getByRole('button', { name: 'Pay Annually' }), { via: 'after monthly toggle' });
  await page.getByRole('button', { name: 'Pay Annually' }).click();
  await page.waitForTimeout(200);
  await record(page, 'price', 'default', page.locator('p.font-display, p.text-6xl').first());
  await record(page, 'plan-card', 'default', page.locator('div').filter({ hasText: /^Free/ }).first());
  const quiet = page.locator('a').filter({ hasText: 'Get Started' }).nth(1);
  await record(page, 'secondary-button', 'default', quiet);
  await states(page, 'secondary-button', quiet);
  const popular = page.locator('text=Popular').first();
  await record(page, 'badge', 'default', popular);

  await open(page, BASE + '/for-agencies');
  await record(page, 'eyebrow', 'default', page.locator('p').filter({ hasText: 'For Agencies' }).first());
  await states(page, 'primary-button-lg', page.getByRole('link', { name: 'Get Started' }).nth(1));
  const watch = page.getByRole('link', { name: /Watch/ }).first();
  await record(page, 'watch-link', 'default', watch);
  await states(page, 'watch-link', watch);

  await open(page, BASE + '/demo');
  await record(page, 'display', 'demo', page.locator('h1').first());
  const iframe = page.locator('iframe').first();
  const iframeN = await iframe.count();
  out.components.demoEmbed = {
    default: iframeN
      ? { ...(await styleOf(iframe).catch(() => ({}))), note: 'embed present; not submitted', srcHost: await iframe.evaluate((el) => { try { return new URL(el.src).host; } catch { return ''; } }) }
      : { missing: true, note: 'Book A Demo heading painted; no form fields in the signed-out DOM. An empty dialog shell was present on first probe and is not a working form.' },
  };

  await open(page, BASE + '/curated');
  await record(page, 'display', 'curated', page.locator('h1').first());
  await record(page, 'caption', 'default', page.locator('p').filter({ hasText: 'Beautiful interface' }).first());

  // redirects: record the landing, do not type
  for (const route of ['/sign-in', '/register']) {
    const landed = await open(page, BASE + route);
    out.components['gate-' + route.slice(1)] = {
      default: { missing: true, requested: BASE + route, final: landed.final, status: landed.status, note: 'redirects to the archive home; sign-in form not submitted; no fields painted' },
    };
    log('  gate', route, '->', landed.final, landed.status);
  }

  // phone menu
  await page.close();
  const mob = await context.browser().newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
  });
  const mp = await mob.newPage();
  await open(mp, BASE + '/');
  const menuBtn = mp.getByRole('button', { name: 'Open menu' });
  await record(mp, 'icon-button', 'default', menuBtn);
  await menuBtn.click();
  await mp.waitForTimeout(400);
  await record(mp, 'menu', 'open', mp.locator('nav, [role="dialog"], div').filter({ hasText: 'For Agencies' }).last());
  await record(mp, 'menu-item', 'default', mp.getByRole('link', { name: 'For Agencies' }).last());
  await mob.close();

  fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
  log('wrote', Object.keys(out.components).length, 'components');
  await browser.close();
}

run().catch((e) => { console.error(e); process.exit(1); });
