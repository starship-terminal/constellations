import { taxonomyGroups, taxonomySnapshots } from "@/contracts/taxonomy";
export function GET() {
  return Response.json({
    version: 1,
    snapshots: taxonomySnapshots,
    groups: taxonomyGroups,
  });
}
