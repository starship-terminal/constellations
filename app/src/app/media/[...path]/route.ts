import { createReadStream, promises as fs } from "node:fs";
import { Readable } from "node:stream";
import { mediaMime, resolveMedia } from "@/server/sources/files";
export const runtime = "nodejs";
export function parseByteRange(
  header: string,
  size: number,
): { start: number; end: number } | null {
  const match = /^bytes=(\d*)-(\d*)$/.exec(header);
  if (!match || (!match[1] && !match[2]) || size <= 0) return null;
  let start: number, end: number;
  if (!match[1]) {
    const suffix = Number(match[2]);
    if (!Number.isSafeInteger(suffix) || suffix <= 0) return null;
    start = Math.max(0, size - suffix);
    end = size - 1;
  } else {
    start = Number(match[1]);
    end = match[2] ? Number(match[2]) : size - 1;
  }
  if (
    !Number.isSafeInteger(start) ||
    !Number.isSafeInteger(end) ||
    start >= size ||
    start < 0 ||
    end < start
  )
    return null;
  return { start, end: Math.min(end, size - 1) };
}
async function serve(
  request: Request,
  parts: string[],
  head: boolean,
): Promise<Response> {
  const file = await resolveMedia(parts);
  if (!file) return new Response("Not found", { status: 404 });
  const stat = await fs.stat(file),
    size = stat.size;
  const headers = new Headers({
    "Content-Type": mediaMime(file)!,
    "Accept-Ranges": "bytes",
    "Cache-Control": "private, max-age=3600",
    "X-Content-Type-Options": "nosniff",
    "Content-Security-Policy":
      "default-src 'none'; style-src 'unsafe-inline'; sandbox",
  });
  const rangeHeader = request.headers.get("range"),
    range = rangeHeader ? parseByteRange(rangeHeader, size) : null;
  if (rangeHeader && !range) {
    headers.set("Content-Range", `bytes */${size}`);
    return new Response(null, { status: 416, headers });
  }
  const start = range?.start ?? 0,
    end = range?.end ?? size - 1;
  headers.set("Content-Length", String(end - start + 1));
  if (range) headers.set("Content-Range", `bytes ${start}-${end}/${size}`);
  const body = head
    ? null
    : (Readable.toWeb(
        createReadStream(file, { start, end }),
      ) as ReadableStream<Uint8Array>);
  return new Response(body, { status: range ? 206 : 200, headers });
}
export async function GET(
  request: Request,
  context: { params: Promise<{ path: string[] }> },
) {
  return serve(request, (await context.params).path, false);
}
export async function HEAD(
  request: Request,
  context: { params: Promise<{ path: string[] }> },
) {
  return serve(request, (await context.params).path, true);
}
