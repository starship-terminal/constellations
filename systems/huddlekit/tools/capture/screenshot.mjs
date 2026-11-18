// Shared by the kit's Playwright routes. Copy this with the capture directory.
// Dimension checks do not prove popup contents or a DOM-to-image crop mapping.
import fs from 'node:fs';
import path from 'node:path';

export function pngDimensions(bytes) {
  if (bytes.length < 33 || !bytes.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10])) || bytes.readUInt32BE(8) !== 13 ||
      bytes.toString('ascii', 12, 16) !== 'IHDR') throw new Error('Screenshot is not a PNG with an IHDR header');
  const width = bytes.readUInt32BE(16), height = bytes.readUInt32BE(20);
  if (!width || !height) throw new Error('Screenshot PNG has an empty dimension');
  return { width, height };
}

export async function screenshotWithMetadata(page, options, requested = {}) {
  if (typeof options.path !== 'string' || options.type && options.type !== 'png' || !options.path.endsWith('.png')) {
    throw new Error('screenshotWithMetadata requires a .png path and PNG output');
  }
  fs.mkdirSync(path.dirname(options.path), { recursive: true });
  const capturedAt = new Date().toISOString();
  const mode = options.clip ? 'clip' : options.fullPage ? 'fullPage' : 'viewport';
  const metadata = {
    schemaVersion: 1,
    capturedAt,
    screenshot: path.basename(options.path),
    // Never read page.url(): it can contain a signed URL or an account ID.
    sanitizedSourceUrl: requested.sanitizedSourceUrl ?? null,
    requested: { viewport: requested.viewport ?? null, deviceScaleFactor: requested.deviceScaleFactor ?? null },
    configuredViewport: null,
    actual: null,
    capture: { mode, scale: options.scale || 'device', clip: options.clip || null,
      ...(requested.capturedHeight ? { capturedHeight: requested.capturedHeight } : {}),
      ...(requested.partCount ? { partCount: requested.partCount, partIndex: requested.partIndex } : {}) },
    png: null,
    dimensionCheck: { status: 'pending', expected: null, basis: null },
    visualReview: { status: 'pending', note: 'Inspect the final image for complete, settled contents; dimensions alone cannot accept it.' },
    cropCoordinates: { status: 'unverified', note: 'Do not derive crop or masking boxes from requested size or assume DOM rectangles align with this PNG.' },
  };
  // Invalidate a previous same-path pass before any browser call can fail.
  fs.writeFileSync(`${options.path}.capture.json`, JSON.stringify(metadata, null, 2) + '\n');
  try {
    const configuredViewport = page.viewportSize();
    const actual = await page.evaluate(() => {
      const root = document.documentElement, body = document.body, visual = window.visualViewport;
      return {
        innerWidth, innerHeight, devicePixelRatio,
        theme: {
          classes: [...root.classList].filter(name => name === 'light' || name === 'dark'),
          attributes: Object.fromEntries(['data-theme', 'data-mode', 'data-color-mode'].flatMap(name => {
            const value = root.getAttribute(name);
            return ['light', 'dark', 'system', 'auto'].includes(value) ? [[name, value]] : [];
          })),
          colorScheme: getComputedStyle(root).colorScheme,
        },
        visualViewport: visual ? { width: visual.width, height: visual.height, scale: visual.scale,
          offsetLeft: visual.offsetLeft, offsetTop: visual.offsetTop, pageLeft: visual.pageLeft, pageTop: visual.pageTop } : null,
        documentSize: {
          width: Math.max(root.scrollWidth, root.clientWidth, body?.scrollWidth || 0),
          height: Math.max(root.scrollHeight, root.clientHeight, body?.scrollHeight || 0),
        },
        scroll: { x: scrollX, y: scrollY },
      };
    });
    const region = options.clip || (options.fullPage ? actual.documentSize : configuredViewport);
    // viewportSize can be null for an attached live Electron window. Its current
    // inner viewport is the available dimensional basis, not a requested size.
    const cssSize = region || { width: actual.innerWidth, height: actual.innerHeight };
    const scale = options.scale === 'css' ? 1 : actual.devicePixelRatio;
    const expected = { width: Math.round(cssSize.width * scale), height: Math.round(cssSize.height * scale) };
    metadata.configuredViewport = configuredViewport;
    metadata.actual = actual;
    metadata.dimensionCheck.expected = expected;
    metadata.dimensionCheck.basis = mode === 'viewport' ? configuredViewport ? 'configuredViewport' : 'actualInnerViewport' : mode;
    metadata.png = pngDimensions(await page.screenshot({ ...options, type: 'png' }));
    // A fractional CSS edge can round in either direction in the browser.
    const matches = Math.abs(metadata.png.width - expected.width) <= 1 && Math.abs(metadata.png.height - expected.height) <= 1;
    metadata.dimensionCheck.status = matches ? 'pass' : 'fail';
    if (!matches) throw new Error(`Screenshot dimension mismatch: PNG ${metadata.png.width}x${metadata.png.height}, expected ${expected.width}x${expected.height}`);
    return metadata;
  } catch (error) {
    metadata.dimensionCheck.status = 'fail';
    metadata.dimensionCheck.error = error.message;
    throw error;
  } finally {
    fs.writeFileSync(`${options.path}.capture.json`, JSON.stringify(metadata, null, 2) + '\n');
  }
}
