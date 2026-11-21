// Read computed styles for Sonarworks public components. Writes raw/components-computed.json
// and 2x crops under components/crops/. Does not submit forms or type into fields.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { launch, open, BASE, CROPS, RAW, hideOverlays } from './lib.mjs';

fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRadius', 'boxShadow', 'textDecorationLine', 'opacity', 'outline',
];

function spec(name, sel, pagePath) {
  return { name, sel, pagePath };
}

const SPECS = [
  spec('top-link', '#top-navigation a[href="/reviews"]', '/'),
  spec('primary-tab', '#primary-navigation a[data-navigation="soundid-reference-navigation"]', '/'),
  spec('wordmark', '#primary-navigation a[href="/"]', '/'),
  spec('hero-title', 'h1', '/'),
  spec('section-title', 'h2', '/'),
  spec('learn-more', 'a.btn, a.button, a[class*="btn"], a.rounded-full', '/soundid-reference'),
  spec('footer-link', 'footer a[href="/company"]', '/'),
  spec('menu-item', '#company-top-navigation a', '/'),
  spec('subnav-link', '#soundid-reference-navigation a', '/'),
  spec('body', 'body', '/'),
  spec('page', 'main, #content, .container', '/'),
  spec('card', 'article, .card, [class*="card"]', '/'),
  spec('faq', 'details', '/soundid-reference'),
  spec('faq-summary', 'details summary', '/soundid-reference'),
  spec('field', 'input[type="email"], input[type="text"]', '/company/contacts'),
  spec('field-label', 'label', '/company/contacts'),
  spec('send', 'button', '/company/contacts'),
  spec('login-field', 'input[type="email"]', '/account/login'),
  spec('login-button', 'button, input[type="submit"]', '/account/login'),
  spec('mobile-menu-button', '#menu-open-button', '/'),
  spec('badge', '.rounded-full, [class*="badge"]', '/soundid-reference'),
  spec('store-button', 'button, a.btn, .btn', 'https://store.sonarworks.com/'),
];

async function readBox(page, sel) {
  return page.evaluate(({ sel, PROPS }) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const k of PROPS) style[k] = cs[k];
    return {
      text: (el.innerText || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      tag: el.tagName,
      className: (el.className || '').toString().slice(0, 160),
      rect: { x: r.x, y: r.y, width: r.width, height: r.height },
      style,
    };
  }, { sel, PROPS });
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const out = { capturedAt: new Date().toISOString(), viewport: { width: 1440, height: 900, dpr: 1 }, components: {} };
let current = '';

for (const spec of SPECS) {
  const url = spec.pagePath.startsWith('http') ? spec.pagePath : BASE + spec.pagePath;
  if (url !== current) {
    await open(page, url, { wait: 1400 });
    current = url;
    if (spec.name === 'menu-item') {
      await page.locator('[data-menu="company-top-navigation"]').hover({ force: true }).catch(() => {});
      await page.waitForTimeout(400);
    }
    if (spec.name === 'subnav-link') {
      await page.locator('a[data-navigation="soundid-reference-navigation"]').first().hover({ force: true }).catch(() => {});
      await page.waitForTimeout(500);
    }
  }
  const reading = await readBox(page, spec.sel);
  out.components[spec.name] = { selector: spec.sel, url: page.url().split('?')[0], reading };
  if (!reading || reading.rect.width < 2 || reading.rect.height < 2) {
    console.log('miss', spec.name);
    continue;
  }
  const clip = {
    x: Math.max(0, reading.rect.x - 8),
    y: Math.max(0, reading.rect.y - 8),
    width: Math.min(1400, reading.rect.width + 16),
    height: Math.min(400, reading.rect.height + 16),
  };
  const file = path.join(CROPS, `${spec.name}-default.png`);
  await page.screenshot({ path: file, clip }).catch((e) => console.log('crop fail', spec.name, e.message.split('\n')[0]));
  console.log('ok', spec.name, reading.style.backgroundColor, reading.style.color, reading.style.fontSize);
}

// hover / focus on a primary tab and a learn-more link, without navigation
await open(page, BASE + '/', { wait: 1000 });
const tab = page.locator('#primary-navigation a[data-navigation="soundid-vm-pro-navigation"]').first();
await tab.hover({ force: true });
await page.waitForTimeout(300);
const hover = await readBox(page, '#primary-navigation a[data-navigation="soundid-vm-pro-navigation"]');
out.components['primary-tab-hover'] = { selector: 'a[data-navigation="soundid-vm-pro-navigation"]', state: 'hover', reading: hover };
if (hover && hover.rect.width > 2) {
  await page.screenshot({
    path: path.join(CROPS, 'primary-tab-hover.png'),
    clip: { x: Math.max(0, hover.rect.x - 8), y: Math.max(0, hover.rect.y - 8), width: Math.min(500, hover.rect.width + 16), height: Math.min(200, hover.rect.height + 16) },
  }).catch(() => {});
}
await tab.focus();
await page.waitForTimeout(200);
const focus = await readBox(page, '#primary-navigation a[data-navigation="soundid-vm-pro-navigation"]');
out.components['primary-tab-focus'] = { selector: 'a[data-navigation="soundid-vm-pro-navigation"]', state: 'focus', reading: focus };

// details open on reference page
await open(page, BASE + '/soundid-reference', { wait: 1400 });
const opened = await page.evaluate(() => {
  const d = document.querySelector('details');
  if (!d) return null;
  d.open = true;
  const s = d.querySelector('summary');
  const cs = s ? getComputedStyle(s) : null;
  const r = d.getBoundingClientRect();
  return { open: d.open, h: Math.round(r.height), summaryColor: cs && cs.color, summarySize: cs && cs.fontSize };
});
out.components['faq-open'] = { state: 'open', reading: opened };

// mobile menu button computed at 390
await context.close();
const mobile = await launch({ mobile: true });
const mp = await mobile.context.newPage();
await open(mp, BASE + '/', { wait: 1200 });
const menuBtn = await readBox(mp, '#menu-open-button');
out.components['mobile-menu-button'] = { selector: '#menu-open-button', viewport: '390x844', reading: menuBtn };
await mp.locator('#menu-open-button').click({ force: true });
await mp.waitForTimeout(400);
const menu = await mp.evaluate(() => {
  const el = document.getElementById('mobile-navigation');
  if (!el) return null;
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return { visibility: cs.visibility, bg: cs.backgroundColor, color: cs.color, h: Math.round(r.height), w: Math.round(r.width) };
});
out.components['mobile-menu'] = { state: 'open', reading: menu };
await mobile.browser.close();
await browser.close();

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2) + '\n');
console.log('wrote', path.join(RAW, 'components-computed.json'));
