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
export function notModifiedSince(header: string, mtimeMs: number): boolean {
  const since = Date.parse(header);
  return (
    Number.isFinite(since) &&
    Math.floor(mtimeMs / 1000) <= Math.floor(since / 1000)
  );
}
export function rangeValidatorMatches(
  header: string,
  mtimeMs: number,
): boolean {
  const since = Date.parse(header);
  return (
    Number.isFinite(since) &&
    Math.floor(since / 1000) === Math.floor(mtimeMs / 1000)
  );
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
    "Cache-Control": "private, max-age=86400",
    "Last-Modified": stat.mtime.toUTCString(),
    "X-Content-Type-Options": "nosniff",
    "Content-Security-Policy":
      "default-src 'none'; style-src 'unsafe-inline'; sandbox",
  });
  const since = request.headers.get("if-modified-since");
  if (since && notModifiedSince(since, stat.mtimeMs))
    return new Response(null, { status: 304, headers });
  const rangeHeader = request.headers.get("range"),
    ifRange = request.headers.get("if-range"),
    rangeAllowed = !ifRange || rangeValidatorMatches(ifRange, stat.mtimeMs),
    range =
      rangeHeader && rangeAllowed ? parseByteRange(rangeHeader, size) : null;
  if (rangeHeader && rangeAllowed && !range) {
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
