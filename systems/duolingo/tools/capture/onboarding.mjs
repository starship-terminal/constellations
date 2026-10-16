// Logged-out "Get started" onboarding, captured headless in a fresh browser context (no account,
// nothing signed in), 2026-10-17. Usage:
//   PLAYWRIGHT=... OUT=<dir> node onboarding.mjs <light|dark> <width> [step ...]
// Each step is `click:<text or data-test>`, `wait:<ms>` or `shot:<name>` (a screenshot and the
// readings below, mid-flow); after the last step it also saves <OUT>/<theme>-<width>-<n>.png
// (full colour, before quantising) and <n>.json: every button and link on screen with its
// data-test, plus the computed style of each clickable choice, so the values are Measured.
// Only generic choices are clicked (a course, a reason, a goal); the flow stops before any
// field that asks for an age, a name or an email, and nothing is submitted.
import fs from 'node:fs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const [,, theme = 'light', width = '1440', ...steps] = process.argv;
const OUT = process.env.OUT; fs.mkdirSync(OUT, { recursive: true });
const b = await chromium.launch();
async function shoot(base) {
  await p.screenshot({ path: base + '.png' });
  fs.writeFileSync(base + '.json', JSON.stringify(await p.evaluate(read), null, 1));
}
const ctx = await b.newContext({ viewport: { width: +width, height: +width < 700 ? 844 : 900 }, deviceScaleFactor: 2, colorScheme: theme, locale: 'en-US' });
const p = await ctx.newPage();
await p.goto('https://www.duolingo.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await p.waitForTimeout(4000);
for (const s of steps) {
  const [verb, ...rest] = s.split(':'); const arg = rest.join(':');
  if (verb === 'click') {
    const byTest = p.locator(`[data-test="${arg}"]`);
    const loc = (await byTest.count()) ? byTest.first() : p.getByText(arg, { exact: false }).first();
    await loc.click({ timeout: 15000 });
  } else if (verb === 'wait') await p.waitForTimeout(+arg);
  else if (verb === 'goto') await p.goto(arg, { waitUntil: 'domcontentloaded' });
  else if (verb === 'shot') { await shoot(`${OUT}/${theme}-${width}-${arg}`); console.log('shot', arg); continue; }
  await p.waitForTimeout(2500);
}
const n = steps.length;
const base = `${OUT}/${theme}-${width}-${String(n).padStart(2, '0')}`;
await p.screenshot({ path: base + '.png' });
function read() {
  const P = ['background-color', 'color', 'border-top-color', 'border-top-width', 'border-bottom-width', 'border-radius', 'box-shadow', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'text-transform', 'height', 'padding-top', 'padding-left'];
  const st = (e) => { const c = getComputedStyle(e); const o = {}; for (const k of P) o[k] = c.getPropertyValue(k); return o; };
  const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.y < innerHeight; };
  const clickables = [...document.querySelectorAll('button, a, [role=button], [role=radio], [role=checkbox], li[tabindex], label')].filter(vis);
  return {
    url: location.pathname, theme: document.documentElement.dataset.duoTheme, w: innerWidth,
    headings: [...document.querySelectorAll('h1,h2,h3,[data-test*="title"]')].filter(vis).map((h) => ({ t: h.textContent.trim().slice(0, 80), s: st(h) })),
    items: clickables.slice(0, 40).map((e) => { const r = e.getBoundingClientRect(); return { tag: e.tagName, dt: e.dataset.test || '', role: e.getAttribute('role') || '', text: e.textContent.trim().slice(0, 50), rect: [r.x, r.y, r.width, r.height].map(Math.round), s: st(e), before: getComputedStyle(e, '::before').content !== 'none' ? st(e) && (() => { const c = getComputedStyle(e, '::before'); return { bg: c.backgroundColor, border: c.borderTopColor + ' ' + c.borderTopWidth, shadow: c.boxShadow, radius: c.borderRadius }; })() : null }; }),
    inputs: [...document.querySelectorAll('input, textarea, select')].filter(vis).map((i) => ({ type: i.type, ph: i.placeholder })),
  };
}
const info = await p.evaluate(read);
fs.writeFileSync(base + '.json', JSON.stringify(info, null, 1));
console.log(base, info.url, info.theme, '\n', info.headings.map((h) => h.t).join(' | '), '\n', info.items.map((i) => `[${i.dt || i.tag}] ${i.text}`).join('\n '), '\ninputs', JSON.stringify(info.inputs));
await b.close();
