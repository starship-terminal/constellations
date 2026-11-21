// Map polar.sh site tree. No typing, no submit, no identity-provider click.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const OUT = path.join(os.homedir(), '.design-systems', 'polar', 'map.json');
fs.mkdirSync(path.dirname(OUT), { recursive: true });
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const browser = await chromium.launch({ headless: true });

async function contextFor(mobile) {
  return browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1', locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
}

const page = await (await contextFor(false)).newPage();
page.setDefaultTimeout(25000);

async function evalPage() {
  return page.evaluate(() => {
    const txt = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100);
    const hrefOf = (a) => {
      try { const u = new URL(a.href); return u.origin + u.pathname + (u.search || ''); } catch { return a.getAttribute('href'); }
    };
    const nav = document.querySelector('header') || document.querySelector('nav');
    const footer = document.querySelector('footer');
    const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 2 && r.height > 2; };
    const items = (root, limit) => root ? [...root.querySelectorAll('a, button')].filter(vis).slice(0, limit).map((el) => ({
      tag: el.tagName, text: txt(el), href: el.tagName === 'A' ? hrefOf(el) : null,
    })).filter((x) => x.text.length < 80) : [];
    const dialogs = [...document.querySelectorAll('[role=dialog], dialog')].map((d) => ({
      text: (d.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 500),
      inputs: [...d.querySelectorAll('input')].map((i) => ({ type: i.type, name: i.name, placeholder: i.placeholder, valueLen: (i.value || '').length })),
    }));
    return {
      url: location.origin + location.pathname + location.search,
      title: document.title.slice(0, 140),
      statusHint: document.title,
      htmlClass: document.documentElement.className,
      bodyBg: getComputedStyle(document.body).backgroundColor,
      htmlBg: getComputedStyle(document.documentElement).backgroundColor,
      h1: ((document.querySelector('h1') || {}).innerText || '').replace(/\s+/g, ' ').trim().slice(0, 140),
      navText: nav ? nav.innerText.replace(/\s+/g, ' ').trim().slice(0, 300) : '',
      navItems: items(nav, 40),
      footerText: footer ? footer.innerText.replace(/\s+/g, ' ').trim().slice(0, 800) : '',
      footerItems: items(footer, 50),
      dialogs,
      captcha: !!document.querySelector('iframe[src*="turnstile"], iframe[src*="captcha"], iframe[src*="challenge"]'),
      parked: /domain for sale|this domain|buy this domain|parked/i.test(document.body.innerText.slice(0, 500)),
    };
  });
}

const pages = [
  '/',
  '/features/usage-billing',
  '/docs',
  '/docs/introduction',
  '/blog',
  '/company',
  '/integrate',
  '/resources/pricing',
  '/pricing',
  '/field-guide',
  '/customers/stilla-ai',
  '/startup-program',
  '/signup',
  '/login',
  '/auth',
];
const report = { captured: new Date().toISOString(), desktop: [], hover: null, mobile: null };

for (const p of pages) {
  const res = await page.goto('https://polar.sh' + p, { waitUntil: 'domcontentloaded', timeout: 45000 }).catch((e) => ({ error: String(e.message).split('\n')[0] }));
  await page.waitForTimeout(1400);
  const info = await evalPage().catch((e) => ({ error: String(e.message).split('\n')[0] }));
  info.http = res && res.status ? res.status() : null;
  info.final = page.url().split('?')[0].split('#')[0];
  report.desktop.push(info);
  console.log(p, info.http, info.final, info.h1 || info.title);
}

// Hover Features and Docs in the nav text nodes
await page.goto('https://polar.sh/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1000);
const hoverNames = await page.evaluate(() => {
  const nav = document.querySelector('nav, header');
  if (!nav) return [];
  const hits = [];
  const walk = (el) => {
    for (const n of el.childNodes) {
      if (n.nodeType === 3 && /Features|Docs/.test(n.textContent || '')) {
        const p = n.parentElement;
        if (p) {
          p.setAttribute('data-map-hover', (n.textContent || '').trim().slice(0, 20));
          hits.push((n.textContent || '').trim().slice(0, 40));
        }
      } else if (n.nodeType === 1) walk(n);
    }
  };
  walk(nav);
  return hits;
});
report.hoverLabels = hoverNames;
const hovers = [];
for (const label of ['Features', 'Docs']) {
  const loc = page.locator(`[data-map-hover="${label}"]`).first();
  if (await loc.count()) {
    await loc.hover();
    await page.waitForTimeout(700);
    const overlays = await page.evaluate(() => [...document.querySelectorAll('[role=menu], [data-state=open], [data-radix-popper-content-wrapper], [role=dialog]')].map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400)));
    const links = await page.evaluate(() => [...document.querySelectorAll('a')].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.top > 40 && r.top < 500 && r.height > 0 && (a.innerText || '').trim();
    }).slice(0, 25).map((a) => ({ text: a.innerText.replace(/\s+/g, ' ').trim().slice(0, 80), href: a.getAttribute('href') })));
    hovers.push({ label, overlays, links });
  } else hovers.push({ label, missing: true });
}
report.hover = hovers;

// Mobile nav
const mp = await (await contextFor(true)).newPage();
await mp.goto('https://polar.sh/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await mp.waitForTimeout(1500);
const mobileNav = await mp.evaluate(() => {
  const nav = document.querySelector('nav, header');
  const txt = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60);
  const items = nav ? [...nav.querySelectorAll('a, button')].map((el) => {
    const r = el.getBoundingClientRect();
    return { tag: el.tagName, text: txt(el), aria: el.getAttribute('aria-label'), w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x) };
  }).filter((x) => x.w > 0) : [];
  return { w: innerWidth, h: innerHeight, items, navText: nav ? nav.innerText.replace(/\s+/g, ' ').trim().slice(0, 200) : '' };
});
report.mobile = mobileNav;
console.log('mobile', JSON.stringify(mobileNav));

fs.writeFileSync(OUT, JSON.stringify(report, null, 2));
console.log('wrote', OUT);
await browser.close();
