import { loadData } from "@/lib/catalog";
import { GalleryIndex } from "@/components/GalleryIndex";
import { Suspense } from "react";

export const metadata = { title: "Gallery" };

export default async function GalleryPage() {
  const data = await loadData();
  return (
    <Suspense>
      <GalleryIndex data={data} />
    </Suspense>
  );
}
