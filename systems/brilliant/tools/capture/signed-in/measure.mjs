// Measure Brilliant's components per state from the static page copies (headless, both themes).
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=~/.design-systems/snaps/brilliant node tools/capture/signed-in/measure.mjs
// Writes raw/components-computed.json. Each spec names a copy, a selector (found by data-slot, role
// or label, never by account text) and the states to read. hover, active (pressed) and
// focus-visible are forced on the element with the DevTools protocol (CSS.forcePseudoState), so
// they are the browser's own computed styles for that state, not inferred. selected, checked,
// disabled and open are read where the product rendered them that way in the copy.
// Each state is also cut out as a crop (the element's box plus 16px) into $SNAPS/crops/, which
// quantize.py turns into components/crops/2026-10/<component>-<theme>-<state>.png.
// Adapted from the kit's signed-in measure.mjs (tools/kit/capture/signed-in/measure.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { chromium, RAW, openSnap, newContext, metaOf } from './lib.mjs';

// PRODUCT (adapt): one entry per checklist component the product has.
const S = (name, copy, sel, opts = {}) => ({ name, copy, sel, states: ['default', 'hover', 'focus-visible', 'active'], ...opts });
const SPECS = [
  S('button3d-blue', 'home-dark-default', '[data-slot=button3d]', { part: '[data-slot=button3d-face]', pick: (els) => els.find((e) => e.textContent.trim() === 'Start') }),
  S('button3d-neutral', 'lesson-dark-quit-dialog', '[data-slot=modal-content] [data-slot=button3d]', { part: '[data-slot=button3d-face]' }),
  S('button3d-disabled', 'lesson-dark-quit-dialog', '[data-slot=button3d][data-disabled]', { part: '[data-slot=button3d-face]', states: ['default'] }),
  S('button-danger-text', 'lesson-dark-quit-dialog', '[data-slot=modal-content] [data-slot=button]'),
  S('button-inverse', 'settings-dark-account', '[data-slot=button]', { pick: (els) => els.find((e) => /Add another email/.test(e.textContent)) }),
  S('button-outline', 'settings-dark-account', '[data-slot=button]', { pick: (els) => els.find((e) => /Send verification/.test(e.textContent)) }),
  S('button-disabled', 'settings-dark-account', '[data-slot=button][data-disabled]', { states: ['default', 'hover'] }),
  S('icon-button', 'you-dark-empty', '[data-slot=icon-button][aria-label="Previous period"]'),
  S('icon-button-disabled', 'you-dark-empty', '[data-slot=icon-button][aria-label="Next period"]', { states: ['default', 'hover'] }),
  S('icon-button-toggle', 'courses-dark-default', '[data-slot=icon-button][aria-pressed]'),
  S('link', 'settings-dark-account', 'footer a[data-slot=link], a[data-slot=link]'),
  S('nav-tab-selected', 'home-dark-default', 'a[data-selected="true"]'),
  S('nav-tab', 'home-dark-default', 'a[data-selected="false"]'),
  S('settings-tab-selected', 'settings-dark-preferences', 'button[data-slot=button]', { pick: (els) => els.find((e) => e.textContent.trim() === 'Preferences') }),
  S('settings-tab', 'settings-dark-preferences', 'button[data-slot=button]', { pick: (els) => els.find((e) => e.textContent.trim() === 'Account') }),
  S('segment-selected', 'settings-dark-preferences', '[data-slot=segment][data-checked], [role=radio][data-checked]'),
  S('segment', 'settings-dark-preferences', '[data-slot=segment][data-unchecked], [role=radio][data-unchecked]'),
  S('segment-track', 'settings-dark-preferences', '[data-slot=radio-group], [role=radiogroup]', { states: ['default'] }),
  S('switch-on', 'settings-dark-preferences', '[data-slot=switch][data-checked]', { part: '[data-slot=switch-thumb]' }),
  S('switch-off', 'settings-dark-preferences', '[data-slot=switch][data-unchecked]', { part: '[data-slot=switch-thumb]' }),
  S('radio', 'settings-dark-account', '[data-slot=radio]', { part: '[data-slot=radio-indicator]' }),
  S('text-field', 'settings-dark-account', 'input[type=text]'),
  S('text-area', 'koji-dark-textarea-filled', 'textarea', { states: ['default', 'focus-visible'] }),
  S('text-area-pill', 'koji-dark-textarea-filled', 'textarea', { up: 4, states: ['default', 'focus-visible'] }),
  S('menu-item', 'home-dark-menu-keyboard', '[data-slot=dropdown-menu-item]:not([data-highlighted])'),
  S('menu-item-highlighted', 'home-dark-menu-keyboard', '[data-slot=dropdown-menu-item][data-highlighted]', { states: ['default', 'focus-visible'] }),
  S('menu', 'home-dark-menu-keyboard', '[role=menu]', { states: ['default'] }),
  S('tooltip', 'you-dark-tooltip', '[data-slot=tooltip-content]', { states: ['default'] }),
  S('tooltip-trigger', 'you-dark-tooltip', '[data-slot=tooltip-trigger]'),
  S('dialog', 'lesson-dark-quit-dialog', '[data-slot=modal-content]', { states: ['default'] }),
  S('dialog-scrim', 'lesson-dark-quit-dialog', '[data-slot=modal-overlay]', { states: ['default'] }),
  S('card-course', 'courses-dark-default', '[data-slot=card]'),
  S('list-row-setting', 'settings-dark-preferences', 'div', { pick: (els) => els.filter((e) => /^Enable sound effects in lessons$/.test(e.innerText.trim()) && parseFloat(getComputedStyle(e).borderTopWidth) > 0).pop(), states: ['default', 'hover'] }),
  S('avatar', 'mobile-you-dark-empty', '[role=img][aria-label]', { states: ['default'] }),
  S('badge-unverified', 'settings-dark-account', '.panda-badge--colorPalette_yellow', { states: ['default'] }),
  S('badge-primary', 'settings-dark-account', '.panda-badge--colorPalette_blue', { states: ['default'] }),
  S('premium-button', 'home-dark-default', '[data-slot=premium-button]'),
  S('progress', 'home-dark-default', '[data-slot=progress], [role=progressbar]', { states: ['default'] }),
  S('weekly-summary-card', 'you-dark-empty', 'section, [data-slot=box]', { pick: (els) => els.find((e) => /Weekly summary/.test(e.textContent) && e.getBoundingClientRect().height < 200 && e.getBoundingClientRect().height > 80), states: ['default'] }),
];
const PROPS = ['width', 'height', 'background-color', 'background-image', 'color', 'border-top-width', 'border-top-style', 'border-top-color', 'border-radius', 'box-shadow', 'outline-color', 'outline-style', 'outline-width', 'outline-offset', 'opacity', 'transform', 'padding', 'gap', 'font-family', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'text-transform', 'text-decoration-line', 'backdrop-filter', 'transition', 'cursor'];
const FORCE = { hover: ['hover'], 'focus-visible': ['focus', 'focus-visible'], active: ['active', 'hover'] };

