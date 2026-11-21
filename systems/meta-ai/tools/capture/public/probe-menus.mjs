// Hover each homepage header control and record what opens. No form
// submit, no identity-provider click, no password.
import fs from 'node:fs';
import { chromium } from './lib.mjs';

const OUT = process.env.MAP_OUT || '/tmp/meta-ai-menus.json';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  locale: 'en-US',
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
});
const page = await context.newPage();
await page.goto('https://www.meta.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(3500);

const dumpVisible = () => page.evaluate(() => {
  const textOf = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 120);
  const open = [...document.querySelectorAll('[aria-expanded="true"], [role="menu"], [role="dialog"], dialog')].map((el) => ({
    tag: el.tagName,
    role: el.getAttribute('role'),
    aria: el.getAttribute('aria-label'),
    text: textOf(el).slice(0, 200),
  }));
  const menus = [...document.querySelectorAll('header [role="menu"], header nav, [data-testid*="menu"], [class*="submenu"], [class*="flyout"], [class*="dropdown"]')].slice(0, 12).map((el) => ({
    tag: el.tagName,
    hidden: el.hidden || el.getAttribute('aria-hidden'),
    text: textOf(el).slice(0, 180),
  }));
  return { open, menus };
});

const labels = ['AI glasses', 'Meta Quest', 'Meta VR Glasses', 'Explore Meta', 'Support'];
const hovers = [];
for (const label of labels) {
  const loc = page.getByRole('link', { name: label, exact: true }).first();
  if (!(await loc.count())) {
    hovers.push({ label, missing: true });
    continue;
  }
  await loc.hover();
  await page.waitForTimeout(1200);
  const links = await page.evaluate(() => {
    const visible = (el) => {
      const r = el.getBoundingClientRect();
      const s = getComputedStyle(el);
      return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && r.top < 900;
    };
    return [...document.querySelectorAll('a')].filter(visible).map((a) => ({
      text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100),
      href: a.getAttribute('href'),
      top: Math.round(a.getBoundingClientRect().top),
    })).filter((a) => a.top < 700 && a.top > 40).slice(0, 60);
  });
  hovers.push({ label, links });
  await page.mouse.move(8, 8);
  await page.waitForTimeout(400);
}

const extras = await page.evaluate(() => {
  const textOf = (el) => (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 100);
  const all = [...document.querySelectorAll('a, button')].map((el) => ({
    tag: el.tagName,
    text: textOf(el),
    href: el.href || null,
    aria: el.getAttribute('aria-label'),
  }));
  const interesting = all.filter((x) => /sign|log ?in|account|cookie|region|country|language|search|bag|cart|locale/i.test(`${x.text} ${x.aria || ''} ${x.href || ''}`));
  const footer = [...document.querySelectorAll('footer a')].map((a) => ({
    text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    href: a.getAttribute('href'),
  }));
  return {
    title: document.title,
    href: location.href,
    interesting: interesting.slice(0, 40),
    footer,
    buttonCount: document.querySelectorAll('button').length,
  };
});

fs.writeFileSync(OUT, JSON.stringify({ finalUrl: page.url(), hovers, extras }, null, 2));
console.log('wrote', OUT, 'hovers', hovers.map((h) => `${h.label}:${h.links?.length ?? 'miss'}`).join(' '));
await browser.close();
