// Measures the components the 2026-10-17 refresh copied from the signed-in
// account: the course overflow menu and its tooltip, the review dialog (a CDS
// multiline text field and a disabled Submit), the share dialog after Copy, the
// colour-theme select and the switches on Account settings, and the same
// settings, My Learning and course home in the dark theme the learner can pick.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=~/.design-systems/snaps/coursera node refresh.mjs
//
// The copies come from snapshot.js in a real signed-in tab. Before each copy was
// taken, every element to measure was tagged data-m=<name> in the live page, and
// keyboard states were reached with real keys there, so the CDS focusVisible
// classes and cds-input-focused are in the copy as the product set them
// (state "focus-visible (as captured)"). Hover is a real mouse hover on the copy.
// Nothing here clicks: the copies have no scripts, and the review was never
// rated or submitted.
//
// The copies hold the learner's own course list, so they stay outside the
// repository (SNAPS); unsnap.py refused any copy in which a redacted string
// survived. Writes raw/components-signed-in.json (merged under the keys below),
// crops into components/crops/signed-in/, and one dark screenshot.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { chromium, styleOf, crop, REF, RAW, quantize } from '../lib.mjs';

const SNAPS = (process.env.SNAPS || path.join(os.homedir(), '.design-systems', 'snaps', 'coursera')).replace(/^~/, os.homedir());
const OUT = path.join(RAW, 'components-signed-in.json');
const out = JSON.parse(fs.readFileSync(OUT, 'utf8'));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const CAPTURED = 'focus-visible (as captured)';
const DARK = 'learner chose Appearance: Dark mode';
// [snapshot label, component key, selector, state, description, options]
const SPECS = [
  ['ml-overflow-tooltip', 'ml-overflow-button', '[data-m=overflow-trigger]', CAPTURED, null, { via: 'Shift+Tab, Tab in the live page; the tooltip opened on keyboard focus' }],
  ['ml-overflow-tooltip', 'tooltip-signed-in', '[data-m=tooltip]', 'opened', 'CDS tooltip ("More") shown on keyboard focus of the course overflow button, z-index 11000.', { pad: 6 }],
  ['ml-menu-open', 'overflow-menu', '[data-m=menu-paper]', 'opened', 'Course overflow menu on My Learning (cds-actionOverflowMenu): white popover paper, 16 radius, --cds-elevation-level2, inside a fixed z-index 10000 layer. Opened with Enter on the trigger.', { pad: 16 }],
  ['ml-menu-open', 'overflow-menu-item', '[data-m=menu-item-a]', CAPTURED, 'Menu item (Rate, Share): 40px, 8px padding, 16/24 400. Enter on the trigger focuses the first item with the CDS focus ring.', { via: 'Enter on the trigger in the live page' }],
  ['ml-menu-open', 'overflow-menu-item', '[data-m=menu-item-b]', 'default', null, {}],
  ['ml-menu-open', 'overflow-menu-item', '[data-m=menu-item-b]', 'hover', null, {}],
  ['ml-rate-dialog', 'rate-dialog', '[data-m=rate-paper]', 'opened', 'Course review dialog (legacy rc-Modal, not CDS): white, 3px radius, 28px padding, over a z-index 3000 overlay. Opened from the overflow menu; nothing was rated or submitted.', { pad: 0 }],
  ['ml-rate-dialog', 'text-area-cds', '[data-m=rate-textarea]', 'default', 'CDS multiline text field ("Write your review (optional)"): cds-input-root with cds-input-multiline, notched-outline fieldset, 8 radius.', { pad: 6 }],
  ['ml-rate-dialog', 'text-area-cds', '[data-m=rate-textarea]', 'hover', null, { pad: 6 }],
  ['ml-rate-dialog-textarea-focus', 'text-area-cds', '[data-m=rate-textarea]', CAPTURED, null, { pad: 6, via: 'focused in the live page (cds-input-focused)' }],
  ['ml-rate-dialog', 'button-disabled-legacy', '[data-m=rate-submit]', 'disabled', 'Submit in the review dialog while no rating is chosen: a legacy (non-CDS) button, disabled, grey.200 fill with grey.25 label, 2px radius.', { pad: 6 }],
  ['ml-share-copied', 'share-dialog', '[data-m=share-paper]', 'default', 'Share dialog (legacy, not CDS): five round share targets over the course link and a COPY text button. Pressing COPY in the live page swapped its label to "COPIED!" (read from the DOM straight after); that label swap is the only feedback, no toast appears. The copy was taken after the label had reverted.', { pad: 0 }],
  ['ml-share-copied', 'share-copy-button', '[data-m=share-copy]', 'default', 'COPY text button beside the share link; its label reads "COPIED!" for a moment after a press.', { pad: 6 }],
  ['settings-theme-select-open', 'select-signed-in', '[data-m=theme-select]', 'opened', 'Colour theme select on Account settings (Light mode, Dark mode, System default), CDS select.', { pad: 6 }],
  ['settings-theme-select-open', 'select-menu-signed-in', '[data-m=theme-select-menu]', 'opened', 'Open CDS select list: white paper, 16 radius, --cds-elevation-level2, fixed z-index 10000 layer.', { pad: 16 }],
  ['settings-theme-select-open', 'select-option-signed-in', '[data-m=theme-option-selected-focus]', 'selected, ' + CAPTURED, 'Option row in the CDS select list, 40px. Enter on the field focuses the selected option with cds-selectOption-focusVisible.', { via: 'Enter on the select in the live page' }],
  ['settings-theme-select-open', 'select-option-signed-in', '[data-m=theme-option]', 'default', null, {}],
  ['settings-theme-select-open', 'select-option-signed-in', '[data-m=theme-option]', 'hover', null, {}],
  ['settings-switch-focus', 'switch', '[data-m=switch-on-focus]', 'checked, ' + CAPTURED, 'CDS switch (cds-labs-Switch): 40x24 track, 12 radius, 20px white knob; on is --cds-color-interactive-primary, off is --cds-color-neutral-stroke-primary; the fill and knob move in 0.1s ease-in-out.', { pad: 8, via: 'Shift+Tab, Tab in the live page; the switch was never toggled' }],
  ['settings-switch-focus', 'switch', '[data-m=switch-off]', 'default', null, { pad: 8 }],
  ['settings-switch-focus', 'switch', '[data-m=switch-off]', 'hover', null, { pad: 8 }],
  ['settings-switch-focus', 'callout-warning', '[data-m=callout-warning-0]', 'default', 'Warning callout on Account settings ("Warning: ..."): --cds-color-feedback-background-warning-weak fill, 16 radius, 12px 16px padding, 20px icon in --cds-color-feedback-warning, no border.', { pad: 6 }],
  ['settings-switch-focus', 'button-secondary-destructive', '[data-m=button-danger]', 'default', 'Delete account: the destructive action is an ordinary 48px secondary (outlined blue) button. Never pressed.', { pad: 6 }],
  ['settings-switch-focus', 'button-secondary-destructive', '[data-m=button-danger]', 'hover', null, { pad: 6 }],
  ['settings-dark', 'switch', '[data-m=switch-on]', 'checked, dark', null, { pad: 8, via: DARK }],
  ['settings-dark', 'switch', '[data-m=switch-off]', 'dark', null, { pad: 8, via: DARK }],
  ['settings-dark', 'callout-warning', '[data-m=callout-warning-0]', 'dark', null, { pad: 6, via: DARK }],
  ['settings-dark', 'select-signed-in', '[data-m=theme-select]', 'dark', null, { pad: 6, via: DARK }],
];
// The dark course home (learn-home-dark) was copied too but is not published:
// its module text, item titles and deadlines name the enrolled course.
const SHOTS = [
  ['my-learning-dark', 'my-learning-dark-default.png'],
];

