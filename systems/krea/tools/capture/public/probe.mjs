// One-shot probe of krea.ai public surfaces. Writes a JSON report to stdout and
// a scratch file. Never clicks consent, never signs in, never submits.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const OUT = path.join(os.homedir(), '.design-systems', 'krea', 'probe.json');
const routes = (process.argv[2] || '/').split(',');

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
// navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
const page = await context.newPage();
const report = [];

function hideOverlays() {
  return page.evaluate(() => {
    const sels = [
      '#onetrust-consent-sdk', '#onetrust-banner-sdk', '.onetrust-pc-dark-filter',
      '#CybotCookiebotDialog', '#CybotCookiebotDialogBodyUnderlay',
      '[id*="cookie" i]', '[class*="cookie" i]', '[id*="consent" i]', '[class*="consent" i]',
      '[aria-label*="cookie" i]', '[aria-label*="consent" i]',
    ];
    let n = 0;
    for (const s of sels) {
      for (const el of document.querySelectorAll(s)) {
        const t = (el.innerText || '').slice(0, 200).toLowerCase();
        if (/cookie|consent|privacy|accept all|reject/.test(t) || /cookie|consent/i.test(el.id + el.className)) {
          el.style.setProperty('display', 'none', 'important');
          el.setAttribute('data-krea-hidden', '1');
          n++;
        }
      }
    }
    return n;
  });
}

for (const route of routes) {
  const url = route.startsWith('http') ? route : 'https://www.krea.ai' + route;
  const row = { url, route };
  try {
    const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    row.status = res?.status() ?? null;
    row.finalUrl = page.url();
    await page.waitForTimeout(3500);
    row.hidden = await hideOverlays();
    row.title = await page.title();
    row.meta = await page.evaluate(() => {
      const html = document.documentElement;
      const body = document.body;
      const vars = [];
      for (const el of [html, body]) {
        const cs = getComputedStyle(el);
        for (const k of cs) if (k.startsWith('--')) vars.push(k);
      }
      // also :root declared via sheets if readable
      const sheetVars = new Set();
      for (const sheet of document.styleSheets) {
        let rules;
        try { rules = sheet.cssRules; } catch { continue; }
        const walk = (list) => {
          for (const r of list) {
            if (r.style) {
              for (let i = 0; i < r.style.length; i++) {
                const k = r.style[i];
                if (k.startsWith('--')) sheetVars.add(k);
              }
            }
            if (r.cssRules) walk(r.cssRules);
          }
        };
        walk(rules);
      }
      const links = [...document.querySelectorAll('a[href]')].slice(0, 80).map((a) => ({
        text: (a.innerText || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        href: a.getAttribute('href'),
      }));
      const buttons = [...document.querySelectorAll('button, [role="button"]')].slice(0, 40).map((b) => ({
        text: (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        aria: b.getAttribute('aria-label'),
      }));
      const dialogs = [...document.querySelectorAll('[role="dialog"], [aria-modal="true"]')].map((d) => (d.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 180));
      return {
        htmlClass: html.className,
        htmlAttrs: [...html.attributes].map((a) => a.name + '=' + a.value).slice(0, 20),
        bodyClass: (body.className || '').toString().slice(0, 200),
        theme: html.getAttribute('data-theme') || html.getAttribute('data-mode') || body.getAttribute('data-theme'),
        colorScheme: getComputedStyle(html).colorScheme,
        bg: getComputedStyle(body).backgroundColor,
        color: getComputedStyle(body).color,
        font: getComputedStyle(body).fontFamily,
        sheetCount: document.styleSheets.length,
        sheetVarCount: sheetVars.size,
        sheetVarSample: [...sheetVars].slice(0, 40),
        computedVarCount: vars.length,
        links,
        buttons,
        dialogs,
        h1: [...document.querySelectorAll('h1')].map((h) => h.innerText.trim().slice(0, 120)),
        textSample: (body.innerText || '').replace(/\s+/g, ' ').slice(0, 500),
      };
    });
  } catch (e) {
    row.error = String(e).split('\n')[0];
  }
  report.push(row);
  console.log(JSON.stringify({ route: row.route, status: row.status, title: row.title, finalUrl: row.finalUrl, error: row.error, h1: row.meta?.h1, text: row.meta?.textSample?.slice(0, 180) }));
}

fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(report, null, 1));
console.log('wrote', OUT);
await browser.close();
