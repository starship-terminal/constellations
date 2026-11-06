// The refero index: loads the third-party styles snapshot and hands it to
// the client grid for searching and filtering.
import { Suspense } from "react";
import { loadReferoIndex } from "@/lib/refero";
import { ReferoIndex } from "@/components/ReferoIndex";
import "./refero.css";

export const dynamic = "force-dynamic";
export const metadata = { title: "Refero" };

export default async function ReferoPage() {
  const index = await loadReferoIndex();
  return (
    <Suspense>
      <ReferoIndex index={index} />
    </Suspense>
  );
}
