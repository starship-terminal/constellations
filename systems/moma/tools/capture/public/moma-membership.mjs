// Membership marketing on membership.moma.org, plus component crops from
// pages that already loaded without a challenge. Headed Chrome. One launch.
// Stops if the title is a Cloudflare challenge. Does not click Join, Donate,
// or Tickets.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = path.join(os.homedir(), '.design-systems', 'moma', 'raw-shots');
const CROPS = path.join(PKG, 'components', 'crops');
const READ = path.join(PKG, 'raw');
fs.mkdirSync(CROPS, { recursive: true });

const browser = await chromium.launch({ channel: 'chrome', headless: false });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
});
const page = await context.newPage();
const log = (...a) => console.log(...a);
const req = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 };

async function guard(source) {
  const title = await page.title();
  if (/just a moment|attention required|checking your browser/i.test(title)) {
    console.error('STOP Cloudflare', title, source);
    await browser.close();
    process.exit(3);
  }
  return title;
}

async function cropNamed(name, selectorText) {
  const box = await page.evaluate((needle) => {
    const els = [...document.querySelectorAll('a, button, h1, h2, input, p')];
    const el = els.find((e) => {
      const t = (e.innerText || e.getAttribute('aria-label') || e.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim();
      return t === needle || t.startsWith(needle);
    });
    if (!el) return null;
    const r = el.getBoundingClientRect();
    const s = getComputedStyle(el);
    return {
      x: r.x, y: r.y, w: r.width, h: r.height,
      fontSize: s.fontSize, fontWeight: s.fontWeight, color: s.color,
      bg: s.backgroundColor, radius: s.borderRadius, pad: s.padding,
      border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
      letterSpacing: s.letterSpacing, lineHeight: s.lineHeight,
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
    };
  }, selectorText);
  if (!box || box.w < 8 || box.h < 8) {
    log('miss', name, selectorText);
    return null;
  }
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(1440 - Math.max(0, box.x - pad), box.w + pad * 2),
    height: Math.min(900 - Math.max(0, box.y - pad), box.h + pad * 2),
  };
  await screenshotWithMetadata(page, { path: `${CROPS}/${name}.png`, clip }, { ...req, sanitizedSourceUrl: page.url().split('?')[0] });
  log('crop', name, Math.round(clip.width), Math.round(clip.height), box.bg, box.fontSize);
  return box;
}

const notes = {};

await page.goto('https://www.moma.org/', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(1800);
await guard('home');
await page.addStyleTag({ content: '[class*="cookie" i],[id*="cookie" i],[class*="klaviyo"],div[class*="needsclick"]{display:none!important}' }).catch(() => {});
await page.waitForTimeout(300);

notes.tickets = await cropNamed('tickets-default', 'Tickets');
notes.donate = await cropNamed('donate-default', 'Donate');
notes.visit = await cropNamed('nav-visit-default', 'Visit');
notes.wordmark = await page.evaluate(() => {
  const a = document.querySelector('a[href="/"] svg, header svg');
  if (!a) return null;
  const r = a.getBoundingClientRect();
  return { x: r.x, y: r.y, w: r.width, h: r.height };
});
if (notes.wordmark) {
  const b = notes.wordmark;
  await screenshotWithMetadata(page, {
    path: `${CROPS}/wordmark-default.png`,
    clip: { x: Math.max(0, b.x - 4), y: Math.max(0, b.y - 4), width: b.w + 8, height: b.h + 8 },
  }, { ...req, sanitizedSourceUrl: 'https://www.moma.org/' });
  log('crop wordmark');
}

const visitBtn = page.getByRole('button', { name: 'Visit', exact: true }).first();
if (await visitBtn.count()) {
  await visitBtn.hover();
  await page.waitForTimeout(300);
  notes.visitHover = await page.evaluate(() => {
    const el = [...document.querySelectorAll('button')].find((b) => (b.innerText || '').trim() === 'Visit' && b.getBoundingClientRect().width > 20);
    if (!el) return null;
    const s = getComputedStyle(el);
    return { color: s.color, textDecoration: s.textDecorationLine, bg: s.backgroundColor };
  });
  log('visit hover', JSON.stringify(notes.visitHover));
  await cropNamed('nav-visit-hover', 'Visit');
}

await page.goto('https://membership.moma.org/', { waitUntil: 'domcontentloaded', timeout: 40000 });
await page.waitForTimeout(2500);
const title = await guard('membership');
log('membership title', title, 'url', page.url());
await page.addStyleTag({ content: '[class*="cookie" i],[id*="cookie" i],[class*="consent" i]{display:none!important}' }).catch(() => {});
await screenshotWithMetadata(page, { path: `${RAW}/membership-light-default.png` }, { ...req, sanitizedSourceUrl: 'https://membership.moma.org/' });
log('shot membership');
notes.membership = await page.evaluate(() => {
  function read(el) {
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      fontFamily: s.fontFamily, fontSize: s.fontSize, fontWeight: s.fontWeight,
      color: s.color, bg: s.backgroundColor, radius: s.borderRadius, pad: s.padding,
      letterSpacing: s.letterSpacing, lineHeight: s.lineHeight,
      box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
    };
  }
  const h1 = document.querySelector('h1');
  const buttons = [...document.querySelectorAll('a, button')].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 40 && r.height > 24 && r.top < 900 && r.top > 0;
  }).slice(0, 8).map(read);
  const body = getComputedStyle(document.body);
  return {
    h1: read(h1),
    buttons,
    bodyFont: body.fontFamily,
    bodyBg: body.backgroundColor,
    bodyColor: body.color,
    title: document.title,
  };
});
log('membership measure', JSON.stringify(notes.membership).slice(0, 1500));

const join = (notes.membership.buttons || []).find((b) => /join|become|member/i.test(b.text || ''));
if (join) {
  await screenshotWithMetadata(page, {
    path: `${CROPS}/membership-cta-default.png`,
    clip: { x: Math.max(0, join.box.x - 6), y: Math.max(0, join.box.y - 6), width: join.box.w + 12, height: join.box.h + 12 },
  }, { ...req, sanitizedSourceUrl: 'https://membership.moma.org/' });
  log('crop membership cta', join.text);
}

fs.writeFileSync(path.join(READ, 'states.json'), JSON.stringify({ ...notes, capturedAt: new Date().toISOString() }, null, 2));
await browser.close();
log('done');
