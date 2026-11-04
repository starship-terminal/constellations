import { getSourceStats, listLibrary } from "@/server/sources";
import type { LibraryQuery } from "@/contracts/library";
export const runtime = "nodejs";
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const source = params.get("source");
  if (source && source !== "systems" && source !== "refero")
    return Response.json({ error: "Unknown library source" }, { status: 400 });
  const pagination = (name: string, fallback: number, max: number) => {
    const raw = params.get(name);
    if (raw === null) return fallback;
    const value = Number(raw);
    return Number.isInteger(value) && value >= 0 ? Math.min(max, value) : null;
  };
  const limit = pagination("limit", 60, 200),
    offset = pagination("offset", 0, Number.MAX_SAFE_INTEGER);
  if (limit === null || offset === null)
    return Response.json({ error: "Invalid pagination" }, { status: 400 });
  const query: LibraryQuery = {
    query: params.get("q") || undefined,
    source: source === "systems" || source === "refero" ? source : undefined,
    platform: params.get("platform") || undefined,
    theme: params.get("theme") || undefined,
  };
  const [all, stats] = await Promise.all([
    listLibrary(query),
    getSourceStats(),
  ]);
  return Response.json({
    items: all.slice(offset, offset + limit),
    total: all.length,
    stats,
  });
}
