import {
  listScreens,
  validScreenId,
  validScreenTermId,
  UnknownScreenTermError,
} from "@/server/sources/screens";
import { parseReferenceId } from "@/server/sources";
import type { ScreenQuery } from "@/contracts/screens";
export const runtime = "nodejs";
export async function GET(request: Request) {
  const params = new URL(request.url).searchParams;
  const pagination = (name: string, fallback: number, max: number) => {
    const raw = params.get(name);
    if (raw === null) return fallback;
    const value = Number(raw);
    return Number.isSafeInteger(value) && value >= 0
      ? Math.min(max, value)
      : null;
  };
  const offset = pagination("offset", 0, Number.MAX_SAFE_INTEGER);
  const limit = pagination("limit", 60, 200);
  if (offset === null || limit === null)
    return Response.json({ error: "Invalid pagination" }, { status: 400 });
  const kind = params.get("kind"),
    sort = params.get("sort") || params.get("order"),
    scope = params.get("scope"),
    mode = params.get("mode"),
    screenId = params.get("screenId"),
    referenceIds = [...new Set(params.getAll("referenceId").filter(Boolean))],
    termIds = [...new Set(params.getAll("term"))];
  if (screenId && !validScreenId(screenId))
    return Response.json(
      { error: "Invalid capture identity" },
      { status: 400 },
    );
  if (scope && scope !== "all" && scope !== "media")
    return Response.json(
      { error: "Unknown capture search scope" },
      { status: 400 },
    );
  if (kind && kind !== "screenshot" && kind !== "crop")
    return Response.json({ error: "Unknown capture kind" }, { status: 400 });
  if (sort && sort !== "recent" && sort !== "name")
    return Response.json({ error: "Unknown capture order" }, { status: 400 });
  if (mode && mode !== "screens" && mode !== "flows")
    return Response.json({ error: "Unknown capture mode" }, { status: 400 });
  if (referenceIds.some((id) => parseReferenceId(id)?.source !== "systems"))
    return Response.json(
      { error: "Unknown captured package" },
      { status: 400 },
    );
  if (termIds.some((id) => !validScreenTermId(id)))
    return Response.json(
      { error: "Invalid capture filter term" },
      { status: 400 },
    );
  const query: ScreenQuery = {
    query: params.get("q") || undefined,
    scope: scope === "media" ? "media" : "all",
    platform: params.get("platform") || undefined,
    category: params.get("category") || undefined,
    tag: params.get("tag") || undefined,
    theme: params.get("theme") || undefined,
    group: params.get("group") || undefined,
    referenceIds,
    termIds,
    mode: mode === "flows" ? "flows" : "screens",
    screenId: screenId || undefined,
    kind:
      kind === "crop"
        ? "crop"
        : kind === "screenshot"
          ? "screenshot"
          : undefined,
    sort: sort === "name" ? "name" : "recent",
    offset,
    limit,
  };
  try {
    return Response.json(await listScreens(query));
  } catch (error) {
    if (error instanceof UnknownScreenTermError)
      return Response.json({ error: error.message }, { status: 400 });
    throw error;
  }
}
