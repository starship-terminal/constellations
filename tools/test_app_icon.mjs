// Runs docs/assets/app-icon.js against a recording DOM stub: no browser needed.
// `make test` runs it through tools/test_site.py when Node.js is on PATH.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import vm from 'node:vm';

const SRC = fs.readFileSync(path.join(import.meta.dirname, '..', 'docs', 'assets', 'app-icon.js'), 'utf8');
const ASSETS = 'http://site.test/assets/';
const FLAT = ['icon ' + ASSETS + 'icons/favicon.ico', 'icon ' + ASSETS + 'favicon.svg',
              'apple-touch-icon ' + ASSETS + 'icons/apple-touch-icon.png'];
const GLASS = [16, 32, 48].map((s) => `icon ${ASSETS}icons/glass/favicon-${s}.png`)
  .concat('apple-touch-icon ' + ASSETS + 'icons/glass/apple-touch-icon.png');

// A page whose <head> holds the Flat links and the manifest, as site.py writes it.
function page(stored) {
  const log = [];
  const events = [];
  const listeners = {};
  const store = new Map(stored ? [['ds-icon', stored]] : []);
  const head = { children: [] };
  const link = (rel, href) => {
    const el = { rel, href, attrs: {}, setAttribute(k, v) { this.attrs[k] = v; },
                 get nextSibling() { return head.children[head.children.indexOf(el) + 1] ?? null; },
                 remove() { head.children.splice(head.children.indexOf(el), 1); log.push('remove'); } };
    return el;
  };
  head.children.push(...FLAT.map((s) => link(...s.split(' '))), link('manifest', 'http://site.test/site.webmanifest'));
  head.querySelectorAll = (sel) => {
    const rels = [...sel.matchAll(/rel="([^"]+)"/g)].map((m) => m[1]);
    return head.children.filter((el) => rels.includes(el.rel));
  };
  head.insertBefore = (el, ref) => {
    const at = ref ? head.children.indexOf(ref) : -1;
    head.children.splice(at < 0 ? head.children.length : at, 0, el);
    log.push('insert');
  };
  const document = {
    head,
    currentScript: { src: ASSETS + 'app-icon.js' },
    documentElement: { dataset: {} },
    createElement: () => link('', ''),
    dispatchEvent: (e) => events.push(e.detail),
  };
  const window = { addEventListener: (type, fn) => { listeners[type] = fn; } };
  const localStorage = { getItem: (k) => store.get(k) ?? null, setItem: (k, v) => store.set(k, v) };
  class CustomEvent { constructor(type, init) { this.type = type; this.detail = init.detail; } }
  vm.runInNewContext(SRC, { document, window, localStorage, CustomEvent, URL });
  return {
    api: window.dsAppIcon, log, events, store, listeners,
    icons: () => head.children.filter((el) => el.rel !== 'manifest').map((el) => `${el.rel} ${el.href}`),
    last: () => head.children[head.children.length - 1].rel,
    icon: () => document.documentElement.dataset.icon,
  };
}

test('a fresh visit keeps the Flat links the markup carries', () => {
  const p = page();
  assert.deepEqual(p.icons(), FLAT);
  assert.equal(p.icon(), 'flat');
  assert.deepEqual(p.log, []);
});

test('a stored Glass choice is applied while the script runs, before first paint', () => {
  const p = page('glass');
  assert.deepEqual(p.icons(), GLASS);
  assert.equal(p.icon(), 'glass');
  assert.equal(p.last(), 'manifest');
});

test('an unknown stored value falls back to Flat', () => {
  assert.deepEqual(page('neon').icons(), FLAT);
});

test('a live switch removes every old link before adding the new set', () => {
  // Chrome re-picks the tab icon on insertion only; inserting first leaves it on the old set.
  const p = page();
  p.api.set('glass');
  assert.deepEqual(p.log, ['remove', 'remove', 'remove', 'insert', 'insert', 'insert', 'insert']);
  assert.deepEqual(p.icons(), GLASS);
  assert.equal(p.store.get('ds-icon'), 'glass');
  assert.deepEqual(p.events, ['glass']);
  p.log.length = 0;
  p.api.set('flat');
  assert.deepEqual(p.log, ['remove', 'remove', 'remove', 'remove', 'insert', 'insert', 'insert']);
  assert.deepEqual(p.icons(), FLAT);
  assert.equal(p.icon(), 'flat');
});

test('another tab changing the choice is followed', () => {
  const p = page();
  p.store.set('ds-icon', 'glass');
  p.listeners.storage({ key: 'ds-icon' });
  assert.deepEqual(p.icons(), GLASS);
  assert.equal(p.api.get(), 'glass');
  assert.deepEqual(p.events, ['glass']);
});
