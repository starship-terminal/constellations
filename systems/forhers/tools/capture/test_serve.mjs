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
  fs.mkdirSync(path.join(assets, 'www.forhers.com', 'css'), { recursive: true });
  fs.mkdirSync(path.join(assets, 'cloudinary.forhims.com', 'image'), { recursive: true });
  fs.mkdirSync(pages, { recursive: true });
  fs.writeFileSync(path.join(root, 'secret.txt'), 'SECRET');
  fs.writeFileSync(path.join(assets, 'secret.txt'), 'SECRET');
  fs.writeFileSync(path.join(pages, 'home.html'), '<p>home</p>');
  fs.writeFileSync(path.join(assets, 'www.forhers.com', 'css', 'a.png'), 'PNG');
  fs.writeFileSync(path.join(assets, 'cloudinary.forhims.com', 'image', 'a.png'), 'CDN');
  const { srv, port } = await servePages(pages, assets);
  try {
    assert.equal((await get(port, '/pages/home.html')).body, '<p>home</p>');
    assert.equal((await get(port, '/css/a.png')).body, 'PNG');
    assert.equal((await get(port, '/asset/cloudinary.forhims.com/image/a.png')).body, 'CDN');
    for (const bad of [
      '/css/..%2fsecret.txt', '/css/..%2f..%2fsecret.txt', '/css/%2e%2e%2f%2e%2e%2fsecret.txt',
      '/css/../secret.txt', '/pages/..%2fsecret.txt', '/pages/%2e%2e/secret.txt', '/pages/%00',
      '/asset/%2e%2e/secret.txt', '/asset/..%2fsecret.txt', '/asset/%2e%2e/%2e%2e/secret.txt',
      '/asset/evil.example/secret.txt',
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
