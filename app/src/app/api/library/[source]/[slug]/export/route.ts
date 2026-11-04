import { readExport } from "@/server/sources";
export const runtime = "nodejs";
export async function GET(
  request: Request,
  context: { params: Promise<{ source: string; slug: string }> },
) {
  const { source, slug } = await context.params;
  const format = new URL(request.url).searchParams.get("format") || "DESIGN.md";
  const text = await readExport(`${source}:${slug}`, format);
  if (text === null)
    return Response.json({ error: "Export not available" }, { status: 404 });
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
