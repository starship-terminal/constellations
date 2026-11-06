import { getStore } from "@/server/db";

export async function GET() {
  const snapshots = await (await getStore()).listTaxonomySnapshots();
  return Response.json({
    version: 1,
    snapshots,
    groups: snapshots.flatMap((snapshot) => snapshot.groups),
  });
}
