// Streams repo files the pages reference: /media/systems/..., /media/data/...
// (generated under web/data/), /media/docs/..., /media/refero-media/<kind>/<file>
// (local mirror), and the other REPO_PATHS roots. Bounded by the same rules as
// catalog.py's repo_file and refero_media.media_file. Videos get single-range
// 206 support.
import { createReadStream } from "node:fs";
import { promises as fs } from "node:fs";
import { fileExists, mimeOf, referoMediaFile, repoFile } from "@/lib/repo";
import { Readable } from "node:stream";

type Params = { params: Promise<{ path: string[] }> };

function resolve(parts: string[]): string | null {
  const urlPath = "/" + parts.join("/");
  if (urlPath.startsWith("/refero-media/")) {
    const t = referoMediaFile(urlPath);
    if (t) return t;
    return null;
  }
  // data/..., docs/... and the REPO_PATHS roots all go through repoFile's
  // allow-list and EXTRA_PATHS map.
  return repoFile(urlPath);
}

export async function GET(req: Request, { params }: Params) {
  const { path: parts } = await params;
  const target = resolve(parts);
  if (!target || !(await fileExists(target))) return new Response("not found", { status: 404 });

  const stat = await fs.stat(target);
  const mime = mimeOf(target);
  const range = req.headers.get("range");
  const headers: Record<string, string> = {
    "content-type": mime,
    "cache-control": "public, max-age=60",
    "accept-ranges": "bytes",
  };

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
