// Read computed styles, the styled-components theme object, brand meta and
// layout from the public dona.ai pages. Writes systems/dona/raw/.
// Never fills a form. Hides the cookie bar; does not click Accept.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { launch, open, BASE, RAW, styleOf } from './public/lib.mjs';

const OUT = path.join(RAW);
fs.mkdirSync(OUT, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await open(page, BASE + '/');

const home = await page.evaluate(() => {
  function box(el) {
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName,
      cls: String(el.className).slice(0, 80),
      text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60),
      color: s.color,
      backgroundColor: s.backgroundColor,
      fontFamily: s.fontFamily,
      fontSize: s.fontSize,
      fontWeight: s.fontWeight,
      lineHeight: s.lineHeight,
      letterSpacing: s.letterSpacing,
      borderRadius: s.borderRadius,
      padding: `${s.paddingTop} ${s.paddingRight} ${s.paddingBottom} ${s.paddingLeft}`,
      border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
      boxShadow: s.boxShadow,
      width: Math.round(r.width),
      height: Math.round(r.height),
      transition: s.transitionDuration + ' ' + s.transitionTimingFunction,
    };
  }
  const byText = (sel, text) => [...document.querySelectorAll(sel)].find((el) => (el.innerText || '').trim().startsWith(text));
  const themeEl = document.querySelector('button');
  const fiberKey = Object.keys(themeEl).find((k) => k.startsWith('__reactFiber') || k.startsWith('__reactInternalInstance'));
  function findTheme(fiber, depth = 0) {
    if (!fiber || depth > 50) return null;
    const p = fiber.memoizedProps;
    if (p && p.theme && p.theme.background && p.theme.id) return p.theme;
    return findTheme(fiber.return, depth + 1);
  }
  const theme = findTheme(themeEl[fiberKey]);
  function plainTheme(t) {
    if (!t) return null;
    const roles = {};
    for (const k of ['id', 'name', 'foreground', 'background', 'body']) roles[k] = t[k];
    for (const k of ['primary', 'secondary', 'success', 'warning', 'danger']) {
      const r = t[k];
      roles[k] = r ? { background: r.background, foreground: r.foreground } : null;
    }
    return roles;
  }
  const headlines = [...document.querySelectorAll('h1, h2, p, span')].filter((el) => {
    const s = getComputedStyle(el);
    return parseFloat(s.fontSize) >= 28 && (el.innerText || '').trim().length > 3 && (el.innerText || '').length < 90;
  }).slice(0, 6).map(box);
  return {
    url: location.href,
    title: document.title,
    viewport: { innerWidth: innerWidth, innerHeight: innerHeight, dpr: devicePixelRatio },
    theme: plainTheme(theme),
    body: box(document.body),
    buttons: [...document.querySelectorAll('button')].map((b) => ({ label: (b.innerText || '').trim().slice(0, 40), ...box(b) })),
    input: box(document.querySelector('input')),
    headlines,
    footerLink: box(document.querySelector('footer a, [class*="Footer"] a')),
    meta: {
      description: document.querySelector('meta[name="description"]')?.content || null,
      themeColor: document.querySelector('meta[name="theme-color"]')?.content || null,
      icons: [...document.querySelectorAll('link[rel*="icon"]')].map((l) => l.href),
      generator: document.querySelector('meta[name="generator"]')?.content || null,
    },
    container: box(document.querySelector('[class*="Container"]')),
  };
});

// hover the primary CTA without navigating
const cta = page.getByRole('button', { name: 'Try for free' });
await cta.hover();
await page.waitForTimeout(300);
const ctaHover = await styleOf(page, cta);
await page.keyboard.press('Tab');
const about = page.getByRole('button', { name: 'About' });
await about.focus();
const aboutFocus = await styleOf(page, about);

// video modal
await page.getByRole('button', { name: 'Watch video' }).click({ force: true });
await page.waitForTimeout(700);
const modal = await page.evaluate(() => {
  const m = document.querySelector('[class*="pages__Modal-"]');
  const inner = document.querySelector('[class*="ModalInner"]');
  const iframe = document.querySelector('iframe');
  if (!m) return null;
  const s = getComputedStyle(m);
  const si = inner ? getComputedStyle(inner) : null;
  return {
    backgroundColor: s.backgroundColor,
    opacity: s.opacity,
    zIndex: s.zIndex,
    innerRadius: si && si.borderRadius,
    innerShadow: si && si.boxShadow,
    innerWidth: inner ? Math.round(inner.getBoundingClientRect().width) : null,
    iframe: iframe ? iframe.src.split('?')[0] : null,
  };
});

fs.writeFileSync(path.join(OUT, 'readings.json'), JSON.stringify({ home, ctaHover, aboutFocus, modal, capturedAt: new Date().toISOString() }, null, 2));
console.log('wrote readings', home.theme && home.theme.id, home.viewport);
await browser.close();
