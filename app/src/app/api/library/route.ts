import { getSourceStats, listLibrary } from "@/server/sources";
import type { LibraryQuery } from "@/contracts/library";
import { parsePagination } from "@/server/sources/pagination";
export const runtime = "nodejs";
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const source = params.get("source");
  if (source && source !== "systems" && source !== "refero")
    return Response.json({ error: "Unknown library source" }, { status: 400 });
  const page = parsePagination(params, { limit: 60, maxLimit: 200 });
  if (!page)
    return Response.json({ error: "Invalid pagination" }, { status: 400 });
  const { limit, offset } = page;
  const query: LibraryQuery = {
    query: params.get("q") || undefined,
    category: params.get("category") || undefined,
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
