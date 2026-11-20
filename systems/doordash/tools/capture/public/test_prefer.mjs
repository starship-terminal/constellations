import assert from 'node:assert/strict';
import test from 'node:test';
import { prefer } from './prefer.mjs';

// A stand-in for Playwright locators over a list of nodes in DOM order. A node is { id, visible, kind }.
function locator(nodes, match) {
  return {
    filter: ({ visible }) => locator(nodes, (n) => match(n) && (!visible || n.visible)),
    count: async () => nodes.filter(match).length,
  };
}

test('prefer takes the first candidate with a visible match, not the first match in the DOM', async () => {
  const nodes = [{ id: 'fallback', visible: true, kind: 'input' }, { id: 'hidden', visible: false, kind: 'pc' }, { id: 'wanted', visible: true, kind: 'm' }];
  const m = locator(nodes, (n) => n.kind === 'm'), pc = locator(nodes, (n) => n.kind === 'pc'), any = locator(nodes, () => true);
  assert.equal(await prefer(m, pc, any), m);
  assert.equal(await prefer(pc, any), any, 'a candidate matching only hidden nodes is passed over');
  const none = locator(nodes, () => false);
  assert.equal(await prefer(none, pc), none, 'with no visible match the first is returned, and S records it missing');
});
