import { loadData } from "@/lib/catalog";
import type { GalleryData } from "@/lib/catalog";
import { NotBuilt, isNotBuilt } from "@/components/NotBuilt";
import { GalleryIndex } from "@/components/GalleryIndex";
import { Suspense } from "react";

// Read web/data at request time, like the other listings: a static render
// would bake in whatever the build saw, or the empty state if it saw nothing.
export const dynamic = "force-dynamic";
export const metadata = { title: "Gallery" };

export default async function GalleryPage() {
  let data: GalleryData | null = null;
  try {
    data = await loadData();
  } catch (e) {
    if (!isNotBuilt(e)) throw e;
  }
  if (!data) return <NotBuilt />;
  return (
    <Suspense>
      <GalleryIndex data={data} />
    </Suspense>
  );
}
