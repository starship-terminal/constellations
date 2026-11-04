import { readExport } from "@/server/sources";
import { isExportVariant } from "@/server/sources/style-exports";
export const runtime = "nodejs";
export async function GET(
  request: Request,
  context: { params: Promise<{ source: string; slug: string }> },
) {
  const { source, slug } = await context.params;
  const query = new URL(request.url).searchParams;
  const format = query.get("format") || "DESIGN.md";
  const variant = query.get("variant");
  if (variant !== null && !isExportVariant(variant))
    return Response.json({ error: "Invalid export variant" }, { status: 400 });
  const text = await readExport(
    `${source}:${slug}`,
    format,
    variant ?? undefined,
  );
  if (text === null)
    return Response.json(
      {
        error:
          source === "refero" && variant
            ? "Captured source for this export variant is not available."
            : "Export not available",
      },
      { status: 404 },
    );
  const mime = format.endsWith(".json")
    ? "application/json"
    : format.endsWith(".css")
      ? "text/css"
      : "text/markdown";
  return new Response(text, {
    headers: {
      "Content-Type": `${mime}; charset=utf-8`,
      "Content-Disposition": `attachment; filename="${slug}-${format}"`,
      "X-Content-Type-Options": "nosniff",
    },
  });
}
