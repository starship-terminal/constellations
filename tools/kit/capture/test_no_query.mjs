import assert from 'node:assert/strict';
import test from 'node:test';
import { noQuery, scrubQueries } from './no-query.mjs';

test('queries go from absolute, scheme-relative and relative URLs in recorded text', () => {
  const cases = {
    'https://cdn.example.test/a.png?X-Amz-Signature=1': 'https://cdn.example.test/a.png',
    '"https://cdn.example.test/a(1).png?token=abc"': '"https://cdn.example.test/a(1).png"',
    'https://cdn.example.test/a.png?crop=(0,0)&token=abc 2x': 'https://cdn.example.test/a.png 2x',
    '//cdn.example.test/avatar.png?token=secret': '//cdn.example.test/avatar.png',
    '"//cdn.example.test/a.png#access_token=abc"': '"//cdn.example.test/a.png"',
    'image-set("//cdn.example.test/a.png?sig=1" 1x, //cdn.example.test/b.png?sig=2 2x)': 'image-set("//cdn.example.test/a.png" 1x, //cdn.example.test/b.png 2x)',
    '/media/avatar.png?token=secret': '/media/avatar.png',
    '"avatar.png?sig=abc"': '"avatar.png"',
    'img[src="/a/b.png?sig=1"]': 'img[src="/a/b.png"]',
  };
  for (const [v, want] of Object.entries(cases)) assert.equal(noQuery(v), want, v);
});

test('plain values are left alone', () => {
  for (const v of ['#5e6ad2', 'calc(100% - 2px)', '0 1px 2px rgba(0, 0, 0, 0.1)', '1.5rem', 'url(…)', 'a // b', '', 'var(--x, 4px)', 'icons.svg#close'])
    assert.equal(noQuery(v), v, v);
  assert.equal(noQuery(3), 3);
});

test('scrubQueries walks objects, arrays and keys', () => {
  assert.deepEqual(scrubQueries({ '--a': '//x.test/a.png?t=1', list: ['/b.png?t=2', 4], 'img[src="/c.png?sig=3"]': 1 }),
    { '--a': '//x.test/a.png', list: ['/b.png', 4], 'img[src="/c.png"]': 1 });
});
