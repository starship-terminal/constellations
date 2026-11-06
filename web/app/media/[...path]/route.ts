// Streams repo files the pages reference: /media/systems/..., /media/data/...
// (generated under web/data/), /media/docs/..., /media/refero-media/<kind>/<file>
// (local mirror), and the other REPO_PATHS roots. Bounded by the same rules as
// catalog.py's repo_file and refero_media.media_file, plus: symlinks are
// resolved before the containment check, gitignored files are refused, and
// every response is sandboxed so a served HTML or SVG file (a package's
// style-guide.html) runs in an opaque origin and cannot read this app's
// storage, where Settings keeps the user's provider key. Videos get
// single-range 206 support.
import { createReadStream } from "node:fs";
import { promises as fs } from "node:fs";
import path from "node:path";
import { isGitIgnored, mediaRoot, mimeOf, realInside, referoMediaFile, repoFile, repoRoots, ROOT } from "@/lib/repo";
import { Readable } from "node:stream";

type Params = { params: Promise<{ path: string[] }> };

// A package's style guide loads its proprietary fonts from systems/<slug>/fonts/,
// which is gitignored so they are never committed; serve only the font files.
// Font loads are CORS requests, and the sandboxed guide's origin is opaque
// ("null"), so these responses (and only these) allow that origin.
const FONT_FILE = /^systems\/[a-z0-9][a-z0-9-]*\/fonts\/[^/]+\.(woff2?|ttf|otf)$/i;

async function resolve(parts: string[]): Promise<string | null> {
  const urlPath = "/" + parts.join("/");
  if (urlPath.startsWith("/refero-media/")) {
    const t = referoMediaFile(urlPath);
    return t ? realInside(t, mediaRoot()) : null;
  }
  // data/..., docs/... and the REPO_PATHS roots all go through repoFile's
  // allow-list and EXTRA_PATHS map.
  const target = repoFile(urlPath);
  if (!target) return null;
  const roots = repoRoots();
  const root = roots.find((r) => target === r || target.startsWith(r + path.sep));
  const real = root ? await realInside(target, root) : null;
  if (!real) return null;
  // web/data/ is generated, so gitignored by design, and always served.
  if (root === path.resolve(ROOT, "web/data")) return real;
  const rel = path.relative(await fs.realpath(ROOT), real).split(path.sep).join("/");
  if (FONT_FILE.test(rel)) return real;
  return (await isGitIgnored(real)) ? null : real;
}

export async function GET(req: Request, { params }: Params) {
  const { path: parts } = await params;
  let target: string | null;
  try {
    target = await resolve(parts);
  } catch (e) {
    if (e instanceof URIError) return new Response("bad path", { status: 400 });
    throw e;
  }
  const stat = target ? await fs.stat(target).catch(() => null) : null;
  if (!target || !stat?.isFile()) return new Response("not found", { status: 404 });

  const mime = mimeOf(target);
  const range = req.headers.get("range");
  const headers: Record<string, string> = {
    "content-type": mime,
    "cache-control": "private, max-age=60",
    "accept-ranges": "bytes",
    "x-content-type-options": "nosniff",
    "content-security-policy": "sandbox allow-scripts",
  };

  if (FONT_FILE.test(path.relative(await fs.realpath(ROOT), target).split(path.sep).join("/")))
    headers["access-control-allow-origin"] = "null";

  if (range) {
    const m = /^bytes=(\d*)-(\d*)$/.exec(range.trim());
    if (m && (m[1] || m[2])) {
      let start = m[1] ? parseInt(m[1], 10) : Math.max(0, stat.size - parseInt(m[2], 10));
      let end = m[1] ? (m[2] ? Math.min(parseInt(m[2], 10), stat.size - 1) : stat.size - 1) : stat.size - 1;
      if (start <= end && start < stat.size) {
        headers["content-range"] = `bytes ${start}-${end}/${stat.size}`;
        headers["content-length"] = String(end - start + 1);
        const stream = Readable.toWeb(createReadStream(target, { start, end })) as ReadableStream;
        return new Response(stream, { status: 206, headers });
      }
    }
    headers["content-range"] = `bytes */${stat.size}`;
    return new Response(null, { status: 416, headers });
  }

  headers["content-length"] = String(stat.size);
  const stream = Readable.toWeb(createReadStream(target)) as ReadableStream;
  return new Response(stream, { headers });
}
