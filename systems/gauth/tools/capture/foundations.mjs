// Reads the foundations the other readers do not: what Gauth's stylesheets change under
// prefers-reduced-motion (and what a page actually paints with it emulated), the z-index of every
// layer on each page and in its dialogs, and the brand colour evidence (theme-color meta, mask-icon,
// web manifest). Writes raw/foundations.json.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node foundations.mjs
//
// Like vars.mjs it keeps every stylesheet response body, since Gauth's CSS sits on a CDN the CSSOM
// cannot read cross-origin, and parses each with a constructed CSSStyleSheet. The only presses are the
// ones that open a dialog (the Sign in dialog, the Gauth PLUS dialog) so their layers can be read;
// both are closed again and nothing in them is used.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, open, RAW } from './lib.mjs';

const PAGES = {
  home: '/', academy: '/course/science', unit: '/course/math/algebra-1?unit=real-numbers-and-sets',
  'lesson-science': '/course/science/how-things-work-1/learn?entry_source=start&from=science',
  'lesson-math': '/course/math/algebra-1/fundamentals-of-set-theory/learn?entry_source=start&return_to=course_detail',
  atlas: '/atlas', news: '/news', plus: '/plus',
};

// Elements whose transitions are compared with and without reduced motion emulated.
const PROBES = {
  home: [['sidebar item', M('side-menu_side-menu-item')], ['subject chip', M('resources-list_resources-item')]],
  academy: [['lesson card', M('catalog_premiumCard')], ['category tab', M('catalog_categoryTab')], ['Create Course', M('catalog_createButton')]],
  unit: [['Start button', M('math-course-detail_lessonAction')], ['topic node', M('math-course-detail_topicButton')]],
  'lesson-science': [['transport button', 'button.astryx-button'], ['Ask Tutor bar', M('canvas_shell')]],
  atlas: [['story card', M('user-cases_card')], ['recommendation chip', M('atlas-landing_recommendation-chip')]],
};

const strip = (s) => String(s).replace(/__[A-Za-z0-9_-]{5,6}\b/g, '');
const out = { url: BASE, read: new Date().toLocaleDateString('en-CA'), pages: PAGES, reducedMotion: {}, reducedMotionPaint: {}, zIndex: {}, brand: {}, declaredRules: {}, astryxResolved: {} };

// Gauth rules recorded verbatim (hash stripped) because the package cites values read from them that no page
// captured paints: the button component's states, the form error, the markdown code styles, the Atlas delete dialog.
const DECLARED = /^(\.button_btn-primary(__\w+)?(:not\([^)]*\))*(:hover|:active)?|\.button_btn-primary-default-disabled|\.form_error-msg|\.form_form-item(\.form_\w+)+(:not\([^)]*\))?( input)?|\.input_input-wrapper\.input_(email|password)-error.*|\.md-container (code|pre).*|\.markdown-body code|\.highlight pre, pre|pre code, pre tt|\.wap-atlas-drawer_(delete|cancelDelete|confirmDelete)\w*.*|\.header_delete\w+.*|\.header_historyItem:(hover|focus-within) \.header_deleteBtn)$/;
// Astryx's status variables, resolved on the page root and inside a stone-themed Astryx element of the science player.
const ASTRYX_VARS = ['--color-background-yellow', '--color-text-yellow', '--color-border-yellow', '--color-background-green', '--color-text-green', '--color-border-green', '--color-background-red', '--color-text-red', '--color-border-red', '--color-background-blue', '--color-text-blue', '--color-border-blue', '--color-text-primary'];

