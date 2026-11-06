import {
  listPackageDocuments,
  readPackageDocument,
} from "@/server/sources/files";
export const runtime = "nodejs";
export async function GET(
  request: Request,
  context: { params: Promise<{ slug: string }> },
) {
  const { slug } = await context.params;
  const relative = new URL(request.url).searchParams.get("path");
  if (relative === null)
    return Response.json({
      documents: await listPackageDocuments(`systems:${slug}`),
    });
  const document = await readPackageDocument(`systems:${slug}`, relative);
  return document
    ? Response.json(document)
    : Response.json({ error: "Package document not found" }, { status: 404 });
}
