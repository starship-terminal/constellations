// The refero index: loads the third-party styles snapshot and hands it to
// the client grid for searching and filtering.
import { Suspense } from "react";
import { loadReferoIndex } from "@/lib/refero";
import type { ReferoIndex as ReferoIndexData } from "@/lib/refero";
import { NotBuilt, isNotBuilt } from "@/components/NotBuilt";
import { ReferoIndex } from "@/components/ReferoIndex";
import "./refero.css";

export const dynamic = "force-dynamic";
export const metadata = { title: "Refero" };

export default async function ReferoPage() {
  let index: ReferoIndexData | null = null;
  try {
    index = await loadReferoIndex();
  } catch (e) {
    if (!isNotBuilt(e)) throw e;
  }
  if (!index) return <NotBuilt what="The refero index" />;
  return (
    <Suspense>
      <ReferoIndex index={index} />
    </Suspense>
  );
}
