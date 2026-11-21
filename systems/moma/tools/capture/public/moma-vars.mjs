// Read computed custom properties from the live homepage. Writes raw/css-vars-live.json.
// Does not click Tickets, Donate, or Log in.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ channel: 'chrome', headless: false, args: ['--disable-blink-features=AutomationControlled'] });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
try {
  await page.goto('https://www.moma.org/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1800);
  const title = await page.title();
  if (/just a moment|attention required/i.test(title)) {
    console.error('STOP', title);
    process.exitCode = 3;
  } else {
    const data = await page.evaluate(async () => {
      const root = getComputedStyle(document.documentElement);
      const names = new Set();
      for (const sheet of document.styleSheets) {
        let rules;
        try { rules = sheet.cssRules; } catch { continue; }
        const walk = (list) => {
          if (!list) return;
          for (const rule of list) {
            if (rule.cssRules) walk(rule.cssRules);
            if (!rule.style) continue;
            for (let i = 0; i < rule.style.length; i++) {
              const p = rule.style[i];
              if (p.startsWith('--')) names.add(p);
            }
          }
        };
        walk(rules);
      }
      let sheetText = '';
      const href = [...document.querySelectorAll('link[rel=stylesheet]')].map((l) => l.href).find((h) => /sol\./.test(h));
      if (href) {
        const res = await fetch(href);
        sheetText = await res.text();
        for (const m of sheetText.matchAll(/(--[A-Za-z0-9_-]+)\s*:/g)) names.add(m[1]);
      }
      const resolved = {};
      for (const n of [...names].sort()) {
        const v = root.getPropertyValue(n).trim();
        if (v) resolved[n] = v.slice(0, 180);
      }
      const tickets = [...document.querySelectorAll('a')].find((a) => (a.innerText || '').trim() === 'Tickets' && a.getBoundingClientRect().width > 40 && a.getBoundingClientRect().top < 80);
      const ticketsStyle = tickets ? getComputedStyle(tickets) : null;
      return {
        title: document.title,
        href,
        sheetBytes: sheetText.length,
        nameCount: names.size,
        resolvedCount: Object.keys(resolved).length,
        colorScheme: root.colorScheme,
        htmlClass: document.documentElement.className.slice(0, 200),
        viewport: { innerWidth, innerHeight, devicePixelRatio },
        tickets: ticketsStyle && {
          backgroundColor: ticketsStyle.backgroundColor,
          color: ticketsStyle.color,
          fontSize: ticketsStyle.fontSize,
          fontWeight: ticketsStyle.fontWeight,
          borderRadius: ticketsStyle.borderRadius,
          fontFamily: ticketsStyle.fontFamily,
        },
        resolved,
      };
    });
    const out = path.join(PKG, 'raw', 'css-vars-live.json');
    fs.writeFileSync(out, JSON.stringify(data, null, 2));
    console.log('wrote', out, 'vars', data.resolvedCount, 'sheet', data.href, data.sheetBytes);
    console.log('tickets', JSON.stringify(data.tickets));
    console.log('session', data.resolved['--color--session'], 'brand10', data.resolved['--color--brand--10'], 'page', data.resolved['--page-spacing']);
  }
} finally {
  await browser.close();
}
