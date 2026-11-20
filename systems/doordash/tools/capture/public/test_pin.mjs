import assert from 'node:assert/strict';
import test from 'node:test';
import { pin, prefer, unpin } from './pin.mjs';

// A stand-in for Playwright: a list of nodes in DOM order, and locators that find nodes again on
// every call, as Playwright's do. A node is { id, visible, attrs }.
function fakePage(nodes) {
  const locator = (match) => ({
    match,
    all: () => nodes.filter(match),
    filter: ({ visible }) => locator((n) => match(n) && (!visible || n.visible)),
    first() { const self = this; return { ...locator((n) => self.all()[0] === n), count: async () => (self.all().length ? 1 : 0),
      evaluate: async (fn, arg) => { const n = self.all()[0]; fn({ setAttribute: (k, v) => { n.attrs[k] = v; } }, arg); } }; },
    count: async () => nodes.filter(match).length,
  });
  const page = {
    locator: (sel) => { const m = sel.match(/^\[data-m-pin="(.+)"\]$/); return locator((n) => n.attrs['data-m-pin'] === m[1]); },
    evaluate: async (fn, arg) => {
      const doc = { querySelectorAll: (sel) => { const m = sel.match(/^\[data-m-pin="(.+)"\]$/); return nodes.filter((n) => n.attrs['data-m-pin'] === m[1]).map((n) => ({ removeAttribute: (k) => { delete n.attrs[k]; } })); } };
      const saved = globalThis.document; globalThis.document = doc;
      try { return fn(arg); } finally { globalThis.document = saved; }
    },
  };
  return { page, locator };
}

test('every state is read from the node the finder found first, though the finder now finds another', async () => {
  const nodes = [{ id: 'tab1', visible: true, attrs: { class: 'current' } }, { id: 'tab2', visible: true, attrs: {} }, { id: 'tab3', visible: true, attrs: {} }];
  const { page, locator } = fakePage(nodes);
  const notCurrent = locator((n) => n.attrs.class !== 'current');     // like [role=tab]:not(.current)
  const loc = await pin(page, notCurrent, 'tab');
  assert.equal(loc.all()[0].id, 'tab2');
  nodes[0].attrs.class = ''; nodes[1].attrs.class = 'current';        // the "selected" state moved .current
  assert.equal(notCurrent.filter({ visible: true }).all()[0].id, 'tab1', 'the finder alone now gives another node');
  assert.deepEqual(loc.all().map((n) => n.id), ['tab2']);
  await unpin(page, 'tab');
  assert.equal(await loc.count(), 0);
});

test('a second pin of the same component moves the mark; nothing visible gives null', async () => {
  const nodes = [{ id: 'a', visible: true, attrs: {} }, { id: 'b', visible: false, attrs: {} }];
  const { page, locator } = fakePage(nodes);
  await pin(page, locator(() => true), 'x');
  nodes[0].visible = false; nodes[1].visible = true;
  const loc = await pin(page, locator(() => true), 'x');
  assert.deepEqual(loc.all().map((n) => n.id), ['b']);
  assert.equal(await pin(page, locator((n) => n.id === 'none'), 'y'), null);
});

test('prefer takes the first candidate with a visible match, not the first match in the DOM', async () => {
  const nodes = [{ id: 'fallback', visible: true, attrs: { kind: 'input' } }, { id: 'hidden', visible: false, attrs: { kind: 'pc' } }, { id: 'wanted', visible: true, attrs: { kind: 'm' } }];
  const { locator } = fakePage(nodes);
  const m = locator((n) => n.attrs.kind === 'm'), pc = locator((n) => n.attrs.kind === 'pc'), any = locator(() => true);
  assert.equal(await prefer(m, pc, any), m);
  assert.equal(await prefer(pc, any), any, 'a candidate matching only hidden nodes is passed over');
  const none = locator(() => false);
  assert.equal(await prefer(none, pc), none, 'with no visible match the first is returned, and S records it missing');
});
