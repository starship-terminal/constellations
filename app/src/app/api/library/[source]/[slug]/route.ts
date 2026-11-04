import { getReference } from "@/server/sources";
export const runtime = "nodejs";
export async function GET(
  _request: Request,
  context: { params: Promise<{ source: string; slug: string }> },
) {
  const { source, slug } = await context.params;
  const detail = await getReference(`${source}:${slug}`);
  return detail
    ? Response.json(detail)
    : Response.json({ error: "Reference not found" }, { status: 404 });
}
