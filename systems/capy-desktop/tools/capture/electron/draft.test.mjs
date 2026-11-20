// node --test draft.test.mjs (test_draft.py runs it from `make test`).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { draftText, restoreDraft } from './draft.mjs';

// A fake localStorage key; reload() can drop the write to model a composer that overwrote it.
function fake({ lose = false } = {}) {
  const s = { value: 'null', writes: 0, reloads: 0 };
  return {
    s,
    write: async v => { s.writes++; s.value = v; },
    reload: async () => { s.reloads++; if (lose) s.value = 'null'; },
    read: async () => s.value,
  };
}

test('an empty draft (the JSON text null) needs nothing', async () => {
  const f = fake();
  assert.equal(await restoreDraft({ ...f, saved: 'null' }), false);
  assert.equal(await restoreDraft({ ...f, saved: null }), false);
  assert.equal(f.s.writes, 0);
});

test('no saved draft still checks the composer read back empty', async () => {
  const f = fake();
  f.s.value = JSON.stringify({ text: 'left over from the run' });
  await assert.rejects(restoreDraft({ ...f, saved: 'null' }), /not restored/);
  assert.equal(f.s.writes, 0);
});

test('a multi-line draft is written back whole, never typed', async () => {
  const saved = JSON.stringify({ text: 'first line\nsecond line\n', project: 'p' });
  const f = fake();
  assert.equal(await restoreDraft({ ...f, saved }), true);
  assert.equal(f.s.value, saved);
  assert.equal(f.s.writes, 1);
  assert.equal(f.s.reloads, 1);
});

test('a draft that does not read back fails the capture', async () => {
  const f = fake({ lose: true });
  await assert.rejects(restoreDraft({ ...f, saved: JSON.stringify({ text: 'keep me' }) }), /not restored/);
});

test('unreadable storage counts as no draft', () => {
  assert.equal(draftText('{not json'), '');
  assert.equal(draftText(JSON.stringify({ text: 'a\nb' })), 'a\nb');
});