const CROPS_RAW = path.join(process.env.SNAPS, 'crops');
fs.mkdirSync(CROPS_RAW, { recursive: true });
const b = await chromium.launch();
const out = { _meta: { source: 'Computed styles from the 2026-10-17 page copies of the signed-in app, rendered headless at the captured viewport, 2x. hover, focus-visible and active are forced with CSS.forcePseudoState; light is the same copy with <html data-theme="light">.', props: PROPS } };
const byCopy = {};
for (const s of SPECS) (byCopy[s.copy] ||= []).push(s);
for (const [copy, specs] of Object.entries(byCopy)) {
  for (const theme of ['dark', 'light']) {
    let ctx, page;
    try {
      ctx = await newContext(b, metaOf(copy), theme === 'light');
      page = await openSnap(ctx, copy, { light: theme === 'light' });
    } catch (e) { for (const s of specs) (out[s.name] ||= {})[theme] = { error: 'copy did not open: ' + e.message }; continue; }
    const cdp = await ctx.newCDPSession(page);
    await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
    for (const s of specs) {
      const found = await page.evaluate(({ sel, pick, up, name }) => {
        const els = [...document.querySelectorAll(sel)].filter((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
        let el = pick ? (0, eval)('(' + pick + ')')(els) : els[0];
        for (let i = 0; el && i < (up || 0); i++) el = el.parentElement;
        if (!el) return { count: els.length };
        el.setAttribute('data-m', name);
        return { count: els.length, text: el.textContent.trim().slice(0, 40) };
      }, { sel: s.sel, pick: s.pick && s.pick.toString(), up: s.up, name: s.name });
      const rec = { selector: s.sel, matches: found.count };
      if (found.text === undefined) { rec.error = 'not found in copy'; (out[s.name] ||= {})[theme] = rec; continue; }
      rec.label = found.text;
      const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
      const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: `[data-m="${s.name}"]` });
      for (const st of s.states) {
        await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: FORCE[st] || [] });
        await page.waitForTimeout(st === 'default' ? 50 : 450); // let transitions settle
        rec[st] = await page.evaluate(({ name, part, props }) => {
          const el = document.querySelector(`[data-m="${name}"]`);
          const read = (n) => { const cs = getComputedStyle(n); const o = {}; for (const p of props) o[p] = cs.getPropertyValue(p); return o; };
          const r = { self: read(el) };
          const p = part && el.querySelector(part);
          if (p) r.part = read(p);
          return r;
        }, { name: s.name, part: s.part, props: PROPS });
        const box = await page.evaluate((name) => { const e = document.querySelector(`[data-m="${name}"]`); const r0 = e.getBoundingClientRect(); if (r0.bottom > innerHeight || r0.top < 0) e.scrollIntoView({ block: 'center' }); const r = e.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; }, s.name);
        const pad = 16, vw = page.viewportSize();
        const clip = { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad) };
        clip.width = Math.min(vw.width, box.x + box.w + pad) - clip.x; clip.height = Math.min(vw.height, box.y + box.h + pad) - clip.y;
        // A forced state that changed nothing gets no crop, so every crop shows a real difference.
        const same = st !== 'default' && JSON.stringify(rec[st]) === JSON.stringify(rec.default);
        if (!same && clip.width > 4 && clip.height > 4) await page.screenshot({ path: path.join(CROPS_RAW, `${s.name}-${theme}-${st}.png`), clip });
      }
      await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] });
      (out[s.name] ||= {})[theme] = rec;
    }
    await ctx.close();
    console.log('measured', copy, theme);
  }
}
await b.close();
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote raw/components-computed.json', Object.keys(out).length - 1, 'components');
