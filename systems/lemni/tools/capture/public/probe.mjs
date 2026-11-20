// One-shot DOM probe for lemni.com. Not part of the rebuild.
const { chromium } = await import(process.env.PLAYWRIGHT || 'playwright');

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const url = process.argv[2] || 'https://www.lemni.com/';
const b = await chromium.launch({ headless: true });
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
// automation is not hidden: the webdriver flag stays as Chromium sets it (bot check: recorded as a boundary, not bypassed)
const p = await ctx.newPage();
await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
await p.waitForTimeout(5000);
const info = await p.evaluate(() => {
  const vars = new Set();
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.style) for (const n of r.style) if (n.startsWith('--')) vars.add(n);
        if (r.cssRules) walk(r.cssRules);
      }
    };
    if (rules) walk(rules);
  }
  const token = [...vars].filter((n) => n.startsWith('--token-'));
  const framer = [...vars].filter((n) => n.startsWith('--framer-'));
  const other = [...vars].filter((n) => !n.startsWith('--token-') && !n.startsWith('--framer-'));
  const html = document.documentElement;
  const body = document.body;
  const cs = getComputedStyle(body);
  const bg = getComputedStyle(html).backgroundColor;
  const links = [...document.querySelectorAll('a')].slice(0, 40).map((a) => ({
    t: (a.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40),
    h: a.getAttribute('href'),
  })).filter((x) => x.t || x.h);
  const buttons = [...document.querySelectorAll('button, [role="button"]')].slice(0, 30).map((a) => ({
    t: (a.innerText || a.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 50),
    name: a.getAttribute('data-framer-name'),
  }));
  const names = [...new Set([...document.querySelectorAll('[data-framer-name]')].map((n) => n.getAttribute('data-framer-name')))];
  const fixed = [...document.querySelectorAll('body *')].filter((el) => {
    const c = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return (c.position === 'fixed' || c.position === 'sticky') && r.width > 40 && r.height > 20 && r.height < 900;
  }).slice(0, 12).map((el) => ({
    tag: el.tagName, name: el.getAttribute('data-framer-name'), pos: getComputedStyle(el).position,
    t: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    r: (() => { const r = el.getBoundingClientRect(); return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)]; })(),
  }));
  const inputs = [...document.querySelectorAll('input, textarea, select')].map((el) => ({
    tag: el.tagName, type: el.getAttribute('type'), ph: el.getAttribute('placeholder'), name: el.getAttribute('name'),
  }));
  return {
    title: document.title,
    url: location.href,
    htmlClass: html.className,
    htmlAttrs: [...html.attributes].map((a) => a.name + '=' + a.value).slice(0, 20),
    colorScheme: cs.colorScheme,
    bodyBg: cs.backgroundColor,
    htmlBg: bg,
    bodyColor: cs.color,
    font: cs.fontFamily,
    scrollH: document.documentElement.scrollHeight,
    tokenCount: token.length,
    tokenSample: token.slice(0, 12),
    framerCount: framer.length,
    framerSample: framer.slice(0, 20),
    otherVars: other.slice(0, 30),
    names,
    links,
    buttons,
    fixed,
    inputs,
    textStart: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 500),
  };
});
console.log(JSON.stringify(info, null, 2));
await b.close();