const { browser, context } = await launch();
for (const [key, p] of Object.entries(PAGES)) {
  const page = await context.newPage();
  const bodies = new Map();
  page.on('response', async (r) => {
    if (r.request().resourceType() !== 'stylesheet') return;
    try { bodies.set(r.url().split('?')[0], await r.text()); } catch { /* body gone */ }
  });
  console.log('open', key);
  try {
    await open(page, BASE + p, { wait: 7000 });
  } catch (e) { out.reducedMotion[key] = { error: String(e.message).split('\n')[0] }; await page.close(); continue; }
  const themes = () => page.evaluate(() => [...document.querySelectorAll('[data-astryx-theme]')].map((e) => `${e === document.documentElement ? 'html' : e.tagName.toLowerCase()}=${e.getAttribute('data-astryx-theme')}`));
  const themesBefore = await themes();
  const nn = page.getByRole('button', { name: 'Not now' });
  if (await nn.count()) { await nn.click().catch(() => {}); await page.waitForTimeout(1200); }
  if (key === 'lesson-science') out.astryxThemes = { withAudioDialog: themesBefore, afterNotNow: await themes() };
  // the math player waits behind an audio gate; its Continue starts playback, so the layers read are the player's
  const gate = page.getByRole('button', { name: 'Continue', exact: true });
  if (key === 'lesson-math' && await gate.count()) { await gate.click().catch(() => {}); await page.waitForTimeout(4000); }

  // every rule inside a prefers-reduced-motion condition, in Gauth's sheets and the inline ones
  const inline = await page.evaluate(() => [...document.styleSheets].filter((s) => !s.href).map((s, i) => { try { return ['inline-' + i, [...s.cssRules].map((r) => r.cssText).join('\n')]; } catch { return null; } }).filter(Boolean));
  const sheets = [...bodies.entries()].map(([u, t]) => [u.replace(/^https?:\/\/[^/]+/, '').replace(/^.*\/static\/css\//, 'css/'), t]).concat(inline);
  const rules = await page.evaluate((sheets) => {
    const res = [];
    for (const [name, text] of sheets) {
      const s = new CSSStyleSheet();
      try { s.replaceSync(text); } catch { continue; }
      const walk = (rs, media) => {
        for (const r of rs) {
          if (r instanceof CSSMediaRule) { walk(r.cssRules, [...media, r.conditionText]); continue; }
          if (r.cssRules && !r.style) { walk(r.cssRules, media); continue; }
          if (!r.style || !media.some((m) => /prefers-reduced-motion/.test(m))) continue;
          res.push({ sheet: name.startsWith('inline-') ? 'inline' : name, media: media.join(' and '), selector: (r.selectorText || '').slice(0, 200), declarations: r.style.cssText.slice(0, 300) });
        }
      };
      walk(s.cssRules, []);
    }
    return res;
  }, sheets);
  out.reducedMotion[key] = rules.map((r) => ({ ...r, selector: strip(r.selector) }));
  const declared = await page.evaluate((sheets) => {
    const res = [];
    for (const [name, text] of sheets) {
      if (name.startsWith('inline-')) continue;
      const s = new CSSStyleSheet();
      try { s.replaceSync(text); } catch { continue; }
      const walk = (rs, media) => { for (const r of rs) { if (r instanceof CSSMediaRule) { walk(r.cssRules, [...media, r.conditionText]); continue; } if (r.cssRules && !r.style) { walk(r.cssRules, media); continue; } if (r.style && r.selectorText) res.push({ sheet: name, media: media.join(' and ') || null, selector: r.selectorText, declarations: r.style.cssText }); } };
      walk(s.cssRules, []);
    }
    return res;
  }, sheets);
  for (const r of declared) {
    const sel = strip(r.selector).replace(/\[dir=(ltr|rtl)\] /, '');
    if (!DECLARED.test(sel)) continue;
    out.declaredRules[sel] ??= { declarations: r.declarations, media: r.media, sheet: r.sheet.replace(/\.[0-9a-f]{10}\.css$/, '.css'), pages: [] };
    if (!out.declaredRules[sel].pages.includes(key)) out.declaredRules[sel].pages.push(key);
  }
  if (key === 'lesson-science') {
    await page.waitForSelector('[data-astryx-theme="stone"]', { timeout: 20000 }).catch(() => {});
    out.astryxResolved = await page.evaluate((names) => {
      const read = (el) => { const probe = document.createElement('span'); el.appendChild(probe); const o = {}; for (const n of names) { probe.style.color = `var(${n})`; o[n] = getComputedStyle(probe).color; } probe.remove(); return o; };
      const all = [...document.querySelectorAll('[data-astryx-theme="stone"]')].filter((e) => e !== document.documentElement);
      const stone = all.find((e) => e.getBoundingClientRect().width > 0) || all[0];
      const box = stone && stone.getBoundingClientRect();
      return { root: { element: 'body', htmlTheme: document.documentElement.getAttribute('data-astryx-theme'), values: read(document.body) }, stone: stone ? { element: stone.tagName.toLowerCase() + '[data-astryx-theme="stone"]', size: `${Math.round(box.width)}x${Math.round(box.height)}`, values: read(stone) } : null };
    }, ASTRYX_VARS);
  }

  // what the probes paint with and without reduced motion
  if (PROBES[key]) {
    const read = () => page.evaluate((probes) => Object.fromEntries(probes.map(([n, sel]) => {
      const e = [...document.querySelectorAll(sel)].find((x) => x.getBoundingClientRect().width > 0);
      if (!e) return [n, null];
      const c = getComputedStyle(e);
      return [n, { transitionProperty: c.transitionProperty, transitionDuration: c.transitionDuration, animationName: c.animationName, animationDuration: c.animationDuration }];
    })), PROBES[key]);
    const normal = await read();
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.waitForTimeout(600);
    const reduced = await read();
    await page.emulateMedia({ reducedMotion: 'no-preference' });
    out.reducedMotionPaint[key] = Object.fromEntries(Object.keys(normal).map((n) => [n, { normal: normal[n], reduced: reduced[n], changed: JSON.stringify(normal[n]) !== JSON.stringify(reduced[n]) }]));
  }

  // z-index layers: every element that sets one and is on screen or fixed
  const layers = () => page.evaluate(() => {
    const st = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}\b/g, '');
    const seen = new Map();
    for (const e of document.querySelectorAll('body *')) {
      if (e.closest('svg')) continue;
      const c = getComputedStyle(e);
      if (c.zIndex === 'auto' || c.position === 'static') continue;
      const r = e.getBoundingClientRect();
      if (r.width < 8 || r.height < 8) continue;
      const name = e.tagName.toLowerCase() + [...e.classList].map(st).filter((x) => /_|astryx|ant-/.test(x)).slice(0, 2).map((x) => '.' + x).join('');
      const k = name + '|' + c.zIndex;
      if (!seen.has(k)) seen.set(k, { el: name, z: Number(c.zIndex), position: c.position, w: Math.round(r.width), h: Math.round(r.height) });
    }
    return [...seen.values()].sort((a, b) => b.z - a.z).slice(0, 25);
  });
  out.zIndex[key] = await layers();
  if (key === 'home') {
    // the two dialogs a visitor can open here: read their layers, then close them
    await page.locator(M('pc-header_loginEntry')).first().click().catch(() => {});
    await page.waitForTimeout(2500);
    out.zIndex['home: Sign in dialog open'] = await layers();
    await page.locator(M('modal-container_modal-close')).filter({ visible: true }).first().click({ force: true }).catch(() => page.keyboard.press('Escape'));
    await page.waitForTimeout(1000);
    await page.locator(M('side-menu-small-cards_btn')).first().click().catch(() => {});
    await page.waitForTimeout(2500);
    out.zIndex['home: PLUS dialog open'] = await layers();
    await page.keyboard.press('Escape').catch(() => {});
    // brand colour evidence
    out.brand = await page.evaluate(async () => {
      const metas = [...document.querySelectorAll('meta[name="theme-color"]')].map((m) => ({ content: m.content, media: m.media || null }));
      const mask = [...document.querySelectorAll('link[rel="mask-icon"]')].map((l) => ({ color: l.getAttribute('color') }));
      const man = document.querySelector('link[rel="manifest"]');
      let manifest = null;
      if (man) { try { const j = await (await fetch(man.href)).json(); manifest = { href: man.getAttribute('href'), theme_color: j.theme_color ?? null, background_color: j.background_color ?? null }; } catch (e) { manifest = { href: man.getAttribute('href'), error: String(e) }; } }
      return { themeColor: metas, maskIcon: mask, manifest };
    });
  }
  await page.close();
}
await browser.close();
const file = path.join(RAW, 'foundations.json');
fs.writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
console.log('->', file);
