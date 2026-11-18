import assert from 'node:assert/strict';
import fs from 'node:fs';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';

// servePages lives in lib.mjs, which imports Playwright at load time; skip when
// it is not installed (set PLAYWRIGHT=<playwright>/index.mjs to run these).
let servePages;
try { ({ servePages } = await import('./public/lib.mjs')); } catch { /* playwright missing */ }

// A raw socket request, so ../ and %2e%2e%2f reach the server exactly as written.
const get = (port, rawPath) => new Promise((resolve, reject) => {
  const req = http.request({ host: '127.0.0.1', port, path: rawPath, method: 'GET' }, (res) => {
    const chunks = [];
    res.on('data', (c) => chunks.push(c));
    res.on('end', () => resolve({ status: res.statusCode, body: Buffer.concat(chunks).toString() }));
  });
  req.on('error', reject);
  req.end();
});

test('servePages never serves or caches a file outside its roots', { skip: !servePages }, async () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'ff-serve-'));
  const pages = path.join(root, 'pages');
  const assets = path.join(root, 'assets');
  fs.mkdirSync(path.join(assets, 'cdn-images'), { recursive: true });
  fs.mkdirSync(pages, { recursive: true });
  fs.writeFileSync(path.join(root, 'secret.txt'), 'SECRET');
  fs.writeFileSync(path.join(assets, 'secret.txt'), 'SECRET');
  fs.writeFileSync(path.join(pages, 'home.html'), '<p>home</p>');
  fs.writeFileSync(path.join(assets, 'cdn-images', 'a.png'), 'PNG');
  const { srv, port } = await servePages(pages, assets);
  try {
    assert.equal((await get(port, '/pages/home.html')).body, '<p>home</p>');
    assert.equal((await get(port, '/cdn-images/a.png')).body, 'PNG');
    for (const bad of [
      '/cdn-images/..%2fsecret.txt', '/cdn-images/..%2f..%2fsecret.txt', '/cdn-images/%2e%2e%2f%2e%2e%2fsecret.txt',
      '/cdn-images/../secret.txt', '/pages/..%2fsecret.txt', '/pages/%2e%2e/secret.txt', '/pages/%00',
    ]) {
      const r = await get(port, bad);
      assert.ok(r.status === 404 || r.status === 400, `${bad} -> ${r.status}`);
      assert.ok(!r.body.includes('SECRET'), `${bad} leaked`);
    }
  } finally {
    srv.close();
    fs.rmSync(root, { recursive: true, force: true });
  }
});