const browser = await chromium.launch();
const pages = {};
async function pageFor(label) {
  if (pages[label]) return pages[label];
  const meta = JSON.parse(fs.readFileSync(path.join(SNAPS, `${label}.json`), 'utf8'));
  const ctx = await browser.newContext({ viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  // Nothing may leave the file: only GETs for images, fonts and styles load.
  await page.route('**/*', (r) => (r.request().url().startsWith('file:') || (r.request().method() === 'GET' && ['image', 'font', 'stylesheet'].includes(r.request().resourceType())) ? r.continue() : r.abort()));
  await page.goto(pathToFileURL(path.resolve(SNAPS, `${label}.html`)).href, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(2000);
  if (meta.scrollY) await page.evaluate((y) => scrollTo(0, y), meta.scrollY);
  await page.evaluate(() => { const s = document.createElement('style'); s.textContent = '*{caret-color:transparent!important}'; document.head.appendChild(s); });
  pages[label] = { page, meta };
  return pages[label];
}

out._meta.refresh = {
  capturedAt: '2026-10-17',
  source: 'snapshot.js copies of the signed-in pages, kept outside the repository; measured by tools/capture/signed-in/refresh.mjs',
  pages: {},
};
for (const [label, key, sel, state, description, opts] of SPECS) {
  const { page, meta } = await pageFor(label);
  out._meta.refresh.pages[label] = { url: meta.url.replace(/\/learn\/[^/]+/, '/learn/example-course'), w: meta.w, h: meta.h, theme: /dark/.test(label) ? 'dark (learner setting)' : 'light' };
  const c = (out.components[key] ??= { states: {} });
  c.page = c.page || label;
  if (description) c.description = description;
  c.refresh = true;
  const loc = page.locator(sel).first();
  try {
    await page.mouse.move(meta.w - 2, meta.h - 2);
    await loc.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' }));
    await page.waitForTimeout(250);
    if (state === 'hover') { await loc.hover({ force: true }); await page.waitForTimeout(450); }
    const s = await styleOf(loc);
    s.text = s.text ? s.text.replace(/\s+/g, ' ').slice(0, 40) : s.text;
    const name = `signed-in/${key}-${state.replace(/[^a-z0-9]+/gi, '-').replace(/-+$/, '').toLowerCase()}`;
    s.crop = await crop(page, loc, name, opts.pad ?? 8).catch((e) => { s.cropError = String(e.message).slice(0, 120); return undefined; });
    c.states[state] = { ...s, via: opts.via || (state === 'hover' ? 'mouse hover on the copy' : 'as captured'), snapshot: label };
    log(key, state, `${s.rect.w}x${s.rect.h}`);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200), snapshot: label };
    log('!', key, state, String(e.message).slice(0, 120));
  }
}
for (const [label, file] of SHOTS) {
  const { page } = await pageFor(label);
  await page.mouse.move(2, 2);
  const f = path.join(REF, 'screenshots', file);
  await page.screenshot({ path: f });
  quantize(f);
  log('shot', file);
}
fs.writeFileSync(OUT, JSON.stringify(out, null, 1));
await browser.close();
