import { readPackageGuide } from "@/server/sources/files";
export const runtime = "nodejs";
export async function GET(
  _request: Request,
  context: { params: Promise<{ slug: string; path: string[] }> },
) {
  const { slug, path } = await context.params;
  const result = await readPackageGuide(`systems:${slug}`, path.join("/"));
  if (!result) return new Response("Not found", { status: 404 });
  return new Response(Buffer.from(result.body), {
    headers: {
      "Content-Type": result.mime,
      "X-Content-Type-Options": "nosniff",
      "Cache-Control": "private, max-age=300",
      "Content-Security-Policy":
        "default-src 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'unsafe-inline'; font-src 'self'; connect-src 'none'; form-action 'none'; base-uri 'self'; sandbox allow-scripts",
    },
  });
}
