// Deeper signed-out probe: theme, nav links, footer, tool gates. No consent click, no auth, no submit.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US',
});
// navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
const page = await context.newPage();

async function hide() {
  await page.evaluate(() => {
    for (const el of document.querySelectorAll('[id*="cookie" i], [class*="cookie" i], [id*="consent" i], [id*="onetrust" i], #CybotCookiebotDialog')) {
      el.style.setProperty('display', 'none', 'important');
    }
  });
}

const report = {};

await page.goto('https://www.krea.ai/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(3000);
await hide();
report.home = await page.evaluate(() => {
  const html = document.documentElement;
  const allLinks = [...document.querySelectorAll('a[href]')].map((a) => ({
    t: (a.innerText || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 70),
    h: a.getAttribute('href'),
  }));
  const uniq = [];
  const seen = new Set();
  for (const l of allLinks) {
    const k = l.h + '|' + l.t;
    if (seen.has(k)) continue;
    seen.add(k);
    uniq.push(l);
  }
  const themeBits = [...document.querySelectorAll('button, [role="switch"], [role="button"]')]
    .map((b) => (b.getAttribute('aria-label') || b.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80))
    .filter((t) => /theme|dark|light|appearance|color mode/i.test(t));
  return {
    htmlClass: html.className,
    colorScheme: getComputedStyle(html).colorScheme,
    bg: getComputedStyle(document.body).backgroundColor,
    themeBits,
    linkCount: uniq.length,
    links: uniq.filter((l) => l.h && !l.h.startsWith('#')).slice(0, 200),
  };
});

// pricing structure
await page.goto('https://www.krea.ai/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(3000);
await hide();
report.pricing = await page.evaluate(() => {
  const html = document.documentElement;
  const buttons = [...document.querySelectorAll('button, a')].slice(0, 60).map((b) => ({
    tag: b.tagName.toLowerCase(),
    t: (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    h: b.getAttribute('href'),
  })).filter((b) => b.t);
  return {
    htmlClass: html.className,
    bg: getComputedStyle(document.body).backgroundColor,
    color: getComputedStyle(document.body).color,
    font: getComputedStyle(document.body).fontFamily,
    h: [...document.querySelectorAll('h1,h2,h3')].slice(0, 20).map((e) => e.innerText.trim().replace(/\s+/g, ' ').slice(0, 80)),
    buttons,
    text: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 800),
  };
});

// login boundary (do not click providers)
await page.goto('https://www.krea.ai/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2500);
report.login = await page.evaluate(() => ({
  htmlClass: document.documentElement.className,
  bg: getComputedStyle(document.body).backgroundColor,
  buttons: [...document.querySelectorAll('button, a')].slice(0, 30).map((b) => ({
    t: (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    h: b.getAttribute('href'),
  })),
  inputs: [...document.querySelectorAll('input')].map((i) => ({ type: i.type, name: i.name, ph: i.placeholder, aria: i.getAttribute('aria-label') })),
}));

// docs host?
await page.goto('https://www.krea.ai/docs', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);
report.docs = { url: page.url(), title: await page.title(), htmlClass: await page.evaluate(() => document.documentElement.className) };

const dest = path.join(os.homedir(), '.design-systems', 'krea', 'deep.json');
fs.writeFileSync(dest, JSON.stringify(report, null, 1));
console.log('home links', report.home.linkCount, 'themeBits', report.home.themeBits);
console.log('pricing h', report.pricing.h);
console.log('login inputs', report.login.inputs.length, 'buttons', report.login.buttons.map((b) => b.t).slice(0, 12));
console.log('docs', report.docs);
await browser.close();
